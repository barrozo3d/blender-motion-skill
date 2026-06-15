---
title: My New Favorite Lighting Trick in Blender!
source: YouTube
url: https://www.youtube.com/watch?v=1-Cj4mtdCMc
author: Curtis Holt
ingested: 2026-06-15
blender_version: "Not specified (4.x/5.x era)"
tags: [lighting, animation, materials, shaders, cycles, abstract, laser, vfx, intermediate, youtube, curtis-holt]
extraction_status: complete
frames_dir: tutorials/frames/my-new-favorite-lighting-trick-in-blender/
frame_count: 4
---

# My New Favorite Lighting Trick in Blender!

**Source:** [YouTube](https://www.youtube.com/watch?v=1-Cj4mtdCMc)
**Author:** Curtis Holt
**Duration:** 8m24s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Alright, everyone. I've got something pretty cool to show you. So, as a part of my new animated production I'm working on, called Project Fold, of which the production files are available on Patreon. I have recently just done some new lighting tests, relating to laser-like lighting. So, just showing you some animation tests here on the screen now. You can see we're like lines of inconsistent laser-like passing over an object. Some of the laser-like has bleed away from the actual main line, whereas other parts don't actually have bleed, they're actually just blocking light. It's a really interesting technique. It's something that I've sort of come up with myself. I know that a lot of people have done laser lighting and blender with a variety of methods. Some using area lights, some using the new kind of raycast projection. I'm doing a more physical way of doing it, where it's literally just intersecting objects with the statue in this case, which is a CC0 model from No-3D or AT on Sketchfab. I know that before I explain it, I will get people asking, why didn't you use this method? Why didn't you use this method? Because that always happens whenever I share a technique that I'm playi...

**Frame:** tutorials\frames\my-new-favorite-lighting-trick-in-blender\frame_000.jpg


---

## Structured Notes

### Core Technique
Physical intersecting-mesh laser lighting in Cycles — a sphere or flat plane with a mixed Emission/Transparent/Holdout material passes through a subject; the material texture controls which regions emit light (creating bleed/glow), which block light (hard shadow lines), and which are transparent, producing an organic scanner/laser aesthetic without any actual light actors.

### Summary
Curtis Holt (Project Fold production) demonstrates a custom laser lighting technique developed for his animated short. Unlike area-light lasers or IES profiles, this method uses a physical mesh (sphere or flat plane) that literally intersects the subject geometry. A noise-driven texture masks the mesh into three zones: emission (visible glowing bleed), shadow (hard light-blocking silhouette), and transparent (invisible pass-through). The combination produces an organic, inconsistent laser-scanner effect where some lines glow and others cast sharp shadows. All rendered in Cycles, asset is a CC0 statue (No-3D/AT on Sketchfab).

### Key Steps
1. **Get or model your subject** — Curtis uses a CC0 classical statue from Sketchfab (No-3D/AT). Any detailed mesh with surface variation will work well.
2. **Create the intersecting geometry** — Add a UV Sphere (or flat plane) that will pass through the subject. Scale it to be just larger than the subject. This is the "laser blade" object.
3. **Enter the Shader Editor for the laser mesh** — Tick `Use Nodes` and build a custom material mixing three behaviours:
   - **Emission** — the glowing/bleed regions; set to a bright colour (red, green, cyan — whatever the laser colour should be)
   - **Transparent BSDF** — the invisible pass-through regions
   - **Principled BSDF at black / Holdout** — the light-blocking shadow regions
4. **Texture-drive the mix** — Feed a **Noise Texture** (or hand-painted scattered dots texture, as seen in frame_003) into two `Mix Shader` nodes in series. The first Mix controls Transparent vs. Emission; the second Mix blends that result with the Shadow/Holdout. This creates the inconsistent organic line pattern.
5. **Key settings for the noise texture** — Use a `Texture Coordinate > Object` input for stable UV-independent mapping. Crank `Scale` (5–20) for fine lines, lower for broader bands. Adjust `Detail` and `Roughness` for organic irregularity vs. clean edges. Use a `Color Ramp` between the noise and the Mix Factor to sharpen the soft noise into crisp mask bands.
6. **Animate the laser mesh** — Keyframe the mesh **moving through the subject** (Z or Y location), or **rotating** around the subject for a sweep effect. A single pass creates a scan; looping creates a continuous scanner.
7. **Scene lighting** — Use a separate fill light (Area Light or World) at low intensity for ambient visibility. The laser mesh's emission handles the dramatic lighting; the fill light reveals ambient surfaces without washing out the effect.
8. **Render in Cycles** — The physical intersection only works in Cycles (ray-traced). In Eevee the emission still shows but shadow-blocking won't behave correctly. Use OptiX/HIP denoising to clean up at 256–512 samples.
9. **Optional: volumetric atmosphere** — Add a Volume Scatter cube (density ~0.02–0.05) around the scene so the laser lines become visible as volumetric beams cutting through space, dramatically increasing the sci-fi/dramatic feel.

### Nodes / Settings

**Laser Mesh Material (Shader Editor):**
```
Texture Coordinate (Object) → Noise Texture
  Scale: 8–15 | Detail: 6 | Roughness: 0.5 | Distortion: 1.0
→ Color Ramp (Constant mode for sharp edges)
  Stops: 0.0=Black, 0.45=Black, 0.5=White, 1.0=White
→ Mix Shader (Factor: Color Ramp output)
  Shader A: Transparent BSDF
  Shader B: Emission (Color: laser hue, Strength: 5–20)
→ Mix Shader 2 (Factor: second Color Ramp / inverted)
  Shader A: (result above)
  Shader B: Principled BSDF (Base Color: Black, Roughness: 1.0) OR Holdout
→ Material Output
```

**Key Cycles Settings:**
- `Render > Sampling` → 256–512 samples + OptiX denoiser
- `Render > Light Paths > Transparent > Max Bounces` → 8+ (needed for Transparent BSDF to work correctly with many intersections)
- Volume Scatter (optional): World Shader → `Principled Volume` (Density: 0.02)

**Scene:**
- Subject: Any high-poly mesh; CC0 from Sketchfab works. Enable Smooth Shading.
- Laser object: UV Sphere (subdivided, ~64 segments) or flat Grid. Position to overlap subject.
- Background fill: Area Light at 0.5–1.0 W with warm/cool contrast to laser colour.

### Difficulty
Intermediate

### Blender Version
Not specified (4.x/5.x era based on UI; technique works in any modern Blender with Cycles)

### Tags
`#lighting` `#animation` `#materials` `#shaders` `#cycles` `#abstract` `#laser` `#vfx` `#intermediate` `#youtube` `#curtis-holt`

---

## Frame Analysis

**frame_000:** Final animation output — classical statue lit with atmospheric blue/purple from below, a bold red diagonal laser line crossing the body. Dark background. High contrast dramatic result.

**frame_001:** Blender full editor view — Shader Editor on the left (node graph partially visible), 3D viewport on the right showing the statue under the laser effect with the blue/purple ambience. Main technique demo frame.

**frame_002:** Blender viewport in edit/wireframe mode showing a UV Sphere — this is the physical intersecting mesh. Shader Editor visible left with a node setup. Confirms the sphere-as-laser-blade approach.

**frame_003:** A flat plane mesh displaying a **scattered black-and-white dot/noise pattern** (the mask texture) alongside a **red crescent/banana-shaped curve object** in the 3D viewport. This shows the texture driving the three-zone mask (emit / block / transparent) and likely a variant curved laser shape.

---

## Related Tutorials

- [[tutorial-how-to-make-a-volumetric-projector-in-blender-45]] — Physical light-through-volume technique (World Volume Scatter + Spotlight texture). Shares: `#lighting` `#volume` `#cycles`
- [[real-time-caustics-in-blender-51]] — Uses `Light Path (Is Shadow Ray)` + Transparent BSDF to manipulate shadow behaviour from shader — closest conceptual cousin to the blocking regions in this technique. Shares: `#shaders` `#cycles` `#lighting`
- [[3-easy-lighting-setups-blender-tutorial]] — General Cycles lighting setups including dramatic spotlights with volume scatter. Shares: `#lighting` `#cycles` `#volume`
- [[fundamentals-of-lighting-in-blender]] — Core lighting principles (key/fill, shadow, size, falloff). Shares: `#lighting` `#cycles`
