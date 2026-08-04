---
title: Grease Pencil in Blender 5 - New Pen tool and Sharp Corners (and some common Grease Pencil issues)
source: YouTube
url: https://www.youtube.com/watch?v=tyPirJ_qWKs
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: needs-review
frames_dir: tutorials/frames/grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea/
frame_count: 0
frame_status: pending-selection
---

# Grease Pencil in Blender 5 - New Pen tool and Sharp Corners (and some common Grease Pencil issues)

**Source:** [YouTube](https://www.youtube.com/watch?v=tyPirJ_qWKs)
**Author:** Blender Secrets
**Duration:** 4m24s | 14 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'Remove background sketch'

---


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Blender 5 adds some new grease pencil features, such as sharp corners and a pen tool
[0:06] Two features which are desired by vector artists that are used to Adobe Illustrator
[0:12] To get started, I open a new 2D animation project and I drag and drop a quick sketch that I made
[0:19] Then I switch to Edit mode and to Point Selection mode


### The new Pen tool (Blender 5) [0:24]
**Transcript (timestamped):**
[0:24] Select the Pen tool
[0:27] Draw a point and then another point to create a segment and so on to create a curve stroke
[0:34] You may have to zoom in, otherwise instead of drawing more points, it will just select the handles
[0:40] Drag after clicking to create a bezier curve with handles


### Corner Types [0:45]
**Transcript (timestamped):**
[0:46] Select a point and change it to a different type, like free, by pressing V
[0:51] Select the handles and adjust the curve shape as needed
[0:54] I recommend using tweak selection mode for this
[0:59] Go to Stroke, set uniform thickness so that you can adjust the thickness of the strokes


### Stroke Thickness [1:00]
**Transcript (timestamped):**
[1:06] After that, when you select a corner point, you can change it by going to Point, set corner type


### Corner Sharpness (Blender 5) [1:07]
**Transcript (timestamped):**
[1:12] Now you can make sharp corners, which was not possible before Blender 5
[1:17] Using a mirror modifier, we can mirror the stroke
[1:21] If you want to add more strokes that are not connected, make sure that you deselect any points with Alt A before drawing the new stroke
[1:34] Sometimes smoother strokes can be achieved by removing unnecessary points


### Smoother strokes [1:35]
**Transcript (timestamped):**
[1:39] To do that, select those points and press Ctrl X, then choose dissolve
[1:44] Then adjust the remaining points
[1:47] By clicking without dragging, you create points that create straight lines


### Straight strokes [1:49]
**Transcript (timestamped):**
[1:53] Be careful not to create new points too close to existing strokes
[1:57] You can always adjust their location later
[2:01] If you click close enough to the start point, it will close the loop


### Cyclic strokes [2:02]
**Transcript (timestamped):**
[2:05] Or you can make it a closed loop by checking the Cyclic box in Edit mode
[2:10] Select the rest of a stroke by pressing L while hoovering over it and duplicate it with Shift D
[2:17] To create the circle, first add a new blank grease pencil object in Object mode


### Perfect circle [2:20]
**Transcript (timestamped):**
[2:26] You can find these primitive shapes in the tool panel
[2:31] Instead of drawing the circle like this, hold Alt and start from the middle
[2:35] Then press Enter to confirm
[2:41] Then you can adjust the stroke thickness
[2:46] And also the stroke opacity
[2:48] Otherwise a black material will just look gray


### Stroke Opacity [2:49]
**Transcript (timestamped):**
[2:52] In the option panel, you can increase the resolution of the stroke as well
[2:57] Besides the stroke color, you can also set a fill color


### Fill [3:00]
**Transcript (timestamped):**
[3:01] Be sure to stack the stroke in Edit mode and set fill opacity to 1
[3:11] If you want some strokes to be in front of others, move them on the Y axis
[3:16] You can go back to the camera view by pressing 0 on the numpad
[3:20] To fill the nose with a different color, select it by hoovering over it and pressing L


### Layers [3:22]
**Transcript (timestamped):**
[3:25] Create a new material, give it a name and a different fill color and click on Assign
[3:32] Be sure to stack the stroke in Edit mode and set fill opacity to 1
[3:39] If you encounter the problem that something is in front of something else, even though in 3D space they're behind that thing
[3:45] That's because they're probably on the same layer
[3:47] You can select that stroke, press M and then move it to its own layer
[3:53] And then you can play with the order of the layers to change the visibility
[3:57] Alternatively, you can press P and separate it by selection to make it a separate grease pencil object
[4:04] Finally, to remove the background image, uncheck Background Images in the Camera Settings


### Separate to new object [4:09]
**Transcript (timestamped):**
[4:09] You can also change the background image to be in the camera settings
[4:13] To remove the background image, uncheck Background Images in the Camera Settings


### Remove background sketch [4:18]


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
