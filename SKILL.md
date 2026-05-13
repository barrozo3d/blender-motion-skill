---
name: blender-motion
description: Analyze a photo, video frame, or render reference and generate step-by-step Blender tutorials to recreate it. Specialized in 3D motion design, geometry nodes, simulations, and ad/brand video production. Can ingest YouTube tutorials and articles to grow its knowledge base. Triggers on: "how do I make this in blender", "recreate this", "blender tutorial for this", "how was this made", "blender workflow", "geometry nodes", "ingest tutorial", "analyze this render".
---

# Blender Motion — Reference Analysis & Tutorial Skill

Analyze any visual reference (image, video frame, render) and produce a step-by-step Blender workflow to recreate it. Specialized in motion design, geometry nodes, simulations, and luxury/brand ad videos.

## Two Modes

### Mode 1 — Analyze & Recreate
User provides a reference image or video frame. The skill deconstructs it and outputs a structured tutorial plan.

### Mode 2 — Ingest Tutorial
User provides a URL (YouTube, article, documentation). The skill fetches, summarizes, and stores it as a searchable tutorial entry. **This is how the skill learns.**

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

### For YouTube URLs:
```bash
python -m yt_dlp --write-auto-subs --sub-lang en --skip-download \
  --output "%(id)s" --paths /tmp/ "[URL]" 2>/dev/null
```
Then read the subtitle file to extract transcript content.

### For web articles/documentation:
Use WebFetch to retrieve the page content.

### After fetching — run ingest.py:
```bash
python C:/Users/KABUM/.claude/skills/blender-motion/ingest.py "[URL]" "[TITLE]"
```

Or manually structure the entry and save to `tutorials/` and update `tutorials/INDEX.md`.

---

## Key Rules

1. **Never invent node names** — only use nodes confirmed to exist in the target Blender version
2. **Version-check everything** — simulation zones, certain GeoNodes, and rendering features are version-specific
3. **Always check INDEX.md first** — the tutorial library grows with every ingest
4. **Cite the reference files** — tell the user which technique library entry you're drawing from
5. **Estimate honestly** — if a technique requires a paid addon, say so
6. **Albin Merle shortcut** — if the aesthetic resembles his work, see `references/albin-merle-techniques.md` for exact setups

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
