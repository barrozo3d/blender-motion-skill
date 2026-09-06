---
title: Make THIS Blender Particle Effect With Just 2 Objects
source: YouTube
url: https://www.youtube.com/watch?v=YZYXQSFwJEY
author: Aria Faith Jones
ingested: 2026-09-06
blender_version: "Blender 5.2.0 -- observed in frame_000"
tags: [geometry-nodes, simulation, particles, procedural, motion-design, abstract, intermediate, blender-5x]
extraction_status: complete
frames_dir: tutorials/frames/make-this-blender-particle-effect-with-just-2-objects/
frame_count: 8
frame_status: complete
uncertainty_frames: []
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Make THIS Blender Particle Effect With Just 2 Objects

**Source:** [YouTube](https://www.youtube.com/watch?v=YZYXQSFwJEY)
**Author:** Aria Faith Jones
**Duration:** 7m8s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


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

## Captured Frames

- [0:40] tutorials/frames/make-this-blender-particle-effect-with-just-2-objects/frame_000.jpg
- [0:53] tutorials/frames/make-this-blender-particle-effect-with-just-2-objects/frame_001.jpg
- [1:58] tutorials/frames/make-this-blender-particle-effect-with-just-2-objects/frame_002.jpg
- [3:20] tutorials/frames/make-this-blender-particle-effect-with-just-2-objects/frame_003.jpg
- [4:16] tutorials/frames/make-this-blender-particle-effect-with-just-2-objects/frame_004.jpg
- [5:10] tutorials/frames/make-this-blender-particle-effect-with-just-2-objects/frame_005.jpg
- [5:46] tutorials/frames/make-this-blender-particle-effect-with-just-2-objects/frame_006.jpg
- [6:42] tutorials/frames/make-this-blender-particle-effect-with-just-2-objects/frame_007.jpg

---

## Structured Notes

### Core Technique
A geometry-nodes simulation zone that emits points with Distribute Points on Faces and pushes them outward using a **Geometry Proximity** node measured against a second, smaller object -- a two-object substitute for writing the outward vector in pure math -- with every force scaled by Delta Time and a stored `life` attribute driving both culling and radius falloff.

### Summary
Two icospheres, one scaled to 0.5, are all the geometry this effect needs: the small one is never rendered, it only serves as the thing points are pushed *away from*. Points are distributed on the large sphere's faces, accumulated inside a simulation zone, and offset each step by the Geometry Proximity position vector, so they travel radially outward without any vector math. A noise texture recentred by subtracting 0.5 adds organic drift, and a hand-rolled `life` counter (Named Attribute + Math Add 1) gives the points an age that a Compare node uses to delete them and a Map Range + Float Curve uses to shrink them.

### Key Steps
1. Add an icosphere, `Shift D` to duplicate, `S` `0.5` to scale the copy -- the small copy is the push object. With the **original** selected, open the Geometry Nodes workspace and click New, then drag the duplicate into the node tree, which creates an **Object Info** node [frame_000] [transcript 0:15-0:35]. *(Whisper renders "into the node tree" as "in Tornow Tree" -- the frame settles it.)*
2. `Shift A` -> **Distribute Points on Faces**, left on its defaults: distribution **Random**, **Density 10.000**, **Seed 0** [frame_001].
3. Add a **Simulation Zone** and put a **Join Geometry** inside it feeding Simulation Output -> Group Output. Nothing appears to happen on playback, but the Spreadsheet shows the point count climbing every frame -- they are stacking in place [transcript 1:00-1:21].
4. Add **Set Position** inside the zone. An Offset of 0.1 proves the mechanism but only pushes up the Z axis [transcript 1:21-1:32].
5. Add **Geometry Proximity**, feed the Object Info geometry into its Target (Target Element **Faces**), and wire its **Position** output into Set Position's **Offset** [frame_002]. Object Info's **Original** mode works only while the object sits at the world origin; switch it to **Relative** if the object will ever move -- the frame at 1:58 shows Relative selected [frame_002] [transcript 1:45-1:56].
6. The particles jump outward the instant the force is connected, because the offset is applied *per frame* and frame 1 already counts [transcript 2:26-2:41]. Fix it with a **Vector Math -> Scale**: force into Vector, the Simulation Input's **Delta Time** into Scale [frame_003]. The motion becomes one unit per *second*, so the same distance now takes 24 frames [transcript 3:09-3:32].
7. For organic drift, add a second **Set Position** driven by a **Noise Texture**. Its Color output is all-positive, so every point drifts into +X/+Y/+Z; a **Vector Math -> Subtract** with **0.500 / 0.500 / 0.500** recentres it [frame_004] [transcript 3:50-4:14]. Scale this force by Delta Time as well, then set the noise to **4D** and drive **W** from a **Scene Time** node through a **Multiply** to slow the evolution [transcript 4:20-4:37].
8. There is no age attribute to work with, so build one: **Store Named Attribute** named `life`, fed by a **Named Attribute** (`life`) into a **Math -> Add** of **1.000**, inside the zone. Each point's value now climbs by one per frame -- visible as a new `life` column in the Spreadsheet [frame_005] [transcript 4:44-5:14].
9. Cull with **Delete Geometry** (domain **Point**, mode **All**) gated by a **Compare -> Greater Than** with **B = 75.000** [frame_006]. Replace that constant with a **Random Value** node (**Min 75.000, Max 100.000**) so the deaths stagger instead of happening in one wave [frame_006] [transcript 5:25-5:56].
10. Shrink points as they age with **Set Point Radius** driven by a **Float Curve**. The curve expects 0-1 but `life` runs to 100, so add a second Store Named Attribute -- the Spreadsheet column reads **`lifescale`**, one word, though the narration says "life scale" [frame_007] -- fed by a **Map Range** whose **From Max** is the Random Value output, normalising each point's own lifespan to 0-1 [frame_007] [transcript 6:02-6:47].

### Nodes / Settings
| Node | Setting | Value | Source |
|---|---|---|---|
| Distribute Points on Faces | Distribution / Density / Seed | Random / **10.000** / **0** | [frame_001] |
| Object Info | Transform Space | **Original**, switched to **Relative** once the object may move | [frame_001] [frame_002] |
| Geometry Proximity | Target Element | **Faces** | [frame_002] |
| Simulation Input | Delta Time | drives Vector Math -> Scale | [frame_003] |
| Vector Math (force scale) | Operation | **Scale** | [frame_003] |
| Noise Texture | Dimensions / Scale / Detail / Roughness / Lacunarity / Normalize | 3D->**4D** / **5.000** / **2.000** / **0.500** / **2.000** / on | [frame_004] |
| Vector Math (recentre) | Subtract | **0.500, 0.500, 0.500** | [frame_004] |
| Math (age counter) | Add | **1.000** | [frame_005] |
| Store Named Attribute | Name / Type / Domain | `life` -- Float, Point | [frame_005] |
| Compare | Operation / B | **Greater Than** / **75.000** | [frame_006] |
| Random Value | Min / Max | **75.000** / **100.000** | [frame_006] |
| Delete Geometry | Domain / Mode | **Point** / **All** | [frame_006] |
| Store Named Attribute (2) | Name | **`lifescale`** (narration says "life scale") | [frame_007] |
| Map Range | From Max | the Random Value output, so 0-`life` maps to 0-1 | [frame_007] |
| Set Point Radius | Radius | driven by a **Float Curve** on `lifescale` | [frame_007] |

### Difficulty
Intermediate

### Blender Version
Blender 5.2.0 -- read from the status bar in [frame_000]; the transcript never states a version.

### Tags
geometry-nodes, simulation, particles, procedural, motion-design, abstract, intermediate, blender-5x

---

## Related Tutorials
- `tutorials/blender-50-particle-attraction-and-follow-surface-motion.md` -- the same simulation-zone-plus-proximity family, solving the opposite problem (attraction to a surface rather than repulsion from an object); shares tags: geometry-nodes, simulation, particles, procedural.
- `tutorials/sand-simulation---blender-tutorial-nexus.md` -- points in a simulation zone with a per-point stored attribute driving behaviour, at much higher counts; shares tags: geometry-nodes, simulation, particles, procedural, abstract.
- `tutorials/я-сделал-инструмент-которого-мне-не-хватало-в-blender.md` -- a simulation-zone point system wrapped into a reusable node tool; shares tags: geometry-nodes, simulation, particles, procedural, abstract.
- `tutorials/blender-sound-reactive-geometry-nodes-tutorial-how-to-audio-music-simulation-mog.md` -- the same Store Named Attribute -> shader-side read pattern, driven by audio instead of age; shares tags: geometry-nodes, simulation, particles, procedural, abstract.
