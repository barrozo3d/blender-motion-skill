---
title: Daily Blender Tip Number 45 - Quick Hair / Fur and How to Comb and Weight Paint
source: YouTube
url: https://www.youtube.com/watch?v=cZlzzIBqYbY
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Hair Particle System with Vertex Group density masking and Particle Edit combing are version-agnostic core Blender features"
tags: [particles, hair, weight-paint, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-number-45---quick-hair-fur-and-how-to-comb-and-weight-paint/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip Number 45 - Quick Hair / Fur and How to Comb and Weight Paint

**Source:** [YouTube](https://www.youtube.com/watch?v=cZlzzIBqYbY)
**Author:** Blender Secrets
**Duration:** 2m18s | 3 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'QUICK FUR'
- **CRITICAL:** Empty transcript in chapter 'SHIFT+A, Add a Monkey! Set to Smooth Shading..'
- **CRITICAL:** Total transcript only 7 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (7 chars) in 'You can comb, change the length, make it smooth...'

---


Frames captured — see "Captured Frames" section below.


### QUICK FUR [0:00]

### SHIFT+A, Add a Monkey! Set to Smooth Shading.. [0:05]

### You can comb, change the length, make it smooth... [1:38]
**Transcript (timestamped):**
[2:00] Hurray!



---

## Captured Frames

- [0:05] tutorials/frames/daily-blender-tip-number-45---quick-hair-fur-and-how-to-comb-and-weight-paint/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-number-45---quick-hair-fur-and-how-to-comb-and-weight-paint/frame_001.jpg
- [0:50] tutorials/frames/daily-blender-tip-number-45---quick-hair-fur-and-how-to-comb-and-weight-paint/frame_002.jpg
- [1:20] tutorials/frames/daily-blender-tip-number-45---quick-hair-fur-and-how-to-comb-and-weight-paint/frame_003.jpg
- [1:40] tutorials/frames/daily-blender-tip-number-45---quick-hair-fur-and-how-to-comb-and-weight-paint/frame_004.jpg
- [2:10] tutorials/frames/daily-blender-tip-number-45---quick-hair-fur-and-how-to-comb-and-weight-paint/frame_005.jpg

---

## Structured Notes

### Core Technique
Adding a **Hair Particle System** to only specific areas of a mesh (using a **Weight Paint**-defined vertex group as a density mask), then styling it directly in the 3D viewport with **Particle Edit** mode's **Comb** brush — a quick way to add localized fur/hair (e.g. a beard) without particles spawning across the entire surface.

### Summary
Frame 000 shows a blank viewport with the Add menu area, captioned "SHIFT+A, Add a Monkey! Set to Smooth Shading..." — starting from a Suzanne monkey head as the demo subject. Frame 001 shows the monkey head in **Weight Paint** mode with a bright red painted patch on the chin/jaw area (rest of the mesh blue = unweighted), the Weight Paint mode selector highlighted at the bottom, captioned "Go to Weight Paint mode, and paint red where you want hair/fur..." Frame 002 shows the same weight paint pass from another angle, red patches also visible around the head/cheek areas, reinforcing the localized density-masking approach. Frame 003 shows the resulting particle-based fur emitted only from the red-weighted regions (a chin beard), now in **Particle Edit** mode with the Comb brush active (Brush Type: Comb, Radius, Strength sliders), captioned "Go to Particle Edit and Comb that Monkey!" Frame 004 shows the beard combed into a more directed, flowing shape, captioned "You can comb, change the length, make it smooth..." Frame 005 shows the finished result: Suzanne with a full, styled fur beard and eyebrows, shaded and rendered smoothly.

### Key Steps
1. Add a mesh (e.g. Suzanne the monkey) and set it to **Smooth Shading**.
2. Switch to **Weight Paint** mode and paint a vertex group (red = full weight) only on the areas that should grow hair/fur — e.g. just the chin for a beard, or the scalp for hair.
3. Add a **Particle System** set to **Hair** emission type, and in its **Vertex Groups** settings, assign the painted vertex group to the **Density** field — this restricts particle emission to only the weighted (red-painted) regions instead of the whole mesh.
4. Enter **Particle Edit** mode and use the **Comb** brush to directly style the hair strands in the viewport — dragging to redirect their flow/direction.
5. Adjust particle **Length** and enable **Smooth** brushing to refine the fur's shape and flow into a natural-looking style (e.g. a combed beard).

### Nodes / Settings
- **Weight Paint mode** — defines a vertex group as a hair-density mask.
- **Particle System (Hair):** Vertex Groups > Density (assigned to the painted group) — restricts emission to weighted areas.
- **Particle Edit mode:** Comb brush (Radius, Strength), plus Length and Smooth options — for direct in-viewport hair styling.

### Difficulty
Intermediate

### Blender Version
Not specified — Hair Particle System with Vertex Group density masking and Particle Edit combing are version-agnostic core Blender features.

### Tags
particles, hair, weight-paint, intermediate

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover Hair Particle Systems, Weight Paint density masking, or Particle Edit combing.
