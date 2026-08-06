---
title: Daily Blender Tip 128 - Material Basics: Dust/Snow
source: YouTube
url: https://www.youtube.com/watch?v=1F-wFa-oExw
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — node-based Geometry/Normal shading, version-agnostic core Cycles/EEVEE workflow"
tags: [shaders, materials, procedural, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-128---material-basics-dustsnow/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 128 - Material Basics: Dust/Snow

**Source:** [YouTube](https://www.youtube.com/watch?v=1F-wFa-oExw)
**Author:** Blender Secrets
**Duration:** 1m57s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 20 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (20 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] Shorten items after及



---

## Captured Frames

- [0:10] tutorials/frames/daily-blender-tip-128---material-basics-dustsnow/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-128---material-basics-dustsnow/frame_001.jpg
- [0:50] tutorials/frames/daily-blender-tip-128---material-basics-dustsnow/frame_002.jpg
- [1:10] tutorials/frames/daily-blender-tip-128---material-basics-dustsnow/frame_003.jpg
- [1:30] tutorials/frames/daily-blender-tip-128---material-basics-dustsnow/frame_004.jpg
- [1:50] tutorials/frames/daily-blender-tip-128---material-basics-dustsnow/frame_005.jpg

---

## Structured Notes

### Core Technique
A classic "upward-facing surfaces get dust/snow" shader trick: the object's surface Normal is broken into its individual X/Y/Z color channels, and the channel corresponding to "how much this point faces upward" is used as the Fac input of a Mix Shader to blend a dust/snow material onto upward-facing surfaces while leaving vertical/downward-facing surfaces as the base material — with a ColorRamp node added afterward to control the sharpness/threshold of that transition. Note: this video's audio track is silent/near-empty; this summary is built entirely from the captured on-screen text captions and frames.

### Summary
Frame 000 shows the starting node chain: a Geometry node (Position, Normal, Tangent, True Normal, Incoming, Parametric, Backfacing, Pointiness outputs) feeding into a Mix (Color) node, over a smooth purple/pink-lit test shape — captioned "Materials Basics: Dust/Snow." Frame 001 shows the next step: that Mix node's Color output plugged into a **Separate RGB** node, captioned "Plug it into a SeparateRGB node and use the B output" — extracting the individual color channels (which, derived from the surface Normal, correspond to facing-direction components) so the "upward-facing" channel can be isolated. Frame 002 shows the payoff: a Diffuse BSDF (Roughness 0.608, representing the dust/snow material) and a Glossy BSDF (the base material) both feeding into a **Mix Shader**, captioned "And use it to mix two materials" — with the model now showing a stippled dust/snow texture across its upper surfaces. Frame 003 shows a **ColorRamp** node inserted between the Separate RGB "B" output (labeled GB/R/G/B) and the Diffuse BSDF, its black-to-white gradient handle positioned around 0.341, captioned "You can change the look with the ColorRamp node" — the model now showing sparser dust coverage. Frames 004–005 show the same ColorRamp setup with its position slider moved further right (0.391, then 0.955), each producing progressively more/less dust coverage and a different transition sharpness on the model's surface — demonstrating how sliding the ramp's color stop changes how much of the surface reads as "dusted."

### Key Steps
1. Add a **Geometry** node to the material's shader graph — its Normal output describes each point's facing direction as an RGB-like vector.
2. Feed that Normal (via a Mix/Color node, likely converting World/Object space as needed) into a **Separate RGB** node to break it into individual R, G, and B channel values.
3. Use the channel that corresponds to "upward-facing" (the video isolates the B output specifically) as a mask value — high where the surface faces up, low where it faces sideways or down.
4. Build two materials: one representing the base surface (e.g. a Glossy BSDF) and one representing the dust/snow coating (e.g. a Diffuse BSDF with tuned Roughness); feed both into a **Mix Shader**.
5. Plug the isolated upward-facing channel into the Mix Shader's **Fac** input — upward-facing areas blend toward the dust/snow material, while vertical/downward-facing areas stay as the base material.
6. Insert a **ColorRamp** node between the isolated channel and the Mix Shader's Fac input to art-direct the effect — sliding the ramp's color stop position changes how much of the surface counts as "dusted" and how sharp or gradual that transition looks, without needing to touch the underlying normal-based mask logic.

### Nodes / Settings
- **Geometry node:** Normal output (facing-direction vector).
- **Separate RGB node:** isolates the upward-facing component (B channel used in this example) from the normal-derived color/vector.
- **Mix Shader:** Fac driven by the isolated normal channel (optionally through a ColorRamp), blending a base material (e.g. Glossy BSDF) with a dust/snow material (e.g. Diffuse BSDF).
- **ColorRamp node:** Linear interpolation, adjustable color-stop Position — art-directs the sharpness/coverage of the dust/snow transition.

### Difficulty
Beginner

### Blender Version
Not specified — this is a version-agnostic core Cycles/EEVEE node-shading technique based on the Geometry node's Normal output.

### Tags
shaders, materials, procedural, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover this Normal-based dust/snow shader mixing technique.
