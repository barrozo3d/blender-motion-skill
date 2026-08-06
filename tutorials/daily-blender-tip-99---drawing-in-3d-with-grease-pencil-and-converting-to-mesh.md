---
title: Daily Blender Tip 99 - Drawing In 3D With Grease Pencil And Converting To Mesh
source: YouTube
url: https://www.youtube.com/watch?v=Fl8PXZWnxr4
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Grease Pencil 3D drawing, Curve conversion, and Mesh from Curve are version-agnostic core Blender features"
tags: [grease-pencil, modelling, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-99---drawing-in-3d-with-grease-pencil-and-converting-to-mesh/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 99 - Drawing In 3D With Grease Pencil And Converting To Mesh

**Source:** [YouTube](https://www.youtube.com/watch?v=Fl8PXZWnxr4)
**Author:** Blender Secrets
**Duration:** 1m48s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'GREASE PENCIL CONVERT TO MESH'
- **CRITICAL:** Empty transcript in chapter 'Grease Pencil can be used to quickly sketch out some concepts in 3D space.'
- **CRITICAL:** Empty transcript in chapter 'Add a new Grease Pencil object: SHIFT+A GreasePencil Blank And go to Draw Mode.'
- **CRITICAL:** Empty transcript in chapter 'In Edit Mode you can edit the individual points of the grease pencil stroke, as if it is a mesh.'
- **CRITICAL:** Empty transcript in chapter 'Now that it is a normal path you can add some thickness and resolution.'
- **CRITICAL:** Empty transcript in chapter 'Press F3 again and search for "convert to", then choose Mesh from Curve.'
- **CRITICAL:** Total transcript only 2 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (2 chars) in 'You probably will want to use a decimate modifier to make the resulting mesh less dense.'

---


Frames captured — see "Captured Frames" section below.


### GREASE PENCIL CONVERT TO MESH [0:00]

### Grease Pencil can be used to quickly sketch out some concepts in 3D space. [0:03]

### Add a new Grease Pencil object: SHIFT+A GreasePencil Blank And go to Draw Mode. [0:10]

### In Edit Mode you can edit the individual points of the grease pencil stroke, as if it is a mesh. [0:46]

### Now that it is a normal path you can add some thickness and resolution. [1:02]

### Press F3 again and search for "convert to", then choose Mesh from Curve. [1:12]

### You probably will want to use a decimate modifier to make the resulting mesh less dense. [1:25]
**Transcript (timestamped):**
[1:30] 거야



---

## Captured Frames

- [0:03] tutorials/frames/daily-blender-tip-99---drawing-in-3d-with-grease-pencil-and-converting-to-mesh/frame_000.jpg
- [0:10] tutorials/frames/daily-blender-tip-99---drawing-in-3d-with-grease-pencil-and-converting-to-mesh/frame_001.jpg
- [0:46] tutorials/frames/daily-blender-tip-99---drawing-in-3d-with-grease-pencil-and-converting-to-mesh/frame_002.jpg
- [1:02] tutorials/frames/daily-blender-tip-99---drawing-in-3d-with-grease-pencil-and-converting-to-mesh/frame_003.jpg
- [1:14] tutorials/frames/daily-blender-tip-99---drawing-in-3d-with-grease-pencil-and-converting-to-mesh/frame_004.jpg
- [1:40] tutorials/frames/daily-blender-tip-99---drawing-in-3d-with-grease-pencil-and-converting-to-mesh/frame_005.jpg

---

## Structured Notes

### Core Technique
Using **Grease Pencil** as a fast, freeform **3D sketching tool** (drawing strokes directly in 3D space, not just on a flat 2D canvas) to rough out organic/tube-like shapes, then converting the sketch into real editable mesh geometry via **Convert To > Mesh from Curve** — turning quick 3D doodles into usable, deformable 3D models with thickness and resolution.

### Summary
Frame 000 shows a rough white tube-like squiggle drawn freely in 3D perspective space, captioned "Grease Pencil can be used to quickly sketch out some concepts in 3D space." Frame 001 shows the Shift+A Add menu with **Grease Pencil > Blank** highlighted (Stroke and Monkey also available), captioned "Add a new Grease Pencil object: SHIFT+A > GreasePencil > Blank And go to Draw Mode." Frame 002 shows the drawn stroke now in Edit Mode with individual control points visible and selectable along the path, captioned "In Edit Mode you can edit the individual points of the grease pencil stroke, as if it is a mesh." Frame 003 shows the stroke converted into a **Curve** object (Geometry panel visible: Offset, Extrude, Taper Object, Bevel Depth/Resolution, Path Animation), the once-flat line now given visible thickness, captioned "Now that it is a normal path you can add some thickness and resolution." Frame 004 shows the F3 search menu with "convert to" typed and **Mesh from Curve** highlighted, the curve now a tube-shaped mesh, captioned "Press F3 again and search for 'convert to', then choose Mesh from Curve." Frame 005 shows the finished mesh geometry (a dense wireframe tube mesh) ready for further editing, in Edit Mode.

### Key Steps
1. Add a new Grease Pencil object via **Shift+A > Grease Pencil > Blank**, then switch to **Draw Mode**.
2. Freely draw strokes directly in 3D perspective space — Grease Pencil strokes aren't limited to a flat 2D plane, so this works as a rapid 3D concept-sketching tool.
3. Switch to **Edit Mode** on the Grease Pencil object to adjust individual stroke control points, similar to editing mesh vertices.
4. Convert the Grease Pencil stroke into a **Curve** object — this gives access to Curve **Geometry** settings like Bevel **Depth** (thickness) and **Resolution** (smoothness), turning the flat stroke into a tube-like 3D shape.
5. Press **F3**, search "convert to," and choose **Mesh from Curve** — this bakes the curve (with its bevel thickness) into real, editable mesh geometry.
6. Since curve-to-mesh conversion at high resolution can produce a very dense mesh, add a **Decimate** modifier afterward to reduce the polygon count to something more manageable.

### Nodes / Settings
- **Add menu:** Grease Pencil > Blank.
- **Grease Pencil > Edit Mode** — point-level stroke editing.
- **Curve Geometry:** Bevel Depth, Bevel Resolution (adds thickness/smoothness to the converted curve).
- **F3 > Convert To > Mesh from Curve.**
- **Modifier:** Decimate — recommended afterward to reduce resulting mesh density.

### Difficulty
Intermediate

### Blender Version
Not specified — Grease Pencil 3D drawing, Curve conversion, and Mesh from Curve are version-agnostic core Blender features (Grease Pencil as a first-class 3D object dates from Blender 2.8x).

### Tags
grease-pencil, modelling, procedural, intermediate

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover converting Grease Pencil strokes to mesh geometry.
