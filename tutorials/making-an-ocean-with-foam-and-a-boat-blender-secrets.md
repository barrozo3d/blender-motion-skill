---
title: Making an Ocean with Foam and a Boat | Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=qjJ3kSCis4k
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Ocean modifier + node-based foam shading works in both EEVEE and Cycles; consistent with 3.x-5.x"
tags: [displacement, shaders, materials, rigging, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/making-an-ocean-with-foam-and-a-boat-blender-secrets/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Making an Ocean with Foam and a Boat | Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=qjJ3kSCis4k)
**Author:** Blender Secrets
**Duration:** 4m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this video we'll look at how to create an ocean with only modifiers, and how to add a foam material that works in both EEVEE and Cycles.
[0:08] Finally, we'll add a little boat to it.
[0:11] Add a plane.
[0:13] Press S and 10 on the Numpad to scale it up to 200 meters.
[0:18] Right-click and choose Shade Smooth. Press Ctrl A and apply the scale.
[0:24] Subdivide it in Edit Mode with 99 cuts.
[0:30] Then add an Ocean modifier.
[0:34] Set Geometry to Displace and Spatial Size to 20 to match the size of the plane.
[0:41] Set Resolution to 20 or even more.
[0:44] Be careful not to set it too high as Blender might freeze depending on your computer specs.
[0:51] Go to Material View and add a material with a dark color and decrease the roughness to make the waves more shiny.
[1:00] If you drag the time value on the modifier, you'll notice that the ocean moves.
[1:06] The waves scale value controls how high the waves are.
[1:14] Set keyframes for the time value if you wanted to animate the waves.
[1:19] Make sure to set the keyframes to Linear.
[1:24] You can set the resolution of the Ocean modifier low for the viewport and high for the render.
[1:30] Now let's add some foam.
[1:36] For the higher waves to have a lighter color, you need a Color Ramp node.
[1:42] Add a dark blue and light blue color to the Color Ramp and plug it into the base color of the principal to be a TF node.
[1:51] Set the Interpolation mode of the Color Ramp node to Ease for a more gradual color gradient.
[1:59] Then use a separate XYZ node and plug the Z output into the Color Ramp.
[2:06] Now the waves show the light blue color for the peaks and the dark blue color for the valleys.
[2:14] You can experiment with the roughness value to get the right amount of glossiness.
[2:19] In the Ocean modifier, check the Generate Foam box and name the foam data layer Foam.
[2:26] To create the foam, add another principal to be a TF node and set the base color to White.
[2:32] Add an Attribute node and type Foam in the Name field.
[2:36] Plug it into a Math node and set that one to Power.
[2:40] Use the output of the Math node for the mixed shader.
[2:45] Experiment with the Exponent value to get the results you like.
[2:51] Please note that the H2RI that you choose has a lot of influence over how the water looks as it's a very glossy material.
[3:03] Now that we have our ocean, let's add a little boat to it.
[3:08] In Object mode, add a smaller plane and subdivide it a few times.
[3:14] Name this plane ShrinkRap and name the ocean Ocean to avoid confusion.
[3:19] Add a ShrinkRap modifier to the small plane and set the ocean as the target.
[3:24] Select three vertices like this and assign them to a vertex group.
[3:28] Append a little boat to your scene.
[3:31] Give it a Copy Transforms Object Constraint.
[3:34] Use the ShrinkRap plane and its vertex group as its target.
[3:39] Turn off Render visibility of the ShrinkRap plane.
[3:42] To reduce the shakiness, you can experiment with lowering the offset of the ShrinkRap modifier.
[3:48] You can also try lowering the influence value of the Copy Transforms Object Constraint.



---

## Captured Frames

- [0:34] tutorials/frames/making-an-ocean-with-foam-and-a-boat-blender-secrets/frame_000.jpg
- [1:06] tutorials/frames/making-an-ocean-with-foam-and-a-boat-blender-secrets/frame_001.jpg
- [1:42] tutorials/frames/making-an-ocean-with-foam-and-a-boat-blender-secrets/frame_002.jpg
- [2:19] tutorials/frames/making-an-ocean-with-foam-and-a-boat-blender-secrets/frame_003.jpg
- [2:36] tutorials/frames/making-an-ocean-with-foam-and-a-boat-blender-secrets/frame_004.jpg
- [3:34] tutorials/frames/making-an-ocean-with-foam-and-a-boat-blender-secrets/frame_005.jpg

---

## Structured Notes

### Core Technique
A fully modifier- and shader-based ocean (no fluid simulation): the built-in Ocean modifier drives wave displacement, a height-based Color Ramp shader fakes wave-peak/valley coloring, the modifier's Generate Foam data layer drives a separate foam shader mixed in via an Attribute + Power node, and a small boat is floated on top using a Shrinkwrap-plane + Copy Transforms rig.

