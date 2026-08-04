---
title: Blender Secrets - Making Holes in Cylinders with decent Quad Topology
source: YouTube
url: https://www.youtube.com/watch?v=JvJ_Hoj82us
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-secrets---making-holes-in-cylinders-with-decent-quad-topology/
frame_count: 0
frame_status: pending-selection
---

# Blender Secrets - Making Holes in Cylinders with decent Quad Topology

**Source:** [YouTube](https://www.youtube.com/watch?v=JvJ_Hoj82us)
**Author:** Blender Secrets
**Duration:** 6m47s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-secrets---making-holes-in-cylinders-with-decent-quad-topology <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Blender Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
