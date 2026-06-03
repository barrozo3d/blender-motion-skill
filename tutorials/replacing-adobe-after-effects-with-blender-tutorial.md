---
title: Replacing Adobe After Effects with Blender (tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=ZK92Uuhiesg
author: Ducky 3D
ingested: 2026-06-03
blender_version: "4.x"
tags: [materials, shaders, animation, motion-design, abstract, procedural, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/replacing-adobe-after-effects-with-blender-tutorial/
frame_count: 4
---

# Replacing Adobe After Effects with Blender (tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=ZK92Uuhiesg)
**Author:** Ducky 3D
**Duration:** 16m42s | Part of the "Blender as After Effects" series

---

## Structured Notes

### Core Technique
Procedural 2D texture animation on a flat plane using Shader Editor nodes (Voronoi + Wave Texture + radial masks), with all motion achieved by keyframing node values — treating Blender like After Effects.

### Summary
Part of Ducky 3D's "Blender as After Effects" series, this tutorial creates a looping animated texture from basic 2D procedural textures with a convincing 3D feel. A Voronoi Texture is twisted in a circular pattern by combining it with a Wave Texture, then three masks (outer edge, inner core, animated lighting variation) control how the pattern is revealed and animated. Everything moves via keyframed node values — no geometry animation needed.

### Key Steps
1. Start with a flat plane as the canvas, camera pointing straight down
2. Open Shader Editor — add a **Voronoi Texture** node (Smooth F1, distance metric)
3. Add a **Wave Texture** node (Rings type) — use its output to distort the Voronoi's Vector input, creating a circular twist effect
4. Build an **outer mask**: Texture Coordinate (UV or Object) → Vector Length → Color Ramp — creates a radial gradient that blacks out the canvas edges
5. Build an **inner mask**: same Vector Length approach with tighter Color Ramp falloff — isolates the center zone
6. Build a **lighting variation mask** (third mask): second Noise or Wave Texture → Color Ramp — drives highlight/shadow variation and can be animated independently
7. Combine the three masks using **Mix Color** (Multiply mode) or Math nodes to composite the final look
8. Add **Z rotation keyframes** on the plane object itself to spin the canvas
9. Keyframe animatable node values: Voronoi Scale, Wave Distortion amount, Wave offset (drives lateral motion), mask Color Ramp positions
10. Use the NLA Editor or Graph Editor to smooth/loop keyframe curves for a seamless loop

### Nodes / Settings
| Node | Key Parameters |
|------|---------------|
| Voronoi Texture | Feature: Smooth F1; Scale: ~5–10; Randomness: 1.0 |
| Wave Texture | Type: Rings; Distortion: 2–5 (drives the circular twist); Scale: ~5 |
| Texture Coordinate | Object mode for masks; UV for texture details |
| Vector Length (Math) | Converts XY vector to radial distance for masks |
| Color Ramp | Outer mask: black at edge, white toward center; Inner mask: inverse; Lighting: custom |
| Mix Color (Multiply) | Stacks the three masks together |
| Emission Shader | Used for the final color output (no lighting needed) |
| Principled BSDF | Alternative if rendering with lights |

### Difficulty
Beginner / Intermediate

### Blender Version
Not specified (4.x UI visible in frames)

### Tags
#materials #shaders #animation #motion-design #abstract #procedural #beginner #intermediate

---

## Related Tutorials
- **[You Should Make Glass Animations in Blender 5.1](you-should-make-glass-animations-in-blender-51.md)** — same emissive texture-plane approach, no scene lights
- **[You Should Try this Blender Color Hack](you-should-try-this-blender-color-hack.md)** — Ducky 3D, two-texture combination technique for color distribution
- **[A New Way To Loop Animations in Blender](a-new-way-to-loop-animations-in-blender.md)** — Ducky 3D, seamless loop keyframing
- **[How To Make This Style in Blender 5.0](how-to-make-this-style-in-blender-50.md)** — Ducky 3D, Wave Texture–driven animation on geometry
- **[How Apple Makes 3D Wallpapers (Blender Tutorial)](how-apple-makes-3d-wallpapers-blender-tutorial.md)** — flat plane + procedural texture as canvas

---

## Raw Data (for reference)

### Full Content [0:00]
**Transcript:** How's it going guys? Today we are going to make this animation. It's really cool and it's completely made from basic textures. This tutorial is part of a series of tutorials where we're using Blender in a similar way that we would use Photoshop or After Effects. The theme of today's is creating beautiful animations just from 2D textures and giving it kind of a 3D feel and animating it in a really cool, interesting way. So if you want to check out more from this series, there's a YouTube playlist linked in the description. So here's the steps that we're going to go through to make this animation. First we're going to get just a basic Voronoid texture. Then we'll get a wave texture combined those so that it twists the Voronoid texture in a circular way. Then we're going to get three masks. We're going to create an outer mask. We're going to create an inner mask. And then we're going to create a third mask to have variations in lighting and be able to animate that as well. After that all we'll need to do is spin the canvas, animate all of the nodes so that they move, and we will be done. If you like the subject, there's actually bonus content from this using Blender like After Effects...

**Frame:** tutorials/frames/replacing-adobe-after-effects-with-blender-tutorial/frame_000.jpg
*(Frame shows: Blender 4.x viewport with a flat white plane on a dark grid — the starting canvas before any material is applied)*