### Summary
Frame 000 shows the starting setup: a flat, undisplaced plane with the Ocean modifier freshly added, its Geometry set to Generate and default Resolution/Time/Depth/Spatial Size fields visible in the sidebar. Frame 001 shows the modifier reconfigured — Geometry switched to Displace, Resolution Viewport raised to 20, Spatial Size set to 20 — producing a large, richly displaced wave surface viewed from a low grazing angle, dark unlit material applied. Frame 002 shows the shading setup in progress: a ColorRamp node (Linear interpolation, black-to-white) connected toward a Principled BSDF's Base Color, over the same wave surface now lit and showing subtle tonal variation. Frame 003 shows the completed height-based coloring node graph: Texture Coordinate → Mapping (Point) → Separate XYZ (Z output used) → ColorRamp (dark-to-light blue, Ease interpolation) → Base Color, with a Roughness value (0.279) also visible in the Principled BSDF — producing a wave surface with lighter-blue peaks and darker-blue troughs. Frame 004 shows the foam shader piece in isolation: an Attribute node (Type: Geometry, Name: "Foam") feeding a Power node's Base input (Exponent 0.800), highlighted with a red arrow — this Power output goes on to drive a Mix Shader's factor. Frame 005 shows the finished scene: a small sailboat resting convincingly on the wave surface, with the Add Object Constraint menu open and "Copy Transforms" highlighted — the step that locks the boat to the Shrinkwrap-plane's motion.

### Key Steps
**Ocean surface:**
1. Add a Plane, scale it up (S, 10 on the Numpad → 200m), Shade Smooth, Ctrl+A to Apply Scale.
2. In Edit Mode, Subdivide with 99 cuts for enough resolution to displace.
3. Add an Ocean modifier; set Geometry to Displace; set Spatial Size to match the plane's real-world size (20, in this example); set Resolution to 20 or more (raising it further risks freezing Blender depending on hardware).
4. In Material/Rendered view, add a dark, low-Roughness material for shiny, glossy-looking waves as a baseline.
5. Dragging the Ocean modifier's Time value animates the waves; the Waves > Scale value controls wave height. To animate over time, keyframe the Time value and set those keyframes' interpolation to Linear (so wave motion doesn't ease/ramp unnaturally).
6. Set Resolution Viewport low for real-time editing and Resolution Render high for the final output — the modifier supports separate viewport/render resolution values.

**Wave-height color shading (works in both EEVEE and Cycles):**
7. Build a node chain: Texture Coordinate → Mapping → Separate XYZ, using the Z output (world-space height) as the Fac input to a ColorRamp node.
8. Set the ColorRamp's two color stops to a dark blue (low/valleys) and a light blue (high/peaks); set its Interpolation to Ease for a smoother, more gradual color transition than Linear.
9. Plug the ColorRamp's Color output into a Principled BSDF's Base Color — wave peaks now render lighter blue, valleys darker blue. Adjust Roughness to taste for the right glossiness.

**Foam shading:**
10. In the Ocean modifier, enable Generate Foam and name the foam vertex-color/attribute data layer "Foam."
11. Add a second Principled BSDF with Base Color set to White (the foam material).
12. Add an Attribute node, set Type to Geometry and Name to "Foam" (matching the modifier's data layer name exactly).
13. Plug the Attribute's output into a Math node set to Power; adjust the Exponent value to control how much/little of the surface reads as foam.
14. Feed the Power node's output into a Mix Shader's Fac input, mixing between the water shader and the white foam shader.
15. Note: the choice of HDRI has a large visual effect on the final look, since water is an extremely glossy/reflective material.

**Floating a boat on the ocean:**
16. Add a small Plane, subdivide it a few times, and rename it (e.g. "Shrinkwrap") to avoid confusion with the ocean object (renamed "Ocean").
17. Add a Shrinkwrap modifier to this small plane, targeting the Ocean object — it now conforms to the wave surface in real time.
18. Select three vertices on the Shrinkwrap plane (spread out for stability) and assign them to a Vertex Group.
19. Append a boat model into the scene; add a Copy Transforms Object Constraint to it, targeting the Shrinkwrap plane and its vertex group — the boat now inherits the averaged position/orientation of those three wave-following vertices, appearing to float and rock naturally.
20. Disable the Shrinkwrap plane's Render visibility (it's a rig helper, not meant to be seen).
21. If the boat shakes too much, reduce the Shrinkwrap modifier's Offset value, and/or lower the Copy Transforms constraint's Influence value to soften the effect.

### Nodes / Settings
- **Modifiers:** Ocean (Geometry: Displace, Resolution Viewport/Render, Time, Spatial Size, Waves > Scale, Generate Foam + data layer name), Shrinkwrap (Target: Ocean object).
- **Shader nodes:** Texture Coordinate, Mapping, Separate XYZ (Z channel), ColorRamp (Ease interpolation for water color, dark-to-light blue), Principled BSDF ×2 (water + white foam), Attribute node (Type: Geometry, Name matching the Ocean modifier's foam layer), Math node set to Power (Exponent), Mix Shader.
- **Constraints:** Copy Transforms (target: Shrinkwrap plane + Vertex Group, Influence adjustable for stability).
- **Other:** Vertex Group (3 spread-out vertices on the Shrinkwrap plane), keyframed Time value with Linear interpolation for wave animation, HDRI choice (significant visual impact on a glossy water material).

### Difficulty
Intermediate

### Blender Version
Not specified — the Ocean modifier and node-based foam shading are noted to work in both EEVEE and Cycles, consistent with Blender 3.x through 5.x.

### Tags
displacement, shaders, materials, rigging, procedural, intermediate

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover the Ocean modifier or Shrinkwrap-based floating-object rigs.
