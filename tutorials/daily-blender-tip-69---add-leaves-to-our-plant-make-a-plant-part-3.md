---
title: Daily Blender Tip 69 - Add Leaves To Our Plant (Make a Plant Part 3)
source: YouTube
url: https://www.youtube.com/watch?v=DOfWm3GIh-k
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Import Images as Planes, Decimate modifier, and Hair Particle System are version-agnostic core Blender features"
tags: [particles, procedural, organic, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-69---add-leaves-to-our-plant-make-a-plant-part-3/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 69 - Add Leaves To Our Plant (Make a Plant Part 3)

**Source:** [YouTube](https://www.youtube.com/watch?v=DOfWm3GIh-k)
**Author:** Blender Secrets
**Duration:** 1m53s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'ADD LEAVES (MAKE A PLANT PART 3)'
- **CRITICAL:** Empty transcript in chapter 'Use the Import Images As Planes Add-on (comes default with Blender) to import a leaf texture.'
- **CRITICAL:** Empty transcript in chapter 'On layer one I have the trunk from Tip 68. Apply the Particle modifier and delete the Particle system.'
- **CRITICAL:** Empty transcript in chapter 'Apply the skin modifier and add a decimate modifier to make the twigs less polygon-dense, then apply the modifier (0,1 works as a setting)'
- **CRITICAL:** Total transcript only 23 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (23 chars) in 'Add a particle system to the twigs, Hair/Advanced, Number: 50.'

---


Frames captured — see "Captured Frames" section below.


### ADD LEAVES (MAKE A PLANT PART 3) [0:00]

### Use the Import Images As Planes Add-on (comes default with Blender) to import a leaf texture. [0:05]

### On layer one I have the trunk from Tip 68. Apply the Particle modifier and delete the Particle system. [0:51]

### Apply the skin modifier and add a decimate modifier to make the twigs less polygon-dense, then apply the modifier (0,1 works as a setting) [1:09]

### Add a particle system to the twigs, Hair/Advanced, Number: 50. [1:16]
**Transcript (timestamped):**
[1:30] block ك
[1:33] text
[1:43] rigid
[1:47] Nous



---

## Captured Frames

- [0:05] tutorials/frames/daily-blender-tip-69---add-leaves-to-our-plant-make-a-plant-part-3/frame_000.jpg
- [0:20] tutorials/frames/daily-blender-tip-69---add-leaves-to-our-plant-make-a-plant-part-3/frame_001.jpg
- [0:51] tutorials/frames/daily-blender-tip-69---add-leaves-to-our-plant-make-a-plant-part-3/frame_002.jpg
- [1:09] tutorials/frames/daily-blender-tip-69---add-leaves-to-our-plant-make-a-plant-part-3/frame_003.jpg
- [1:16] tutorials/frames/daily-blender-tip-69---add-leaves-to-our-plant-make-a-plant-part-3/frame_004.jpg
- [1:45] tutorials/frames/daily-blender-tip-69---add-leaves-to-our-plant-make-a-plant-part-3/frame_005.jpg

---

## Structured Notes

### Core Technique
Finishing the plant series (Part 3): converting the twig-covered trunk from [Tip 68](daily-blender-tip-68---plant-part-2-adding-twigs-with-particles.md) into a clean, decimated base mesh, then scattering a hand-shaped leaf texture plane (imported via **Import Images as Planes**) across the twigs with a second **Hair Particle System** (Advanced emission, Number: 50), tuning rotation/size randomness for a natural leafy silhouette.

### Summary
Frame 000 is a title card, captioned "Use the Import Images As Planes Add-on (comes default with Blender) to import a leaf texture." Frame 001 shows a single leaf-shaped plane (a compound leaf texture with an alpha cutout) subdivided once and vertex-shaped into a slightly curved, natural leaf silhouette, captioned "This one I bought from Poliigon, you can find free ones on Textures.com. I subdivide the plane once and give it some shape by moving vertices." Frame 002 shows the trunk-with-twig-particles from Tip 68, captioned "On layer one I have the trunk from Tip 68. Apply the Particle modifier and delete the Particle system" — converting the previous particle-instanced twigs into real, applied geometry so the twigs themselves can now be edited/decimated. Frame 003 shows the twig geometry with a **Decimate** modifier in the stack, captioned "Apply the skin modifier and add a decimate modifier to make the twigs less polygon-dense, then apply the modifier (0,1 works as a setting)" — reducing the twig mesh's polycount before adding a second particle layer for leaves. Frame 004 shows the now-white/unshaded twig structure with a new **Particle System** slot added, Emission set to **Hair** with **Advanced** and **Number: 50**, captioned "Add a particle system to the twigs, Hair / Advanced, Number: 50." Frame 005 shows the finished leafy plant with green leaf instances scattered across the twigs, a Rotation section visible in the sidebar, captioned "Play with the rotation and rotation randomness, as well as the size and size randomness."

### Key Steps
1. Import a leaf texture image (with alpha transparency for the leaf silhouette) using **Import Images as Planes**.
2. Subdivide the leaf plane once and reshape it slightly with vertex moves for a more natural, less perfectly-flat leaf silhouette.
3. Take the twig-covered trunk from Tip 68: **apply** the twigs' Particle system (converting instances to real geometry) and delete the now-redundant particle system.
4. **Apply** the Skin modifier on the twig geometry, then add a **Decimate** modifier (around 0.1 ratio) to reduce the twig mesh's polygon density before it becomes the base for a second particle layer — keeps performance manageable when leaves are added.
5. Add a new **Particle System** to the twig object, set to **Hair** emission with **Advanced** mode, and set **Number** to around 50 (a starting point, tuned to taste) — this scatters leaf-plane instances across the twig surface.
6. Adjust **Rotation** and **Rotation Randomness**, plus **Size** and **Size Randomness**, until the leaf coverage looks natural rather than uniform/robotic.

### Nodes / Settings
- **Add-on:** Import Images as Planes (built-in) — for the leaf texture plane.
- **Particle system workflow:** Apply Particle (twigs) → delete particle system → Apply Skin modifier → Decimate modifier (~0.1) → Apply → new Particle System (Hair, Advanced, Number ~50) for leaves.
- **Particle System:** Rotation + Rotation Randomness, Size + Size Randomness.

### Difficulty
Intermediate

### Blender Version
Not specified — Import Images as Planes, Decimate modifier, and Hair Particle System are version-agnostic core Blender features.

### Tags
particles, procedural, organic, intermediate

---

## Related Tutorials
- [Daily Blender Tip 68 - Plant Part 2: Adding Twigs With Particles](daily-blender-tip-68---plant-part-2-adding-twigs-with-particles.md) — shares particles, procedural, organic; this is the direct Part 3 continuation, converting Part 2's particle-instanced twigs to real geometry and adding a second leaf-particle layer.
- [Daily Blender Tip 66 - Quick Tree Trunk With Skin Modifier](daily-blender-tip-66---quick-tree-trunk-with-skin-modifier.md) — shares procedural, organic; Part 1 of this same 3-part plant-building series, providing the original trunk/branch base mesh.
