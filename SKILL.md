---
name: blender-motion
description: Analyze a photo, video frame, or render reference and generate step-by-step Blender tutorials to recreate it — or build it directly in Blender via MCP. Specialized in 3D motion design, geometry nodes, simulations, and ad/brand video production. Can ingest YouTube tutorials and articles to grow its knowledge base. Triggers on: "how do I make this in blender", "recreate this", "blender tutorial for this", "how was this made", "blender workflow", "geometry nodes", "build this in blender", "create geometry nodes", "ingest tutorial", "analyze this render".
---

# Blender Motion — Reference Analysis, Tutorial & Direct Execution Skill

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
Before analyzing, read `tutorials/INDEX.md`. Search for matching techniques. If relevant tutorials exist, cite them in the output.

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

## Mode 2: Ingest Tutorial

**Both steps happen automatically** when the user says "ingest this tutorial: [URL]".
Do NOT wait to be asked for step 2 — run it immediately after step 1 completes.

### Step 1 — Data collection (run ingest.py)

```bash
python C:/Users/KABUM/.claude/skills/blender-motion/ingest.py "[URL]"
```

This runs without any API calls. It:
- Downloads audio and transcribes with Whisper
- Parses YouTube chapters
- Downloads low-quality video and extracts one frame per chapter
- Saves `tutorials/<slug>.md` with raw transcript + frame paths
- Saves frames to `tutorials/frames/<slug>/` (local only, not in git)
- Updates `INDEX.md` with a pending stub
- Commits and pushes raw data to GitHub

The script prints the tutorial file path and frames directory at the end.

### Step 2 — Extraction (done by Claude Code immediately after)

After ingest.py completes, run the full extraction pass without being asked:

1. **Read the tutorial file** printed by ingest.py (e.g. `tutorials/my-tutorial.md`)
2. **Read each frame** listed in the Raw Data section using the Read tool — the Read tool supports images, so `Read("tutorials/frames/slug/frame_000.jpg")` shows the actual frame
3. **Analyze each frame**: identify which Blender editor is shown, list exact node names, parameter values, viewport content
4. **Fill in ALL Structured Notes** (replace every `[PENDING EXTRACTION]`):
   - **Core Technique** — one sentence, the main Blender technique
   - **Summary** — 2-3 sentences, what the viewer learns and the end result
   - **Key Steps** — 5-10 steps with exact node names, menu paths, shortcuts
   - **Nodes / Settings** — all nodes and parameter values seen in transcript + frames
   - **Difficulty** — Beginner / Intermediate / Advanced / Expert
   - **Blender Version** — from transcript or frames; "Not specified" if unclear
   - **Tags** — from the approved tag pool in the Key Rules section
5. **Update frontmatter**: set `blender_version:`, `tags:`, `extraction_status: complete`
6. **Find related tutorials**: scan `INDEX.md` for entries sharing 2+ tags, add cross-links in `## Related Tutorials`
7. **Update INDEX.md entry**: replace `[PENDING]` fields with real version, tags, and summary
8. **Commit and push**:
```bash
cd C:/Users/KABUM/.claude/skills/blender-motion
git add tutorials/<slug>.md tutorials/INDEX.md
git commit -m "extract: [tutorial title]"
git push
```

### For web articles/documentation:
Run ingest.py with the article URL — it fetches page text. Then follow Step 2 above (no frames for articles).

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

## Key Rules

1. **Always validate before building** — call `get_scene_info` before any Mode 2 work; report the result; stop if the connection is not live
2. **Never invent node names** — only use nodes confirmed to exist in the target Blender version
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
