---
name: blender-motion
description: Analyze a photo, video frame, or render reference and generate step-by-step Blender tutorials to recreate it — or build it directly in Blender via MCP. Specialized in 3D motion design, geometry nodes, simulations, and ad/brand video production. Can ingest YouTube tutorials and articles to grow its knowledge base. Triggers on: "how do I make this in blender", "recreate this", "blender tutorial for this", "how was this made", "blender workflow", "geometry nodes", "build this in blender", "create geometry nodes", "ingest tutorial", "analyze this render".
---

# Blender Motion — Reference Analysis, Tutorial & Direct Execution Skill

## About

Expert consultant for **Blender**, covering motion design, geometry nodes, simulation (fluid, pyro, rigid body, cloth, particles), materials/shaders, lighting & compositing, and ad/brand video production. Analyzes any visual reference (image, video frame, render) and either produces a step-by-step tutorial plan or builds the scene directly inside a running Blender session over the Blender MCP connection. Answers questions, writes Python/geometry-node setups, and grows its own knowledge base by ingesting tutorials — same architecture as this skill's siblings (`houdini-wand`, `unreal-sidekick`, `nuke-em-all`, `paint-me-like-your-french-substances`).

**Not in scope:** other DCC tools (Houdini, Unreal Engine, Nuke, Substance Painter — see the sibling skills for those) and manual hand-painted texturing/sculpting workflows outside Blender's procedural/GeoNodes toolset.

> **Live Blender connection.** Mode 2 drives a real, running Blender scene directly via the BlenderMCP addon (`get_scene_info`, `execute_blender_code`, `get_viewport_screenshot`, `create_object`, `set_material`) — see "Blender MCP — Connection Validation" below. It requires Blender open with the BlenderMCP addon connected before use; Mode 0 validates the connection first.

Analyze any visual reference (image, video frame, render) and either produce a step-by-step tutorial plan **or build the scene directly inside Blender** using the Blender MCP connection.

## Modes

### Mode Setup — New Machine Setup
User says "set up this skill", "new machine", "check if installed", "is this configured", or "help me install this". Read `SETUP.md` and follow the "For Claude: New Machine Setup Protocol" checklist. Run each check, report what's missing, and fix it.

### Mode 0 — Validate Connection
User says "check blender connection", "is blender connected", "validate blender", or "test mcp". Run the connection check and report status. Do not proceed with any build work.

### Mode 1 — Analyze & Recreate (tutorial output)
User provides a reference image or video frame. The skill deconstructs it and outputs a structured tutorial plan.

### Mode 2 — Build in Blender (direct execution via MCP)
User provides a reference and says "build it" or "do it in Blender". The skill analyzes the reference, writes Python scripts, and executes them live in the user's open Blender scene via the Blender MCP server. **Always run the connection check (Mode 0) before any build work.**

### Mode 3 — Ingest Tutorial
User provides a URL (YouTube, article, documentation). The skill fetches, summarizes, and stores it as a searchable tutorial entry. **This is how the skill learns.**

---

## Blender MCP — Connection Validation

**Run this check at the start of every Mode 2 session, and whenever the user asks to validate.**

### Validation Procedure

1. Call `get_scene_info` (lightweight — reads scene metadata only).
2. **If it succeeds:** report the following and confirm connection is live:
   ```
   ✓ Blender MCP connected
   Scene: [scene name]
   Objects: [count]
   Active object: [name or "none"]
   ```
3. **If it fails** (error, timeout, or tool not found): stop immediately. Do not attempt any build work. Show this checklist:

   ```
   ✗ Blender MCP not connected

   Fix checklist — complete in order:
   1. Open Blender (must be running before Claude Code)
   2. Edit → Preferences → Add-ons → search "BlenderMCP" → enable it
   3. Press N in the viewport → BlenderMCP tab → click "Connect"
      Confirm it shows: "Running on port 9876"
   4. Restart Claude Code (MCP tools only register at session start)
   5. Run "check blender connection" again

   Note: first connection after Blender opens takes ~40 seconds.
   Blender must be open and warmed up for at least a minute.
   ```

