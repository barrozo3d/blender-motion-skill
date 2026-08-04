---
title: Blender Secrets - Hard Surface Sculpting Tips Part 2
source: YouTube
url: https://www.youtube.com/watch?v=f8xoUkPY4e8
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-secrets---hard-surface-sculpting-tips-part-2/
frame_count: 0
frame_status: pending-selection
---

# Blender Secrets - Hard Surface Sculpting Tips Part 2

**Source:** [YouTube](https://www.youtube.com/watch?v=f8xoUkPY4e8)
**Author:** Blender Secrets
**Duration:** 5m26s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-secrets---hard-surface-sculpting-tips-part-2 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Base mesh sculpting [0:00]
**Transcript (timestamped):**
[0:00] To create the base mesh, I add a round cube.
[0:03] Using the Grab brush, I push and pull it into shape.
[0:07] With Dintopo enabled, the Snake Hook brush allows me to pull out geometry.
[0:11] The Glace Trip brush is useful for adding and removing volume,
[0:15] which can then be smoothed out by holding Shift.
[0:18] Using the Crease brush, you can sketch out some ideas for refining the shape on the geometry.
[0:24] The Scrape brush is good for creating more angular and flattened hard surface shapes.
[0:29] Areas you don't like can just be erased with the Smooth brush.


### Mesh Filter - Inflate [0:34]
**Transcript (timestamped):**
[0:35] Create some panel cuts using the Mask brush.
[0:39] Using the Curve Stroke method, we can keep them nice and angular.
[0:50] Enable Symmetry so you get both sides.
[0:53] Select the Mesh filter in the Tool panel.
[0:56] Set Filter Type to Inflate.
[0:59] Drag the mouse cursor to the right to Inflate.
[1:04] Press Alt-M to clear the mask.
[1:07] Then set Filter Type to Smooth.
[1:10] It's a good idea to remesh at this point.
[1:13] So sample the geometry and then click on Remesh and wait for a moment.
[1:19] Finally, drag the mouse cursor to the right to smooth the geometry.


### Mask Extract [1:27]
**Transcript (timestamped):**
[1:27] One way to work with Hi-Polygon counts is to split an object into several smaller objects.
[1:33] Once you've created a rough base shape, you can use Mask Extract to extract geometry.
[1:40] Press E and choose a more hard surface friendly stroke method such as Curve.
[1:45] Draw some panel cuts.
[1:47] Then invert the mask with Ctrl-I.
[1:50] I want to remesh this object because I don't need that much geometry at this stage
[1:54] and I don't want everything to be slowed down.
[1:56] In the Remesh options, check Paint Mask so you can remesh without losing the mask.
[2:02] Choose a fox or size and click on Remesh.
[2:06] Go to Mask, Mask Extract.
[2:11] Click on OK.
[2:13] New geometry has been created based on the masked parts.
[2:17] We can hide the original round cube in the Outliner.
[2:20] A solidifier modifier was added automatically.
[2:23] We can increase the thickness of the extracted geometry.
[2:27] If we unhide the round cube, we can select all its vertices in edit mode and scale them down.
[2:36] Add a remesh modifier to the new geometry and set a fox or size that looks OK.
[2:41] It doesn't have to be too high res.
[2:43] Then right click and choose Visual Geometry to Mesh to apply all modifiers.
[2:48] Using the Mesh Filter set to Smooth, we can smooth out the remeshed geometry.
[2:53] If you want to separate these into individual objects, select all in edit mode and press B.
[2:59] Then choose Separate by Lose Parts.
[3:04] Hoover over an object and press Alt-Q in Scalp mode to sculpt on it.
[3:10] Or click left of the item in the Outliner.
[3:14] The current object selected for sculpting is then indicated with a brush icon.
[3:22] Now we can use the scrape brush in combination with a line or curve stroke method
[3:26] to add some beveling to the edges of these objects.
[3:29] And using a multiresse modifier to increase the resolution,
[3:34] we can add detail to the individual objects by using alpha textures.
[3:39] For more info about this, watch the previous hard surface sculpting tips video.
[3:44] Using a multiresse modifier, by default only the detail on the currently active object is shown.
[3:50] Using the Mesh Filter set to Smooth, we can select all the objects that we want to sculpt.


### Line Project [3:57]
**Transcript (timestamped):**
[3:57] Using Line Project, we can quickly create hard surface shapes.
[4:01] Add a Round Cube.
[4:03] Set it to Quadsphere with an arc value of 100 or more.
[4:07] The Round Cube is available after you enable the extra object add-on in Preferences.
[4:13] In Scalp mode, select the Line Project tool.
[4:17] In case your Quadsphere is too low-res for your taste, go back to Object mode.
[4:22] Right-click and choose Change Round Cube, then increase the arc value.
[4:28] Enable Mesh Symmetry.
[4:30] Drag the left mouse button to use the Line Project tool.
[4:35] Pressing F flips the direction.
[4:38] You can hold the spacebar to move the position of the line.
[4:43] Hold CTRL to constrain the angle.
[4:47] Check Limit to Segment if you want to limit the angle.
[4:51] If you want to limit the effect to where you draw the line.
[4:55] The Line Project tool flattens geometry, but doesn't actually do any boolean cutting.
[5:01] So it's a good idea to remesh after you've finished using it.
[5:05] Press Shift R to preview the remesh resolution.
[5:09] Then press CTRL R to remesh the geometry.
[5:14] This will make it easier to continue sculpting on it.
[5:17] When you add another round cube, it will remember the previous settings you used.



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
