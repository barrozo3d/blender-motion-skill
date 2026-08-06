---
title: Daily Blender Secrets - 15 Tips Compilation (part 3)
source: YouTube
url: https://www.youtube.com/watch?v=xLAakVcA1hc
author: Blender Secrets
ingested: 2026-08-04
blender_version: "2.8+ (Scatter Objects is described as a new default 2.8 add-on; Blue Noise Particles and Molecular are third-party add-ons)"
tags: [rigging, animation, cloth, simulation, rendering, particles]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-secrets---15-tips-compilation-part-3/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Secrets - 15 Tips Compilation (part 3)

**Source:** [YouTube](https://www.youtube.com/watch?v=xLAakVcA1hc)
**Author:** Blender Secrets
**Duration:** 10m47s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Scale down the constraints so that they are easier to work with.
[0:17] Move and rotate the empties to be aligned with the body parts.
[0:21] Temporarily check the animated box for any body parts you don't want to move.
[0:26] Change body constraint type to generic.
[0:29] Check the linear boxes and set them to zero.
[0:33] Check the angular boxes as well.
[0:34] In the case of this joint, we only rotate around the x-axis.
[0:38] Lower means on the left side, upper means on the right side.
[0:43] We can check that we've limited the right axis with the passive rigid body box.
[0:50] Of course some joints need more than one axis of rotation, like the neck.
[0:55] Now repeat this for every joint on the body.
[1:03] Now we are going to connect our ragdoll to this armature.
[1:07] First in edit mode, we need to remove the parent from each bone.
[1:12] Next we go to post mode.
[1:14] Select a bone and add a child of bone constraint.
[1:18] As the target, select the part of the ragdoll that surrounds the bone, the hitbox.
[1:23] If the bone jumps away, click on set inverse.
[1:26] Be careful that you select the hitbox and not the armature.
[1:30] Zooming in helps.
[1:32] Do this for all the bones.
[1:33] Now the armature is parented to the ragdoll.
[1:42] To simulate a piece of cloth moving in ultra slow motion is actually very easy.
[1:47] First we add a cloth modifier to this subdivided plane and a collision modifier to this sphere.
[1:52] Then set enough keyframes in the render settings.
[1:55] Similarly set enough keyframes in the cloth cache settings.
[1:59] Now simply change the value in the speed multiplier to something smaller like 0.05.
[2:05] Then play the simulation by pressing the spacebar.
[2:13] I decided to update this inverted hill video since the interface of blender 2.0 changed
[2:18] a lot and a lot of people asked me where the backface culling option went.
[2:22] So here we go.
[2:24] Create a base color material.
[2:26] Go to render view and increase the world brightness so you can see what you're doing.
[2:30] Create a second material for the outline.
[2:33] You can use an emission shader or tune shader for the outline material.
[2:37] In the material settings, turn on backface culling.
[2:40] Add the solidify modifier and check flip normals.
[2:44] Set the material index offset to 1 and play with the thickness to get the outline.
[2:52] To render, turn off overlays and go to view and choose viewport render image.
[3:02] Scalp some detail on a subdivided plane.
[3:05] Turn on smooth shading.
[3:07] Add this colorful matte cap.
[3:09] Go to the top view by pressing 7 on the numpad and press Ctrl Alt 0 to move the camera to
[3:14] match the top view.
[3:16] Set the resolution to something like 1024 by 1024.
[3:21] Lock camera to view and move it so the plane fills the image.
[3:24] Turn off overlays.
[3:26] Now render the viewport with view viewport render image.
[3:30] Now we've got a normal map.
[3:32] Add a second plane with just one face.
[3:34] Add a material to it and plug in a normal map node and the image you saved.
[3:38] Set the image to non-color data.
[3:41] In rendered mode we can see the normal map working.
[3:49] Create an object with enough subdivisions around the thing that you want to vacuum pack.
[3:54] Select a rim of vertices.
[3:55] Add the vertices to a vertex group.
[3:58] Enable collision for the monkey.
[4:00] Turn on cloth for the packing object.
[4:03] Increase the quality steps to 25.
[4:05] Add the vertex group to the pin group.
[4:08] Increase the collision quality to 10.
[4:10] And turn on self-collisions.
[4:12] Turn off gravity.
[4:14] Turn on pressure.
[4:15] Now at frame 0 set the pressure keyframe of 0.
[4:18] Then at the later frame set the pressure keyframe of minus 100 or minus 200.
[4:24] Limit the cache size to what is needed and pick the simulation.
[4:28] Press the spacebar to see the result.
[4:37] The scatter objects add-on is a new default add-on in Blender 2.8 that you need to activate
[4:41] in preferences to use.
[4:43] It allows us to quickly scatter things in a more intuitive and easy way than using the
[4:47] particle system.
[4:49] Select an object that you want to scatter, then holding shift select the surface you
[4:52] want to scatter them on.
[4:54] Press F3 for the search menu and search for scatter.
[4:57] Then click and draw the objects on the surface.
[5:00] What makes this add-on really cool is that you can now change a lot of the settings and
[5:03] see visually what you are doing.
[5:06] Then press enter to confirm.
[5:08] This is really a lot faster and more fun than tweaking particle settings options.
[5:12] This object in the middle is the instancer, which won't show up in the render, but you
[5:15] can use it to quickly move or scale the instances.
[5:22] Add some particles on a surface.
[5:25] Activate the 3D print toolbox add-on in preferences.
[5:28] Apply the protocol modifier and delete the particle system.
[5:31] Select all the particles, which are now mesh objects, and select one again to make it the
[5:35] active one.
[5:36] Press Ctrl J to join them all into one object.
[5:39] Press N to open the option panel and open the 3D print tab.
[5:42] Click on intersections.
[5:44] Click on the resulting intersect face button.
[5:47] Press Ctrl L to extend the selection.
[5:49] Now press X and choose delete faces.
[5:52] Now you only have non-overlapping particles left.
[5:59] Download the Zid file from GitHub.
[6:01] Don't unzip it, but install it as a file from their blender preferences.
[6:04] Now select the surface that you want to distribute particles onto.
[6:08] Press Shift A and from the mesh menu, choose blue noise particles.
[6:12] This opens the blue noise menu.
[6:13] For nice evenly spaced particles, choose the highest quality setting.
[6:17] Set noise type to even and generate vertices.
[6:20] Press OK.
[6:21] Now a particle system is generated.
[6:23] You can go to render and choose objects as the particle and choose which object you want
[6:27] to use.
[6:28] You may need to increase the size a bit.
[6:29] This creates a very nice organic looking distribution of particles that don't overlap
[6:33] each other.
[6:34] You can also choose a patchy distribution or use a vertex group from weight painting.
[6:38] In that case the particles do overlap a bit sometimes.
[6:48] Download the new object build of Blender from Graphic All.
[6:51] Download an OpenVDb file.
[6:53] You can find a list of websites with free OpenVDb files on my website.
[6:58] Add some light like a sun.
[7:00] Press Shift A and choose volume and import the OpenVDb file.
[7:04] Navigate to the OpenVDb file and click on import.
[7:07] If you don't see anything, you may need to scale the object down.
[7:12] And turn on volumetric shadows.
[7:14] And lower the tile size for more detail.
[7:17] Create a new material.
[7:19] Increase the density.
[7:20] Change the name in the temperature attribute in the shader to what it is in the volume
[7:24] grids panel.
[7:26] Increase the blackbody intensity and the temperature.
[7:35] Create a duplicate of your surface.
[7:37] Name one force and the other emitter.
[7:39] Add a particle system to the emitter object with these settings.
[7:42] These ensure the particles appear immediately and don't disappear.
[7:45] Turn on rotation and use these settings so they rotate randomly.
[7:48] Set physics type to fluid and use these settings.
[7:51] This basically makes sure the particles don't fly away.
[7:53] Now for the advanced stuff.
[7:55] These settings make the particles be repulsed by each other.
[7:58] Render them as objects and choose your particle instance object.
[8:01] Change the size and randomness to your liking.
[8:03] Turn off gravity so everything doesn't fall down.
[8:06] Select the force object and add a force to it with these settings so the particles will
[8:10] be moving around.
[8:11] Now when you start the simulation, the particles will rearrange themselves until they are no
[8:15] longer touching.
[8:16] Thanks to the talented Yigur Smirnov for figuring this out.
[8:22] In edit mode, select the edges that you want to add thickness to and press Ctrl F and choose
[8:27] wireframe.
[8:28] You can then adjust the thickness and choose whether to replace those edges or add the
[8:32] thickness on top of the model.
[8:34] For a non-destructive version of this, you can add the wireframe modifier.
[8:38] The benefit of this besides the non-destructive workflow is that you can use weight painting
[8:43] to influence the thickness.
[8:50] First install the free molecular add-on.
[8:52] Follow the zip file and without unpacking it, install it from Blender's preferences.
[8:57] Create a ground plane with collision enabled and damping set to 1.
[9:00] Add a meter ball to the scene and move it to the side.
[9:03] Add another plane, scale it down in edit mode and add a particle system to it.
[9:07] Decrease the particle number and increase their lifetime.
[9:10] Under physics and deflection, enable size deflect.
[9:13] Use the meter ball as a particle object.
[9:15] You may need to increase the scale to see anything.
[9:17] You can increase the meter ball resolution.
[9:19] A lower number means more detail.
[9:21] Then scroll down in the particle system and activate molecular.
[9:25] Activate the particles linking.
[9:26] This makes them stick together.
[9:28] Increase the search length to increase how much they stick.
[9:31] Then click on start molecular simulation.
[9:41] To inset individual faces, press I twice.
[9:45] Toggle this by pressing I.
[9:47] You can even turn it into an extrude by holding CTRL.
[9:50] Press O if you want the extra edges to be created outside of your selection instead
[9:54] of inside.
[9:56] This is called an outset.
[9:58] Pressing B toggles whether the boundary is also inset or not.
[10:02] You can also use the inset menu for these options and more.
[10:10] If you need to focus on just one object, there's a couple of things you can do.
[10:14] With the object you want to work on selected, press SHIFT H to hide everything else.
[10:19] Alt H unhides them again.
[10:20] This also works in edit mode.
[10:23] Another thing you can do is press forward slash.
[10:25] That will isolate the selected object and zoom in on it as well.
[10:29] Press forward slash again and the view will go back to what it was before.
[10:32] Finally if your object is in a collection, you can right click on it in the outliner
[10:36] and go to visibility isolate.



---

## Captured Frames

- [0:26] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-3/frame_000.jpg
- [1:14] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-3/frame_001.jpg
- [2:05] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-3/frame_002.jpg
- [2:37] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-3/frame_003.jpg
- [3:30] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-3/frame_004.jpg
- [4:14] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-3/frame_005.jpg
- [4:54] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-3/frame_006.jpg
- [6:08] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-3/frame_007.jpg

---

## Structured Notes

### Core Technique
A direct continuation of Part 2's ragdoll build (finishing Rigid Body Constraint limits and parenting an Armature to the ragdoll hitboxes via Child Of bone constraints), followed by 13 more standalone tips spanning cloth (slow-motion sim, vacuum-pack pressure), rendering tricks (inverted-hull outline shader, baked normal maps), and four different particle/scatter techniques (Scatter Objects add-on, 3D-Print-Toolbox non-overlap cleanup, Blue Noise Particles add-on, self-repulsing fluid-physics particles), plus OpenVDB volumetrics, wireframe thickness, inset/outset, and viewport-isolation shortcuts.

### Summary
Frame 000 continues the Part 2 ragdoll build: a cube-built stick figure with the Rigid Body panel open, Animated checkbox highlighted in red, as instructed to temporarily freeze body parts that shouldn't move while tuning constraints. Frame 001 shows the next stage — switching to Pose Mode on an Armature overlaid on the ragdoll's colored hitbox cubes, about to add a Child Of bone constraint per bone so the armature follows the physics rig. Frame 002 shows the ultra-slow-motion cloth setup: a draped plane over a sphere with the Cloth modifier's Speed Multiplier field highlighted, being lowered to 0.05. Frame 003 shows the inverted-hull outline technique: a green cube's "Outline" material with Surface set to Toon BSDF-derived settings and "Backface Culling" highlighted in the Settings section. Frame 004 shows the payoff of the normal-map-baking tip: a colorful tangent-space normal map image, captioned "Now you've got a normal map!" — baked by viewport-rendering a mattecap-shaded plane from a locked top-down camera. Frame 005 shows the vacuum-pack effect: an organic blob-shaped cloth mesh wrapped tightly around a hidden object, with the Cloth Physical Properties panel open and Pressure just enabled. Frame 006 shows the Scatter Objects add-on's F3 search menu open with "Scatter" typed, about to invoke the operator. Frame 007 shows the Blue Noise Particles add-on's Mesh Add menu with "Blue Noise Particles" highlighted, for generating evenly-spaced, non-overlapping particle distributions on a landscape mesh.

### Key Steps
1. **Ragdoll finishing (continued from Part 2):** scale down Rigid Body Constraint empties for easier handling; move/rotate them to align with each body part; temporarily enable the Animated checkbox on parts you don't want moving while tuning; set each constraint's Type to Generic; enable and zero the Linear limit axes, then enable the Angular limits per joint (e.g. only X rotation for a simple hinge, with "lower" = one side / "upper" = the other), verifying limits visually via the passive Rigid Body box; repeat per joint (multi-axis joints like the neck need more than one enabled axis).
2. **Parenting an Armature to a ragdoll:** in Edit Mode, clear each bone's parent; switch to Pose Mode, select a bone, add a Child Of bone constraint targeting the corresponding ragdoll hitbox part (not the armature itself — zoom in to avoid mis-picking); click Set Inverse if the bone jumps out of place; repeat for every bone so the armature now follows the ragdoll simulation.
3. **Ultra-slow-motion cloth:** add a Cloth modifier to a subdivided plane and a Collision modifier to the object it drapes over; set enough keyframes in both the render range and the Cloth cache settings; lower the Cloth modifier's Speed Multiplier (e.g. to 0.05) and play the sim for extreme slow motion.
4. **Inverted-hull outline shader (updated for the 2.8 UI):** create a base-color material; raise World brightness in Render view for visibility; create a second "outline" material using an Emission or Toon shader; enable Backface Culling on it; add a Solidify modifier to the object with Flip Normals checked, set the modifier's Material Index Offset to 1, and tune Thickness for outline width; disable overlays and use View > Viewport Render Image to render the stylized result.
5. **Baking a normal map from sculpted detail without UVs:** sculpt detail on a subdivided plane, enable smooth shading, apply a colorful matcap; frame it exactly from the top (Numpad 7, then Ctrl+Alt+Numpad0 to snap the camera to that view); set render resolution (e.g. 1024×1024); lock the camera to the view and frame the plane to fill it; disable overlays; render via View > Viewport Render Image to capture a tangent-space normal map. Add a second single-face plane, create a material with an Image Texture (set to Non-Color data) piped into a Normal Map node, and the baked image reads correctly in Rendered view.
6. **Vacuum-pack cloth effect:** build a well-subdivided wrapping mesh around the target object; select a rim of vertices into a Vertex Group; enable Collision on the target (e.g. a monkey) and Cloth on the wrapping mesh; raise Quality Steps (≈25) and Collision Quality (≈10); assign the rim group as the Pin Group; enable Self Collisions; disable Gravity; enable Pressure and keyframe it (0 at frame 0, then −100 to −200 at a later frame) so the cloth sucks inward and wraps the target; limit the cache size to what's needed and bake before playing.
7. **Scatter Objects add-on (bundled since Blender 2.8, needs enabling in Preferences):** select the object to scatter, Shift-select the target surface, press F3 and search "Scatter," then click-drag across the surface to paint instances while live-tuning settings, Enter to confirm — much faster than particle-system tuning; the small object left at the scatter origin is the Instancer, used to move/scale the whole scatter without appearing in the render.
8. **3D Print Toolbox for non-overlapping particles:** scatter particles on a surface, enable the 3D-Print-Toolbox add-on, apply the particle system as real mesh objects (via Convert modifier equivalent) and delete the particle system; select all resulting objects, make one active, Ctrl+J to join into a single object; open the N-panel's 3D-Print tab, run Intersections, click the resulting "Intersect" face-select button, Ctrl+L to select linked, then X > Delete Faces — leaving only the non-overlapping particle instances.
9. **Blue Noise Particles add-on:** install the add-on's zip directly from Preferences (don't unzip first); select the target surface, Shift+A from the Mesh menu choose Blue Noise Particles; in its dialog pick the highest quality setting for evenly spaced results, set Noise Type to Even, generate vertices, OK; the resulting particle system's Render tab lets you pick Object as the render type and choose the instanced object (may need a size bump) for an organic, non-overlapping distribution — a Patchy option or a weight-painted Vertex Group can also drive density, at the cost of some overlap.
10. **OpenVDB volumetrics:** obtain a build of Blender with volume support and an OpenVDB file; add a Sun light; Shift+A > Volume > Import OpenVDB, navigating to the file (may need to scale the resulting volume object down); enable Volumetric Shadows and lower Tile Size for more detail; create a volume material, raise Density, rename the shader's temperature attribute to match the name shown in the Volume grids panel, and raise Blackbody Intensity/Temperature for a fire-like look.
11. **Self-repulsing fluid-physics particles:** duplicate the target surface into a "force" copy and an "emitter" copy; add a particle system to the emitter tuned so particles appear immediately and persist, with randomized rotation; set the particle Physics type to Fluid so particles don't fly apart, and enable settings that make particles repel each other; render them as objects with a chosen instance object, tuned size/randomness; disable Gravity; add a Force field to the force object; running the sim lets the particles self-arrange until none overlap (technique credit: Yigür Smirnov).
12. **Wireframe thickness:** in Edit Mode, select the edges to thicken and press Ctrl+F > Wireframe, then adjust thickness and choose whether to replace the edges or add thickness on top; for a non-destructive version, add the Wireframe modifier instead, which also supports weight-painting to vary thickness.
13. **Molecular add-on foam/bubble sim:** install the free Molecular add-on's zip from Preferences without unpacking; create a ground plane with Collision enabled and Damping 1; add a Metaball and move it aside; add another plane, scale it down in Edit Mode, and give it a particle system with reduced particle count and increased lifetime; under Physics > Deflection enable Size Deflect; set the Metaball as the particle's dupli-object, scaling as needed, and adjust Metaball resolution (lower value = more detail); scroll to the particle system's Molecular panel, activate it, enable Particle Linking (with a tuned search length) so particles stick together, then click Start Molecular Simulation.
14. **Inset/Outset faces:** press I twice to toggle Individual Faces insetting; hold Ctrl while insetting to turn it into an extrude; press O during the operation for an Outset (extra edges created outside the selection instead of inside); press B to toggle whether the selection boundary is also inset; the same options are available from the Face > Inset Faces menu.
15. **Isolating an object in the viewport:** select the object and press Shift+H to hide everything else (Alt+H restores, works in Edit Mode too); alternatively press `/` (forward slash) to locally isolate and zoom to the selection, press `/` again to restore the previous view; for a collection-based approach, right-click the object in the Outliner and choose Visibility > Isolate.

