---
title: 6 Panel Cut Tips - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=IZFniY_vyGo
author: Blender Secrets
ingested: 2026-08-04
blender_version: "5.0+ (Instances on Elements modifier is explicitly new in 5.0)"
tags: [procedural, materials, displacement, cycles, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/6-panel-cut-tips---blender-secrets/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# 6 Panel Cut Tips - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=IZFniY_vyGo)
**Author:** Blender Secrets
**Duration:** 5m19s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] When you're creating a model using a subdiff workflow, there's a couple of similar methods
[0:06] for creating panel cuts using modifiers.
[0:09] And both have some unique benefits.
[0:11] One way is to mark edges as sharp in edit mode and then add these modifiers in disorder.
[0:17] On the bevel modifier set miter outer to arc to avoid overhang issues in the corners.
[0:22] Use one or two segments depending on what you think looks best.
[0:26] The rest of the modifiers use their default settings.
[0:29] The good thing about this is that it's non-destructive, you can just change which edges are marked
[0:34] as sharp.
[0:35] For diagonal cuts, simply select vertices and press J to join them and then mark as sharp.
[0:40] Similarly, rather than marking edges as sharp, you can select them and then rip them by pressing
[0:45] V. The modifier stack remains the same except for the edge split modifier which we don't
[0:50] need.
[0:51] What's nice about this ripping method is that it creates these nice rounded panel cut
[0:55] corners.
[0:57] With all these modifiers to work a bit faster in edit mode, just turn off the option display
[1:01] modifier in edit mode.
[1:03] By the way, nothing's stopping you from using both methods at the same time.
[1:07] Just mark some edges as sharp for straight panel cuts and rip other edges so you get nice
[1:12] rounded panel cuts.
[1:13] If you're worried that all this is going to give you very bad or dense geometry, keep
[1:17] in mind that you're going to simply bake the result to a normal map and then use that
[1:21] on the original mesh.
[1:22] Let's look at another quick and easy way of making panel cuts in Blender.
[1:27] Draw some panel cuts using the Mask brush with a strength of 1.
[1:30] If the mask is not smooth, make sure you have plenty of geometry.
[1:34] Using the Curve Stroke method, we can keep everything nice and angular.
[1:38] Control right mouse button drag for curve handles or control right mouse button click
[1:42] for sharp angles.
[1:44] Hit enter to draw the mask under the curve.
[1:46] The curve projects the mask from the view so you can adjust the view to reuse the curve.
[1:50] Set brush size unit to scene to make sure that the radius doesn't change depending on the
[1:55] view.
[1:56] Press A to select all and X to delete the curve if you don't want to reuse its shape.
[2:00] You can also use the line stroke method for quick straight lines.
[2:04] Press Alt E and set the stroke method back to the default dots.
[2:07] Now select the mesh filter and set it to Inflate.
[2:10] Invert the mask with Ctrl I and drag the cursor to the left to deflate the unmasked panel
[2:15] cuts.
[2:16] Clear the mask with Alt M, sample the resolution and do a foxle remesh.
[2:20] Then use the mesh filter set to smooth to make the edges of the panel cuts less jagged
[2:25] if necessary.
[2:26] Later you can bake this to a normal map and use it on low poly geometry.
[2:30] Here's a quick and easy way to create panel cuts in Blender.
[2:33] First make sure you have enough subdivisions in your geometry.
[2:36] Also add a motorist modifier and subdivide it a few times.
[2:39] This way we have enough geometry to work with.
[2:41] In sculpt mode select the layer brush.
[2:44] Set it to subtract, reduce the height and then enable persistent and click on set persistent
[2:49] base.
[2:50] This allows you to draw strokes that don't accumulate in height.
[2:53] Press Alt E for the stroke method menu and choose a line.
[2:57] Now we can draw really straight lines.
[2:59] If you want to make sure the radius remains the same when you zoom in or out, set the
[3:03] brush size unit to scene instead of view.
[3:08] Sometimes when you press Ctrl Z it also undoes the set persistent base.
[3:12] If that happens just click on it again.
[3:14] In my opinion doing this in sculpt mode is the most fun and easy way to do this.
[3:19] If you don't want to mess with the dense high poly meshes required for painting a fine
[3:23] mask, painting panel cuts directly on a normal map is also possible.
[3:27] For this I recommend installing the free extension Youku Paint.
[3:31] Then click on quick Youku Paint node setup.
[3:34] Add a new image, choose normal and a high enough resolution.
[3:38] In texture paint mode you can now paint depth on the surface.
[3:42] With the line or curve stroke method you can paint panel cuts.
[3:46] Now to bake this to a real normal map texture select the normal channel, click on this gear
[3:51] icon and choose bake normal channel.
[3:54] Once it's baked you can save the normal map image texture.
[3:57] If there are some parts where afterwards you want to erase them or blur them you can open
[4:01] the normal map texture in the image viewer and then set it to paint mode.
[4:06] Pick the neutral color from the normal map texture and paint directly on the normal map
[4:10] or on the model in the 3D viewport.
[4:12] And of course save the image again to save the changes.
[4:15] Placing details on a surface is easy with the instances on elements modifier which was
[4:20] added in Blender 5.0.
[4:23] First create a vertex group and add some vertices to it.
[4:26] Add the instances on elements modifier to the object and select the detail that you
[4:31] want to place on the surface.
[4:32] Then pick the vertex group in the mask field.
[4:36] Adjust the scale as needed.
[4:37] You can also add objects to a collection and then use that collection in the modifier.
[4:42] Enable pick instance to make sure that it's placed correctly.
[4:45] If there's a gap between the surface and the instances you can use the surface offset
[4:49] to close the gap.
[4:50] Add and remove from the vertex group to place more or less details.
[4:54] You can also edit the vertex group in waitpaint mode with the strength of 2 and overlay is
[4:58] disabled.
[4:59] Now you have a nice interactive and non-destructive method for adding details.
[5:04] Before baking this to a normal or height map make sure a realized instances is enabled.
[5:09] Otherwise the instances won't show up on the baked texture.
[5:12] For more hard service tips check out my complete hard service bundle on 3dsecrets.com.



