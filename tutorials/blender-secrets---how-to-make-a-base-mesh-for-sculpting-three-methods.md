---
title: Blender Secrets -  How to make a Base Mesh for Sculpting (three methods)
source: YouTube
url: https://www.youtube.com/watch?v=UojINqTfZsM
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 3.3.0 -- observed in frame_000"
tags: [organic, procedural, rigging, modelling, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---how-to-make-a-base-mesh-for-sculpting-three-methods/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets -  How to make a Base Mesh for Sculpting (three methods)

**Source:** [YouTube](https://www.youtube.com/watch?v=UojINqTfZsM)
**Author:** Blender Secrets
**Duration:** 5m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Enable the Skinify Rig Add-on in Preferences
[0:14] Enable the Rigify Add-on as well Press Shift A and add an armature of choice
[0:22] In post mode select the bones that you want to create a geometry from
[0:26] the Create tab in the Option panel and in the Skinify Rig options click Add Shape
[0:32] Hide or delete the armature With the geometry selected, press Ctrl A
[0:37] and choose Visual Geometry to mesh This applies to skin and subdivision modifiers
[0:42] that were added automatically Now you can use the Inflate Brush in Skulled
[0:47] mode to inflate the geometry From here you can separate all by loose parts
[1:00] in Edit mode and then join the parts together that you want to remesh
[1:17] In Object mode press Shift A and select Metaball Ball
[1:43] Press Shift D to duplicate it then move it to where you want to add it to the overall
[1:47] volume There are also a few other Metaball parameters
[1:52] to choose from You can press S to change their size, R
[1:57] to rotate and of course G to move
[2:27] When you're happy with the blockout, click on the main shape instead of the individual
[2:34] circles Right click and choose Convert to Mesh
[2:39] In Edit mode, select all and go to Mesh Symmetries
[2:44] You may have to switch the symmetries direction Then press M and choose By Distance so you
[2:50] can clean up overlapping vertices by reducing the Merge Distance
[2:55] Now you have a symmetrical base mesh that you can sculpt on
[3:26] Let's look at going from a thumbnail sketch to a sculpted 3D mesh
[3:32] First we need a base mesh Drag and drop your thumbnail sketch into the
[3:37] Front Viewport Press Alt G to make sure its location is
[3:42] reset to the World Origin Convert it to Grease Pencil using the Trace
[3:47] Image to Grease Pencil option Then convert that to a path
[3:55] And finally, convert the path to Mesh Hide or delete the original thumbnail empty
[4:01] and the Grease Pencil object Select all the vertices in Edit mode and
[4:05] press M to choose By Distance This way you can reduce the amount of vertices
[4:12] Then select all in Edit mode and press F to fill the shape
[4:16] Using Circle Select, select and dissolve or delete any vertices that aren't part of
[4:21] the outline Add a Mirror modifier set to Bisect so the
[4:25] model is symmetrical Then add a Solidify modifier and a Remesh
[4:32] modifier And set the Remesh modifier to Voxel
[4:37] Adjust the Voxel size but be careful Too small can cause Blender to freeze
[4:43] Now you can add Primitive Meshes to the shape in Edit mode
[4:47] These will be merged automatically with the rest of the model by the Voxel modifier
[4:52] Don't worry about achieving perfection at this point
[4:55] This is just a base mesh for the next sculpting stage
[5:07] If you found this topic interesting and would like to know more, don't forget that you can
[5:24] find it in my Blender Secrets ebook Along with almost 2000 pages of other tips
[5:30] To get an idea of what the ebook is like, you can download the free sample from my website



---

## Captured Frames

- [0:30] tutorials/frames/blender-secrets---how-to-make-a-base-mesh-for-sculpting-three-methods/frame_000.jpg
- [0:45] tutorials/frames/blender-secrets---how-to-make-a-base-mesh-for-sculpting-three-methods/frame_001.jpg
- [1:00] tutorials/frames/blender-secrets---how-to-make-a-base-mesh-for-sculpting-three-methods/frame_002.jpg
- [1:50] tutorials/frames/blender-secrets---how-to-make-a-base-mesh-for-sculpting-three-methods/frame_003.jpg
- [2:35] tutorials/frames/blender-secrets---how-to-make-a-base-mesh-for-sculpting-three-methods/frame_004.jpg
- [2:50] tutorials/frames/blender-secrets---how-to-make-a-base-mesh-for-sculpting-three-methods/frame_005.jpg
- [3:45] tutorials/frames/blender-secrets---how-to-make-a-base-mesh-for-sculpting-three-methods/frame_006.jpg
- [4:35] tutorials/frames/blender-secrets---how-to-make-a-base-mesh-for-sculpting-three-methods/frame_007.jpg

---

## Structured Notes

### Core Technique
Three distinct workflows for generating a sculptable base mesh from scratch: skeleton-driven mesh generation via the Skinify Rig + Rigify add-ons (demoed on a dragon/wyvern rig), Metaball blockout over a photo reference (demoed on a horse), and 2D silhouette tracing via Grease Pencil converted to a Voxel-remeshed 3D blob (demoed on a mech/robot design).

### Summary
Frame 000 shows Method 1's starting rig: a dragon/wyvern-style Rigify armature in Pose Mode with the Skinify Rig panel open (Add Shape, Thickness, Resolution, Bevel Faces, Head Offset visible) ready to generate mesh geometry from the selected bones. Frame 001 shows the resulting skinned mesh in Edit Mode — capsule-like tube geometry following each bone of the wing/limb rig, about to be inflated and cleaned up. Frame 002 shows the Separate menu with "By Loose Parts" highlighted, splitting the skinified mesh into individual pieces for selective remeshing/joining. Frame 003 shows Method 2's setup: a Metaball ball being scaled/positioned over a horse-and-rider photo reference, with Resolution, Influence, and Update settings visible in the sidebar. Frame 004 shows a further-developed metaball blockout — a smooth horse-body silhouette built from several overlapping metaball spheres, still shown with their individual influence-radius wireframes over the reference photo. Frame 005 shows the metaball, after Convert to Mesh, being cleaned up in Edit Mode: the Merge menu open with "By Distance" highlighted (red arrow) and a Symmetrize operator's redo panel visible (Direction, Threshold) — confirming the transcript's symmetry-fix-then-merge-vertices step. Frame 006 shows Method 3's source material: a black silhouette of a bipedal mech/robot design loaded as a Front Orthographic background reference Empty. Frame 007 shows the resulting traced base mesh — a blocky, low-poly silhouette matching the robot's outline — with a modifier stack of Mirror → Solidify → Remesh (Voxel mode, Voxel Size, Smooth Shading) visible in the sidebar.

### Key Steps
**Method 1 — Skeleton-driven (Skinify Rig + Rigify):**
1. Enable the Skinify Rig add-on and the Rigify add-on in Preferences.
2. Shift+A to add an armature of choice (a Rigify metarig).
3. In Pose Mode, select the bones to generate geometry from, open the Create tab in the N-panel, and click Add Shape under Skinify Rig options.
4. Hide or delete the armature once the mesh is generated.
5. With the generated geometry selected, Ctrl+A → Visual Geometry to Mesh — this applies the Skin and Subdivision modifiers that Skinify Rig adds automatically.
6. Switch to Sculpt Mode and use the Inflate brush to round out the tube-like base shape.
7. In Edit Mode, Separate by Loose Parts, then re-join (Ctrl+J) whichever pieces should be remeshed together as a single object.

**Method 2 — Metaball blockout over reference:**
1. Shift+A → Metaball → Ball in Object Mode.
2. Shift+D to duplicate additional metaball spheres, moving (G), scaling (S), and rotating (R) each one into place to block out major volumes against a photo reference.
3. Once the blockout reads correctly, select the main metaball object (not the individual sub-balls) and right-click → Convert to Mesh.
4. In Edit Mode, select all, use Mesh → Symmetrize (switching the symmetry Direction if the result mirrors the wrong way), then M → By Distance to merge overlapping vertices — lowering the Merge Distance value as needed for clean results without collapsing intended detail. This produces a clean, symmetrical sculptable base mesh.

**Method 3 — 2D silhouette trace (Grease Pencil) + Voxel Remesh:**
1. Drag and drop a thumbnail/silhouette sketch into the Front Viewport as a reference image; press Alt+G to reset its position to World Origin.
2. Convert it to Grease Pencil using the "Trace Image to Grease Pencil" operator, convert that Grease Pencil object to a Path, then convert the Path to a Mesh.
3. Hide or delete the original reference image Empty and the intermediate Grease Pencil object.
4. In Edit Mode, select all vertices and M → By Distance to reduce vertex count from the trace; select all and press F to fill the outline into a flat face.
5. Use Circle Select to select and dissolve/delete any stray vertices that aren't part of the intended outline.
6. Add a Mirror modifier set to Bisect for symmetry, then a Solidify modifier for thickness, then a Remesh modifier set to Voxel mode — carefully tune Voxel Size (too small can freeze Blender).
7. Optionally add primitive meshes directly in Edit Mode near the traced shape — the Voxel Remesh will automatically merge them into the base mesh. Precision doesn't matter at this stage since it's only a rough base for the subsequent sculpting pass.

### Nodes / Settings
- **Add-ons:** Skinify Rig, Rigify.
- **Skinify Rig panel:** Add Shape, Thickness, Resolution, Bevel Faces, Head Offset.
- **Modifiers (auto-added / manually stacked):** Skin + Subdivision (from Skinify Rig, applied via Visual Geometry to Mesh), Mirror (Bisect), Solidify, Remesh (Voxel mode, Voxel Size, Smooth Shading).
- **Sculpt:** Inflate brush (rounding out skinified tube geometry).
- **Metaball settings:** Resolution, Render, Influence, Update on (Always, etc.).
- **Mesh operators:** Separate → By Loose Parts, Ctrl+J (join), Convert to Mesh, Mesh → Symmetrize, M → Merge By Distance, F (fill), Circle Select + Dissolve/Delete.
- **Grease Pencil workflow:** Trace Image to Grease Pencil, Convert → Path, Convert → Mesh, Alt+G (reset location).

### Difficulty
Intermediate to Advanced

### Blender Version
Not specified — Skinify Rig/Rigify, Metaball, and Grease Pencil trace/Voxel Remesh are all consistent with modern Blender 3.x-5.x.

### Tags
organic, procedural, rigging, modelling, intermediate, advanced

---

## Related Tutorials
- [Blender Secrets - Hard Surface Sculpting Tips](blender-secrets---hard-surface-sculpting-tips.md) — shares organic, procedural, advanced; same channel, natural next step once a base mesh exists.
- [Blender Secrets - Hard Surface Sculpting Tips Part 2](blender-secrets---hard-surface-sculpting-tips-part-2.md) — shares organic, procedural, advanced; same channel, its own base-mesh-sculpting section (Round Cube start) is a simpler alternative to these three methods.
