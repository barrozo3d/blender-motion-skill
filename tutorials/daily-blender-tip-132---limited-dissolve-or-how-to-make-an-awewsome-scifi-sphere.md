---
title: Daily Blender Tip 132 - Limited Dissolve (Or How To Make An Awewsome Scifi Sphere...)
source: YouTube
url: https://www.youtube.com/watch?v=HnbVAwIk0lk
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Limited Dissolve + Solidify/Bevel workflow, version-agnostic core tools"
tags: [modelling, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-132---limited-dissolve-or-how-to-make-an-awewsome-scifi-sphere/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 132 - Limited Dissolve (Or How To Make An Awewsome Scifi Sphere...)

**Source:** [YouTube](https://www.youtube.com/watch?v=HnbVAwIk0lk)
**Author:** Blender Secrets
**Duration:** 1m44s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'LIMITED DISSOLVE (OR HOW TO MAKE SCI-FI SPHERES...)'
- **CRITICAL:** Empty transcript in chapter 'choose Limited Dissolve from the options.'
- **CRITICAL:** Empty transcript in chapter 'press CTRL+i to invert the selection (faces)...'
- **CRITICAL:** Empty transcript in chapter 'Apply the modifier'
- **CRITICAL:** Total transcript only 37 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (37 chars) in 'Add a bevel modifier'

---


Frames captured — see "Captured Frames" section below.


### LIMITED DISSOLVE (OR HOW TO MAKE SCI-FI SPHERES...) [0:00]

### choose Limited Dissolve from the options. [0:10]

### press CTRL+i to invert the selection (faces)... [0:51]

### Apply the modifier [1:14]

### Add a bevel modifier [1:21]
**Transcript (timestamped):**
[1:30] VDB, Teleport Drawed Licopter Nagajaש



---

## Captured Frames

- [0:10] tutorials/frames/daily-blender-tip-132---limited-dissolve-or-how-to-make-an-awewsome-scifi-sphere/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-132---limited-dissolve-or-how-to-make-an-awewsome-scifi-sphere/frame_001.jpg
- [0:51] tutorials/frames/daily-blender-tip-132---limited-dissolve-or-how-to-make-an-awewsome-scifi-sphere/frame_002.jpg
- [1:14] tutorials/frames/daily-blender-tip-132---limited-dissolve-or-how-to-make-an-awewsome-scifi-sphere/frame_003.jpg
- [1:30] tutorials/frames/daily-blender-tip-132---limited-dissolve-or-how-to-make-an-awewsome-scifi-sphere/frame_004.jpg

---

## Structured Notes

### Core Technique
The classic "Death Star" / sci-fi greebled sphere trick: run **Limited Dissolve** on a dense subdivided sphere to randomly merge its uniform triangles/quads into an irregular jigsaw pattern of flat n-gon panels, then invert the face selection and apply a Solidify (or similar offset) modifier so alternating panels sit at a different height, finished with a Bevel modifier for defined panel edges. Note: this video's audio track is silent/near-empty; this summary is built entirely from the captured on-screen text captions and frames.

### Summary
Frame 000 shows the starting point: a densely subdivided UV sphere with uniform quad/triangle topology, a right-click context menu open with **Limited Dissolve** highlighted, captioned "...choose Limited Dissolve from the options." Frame 001 shows the Limited Dissolve operator's redo panel (Max Angle, Boundary, Delimit options: Normal/Material/Seam/Sharp/UV) with the sphere now broken into an irregular patchwork of flat, randomly-sized polygonal panels — the signature jigsaw/greeble pattern this operator produces. Frame 002 shows a closer view of that same panelized sphere with the on-screen instruction "press CTRL+i to invert the selection (faces)..." — selecting the complementary set of panels from whatever was selected during the dissolve step. Frame 003 shows the panels now offset outward/inward from each other (visible height difference between adjacent panels, giving a paneled, armor-plate look), captioned "Apply the modifier," with a Solidify-style modifier's settings (Offset, Clamp, Even Thickness, High Quality Normals, Rim) visible in the sidebar. Frame 004 shows a Bevel modifier freshly added (Amount, Segments, Limit Method, Miter, Loop Slide options visible in the sidebar) over the same paneled sphere, captioned "Add a bevel modifier" — rounding/defining the panel edges for a more finished hard-surface look.

### Key Steps
1. Start with a UV Sphere that has a reasonably dense, uniform subdivision (enough triangles/quads for the dissolve pattern to look organic/random rather than blocky).
2. In Edit Mode with all faces selected, right-click and choose **Limited Dissolve** from the context menu — this merges adjacent coplanar-ish faces together based on a Max Angle threshold, producing an irregular jigsaw pattern of flat n-gon panels instead of the sphere's original uniform grid. Delimit options (Normal, Material, Seam, Sharp, UV) can constrain which edges are allowed to merge across.
3. Select some subset of the resulting panels (e.g. every other one, or a random selection), then press **Ctrl+I** to invert the selection — isolating the complementary set of panels.
4. Apply an offset-style modifier (a Solidify modifier is implied by the visible settings — Offset, Clamp, Even Thickness, Rim) to that selected subset so those panels sit proud of or recessed from their neighbors, creating a paneled, armor-plate look. Apply the modifier once satisfied.
5. Add a **Bevel modifier** on top to round and define the edges between panels for a more finished, hard-surface sci-fi look.

### Nodes / Settings
- **Mesh Cleanup operator:** Limited Dissolve (right-click context menu; Max Angle, Delimit: Normal/Material/Seam/Sharp/UV).
- **Selection:** Ctrl+I (Invert Selection) to target the complementary panel subset.
- **Modifiers:** Solidify-style offset modifier (Offset, Clamp, Even Thickness, Rim — applied to selected panels for a height difference), Bevel modifier (Amount, Segments, Limit Method, Miter, Loop Slide).

### Difficulty
Intermediate

### Blender Version
Not specified — Limited Dissolve, Solidify, and Bevel are version-agnostic core Blender tools.

### Tags
modelling, procedural, intermediate

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover the Limited Dissolve panelized-sphere technique.
