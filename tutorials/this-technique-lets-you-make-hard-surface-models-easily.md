---
title: This technique lets you make Hard Surface models easily
source: YouTube
url: https://www.youtube.com/watch?v=_6uBdIsvm7c
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/this-technique-lets-you-make-hard-surface-models-easily/
frame_count: 0
frame_status: pending-selection
---

# This technique lets you make Hard Surface models easily

**Source:** [YouTube](https://www.youtube.com/watch?v=_6uBdIsvm7c)
**Author:** Blender Secrets
**Duration:** 9m21s | 21 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py this-technique-lets-you-make-hard-surface-models-easily <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Hard Surface Course update [0:00]
**Transcript (timestamped):**
[0:00] I recently added a new lesson to my hard surface sculpting course and I want to share
[0:05] it here as a preview for anyone curious in that course.
[0:08] The alpha brushes that you see used in the video are included with the course as well
[0:12] as the blend file.
[0:13] One thing you'll notice is that there's not a lot of sculpting in this video.


### What are we making? [0:17]
**Transcript (timestamped):**
[0:17] This video is more about making a sculpting tool.
[0:19] Specifically, we're making a tiling displacement map, which can be a really fun tool to use
[0:23] to quickly generate some concepts in 3D.
[0:26] It's not the only method for making this kind of tiling map and the course explores
[0:29] another technique as well, but this one is pretty easy.
[0:32] For the occasion of this small update, I'm running a short discount just for the weekend,


### Paying the bills [0:33]
**Transcript (timestamped):**
[0:37] so if you're curious about this course and you want to get it, now is a good time.
[0:40] So go to 3dcquests.com if you want to learn more.
[0:43] So here I'm in a fresh scene and I'm just going to switch to the top orthographic view


### Start of the tutorial [0:45]
**Transcript (timestamped):**
[0:48] and I'm going to add a grid.
[0:50] A grid is basically the same as a plane except it already has some subdivisions and I'm going
[0:54] to set it a couple more times.
[0:56] Just so that we have enough geometry.
[0:58] I just want to make sure that the unit scale is 1 and that the scale of the grid is 1 so
[1:03] that there are no surprises later with the scale or anything like that.
[1:07] So let's add a camera and we're going to set this camera to orthographic.


### Setting up the Camera [1:08]
**Transcript (timestamped):**
[1:11] But first let's move it up on the z-axis.
[1:13] It doesn't really matter how high with an orthographic camera, but just set it to orthographic
[1:18] and then set the orthographic scale to 1.5 and I'll explain in a minute why that is.
[1:23] Now let's set the resolution to a square format.
[1:25] So 1080 by 1080 for example.
[1:28] As long as it's square it's all fine.
[1:30] And let's switch by pressing 0 to the camera view and I'm just going to choose a matte
[1:34] cap real quick and turn on the cavity and it's a bit easier to see the depth.
[1:39] Now in sculpt mode I've got my brushes here and these are the brushes from the course


### Using Alpha brushes to add detail [1:44]
**Transcript (timestamped):**
[1:44] and now I can just start dragging them on the surface but as you can see the resolution
[1:48] is much too low.
[1:50] So I'm going to add a militarized modifier.
[1:52] Now it's good that we already have some geometry subdivisions and now if I certified it linearly
[1:58] a few times then it's just easier for the computer to handle all those subdivisions.
[2:03] If we just added a sub-diff modifier to a plane with no geometry subdivisions then it
[2:08] would take a lot more subdivisions and would be heavier for the computer.


### How many Faces do you need? [2:12]
**Transcript (timestamped):**
[2:12] So I have it up to about a million and a half faces, a little bit more, five subdivisions
[2:18] and as you can see now the alphas look nice and crisp.
[2:22] So if they're blurry you basically just don't have enough resolution.


### Tiling Symmetry [2:25]
**Transcript (timestamped):**
[2:25] I want to have tiling symmetry so X and Y tiling that's what we have to turn on and
[2:30] then we're going to set the tile offset X and Y to the same value as the scale of the
[2:35] orthographic camera and that way it's tiling exactly along the borders of the camera but
[2:40] as you can see the alpha doesn't look particularly good.


### Fixing Potential Brush issue [2:43]
**Transcript (timestamped):**
[2:44] It has a radial shape so how do we solve this problem?
[2:48] So let's go to the brush because that's actually a brush setting.
[2:51] We just have to set it to view plane as you can see now it looks fine and so it's really
[2:57] important that the tile offsets and the orthographic camera scale are the same value that way it
[3:02] maps perfectly as you can see.
[3:04] So everywhere we drag the alpha it shows up on the other side as well and unfortunately
[3:09] we have to change for every brush that we use we have to change it to view plane the
[3:14] first time we use it.


### Adding details [3:15]
**Transcript (timestamped):**
[3:15] So now I can just start really quickly adding some detail just have to remember to keep setting
[3:21] it to view plane and no matter where we drag it it will arrive on the other side and it
[3:27] will tile perfectly once we bake it to a displacement map.
[3:31] So I'm just having some fun adding some detail and this one is a negative brush so I have
[3:35] to hold control and so I'm quickly going to add some more detail this way.
[3:39] And of course with control F we can rotate the brush with F we change the radius and
[3:44] with shift F we change the strength but I recommend with alpha brushes that you set
[3:49] the strength always to one to have the correct shape of the alpha.
[3:53] And of course you don't have to stick just to alpha brushes you can also just model geometry


### Where did my details go? [3:58]
**Transcript (timestamped):**
[3:58] and now when we switch to object mode we can't see the detail and that's because we have
[4:02] to increase the viewport levels on the motorized modifier.
[4:05] Now I'm just going to add a single third from the extra objects addon that you have to install


### Adding a Single Vertex and Extruding [4:07]
**Transcript (timestamped):**
[4:11] in extensions and I'm just extruding that vertex and I'm just creating some shapes real
[4:17] quick by just extruding that and it is perfectly on the surface of the grid.
[4:22] It's important that there is no undercut on the curves that I'm going to create from


### Adding Array modifiers for X,Y tiling [4:26]
**Transcript (timestamped):**
[4:27] this and I'm just going to add an array to this extruded vertex and let's set it to constant
[4:32] offset and then again use that value of one and a half on the x axis and then we duplicate
[4:38] it and then we set the negative version of the x value and then we duplicate it again
[4:43] and we repeat that for the y axis.
[4:46] So set y to 1.5 and then another one minus 1.5 on the y axis.
[4:56] So now we have a tiling extruded vertex and we can extrude it and it will appear on the
[5:02] other side as well.
[5:03] And let's quickly set this grid to be non-selectable otherwise we keep accidentally selecting it.
[5:11] And let's turn on on cage so that we can select it everywhere in all the arrays and we can


### Turn on On Cage to edit the Array anywhere [5:12]
**Transcript (timestamped):**
[5:17] just take one vertex and shift t and duplicate it and we just have to make sure that when
[5:22] we exit on one side of the axis we appear on the other side that we just continue it
[5:27] until it goes inside of some extruded alpha shape or something else.
[5:33] So now that I've finished doing that I will convert it to a curve and then we can easily
[5:37] give them all some thickness.
[5:40] So now we can start the shape and then we just undo that and let's select some of these


### Beveling Vertices for nice round corners [5:42]
**Transcript (timestamped):**
[5:44] corner vertices and then we can just bevel them to make them all a bit smoother.
[5:49] So shift control B to bevel these vertices.
[5:52] Then when we convert it to a curve it will have a nice round shape.
[5:56] So when you press shift control and B to bevel these vertices you will be able to scroll
[6:00] the mouse wheel up or down to increase or decrease the amount of vertices.
[6:06] And if you want you can also change the profile but in this case the default is fine.
[6:11] So that looks a bit smoother so let's convert it again to a curve and then again give it


### Convert to Curves, add thickness [6:13]
**Transcript (timestamped):**
[6:16] some depth in the bevel settings here.
[6:19] So then I converted this all to mesh and then I selected everything in edit mode and merged
[6:25] by distance and as you can see that removed a lot of vertices and then I was able to edit
[6:29] the shape with proportional editing.
[6:32] I just wanted to make sure that these pipes don't really overlap each other and just adjust
[6:37] their thickness a bit as well with alt S.
[6:40] So you can select one particular piece with L in edit mode and then alt S to scale it
[6:45] up or down.
[6:46] You just have to make sure that you also do that on the other side.
[6:51] So if it shows up somewhere else in the map then you need to make sure that it's scaled
[6:55] equally.
[6:56] So here I have a test file for detailing displacement and as you can see it tiles very


### Testing the baked displacement map [6:57]
**Transcript (timestamped):**
[7:01] nicely but there is one little problem and that is here things don't match up and that
[7:06] is simply because I was messing up those pipes with proportional editing and let me just show
[7:13] you how you can fix that.
[7:14] You can see it here this is the same problem that is repeated and let me just quickly show
[7:19] you how to solve that.


### How to fix inconsistencies [7:21]
**Transcript (timestamped):**
[7:21] So here we are back in the file and yeah it is basically just this area here that doesn't
[7:28] match up.
[7:29] Here you can see it doesn't even go all the way to the edge.
[7:31] It's pretty easy to solve that.
[7:32] First of all I am just going to take this and I just go to wireframe mode and I am just
[7:39] going to add in x-ray mode.
[7:40] I am just going to make sure this goes all the way till there and then I am just going
[7:44] to take these, select these and just delete them.
[7:49] So I am just going to select these.
[7:50] These are the ones that I edited with proportional editing and I am just going to duplicate them
[7:55] with shift D and just right click to cancel and then transformation.
[8:00] And change it to shift C and Y to move them minus to move them down in the minus y direction.
[8:06] And can you think of the value that I should type on an iPad to move them?
[8:10] Is it one unit, two units?
[8:14] It's one and a half.
[8:15] It's the same value as the camera scale and everything else 1.5.
[8:20] And then it should match up perfectly now so let me just quickly go ahead and bake that


### Result of the bake [8:25]
**Transcript (timestamped):**
[8:25] and I will show you the results.
[8:27] Well, you can see the problem is now completely solved by replacing that texture.
[8:31] And so now we can just tile this as many times as we want.
[8:35] And one more thing before you bake is these things that are looking quite segmented, they


### Use Flat Shading, not Smooth shading (before you bake) [8:36]
**Transcript (timestamped):**
[8:41] will also render that way in the displacement map, even if you set it to shade smooth.
[8:47] So it's important to check.
[8:50] And if necessary, just add a sub-diff modifier.
[8:52] So I'm just pressing Ctrl 2 in this case to add two levels.
[8:56] And then when I bake this, the map will look nice, otherwise you will see those flat faces
[9:02] in the bake.
[9:03] So this concludes making the geometry for the displacement map.


### Conclusion [9:05]
**Transcript (timestamped):**
[9:06] And next we'll bake it with a simple gradient material, and then we can actually use it
[9:10] like in this example here.
[9:12] So if you're curious to learn more about this course and its unique workflow, now is a good
[9:16] time with this discount.
[9:17] So check that out on 3dsecrets.com.



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
