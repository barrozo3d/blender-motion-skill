---
title: Blender Secrets - 5 minutes of Topology Tips
source: YouTube
url: https://www.youtube.com/watch?v=V7Y-Il-7JFE
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-secrets---5-minutes-of-topology-tips/
frame_count: 0
frame_status: pending-selection
---

# Blender Secrets - 5 minutes of Topology Tips

**Source:** [YouTube](https://www.youtube.com/watch?v=V7Y-Il-7JFE)
**Author:** Blender Secrets
**Duration:** 5m16s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-secrets---5-minutes-of-topology-tips <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Rotate edges [0:00]
**Transcript (timestamped):**
[0:00] When low poly models are made of triangles, every edge makes a difference.
[0:05] Here you can see one edge which is causing problematic shading.
[0:09] We can solve this by rotating it in the Edge menu, per passing CTRL E and choosing Rotate Edge.
[0:16] You can choose clockwise or counterclockwise, either is fine.
[0:20] That looks much better.


### Extrude edges [0:23]
**Transcript (timestamped):**
[0:30] To go from 4 to 2 quads, select and extrude these two edges. Extrude again.
[0:35] Select the vertices at the corners and scale them away from each other.
[0:39] Select these edges and fill them by pressing F.
[0:44] Extrude these two edges and you're done.
[0:48] To go from 5 to 3 quads, select the middle edge and extrude it.
[0:54] Select the other edges and extrude them further than the middle one.
[0:58] Then select and merge these vertices by pressing M.
[1:04] Fill the gap by selecting these edges and pressing F.
[1:07] Then select and extrude the three edges.
[1:10] For better distribution of geometry, you can scale this middle face down.
[1:15] To go from 3 quads to a single one, select these two edges and extrude them.
[1:20] Extrude the middle edge as well, but only halfway the other two.
[1:24] Merge these vertices by selecting them and pressing M.
[1:28] Then fill the gap by selecting the edges and pressing F.
[1:32] Finally, extrude the one edge out by pressing E.
[1:39] Normally, you can add an edge loop with Ctrl R, but that doesn't work on triangles.
[1:44] Here's how you can still do it.
[1:46] Make sure you're in edge selection mode in edit mode.
[1:50] Select the bottom edge loop by holding Alt and left clicking on it.
[1:54] Invert the selection by pressing Ctrl I.
[1:57] Right click and choose subdivide.
[2:00] Now, hold Alt and left click on the new edge loop to select it.
[2:03] Then press G twice to slide it to where you need it.


### Conform edges [2:10]
**Transcript (timestamped):**
[2:14] In case you have an edge loop that you need to make perfectly straight,
[2:18] you can press G twice and then press E.
[2:21] Pressing E confirms the edge loop to its neighboring edge loop.
[2:25] So it only works if there is a perfectly straight edge loop next to it.
[2:29] Press F to toggle which edge loop to conform the shape to.
[2:33] If you want to make sure to place the edge loop in the middle,
[2:35] hold down Ctrl to move it in increments.
[2:41] You can also use the loop tools add-on.
[2:44] Select the edges and right click, choose loop tools and then flatten.
[2:51] If you only want to straighten out the edges on one side of the model
[2:54] or a limited amount of edges instead of the entire loop,
[2:57] use the G stretch option instead.
[3:00] Finally, you can scale the edges to zero.
[3:03] In this case, we scale along the Z axis.
[3:06] Press S, Z and then zero on the numpad.


### Flatten [3:09]
**Transcript (timestamped):**
[3:15] Select the faces that you want to flatten.
[3:18] Go to Select Similar, choose Coplanar, then increase the threshold if necessary.
[3:24] Right click, select loop tools and choose Flatten.
[3:27] The good thing about this method is that it works no matter the angle of the faces.
[3:33] Another way is to scale things to zero.
[3:36] In other words, select the faces, press S and Z for the Z axis and then zero on the numpad.
[3:41] This works best if the faces are aligned perpendicular to the exact axis you are skating to.
[3:46] For a third method, delete the selected faces.
[3:50] Select the edges surrounding the resulting hole and fill the hole by pressing Ctrl F and then choosing Great Fill.
[3:56] If your model has some areas that need to be more smooth, there are three ways to do it.


### Smooth [3:59]
**Transcript (timestamped):**
[4:02] You can select those vertices, right click and then choose Smooth Vertices.
[4:07] Then hit Shift R a few times to repeat the last action until it looks smooth enough.
[4:12] Another option is to go over to Sculpt Mode, be sure to turn off Symmetry and Sculpt on the model while you are skating.
[4:18] And Sculpt on the model while holding down Shift.
[4:21] This makes the surface smooth as well, but it works best when you have more subdivisions on your model or within Topo Enabled.
[4:28] It can also take some practice to get perfect.
[4:36] You can also add the non-smooth vertices to a vertex group.
[4:42] And then use that vertex group in a smooth or depletion smooth modifier.
[4:48] If you found this topic interesting and would like to know more,
[4:52] don't forget that you can find it in my Blender Secrets ebook.
[4:56] Along with almost 2000 pages of other tips.
[4:59] To get an idea of what the ebook is like, you can download the free sample from my website.



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
