---
title: Daily Blender Tip 47 - Custom Transform Orientation
source: YouTube
url: https://www.youtube.com/watch?v=dQZ2RwpvFtM
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Custom Transform Orientation (Ctrl+Alt+Space), version-agnostic core shortcut"
tags: [modelling, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-47---custom-transform-orientation/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 47 - Custom Transform Orientation

**Source:** [YouTube](https://www.youtube.com/watch?v=dQZ2RwpvFtM)
**Author:** Blender Secrets
**Duration:** 1m38s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 5 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (5 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] liber



---

## Captured Frames

- [0:10] tutorials/frames/daily-blender-tip-47---custom-transform-orientation/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-47---custom-transform-orientation/frame_001.jpg
- [0:50] tutorials/frames/daily-blender-tip-47---custom-transform-orientation/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-47---custom-transform-orientation/frame_003.jpg
- [1:20] tutorials/frames/daily-blender-tip-47---custom-transform-orientation/frame_004.jpg
- [1:32] tutorials/frames/daily-blender-tip-47---custom-transform-orientation/frame_005.jpg

---

## Structured Notes

### Core Technique
Creating a **Custom Transform Orientation** from a selected face (or edge/vertex normal) with **Ctrl+Alt+Space**, so subsequent Move/Rotate/Scale operations can be constrained to that specific face's local axes — extremely useful for transforming geometry along an angled face that doesn't align with any of the standard Global/Local/Normal orientations.

### Summary
Frame 000 shows the setup: a plain default cube, captioned "Custom Transform Orientation." Frame 001 shows one angled face of the cube selected (highlighted blue with a red/green/blue axis gizmo aligned to that face), captioned "Press CTRL+ALT+SPACE to create a 'custom transform orientation'. This allows movement along that face." Frame 002 shows the same selected face from a slightly different angle, the gizmo's axes clearly aligned to the face's own plane rather than the world's global axes. Frame 003 shows a highlighted rectangular sub-region of that face with the axis gizmo still following the face's custom orientation, demonstrating that transforms are now constrained to move within/along that exact plane. Frame 004 shows the Transform Orientation dropdown menu open (bottom-left toolbar) listing several saved custom orientations (Face.004, Face.003, Face.002, Face.001, Face) plus the standard Global, Normal, Gimbal, and others, one custom entry highlighted, captioned "You will be able to select this new custom orientation from the same menu as the other orientations." Frame 005 shows the same dropdown with a different custom Face orientation entry highlighted near the bottom, reinforcing that each captured orientation persists in the list for later reuse.

### Key Steps
1. Select a face (or edge/vertex) whose orientation you want to use as a custom reference — e.g. one of a cube's angled faces.
2. Press **Ctrl+Alt+Space** to create a **Custom Transform Orientation** based on that selection's normal/local axes.
3. With this orientation active, Move/Rotate/Scale operations are now constrained to that face's own local axes instead of Global, Local, or Normal — letting you slide geometry precisely along an angled surface.
4. Each custom orientation created this way is saved and named automatically (e.g. "Face," "Face.001," "Face.002" for successive captures) and remains available afterward in the **Transform Orientation** dropdown in the header/toolbar, alongside the built-in Global, Local, Normal, Gimbal, and View orientations — so a previously-captured custom orientation can be reselected anytime without recreating it.

### Nodes / Settings
- **Shortcut:** Ctrl+Alt+Space (Create Custom Transform Orientation from the current selection).
- **Transform Orientation dropdown:** lists all saved custom orientations (auto-named Face, Face.001, etc.) alongside Global, Local, Normal, Gimbal, View.

### Difficulty
Beginner

### Blender Version
Not specified — Custom Transform Orientation (Ctrl+Alt+Space) is a version-agnostic core Blender shortcut.

### Tags
modelling, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover Custom Transform Orientations specifically.
