---
title: Daily Blender Tip 59 - Crease Edges
source: YouTube
url: https://www.youtube.com/watch?v=4YF1p_odCwk
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Edge Crease (Shift+E) is a version-agnostic core Blender modeling tool"
tags: [modelling, subdivision-surface, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-59---crease-edges/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 59 - Crease Edges

**Source:** [YouTube](https://www.youtube.com/watch?v=4YF1p_odCwk)
**Author:** Blender Secrets
**Duration:** 1m55s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'Full Content'
- **CRITICAL:** Total transcript only 0 chars (min 500). Captions unavailable or audio silent — extraction will be poor.

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**



---

## Captured Frames

- [0:10] tutorials/frames/daily-blender-tip-59---crease-edges/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-59---crease-edges/frame_001.jpg
- [0:50] tutorials/frames/daily-blender-tip-59---crease-edges/frame_002.jpg
- [1:10] tutorials/frames/daily-blender-tip-59---crease-edges/frame_003.jpg
- [1:30] tutorials/frames/daily-blender-tip-59---crease-edges/frame_004.jpg
- [1:50] tutorials/frames/daily-blender-tip-59---crease-edges/frame_005.jpg

---

## Structured Notes

### Core Technique
Using **Edge Crease** (Shift+E) to non-destructively sharpen selected edges on a Subdivision-Surface-smoothed mesh — pulling the subdivided surface back toward the sharp original cage edge without adding extra support-loop geometry, fully adjustable/reversible at any time.

### Summary
Frame 000 shows a smooth sphere (a subdivided cube cage visible around it), captioned "With a subdivided object like this, you can make edges sharp in a non-destructive way with the crease option." Frame 001 shows the same shape with its top rim edge now sharply creased (a flat-topped, rounded-bottom cup/bucket shape), captioned "Select the edge you want to sharpen and press SHIFT+E and then move the mouse to increase the creasing." Frame 002 shows a fully-hardened result — the shape now looks almost like an uncreased cube on top with a rounded bottom — captioned "If you just want the edge to be sharp you can also press SHIFT+E and 1. Oddly enough, to set it to zero, press SHIFT+E and -1." Frames 003–004 show further creased variants (a rounded box with a creased notch/groove, then a house-like creased shape) demonstrating creasing combined on multiple edges to build sharper architectural forms out of a subdivided mesh. Frame 005 is the closing card ("Check out the IG channel as well: Instagram.com/mandalamotion — Thanks for watching!").

### Key Steps
1. Start with a mesh that has a **Subdivision Surface** modifier applied (or a subdivided cage) so its faces are smoothly rounded.
2. Select the edge(s) whose surrounding surface should read as sharp instead of rounded.
3. Press **Shift+E** and move the mouse to interactively dial in the crease weight (0 = fully smooth/rounded, 1 = fully sharp) — increases the subdivision "pull" toward that edge's original position.
4. For a fully sharp edge instantly, press **Shift+E** then type **1** (sets crease to maximum, 1.0).
5. To reset an edge back to fully smooth, press **Shift+E** then type **-1** (an intentionally counter-intuitive shortcut — typing -1 zeroes out the crease rather than going negative).
6. Because crease is a per-edge modifier-driving attribute (not manually-added geometry), it's fully non-destructive — adjustable, reversible, and stacks cleanly across multiple edges to sculpt sharp/rounded transitions on an otherwise smooth subdivided mesh.

### Nodes / Settings
- **Shortcut:** Shift+E — interactive Edge Crease; type a numeric value (1 = max sharp, -1 = reset to zero) for precise control.
- Works in conjunction with a **Subdivision Surface** modifier on the mesh.

### Difficulty
Beginner

### Blender Version
Not specified — Edge Crease (Shift+E) is a version-agnostic core Blender modeling tool.

### Tags
modelling, subdivision-surface, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover Edge Crease specifically.
- [NS Rock Sculptor Guide - Edge Crease](ns-rock-sculptor-guide---edge-crease.md) — applies this exact native Shift+E crease mechanism inside the NS Rock Sculptor add-on's own weighted panel (weight field + Apply Crease button), plus a manual vertex-nudge fallback for corners the crease/remesh combo can't reach cleanly.
