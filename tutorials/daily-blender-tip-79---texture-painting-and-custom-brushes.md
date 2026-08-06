---
title: Daily Blender Tip 79 - Texture Painting and Custom Brushes
source: YouTube
url: https://www.youtube.com/watch?v=u1h3_0aOBe4
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Texture Paint mode and Brush Curve falloff editing are version-agnostic core Blender features"
tags: [texture-painting, materials, workflow, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-79---texture-painting-and-custom-brushes/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 79 - Texture Painting and Custom Brushes

**Source:** [YouTube](https://www.youtube.com/watch?v=u1h3_0aOBe4)
**Author:** Blender Secrets
**Duration:** 2m1s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 23 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (23 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[2:00] Así es, Laren YouTubers



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-79---texture-painting-and-custom-brushes/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-79---texture-painting-and-custom-brushes/frame_001.jpg
- [0:45] tutorials/frames/daily-blender-tip-79---texture-painting-and-custom-brushes/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-79---texture-painting-and-custom-brushes/frame_003.jpg
- [1:30] tutorials/frames/daily-blender-tip-79---texture-painting-and-custom-brushes/frame_004.jpg
- [1:55] tutorials/frames/daily-blender-tip-79---texture-painting-and-custom-brushes/frame_005.jpg

---

## Structured Notes

### Core Technique
Painting directly on a UV-unwrapped object's texture in **Texture Paint** mode, then creating custom brushes by editing a brush's **Curve** falloff (switching to "Line" type and adding a vector point set to "Vector Handle") to produce distinct hard-edged vs. soft-edged brush presets, saved as separate named brushes ("sharp brush," "soft brush").

### Summary
Frame 000 shows a plain cube alongside a blank checkerboard UV grid, captioned "To paint textures directly onto an object, go to Texture Paint mode. It needs to be uv-unwrapped." Frame 001 shows the Texture Paint workspace with a brush picker (soft circular brush icon) and color wheel on the left, a black cube canvas in the middle, captioned "Pick a color and start painting." Frame 002 shows white blob-shaped paint strokes on the cube and matching strokes on the flat UV grid on the right, with a small red-boxed dropdown, captioned "You can change the UV/image window from View to Paint and paint from there as well" — painting can happen either directly on the 3D model or on the flat 2D UV/texture view. Frame 003 shows the Brush Curve settings panel with **Curve** type set to **Line**, a point added on the line and a highlighted "Curve" handle-type row, captioned "For the curve, click on the 'line' type and then add a vector by clicking on the line. Set it to 'vector handle'." — this produces a hard-edged brush falloff (sharp cross-shaped strokes visible on the UV texture). Frame 004 shows the brush list with a new duplicated brush entry, a soft pink circular stroke on the cube, captioned "Make another copy of this one and call it 'soft brush'. (I should have called the other one 'sharp brush')." Frame 005 shows both brush results combined (a soft blue/pink blended blob plus the earlier sharp cross shape), captioned "These are two useful brushes for texture painting. Have fun! For more playback control check my Youtube."

### Key Steps
1. Ensure the object is **UV Unwrapped**, then switch to **Texture Paint** mode.
2. Pick a color from the color wheel and paint directly on the 3D model's surface — strokes appear both on the model and on its corresponding UV texture.
3. Alternatively, switch the UV/Image Editor from **View** to **Paint** mode to paint directly on the flat 2D texture/UV layout instead of the 3D model.
4. To create a custom hard-edged brush: open the brush's **Curve** settings, change the falloff **Curve type to Line**, click on the line to add a control point, and set that point's handle type to **Vector Handle** — this produces a sharp, non-smoothed brush edge.
5. Duplicate this brush to create a variant — e.g. leaving the default smooth curve for a "soft brush" and keeping the Line/Vector-Handle version as a "sharp brush" — and rename each for easy reuse.
6. Having both a sharp and soft brush preset available speeds up texture painting for different detail needs (crisp edges vs. blended/airbrushed areas).

### Nodes / Settings
- **Mode:** Texture Paint (requires UV-unwrapped mesh).
- **UV/Image Editor:** View vs. Paint mode toggle.
- **Brush > Curve:** Curve type (Line for hard edges vs. default Smooth), Vector Handle on added control points.
- Custom brushes can be duplicated and renamed (e.g. "sharp brush," "soft brush") for a reusable brush library.

### Difficulty
Beginner

### Blender Version
Not specified — Texture Paint mode and Brush Curve falloff editing are version-agnostic core Blender features.

### Tags
texture-painting, materials, workflow, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover Texture Paint mode or custom brush Curve falloff editing specifically.
