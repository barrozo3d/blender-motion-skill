---
name: blender-motion
description: Analyze a photo, video frame, or render reference and generate step-by-step Blender tutorials to recreate it — or build it directly in Blender via MCP. Specialized in 3D motion design, geometry nodes, simulations, and ad/brand video production. Can ingest YouTube tutorials and articles to grow its knowledge base. Triggers on: "how do I make this in blender", "recreate this", "blender tutorial for this", "how was this made", "blender workflow", "geometry nodes", "build this in blender", "create geometry nodes", "ingest tutorial", "analyze this render".
---

# Blender Motion — Reference Analysis, Tutorial & Direct Execution Skill

Analyze any visual reference (image, video frame, render) and either produce a step-by-step tutorial plan **or build the scene directly inside Blender** using the Blender MCP connection.

## Three Modes

### Mode 1 — Analyze & Recreate (tutorial output)
User provides a reference image or video frame. The skill deconstructs it and outputs a structured tutorial plan.

### Mode 2 — Build in Blender (direct execution via MCP)
User provides a reference and says "build it" or "do it in Blender". The skill analyzes the reference, writes Python scripts, and executes them live in the user's open Blender scene via the Blender MCP server.

### Mode 3 — Ingest Tutorial
User provides a URL (YouTube, article, documentation). The skill fetches, summarizes, and stores it as a searchable tutorial entry. **This is how the skill learns.**

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

1. **Get scene info** — understand what's already in the scene
2. **Take screenshot** — see the current state
3. **Analyze reference** — deconstruct the visual (use visual-deconstruction.md)
4. **Plan in phases** — break the setup into 3–5 Python scripts (one per phase)
5. **Execute phase 1** — run script, take screenshot, verify
6. **Iterate** — fix errors, adjust values, continue to next phase
7. **Final screenshot** — confirm result matches reference

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

When the user says "ingest this: [URL]" or "learn from this: [URL]":

### Step 1 — Run ingest.py
```bash
python C:/Users/KABUM/.claude/skills/blender-motion/ingest.py "[URL]"
```
This fetches metadata + transcript, saves the raw `.md` file, updates `INDEX.md`, and pushes to GitHub.

### Step 2 — Extract Structured Notes (MANDATORY after every ingest)

After `ingest.py` completes, **always** run the extraction pass on the new file:

1. Read the saved tutorial file (path printed by ingest.py)
2. Analyze the transcript and description
3. Fill in the **Structured Notes** section:

```markdown
### Core Technique
[One sentence: what is the main Blender technique taught?]

### Key Steps
1. [Specific step with node/menu names]
2. [...]
(5–10 steps, be specific)

### Blender Nodes / Settings
- [Node or setting name]
- [...]

### Difficulty
[Beginner / Intermediate / Advanced / Expert]

### Blender Version
[Version if mentioned, otherwise "Not specified"]

### Tags
[space-separated hashtags from the tag list]
```

4. Update the frontmatter `blender_version:` and `tags:` fields
5. Update the `INDEX.md` entry: fill `**Blender Version:**`, `**Tags:**`, and write a real `**Summary:**`
6. Commit and push:
```bash
cd C:/Users/KABUM/.claude/skills/blender-motion
git add tutorials/
git commit -m "extract: [tutorial title]"
git push
```

### For web articles/documentation:
Use WebFetch to retrieve the page content, then follow Steps 1–6 above manually.

---

## Key Rules

1. **Never invent node names** — only use nodes confirmed to exist in the target Blender version
2. **Version-check everything** — simulation zones, certain GeoNodes, and rendering features are version-specific
3. **Always check INDEX.md first** — the tutorial library grows with every ingest
4. **Cite the reference files** — tell the user which technique library entry you're drawing from
5. **Estimate honestly** — if a technique requires a paid addon, say so
6. **Albin Merle shortcut** — if the aesthetic resembles his work, see `references/albin-merle-techniques.md` for exact setups
7. **Extraction is mandatory after every ingest** — never leave a tutorial file with `[To be extracted]` placeholders. Always run the extraction pass immediately after saving. No exceptions.

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