---

## Blender MCP — Direct Execution

When the Blender MCP is connected (user has the addon running in Blender), use these tools:

| MCP Tool | What it does |
|---|---|
| `get_scene_info` | Read current scene objects, materials, modifiers |
| `execute_blender_code` | Run any Python/bpy script directly in Blender |
| `get_viewport_screenshot` | See what Blender currently looks like |
| `create_object` | Add mesh/curve/light/camera |
| `set_material` | Apply or create materials on objects |

### Geometry Nodes via MCP

The `execute_blender_code` tool gives full access to Blender's Python API for geometry nodes:

```python
import bpy

# Get or create target object
obj = bpy.context.active_object

# Add GeoNodes modifier
mod = obj.modifiers.new("GeoNodes", "NODES")
tree = bpy.data.node_groups.new("Setup", "GeometryNodeTree")
mod.node_group = tree

# Add nodes
in_node  = tree.nodes.new("NodeGroupInput")
out_node = tree.nodes.new("NodeGroupOutput")
dist     = tree.nodes.new("GeometryNodeDistributePointsOnFaces")
inst     = tree.nodes.new("GeometryNodeInstanceOnPoints")

# Position nodes for readability
in_node.location  = (-400, 0)
dist.location     = (-200, 0)
inst.location     = (0, 0)
out_node.location = (200, 0)

# Connect
tree.links.new(in_node.outputs["Geometry"], dist.inputs["Mesh"])
tree.links.new(dist.outputs["Points"],      inst.inputs["Points"])
tree.links.new(inst.outputs["Instances"],   out_node.inputs["Geometry"])
```

### Build Workflow (Mode 2)

1. **Validate connection** — run the connection check above. Stop if it fails.
2. **Get scene info** — understand what's already in the scene
3. **Take screenshot** — see the current state
4. **Analyze reference** — deconstruct the visual (use visual-deconstruction.md)
5. **Plan in phases** — break the setup into 3–5 Python scripts (one per phase)
6. **Execute phase 1** — run script, take screenshot, verify
7. **Iterate** — fix errors, adjust values, continue to next phase
8. **Final screenshot** — confirm result matches reference

### Error handling

If `execute_blender_code` fails:
- Read the error message carefully — usually a wrong node type name or input index
- Check node type names: `bpy.types.GeometryNode*` — names must be exact
- Common mistake: node input/output index vs. name — use names when possible
- Break complex setups into smaller scripts and test each step

---

## Mode 1: Analysis Workflow

### Step 1 — Check the Tutorial Library
Before analyzing, search `tutorials/INDEX.md` for matching techniques. The INDEX is ~1000 lines — grep it by keyword/tag first (e.g. `geometry-nodes`, `#materials`, a node name) and read only the matching entry blocks rather than the whole file. If relevant tutorials exist, cite them in the output.

### Step 2 — Visual Deconstruction
Read `references/visual-deconstruction.md` and apply the full analysis framework:
- **Geometry** — what is the base form? hard surface, organic, procedural, simulated?
- **Materials** — metal, glass, fabric, liquid, particle, emission, subsurface?
- **Lighting & Ambiance** — see `references/lighting-composition.md`
- **Motion** — camera move or geometry move? what easing? is it looping?
- **Simulation type** — fluid, pyro, rigid body, cloth, particles, or procedurally faked?
- **Post-processing** — depth of field, motion blur, lens flare, compositing tells
- **Blender version** — check `references/blender-versions.md` to suggest the right version

### Step 3 — Technique Mapping
Cross-reference the deconstruction against:
- `references/geometry-nodes-library.md` — for procedural setups
- `references/simulation-catalog.md` — for physics/simulation
- `references/materials-shaders.md` — for material recreation
- `references/motion-design-patterns.md` — for motion language
- `references/ad-video-patterns.md` — for brand/commercial context
- `references/albin-merle-techniques.md` — if the style resembles his work

