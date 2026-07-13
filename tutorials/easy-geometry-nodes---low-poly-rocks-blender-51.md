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
frame_count: 0
frame_status: pending-selection
---

# Easy Geometry Nodes - Low-poly Rocks Blender 5.1

**Source:** [YouTube](https://www.youtube.com/watch?v=n1_NMIV7A5U)
**Author:** ALL THE WORKS
**Duration:** 11m4s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py easy-geometry-nodes---low-poly-rocks-blender-51 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Bangkok d'Osmila
[0:20] La Sant south
[0:55] Alright, so the easiest and simplest setup in geometry nodes in Blender is to distribute
[1:19] an object or a set of objects onto other objects and then we can control the scale, position and rotation
[1:29] of those instances. So let's start with this. Okay, so here I have created three basic low poly rock
[1:39] shapes. I used a traditional modeling setup for this. So let's say I start with a cube.
[1:50] And in edit mode, we can use bicec tool to carve out the edges. So you can just drag and select
[2:04] and then in the options you can select fill and clear. That will give you a curved shape.
[2:19] So I have created three of these and I have put those in separate collection. Now let's create
[2:26] a geometry node setup. So I'll take a plane, go to geometry node editor, create a new geometry node.
[2:37] In here, we will drag our rock corner collection. I'll select relative, separate children and
[2:46] reset children. Now press shift A and search for distribute points on faces.
[2:56] Plug the geometry to mesh.
[3:01] Now search instance on point. Plug the points. Plug the collection to instance and select
[3:13] pick instance. Finally, let the instance to geometry output. And here is our rocks distributed on
[3:22] that plane. Now in the distribute node, you can select poison disk. This gives you some more
[3:28] options like distance minimum, which is the distance between the center of these objects,
[3:35] a density maximum and a density factor. Now we can align the instances normal to the surface
[3:44] for that we need a line rotation to vector node. You can plug the normal to vector
[3:53] and output of this to rotation. You can select any axis you want.
[4:01] For now, I'll keep it on Z. Now let's add a random value node.
[4:08] Keep the minimum value to 1 and max to 1.5 and plug it to scale. Now we can keep adding values
[4:18] to the same instance on point nodes or we can add more nodes just for the scaling and rotation
[4:25] of the instances. So let's start with scale instances.
[4:34] I will duplicate the random value node and I will set it to vector.
[4:41] I'll start with setting all the values to 1 and let's plug it to scale.
[4:48] Now I only want to change the Z scale value. So I'll set this max Z to somewhere around 2.2
[4:58] and the min somewhere around 0.2. So now there is a good variation in the scale.
[5:08] Now let's add a rotate instance. Let's copy our random value node again
[5:16] and plug this to rotation. For x and y, I'll keep it at 0 and for Z, I will increase it.
[5:30] So this is our basic setup. Now if you change the base shape which was a plane,
[5:38] it will automatically spawn the instances onto the faces.
[5:46] And you can procedurally change any of these settings. So let's say the alignment if I change to x
[5:57] and I can keep adding the shape.
[6:05] Okay, here is another example of the same node setup. This time I have used this type of
[6:12] low poly rock shape. Now let me edit the shape and show you it's a simple cube.
[6:20] Let me scale it on the base. So right now you can see the points are being
[6:29] instant on each surface of this cube. Now we can control this with the help of normal.
[6:36] So let's add a normal node and let's add a separate xyZ node. Let's plug the normal to vector.
[6:52] Now we want to check the Z normal of each of the face of this cube and remove the points from
[6:59] top and bottom faces. So for that we will take the Z output and let's add a math node.
[7:09] Set it to compare and plug this to selection of the distribute node.
[7:18] Now for seeing the output of any node, you can press control shift and click.
[7:23] So we can see how the points are being distributed. Now right now it's comparing the Z value
[7:31] with the value of 0.5. However the vertical faces have the Z value for normal at 0. So let's change
[7:41] this value to 0 and now we only have the points on the vertical faces. Now this epsilon value
[7:51] controls how much of the Z normal value can deviate from this 0. So let me remove this viewer node
[7:59] and if I edit the cube, let's say I change the angle of this face from vertical, you can see the
[8:10] instances follow up to a certain angle and then they get removed.
[8:15] So in this way we can control the distribution onto our geometry.
[8:24] Okay so here is the final setup for this rock shape. So you can see it's almost same. So I have
[8:32] joined the basic shape which is these cubes into the main geometry and I have also edited this
[8:42] realize instance node. Now anytime you want any of these values to appear in your properties bar
[8:50] right here, you can just drag select and plug it into your grip input node and it will appear here.
[9:00] You can go to this sidebar and rename your property and directly change it from here.
[9:06] Now further I have added some more modifiers. So this remesh and decimate. Now let me show you what it does.
[9:16] If I just remove these right now this shape is just overlapping objects on top of each other.
[9:25] So to get one combined shape I have added the remesh and then to reduce the poly count I have
[9:32] added the decimate modifier. So this makes it one individual shape and finally I have also added
[9:41] this small UV unwrap geometry node modifier. In this I have simply used the UV unwrap node to get
[9:49] the UVs for the combined shape and just for fun I have added this proximity setup to get this
[9:56] merging kind of effect with the ground. Now here is another example where the distribution is the
[10:04] same but the input is a curve. So you can see the input geometry is curve and I have simply converted
[10:13] this curve to a mesh like this with this simple curve circle and again the same setup to instance
[10:22] these objects. Alright so this is how we can create a simple geometry node setup for these low
[10:30] poly rocks. You can download this blender file freely. I'll put the link in the description
[10:37] and you can check out these node setups. So right here we have these three rocks setup.
[10:44] You can just select any one of this and start editing.
[10:52] All the materials in this blender file are from Blenderkit free assets. I'll see you in the next
[11:00] video. Thank you so much. Bye bye.



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
