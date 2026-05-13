---
title: Superhero Landing Tutorial 02 | Ground Destruction VFX in Blender
source: YouTube
url: https://youtu.be/4ULxB4PzbAc
author: Graphical Ninja
ingested: 2026-05-13
blender_version: Not specified
tags: [rigid-body, simulation, particles, smoke-fire, animation, rendering, compositing, advanced]
---

# Superhero Landing Tutorial 02 | Ground Destruction VFX in Blender

**Source:** [YouTube](https://youtu.be/4ULxB4PzbAc)
**Author:** Graphical Ninja
**Ingested:** 2026-05-13

---

## Description

How to do a superhero landing with no knee pain - featuring Blender and Nuke. You'll learn how to do a ground break using rigid bodies, particles, and a smoke sim.

Gumroad source files download: https://graphicalninja.gumroad.com/l/riitz

Auto Path addon Download: https://graphicalninja.gumroad.com/l/ojule
Auto Path Addon Video: https://www.youtube.com/watch?v=LhzuyNLmDHM&t=4s
Instagram: @graphicalninja

Kamden suit 3D model by Mindfront (Blendswap)
Music: Bensound.com

TIMESTAMPS
00:00 Intro
0

---

## Raw Content (for analysis)

Kind: captions Language: en foreign [Music] [Applause] welcome to part two of my superhero Landing tutorial in this part I'll show you how to do the groundbreak effects with a rigid body simulation add some extra Rock chunks with particle system and add a smoke SIM for dust trails let's get into it first I'm going to add another plane and scale it up then I'm going to move it up about five or six inches and this will be our road surface now I'm going to cut out a smaller Chunk in the middle for the part of the ground that's going to break so if we tap it in edit mode do a couple cuts here and then make that about so and just make sure that he's centered in there now we're just going to select this Center face hit p and separate by selection this will be the part that breaks let's move it into a new collection called ground break and then we need to add some more geometry to this so let's tap into edit mode Ctrl R and then we will cut it into smaller chunks somewhere around here looks good and then we'll cut it the other way to get some Square chunks and then I just want to grab random faces and move them around so these aren't all even just don't move the edge faces now that we've somewhat randomized this let's select the whole thing and then extrude it downwards to the actual ground plane and now we have some geometry to work with I want to hide everything except this for now we'll call this fracture and then we're going to start fracturing this so search fracture and you'll find a cell fracture then we're going to use the point source where we own verts and we will add a recursive fracture of two cursor close we should be good to go now let's just watch this fracture and watch it recursively fracture the center ones let's just drop these into our groundbreak collection and our first fracture object we can delete next let's do a rigid body simulation to make these chunks fly upward and outward as he lands we want to speed ramp it so it ends up being slow-mo in the end so let's add a force field Force and move it a bit below the ground now select one of these chunks turn it into a rigid body it'll be active dynamic and then we'll select all of our groundbreak objects go to object rigid body copy from active and now they will all have the same settings now let's go to the scene properties tab rigid body world and set this up first we need more steps per frame for higher quality so we'll do 20 and 20. and then we're going to go into cash and our simulation start should be 50 and the end should be 100. now we want to speed ramp the speed of the simulation so if we go to like frame three hit ion speed and then go three frames forward and set speed to 0.25 hit I again now for the rest of the Sim it'll be quarter speed now our chunks are all just falling through the ground right now so if we grab our original ground mesh let's make that a rigid body passive object now we need the force to be a little bit stronger well a lot stronger so let's find the the frame on which he lands which is frame 50. and on this Frame we want the strength to be way higher so let's try like 100 000. is that a keyframe on there and then we'll see what that does whoa that did a lot and we want this Force to only happen for like two frames so on frame 52 let's make the strength to zero and then we'll see how that works too much let's make the strength ten thousand that's better and we want some fall off so the outer pieces don't get thrown as far we can do that with this fall off option if we turn the power to one that'll give us a lot more fall off around the edges and that's starting to look a lot cooler we've got this one chunk that's flying right up in front of the camera camera and we can just go ahead and delete some of these so let's delete any chunks that might fly in front of the camera next let's do the particle system to add a bunch of little rocks or dirt to Trail Behind These chunks so select one of your chunks go to the particle settings and make a new particle system we will call it dirt dirt chunks I'll make the number two thousand frame star will be 50 frame end will be 200 lifetime will be 50 and then let's go to rotation we want to turn on rotation so it'll randomly rotate and then turn angular velocity to random and make the amount five we'll make the phase one on all of these so it'll randomly rotate them at the start and then randomize phase just turn that up and then turn randomize up as well all right let's set up our physics settings we want to have a little bit of random motion which would be Brownian so let's turn that to 0.1 and we'll turn damping to 0.05 we don't want the force to affect it so let's turn all and force to zero let's turn gravity to .05 so they sort of just hang in the air now let's see um what this is gonna do as you can see there's a bunch of particles coming off make a new collection call it rocks make sure that's active and then in bridge I'm just going to grab this small stones pack it exports and it should put it into that collection now let's go to these rocks they're they're a little higher poly than I would want so let's select them all go to the modifiers Tab and add a decimate modifier ratio to 0.1 and then we'll just copy to selected and then we will apply this modifier let's go into our particle system settings and where it says render instead of Halo make it collection and select your rocks collection pick random and as you can see it's also scattering a bunch of of uh random empties because they're all parented to this empty empty so just select your rocks alt P clear and keep transformation and then delete this empty let's make them a little bit bigger scale 0.05 maybe 0.1 and then scale randomness like 0.8 maybe they can be like 0.2 one thing I want to turn off is the normal velocity so if we go up to velocity turn normal to zero because it's spraying the rocks out and then we want our object velocity we want to inherit the object's motion so turn the object

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/superhero-landing-tutorial-02-ground-destruction-vfx-in-blen.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Creating superhero ground-destruction VFX in Blender combining Cell Fracture rigid body simulation (with a Force Field strength keyframed at the landing moment), a particle system for flying debris chunks, and a smoke simulation for dust trails — with speed ramping for slow-motion effect.

### Key Steps
1. Add a road surface plane; cut out a center section (Tab > Edit Mode > Loop Cuts); P > Separate by Selection for the breakable chunk; move to "groundbreak" collection.
2. Add more geometry to the chunk (Ctrl+R loop cuts); extrude downward to meet the ground plane.
3. Cell Fracture: search for Cell Fracture add-on; use Point Source: Own Verts; Recursive Fracture: 2; execute to shatter the chunk into pieces.
4. Set up rigid body simulation: add Force Field (Force type) below the ground; select one chunk > Rigid Body > Active Dynamic; then select all groundbreak objects > Object > Rigid Body > Copy from Active.
5. Rigid Body World settings: Steps Per Frame: 20, Substeps: 20; Cache Start: 50, End: 100 (landing frame = 50).
6. Speed ramp: at frame 3, I key on Speed = 1.0; at frame 6, I key Speed = 0.25 for slow-motion after landing.
7. Make ground plane a Passive Rigid Body for collision; keyframe Force Field Strength: at frame 50 = 10,000; frame 52 = 0; Fall Off Power: 1 for edge falloff.
8. Particle system for debris: select a chunk > Particle Properties > New; Count: 2,000; Start: 50, End: 200, Lifetime: 50; Rotation: on, Angular Velocity: Random, Amount: 5; Randomize Phase: on; Physics: Brownian: 0.1, Damping: 0.05, Gravity: 0.05; Force: all off.
9. Create a rocks Collection; import small stones pack; add Decimate modifier (Ratio: 0.1); Apply to all rocks; Particle Render Mode: Collection; Pick Random: on; Scale: 0.1–0.2, Scale Randomness: 0.8; Normal Velocity: 0, Object Velocity: inherit.
10. Add a Smoke Simulation for dust trails: smoke domain cube over the breakable area; smoke flow from the breaking ground; render with Cycles for volumetric smoke.

### Blender Nodes / Settings
- Cell Fracture add-on (Point Source: Own Verts, Recursive: 2)
- Rigid Body: Active Dynamic (chunks), Passive (ground)
- Rigid Body World: Steps: 20, Substeps: 20, Cache: frame 50–100
- Force Field (Force type): Strength keyframed (0 → 10,000 at frame 50 → 0 at frame 52)
- Fall Off Power: 1 (edge falloff)
- Speed keyframes: frame 3 = 1.0, frame 6 = 0.25 (slow-motion)
- Particle System: Count: 2000, Rotation, Angular Velocity: Random
- Particle Render: Collection (rocks), Pick Random
- Decimate modifier (Ratio: 0.1) on rock models
- Smoke Simulation (fluid domain + flow)

### Difficulty
Advanced

### Blender Version
Not specified

### Tags
#rigid-body #simulation #particles #smoke-fire #animation #rendering #compositing #advanced
