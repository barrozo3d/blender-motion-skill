---
title: Daily Blender Secrets - 10 ways to make Holes in Blender
source: YouTube
url: https://www.youtube.com/watch?v=oFg367w5Cpo
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (BoolTool + Carver + Box Cutter add-ons, native LoopTools; consistent with Blender 2.9x-5.x)"
tags: [modelling, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-secrets---10-ways-to-make-holes-in-blender/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Secrets - 10 ways to make Holes in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=oFg367w5Cpo)
**Author:** Blender Secrets
**Duration:** 2m55s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- WARNING: Partial frame capture: only 7/8 requested frames were captured.

---


Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Create a circle, place it in front or on top of the cube and go to orthographic view.


### Knife Project [0:04]
**Transcript (timestamped):**
[0:08] Select the circle, hold shift and select the cube as well.
[0:11] Go to edit mode and go to mesh, knife project.
[0:15] Now you can get rid of the circle and extrude the knife cut.
[0:19] Create a cylinder, place it as far inside the cube as you want the hole to go.
[0:23] Select the cylinder, hold shift and select the cube.
[0:25] Now press Ctrl minus to cut.
[0:28] The cutter object remains visible as a wireframe so you can still adjust.
[0:32] To confirm apply the boolean modifier.
[0:35] Make sure there is a vertex where you want the hole to be.
[0:38] Press Shift Ctrl B to bevel and increase the amount of vertices with the middle mouse button.
[0:43] You may need to change the profile and 0.085 seems to work well.
[0:48] Then you can extrude the hole.
[0:50] If you've already got some edge loops, select some phases, 4 is already enough and go to
[0:55] loop tools, circle.


### 4 - Loop Tools Circle [0:56]
**Transcript (timestamped):**
[0:57] Hold that bad boy and throw some subdivisions on it while you're at it.
[1:00] Select phases on both sides of the model and go to loop tools, bridge.


### LoopTools Bridge [1:01]
**Transcript (timestamped):**
[1:04] This will punch a hole right through your model.
[1:07] Create a curve, rectangle and create a curve circle.


### Curves [1:09]
**Transcript (timestamped):**
[1:10] Scale the circle to create a hole.
[1:13] You can press Shift D to duplicate the hole and move it to create many holes really quickly.
[1:18] Then convert the whole thing to mesh if you want.
[1:21] Extrude it if you want.
[1:22] I'm not going to stop you.
[1:23] Create a circle and move it away from the other objects.
[1:26] Turn on snapping and snap to face, project individual elements.
[1:31] In edit mode, select all vertices of the circle, press G to snap them to the surface.
[1:36] Now turn off snapping.
[1:38] Then in object mode, join both objects with Ctrl J.
[1:42] Reposition the circle if needed.
[1:44] Remove the phases underneath.
[1:45] And then fill the phases where needed.
[1:48] Then extrude.


### Intersect [1:50]
**Transcript (timestamped):**
[1:50] Create a second object to cut with and join both objects with Ctrl J.
[1:55] Select the phases of the object that you want to cut out of by selecting one phase and pressing
[1:58] L.
[1:59] Now go to the face menu and choose intersect boolean.
[2:03] Then choose the correct options from the menu to get what you want.
[2:07] Enable the Carver add-on in preferences and go to orthographic view.
[2:11] Press Shift Ctrl X to activate the Carver tool.
[2:14] Press space bar a couple of times until you get the circle cut type.
[2:18] Draw the circle and hold Alt to move it to where you want it.
[2:22] Then let go of Alt and left click to confirm the cut.
[2:25] Box Cutter is a commercial add-on so to use this you'll need to buy it first.
[2:29] Activate box cutter by pressing Alt W.
[2:32] Press D for the pie menu and choose circle to cut with a circle shape.
[2:36] Now left click on a selected object and drag to change the size of the circle.
[2:41] Let go of the left mouse button to confirm, then move the mouse to extrude the circle.
[2:46] Left click again to confirm.
[2:48] Once you start making holes with box cutter it's difficult to stop.



