---
title: Modeling a Devil Fruit from One Piece - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=_-a8k2LaZbA
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/modeling-a-devil-fruit-from-one-piece---blender-secrets/
frame_count: 0
frame_status: pending-selection
---

# Modeling a Devil Fruit from One Piece - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=_-a8k2LaZbA)
**Author:** Blender Secrets
**Duration:** 6m16s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py modeling-a-devil-fruit-from-one-piece---blender-secrets <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Let's make this devil fruit.
[0:02] Start by adding an icosphere.
[0:04] With two subdivisions we have the amount of detail that we need.
[0:07] Add a subdiff modifier.
[0:09] This gives us geometry that helps place these world shapes more evenly,
[0:12] especially when using the cavity option in viewport overlays.
[0:17] You could use a curve, but I find it easier to start with a vertex.
[0:20] Collapse any primitive in edit mode to get one vertex,
[0:23] and then just extrude it to get the shape that you want.
[0:26] After that, you can convert it to a curve.
[0:29] Now that it's a curve, it's easy to give it some thickness by increasing the depth value.
[0:34] Shade Smooth to make it easier on the eyes.
[0:36] You can fine-tune the curve by moving the individual vertices.
[0:39] By pressing Alt S, the thickness around the vertices can be adjusted.
[0:43] To get the curve to end in a spherical shape, we need to convert it back to a mesh.
[0:48] You can do that by pressing Ctrl A and choosing visual geometry to mesh,
[0:52] or by choosing convert to mesh.
[0:56] Add a subdiff modifier to make it all smoother.
[0:59] Enable on-cage on the modifier to see better what you're getting as you fine-tune the shape in edit mode.
[1:04] To get the spherical shape here, we need to fill the gap first.
[1:08] To do that, select the boundary loop and press Ctrl F, and then choose grid fill.
[1:13] Moving the middle face already gives it a more spherical shape.
[1:17] Pressing Ctrl and plus on the numpad grows the selection.
[1:21] Then by pressing E, we extrude the selection, which gives us another loop around the spherical end of this shape,
[1:27] and scale it up by pressing S, or even better Alt S, which scales along the normal directions.
[1:32] Now it's just a matter of fine-tuning the shape to your liking in edit mode.
[1:36] Make sure that the 3D cursor is at world origin, and set the transform orientation to 3D cursor,
[1:42] so you can transform around it as a pivot point.
[1:45] Select all in edit mode by pressing A, then press Shift D, S, X, and type minus 1 on the numpad, and press Enter.
[1:53] In other words, Shift D to duplicate, then scale it to negative 1 on the X axis.
[1:58] This also flips the normals in the wrong direction, so press Shift N to fix that while everything is still selected.
[2:05] Rotate the duplicated part 180 degrees on the X axis by pressing R, X, and 180 on the numpad, and pressing Enter.
[2:13] To make sure it's connected here, select all vertices and press M, then choose Collapse by Distance.
[2:19] Now we can dissolve some edge loops and adjust the shape in edit mode.
[2:23] It's easier to select all the vertices with X-ray mode enabled.
[2:30] We need to rotate the whole object slightly to make it more symmetrical.
[2:34] Don't forget to turn transform orientation back to medium.
[2:38] After some further fine-tuning, we get a nice swirly shape.
[2:42] Finally, give it a name.
[2:43] To make it easy to deform the swirl geometry to fit on the surface of the aquasphere, we'll need some simple geometry to bind it to first.
[2:51] So add a plane and scale it to fit around the swirl in edit mode.
[2:55] Add an edge loop to make the geometry more evenly divided and subdivide it a few times in edit mode.
[3:00] Set the visibility of the plane to wireframe so you can still see it, but also see through it.
[3:06] If you have a sub-diff modifier on the swirl, make sure that the viewport and render levels are the same before the next step.
[3:13] Otherwise, the surface-diff form modifier won't work properly.
[3:17] Now add a surface-diff form modifier to this swirl geometry and pick the plane as the target.
[3:22] Then click on bind.
[3:25] Now, moving the vertices of the plane in edit mode deforms the swirl geometry.
[3:30] This is especially effective with proportional editing.
[3:32] We also want the swirl to follow the plane in object mode, so it's easier to place both on the surface of the aquasphere.
[3:38] To achieve this, select the swirl, hold shift and select the plane.
[3:42] Press Ctrl P and parent the swirl to the plane.
[3:45] Now, moving the plane in object mode makes the swirl follow along.
[3:49] We can move these two to the side and unhide the aquasphere.
[3:52] Duplicate both the swirl and plane in object mode with Shift D.
[3:56] Then move it to the aquasphere.
[3:58] By holding Ctrl, it snaps to the surface, which makes it easier to place it where you want.
[4:03] You'll also need to scale and rotate it to fit.
[4:09] Once it's in a good spot, add a shrink wrap modifier to the plane.
[4:12] Choose the aquasphere as the target.
[4:14] It works best with the project option and both negative and positive options checked.
[4:19] This makes the plane conform to the aquasphere and in turn the swirl follows the shape of the plane.
[4:25] Now it's just a matter of duplicating these objects again and fitting the aquasphere with them.
[4:29] You can save some time by copying the scale of this plane to the original plane,
[4:33] so that you don't have to scale it down every time you duplicate it.
[4:39] And instead of adding the shrink wrap modifier manually each time,
[4:43] you can select the plane you're currently placing, hold shift and select a previously placed plane.
[4:48] Then press Ctrl L and choose modifiers to copy the shrink wrap modifier, including the correct settings.
[4:53] After repeating these steps, the aquasphere is full of swirls.
[4:57] If you render this and these swirls don't follow the curvature of the sphere in the render,
[5:01] that's because you need to have the same level of subdivisions for both viewport and render.
[5:06] So make sure those are all the same.
[5:08] Now let's make the stem.
[5:10] Hold shift and right click here to put the 3D cursor there.
[5:13] Then add a single vertex or add any primitive and collapse it to a single vertex.
[5:17] Extrude it in edit mode to make the shape of the stem.
[5:20] Separate the horizontal and vertical parts by deleting an edge.
[5:24] Then separate them by selecting all and pressing P, then choose separate by loose parts.
[5:29] Convert it to a curve and then add some thickness to it.
[5:32] You can scale the vertices with all S just like we did with the swirl.
[5:36] The very end can be scaled to zero, so it ends in a sharp point.
[5:40] Convert the vertical parts to a curve and give it thickness as well.
[5:43] To make sure there's no hole here, check the fill caps option.
[5:47] Then convert it back to a mesh.
[5:49] You can turn these triangles to quads by selecting them in face selection mode and pressing Alt J.
[5:54] If it doesn't work for all of them, select two triangles and press F to turn them into a quad.
[5:59] We can inset this selection and add in edge loop to protect this corner from the subdiff modifier.
[6:05] And that's it, we've modeled the devil fruit.
[6:08] On my Patreon you can find the longer version of this video as well as the blend file.
[6:12] Thank you for watching until the end.



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
