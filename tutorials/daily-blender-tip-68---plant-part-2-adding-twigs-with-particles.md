---
title: Daily Blender Tip 68 - Plant Part 2: Adding Twigs With Particles
source: YouTube
url: https://www.youtube.com/watch?v=HqwpZutERRU
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Hair Particle System with Group render mode is a version-agnostic core Blender feature"
tags: [particles, procedural, organic, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-68---plant-part-2-adding-twigs-with-particles/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 68 - Plant Part 2: Adding Twigs With Particles

**Source:** [YouTube](https://www.youtube.com/watch?v=HqwpZutERRU)
**Author:** Blender Secrets
**Duration:** 1m53s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'ADD TWIGS (MAKE A PLANT PART 2)'
- **CRITICAL:** Empty transcript in chapter 'In edit mode select the root vertex, Shift+S, cursor to selected, Ctrl+Shift+Alt+C, origin to 3d cursor'
- **CRITICAL:** Empty transcript in chapter 'Play with the rotation settings like Phase until you like what you see.'
- **CRITICAL:** Total transcript only 6 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (6 chars) in 'Switch the particles to "Group" and choose the group of twigs.'

---


Frames captured — see "Captured Frames" section below.


### ADD TWIGS (MAKE A PLANT PART 2) [0:00]

### In edit mode select the root vertex, Shift+S, cursor to selected, Ctrl+Shift+Alt+C, origin to 3d cursor [0:10]

### Switch the particles to "Group" and choose the group of twigs. [0:52]
**Transcript (timestamped):**
[1:30] afraid


### Play with the rotation settings like Phase until you like what you see. [1:37]


---

## Captured Frames

- [0:05] tutorials/frames/daily-blender-tip-68---plant-part-2-adding-twigs-with-particles/frame_000.jpg
- [0:10] tutorials/frames/daily-blender-tip-68---plant-part-2-adding-twigs-with-particles/frame_001.jpg
- [0:52] tutorials/frames/daily-blender-tip-68---plant-part-2-adding-twigs-with-particles/frame_002.jpg
- [1:10] tutorials/frames/daily-blender-tip-68---plant-part-2-adding-twigs-with-particles/frame_003.jpg
- [1:35] tutorials/frames/daily-blender-tip-68---plant-part-2-adding-twigs-with-particles/frame_004.jpg
- [1:50] tutorials/frames/daily-blender-tip-68---plant-part-2-adding-twigs-with-particles/frame_005.jpg

---

## Structured Notes

### Core Technique
Scattering smaller twig objects (built with the same Skin-modifier vertex-skeleton technique as [Daily Blender Tip 66](daily-blender-tip-66---quick-tree-trunk-with-skin-modifier.md)) across a tree trunk/stump surface using a **Hair-type Particle System** set to **Group** render mode — with Rotation set to Normal (aligning twigs to the stump's face normals) and randomized scale/rotation for natural variation.

### Summary
Frame 000 shows the branching trunk/stump model with a small twig object nearby, captioned "These twigs were made like the base stump in TIP nr. 66. Make sure the origins are at the base of the twigs." — twig objects must have their origin point at their base so they attach correctly when instanced. Frame 001 shows the same scene with a Snap menu open (Geometry to Origin, Origin to Geometry, Origin to 3D Cursor, Origin to Center of Mass options), captioned "In edit mode select the root vertex, Shift+S, cursor to selected, Ctrl+Shift+Alt+C, origin to 3d cursor" — precisely placing the twig's origin at its base vertex. Frame 002 shows the Particle System panel with **Render > Group** selected and a group of twig objects assigned, the stump now covered in scattered twig instances, captioned "Switch the particles to 'Group' and choose the group of twigs." Frame 003 shows a denser, more naturally-oriented result with the Particle System's **Rotation** section enabled and set to **Normal**, captioned "Turn on Rotation and set it to Normal. This aligns the twigs with the faces of the stump. Increase randomness." Frame 004 shows a refined, less-cluttered result with fewer, better-sized twigs, captioned "There's way too many, turn down the amount of particles. Play with the size and size randomness." Frame 005 is the closing card.

### Key Steps
1. Build small twig objects using the same vertex-skeleton + **Skin modifier** technique from Tip 66, ensuring each twig's **object origin** sits at its base (where it should attach to the trunk).
2. To precisely set a twig's origin: in Edit Mode select the root/base vertex, **Shift+S > Cursor to Selected**, then **Ctrl+Shift+Alt+C > Origin to 3D Cursor**.
3. Group the twig objects together (e.g. via a Blender Collection/Group), then on the trunk/stump object add a **Particle System** and set **Render > Group**, selecting that twig group as the instanced content.
4. Enable **Rotation** in the Particle System settings and set the rotation source to **Normal** — this aligns each scattered twig with the local surface normal of the face it lands on, so twigs point outward from the trunk correctly.
5. Increase **Randomness** (rotation/phase) so twigs don't all look identically oriented.
6. Reduce the particle **Amount** if the initial scatter is too dense/cluttered, and tune **Size** and **Size Randomness** for natural-looking variation in twig scale.

### Nodes / Settings
- **Particle System > Render:** Group (instances a Collection/Group of twig objects instead of a single object).
- **Particle System > Rotation:** enabled, set to Normal (aligns instances to surface normals); Randomize Rotation/Phase for variation.
- **Particle System:** Amount, Size, Size Randomness.
- **Origin tools:** Shift+S (Cursor to Selected), Ctrl+Shift+Alt+C (Origin to 3D Cursor) — for correctly placing each twig's attachment point.

### Difficulty
Intermediate

### Blender Version
Not specified — Hair Particle System with Group render mode is a version-agnostic core Blender feature.

### Tags
particles, procedural, organic, intermediate

---

## Related Tutorials
- [Daily Blender Tip 66 - Quick Tree Trunk With Skin Modifier](daily-blender-tip-66---quick-tree-trunk-with-skin-modifier.md) — shares modelling→particles workflow and organic tag; this is the direct Part 1 prerequisite, providing the base stump and twig-building technique that this tutorial scatters via Particles.
