---
title: How Apple Makes 3D Wallpapers (Blender Tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=KhBaHDvIamw
author: Ducky 3D
ingested: 2026-05-18
blender_version: "Not specified"
tags: ["materials", "glass", "animation", "rendering", "cycles", "motion-design", "abstract", "beginner", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/how-apple-makes-3d-wallpapers-blender-tutorial/
frame_count: 0
---

# How Apple Makes 3D Wallpapers (Blender Tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=KhBaHDvIamw)
**Author:** Ducky 3D
**Duration:** 15m10s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** How's it going guys? So in today's tutorial, we are going to be creating this image and this animation. Today we are trying to recreate the original MacBook Air Wallpaper that launched maybe about three years ago. So first, I'm going to show you how to create the glass shapes and animate it in an interesting way, pretty easy. And with the help of someone on the Apple team that actually worked on that original image, he told me exactly how to get the highlight shapes the exact way that they did in their image. If you want to grab the project file for the animated version of this tutorial that is available on Patreon right now, along with an exclusive tutorial on how to create this glass animation, how to get that sort of glass plank animation, make it loop, make it look really beautiful, along with a ton of other exclusive tutorials and project files on Patreon. So if you want to check that out, that is linked in the description. And you can get a discount if you subscribe annually. With that being said, let's get into this tutorial. Now it goes without saying all credit goes to Apple and the Apple team that created this image. So first thing we're going to need to do is get a mesh ...



---

## Structured Notes

### Core Technique
Recreates the Apple MacBook Air 3D wallpaper using a tall teardrop-shaped cylinder arranged in a circular Array modifier, a Cycles glass transmission material, and a strategically placed emissive highlight plane that creates the signature glowing band across all shapes.

### Summary
Ducky 3D reverse-engineers the Apple MacBook Air wallpaper with help from an Apple team member who confirmed the highlight technique. The base shape is a cylinder scaled tall on Z (ratio ~47:2) with a tapered top, arranged into a ring of 14 copies using an Array modifier with Object Offset (an Empty rotated 360°/14). Each cylinder receives a glass Principled BSDF material with low roughness in Cycles. The key insight from Apple: a single large emissive plane positioned behind/above the camera creates the glowing highlight band visible through all the glass cylinders. Camera positioning at a low angle looking up through the ring creates the signature spiral composition.

### Key Steps
1. Add a **Cylinder** → in Edit Mode, select the top loop, scale it down (S > 0.3) to taper the top into a teardrop shape
2. Scale the cylinder: Z scale ≈ 10–12 (very tall), X/Y scale ≈ 0.2 (thin) to get the ~47:2 tall teardrop proportion
3. Add an **Array modifier** → Count: 14 → enable **Object Offset** → create an **Empty** rotated Y: 360°/14 ≈ 25.7° → set as Array offset object
4. Position the Empty at a radius offset (X: 2–3 m) so cylinders form a ring around the center
5. Apply a **Principled BSDF** material → set Transmission: 1.0, IOR: 1.45, Roughness: 0.05 for glass
6. Add a large **Plane** (emissive) → assign Emission shader, Strength: 5–20, white color → position it above and behind the camera to create the highlight band
7. Set camera to a low angle looking up through the ring for the signature Apple spiral perspective; use a 50–85mm focal length
8. Render in **Cycles** → enable Transparent Glass; use 256–512 samples with Denoiser

### Nodes / Settings
- Array modifier — Count: 14; Object Offset: Empty rotated ~25.7° around Y; Relative Offset: off
- Principled BSDF (glass) — Transmission: 1.0; IOR: 1.45; Roughness: 0.03–0.08; Base Color: white or very slight blue
- Emission plane — Strength: 5–20; large enough to span the entire ring from camera view
- Cycles — Transparent Glass: on; Caustics: on; Samples: 256+; Denoiser: Intel Open Image Denoise
- Camera — Focal Length: 50–85mm; low angle looking up through the cylinder ring

### Difficulty
Beginner

### Blender Version
Not specified

### Tags
#materials #glass #animation #rendering #cycles #motion-design #abstract #beginner #intermediate

---

## Related Tutorials
- [You Should Make Glass Animations in Blender 5.1](./you-should-make-glass-animations-in-blender-51.md)
- [Glass Cell Division Effect in Blender 5.0 (tutorial)](./glass-cell-division-effect-in-blender-50-tutorial.md)
- [Remake this in Blender in 20 mins](./remake-this-in-blender-in-20-mins.md)
- [You Should Try this Blender Color Hack](./you-should-try-this-blender-color-hack.md)
