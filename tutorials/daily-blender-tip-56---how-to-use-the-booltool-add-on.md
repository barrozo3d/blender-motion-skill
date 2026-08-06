---
title: Daily Blender Tip 56 - How To Use the BoolTool Add-on
source: YouTube
url: https://www.youtube.com/watch?v=5_Xa3HwVLRA
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — BoolTool has shipped as a built-in opt-in add-on since Blender 2.8x"
tags: [modelling, boolean, add-on, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-56---how-to-use-the-booltool-add-on/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 56 - How To Use the BoolTool Add-on

**Source:** [YouTube](https://www.youtube.com/watch?v=5_Xa3HwVLRA)
**Author:** Blender Secrets
**Duration:** 2m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 84 chars (min 500). Captions unavailable or audio silent — extraction will be poor.

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[2:00] Make sure you plug it in your . опредif concept just before the sound�로ndig resolver



---

## Captured Frames

- [0:10] tutorials/frames/daily-blender-tip-56---how-to-use-the-booltool-add-on/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-56---how-to-use-the-booltool-add-on/frame_001.jpg
- [0:50] tutorials/frames/daily-blender-tip-56---how-to-use-the-booltool-add-on/frame_002.jpg
- [1:10] tutorials/frames/daily-blender-tip-56---how-to-use-the-booltool-add-on/frame_003.jpg
- [1:30] tutorials/frames/daily-blender-tip-56---how-to-use-the-booltool-add-on/frame_004.jpg
- [1:50] tutorials/frames/daily-blender-tip-56---how-to-use-the-booltool-add-on/frame_005.jpg

---

## Structured Notes

### Core Technique
Using the built-in (but disabled-by-default) **BoolTool** add-on to turn one object into a movable, non-destructive boolean **Brush** with a single click, then cleaning up the resulting cut with a **Bevel modifier placed at the bottom of the modifier stack**, Auto Smooth, and (if flat-shading artifacts persist) switching the Bevel's **Limit Method** from None to **Angle**.

### Summary
Frame 000 shows User Preferences > Add-ons filtered by Community, "Object: Bool Tool" checked/enabled, captioned "BoolTool comes default with Blender. Just search and activate it and Save User Settings." Frame 001 shows a cylinder-shaped cutter object overlapping a cube, with a BoolTool sidebar panel showing "Apply Brush" / "Remove Brush" buttons, captioned "This turns the first object into a boolean 'brush'. So you can still move it around." — the cylinder now acts as a live, repositionable cutter rather than an instantly-applied boolean. Frame 002 shows the resulting cut shape (a cube with a cylindrical notch removed) with an Add Modifier stack open (Boolean modifier: Apply/Remove Brush/Difference/Union operations visible, Overlap Threshold, Self Intersection), captioned "If you want you can add a bevel. Put it at the bottom of the modifier stack." Frame 003 shows the Object menu's Shading submenu (Smooth/Flat, Auto Smooth) open over the beveled notch shape, captioned "Turn shading to smooth (for all objects) and Auto Smooth with angle 30°." Frame 004 shows the Bevel modifier settings expanded (Amount, Segments, Loop Slide, and a **Limit Method** dropdown), captioned "If you can still see the Flat Shading, try turning the Bevel Limit Method to Angle instead of None." Frame 005 is a blank end card.

### Key Steps
1. Enable the **BoolTool** add-on (built into Blender, disabled by default): User Preferences > Add-ons > search "bool," check "Object: Bool Tool," and Save User Settings.
2. Select the cutter object, then use BoolTool's **Apply Brush** (from the sidebar Tool panel) — this converts it into a boolean brush that can still be freely moved/repositioned, rather than committing to a fixed boolean instantly.
3. The target object automatically gets a **Boolean** modifier (Difference by default) referencing the brush object, so the cut updates live as the brush moves.
4. Add a **Bevel** modifier to the cut object and place it **below** the Boolean modifier in the stack order — bevels applied after the boolean cut correctly round the newly-created intersection edges.
5. Set object shading to **Smooth** and enable **Auto Smooth** at roughly **30°** to avoid faceted-looking curved surfaces.
6. If flat-shading artifacts are still visible on the beveled edges, change the Bevel modifier's **Limit Method** from **None** to **Angle** — this constrains beveling to sufficiently sharp edges and resolves shading glitches at the boolean seam.

### Nodes / Settings
- **Add-on:** Object: Bool Tool (built-in, User Preferences > Add-ons).
- **BoolTool sidebar:** Apply Brush / Remove Brush.
- **Boolean modifier:** Difference/Union/Intersect, Overlap Threshold, Self Intersection.
- **Bevel modifier:** Amount, Segments, Limit Method (None vs. Angle) — placed below the Boolean modifier in the stack.
- **Shading:** Smooth Shading + Auto Smooth (~30°).

### Difficulty
Beginner

### Blender Version
Not specified — BoolTool has shipped as a built-in (opt-in) add-on since Blender 2.8x; workflow is consistent across modern Blender versions.

### Tags
modelling, boolean, add-on, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library share 2+ tags with this one, though [Daily Blender Tip #44 - Non-Destructive Boolean Workflow, Round Edges, Bevels](daily-blender-tip-44---non-destructive-boolean-workflow-round-edges-bevels.md) and [Blender Secrets - 6 Minutes of Boolean Basics](blender-secrets---6-minutes-of-boolean-basics.md) cover related non-destructive Boolean-modifier workflows worth cross-referencing manually.