---

## Captured Frames

- [0:20] tutorials/frames/6-panel-cut-tips---blender-secrets/frame_000.jpg
- [0:55] tutorials/frames/6-panel-cut-tips---blender-secrets/frame_001.jpg
- [1:44] tutorials/frames/6-panel-cut-tips---blender-secrets/frame_002.jpg
- [2:20] tutorials/frames/6-panel-cut-tips---blender-secrets/frame_003.jpg
- [2:57] tutorials/frames/6-panel-cut-tips---blender-secrets/frame_004.jpg
- [3:38] tutorials/frames/6-panel-cut-tips---blender-secrets/frame_005.jpg
- [4:31] tutorials/frames/6-panel-cut-tips---blender-secrets/frame_006.jpg
- [5:04] tutorials/frames/6-panel-cut-tips---blender-secrets/frame_007.jpg

---

## Structured Notes

### Core Technique
Six distinct ways to create hard-surface panel-cut details (armor plating, machined casing seams) — non-destructive modifier stacks, sculpt-mode masking/layer brushes, texture-paint normal painting, and the Blender 5.0 Instances on Elements modifier for scattered surface details — most feeding into a baked normal map for use on low-poly geometry.

### Summary
A dense hard-surface tips reel. Frame 000 shows the payoff of method 1: a Bevel modifier (Miter Outer = Sharp, tested against Arc) on sharp-marked edges producing crisp panel seams, called out with an arrow. Frame 001 shows the same modifier stack (Subdivision → Solidify → Bevel → Subdivision) applied to a cylindrical object, producing clean panel-line geometry. Frame 002 shows method 2: drawing a panel-cut mask in Sculpt Mode with the Curve Stroke tool (Ctrl+RMB drag/click for handles/sharp corners) at Strength 1 on a dense mesh. Frame 003 shows the Mesh Filter set to Inflate being used to deflate the unmasked (inverted) region, carving the panel cut into the surface — before/after split-view. Frame 004 shows method 3: Sculpt Mode's Layer brush (subtract, persistent base) with Alt+E's stroke-method menu open, about to switch to Line for perfectly straight sculpted panel lines. Frame 005 shows method 4: painting panel depth directly onto a normal map via the free Youku Paint extension's New Layer (Bump Map channel) dialog in Texture Paint mode. Frame 006 shows method 5 in action: the Blender 5.0 Instances on Elements modifier scattering five different rivet/bolt-like detail objects around a fluted cylindrical surface via a vertex group mask. Frame 007 shows the baking step — a high-poly panel mesh baking its detail down to a normal map for a low-poly target, split view showing source geometry next to the resulting purple normal-map texture.

