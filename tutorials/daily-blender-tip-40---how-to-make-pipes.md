---
title: Daily Blender Tip #40 - How To Make Pipes
source: YouTube
url: https://www.youtube.com/watch?v=v6mJ6XJatUI
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Curve conversion + Bevel Object workflow, version-agnostic core tools"
tags: [modelling, procedural, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-40---how-to-make-pipes/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip #40 - How To Make Pipes

**Source:** [YouTube](https://www.youtube.com/watch?v=v6mJ6XJatUI)
**Author:** Blender Secrets
**Duration:** 2m51s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'MAKE PIPES'
- **CRITICAL:** Empty transcript in chapter 'First, add any object to a scene. A plane, box, monkey...'
- **CRITICAL:** Empty transcript in chapter 'Shift+CTRL+B bevels vertices, middle mouse button makes it rounder.'
- **CRITICAL:** Total transcript only 98 chars (min 500). Captions unavailable or audio silent — extraction will be poor.

---


Frames captured — see "Captured Frames" section below.


### MAKE PIPES [0:00]

### First, add any object to a scene. A plane, box, monkey... [0:07]

### Shift+CTRL+B bevels vertices, middle mouse button makes it rounder. [0:49]

### Shift+A to add, choose a Curve, Circle. Location doesn't matter... [1:12]
**Transcript (timestamped):**
[2:30] versión total of terms is downloaded to the homepage require screening ask
[2:36] subtthly
[2:40] version
[2:45] to
[2:54] ray



---

## Captured Frames

- [0:07] tutorials/frames/daily-blender-tip-40---how-to-make-pipes/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-40---how-to-make-pipes/frame_001.jpg
- [0:49] tutorials/frames/daily-blender-tip-40---how-to-make-pipes/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-40---how-to-make-pipes/frame_003.jpg
- [1:20] tutorials/frames/daily-blender-tip-40---how-to-make-pipes/frame_004.jpg
- [1:52] tutorials/frames/daily-blender-tip-40---how-to-make-pipes/frame_005.jpg
- [2:10] tutorials/frames/daily-blender-tip-40---how-to-make-pipes/frame_006.jpg
- [2:40] tutorials/frames/daily-blender-tip-40---how-to-make-pipes/frame_007.jpg

---

## Structured Notes

### Core Technique
Turning any mesh object's edges into pipe-shaped 3D tubes: merge all the object's vertices down to a single central edge path (a "skeleton"), bevel the sharp corners of that path for smooth rounded bends, convert it to a Curve, then assign a Circle as its Bevel Object to give it real pipe thickness — with the circle itself editable in Edit Mode to add banded/ridged detail along the pipe's length.

### Summary
Frame 000 shows the Add menu with Curve highlighted, over an otherwise empty scene, captioned "First, add any object to a scene. A plane, box, monkey..." — any starting mesh works as raw material for the pipe path. Frame 001 shows a bare 3D cursor gizmo in an empty viewport, captioned "In edit mode select all (A) and then ALT+M and merge all vertices" — the step that collapses the source object down to a single central skeleton point/path. Frame 002 shows a simple stepped zigzag edge path (like a plumbing elbow shape) with sharp right-angle corners, captioned "Shift+CTRL+B bevels vertices, middle mouse button makes it rounder" — smoothing the sharp corners into rounded pipe bends. Frame 003 shows the same path now with visibly rounded corners and additional vertices along the curves, captioned "Alt+C and choose Curve from Mesh to turn it into a curve..." — converting the mesh edge path into a real Curve object. Frame 004 shows just the bare curve outline (no thickness yet), captioned "Shift+A to add, choose a Curve, Circle. Location doesn't matter..." — adding a Circle curve to use as the pipe's cross-section/Bevel Object. Frame 005 shows the finished round 3D pipe with the profile Circle's control points visible and selected in Edit Mode, captioned "Let's have some fun! Add more detail to the Circle in edit mode..." — editing the bevel-object circle itself (e.g. adding an inset/relief ring) to change the pipe's cross-sectional detail. Frame 006 shows several additional ring copies of the modified circle profile positioned at intervals along the pipe, captioned "Just duplicate the circles in edit mode and move them with G + X or Z" — placing repeated raised bands/ridges along the pipe's length. Frame 007 shows the final rendered result: a smooth, rounded gray pipe with evenly-spaced raised ridge bands running along its length, resembling flexible ducting or a machined pipe fitting.

### Key Steps
1. Add any starting object to the scene (a plane, cube, Suzanne — the actual shape doesn't matter, since it will be reduced to just its vertex layout).
2. In Edit Mode, select all (A) and Merge all vertices (Alt+M) down to a single point/skeleton — collapsing the object into a bare edge-path shape that traces where the pipe should run.
3. Use Shift+Ctrl+B (Bevel Vertices) on sharp corners along the path, scrolling the middle mouse button to add more segments for smoother, rounder bends at each joint.
4. Convert the beveled edge path to a real Curve object with **Alt+C** (Convert to Curve) — the mesh's edge skeleton becomes a Curve's spline.
5. Add a **Curve > Circle** (Shift+A) anywhere in the scene — its position doesn't matter, since it will only be used as a cross-section reference.
6. Assign that Circle as the path curve's **Bevel Object** (in Curve Properties > Geometry > Bevel) — the flat path now reads as a real round 3D pipe following the circle's cross-sectional shape.
7. For added detail/interest, edit the Circle profile itself in Edit Mode — e.g. inset or reshape part of its ring to add a raised band or groove — since any change to this profile propagates along the entire pipe's length automatically.
8. To place repeated ridge/band details at specific points rather than uniformly along the whole pipe, duplicate the modified circle profile in Edit Mode and move the duplicates along the pipe's length axis (G, then X or Z) to position each ridge individually.

### Nodes / Settings
- **Mesh cleanup:** Select All (A), Merge Vertices (Alt+M) — collapses any object into a bare edge-path skeleton.
- **Modeling:** Shift+Ctrl+B (Bevel Vertices, scroll for segments) for rounded corners.
- **Curve conversion:** Alt+C (Convert Mesh to Curve).
- **Curve Properties > Geometry > Bevel:** Object field set to a Circle curve — gives the path curve real pipe thickness/cross-section.
- **Detailing:** editing the Bevel Object circle's own geometry (inset/reshape) in Edit Mode to change the pipe's cross-sectional profile; duplicating and repositioning (G, X/Z) profile copies for localized ridge/band detail along the pipe.

### Difficulty
Beginner

### Blender Version
Not specified — Curve conversion and Bevel Object are version-agnostic core Blender tools.

### Tags
modelling, procedural, beginner

---

## Related Tutorials
- [How to model ornamental iron railings in Blender using Curves - Blender Secrets](how-to-model-ornamental-iron-railings-in-blender-using-curves---blender-secrets.md) — shares modelling, procedural; both build a custom Bevel Object from a mesh-derived curve to give a path curve real 3D thickness, this simpler tip on plain pipe shapes vs. that video's beveled-square railing profile.
