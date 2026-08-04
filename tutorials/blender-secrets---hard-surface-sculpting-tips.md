---
title: Blender Secrets - Hard Surface Sculpting Tips
source: YouTube
url: https://www.youtube.com/watch?v=3Ty0dNNO4bE
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-secrets---hard-surface-sculpting-tips/
frame_count: 0
frame_status: pending-selection
---

# Blender Secrets - Hard Surface Sculpting Tips

**Source:** [YouTube](https://www.youtube.com/watch?v=3Ty0dNNO4bE)
**Author:** Blender Secrets
**Duration:** 8m19s | 3 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-secrets---hard-surface-sculpting-tips <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Round Cube [0:00]
**Transcript (timestamped):**
[0:00] Let's delete all this stuff and add a round cube.
[0:07] This round cube is from the extra object addon that you can enable in preferences.
[0:14] If you accidentally lose this menu, press F9 and it will pop back up.
[0:20] I just needed to select the quad sphere preset.
[0:25] To add some extra subdivisions, which are necessary to sculpt on this sphere, I add
[0:29] a multi-res modifier.
[0:31] And then increase the subdivisions by clicking on subdivide a few times.
[0:36] It always helps to shade smooth.
[0:39] Let's use a red matte cap and pretend we're using Z brush.
[0:44] Here I'm turning on cavity, it makes the sculpting look a bit more pronounced.
[0:49] And I move this sphere up, one unit, by pressing G, Z and 1 on the numpad.
[0:57] Then in scoped mode, drag the toolbar to the right so we can see what all these icons
[1:01] are for.
[1:03] You could use the crease brush with a high strength value to cut some panel lines.
[1:08] Press F to change the radius and make it a bit thinner.
[1:11] In fact, cavity is a bit too extreme a viewport setting I think, so let's turn that off again.
[1:20] So we can draw lines freehand, but it won't look very good, no matter how practice you
[1:24] are.
[1:27] An easier method is to press E and choose a line from the stroke method menu.
[1:32] Now we can draw perfectly straight lines at last.
[1:36] But you can see that where there is any overlap, the crease accumulates in depth.
[1:41] That's not ideal.
[1:44] So instead of the crease brush, let's use the layer brush.
[1:48] Set it to subtract so that it cuts into the surface.
[1:53] Use the height and you can also set it to subtract here if you want.
[1:58] Now we have to press E again for the stroke method menu and choose line again.
[2:03] As you can see, it still accumulates the strokes.
[2:07] We need to check persistent and click on set persistent base.
[2:12] And you have to do this before you draw the strokes.
[2:16] Now we can draw nice straight panel cuts and they won't accumulate.
[2:21] For some reason, sometimes clicking set persistent base once is not enough.
[2:26] You need to click it twice for it to work.
[2:29] So if you find that it doesn't work in your case, just hit that set persistent base button
[2:34] a couple more times instead of once.
[2:38] Here I'm just adding some dots by setting stroke method to drag dot.
[2:43] You could also combine this with an alpha image of a bolt or something to place some
[2:47] bolts.


### Masks [2:50]
**Transcript (timestamped):**
[2:51] Draw a mask.
[2:52] You can do this manually using the mask brush.
[2:56] Press shift F to increase the strength.
[2:59] You can also set the strength higher than 1 by typing the value in the strength field.
[3:04] For example, you can set the strength to 2 for a less blurry mask.
[3:09] The resolution of the mesh is also an important factor for the mask quality.
[3:14] When you press E, you can choose a different stroke method.
[3:18] For example, curve, which you can then use by holding Ctrl and right clicking to draw
[3:22] a curve.
[3:24] Hold Ctrl and click for a sharp corner or hold Ctrl and drag for a smooth corner with
[3:30] handles.
[3:31] Then hold Ctrl and left click to draw the stroke along that curve.
[3:36] You can use both the curve and the line stroke method to draw nice geometric masks.
[3:43] Hold Ctrl if you want to subtract from the mask.
[3:47] To fill the mask, you can use the dots stroke method again.
[3:54] Or you can use the lasso mask, which you can find in the tool panel in the submenu of the
[3:58] box mask tool.
[4:01] If you want to sharpen the mask edges, go to mask sharpen mask.
[4:07] To invert the mask, press Ctrl I.
[4:11] Then you can move the unmasked part to extrude it.
[4:16] Instead, you can also use the mesh filter set to inflate.
[4:21] This gives a different kind of effect, like extruding along face normals.
[4:26] To make the extruded part smoother and remove the artifacts at the sides, first go to mask
[4:31] shrink mask.
[4:33] Repeat if necessary.
[4:36] Sample the mesh resolution in the remesh menu.
[4:40] Check the paint mask option to make sure you can remesh without losing the mask.
[4:46] Then click on remesh.
[4:49] Choose the mesh filter and set it to smooth.
[4:52] Left click and drag the mask cursor to the right until you get the desired smoothness.
[4:59] Press Alt M to clear the mask.
[5:02] Finally you can use the smooth brush for additional smoothing of the sides.


### Alphas [5:06]
**Transcript (timestamped):**
[5:07] The textures are the fastest way to add details to a model in sculpt mode.
[5:12] Previously we had a look at using these to make a sword and we looked at how to create
[5:16] your own alphas.
[5:19] They are used a lot for hard surface sculpting as well.
[5:23] You can find a lot of free alphas and buy big packs of them on Gumroad and Artstation.
[5:28] Usually they are sold as Z brush alphas, but really they are software agnostic and will
[5:33] work just as well in Blender.
[5:36] Make sure your model is subdivided enough for sculpting, for example by using a multi-res
[5:41] modifier.
[5:43] Go to sculpt mode.
[5:46] And press E for the stroke menu and choose drag dot.
[5:50] Now you can drag dots across the surface.
[5:54] For this example I am using these free alphas from JRO Tools.
[5:59] Create a new brush texture and load one of the alpha textures.
[6:05] You can set the display mode to thumbnails to more easily pick the one you like.
[6:11] Depending on the alpha texture you may have to choose either add or subtract as the direction.
[6:18] Set mapping to area plane.
[6:21] Then you can drag the detail to where you want it on the surface.
[6:27] Make on new texture if you want to add additional alpha textures.
[6:36] Press F to change the radius and shift F to change the strength.
[6:45] If you want to rotate the texture to a different angle, press CTRL F before drawing it on
[6:50] the surface.
[6:52] You may want to use constant follow to make sure the entire texture is used.
[7:00] You can also turn on symmetry along an axis of your choosing to mirror the brush.
[7:11] You can drag alpha textures using the drag dot stroke method one by one, but you can
[7:15] also take advantage of the radial array that is available in sculpt mode.
[7:21] This is convenient if you need to create a perfect circular array of bolts for example.
[7:26] Go to sculpt mode and press E for the stroke menu and choose drag dot.
[7:36] Set a radial value on the axis that you want.
[7:40] Now you can drag dots in a radial pattern.
[7:44] You can choose one or several angles on which to sculpt with a radial array.
[7:49] Make on new texture to load a new alpha texture.
[7:53] For this example, I'm using these three alphas from Bergman 3D.
[8:07] Make sure mapping is set to area plane.
[8:11] Now you can create a radial array of hard surface details like bolts.



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
