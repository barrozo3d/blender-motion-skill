# Blender Motion

An expert consultant skill for **Blender** — motion design, geometry nodes, simulation, materials/shaders, lighting/compositing, and ad/brand video production — that also builds its own knowledge base by ingesting tutorials, and can optionally drive a real, running Blender session over MCP.

## What it does

Give it a reference image, video frame, or render and it deconstructs the geometry, materials, lighting, motion, and simulation type, then either hands back a phased step-by-step tutorial or — if the Blender MCP addon is connected — writes and executes the Python/geometry-node scripts directly in your open Blender scene, phase by phase, with screenshot verification. It can also just answer Blender questions directly.

## Quick start

```powershell
git clone https://github.com/barrozo3d/blender-motion-skill.git "$HOME\.claude\skills\blender-motion"
cd "$HOME\.claude\skills\blender-motion"
.\setup.ps1
```

Then just ask Claude Code a question — it reads `SKILL.md` automatically. Full setup and troubleshooting details live in `SETUP.md`.

## The Ingest Pipeline, in full detail

This is the part of the skill you'd actually touch to extend it: give it a video, an article, or any source of technical knowledge and the skill will trigger the steps to extract, read, organize, cross-reference and push it.

```
ingest.py  ──►  select_frames.py  ──►  Claude Code (extraction)  ──►  validate.py
(Step 1:         (Step 2:                (Step 3:                    (integrity
 transcript)      frame capture)          structured notes)           check)
```

### `ingest.py` — Step 1: data collection (no API calls, no video download)

