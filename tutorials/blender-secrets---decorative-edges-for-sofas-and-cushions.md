---
title: Blender Secrets - Decorative Edges for Sofas and Cushions
source: YouTube
url: https://www.youtube.com/watch?v=8D8F0BpeZvQ
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (core mesh/curve workflow, 3.x-5.x)"
tags: [modelling, materials, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---decorative-edges-for-sofas-and-cushions/
frame_count: 4
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - Decorative Edges for Sofas and Cushions

**Source:** [YouTube](https://www.youtube.com/watch?v=8D8F0BpeZvQ)
**Author:** Blender Secrets
**Duration:** 1m31s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- WARNING: Thin transcript: 1109 chars. Notes may be shallow — consider --whisper-model small.

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In Edit Mode select the edges where you want to add decorative edges.
[0:08] Duplicate the selection and separate it to a new object.
[0:11] With only the new object selected, go to Object, Convert, Curve.
[0:16] Give the curve some depth and enable Shade Smooth.
[0:21] If the object has more complicated geometry like a 3D scanned sofa, it's a little different.
[0:26] Turn on snapping to face and project individual elements.
[0:32] Select Duplicate and separate one vertex.
[0:35] Extrude it to create the edge by pressing E or holding CTRL and right clicking.
[0:44] Convert it to a curve and give it depth as explained before.
[0:48] If you want rounder corners, set the fight some vertices and smooth them a few times.
[0:58] If you like this tip, you'll also like the Blender Secrets eBook.
[1:02] With more than a thousand pages and more on the way.
[1:05] By clicking on a topic in the index, you're transported to the relevant pages.
[1:11] And clicking on the link at the bottom of the page takes you back to the index of 400
[1:15] plus topics.
[1:17] To see the corresponding video on a topic, simply click on the topic title.
[1:22] Updates are always free for customers both on Gumroad and Blender Market.



---

## Captured Frames

- [0:10] tutorials/frames/blender-secrets---decorative-edges-for-sofas-and-cushions/frame_000.jpg
- [0:18] tutorials/frames/blender-secrets---decorative-edges-for-sofas-and-cushions/frame_001.jpg
- [0:30] tutorials/frames/blender-secrets---decorative-edges-for-sofas-and-cushions/frame_002.jpg
- [0:45] tutorials/frames/blender-secrets---decorative-edges-for-sofas-and-cushions/frame_003.jpg

---

## Structured Notes

### Core Technique
Curve-based decorative piping/edging for upholstered furniture (sofa seams, cushion edges) — the same technique covered in more depth in this channel's "5 mins of ArchViz Tips" video, presented here as a standalone short tip with clearer on-screen captions confirming each step.

### Summary
A very short (1m31s), caption-heavy tip video using a sofa-cushion model as the example. Frame 000 shows the core first step: after duplicating a selected edge loop, the Separate menu (P) open with "Selection" highlighted by an arrow, on a dense quad-topology cushion mesh. Frame 001 shows the follow-up: the Object right-click context menu with "Shade Smooth" highlighted, alongside the Curve's Bevel settings sidebar (Round profile, Depth 0.0015m, Resolution 4) — confirming the curve-conversion + bevel-depth step. Frame 002 shows the harder case: a dense, irregular triangulated mesh (a photoscanned-looking cushion/sofa) with the on-screen caption "Turn on Snapping to Face and Project Individual Elements" — this is the vertex-by-vertex method for edging complex/scanned geometry that doesn't have a clean edge loop to duplicate. Frame 003 shows the finished result: a smooth, rounded-corner piping seam wrapped around a soft cushion, captioned "Convert it to a Curve and give it Depth, as explained before."

### Key Steps
1. **Simple geometry (clean edge loops):** in Edit Mode, select the edge(s) where a decorative seam/piping should go; duplicate and Separate (P → Selection) into a new object; with only that new object selected, Object → Convert → Curve; give the curve some Bevel Depth and enable Shade Smooth for a rounded piping profile.
2. **Complex/scanned geometry (no clean edge loop):** enable Snapping to Face and "Project Individual Elements"; select, duplicate, and separate a single vertex; extrude it along the desired seam path by pressing E repeatedly, or by holding Ctrl and right-clicking to place each new point snapped to the surface; convert the resulting vertex chain to a Curve and give it Bevel Depth as in step 1.
3. **Rounder corners:** where the piping path turns a corner, subdivide a few extra vertices there and run Smooth Vertices a couple of times to avoid a hard angular kink in the finished curve.

### Nodes / Settings
- **Object conversion:** Object → Convert → Curve (turns a duplicated edge/vertex chain into a beveled piping profile).
- **Curve settings:** Bevel (Round profile, Depth, Resolution, Fill Caps).
- **Snapping:** Snap to Face + Project Individual Elements (for building an edge path on complex/scanned geometry vertex by vertex).
- **Edit-mode operators:** P → Separate (Selection), E (extrude), Ctrl+RMB (snapped vertex placement), Smooth Vertices.

### Difficulty
Intermediate

### Blender Version
Not specified — core mesh/curve workflow, version-agnostic across modern Blender (3.x-5.x).

### Tags
modelling, materials, procedural, intermediate

---

## Related Tutorials
- [Blender Secrets - 5 mins of ArchViz Tips (Diamond Tufting, Pillow Edges, Pillows, Interactive Cloth)](blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in.md) — shares cloth, materials, procedural, intermediate; **this is the same technique** covered in more depth as part of a larger ArchViz tips compilation from the same channel — treat that video as the primary/fuller reference and this one as a focused standalone excerpt.
