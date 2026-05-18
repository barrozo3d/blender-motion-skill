# =============================================================================
# blender-motion skill — Setup Script (Windows)
# =============================================================================
# Run this once on any new machine to install all dependencies.
#
# Usage (from PowerShell):
#   cd ~\.claude\skills\blender-motion
#   .\setup.ps1
#
# What this does:
#   1. Checks Python (3.10+ required)
#   2. Installs ffmpeg via winget
#   3. Installs pip packages: yt-dlp, openai-whisper, anthropic
#   4. Installs CUDA-enabled PyTorch (if NVIDIA GPU detected), else CPU
#   5. Prompts for ANTHROPIC_API_KEY and saves it as a user env var
#   6. Verifies everything works
# =============================================================================

$ErrorActionPreference = "Stop"

function Write-Step  { param($msg) Write-Host "`n[$($args[0]+1)/6] $msg" -ForegroundColor Cyan }
function Write-OK    { param($msg) Write-Host "  OK  $msg" -ForegroundColor Green }
function Write-Warn  { param($msg) Write-Host "  WARN  $msg" -ForegroundColor Yellow }
function Write-Fail  { param($msg) Write-Host "  FAIL  $msg" -ForegroundColor Red }

Write-Host ""
Write-Host "======================================================" -ForegroundColor Magenta
Write-Host "  blender-motion skill — Setup" -ForegroundColor Magenta
Write-Host "======================================================" -ForegroundColor Magenta

# ── Step 1: Python ────────────────────────────────────────────────────────────
Write-Host "`n[1/6] Checking Python..." -ForegroundColor Cyan
try {
    $pyver = python --version 2>&1
    if ($pyver -match "Python (\d+)\.(\d+)") {
        $major = [int]$Matches[1]; $minor = [int]$Matches[2]
        if ($major -ge 3 -and $minor -ge 10) {
            Write-OK "Python $major.$minor found"
        } else {
            Write-Fail "Python $major.$minor is too old. Need 3.10+. Install from https://python.org"
            exit 1
        }
    }
} catch {
    Write-Fail "Python not found. Install from https://python.org (check 'Add to PATH')"
    exit 1
}

# ── Step 2: Deno (JS runtime required by yt-dlp for YouTube) ─────────────────
Write-Host "`n[2/7] Checking Deno..." -ForegroundColor Cyan
$denoPath = Get-Command deno -ErrorAction SilentlyContinue
if ($denoPath) {
    $dver = (deno --version 2>&1 | Select-Object -First 1)
    Write-OK "Deno already installed: $dver"
} else {
    Write-Host "  Installing Deno via winget..." -ForegroundColor Yellow
    try {
        winget install deno --accept-source-agreements --accept-package-agreements
        Write-OK "Deno installed. NOTE: open a new terminal for PATH to update."
    } catch {
        Write-Warn "winget install failed. Install manually: https://docs.deno.com/runtime/manual/getting_started/installation"
    }
}

# ── Step 3: ffmpeg ────────────────────────────────────────────────────────────
Write-Host "`n[3/7] Checking ffmpeg..." -ForegroundColor Cyan
$ffmpegPath = Get-Command ffmpeg -ErrorAction SilentlyContinue
if ($ffmpegPath) {
    $ffver = (ffmpeg -version 2>&1 | Select-Object -First 1)
    Write-OK "ffmpeg already installed: $ffver"
} else {
    Write-Host "  Installing ffmpeg via winget..." -ForegroundColor Yellow
    try {
        winget install ffmpeg --accept-source-agreements --accept-package-agreements
        Write-OK "ffmpeg installed. NOTE: open a new terminal for PATH to update."
    } catch {
        Write-Warn "winget install failed. Install manually: https://ffmpeg.org/download.html"
        Write-Warn "Then re-run this script."
    }
}

# ── Step 3: pip packages ──────────────────────────────────────────────────────
Write-Host "`n[4/7] Installing pip packages (yt-dlp, openai-whisper, anthropic)..." -ForegroundColor Cyan
pip install yt-dlp openai-whisper anthropic --quiet
if ($LASTEXITCODE -eq 0) {
    Write-OK "pip packages installed"
} else {
    Write-Fail "pip install failed. Check your internet connection and try again."
    exit 1
}

