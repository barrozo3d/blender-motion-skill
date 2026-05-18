---
title: Geode Nodes (i am so clever) // Blender Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=1hKAkCP-tFQ
author: CGMatter
ingested: 2026-05-18
blender_version: "4.5"
tags: ["geometry-nodes", "procedural", "displacement", "materials", "shaders", "organic", "abstract", "blender-4x", "advanced"]
extraction_status: complete
frames_dir: tutorials/frames/geode-nodes-i-am-so-clever-blender-tutorial/
frame_count: 0
---

# Geode Nodes (i am so clever) // Blender Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=1hKAkCP-tFQ)
**Author:** CGMatter
**Duration:** 24m1s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** This is a tutorial about notes. It's a set of E, G, O, D notes. There was a time that I was at the Boston Science Museum and as a souvenir I got one of these Amethyst things and that is the inspiration for this tutorial. And yeah, this one will have a lot of improv. I don't know what I'm doing yet. This video is sponsored by Squarespace. We're gonna talk about that later. I'm gonna start off with a icosphere. Higher resolution so that we can play with it. And then before we cut it, it might be nice to get some like organic distortion. In other words, just applying noise. Set position, which is gonna allow me to modify it. Offset by a random quantity, which I'm gonna use a noise texture for. If you're gonna notice that this goes up and to the right. Long time viewers of the channel know this is because noise texture goes from zero to one. On average it goes 0.5 on the X, Y, and Z. Dude, plus dude is four. Minus one. That's free. Quick mess. It's able to normalize and now it is nice and centered. I'm gonna bring down the scale, scale down the size of this effect, and get something like that. So all of this I'm gonna call our initial rock. Next thing I wanna do is I want to cut this i...



---

## Structured Notes

### Core Technique
Procedurally generates an amethyst geode in Blender Geometry Nodes: noise-distorted Icosphere exterior, Boolean cut to reveal an interior cavity, boundary edge isolation via Geometry Proximity, variable-height crystal extrusion driven by Noise→Map Range, and instanced spike geometry with full amethyst and rock material setup.

### Summary
CGMatter builds an amethyst geode from scratch using Geometry Nodes. The outer rock shape is an Icosphere distorted with a Noise Texture via Set Position and normalized to re-center. A Boolean Difference cuts the geode open to reveal the interior cavity. The boundary between rock and crystal interior is isolated using Geometry Proximity to find faces near the cut edge, then a Noise Texture drives Map Range to vary crystal extrusion heights. Crystal spikes are instanced on those boundary faces, and separate Principled BSDF materials are assigned to the rock exterior (dark, rough, subsurface) and the amethyst crystals (low roughness, purple IOR glass-like).

### Key Steps
1. Add **Icosphere** at high subdivision → use **Set Position** with a **Noise Texture** (normalized by subtracting 0.5) as the offset vector to create organic rock distortion
2. Duplicate the Icosphere and apply a **Boolean** modifier (Difference / new Manifold mode in 4.5+) to cut open the geode at the desired angle
3. Use **Geometry Proximity** from the cut boundary edges to find faces near the interior opening — these get the crystal material and extrusion
4. Connect a **Noise Texture** → **Map Range** to control crystal extrusion height per-face; map to 0–2 range for short-to-tall crystals
5. Use **Extrude Mesh** on the isolated interior faces driven by the noise-mapped height attribute
6. Instance elongated spike geometry (scaled cylinder or cone) on the extruded faces via **Instance on Points**
7. Assign two materials: rough dark stone for exterior (Principled BSDF, Roughness 0.9, Subsurface 0.02) and amethyst for crystals (Roughness 0.05, IOR 1.55, Transmission 1.0, purple Base Color)

### Nodes / Settings
- Icosphere — Subdivisions: 4–5 for smooth distortion
- Noise Texture — Scale: 2–4; normalize by subtracting 0.5 from output to center displacement
- Set Position — Offset: normalized noise vector × Strength (0.3–0.8)
- Boolean (Manifold mode in Blender 4.5+) — Difference; cleaner results than legacy Boolean
- Geometry Proximity — Target: cut boundary edges; used to generate a mask for crystal faces
- Map Range — Input: Noise output (0–1); Output: crystal height (0.0–2.5)
- Extrude Mesh — Individual Faces: on; Offset: Map Range result
- Instance on Points — place spike mesh on extruded face centers
- Principled BSDF (rock) — Roughness: 0.85–0.95; Subsurface Weight: 0.02; Base Color: dark grey-brown
- Principled BSDF (amethyst) — Roughness: 0.02–0.08; IOR: 1.55; Transmission: 1.0; Base Color: purple/violet

### Difficulty
Advanced

### Blender Version
4.5

### Tags
#geometry-nodes #procedural #displacement #materials #shaders #organic #abstract #blender-4x #advanced

---

## Related Tutorials
- [ALL 300+ Geometry Nodes in Blender](./all-300-geometry-nodes-in-blender.md)
- [Demystifying Geometry Nodes: The Ultimate Guide to Mastering Blender's Procedural Power](./demystifying-geometry-nodes-the-ultimate-guide-to-mastering.md)
- [I'll teach you Geometry Nodes](./ill-teach-you-geometry-nodes.md)
- [Remake this in Blender in 20 mins](./remake-this-in-blender-in-20-mins.md)
