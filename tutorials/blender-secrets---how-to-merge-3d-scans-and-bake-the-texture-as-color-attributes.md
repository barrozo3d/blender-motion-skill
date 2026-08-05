---
title: Blender Secrets - How to merge 3D Scans and bake the Texture as Color Attributes
source: YouTube
url: https://www.youtube.com/watch?v=AxDXWgFDwLA
author: Blender Secrets
ingested: 2026-08-04
blender_version: "3.2+ (Color Attributes bake workflow)"
tags: [materials, procedural, organic, cycles, advanced]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---how-to-merge-3d-scans-and-bake-the-texture-as-color-attributes/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - How to merge 3D Scans and bake the Texture as Color Attributes

**Source:** [YouTube](https://www.youtube.com/watch?v=AxDXWgFDwLA)
**Author:** Blender Secrets
**Duration:** 4m1s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Let's say you have two 3D scans and you want to merge them into one object without losing
[0:07] any textures.
[0:09] Make sure the objects both have enough geometry.
[0:13] If not, add a Subdiff modifier and apply it.
[0:17] With dense scans, however, it's a good idea to remove double vertices to avoid issues
[0:21] later.
[0:23] To do this, press M in Edit Mode and choose By Distance.
[0:28] Use a boolean cutter to remove any parts that you don't need.
[0:38] Apply the boolean modifier and remove the bounding box.
[0:44] Move and rotate the objects to overlap as desired.
[0:50] You can use proportional editing to adjust the way the objects overlap.
[0:55] Select proportional editing by pressing O and scroll the mouse wheel to change its
[1:00] influence radius.
[1:03] It's important that both objects have the same UV map name.
[1:07] Otherwise one of the objects will lose its texture after you join them.
[1:11] The name doesn't matter as long as it's the same for both objects.
[1:16] Select both objects and press Ctrl and plus on the numpad to join them using bool tool.
[1:22] Now they are merged into one object.
[1:24] I recommend inspecting the model on the inside.
[1:27] If the intersecting parts are not removed, try enabling whole tolerant on the modifier.
[1:34] Apply the boolean modifier and remove the bounding box.
[1:38] Duplicate this object and hide the original.
[1:42] Switch to scope mode.
[1:44] I like to use a madcap, it just makes it easier to see what you're doing.
[1:48] Enable Dintopo with constant detail.
[1:51] You can sample part of the model to get its resolution.
[1:55] Dintopo allows us to sculpt on the seam more easily, but it removes all texture information,
[2:00] which is why we are using a duplicate object.
[2:03] Use the clay strips brush and smooth to blend the two parts together.
[2:09] To get the colors back from the texture, we can bake the original texture to color attributes,
[2:14] formerly known as vertex colors.
[2:17] Hide a color attribute to the duplicate.
[2:23] In the Outliner, run hide and select the original textured mesh.
[2:28] Hold Ctrl and select the duplicate as well.
[2:31] Please note that if you do this selection order in the 3D viewport, you must hold Shift instead
[2:36] of Ctrl.
[2:37] In the Cycles Bake menu, for the bake type, select the texture channel you wish to bake
[2:41] from.
[2:42] In my case, I had the texture setup as an emission shader on the original mesh, so I
[2:46] have to choose Emit.
[2:48] But if your original texture is plugged into the diffuse channel, choose Diffuse and disable
[2:53] Direct and Indirect so there is no influence of lighting.
[2:57] Check Selected to Active to bake from the original textured mesh to the duplicate.
[3:02] As Output, choose Active Color Attribute.
[3:06] Make sure you are in Object Mode and click Bake.
[3:09] When it's done, hide the original mesh again.
[3:13] To see the colors in Object or Scoped Mode, enable Color Attribute in the Viewport Shading
[3:18] options.
[3:20] In case the bake didn't work perfectly, try increasing the extrusion value.
[3:24] This works like a bake cage.
[3:27] Make sure the objects are still selected in the right order and click Bake again.
[3:32] In my experience, an extrusion value of 0.2 often works well.
[3:37] You can use the Paint tool in Scoped Mode to paint on the mesh.
[3:41] By pressing S, you sample the color under the cursor.
[3:46] A low brush strength value helps to blend the colors more gradually.
[3:51] For more scoped tips, check my Scoped Playlist or get my Blender Secrets ebook.
[3:55] There is also a free sample if you want to check that out first.



---

## Captured Frames

- [0:35] tutorials/frames/blender-secrets---how-to-merge-3d-scans-and-bake-the-texture-as-color-attributes/frame_000.jpg
- [0:55] tutorials/frames/blender-secrets---how-to-merge-3d-scans-and-bake-the-texture-as-color-attributes/frame_001.jpg
- [1:20] tutorials/frames/blender-secrets---how-to-merge-3d-scans-and-bake-the-texture-as-color-attributes/frame_002.jpg
- [1:50] tutorials/frames/blender-secrets---how-to-merge-3d-scans-and-bake-the-texture-as-color-attributes/frame_003.jpg
- [2:05] tutorials/frames/blender-secrets---how-to-merge-3d-scans-and-bake-the-texture-as-color-attributes/frame_004.jpg
- [2:45] tutorials/frames/blender-secrets---how-to-merge-3d-scans-and-bake-the-texture-as-color-attributes/frame_005.jpg
- [3:15] tutorials/frames/blender-secrets---how-to-merge-3d-scans-and-bake-the-texture-as-color-attributes/frame_006.jpg
- [3:40] tutorials/frames/blender-secrets---how-to-merge-3d-scans-and-bake-the-texture-as-color-attributes/frame_007.jpg

---

## Structured Notes

### Core Technique
Merge two separately-textured 3D scans into one seamless object (demoed as a deer head grafted onto a cow body) without losing either texture: boolean-trim + join the meshes, Dyntopo-sculpt the seam on a texture-free duplicate, then bake the original photoscan textures back onto that sculpted duplicate as Color Attributes (vertex colors).

### Summary
Frame 000 shows the prep stage: a cow scan (black-and-white photoscanned texture) with a boolean cutter cube positioned to trim away the unwanted head. Frame 001 shows Proportional Editing (O, adjustable falloff circle) being used to smoothly reposition/blend the overlap area between the two scan parts before joining. Frame 002 shows the successful result: a deer head seamlessly boolean-joined (BoolTool, Ctrl+Numpad+, Union) onto the cow body — bounding box outline still visible, "Ctrl+[+]" shortcut hint confirming the join method. Frame 003 shows the Dyntopo sculpting stage on the seam: red matcap shading with the Dyntopo detail menu open (Constant Detail / Relative Detail / Brush Detail options, arrow pointing at it) — texture is grayed out at this point since Dyntopo strips it. Frame 004 shows the Clay Strips brush actively blending the seam on the deer-cow hybrid (still in matcap red, texture-free). Frame 005 shows the Cycles Bake node setup used afterward: an Emission shader chain (Texture Coordinate → Mapping → Image Texture → Emission → Material Output) — matching the transcript's note that the original texture was wired through Emission rather than Diffuse. Frame 006 shows the actual Bake panel mid-setup: Selected to Active checked, Bake Type = Emit, Margin/Extrusion settings visible, with the full-color textured deer-cow model now shown (orange selection outline) ready to bake onto the hidden duplicate. Frame 007 shows the final payoff: the fully colored, seamless deer-cow hybrid displayed via Color Attribute viewport shading directly on the sculpted/baked duplicate — with the Paint tool active in Sculpt Mode's tool list for final touch-up blending.

### Key Steps
1. **Prep both scans:** ensure both objects have enough geometry (add and apply a Subdivision modifier if not); for dense scans, remove doubled vertices first (Edit Mode, M → By Distance) to avoid problems later.
2. **Trim unwanted geometry:** use a boolean cutter object to remove parts you don't need from either scan; apply the Boolean modifier and delete the cutter/bounding-box object afterward.
3. **Position the overlap:** move/rotate the two objects so they overlap as intended; use Proportional Editing (press O, scroll to adjust the influence radius) to smoothly blend how the surfaces overlap where they'll be joined.
4. **Match UV map names:** before joining, make sure both objects' UV maps have the exact same name (the name itself doesn't matter, only that it matches) — otherwise one object loses its texture after joining.
5. **Join via BoolTool:** select both objects and press Ctrl+Numpad+ to union-join them with BoolTool. Inspect the model's interior afterward — if leftover intersecting geometry wasn't cleanly removed, enable "Hole Tolerant" on the Boolean modifier and re-apply, then delete the bounding box.
6. **Sculpt the seam on a texture-free duplicate:** duplicate the joined object and hide the original (which retains its texture); switch the duplicate to Sculpt Mode, use a matcap for clarity, enable Dyntopo with Constant Detail (sample part of the model to set an appropriate resolution) — Dyntopo makes seam-sculpting easy but destroys texture info, which is exactly why a duplicate is used instead of the original. Use Clay Strips and Smooth to blend the seam geometry together.
7. **Bake original texture back onto the sculpted duplicate as Color Attributes (vertex colors):** add a Color Attribute to the duplicate. In the Outliner, select the original textured mesh first, then Ctrl-select the duplicate as well (note: selection order convention flips — in the 3D viewport itself you'd need Shift instead of Ctrl for the same source→target order). In the Cycles Bake panel, set Bake Type to whichever shader channel the original texture is actually plugged into (Emit if it's wired through an Emission shader, as in this example; Diffuse if it's the base color — in that case also disable Direct and Indirect so lighting doesn't influence the bake). Check "Selected to Active" so it bakes from the original onto the duplicate; set Output to Active Color Attribute; make sure you're in Object Mode, then click Bake.
8. **View and refine the result:** once baked, hide the original mesh again; enable Color Attribute in Viewport Shading options to see the baked colors in Object/Sculpt Mode. If the bake has gaps or misses geometry, increase the Extrusion value (acts like a bake cage — 0.2 is often a good starting value) and re-bake with the same selection order. Use the Paint tool in Sculpt Mode to manually touch up color at the seam — press S to sample the color under the cursor, and use a low brush Strength for gradual blending.

