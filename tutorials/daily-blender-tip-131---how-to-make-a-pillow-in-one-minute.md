---
title: Daily Blender Tip 131 - How To Make A Pillow In One Minute
source: YouTube
url: https://www.youtube.com/watch?v=EAKd0g65fo8
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Cloth Sewing Springs + Force Field workflow, standard since 2.8+"
tags: [cloth, simulation, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-131---how-to-make-a-pillow-in-one-minute/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 131 - How To Make A Pillow In One Minute

**Source:** [YouTube](https://www.youtube.com/watch?v=EAKd0g65fo8)
**Author:** Blender Secrets
**Duration:** 1m56s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'PILLOW IN ONE MINUTE'
- **CRITICAL:** Empty transcript in chapter 'Scale down the default cube: press S+Z+0.01'
- **CRITICAL:** Empty transcript in chapter 'In Edit Mode press CTRL+R to add an edge loop...'
- **CRITICAL:** Empty transcript in chapter 'Add a Cloth simulator to the cube, preset "cotton".'
- **CRITICAL:** Empty transcript in chapter 'Turn on "Cloth Sewing Springs" and Gravity: 0.'
- **CRITICAL:** Empty transcript in chapter 'Add a Force Field: Force to the scene.'
- **CRITICAL:** Empty transcript in chapter 'Strength: 200.'
- **CRITICAL:** Total transcript only 116 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (16 chars) in 'Scroll on the timeline to find the best moment....'

---


Frames captured — see "Captured Frames" section below.


### PILLOW IN ONE MINUTE [0:00]

### Scale down the default cube: press S+Z+0.01 [0:07]

### In Edit Mode press CTRL+R to add an edge loop... [0:12]

### Add a Cloth simulator to the cube, preset "cotton". [0:50]

### Turn on "Cloth Sewing Springs" and Gravity: 0. [0:57]

### Add a Force Field: Force to the scene. [1:07]

### Strength: 200. [1:16]

### Let's add a matcap for fun, and use smooth shading. [1:25]
**Transcript (timestamped):**
[1:30] Color Al característica
[1:33] Color for single tone
[1:35] 隻, biggest fraction band
[1:36] is that you need double Doric


### Scroll on the timeline to find the best moment.... [1:44]
**Transcript (timestamped):**
[1:45] 2, messy pattern



---

## Captured Frames

- [0:07] tutorials/frames/daily-blender-tip-131---how-to-make-a-pillow-in-one-minute/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-131---how-to-make-a-pillow-in-one-minute/frame_001.jpg
- [0:57] tutorials/frames/daily-blender-tip-131---how-to-make-a-pillow-in-one-minute/frame_002.jpg
- [1:16] tutorials/frames/daily-blender-tip-131---how-to-make-a-pillow-in-one-minute/frame_003.jpg
- [1:25] tutorials/frames/daily-blender-tip-131---how-to-make-a-pillow-in-one-minute/frame_004.jpg
- [1:44] tutorials/frames/daily-blender-tip-131---how-to-make-a-pillow-in-one-minute/frame_005.jpg

---

## Structured Notes

### Core Technique
A very fast pillow-puffing technique: a flattened cube (two overlapping "fabric" faces) gets Cloth physics with **Sewing Springs** enabled and Gravity disabled, then a Force Field with high Strength blows the two faces apart from the inside — puffing the flattened cube into a naturally-creased pillow shape almost instantly. Note: this video's audio track is silent/near-empty; this summary is built entirely from the captured on-screen text captions and frames.

### Summary
Frame 000 shows the base shape: a default cube scaled flat on Z (S, Z, 0.01) already displaying soft pillow-like creases in a preview render, captioned "Scale down the default cube: press S+Z+0.01." Frame 001 shows the flattened plane in Edit Mode with a dense grid of edge loops added in both directions (Loop Cut and Slide panel visible, Number of Cuts field), captioned "Add an edge loop in the other direction as well" — enough resolution for the cloth sim to fold and crease convincingly. Frame 002 shows the Cloth physics panel with **Cloth Sewing Springs** and **Cloth Self Collision** both checked, and Gravity fields visible, captioned "Turn on 'Cloth Sewing Springs' and Gravity: 0" — disabling gravity so the shape puffs purely from internal pressure rather than sagging downward. Frame 003 shows a Force Field object's settings (Type: Force, Shape: Point, Flow, Noise, Seed, Gravitation, Falloff: Sphere/Tube/Cone) with Strength being set, captioned "Strength: 200" — the force blowing the two cloth faces apart from the inside. Frame 004 shows the Force Field's Shading properties with Matcap enabled, captioned "Let's add a matcap for fun, and use smooth shading" — a purely cosmetic viewport preview improvement. Frame 005 shows the final result: a convincingly puffed, naturally creased golden pillow shape rendered under the matcap, captioned "Scroll on the timeline to find the best moment..." — since the simulation's look changes frame to frame, picking the best-looking frame is the last step.

### Key Steps
1. Start with a default cube, scale it flat on Z (S, Z, 0.01) — this leaves two very close, nearly-overlapping large flat faces (top and bottom) that will act as the pillow's two fabric sides.
2. In Edit Mode, add edge loops with Ctrl+R in both directions across the flattened faces — enough subdivision resolution for the cloth simulation to fold and crease believably.
3. Add a Cloth physics simulation to the object using the "Cotton" preset as a starting point.
4. Enable **Cloth Sewing Springs** (this pulls/holds the two nearly-overlapping flat faces together at their edges, like a pillow's stitched seam) and **Self Collision**; set Gravity to 0 so the shape puffs symmetrically instead of sagging under its own weight.
5. Add a **Force Field** object (Type: Force) positioned inside/near the flattened cube, and set its Strength to a high value (200 in this example) — this pushes the cloth's two internal faces apart from the inside, inflating the sewn shape into a pillow.
6. Play the simulation and **scroll through the timeline** to find the frame with the most naturally pillow-like creases and puffiness — the "best moment" is a manual pick rather than the simulation's final settled state.
7. Purely cosmetic finishing: apply a Matcap and enable Smooth Shading for a nicer, more presentable preview render of the result.

### Nodes / Settings
- **Modeling:** flattened cube (S, Z, 0.01), Ctrl+R loop cuts in both directions for simulation resolution.
- **Cloth modifier:** Cotton preset (starting point), Cloth Sewing Springs (enabled), Self Collision (enabled), Gravity = 0.
- **Force Field object:** Type = Force, Strength ≈200 (positioned to blow the two internal faces apart).
- **Finishing:** Matcap viewport shading, Smooth Shading, manual timeline scrubbing to pick the best simulation frame.

### Difficulty
Beginner

### Blender Version
Not specified — Cloth Sewing Springs and Force Fields are a standard workflow available since Blender 2.8+.

### Tags
cloth, simulation, beginner

---

## Related Tutorials
- [Ruffled Skirts | Virtual Fashion | Blender Tutorial | Blender Secrets](ruffled-skirts-virtual-fashion-blender-tutorial-blender-secrets.md) — shares cloth, simulation; both rely on Cloth Sewing Springs to pull fabric edges together, here to puff a pillow from the inside rather than pucker a ruffled hem.
- [Interactive Cloth + new Cloth Brushes & more - Blender Secrets](interactive-cloth-new-cloth-brushes-more---blender-secrets.md) — shares cloth, simulation; complementary quick Cloth-modifier technique, Force-Field-driven inflation here vs. Hook-driven interactive posing there.
- [Daily Blender Tip 138 - How To Make A Curtain In One Minute](daily-blender-tip-138---how-to-make-a-curtain-in-one-minute.md) — shares cloth, simulation; both are quick "in one minute" Cloth-modifier tricks using an auxiliary object (Force Field here vs. an animated Collision Torus there) to shape the fabric.
