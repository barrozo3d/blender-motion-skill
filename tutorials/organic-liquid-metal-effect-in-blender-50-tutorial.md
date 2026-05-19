---
title: Organic Liquid Metal effect in blender 5.0 (tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=2MKKuHcni1U
author: Ducky 3D
ingested: 2026-05-19
blender_version: "5.0"
tags: [geometry-nodes, sdf, materials, shaders, motion-design, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/organic-liquid-metal-effect-in-blender-50-tutorial/
frame_count: 0
---

# Organic Liquid Metal effect in blender 5.0 (tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=2MKKuHcni1U)
**Author:** Ducky 3D
**Duration:** 10m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** All right, in this tutorial, we are going to be creating this render right here. The point of it is to show you how to use the new volume SDF nodes to get these spheres, to have these really thin liquidity connected pieces to each one of them and show you how to get that. What this is going to teach you is how to combine multiple objects into each other with the grid SDF Boolean node. So it's a really creative application for that node. So if you want to check out the project file that is available on Patreon right now, and Patreon is also 25% off till the end of November. So if you want to check that out, along with all of my courses and real-time materials, are 50% off with this code. All that stuff is available till the end of the month. That's my Black Friday sale. So if you want to check it out, support me. That'd be awesome. But with that being said, let's get into this tutorial. All right, you are going to need Blender 5.0 or later to be able to do this. So let's go ahead, Shift-A. We'll get a plane that'll be our geometry. That'll be the object we need for geometry nodes. I'm going to open up a new window and switch this over to geometry nodes. I'm going to click new. So I'...



---

## Structured Notes

### Core Technique
Using Blender 5.0's new Volume SDF nodes — specifically the Grid SDF Boolean node — to blend multiple sphere instances into organically connected liquid-metal blobs with thin connecting membranes.

### Summary
10-minute focused tutorial on the new SDF volume pipeline in Blender 5.0. Creates scattered spheres as a plane with Geometry Nodes, converts them to SDF volumes, booleans them together with Grid SDF Boolean to produce metaball-like organic connections, then applies a polished metallic shader. Requires Blender 5.0 or later.

### Key Steps
1. **Geometry setup** — Shift+A → Plane; open Geometry Nodes editor, click New
2. **Scatter spheres** — distribute sphere instances on the plane using Instance on Points with Scatter Points or manual point placement; vary radius with random values
3. **Convert to SDF** — use `Mesh to SDF` node (Blender 5.0+) on each sphere instance; each becomes a signed distance field volume
4. **Grid SDF Boolean** — feeds multiple SDF volumes in; blends them together creating organic liquid metal connections between spheres wherever they are close enough
5. **SDF to mesh** — convert resulting SDF volume back to mesh with `SDF to Mesh` node; adjust threshold/iso-value to control membrane thickness
6. **Metallic material** — Principled BSDF: Metallic=1, Roughness ~0.05–0.1, add subtle noise bump for surface imperfection

### Nodes / Settings
- `Mesh to SDF` — converts mesh geometry to SDF volume (Blender 5.0+)
- `Grid SDF Boolean` — blends/booleans multiple SDF volumes organically; key node for liquid connections
- `SDF to Mesh` — extracts mesh from SDF at a given iso-value
- `Instance on Points` — scatter sphere instances as source geometry
- `Random Value` — vary sphere radii
- Principled BSDF: Metallic=1.0, low Roughness for chrome look
- Requires **Blender 5.0 or later** (SDF volume nodes introduced in 5.0)

### Difficulty
Intermediate

### Blender Version
5.0

### Tags
geometry-nodes, sdf, materials, shaders, motion-design, intermediate

---

## Related Tutorials
- [[glass-cell-division-effect-in-blender-50-tutorial]] — another organic Blender 5.0 effect
- [[you-should-make-glass-animations-in-blender-51]] — glass material effects
- [[3d-smoke-blender-geometry-nodes]] — GeoNodes volume effects