### Nodes / Settings
- **Mesh cleanup:** Subdivision modifier (apply if geometry is too sparse), M → By Distance (remove doubles on dense scans).
- **Boolean:** BoolTool (Ctrl+Numpad+ join/union), Boolean modifier's Hole Tolerant option for imperfect intersections.
- **Editing:** Proportional Editing (O, scroll for radius) for smooth overlap blending.
- **Sculpt:** Dyntopo (Constant Detail, sampled resolution), Clay Strips, Smooth, Paint tool (S to sample color, low Strength for blending).
- **Shading (source texture, example used Emission):** Texture Coordinate → Mapping → Image Texture → Emission → Material Output.
- **Baking (Cycles):** Selected to Active, Bake Type (Emit or Diffuse with Direct/Indirect disabled), Output = Active Color Attribute, Extrusion (bake-cage-like offset, ~0.2 often works well), Object Mode required.
- **Viewport:** Color Attribute shading mode (to preview baked vertex colors without a texture).

### Difficulty
Advanced

### Blender Version
Not specified — "Color Attributes" (the modern renamed term for vertex colors) and Cycles Bake-to-Color-Attribute workflow are consistent with Blender 3.2+.

### Tags
materials, procedural, organic, cycles, advanced

---

## Related Tutorials
- [Blender Secrets - Hard Surface Sculpting Tips](blender-secrets---hard-surface-sculpting-tips.md) — shares organic, materials, advanced; same channel, complementary sculpt-mode masking/detailing knowledge.
- [Blender Secrets - 6 Minutes of Boolean Basics](blender-secrets---6-minutes-of-boolean-basics.md) — shares materials, procedural; same channel, directly relevant BoolTool/Boolean-modifier fundamentals used here for the scan-trimming step.