---

## Captured Frames

- [0:04] tutorials/frames/daily-blender-secrets---10-ways-to-make-holes-in-blender/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-secrets---10-ways-to-make-holes-in-blender/frame_001.jpg
- [0:38] tutorials/frames/daily-blender-secrets---10-ways-to-make-holes-in-blender/frame_002.jpg
- [1:00] tutorials/frames/daily-blender-secrets---10-ways-to-make-holes-in-blender/frame_003.jpg
- [1:11] tutorials/frames/daily-blender-secrets---10-ways-to-make-holes-in-blender/frame_004.jpg
- [1:35] tutorials/frames/daily-blender-secrets---10-ways-to-make-holes-in-blender/frame_005.jpg
- [2:30] tutorials/frames/daily-blender-secrets---10-ways-to-make-holes-in-blender/frame_006.jpg

---

## Structured Notes

### Core Technique
A rapid-fire survey of 10 distinct ways to cut a hole into a mesh in Blender — from purely native tools (Knife Project, boolean cylinders, beveled vertices, LoopTools Circle/Bridge, curve-to-mesh, snap-and-project) to add-on-powered cutters (BoolTool, Carver, Box Cutter). The video overlays an on-screen numbered label ("1 - Knife Project", "2 - BoolTool", etc.) for each method as it demonstrates it.

### Summary
Frame 000 (labeled "1 - Knife Project") shows the Add menu open in the viewport with Mesh highlighted, illustrating the first step: adding a circle in front of/on top of the cube in orthographic view before running Knife Project. Frame 001 (labeled "2 - BoolTool") shows the payoff of the second method: a cube with a circular hole already cut where a cylinder was Boolean-subtracted via BoolTool's Ctrl+Numpad− shortcut, the cutter's orange bounding-box outline still visible and editable. Frame 002 (labeled "3 - Bevel vertex") shows a bare plane with a single vertex selected at its center — the setup before Shift+Ctrl+B beveling that vertex into a circular hole opening. Frame 003 (labeled "4 - LoopTools Circle") shows the bevel-vertex result taken further: a rounded cube with a clean circular hole and visible edge subdivision, produced by running LoopTools > Circle on the beveled ring and adding subdivision. Frame 004 (labeled "6 - Curves") shows the Add menu's Curve submenu open with Bezier highlighted, plus a diamond-shaped curve rectangle already in the viewport — the setup for creating a Curve Rectangle + Curve Circle pair, where the circle is scaled to punch a hole once converted to mesh. Frame 005 (labeled "7 - Project") shows Edit Mode on a cylindrical form with a circular ring of vertices selected mid-viewport, matching the "select all vertices of the Circle, press G to snap them to the surface" step of the snap-and-project method. Frame 006 (labeled "10 - Boxcutter add-on") shows a plain cube with the on-screen prompt to activate Box Cutter via Alt+W, the final and most add-on-dependent method in the list.

