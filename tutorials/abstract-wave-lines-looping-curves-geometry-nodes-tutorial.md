---
title: Abstract Wave Lines | Looping Curves | Geometry Nodes Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=CztCgbqaiZk
author: Artemiy Galutskiy
ingested: 2026-08-03
blender_version: "Not specified (silent video, no version indicator visible in captured frames)"
tags: [geometry-nodes, procedural, abstract, typography, motion-design]
extraction_status: complete
frames_dir: tutorials/frames/abstract-wave-lines-looping-curves-geometry-nodes-tutorial/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Abstract Wave Lines | Looping Curves | Geometry Nodes Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=CztCgbqaiZk)
**Author:** Artemiy Galutskiy
**Duration:** 12m3s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report — Reviewed

_Reviewed by Claude Code: genuine issue, not a false positive. This is a music-only/no-narration video ("cigarettes" at 0:00 and "You" repeated on 30s intervals are Whisper mishearing background music, not speech). The Structured Notes below are reconstructed entirely from 8 visual frames spread evenly across the 12-minute runtime, not from transcript content — treat exact node names/values as best-effort visual reads, not verified transcript quotes. Re-watch the video directly if precise parameter values are needed._

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] cigarettes,
[2:30] You
[3:00] You
[3:30] You
[4:00] You
[4:30] You
[5:00] You
[5:30] You
[6:00] You
[6:30] You
[7:00] You
[7:30] You
[8:00] You
[8:30] You
[9:00] You
[9:30] You
[10:00] You
[10:30] You
[11:00] You
[11:30] You
[12:00] You



---

## Captured Frames

- [0:30] tutorials/frames/abstract-wave-lines-looping-curves-geometry-nodes-tutorial/frame_000.jpg
- [2:00] tutorials/frames/abstract-wave-lines-looping-curves-geometry-nodes-tutorial/frame_001.jpg
- [3:30] tutorials/frames/abstract-wave-lines-looping-curves-geometry-nodes-tutorial/frame_002.jpg
- [5:00] tutorials/frames/abstract-wave-lines-looping-curves-geometry-nodes-tutorial/frame_003.jpg
- [6:30] tutorials/frames/abstract-wave-lines-looping-curves-geometry-nodes-tutorial/frame_004.jpg
- [8:00] tutorials/frames/abstract-wave-lines-looping-curves-geometry-nodes-tutorial/frame_005.jpg
- [9:30] tutorials/frames/abstract-wave-lines-looping-curves-geometry-nodes-tutorial/frame_006.jpg
- [11:00] tutorials/frames/abstract-wave-lines-looping-curves-geometry-nodes-tutorial/frame_007.jpg

---

## Structured Notes

### Core Technique
Procedural Geometry Nodes setup that generates dense, evenly-offset "looping" line/ribbon patterns which trace the silhouette of arbitrary input geometry (demonstrated on both a flat plane and 3D text) — an abstract wave-line / contour-line generator.

### Summary
**Extracted from visuals only — the video has no narration (music-only audio), so a meaningful transcript could not be captured.** Artemiy Galutskiy builds a node tree (left panel) from scratch that takes input geometry and produces many repeated, parallel offset curves/ribbons following its form, similar to a topographic-contour or engraved-line look. Mid-build the pattern shows as a radiating swirl of curved lines over a flat plane; later the same node group is applied to 3D text (the letter "A"), producing concentric line contours that trace the letterform, with a Color Ramp (red/pink/blue-purple gradient) driving the line coloring. A final frame shows the setup reduced to a simpler striped blue/white banded test pattern, suggesting the tutorial ends by generalizing/simplifying the core technique or showing a variant.

### Key Steps (inferred from frame progression — verify against the actual video for exact node names/values)
1. Start from a flat plane in the 3D viewport as a simple test case.
2. Build up a node chain (visible chain grows from ~2 nodes to 8-10+ nodes across the timeline) — likely involving curve/mesh conversion and a repeating offset step (the "looping curves" of the title), based on the swirling parallel-line result visible mid-tutorial.
3. Apply the finished node group as a modifier to 3D text geometry (letter "A" shown) — the same line pattern now follows the letterform's outline concentrically, demonstrating the setup generalizes to any input mesh.
4. Add a `Color Ramp` node (pink/red to purple/blue gradient visible in the Shader/attribute color picker) to drive per-line or per-strand color variation.
5. A later, visually simpler node graph drives a plain striped blue/white banded look — possibly a simplified variant, a different color mode, or an isolated sub-part of the graph being demoed separately.

### Nodes / Settings
- Confirmed only by visual inference: a multi-node Geometry Nodes tree (10+ nodes at peak) in the Node Editor, a `Color Ramp` (or similar gradient/attribute-color node) with a pink→purple/blue gradient
- Exact node types (Curve to Mesh, Resample Curve, Set Position, Repeat Zone, etc.) could not be confirmed from frame resolution — re-watch at higher resolution or read on-screen text directly for exact node names
- Applied to: a flat plane (early test) and extruded 3D text (final demo, letter "A")

### Difficulty
Unclear — likely Intermediate/Advanced given the density/complexity of the final node graph, but cannot be confirmed without narration

### Blender Version
Not specified (no narration or visible version indicator captured in the sampled frames)

### Tags
geometry-nodes, procedural, abstract, typography, motion-design

---

## Related Tutorials
No close match found in the current library — no other ingested tutorial covers contour/offset-line generation via Geometry Nodes. Worth cross-linking if a similar "looping curves" or "contour lines" technique is ingested later.
