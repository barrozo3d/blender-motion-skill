---
title: Easy Geometry Nodes - Low-poly Rocks Blender 5.1
source: YouTube
url: https://www.youtube.com/watch?v=n1_NMIV7A5U
author: ALL THE WORKS
ingested: 2026-07-13
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/easy-geometry-nodes---low-poly-rocks-blender-51/
frame_count: 4
---

# Easy Geometry Nodes - Low-poly Rocks Blender 5.1

**Source:** [YouTube](https://www.youtube.com/watch?v=n1_NMIV7A5U)
**Author:** ALL THE WORKS
**Duration:** 11m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Music So, the easiest and simplest setup in geometry nodes in Blender is to distribute an object or a set of objects onto other objects. And then we can control the scale, position and rotation of those instances. So, let's start with this. Okay, so here I have created three basic low poly rock shapes. I used a traditional modeling setup for this. So, let's say I start with a cube. And in edit mode, we can use bicech tool to carve out the edges. So, you can just drag and select. And then in the options, you can select fill and clear. That will give you a curved shape. So, I have created three of these and I have put those in separate collection. Now let's create a geometry node setup. So, I'll take a plane. Go to geometry node editor. Create a new geometry node. In here, we will drag our rock corner collection. I'll select relative, separate children and reset children. Now press shift A and search for distribute points on faces. Plug the geometry to mesh. Now search instance on point. Plug the points. Plug the collection to instance and select pick instance. Finally, plug the instance to geometry output. And here is our rocks distributed on that plane. Now in the distribute node, you can select poison disk. This gives you some more options like distance minimum, which is the distance between the center of these objects, a density maximum and a density factor. Now we can align the instances normal to the surface. For that, we need a line rotation to vector node. You can plug the normal to vector and output of this to rotation. You can select any axis you want. For now, I'll keep it on Z. Now let's add a random value node. Keep the minimum value to 1 and max to 1.5 and plug it to scale. Now we can keep adding values to the same instance on point nodes. Or we can add more nodes just for the scaling and rotation of the instances. So let's start with scale instances. I will duplicate the random value node and I will set it to vector. I'll start with setting all the values to 1 and let's plug it to scale. Now I only want to change the Z scale value. So I'll set this max Z to somewhere around 2.2 and the min somewhere around 0.2. So now there is a good variation in the scale. Now let's add a rotate instance. Let's copy our random value node again and plug this to rotation. For x and y, I'll keep it at 0 and for Z, I will increase it. So this is our basic setup. Now if you change the base shape which was a plane, it will automatically spawn the instances onto the faces. And you can procedurally change any of these settings. So let's say the alignment if I change to x and I can keep adding the shape. Okay, here is another example of the same node setup. This time I have used this type of low poly rock shape. Now let me edit the shape and show you it's a simple cube. Let me scale it on the base. So right now you can see the points are being instant on each surface of this cube. Now we can control this with the help of normal. So let's add a normal node and let's add a separate XYZ node. Let's plug the normal to vector. Now we want to check the Z normal of each of the face of this cube and remove the points from top and bottom faces. So for that, we will take the Z output and let's add a math node. Set it to compare and plug this to selection of the distribute node. Now for seeing the output of any node, you can press control shift and click. So we can see how the points are being distributed. Now right now it's comparing the Z value with the value of 0.5. However, the vertical faces have the Z value for normal at 0. So let's change this value to 0. And now we only have the points on the vertical faces. Now this epsilon value controls how much of the Z normal value can deviate from this 0. So let me remove this viewer node and if I edit the cube, let's say I change the angle of this face from vertical, you can see the instances follow up to a certain angle and then they get removed. So in this way, we can control the distribution onto our geometry. Okay, so here is the final setup for this rock shape. So you can see it's almost same. So I have joined the basic shape, which is these cubes into the main geometry and I have also added this realize instance node. Now anytime you want any of these values to appear in your properties bar right here, you can just drag select and plug it into your grip input node and it will appear here. You can go to this sidebar and rename your property and directly change it from here. Now further, I have added some more modifiers. So this remesh and decimate. Now let me show you what it does. If I just remove these right now, this shape is just overlapping objects on top of each other. So to get one combined shape, I have added the remesh and then to reduce the poly count, I have added the decimate modifier. So this makes it one individual shape. And finally, I have also added this small UV unwrap geometry node modifier. In this, I have simply used the UV unwrap node to get the UVs for the combined shape. And just for fun, I have added this proximity setup to get this merging kind of effect with the ground. Now here is another example where the distribution is the same, but the input is a curve. So you can see the input geometry is curve and I have simply converted this curve to a mesh like this with this simple curve circle. And again, the same setup to instance these objects. All right. So this is how we can create a simple geometry node setup for these low poly rocks. You can download this blender file freely. I'll put the link in the description and you can check out these node setups. So right here, we have these three rocks setup. You can just select any one of this and start editing. All the materials in this blender file are from blender kit free assets. I'll see you in the next video. Thank you so much. Bye bye.

**Frame:** tutorials\frames\easy-geometry-nodes---low-poly-rocks-blender-51\frame_000.jpg
**Frame:** tutorials\frames\easy-geometry-nodes---low-poly-rocks-blender-51\frame_001.jpg
**Frame:** tutorials\frames\easy-geometry-nodes---low-poly-rocks-blender-51\frame_002.jpg
**Frame:** tutorials\frames\easy-geometry-nodes---low-poly-rocks-blender-51\frame_003.jpg


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
