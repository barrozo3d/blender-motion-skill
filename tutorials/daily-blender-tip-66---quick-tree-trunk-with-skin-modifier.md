---
title: Daily Blender Tip 66 - Quick Tree Trunk With Skin Modifier
source: YouTube
url: https://www.youtube.com/watch?v=nfuk9ywJc44
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Skin modifier, Merge at Center, and Proportional Editing are version-agnostic core Blender modeling tools"
tags: [modelling, procedural, organic, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-66---quick-tree-trunk-with-skin-modifier/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 66 - Quick Tree Trunk With Skin Modifier

**Source:** [YouTube](https://www.youtube.com/watch?v=nfuk9ywJc44)
**Author:** Blender Secrets
**Duration:** 2m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 21 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (21 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] Shoulder,
[1:50] Photo mode,



---

## Captured Frames

- [0:10] tutorials/frames/daily-blender-tip-66---quick-tree-trunk-with-skin-modifier/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-66---quick-tree-trunk-with-skin-modifier/frame_001.jpg
- [0:50] tutorials/frames/daily-blender-tip-66---quick-tree-trunk-with-skin-modifier/frame_002.jpg
- [1:10] tutorials/frames/daily-blender-tip-66---quick-tree-trunk-with-skin-modifier/frame_003.jpg
- [1:30] tutorials/frames/daily-blender-tip-66---quick-tree-trunk-with-skin-modifier/frame_004.jpg
- [1:55] tutorials/frames/daily-blender-tip-66---quick-tree-trunk-with-skin-modifier/frame_005.jpg

---

## Structured Notes

### Core Technique
Building a quick tree trunk/branch skeleton by collapsing a mesh to a single vertex, extruding a branching vertex "stick figure" in 3D, then applying the **Skin** modifier to instantly generate thick, tapered tube-like geometry along those edges — a fast way to block out organic branching forms (tree trunks, plants) without manually modeling cylinders.

### Summary
Frame 000 shows a default cube in Edit Mode, captioned "In edit mode merge your default cube to one vertex with Alt+M > merge to center." Frame 001 shows a branching stick-figure structure of connected vertices/edges radiating from a center point, captioned "Extrude that vertex by pressing E and direction X, Y or Z. Rotate the view and extrude some more 'branches'." Frame 002 shows the same vertex skeleton now rendered as a thin uniform-width tube structure with a **Skin** modifier added to the modifier stack, captioned "Add a skin modifier to the resulting object. Select all the vertexes again in edit mode and scale them with CTRL+A and dragging the mouse." Frame 003 shows the skinned branches now varying — thicker at the trunk base tapering out toward the branch tips — with the Skin modifier's Branch Smoothing and Mark Root/Mark Loose options visible in the sidebar. Frame 004 shows the same branching tree-trunk shape with **Proportional Editing** (O) enabled (a falloff circle radius visible), captioned "Press 'o' for proportional editing, select the bottom vertex, drag the middle mouse wheel to change the proportional edit... CTRL+A to scale" — used to smoothly taper multiple nearby vertices together at once. Frame 005 is the closing card, captioned "This is a good start for a tree trunk or some kind of plant. You can apply the skin modifier now if you want and edit it as a normal mesh."

### Key Steps
1. Start with a default cube (or any mesh), enter Edit Mode, select all, and **Alt+M > Merge at Center** to collapse it down to a single vertex.
2. **Extrude (E)** that vertex repeatedly along X/Y/Z, rotating the view between extrusions, to build a branching "stick figure" skeleton representing the trunk and branches.
3. Add a **Skin** modifier to the object — this instantly generates tube-like geometry that follows the vertex/edge skeleton.
4. Back in Edit Mode, select individual vertices (or all with **Ctrl+A**, drag to scale) to control each segment's skin **radius** — thicker near the trunk base, thinner toward branch tips.
5. Use **Proportional Editing (O)**, adjusting the falloff radius with the mouse wheel, to smoothly scale a cluster of nearby vertices together (e.g. a gradual base-to-tip taper) instead of adjusting each one individually.
6. The result is a fast, editable trunk/branch base mesh — apply the Skin modifier once satisfied to convert it into a normal, further-editable mesh (for detailing, UVs, bark texture, etc.).

### Nodes / Settings
- **Shortcut:** Alt+M > Merge at Center — collapse geometry to a single vertex.
- **Shortcut:** E — extrude, building the branch skeleton.
- **Modifier:** Skin — generates tube geometry from a vertex/edge skeleton; per-vertex radius controllable in Edit Mode via Ctrl+A drag.
- **Shortcut:** O — Proportional Editing (mouse wheel adjusts falloff radius) for smooth multi-vertex tapering.
- Skin modifier options: Branch Smoothing, Mark Loose, Mark Root, Equalize Root.

### Difficulty
Beginner

### Blender Version
Not specified — Skin modifier, Merge at Center, and Proportional Editing are version-agnostic core Blender modeling tools.

### Tags
modelling, procedural, organic, beginner

---

## Related Tutorials
- [Daily Blender Tip 68 - Plant Part 2: Adding Twigs With Particles](daily-blender-tip-68---plant-part-2-adding-twigs-with-particles.md) — shares procedural, organic; that tutorial is the direct Part 2 follow-up, scattering smaller twig objects (built with this same technique) across the trunk via a Group Particle System.
