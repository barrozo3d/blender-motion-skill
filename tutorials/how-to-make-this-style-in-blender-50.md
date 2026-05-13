---
title: How To Make This Style in Blender 5.0
source: YouTube
url: https://youtu.be/rbPOL9ibooY
author: Ducky 3D
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# How To Make This Style in Blender 5.0

**Source:** [YouTube](https://youtu.be/rbPOL9ibooY)
**Author:** Ducky 3D
**Ingested:** 2026-05-13

---

## Description

In this Blender 5.0 motion graphics tutorial we will be using a stack of curves we made in geometry nodes, adding a randomized wave texture to it, and making a beautiful animation loop! 
#blender #geometrynodes #motiongraphics 
Thank you Bad Normals for letting me use your title! 
----------------------------------
Patreon - https://patreon.com/user?u=9011118&utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=creatorshare_creator&utm_content=join_link
------------------------------------

---

## Raw Content (for analysis)

Kind: captions Language: en How's it going guys? So, in today's tutorial, we are going to be making this animation. If you're not super comfortable with geometry nodes, don't worry. It's not a very big tree to make something really cool like this. First thing we're going to do is make a big stack of curves. Then, immediately, we're going to hop into the shading workspace where everything else is going to happen. So, we're going to use a wave texture for the movement. We're going to randomize the position of the wave texture to get this really beautiful movement. Then, using noise textures, we're going to add some really cool color. And then we're going to add some compositing to polish it off. If you want to check out the project file that is available currently on Patreon and this month I added a bunch of really cool tutorials that I personally just had a lot of fun working on. They're a little bit different than what I normally do and they're just really cool. I'm working on a bigger video for here on YouTube, but for now all of those tutorials are available exclusively on Patreon. You can get everything. So check that out linked in the description. And with that being said, let's get into this tutorial. All right. So, we are going to be using Blender 5.0. There's really only one thing that we're doing that is kind of very specific to 5.0. Um, and that's not really super important. So, let's go ahead. I'm hit shift A and we're going to get a plane. And I'm going to head right into geometry nodes to get this started. I'm going to click new and we're going to delete the input. And we're going to get in a mesh line. Grab the mesh line and plug that right into geometry. Now we have a line of a count of 10, which means there's 10 spots to add a curve. So what we're going to do, we're going to get an instance on points. So we can add things to those points. And we're going to get a we're going to get a curve circle. Very important that it's a curve circle, not a mesh circle. Um, and then we're going to plug curve right into instance. There we go. We have all 10 of our curves. I'm going to give I'm going to give myself a radius of seven. And then I'm going to give myself a resolution of 80. Now, we need to bring these down. They're too spaced out. So, what we can do is right here on the Z, give it 07. Those are my exact settings on my uh my scene. And then I'll give myself 120 of these curves. So, now we have something pretty cool ready to go. Let's go ahead and get our camera set up. So, first here in geometry nodes, I'm going to bring this guy kind of to the middle. I'm going to hit tab. I'm going to hit the tilda key and go to the front. Uh, if you didn't know, wherever your viewport is facing, when you add a camera, that's where that camera is going to be facing. So, we can, uh, cut out a little extra work and just get it looking where we want. So, I'm going to click on the camera, and then I'm going to hit zero to go to the camera view. Before we move it, let's go ahead click on the camera in the outliner and go to the camera settings over here. Make your focal length eight. It's an we're making an extremely wide uh, very unrealistically wide uh, camera angle. And that's how we get this really cool uh super wide effect. Now I'm going to hit the I'm click on the camera, hit G and middle click and we're going to go right where we pass up this outer ring. So right here. So we want to just pass up so we get this really really cool effect. That's the whole point. Um we have this set up and ready to go. We just need a few nodes to make the shading uh work for us a little bit easier. We're going to be using a wave texture to go in circles around these curves. So, we need to set up an attribute so that it'll map to these curves uh easily. So, what we're going to do is get a store named attribute. We need to get a spline parameter node and just plug [snorts] factor into value and name it whatever you want. I'm going to just do S for spline. Now, we need to add some geometry to these curves. So, we're going to get a curve to mesh. And then we're going to get a curve circle. I'm going to give my radius. 0.5. I think that was my original settings. And then a resolution of probably three just to make it lighter on your computer. Plug curve into profile curve. So now if we zoom in, we actually have some geometry that a material will be able to sit on. Last thing I need to do is I need some randomness to get the wave texture to randomly place on these curves. So, we're going to get one more store named attribute. I'm going to set this over. I want it to recognize that there are instances. Randomize the curve per instance. And then we're going to get a random value node and plug value into value. And then I'm just going to call it R for random. Again, call it whatever you want. All we need to do now is set up a material. So, I'm going to get a set material node right over here to the right in the material section. I'm going to click new where it says principle and I'm going to switch it over to emission. And then I'm going to place that over here. So, before we head into shading, let's go here to the render settings. I'm going to switch over to Eevee. If I click on the render, you can see the emission is working. And I'm going to get my world brightness here down to black. All right. Now, we can head into shading. So, I'm going to click on the shading workspace. We can see here's our tube. So, I'm going to go here to the official render view. And what I'm going to do here on the emission is just bring up the brightness. That'll make the curves look a little thicker. Uh the brighter these curves, the thicker they will uh look. So now what we can do is add in our wave texture. So hit shift a wabbe wave texture. I'm going hit in and remove that. Then what we can do first, I'm going to get in a mix color node. plug that here and make the top one black and the bottom one pure white. And then we're going to g

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/how-to-make-this-style-in-blender-50.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
[To be extracted]

### Key Steps
[To be extracted]

### Blender Nodes / Settings
[To be extracted]

### Difficulty
[Beginner / Intermediate / Advanced]

### Tags
[To be added]
