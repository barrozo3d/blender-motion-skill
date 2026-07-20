---
title: Hair Grooming in Blender ft. New Hair System (Hair Curves)
source: YouTube
url: https://www.youtube.com/watch?v=pQcYoH4H1MM
author: adiidiin
ingested: 2026-07-19
blender_version: "Not specified (hair-curves system, 3.5+ node-group assets)"
tags: [organic, geometry-nodes, materials, shaders, animation, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/hair-grooming-in-blender-ft-new-hair-system-hair-curves/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Hair Grooming in Blender ft. New Hair System (Hair Curves)

**Source:** [YouTube](https://www.youtube.com/watch?v=pQcYoH4H1MM)
**Author:** adiidiin
**Duration:** 6m10s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, today I'll be showing you how I made this hair in Blender using the new Hair Curve system.
[0:09] I start by creating a base mesh where I want the hair to grow, but if your character is already retapologized, you can just simply extract the mesh from there.
[0:22] Since I'll be using weight paint to control the hair density, I make sure this mesh has enough resolution that I can paint on.
[0:32] Once the mesh is ready, I scale it down a bit. This helps me hide it slightly and prevents the hair strands from floating.
[0:41] Before adding any hair, it's important to unwrap the mesh.
[0:45] Hair systems rely on UVs for things like interpolation, so I just quickly do a basic unwrap.
[0:53] Next, with the mesh selected, I shift A and add an empty hair.
[0:59] I go to sculpt mode, turn on symmetry, and start adding hair curves.
[1:05] From here, I slowly build up the modifiers.
[1:09] I begin with a set hair curve profile to adjust the radius.
[1:14] I turn on render preview to see how thick the hair looks.
[1:21] From there, I stack several modifiers. I like adding a bit of variation and character to the hair shape.
[1:29] I suggest experimenting with different modifiers that will suit your character.
[1:36] Once I'm happy with the basic shape, I start styling the hair using the comb, grow, or shrink brushes.
[1:46] I tick all the options on the interpolate so new curves use the average length, radius, shape, and point count of the nearby strands.
[1:57] This will keep everything looking consistent.
[2:01] As I add more curves, I continue styling them using the same brushes.
[2:09] To increase overall density, I add the interpolate hair curves modifier after the duplicate hair curves.
[2:17] I select the mesh as a surface, then increase the density value.
[2:22] As you can see, it starts covering the entire mesh, so now it's time for weight painting.
[2:35] First, I create a new vertex group and rename it appropriately since I'll be adding more for a different area later.
[2:44] With the weight paint of 1, I paint only the areas where I want the hair to grow.
[2:51] I just copy the vertex group name and paste it into the density mask field.
[2:58] Now I go back to more styling and disable symmetry to make it look more natural.
[3:07] To create the hair on the sides, I follow the same process.
[3:12] Add hair curves, comb and trim for styling.
[3:18] I just copy the modifiers from the top hair setup, we'll still adjust the settings later.
[3:25] Create a new vertex group, weight paint the side area, paste the new group name into the density mask.
[3:38] Add more hair curves to fill the space.
[3:46] For the material, I use the principled hair BSDF.
[3:52] I add a curves info node, then connect the intercept output to the factor input of a color ramp.
[4:00] By doing this, you can control the gradient along the curve.
[4:07] To add color variation, I connect the random output to another color ramp, then blend using a mixed node and set this to add.
[4:18] This is great if your character has random white hairs.
[4:22] In my case, the character only has dark hair so I just change the color accordingly.
[4:30] Now for the eyebrows and eyelashes, this was inspired by Nazard's videos which I'll link below.
[4:38] But this is done using the new hair system where you can play with the modifiers.
[4:44] The process is very similar to the head hair, but the eyebrow modifiers are much simpler.
[4:50] You can add more if needed, but this setup is already enough for my character.
[4:56] I'm just like before, I use weight paint for the density mask.
[5:01] This whole setup makes it super easy to reuse the eyebrows on another character and tweak things later.
[5:12] Then I duplicate the eyebrow, mirror it to the other side and use a shrink wrap to attach it to the head.
[5:21] I can also scale or reposition it as needed.
[5:28] For the eyelashes, instead of interpolate hair curbs, I just use the duplicate hair curbs since I won't be needing that much density.
[5:40] But I still have a mesh for the eyelashes.
[5:43] This helps me attach the eyelashes to the surface and not be all over the place.
[5:49] I do it by adding an attached hair curbs to surface modifier and select the mesh as the surface.
[5:59] Then I duplicate and mirror it to the other side.
[6:05] That's all, thank you for watching, happy blending!



---

## Captured Frames

- [0:55] tutorials/frames/hair-grooming-in-blender-ft-new-hair-system-hair-curves/frame_000.jpg
- [1:15] tutorials/frames/hair-grooming-in-blender-ft-new-hair-system-hair-curves/frame_001.jpg
- [1:50] tutorials/frames/hair-grooming-in-blender-ft-new-hair-system-hair-curves/frame_002.jpg
- [2:25] tutorials/frames/hair-grooming-in-blender-ft-new-hair-system-hair-curves/frame_003.jpg
- [2:55] tutorials/frames/hair-grooming-in-blender-ft-new-hair-system-hair-curves/frame_004.jpg
- [3:50] tutorials/frames/hair-grooming-in-blender-ft-new-hair-system-hair-curves/frame_005.jpg
- [4:25] tutorials/frames/hair-grooming-in-blender-ft-new-hair-system-hair-curves/frame_006.jpg
- [5:50] tutorials/frames/hair-grooming-in-blender-ft-new-hair-system-hair-curves/frame_007.jpg

---

## Structured Notes

### Core Technique
Full character hair grooming with Blender's Hair Curves system: Sculpt Mode combing on an Empty Hair object, driven by a stacked hair-curve modifier chain and weight-painted density masks per region (scalp, sides, brows, lashes).

### Summary
Full hair/eyebrow/eyelash workflow with the hair-curves system: an inward-scaled, UV-unwrapped scalp mesh gets an Empty Hair object, groomed in Sculpt Mode (symmetry on) with stacked modifiers — Set Hair Curve Profile → Duplicate Hair Curves → Clump Hair Curves → Curl Hair Curves → Trim Hair Curves → Interpolate Hair Curves. Weight-painted vertex groups are pasted into each modifier's Density Mask field per hair region, the material uses a Principled Hair BSDF fed by Curves Info (Intercept → Color Ramp for root-to-tip gradient, Random → second Color Ramp mixed in via Add for color variation), and eyebrows/eyelashes reuse a simplified version of the same rig (mirrored + Shrink Wrap for brows, Attach Hair Curves to Surface instead of Interpolate for the lower-density lashes).

### Key Steps
1. Model or extract a base scalp mesh where hair should grow (retopologized characters can reuse existing topology); keep enough resolution to weight-paint on, then scale it slightly inward so it hides under the hair and strands don't float.
2. Unwrap the scalp mesh (hair systems need UVs for interpolation), select it, press Shift+A > Curve > Empty Hair to create the hair object (frame_000 confirms the Shift+A > Curve submenu with Empty Hair listed).
3. Enter Sculpt Mode, enable symmetry, and comb in the first hair curves by hand.
4. Build the modifier stack in order: Set Hair Curve Profile (Replace Radius, Radius ~0.015 m, Shape 0, Factor Min/Max 0/1 — confirmed in frame_001) with Render Preview enabled to check thickness, then stack Duplicate Hair Curves, Clump Hair Curves, Curl Hair Curves, and Trim Hair Curves for shape/character (frame_002 and frame_007 show this exact stack order).
5. Style with the Comb, Grow, and Shrink brushes; enable all the Interpolate options (average length, radius, shape, point count) so new curves match neighboring strands and stay consistent.
6. Add an Interpolate Hair Curves modifier after Duplicate Hair Curves, set Surface to the scalp mesh's UV map, and raise Density until the mesh is fully covered (frame_003 shows the modifier stack: Set Hair Curve Profile → Duplicate Hair Curves → Interpolate Hair Curves, with Surface/Surface UV Map, Density, Density Mask, Mask Texture, Viewport Percentage fields).
7. Weight-paint a new vertex group over just the area that region's hair should grow (weight 1 for full growth), rename it per region, then paste that vertex group name into the modifier's Density Mask field so hair only grows where painted (frame_004 shows the orange weight-painted density mask under the groomed hair).
8. Repeat the same mesh > groom > modifier-stack > weight-paint > Density Mask process for the side hair (with symmetry disabled for a more natural asymmetric look) and for the eyebrows (frame_005 shows the eyebrow density-mask region highlighted in orange on the forehead).
9. Shade with Principled Hair BSDF: add a Curves Info node, connect its Intercept output to a Color Ramp's Factor (root-to-tip color gradient), and connect Random to a second Color Ramp mixed in through a Mix (Add) node for per-strand color variation — useful for stray white hairs, though this character stays solid dark hair (frame_006 shows the node graph with a Color Ramp and color-picker open).
10. For eyebrows: duplicate the finished brow, mirror to the other side, and use Shrink Wrap to conform it to the head surface, then reposition/rescale as needed. For eyelashes: use only Duplicate Hair Curves (skip Interpolate, since density needs to stay low), keep a dedicated eyelash mesh, and add an Attach Hair Curves to Surface modifier targeting that mesh so lashes hug the eyelid instead of floating (frame_007 confirms the Set Hair Curve Profile → Duplicate Hair Curves → Clump Hair Curves → Trim Hair Curves → Attach Hair Curves to Surface stack), then duplicate and mirror to the other eye.

### Nodes / Settings
- Object: Empty Hair (Shift+A > Curve > Empty Hair), groomed in Sculpt Mode with Symmetry
- Modifier stack (scalp/side hair): Surface Deform (x2) → Set Hair Curve Profile (Replace Radius, Radius 0.015 m, Shape 0.0, Factor Min 0.0 / Max 1.0) → Duplicate Hair Curves → Clump Hair Curves → Curl Hair Curves → Trim Hair Curves → Interpolate Hair Curves (Surface = scalp mesh, Surface UV Map = UVMap, Follow Surface UV Islands, Density, Density Mask = pasted vertex-group name, Mask Texture, Viewport Percentage)
- Modifier stack (eyelashes): Set Hair Curve Profile → Duplicate Hair Curves → Clump Hair Curves → Trim Hair Curves → Attach Hair Curves to Surface (no Interpolate — lower density)
- Sculpt brushes: Comb, Grow/Shrink; Interpolate options (length, radius, shape, point count) all enabled
- Density control: per-region vertex groups painted in Weight Paint mode, pasted into each Interpolate Hair Curves modifier's Density Mask field
- Material: Principled Hair BSDF + Curves Info node — Intercept → Color Ramp (root/tip gradient), Random → Color Ramp → Mix (Add) for color variation
- Eyebrow finishing: duplicate, mirror, Shrink Wrap modifier to conform to head surface
- Eyelash finishing: dedicated eyelash mesh + Attach Hair Curves to Surface modifier

### Difficulty
Intermediate (relies on sculpt-mode grooming, weight painting, and stacking several hair-curve modifiers correctly, though each individual step is approachable for a beginner)

### Blender Version
Not specified (uses the Hair Curves system, which needs Blender 3.5+ for the node-group-based hair modifiers shown)

### Tags
organic, geometry-nodes, materials, shaders, animation, beginner, intermediate

---

## Related Tutorials
- [Easy Rigging Using RIGIFY in Blender](easy-rigging-using-rigify-in-blender.md) — shares animation, beginner, intermediate
- [How to Quickly Create Clothing using Blender and Marvelous Designer](how-to-quickly-create-clothing-using-blender-and-marvelous-designer.md) — shares organic, animation, intermediate
- [Create a Walk Cycle animation in Blender](create-a-walk-cycle-animation-in-blender.md) — shares organic, animation, beginner, intermediate
