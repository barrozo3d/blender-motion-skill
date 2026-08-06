---
title: Daily Blender Tip 113 - From Sketch To Clean Lines in Grease Pencil
source: YouTube
url: https://www.youtube.com/watch?v=QO5a2rKhMtQ
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Grease Pencil layers system, introduced/matured in Blender 2.8x"
tags: [animation, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-113---from-sketch-to-clean-lines-in-grease-pencil/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 113 - From Sketch To Clean Lines in Grease Pencil

**Source:** [YouTube](https://www.youtube.com/watch?v=QO5a2rKhMtQ)
**Author:** Blender Secrets
**Duration:** 1m59s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter '<Untitled Chapter 1>'
- **CRITICAL:** Empty transcript in chapter 'Grease Pencil now has layers like Photoshop.'
- **CRITICAL:** Empty transcript in chapter 'Lower the opacity of the sketch layer.'
- **CRITICAL:** Empty transcript in chapter 'You can use Sculpt mode to smooth out or change lines.'
- **CRITICAL:** Empty transcript in chapter 'Turn off the sketch layer.'
- **CRITICAL:** Total transcript only 8 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (8 chars) in 'In Edit Mode you can select parts and duplicate them.'

---


Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]

### Grease Pencil now has layers like Photoshop. [0:11]

### Lower the opacity of the sketch layer. [0:30]

### You can use Sculpt mode to smooth out or change lines. [1:03]

### In Edit Mode you can select parts and duplicate them. [1:13]
**Transcript (timestamped):**
[1:30] jamming,


### Turn off the sketch layer. [1:36]


---

## Captured Frames

- [0:11] tutorials/frames/daily-blender-tip-113---from-sketch-to-clean-lines-in-grease-pencil/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-113---from-sketch-to-clean-lines-in-grease-pencil/frame_001.jpg
- [1:03] tutorials/frames/daily-blender-tip-113---from-sketch-to-clean-lines-in-grease-pencil/frame_002.jpg
- [1:13] tutorials/frames/daily-blender-tip-113---from-sketch-to-clean-lines-in-grease-pencil/frame_003.jpg
- [1:36] tutorials/frames/daily-blender-tip-113---from-sketch-to-clean-lines-in-grease-pencil/frame_004.jpg

---

## Structured Notes

### Core Technique
A Photoshop-style rough-sketch-to-clean-lineart workflow using Grease Pencil's layer system: a rough sketch lives on its own low-opacity layer, a new "Clean Line" layer is drawn on top by tracing over it, Sculpt Mode smooths/adjusts the resulting strokes, Edit Mode allows selecting and duplicating stroke parts (e.g. for symmetric features), and finally the sketch layer is hidden to reveal just the finished clean line art. Note: this video's audio track is silent/near-empty; this summary is built entirely from the captured on-screen text captions and frames.

### Summary
Frame 000 shows the starting point: a rough circular/cross construction sketch on a gray canvas, with the Grease Pencil Layers panel open in the sidebar (a "Sketch" layer with Blend and Opacity sliders visible), captioned "Grease Pencil now has layers like Photoshop." Frame 001 shows a much more developed rough head sketch, the Sketch layer's Opacity slider being dragged down, captioned "Lower the opacity of the sketch layer" — fading the rough layer so it reads as a faint underlay guide. Frame 002 shows a "Clean line" layer now active above the faded sketch, with cleaner, more deliberate hair/face strokes drawn on top, captioned "You can use Sculpt mode to smooth out or change lines" — refining the traced clean strokes. Frame 003 shows the clean-line portrait further along (fuller hairline, both eyes, nose, mouth defined) with the Clean Line layer selected in the Layers panel, captioned "In Edit Mode you can select parts and duplicate them" — e.g. duplicating one drawn eye/eyebrow to quickly create its mirrored counterpart rather than redrawing it. Frame 004 shows the final result: the sketch layer's visibility toggled off (eye icon disabled in the Layers panel) so only the finished, clean black line-art portrait remains visible, captioned "Turn off the sketch layer."

### Key Steps
1. Draw a rough sketch on its own Grease Pencil layer (Grease Pencil's Layers panel works much like Photoshop's — each layer has its own Opacity/Blend settings and visibility toggle).
2. Lower that sketch layer's Opacity so it reads as a faint, unobtrusive underlay guide rather than a fully-visible rough drawing.
3. Add a new layer (e.g. named "Clean line") above the sketch layer, and trace clean, deliberate strokes over the faded rough sketch.
4. Use **Sculpt Mode** on the Grease Pencil object to smooth out or reshape existing strokes on the clean-line layer without having to redraw them from scratch.
5. In **Edit Mode**, select specific stroke parts and duplicate them — useful for quickly mirroring/reusing a drawn element (e.g. one eye or eyebrow) rather than manually re-drawing its counterpart.
6. Once the clean line layer is finished, hide the sketch layer's visibility (its eye icon in the Layers panel) to reveal just the finished clean line art.

### Nodes / Settings
- **Grease Pencil Layers panel:** per-layer Opacity, Blend mode, visibility (eye icon) toggle — functions like Photoshop layers.
- **Grease Pencil Sculpt Mode:** stroke smoothing/reshaping tools.
- **Grease Pencil Edit Mode:** stroke/point selection and duplication.

### Difficulty
Beginner

### Blender Version
Not specified — the Grease Pencil layers system referenced ("like Photoshop") matured through the Blender 2.8x series.

### Tags
animation, beginner

---

## Related Tutorials
- [Daily Blender Tip 120 - NEW Curve Tool in Grease Pencil Blender 2.8](daily-blender-tip-120---new-curve-tool-in-grease-pencil-blender-28.md) — shares animation, beginner; the Curve tool covered there (editable control points, Thickness Profile) is well suited to the "clean line" tracing pass used in this workflow.
