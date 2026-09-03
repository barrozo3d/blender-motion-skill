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
- New environment variable required → update `setup.ps1` + `SETUP.md` (add a step + Troubleshooting entry)
- New CLI flag added to `ingest.py` or `select_frames.py` → update `SETUP.md` (Ingest Pipeline Reference section)
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
5. python -c "import torch; print(torch.cuda.is_available())"  → True = GPU ready
6. Test-Path ~\.claude\skills\blender-motion\SKILL.md  → need True
```

For anything missing:
- **ffmpeg missing** → `winget install ffmpeg`
- **pip packages missing** → `pip install yt-dlp openai-whisper`
- **torch CPU-only** → `pip install torch --force-reinstall --index-url https://download.pytorch.org/whl/cu128`
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
- Install `yt-dlp`, `openai-whisper` via pip
- Install PyTorch with CUDA support (if NVIDIA GPU detected)

> **Note:** The CUDA torch download is ~2.8 GB. It may take 10–30 minutes depending on your connection.

---

## Step 4 — Verify

```powershell
ffmpeg -version
python -c "import whisper, yt_dlp; print('all OK')"
python -c "import torch; print('CUDA:', torch.cuda.is_available())"
```

Expected output:
```
ffmpeg version 8.x ...
all OK
CUDA: True    ← only if NVIDIA GPU present
```

---

## Step 5 — Test Ingest

Run a quick test without downloading the full video:
```powershell
cd "$HOME\.claude\skills\blender-motion"
python ingest.py "https://www.youtube.com/watch?v=WreZ_VKDn4M" --skip-video
```

Step 1 alone (`ingest.py`, with or without `--skip-video`) never downloads video anymore — it only collects transcript + metadata, so this test runs in ~2 minutes either way. `--skip-video` instead permanently marks the tutorial `frame_status: skipped` (use it for articles or text-only ingests where frame capture will never apply); without it, frames stay `pending-selection` until you run `select_frames.py`.

---

## YouTube Bot Detection (cookies.txt)

As of 2026-08, `ingest.py` automatically passes `--extractor-args youtube:player_client=android` on every call that doesn't have a `cookies.txt` present, since YouTube's default `web_safari` client started throwing HTTP 429 + `Sign in to confirm you're not a bot` on many (not all) videos. This needs no setup — it's built into `_ytdlp_cmd()` in `ingest.py`. The android client only exposes a single combined mp4 (no audio-only stream); `download_audio()` handles that fine since it re-encodes to mp3 either way.

If a video *still* fails under the android client (rare — seen mainly on age-restricted or region-locked videos), fall back to cookies. Chrome 127+ broke yt-dlp's automatic cookie extraction (`--cookies-from-browser` fails with DPAPI error), so this has to be manual:

1. Install the **"Get cookies.txt LOCALLY"** extension in Chrome/Edge/Firefox
2. Go to **youtube.com** while logged in to your Google account
3. Click the extension icon → **Export** → save as **`cookies.txt`**
4. Place `cookies.txt` in `~/.claude/skills/blender-motion/` (same folder as `ingest.py`)
5. `ingest.py` detects it automatically and switches to cookie auth (dropping the android-client arg) — no other changes needed

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

**Git push fails (authentication)**
```powershell
git config --global credential.helper manager
```
Then re-run the push — Windows Credential Manager will prompt for GitHub login.

**Whisper model download on first run**
The first time Whisper runs it downloads the model (~150 MB for `base`, ~461 MB for `small` — the default on CUDA machines). ingest.py prints a single "downloading weights (one-time)" notice instead of a progress bar. This is normal — subsequent runs use the cached model.

---

## Skill Structure (reference)

