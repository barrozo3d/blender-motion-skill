---
title: Organic Liquid Metal effect in blender 5.0 (tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=2MKKuHcni1U
author: Ducky 3D
ingested: 2026-05-18
blender_version: "5.0"
tags: ["geometry-nodes", "simulation", "metal", "materials", "shaders", "animation", "abstract", "organic", "blender-5x", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/organic-liquid-metal-effect-in-blender-50-tutorial/
frame_count: 0
---

# Organic Liquid Metal effect in blender 5.0 (tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=2MKKuHcni1U)
**Author:** Ducky 3D
**Duration:** 10m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** All right, in this tutorial, we are going to be creating this render right here. The point of it is to show you how to use the new volume SDF nodes to get these spheres, to have these really thin liquidity connected pieces to each one of them and show you how to get that. What this is going to teach you is how to combine multiple objects into each other with the grid SDF Boolean node. So it's a really creative application for that node. So if you want to check out the project file that is available on Patreon right now, and Patreon is also 25% off till the end of November. So if you want to check that out, along with all of my courses and real-time materials, are 50% off with this code. All that stuff is available till the end of the month. That's my Black Friday sale. So if you want to check it out, support me. That'd be awesome. But with that being said, let's get into this tutorial. All right, you are going to need Blender 5.0 or later to be able to do this. So let's go ahead, Shift-A. We'll get a plane that'll be our geometry. That'll be the object we need for geometry nodes. I'm going to open up a new window and switch this over to geometry nodes. I'm going to click new. So I'...



---

## Structured Notes

### Core Technique
Creates an organic liquid metal effect in Blender 5.0 using the new **SDF Grid Boolean (Union)** node to merge multiple sphere instances into a unified organic mesh with liquid connective tissue, animated via 4D Noise Texture W value — with metallic and subsurface material variants.

### Summary
Ducky 3D demonstrates a creative application of Blender 5.0's SDF volume nodes to simulate the look of liquid mercury or metallic blobs merging. A Plane receives a Geometry Nodes setup where multiple UV Sphere instances are placed at distributed positions. Each sphere is converted to an SDF Grid via **Mesh to SDF Grid**, then all grids are merged with **SDF Grid Boolean (Union)** — this produces the organic liquid connective tissue between spheres at no extra cost. The unified SDF Grid is converted back to a mesh with **SDF Grid to Mesh**. A 4D Noise Texture animates the W value to make the connection tissue morph organically over time. A **Smooth Geometry** node removes shading artifacts. The material is a highly metallic Principled BSDF (Metallic: 1.0, Roughness: 0.05–0.2) with optional subsurface for a fleshy-organic variant.

### Key Steps
1. Add a **Plane** → add **Geometry Nodes** modifier → New; delete Group Input (plane geometry not needed)
2. Add **Points** node (or **Distribute Points on Faces** on a sphere) → set 5–10 positions for sphere centers
3. **Instance on Points** → object: UV Sphere (or Icosphere, Radius: 0.3–0.8)
4. **Realize Instances** (required before mesh→SDF conversion)
5. **Mesh to SDF Grid** → Voxel Size: 0.05 (smaller = more detail + slower); Bandwidth: 3
6. **SDF Grid Boolean** → Operation: Union → connects all spheres into one unified liquid SDF field; the connective tissue appears automatically where spheres are close
7. **SDF Grid to Mesh** → Threshold: 0.0
8. **Smooth by Angle** or **Set Shade Smooth** to clean up shading artifacts at merge regions
9. Animate: add a **Noise Texture** node with a **Scene Time → Divide by 24** as the W input → route Noise output to **Set Position** offset or to sphere instance positions for organic movement
10. Assign **Principled BSDF** material: Metallic: 1.0; Roughness: 0.05; Base Color: silver/chrome for liquid metal; or add Subsurface: 0.1, pink color for organic fleshy variant

### Nodes / Settings
- Points node — 5–15 positions for sphere placement; can be animated with Noise for movement
- Instance on Points — UV Sphere; Radius: 0.3–0.8; Realize Instances: required before SDF conversion
- Mesh to SDF Grid — Voxel Size: 0.05–0.1; Bandwidth: 3 (controls merge distance)
- SDF Grid Boolean — Operation: Union; merges all sphere SDFs into one field; connective tissue forms where spheres are within Bandwidth distance
- SDF Grid to Mesh — Threshold: 0.0; lower values = more bloated/rounder result
- Smooth by Angle — Angle: 30°; removes hard shading at merge seams
- Noise Texture (animation) — W input: Scene Time ÷ 24 × speed; drives organic morph via Set Position
- Principled BSDF (metal) — Metallic: 1.0; Roughness: 0.05–0.15; Base Color: white/silver
- Principled BSDF (organic) — Subsurface Weight: 0.1; Subsurface Radius: (1.0, 0.2, 0.1) for pink flesh tones; Roughness: 0.3

### Difficulty
Intermediate

### Blender Version
5.0

### Tags
#geometry-nodes #simulation #metal #materials #shaders #animation #abstract #organic #blender-5x #intermediate

---

## Related Tutorials
- [Glass Cell Division Effect in Blender 5.0 (tutorial)](./glass-cell-division-effect-in-blender-50-tutorial.md)
- [3D Smoke (Blender Geometry Nodes)](./3d-smoke-blender-geometry-nodes.md)
- [How To Make This Style in Blender 5.0](./how-to-make-this-style-in-blender-50.md)
- [You Should Make Glass Animations in Blender 5.1](./you-should-make-glass-animations-in-blender-51.md)
