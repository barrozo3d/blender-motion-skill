---
title: Daily Blender Tip 146 - Microdisplacement in one minute!
source: YouTube
url: https://www.youtube.com/watch?v=i0c4uCa-WRQ
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — true Cycles Adaptive Subdivision microdisplacement, Experimental feature set required, consistent with Blender 2.9x-5.x"
tags: [displacement, shaders, cycles, materials, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-146---microdisplacement-in-one-minute/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 146 - Microdisplacement in one minute!

**Source:** [YouTube](https://www.youtube.com/watch?v=i0c4uCa-WRQ)
**Author:** Blender Secrets
**Duration:** 1m29s | 14 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'MICRODISPLACEMENT IN ONE MINUTE'
- **CRITICAL:** Empty transcript in chapter 'Add a Round cube and subdivide smooth twice.'
- **CRITICAL:** Empty transcript in chapter 'Add a material and add a noise texture node.'
- **CRITICAL:** Empty transcript in chapter 'Connect the Noise Fac to the Displacement socket.'
- **CRITICAL:** Empty transcript in chapter 'You can see the node output with node wrangler.'
- **CRITICAL:** Empty transcript in chapter 'That way you can preview the noise as you change it.'
- **CRITICAL:** Empty transcript in chapter 'Use the experimental settings in the render tab.'
- **CRITICAL:** Empty transcript in chapter 'Under Geometry you get new settings.'
- **CRITICAL:** Empty transcript in chapter 'Add a subdiv modifier and turn on Adaptive.'
- **CRITICAL:** Empty transcript in chapter 'Go in and out of edit mode to see the difference.'
- **CRITICAL:** Empty transcript in chapter 'Add a math node and set it to Multiply.'
- **CRITICAL:** Empty transcript in chapter 'You can use the Multiply node to control the strength.'
- **CRITICAL:** Total transcript only 29 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (21 chars) in 'In the material tab set Displacement to True.'
- WARNING: Very short transcript (8 chars) in 'Increase detail with dicing scale. Less = more detail.'

---


Frames captured — see "Captured Frames" section below.


### MICRODISPLACEMENT IN ONE MINUTE [0:00]

### Add a Round cube and subdivide smooth twice. [0:09]

### Add a material and add a noise texture node. [0:15]

### Connect the Noise Fac to the Displacement socket. [0:22]

### You can see the node output with node wrangler. [0:28]

### That way you can preview the noise as you change it. [0:35]

### Use the experimental settings in the render tab. [0:42]

### Under Geometry you get new settings. [0:46]

### Add a subdiv modifier and turn on Adaptive. [0:51]

### In the material tab set Displacement to True. [0:56]
**Transcript (timestamped):**
[1:00] VDV, Render V1 occupy


### Go in and out of edit mode to see the difference. [1:03]

### Add a math node and set it to Multiply. [1:08]

### You can use the Multiply node to control the strength. [1:12]

### Increase detail with dicing scale. Less = more detail. [1:17]
**Transcript (timestamped):**
[1:27] Coolging



---

## Captured Frames

- [0:09] tutorials/frames/daily-blender-tip-146---microdisplacement-in-one-minute/frame_000.jpg
- [0:15] tutorials/frames/daily-blender-tip-146---microdisplacement-in-one-minute/frame_001.jpg
- [0:22] tutorials/frames/daily-blender-tip-146---microdisplacement-in-one-minute/frame_002.jpg
- [0:42] tutorials/frames/daily-blender-tip-146---microdisplacement-in-one-minute/frame_003.jpg
- [0:51] tutorials/frames/daily-blender-tip-146---microdisplacement-in-one-minute/frame_004.jpg
- [0:56] tutorials/frames/daily-blender-tip-146---microdisplacement-in-one-minute/frame_005.jpg
- [1:08] tutorials/frames/daily-blender-tip-146---microdisplacement-in-one-minute/frame_006.jpg
- [1:17] tutorials/frames/daily-blender-tip-146---microdisplacement-in-one-minute/frame_007.jpg

---

## Structured Notes

### Core Technique
True Cycles microdisplacement in a single minute: a Noise Texture's Fac output feeds a material's Displacement socket, Adaptive Subdivision is enabled via Cycles' Experimental feature set plus a Subdivision Surface modifier, and Material Displacement is set to True (real, not just Bump) — producing actual sculpted-looking geometric surface detail rather than a shading trick, with a Math (Multiply) node to control strength and the Dicing Scale controlling final render resolution.

### Summary
Frame 000 shows the base object: the Add Mesh menu open with Round Cube highlighted, about to add a rounded primitive to subdivide smooth twice. Frame 001 shows a plain smooth gray sphere with a new material and a Noise Texture node added in the Shader Editor below. Frame 002 shows the Noise Texture's Fac output wired directly into the material's Displacement input socket (Displacement/Material Output nodes visible), the sphere still smooth since displacement isn't yet enabled at the render/material level. Frame 003 shows the payoff: the sphere now covered in a fine, sand-like bumpy surface, with Render Properties' Feature Set switched to **Experimental** in the sidebar — the setting that unlocks true adaptive-subdivision displacement in Cycles. Frame 004 shows the same sandy-textured sphere with a Subdivision Surface modifier added and its **Adaptive Subdivision** checkbox enabled (Cycles Dicing Rate settings visible below it). Frame 005 shows the Material Properties Settings panel with **Displacement** set to **Displacement** (labeled "True" in the caption, i.e. real geometric displacement rather than Bump/Bump+Displacement) alongside the Principled BSDF node graph. Frame 006 shows a Math node set to **Multiply** inserted between the Noise Texture and the Displacement socket, the sphere's surface bumps now visibly reduced in intensity — using the Multiply value to scale down displacement strength. Frame 007 shows the finished, richly-detailed rock/asteroid-like sphere with the Subdivision modifier's **Dicing Rate** area highlighted, captioned about the Dicing Scale controlling final surface resolution (lower = more detail, more render cost).

### Key Steps
1. Add a **Round Cube** primitive and apply Subdivide Smooth twice for a good base sphere-like shape with real geometry to displace.
2. Create a new Material and add a **Noise Texture** node in the Shader Editor.
3. Connect the Noise Texture's **Fac** output directly to the material's **Displacement** socket (on the Material Output node).
4. Use Node Wrangler (Ctrl+T or similar) to preview the node's output live in the viewport while adjusting settings.
5. In Render Properties, switch the **Feature Set** to **Experimental** — this is required to unlock Cycles' true adaptive-subdivision displacement pipeline (regular Cycles only supports Bump-style fake displacement).
6. Once Experimental is enabled, new **Geometry** settings appear in Render Properties for controlling subdivision/dicing behavior.
7. Add a **Subdivision Surface** modifier to the object and enable its **Adaptive Subdivision** checkbox — this makes the mesh subdivide dynamically at render time based on camera distance, rather than using a fixed subdivision level.
8. In Material Properties > Settings, set **Displacement** to **Displacement** (real geometric displacement, as opposed to Bump Only or Displacement and Bump) — labeled as setting "Displacement to True" in the video.
9. Toggle in and out of Edit Mode to visually compare the object's cage geometry versus the actual displaced/subdivided render result.
10. Add a **Math** node set to **Multiply**, insert it between the Noise Texture's Fac output and the Displacement socket, and use its Value input to scale the displacement strength up or down.
11. Control final render detail via the Subdivision modifier's **Dicing Scale/Rate** — lower values produce more subdivision detail (and heavier render cost), higher values produce coarser, faster results.

### Nodes / Settings
- **Shader nodes:** Noise Texture (Fac output → Displacement), Math node (Multiply, for displacement strength control), Material Output (Displacement socket), Principled BSDF.
- **Render Properties:** Feature Set = Experimental (required for true displacement), Geometry section (appears once Experimental is enabled), Dicing Rate/Scale (render resolution control).
- **Material Settings:** Displacement = Displacement (real geometric displacement, not Bump Only).
- **Modifiers:** Subdivision Surface with Adaptive Subdivision enabled.
- **Base shape:** Round Cube primitive, Subdivide Smooth ×2.

### Difficulty
Intermediate

### Blender Version
Not specified — true Cycles Adaptive Subdivision microdisplacement requires the Experimental feature set, consistent with Blender 2.9x through 5.x.

### Tags
displacement, shaders, cycles, materials, intermediate

---

## Related Tutorials
- [Easy PBR Textures - Blender Secrets](easy-pbr-textures---blender-secrets.md) — shares displacement, cycles, materials, intermediate; that fuller tutorial covers the same Experimental/Adaptive-Subdivision/Dicing-Scale displacement pipeline applied to real PBR texture sets rather than a procedural Noise Texture.
