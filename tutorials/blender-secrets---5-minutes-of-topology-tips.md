---
title: Blender Secrets - 5 minutes of Topology Tips
source: YouTube
url: https://www.youtube.com/watch?v=V7Y-Il-7JFE
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (core mesh-editing workflow, 3.x-5.x)"
tags: [modelling, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---5-minutes-of-topology-tips/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - 5 minutes of Topology Tips

**Source:** [YouTube](https://www.youtube.com/watch?v=V7Y-Il-7JFE)
**Author:** Blender Secrets
**Duration:** 5m16s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Rotate edges [0:00]
**Transcript (timestamped):**
[0:00] When low poly models are made of triangles, every edge makes a difference.
[0:05] Here you can see one edge which is causing problematic shading.
[0:09] We can solve this by rotating it in the Edge menu, per passing CTRL E and choosing Rotate Edge.
[0:16] You can choose clockwise or counterclockwise, either is fine.
[0:20] That looks much better.


### Extrude edges [0:23]
**Transcript (timestamped):**
[0:30] To go from 4 to 2 quads, select and extrude these two edges. Extrude again.
[0:35] Select the vertices at the corners and scale them away from each other.
[0:39] Select these edges and fill them by pressing F.
[0:44] Extrude these two edges and you're done.
[0:48] To go from 5 to 3 quads, select the middle edge and extrude it.
[0:54] Select the other edges and extrude them further than the middle one.
[0:58] Then select and merge these vertices by pressing M.
[1:04] Fill the gap by selecting these edges and pressing F.
[1:07] Then select and extrude the three edges.
[1:10] For better distribution of geometry, you can scale this middle face down.
[1:15] To go from 3 quads to a single one, select these two edges and extrude them.
[1:20] Extrude the middle edge as well, but only halfway the other two.
[1:24] Merge these vertices by selecting them and pressing M.
[1:28] Then fill the gap by selecting the edges and pressing F.
[1:32] Finally, extrude the one edge out by pressing E.
[1:39] Normally, you can add an edge loop with Ctrl R, but that doesn't work on triangles.
[1:44] Here's how you can still do it.
[1:46] Make sure you're in edge selection mode in edit mode.
[1:50] Select the bottom edge loop by holding Alt and left clicking on it.
[1:54] Invert the selection by pressing Ctrl I.
[1:57] Right click and choose subdivide.
[2:00] Now, hold Alt and left click on the new edge loop to select it.
[2:03] Then press G twice to slide it to where you need it.


### Conform edges [2:10]
**Transcript (timestamped):**
[2:14] In case you have an edge loop that you need to make perfectly straight,
[2:18] you can press G twice and then press E.
[2:21] Pressing E confirms the edge loop to its neighboring edge loop.
[2:25] So it only works if there is a perfectly straight edge loop next to it.
[2:29] Press F to toggle which edge loop to conform the shape to.
[2:33] If you want to make sure to place the edge loop in the middle,
[2:35] hold down Ctrl to move it in increments.
[2:41] You can also use the loop tools add-on.
[2:44] Select the edges and right click, choose loop tools and then flatten.
[2:51] If you only want to straighten out the edges on one side of the model
[2:54] or a limited amount of edges instead of the entire loop,
[2:57] use the G stretch option instead.
[3:00] Finally, you can scale the edges to zero.
[3:03] In this case, we scale along the Z axis.
[3:06] Press S, Z and then zero on the numpad.


### Flatten [3:09]
**Transcript (timestamped):**
[3:15] Select the faces that you want to flatten.
[3:18] Go to Select Similar, choose Coplanar, then increase the threshold if necessary.
[3:24] Right click, select loop tools and choose Flatten.
[3:27] The good thing about this method is that it works no matter the angle of the faces.
[3:33] Another way is to scale things to zero.
[3:36] In other words, select the faces, press S and Z for the Z axis and then zero on the numpad.
[3:41] This works best if the faces are aligned perpendicular to the exact axis you are skating to.
[3:46] For a third method, delete the selected faces.
[3:50] Select the edges surrounding the resulting hole and fill the hole by pressing Ctrl F and then choosing Great Fill.
[3:56] If your model has some areas that need to be more smooth, there are three ways to do it.


### Smooth [3:59]
**Transcript (timestamped):**
[4:02] You can select those vertices, right click and then choose Smooth Vertices.
[4:07] Then hit Shift R a few times to repeat the last action until it looks smooth enough.
[4:12] Another option is to go over to Sculpt Mode, be sure to turn off Symmetry and Sculpt on the model while you are skating.
[4:18] And Sculpt on the model while holding down Shift.
[4:21] This makes the surface smooth as well, but it works best when you have more subdivisions on your model or within Topo Enabled.
[4:28] It can also take some practice to get perfect.
[4:36] You can also add the non-smooth vertices to a vertex group.
[4:42] And then use that vertex group in a smooth or depletion smooth modifier.
[4:48] If you found this topic interesting and would like to know more,
[4:52] don't forget that you can find it in my Blender Secrets ebook.
[4:56] Along with almost 2000 pages of other tips.
[4:59] To get an idea of what the ebook is like, you can download the free sample from my website.



---

## Captured Frames

- [0:20] tutorials/frames/blender-secrets---5-minutes-of-topology-tips/frame_000.jpg
- [0:44] tutorials/frames/blender-secrets---5-minutes-of-topology-tips/frame_001.jpg
- [1:32] tutorials/frames/blender-secrets---5-minutes-of-topology-tips/frame_002.jpg
- [2:03] tutorials/frames/blender-secrets---5-minutes-of-topology-tips/frame_003.jpg
- [2:33] tutorials/frames/blender-secrets---5-minutes-of-topology-tips/frame_004.jpg
- [3:24] tutorials/frames/blender-secrets---5-minutes-of-topology-tips/frame_005.jpg
- [3:50] tutorials/frames/blender-secrets---5-minutes-of-topology-tips/frame_006.jpg
- [4:07] tutorials/frames/blender-secrets---5-minutes-of-topology-tips/frame_007.jpg

---

## Structured Notes

### Core Technique
Five manual topology-cleanup techniques for hand-modeling: rotating edges to fix bad triangle shading, systematically reducing N quads down to fewer quads via extrude/merge/fill patterns, adding an edge loop across triangulated geometry (where Ctrl+R doesn't work), conforming/straightening a wavy edge loop, and three different ways to flatten or smooth a patch of geometry.

### Summary
Frame 000 shows the payoff of tip 1: a low-poly triangulated character bust (Suzanne-like) mid-Edit-Mode with the status bar reading "Rotate Selected Edge" after using Ctrl+E → Rotate Edge to fix a shading artifact caused by a poorly-oriented triangle diagonal. Frames 001-002 show tip 2's quad-reduction pattern on a plane: frame 001 is the "before" (4 quads, Top Orthographic), frame 002 mid-process with F (fill) about to close a gap after extruding and merging — the systematic edge-count-reduction dance described in the transcript. Frame 003 shows tip 3's setup: a triangulated cone, illustrating the case where the normal Ctrl+R loop cut doesn't work and the Alt-select-loop → Ctrl+I invert → Subdivide → Alt-select-new-loop → G,G-slide method is needed instead. Frame 004 shows tip 4 (conform edges): a subdivided cube with an internal edge loop highlighted orange and an Edge Slide double-arrow icon — mid G,G,E conform-to-neighbor operation. Frame 005 shows tip 5's "Select Similar → Coplanar" step (panel open, Type=Coplanar, Compare=Equal) on a cube face selection, and frame 006 shows the alternate "delete + grid fill" method's X (Delete) menu with "Faces" highlighted by an arrow. Frame 007 shows the Vertex context menu on a sphere with "Smooth Vertices" highlighted by an arrow — the first of the three smoothing methods.

### Key Steps
1. **Rotate problem edges:** on low-poly triangulated models, a badly-oriented diagonal edge causes visible faceted/incorrect shading — select it, Ctrl+E → Rotate Edge (CW or CCW, either works), which flips the diagonal to the other pair of corners for better shading.
2. **Reduce N quads to fewer quads (geometry-reduction patterns):**
   - 4→2: select and extrude two edges, extrude again, select the corner vertices and scale them apart, select the resulting edges and fill (F), then extrude the final two edges.
   - 5→3: extrude the middle edge, extrude the other edges further out than the middle one, merge (M) the resulting close vertices, fill the gap (F), extrude the three remaining edges, and optionally scale the middle face down for better geometry distribution.
   - 3→1: extrude two edges plus the middle edge (only halfway as far as the outer two), merge (M) the close vertices, fill the gap (F), then extrude the single remaining edge out (E).
3. **Add an edge loop across triangulated geometry (Ctrl+R doesn't work on tris):** in Edge select mode, Alt+click the boundary edge loop nearest where you want the cut, Ctrl+I to invert the selection (grabbing everything except that loop), right-click → Subdivide, then Alt+click the newly created loop and press G,G to slide it into position.
4. **Conform/straighten a wavy edge loop:** select it, press G,G (Edge Slide) then E to conform its shape to the neighboring loop — only works if a perfectly straight loop exists adjacent to it; press F while sliding to toggle which side to conform to; hold Ctrl while sliding to move in increments (useful for centering). Alternative: select the edges, right-click → LoopTools → Flatten (add-on). For straightening only part of a loop rather than the whole thing, use the G-stretch option instead. A blunt-but-effective alternative: select the edges and press S, Z, 0 (scale to zero on the relevant axis).
5. **Flatten a patch of faces (3 methods):** (a) select target faces, Select Similar → Coplanar (raise the threshold if needed), right-click → LoopTools → Flatten — works regardless of the faces' angle; (b) select faces and scale to zero on the axis they're most perpendicular to (S, Z, 0) — works best when faces are aligned close to that axis; (c) delete the selected faces entirely, select the surrounding boundary edges, and Ctrl+F → Grid Fill to rebuild a clean flat patch.
6. **Smooth a rough area (3 methods):** (a) select vertices, right-click → Smooth Vertices, then Shift+R to repeat until smooth enough; (b) switch to Sculpt Mode, disable Symmetry, and sculpt/smooth while holding Shift — works best with more subdivisions or Dyntopo enabled, takes practice; (c) add the non-smooth vertices to a Vertex Group and use that group as the input mask for a Smooth or Laplacian Smooth modifier for a non-destructive, adjustable result.

### Nodes / Settings
- **Edit-mode operators:** Ctrl+E → Rotate Edge, E (extrude), M (merge), F (fill), Ctrl+R (loop cut — doesn't work on triangles), Ctrl+I (invert selection), Subdivide, G,G (Edge Slide), Ctrl+F → Grid Fill, S+axis+0 (scale to zero), right-click → Smooth Vertices, Shift+R (repeat last operator).
- **Selection:** Alt+click (select edge loop), Select Similar → Coplanar (Type, Compare, Threshold).
- **Add-on:** LoopTools (built-in) — Flatten operator.
- **Sculpt:** Sculpt Mode smoothing (Shift-hold), Dyntopo for better results, Symmetry disabled.
- **Modifiers:** Smooth modifier / Laplacian Smooth modifier, driven by a Vertex Group mask.

### Difficulty
Intermediate

### Blender Version
Not specified — core mesh-editing workflow, version-agnostic across modern Blender (3.x-5.x).

### Tags
modelling, procedural, intermediate

---

## Related Tutorials
- [Blender Secrets - 5 minutes of N-Gons to Quads tips](blender-secrets---5-minutes-of-n-gons-to-quads-tips.md) — shares modelling, procedural, intermediate; same channel, direct companion topology-cleanup video.
- [4 new retopology tips to discover! - Blender Secrets](4-new-retopology-tips-to-discover---blender-secrets.md) — shares modelling, intermediate; same channel, overlapping topology/retopology subject matter.
