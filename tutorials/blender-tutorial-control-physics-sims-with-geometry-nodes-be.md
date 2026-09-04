---
title: Blender Tutorial - Control Physics Sims with Geometry Nodes (Beginner Friendly)
source: YouTube
url: https://youtu.be/Fec4BhDFBUo
author: Skramble 
ingested: 2026-05-13
blender_version: "4.5"
tags: [geometry-nodes, rigid-body, simulation, animation, procedural, blender-4x, intermediate]
extraction_status: complete
---

# Blender Tutorial - Control Physics Sims with Geometry Nodes (Beginner Friendly)

**Source:** [YouTube](https://youtu.be/Fec4BhDFBUo)
**Author:** Skramble 
**Ingested:** 2026-05-13

---

## Description

Beginner friendly (I hope) tutorial made in Blender 4.5. Take flexible, procedural control of physics sims, never have to worry about start points or keyframe flipping UI nightmares again. Or get weird with it. Merry X-Mess 2025!

Chapters:

00:00 Intro
00:29 Overview
04:10 Chapter 1 - Physics and Collections Setup
13:37 Chapter 2 - Physics Controller Geometry Node

---

## Raw Content (for analysis)

Kind: captions Language: en [music] Here is a standard Blender rigid body physics simulation, and it looks fantastic. I love it. The only thing I don't love about it is how little control I have over when it happens. Yes, if I was certain I wanted my box to collapse on frame 112, I could start the simulation there. But what if I wasn't certain? Stepping back, what if I didn't want to have to be certain? Wouldn't it be convenient, having baked these lovely physics? If I had some kind of non-destructive system that could give me quick and flexible control over the playback so that I could activate it at any point on the timeline at any speed in any direction. Well, I have built that system in geometry nodes. It is the identical physics simulation but the what happens here is we control the playback of it. So let's say I wanted it to start frame 30 and have finished by I don't know frame 100. So I plug in the values, press play, it starts at 30 and it's done by 100. Okay. What if we think I'd like I really like it to start a bit sooner like maybe frame 20. And I want it to go faster. I want it to end faster. So, let's take the end down to 60. There we go. Starts at 20 and it goes faster. What if we wanted to do backwards physics like that? Well, think about it. Backwards physics would just be physics where the start is towards the end and the end is towards the start. So if we just invert these two values, say we start on frame 60, but we end paradoxically on frame 20, then we have backwards physics like that. Now, easily controllable backwards physics. If you have ever tried to do backwards physics by conventional means, you should appreciate how uh how nice this system is by contrast. But really, the fun is only just getting started. Because what if I didn't want to use a global time parameter to control the beginning and end of the simulation? What if I wanted to use something like a local spatial influence? In this case, the box is falling up and down. The physics are going forwards and backwards driven by the proximity of this empty. And this is exactly the same node tree, exactly the same system as the timed one, just with a different controller mechanism. And the system itself, the geometry nodes, is surprisingly lightweight. Let's have a look at it here. Um, yeah, it's not very big. It's not very many nodes. And so it shouldn't take too long um to build and to show you how it works. I won't say it's it's lightweight and it's not many nodes. It's not exactly straightforward. Um nonetheless, I would like to try and make this tutorial beginner friendly. By which I mean I will put screencast keys here so that if a beginner wants to um they can at least uh follow my steps and end up with this uh animation. The explanations might go a little bit over a beginner's head but you know that's life. Let's get started. Okay. in a fresh Blender scene. The first thing I'm going to do is select the light and the camera and get rid of them because they can be annoying and might get in my way. I'm now going to select our default cube. Go into edit mode and move it down by 1 meter so that the origin is now at the top. I'm going to scale this up considerably and then scale it down on the Z because this is going to be our floor and we want we don't want pieces of the cube falling off. We want, you know, too much space. So, let's apply the scale. Um, let's rename it to floor. And while we're doing some housekeeping, let's turn on Well, you don't have to do this. This is personal preference, but I find cavity both can make things really nice and legible. Okay, let's add another cube. This one, let's move up in object mode [clears throat] 1 meter. And because I am superstitious, I'm just going to move this up a tiny tiny bit because I don't want collision problems. Um, let's take our cube. Um, we're going to self fracture this thing to get to get it into fragments. To do that properly, we need to give it some more geometry. So, let's go into edit mode, subdivide it once, twice, three, and four for good luck. And simply because I think it looks cooler um when when fragmented, I am going to rather than have a solid cube, I'm going to have a kind of hollow cube which um use a solidify modifier and I'm going to go into X-ray view so I can see the thickness of the thing and make it a bit thicker. Yeah, something like that should be just fine. out of X-ray view. Go to object down to quick effects to self fracture. If you're a beginner, um you may and you haven't enabled this already, you'll have to go into preferences to enable self fracture. So, hit self fracture. The standard settings should be fine for this. About 100 particles sounds fine. So, hit okay. Let it do its thing. And when it's ready, um, without clicking away from it, um, hit M to move all these pieces into a new collection. And we'll call that collection static. Create again without clicking away. Uh, hit shift D to duplicate all of the pieces. Um, right click to confirm. Hit M again to move them into another new collection. this one called physics. Okay. So, I'm going to uh just for now disable both static and physics. We don't need the original cube anymore. So, let's get rid of it. Now, uh before we move on to the physics, I have to point something out. If you have your own physics system um or your own, you know, your own objects with physics, uh you're going to have to assemble in the same way two identical collections for them. One static with no physics and the other with which will have the physics. And what's critical is not only that they have the same uh contents, but that the contents be in exactly the same order. Um, so when we ran the self fracture, um, it will have made the pieces and then given them an order. And who who the hell knows, uh, what the order is? Um, let's just find out, um, where the first one is. Okay. So, it's down here. So, keep that in mind. We'll unselect and um disable the static, enable the physics, and let's 

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/blender-tutorial-control-physics-sims-with-geometry-nodes-be.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Building a non-destructive Geometry Nodes system in Blender 4.5 that gives flexible, non-linear playback control over baked rigid body physics simulations — allowing start frame, end frame, playback speed, direction reversal, and spatial proximity-based triggering without rebaking.

### Key Steps
1. Create a floor (scaled cube, origin at top) and a test cube; enable cavity shading for legibility.
2. Go into Edit Mode on the cube, subdivide 4 times for more geometry; add a Solidify modifier for a hollow look.
3. Use Quick Effects > Cell Fracture (enable in Preferences first; ~100 particles) to break the cube into fragments.
4. Without clicking away, press M to move all fragments into a new collection named "static".
5. Shift+D to duplicate all fragments; M to move them into a second collection named "physics" — both collections must have identical pieces in the same order.
6. Add Rigid Body physics to the physics collection pieces; bake the simulation.
7. Create a Geometry Nodes modifier on a new controller object; build the playback controller: map a custom start/end frame input to the baked simulation's frame range using a Map Range node.
8. Use the mapped frame value to drive the Evaluate at Frame node (or equivalent) to sample the static collection's transforms at the computed frame.
9. Set piece transforms from the sampled positions/rotations to display the physics at any controllable point in time.
10. For spatial control variant: replace the time parameter with an Empty's proximity distance to drive the physics playback, creating a spatially-triggered simulation.

### Blender Nodes / Settings
- Cell Fracture add-on (Quick Effects > Cell Fracture, ~100 particles)
- Rigid Body physics (baked simulation)
- Collections: "static" (no physics), "physics" (with physics — same order required)
- Geometry Nodes: Map Range node, Evaluate at Frame (or equivalent)
- Instance on Points node (transform sampling)
- Empty object (proximity driver for spatial variant)
- Solidify modifier

### Difficulty
Intermediate

### Blender Version
4.5

### Tags
#geometry-nodes #rigid-body #simulation #animation #procedural #blender-4x #intermediate
