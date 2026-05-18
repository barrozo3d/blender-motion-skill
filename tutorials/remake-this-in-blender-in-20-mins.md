---
title: Remake this in Blender in 20 mins
source: YouTube
url: https://www.youtube.com/watch?v=erICwexR7Iw
author: Bad Normals
ingested: 2026-05-18
blender_version: "Not specified"
tags: ["materials", "glass", "shaders", "rendering", "cycles", "organic", "abstract", "geometry-nodes", "intermediate"]
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
Recreates an AI-generated glass flower in 20 minutes using organic sculpting from a remeshed cylinder base, with a distance-based center glow emission in the glass shader built from Texture Coordinate + Vector Length + Color Ramp nodes — producing a glowing luminescent glass effect matching the AI reference.

### Summary
Bad Normals takes an AI-generated glass flower image from Luma AI and reverse-engineers it in Blender using a structured approach: shape first, then lighting. The flower base is a cylinder with a Remesh modifier for dense sculpting topology; the Sculpt Mode inflate, draw, and smooth brushes shape the petals and stem. Once the sculpt is complete, the geometry is clean enough for a glass material. The key glass shader trick: a Texture Coordinate (Object) → Vector Length node measures distance from the object center; this drives a Color Ramp that maps center distance to emission intensity — creating a glowing core that fades to clear at the petal edges, just like the AI reference. The glass itself uses Principled BSDF with Transmission: 1.0, slight blue Base Color (Roughness: 0.05–0.1). Lighting uses an HDRI plus a couple of strategic point lights to highlight the refraction.

### Key Steps
1. Add a **Circle** → select all edges → **Extrude** (E) upward to create a cylinder form → scale to approximate flower proportions
2. Add **Remesh modifier** → mode: **Voxel**; Voxel Size: 0.02–0.04 for dense sculpting mesh → Apply modifier
3. Switch to **Sculpt Mode** → use **Inflate brush** to puff out petal areas; **Draw brush** for surface detail; **Smooth brush** (Shift) to blend
4. Sculpt 5–6 petals radiating from center, with an organic bent/curved form; sculpt stem below
5. Apply modifier → in Material Properties: new material → in Shader Editor, delete Principled BSDF to start fresh
6. Build the glass emission shader:
   - **Texture Coordinate** → Object output → **Vector Length** node → gives scalar 0 at center, 1 at edges
   - **Map Range** → remap 0–0.3 to 1–0 (so center = bright, edges = dark)
   - Use result as **Mix** factor between **Emission** (Strength: 3–8, white/light blue) and transparent component
7. **Principled BSDF** for the glass base: Transmission: 1.0; Roughness: 0.05; IOR: 1.45; Base Color: very slight blue
8. **Mix Shader**: glass BSDF + Emission shader; Factor: distance map from step 6
9. Add **HDRI** in World for ambient light; add 1–2 **Point Lights** (blue/white) near petals to enhance refraction
10. Render in **Cycles** → enable **Transparent Glass** in Render Properties → 256–512 samples + Denoiser

### Nodes / Settings
- Remesh modifier — Voxel mode; Voxel Size: 0.02–0.04 m; Smooth Normals: on
- Texture Coordinate — Object output → Vector Length → scalar distance from object origin
- Map Range — Input: Vector Length (0.0–0.5); Output: 1.0 → 0.0 (inverted center glow)
- Emission shader — Strength: 3–8; Color: white or very light cyan/blue
- Principled BSDF — Transmission: 1.0; Roughness: 0.05–0.1; IOR: 1.45; Base Color: slight blue tint
- Mix Shader — Factor: distance-based Color Ramp; A: Principled BSDF; B: Emission
- HDRI World — Strength: 1.0; outdoor or studio HDRI for natural glass refraction
- Cycles — Transparent Glass: on; Caustics: on; Samples: 256+; Denoiser: OIDN or OptiX

### Difficulty
Intermediate

### Blender Version
Not specified

### Tags
#materials #glass #shaders #rendering #cycles #organic #abstract #geometry-nodes #intermediate

---

## Related Tutorials
- [You Should Make Glass Animations in Blender 5.1](./you-should-make-glass-animations-in-blender-51.md)
- [How Apple Makes 3D Wallpapers (Blender Tutorial)](./how-apple-makes-3d-wallpapers-blender-tutorial.md)
- [Glass Cell Division Effect in Blender 5.0 (tutorial)](./glass-cell-division-effect-in-blender-50-tutorial.md)
- [Geode Nodes (i am so clever) // Blender Tutorial](./geode-nodes-i-am-so-clever-blender-tutorial.md)
