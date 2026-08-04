---
title: Making an Ocean with Foam and a Boat | Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=qjJ3kSCis4k
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/making-an-ocean-with-foam-and-a-boat-blender-secrets/
frame_count: 0
frame_status: pending-selection
---

# Making an Ocean with Foam and a Boat | Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=qjJ3kSCis4k)
**Author:** Blender Secrets
**Duration:** 4m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py making-an-ocean-with-foam-and-a-boat-blender-secrets <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Blender Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
