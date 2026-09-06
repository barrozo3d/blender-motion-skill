---
title: Make THIS Blender Particle Effect With Just 2 Objects
source: YouTube
url: https://www.youtube.com/watch?v=YZYXQSFwJEY
author: Aria Faith Jones
ingested: 2026-09-06
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/make-this-blender-particle-effect-with-just-2-objects/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: []
---

# Make THIS Blender Particle Effect With Just 2 Objects

**Source:** [YouTube](https://www.youtube.com/watch?v=YZYXQSFwJEY)
**Author:** Aria Faith Jones
**Duration:** 7m8s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py make-this-blender-particle-effect-with-just-2-objects <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this concept, it was a little bit difficult to understand at first, but being able to visualize
[0:05] it helped me to understand it a lot better. Sometimes when you jump into Blender, it can be
[0:10] really difficult to get started. So in this video, I want to show you how easy it is to get started
[0:15] with just 2 objects and some points. First, add an icosphere to your scene, and then duplicate it
[0:22] with Shift D, hit S to scale, and type in 0.5. Make sure you have the original icosphere selected,
[0:29] and then head over to the geometry nodes workspace and click New. And what we want to do is use the
[0:35] smaller object to push the particles outward. Click and drag the push object in Tornow Tree.
[0:42] Now that we have our basic setup, we need to add our particles, so hit Shift A, and search for
[0:47] Distribute Points on Faces, and add that in. Now that we have our points, we need some way to animate
[0:54] them. And in this case, the simplest way to do that is by adding a simulation zone.
[1:00] Let's add our points into the simulation by using a joined geometry node and connecting our points.
[1:06] And make sure to connect the simulation to the group output. If we hit play, it doesn't look
[1:11] like anything is happening, but if you open up the spreadsheet editor, you'll see that more
[1:16] points are being added to each frame. They're just sitting on top of one another. So the next thing
[1:21] we need to do is to push them outwards. Add a Set Position node, and if I quickly set this to 0.1,
[1:28] you'll see our points are being pushed upwards each frame. But what we actually want is for the
[1:32] points to push outwards in all directions. And you could just do this using pure math,
[1:38] but I think this method will be a lot easier for most non-technical artists, such as myself.
[1:45] Add a geometry proximity node, connect our object to it, and we could just leave this to original,
[1:51] since our object is centered around the world origin. But if you plan to move the object at all,
[1:56] you should set this to relative instead. Now, if we connect the position output of our proximity
[2:01] node to the offset of our set position, you'll notice that our particles jump outward a bit,
[2:06] and if I hit play, you'll see we now have some animation, but it's not really what we want.
[2:12] We need to address why our particles jumped outward when we connected the force to our
[2:16] simulation. I'm going to join our original object at the end so we can visualize it,
[2:21] and you'll see that our particles are sitting on the surface, but as soon as we add our force
[2:26] into the simulation, they jump outward. And the reason this happens is because we're telling
[2:30] Blender that for each frame of the animation, push our particles out by one unit. And since
[2:36] we're on frame one, when we connect our force, Blender immediately pushes them out by that amount.
[2:42] And this concept was a little bit difficult to understand at first, but being able to visualize
[2:47] it helped me to understand it a lot better. When doing a simulation in geometry nodes,
[2:53] something that's very important to consider is delta time. And I won't go too deeply into it,
[2:58] but basically what it does is make sure your simulation relies on real-world seconds to
[3:03] calculate the movement rather than just how many frames have passed. And the way we can utilize it
[3:09] is by scaling our force using delta time. So I'll add a vector math node and set it to scale,
[3:15] connect my force and scale it by delta time. Now instead of telling Blender to move our particles
[3:21] one unit each frame, we're telling Blender to move our particles one unit per second,
[3:26] making our simulation independent of our frame rate, which means our particles take 24 frames
[3:32] to reach the same distance as before. Next, we want to give the simulation some organic movement,
[3:40] so I'll add another set position node and we can use a noise texture for the movement.
[3:44] If we connect the color output directly to the offset, we get something, but it's not what we want.
[3:50] The reason our particles are all moving in one direction is because the noise texture is currently
[3:55] outputting only positive values, which means our particles are getting pushed in the positive
[4:00] x, y and z directions. Instead, we want them to move in all directions, and to do that,
[4:06] we can use a vector math node set to subtract, then set all three values to 0.5. If we hit play again,
[4:14] now our particles are moving evenly around the object, but something still looks a bit off.
[4:20] And just like before, we need to make sure our noise force is also scaled by delta time in order
[4:26] to get the results we're looking for. Then finally, let's make sure we change the texture over time
[4:32] by setting the noise to 4D, connecting a scene time node to the w socket, and slowing it down
[4:37] by using a multiply node. Next, we need to limit how long our particles last for, but if we look
[4:44] at the spreadsheet, there really isn't any attribute we can use to achieve this, so we need to create
[4:49] one, and the easiest way to do that is by using a store named attribute node. You can name it
[4:54] whatever you want, but for now, I'll just name this life. Then we need to add a value that increases
[5:00] each new frame. So I'll add a named attribute node and connect it to the value socket. Then to increase
[5:07] this value each frame, we can use a math node set to add and set its value to 1. Now when we move
[5:14] through the timeline, you'll see each of our particles gets assigned a life value that increases
[5:18] by one each frame. Next, we need to delete any particle that reaches a certain threshold by
[5:25] using a delete geometry node. You'll see it deleted all of our particles, so now we can use our life
[5:31] attribute to specify which particles to keep and which particles to delete. Now to compare node and
[5:37] set it to greater than. Then I'll set the value to 75. Hit play, and now Blender will delete any
[5:44] particle that has existed for more than 75 frames. And I'll make this a bit more natural by adding a
[5:51] random value node, and now we have our basic simulation complete. Now that our base simulation is
[5:57] complete, all we need to do is finalize the look of the simulation. First, I want to scale the particles
[6:02] smaller as they move outward, and to do that, I'm going to add a set point radius node and use a float
[6:08] curve. But you can see when I connect the live attribute to it, it doesn't really work, and
[6:14] that's because the float curve is expecting a value from 0 to 1. And since our life value goes from 0
[6:20] to 100, we'll need to create a new attribute that has a range of 0 to 1. I'll add a second store named
[6:27] attribute node and name it life scale. I'll connect our life attribute to a map range node,
[6:33] then plug our random value node into the from max input, then the map range node will convert all of
[6:40] our values to values between 0 and 1. Finally, we can connect this new attribute to the float curve,
[6:47] and things are working again. If you want to see how I finalized the look of this simulation, you can
[6:52] join my patreon, get this and a few of my most recent blend files all for $5 per month, or just
[6:59] download this blend file directly from my gumroad. And I'll see you soon, okay? Bye!



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
