---
title: Daily Blender Tip 96 - 2D Animation From 3D Animation (Blender 2.8)
source: YouTube
url: https://www.youtube.com/watch?v=QI5rEvu7r4I
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 2.8 (title explicitly references \"Blender 2.8\")"
tags: [grease-pencil, animation, workflow, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-96---2d-animation-from-3d-animation-blender-28/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 96 - 2D Animation From 3D Animation (Blender 2.8)

**Source:** [YouTube](https://www.youtube.com/watch?v=QI5rEvu7r4I)
**Author:** Blender Secrets
**Duration:** 1m56s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 68 chars (min 500). Captions unavailable or audio silent — extraction will be poor.

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] bit palette,
[1:35] VD-mode,
[1:49] And practicing itすこ bunch,
[1:54] Quantity Bed Speak,



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-96---2d-animation-from-3d-animation-blender-28/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-96---2d-animation-from-3d-animation-blender-28/frame_001.jpg
- [0:45] tutorials/frames/daily-blender-tip-96---2d-animation-from-3d-animation-blender-28/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-96---2d-animation-from-3d-animation-blender-28/frame_003.jpg
- [1:30] tutorials/frames/daily-blender-tip-96---2d-animation-from-3d-animation-blender-28/frame_004.jpg
- [1:50] tutorials/frames/daily-blender-tip-96---2d-animation-from-3d-animation-blender-28/frame_005.jpg

---

## Structured Notes

### Core Technique
A fast rotoscoping workflow: dragging a viewport render/playback of a rigged 3D character walk cycle directly into Blender's **2D Animation** (Grease Pencil) workspace as a background reference, then hand-drawing over it frame-by-frame with the **Draw Pencil** tool — producing a rough, hand-drawn 2D animation in a fraction of the time hand-drawing from scratch would take, since the 3D animation already solves the underlying motion/timing.

### Summary
Frame 000 shows a rough pencil-sketch outline of a walking character in the 2D Animation workspace's Draw Pencil interface, captioned "Hand-drawn animation is really beautiful, but let's face it - it takes forever to make! However..." Frame 001 shows a shaded/colored 3D character render loaded as a background reference layer in the same 2D Animation canvas, mid-walk-cycle pose, captioned "I just dragged a viewport render of a 3D character walk cycle into the 2D animation interface." Frame 002 shows the same colored 3D reference from a different walk-cycle frame. Frame 003 shows the reference again, captioned "This footage is speed up, but it only took me 5 minutes or so to draw all the frames for the walk cycle" — confirming the actual drawing pass over the reference was very fast. Frame 004 shows the Draw Pencil toolbar's mode dropdown (Draw/Edit Mode/Sculpt Mode/Weight Paint) with **Object Mode** highlighted, the camera selected, captioned "Switch from Draw mode to Object mode and select the camera. Turn off the background" — hiding the 3D reference footage once the tracing is complete. Frame 005 shows the final result: a rough black-line hand-drawn walk-cycle sketch with the 3D reference now hidden, captioned "Sweet! I personally really love the rough handdrawn look. I really did this very quickly and roughly."

### Key Steps
1. Have a finished 3D character walk-cycle animation ready (e.g. the Rigify walk cycle from the character rigging series).
2. Open a **2D Animation** workspace (Grease Pencil) and drag/import a rendered playback of the 3D walk cycle in as a background reference (via a Movie Clip / Image Sequence background, or a rendered viewport clip dropped into the canvas).
3. Using the **Draw Pencil** tool, hand-draw over the 3D reference frame-by-frame, tracing the character's silhouette/pose loosely rather than precisely — the goal is a fast, rough hand-drawn look, not exact tracing.
4. Repeat across the walk cycle's frame range; because the underlying motion/timing is already solved by the 3D animation, this drastically speeds up drawing compared to animating from scratch.
5. Once drawing is complete, switch from **Draw Mode** to **Object Mode**, select the background reference/camera object, and hide/disable the background footage — leaving just the finished hand-drawn Grease Pencil animation.

### Nodes / Settings
- **Workspace:** 2D Animation (Grease Pencil).
- **Background reference:** a rendered/viewport playback of a 3D walk cycle, imported as a background clip in the 2D Animation canvas.
- **Tool:** Draw Pencil (Grease Pencil drawing tool), Object Mode toggle for managing the background reference visibility.

### Difficulty
Intermediate

### Blender Version
Blender 2.8 (title explicitly references "Blender 2.8" — 2D Animation/Grease Pencil workspace consistent with the 2.8x redesign that introduced GPencil as a first-class object type).

### Tags
grease-pencil, animation, workflow, intermediate

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover rotoscoping a 3D animation into Grease Pencil 2D drawing.
