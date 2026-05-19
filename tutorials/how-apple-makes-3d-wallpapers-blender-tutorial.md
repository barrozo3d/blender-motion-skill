---
title: How Apple Makes 3D Wallpapers (Blender Tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=KhBaHDvIamw
author: Ducky 3D
ingested: 2026-05-19
blender_version: "4.x"
tags: [materials, glass, shaders, motion-design, animation, intermediate]
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
Recreating the MacBook Air 3D glass wallpaper in Blender: flat glass pane meshes with a glass + anisotropic highlight shader that produces the distinctive long horizontal highlight streaks characteristic of Apple's wallpaper aesthetic, with animated camera-relative gradient for the colour wash.

### Summary
15-minute recreation of the original MacBook Air wallpaper by Ducky 3D, with input from an Apple team member on the exact highlight technique. Key insight: the long horizontal highlights are achieved with an Anisotropic BSDF (or Principled BSDF Anisotropy parameter) combined with rotated tangent — not simple glass. The glass planes are thin flat meshes; the gradient color comes from a camera-parented texture (same technique as the light trails tutorial). Ends with both still image and animated versions.

### Key Steps
1. **Glass mesh** — flat thin planes (or slightly bevelled); oriented horizontally; can be a simple grid of planes or a single looping ribbon shape
2. **Glass + Anisotropic highlight shader** — the key Apple secret: combine Principled BSDF (Transmission=1, low roughness) with Anisotropic BSDF for the long streak highlights; Mix Shader; Anisotropy Rotation drives the highlight angle
3. **Tangent control** — Tangent node (UV-based or object-space) feeds into Anisotropy Rotation → rotates the streak to be perfectly horizontal
4. **Gradient color** — Object (camera-parented empty) → Texture Coordinates → Gradient Texture or noise → Color Ramp (Apple palette: white, light blue, soft pink, subtle tones) → Base Color of glass
5. **Camera-parented gradient** — same technique as light trails: empty parented to camera; gradient sweeps through glass planes as camera moves = animated colour wash
6. **Animation** — animate camera slightly; gradient washes through glass; OR animate glass rotation for prismatic effect
7. **Render** — Cycles; Transmission bounces 8+; HDRI for ambient; Bloom in compositor

### Nodes / Settings
- Principled BSDF: Transmission=1.0, IOR=1.5, Roughness=0.01
- Anisotropic BSDF: Roughness 0.1, Anisotropy 0.8–1.0; Rotation from Tangent node
- Mix Shader: Glass + Anisotropic; ratio controls highlight strength
- Tangent node: Axis (horizontal = Z or Y depending on orientation)
- Texture Coordinate (Object, referenced to camera-parented empty) → Gradient Texture → Color Ramp (Apple palette)
- Render: Cycles, Transmission 8 bounces, Caustics ON; Compositor: Bloom + slight Glare

### Difficulty
Intermediate

### Blender Version
4.x

### Tags
materials, glass, shaders, motion-design, animation, intermediate

---

## Related Tutorials
- [[powerful-light-trails-in-blender-45-tutorial]] — same camera-parented gradient technique
- [[you-should-make-glass-animations-in-blender-51]] — broader glass animation overview
- [[you-should-try-this-blender-color-hack]] — color distribution tricks for glass shaders
