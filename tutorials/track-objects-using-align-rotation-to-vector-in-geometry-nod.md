---
title: Track Objects Using Align Rotation To Vector In Geometry Nodes – Blender Tutorial
source: YouTube
url: https://youtu.be/ZBZ26xQ9Pnk
author: Photini By Design
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# Track Objects Using Align Rotation To Vector In Geometry Nodes – Blender Tutorial

**Source:** [YouTube](https://youtu.be/ZBZ26xQ9Pnk)
**Author:** Photini By Design
**Ingested:** 2026-05-13

---

## Description

Hey folks, in this Blender tutorial I will show you how to track any object using align rotation to vector in geometry nodes. There are many different ways to point an object towards a target object, in this example you will learn a simple but effective method to rotate instances in the direction of a target. This episode also shows you how to set up a simple scale by proximity sub system. As an extra bonus, I have included a free download to a procedural eyeball which you can use in your blende

---

## Raw Content (for analysis)

Kind: captions Language: en Hey folks, in this episode, I'm going to show you how to track any object in geometry nodes using the align rotation to vector node. This technique is useful for various different applications, so it's worth taking the time to learn this method. So, without further ado, let's get to it. So, open up Blender. We're going to go to edit, preferences, and under add-ons, we're going to search for node, and then enable the node wrangler here. Once you've enabled that, we're going to click this button and click save preferences. That will ensure the node wrangler loads every time we load Blender. We'll then close this window here. In my 3D viewport, with the default cube selected, I'm going to hit numpad one to go into front view. I'll then tab into edit mode. I'm going to hit G, Z. I'm going to hold down control to snap it to the grid, and I'm going to bring it up to right about there, just so the base is in line with the origin. I'll then hit S, shift Z, and that will scale it on all axes excluding the Z axis. I'll then hit point one. I'll hit enter. I'll now toggle into X-ray view. I'm going to box select these top vertices here. I'm going to hit G, Z, and I'm going to snap them down to five units. I'll then hit E to extrude, S to scale, and I'll scale it by two. I'll hit enter. I'll then hit E, Z. I'm going to hold down control to snap it to the grid, and I'm going to bring it up to right about there. I'll then hit S, point one, enter. Tab out of edit mode. I'll just toggle off X-ray view. In my outliner, I'm going to rename this object to arrow. I'll then hit G, X. I'm going to hold down control to snap it to the grid, and I'm going to bring it to right about there. I'll then hit shift A. I'll go mesh, and I'm going to choose icosphere. I'll navigate to the icosphere options down in the bottom left. I'll expand these options, and I'm going to increase the subdivisions to three. In the 3D viewport, I'm going to right click and select shade smooth. I'll then tab into edit mode. I'm going to hit S two, enter to scale it up by two. Tab out of edit mode. The idea behind this is we're going to take this arrow and create instances of the arrow on this sphere. We'll then add an empty object into the scene, which will become the target for the arrow instances. So, let's add the empty target object now. So, I'll hit shift A. We'll go empty, and I'll choose sphere. I'll then hit numpad seven to go into top view. I'm going to hit G, Y. I'm going to hold down control to snap it to the grid, and I'm going to bring it to right about there. I'll then navigate to my outliner, and I'll rename this object to target. I'm going to go to my 3D viewport. I'm going to select the icosphere. I'm going to hit numpad one to go into front view. I'll then take my cursor to the bottom left of the 3D viewport until I see a crosshair. I'll left click and drag up and open up a new window. I'll then change this window from the 3D viewport to geometry node editor. In the geometry node editor, I'm going to click new, and I'll rename this to follow target. I'm going to hit N to hide the N panel. The first thing we need to do is distribute points on this icosphere, and then we can create instances on those points. So, I'll take this group input. I'll just drag this over to here for now. I'll hit shift A, and I'm going to search for distribute, and I'll select distribute points on faces, and I'll pop that there. I'm going to change it from random to Poisson disk. I want to see the original geometry, so I'm going to hit shift A and search for join, and we'll choose join geometry, and I'll pop that there. I'll then connect the original geometry from the group input into the join geometry. So, now on each of these points, we want to create an instance of this arrow. So, I'll hit shift A, and I'll search for instance, and we'll choose instance on points, and I'll pop that in between there. And the object we want to instance will be the arrow. So, I'm going to go to my outliner, and I'm just going to drag this arrow into the geometry node window. Maybe I'll give us a bit more room. I'll then connect the geometry socket from the object info into the instance socket of the instance on points node. And now I can dial in the distribute points on faces. So, maybe I can set the distance minimum to 1 m, and I'll set the density max to 200. So, next up, we want all of these arrows to point in the direction of our empty object. To do that, I'm going to hit shift A, and I'm going to search for rotate instances, and I'll pop that after the instance on points node. I'll then go to the outliner, and I'm going to drag that target empty object into the geometry node window. I'll then hit shift A, and I'll search for position, and I'll add a position node here. Shift A, and I'll search for vector maths, and I'll pop that there. I'm going to change it from add to subtract. I'll then take the location socket from the object info, which is our target empty object, and plug it into the top socket of the vector math node. I'll then take the position socket and plug it into the bottom socket of the vector math node. I'll then hit shift A, and I'm going to search for align, and we'll choose align rotation to vector, and I'll pop that there. I'll then connect the vector socket from the vector math node into the vector socket of the align rotation to vector. And now I can take this socket and plug it into the rotation socket of the rotate instances node. I'll just increase the 3D viewport. So, now I can take this empty object here. I can hit G, and you can see that the arrows are pointing in the direction of the target. Excellent. I'll just select the icosphere object. We're going to take this step further. I'll just box select these nodes here. I'm going to hit G. I'll bring these across over to here. I'll then grab this one and bring this over to here. In fact, I'll just bring this down here. For this next part, I want to be able

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/track-objects-using-align-rotation-to-vector-in-geometry-nod.md and extract:
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
