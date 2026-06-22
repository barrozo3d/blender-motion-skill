---
title: NeXus for Blender Official Training - Follow Curve
source: YouTube
url: https://www.youtube.com/watch?v=na6NGPw4XWM
author: INSYDIUM LTD
ingested: 2026-06-22
blender_version: "unspecified (NeXus plugin)"
tags: [particles, simulation, fluid, meshing, motion-blur, intermediate, addon]
extraction_status: complete
frames_dir: tutorials/frames/nexus-for-blender-official-training---follow-curve/
frame_count: 0
---

# NeXus for Blender Official Training - Follow Curve

**Source:** [YouTube](https://www.youtube.com/watch?v=na6NGPw4XWM)
**Author:** INSYDIUM LTD
**Duration:** 25m42s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en Hi, this is Bob from Insidium. In today's video, I'm going to show you how we can set up a particle simulation so it follows the path of scene curves. We're going to do a liquid one in this instance. I'm going to show you some meshing tricks, and then we're going to have a look at applying some motion blur to that mesh at render time to get some pretty nice effects. So, this is what we're going to have a look at recreating. Let's jump into a fresh scene in Blender, and we'll get started. Let's get some particles in the scene, then. So, we'll just add an emitter, and this emitter, we want it to be a sphere emitter. We're going to reduce the radius down to 0.2. We're going to have the direction We want the particles to go downwards, so we're going to do minus Z axis direction. We'll leave it in rate random, but we want a birth rate quite high, maybe 50,000 particles per second. Uh leave speed on default. The radius we're going to put down to 0.01, and then we want our frames uh to be limited. So, let's just put this on 120 frames worth of an emission. So, then we get our particles being emitted. Okay. Now, what we want to do is we want these particles to f...



---

## Structured Notes

### Core Technique
Using the NeXus particle plugin for Blender (by Insydium) to emit a liquid particle stream from a sphere emitter and make it follow the path of a scene curve, then meshing the particles and applying render-time motion blur for a fluid-trail effect.

### Summary
Bob from Insydium demonstrates setting up a particle simulation that follows a curve's path, using a liquid-style emission as the example. A sphere emitter (radius 0.2) emits particles downward (-Z direction) at a high birth rate (~50,000/sec) with a small particle radius (0.01), limited to a 120-frame emission window. The particles are then made to follow a scene curve's path (NeXus's curve-following force/operator). The tutorial continues into meshing the particle stream into a continuous liquid-like surface, and finishes by applying motion blur at render time to the resulting mesh for a more dynamic, fluid look. (Transcript truncated by ingestion at ~1200 characters; the curve-follow setup, meshing node specifics, and motion blur settings beyond this point were not captured and would need a follow-up Whisper pass or manual review of the full video for complete node-level detail.)

### Key Steps
1. [Sphere emitter] Add a particle emitter, set to sphere type, radius 0.2
2. [Direction] Set emission direction to -Z (downward)
3. [Birth rate] Set a high birth rate (~50,000 particles/second) for a dense stream
4. [Particle radius] Reduce particle radius to 0.01 for a fine liquid-like stream
5. [Emission window] Limit emission to 120 frames
6. [Curve follow] Apply a curve-following force/operator so particles travel along a scene curve's path
7. [Meshing] Convert the particle stream into a continuous mesh ("meshing tricks" per the intro)
8. [Render] Apply motion blur to the meshed result at render time for the final effect

### Nodes / Settings
- NeXus sphere emitter — radius, direction, birth rate, particle radius, emission frame range
- Curve-follow force (NeXus) — drives particles along a defined scene curve
- NeXus mesher — converts particle data into a renderable continuous mesh
- Render-time motion blur — applied to the meshed liquid for added dynamism

### Difficulty
Intermediate

### Blender Version
Unspecified (NeXus is a third-party Insydium plugin for Blender, successor to X-Particles)

### Tags
particles, simulation, fluid, meshing, motion-blur, addon, intermediate

---

## Related Tutorials
- [Blender 5.0 particle attraction and follow surface motion](blender-50-particle-attraction-and-follow-surface-motion.md) — a native-Blender Geometry Nodes approach to particle path-following, useful for comparison against this NeXus plugin workflow
