---
title: Blender Secrets - Modeling Circular Hard Surface Details
source: YouTube
url: https://www.youtube.com/watch?v=tHnKR8DB1gg
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Curve modifier + Knife Project workflow, version-agnostic core tools"
tags: [modelling, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---modeling-circular-hard-surface-details/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - Modeling Circular Hard Surface Details

**Source:** [YouTube](https://www.youtube.com/watch?v=tHnKR8DB1gg)
**Author:** Blender Secrets
**Duration:** 1m30s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'Now turn the Curve modifier back on, and you've got yourself a nice circular scifi rectangle.'
- WARNING: Very short transcript (41 chars) in '<Untitled Chapter 1>'

---


Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Let's stretch out the default cube first.


### Let's stretch out the default cube first [0:04]
**Transcript (timestamped):**
[0:06] Draw a sci-fi design on it using the Annotate tool, then use boolean shapes to make it real.


### Adding slice cuts is easy by using Boolean cutters with Solidity modifiers on them. [0:12]
**Transcript (timestamped):**
[0:12] Adding slice cuts is easy by using boolean cutters with solidify modifiers on them.
[0:18] Fill the recessed parts with pipes and other details.
[0:21] Add a Bezier circle.
[0:23] Using the Curve modifier on the object, with the circle as the curve object, we can bend
[0:27] it.
[0:28] There's not enough geometry, so the result is a disaster.
[0:32] Add a plane, then add a lot of vertical edge loops with Ctrl R and scrolling the mouse wheel.
[0:36] Select all faces of the plane in edit mode and press X, delete only faces.
[0:41] Holding Shift, select the plane and then the cube in object mode.


### Holding Shift select the Plane and then the Cube in Object Mode. [0:42]
**Transcript (timestamped):**
[0:44] In Front View, go to edit mode and go to mesh, knife project.
[0:49] Now turn the curve modifier back on and you've got yourself a nice circular sci-fi rectangle.


### Now turn the Curve modifier back on, and you've got yourself a nice circular scifi rectangle. [0:50]

### If you like this tip, you'll also like the Blender Secrets e-book. [0:57]
**Transcript (timestamped):**
[0:57] If you like this tip, you'll also like the Blender Secrets ebook.
[1:01] With more than a thousand pages and more on the way.
[1:04] By clicking on a topic in the index, you're transported to the relevant pages.
[1:09] And clicking on the link at the bottom of the page takes you back to the index of 400
[1:13] plus topics.
[1:15] To see the corresponding video on a topic, simply click on the topic title.


### Updates are always free for customers both on Gumroad and Blender Market [1:21]
**Transcript (timestamped):**
[1:21] These are always free for customers both on Gumroad and Blender Market.



---

## Captured Frames

- [0:06] tutorials/frames/blender-secrets---modeling-circular-hard-surface-details/frame_000.jpg
- [0:18] tutorials/frames/blender-secrets---modeling-circular-hard-surface-details/frame_001.jpg
- [0:28] tutorials/frames/blender-secrets---modeling-circular-hard-surface-details/frame_002.jpg
- [0:44] tutorials/frames/blender-secrets---modeling-circular-hard-surface-details/frame_003.jpg
- [0:52] tutorials/frames/blender-secrets---modeling-circular-hard-surface-details/frame_004.jpg

---

## Structured Notes

### Core Technique
Turning a flat, hand-designed sci-fi panel pattern into a circular hard-surface detail band by modeling the pattern flat first (annotated sketch → Boolean cutters + Solidify slice cuts → Knife-Project-transferred pipe/greeble details on a dense plane), then bending the whole thing around a Bezier Circle using a Curve modifier.

### Summary
Frame 000 shows the very first step: a default cube stretched out into a long thin bar — the base shape the sci-fi panel will be built on top of. Frame 001 shows the boolean slice-cut technique mid-process: a blue-shaded cube with a visible diagonal cut and a Solidify modifier in the sidebar (Thickness 0.06m, Offset 1.0, Even Thickness, Rim Fill) — the boolean-cutter-plus-solidify combo used for quick panel-line slices. Frame 002 shows the low-geometry "disaster" mentioned in the transcript: a Curve modifier (Curve Object: BezierCircle, Deform Axis X) applied to a sci-fi-detailed plane, the bend badly faceted and jagged because the plane doesn't yet have enough vertical edge loops to bend smoothly. Frame 003 shows the Knife Project step: a dense, dark, tightly-ribbed plane positioned directly behind the finished sci-fi-detailed bar shape (both viewed from the front, arrows labeled "1" and "2" indicating the Shift-select order) — about to transfer the panel's shape via Knife Project onto the high-resolution plane. Frame 004 shows the finished payoff: the same sci-fi panel bar now smoothly curved into an arc via the same Curve modifier (BezierCircle, Deform Axis X) — "a nice circular sci-fi rectangle," confirming the extra geometry from the Knife Project step fixed the earlier faceting problem.

### Key Steps
1. Stretch the default cube into a long bar shape as the base panel.
2. Use the Annotate tool to sketch a sci-fi panel design directly onto the bar, then convert that sketch into real geometry using Boolean shapes.
3. For quick slice-cut panel lines, use Boolean cutter objects with a Solidify modifier applied to each cutter — an easy way to carve clean recessed panel gaps.
4. Fill the recessed panel areas with additional details like pipes and other greebles.
5. **First attempt at bending it into a circle:** add a Bezier Circle; apply a Curve modifier to the panel object with the circle set as its Curve Object to bend the shape along the circle's curvature. Result: since the panel doesn't have enough geometry along the bend axis, the curved result comes out badly faceted/broken-looking.
6. **Fix — add resolution via a dense reference plane and Knife Project:** add a Plane and give it many vertical edge loops (Ctrl+R, scroll the mouse wheel for more cuts); in Edit Mode select all its faces and press X > **Only Faces** (deleting faces but keeping the dense edge/vertex grid); in Object Mode, Shift-select the plane then the original detailed cube/bar (order matters for Knife Project's active-object requirement); switch to Front View, enter Edit Mode, and run Mesh > **Knife Project** to transfer/cut the panel shape onto the dense plane's high-resolution geometry.
7. Turn the Curve modifier back on (now targeting the newly-detailed, sufficiently-dense geometry) — the bend now comes out smooth and clean, producing a properly circular sci-fi panel band.

### Nodes / Settings
- **Modifiers:** Boolean (cutter objects), Solidify (Thickness, Offset, Even Thickness, Rim Fill — for slice-cut cutters), Curve (Curve Object: Bezier Circle, Deform Axis).
- **Tools:** Annotate tool (sketch guide), Ctrl+R (loop cuts for bend resolution), X > Only Faces (keep edges/verts, remove faces), Knife Project (Mesh menu, requires correct Shift-select order of target then reference).
- **Primitives:** Bezier Circle (curve-modifier bend target).

### Difficulty
Intermediate

### Blender Version
Not specified — Curve modifier and Knife Project are version-agnostic core Blender tools.

### Tags
modelling, procedural, intermediate

---

## Related Tutorials
- [Step by Step: Image File to 3D Geometry | Blender Secrets](step-by-step-image-file-to-3d-geometry-blender-secrets.md) — shares modelling, procedural; both rely on Knife Project to transfer a flat shape onto denser target geometry, applied here for bend-resolution rather than engraving a logo.
