---
title: Daily Blender Tip 133 - Cast Modifier (Or How To Make Another Weird Sphere...)
source: YouTube
url: https://www.youtube.com/watch?v=yEDi5SIqXxs
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Cast modifier + Solidify/Subdivision workflow, version-agnostic core tools"
tags: [modelling, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-133---cast-modifier-or-how-to-make-another-weird-sphere/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 133 - Cast Modifier (Or How To Make Another Weird Sphere...)

**Source:** [YouTube](https://www.youtube.com/watch?v=yEDi5SIqXxs)
**Author:** Blender Secrets
**Duration:** 1m46s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'CAST MODIFIER (OR HOW TO MAKE ANOTHER WEIRD SPHERE..)'
- **CRITICAL:** Empty transcript in chapter 'In Edit Mode subdivide a cube a few times...'
- **CRITICAL:** Empty transcript in chapter 'Select an interesting pattern of faces...'
- **CRITICAL:** Empty transcript in chapter 'Invert the selection and delete the other faces.'
- **CRITICAL:** Empty transcript in chapter 'Add a Cast modifier, set it to Sphere and factor 1.'
- **CRITICAL:** Empty transcript in chapter 'Add a Solidify and Subdiv modifier to add thickness.'
- **CRITICAL:** Total transcript only 22 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (7 chars) in 'Add a second sphere and scale it up...'
- WARNING: Very short transcript (15 chars) in 'Change the modifier order for a different look.'

---


Frames captured — see "Captured Frames" section below.


### CAST MODIFIER (OR HOW TO MAKE ANOTHER WEIRD SPHERE..) [0:00]

### In Edit Mode subdivide a cube a few times... [0:07]

### Select an interesting pattern of faces... [0:15]

### Invert the selection and delete the other faces. [0:43]

### Add a Cast modifier, set it to Sphere and factor 1. [0:56]

### Add a Solidify and Subdiv modifier to add thickness. [1:04]

### Add a second sphere and scale it up... [1:16]
**Transcript (timestamped):**
[1:30] ...
[1:32] ...


### Change the modifier order for a different look. [1:33]
**Transcript (timestamped):**
[1:35] ...
[1:40] ...
[1:45] ...
[1:52] ...



---

## Captured Frames

- [0:07] tutorials/frames/daily-blender-tip-133---cast-modifier-or-how-to-make-another-weird-sphere/frame_000.jpg
- [0:20] tutorials/frames/daily-blender-tip-133---cast-modifier-or-how-to-make-another-weird-sphere/frame_001.jpg
- [0:43] tutorials/frames/daily-blender-tip-133---cast-modifier-or-how-to-make-another-weird-sphere/frame_002.jpg
- [0:56] tutorials/frames/daily-blender-tip-133---cast-modifier-or-how-to-make-another-weird-sphere/frame_003.jpg
- [1:10] tutorials/frames/daily-blender-tip-133---cast-modifier-or-how-to-make-another-weird-sphere/frame_004.jpg
- [1:30] tutorials/frames/daily-blender-tip-133---cast-modifier-or-how-to-make-another-weird-sphere/frame_005.jpg

---

## Structured Notes

### Core Technique
A companion sci-fi-sphere trick to the Limited Dissolve technique: instead of dissolving faces into random panels, a subdivided cube has a deliberate maze-like pattern of faces selected and kept (the rest deleted), then a **Cast modifier** (Sphere type, Factor 1) bends the resulting open lattice into a spherical shape, with Solidify + Subdivision modifiers adding thickness and smoothness — producing an ornate, cage-like metallic sphere. Note: this video's audio track is silent/near-empty; this summary is built entirely from the captured on-screen text captions and frames.

### Summary
Frame 000 shows the starting shape: a plain default cube, captioned "In Edit Mode subdivide a cube a few times..." Frame 001 shows the cube after heavy subdivision, its faces now covered in a fine repeating diamond/cross ornamental pattern (visible as a texture-like grid across all faces), captioned "Select an interesting pattern of faces..." Frame 002 shows the payoff of the selection step: the cube's faces reduced to just an interlocking maze/key-pattern of remaining faces (dark gaps where faces were deleted), captioned "Invert the selection and delete the other faces." Frame 003 shows the same maze-patterned cube now curved into a rounded, ball-like shape via a Cast modifier (Modifier panel: Cast Type Sphere, Factor 0.50 mid-adjustment, Radius, Size, From Radius, Vertex Group/Control Object fields visible), captioned "Add a Cast modifier, set it to Sphere and factor 1." Frame 004 shows the shape after Solidify and Subdivision modifiers are added (Particle Instance/Particle System/Smoke/Soft Body/Face Deform/Cloth modifier-add search list visible mid-search), now a smooth, golden, 3D maze-pattern lattice ball with real thickness and rounded edges. Frame 005 shows the polished final result: a golden ornamental spherical lattice with a raised jigsaw/maze surface pattern, rendered under studio-style lighting.

### Key Steps
1. In Edit Mode, subdivide a default cube several times to get enough face density for an interesting pattern.
2. Select an "interesting pattern" of faces across the subdivided cube's surface — e.g. a repeating maze, key, or diamond-like pattern — leaving gaps between selected regions.
3. Invert the selection (so the previously-unselected faces are now selected) and delete those faces, leaving only the chosen pattern of faces as an open, lattice-like mesh.
4. Add a **Cast** modifier, set its Cast Type to **Sphere** and Factor to **1** — this bends/projects the flat, patterned cube faces onto a spherical shape while preserving the maze-like gaps as openings in the surface.
5. Add a **Solidify** modifier (for real thickness on the thin lattice pattern) and a **Subdivision Surface** modifier (for smoothing) to turn the flat patterned shell into a rounded, dimensional lattice ball.
6. Variation: add a second sphere and scale it up (implied to sit either inside or around the lattice shell, e.g. as a visible "core" glimpsed through the gaps, or as a bounding shape) — the exact placement isn't detailed on-screen.
7. Variation: changing the order of the modifiers in the stack (e.g. Solidify before vs. after Cast, or Subdivision before vs. after Cast) produces a noticeably different final look, encouraging experimentation.

### Nodes / Settings
- **Modeling:** Cube subdivision (Edit Mode), face pattern selection, Invert Selection + Delete (pattern-cutting technique).
- **Modifiers:** Cast (Cast Type: Sphere, Factor, Radius, Size, From Radius, optional Vertex Group/Control Object), Solidify (thickness), Subdivision Surface (smoothing) — modifier stack order is explicitly called out as affecting the final look.
- **Variation:** a second, scaled-up sphere object added alongside the lattice shell.

### Difficulty
Intermediate

### Blender Version
Not specified — Cast, Solidify, and Subdivision Surface are version-agnostic core Blender modifiers.

### Tags
modelling, procedural, intermediate

---

## Related Tutorials
- [Daily Blender Tip 132 - Limited Dissolve (Or How To Make An Awewsome Scifi Sphere...)](daily-blender-tip-132---limited-dissolve-or-how-to-make-an-awewsome-scifi-sphere.md) — shares modelling, procedural, intermediate; a direct companion "weird sphere" trick from the same channel, using deliberate pattern-face-deletion + a Cast modifier instead of Limited Dissolve's randomized panel pattern.
