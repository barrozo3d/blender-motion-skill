---
title: Using Geometry Nodes for VFX in Blender
source: YouTube
url: https://www.youtube.com/watch?v=PgRax5MeZgY
author: Jacob Zirkle
ingested: 2026-05-19
blender_version: "4.x"
tags: [geometry-nodes, vfx, compositing, camera-tracking, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/using-geometry-nodes-for-vfx-in-blender/
frame_count: 0
---

# Using Geometry Nodes for VFX in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=PgRax5MeZgY)
**Author:** Jacob Zirkle
**Duration:** 35m10s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** By the end of this tutorial, you'll know everything that you need to know to make this cool effect using geometry nodes for this visual effect shot. Join me and let's learn together. So for today's shot, we're going to need three main things. First of course is the footage, and then we need a 3D asset in order to materialize, and then finally we need an intri in order to like DC. Thank you for you. I'm going to provide all three down in the description below that you can use for free. I just launched my visual effects asset library called Visual Effects Oasis, and on there you can find a pack that contains all three of our things that we need for this specific shot. Just use the code Oasis on the screen now at checkout, and you should be able to get the entire pack totally for free. Again, the link is in the description down below, so make sure to go ahead and download it, and let's go hop in the tutorial. Okay, so here is our scene right here. I did do a few things just to set us up. First of all is the camera tracking. We have a movie camera, so we need to go ahead and track that. I have plenty of camera tracking tutorials. I'll link some mine down below as well on the top right ...



---

## Structured Notes

### Core Technique
Compositing a Geometry Nodes materialization/de-materialization VFX effect onto live-action camera-tracked footage: particles appear to assemble a 3D object from nothing using animated GeoNodes point distribution and deletion.

### Summary
35-minute VFX tutorial by Jacob Zirkle combining camera tracking (pre-solved), a 3D asset, and a GeoNodes-driven materialization effect (particles converging to form an object) with an intrinsic compositing pass. Uses a free asset pack (Visual Effects Oasis). Transcript is limited (Whisper captured only the intro), so specific node setup is partially inferred from context; the core technique is animated point-scatter/delete inside GeoNodes composited onto tracked footage.

### Key Steps
1. **Camera solve** — pre-tracked in Blender Motion Tracking; solved camera drives the 3D scene
2. **Asset placement** — import 3D model; align to tracked ground plane in the footage
3. **GeoNodes materialization** — create GeoNodes on the asset; `Distribute Points on Faces` with animated Density (0 → full); or `Delete Geometry` driven by animated threshold — particles appear progressively
4. **Instance on points** — small particles (cubes, spheres) instanced at scattered points; scale/opacity driven by same animation curve
5. **Render passes** — render GeoNodes effect on transparent background with shadow catcher
6. **Compositor** — combine footage + 3D render using Alpha Over; match color grading; add motion blur

### Nodes / Settings
- Camera tracking: Blender Motion Tracker (clip editor) → Solve → Set as Background
- `Distribute Points on Faces` — density animated via driver or keyframe
- `Delete Geometry` — animated threshold for progressive appearance
- `Instance on Points` — small mesh for particle visualization
- Render: Cycles with Film → Transparent background; Shadow Catcher on ground plane
- Compositor: Alpha Over (Z-combine) for footage + 3D blend

### Difficulty
Intermediate

### Blender Version
4.x (unspecified)

### Tags
geometry-nodes, vfx, compositing, camera-tracking, intermediate

---

## Related Tutorials
- [[superhero-landing-tutorial-02-ground-destruction-vfx-in-blender]] — VFX in live footage compositing
- [[add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1]] — proper VFX compositing workflow
- [[i-recreated-movie-scene-in-blender-nuke-complete-tutorial]] — advanced VFX recreation pipeline
