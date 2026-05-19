---
title: Remake this in Blender in 20 mins
source: YouTube
url: https://www.youtube.com/watch?v=erICwexR7Iw
author: Bad Normals
ingested: 2026-05-19
blender_version: "4.x"
tags: [sculpting, materials, glass, shaders, lighting, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/remake-this-in-blender-in-20-mins/
frame_count: 0
---

# Remake this in Blender in 20 mins

**Source:** [YouTube](https://www.youtube.com/watch?v=erICwexR7Iw)
**Author:** Bad Normals
**Duration:** 23m47s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** I was looking for web design inspiration and I've always really liked the design language of Luma, which is a generative AI company. And while I was checking the page for completely unrelated stuff, I just suddenly saw the trailer of the different AI videos people have created from prompts in Luma and one with those glass flowers immediately caught my eye. I felt like I need to know how to make something like that in blender. So unlike the AI version, it will actually be controllable. We can use it in whichever scenes we want and hopefully we'll learn a lot of useful stuff which a spoiler is true. So the general approach of remaking something is to do the most important stuff first. On their efforts I see two important things. I can see the lighting, I can see the shape of the flower. Now we cannot work on lighting before the shape, so obviously let's do the shape first. And the flower is quite organic. The best way to do organic things is to sculpt. So we need a base mesh that kind of looks like the flower and for that I just added a circle, extruded it, essentially a cylinder and added a remesh modifier. So it becomes this dense thing that you can easily sculpt. And then I added ...



---

## Structured Notes

### Core Technique
Recreating glass flowers from a Luma AI concept video in Blender: sculpt organic petal shape from a cylinder with Remesh, apply a convincing glass shader with caustics/refraction, and nail the lighting to match the reference aesthetic.

### Summary
23-minute recreation challenge by Bad Normals: starts from a reference (Luma AI trailer glass flower), identifies the two most critical elements (shape + lighting), sculpts the flower petal using a remeshed cylinder as a sculpt base, builds a glass/translucent shader, and focuses heavily on lighting to achieve the ethereal look. Emphasises a methodology: do the most impactful things first.

### Key Steps
1. **Analyse reference** — identify key visual elements: shape (organic flower), lighting (rim/backlight), glass material
2. **Sculpt base** — Add Circle → Extrude into cylinder → Add Remesh modifier (high Voxel Size for dense mesh) → Apply
3. **Sculpt petals** — use Sculpt Mode: `Grab` brush to pull out petals, `Smooth` to refine, `Crease` for vein details; create multiple petals by sculpting from the cylinder silhouette
4. **Duplicate & vary** — duplicate petal, rotate, scale, overlap for natural flower arrangement
5. **Glass shader** — Principled BSDF: Transmission=1.0, IOR ~1.45, Roughness ~0.02; enable `Screen Space Refraction` in Material Settings (EEVEE) or use Cycles for accurate caustics
6. **Lighting** — key light behind flower for backlit glow through petals; rim/edge light to define silhouette; adjust intensity for overexposed look matching reference
7. **Render** — Cycles preferred for accurate glass; enable Caustics in Render Properties; Light Path bounces: Transmission 8–12

### Nodes / Settings
- Remesh modifier: Voxel mode, Voxel Size ~0.02–0.05; Apply before sculpting
- Sculpt brushes: Grab, Smooth, Inflate, Crease
- Principled BSDF: Transmission=1.0, IOR=1.45, Roughness=0.02, Base Color light blue tint
- EEVEE: Materials → Settings → Screen Space Refraction ON; Render → Screen Space Reflections ON
- Cycles: Render Properties → Caustics → Reflective + Refractive ON; Transmission bounces 8+
- Area Light behind subject for backlit transmission glow

### Difficulty
Intermediate

### Blender Version
4.x

### Tags
sculpting, materials, glass, shaders, lighting, intermediate

---

## Related Tutorials
- [[you-should-make-glass-animations-in-blender-51]] — glass materials and animation
- [[how-to-make-cyberpunk-scenes-in-blender]] — lighting-focused scene recreation
- [[fundamentals-of-lighting-in-blender]] — lighting principles used in this recreation
