---
title: Glass Cell Division Effect in Blender 5.0 (tutorial)
source: YouTube
url: https://youtu.be/XOLuYDLYEgI
author: Ducky 3D
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# Glass Cell Division Effect in Blender 5.0 (tutorial)

**Source:** [YouTube](https://youtu.be/XOLuYDLYEgI)
**Author:** Ducky 3D
**Ingested:** 2026-05-13

---

## Description

In this Blender 5.0 tutorial we will be using the new Blender SDF Grid nodes to make a cell division effect. We will be making a beautiful GRB glass dispersion  material and adding that to the animation. Enjoy! 
#blender #geometrynodes #blender5.0 
----------------------------------
Patreon - https://patreon.com/user?u=9011118&utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=creatorshare_creator&utm_content=join_link
-----------------------------------------------
🌐 Connect with me:
- 

---

## Raw Content (for analysis)

Kind: captions Language: en How's it going, guys? In this tutorial, we're going to be making this animation right here. It is going to be done in Blender 5.0, which is in beta. So, you'll need to go to blender.org and check out the daily builds and get the beta. Uh, otherwise, you're probably watching this in a later time and it's already out and normal and you already have it. This is a really cool tutorial cuz we're going to be remaking kind of traditional Metabol uh movements and behaviors, which is kind of the whole point and the thing that got me really excited about this. So, I am going to show you how to create those metabol actions, how to fix geometry problems that you might run into. And at the very end, uh, we're going to make a really beautiful background and some glass dispersion and show you some cool stuff with that. I had a lot of fun this month on Patreon playing with these metabols and showing you different ways you can style them and make them look really cool. So, if you want to check out those four exclusive tutorials on Patreon, that is linked in the description and you get a discount if you subscribe annually. With that being said, let's get into this tutorial. So, open up a just totally empty document in Blender 5.0. And I'm going to go here to the geometry nodes window and make my own [clears throat] custom window situation here. Just throw in any piece of geometry and then click uh new up here and delete delete the input. And we're going to pick an object that uh just pick a just pick an icosphere. I'm It's the morning so I can't explain what I'm thinking. So take an icosphere. Uh this is the shape that the uh spheres the metabols are going to exist within. So you have to start with a shape uh in order to put things within the volume of that shape. So we're going to start with here and we're going to do a mesh to volume node. And that's going to allow us to then do a distribute points within the volume. So distribute points in volume. Now we have points. So this is the spot where we uh get ourselves the ability to animate and move the points around with a set position. So all this stuff is not 5.0 relevant. Like you can do this anywhere. All this stuff is sort of stable stuff. So now we'll get in a noise texture and then click on the uh color socket and just drag andclick. And I'm going to type in scale vector math because I want to get a vector math scale node. And we'll plug that right at the offset. Uh click normalize. And we're going to switch this over to 4D so that we can animate our points around. So I'm going to take the detail down. Give it a scale of two. Bring the scale up a little bit. And now we have this. And we got a lot of points. We're going to do less of those points. I just want a few. That's probably good. So, now we're going to introduce, if you've never used uh Blender 5.0 yet, we are going to go ahead and get in a points to SDF grid. [snorts] So, points to SDF grid. When we plop that in there, it's going to cut from the output. And that is because this is not compatible with that. So, it's going to cut it. So, we have to convert it back to readable geometry information. That is going to be a grid to mesh. So grid to mesh. It's going to take that grid information we just turned those points into back into geometry. And now we have this. Now back uh the the version of this that I posted 6 months ago. I instanced icospheres on the points that we just created and then I converted those um I converted those new icospheres into a volume and then I converted them back to geometry and I also had to realize the instances. So that's what this takes the place of. It's far easier on your computer. It's way more efficient and it just works better. So there's a lot of great things. Now you can notice this is pretty low poly. So your voxil size is where you are going to get higher poly. So if you bring it to the left, it is going to subdivide it. Um, and now we have this. So if I play with the noise texture, I'm just going to bring it over here so we can see it. If I play with that, you can see now they're all molding into each other. Now there's a lot of issues that we have to now fix. So notice when I move these around, you can see how the geometry is just kind of dancing around. That is again uh because it's low poly. And you'll also notice there's this circular behavior happening uh when we move it around. See that? Notice there's little circles happening. That is going to be incredibly noticeable. See that? That is going to be incredibly noticeable when we add glass to this. Now, if we do like um subsurface materials, other things like that, it'll be less noticeable. I prefer not to dance around problems and try to solve them, which is what has prevented me from making like a perfect metabol geometry notes tutorial, but fear no more. We have every fix. Thanks to everyone on Twitter who helps me out. So, first we're going to get a set shade smooth. Now, that doesn't actually fix anything. It just smooths out the geometry and shows all of our glaring problems. So, a couple things. One, voxil size. Bring it down to like 03. The v better voxil size, the better it's going to be. Higher poly, all that fun stuff. Then [snorts] we're going to get a smooth geometry node. Now, this is a fun node because you can see some stuff under it. If I double click on the node, it is a position node, a blur attribute, and a set position. So, that is an old trick um that they've now turned into this node. I think it's cool that we're double clicking and you can see stuff. So, it's a group node that is automatically available in 5.0. So, if I plop it right here, if I bring up my iterations, it will smooth that out. So, see all this ugliness right here? It will smooth that out. So now when we animate it's not quite as insane. Now you can still see some issues. So let's go ahead and fix those issues. So after the smooth geometry, it still doesn't fix this circular kind of we

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/glass-cell-division-effect-in-blender-50-tutorial.md and extract:
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
