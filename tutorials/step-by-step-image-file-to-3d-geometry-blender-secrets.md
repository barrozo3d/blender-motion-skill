---
title: Step by Step: Image File to 3D Geometry | Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=HUL9o27m11M
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 4.0.2 -- observed in frame_000"
tags: [modelling, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/step-by-step-image-file-to-3d-geometry-blender-secrets/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Step by Step: Image File to 3D Geometry | Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=HUL9o27m11M)
**Author:** Blender Secrets
**Duration:** 7m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Knife Project is another interesting tool for making holes.
[0:08] To demonstrate it, I'll use a round cube.
[0:13] This is the Quadsphere preset.
[0:17] I'll just hide that for now.
[0:21] You can just drag and drop images from a File Explorer window.
[0:27] This image is imported as an empty object.
[0:34] Convert it to a grease pencil object by going to this menu.
[0:40] I recommend the default resolution, which is 5.
[0:50] This creates a new grease pencil object.
[0:52] We can hide the original image empty.
[0:54] It's a bit difficult to see, but it also kept the keyhole of the logo.
[0:59] But we actually still need to convert it to a path.
[1:05] If we disable the grease pencil object, we can see the path.
[1:09] Finally, we convert it to a mesh.
[1:12] I hope that in the future we can convert directly from grease pencil to mesh.
[1:18] I'll just rename this mesh to logo in the Outliner.
[1:27] Now as you can see, this has a lot of vertices.
[1:31] That will make it difficult later to get a nice smooth result when we cut into the Quadsphere.
[1:36] What we can do is select all the vertices and then press M for the Merge menu.
[1:40] Then Merge by Distance and experiment with the Distance value.
[1:55] To further get rid of vertices, we can use Checker Deselect.
[2:00] Unfortunately, we need to do it per individual mesh island.
[2:08] So select one mesh island by hoovering the cursor over it and pressing L.
[2:12] Then go to Checker Deselect.
[2:15] This selects every other vertex.
[2:19] Then you can press Ctrl X to dissolve these selected vertices.
[2:24] Repeat these steps for each mesh island.
[2:27] I do recommend deselecting the corner vertices as these are important for the shape.
[2:34] We can manually slide or remove some vertices to repair these corners where the shape got
[2:45] destroyed a bit.
[2:50] For the next step, first select all the corner vertices and then invert the selection.
[3:10] Then you can use the Loop Tools space tool to evenly space out those vertices.
[3:20] I'm just manually sliding and moving some vertices for some final improvements.
[3:31] Unhide the Quadsphere.
[3:37] Move the logo along the Y-axis.
[3:39] And distance doesn't matter as long as it's not inside of the sphere.
[3:44] If we select both objects and go to Edit Mode, we can inspect and compare the vertex distribution.
[3:50] Usually it's a good idea to have the resolution of both objects fairly similar to make things
[3:54] easier later on.
[3:56] In this case, the sphere is a much lower resolution than the logo, so I'll add some
[4:00] subdivisions to it.
[4:02] After applying that Subdiff modifier, we can see that the objects now match better in terms
[4:05] of their resolution.
[4:09] Now we're ready to use Knife Project.
[4:11] Select only this sphere in Object Mode.
[4:13] I will enable Shade Autos Mode.
[4:19] Go to Edit Mode.
[4:20] It doesn't matter if you're in Vertex Edge or Face Mode or if anything or nothing is
[4:25] selected.
[4:26] Then hold Ctrl and in the Outliner, select the logo.
[4:31] Go to Mesh Knife Project.
[4:38] As you can see, this has cut the logo shape into the sphere.
[4:42] We can enable Cut Through in the last operator panel to cut all the way to the other side
[4:46] of the sphere.
[4:48] One thing that's important to know is that the viewing angle determines how you cut.
[4:53] So for example, if we cut from this view, we only cut the overlapping part of the logo.
[5:01] While the last operator panel is active, we can still cut from different angles.
[5:05] In this case, we're going to cut from the front and without cutting through the sphere.
[5:12] Since these faces are all selected after the cut, we can easily delete them.
[5:18] As you can see, the Knife Project operation has left us all these unwanted vertices.
[5:23] You could enable Auto Merge Vertices and then slide them, we're pressing G twice to clean
[5:28] up this mess manually.
[5:30] However, that's quite time consuming.
[5:34] We can take advantage of some nice time saving steps.
[5:38] First select the non-manifold geometry, which is just the verges around the hole.
[5:43] Then merge by distance.
[5:48] Experiment with the value until you get a good result.
[5:52] As you can see, this took care of a lot of vertices.
[5:57] We can still manually clean the leftover ones by sliding them and merging them.
[6:04] Here there is a hole and we can fill it by selecting the vertices and pressing F.
[6:14] I want to keep this vertex and connect it to another one by pressing J, as I think that
[6:18] vertex is important for the overall shape.
[6:27] This is also an opportunity to fix the shape of the hole where necessary.
[6:35] Select the non-manifold vertices again.
[6:38] Let's switch to edge mode so we can deselect these edges.
[6:45] Now if we extrude with E and then scale with S, we get a not so great result.
[6:55] Let's scale with Alt S, which scales in the direction of the normals.
[7:03] This gives a pretty clean and smooth result.
[7:11] Let's add another quad sphere.
[7:14] Subdivide and shade it smooth, then scale it down.
[7:18] This gives us an easy and non-destructive way to control the depth of the logo.
[7:29] If necessary, you can still adjust some edges to improve the shape.



