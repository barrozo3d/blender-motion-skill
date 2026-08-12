# Blender Motion

A Claude Code skill: an expert consultant for **Blender** — motion design, geometry nodes, simulation, materials/shaders, lighting/compositing, and ad/brand video production — that also builds its own knowledge base by ingesting tutorials, and can optionally drive a real, running Blender session over MCP.

## What it does

Give it a reference image, video frame, or render and it deconstructs the geometry, materials, lighting, motion, and simulation type, then either hands back a phased step-by-step tutorial or — if the Blender MCP addon is connected — writes and executes the Python/geometry-node scripts directly in your open Blender scene, phase by phase, with screenshot verification. It can also just answer Blender questions directly. Its library currently holds 283 ingested tutorials spanning geometry nodes, simulation, materials, lighting, compositing, and motion-design/ad-video technique.

## Quick start

```powershell
git clone https://github.com/barrozo3d/blender-motion-skill.git "$HOME\.claude\skills\blender-motion"
cd "$HOME\.claude\skills\blender-motion"
.\setup.ps1
```

Then just ask Claude Code a question — it reads `SKILL.md` automatically. Full setup and troubleshooting details live in `SETUP.md`.

## How it works

**Consulting.** Every reference or question is checked against `tutorials/INDEX.md` (the ingested-tutorial library, searched by tag/keyword) plus the technique library in `references/*.md`: `visual-deconstruction.md` (how to read any render), `lighting-composition.md`, `geometry-nodes-library.md` (~50 core GeoNodes techniques), `simulation-catalog.md`, `materials-shaders.md`, `motion-design-patterns.md`, `ad-video-patterns.md`, `render-pipeline.md`, `blender-versions.md`, and `albin-merle-techniques.md` for that specific artist's style. See `SKILL.md` for the full reference-file map and tutorial output format.

**Growing the library.** Say "ingest this tutorial: [URL]" and a three-step pipeline runs:
1. `ingest.py` — pulls a YouTube transcript (Whisper, with per-sentence timestamps) or article text, no video download, no API calls.
2. `select_frames.py` — Claude reads the timestamped transcript, picks 4-8 moments that actually show a technique, and this script captures just those frames.
3. Claude reads the captured frames and the transcript, writes structured notes (technique, steps, nodes/settings, tags), cross-links related tutorials, and commits everything to this repo.

`validate.py` is a post-ingest integrity checker (no `[PENDING]` leftovers, no broken INDEX cross-references, transcripts long enough to be real) — run `python validate.py` after a batch of ingests.

**Live connection (optional).** Mode 2 connects to a real, running Blender scene via the BlenderMCP addon (`get_scene_info`, `execute_blender_code`, `get_viewport_screenshot`, `create_object`, `set_material`). Mode 0 validates the connection first and Mode 2 refuses to proceed with build work if it's not live — Blender must already be open with the addon connected (port 9876). Full connection-check and troubleshooting steps are in `SKILL.md` → "Blender MCP — Connection Validation".

## Repo structure

```
blender-motion/
├── SKILL.md              ← main skill instructions Claude reads (modes, workflows, key rules)
├── README.md              ← this file
├── SETUP.md               ← human + Claude setup guide
├── setup.ps1               ← Windows automated installer
├── ingest.py                ← Step 1: transcript/metadata collection (no video/frames)
├── select_frames.py         ← Step 2: content-aware frame capture (Claude picks timestamps)
├── batch_ingest.py           ← batch URL ingestion
├── validate.py                ← post-ingest integrity checker + cross-skill drift check
├── requirements.txt            ← pip dependency list
├── references/                  ← hand-written Blender technique library (11 files)
│   ├── visual-deconstruction.md
│   ├── lighting-composition.md
│   ├── geometry-nodes-library.md
│   ├── simulation-catalog.md
│   ├── materials-shaders.md
│   ├── motion-design-patterns.md
│   ├── ad-video-patterns.md
│   ├── render-pipeline.md
│   ├── blender-versions.md
│   ├── albin-merle-techniques.md
│   └── version-tracker.md
└── tutorials/
    ├── INDEX.md            ← searchable catalog of all 283 ingested tutorials
    └── *.md                ← one file per ingested tutorial
```

## Sibling skills

Same ingest/validate/setup architecture as this skill's siblings — `houdini-wand`, `unreal-sidekick`, `nuke-em-all`, and `paint-me-like-your-french-substances` — each covering a different DCC/VFX toolset. `validate.py`'s drift check compares shared pipeline internals across all five and warns (never fails) if a copy has drifted.

## Status

Public personal project, no warranty. **283 tutorials ingested** (count auto-updates on every `ingest.py` run — do not hand-edit this line).