### Nodes / Settings
- **Rigid Body:** Rigid Body Constraint (Type: Generic, Linear/Angular limit checkboxes with lower/upper bounds), Animated checkbox for temporary locking.
- **Armature:** Child Of bone constraint (Set Inverse), bone parent clearing in Edit Mode.
- **Cloth:** Speed Multiplier (slow-motion), Pressure (keyframed, vacuum-pack), Pin Group, Quality Steps, Collision Quality, Self Collisions, Gravity toggle.
- **Shading/Rendering:** Toon/Emission shader for outline material, Backface Culling, Solidify modifier (Flip Normals, Material Index Offset), Normal Map node + Image Texture set to Non-Color, matcap shading, Viewport Render Image.
- **Particles/Scatter:** Scatter Objects add-on (F3 search), 3D Print Toolbox (Intersections/Select Intersect/Delete Faces), Blue Noise Particles add-on (Noise Type Even, Highest quality), particle Physics type Fluid + self-repulsion settings, Force field.
- **Volume:** Volume object import (OpenVDB), Volumetric Shadows, Tile Size, Density, Blackbody Intensity/Temperature, custom grid attribute naming (e.g. temperature).
- **Modeling:** Ctrl+F Wireframe / Wireframe modifier, Inset Faces (I, Ctrl for extrude, O for outset, B for boundary toggle).
- **Viewport:** Shift+H / Alt+H (hide/unhide others), `/` (local view isolate toggle), Outliner right-click > Visibility > Isolate.
- **Add-ons used:** BoolTool-adjacent Rigid Body/Armature tools (native), Scatter Objects (native since 2.8), 3D Print Toolbox (native), Blue Noise Particles (third-party, installed via zip), Molecular (third-party, free, installed via zip).

### Difficulty
Advanced

### Blender Version
2.8 or later — Scatter Objects is explicitly described as "a new default add-on in Blender 2.8," and the video separately notes updating its inverted-hull tip because "the interface of blender 2.[8]0 changed a lot."

### Tags
rigging, animation, cloth, simulation, rendering, particles

---

## Related Tutorials
- [Making a new Logo Animation - Blender Secrets](making-a-new-logo-animation---blender-secrets.md) — shares rigid-body, animation; that video's stunt-cube-launched-through-hatch-doors sequence is a more elaborate application of this compilation's ragdoll Rigid Body Constraint technique.
- [Daily Blender Secrets - 15 Tips Compilation (Part 2)](daily-blender-secrets---15-tips-compilation-part-2.md) — shares simulation, cloth, rigid-body; this video opens mid-sentence continuing Part 2's ragdoll build (Rigid Body Constraints, then Armature parenting) before moving into 13 further standalone tips.