> ### ⚠️ Reference files are not all trustworthy
>
> Every `references/*.md` carries a provenance header. **Check `class:` and
> `verified:` before citing:**
>
> | `class:` | Means |
> |---|---|
> | `release-notes` | Condensed from the vendor's official release notes (URL in `sources:`). Comparatively trustworthy. |
> | `topic-reference` | ⚠️ **Written from model memory, not ingested from any source** (`verified: no`). Do not cite as authority. |
> | `operational` | Internal state file, not knowledge. |
>
> - **When a reference file and an ingested tutorial disagree, the tutorial
>   wins** — tutorials are transcript- and frame-verified against real footage.
> - Expect `topic-reference` files to be *least* reliable on the *newest*
>   subsystems — that is where invented detail is most likely and hardest to spot.
>
> **Precedent:** on 2026-08-19 `houdini-wand`'s `references/copernicus.md` was
> found to be fabricated — 26 of its 33 asserted node names had **zero**
> corroboration across 545 ingested tutorials — after it caused four consecutive
> wrong answers to a simple question. Audit status is tracked in
> `houdini-wand/PROMO_ENTRY_CLEANUP_PLAN.md` (workstream B).

> ### ⚠️ Attribute every claim — "never invent" is not enough on its own
>
> Key Rule #2 ("never invent ... names") has been in this file from the start and
> did **not** prevent the 2026-08-19 incident. Fabrication entered at *authoring*
> time: once wrong names were written into `references/copernicus.md`, citing them
> *satisfied* the rule. **A rule that can be satisfied by a corrupted source
> protects nothing.**
>
> It also cannot work by introspection. Generating a plausible name feels
> identical to recalling a real one — there is no internal signal to check
> against. So do not ask yourself *"am I sure?"*. Ask **"which file does this come
> from?"** and write the answer down:
>
> | Tag | Meaning |
> |---|---|
> | `[tutorials/<file>.md]` | confirmed in an ingested tutorial — grep-able, so the reader can check you |
> | `[docs: <url>]` | official vendor documentation |
> | `[unverified]` | your own knowledge; no source in this skill |
>
> **`[unverified]` is a correct and expected tag, not a failure.** Use it rather
> than dropping the claim. **Never invent a citation to avoid it** — a fabricated
> filename is far worse than an honest `[unverified]`, because it destroys the
> reader's ability to check anything. Cite only files you actually opened.
>
> ### "Not covered" is a correct answer
>
> If the library and references do not cover the question, **say so and stop.**
> State what *is* covered, what is missing, and offer to ingest a source.
>
> **The answer format is a guide, not a quota.** It asks for exact names and
> parameter values; when you do not have them, write
> `[unverified — exact name not confirmed]` instead of a plausible guess. That
> demand for exact names is itself a fabrication pressure: three sourced steps
> with an honest gap beat six steps where two are invented.


### Step 4 — Tutorial Output

Structure the response as:

```
## Visual Analysis
[What you see: geometry, materials, lighting, motion, post — be specific]

## Closest Match in Tutorial Library
[If found in INDEX.md, cite it. Otherwise: "No direct match — generating from technique library."]

## Blender Version Recommendation
[Which version and why — see blender-versions.md]

## Technique Breakdown
[List the 3–6 core techniques required, in order of complexity]

## Step-by-Step Tutorial

### Phase 1 — [Name]
[Detailed steps]

### Phase 2 — [Name]
[Detailed steps]

[Continue for each phase]

## Render Settings
[Cycles vs EEVEE, samples, denoising, motion blur settings]

## Compositing (After Effects / Blender Compositor)
[Post-production steps]

## Estimated Complexity
[Beginner / Intermediate / Advanced + estimated hours]

## Related Tutorials in Library
[List any relevant ingested tutorials from INDEX.md]
```

