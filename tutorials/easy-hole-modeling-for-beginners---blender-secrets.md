---
title: Easy hole modeling for beginners - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=jrR1T-dIA8c
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/easy-hole-modeling-for-beginners---blender-secrets/
frame_count: 0
frame_status: pending-selection
---

# Easy hole modeling for beginners - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=jrR1T-dIA8c)
**Author:** Blender Secrets
**Duration:** 3m32s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py easy-hole-modeling-for-beginners---blender-secrets <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] An easy way to add a circular hole is by beveling a vertex.
[0:03] You can do this by selecting a vertex and pressing Shift Ctrl B.
[0:07] Then scroll the mouse wheel up to add more segments.
[0:11] You can also increase or decrease the segments with the plus and minus keys on the numpad.
[0:16] Or, after left clicking to confirm, increase the segments in the operator panel.
[0:22] To make it round, adjust the profile shape to 0.0865.
[0:28] Or, even easier, right click and use Loop Tools, Circle for a perfect circle.
[0:33] Loop Tools is an extension that you need to enable in preferences.
[0:36] Then you can extrude these faces inwards.
[0:39] You can even do this with several vertices at once.
[0:43] And then press Alt E and choose Extrude Faces along normals.
[0:47] This works fine in a quick boolean workflow, but it creates endgones.
[0:51] Faces with more than four edges.
[0:53] Although in some cases endgones are fine even in a sub-diff workflow,
[0:57] if you're going for an old Kuat workflow, for scoping for example, you'll want to avoid endgones.
[1:02] In that case, you'll need at least three intersecting edge loops.
[1:06] In Edge Selection Mode, select two intersecting edges and press Ctrl B to bevel them.
[1:12] Here too, you can increase segments with the middle mouse button,
[1:15] or by pressing the plus key on the numpad.
[1:17] Or, after left clicking to confirm, by adjusting the segments in the operator panel.
[1:23] You need two segments to get three intersecting edges like this.
[1:27] Switch back to Vertex Selection Mode and bevel the vertex in the center as before with Shift
[1:32] Ctrl B. You can also do this by going to Vertex Bevel Vertices and move the mouse until you see
[1:39] it change. Adjust the profile in the operator panel or use Loop Tools Circle.
[1:44] Now to get all Kuat topology, select two vertices at a time while holding Shift,
[1:49] and then press J to connect them. Switch to Face Selection Mode and select the faces.
[1:55] Press E to extrude them to create a hole. If you don't want to keep those extruded faces,
[2:00] press Delete or X and choose Faces. Now when you add a sub-diff modifier,
[2:06] it will become more round but also smooth. To keep the corners sharp, you can do a couple of things.
[2:12] You can select the corner edges and increase them by pressing Shift E and 1 on the numpad.
[2:18] Or slide the mean crease value to the right in the option panel with those edges selected.
[2:24] Now despite the sub-diff modifier, the corner remains sharp.
[2:28] Alternatively, we can do some more beveling. With those edges selected, press Ctrl B and
[2:33] then move the mouse. You want a profile shape of one for this and two segments is enough to
[2:38] keep the corners sharp. The closer together those edge loops are, the sharper the corner will be.
[2:43] When exporting a mesh to other software, you want to add geometry like this to keep corners sharp,
[2:49] because creasing only works inside of Blender. Right-click and choose Shade Auto Smooth to
[2:54] make it look even smoother. Blender 5 has really nice matte caps that you can use to make your
[2:59] models more visually appealing in the viewport. Learning how to make holes, either with Booleans
[3:04] or with Subdivision Ready Topology, is one of the key skills that you need to have as a 3D artist.
[3:09] I've learned this the hard way, but I've struggled so you don't have to.
[3:13] I've connected all my knowledge about hole modeling in a new PDF, The Big Book of Holes.
[3:18] You can get this now on my website or on YouTube. If you already have my Big Blender
[3:22] Sequence book, you don't need this PDF as you already have all these topics in that book.
[3:26] So if you want to learn all there is about holes in 3D modeling, go and get that PDF.



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