### Key Steps
1. **Knife Project:** create a circle, place it in front of or on top of the cube, switch to orthographic view; select the circle, then Shift-select the cube; in Edit Mode use Mesh > Knife Project to cut the circle's silhouette into the cube's surface; delete the now-unneeded circle and extrude the cut face inward/outward for the hole.
2. **BoolTool (Boolean Difference):** create a cylinder sized to the depth the hole should go; select the cylinder, Shift-select the cube, press Ctrl+Numpad− to cut — the cutter stays visible as an adjustable wireframe until the Boolean modifier is applied.
3. **Bevel vertex:** ensure there is a single vertex exactly where the hole should be; press Shift+Ctrl+B to bevel it into vertices, scroll the middle mouse button to add more vertices (rounding the hole), adjust the bevel Profile (≈0.085 worked well in the demo) for the right curvature, then extrude the resulting hole.
4. **LoopTools Circle:** with an existing edge loop (as few as 4 faces is enough), select the faces and run LoopTools > Circle to snap them into a perfect circle, then add subdivision for smoother geometry.
5. **LoopTools Bridge:** select faces on both opposing sides of the model and run LoopTools > Bridge to punch a hole straight through, connecting the two openings.
6. **Curves to mesh:** add a Curve Rectangle and a Curve Circle; scale the circle to the desired hole size; Shift+D duplicate the circle to quickly create many holes at once; convert the whole curve setup to mesh, then extrude as needed.
7. **Snap-and-project:** create a circle and move it away from the target mesh; enable snapping set to Face with "Project Individual Elements"; in Edit Mode select all the circle's vertices and press G to snap them onto the target surface; turn off snapping, join both objects with Ctrl+J, reposition the circle if needed, delete the faces underneath it, fill the resulting gap where needed, then extrude for depth.
8. **Intersect (Boolean via Face menu):** create a second cutter object and join it to the target with Ctrl+J; select the faces to be cut (press L to select linked), then use the Face menu's Intersect (Boolean) option, choosing the appropriate settings from its menu for the desired result.
9. **Carver add-on:** enable Carver in Preferences; switch to orthographic view; press Shift+Ctrl+X to activate the Carver tool; tap Spacebar repeatedly to cycle to the circle cut type; draw the circle, hold Alt to reposition it, release Alt and left-click to confirm the cut.
10. **Box Cutter add-on (commercial):** activate Box Cutter with Alt+W; press D for its pie menu and choose the circle shape; left-click on the target object and drag to size the circle, release to confirm, move the mouse to extrude the cut, left-click again to finalize.

### Nodes / Settings
- **Native tools:** Mesh > Knife Project; Boolean modifier (manual Difference); Bevel (Shift+Ctrl+B, vertex bevel with adjustable segments/Profile); LoopTools add-on operators Circle and Bridge; Curve objects (Rectangle, Circle) converted to mesh; Snap settings (Face target, Project Individual Elements); Face menu > Intersect (Boolean).
- **Add-ons:** BoolTool (Ctrl+Numpad− live Boolean Difference), Carver (Shift+Ctrl+X, Spacebar to cycle cut shapes), Box Cutter (Alt+W to activate, D for shape pie menu) — Box Cutter is explicitly noted as a paid/commercial add-on.
- **Shortcuts:** Shift+D (duplicate), Ctrl+J (join objects), L (select linked under cursor), G (grab/snap-to-surface with snapping enabled).

### Difficulty
Intermediate

### Blender Version
Not specified in transcript or frames — relies on BoolTool, Carver, and Box Cutter add-ons plus native LoopTools, consistent with Blender 2.9x through 5.x.

### Tags
modelling, procedural, intermediate

---

## Related Tutorials
- [Blender Secrets - 6 Minutes of Boolean Basics](blender-secrets---6-minutes-of-boolean-basics.md) — shares modelling, procedural, intermediate; that tutorial goes deep on the BoolTool/Boolean-modifier method (#2 here) plus cleanup, this one surveys 9 other hole-cutting alternatives.
- [Daily Blender Secrets - 15 Tips Compilation (Part 2)](daily-blender-secrets---15-tips-compilation-part-2.md) — shares modelling, procedural; that compilation's Tips 5-6 (Bevel Holes, Round Holes) cover the same bevel-vertex and LoopTools Circle methods (#3 and #4 here) as standalone tips within a broader mix.
- [Easy hole modeling for beginners - Blender Secrets](easy-hole-modeling-for-beginners---blender-secrets.md) — shares modelling, procedural; a deeper dive on this survey's "Bevel vertex" and "LoopTools Circle" methods (#3-4), plus an added all-quad subdivision-ready topology technique not covered here.
- [Perfect Holes with Quad Topology in Curved Surfaces](perfect-holes-with-quad-topology-in-curved-surfaces---step-by-step-blender-begin.md) — shares modelling, procedural; solves the specific problem of keeping the surface *around* a hole perfectly smooth on a curved (cylindrical) base, via a Shrinkwrap + vertex-group-exclusion trick not covered in this survey.
