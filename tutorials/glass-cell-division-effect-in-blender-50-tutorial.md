---
title: Glass Cell Division Effect in Blender 5.0 (tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=XOLuYDLYEgI
author: Ducky 3D
ingested: 2026-05-18
blender_version: "5.0"
tags: ["geometry-nodes", "simulation", "glass", "materials", "shaders", "animation", "motion-design", "abstract", "blender-5x", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/glass-cell-division-effect-in-blender-50-tutorial/
frame_count: 0
---

# Glass Cell Division Effect in Blender 5.0 (tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=XOLuYDLYEgI)
**Author:** Ducky 3D
**Duration:** 15m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** How's it going guys? In this tutorial, we're going to be making this animation right here. It is going to be done in Blender 5.0, which is in beta. So you'll need to go to Blender.org and check out the daily builds and get the beta. Otherwise, you're probably watching this in a later time and it's already out and normal and you already have it. This is a really cool tutorial because we're going to be remaking kind of traditional Metaball movements and behaviors, which is kind of the whole point and the thing that got me really excited about this. So I am going to show you how to create those Metaball actions. How to fix geometry problems that you might run into and at the very end, we're going to make a really beautiful background and some glass dispersion and show you some cool stuff with that. I had a lot of fun this month on Patreon playing with these Metaballs and showing you different ways you can style them and make them look really cool. So if you want to check out those four exclusive tutorials on Patreon that is linked in the description and you need a discount if you subscribe annually. With that being said, let's get into this tutorial. So open up a just totally empty do...



---

## Structured Notes

### Core Technique
Recreates metaball-style cell division animation in Blender 5.0 using the new **Points to SDF Grid** and **SDF Grid to Mesh** nodes to merge animated point clouds into organic blob geometry — far more efficient than the old instances-to-volume approach — topped with an RGB glass dispersion material in Cycles.

### Summary
Ducky 3D uses Blender 5.0's new SDF Grid volume nodes to simulate cell division / metaball-style organic merging. An array of points is animated with randomized velocities to split and merge over time; the Points to SDF Grid node converts the point cloud to a signed distance field, and SDF Grid to Mesh converts it back to a smooth unified mesh without needing traditional Metaballs. A Smooth by Angle node eliminates shading artifacts at merge points. The background uses an emissive gradient plane, and the organic mesh receives an RGB glass dispersion Cycles material with separate IOR values per color channel.

### Key Steps
1. Create an empty scene → add a **Plane** → apply a **Geometry Nodes** modifier → click New
2. In GN editor, add **Points** node → **Instance on Points** with a UV Sphere → animate point positions with Random Value + keyframed offsets to simulate splitting/merging behavior
3. Add **Points to SDF Grid** node → set Voxel Size to 0.05–0.1 for quality vs. performance
4. Connect to **SDF Grid to Mesh** node → adjust Threshold to control blob merge distance (lower = blobs merge sooner)
5. Add **Smooth by Angle** or **Set Shade Smooth** to remove hard edges at merge boundaries
6. Apply a **Principled BSDF** material in Cycles with Transmission: 1.0, IOR: 1.45, Roughness: 0.0 for glass base
7. Add **RGB Dispersion**: duplicate Principled BSDF → use separate R/G/B IOR values (1.43, 1.45, 1.47) and combine in Mix Shader for chromatic aberration glass effect
8. Add background: emissive gradient plane with a **Color Ramp** for colorful backdrop; set World to black

### Nodes / Settings
- Points to SDF Grid — Voxel Size: 0.05–0.1; Radius: controls blob size (0.3–0.8)
- SDF Grid to Mesh — Threshold: 0.0 (default); lower values = blobs merge at larger distance
- Smooth by Angle — Angle: 30° for clean shading across merged blobs
- Principled BSDF (glass) — Transmission: 1.0; IOR: 1.45; Roughness: 0.0; Base Color: white/slight tint
- RGB Dispersion — three Principled BSDF nodes with IOR 1.43 / 1.45 / 1.47 mixed via Mix Shader
- World Shader — Strength: 0 (black background); emissive plane provides all scene color
- Cycles render — Transparent Glass: on; Caustics: on for proper glass light behavior

### Difficulty
Intermediate

### Blender Version
5.0

### Tags
#geometry-nodes #simulation #glass #materials #shaders #animation #motion-design #abstract #blender-5x #intermediate

---

## Related Tutorials
- [Organic Liquid Metal effect in blender 5.0 (tutorial)](./organic-liquid-metal-effect-in-blender-50-tutorial.md)
- [How To Make This Style in Blender 5.0](./how-to-make-this-style-in-blender-50.md)
- [You Should Make Glass Animations in Blender 5.1](./you-should-make-glass-animations-in-blender-51.md)
- [Remake this in Blender in 20 mins](./remake-this-in-blender-in-20-mins.md)
