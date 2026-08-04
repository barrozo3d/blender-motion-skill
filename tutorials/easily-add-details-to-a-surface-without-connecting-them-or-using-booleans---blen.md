---
title: Easily Add Details to a Surface without Connecting them or using Booleans - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=juXPyDLTJTE
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/easily-add-details-to-a-surface-without-connecting-them-or-using-booleans---blen/
frame_count: 0
frame_status: pending-selection
---

# Easily Add Details to a Surface without Connecting them or using Booleans - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=juXPyDLTJTE)
**Author:** Blender Secrets
**Duration:** 2m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py easily-add-details-to-a-surface-without-connecting-them-or-using-booleans---blen <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Let's look at how to non-destructively add details to the surface of another object
[0:04] without using booleans.
[0:06] First turn on snapping with these options, face project and align rotation to target.
[0:11] Make sure the origin of the detail object is at its bottom or even a bit lower.
[0:16] If that's not the case, select the bottom vertices, Shift S and set cursor to selection
[0:21] in add mode, then go to object mode and go to object, set origin to 3D cursor.
[0:26] Now the mesh snaps to the surface of the other mesh.
[0:29] To fix this gap between both objects, first turn off snapping.
[0:34] Press E to extrude the bottom vertices and then right click to cancel the transformation.
[0:38] Press S to scale the new extruded vertices.
[0:41] Add some more loops by pressing Ctrl R and scrolling up the mouse wheel.
[0:45] Create a new vertex group and add a shrinkwrap modifier to the detail object and then pick
[0:50] the surface as the target.
[0:53] Add the vertex group to the modifier so the object doesn't get flattened.
[0:57] In weight paint mode you can use the gradient tool to add a gradient of values to the vertex
[1:01] group.
[1:02] Or you can do it manually, Ctrl left mouse button click to select the bottom loop of
[1:06] vertices and assign them to the vertex group with a weight of 1.
[1:10] Do the same for the other loops but with decreasing weight values.
[1:13] Either way, make sure the bottom loop of vertices has a weight of 1.
[1:18] Let's use a shiny matte cap and turn off random colors.
[1:22] Turn off outline in viewport shading as well.
[1:25] To better inspect the result.
[1:27] If it doesn't look good, make sure both objects have enough subdivisions.
[1:31] And make sure the shrinkwrap modifier is after the subdivf modifier.
[1:35] By holding down Ctrl you temporarily re-enable snapping so that you can adjust the placement
[1:40] of the detail.
[1:41] As you can see there are still some shading differences.
[1:44] To make it perfect add a data transfer modifier to the small object.
[1:48] As the source, pick the object that it's snapping to and for the vertex group use the
[1:53] same one as in the shrinkwrap modifier.
[1:55] Then enable face corner data and custom normals and set mapping to nearest face interpolated.
[2:02] There's currently a discount on my hard service modeling course so if you want to learn more
[2:06] hard service modeling techniques check out that sale.
[2:09] It's over 20 hours of step by step narrated and subtitled video about making this spider
[2:14] mac.
[2:15] So you can follow along with support from me as your teacher.
[2:18] So far it contains a chapter about modeling with modifiers, a chapter about retopology,
[2:24] about UV unwrapping and currently I'm adding new lessons about making materials and textures.
[2:29] If you missed this short sale that ends on Monday, you can always have an even bigger
[2:33] discount by getting the complete hard service bundle.
[2:37] The bundle also contains the updating course.
[2:39] So check all that out on 3dsecrets.com or blendersecrets.org.



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
