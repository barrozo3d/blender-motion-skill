---
title: Geode Nodes (i am so clever) // Blender Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=1hKAkCP-tFQ
author: CGMatter
ingested: 2026-05-19
blender_version: "4.x"
tags: [geometry-nodes, procedural, materials, shaders, intermediate]
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
Procedural geode/crystal rock in Geometry Nodes (CGMatter improv style): icosphere with noise-displaced rock exterior, boolean-cut open to reveal interior crystal faces, procedural crystal spike growth using extrude + scale toward center, and a colored translucent crystal material.

### Summary
24-minute improvised GeoNodes tutorial by CGMatter (Default Cube), inspired by an Amethyst souvenir. Builds a geode from scratch: organic rock exterior via icosphere + noise deformation, a boolean cut to create the opening, crystal growth on interior faces using iterative extrude+scale nodes, and a glassy/translucent procedural material. The tutorial is improvisational — CGMatter figures out the approach live, making it valuable for seeing a GeoNodes problem-solving workflow.

### Key Steps
1. **Rock exterior** — Icosphere (higher resolution subdivisions); Set Position + Noise Texture offset = organic deformation; normalize noise (Subtract 0.5 + multiply) to center it; tune Scale to reduce noise size
2. **Boolean cut** — use a Cube scaled to half the icosphere; Mesh Boolean node: Difference → cuts away half the rock to expose the interior; adjust cube position for angle
3. **Identify interior faces** — the boolean cut creates interior faces; use `Face Is Planar` or face group/selection to isolate interior-only faces for crystal growth
4. **Crystal growth** — on interior faces: `Extrude Mesh` (inward, toward center) + `Scale Elements` (scale down each extrusion); repeat/chain for multiple crystal spire iterations; vary extrude offset with noise or random for organic crystal sizes
5. **Crystal tips** — final `Scale Elements` to very small value creates pointed tips
6. **Rock material** — Principled BSDF: dark grey/black, roughness ~0.7, slight bump from noise texture
7. **Crystal material** — Principled BSDF: Transmission=0.8, IOR=1.6, Base Color purple/blue/any gem color, Roughness very low; add slight emission for inner glow

### Nodes / Settings
- Icosphere: subdivisions 4–5 for smooth but detailed base
- Set Position + Noise Texture: Subtract 0.5 → normalized zero-centered noise for deformation
- Mesh Boolean: Difference; target = half-cutting cube
- `Extrude Mesh`: Mode Faces; individual faces; negative offset (inward)
- `Scale Elements`: Mode Faces; Scale < 1 to taper crystals
- Chain: Extrude → Scale → Extrude → Scale (repeat 3–5× for crystal look)
- Crystal: Principled BSDF Transmission 0.8, IOR 1.6, Roughness 0.02, gem color Base Color
- Rock: Principled BSDF dark color, Roughness 0.6–0.8, Noise bump texture

### Difficulty
Intermediate

### Blender Version
4.x

### Tags
geometry-nodes, procedural, materials, shaders, intermediate

---

## Related Tutorials
- [[fractals-in-blender---geometry-nodes-extrude-node]] — same Extrude Mesh + Scale pattern for fractal geometry
- [[all-300-geometry-nodes-in-blender]] — reference for Extrude Mesh and Mesh Boolean nodes
- [[organic-liquid-metal-effect-in-blender-50-tutorial]] — another organic procedural shape technique
