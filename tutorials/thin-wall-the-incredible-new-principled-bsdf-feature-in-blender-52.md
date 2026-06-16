---
title: THIN WALL, the incredible new Principled BSDF feature in Blender 5.2
source: YouTube
url: https://www.youtube.com/watch?v=eQLCfPwEcrI
author: Christopher 3D
ingested: 2026-06-16
blender_version: "5.2"
tags: [materials, shaders, rendering, cycles, eevee, organic, blender-5x, beginner]
extraction_status: complete
frames_dir: tutorials/frames/thin-wall-the-incredible-new-principled-bsdf-feature-in-blender-52/
frame_count: 4
---

# THIN WALL, the incredible new Principled BSDF feature in Blender 5.2

**Source:** [YouTube](https://www.youtube.com/watch?v=eQLCfPwEcrI)
**Author:** Christopher 3D
**Duration:** 16m44s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Blender 5.2 is introducing a powerful new shading feature built directly into the Prinsbolt BSDF called ThinWald. It's an unassuming little checkbox, the Desm important shading operations, the Prinsbolt BSDF has lacked up until now. You might already know that the Blender developers are working on implementing the new industry standard OpenPBR material specification. While the OpenPBR effort is going to have its own new Uber Material node, the developers are porting some aspects of OpenPBR's technology directly into the Prinsbolt BSDF. The arrival of the ThinWald toggle is the first major fruit of that effort. It critically feels a feature gap that people have spent years using less than ideal workarounds to solve. Simply put, ThinWald simulates light passing cleanly through geometry that has zero physical thickness. This is an absolute game changer for rendering foliage, receipt paper, lampshades, curtains, soap bubbles, and large pains of architectural glass. Previously, to get realistic light transport on these surfaces, you had two choices. You either had to add a solidify modifier to give the mesh physical volume, which increased render with deep subsurface scattering calculat...

**Frame:** tutorials\frames\thin-wall-the-incredible-new-principled-bsdf-feature-in-blender-52\frame_000.jpg


---

## Structured Notes

### Core Technique
The **Thin Wall** toggle in the Principled BSDF (Blender 5.2) — simulates physically correct light transport through zero-thickness geometry without needing a Solidify modifier or manual Translucent BSDF mixing.

### Summary
Blender 5.2 adds a "Thin Wall" checkbox directly inside the Principled BSDF, the first major fruit of the OpenPBR integration effort. Enabling it tells the renderer to treat the mesh as a surface with no physical volume, so light scatters and transmits through it correctly. This replaces years of workarounds (Solidify modifier for SSS volume or Translucent + Diffuse BSDF mixing) for foliage, curtains, lampshades, receipt paper, soap bubbles, and large architectural glass panes. Two sub-parameters — **Weight** and **Anisotropy** — control the intensity and directionality of the scattered light.

### Key Steps
1. Select your zero-thickness mesh (leaf card, curtain plane, glass pane, etc.)
2. Open the Shader Editor; add or select the **Principled BSDF** node
3. Scroll down in the node to find the **Thin Wall** checkbox — enable it
4. Set **Weight** (0.0–1.0) to control how strongly back-light transmits through the surface (0.5 is a natural starting point for foliage; seen in frame_003)
5. Set **Anisotropy** (-1.0 to 1.0) to control directional light scatter — negative values (-0.25) work well for fabric/curtains (frame_002); 0.0 is isotropic (frame_003 foliage)
6. No Solidify modifier needed — keep geometry as single-sided planes for best performance
7. Works in both **Cycles** and **Eevee** (built into the shader core)
8. For foliage: pair with an alpha-mapped Base Color + Alpha socket for leaf card cutouts

### Nodes / Settings
| Node / Setting | Value | Notes |
|---|---|---|
| Principled BSDF → Thin Wall | ON | The main toggle; hidden below the fold in the node |
| Thin Wall → Weight | 0.5 | Shown in frame_003 (foliage/trees scene) |
| Thin Wall → Anisotropy | −0.25 | Shown in frame_002 (kitchen curtains); 0.0 for foliage |
| Render Engine | Cycles or Eevee | Both supported |
| Solidify Modifier | Not needed | Remove it — Thin Wall replaces its shading role |

**Old workarounds (now obsolete for these cases):**
- Solidify modifier → adds physical volume for SSS but increases render cost significantly
- Mix Shader (Translucent BSDF + Diffuse/Principled) → approximation, no OpenPBR accuracy

### Difficulty
Beginner — it is a single checkbox inside an existing node, with two optional sub-parameters to tune.

### Blender Version
**5.2** — part of the OpenPBR specification integration; not available in 5.1 or earlier.

### Tags
`#materials` `#shaders` `#rendering` `#cycles` `#eevee` `#organic` `#blender-5x` `#beginner`

---

## Related Tutorials
- [[blender-5-beginner-tutorial-part-2-materials-and-rendering]] — Materials & rendering intro for Blender 5.x; shares `#materials #rendering #cycles #eevee #beginner #blender-5x`
- [[photorealistic-eevee-renders-in-blender-51]] — Eevee photorealism with glass/translucent materials; shares `#eevee #rendering #materials #glass #blender-5x`
- [[real-time-caustics-in-blender-51]] — Fake caustics via shadow shader manipulation; related transparent/glass material technique in Cycles; shares `#shaders #glass #cycles`
