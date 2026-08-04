---
title: Blender Secrets - Every Circular Array or Radial Array method
source: YouTube
url: https://www.youtube.com/watch?v=Q6nq1HEA5Y8
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-secrets---every-circular-array-or-radial-array-method/
frame_count: 0
frame_status: pending-selection
---

# Blender Secrets - Every Circular Array or Radial Array method

**Source:** [YouTube](https://www.youtube.com/watch?v=Q6nq1HEA5Y8)
**Author:** Blender Secrets
**Duration:** 5m46s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-secrets---every-circular-array-or-radial-array-method <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Circular Arary using Spin [0:00]
**Transcript (timestamped):**
[0:00] Place the 3D cursor where you want the center of your circular array to be.
[0:10] In edit mode, select the whole mesh by pressing A. Then press Alt E and S to create the array.
[0:17] You can then use the menu to change the amount of duplicates in your array.


### Circular Array using Duplicate [0:25]
**Transcript (timestamped):**
[0:26] Make sure that the pivot point is set to 3D Cursor.
[0:30] The 3D cursor and the object that you want to create an array of should not overlap.
[0:36] Press Shift D. Then immediately follow that up by pressing R and 30 on the numpad.
[0:41] Then press Enter.
[0:43] Press Shift R to repeat that action as many times as needed to complete the array.
[0:48] The rotation is dependent on the view.
[0:52] So make sure you're in, for example, Front Autographic View for best results.
[0:57] In this example, I rotated 30 degrees to get 12 instances.
[1:02] In other words, 360 degrees divided by 12.
[1:08] If you know exactly how many duplicates you want in an array, this is an easy and fast


### Circular Array using Instancing [1:09]
**Transcript (timestamped):**
[1:13] method.
[1:14] First, create the object you want to have in an array.
[1:17] Then create a mesh circle, not a curve.
[1:20] Then set it to have the amount of vertices that you want the array to have.
[1:23] 12, for example.
[1:25] Scale the circle to the size that you want the array to have.
[1:28] Now parent the object to the circle with Ctrl P and choose parent with vertex.
[1:34] Select the circle and under Instancing, turn on vertex.
[1:37] You can choose whether to align the objects to the circle or not and if you want to have
[1:41] the original object, show up in Renders or not.
[1:45] Now you can still manipulate the circle.
[1:49] If you don't align the objects to the circle, you can create some interesting animation
[1:53] like this.


### Circular Array using Screw modifier [1:57]
**Transcript (timestamped):**
[2:02] Select the default cube and go into Edit Mode by pressing Tab.
[2:06] Press M, then choose to Center.
[2:08] Now you have one vertex.
[2:10] While still in Edit Mode, make sure the vertex is selected by pressing A, then move it away
[2:15] from its origin.
[2:17] In Object Mode, add a screw modifier to it.
[2:23] Now select the object that you want to have in an array and hold Shift and select the
[2:27] vertex.
[2:29] Then press Ctrl P to parent to vertex.
[2:33] It might be easier to select these things in the Outliner than in the Viewport.


### Circular Array using Curve [2:53]
**Transcript (timestamped):**
[2:59] Scale a cube on the X-axis.
[3:02] Create a Bezier circle.
[3:06] Add a Bevel modifier, an Array modifier and a Curve modifier to the cube.
[3:12] Choose the Bezier circle as the object in the Curve modifier.
[3:16] Increase the Array count until the cubes go all the way around the circle.
[3:19] You may need to scale the cube slightly.
[3:24] Add another Array modifier to increase the height.
[3:29] Please note that the modifier order is important.
[3:35] If you want to have it taper towards the top, you can twist the curve with Ctrl T with all
[3:39] its vertices selected in Edit Mode.
[3:47] You can offset the cubes by turning on Constant Offset in the second Array modifier and increasing
[3:52] the X value.
[3:54] If you want the stones to follow the curve more smoothly, in Edit Mode add more edge loops
[3:59] by pressing Ctrl R and scrolling the mouse wheel up.
[4:05] You may want to turn on Smooth Shading and Auto Smooth at this point.
[4:13] You can also subdivide the Bezier circle for a smoother result.


### Circular Array using Empty [4:24]
**Transcript (timestamped):**
[4:35] Add a Displace modifier to your object and set the direction to X.
[4:40] Please mid-level to 0 and increase the strength.
[4:43] Now you can non-destructively move the object away from its origin.
[4:48] Next add an Array modifier.
[4:50] Enable Object Offset instead of Relative Offset.
[4:54] Add an empty and use it as the Offset object.
[4:57] In the Array modifier, increase the count to the amount of instances that you want.
[5:02] Select the empty in the Outliner.
[5:04] Press R and Z to rotate along the Z axis and eyeball the rotation until it looks okay.
[5:10] You can see the rotation value in the top left corner.
[5:13] Round that number off and type it on the numpad followed by Enter.
[5:24] If you found this topic interesting and would like to know more, don't forget that you can
[5:28] find it in my Blender Secrets ebook, along with almost 2000 pages of other tips.
[5:34] To get an idea of what the ebook is like, you can download the free sample from my website.



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