# ── Step 4: PyTorch (CUDA if NVIDIA, else CPU) ────────────────────────────────
Write-Host "`n[5/7] Installing PyTorch..." -ForegroundColor Cyan
$hasNvidia = Get-Command nvidia-smi -ErrorAction SilentlyContinue
if ($hasNvidia) {
    $cudaLine = (nvidia-smi 2>&1 | Select-String "CUDA Version")
    Write-Host "  NVIDIA GPU detected: $cudaLine" -ForegroundColor Yellow
    Write-Host "  Installing CUDA 12.8 build (best for RTX 30xx/40xx/50xx)..." -ForegroundColor Yellow
    pip install torch --force-reinstall --index-url https://download.pytorch.org/whl/cu128 --quiet
    if ($LASTEXITCODE -eq 0) {
        Write-OK "PyTorch (CUDA 12.8) installed — Whisper will use your GPU"
    } else {
        Write-Warn "CUDA torch install failed. Falling back to CPU build..."
        pip install torch --quiet
    }
} else {
    Write-Host "  No NVIDIA GPU detected — installing CPU build..." -ForegroundColor Yellow
    pip install torch --quiet
    Write-OK "PyTorch (CPU) installed — Whisper will run on CPU (slower)"
}

# ── Step 5: ANTHROPIC_API_KEY ─────────────────────────────────────────────────
Write-Host "`n[6/7] ANTHROPIC_API_KEY setup..." -ForegroundColor Cyan
$existingKey = [Environment]::GetEnvironmentVariable("ANTHROPIC_API_KEY", "User")
if ($existingKey -and $existingKey.StartsWith("sk-ant-")) {
    Write-OK "ANTHROPIC_API_KEY already set (user environment)"
} else {
    Write-Host "  The ingest pipeline calls the Claude API directly and needs your Anthropic API key." -ForegroundColor Yellow
    Write-Host "  Get it from: https://console.anthropic.com/settings/keys" -ForegroundColor Yellow
    Write-Host ""
    $key = Read-Host "  Paste your ANTHROPIC_API_KEY (starts with sk-ant-)"
    if ($key -and $key.StartsWith("sk-ant-")) {
        [Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", $key, "User")
        $env:ANTHROPIC_API_KEY = $key
        Write-OK "ANTHROPIC_API_KEY saved to user environment"
    } else {
        Write-Warn "Key not saved (invalid format). Set it manually:"
        Write-Warn '  [Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY","sk-ant-...","User")'
    }
}

# ── Step 6: Verify ────────────────────────────────────────────────────────────
Write-Host "`n[7/7] Verifying installation..." -ForegroundColor Cyan
$allOK = $true

# yt-dlp
try {
    $ytver = python -c "import yt_dlp; print(yt_dlp.version.__version__)" 2>&1
    Write-OK "yt-dlp $ytver"
} catch { Write-Fail "yt-dlp import failed"; $allOK = $false }

# whisper
try {
    $wver = python -c "import whisper; print(whisper.__version__)" 2>&1
    Write-OK "openai-whisper $wver"
} catch { Write-Fail "whisper import failed"; $allOK = $false }

# anthropic
try {
    $aver = python -c "import anthropic; print(anthropic.__version__)" 2>&1
    Write-OK "anthropic $aver"
} catch { Write-Fail "anthropic import failed"; $allOK = $false }

# torch + CUDA
try {
    $torchInfo = python -c "import torch; print(torch.__version__, '| CUDA:', torch.cuda.is_available())" 2>&1
    Write-OK "torch $torchInfo"
} catch { Write-Warn "torch import failed (Whisper will still work without GPU)" }

# ffmpeg
if (Get-Command ffmpeg -ErrorAction SilentlyContinue) {
    Write-OK "ffmpeg on PATH"
} else {
    Write-Warn "ffmpeg not on PATH yet — open a new terminal and re-run 'ffmpeg -version' to confirm"
}

# deno
if (Get-Command deno -ErrorAction SilentlyContinue) {
    Write-OK "deno on PATH"
} else {
    Write-Warn "deno not on PATH yet — open a new terminal and re-run 'deno --version' to confirm"
}

# API key
if ($env:ANTHROPIC_API_KEY -and $env:ANTHROPIC_API_KEY.StartsWith("sk-ant-")) {
    Write-OK "ANTHROPIC_API_KEY is set"
} else {
    Write-Warn "ANTHROPIC_API_KEY not set in current session — open new terminal to pick up env var"
}

Write-Host ""
if ($allOK) {
    Write-Host "======================================================" -ForegroundColor Green
    Write-Host "  All dependencies installed. Skill is ready." -ForegroundColor Green
    Write-Host "  Test with: python ingest.py <youtube-url> --skip-video" -ForegroundColor Green
    Write-Host "======================================================" -ForegroundColor Green
} else {
    Write-Host "======================================================" -ForegroundColor Yellow
    Write-Host "  Some steps failed — see FAIL messages above." -ForegroundColor Yellow
    Write-Host "  Fix them and re-run setup.ps1" -ForegroundColor Yellow
    Write-Host "======================================================" -ForegroundColor Yellow
}
Write-Host ""
