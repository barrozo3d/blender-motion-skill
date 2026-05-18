---
title: How to Make Cyberpunk Scenes in Blender
source: YouTube
url: https://www.youtube.com/watch?v=SybPYdsd_DI
author: Max Hay
ingested: 2026-05-18
blender_version: "Not specified"
tags: ["materials", "shaders", "lighting", "rendering", "compositing", "procedural", "displacement", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/how-to-make-cyberpunk-scenes-in-blender/
frame_count: 0
---

# How to Make Cyberpunk Scenes in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=SybPYdsd_DI)
**Author:** Max Hay
**Duration:** 59m24s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** This is going to be an intermediate guide on making cyberpunk renders and blender. So I'm going to be showing you a whole bunch of techniques from creating wet concrete streets, making buildings, creating neon signs, and just creating a whole cyberpunk atmosphere. I'm going to be putting all this into practice and creating a render using all these techniques as I show you them. So by the end of it, I'll show you how I made this scene from scratch. So let's just get into the video. There's also a free download on this blend file if you want to peek around there or take in the assets from there. That's linked in the description. Okay, so the first thing we need to do in a cyberpunk scene is probably a surface or just a floor to work off of and then we can build up literally from the ground up. So let's just get that in here and let's get a wet concrete floor material going here just so I have some sort of thing to work off of. So I've really been liking the polyhapen add on. I'm not affiliated or anything. It's just a good add on I've been using for textures. If you get this add on, it just installs all of the polyhapen textures, which are all free from their site. You can get them a...



---

## Structured Notes

### Core Technique
Intermediate guide to building a cyberpunk alleyway scene in Blender covering wet concrete materials with noise-driven puddle effects, fast building construction from photo reference, neon emissive signs, and volumetric atmosphere — all combined into a cohesive cyberpunk render.

### Summary
Max Hay builds a full cyberpunk environment starting from the ground up. Wet concrete uses the Polyhaven add-on for free PBR textures, then a Noise Texture drives Roughness variation (low Roughness = wet/reflective patches) and Normal strength modulation to simulate puddle bumps without an actual roughness map. Buildings are constructed using Ian Hubert's lazy reference photo technique: take a photo of a building, map it as an image texture onto flat box geometry, then extrude faces to match architectural depth. Neon signs are created with Emission materials at very high Strength (30–100) on sign geometry. A Volume Scatter cube covers the entire scene for fog/atmosphere. Compositing in the Blender compositor adds Glare (Fog Glow type) on the emissive neon lights. The final color grading uses Filmic tone mapping with high contrast.

### Key Steps
1. Install and enable the **Polyhaven add-on** → browse concrete textures → download a wet concrete PBR set directly into Blender
2. In the concrete shader: add a **Noise Texture** → route its output to a **Math (Multiply)** → use the result to modulate **Roughness** (lower Noise = wet/reflective); also modulate **Normal** strength for puddle surface bumps
3. For buildings: import a reference photo as an **Image Texture** → apply to a flat **Plane** → in Edit Mode, extrude faces forward to approximate building depth from the reference
4. Neon signs: create sign text/geometry → assign **Emission** material, Strength: 30–100, Color: cyan/pink/orange for classic cyberpunk palette
5. Add a large **Cube** over the scene → assign **Volume Scatter** material: Density: 0.01–0.03; Anisotropy: 0.3 for atmospheric haze
6. Add colored **Area Lights** (cyan, magenta) at low energy (50–200 W) to simulate neon sign bounce light on wet ground and walls
7. In **Compositor**: enable **Use Nodes** → add **Glare** node (Type: Fog Glow, Quality: High, Threshold: 0.8) after the Render Layers node to make neons bloom
8. Set **Color Management** → View Transform: Filmic; Look: High Contrast for punchy cyberpunk color grade

### Nodes / Settings
- Noise Texture (wet concrete) — Scale: 3–6; drives Roughness (0.0 wet → 0.8 dry) and Normal Strength (0.2–1.0)
- Polyhaven add-on — provides free PBR textures with automatic node setup (Albedo + Normal + Roughness + Displacement)
- Emission shader (neon) — Strength: 30–100; Color: saturated cyan (#00FFFF), hot pink (#FF00AA), or warm orange
- Volume Scatter cube — Density: 0.01–0.05; Anisotropy: 0.3–0.5; covers entire scene
- Area Light (neon fill) — Energy: 50–200 W; Color matching nearest neon sign; positioned at sign locations
- Compositor Glare node — Type: Fog Glow; Quality: High; Threshold: 0.7–1.0; Size: 8; Strength: 0.5–1.0
- Filmic Color Management — Look: High Contrast; recommended for all cyberpunk renders

### Difficulty
Intermediate

### Blender Version
Not specified

### Tags
#materials #shaders #lighting #rendering #compositing #procedural #displacement #intermediate

---

## Related Tutorials
- [3 Easy Lighting Setups | Blender Tutorial](./3-easy-lighting-setups-blender-tutorial.md)
- [How I Built This Gate Animation in Blender | Scene Breakdown](./how-i-built-this-gate-animation-in-blender-scene-breakdown.md)
- [Creating an Underground Scene in Blender (Step by Step)](./creating-an-underground-scene-in-blender-step-by-step.md)
- [Fundamentals of Lighting in Blender](./fundamentals-of-lighting-in-blender.md)
- [A FULL Blender Compositor Course!](./a-full-blender-compositor-course.md)