```
blender-motion/
├── SKILL.md              ← main skill instructions Claude reads
├── README.md              ← human-facing overview
├── CODE_OF_CONDUCT.md     ← purpose/ethics statement
├── SETUP.md              ← this file
├── setup.ps1             ← Windows automated installer
├── ingest.py             ← Step 1: transcript/metadata collection (no video/frames)
├── select_frames.py      ← Step 2: content-aware frame capture (Claude picks timestamps)
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

The pipeline is two scripts, run in sequence — frame capture is a deliberate,
content-aware step done by Claude Code, not something either script guesses at:

```
Step 1 — collect transcript only, no video/frames:
python ingest.py <url>
python ingest.py <url> --skip-video            article/text-only ingest, no frames ever
python ingest.py <url> --whisper-model medium  best accuracy, much slower
# Default model is auto-selected: "small" when a CUDA GPU is available, else "base".
# Pass --whisper-model explicitly to override either way.
python ingest.py <url> --force                 re-collect even if extraction_status: complete (overwrites Structured Notes)

Step 2 — after reading the timestamped transcript, capture the chosen moments:
python select_frames.py <slug> <ts1> <ts2> ...   seconds or mm:ss, e.g. 10 60 4:20 8:05
python select_frames.py <slug> ... --force       re-capture even if frame_status: complete
```

`ingest.py` refuses to overwrite a tutorial `.md` whose frontmatter already has `extraction_status: complete`, to protect hand-written Structured Notes from being wiped by an accidental re-ingest. Pass `--force` only when you intend to discard the existing extraction (e.g. recovering from a truncated/corrupt transcript) and will re-run the extraction pass afterward. `select_frames.py` has the same guard on `frame_status: complete`.

Pipeline stages:
1. yt-dlp metadata + chapter list
2. Whisper transcription (or yt-dlp captions fallback), per-sentence timestamps preserved even inside chapters
3. Transcript segmented by chapter
4. Write `tutorials/<slug>.md` (`frame_status: pending-selection`) + update `INDEX.md` + git push — **no video download, no frames yet**
5. Claude Code reads the timestamped transcript and picks 4-8 content-anchored moments (not blind percentages)
6. `select_frames.py <slug> <timestamps>` downloads the low-quality video, extracts exactly those frames to `tutorials/frames/<slug>/`, sets `frame_status: complete` — not committed yet
7. Claude Code vision-reads each captured frame (node graphs, settings, viewport) and writes the Structured Notes (core technique, steps, nodes, tags)
8. Auto cross-linking with existing tutorials (2+ shared tags)
9. Update `INDEX.md`, commit `.md` + `INDEX.md` together, git push

## Frame capture height (`INGEST_FRAME_HEIGHT`)

Frames are captured at **720p** in this skill (viewport/result-led content more often than parameter-pane-led), set by
`DEFAULT_FRAME_HEIGHT` at the top of `ingest.py`. The value is per-skill on
purpose: `download_video_low()` itself is drift-gated across all five skills, so
its source stays identical while only the constant changes.

Raise or lower it for a single run without editing anything:

```
# PowerShell
$env:INGEST_FRAME_HEIGHT = "1080"; python ingest.py <url>
# bash
INGEST_FRAME_HEIGHT=1080 python ingest.py <url>
```

Why it matters: frames are how a claim gets checked against what was actually on
screen, and text that cannot be read cannot settle anything. Frames below **480p**
count as blind-era and `reground_frames.py` treats them as needing re-capture.
Raise this when a tutorial is a UI-heavy screencast and lower it only if disk or
bandwidth genuinely bites — the cap exists for download cost, not quality.

> This variable existed for weeks before being documented here, and so defaulted
> to 720p everywhere by accident. Per the Setup Sync Rule at the top of this
> file, a new environment variable must be added here in the same change.

## Note: captured frames are local-only

`tutorials/frames/` is gitignored — frame images never sync to GitHub. On a fresh
clone, `frame_status: complete` in a tutorial's frontmatter refers to frames that
existed on the machine that ingested it; the durable knowledge is the extracted
Structured Notes, not the images. If you need the stills again on this machine,
re-capture them with:

```
python select_frames.py <slug> <ts1> <ts2> ... --force
```

(timestamps are listed in the tutorial file's "Captured Frames" section).
