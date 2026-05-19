---
title: How to Make Cyberpunk Scenes in Blender
source: YouTube
url: https://www.youtube.com/watch?v=SybPYdsd_DI
author: Max Hay
ingested: 2026-05-19
blender_version: "4.x"
tags: [lighting, materials, modeling, environment, intermediate]
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
Intermediate cyberpunk scene construction in Blender: wet concrete floor with reflection puddles (Polyhaven PBR textures), modular building geometry, neon signs using emission materials with bloom, atmospheric volume scatter for fog and light rays, and a dark dramatic lighting setup — built from ground up as a complete render.

### Summary
59-minute intermediate guide by Max Hay building a full cyberpunk street scene from scratch. Covers every element: wet concrete floor using Polyhaven textures with procedural puddle reflection nodes, modular building construction with architectural details, glowing neon signs using emission + bloom, atmospheric fog via volume scatter, and the full cinematic dark lighting setup (dramatic spotlights, coloured neon fill lights). Blend file available for free. Uses Polyhaven addon throughout for free high-quality PBR textures.

### Key Steps
1. **Wet concrete floor** — add Plane; UV unwrap; apply Polyhaven concrete PBR texture (Base Color, Roughness, Normal); add puddle effect: noise texture → Color Ramp (sharp black/white) → Mix between dry concrete roughness (0.8) and wet roughness (0.01); wet areas become reflective
2. **Buildings** — box-model building facades using Extrude and Loop Cuts; keep geometry simple and modular; add ledges, window indentations, AC units as separate objects; Polyhaven textures for concrete walls and metal
3. **Neon signs** — create text objects or plane with logo; Emission material; Strength 5–30 for glow; Bloom in compositor turns emission into visible halo; coloured neons (red, blue, pink, green) are the signature cyberpunk light sources
4. **Atmospheric volume** — cube encompassing scene; Volume Scatter material, Density 0.01–0.03, Anisotropy 0.3; makes light rays visible from neons and spotlights
5. **Lighting** — dark world (World Strength 0); primary: narrow spotlights for god rays and key illumination; secondary: neon geometry as coloured fill lights; use different coloured spotlights (blue, red) for cyberpunk colour contrast
6. **Rain puddle reflections** — the noise-based puddle shader creates random reflective patches on the floor that reflect neon lights; adjust noise Scale for puddle size, Color Ramp contrast for puddle sharpness
7. **Compositor** — Bloom (Glare node) essential for neon glow halos; Lens Distortion for cinematic barrel distortion; Vignette; Film Grain; slight desaturation with Color Balance for moody look

### Nodes / Settings
- Polyhaven addon (Blender built-in via Extensions): provides all free PBR textures
- Wet puddle: Noise Texture (Scale 5–10) → Color Ramp (sharp contrast) → Mix Shader (wet Principled: Roughness 0.01, dry Principled: Roughness 0.7)
- Neon Emission: Strength 10–30; color matches neon tube color
- Volume Scatter: Density 0.015, Anisotropy 0.3; cube displayed as Bounds
- Compositor: Glare (Bloom, High quality, Threshold 0.9), Lens Distortion (Distort 0.05), Vignette ellipse mask, Film Grain

### Difficulty
Intermediate

### Blender Version
4.x

### Tags
lighting, materials, modeling, environment, intermediate

---

## Related Tutorials
- [[3-easy-lighting-setups-blender-tutorial]] — Setup 3 (dark emissive scene) is exactly this cyberpunk approach
- [[how-i-built-this-gate-animation-in-blender-scene-breakdown]] — same author (Max Hay), related dramatic scene work
- [[fundamentals-of-lighting-in-blender]] — lighting theory behind the dramatic spotlight setup
