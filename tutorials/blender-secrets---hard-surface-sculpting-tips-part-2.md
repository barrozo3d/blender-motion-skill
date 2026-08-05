---
title: Blender Secrets - Hard Surface Sculpting Tips Part 2
source: YouTube
url: https://www.youtube.com/watch?v=f8xoUkPY4e8
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (Dyntopo/Multires/Mask Extract workflow, 3.x-5.x)"
tags: [organic, procedural, materials, advanced]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---hard-surface-sculpting-tips-part-2/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - Hard Surface Sculpting Tips Part 2

**Source:** [YouTube](https://www.youtube.com/watch?v=f8xoUkPY4e8)
**Author:** Blender Secrets
**Duration:** 5m26s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Base mesh sculpting [0:00]
**Transcript (timestamped):**
[0:00] To create the base mesh, I add a round cube.
[0:03] Using the Grab brush, I push and pull it into shape.
[0:07] With Dintopo enabled, the Snake Hook brush allows me to pull out geometry.
[0:11] The Glace Trip brush is useful for adding and removing volume,
[0:15] which can then be smoothed out by holding Shift.
[0:18] Using the Crease brush, you can sketch out some ideas for refining the shape on the geometry.
[0:24] The Scrape brush is good for creating more angular and flattened hard surface shapes.
[0:29] Areas you don't like can just be erased with the Smooth brush.


### Mesh Filter - Inflate [0:34]
**Transcript (timestamped):**
[0:35] Create some panel cuts using the Mask brush.
[0:39] Using the Curve Stroke method, we can keep them nice and angular.
[0:50] Enable Symmetry so you get both sides.
[0:53] Select the Mesh filter in the Tool panel.
[0:56] Set Filter Type to Inflate.
[0:59] Drag the mouse cursor to the right to Inflate.
[1:04] Press Alt-M to clear the mask.
[1:07] Then set Filter Type to Smooth.
[1:10] It's a good idea to remesh at this point.
[1:13] So sample the geometry and then click on Remesh and wait for a moment.
[1:19] Finally, drag the mouse cursor to the right to smooth the geometry.


### Mask Extract [1:27]
**Transcript (timestamped):**
[1:27] One way to work with Hi-Polygon counts is to split an object into several smaller objects.
[1:33] Once you've created a rough base shape, you can use Mask Extract to extract geometry.
[1:40] Press E and choose a more hard surface friendly stroke method such as Curve.
[1:45] Draw some panel cuts.
[1:47] Then invert the mask with Ctrl-I.
[1:50] I want to remesh this object because I don't need that much geometry at this stage
[1:54] and I don't want everything to be slowed down.
[1:56] In the Remesh options, check Paint Mask so you can remesh without losing the mask.
[2:02] Choose a fox or size and click on Remesh.
[2:06] Go to Mask, Mask Extract.
[2:11] Click on OK.
[2:13] New geometry has been created based on the masked parts.
[2:17] We can hide the original round cube in the Outliner.
[2:20] A solidifier modifier was added automatically.
[2:23] We can increase the thickness of the extracted geometry.
[2:27] If we unhide the round cube, we can select all its vertices in edit mode and scale them down.
[2:36] Add a remesh modifier to the new geometry and set a fox or size that looks OK.
[2:41] It doesn't have to be too high res.
[2:43] Then right click and choose Visual Geometry to Mesh to apply all modifiers.
[2:48] Using the Mesh Filter set to Smooth, we can smooth out the remeshed geometry.
[2:53] If you want to separate these into individual objects, select all in edit mode and press B.
[2:59] Then choose Separate by Lose Parts.
[3:04] Hoover over an object and press Alt-Q in Scalp mode to sculpt on it.
[3:10] Or click left of the item in the Outliner.
[3:14] The current object selected for sculpting is then indicated with a brush icon.
[3:22] Now we can use the scrape brush in combination with a line or curve stroke method
[3:26] to add some beveling to the edges of these objects.
[3:29] And using a multiresse modifier to increase the resolution,
[3:34] we can add detail to the individual objects by using alpha textures.
[3:39] For more info about this, watch the previous hard surface sculpting tips video.
[3:44] Using a multiresse modifier, by default only the detail on the currently active object is shown.
[3:50] Using the Mesh Filter set to Smooth, we can select all the objects that we want to sculpt.


### Line Project [3:57]
**Transcript (timestamped):**
[3:57] Using Line Project, we can quickly create hard surface shapes.
[4:01] Add a Round Cube.
[4:03] Set it to Quadsphere with an arc value of 100 or more.
[4:07] The Round Cube is available after you enable the extra object add-on in Preferences.
[4:13] In Scalp mode, select the Line Project tool.
[4:17] In case your Quadsphere is too low-res for your taste, go back to Object mode.
[4:22] Right-click and choose Change Round Cube, then increase the arc value.
[4:28] Enable Mesh Symmetry.
[4:30] Drag the left mouse button to use the Line Project tool.
[4:35] Pressing F flips the direction.
[4:38] You can hold the spacebar to move the position of the line.
[4:43] Hold CTRL to constrain the angle.
[4:47] Check Limit to Segment if you want to limit the angle.
[4:51] If you want to limit the effect to where you draw the line.
[4:55] The Line Project tool flattens geometry, but doesn't actually do any boolean cutting.
[5:01] So it's a good idea to remesh after you've finished using it.
[5:05] Press Shift R to preview the remesh resolution.
[5:09] Then press CTRL R to remesh the geometry.
[5:14] This will make it easier to continue sculpting on it.
[5:17] When you add another round cube, it will remember the previous settings you used.



---

## Captured Frames

- [0:15] tutorials/frames/blender-secrets---hard-surface-sculpting-tips-part-2/frame_000.jpg
- [0:58] tutorials/frames/blender-secrets---hard-surface-sculpting-tips-part-2/frame_001.jpg
- [1:15] tutorials/frames/blender-secrets---hard-surface-sculpting-tips-part-2/frame_002.jpg
- [1:45] tutorials/frames/blender-secrets---hard-surface-sculpting-tips-part-2/frame_003.jpg
- [2:15] tutorials/frames/blender-secrets---hard-surface-sculpting-tips-part-2/frame_004.jpg
- [2:55] tutorials/frames/blender-secrets---hard-surface-sculpting-tips-part-2/frame_005.jpg
- [3:25] tutorials/frames/blender-secrets---hard-surface-sculpting-tips-part-2/frame_006.jpg
- [4:35] tutorials/frames/blender-secrets---hard-surface-sculpting-tips-part-2/frame_007.jpg

---

## Structured Notes

### Core Technique
Part 2 of a hard-surface sculpting series (a helmet/creature-head hybrid is the running example): organic base-mesh blocking with standard sculpt brushes, Mask+Mesh-Filter panel-cut carving, Mask Extract for splitting a design into separately-sculptable sub-objects with automatic Solidify thickness, and the Line Project tool for fast flat hard-surface faceting.

### Summary
Frame 000 shows the very start: a Dyntopo-sculpted organic base blob (round cube pushed/pulled with Grab/Snake Hook/Clay Strip/Crease/Scrape/Smooth brushes) already reading as a horned helmet silhouette. Frame 001 shows the panel-cut stage: the same shape now covered in an angular armor-plate pattern carved via Mask+Inflate, tool menu open on the left. Frame 002 shows the refined, remeshed-and-smoothed result of that same panel-cut pass — crisp raised plate seams with clean geometry. Frame 003 shows the Mask Extract setup: a Curve-stroke mask being drawn (orange highlighted path with red arrow) to define a plate boundary that will be extracted as a separate object. Frame 004 shows the Mask Extract operator's redo panel (Add Boundary Loop, Smooth Iterations, Apply Shrinkwrap) immediately after extraction — one helmet plate has now become its own detached shell. Frame 005 shows that extracted plate mid-refinement, with its own Solidify-modifier thickness and a visible extruded rim (orange outline) around the panel edges. Frame 006 shows close-up detail sculpting on one such extracted plate — sharper, more defined panel-line grooves being refined individually. Frame 007 shows the Line Project section's starting point: a plain Round Cube primitive (from the Extra Objects add-on) set to a low-facet Quadsphere shape, about to be faceted with the Line Project tool.

### Key Steps
1. **Base mesh sculpting:** start from a Round Cube (Extra Objects add-on); use the Grab brush to push/pull the overall shape; with Dyntopo enabled, Snake Hook pulls out new geometry (e.g. a horn); Clay Strip adds/removes volume (hold Shift to smooth); Crease sketches refinement lines; Scrape flattens areas into more angular hard-surface planes; Smooth erases mistakes.
2. **Panel cuts via Mask + Mesh Filter Inflate:** draw panel-cut lines with the Mask brush using Curve Stroke for clean angular shapes; enable Symmetry for matching both sides; open the Tool panel's Mesh Filter, set Filter Type to Inflate, and drag right to inflate the masked/unmasked regions into raised plates; Alt+M to clear the mask; switch Filter Type to Smooth; it's a good idea to Remesh at this point (sample the current geometry resolution, click Remesh, wait), then drag right again with the Smooth filter for a final clean pass.
3. **Mask Extract to split high-poly designs into sub-objects:** once a rough base shape exists, press E for a hard-surface-friendly stroke method (e.g. Curve) and draw panel-cut lines with the Mask tool; Ctrl+I to invert the mask; before extracting, Remesh the object down to a lighter resolution (enable "Paint Mask" in the Remesh options first so the mask survives the remesh) at whatever Voxel Size looks reasonable; go to Mask → Mask Extract, click OK — this creates new standalone geometry from the masked region (an automatic Solidify modifier is added, whose thickness can be increased). Hide the original base mesh in the Outliner once its plates have been extracted; if needed, unhide it, select all vertices in Edit Mode and scale down slightly so the base sits just under the plates. Add a Remesh modifier to the new extracted geometry (doesn't need to be high-res), right-click → Visual Geometry to Mesh to apply all modifiers, and use Mesh Filter → Smooth to clean up the result.
4. **Separate multiple extracted pieces into individual objects:** select all in Edit Mode, press P → Separate by Loose Parts. To sculpt on a specific piece afterward, hover over it and press Alt+Q (or click to the left of its name in the Outliner) — the actively-sculptable object is marked with a brush icon.
5. **Detail individual plates:** use the Scrape brush with a Line or Curve stroke method to bevel plate edges; add a Multiresolution modifier to increase resolution and sculpt fine detail using alpha textures (referenced as covered more fully in "Part 1" of this series). By default a Multires modifier only shows sculpted detail on the currently active object — select all objects you want to sculpt together first if working across several plates, and use Mesh Filter → Smooth across the whole selection when needed.
6. **Line Project for fast hard-surface faceting:** add a Round Cube (Extra Objects add-on) set to Quadsphere type with Arc value 100+ for a dense enough base; in Sculpt Mode select the Line Project tool; if the Quadsphere is too low-res, go back to Object Mode, right-click → Change Round Cube, and raise the Arc value. Enable Mesh Symmetry; drag the LMB to draw a flattening line-cut; press F to flip the flattening direction; hold Spacebar to reposition the line mid-draw; hold Ctrl to constrain the angle; enable "Limit to Segment" to restrict the effect to only where the line was drawn. Line Project flattens geometry but performs no actual boolean cut, so remeshing afterward is recommended — press Shift+R to preview the remesh resolution, then Ctrl+R to commit the remesh, making it easier to keep sculpting cleanly. New Round Cubes remember the previously-used settings.

### Nodes / Settings
- **Sculpt brushes:** Grab, Snake Hook (with Dyntopo), Clay Strip, Crease, Scrape, Smooth, Mask (Curve/Line stroke methods), Line Project.
- **Mesh Filter:** Inflate, Smooth (Tool panel).
- **Mask operations:** Ctrl+I (invert), Alt+M (clear), Mask → Mask Extract (Add Boundary Loop, Smooth Iterations, Apply Shrinkwrap options).
- **Modifiers:** Solidify (auto-added by Mask Extract), Remesh (Voxel Size, Paint Mask option to preserve mask through remesh), Multiresolution (for alpha-texture detail sculpting).
- **Add-on:** Extra Objects (Round Cube primitive, Quadsphere type with Arc value).
- **Edit-mode/object operators:** P → Separate by Loose Parts, Alt+Q (set active sculpt object), right-click → Visual Geometry to Mesh, right-click (Object Mode) → Change Round Cube.

### Difficulty
Advanced

### Blender Version
Not specified — Dyntopo/Multires sculpt workflow with Mask Extract and Line Project, consistent with modern Blender 3.x-5.x.

### Tags
organic, procedural, materials, advanced

---

## Related Tutorials
- [Blender Secrets - Hard Surface Sculpting Tips](blender-secrets---hard-surface-sculpting-tips.md) — shares organic, procedural, materials, advanced; **Part 1 of this same series** — covers panel cuts (Crease vs. persistent-base Layer brush), mask-based extrusion, and alpha-texture stamping/radial arrays that this Part 2 builds on.
- [Blender Secrets - Auto Masking Cavities in Sculpt Mode](blender-secrets---auto-masking-cavities-in-sculpt-mode.md) — shares organic, procedural; same channel, complementary Sculpt Mode masking technique.
- [6 Panel Cut Tips - Blender Secrets](6-panel-cut-tips---blender-secrets.md) — shares procedural, materials, advanced; same channel, directly overlapping panel-cut/hard-surface-detailing subject from a modifier-based (rather than sculpt-based) angle.