| Function | What it does |
|---|---|
| `slugify(text)` | Turns a title into a filesystem-safe slug (`tutorials/<slug>.md`) — lowercases, strips punctuation, collapses whitespace to hyphens, caps at 80 chars. |
| `_default_whisper_model()` | Picks the default Whisper model size: `small` when a CUDA GPU is available, `base` otherwise. |
| `_ytdlp_cmd()` | Builds the base yt-dlp command. Defaults to forcing the `android` player client to dodge YouTube's "Sign in to confirm you're not a bot" 429s; switches to `cookies.txt`-based auth (plus `--remote-components ejs:github`) automatically if that file exists in the skill directory. |
| `check_prerequisites()` | Verifies `yt-dlp` is importable (hard requirement, exits if missing); detects whether `ffmpeg` and `whisper` are available (soft — pipeline degrades gracefully without them). |
| `get_info(url)` | Runs `yt-dlp --dump-json` and parses the result: title, uploader, duration, chapters, video ID. |
| `WHISPER_VOCAB_HINT` | A domain-vocabulary string (Blender terms: geometry nodes, Cycles, EEVEE, Node Wrangler, Principled BSDF, etc.) fed to Whisper as an `initial_prompt` so it transcribes jargon correctly instead of mishearing it. |
| `_load_whisper_model(model_name)` | Loads (and caches) a Whisper model, suppressing the noisy first-download progress bar in favor of one clean notice. |
| `whisper_transcribe(audio_path, model_name)` | Runs Whisper transcription with the vocab hint applied. |
| `download_audio(url, tmp)` | Downloads and extracts audio as mp3 (one automatic retry on YouTube throttling failures). |
| `ytdlp_captions(url, tmp)` | Fallback path when Whisper isn't installed or transcription fails: pulls YouTube's own auto-captions and strips VTT markup down to plain text (no per-sentence timestamps in this path). |
| `segment_by_chapters(transcript, chapters)` | Buckets the transcript into per-chapter sections (or one "Full Content" section if the video has no chapters), preserving a per-sentence `(timestamp, text)` list per section — this is what lets Step 2 pick *content-anchored* frame moments instead of guessing blind percentages. |
| `download_video_low(url, tmp)` | Downloads the lowest-quality video stream available (reused by `select_frames.py` — frame pixels don't need to be high-res). |
| `extract_frames(video_path, timestamps, out_dir)` | Runs `ffmpeg -ss <t> -frames:v 1` per timestamp to grab exact stills. |
| `_STOP_WORDS` | A common-word set used to filter noise out of the hallucination check below. |
| `_detect_hallucination(text)` | ASR-hallucination guard: flags a chapter if one content word repeats ≥8 times in its last 50 words (a classic Whisper infinite-loop symptom). |
| `run_safeguards(ch_transcripts)` | Runs all Step-1 quality checks: per-chapter transcript emptiness/shortness, total-transcript-length thresholds (<500 chars = critical, <1200 = warning), and the hallucination check above. Returns `(warnings, critical)`. |
| `_print_safeguard_report(warnings, critical)` | Prints the safeguard findings to the console during a live ingest run. |
| `build_safeguard_section(...)` / `append_safeguard_note(...)` | Render safeguard findings as a `## Ingest Safeguard Report` markdown block and persist it *inside* the tutorial file — so a `needs-review` flag stays auditable later instead of only ever existing in a terminal that's since closed. Shared with `select_frames.py`, which appends its own frame-capture findings into the same section. |
| `build_raw_md(...)` | Assembles the actual `tutorials/<slug>.md` file: YAML frontmatter (title/source/url/author/tags/extraction_status/frame_status) + the chapter-by-chapter timestamped transcript + a `Structured Notes` skeleton full of `[PENDING EXTRACTION]` markers for Step 3 to fill in. |
| `update_index_pending(...)` | Appends (or refuses to duplicate) a pending stub entry in `tutorials/INDEX.md`. |
| `update_readme_tutorial_count()` | Recomputes the real on-disk tutorial count and rewrites this README's `**N tutorials ingested**` line — runs automatically at the end of every ingest so the number never goes stale. |
| `fetch_article(url)` | Non-YouTube path: fetches a plain HTML page, strips scripts/styles/tags, and extracts a title + up to 8000 chars of body text for text-only ingestion. |
| `find_duplicate_by_video_id(video_id, exclude_name)` | Dedup guard — searches existing tutorial files for the same 11-char YouTube video ID (catches re-ingests where the uploader renamed the video, which a slug/URL-only check would miss). |
| `main()` | Orchestrates all of the above: fetch metadata → transcribe → segment → run safeguards → write the `.md` file → update `INDEX.md` and `README.md` → `git add` + `commit` + `push`. Flags: `--whisper-model {tiny,base,small,medium,large}`, `--skip-video` (permanently marks `frame_status: skipped`, text-only), `--force` (overwrite even if `extraction_status: complete`). |

**Run it:** `python ingest.py "<url>"` from this skill's own directory.

### `batch_ingest.py` — queue multiple URLs through Step 1

A thin wrapper: edit the `URLS` list at the top of the file, then run `python batch_ingest.py` (`--skip-video` / `--whisper-model` pass through). It calls `ingest.py` once per URL as a subprocess, commits/pushes each one individually, and prints a success/failure summary at the end. It only runs Step 1 — after it finishes, Claude still needs to run Step 2 (`select_frames.py`) and Step 3 (extraction) per tutorial.

### `select_frames.py` — Step 2: content-aware frame capture

| Function | What it does |
|---|---|
| `parse_timestamp(raw)` | Accepts plain seconds (`"485"`) or `mm:ss` / `h:mm:ss` (`"8:05"`) — Claude picks these by hand after reading the timestamped transcript, not by blind percentage splits. |
| `read_frontmatter_field(content, key)` / `set_frontmatter_field(content, key, value)` | Regex-based YAML-frontmatter getter/setter used to read `frame_status`/`url` and write back `frame_count`/`frame_status`/`frame_selection`. |
| `main()` | Guards against re-capturing an already-`complete` or `skipped` file (unless `--force`), clears stale frames from a prior capture, downloads the low-quality video via `ingest.download_video_low()`, extracts the requested frames via `ingest.extract_frames()`, appends a `## Captured Frames` section, and updates frontmatter. Does **not** commit — that happens together with the Structured Notes in Step 3. |

**Run it:** `python select_frames.py <slug> <ts1> <ts2> ...` (4-8 timestamps is typical) after reading the transcript in `tutorials/<slug>.md`.

### Step 3 — Extraction (done by Claude Code, not a script)

Claude reads each captured frame with the Read tool (which supports images), identifies which Blender editor is shown and lists exact node names/parameter values/viewport content, fills in every `[PENDING EXTRACTION]` marker in the Structured Notes (Core Technique, Summary, Key Steps, Nodes/Settings, Difficulty, Blender Version, Tags), cross-links related tutorials sharing 2+ tags, updates frontmatter (`blender_version:`, `tags:`, `extraction_status: complete`), and commits `tutorials/<slug>.md` + `INDEX.md` together.

### `validate.py` — post-ingest integrity checker

| Function | What it does |
|---|---|
| `fail(msg)` | Records a failure message and prints it — shared by every check below. |
| `get_tutorial_files()` | Lists every `tutorials/*.md` file except `INDEX.md`. |
| `parse_index_refs()` | Extracts every `**File:** tutorials/...` reference out of `INDEX.md`. |
| `get_notes_content(content)` | Pulls the `## Structured Notes` section body out of a tutorial file. |
| `is_youtube_source(content)` / `parse_duration_secs(content)` | Read `source:` frontmatter and the `**Duration:**` line. |
| `get_transcript_text(content)` | Reconstructs the raw transcript text from the `## Raw Data` section (stripping out any `## Ingest Safeguard Report` box first, since that has its own `---` divider that would otherwise be mistaken for the section boundary). |
| `check_tutorials()` | Runs checks 1–4 and 8–10: no `[PENDING EXTRACTION]` markers, no `extraction_status: pending`, no `blender_version` PENDING placeholders, no empty `tags: []`, no `PLACEHOLDER` URLs, structured notes ≥200 chars for YouTube sources, and a transcript-length sanity check (≥3 chars/sec of runtime) for videos over 3 minutes. |
| `check_index()` | Runs checks 5–7: no duplicate `INDEX.md` entries, every disk file is indexed, no `INDEX.md` entry points at a missing file. |
| `check_script_drift()` | Cross-skill check (warn-only, never fails the run): compares this repo's shared helper functions (`slugify`, `download_audio`, `ytdlp_captions`, `segment_by_chapters`, `_detect_hallucination`, `append_safeguard_note`, `find_duplicate_by_video_id`) against the same functions in every sibling skill installed on the same machine, and warns if a copy has drifted — catching an intentional fix in one skill that never got ported to the others. |
| `main()` | Runs all checks, prints a pass/fail summary, exits 1 on any failure. |

**Run it:** `python validate.py` after a batch of ingests, or any time you want to sanity-check the library.

### Extending this pipeline

- **New source type** (e.g. a forum thread, a PDF): follow the `fetch_article()` pattern — fetch + extract title/text, feed it through `build_raw_md()`'s `is_yt=False` path, no frame capture needed.
- **New quality check**: add a check function inside `check_tutorials()`/`check_index()` in `validate.py`, following the existing `fail(msg)` pattern.
- **New safeguard**: add a check inside `run_safeguards()` in `ingest.py`, appending to `warnings`/`critical` — it'll automatically get persisted via `build_safeguard_section()`.
- **New reference file**: add `references/<topic>.md`, then add it to the "Reference Files" table in `SKILL.md` so Claude knows when to reach for it.
- **Drive a live Blender scene**: see "Live Blender connection" below — no ingest-pipeline code changes needed, it's a separate MCP layer documented directly in `SKILL.md`.

---

## Every mode this skill supports

| Mode | Trigger phrases | What happens |
|---|---|---|
| **Setup** | "set up this skill", "new machine", "check if installed", "is this configured", "help me install this" | Reads `SETUP.md` and follows the "For Claude: New Machine Setup Protocol" checklist — runs each dependency check, reports what's missing, fixes it. |
| **0 — Validate Connection** | "check blender connection", "is blender connected", "validate blender", "test mcp" | Runs the Blender MCP connection check (`get_scene_info`) and reports status. Does not proceed with any build work regardless of the result. |
| **1 — Analyze & Recreate** | User provides a reference image/video frame/render | Deconstructs the reference (geometry, materials, lighting, motion, simulation type, post-processing, version) against `tutorials/INDEX.md` and the `references/*.md` library, and outputs a structured phased tutorial plan. |
| **2 — Build in Blender** | User provides a reference and says "build it" / "do it in Blender" | Runs Mode 0's connection check first (mandatory), then analyzes the reference, plans 3–5 Python/geometry-node phases, and executes each phase live in the user's open Blender scene via the Blender MCP server, with a screenshot after each phase. |
| **3 — Ingest Tutorial** | "ingest this tutorial: [URL]" | Runs the three-step pipeline above end to end without waiting to be re-prompted between steps. |

**Auto-Version-Check Rule (not a numbered mode):** at the start of a Mode 1 consultation, if `references/version-tracker.md`'s `last_checked` date is over 7 days old, the skill fetches Blender's release notes, compares against the Known Versions table, and ingests anything new into `references/blender-versions.md` — skipped when the user is in a hurry, so it never adds latency to a quick question.

## Live Blender connection

Mode 2 drives a real, running Blender scene directly via the **BlenderMCP addon** — this is the one connection protocol `SKILL.md` documents (not a menu of interchangeable third-party servers like some sibling skills offer). It requires Blender open, the addon enabled, and connected on port 9876 before any build work; Mode 0 validates this first and Mode 2 refuses to proceed if the connection isn't live.

| MCP Tool | What it does |
|---|---|
| `get_scene_info` | Read current scene objects, materials, modifiers |
| `execute_blender_code` | Run any Python/bpy script directly in Blender |
| `get_viewport_screenshot` | See what Blender currently looks like |
| `create_object` | Add mesh/curve/light/camera |
| `set_material` | Apply or create materials on objects |

`execute_blender_code` gives full access to Blender's Python API, including building geometry-node trees from scratch (`bpy.data.node_groups.new(..., "GeometryNodeTree")`, `tree.nodes.new(...)`, `tree.links.new(...)`). The Mode 2 build workflow is: validate connection → get scene info → take a screenshot → analyze the reference → plan 3–5 phases → execute one phase at a time, screenshotting and verifying after each → final screenshot to confirm the result matches. Full connection-check, error-handling, and troubleshooting steps are in `SKILL.md` → "Blender MCP — Connection Validation" and "Blender MCP — Direct Execution".

## Repo structure

```
blender-motion/
├── SKILL.md              ← main skill instructions Claude reads (modes, workflows, key rules)
├── README.md              ← this file
├── CODE_OF_CONDUCT.md      ← purpose/ethics statement — knowledge + consultation, not reproduction
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

Public personal project, no warranty. **299 tutorials ingested** (count auto-updates on every `ingest.py` run — do not hand-edit this line).
