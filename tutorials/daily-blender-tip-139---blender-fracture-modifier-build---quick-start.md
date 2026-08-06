---
title: Daily Blender Tip 139 - Blender Fracture Modifier Build - Quick Start
source: YouTube
url: https://www.youtube.com/watch?v=6Tk22EdbbLc
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Custom \"Fracture Modifier\" build of Blender (a third-party/experimental fork, not stock Blender) — explicitly named in the title"
tags: [rigid-body, simulation, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-139---blender-fracture-modifier-build---quick-start/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 139 - Blender Fracture Modifier Build - Quick Start

**Source:** [YouTube](https://www.youtube.com/watch?v=6Tk22EdbbLc)
**Author:** Blender Secrets
**Duration:** 1m30s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'FRACTURE MODIFIER'
- **CRITICAL:** Empty transcript in chapter 'Add a rigid body system to the ground plane.'
- **CRITICAL:** Empty transcript in chapter 'Set it to "passive".'
- **CRITICAL:** Empty transcript in chapter 'Add a Fracture system to the other object.'
- **CRITICAL:** Empty transcript in chapter 'Enter an amount of shards. In this case, 1000'
- **CRITICAL:** Empty transcript in chapter 'Press "Execute Fracture". Wait... then press Alt+A.'
- **CRITICAL:** Total transcript only 19 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (19 chars) in 'Check the description for more info...'

---


Frames captured — see "Captured Frames" section below.


### FRACTURE MODIFIER [0:00]

### Add a rigid body system to the ground plane. [0:13]

### Set it to "passive". [0:25]

### Add a Fracture system to the other object. [0:37]

### Enter an amount of shards. In this case, 1000 [0:47]

### Press "Execute Fracture". Wait... then press Alt+A. [0:59]

### Check the description for more info... [1:11]
**Transcript (timestamped):**
[1:30] Hello, and welcome!



---

## Captured Frames

- [0:13] tutorials/frames/daily-blender-tip-139---blender-fracture-modifier-build---quick-start/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-139---blender-fracture-modifier-build---quick-start/frame_001.jpg
- [0:37] tutorials/frames/daily-blender-tip-139---blender-fracture-modifier-build---quick-start/frame_002.jpg
- [0:47] tutorials/frames/daily-blender-tip-139---blender-fracture-modifier-build---quick-start/frame_003.jpg
- [0:59] tutorials/frames/daily-blender-tip-139---blender-fracture-modifier-build---quick-start/frame_004.jpg
- [1:15] tutorials/frames/daily-blender-tip-139---blender-fracture-modifier-build---quick-start/frame_005.jpg

---

## Structured Notes

### Core Technique
A quick-start for the **Fracture Modifier build** — a special third-party/experimental fork of Blender (not part of stock Blender) that adds a dedicated Fracture system: an object is set up with Rigid Body physics as usual, then a separate **Fracture** modifier pre-shatters it into a large number of Voronoi+Boolean "shards" ahead of time, so a rigid body simulation can break it apart realistically when it collides with the ground.

### Summary
Frame 000 shows the test scene: an Einstein bust model sitting on a scattered rock/gravel ground plane, captioned "Add a rigid body system to the ground plane." Frame 001 shows the Physics properties tab's "Enable physics for" icon grid (Force Field, Collision, Cloth, Dynamic Paint, Soft Body, Fluid, Smoke, Rigid Body, **Fracture**) with Rigid Body sub-panels (Rigid Body Trigger Advanced, Rigid Body Collisions, Rigid Body Dynamics) visible, captioned "Set it to 'passive'" — the ground plane's Rigid Body Type set to Passive so it acts as an immovable floor. Frame 002 shows the Einstein bust with small colored gizmo markers on its head, captioned "Add a Fracture system to the other object" — enabling the Fracture physics type on the object that should break. Frame 003 shows the Fracture Settings panel (Fracture Presets: Prefractured, Fracture Algorithm: Voronoi + Boolean, Boolean Solver: Carver, Shard Count, Seed, Inner Material, Inner UV Map, Split Shards to Islands, Smooth Inner, Splinter X/Y/Length, Advanced Fracture Settings, Execute Fracture button) over the flat gravel plane, captioned "Enter an amount of shards. In this case, 1000." Frame 004 shows the same Fracture Settings panel, captioned "Press 'Execute Fracture'. Wait... then press Alt+A" — running the fracture computation (which takes time for 1000 shards) and then Alt+A to play the resulting rigid body simulation. Frame 005 shows the final result: the Einstein bust now visibly cracked into shard lines across its surface, sitting on its pedestal, captioned "Check the description for more info..." — the pre-fractured object ready to break apart realistically once the simulation runs and it interacts with the passive ground.

### Key Steps
1. Add a **Rigid Body** system to the ground/floor object and set its Rigid Body Type to **Passive** — it acts as an immovable collision surface for anything that falls onto it.
2. Select the object that should shatter (e.g. a bust/statue) and enable the **Fracture** physics type on it (alongside its own Rigid Body settings, implied active).
3. Open the Fracture Settings panel: choose a Fracture Preset (Prefractured shown), Fracture Algorithm (Voronoi + Boolean), Boolean Solver (Carver), and set the **Shard Count** — 1000 in this example — controlling how many pieces the object will be pre-divided into.
4. Click **Execute Fracture** and wait for the computation to finish (pre-fracturing a high shard count takes real time).
5. Once fracturing completes, press **Alt+A** to play the scene's rigid body simulation — the pre-shattered object now breaks apart realistically as it interacts with the passive ground plane.
6. The video points viewers to the description for more detailed information/links about the Fracture Modifier build itself (since it's a non-stock, separately-distributed version of Blender).

### Nodes / Settings
- **Rigid Body physics:** Type (Passive for the ground, Active implied for the fracturing object), Rigid Body Collisions, Rigid Body Dynamics, Rigid Body Trigger Advanced.
- **Fracture physics type + Fracture Settings panel:** Fracture Presets (Prefractured), Fracture Algorithm (Voronoi + Boolean), Boolean Solver (Carver), Shard Count, Seed, Inner Material, Inner UV Map, Split Shards to Islands, Smooth Inner, Splinter X/Y/Length, Advanced Fracture Settings, Execute Fracture button.
- **Playback:** Alt+A (play simulation after fracturing completes).

### Difficulty
Beginner

### Blender Version
Custom "Fracture Modifier" build of Blender (a third-party/experimental fork, not part of stock Blender) — explicitly named in the video title; not available in standard Blender releases.

### Tags
rigid-body, simulation, beginner

---

## Related Tutorials
- [Daily Blender Tip 140 - Fracture Modifier: Use Constraints](daily-blender-tip-140---fracture-modifier-use-constraints.md) — shares rigid-body, simulation; direct sequel covering Fracture Constraint Settings (Use Constraints, breaking Angle) that build on top of this tip's base Fracture Settings.
- [Daily Blender Tip 141 - Fracture Modifier: Helper Add-on](daily-blender-tip-141---fracture-modifier-helper-add-on.md) — shares rigid-body, simulation; a third-party add-on that streamlines this tip's manual Fracture Settings workflow into one-click Add Fracture/Add RigidBody buttons.
- [Daily Blender Tip 75 - More Fracture Stuff!](daily-blender-tip-75---more-fracture-stuff.md) — shares rigid-body, simulation; a simpler, stock-Blender alternative using the built-in Cell Fracture add-on + standard Rigid Body physics instead of this custom Fracture Modifier build.
