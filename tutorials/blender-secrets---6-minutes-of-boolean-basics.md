---
title: Blender Secrets - 6 Minutes of Boolean Basics
source: YouTube
url: https://www.youtube.com/watch?v=_S3D8djM5bE
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-secrets---6-minutes-of-boolean-basics/
frame_count: 0
frame_status: pending-selection
---

# Blender Secrets - 6 Minutes of Boolean Basics

**Source:** [YouTube](https://www.youtube.com/watch?v=_S3D8djM5bE)
**Author:** Blender Secrets
**Duration:** 6m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-secrets---6-minutes-of-boolean-basics <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Let's turn this cube into something instead of deleting it.
[0:13] Delete one edge and bevel another one with Ctrl B.
[0:18] Scroll the middle mouse wheel up to increase the amount of segments.
[0:24] You can bevel these corner vertices with Shift Ctrl B.
[0:28] In Object Mode, right-click and choose Shade Smooth and enable Auto Smooth as well.
[0:36] Add a Solidify modifier and increase the thickness.
[0:40] Add a cylinder and scale it down, then enable Shade Smooth and Auto Smooth as well.
[0:48] Duplicate the cylinder a few times and join these cylinders into one object with Ctrl J.
[0:55] Add a boolean modifier to the cube, set to Difference with the cylinders as the object.
[1:01] Under Viewport Display, set the maximum draw type of the cylinders to Wire.
[1:07] You can also just disable their render visibility in the Outliner.
[1:12] Finally, add a Bevel modifier.
[1:33] Pool Tool is a useful cutting tool that you can enable in preferences.
[1:38] First, create an object that acts like a cutter.
[1:43] With the cutter selected, hold Shift and select the other object.
[1:47] Press Ctrl and minus on the numpad to cut.
[1:51] You can still see the cutter object as a bounding box and you can move, rotate and scale it.
[1:58] When you press Tab, you can still edit the object like a normal mesh, so you can add bevels to it, for example.
[2:05] In Edit Mode, you can also duplicate the mesh if you want to create some kind of array quickly.
[2:11] If it doesn't work, try moving the cutter slightly until it does.
[2:19] You can find all the other functions in the Edit tab in the Option panel.
[2:24] What I like to do in a boolean workflow is add some useful things to the Quick Favorites menu.
[2:29] For example, you'll always need Shade Smooth and Auto Smooth.
[2:35] Shadow and Gavety from the Viewport Shading menu are also nice for some extra visual appeal.
[2:41] Apply All is a function that is added by enabling the modifier tools in preferences.
[2:50] It applies all modifiers at once.
[3:06] To make slice cuts like this, create a second object that acts like a cutter and then assuming you have the bool tool add on enabled,
[3:13] press Ctrl and minus on the numpad.
[3:16] This adds a boolean modifier with a difference operation on your object.
[3:20] Now, select the cutter object and add a solidify modifier.
[3:24] Change the thickness value to change the thickness of the slice.
[3:28] Then you can add a bevel to the cutter object to make the slice look around like this.
[3:33] You can add more segments to make the bevel rounder.
[3:38] You can also add a bevel to the original object.
[3:46] To create more than one slice, just keep adding solidify modifier to the cutter object.
[3:56] Make sure that they are above the bevel modifier.
[3:59] Adjusting thickness values will change the way it looks.
[4:12] You can create a lot of variation with just these modifiers.
[4:16] Select the cylinder, hold shift and select the cube.
[4:22] Then press Ctrl and minus on the numpad.
[4:26] Apply all modifiers and delete the cutter object.
[4:30] As you can see, some unnecessary further changes are made.
[4:34] You can also add a boolean modifier to the cutter object.
[4:38] As you can see, some unnecessary vertices are left over.
[4:42] We can fix this in a couple of ways.
[4:44] We can select them and then merge them one by one.
[4:50] Or we can turn on auto merge vertices.
[4:54] Then just slide the vertices to their neighbors by pressing G twice.
[4:58] The vertices are then merged automatically.
[5:01] Now we just have to repeat this step as we do the other vertices.
[5:04] To create some support loops around this hole, an easy way is to select the interfaces and press
[5:09] I to insert, but don't move the mouse.
[5:12] Then press Alt S and scale the selection inwards.
[5:16] Now add an inch loop on the inside with Ctrl R.
[5:24] Subdivide it, it looks perfect.
[5:28] Now we can add a new layer to the inside of the mouse.
[5:32] No boolean issues left.
[5:40] The weld modifier also comes in handy when cleaning up unnecessary vertices left over from boolean cutting.
[5:50] Simply add the weld modifier
[5:54] and turn on the on cage button so we can see the result in edit mode.
[5:58] Then increase the value until you get something that works.
[6:02] If you want to limit the modifier to a specific area, you can also use a vertex group.
[6:18] If you found this topic interesting and would like to know more, don't forget that you can find it in my Blender Secrets ebook.
[6:24] Along with almost 2000 pages of other tips.
[6:28] To get an idea of what the ebook is like, you can download the free sample from my website.



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
