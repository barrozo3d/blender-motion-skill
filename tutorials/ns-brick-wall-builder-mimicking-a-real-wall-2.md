---
title: NS Brick Wall Builder   Mimicking a Real Wall 2
source: YouTube
url: https://www.youtube.com/watch?v=v3rbV49UVwo
author: Nick Sayce
ingested: 2026-08-17
blender_version: "5.1.x (approximate, viewport title bar in captured frames; not stated verbally)"
tags: [procedural, geometry-nodes, materials, organic, product-viz, beginner]
extraction_status: complete
frames_dir: tutorials/frames/ns-brick-wall-builder-mimicking-a-real-wall-2/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Brick Wall Builder   Mimicking a Real Wall 2

**Source:** [YouTube](https://www.youtube.com/watch?v=v3rbV49UVwo)
**Author:** Nick Sayce
**Duration:** 1m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 29 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (29 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] monde regretology survive
[1:00] you



---

## Captured Frames

- [0:05] tutorials/frames/ns-brick-wall-builder-mimicking-a-real-wall-2/frame_000.jpg
- [0:18] tutorials/frames/ns-brick-wall-builder-mimicking-a-real-wall-2/frame_001.jpg
- [0:30] tutorials/frames/ns-brick-wall-builder-mimicking-a-real-wall-2/frame_002.jpg
- [0:42] tutorials/frames/ns-brick-wall-builder-mimicking-a-real-wall-2/frame_003.jpg
- [0:55] tutorials/frames/ns-brick-wall-builder-mimicking-a-real-wall-2/frame_004.jpg

---

> **Third-party add-on note:** Part 2 of the **NS Brick Wall Builder** (Nick Sayce / NS add-on) real-wall-matching tip. Same silent-demo format as Part 1 — Whisper again returned a near-empty transcript, flagged by the ingest safeguard as unreliable; extraction is based entirely on the 5 captured frames.

## Structured Notes

### Core Technique
Continuing the same side-by-side visual-matching method from Part 1, but shifted from shape/jitter matching to **color and surface-depth matching**: with the reference brick photo and the generated English Bond wall still shown side by side, the presenter works through Brick Colour 1/2 (via the HSV color picker), Brick Colour Variation, Dirt Colour, Mortar Colour 1/2, Mortar Roughness/Brightness, and finally the Pattern/Coin/Mortar Bump strength sliders — again tuning entirely by eye against the photo rather than fixed values.

### Summary
Picks up where Part 1 left off (shape/distortion matched), now matching color and surface response. Frames show the HSV color wheel open while sampling/adjusting Brick Colour 1 and Colour 2 to approximate the reference photo's brick tone, followed by Brick Colour Variation and a Dirt Colour pass for added realism. One frame shows the reference wall next to a fully grey/neutral, unlit-looking version of the generated wall — likely a check of the surface's value/roughness response in isolation from color, before color is reintroduced (visible again in the final frame). The final captured frame shows the sidebar's Bump section active — Pattern Bump Strength, Coin Bump Strength, and Mortar Bump Strength all being dialed in — matching how deep the real wall's shadows read at the mortar lines and brick faces. As in Part 1, there's no fixed numeric recipe; the whole video demonstrates an iterative, comparison-driven workflow rather than a one-shot setting.

### Key Steps
1. Continue from a shape/jitter-matched wall (see Part 1) with the reference photo still visible alongside it in the viewport.
2. Open the HSV color picker on Brick Colour 1 (and Colour 2, if the pattern uses a second brick color) and sample/adjust toward the reference photo's actual brick tone.
3. Add Brick Colour Variation for per-brick tonal differences, and a Dirt Colour pass to introduce weathering color that isn't part of the base brick material.
4. Check the surface in a neutral/desaturated state (as seen mid-video) to judge value and roughness response independent of hue, before reintroducing full color.
5. Tune Mortar Colour 1/2, Mortar Roughness, and Mortar Brightness to match the reference wall's mortar lines specifically (often a different color/value than the bricks themselves).
6. Finish with the Bump section: dial in Pattern Bump Strength, Coin Bump Strength, and Mortar Bump Strength together, comparing shadow depth at brick edges and mortar lines against the reference photo until the surface relief reads similarly.

### Nodes / Settings
- Sidebar sections used: Bricks (Brick Colour 1/2, Brick Colour Variation, Dirt Colour), Mortar (Mortar Colour 1/2, Mortar Roughness, Mortar Brightness, Mortar Depth), Bump (Pattern Bump Strength, Coin Bump Strength, Mortar Bump Strength)
- Standard Blender HSV color picker used throughout for color sampling/matching
- Pattern used in the demo: English Bond (same as Part 1, continuing the same wall)

### Difficulty
Beginner (color/value matching by eye using existing sliders — no new controls introduced beyond what's covered in the main guides)

### Blender Version
5.1.x (approximate, viewport title bar in captured frames; not stated verbally).

### Tags
procedural, geometry-nodes, materials, organic, product-viz, beginner

---

## Related Tutorials
Part of the **NS Brick Wall Builder** guide set (Nick Sayce / NS add-on). Direct continuation of Part 1.
- [NS Brick Wall Builder - Mimicking a Real Wall](ns-brick-wall-builder---mimicking-a-real-wall.md) — Part 1 of this same technique tip (shape/jitter matching); this video continues into color and bump matching.
- [NS Brick Wall Builder v4.0 Guide](ns-brick-wall-builder-v4-0-guide.md) — full guide covering Brick Colour, Mortar and Bump controls in depth.
- [NS Brick Wall Builder Guide](ns-brick-wall-builder-guide.md) — earlier full guide, also covers these same color/bump controls under a slightly different panel layout.
