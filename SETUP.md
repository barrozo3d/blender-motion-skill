# blender-motion — Setup Guide

This file serves two purposes:
- **For you (human):** step-by-step instructions to get the skill running on a new machine
- **For Claude:** checklist to follow when the user says "set up this skill", "check if installed", or "new machine setup"

---

## For Claude: Setup Sync Rule

**Every structural change to the skill must update these three files in the same commit.**

A structural change is anything that would affect how someone installs or runs this skill on a fresh machine:
- New pip dependency added to `ingest.py` or any script → update `requirements.txt` + `setup.ps1` (pip install step) + `SETUP.md` (Step 3 or Troubleshooting)
- New system dependency (new tool required) → update `setup.ps1` + `SETUP.md`
- New environment variable required → update `setup.ps1` (Step 5) + `SETUP.md` (Step 4 or Troubleshooting)
- Claude API model changed → update `SETUP.md` (reference table if present)
- New CLI flag added to `ingest.py` → update `SETUP.md` (Ingest Pipeline Reference section)
- Directory or file renamed/added → update `SETUP.md` (Skill Structure section)
- Git repo URL changed → update `SETUP.md` (Step 2) + `setup.ps1` (clone URL comment)

**Commit + push format for structural changes:**
```
git add ingest.py requirements.txt setup.ps1 SETUP.md
git commit -m "feat/fix: <what changed> + sync setup pack"
git push
```

Never leave setup files out of sync with the actual skill state. The push is mandatory — the GitHub copy is what other machines clone, so a local-only commit is not enough.

---

## For Claude: New Machine Setup Protocol

When the user says any of: "set this up", "new machine", "is this installed", "check dependencies", "help me configure this skill" — follow this checklist in order. Run each check as a shell command, report results, and fix what's missing.

```
CHECKLIST:
1. python --version                          → need 3.10+
2. ffmpeg -version                           → need any version on PATH
3. python -c "import yt_dlp"                 → need installed
4. python -c "import whisper"                → need installed
5. python -c "import anthropic"              → need installed
6. python -c "import torch; print(torch.cuda.is_available())"  → True = GPU ready
7. echo $env:ANTHROPIC_API_KEY               → need sk-ant-... value
8. Test-Path ~\.claude\skills\blender-motion\SKILL.md  → need True
```

For anything missing:
- **ffmpeg missing** → `winget install ffmpeg`
- **pip packages missing** → `pip install yt-dlp openai-whisper anthropic`
- **torch CPU-only** → `pip install torch --force-reinstall --index-url https://download.pytorch.org/whl/cu128`
- **ANTHROPIC_API_KEY missing** → prompt user to get key from console.anthropic.com, then: `[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY","sk-ant-...","User")`
- **Skill not found** → `git clone https://github.com/barrozo3d/blender-motion-skill.git ~\.claude\skills\blender-motion`

After fixing, re-run the checklist and confirm all green before proceeding.

---

## System Requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 / macOS 12 / Ubuntu 20.04 | Windows 11 |
| Python | 3.10 | 3.11–3.12 |
| RAM | 8 GB | 16 GB+ |
| GPU | — (CPU works) | NVIDIA RTX (any) for fast Whisper |
| Disk | 5 GB free | 10 GB (Whisper models cache here) |
| Internet | Required for ingest | — |

---

## Step 1 — Install Claude Code

If Claude Code isn't installed yet:
- Download from: https://claude.ai/download
- Or install the VS Code extension: search "Claude" in Extensions

---

## Step 2 — Clone the Skill

Open PowerShell and run:

```powershell
git clone https://github.com/barrozo3d/blender-motion-skill.git "$HOME\.claude\skills\blender-motion"
```

> If you don't have git: `winget install git`

---

## Step 3 — Run the Setup Script

```powershell
cd "$HOME\.claude\skills\blender-motion"
.\setup.ps1
```

The script will:
- Check Python version
- Install `ffmpeg` via winget
- Install `yt-dlp`, `openai-whisper`, `anthropic` via pip
- Install PyTorch with CUDA support (if NVIDIA GPU detected)
- Prompt for your `ANTHROPIC_API_KEY` and save it to your user environment

> **Note:** The CUDA torch download is ~2.8 GB. It may take 10–30 minutes depending on your connection.

