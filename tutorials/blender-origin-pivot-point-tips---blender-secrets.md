---
title: Blender Origin / Pivot Point Tips - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=t_r8qT_4oGM
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified"
tags: [beginner]
extraction_status: complete
frames_dir: tutorials/frames/blender-origin-pivot-point-tips---blender-secrets/
frame_count: 3
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Origin / Pivot Point Tips - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=t_r8qT_4oGM)
**Author:** Blender Secrets
**Duration:** 1m32s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this video we'll look at how to adjust the origin or the pivot point in Blender.
[0:04] The origin is the little orange dot. By default, the transform pivot point is set to medium.
[0:11] That means that Blender uses the origin as the pivot point for rotating and scaling objects.
[0:17] For that reason, it's important that the origin is where you need it to be.
[0:21] It also influences the center of gravity in objects when you use a rigid body simulation.
[0:28] When you're a beginner to Blender and you don't yet know the keyboard shortcuts for
[0:31] transformations, you can enable the gizmo. That way you have a visual way to transform the
[0:37] object around the pivot point. To only adjust the origin, make sure first that you are in
[0:42] object mode. Then from this option menu, choose the option effect only origins.
[0:48] And by the way, this option is only available in object mode, not in edit mode.
[0:52] Don't forget to turn this option off when you no longer need it.
[0:56] Alternatively, you can go to edit mode, press a to select everything, and then you can move the
[1:00] mesh independently of the origin. If you're coming from Maya and you're used to affecting
[1:04] the origin just by pressing D, you can enable this extension. You can toggle this option on and off
[1:10] by pressing the D key and then left mouse drag to place the origin where you want. Finally,
[1:15] to move the origin to the center of the object, select the object and then go to origin to geometry.
[1:21] Or shift and right click to place the 3D cursor somewhere and then choose origin to 3D cursor.
[1:27] For more tips, a Blender ebook and Blender courses go to 3dscrets.com.



---

## Captured Frames

- [0:37] tutorials/frames/blender-origin-pivot-point-tips---blender-secrets/frame_000.jpg
- [0:44] tutorials/frames/blender-origin-pivot-point-tips---blender-secrets/frame_001.jpg
- [1:18] tutorials/frames/blender-origin-pivot-point-tips---blender-secrets/frame_002.jpg

---

## Structured Notes

### Core Technique
A rundown of every way to move or set an object's origin (the orange dot / default rotate-scale pivot point) independently of its geometry, without accidentally moving the mesh itself.

### Summary
The origin matters because, with the default Median transform pivot point, Blender rotates and scales around it, and it also sets an object's center of gravity in rigid body sims. Covers: enabling the on-screen move/rotate/scale gizmo as a beginner-friendly alternative to keyboard shortcuts; Object Mode's "Affect Only → Origins" toggle (Object Mode only, must be manually toggled back off after use) to drag the origin without moving the mesh; the inverse — Edit Mode, Select All, then move the mesh independently of the origin; a Maya-style "Affect Only Origins" toggle bound to the D key (drag with left mouse) for artists used to Maya's origin workflow; and the standard Object → Set Origin → Origin to Geometry (centers the origin in the mesh) or Shift+Right-click to place the 3D Cursor then Origin to 3D Cursor (places the origin at an arbitrary point).

### Key Steps
1. Enable the on-screen transform gizmo (View → Gizmos, or the gizmo toggle in the header) for a visual, click-and-drag way to move/rotate/scale before you know the G/R/S shortcuts.
2. To move the origin without moving the mesh: in **Object Mode**, open the header's Options/context menu → **Affect Only → Origins**, then transform (G/R/S) as normal — only the origin moves. This option is unavailable in Edit Mode. Remember to toggle it back off afterward or all subsequent transforms will only move origins.
3. To move the mesh without moving the origin: go to **Edit Mode**, press **A** to select all geometry, then transform — the origin stays put since it's an object-level property, not mesh data.
4. Maya users: enable the "D-key affects only origins" preference/extension, then hold **D** and left-mouse-drag to place the origin interactively, matching Maya's muscle memory.
5. To center the origin in the mesh: **Object → Set Origin → Origin to Geometry**.
6. To place the origin at an arbitrary point: **Shift+Right-click** to move the 3D Cursor there, then **Object → Set Origin → Origin to 3D Cursor**.

### Nodes / Settings
- Header Options menu → Affect Only → Origins (Object Mode only)
- Object → Set Origin → Origin to Geometry / Origin to 3D Cursor
- Transform Pivot Point: Median (default) — determines what rotate/scale operate around
- Shortcuts: G/R/S (move/rotate/scale), A (select all, Edit Mode), Shift+Right-click (move 3D Cursor), D + LMB-drag (Maya-style origin drag, requires enabling the option first)

### Difficulty
Beginner

### Blender Version
Not specified.

### Tags
beginner

---

## Related Tutorials
No other ingested tutorials share 2+ tags with this one yet.
