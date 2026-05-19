---
title: Glass Cell Division Effect in Blender 5.0 (tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=XOLuYDLYEgI
author: Ducky 3D
ingested: 2026-05-19
blender_version: "5.0"
tags: [geometry-nodes, sdf, animation, glass, materials, intermediate]
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
Animated glass cell division effect in Blender 5.0 using Metaball-like SDF volume blending (Grid SDF Boolean node from the SDF pipeline) — animated sphere positions drive organic blob merging/splitting behaviour, rendered through a glass dispersion shader for an elegant transparent cell biology aesthetic.

### Summary
15-minute tutorial recreating the organic blob merging/splitting behaviour of Metaballs but using Blender 5.0's Volume SDF pipeline for higher quality and render control. Spheres are animated along paths; the SDF Grid Boolean blends them organically where they overlap. A glass material with dispersion creates the prismatic color splitting effect. Ends with a procedural animated background and Cycles render tips.

### Key Steps
1. **Animated sphere positions** — create several sphere objects; keyframe their positions to simulate cell division movement (spheres moving apart/together)
2. **SDF pipeline (Blender 5.0)** — on a plane GeoNodes modifier: `Mesh to SDF` on each sphere → `Grid SDF Boolean` to blend them all together → `SDF to Mesh` to extract final mesh; adjust iso-value for membrane thickness
3. **Fix geometry issues** — SDF-to-mesh can create non-manifold geometry; use `Merge by Distance` and check normals; flip normals if needed for correct glass refraction
4. **Glass material** — Principled BSDF: Transmission=1.0, IOR~1.5, Roughness near 0; add slight dispersion for chromatic rainbow splitting through glass; Abbe Number (dispersion) in Cycles material settings
5. **Background** — gradient/noise-based emissive plane or HDRI; ensure dark background to showcase glass transparency
6. **Render** — Cycles; Transmission bounces 8+; Caustics ON for light patterns through glass

### Nodes / Settings
- `Mesh to SDF` — per sphere (Blender 5.0 required)
- `Grid SDF Boolean` — blends multiple SDF fields; key for organic cell merger
- `SDF to Mesh` — iso-value controls surface position and membrane thinness
- `Merge by Distance` — fix topology issues from SDF extraction
- Principled BSDF: Transmission=1.0, IOR=1.5, Roughness=0.01; Dispersion (Abbe Number) for prismatic effect
- Cycles: Transmission bounces 8; Caustics Reflective+Refractive; Denoiser essential

### Difficulty
Intermediate

### Blender Version
5.0

### Tags
geometry-nodes, sdf, animation, glass, materials, intermediate

---

## Related Tutorials
- [[organic-liquid-metal-effect-in-blender-50-tutorial]] — same SDF volume pipeline for liquid metal spheres
- [[you-should-make-glass-animations-in-blender-51]] — 6 glass animation styles overview
- [[you-should-try-this-blender-color-hack]] — glass + emission color techniques
