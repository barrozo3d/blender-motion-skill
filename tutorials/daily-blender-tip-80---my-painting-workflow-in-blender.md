---
title: Daily Blender Tip 80 - My Painting Workflow In Blender
source: YouTube
url: https://www.youtube.com/watch?v=Z7JCMVygWoA
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Texture Paint mode, Sample Color (S), brush radius resize (F), and Save As Image are version-agnostic core Blender features"
tags: [texture-painting, materials, workflow, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-80---my-painting-workflow-in-blender/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 80 - My Painting Workflow In Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=Z7JCMVygWoA)
**Author:** Blender Secrets
**Duration:** 1m37s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 36 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (36 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] Down下留掉,
[1:44] SOLID retract your carrier,



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-80---my-painting-workflow-in-blender/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-80---my-painting-workflow-in-blender/frame_001.jpg
- [0:45] tutorials/frames/daily-blender-tip-80---my-painting-workflow-in-blender/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-80---my-painting-workflow-in-blender/frame_003.jpg
- [1:25] tutorials/frames/daily-blender-tip-80---my-painting-workflow-in-blender/frame_004.jpg
- [1:35] tutorials/frames/daily-blender-tip-80---my-painting-workflow-in-blender/frame_005.jpg

---

## Structured Notes

### Core Technique
A practical hand-painting workflow inside Blender's **Texture Paint** mode using mostly the custom sharp brush built in [Tip 79](daily-blender-tip-79---texture-painting-and-custom-brushes.md), plus three key shortcuts — **S** (Sample/Color Picker, to pull colors directly from the painting), **F** (interactive brush radius resize), and **F3 / Image > Save As Image** (to export the finished texture) — for a fast, flat-color landscape-painting demo.

### Summary
Frame 000 shows a blank black canvas in Texture Paint mode, captioned "First off, use the Fill brush to give the texture some overall color." Frame 001 shows the Brush Curve panel (Line, Vector Handle, Auto Handle options) with a soft blue-gray blob painted, captioned "I really ever only use a sharp brush, like the one I show how to make in tip 79. Here I make it again." — confirming the exact same custom brush technique from Tip 79 is the primary tool used. Frame 002 shows a landscape scene taking shape (blue sky, green rolling hills) with the color wheel open, captioned "The keyboard shortcut for the color picker is 's'. Just pick values directly from the painting" — sampling existing painted colors instead of re-selecting from the color wheel each time. Frame 003 shows a more detailed sky with soft cloud shapes, captioned "To change the brush radius I use the 'f' key. Press 'f' and drag to in- or decrease the brush size." Frame 004 shows the finished landscape painting (green hills, blue sky, soft clouds) in the UV/Image Editor, captioned "In the UV/Image editor display the texture and press F3 or Image> Save As Image. Don't forget..." Frame 005 is the closing card.

### Key Steps
1. Use the **Fill** brush first to lay down a base/overall color across the whole texture before detail painting.
2. Rely primarily on a custom **sharp brush** (built via the Curve > Line > Vector Handle technique from Tip 79) for most of the painting work.
3. Use **S** (the Sample/Color Picker shortcut) to pick colors directly from already-painted areas of the texture, rather than repeatedly reopening the color wheel — keeps the palette consistent and speeds up painting.
4. Use **F**, then drag the mouse, to interactively resize the brush radius on the fly without leaving the canvas.
5. Once finished, switch to the **UV/Image Editor**, display the painted texture, and press **F3** (or **Image > Save As Image**) to export the finished texture file to disk.

### Nodes / Settings
- **Brush:** Fill (base color), custom sharp brush from Tip 79 (Curve > Line > Vector Handle).
- **Shortcut:** S — Sample/Color Picker (pick color from the canvas).
- **Shortcut:** F — interactive brush radius resize.
- **Shortcut:** F3, or UV/Image Editor > Image > Save As Image — export the finished texture.

### Difficulty
Beginner

### Blender Version
Not specified — Texture Paint mode, Sample Color (S), brush radius resize (F), and Save As Image are version-agnostic core Blender features.

### Tags
texture-painting, materials, workflow, beginner

---

## Related Tutorials
- [Daily Blender Tip 79 - Texture Painting and Custom Brushes](daily-blender-tip-79---texture-painting-and-custom-brushes.md) — shares texture-painting, materials, workflow; this tutorial explicitly reuses the exact sharp-brush Curve technique taught there as its primary painting tool.
