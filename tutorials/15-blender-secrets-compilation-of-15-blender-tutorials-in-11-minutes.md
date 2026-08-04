---
title: 15 Blender Secrets (Compilation of 15 Blender Tutorials in 11 minutes)
source: YouTube
url: https://www.youtube.com/watch?v=hZ2iWrbRNd0
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/15-blender-secrets-compilation-of-15-blender-tutorials-in-11-minutes/
frame_count: 0
frame_status: pending-selection
---

# 15 Blender Secrets (Compilation of 15 Blender Tutorials in 11 minutes)

**Source:** [YouTube](https://www.youtube.com/watch?v=hZ2iWrbRNd0)
**Author:** Blender Secrets
**Duration:** 10m52s | 13 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py 15-blender-secrets-compilation-of-15-blender-tutorials-in-11-minutes <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Create a simulation in the Factor modifier build of Blender.
[0:10] Select the factored object and click on Inner Smoke.
[0:13] Select the factoring object and click on Create a brush.
[0:16] Now you have smoke added to the simulation.
[0:18] Name the smoke cache and click on Bake.
[0:22] Turn on External and turn off Use Light Path.
[0:25] Click on the File Path icon.
[0:27] Open the Cache folder and click Accept.
[0:29] Now the smoke cache is loaded from disk.
[0:33] Save the blend file and export it as well as an Alembic file.
[0:38] Import the Alembic file in Blender 2.8.
[0:42] Append the smoke domain from the blend file that you saved.
[0:50] Now you have your simulation and smoke in Blender 2.8.


### Connected Faces [0:54]
**Transcript (timestamped):**
[0:58] Mover the mouse cursor over a face and press L to select connected faces.
[1:04] Or with one or more faces selected, press Ctrl L to select connected faces.


### Textures [1:12]
**Transcript (timestamped):**
[1:16] Procedural textures are a great way to add detail to your objects.
[1:21] To get started, add a bump map, color ramp and noise texture to the material.
[1:30] To change the noise appearance, experiment with its values.
[1:36] The color ramp gives us extra control over the noise texture.
[1:42] There are several different noise textures available.
[1:48] To mix them for even crazier results, use a Mix RGB node.


### Reroute Node [1:53]
**Transcript (timestamped):**
[1:57] Connecting nodes is easy.
[1:59] Just drag one socket to the next.
[2:02] Node trees can get kinda crazy though.
[2:07] Using the reroute node, we can at least connect the nodes more efficiently.
[2:12] Hold Shift and drag the right mouse button across a node connection.
[2:16] Now drag a new connection.
[2:20] You can add a reroute node just to create an angle in the connection.
[2:25] Press G to move the reroute node.
[2:30] Node by atlateasusual, atabdubwem and attopkum on Twitter.
[2:35] Thanks guys.


### Edit Mode [2:38]
**Transcript (timestamped):**
[2:42] Let's say you've downloaded this model somewhere.
[2:45] When you go to edit mode, you discover that it's all triangles.
[2:51] We can fix that quickly by pressing Alt J in edit mode.
[2:57] Now it's all quads.
[3:02] You can also do this through the face menu.
[3:06] Just make sure the faces are all selected.


### Transform Orientation [3:11]
**Transcript (timestamped):**
[3:14] Let's say you want to slide this cube along the surface of this other cube.
[3:19] Manually rotating one cube to match the other is impractical.
[3:23] So is moving it along the surface accurately.
[3:26] For this, you can create a custom transform orientation.
[3:30] In edit mode, select a face as the basis of the orientation.
[3:34] In the transform orientations menu, click on the plus icon.
[3:38] Give your new transform orientation a name.
[3:40] Or have the blender community do it for you.
[3:45] You can align the cube's rotation to the other cube now.
[3:48] By going to object, transform, align to transform orientation.
[3:53] Pressing G and then X or Y will move it along the face surface.
[3:58] Bonus tip.
[3:59] Press G and then shift C to exclude the C axis.


### Copy Rotation [4:05]
**Transcript (timestamped):**
[4:08] Select if you want to copy the rotation of one object to another object.
[4:13] Go to preferences and find the copy attribute addon.
[4:20] Enable the addon and close preferences.
[4:23] Now select the object that you want to rotate.
[4:26] Then select the object from which you want to copy the rotation.
[4:30] Press Ctrl C and choose copy rotation.
[4:35] Now both objects are rotated in the same way.


### Copy Animation [4:40]
**Transcript (timestamped):**
[4:43] To copy animation from one object to another, select the object you want to animate.
[4:49] Then select the object you want to copy animation from.
[4:53] Now press Ctrl L and choose animation data.
[4:57] As the animation data is now linked, changing the animation on one object also changes the
[5:02] animation on the other.
[5:04] To prevent this, make the object single user.
[5:07] Go to objects, relations, make single user, object animation, all.
[5:15] Now you can edit the animation of each object independently.
[5:20] You can even do this with armatures as long as they are the same.


### Cloth seam [5:26]
**Transcript (timestamped):**
[5:29] Create a plane.
[5:31] Set it to shade smooth.
[5:33] In edit mode, rotate the plane.
[5:36] Subdify it a few times.
[5:38] Select the top row of vertices and add them to a vertex group.
[5:42] Create a basis shape key and create another shape key.
[5:46] Set the shape key value to 1 and scale the top vertices down.
[5:53] Now set the key at the first frame on the timeline for value 0.
[5:57] Set the key at the later frame on the timeline for value 1.
[6:03] Now add a cloth sim.
[6:06] Under a shape, add the vertex group to the pin group.
[6:09] This will make sure the cloth doesn't fall down.
[6:12] Turn on self-collisions so the cloth doesn't clip through itself.
[6:16] Then play the simulation.
[6:25] So you've created a curtain with the cloth simulation and now you want to turn it into
[6:29] a regular polygonal mesh.
[6:32] Pick the frame of the simulation you like best.
[6:35] Create a new shape key from the mix.
[6:38] Delete the old shape keys and then the mix.
[6:40] Finally press apply on the cloth modifier.
[6:44] And there you go, a regular old fashioned polygonal mesh, just like your grandmother
[6:48] used to make.


### Holdout [6:51]
**Transcript (timestamped):**
[6:54] A holdout is an object that acts like a mask creating transparency.
[6:59] Select the object you want to use and press M to add it to collection.
[7:03] Go to the filter icon in the outliner and make the holdout icon visible.
[7:08] Then click on the holdout icon for the collection you want to use as a mask.
[7:12] It doesn't work until you turn on transparent under the film options.
[7:18] Here we see the result in the EV render.
[7:20] It works the same in cycles.


### Support loops [7:25]
**Transcript (timestamped):**
[7:29] Support loops are a fundamental part of polygonal modeling.
[7:32] We can see what it does more clearly by adding a sub-div modifier to the object.
[7:37] Add a loop cut with the shortcut Ctrl R.
[7:40] Left click to add the loop cut, then move it to where you want.
[7:44] Left click again to confirm the position.
[7:50] The closer the loop cut gets to the edge, the sharper that edge will be.
[7:54] To change the position of the loop cut again, select it by double clicking on it, then
[7:59] press G twice to move it.
[8:01] Left click to confirm the new position.
[8:03] There are other, more non-destructive ways to create sharp edges like creasing or the
[8:08] battle modifier.
[8:09] The benefit of support loops is that the model will look the same if you export it to other
[8:14] software.


### Cloth brush [8:16]
**Transcript (timestamped):**
[8:19] The cloth brush is an amazing new feature available from a special build of Blender 2.83 alpha.
[8:26] You can download it now from Graphic All.
[8:29] Unpack the file with 7-zip and double click on the Blender XC file to launch it.
[8:35] Be careful using experimental versions of Blender for series work as it may crash.
[8:40] Let's try it out on this plane.
[8:43] Add some sub-div, turn on shade smooth.
[8:46] Go to the sculpting layout and turn off symmetry.
[8:49] Select the non-brush, there is no icon yet for this brush.
[8:53] You may need to change the cloth mask value to something like 0.1.
[8:58] And now you can just drag and see the magic happen.
[9:01] Thanks to Pablo de Barro for making his amazing sculpting brush available to everybody.
[9:12] If you want the camera to match what you see in the viewport, press Alt-Ctrl-0.
[9:18] This will move the camera to match what you are seeing in the viewport.
[9:21] To change the active camera, select the camera you want and press Ctrl-0.
[9:26] When you render, it will be what the active camera sees.
[9:30] Check the box next to Lock Camera to View to be able to move the camera view much like
[9:34] the viewport.
[9:36] This is a quick and familiar way to reposition the camera.
[9:39] You can add this checkbox to the quick favorites for easy access.


### Mask [9:45]
**Transcript (timestamped):**
[9:48] I recommend adding a sub-div modifier on top just to smooth everything out a bit more.
[9:54] The mask brush creates a pinned area.
[9:56] Keep in mind modifiers hide the mask, so turn them off for a moment.
[10:00] With the mask and expand function of the cloth brush, you can do stuff like this.
[10:05] The plain force falloff seems to get a better result in this case.
[10:09] Holding Shift smooths out areas where needed.
[10:12] Pinch Point works well together with plain force falloff to create this kind of pinched
[10:16] cloth.
[10:17] Set the cloth mask lower or the strength higher.
[10:20] I like to use 0.1 for the cloth mask and 1 for the strength.
[10:24] Press F to change the radius quickly.
[10:26] You can also use the cloth brush on a shape key, so you can kind of animate it.
[10:31] If you don't know where to get this build of blender or how to install it, watch my
[10:34] previous tutorial on installing the cloth brush build.



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
