---
title: Daily Blender Tip 46 - 2 Types Of Quick Fluids
source: YouTube
url: https://www.youtube.com/watch?v=eElKEBoKUG8
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Legacy \"Quick Fluid\" operator + FLIP Fluid domain (pre-Mantaflow-only-menu era; consistent with Blender 2.8x)"
tags: [fluid, simulation, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-46---2-types-of-quick-fluids/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 46 - 2 Types Of Quick Fluids

**Source:** [YouTube](https://www.youtube.com/watch?v=eElKEBoKUG8)
**Author:** Blender Secrets
**Duration:** 1m38s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 27 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (27 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] Core guy inconvenience
[1:38] Raid



---

## Captured Frames

- [0:10] tutorials/frames/daily-blender-tip-46---2-types-of-quick-fluids/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-46---2-types-of-quick-fluids/frame_001.jpg
- [0:50] tutorials/frames/daily-blender-tip-46---2-types-of-quick-fluids/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-46---2-types-of-quick-fluids/frame_003.jpg
- [1:20] tutorials/frames/daily-blender-tip-46---2-types-of-quick-fluids/frame_004.jpg
- [1:32] tutorials/frames/daily-blender-tip-46---2-types-of-quick-fluids/frame_005.jpg

---

## Structured Notes

### Core Technique
Using the **Quick Fluid** operator (Search menu, Space or F3) to instantly set up a full fluid simulation rig around any object — one variant makes the object itself the falling/settling fluid mass (Domain + auto-generated fluid source), the other makes it an **Inflow** source that continuously spawns fluid into a separate domain, producing an ongoing stream/fountain effect instead of a single splash.

### Summary
Frame 000 shows the Search menu (Space or F3) open with "Add Worm Gear" highlighted among other operators, over a Suzanne monkey head, captioned "SHIFT+A, Add a Monkey... or other object. Press SPACE, type 'quick fluid', choose Quick Fluid..." — the entry point for both fluid types. Frame 001 shows the completed first setup: the monkey head now shaded as a smooth fluid blob, a Fluid Domain panel open (Type: Domain, Bake, Resolution Final/Preview 65/45, Render/Viewport Display, Time Start/End, Generate Speed Vectors, Reverse Frames), captioned "Bam! Everything is set up. That cube is the 'Fluid domain'. Press 'Bake'. It will take a little while... take a nap." — the first fluid type: the object itself becomes a falling fluid mass inside an auto-created domain cube. Frame 002 shows a second, separate object (again monkey-shaped) with a wireframe overlay, captioned "Let's try another kind of Fluid! Start from a new object, Spacebar, Quick Fluid... just like before" — repeating Quick Fluid on a fresh object for the second type. Frame 003 shows the Physics panel with the wireframe object's Fluid Type set to **Inflow** (Enabled, Volume Initialization: Volume, Inflow Velocity X/Y/Z all 0 m/s), captioned "Make sure the wireframe object is selected (that's your original object) and in Type, this time choose Inflow." Frame 004 shows the Fluid Domain object selected again, captioned "Select the other object (the domain) and Bake again..." — baking the second simulation. Frame 005 shows the finished result: fluid continuously pouring/dripping down from the inflow-shaped source into a growing pool below, captioned "'Inflow' type causes a continuous flow of fluids" — confirming the ongoing-stream behavior versus a single splash.

### Key Steps
**Type 1 — Object becomes the fluid itself (a single splash/settle):**
1. Add any object (e.g. Suzanne).
2. Open the Search menu (Space or F3), type "quick fluid," and select **Quick Fluid**.
3. This auto-generates a bounding Domain cube and configures the original object as the fluid mass falling/settling within it — everything (Fluid, Domain type, Resolution, Time range) is pre-configured automatically.
4. Click **Bake** on the Domain object and wait for the simulation to compute.

**Type 2 — Object becomes an Inflow (continuous fluid stream):**
5. Start fresh with a new object and repeat: Space/F3 > Quick Fluid, exactly as before, to auto-generate a Domain.
6. Select the original (now wireframe-displayed) object and, in its Physics > Fluid settings, change **Type** from Domain/Flow to **Inflow** (Enabled, with adjustable Volume Initialization and Inflow Velocity X/Y/Z).
7. Select the separate Domain object and click **Bake** again.
8. Result: instead of a one-time falling/settling blob, the Inflow object continuously spawns new fluid into the domain for as long as the simulation runs, producing an ongoing pour/fountain/stream effect rather than a single splash.

### Nodes / Settings
- **Operator:** Quick Fluid (Search menu — Space or F3).
- **Fluid Domain:** Type: Domain, Bake, Resolution (Final/Preview), Render/Viewport Display, Time Start/End, Generate Speed Vectors, Reverse Frames.
- **Fluid Type (on the source object):** Domain (auto, Type 1) vs. **Inflow** (Type 2 — Enabled, Volume Initialization, Inflow Velocity X/Y/Z).

### Difficulty
Beginner

### Blender Version
Legacy "Quick Fluid" operator + FLIP Fluid domain — this menu-driven Quick Fluid setup and its UI (Domain/Flow/Inflow terminology) is consistent with Blender 2.8x-era fluid simulation, predating the later Mantaflow panel redesign.

### Tags
fluid, simulation, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover the legacy Quick Fluid operator or Inflow fluid sources.
