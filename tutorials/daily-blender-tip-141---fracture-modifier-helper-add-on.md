---
title: Daily Blender Tip 141 - Fracture Modifier: Helper Add-on
source: YouTube
url: https://www.youtube.com/watch?v=Tc3Q_OzR628
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Custom \"Fracture Modifier\" build of Blender (third-party fork, not stock Blender), same as Tips 139-140"
tags: [rigid-body, simulation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-141---fracture-modifier-helper-add-on/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 141 - Fracture Modifier: Helper Add-on

**Source:** [YouTube](https://www.youtube.com/watch?v=Tc3Q_OzR628)
**Author:** Blender Secrets
**Duration:** 1m52s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 131 chars (min 500). Captions unavailable or audio silent — extraction will be poor.

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] You can also add tunnel as the purposes of the application.
[1:45] In a new class, you will build a line correctly by origin配 born type 응.



---

## Captured Frames

- [0:10] tutorials/frames/daily-blender-tip-141---fracture-modifier-helper-add-on/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-141---fracture-modifier-helper-add-on/frame_001.jpg
- [0:50] tutorials/frames/daily-blender-tip-141---fracture-modifier-helper-add-on/frame_002.jpg
- [1:10] tutorials/frames/daily-blender-tip-141---fracture-modifier-helper-add-on/frame_003.jpg
- [1:30] tutorials/frames/daily-blender-tip-141---fracture-modifier-helper-add-on/frame_004.jpg
- [1:45] tutorials/frames/daily-blender-tip-141---fracture-modifier-helper-add-on/frame_005.jpg

---

## Structured Notes

### Core Technique
A third-party helper add-on (a separate .py file, installed the standard way) that streamlines the Fracture Modifier build's workflow with one-click "Add Fracture" / "Add Rigid Body" buttons and quality-of-life toggles, rather than manually digging through the Fracture Settings panels covered in Tips 139-140.

### Summary
Frame 000 shows the setup: a pink/magenta cube resting on a scattered pile of gray/green rock fragments, captioned "Fracture Modifier Helper Add-on." Frame 001 shows Blender's User Preferences > Add-ons "Install add-on from file" file browser, with two files visible in the target folder — "fracture_helper.py" (221 KB) and what looks like "pkg/fracturemodifier.py" (14.2 KB) — captioned "Install it in User Preferences ('Install add-on from file')." Frame 002 shows the resulting Tool panel added to the 3D viewport sidebar: **Main operations** (Add Fracture, Add RigidBody buttons), 3D View Settings (Toggle Wireframe, Toggle Relationship Lines), Generate smaller shards, Timing, Automations, Smoke/Dust/Debris (All Emissions, Inner Smoke, Dust, Debris, Create Brush, Brush Fadeout, Set Brush Fadeout, Collision on selected objects) — captioned "Now you can find it in the tool panel," shown alongside a pink cube and a green cube in the viewport. Frame 003 shows the same tool panel again, captioned "It lets you quickly set rigid bodies and fracture objects" — confirming the add-on's core value: one-click setup instead of manual per-panel configuration. Frame 004 shows the Rigid Body Dynamics deactivation settings (Enable Deactivation checked, Start Deactivated checked, Linear Vel 0.400, Angular Vel 0.500, Force Thresh) alongside Surface Response (Friction 0.500, Bounciness 0.000) and Damping (Translation 0.040, Rotation 0.100), captioned "Let's start deactivated so it doesn't shatter immediately" — a specific setting the helper add-on makes easy to toggle, keeping a fractured object visually intact until it's actually disturbed. Frame 005 shows the final demo result: the pink cube sitting stably on its bed of pre-generated rock debris (the "Smoke/Dust/Debris" pile), unchanged from the opening shot — confirming the "Start Deactivated" setting successfully prevented the object from shattering prematurely.

### Key Steps
1. Download the helper add-on's files (in this case a "fracture_helper.py" script alongside the base "fracturemodifier.py").
2. Install it via Blender User Preferences > Add-ons > **Install add-on from file**, pointing at the downloaded .py file, then enable it.
3. Once enabled, a new **Tool panel** section appears in the 3D viewport sidebar with one-click **Add Fracture** and **Add RigidBody** buttons — replacing the need to manually enable each physics type and dig through settings panels separately.
4. Additional convenience toggles in the same panel: Toggle Wireframe, Toggle Relationship Lines (visual debug aids), Generate Smaller Shards, Timing/Automations controls, and a Smoke/Dust/Debris section (emission controls, a Debris "Create Brush" tool with adjustable Brush Fadeout, and Collision on Selected Objects) for scattering pre-made rubble/dust around a fracture setup.
5. **Prevent premature shattering:** in the Rigid Body Dynamics deactivation settings, enable **Enable Deactivation** and **Start Deactivated** — this keeps a fractured object visually intact and stable at the start of the simulation (rather than immediately falling apart from its own rigid body jitter) until something actually disturbs it enough to exceed the Linear/Angular Velocity or Force thresholds.

### Nodes / Settings
- **Helper add-on Tool panel:** Add Fracture, Add RigidBody (one-click setup buttons), Toggle Wireframe, Toggle Relationship Lines, Generate Smaller Shards, Timing, Automations, Smoke/Dust/Debris (All Emissions, Inner Smoke, Dust, Debris, Create Brush, Brush Fadeout, Collision on Selected Objects).
- **Rigid Body Dynamics (Deactivation):** Enable Deactivation, Start Deactivated, Linear Velocity threshold, Angular Velocity threshold, Force Threshold — keeps a fractured object stable until disturbed.
- **Rigid Body (other visible settings):** Surface Response (Friction, Bounciness), Damping (Translation, Rotation).

### Difficulty
Intermediate

### Blender Version
Custom "Fracture Modifier" build of Blender (third-party fork, not stock Blender) — same non-standard build referenced in Tips 139-140, plus a separately-installed third-party helper add-on script on top of it.

### Tags
rigid-body, simulation, intermediate

---

## Related Tutorials
- [Daily Blender Tip 139 - Blender Fracture Modifier Build - Quick Start](daily-blender-tip-139---blender-fracture-modifier-build---quick-start.md) — shares rigid-body, simulation; this helper add-on streamlines exactly the manual Fracture Settings workflow taught there into one-click buttons.
- [Daily Blender Tip 140 - Fracture Modifier: Use Constraints](daily-blender-tip-140---fracture-modifier-use-constraints.md) — shares rigid-body, simulation, intermediate; complementary Fracture Modifier build tip, constraint-breaking Angle tuning there vs. this workflow-speedup add-on.
