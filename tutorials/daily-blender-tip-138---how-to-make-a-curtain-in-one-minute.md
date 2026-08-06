---
title: Daily Blender Tip 138 - How To Make A Curtain In One Minute
source: YouTube
url: https://www.youtube.com/watch?v=lYoeTliKX_4
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Cloth Pinning + animated Collision object, standard since 2.8+"
tags: [cloth, simulation, animation, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-138---how-to-make-a-curtain-in-one-minute/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 138 - How To Make A Curtain In One Minute

**Source:** [YouTube](https://www.youtube.com/watch?v=lYoeTliKX_4)
**Author:** Blender Secrets
**Duration:** 1m49s | 14 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'CURTAIN IN 1 MINUTE'
- **CRITICAL:** Empty transcript in chapter 'Create a plane, subdivide and rotate it.'
- **CRITICAL:** Empty transcript in chapter 'Scale it vertically and add an edge loop in the middle'
- **CRITICAL:** Empty transcript in chapter 'Subdivide the mesh a few times.'
- **CRITICAL:** Empty transcript in chapter 'Select some vertical edge loops and move them.'
- **CRITICAL:** Empty transcript in chapter 'Select the top edge row and make a vertex group.'
- **CRITICAL:** Empty transcript in chapter 'Add a Cloth system with the Silk preset'
- **CRITICAL:** Empty transcript in chapter 'Turn on Pinning and choose the vertex group you made.'
- **CRITICAL:** Empty transcript in chapter 'Add a Torus primitive and scale it down.'
- **CRITICAL:** Empty transcript in chapter 'Set a scale keyframe at frame 50 (press ";").'
- **CRITICAL:** Empty transcript in chapter 'Scale up the torus, go to frame 1, add a keyframe.'
- **CRITICAL:** Total transcript only 146 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (9 chars) in 'Add a Collision system to the torus.'

---


Frames captured — see "Captured Frames" section below.


### CURTAIN IN 1 MINUTE [0:00]

### Create a plane, subdivide and rotate it. [0:04]

### Scale it vertically and add an edge loop in the middle [0:12]

### Subdivide the mesh a few times. [0:19]

### Select some vertical edge loops and move them. [0:26]

### Select the top edge row and make a vertex group. [0:44]

### Add a Cloth system with the Silk preset [0:51]

### Turn on Pinning and choose the vertex group you made. [0:57]

### Add a Torus primitive and scale it down. [1:04]

### Set a scale keyframe at frame 50 (press ";"). [1:11]

### Scale up the torus, go to frame 1, add a keyframe. [1:19]

### Add a Collision system to the torus. [1:26]
**Transcript (timestamped):**
[1:30] Unity 여기,


### Add a Subdiv modifier to the curtain [1:33]
**Transcript (timestamped):**
[1:34] with code or the view field to pull out in the movies.


### Play the simulation! [1:38]
**Transcript (timestamped):**
[1:38] izz
[1:40] Press F tips on the info bar.
[1:42] Click on spectacular.
[1:46] At this point click on theإ



---

## Captured Frames

- [0:04] tutorials/frames/daily-blender-tip-138---how-to-make-a-curtain-in-one-minute/frame_000.jpg
- [0:12] tutorials/frames/daily-blender-tip-138---how-to-make-a-curtain-in-one-minute/frame_001.jpg
- [0:26] tutorials/frames/daily-blender-tip-138---how-to-make-a-curtain-in-one-minute/frame_002.jpg
- [0:51] tutorials/frames/daily-blender-tip-138---how-to-make-a-curtain-in-one-minute/frame_003.jpg
- [1:04] tutorials/frames/daily-blender-tip-138---how-to-make-a-curtain-in-one-minute/frame_004.jpg
- [1:11] tutorials/frames/daily-blender-tip-138---how-to-make-a-curtain-in-one-minute/frame_005.jpg
- [1:25] tutorials/frames/daily-blender-tip-138---how-to-make-a-curtain-in-one-minute/frame_006.jpg
- [1:38] tutorials/frames/daily-blender-tip-138---how-to-make-a-curtain-in-one-minute/frame_007.jpg

---

## Structured Notes

### Core Technique
A curtain drape made from a pre-wrinkled plane, pinned at the top with Cloth physics (Silk preset), and pulled into a tied-back shape by an animated Torus "curtain ring" that scales from large to small around it, using Collision so the fabric visibly gets pulled together and clumps under the ring.

### Summary
Frame 000 shows the starting shape: a bare subdivided plane, captioned "Create a plane, subdivide and rotate it." Frame 001 shows the plane scaled tall and vertical with a center edge loop added (dashed centerline visible), captioned "Scale it vertically and add an edge loop in the middle." Frame 002 shows the mesh after further subdivision with several vertical edge loops selected and offset slightly from each other (creating a pre-wrinkled, fluted starting silhouette rather than a flat sheet), captioned "Select some vertical edge loops and move them." Frame 003 shows the Cloth physics panel with a Vertex Group ("Group") assigned and Shape Keys/UV Maps/Vertex Colors sections visible, over the fluted curtain shape, captioned "Add a Cloth system with the Silk preset" — the pre-wrinkled geometry combined with a light Silk material preset. Frame 004 shows a Torus primitive scaled down to a thin ring, positioned partway down the curtain's length, captioned "Add a Torus primitive and scale it down" — this becomes the curtain tie/ring. Frame 005 shows a green keyframe marker (the curved dashed line) at the base of the curtain where the torus sits, captioned "Set a scale keyframe at frame 50 (press \"i\")" — keyframing the torus at its small/tied scale. Frame 006 shows the Physics properties tab open with Force Field/Collision/Cloth/Dynamic Paint/Soft Body/Rigid Body/Fluid icons visible on the torus object, captioned "Scale up the torus, go to frame 1, add a keyframe" — animating the ring from large (frame 1, not yet constricting) to small (frame 50, cinching the curtain). Frame 007 shows the finished simulated result: the curtain fabric visibly pulled together and bunched right where the torus ring sits, creating a natural tied-back curtain silhouette, captioned "Play the simulation!"

### Key Steps
1. Create a Plane, subdivide it, and rotate it into a vertical orientation.
2. Scale it tall/vertical and add a center edge loop for extra structure.
3. Subdivide the mesh further for enough resolution to simulate folds convincingly.
4. Select some vertical edge loops and offset/move them slightly relative to each other — pre-wrinkling the flat plane into a fluted starting silhouette so the cloth sim has natural folds to work with from the start, rather than starting perfectly flat.
5. Select the top edge row (the curtain's rod-mounted edge) and assign it to a new Vertex Group.
6. Add a **Cloth** simulation using the **Silk** preset as a starting material.
7. Enable **Pinning** on the Cloth modifier and assign the vertex group made in step 5 — this fixes the top edge in place (as if hung from a curtain rod) while the rest of the fabric simulates freely.
8. Add a **Torus** primitive, scale it down into a thin ring shape, and position it partway down the curtain — this represents a decorative curtain tie/ring.
9. Animate the tie: at frame 50, keyframe the torus scaled down small (press I to insert a Scale keyframe); go back to frame 1, scale the torus up large (so it doesn't initially constrict the fabric), and insert another Scale keyframe there.
10. Add a **Collision** physics system to the torus so the simulated cloth reacts to and is physically stopped/pulled by it as it shrinks.
11. Add a Subdivision modifier to the curtain mesh for a smoother final look.
12. Play the simulation — as the torus scales down toward frame 50, it visibly cinches the cloth together at that point, producing a natural tied-back curtain drape.

### Nodes / Settings
- **Modeling:** Plane subdivision + rotation + vertical scale, pre-wrinkling via offset vertical edge loops, center edge loop.
- **Vertex Groups:** top-edge Pin Group (assigned before adding Cloth).
- **Cloth modifier:** Silk preset, Pinning (Vertex Group field).
- **Animation:** Torus primitive (curtain ring/tie), Scale keyframes (I) at frame 1 (large) and frame 50 (small).
- **Physics:** Collision (on the animated torus, so the cloth reacts to it).
- **Finishing:** Subdivision Surface modifier on the curtain for smoothness.

### Difficulty
Beginner

### Blender Version
Not specified — Cloth Pinning and an animated Collision object are a standard workflow available since Blender 2.8+.

### Tags
cloth, simulation, animation, beginner

---

## Related Tutorials
- [Daily Blender Tip 131 - How To Make A Pillow In One Minute](daily-blender-tip-131---how-to-make-a-pillow-in-one-minute.md) — shares cloth, simulation; both are quick "in one minute" Cloth-modifier tricks using an auxiliary Force/Collision object to shape the fabric.
- [Ruffled Skirts | Virtual Fashion | Blender Tutorial | Blender Secrets](ruffled-skirts-virtual-fashion-blender-tutorial-blender-secrets.md) — shares cloth, simulation; complementary Cloth Pinning technique, here pinning the top edge of a curtain rather than excluding parts of a garment from simulation.
