---
title: Blender Secrets - 5 minutes of N-Gons to Quads tips
source: YouTube
url: https://www.youtube.com/watch?v=DwpajQ0oQPI
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (core mesh-editing/modifier workflow, 3.x-5.x)"
tags: [modelling, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---5-minutes-of-n-gons-to-quads-tips/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - 5 minutes of N-Gons to Quads tips

**Source:** [YouTube](https://www.youtube.com/watch?v=DwpajQ0oQPI)
**Author:** Blender Secrets
**Duration:** 5m28s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] In this example I've traced the outline of a leaf.
[0:12] Pressing F fills it with one endgon.
[0:15] It is perfectly flat and can't bend at all.
[0:21] Pressing Alt F fills it with triangles.
[0:24] Follow that up with Alt J to convert some of them to quads.
[0:29] Now we can bend it a bit, but you get these ugly artifacts.
[0:34] Instead of triangulating the leaf, create a new plane with some subdivisions and move
[0:38] it above the leaf.
[0:41] Select all the faces of the plane in edit mode, press X and choose only faces.
[0:49] Fill the leaf with a single endgon by pressing F.
[0:52] Select the leaf in object mode and press Tab to enter edit mode.
[0:56] Hold Ctrl and left click on the plane.
[0:59] Make sure that you are in Autographic View so that you can see the leaf and plane on
[1:03] top of each other.
[1:05] Go to Mesh, Knife Project.
[1:09] Now the leaf has many square cuts and can bend well.
[1:14] You don't need this plane anymore.
[1:17] There are still small endgones, but they don't cause shading issues at this scale.
[1:22] If you really want to, you can turn on Auto Merge and then slide these verges to each
[1:27] other by pressing G twice in order to clean up these parts.
[1:33] Or select them and press Ctrl X to dissolve them.


### Remesh Modifier [1:42]
**Transcript (timestamped):**
[1:43] If you have a flat object with endgones that you want to convert to quads, you can use
[1:47] a Remesh modifier.
[1:51] The Remesh modifier by itself doesn't really do the trick.
[1:54] It's because it needs more geometry than just a flat plane to work.
[1:59] Turn on Wireframe in the Object Viewport properties so that you can see better what's happening.
[2:04] Add a Solidify modifier with a low thickness value like 0.001.
[2:10] Make sure it is placed above the Remesh modifier.
[2:14] Set the Remesh modifier to Smooth.
[2:17] Carefully increase the OCT3 depth until you get the amount of faces that you want.
[2:23] Right click and choose Convert to Mesh to apply both modifiers at once.
[2:29] In Edit Mode, select All and press M and choose Merge by Distance.
[2:35] Then set the distance to a slightly higher value than what you used for the thickness
[2:39] before.


### Quads [2:42]
**Transcript (timestamped):**
[2:47] When modeling with booleans, sometimes you end up with large endgone areas.
[2:52] If they are surrounded by a quad geometry like in this case, you can easily turn them
[2:56] into quads.
[2:58] Just select the endgones while holding Shift.
[3:01] Then press Ctrl T to Triangulate.
[3:05] And press Alt J to turn Tri's to quads.
[3:08] In some cases, you may need to dissolve an edge or two with Ctrl X.
[3:13] Or slide a vertex by pressing G twice with other merge vertices enabled.


### Creasing [3:19]
**Transcript (timestamped):**
[3:25] Using the Knife tool can sometimes create endgones or triangles.
[3:32] In Edge Selection Mode, hold Alt and double click on the boundary loop to select it.
[3:38] Then go to Select, select Sharp edges.
[3:41] Press Shift E and 1 on the numpad to crease them with a value of 1.
[3:46] In Object Mode, add a Subtiff modifier with one level of subdivision and then apply the
[3:50] modifier.
[3:52] In Edit Mode, remove the creasing by pressing Shift E and minus 1 on the numpad.
[3:57] Now the endgones and triangles have been converted to quads.
[4:03] As you can see, the creasing has protected the shape from the Subtiff modifier.
[4:08] This technique adds geometry, so it's best used early in the modeling process.


### All triangles [4:23]
**Transcript (timestamped):**
[4:30] When you have a model like this, that's all triangles.
[4:33] Select All in Edit Mode and press Alt J.
[4:36] Now it's all quads.
[4:40] You can also do this through the Face menu.
[4:43] Just make sure all the faces are selected.
[4:49] This only works when the model was originally created with quads and then converted to triangles,
[4:54] as is often the case with models downloaded from the internet.
[5:06] If you found this topic interesting and would like to know more, don't forget that you can
[5:09] find it in my Blender Secrets ebook, along with almost 2000 pages of other tips.
[5:16] To get an idea of what the ebook is like, you can download the free sample from my website.



---

## Captured Frames

- [0:29] tutorials/frames/blender-secrets---5-minutes-of-n-gons-to-quads-tips/frame_000.jpg
- [1:09] tutorials/frames/blender-secrets---5-minutes-of-n-gons-to-quads-tips/frame_001.jpg
- [1:59] tutorials/frames/blender-secrets---5-minutes-of-n-gons-to-quads-tips/frame_002.jpg
- [2:17] tutorials/frames/blender-secrets---5-minutes-of-n-gons-to-quads-tips/frame_003.jpg
- [2:56] tutorials/frames/blender-secrets---5-minutes-of-n-gons-to-quads-tips/frame_004.jpg
- [3:05] tutorials/frames/blender-secrets---5-minutes-of-n-gons-to-quads-tips/frame_005.jpg
- [3:41] tutorials/frames/blender-secrets---5-minutes-of-n-gons-to-quads-tips/frame_006.jpg
- [4:36] tutorials/frames/blender-secrets---5-minutes-of-n-gons-to-quads-tips/frame_007.jpg

---

## Structured Notes

### Core Technique
Five ways to eliminate problem N-gons/triangles and get clean quad topology: Knife Project retopology from an overlaid subdivided plane, a Remesh+Solidify combo for flat n-gon shapes, Triangulate+Tris-to-Quads for boolean-created n-gon patches, Crease-protected Subdivision Surface to quad-ify knife-cut geometry, and a plain Tris-to-Quads pass for models that were originally all-quad before being triangulated.

### Summary
Frame 000 shows the core problem: a hand-traced leaf outline filled with triangles (Alt+F) then partially converted with Alt+J, which still produces visible bending artifacts (purple leaf, edit mode, triangulated fan pattern visible). Frame 001 shows the fix mid-process: a Top Orthographic view of the same leaf after Knife Project from an overlaid subdivided plane — the outline is now cut into a clean grid of small quads that will bend correctly. Frame 003 shows the Remesh-modifier tip's setup: a flat n-gon shape with a Solidify modifier (thin thickness) stacked above a Remesh modifier set to Smooth, Octree Depth 4 — converting the flat n-gon into a quad-covered mesh. Frame 004 shows a boolean-modeled cylindrical object with a stray large n-gon patch (orange) next to clean quad geometry. Frame 005 shows that same patch selected and circled, with Ctrl+T (Triangulate Faces, Quad/Ngon Method = Beauty) about to run on it before Alt+J converts it back to quads. Frame 006 shows a plane with an n-gon corner mid-knife-cut, about to have its boundary loop creased and Subdivision-Surface-protected. Frame 007 shows the payoff of the simplest tip: a classic Utah-teapot-style model, entirely selected, with Alt+J ("Tris to Quads") about to run — converting an all-triangle downloaded model back into clean quads.

### Key Steps
1. **Knife Project for organic/traced shapes:** filling a hand-traced outline with F (single n-gon, can't bend/deform) or Alt+F (triangles, then Alt+J for partial quads) both produce bad bending — instead, add a new subdivided Plane above the shape, in Edit Mode select all its faces and press X → Only Faces to delete just the plane's faces (keeping the grid of edges), fill the outline shape itself with a single n-gon (F), select the outline object in Object Mode → Tab into Edit Mode, Ctrl+click the plane to add it to the selection, switch to an orthographic view where both overlap cleanly, then Mesh → Knife Project — this cuts the plane's quad grid pattern into the outline. Delete the helper plane afterward. Leftover tiny n-gons at this scale usually don't cause shading problems; if needed, enable Auto Merge and slide vertices together with double-G, or select and Dissolve them with Ctrl+X.
2. **Remesh modifier for flat n-gon shapes:** a Remesh modifier alone fails on a flat plane because it needs volume to work with — enable Wireframe display to see what's happening, add a Solidify modifier with a very low thickness (e.g. 0.001) placed *above* the Remesh modifier in the stack, set Remesh to Smooth, and carefully raise Octree Depth until face density looks right. Right-click → Convert to Mesh to apply both modifiers together, then in Edit Mode select all and Merge by Distance at a threshold slightly larger than the Solidify thickness used, to weld the front/back shells back into one flat surface.
3. **Boolean-created n-gon patches:** when boolean modeling leaves a large n-gon area surrounded by clean quads, Shift-select just the n-gon(s), Ctrl+T to Triangulate, then Alt+J to convert back to quads — occasionally you'll still need to Dissolve a stray edge (Ctrl+X) or slide a vertex (double-G with Merge Vertices enabled) to fully clean up the result.
4. **Crease + Subdivision Surface to protect Knife-tool cuts:** the Knife tool can leave n-gons/triangles behind. In Edge Select mode, Alt+double-click the boundary loop to select it, Select → Select Sharp Edges to catch the rest, Shift+E then type 1 to crease those edges to full strength, add a Subdivision Surface modifier (1 level) in Object Mode and Apply it — the crease protects the original shape from being smoothed away while the subdivision itself converts the n-gons/triangles into quads. Afterward, in Edit Mode remove the now-unneeded crease with Shift+E, -1. Because this adds geometry, it's best applied early in the modeling process.
5. **All-triangle model → quads (simplest case):** if a model was originally quad-based and got triangulated somewhere along the way (common for internet-downloaded assets), simply select all in Edit Mode and press Alt+J (or Face menu → Tris to Quads) — this only works cleanly when the underlying topology was quad-based to begin with.

### Nodes / Settings
- **Mesh operators:** F (fill n-gon), Alt+F (fill triangle fan), Alt+J (Tris to Quads), Ctrl+T (Triangulate Faces), Mesh → Knife Project, M → Merge by Distance, Ctrl+X (Dissolve), double-G (Edge Slide with Auto Merge / Merge Vertices), Shift+E (Edge Crease, type 1 to add / -1 to remove), Select → Select Sharp Edges.
- **Modifiers:** Solidify (thin thickness, placed above Remesh in stack), Remesh (Smooth mode, Octree Depth), Subdivision Surface (1 level, used with creasing then applied).
- **Selection:** X → Only Faces (delete helper plane's faces while keeping its edge grid), Alt+double-click (select boundary edge loop).

### Difficulty
Intermediate

### Blender Version
Not specified — core mesh-editing and modifier workflow, version-agnostic across modern Blender (3.x-5.x).

### Tags
modelling, procedural, intermediate

---

## Related Tutorials
- [4 new retopology tips to discover! - Blender Secrets](4-new-retopology-tips-to-discover---blender-secrets.md) — shares modelling, intermediate; same channel, overlapping retopology/quad-cleanup subject matter.
- [Blender Secrets - 5 minutes of Topology Tips](blender-secrets---5-minutes-of-topology-tips.md) — shares modelling, procedural, intermediate; same channel, direct companion topology-cleanup video.
