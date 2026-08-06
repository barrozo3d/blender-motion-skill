---
title: Grease Pencil in Blender 5 - New Pen tool and Sharp Corners (and some common Grease Pencil issues)
source: YouTube
url: https://www.youtube.com/watch?v=tyPirJ_qWKs
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 5 — Pen tool and Sharp corner point type are explicitly new features in this release"
tags: [grease-pencil, workflow, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
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


Frames captured — see "Captured Frames" section below.


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

## Captured Frames

- [0:24] tutorials/frames/grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea/frame_000.jpg
- [0:46] tutorials/frames/grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea/frame_001.jpg
- [1:13] tutorials/frames/grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea/frame_002.jpg
- [1:40] tutorials/frames/grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea/frame_003.jpg
- [2:20] tutorials/frames/grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea/frame_004.jpg
- [3:05] tutorials/frames/grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea/frame_005.jpg
- [3:30] tutorials/frames/grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea/frame_006.jpg
- [4:17] tutorials/frames/grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea/frame_007.jpg

---

## Structured Notes

### Core Technique
A full walkthrough of Blender 5's two headline **Grease Pencil** additions long requested by vector artists coming from Adobe Illustrator — a proper **Pen tool** for click-to-place Bezier curve strokes with draggable handles, and true **sharp/Corner point types** (previously all points were smooth-only) — demonstrated end-to-end by inking a rough sketch into a clean, filled, layered vector-style cat illustration.

### Summary
Frame 000 shows a rough pencil sketch of a cartoon cat (ears, face, paws, striped body) dragged into a 2D Animation project as a background reference, with Edit Mode + Point Selection active. Frame 001 shows the new **Pen tool** selected in the toolbar, actively drawing one ear as a smooth Bezier curve with visible control handles (drag-after-click to shape the curve). Frame 002 shows a right-click context menu with **Set Corner Type** open (options including Smooth/Free and **Sharp**), a point on the ear stroke selected and about to be converted — this is the new Blender 5 sharp-corner capability. Frame 003 shows the paw-claw strokes being repositioned/moved as a group via the Move operator's redo panel (Global/Individual Origins options), the full inked line-art cat now taking shape in solid black over the gray sketch. Frame 004 shows the completed black-ink line-art cat (ears, face, paws, striped tail/body) fully drawn, sketch still faintly visible underneath. Frame 005 shows the same line art with a skin-tone Fill color applied to the head/body via the color picker, a highlighted tooltip warning "(Make sure the Alpha is set to 1 otherwise it's transparent)." Frame 006 shows the finished orange-and-white colored cat illustration with all fill colors applied per shape (orange body, white paws, black outlines). Frame 007 is a sponsored end card for the "Blender Secrets" e-book.

### Key Steps
**Setup:**
1. Open a **2D Animation** project and drag/drop a rough sketch image in as a background reference.
2. Switch the Grease Pencil object to **Edit Mode > Point Selection** mode.

**Pen tool (new in Blender 5):**
3. Select the **Pen** tool; click to place a point, click again elsewhere to create a connecting segment, repeating to build a curve stroke (zoom in if clicks are landing on existing handles instead of creating new points).
4. **Click-and-drag** (instead of a plain click) to create a Bezier point with pull-able handles, letting you shape smooth curves as you draw.

**Corner Types & sharp corners (new in Blender 5):**
5. Select a point and press **V** to change its handle type (e.g. to Free), then adjust handles individually — **Tweak** selection mode is recommended for this.
6. Go to **Stroke > Uniform Thickness** to enable adjustable stroke thickness.
7. Select a corner point, go to **Point > Set Corner Type**, and choose **Sharp** — this is the new Blender 5 feature enabling true hard corners, not possible in earlier versions.
8. Use a **Mirror** modifier to mirror strokes for symmetrical shapes (e.g. matching ears/paws).
9. Press **Alt+A** to deselect all points before starting a new, unconnected stroke.

**Cleanup & shape tools:**
10. To smooth a stroke, select unnecessary points and **Ctrl+X > Dissolve** to remove them while keeping the overall curve shape, then adjust remaining points.
11. Click (without dragging) to place points that form **straight-line** segments instead of curves.
12. Clicking close enough to a stroke's start point automatically **closes the loop**; alternatively check the **Cyclic** box in Edit Mode to force a closed loop.
13. Hover over a stroke and press **L** to select it entirely, then **Shift+D** to duplicate it.
14. For perfect circles: add a new blank Grease Pencil object in Object Mode, use the built-in primitive shapes in the Tool panel, hold **Alt** and start dragging from the center, and press **Enter** to confirm.

**Fill, layers, and organization:**
15. Adjust stroke **Thickness** and **Opacity** — a black material with low opacity renders as gray, not solid black.
16. In the Option panel, increase stroke **Resolution** for smoother curves.
17. Besides stroke color, set a **Fill** color per shape; ensure the stroke is stacked correctly in Edit Mode and **Fill Opacity is set to 1** (otherwise it renders transparent).
18. Move strokes along the **Y axis** to control front/back stacking order in 3D space; press **Numpad 0** to return to camera view.
19. Hover + **L** to select a specific enclosed region (e.g. the nose) and create a new **Material** with a different fill color, then click **Assign**.
20. If a stroke visually appears in front of another despite being behind it in 3D space, they're likely on the **same layer** — select the stroke, press **M**, and move it to its own **Layer**, then reorder layers to fix visibility.
21. Alternatively, press **P** (Separate) to split a selection into its own independent Grease Pencil object.
22. To remove the background reference sketch once done, uncheck **Background Images** in the Camera Settings.

### Nodes / Settings
- **Pen tool** (new, Blender 5) — click for straight points, click-drag for Bezier handle points.
- **Point > Set Corner Type:** Smooth / Free / **Sharp** (Sharp is new in Blender 5).
- **Shortcut:** V — cycle a point's handle type.
- **Stroke > Uniform Thickness.**
- **Modifier:** Mirror — for symmetric stroke duplication.
- **Shortcuts:** Alt+A (deselect all), Ctrl+X > Dissolve (remove points while preserving curve shape), L (select linked stroke under cursor), Shift+D (duplicate), M (move stroke to layer), P (Separate to new object).
- **Edit Mode > Cyclic** checkbox — force-close an open stroke loop.
- **Material:** Stroke color + Fill color (Fill Opacity must be 1 to render solid).
- **Camera Settings > Background Images** — toggle to show/hide reference sketch.

### Difficulty
Intermediate

### Blender Version
Blender 5 — the Pen tool and true Sharp corner point type are explicitly new features introduced in this release (previously grease pencil corners could only be smooth).

### Tags
grease-pencil, workflow, intermediate

---

## Related Tutorials
- [Daily Blender Tip 97 - Exploring Grease Pencil - Different Brushes](daily-blender-tip-97---exploring-grease-pencil---different-brushes.md) — shares grease-pencil, workflow; that earlier (Blender 2.8-era) tutorial surveys basic Draw Mode brush presets, a useful contrast to this Blender 5 tutorial's more advanced vector-style Pen tool and corner-editing workflow.
