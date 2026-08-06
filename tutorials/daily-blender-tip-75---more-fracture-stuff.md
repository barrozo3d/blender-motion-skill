---
title: Daily Blender Tip 75 - More Fracture Stuff!
source: YouTube
url: https://www.youtube.com/watch?v=ZDq2WOrqpRM
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — built-in Cell Fracture add-on + Rigid Body physics workflow is version-agnostic"
tags: [simulation, rigid-body, procedural, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-75---more-fracture-stuff/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 75 - More Fracture Stuff!

**Source:** [YouTube](https://www.youtube.com/watch?v=ZDq2WOrqpRM)
**Author:** Blender Secrets
**Duration:** 1m36s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 17 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (17 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] Complete the work



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-75---more-fracture-stuff/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-75---more-fracture-stuff/frame_001.jpg
- [0:45] tutorials/frames/daily-blender-tip-75---more-fracture-stuff/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-75---more-fracture-stuff/frame_003.jpg
- [1:25] tutorials/frames/daily-blender-tip-75---more-fracture-stuff/frame_004.jpg
- [1:35] tutorials/frames/daily-blender-tip-75---more-fracture-stuff/frame_005.jpg

---

## Structured Notes

### Core Technique
Using Blender's built-in **Cell Fracture** add-on (distinct from the third-party "Fracture Modifier" build covered in Tips 139–141) to shatter a subdivided cube into voronoi-like chunks, then assigning **Rigid Body** physics to the resulting fragments so they explode/collapse realistically when the simulation is played.

### Summary
Frame 000 shows a plain cube with a **Subdivision Surface** modifier applied, captioned "Add a subdiv modifier to a cube, level 3, set it to simple and apply it" — extra geometry gives Cell Fracture more points to shatter along, producing more numerous/varied fragments. Frame 001 shows the Cell Fracture operator panel (Source Limit, Source, Recursion settings, Shrink Factor, Clamp Recursion, Smooth Faces, Sharp Edges, Apply Split Edge, Material, Point Source Volume/Mesh/Own, Recursion, Layer Index) open over the cube, captioned "Use Cell Fracture on the cube, turn off Sharp Edges. Click OK." Frame 002 shows the resulting shattered chunks reassembled to look like the original cube shape, shaded smooth, captioned "... and choose modifiers. Set the shading to smooth." Frame 003 shows the same fractured chunk cluster from a wider angle sitting on a ground plane, ready for physics setup. Frame 004 shows the Physics Properties Rigid Body panel (Rigid Body Tools: AddPassive/AddPassive, Change Shape, Calculate Mass, Apply Transformation, Bake to Keyframes, Connect; Rigid Body Type visible), captioned "Press Alt+a to play the simulation" — the fractured chunks now shown scattered/collapsed mid-explosion. Frame 005 is the closing Mandala Motion channel card.

### Key Steps
1. Start with a cube and add a **Subdivision Surface** modifier (level 3, Simple), then **Apply** it — pre-subdividing gives Cell Fracture more geometry to generate a larger number of varied fragments from.
2. Select the cube and run **Object > Quick Effects > Cell Fracture** (built-in add-on, enable it in Preferences if not already active).
3. In the Cell Fracture operator options, turn **off Sharp Edges** (avoids overly hard shading seams on the new fracture faces) and confirm.
4. Select all resulting fragment objects and set their shading to **Smooth** for a cleaner look.
5. Select all fragments and add **Rigid Body** physics (Object > Rigid Body > Add Active, or via the Physics Properties panel), optionally also adding a Passive Rigid Body ground plane for collision.
6. Press **Alt+A** to play the simulation — the fractured chunks separate and fall/collapse under rigid body physics, producing a realistic explosion/collapse effect.

### Nodes / Settings
- **Modifier:** Subdivision Surface (level 3, Simple) — applied before fracturing for more fragment detail.
- **Add-on operator:** Cell Fracture (Source, Recursion, Shrink Factor, Sharp Edges toggle, Material, Point Source options).
- **Physics:** Rigid Body (Active on fragments, Passive on ground); Alt+A to play.

### Difficulty
Beginner

### Blender Version
Not specified — built-in Cell Fracture add-on + Rigid Body physics workflow is version-agnostic and predates (and is distinct from) the third-party Fracture Modifier build covered in Tips 139–141.

### Tags
simulation, rigid-body, procedural, beginner

---

## Related Tutorials
- [Daily Blender Tip 139 - Blender Fracture Modifier Build - Quick Start](daily-blender-tip-139---blender-fracture-modifier-build---quick-start.md) — shares rigid-body, simulation; covers a more advanced third-party Fracture Modifier build for fracturing, as opposed to this tutorial's built-in Cell Fracture + Rigid Body approach.
- [Daily Blender Tip 140 - Fracture Modifier Use Constraints](daily-blender-tip-140---fracture-modifier-use-constraints.md) — shares rigid-body, simulation; same third-party Fracture Modifier series, a more advanced alternative to this Cell Fracture technique.
- [Daily Blender Tip 90 - How To Have Characters Interact With Physics Simulations](daily-blender-tip-90---how-to-have-characters-interact-with-physics-simulations.md) — shares rigid-body, simulation; uses this tutorial's Cell Fracture + Rigid Body wall-shattering setup as the simulation a rigged character physically interacts with via bone-parented Animated proxies.
