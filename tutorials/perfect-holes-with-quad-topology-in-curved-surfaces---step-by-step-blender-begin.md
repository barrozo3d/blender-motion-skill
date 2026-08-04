---
title: Perfect Holes with Quad Topology in Curved Surfaces - Step by step Blender beginner version
source: YouTube
url: https://www.youtube.com/watch?v=bfdI_-ymkas
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/perfect-holes-with-quad-topology-in-curved-surfaces---step-by-step-blender-begin/
frame_count: 0
frame_status: pending-selection
---

# Perfect Holes with Quad Topology in Curved Surfaces - Step by step Blender beginner version

**Source:** [YouTube](https://www.youtube.com/watch?v=bfdI_-ymkas)
**Author:** Blender Secrets
**Duration:** 4m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py perfect-holes-with-quad-topology-in-curved-surfaces---step-by-step-blender-begin <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] This method of making holes is useful when you want to make a perfectly circular hole in a curved surface.
[0:08] Press Shift A and add a cylinder.
[0:11] As cap fill type we choose nothing.
[0:16] I'm just going to move this up on the Z-axis by pressing G, Z and 1 on the numpad and then pressing Enter.
[0:24] In Edit Mode I'll add some horizontal edge loops by pressing Ctrl R and scrolling the mouse wheel up.
[0:31] Left click to confirm, then right click to cancel the transformation.
[0:36] In Object Mode add a couple of levels of subdivision by pressing Ctrl 2 just to make it smoother.
[0:43] And right click and choose Shade Smooth.
[0:47] Press Shift D to duplicate the cylinder and right click to cancel the transformation so that it's exactly in the same location as the original.
[0:56] We can disable the viewport visibility of the duplicate.
[1:02] In Edit Mode select a square of faces.
[1:06] Right click and choose Loop Tools, Circle to make the selection circular.
[1:11] I'll disable the Subdiv modifier temporarily so that you can see better what I'm doing next.
[1:19] Inset the selection with I to create a loop of faces around the hole.
[1:23] This helps to protect the boundary when it's subdivided later.
[1:27] Extrude Inwards for another loop of faces for boundary protection.
[1:31] Then extrude again to create some depth.
[1:33] Then extrude and insert a little bit again for some more boundary protection face loops.
[1:38] Now if we turn the Subdiv modifier back on we can see what that gets us.
[1:44] We can see the surface better by using a Matte Cap, especially one that shows imperfections.
[1:51] You can see that the area around the hole is quite lumpy.
[1:55] There are some Matte Caps that are specifically designed to spot lumpy surfaces like this.
[1:59] Ideally those lines should be straight, like at the back of the hole.
[2:03] I'll show you how to fix this.
[2:05] First increase the selection in Edit Mode by pressing Ctrl and plus on the numpad.
[2:11] Create a new vertex group.
[2:14] And click on Remove to give the selection a weight of 0.
[2:18] Press Ctrl I to invert the selection and click on Assign to give that selection a weight of 1.
[2:24] In Weight Pane Mode we can see these values are very similar to the ones in the previous video.
[2:30] In Weight Pane Mode we can see these values as colors.
[2:34] Everything that's red has a value of 1 and the blue part has a value of 0.
[2:42] I'll go back to Edit Mode by pressing Tab and I'll turn the Subdiv modifier on again.
[2:49] Let's use a shiny Matte Cap so we can inspect the surface better.
[2:54] Add a Shrinkwrap modifier to the cylinder.
[2:58] And as the target, pick the duplicate of the cylinder.
[3:02] This destroys the hole so we need to exclude it from the modifier by using the vertex group.
[3:08] Now we have a perfect hole.
[3:10] You can see the difference the Shrinkwrap modifier makes when I turn the modifier off.
[3:18] This Matte Cap makes it even more obvious.
[3:22] Now what happens if we try to apply the Shrinkwrap modifier?
[3:27] Unfortunately that brings back the lumpiness of the surface so let's undo that with Ctrl Z.
[3:33] Instead press Ctrl A and choose Visual Geometry to Mesh to apply all the modifiers at once.
[3:39] Now we keep the perfect surface.
[3:41] However, it also means that we have a lot of subdivided geometry which may not be what we want.
[3:47] We can solve this by adding a Decimate modifier.
[3:51] Set it to Unsubdivide and use an even number of iterations.
[3:55] First let's try a value of 2.
[3:58] Apply the modifier.
[4:01] In Edit Mode you can see that the geometry is less dense and we still keep the smooth surface.
[4:08] We can add a subdivid modifier to it to make it more smooth.
[4:16] Let's see if we can unsubdivide it one more time to make the geometry even simpler.
[4:21] Again use an even number and then apply the modifier.
[4:26] As you can see when I add a subdivid modifier back on it with two levels we keep the perfectly smooth surface.
[4:32] But with a lower resolution geometry.
[4:36] How high or low the resolution needs to be depends on your use case.
[4:41] For example a game might be low poly with normal maps for detail,
[4:45] but on the other hand a movie asset may be sculpted on so it can be very high poly.



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