---

## Mode 3: Ingest Tutorial

Three steps happen when the user says "ingest this tutorial: [URL]". Do NOT wait
to be asked for step 2 or step 3 — run each immediately after the previous one
completes. Frame capture is deliberately **not** automatic — it requires
judgment about which moments in the video are worth a still, which is why it's
a separate step done by Claude reading the transcript, not something ingest.py
guesses at with blind percentages.

### Step 1 — Data collection (run ingest.py)

Run from this skill's own directory (the folder containing this SKILL.md — works on any machine):
```bash
python ingest.py "[URL]"
```

This runs without any API calls and downloads no video. It:
- Downloads audio and transcribes with Whisper, preserving per-sentence timestamps (even inside chapters)
- Parses YouTube chapters
- Saves `tutorials/<slug>.md` with the raw timestamped transcript (`frame_status: pending-selection`)
- Updates `INDEX.md` with a pending stub
- Commits and pushes raw data to GitHub

The script prints the tutorial file path and a reminder to run `select_frames.py` next.

### Step 2 — Frame selection (run select_frames.py)

1. **Read the timestamped transcript** in the tutorial file's `## Raw Data` section.
2. **Pick 4-8 moments** that actually show a technique/result worth a still — not blind percentages of the runtime, and not just chapter-start + a few seconds. Verify each pick against the transcript's own timestamps.
3. **Run the script** with those timestamps (seconds or mm:ss, mixed freely):
```bash
python select_frames.py <slug> <ts1> <ts2> ...
```
This downloads the low-quality video, extracts exactly those frames to `tutorials/frames/<slug>/` (local only, not in git), appends a `## Captured Frames` section to the tutorial file, and sets `frame_status: complete` in the frontmatter. It does **not** commit — that happens together with the Structured Notes in Step 3.

### Step 3 — Extraction (done by Claude Code immediately after)

1. **Read each frame** listed in the `## Captured Frames` section using the Read tool — the Read tool supports images, so `Read("tutorials/frames/slug/frame_000.jpg")` shows the actual frame
2. **Analyze each frame**: identify which Blender editor is shown, list exact node names, parameter values, viewport content
3. **Fill in ALL Structured Notes** (replace every `[PENDING EXTRACTION]`):
   > **Cite where each name came from (D2 provenance convention).** When a node
   > name, parameter value or setting comes from a frame, tag it: ``
   > `Fractal Noise 3D` [frame_003] ``. When it comes from narration, tag the
   > timestamp: `[transcript 12:04]`. **Where the frame and the transcript
   > disagree, prefer the frame and record both** — the transcript is the
   > unreliable source (Whisper mishears node names), the frame is not.
   >
   > This is already common practice — 719 such citations exist across the five
   > skills — and `validate.py` **check #16** now verifies every `frame_NNN`
   > citation against the file's own `frame_count`. It checks the file's record,
   > not the filesystem, because frames are gitignored and device-local: a
   > machine that never downloaded them is not evidence of absence.
   - **Core Technique** — one sentence, the main Blender technique
   - **Summary** — 2-3 sentences, what the viewer learns and the end result
   - **Key Steps** — 5-10 steps with exact node names, menu paths, shortcuts
   - **Nodes / Settings** — all nodes and parameter values seen in transcript + frames
   - **Difficulty** — Beginner / Intermediate / Advanced / Expert
   - **Blender Version** — from transcript or frames; "Not specified" if unclear
   - **Tags** — from the approved tag pool in the Key Rules section
