---
title: Blender Secrets -  Scaling Tips for Better 3D Modeling
source: YouTube
url: https://www.youtube.com/watch?v=jlh275ZKsLw
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 3.3.0 -- observed in frame_003"
tags: [modelling, procedural, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---scaling-tips-for-better-3d-modeling/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets -  Scaling Tips for Better 3D Modeling

**Source:** [YouTube](https://www.youtube.com/watch?v=jlh275ZKsLw)
**Author:** Blender Secrets
**Duration:** 3m43s | 3 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Extruding [0:00]
**Transcript (timestamped):**
[0:00] When you have an inset phase that you want to scale up in a way that conforms to edges
[0:10] around it, pressing S to scale is not ideal when the geometry around the phase has a different
[0:16] shape.
[0:17] But pressing G twice conforms the inset phase to the surrounding edges as you scale it up.
[0:24] If you want to inset the phase but pressing CTRL I creates overlapping geometry, inset
[0:29] only a tiny bit, left click and press S to scale it further.
[0:33] When extruding these phases we can press ALT E for the extrude menu and choose extrude
[0:39] phases along normals.
[0:40] However, scaling down the extrusion doesn't give a desirable result in this case.
[0:45] Instead after extruding we left click to conform without scaling the extruded phases, then
[0:51] press S and then while scaling press SHIFT on the axis you want to exclude from the scaling
[0:55] operation.
[0:56] In this case the Y axis.
[0:58] In other words, in this example press S and then SHIFT Y.


### Skill Cage [1:05]
**Transcript (timestamped):**
[1:16] You probably know that you can scale objects uniformly by pressing S or on an axis by pressing
[1:21] S and that axis.
[1:23] For example, S and Y to scale along the Y axis.
[1:27] A lesser known method of scaling is the scale cage found in the tool panel.
[1:32] It adds a cage around one or more selected objects that allows you to scale them.
[1:37] You can drag the corner handles to scale proportionally or drag the center handles to scale on one
[1:42] axis.
[1:45] It always uses the opposite handle as the pivot point.
[1:51] This is handy for scaling multiple objects away from a specific point.
[1:56] Some options become available after using the tool.
[1:59] For example, fields for typing specific values.
[2:12] You can also use the tool on a selection in edit mode.
[2:22] If you scale in object mode, don't forget to apply the scale by pressing CTRL A and
[2:27] choosing scale.


### Shrink [2:30]
**Transcript (timestamped):**
[2:35] The shrink pattern transform option is useful for when you want to make a cylinder thicker
[2:40] without making it longer or shorter.
[2:43] You can shrink or flatten a selection in edit mode by pressing ALT S.
[2:51] Or find it in the mesh transform menu.
[2:56] Turning on proportional editing allows you to shrink or flatten the selection with proportional
[3:01] follow.
[3:02] By checking the connected option, parts of the mesh that are not connected like the
[3:06] eyes in this monkey will not be affected.
[3:09] It can also be a useful way to move vertices.
[3:12] For example, the selection in this ornament model.
[3:20] If you found this topic interesting and would like to know more, don't forget that you can
[3:24] find it in my Blender Secrets ebook, along with almost 2000 pages of other tips.
[3:30] To get an idea of what the ebook is like, you can download the free sample from my website.



---

## Captured Frames

- [0:20] tutorials/frames/blender-secrets---scaling-tips-for-better-3d-modeling/frame_000.jpg
- [0:35] tutorials/frames/blender-secrets---scaling-tips-for-better-3d-modeling/frame_001.jpg
- [0:55] tutorials/frames/blender-secrets---scaling-tips-for-better-3d-modeling/frame_002.jpg
- [1:35] tutorials/frames/blender-secrets---scaling-tips-for-better-3d-modeling/frame_003.jpg
- [2:00] tutorials/frames/blender-secrets---scaling-tips-for-better-3d-modeling/frame_004.jpg
- [2:40] tutorials/frames/blender-secrets---scaling-tips-for-better-3d-modeling/frame_005.jpg
- [3:05] tutorials/frames/blender-secrets---scaling-tips-for-better-3d-modeling/frame_006.jpg

---

## Structured Notes

### Core Technique
Three under-used scaling techniques: G,G (shape-conforming scale) and axis-excluding S+Shift for inset/extruded faces, the Scale Cage tool for interactive multi-object/edit-mode scaling from an opposite-corner pivot, and Shrink/Fatten (Alt+S) with Proportional Editing's Connected option for thickness-only adjustments that respect mesh topology boundaries.

### Summary
Frame 000 shows G,G (double-G "shape-conforming scale") in action on an inset face — a trapezoid-shaped inset conforming naturally to its non-rectangular surrounding edges as it's scaled, rather than distorting like a normal S-scale would. Frame 001 shows the result of Alt+E → Extrude Faces Along Normals on a similar inset window/frame shape, with Alt held to browse the extrude menu. Frame 002 shows the fix for scaling that extrusion cleanly: "Shift+Y" held during an S-scale to exclude the Y axis from the operation, keeping the extruded frame's depth consistent while only the other axes scale. Frame 003 shows the Scale Cage tool selected in the Toolbar, applied to a rusty vintage machine model — a wireframe cage with corner and edge-midpoint handles surrounds the selected object(s). Frame 004 shows the Scale Cage cage further in use on the same machine object, illustrating how it can wrap multiple selected objects together. Frame 005 is a clear before/after: a cylindrical handle/roller shape shown thin (top) and then noticeably thicker (bottom, red arrow) via Shrink/Fatten — its end caps (green) stay the same size while only the cylindrical body's radius increases, with length unchanged. Frame 006 shows a side-by-side comparison of Shrink/Fatten's "Connected" option on a Suzanne-like character head: with Connected unchecked (left) the operation affects all proportionally-nearby geometry including disconnected parts, while Connected checked (right) correctly isolates the effect so nearby-but-disconnected elements (like eyes) aren't dragged along.

### Key Steps
1. **Shape-conforming scale (G,G) for inset faces:** for an inset face you want to scale up so it conforms to non-uniform surrounding edges, pressing S scales uniformly and ignores the actual shape of the surrounding geometry — instead, press G twice (the "shape-conforming scale" shortcut) to scale the face while conforming its edges to the surrounding topology.
2. **Avoiding overlapping inset geometry:** if Ctrl+I (Inset Faces) creates unwanted overlaps, inset only a tiny amount first, left-click to confirm, then press S to scale it further afterward as a separate step.
3. **Extruding insets cleanly:** Alt+E → Extrude Faces Along Normals; scaling the extrusion down directly during the extrude often looks wrong. Instead, left-click first to confirm the extrusion without scaling, then separately press S and hold Shift plus the axis you want to *exclude* from scaling (e.g. S then Shift+Y to scale on all axes except Y) — keeps extrusion depth consistent while adjusting the rest.
4. **Scale Cage tool:** found in the Toolbar (alongside Move/Rotate/Select Box); wraps a draggable cage around one or more selected objects (works in Object Mode on multiple objects, or in Edit Mode on a mesh selection). Drag a corner handle to scale proportionally, or a center/edge handle to scale along a single axis; the cage always uses the *opposite* handle as the pivot point, which is handy for scaling several objects away from a specific reference point. After starting the tool, numeric input fields become available for typing exact scale values. If scaling objects in Object Mode with this tool, remember to Ctrl+A → Scale afterward to apply the resulting non-1.0 scale values.
5. **Shrink/Fatten for thickness-only adjustment:** press Alt+S in Edit Mode (or find it in the Mesh → Transform menu) to shrink or flatten (fatten) a selection along its own normals — ideal for making a cylinder thicker/thinner without changing its length. Enable Proportional Editing for a soft falloff (Proportional Follow) while shrinking/flattening; critically, check the **Connected** option so the effect only propagates through actually-connected geometry — this prevents nearby-but-disconnected mesh parts (e.g. eyes sitting near a face surface) from being unintentionally affected. Shrink/Fatten with proportional falloff is also a generally useful way to nudge groups of vertices (e.g. sculpting fine adjustments into an ornament model).

### Nodes / Settings
- **Scale operators:** G,G (shape-conforming scale), S (uniform/axis scale), S + Shift+[axis] (scale excluding one axis), Alt+S (Shrink/Fatten along normals).
- **Tool:** Scale Cage (Toolbar) — corner handles (proportional), edge/center handles (single-axis), opposite-handle pivot, numeric input fields after activation.
- **Edit-mode operators:** Ctrl+I (Inset Faces), Alt+E → Extrude Faces Along Normals.
- **Proportional Editing:** Proportional Follow, Connected option (isolates effect to actually-connected geometry).
- **Object Mode:** Ctrl+A → Scale (apply scale after using the Scale Cage tool on objects).

### Difficulty
Beginner to Intermediate

### Blender Version
Not specified — core transform-tool workflow, version-agnostic across modern Blender (2.9x-5.x).

### Tags
modelling, procedural, beginner, intermediate

---

## Related Tutorials
- [Blender Secrets - 5 minutes of Topology Tips](blender-secrets---5-minutes-of-topology-tips.md) — shares modelling, procedural, intermediate; same channel, overlapping general mesh-editing-technique subject matter.
- [Blender Secrets - Making Holes in Cylinders with decent Quad Topology](blender-secrets---making-holes-in-cylinders-with-decent-quad-topology.md) — shares modelling, procedural, intermediate; same channel, this video's Shrink/Fatten cylinder-thickening tip is directly relevant to detailing cylindrical hard-surface shapes.
