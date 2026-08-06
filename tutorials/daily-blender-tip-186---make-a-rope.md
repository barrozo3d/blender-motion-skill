---
title: Daily Blender Tip 186 - Make a rope
source: YouTube
url: https://www.youtube.com/watch?v=v6WFoVV3IhY
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Screw + Curve + Array modifier workflow, version-agnostic core tools"
tags: [modelling, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-186---make-a-rope/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 186 - Make a rope

**Source:** [YouTube](https://www.youtube.com/watch?v=v6WFoVV3IhY)
**Author:** Blender Secrets
**Duration:** 1m53s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter '<Untitled Chapter 1>'
- **CRITICAL:** Empty transcript in chapter 'Delete inner verts, merge where needed (alt+m)'
- **CRITICAL:** Empty transcript in chapter 'Add a screw modifier, set a screw value, like 10 m.'
- **CRITICAL:** Empty transcript in chapter 'Alt+C, turn the circle to a curve. Add curve modifier'
- **CRITICAL:** Total transcript only 5 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (5 chars) in 'Check "merge". Choose correct deformation axis.'

---


Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]

### Delete inner verts, merge where needed (alt+m) [0:13]

### Add a screw modifier, set a screw value, like 10 m. [0:38]

### Alt+C, turn the circle to a curve. Add curve modifier [1:09]

### Check "merge". Choose correct deformation axis. [1:27]
**Transcript (timestamped):**
[1:30] Studs



---

## Captured Frames

- [0:05] tutorials/frames/daily-blender-tip-186---make-a-rope/frame_000.jpg
- [0:20] tutorials/frames/daily-blender-tip-186---make-a-rope/frame_001.jpg
- [0:38] tutorials/frames/daily-blender-tip-186---make-a-rope/frame_002.jpg
- [1:00] tutorials/frames/daily-blender-tip-186---make-a-rope/frame_003.jpg
- [1:18] tutorials/frames/daily-blender-tip-186---make-a-rope/frame_004.jpg
- [1:40] tutorials/frames/daily-blender-tip-186---make-a-rope/frame_005.jpg

---

## Structured Notes

### Core Technique
A procedural rope: two overlapping circles are merged into a cloverleaf-like profile shape, which the **Screw** modifier twists into a helical, braided-looking rope strand; the strand is then bent along a target path with a **Curve** modifier and repeated/extended with an **Array** modifier to build a longer coiled rope.

### Summary
Frame 000 shows the starting profile: a single Bezier/mesh Circle in the viewport, captioned "Create a circle, duplicate it with Shift+D." Frame 001 shows two overlapping circles merged into a cloverleaf/figure-eight-like outline (their inner intersecting vertices deleted and remaining ones merged), captioned "Delete inner verts, merge where needed (alt+m)." Frame 002 shows the same cloverleaf profile with a Screw modifier applied, its gizmo visible at the origin, captioned "Add a screw modifier, set a screw value, like 10 m" — the modifier about to twist the flat profile into a 3D helix. Frame 003 shows the resulting twisted, organic-looking braided rope strand (a tall, gnarled spiral column) next to the original flat circle reference, captioned "Add a circle, scale it and randomize/smooth it" — a bevel/profile circle used to add irregular, rope-like thickness variation to the strand. Frame 004 shows an Array modifier's settings (Object/Vertex Group, Deformation Axis, Fit Type: Fixed Count, Count, Relative Offset, Merge, Object Offset) applied to the rope object, captioned "...to the rope object. Add an array modifier as well." Frame 005 shows the finished coiled rope: a long, looped circular coil of rope resting flat, the Array modifier's Count raised to 21 and Merge/First Last/Object Offset options visible, captioned "Scale the rope, increase the array count."

### Key Steps
1. Create a Circle, duplicate it with Shift+D and offset the copy so the two circles overlap.
2. Delete the inner/intersecting vertices where the two circles overlap and merge (Alt+M) the remaining vertices where needed — producing a cloverleaf/figure-eight-like closed profile shape instead of a plain circle.
3. Add a **Screw** modifier to this profile and set a Screw (height/travel) value — e.g. 10m — twisting the flat cloverleaf profile into a tall, helical, rope-like 3D strand as it screws upward.
4. Add a second Circle, scale it down, and use it (with some randomization/smoothing) to vary the rope strand's cross-sectional thickness along its length for a more natural, less mechanically-uniform look.
5. Convert the target path to a curve with **Alt+C** (Convert to Curve), then add a **Curve** modifier to the rope object referencing that curve — bending the straight rope strand to follow any custom path shape.
6. In the Curve modifier, check **Merge** and choose the correct Deformation Axis so the rope bends along the path correctly without twisting incorrectly.
7. Add an **Array** modifier to extend/repeat the rope segment along its length (Fixed Count, adjustable Count, Relative Offset, Merge, Object Offset) — scale the whole rope and increase the Array Count to build up a longer coiled rope, such as the looped circular coil shown in the final result.

### Nodes / Settings
- **Modeling:** Circle duplication (Shift+D), Delete inner vertices, Merge (Alt+M) — building a cloverleaf profile shape.
- **Modifiers:** Screw (Screw/height value, twists a 2D profile into a 3D helix), Curve (Deformation Axis, Merge option — bends the strand along a target curve), Array (Fit Type: Fixed Count, Count, Relative Offset, Merge, Object Offset — extends/repeats the rope).
- **Curve conversion:** Alt+C (Convert mesh/circle to Curve, used as the Curve modifier's target path).

### Difficulty
Intermediate

### Blender Version
Not specified — Screw, Curve, and Array modifiers are version-agnostic core Blender tools.

### Tags
modelling, procedural, intermediate

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover the Screw-modifier rope technique.