---

## Captured Frames

- [0:40] tutorials/frames/step-by-step-image-file-to-3d-geometry-blender-secrets/frame_000.jpg
- [1:31] tutorials/frames/step-by-step-image-file-to-3d-geometry-blender-secrets/frame_001.jpg
- [2:19] tutorials/frames/step-by-step-image-file-to-3d-geometry-blender-secrets/frame_002.jpg
- [3:44] tutorials/frames/step-by-step-image-file-to-3d-geometry-blender-secrets/frame_003.jpg
- [4:31] tutorials/frames/step-by-step-image-file-to-3d-geometry-blender-secrets/frame_004.jpg
- [4:53] tutorials/frames/step-by-step-image-file-to-3d-geometry-blender-secrets/frame_005.jpg
- [5:57] tutorials/frames/step-by-step-image-file-to-3d-geometry-blender-secrets/frame_006.jpg
- [7:03] tutorials/frames/step-by-step-image-file-to-3d-geometry-blender-secrets/frame_007.jpg

---

## Structured Notes

### Core Technique
Engraving a flat 2D logo image (the channel's own "Blender Secrets" keyhole-box mark) onto a curved 3D surface using **Knife Project**: the image is traced into flat mesh geometry via the Grease Pencil pipeline, cleaned up to a manageable vertex count, then projected/cut directly into a sphere's surface from the current view angle, with the resulting hole cleaned up and given depth via normal-direction extrusion.

### Summary
Frame 000 shows the source: the channel's own green keyhole-box logo image dropped into the viewport as an Empty, with the "Convert Image to Grease Pencil" operator panel open (Target Object: New Object, Thickness, Threshold, Corner, Frame settings). Frame 001 shows the resulting Grease Pencil trace: a clean orange wireframe outline of the box + keyhole shape, matching the source logo's silhouette exactly. Frame 002 shows the "logo" mesh after conversion, with a Vertex context menu open (Dissolve Vertices highlighted, "Ctrl+X" shortcut badge visible) — the cleanup pass removing excess trace-generated vertices. Frame 003 shows the two objects positioned together: the flat black-outlined logo mesh floating in front of a smooth, subdivided Round Cube/Quadsphere target sphere, Subdivision modifier (Catmull-Clark, Levels Viewport) visible in the sidebar — comparing vertex resolution between the two before projecting. Frame 004 shows the Vertex menu open with "Knife Project" highlighted, mid-operation on the sphere's surface with the logo shape visible faintly cut into it. Frame 005 shows the "Cut Through" option checked in the Knife Project redo panel (bottom-left), the box-shape cut now visible in orange piercing through the sphere from one viewing angle. Frame 006 shows an extreme close-up of the resulting cut boundary on the sphere — dense, irregular vertex clustering exactly where the logo's outline was projected in, the raw "unwanted vertices" mess Knife Project leaves behind. Frame 007 shows the finished engraved result: the keyhole-box logo shape cleanly recessed into the sphere's surface with smooth shading and soft lighting, matching the original 2D logo's silhouette in 3D relief.

### Key Steps
1. **Import and trace the source image:** drag-and-drop an image file directly from a File Explorer window into the viewport — it's imported as an Empty object with the image as its display. Convert it to a Grease Pencil object via the conversion menu, using the default Resolution value of 5 (higher isn't necessary and adds needless density); hide the original image Empty afterward. Note that fine details (e.g. a keyhole cutout inside a larger shape) are preserved as separate strokes/holes automatically.
2. **Convert Grease Pencil to a real mesh:** Grease Pencil can't yet be converted directly to mesh (as of this video) — first convert it to a Path, then convert that Path to a Mesh; rename the result clearly (e.g. "Logo") in the Outliner.
3. **Reduce excess vertices (the trace produces far too many for clean cutting):** select all vertices, M > Merge by Distance, experimenting with the Distance value until density drops significantly without losing the shape. For further reduction, work **per mesh island** (hover + L to select one island at a time) using **Checker Deselect** (selects every other vertex), then Ctrl+X to Dissolve the selected ones — repeat per island. Deliberately deselect/preserve corner vertices before this step, since they define the overall silhouette and are easy to accidentally destroy; manually slide or remove nearby vertices afterward to repair any corners that did get distorted. Once corners are protected, select all corner vertices, invert the selection, and use the **LoopTools > Space** tool to evenly redistribute the remaining vertices along each edge run; finish with manual vertex sliding for final polish.
4. **Match resolution between the logo and the target surface:** position the cleaned logo mesh near the target object (e.g. offset along Y — exact distance doesn't matter as long as it's not already inside the target). Select both objects and enter Edit Mode together to visually compare vertex density; if the target (e.g. a low-poly Quadsphere/Round Cube) is much coarser than the logo, add Subdivision levels and apply, so both objects have roughly similar resolution — this makes the eventual cut cleaner and later cleanup easier.
5. **Run Knife Project:** select only the target surface, enable Shade Auto Smooth, enter Edit Mode (selection mode/state doesn't matter); Ctrl+click the logo object in the Outliner to add it as the active/reference object; run Mesh > Knife Project. This cuts the logo's silhouette directly into the target's surface from the current viewing angle.
6. **Understand the projection direction:** Knife Project cuts based on the exact camera/view angle at the time it's run — cutting from one angle only affects the overlapping/visible portion of the shape from that view. While the redo panel is still active, re-orienting the view and re-running effectively re-projects from a new angle; enabling **Cut Through** in the redo panel cuts all the way to the opposite side of the surface instead of just the near side.
7. **Clean up post-cut:** the newly-selected cut faces (selected automatically after the operation) can simply be deleted if a hole is wanted. Knife Project leaves many small, messy, unwanted vertices around the cut boundary — manually cleaning these via Auto Merge Vertices + G,G (double-tap G) sliding works but is slow. **Faster approach:** select just the non-manifold geometry (the loose vertices/edges specifically around the hole boundary), then Merge by Distance with an experimentally-tuned value — this resolves most of the mess in one step; manually slide/merge any stragglers afterward. Fill any resulting open gap by selecting its boundary vertices and pressing F; where a specific vertex is important to the overall shape and shouldn't be deleted, connect it to a neighboring vertex with J instead of merging it away. This cleanup pass also doubles as an opportunity to manually refine the hole's shape where needed.
8. **Add depth to the engraving:** reselect the non-manifold boundary vertices, switch to Edge mode and deselect edges as needed; a plain Extrude (E) + Scale (S) gives a poor result, but **Extrude (E) then Alt+S** (scale along the vertex normals rather than a flat axis) produces a clean, smooth recessed/embossed result that properly follows the surface's curvature.
9. **Non-destructive depth control (optional):** add a second Quadsphere/Round Cube, subdivide and shade it smooth, then scale it down and use it purely to visually gauge/control how deep the logo recess should read — an easy, non-destructive way to iterate on depth before committing; adjust individual edges afterward for final shape polish as needed.

### Nodes / Settings
- **Import pipeline:** drag-and-drop image import (creates an Empty), Convert to Grease Pencil (Resolution setting), Convert to Path, Convert to Mesh (no direct Grease-Pencil-to-Mesh path available at time of recording).
- **Vertex cleanup:** Merge by Distance (M), Checker Deselect (per mesh island, hover+L to isolate), Dissolve Vertices (Ctrl+X), LoopTools > Space (even redistribution).
- **Resolution matching:** Subdivision Surface modifier (Catmull-Clark) applied to the lower-res target before cutting.
- **Cutting:** Knife Project (Mesh menu; Ctrl+click in Outliner to set the reference cutter object), Cut Through option (redo panel), viewing-angle-dependent projection.
- **Post-cut cleanup:** Select Non-Manifold, Merge by Distance, Fill (F), Connect Vertex Path (J), Auto Merge Vertices + G,G slide (manual fallback).
- **Depth:** Extrude (E) + Alt+S (scale along normals, not a flat axis) for clean recessed/embossed results; a scaled-down secondary Quadsphere as a non-destructive depth-reference guide.

### Difficulty
Intermediate

### Blender Version
Not specified — the Grease-Pencil-trace-to-mesh pipeline (requiring an intermediate Path conversion step) and Knife Project workflow are consistent with Blender 3.x-4.x.

### Tags
modelling, procedural, intermediate

---

## Related Tutorials
- [Image to 3D model workflow in Blender](image-to-3d-model-workflow-in-blender.md) — shares modelling, procedural; that flagship video's "Path A" (Trace Image to Grease Pencil → Mesh) is the same image-tracing pipeline used here, applied there to a full silhouette blockout rather than a Knife Project engraving.
- [Daily Blender Secrets - 10 ways to make Holes in Blender](daily-blender-secrets---10-ways-to-make-holes-in-blender.md) — shares modelling, procedural; that survey's Knife Project method (#1) is the same technique demonstrated here in full step-by-step depth on a curved surface.
- [Blender Secrets - Modeling Circular Hard Surface Details](blender-secrets---modeling-circular-hard-surface-details.md) — shares modelling, procedural; both rely on Knife Project to transfer a flat shape onto denser target geometry, applied there for bend-resolution rather than engraving a logo.