4. **Update frontmatter**: set `blender_version:`, `tags:`, `extraction_status: complete`
5. **Find related tutorials**: scan `INDEX.md` for entries sharing 2+ tags, add cross-links in `## Related Tutorials`
6. **Update INDEX.md entry**: replace `[PENDING]` fields with real version, tags, and summary

   > ⚠️ **Edit that ONE block. Never rewrite `INDEX.md` wholesale.**
   > On 2026-08-20 a `git blame` audit (plan batch E2) traced every piece of
   > INDEX corruption to this step regenerating the whole file: an "extract:
   > Dash batch 6" commit rewrote **174 lines** for 5 tutorials and mojibake'd
   > line 1, the file's own title; a single-tutorial extract changed INDEX.md by
   > **−1031/+72**; a 4-tutorial batch wrote **one summary into three blocks**.
   > Passing the whole file through an ad-hoc read/write damages lines nobody was
   > editing — on Windows, PowerShell's `Set-Content`/`Out-File` default to the
   > ANSI code page and a UTF-8→cp1252 round-trip produces exactly that mojibake.
   >
   > Use the tool, which edits a single block with explicit UTF-8:
   > ```bash
   > python update_index_entry.py <slug> --from-file      # fields from the file
   > python update_index_entry.py <slug> --set 'Tags=a, b' # set one field exactly
   > python update_index_entry.py --all --check           # differences, writes nothing
   > ```
   > A batch is **N single-block edits**, never one regeneration. The summary is
   > still written by you — `--summary` regenerates it from the file and is for
   > *repair*, since INDEX summaries are curated, not mechanical truncations.
   > `validate.py` check #12 catches recurrence; this prevents it.

