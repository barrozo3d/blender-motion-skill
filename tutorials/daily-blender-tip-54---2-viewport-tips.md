---
title: Daily Blender Tip 54 - 2 Viewport Tips
source: YouTube
url: https://www.youtube.com/watch?v=qj2yDtU2M_I
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 2.8+ (Viewport Display material color + Matcap/Cavity Viewport Shading popover)"
tags: [workflow, viewport, materials, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-54---2-viewport-tips/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 54 - 2 Viewport Tips

**Source:** [YouTube](https://www.youtube.com/watch?v=qj2yDtU2M_I)
**Author:** Blender Secrets
**Duration:** 1m32s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter '<Untitled Chapter 1>'
- **CRITICAL:** Empty transcript in chapter 'One thing I always do is give parts different Viewport Colors. This has nothing to do with the render color'
- **CRITICAL:** Empty transcript in chapter 'You can use any random color. It keeps things more clear, especially with lots of mechanical parts.'
- **CRITICAL:** Empty transcript in chapter 'Another good trick is to use a matcap (option panel: press "n") as well as Ambient Occlusion'
- **CRITICAL:** Empty transcript in chapter 'Turn on Matcap and Ambient Occlusion, and play with the Strength.'
- **CRITICAL:** Empty transcript in chapter 'Samples controls how grainy it is, so make sure it's set high enough.'
- **CRITICAL:** Total transcript only 15 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (15 chars) in 'The combination of Matcaps and Ambient Occlusion makes it easier to see what you are doing.'

---


Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]

### One thing I always do is give parts different Viewport Colors. This has nothing to do with the render color [0:04]

### You can use any random color. It keeps things more clear, especially with lots of mechanical parts. [0:15]

### Another good trick is to use a matcap (option panel: press "n") as well as Ambient Occlusion [0:28]

### Turn on Matcap and Ambient Occlusion, and play with the Strength. [0:42]

### Samples controls how grainy it is, so make sure it's set high enough. [0:52]

### The combination of Matcaps and Ambient Occlusion makes it easier to see what you are doing. [1:02]
**Transcript (timestamped):**
[1:30] PEX Guru dakika



---

## Captured Frames

- [0:04] tutorials/frames/daily-blender-tip-54---2-viewport-tips/frame_000.jpg
- [0:15] tutorials/frames/daily-blender-tip-54---2-viewport-tips/frame_001.jpg
- [0:28] tutorials/frames/daily-blender-tip-54---2-viewport-tips/frame_002.jpg
- [0:42] tutorials/frames/daily-blender-tip-54---2-viewport-tips/frame_003.jpg
- [0:52] tutorials/frames/daily-blender-tip-54---2-viewport-tips/frame_004.jpg
- [1:02] tutorials/frames/daily-blender-tip-54---2-viewport-tips/frame_005.jpg

---

## Structured Notes

### Core Technique
Two viewport-only clarity tricks for working on complex mechanical models in Solid shading mode: (1) assigning each material a distinct **Viewport Display Color** independent of the actual render/shader color, and (2) enabling **Matcap** shading combined with **Cavity/Ambient Occlusion** (with tuned Strength and Samples) in the Shading popover — so part boundaries and surface detail read clearly while modeling, without affecting the final render.

### Summary
Frame 000 shows the Material Properties panel's **Viewport Display > Color** swatch open with a color wheel, over a mechanical assembly (blue/green/pink parts, a small toy-like figure on top), captioned "One thing I always do is give parts different Viewport Colors. This has nothing to do with the render color." Frame 001 shows the same color wheel with the Alpha slider highlighted at the bottom, captioned "You can use any random color. It keeps things more clear, especially with lots of mechanical parts." Frame 002 shows the Material Properties Surface section (Diffuse BSDF, Color, Roughness, Normal) with the model now in a flat gray studio view, captioned "Another good trick is to use a matcap (option panel: press 'n') as well as Ambient Occlusion" — indicating the N-panel/Viewport Shading popover is the entry point. Frame 003 shows the Viewport Shading popover (Solid mode) with **Cavity/Matcap** section expanded, a Strength/World Space/Screen Space/Samples set of sliders highlighted in red, captioned "Turn on Matcap and Ambient Occlusion, and play with the Strength." Frame 004 shows the same popover with **Samples** specifically highlighted, captioned "Samples controls how grainy it is, so make sure it's set high enough." Frame 005 shows the **Matcap picker grid** (a wall of sphere preview thumbnails — chrome, clay, colored, checkered options) with a white/gray sphere selected and Cavity settings still visible below, captioned "The combination of Matcaps and Ambient Occlusion makes it easier to see what you are doing."

### Key Steps
**Tip 1 — Per-material Viewport Display Color:**
1. Select a part/material and go to **Material Properties > Viewport Display > Color**.
2. Pick any distinct color per material/part via the color wheel — this only affects Solid-shading viewport display, not the actual render/shader Base Color, so it's purely an organizational aid for telling mechanical parts apart at a glance.

**Tip 2 — Matcap + Cavity/Ambient Occlusion for viewport clarity:**
3. Open the **Viewport Shading** popover (click-and-hold the Solid shading sphere icon, or press N for the sidebar panel) and switch/expand to **Matcap**.
4. Pick a matcap from the sphere-thumbnail picker grid (e.g. a neutral clay/chrome sphere) for quick, lighting-independent shape readability.
5. Enable **Cavity** (Ambient Occlusion-style crevice darkening) in the same popover and increase **Strength** to make part seams/edges pop visually.
6. Raise **Samples** if the cavity/AO effect looks grainy/noisy — higher samples smooth it out.
7. Combined, Matcap + Cavity makes it much easier to visually parse dense mechanical geometry while modeling, without touching actual render settings.

### Nodes / Settings
- **Material Properties > Viewport Display > Color** — per-material Solid-view-only color override.
- **Viewport Shading popover (Solid mode) > Matcap** — sphere-thumbnail picker for a quick-shading preview material.
- **Viewport Shading popover > Cavity** — Strength, World Space/Screen Space, Samples sliders (Ambient-Occlusion-style edge/crevice darkening for viewport clarity).

### Difficulty
Beginner

### Blender Version
Blender 2.8+ (Viewport Display material color + Matcap/Cavity Viewport Shading popover — post-Eevee/2.8 UI redesign).

### Tags
workflow, viewport, materials, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover Viewport Display colors or Matcap/Cavity shading specifically.
