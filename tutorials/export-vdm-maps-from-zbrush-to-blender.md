---
title: Export VDM maps from Zbrush to Blender
source: YouTube
url: https://www.youtube.com/watch?v=KACmuXsoc30
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/export-vdm-maps-from-zbrush-to-blender/
frame_count: 0
frame_status: pending-selection
---

# Export VDM maps from Zbrush to Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=KACmuXsoc30)
**Author:** Blender Secrets
**Duration:** 3m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py export-vdm-maps-from-zbrush-to-blender <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] If you're somebody who has VDMs that you used before in ZBrush, and now you want to use them in Blender,
[0:10] or maybe you're somebody who makes VDMs and sells them on ArtStation, for example,
[0:15] then you may want to know how to export them, that you can use them in Blender as well.
[0:20] So it's pretty simple, you just go to Brush, Load Brush, and then you open the VDM ZBrush file.
[0:29] You need to have some primitive object loaded.
[0:36] And so now you can see all these VDMs here, so I can select one, and I can go to Brush, To Mesh.
[0:48] So this is the VDM brush, as a mesh.
[0:51] And now we can go to Texture, From Mesh.
[0:56] And here we have now our VDM Texture, but as you can see, there's a problem with it.
[1:00] There's this red color.
[1:04] And all around the displacement, it actually needs to be black in Blender.
[1:09] So we can go to Deformation here, and if it's red, then you need to mirror the X axis.
[1:17] So X is selected, and click on Mirror.
[1:22] And now we can do the same thing from Mesh.
[1:26] So now we have the correct Texture.
[1:28] If it's blue at the bottom, then you need to mirror it along the Y axis.
[1:33] So we can go to Export, and then Export the VDM, as an OpenEXR of course.
[1:42] There's still one more step we need to do in Photoshop, before we can use the VDM in Blender.
[1:47] So open the VDM in Photoshop.
[1:52] Then go to Image, Adjustments, Channel Mixer.
[1:56] And in the Green channel, set Green to 0, and Blue to 200.
[2:03] And in the Blue channel, set Blue to 0, and Green to 200%.
[2:09] So now we've flipped the Green and the Blue channel, and we've boosted them to 200%.
[2:14] So we can save this.
[2:21] And now in Blender, we can make a copy of the Drop Brush.
[2:27] We can open the Texture here.
[2:29] And then we need to make sure that the Clamp is turned off.
[2:33] And then we just do the usual stuff that we would do with an architecture.
[2:37] We set it to Mapping Area Plane, and of course Enable Vector Displacement.
[2:41] Set Stroke Method to Drag.
[2:44] And Falloff to Constant.
[2:47] And finally set the Strength to 1.
[2:50] And now you have your VDM in Blender.
[3:02] And now we can make a copy of the Vector Displacement.



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
