---
title: Blender Secrets - Making Holes in Cylinders with decent Quad Topology
source: YouTube
url: https://www.youtube.com/watch?v=JvJ_Hoj82us
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (core mesh/modifier + Loop Tools workflow, 2.9x-5.x)"
tags: [modelling, procedural, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---making-holes-in-cylinders-with-decent-quad-topology/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - Making Holes in Cylinders with decent Quad Topology

**Source:** [YouTube](https://www.youtube.com/watch?v=JvJ_Hoj82us)
**Author:** Blender Secrets
**Duration:** 6m47s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Add a cylinder by pressing Shift A and choosing Mesh Cylinder
[0:11] In Edit Mode, press Ctrl R and scroll the mouse wheel up to add some horizontal edge
[0:16] loops.
[0:18] Add a circle with Shift A Mesh Circle.
[0:21] You don't need too many vertices, 12 is more than enough.
[0:27] Move it away from the other object.
[0:30] It can be useful to turn on wireframe display to see the wireframe of the cylinder.
[0:35] Turn on snapping, snap to face and project individual elements.
[0:41] In Edit Mode, select all vertices of the circle.
[0:45] Move or scale the circle as needed to line it up better to the cylinder geometry.
[0:51] Press G to snap the circle vertices to the cylinder.
[0:55] Now disable snapping.
[0:58] In Object Mode, join both objects with Ctrl J.
[1:02] Remove the faces of the cylinder underneath the circle.
[1:08] And then fill the faces where needed.
[1:12] In case triangles are generated, you can press Alt J to convert those to quads.
[1:17] If some triangles still remain, select the unwanted edges and press Ctrl X to dissolve
[1:22] them.
[1:25] Control the gap by pressing Ctrl F and choosing Grid Fill.
[1:31] You can change the offset value to rotate the new faces.
[1:35] Finally, use Inset and Extrude to create the hole.
[1:42] Press Ctrl and a number from 1 to 5 to add that level of subdivisions.
[1:46] Then right click and choose Shade Smooth.
[2:00] Instead of creating a circle, you can also turn a duplicate of selected faces into a
[2:04] circular shape.
[2:06] First select 6 or more faces using Circle Select.
[2:11] Duplicate them by pressing Shift D.
[2:14] Remove them away from the cylinder and scale them down slightly.
[2:19] Right click, choose Loop Tools Circle.
[2:25] You can use Wireframe View and View per Overlace or Wireframe View in Edit Mode to see the geometry
[2:31] of both objects.
[2:33] Turn on snapping, snap to face and project individual elements.
[2:38] Press G to snap the selected geometry to the cylinder.
[2:42] Now the faces are snapped to the mesh.
[2:46] Press H to hide the selection temporarily.
[2:50] Select the 6 or more original faces on the cylinder again.
[2:55] Press X to delete them and Alt H to unhide hidden faces.
[3:00] Select the edges.
[3:03] Right click and choose Bridge Edge Loops.
[3:07] Now you can select inset and extrude faces as needed to create a hole.
[3:26] Similarly to the previous method, you can snap previously made geometry to the surface
[3:30] to save time.
[3:32] You can keep these in your asset browser for easy access.
[3:36] Just move, rotate and scale the geometry to roughly where you need it to be.
[3:42] Here using Wireframe Display is again handy.
[3:47] Turn on snapping, snap to face and project individual elements.
[3:52] In Edit Mode move the geometry a bit so it snaps to the surface of the cylinder.
[3:59] Then close the gaps by moving the boundary vertices with vertex snapping.
[4:05] Note that to snap a vertex you need to move the mouse cursor to the target vertex.
[4:11] Turn off snapping when that's all done and temporarily hide the selection by pressing
[4:15] H.
[4:20] Remove the faces that will be replaced.
[4:23] Unhide the hidden geometry by pressing Alt H.
[4:27] Then join both objects with Ctrl J in Object Mode.
[4:31] Merge vertices by selecting all and pressing M.
[4:34] Then choose Merge by Distance.
[4:37] You may have to select all and press Shift N to recalculate the normals.
[4:45] Now you can extrude the circular part.
[4:52] Another method of adding holes to a cylinder is by creating the holes first on a flat surface
[4:57] and then turning that into a cylinder.
[5:00] Make sure Loop Tools is enabled in Preferences.
[5:04] Add a plane and set it to Shade Smooth.
[5:07] Subdivide the plane twice in Edit Mode.
[5:10] Select the four middle faces, right click and use Loop Tools Circle.
[5:17] Inset the faces then delete them.
[5:21] Duplicate and move selected faces if you want to create an uneven look.
[5:29] Add an Array modifier and increase the count.
[5:34] Duplicate it, set the offset to Y instead of X and increase the count.
[5:44] Add an empty and set the X rotation to minus 90.
[5:49] Give the plane a simple D4 modifier set to 360° bend with the empty as the origin.
[5:59] Add a Weld modifier and a Solidify modifier with some thickness.
[6:06] You may want to turn on Auto Smooth at this point.
[6:10] Finally, add a Subdiv modifier.
[6:15] You can change the Array Count to adjust the shape as needed.
[6:20] Please note that the modifier order is important.
[6:27] If you found this topic interesting and would like to know more, don't forget that you can
[6:31] find it in my Blender Secrets eBook, along with almost 2000 pages of other tips.
[6:37] To get an idea of what the eBook is like, you can download the free sample from my website.



---

## Captured Frames

- [0:35] tutorials/frames/blender-secrets---making-holes-in-cylinders-with-decent-quad-topology/frame_000.jpg
- [1:05] tutorials/frames/blender-secrets---making-holes-in-cylinders-with-decent-quad-topology/frame_001.jpg
- [1:40] tutorials/frames/blender-secrets---making-holes-in-cylinders-with-decent-quad-topology/frame_002.jpg
- [2:20] tutorials/frames/blender-secrets---making-holes-in-cylinders-with-decent-quad-topology/frame_003.jpg
- [3:05] tutorials/frames/blender-secrets---making-holes-in-cylinders-with-decent-quad-topology/frame_004.jpg
- [3:50] tutorials/frames/blender-secrets---making-holes-in-cylinders-with-decent-quad-topology/frame_005.jpg
- [4:45] tutorials/frames/blender-secrets---making-holes-in-cylinders-with-decent-quad-topology/frame_006.jpg
- [5:55] tutorials/frames/blender-secrets---making-holes-in-cylinders-with-decent-quad-topology/frame_007.jpg

---

## Structured Notes

### Core Technique
Four different ways to cut clean, all-quad holes into a cylinder (avoiding the messy n-gons/triangles a naive boolean cut leaves behind): snap-and-join a separate circle, duplicate-and-circularize existing faces, snap in pre-made reusable asset geometry, or build the hole pattern flat first and bend it into a cylinder afterward.

### Summary
Frame 000 shows Method 1's setup: a low-poly (12-vertex) Circle object positioned in front of a cylinder in Front Orthographic wireframe view, ready to be projected onto the surface. Frame 001 shows the circle's vertices selected and about to be snapped onto the cylinder's face grid (Snap to Face + Project Individual Elements enabled). Frame 002 shows the finished hole from Method 1: a clean octagon-shaped opening cut into the cylinder wall with all-quad surrounding topology, viewed from inside/behind. Frame 003 shows Method 2's key operator: the right-click Loop Tools submenu (Bridge, Circle, Curve, Flatten, GStretch, Loft, Relax, Space) about to run Circle on a duplicated patch of faces to round them out before snapping. Frame 004 shows the snapping step for a reusable asset piece: the Snap Target dropdown open (Face highlighted) with "Project Individual Elements" checked (arrow), aligning a pre-made "Pipe Detail" asset against the cylinder surface — confirming Method 3's asset-browser reuse workflow. Frame 005 shows that pipe-detail asset successfully snapped flush against the cylinder's curved surface, selected geometry highlighted orange/white. Frame 006 shows Method 4's core trick: a flat Plane with an Array modifier (Fixed Count, Relative Offset) generating a repeating grid of octagonal holes, top-down view, ready to be wrapped into a cylinder via a Simple Deform (Bend) modifier further down the stack.

### Key Steps
**Method 1 — Snap a separate circle onto the cylinder:**
1. Add a Cylinder (Shift+A → Mesh → Cylinder); in Edit Mode, Ctrl+R and scroll to add horizontal edge loops for enough surrounding geometry.
2. Add a Circle (Shift+A → Mesh → Circle) with modest vertex count (12 is plenty); move it away from the cylinder; enable Wireframe display to see through both objects.
3. Enable Snapping (Snap to Face, Project Individual Elements); in Edit Mode select all circle vertices, move/scale to roughly line it up with the cylinder's geometry, then press G to snap it onto the cylinder's curved surface; disable snapping afterward.
4. In Object Mode, Ctrl+J to join both objects; remove the cylinder faces underneath the snapped circle, then fill the resulting gap (F). If triangles appear, Alt+J converts them to quads; dissolve (Ctrl+X) any stubborn leftover edges. Use Ctrl+F → Grid Fill to control/clean the fill pattern (Offset value rotates the new faces if the grid doesn't align well).
5. Finish with Inset + Extrude on the filled circle to actually create the hole depth; Ctrl+[1-5] to add a Subdivision level, Shade Smooth to finish.

**Method 2 — Circularize existing cylinder faces:**
1. Circle Select 6 or more faces directly on the cylinder; Shift+D to duplicate them, move the duplicate away and scale it down slightly.
2. Right-click → Loop Tools → Circle to round the duplicated patch into a clean circular shape.
3. Enable Wireframe/overlay display to see both pieces; enable Snapping (Face, Project Individual Elements) and press G to snap the circularized duplicate back onto the cylinder surface.
4. Press H to temporarily hide the snapped selection; reselect the original 6+ faces on the cylinder and X to delete them; Alt+H to unhide the snapped geometry.
5. Select the boundary edges and right-click → Bridge Edge Loops to connect the circle to the hole in the cylinder; Inset + Extrude as needed to finish the hole.

**Method 3 — Reuse pre-made geometry from the Asset Browser:**
1. Keep useful hole/detail geometry pieces saved in the Asset Browser for quick reuse; move/rotate/scale a saved piece roughly into position against the target surface (Wireframe display helps).
2. Enable Snapping (Face, Project Individual Elements); in Edit Mode nudge the geometry so it snaps flush to the cylinder surface, then close any remaining gaps by moving boundary vertices with vertex snapping (move the cursor onto the exact target vertex to snap to it).
3. Turn off snapping when done; H to hide the snapped selection, delete the cylinder faces it will replace, Alt+H to unhide.
4. Ctrl+J to join both objects in Object Mode; select all and M → Merge by Distance to weld the seam; Shift+N to recalculate normals if needed. Extrude the circular part to finish the hole.

**Method 4 — Build the hole pattern flat, then bend into a cylinder:**
1. Ensure Loop Tools is enabled in Preferences. Add a Plane, Shade Smooth, Subdivide twice in Edit Mode.
2. Select the four middle faces, right-click → Loop Tools → Circle; Inset those faces then delete them to punch a clean circular hole.
3. Optionally duplicate and offset selected hole-faces for an uneven/randomized look.
4. Add an Array modifier (increase Count) for repetition along one axis; duplicate that modifier, set its offset to the Y axis instead of X, and increase its count too — producing a full 2D grid of holes.
5. Add an Empty, set its X rotation to -90°; add a Simple Deform modifier set to Bend 360° using the Empty as the origin — this wraps the flat, hole-patterned plane into a closed cylinder.
6. Add a Weld modifier (closes the seam), a Solidify modifier (wall thickness), enable Auto Smooth, and finish with a Subdivision Surface modifier. Adjust the Array Count(s) to change hole density/spacing. Modifier order matters throughout this stack.

### Nodes / Settings
- **Snapping:** Snap Target = Face, Project Individual Elements (used in Methods 1-3 to conform geometry to the cylinder's curved surface).
- **Mesh operators:** Ctrl+R (loop cut), Alt+J (Tris to Quads), Ctrl+X (Dissolve), Ctrl+F → Grid Fill, Inset, Extrude, H/Alt+H (hide/unhide selection), M → Merge by Distance, Shift+N (recalculate normals), Ctrl+J (join objects).
- **Add-on:** Loop Tools (Circle operator — rounds a selected face patch into a clean circle; Bridge Edge Loops for connecting boundaries).
- **Modifiers (Method 4):** Array (x2, one per axis, Fixed Count, Relative Offset), Simple Deform (Bend 360°, Origin = an Empty rotated -90° on X), Weld, Solidify, Subdivision Surface — with Auto Smooth enabled.
- **Asset workflow:** Asset Browser for storing/reusing pre-made hole/detail geometry.

### Difficulty
Intermediate to Advanced

### Blender Version
Not specified — core mesh/modifier workflow with Loop Tools, version-agnostic across modern Blender (2.9x-5.x).

### Tags
modelling, procedural, intermediate, advanced

---

## Related Tutorials
- [Blender Secrets - 5 minutes of N-Gons to Quads tips](blender-secrets---5-minutes-of-n-gons-to-quads-tips.md) — shares modelling, procedural, intermediate; same channel, directly overlapping "Knife Project a helper shape onto a surface" philosophy applied here specifically to cylinders.
- [Blender Secrets - Every Circular Array or Radial Array method](blender-secrets---every-circular-array-or-radial-array-method.md) — shares procedural, intermediate, advanced; same channel, its Curve+Array method for wrapping segments around a circle is closely related to this video's Method 4 (Array + Simple Deform Bend).
