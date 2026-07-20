---
title: How this 2D/3D animation was made - Introduction to Blender greasepencil and tips for beginners
source: YouTube
url: https://www.youtube.com/watch?v=saIFT8_j0LQ
author: Dédouze
ingested: 2026-07-19
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-this-2d3d-animation-was-made---introduction-to-blender-greasepencil-and-tips/
frame_count: 0
frame_status: pending-selection
---

# How this 2D/3D animation was made - Introduction to Blender greasepencil and tips for beginners

**Source:** [YouTube](https://www.youtube.com/watch?v=saIFT8_j0LQ)
**Author:** Dédouze
**Duration:** 19m52s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-this-2d3d-animation-was-made---introduction-to-blender-greasepencil-and-tips <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction & news [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone, welcome to the channel if you are new or welcome back.
[0:05] I hope you are well, I hope you had a great day and enough time to develop your art and try new things lately.
[0:13] I got asked a lot about the software and the techniques I used to create these animations.
[0:18] Well, most of you already know, I used the free software Blender 3D and most importantly the tool called grease pencil in that software.
[0:28] So what can you do with Blender's grease pencil tool?
[0:31] This video is not really a tutorial, I wanted to record some detailed tutorial during this whole year but I never found the time to make a proper video.
[0:40] And you see the software evolved this a lot and even my technique changes all the time so it was hard to settle on one content for a full tutorial.
[0:50] So I thought maybe I could start with a presentation where I would show one particular scene and I would explain what tools I used to create it.
[1:00] So I will give you all the keywords you need to know so you can search properly and learn from the many contents available on YouTube after watching this.
[1:10] Plus, after this presentation, I will give a few tips for beginners with an update about the tutorials that I made a year ago.
[1:19] And also I will showcase some artists that use the same grease pencil tool who might inspire you or help you with some tutorials.


### Behind the scenes [1:27]
**Transcript (timestamped):**
[1:27] Today we are going to explore this particular scene.
[1:31] This is a network commissioned by the YouTube company.
[1:34] They asked me to create an animation for the upcoming library of timer countdowns for Premiere videos.
[1:41] So very soon when you launch your video as a YouTube Premiere, you will have a list of new countdown themes for the 10 minutes before the launch and my work will be in this list.
[1:52] This was a great opportunity and I also made all the scenes that will appear during the 10 minutes animation but today we are going to focus on this particular scene.
[2:04] Everything you see here was created, drawn and animated in Blender 3D, directly with a pen, tablet and a mouse.
[2:12] There is not a single JPEG or PNG imported from another software and also I didn't have to buy any extra plugin to achieve this.
[2:21] It's all made with all the tools already available in Blender.
[2:25] This scene has basically two types of objects, 3D objects and Christmas-y objects.
[2:31] Of course there are also elements like lights and grids and so on but the things you see in the end are just the 3D stuff and Christmas-y stuff.
[2:41] The 3D objects are easy to spot, it's the teapot, the table, the blocks that made the floor and the walls.
[2:49] And the Christmas-y object are these hand-drawn cloths and these plants and the lines in the background and also some lines drawn or there are some 3D objects.
[3:00] Yes because Christmas-y lines can also be drawn over the surface of 3D objects and we'll see that later.
[3:08] An extra element, I won't go that this part today but for information you can also make some compositing inside Blender.
[3:16] Here on top of the image there is a grain effect made with a bunch of moist textures generated in Blender.
[3:23] I even added some dust and scratches that I drew manually with Christmas-y on top of the grains but back to the scene contents now.
[3:32] First part, the Christmas-y objects.
[3:36] A Christmas-y object is like a piece of paper floating in space.
[3:40] You place it somewhere and you draw on it like if you were drawing on a canvas in a 2D software except that now it's floating in 3D space
[3:49] and you can just draw on it with your pen tablet without leaving the software.
[3:54] The Christmas-y object is a canvas that can contain a hand-drawn animation with layers and masks and a lot of things.
[4:02] And the canvas itself can also be animated and deformed.
[4:07] It can be spread on a 3D object and spoiler for the other scenes.
[4:12] It can be attached to other objects and move with them or it can just move along like a single 3D object in a 3D scene while still having its own layers and 2D animation inside.
[4:25] So it can do a lot of things.
[4:28] Here for example, I drew this plant in a Christmas-y object so the Christmas-y is just this transparent canvas that I placed here
[4:36] and you can see the 2D frames displayed in the timeline below and the layers in this panel.
[4:42] There is a loop effect on these objects so the frames just fill a portion of the timeline and they are repeated automatically.
[4:50] I started drawing the leaves frame by frame with traditional 2D techniques with onion skins but for the images in between
[4:59] I used the sculpt tool to duplicate and deform the previous images and make a smooth transition to the next image.
[5:07] Gris pencil has a feature to smoothen your lines and to edit multiple frames at the same time.
[5:14] And there is also an auto-interpolation feature but you have to separate your drawing into simple parts to make it work properly.
[5:21] So I used it for little parts on the leaves like the lights and the shadows.
[5:27] On top of this traditional 2D animation I placed something called lattice.
[5:33] I have no idea how to pronounce that.
[5:36] It's like you're going to a Starbucks and you ask for a chai tea lattice.
[5:43] Basically it's like a creed that warps everything that you put in it and it warps them in real time.
[5:51] You can animate your drawing without this tool but in addition to the frame by frame animation in the object.
[5:58] This can make the animation a bit more complex because as you can see, you can move the points of the lattice in any direction
[6:05] and the drawing attached to it will follow the creed smoothly.
[6:09] And even more, you can attach an armature to the lattice.
[6:14] It's the same armatures used for 3D animation so instead of animating the lattice point by point,
[6:21] you can just associate each bone of your armature to a group of points of the lattice
[6:27] and then when the armature moves, each bone grabs its associated points.
[6:33] So the whole creed follows the bones and the drawing follows the creed.
[6:40] And in the same time inside the drawing, there's a 2D animation that is still playing so the whole thing becomes like something more organic.
[6:51] This idea of adding a deformer on the plants was not initially in the artwork for the commission.
[6:58] I added it later and I was not sure if I would keep it so it might not be in the final video but I wanted to show it in today's demo so you know that this option exists.
[7:09] The gloves are also just flat drawings, simple, grisp and seal objects.
[7:14] I also tried an alternate version with a lattice and an armature to add an extra motion on the whole group including the string.
[7:25] The building at the back is just a group of free flat drawings, very simple grisp and seal objects also.
[7:32] As you can see, you don't always need complex 3D shapes to make a scene like this.
[7:37] Most of my drawing has just flat drawings now.
[7:40] And that was not always the case I admit.
[7:43] For my first artworks in Blender, I used to create complex grisp and seal objects with a lot of faces inside.
[7:51] As the example you can see in my old tutorial where I show how I create a juice box.
[7:56] The main element in this tutorial was made with one single grisp and seal object but with three faces inside.
[8:04] Well, if you already followed that tutorial, don't worry, you didn't lose your time because you actually learned the hard way.
[8:12] That is the technique I use for my most complex objects today.
[8:17] And now for the simple parts in my creations, I just assemble multiple grisp and seal objects that all have only one face.
[8:26] Instead of making one single grisp and seal object with many faces or planes inside.
[8:31] I will go back to that subject later in the part about the updates on my old tutorial but for now, let's see the other objects in this scene.
[8:41] Little break, I got sick today and my voice is getting worse every hour so sorry if I sound weird now.
[8:49] I'm going to try to finish this recording before I cannot talk anymore.
[8:54] This is also a grisp and seal object but it's different than the others.
[9:00] You don't really see where is the plane, the canvas. The strokes go on different planes and directions.
[9:07] This is because this time when I am inside the drawing, which means in...
[9:14] This time when I am inside the drawing, which means in draw mode, instead of using this default option for a stroke placement, I switch it to surface.
[9:25] When this option is selected, everything that I draw is projected on the 3D surfaces below the pen.
[9:32] There can be weird things happening when you're drawing in this mode like sometimes the lines are super far from the object
[9:39] or sometimes they are half hidden inside the polygons. To fix that you have to adjust this offset option.
[9:46] Most of the time for me it works with a value around 0.01 but it can be completely far from this value for some cases.
[9:56] In the current version of Blender, as I am recording this video, the ideal offset value seems to depend on the camera settings and the scale of the objects in the scene.
[10:07] And when you draw from the camera view, the drawings on 3D surfaces are more accurate and the offset seems to make more sense than when you draw from the 3D view in the viewport.
[10:20] This could be the subject of the whole video but you will find more resources out there if you want to know more about how to draw on 3D surfaces with Prismarcile.
[10:31] Now let's see the other kind of objects in this scene, the 3D objects.
[10:37] Even if your plan is to just master 2D animation in Blender, some tips on 3D animation will help you a lot, even just for stuff like camera animation modifiers
[10:50] and also some crucial key shortcuts that will save hours of work.
[10:55] Because important tip, the shortcuts used for 3D modeling can also work to edit your 2D drawings.
[11:02] I will give an example in the tips section later. But let's go back to the objects in the scene now.
[11:09] This teapot was modeled from a basic 3D cylinder and to give this stylized aspect, I created my own cell shader or tune shader if you prefer that other name.
[11:22] This shader applies a custom color gradient on the object's surface, depending on where the lights fall.
[11:29] The gradient has sharp step transitions and I've placed my colors in each step of the gradient.
[11:37] The object is globally colored in shades of blue and depending on the lights around, the brightest parts are turned into yellow or pink.
[11:47] It could be any other color, these are just my usual colors.
[11:52] There are many tutorials about how to create your own tune shader in Blender.
[11:57] It involves some nodes and I know nodes seem scary the first time you see them, but it's actually easy to understand and to manipulate.
[12:07] Around the object, there is this outline that I created using the Solidify modifier.
[12:13] Basically, this modifier duplicates the object on top of itself at a slightly bigger scale.
[12:19] I just invert the polygons on that copy and I apply a dark texture on it. And this makes this outline effect.
[12:27] Some people call this technique the inverted hula or inverted normals method. I don't really know if it has a name.
[12:36] There are other ways in Blender to add outlines on 3D objects, but I like this technique and for the result I am looking for, it's fast and simple.
[12:46] However, there is already another feature called Lineart modifier in Grisbassil and it looks very promising so I will give it a try in my future projects.
[12:57] So that's it for this first presentation video.
[13:01] Yes, everything you see here is just a combination of 3D stuff and Grisbassil stuff and some effects, grids, bones, etc.
[13:11] Nothing else. I will make some other breakdown videos and I hope I'll have time for a more detailed tutorial soon.
[13:18] So I hope you got enough information from this video to start your journey for self-learning this Grisbassil tool.


### 3 Bonus tips for beginners [13:25]
**Transcript (timestamped):**
[13:26] Now before my recommendations, a few more tips.
[13:30] First, I wanted to make an update for my previous Blender tutorial.
[13:34] A year ago I made a tutorial to show how to create a juice box with just one single Grisbassil object.
[13:41] This technique is still relevant but now, as I told you before, I use that technique only for my complex 3D drawings.
[13:49] In that old tutorial, I show people how to draw an object starting from the face, then tweak some options to make the pencil draw on the side and then on the top, etc.
[14:00] All that inside one single Grisbassil object or one canvas if you prefer.
[14:06] But today, if I have to create that same artwork, I would just create one face, I would draw inside, then I would leave the drawing,
[14:15] which means switch to object mode if you already followed that tutorial.
[14:19] And then I would duplicate the whole object, shift it, you know this shortcut, and I would rotate it to the top, then I would draw inside, and then I would do the same for the side.
[14:31] And during all the process, I wouldn't have to switch face options to side or top,
[14:38] because all the objects now just have one face, the front face.
[14:43] I would just have to jump from one Grisbassil object to another and always draw on the front for each.
[14:51] Second tip, remember, it's important to also learn the basics of 3D modeling, at least for the key shortcuts.
[14:59] Let's see one crucial shortcut for example.
[15:02] This is a shortcut that any blender user must know.
[15:06] Suppose you have a drawing placed like this in space.
[15:10] Suppose you want to adjust the strokes inside this drawing.
[15:14] You go to edit mode, and when you try to move the lines, you see that it's impossible to keep the strokes in the same plane as the rest of the drawing,
[15:26] because the canvas is not aligned to the orthogonal axis anymore.
[15:30] So, if you grab the lines with the GK and press X, your lines are moving on the X axis of the scene.
[15:40] But if you press G, then X twice, the lines move along the X axis relative to your canvas.
[15:48] And this works for the Y and Z keys too.
[15:52] Y once, Y twice, Z once, Z twice.
[15:55] This is just one of the most basic shortcuts, and there are many more that you need to discover out there.
[16:01] They are all in the tutorials about 3D modeling with Blender for beginners.
[16:07] Last tip, in the interface, this record button.
[16:11] It is the auto-caging button, and I think it is enabled by default now when you start a project with a 2D animation template.
[16:19] With this button enabled, when you move in the timeline and start to draw, it creates new keyframes automatically.
[16:27] And that's great, but beware, this option also works for the 3D objects, so whatever you do in the scene.
[16:35] If you change the position of an object, a drawing, a camera or anything, the changes you make are going to be saved as an animation,
[16:43] so you are going to be surprised to see your stuff moving once you press the play button.
[16:49] So I try to enable this button only when I am drawing my 2D keyframes, or when I am animating one specific object,
[16:58] and I try to not forget to disable it immediately when I am done.
[17:03] Ok, thanks for watching, and also thanks for watching my own tutorial.


### Other tutorials, artists showcase and thanks [17:05]
**Transcript (timestamped):**
[17:18] There are people that are still learning with it now, and I am very happy to read the nice comments on that tutorial.
[17:25] If you like my work and want to support me, you can like and subscribe, or you can also give a tip on my tp page.
[17:35] Your support helps me to work on personal artworks and develop new things when I am not working on client works and commissions.
[17:45] And in return you get some goodies, wallpapers and new things that are coming soon.
[17:51] Stay tuned on my social media for the news.
[17:56] And now here are my recommendations for artworks and tutorials made by awesome artists which use RISP Brazil.
[18:04] Don't hesitate to check their contents and leave some nice comments.
[18:09] Stay safe and have a nice day!
[18:21] Thank you for watching!



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
