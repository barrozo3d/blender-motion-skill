---
title: Daily Blender Tip 72 - Wave Modifier And Blender 2.8!
source: YouTube
url: https://www.youtube.com/watch?v=gHx-hH5rrD8
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 2.8 (title explicitly references \"Blender 2.8 Stuff\")"
tags: [modelling, animation, organic, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-72---wave-modifier-and-blender-28/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 72 - Wave Modifier And Blender 2.8!

**Source:** [YouTube](https://www.youtube.com/watch?v=gHx-hH5rrD8)
**Author:** Blender Secrets
**Duration:** 2m0s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'WAVE MODIFIER + BLENDER 2.8 STUFF'
- **CRITICAL:** Empty transcript in chapter 'Add a mirror modifier to restore the deleted parts.'
- **CRITICAL:** Empty transcript in chapter 'Extrude with "e". Add some edge loops with ctrl+r and drag the middle mouse button up.'
- **CRITICAL:** Total transcript only 14 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (14 chars) in 'Press "o" to activate proportional editing and middle mouse button to change the radius...'

---


Frames captured — see "Captured Frames" section below.


### WAVE MODIFIER + BLENDER 2.8 STUFF [0:00]

### Add a mirror modifier to restore the deleted parts. [0:29]

### Extrude with "e". Add some edge loops with ctrl+r and drag the middle mouse button up. [0:52]

### Press "o" to activate proportional editing and middle mouse button to change the radius... [1:12]
**Transcript (timestamped):**
[2:00] Bevel Agilityべ



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-72---wave-modifier-and-blender-28/frame_000.jpg
- [0:29] tutorials/frames/daily-blender-tip-72---wave-modifier-and-blender-28/frame_001.jpg
- [0:52] tutorials/frames/daily-blender-tip-72---wave-modifier-and-blender-28/frame_002.jpg
- [1:15] tutorials/frames/daily-blender-tip-72---wave-modifier-and-blender-28/frame_003.jpg
- [1:35] tutorials/frames/daily-blender-tip-72---wave-modifier-and-blender-28/frame_004.jpg
- [1:55] tutorials/frames/daily-blender-tip-72---wave-modifier-and-blender-28/frame_005.jpg

---

## Structured Notes

### Core Technique
Modeling symmetrical creature legs with a **Mirror modifier** and **Proportional Editing**, then applying a **Wave modifier** to add a continuous jiggly/wobbly ripple animation across the mesh — demonstrated on a small jelly-like walking character with a shiny chrome dome body and two thin legs.

### Summary
Frame 000 shows the finished render concept: a chrome, mirror-reflective blob body with glowing pink eyes standing on thin white legs — the target creature design. Frame 001 shows a partial leg mesh in Edit Mode with a **Mirror** modifier added to the stack, captioned "Add a mirror modifier to restore the deleted parts" — one leg is modeled and mirrored to instantly create its symmetrical pair. Frame 002 shows the top of the leg mesh with a highlighted face selected for extrusion into a rounded body shape, captioned "Extrude with 'e'. Add some edge loops with ctrl+r and drag the middle mouse button up." — building up the dome-shaped body on top of the leg base. Frame 003 shows the full two-legged blob shape with a **Proportional Editing** falloff circle visible around the top dome, captioned "Press 'o' to activate proportional editing and middle mouse button to change the radius..." — smoothly reshaping the dome/body silhouette. Frame 004 shows the finished pale character model with the modifier stack open (Delta Transfer, Mesh Cache, Normal Edit, Weighted Normal, UV Project, UV Warp, Vertex Weight Edit/Mix/Proximity visible in the Add Modifier search, about to add Wave), captioned "Now finally... add the Wave modifier! Play with the settings to change the speed etc. It's a fun one." Frame 005 shows the same character with the Wave modifier's settings panel open in the sidebar (a jiggly animated ripple now applied across the mesh).

### Key Steps
1. Model one leg, then add a **Mirror** modifier to instantly generate its symmetrical counterpart, restoring/duplicating any geometry deleted on one side.
2. **Extrude (E)** upward from the leg base to build the rounded body/head shape; add supporting **edge loops** with **Ctrl+R**, dragging the middle mouse button to position them, for smoother topology.
3. Use **Proportional Editing (O)**, scrolling the middle mouse wheel to adjust the falloff radius, to smoothly reshape a cluster of nearby vertices at once — useful for sculpting an organic dome/body silhouette without hard edges.
4. Once the base mesh is finished, add a **Wave** modifier — this generates a continuous rippling/jiggly deformation animated over time, giving the model a wobbly, gelatinous motion effect.
5. Adjust the Wave modifier's Speed, Height, Width, and Narrowness settings to taste for the desired jiggle style.

### Nodes / Settings
- **Modifier:** Mirror — symmetrical modeling.
- **Shortcuts:** E (extrude), Ctrl+R (loop cut, drag MMB to position).
- **Shortcut:** O — Proportional Editing (mouse wheel adjusts falloff radius).
- **Modifier:** Wave — animated ripple/jiggle deformation (Speed, Height, Width, Narrowness settings).

### Difficulty
Beginner

### Blender Version
Blender 2.8 (title explicitly references "Blender 2.8 Stuff" — modifier stack UI and workflow consistent with the 2.8x redesign).

### Tags
modelling, animation, organic, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover the Wave modifier specifically.