---

## Step 4 — Get Your Anthropic API Key

The `ingest.py` script calls the Claude API directly (for vision analysis and extraction). You need a key:

1. Go to https://console.anthropic.com/settings/keys
2. Create a new key
3. The setup script will ask for it — paste it when prompted

If you need to set it manually:
```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-YOUR-KEY", "User")
```

Then open a new terminal for it to take effect.

---

## Step 5 — Verify

```powershell
ffmpeg -version
python -c "import whisper, anthropic, yt_dlp; print('all OK')"
python -c "import torch; print('CUDA:', torch.cuda.is_available())"
```

Expected output:
```
ffmpeg version 8.x ...
all OK
CUDA: True    ← only if NVIDIA GPU present
```

---

## Step 6 — Test Ingest

Run a quick test without downloading the full video:
```powershell
cd "$HOME\.claude\skills\blender-motion"
python ingest.py "https://www.youtube.com/watch?v=WreZ_VKDn4M" --skip-video
```

`--skip-video` skips frame extraction so the test runs in ~2 minutes instead of 10+.

---

## YouTube Bot Detection (cookies.txt)

Chrome 127+ broke yt-dlp's automatic cookie extraction (`--cookies-from-browser` fails with DPAPI error). If you see `Sign in to confirm you're not a bot` errors, fix it once:

1. Install the **"Get cookies.txt LOCALLY"** extension in Chrome/Edge/Firefox
2. Go to **youtube.com** while logged in to your Google account
3. Click the extension icon → **Export** → save as **`cookies.txt`**
4. Place `cookies.txt` in `~/.claude/skills/blender-motion/` (same folder as `ingest.py`)
5. `ingest.py` detects it automatically — no other changes needed

> `cookies.txt` is in `.gitignore` and will never be committed to GitHub.

---

## Troubleshooting

**`ffmpeg: command not found` after install**
Open a new PowerShell window — PATH updates don't apply to the current session.

**`ModuleNotFoundError: No module named 'whisper'`**
```powershell
pip install openai-whisper
```

**`CUDA: False` when you have an NVIDIA GPU**
```powershell
pip install torch --force-reinstall --index-url https://download.pytorch.org/whl/cu128
```

**`ANTHROPIC_API_KEY not set` errors during ingest**
```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-YOUR-KEY"   # current session only
# OR to persist across sessions:
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-YOUR-KEY", "User")
```

**Git push fails (authentication)**
```powershell
git config --global credential.helper manager
```
Then re-run the push — Windows Credential Manager will prompt for GitHub login.

**Whisper model download on first run**
The first time Whisper runs it downloads the model (~150 MB for `base`). This is normal — subsequent runs use the cached model.

---

## Skill Structure (reference)

```
blender-motion/
├── SKILL.md              ← main skill instructions Claude reads
├── SETUP.md              ← this file
├── setup.ps1             ← Windows automated installer
├── ingest.py             ← enhanced tutorial ingestion pipeline
├── batch_ingest.py       ← batch URL ingestion
├── requirements.txt      ← pip dependency list
├── references/           ← technique library (Blender-specific knowledge)
│   ├── geometry-nodes-library.md
│   ├── materials-shaders.md
│   ├── lighting-composition.md
│   └── ...
└── tutorials/
    ├── INDEX.md          ← searchable catalog of all ingested tutorials
    └── *.md              ← one file per ingested tutorial
```

---

## Ingest Pipeline Reference

```
python ingest.py <url>                         full pipeline
python ingest.py <url> --skip-video            no frames (faster, no ffmpeg needed)
python ingest.py <url> --whisper-model small   better accuracy, slower
python ingest.py <url> --whisper-model medium  best accuracy, much slower
```

Pipeline stages:
1. yt-dlp metadata + chapter list
2. Whisper transcription (or yt-dlp captions fallback)
3. Transcript segmented by chapter
4. Low-quality video download → ffmpeg frame extraction at chapter timestamps
5. Claude vision analysis per frame (reads node graphs, settings, viewport)
6. Claude multi-pass extraction (core technique, steps, nodes, tags)
7. Auto cross-linking with existing tutorials (2+ shared tags)
8. Write `.md` + update `INDEX.md` + git push
