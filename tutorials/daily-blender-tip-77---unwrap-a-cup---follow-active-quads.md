---
title: Daily Blender Tip 77 - Unwrap a Cup - Follow Active Quads
source: YouTube
url: https://www.youtube.com/watch?v=ScRIlkmNTfw
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Mark Seam, Align Auto, and Follow Active Quads are version-agnostic core Blender UV tools"
tags: [uv, modelling, workflow, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-77---unwrap-a-cup---follow-active-quads/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 77 - Unwrap a Cup - Follow Active Quads

**Source:** [YouTube](https://www.youtube.com/watch?v=ScRIlkmNTfw)
**Author:** Blender Secrets
**Duration:** 1m38s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 9 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (9 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] Make pole



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-77---unwrap-a-cup---follow-active-quads/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-77---unwrap-a-cup---follow-active-quads/frame_001.jpg
- [0:45] tutorials/frames/daily-blender-tip-77---unwrap-a-cup---follow-active-quads/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-77---unwrap-a-cup---follow-active-quads/frame_003.jpg
- [1:25] tutorials/frames/daily-blender-tip-77---unwrap-a-cup---follow-active-quads/frame_004.jpg
- [1:35] tutorials/frames/daily-blender-tip-77---unwrap-a-cup---follow-active-quads/frame_005.jpg

---

## Structured Notes

### Core Technique
UV unwrapping a cylindrical cup mesh cleanly by manually marking seams (thinking of the mesh "as if it were cut open like paper"), then using **UV > Follow Active Quads** (via one square-looking face and its two adjacent vertices, W > Align Auto) to force the whole ring of side faces to unwrap into a perfectly even, undistorted grid instead of a warped/uneven default unwrap.

### Summary
Frame 000 shows a cup-shaped model (a cylindrical mug with a handle) in Edit Mode with edges highlighted red as marked seams, captioned "...or how to unwrap a complex cylindrical object. Select edges to mark as seams." Frame 001 shows the cup from a front-orthographic angle with a vertical seam line running down one side, captioned "This is a matter of experience... try to think about as if you are cutting an object made of paper" — choosing seam placement as if physically unfolding the 3D shape flat. Frame 002 shows the UV Editor split-screen: the 3D mesh on the left and a rough/uneven initial UV unwrap on the right, captioned "Choose a face that looks square already, select two vertices and press 'w' > Align Auto." Frame 003 shows a cleaner UV layout after Follow Active Quads, the side-wall faces now forming an even, grid-aligned checkerboard-style UV map. Frame 004 shows the final even grid UV layout with the cup model beside it, captioned "Now any texture you use on the cup will not be warped incorrectly." Frame 005 is the closing Mandala Motion channel card.

### Key Steps
1. Enter Edit Mode on the cylindrical cup mesh and select edges to **Mark Seam** — thinking of the shape as if it were made of paper and being physically cut open/unfolded flat, choosing natural, hidden edges (e.g. along the handle, top/bottom rim) for seam placement.
2. Select all faces and do a normal **Unwrap (U)** first — on a cylindrical object this often produces an uneven, distorted UV grid where side-wall face sizes don't match.
3. To fix distortion: select one face on the side wall that already looks reasonably square, then select **two vertices** on that face and press **W > Align Auto** — this straightens/normalizes the reference geometry Follow Active Quads will propagate from.
4. Run **UV > Follow Active Quads** — this uses the active/aligned face as a template and propagates a perfectly even grid unwrap across the entire connected quad strip (the whole cylindrical wall).
5. Result: a clean, evenly-spaced UV grid where any applied texture (labels, patterns) maps without stretching or warping around the cup's circumference.

### Nodes / Settings
- **Shortcut:** Ctrl+E > Mark Seam (or Edge menu).
- **Shortcut:** U > Unwrap — initial unwrap pass.
- **Shortcut:** W > Align Auto — straightens two selected vertices for a clean reference face.
- **UV menu:** Follow Active Quads — propagates an even grid unwrap from the active face across a connected quad mesh (ideal for cylindrical/tube shapes).

### Difficulty
Intermediate

### Blender Version
Not specified — Mark Seam, Align Auto, and Follow Active Quads are version-agnostic core Blender UV tools.

### Tags
uv, modelling, workflow, intermediate

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover Follow Active Quads or manual seam-marking specifically.
