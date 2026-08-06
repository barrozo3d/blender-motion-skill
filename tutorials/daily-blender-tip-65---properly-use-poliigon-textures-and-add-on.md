---
title: Daily Blender Tip 65 - Properly Use Poliigon Textures And Add-On
source: YouTube
url: https://www.youtube.com/watch?v=mOwgdioU1Pw
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Poliigon add-on + Material Settings Displacement dropdown is consistent with Cycles-based displacement across modern Blender versions"
tags: [materials, workflow, add-on, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-65---properly-use-poliigon-textures-and-add-on/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 65 - Properly Use Poliigon Textures And Add-On

**Source:** [YouTube](https://www.youtube.com/watch?v=mOwgdioU1Pw)
**Author:** Blender Secrets
**Duration:** 2m0s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'POLIGON TEXTURES'
- **CRITICAL:** Empty transcript in chapter 'There are still a couple of things you need to do to really get the most out of them!'
- **CRITICAL:** Empty transcript in chapter 'In the material tab under Settings go and choose "True" as the displacement type. TAB in and out of edit mode to update the mesh.'
- **CRITICAL:** Total transcript only 41 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (41 chars) in 'A bit dark... increase the brightness of the enviroment... You can see the displacement, but it needs a Subdiv modifier'

---


Frames captured — see "Captured Frames" section below.


### POLIGON TEXTURES [0:00]

### There are still a couple of things you need to do to really get the most out of them! [0:10]

### In the material tab under Settings go and choose "True" as the displacement type. TAB in and out of edit mode to update the mesh. [1:05]

### A bit dark... increase the brightness of the enviroment... You can see the displacement, but it needs a Subdiv modifier [1:19]
**Transcript (timestamped):**
[1:30] darken make up, S accidentally
[1:54] shine
[1:56] down



---

## Captured Frames

- [0:05] tutorials/frames/daily-blender-tip-65---properly-use-poliigon-textures-and-add-on/frame_000.jpg
- [0:10] tutorials/frames/daily-blender-tip-65---properly-use-poliigon-textures-and-add-on/frame_001.jpg
- [0:30] tutorials/frames/daily-blender-tip-65---properly-use-poliigon-textures-and-add-on/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-65---properly-use-poliigon-textures-and-add-on/frame_003.jpg
- [1:19] tutorials/frames/daily-blender-tip-65---properly-use-poliigon-textures-and-add-on/frame_004.jpg
- [1:50] tutorials/frames/daily-blender-tip-65---properly-use-poliigon-textures-and-add-on/frame_005.jpg

---

## Structured Notes

### Core Technique
Getting real geometric displacement to actually work with **Poliigon** PBR textures (installed via Poliigon's free add-on): the imported material's auto-wired **Displacement** node output needs the object properly **UV unwrapped** and its Material Settings **Displacement** dropdown switched from the default Bump-only mode to **True** (real geometric displacement), which requires re-entering Edit Mode to force a mesh update and adding a **Subdivision Surface** modifier for enough geometry resolution to actually displace.

### Summary
Frame 000 shows the Poliigon.com website's texture browser (metal spheres category), captioned "Poliigon (Andrew Price's texture site) has a free add-on that allows you to install the materials easily. But..." Frame 001 shows the same browser filtered to Metal category with more material swatches, captioned "There are still a couple of things you need to do to really get the most out of them!" Frame 002 shows a plain flat plane in the viewport, captioned "Press u in edit mode and choose Unwrap" — the object must be UV unwrapped for the Poliigon material's image textures to map correctly. Frame 003 shows the plane now covered in a gravel/rock PBR texture with the Material Settings panel open (Surface, Settings > Displacement dropdown), captioned "In the material tab under Settings go and choose 'True' as the displacement type. TAB in and out of edit mode to update the mesh." Frame 004 shows the same setup with the material looking dark/underlit, captioned "A bit dark... increase the brightness of the environment... You can see the displacement, but it needs a Subdiv modifier" — real displacement is visible but coarse without enough polygon density. Frame 005 shows the finished shader node graph feeding the material, captioned "Now it all works as it should! In render view, that is... Have fun!" — confirming the combination of unwrap + True displacement + Subdivision Surface + adequate lighting produces the correct final result.

### Key Steps
1. Install the free **Poliigon** add-on and download/apply a PBR material from Poliigon's library to an object.
2. **UV Unwrap** the object (Edit Mode, select all, **U > Unwrap**) — Poliigon's auto-generated material node setup relies on correct UVs for its Base Color, Roughness, Normal, and Displacement image textures to map properly.
3. In **Material Properties > Settings > Displacement**, change the dropdown from the default (Bump Only) to **True** (or "Displacement and Bump") to enable real geometric displacement instead of a fake normal-map-style bump.
4. **Tab** into and back out of Edit Mode to force Blender to recompute/update the mesh with the new displacement setting — the viewport doesn't always refresh automatically.
5. If the result looks too dark to judge, increase the scene/environment lighting brightness so the displaced surface detail is actually visible.
6. Add a **Subdivision Surface** modifier to the object — true displacement needs enough underlying geometry resolution to actually deform, otherwise the surface will look flat despite the correct settings.

### Nodes / Settings
- **Add-on:** Poliigon (free material-install add-on).
- **Edit Mode > U > Unwrap** — required for correct PBR texture mapping.
- **Material Properties > Settings > Displacement:** True/Displacement and Bump (instead of default Bump Only).
- **Subdivision Surface modifier** — required for visible real displacement detail.

### Difficulty
Beginner

### Blender Version
Not specified — Poliigon add-on + Material Settings Displacement dropdown (True/Bump) workflow is consistent with Cycles-based displacement across modern Blender versions.

### Tags
materials, workflow, add-on, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library share 2+ tags with this one, though [Easy PBR Textures - Blender Secrets](easy-pbr-textures---blender-secrets.md) covers the same True-displacement + Subdivision Surface pipeline (via Polyhaven/Node Wrangler instead of Poliigon) and is worth cross-referencing manually.