### Key Steps
Six independent methods, each ending in "bake to a normal map for low-poly use":
1. **Sharp-edge + modifier stack (non-destructive, straight/diagonal cuts):** mark edges Sharp in Edit Mode; stack modifiers in order (Subdivision → Solidify/Edge Split as needed → Bevel → Subdivision); on the Bevel modifier set Miter Outer to Arc to avoid overhang artifacts at corners, 1-2 segments. For diagonal cuts, select two vertices and press J to create a new edge, then mark it Sharp too. Toggle "Display Modifier in Edit Mode" off to work faster.
2. **Rip-edge variant (rounded corners):** instead of marking Sharp, select edges and press V to rip them; same modifier stack minus the Edge Split modifier — produces naturally rounded panel-cut corners. Both methods can be combined on the same mesh (some edges marked Sharp for straight cuts, others ripped for rounded ones).
3. **Sculpt-mode mask + Inflate filter:** draw panel cuts with the Mask brush (Strength 1) using Curve Stroke (Ctrl+RMB drag = curve handle, Ctrl+RMB click = sharp corner, Enter to commit); set Brush Size unit to Scene so radius doesn't change with zoom; select all + X to delete the curve if not reusing it (Line Stroke method available for straight segments, Alt+E to reset stroke method to Dots); set Mesh Filter to Inflate, invert the mask (Ctrl+I) and drag left to deflate the panel-cut area; clear mask (Alt+M); optionally Quadriflow remesh at the sampled resolution and run Smooth mesh filter to soften jagged edges before baking to a normal map.
4. **Sculpt-mode Layer brush (straight lines, most ergonomic per the author):** ensure dense geometry (Multiresolution modifier subdivided a few times); select the Layer brush, set to Subtract, reduce height, enable Persistent + click "Set Persistent Base" so repeated strokes don't accumulate depth; Alt+E → Line stroke method for straight cuts; Brush Size unit = Scene for zoom-independent radius. Note: Ctrl+Z sometimes also undoes the persistent-base state — just re-click "Set Persistent Base" if that happens.
5. **Direct normal-map painting (no dense mesh required):** install the free Youku Paint extension, run "Quick Youku Paint Node Setup", add a new image (Normal channel, high resolution); in Texture Paint mode paint depth using Line/Curve stroke methods; bake to a real normal map via the channel's gear icon → Bake Normal Channel, then save the image. To fix mistakes, reopen the normal map in the Image Editor, sample the neutral (flat) normal color, and paint directly over problem areas either on the texture or in the 3D viewport.
6. **Instances on Elements modifier (Blender 5.0+, scattered surface details):** create a vertex group and add target vertices to it; add the Instances on Elements modifier, pick the detail object (or a Collection of several), set the Mask field to that vertex group, adjust Scale; enable Pick Instance for correct per-point placement, and use Surface Offset to close any gap between instances and the base surface. Edit the vertex group live in Weight Paint mode (Strength 2, overlay disabled) to add/remove detail placements. Before baking to a normal/height map, enable "Realized Instances" or the instances won't appear in the bake.

### Nodes / Settings
- **Modifiers:** Bevel (Miter Outer = Arc, 1-2 segments), Solidify, Edge Split, Subdivision Surface (Catmull-Clark), Multiresolution, Instances on Elements (Blender 5.0+: Instance On field, Instance Type Object/Collection, Mask vertex group, Pick Instance, Realized Instances, Surface Offset).
- **Sculpt tools:** Mask brush (Strength, Curve Stroke, Line Stroke), Mesh Filter (Inflate, Smooth), Layer brush (Subtract, Persistent Base), Brush Size Unit (Scene vs View).
- **Texture Paint / extension:** Youku Paint (free) — Bump/Normal channel node setup, Bake Normal Channel.
- **Baking:** high-poly detail → normal map for low-poly target, standard for all six methods.

### Difficulty
Intermediate to Advanced

### Blender Version
Blender 5.0+ (Instances on Elements modifier is explicitly stated as new in Blender 5.0; other five methods are version-agnostic modifier/sculpt workflows usable in any modern Blender)

### Tags
procedural, materials, displacement, cycles, intermediate, advanced

---

## Related Tutorials
- [How to Texture Realistic Buildings in Blender](how-to-texture-realistic-buildings-in-blender-b3d.md) — shares materials, procedural, displacement, intermediate; similar detail/wear-baking philosophy applied to a different surface domain.
- [How to Make Cyberpunk Scenes in Blender](how-to-make-cyberpunk-scenes-in-blender.md) — shares materials, procedural, displacement, intermediate.