7. **Commit and push** (from this skill's own directory):
```bash
git add tutorials/<slug>.md tutorials/INDEX.md
git commit -m "extract: [tutorial title]"
git push
```

### For web articles/documentation:
Run ingest.py with the article URL — it fetches page text, `can_have_frames` is false, `frame_status: skipped`. Skip Step 2 (no frames) and go straight to Step 3.

### The promo gate — `validate.py` check #11

**A tutorial must teach a technique, not advertise one.** `validate.py` fails on
any entry that looks promotional and has not been triaged. Scoring lives in
`scan_promo.py` (imported, never duplicated); run it directly to investigate:

```bash
python scan_promo.py                  # ranked candidates
python scan_promo.py --explain FILE   # why one file scores what it does
```

**Why the gate exists.** `tutorials/noise.md` was a 1m31s course trailer titled
exactly "Noise", tagged with eleven topics it never demonstrated. It was the top
grep hit for any noise question and produced four consecutive wrong answers. The
two older content checks are both length-based (#8 notes > 200 chars, #9 ≥ 3
chars/sec above 180s), and a trailer beats length heuristics by construction —
dense fluent speech about material that is never shown. Nothing asked *"does
this teach a technique?"*

**What trips it.** Only a **self-declared** signal: the extraction's own prose
calling the entry a trailer, an advertisement, or a course announcement.
Structural signals — short video, thin Key Steps, few named nodes — corroborate
but never accuse on their own, because that shape is *also* a perfectly good
short-form feature tutorial, which is how most plugin and add-on documentation
is published. Entries scoring on structure alone are reported as
`STRUCTURAL-ONLY` and are **not** failures.

**When it fires, you have three honest options** — never loosen the scorer:

| Option | When | What to do |
|---|---|---|
| **REMOVE** | Pure promo: no technique, no curriculum outline | Follow the Removal Procedure in `PROMO_ENTRY_CLEANUP_PLAN.md` — **grep for inbound links first**, they are not reciprocal |
| **DEMOTE** | Real content, oversold framing | Lead the INDEX summary with a depth marker, strip tags that let it beat real tutorials, then allowlist it |
| **KEEP** | False positive, series intro chapter, deliberate paywalled gap-filler | Add to `scan_promo.ALLOWLIST` **with a written reason** |

`ALLOWLIST` is a **decision record, not a mute button**. Every entry states what
was decided and why the entry legitimately keeps scoring. Adding one is the
intended way to clear this check.

**At ingest time** `ingest.py` emits a WARNING (never `needs-review`) for a
short video whose transcript ends in a call to action. It cannot decide — the
Structured Notes do not exist yet — so it does the one useful thing it can: it
asks the extraction pass to **state plainly whether the video demonstrates a
technique or only advertises one**. That sentence is what check #11 reads, so
write it honestly either way.

### Re-ingesting an existing tutorial
`ingest.py --force` re-collects transcript-only data and refuses to overwrite a file that's already `extraction_status: complete` unless `--force` is passed. `select_frames.py --force` re-captures frames even if `frame_status` is already `complete`.

### Approved tag pool
```
geometry-nodes, simulation, particles, fluid, rigid-body, cloth, smoke-fire,
materials, shaders, procedural, displacement, animation, rigging, camera,
compositing, rendering, cycles, eevee, lighting, hdri, volume,
product-viz, motion-design, abstract, logo-animation, typography,
glass, metal, organic, brand-video,
beginner, intermediate, advanced, expert,
blender-3x, blender-4x, blender-5x
```

---

## Auto-Version-Check Rule

**Trigger:** At the start of a consultation/analysis (Mode 1), before recommending versions or features.

1. Read `references/version-tracker.md`; check `last_checked`.
2. If more than 7 days ago: fetch `https://developer.blender.org/docs/release_notes/` and compare against the Known Versions table.
3. New version found -> ingest its notes into `references/blender-versions.md`, update the tracker, commit and push.
4. No new version -> just update `last_checked`.

**Skip when** the user is in a hurry — don't add latency to a quick question.

---

## Key Rules

1. **Always validate before building** — call `get_scene_info` before any Mode 2 work; report the result; stop if the connection is not live
2. **Never invent node names** — only use nodes confirmed to exist in the target Blender version. **And attribute them** — "confirmed" means you can name the file it came from (see *Attribute every claim*)
3. **Version-check everything** — simulation zones, certain GeoNodes, and rendering features are version-specific
4. **Always check INDEX.md first** — the tutorial library grows with every ingest
5. **Cite the reference files** — tell the user which technique library entry you're drawing from
6. **Estimate honestly** — if a technique requires a paid addon, say so
7. **Albin Merle shortcut** — if the aesthetic resembles his work, see `references/albin-merle-techniques.md` for exact setups
8. **Extraction is mandatory after every ingest** — never leave a tutorial file with `[To be extracted]` placeholders. Always run the extraction pass immediately after saving. No exceptions.
9. **Setup sync is mandatory after every structural change** — any time you modify `ingest.py`, add a dependency, change a model name, add a CLI flag, rename a file or directory, or change any configuration that affects how the skill is installed or run, you MUST update all three setup files in the same commit:
   - `requirements.txt` — add/remove/update the pip package
   - `setup.ps1` — reflect the new install step or config change
   - `SETUP.md` — update the relevant step, troubleshooting entry, or reference table
   Never commit a structural change without syncing the setup pack. The rule: **if a user on a fresh machine would need to do something different to get the skill working, the setup files must reflect that.** Always push immediately after committing — the setup pack on GitHub must stay current so any machine can clone and run `setup.ps1` without extra steps.

---

## Reference Files

| File | What it covers |
|------|---------------|
| `visual-deconstruction.md` | How to read any render |
| `lighting-composition.md` | Lighting rigs, ambiance, composition |
| `geometry-nodes-library.md` | ~50 core GeoNodes techniques |
| `simulation-catalog.md` | Physics and simulation recipes |
| `materials-shaders.md` | Cycles material setups |
| `motion-design-patterns.md` | Motion language and animation |
| `ad-video-patterns.md` | Brand and commercial patterns |
| `render-pipeline.md` | Cycles → AE compositing |
| `blender-versions.md` | Version changelog and feature availability |
| `albin-merle-techniques.md` | Albin Merle specific setups |
| `tutorials/INDEX.md` | All ingested tutorials |
