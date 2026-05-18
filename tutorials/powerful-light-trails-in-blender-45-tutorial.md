---
title: Powerful Light Trails in Blender 4.5 (tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=965bgIUHoxA
author: Ducky 3D
ingested: 2026-05-18
blender_version: "4.5"
tags: ["geometry-nodes", "simulation", "animation", "motion-design", "materials", "shaders", "camera", "abstract", "blender-4x", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/powerful-light-trails-in-blender-45-tutorial/
frame_count: 0
---

# Powerful Light Trails in Blender 4.5 (tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=965bgIUHoxA)
**Author:** Ducky 3D
**Duration:** 23m26s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Has gone so in today's tutorial we're going to be making this animation. It's honestly one of my favorite I've done in a really long time. First thing we're going to do is duplicate a bunch of curves and make sure that they are sitting in the right position So this animation is going to loop then we're going to go ahead and Displace the curves and shape that displacement to look more like a topographic map. Then we're going to go ahead and parent a gradient to the camera movement which is going to create the animation. Then we're going to go ahead and edit that gradient to create a really cool glowing effect and then after that we're going to use a wave texture to select the center curves to make them brighter And create a really nice focal point then we're going to make a simple metallic floor material and will be totally done. This animation is part of a series of Tutorials here on YouTube that are inspired by topographic map art and animations. I'll be posting four of these tutorials back to back here on YouTube So if you want to learn more of this stuff you can go and check out the other ones like this. They're all really cool And there's a lot of fun things to learn on patreon...



---

## Structured Notes

### Core Technique
Topographic map-inspired light trail animation using a Simulation Zone to array 77 Quadratic Bezier curves, Noise Texture displacement shaped by RGB Curves for flat ground areas, and a camera-parented gradient transparency that reveals curves as the camera moves — creating the illusion of traveling over an infinite glowing landscape.

### Summary
Ducky 3D builds a looping light trail animation inspired by topographic contour map art. A Simulation Zone arrays 77 Quadratic Bezier curves along the Z axis with equal spacing. A Noise Texture drives the Y displacement of each curve to create terrain-like contour shapes; an RGB Curves node on the noise output flattens mid-values to create wide "plateau" areas between peaks, mimicking topographic map contours. A gradient plane parented to the camera acts as a transparency mask — as the camera moves forward, curves fade in from the front and fade out behind, creating the infinity reveal. A Wave Texture selects the central curves by position and applies higher Emission Strength, creating a bright focal stripe. The floor receives a simple metallic material. The animation loops perfectly because the camera path length matches the curve Z spacing.

### Key Steps
1. Add a **Plane** → Geometry Nodes → New → use a **Simulation Zone** to create and array 77 **Quadratic Bezier** curves evenly spaced along Z (spacing: 0.15 m)
2. Store **Spline Parameter (Factor)** as a named attribute on each curve point for use in the shader
3. Add a **Noise Texture** → route output through **RGB Curves** (flatten mid-range with an S-curve inversion to create plateau areas) → use result as Y-axis offset via **Set Position**
4. Parent a large flat **Plane** (gradient material) to the **Camera** → assign a **Gradient Texture** (Linear, along Y) → **Color Ramp** (black to white) → use as **Alpha** on the curve material for the proximity reveal
5. In the curve material: route gradient alpha to mix between Emission and Transparent BSDF — curves near camera are visible, distant ones fade
6. Add a **Wave Texture** along the X/Y position → **Color Ramp** → **Math (Greater Than)** to select only the center-most curves → multiply their Emission Strength by 3–5× for the bright focal stripe
7. Apply a **Metallic floor material** to the ground plane: Principled BSDF, Metallic: 1.0, Roughness: 0.1–0.3, dark color
8. Keyframe the camera's Y location to move forward by exactly (77 × spacing) over the timeline length for a perfect seamless loop

### Nodes / Settings
- Simulation Zone — creates 77 Quadratic Bezier curves; Z spacing: 0.15 m per iteration
- Quadratic Bezier — curve resolution: 32; provides smooth curve geometry
- Noise Texture — Scale: 1.5–3; Y displacement: 0.5–2.0 m; shapes terrain contours
- RGB Curves — applied to Noise output; S-curve inversion creates plateau regions between peaks
- Set Position — Y offset driven by noise RGB Curves result
- Gradient Texture (camera-parented plane) — Linear type; drives transparency reveal mask
- Color Ramp (transparency) — black (transparent) to white (visible); controls fade distance
- Wave Texture — Bands type; selects center curves for highlight stripe
- Emission shader — Strength: 3–8 for bright curves; multiply center stripe by 3–5× 
- Principled BSDF (floor) — Metallic: 1.0; Roughness: 0.15; Base Color: dark grey/black

### Difficulty
Intermediate

### Blender Version
4.5

### Tags
#geometry-nodes #simulation #animation #motion-design #materials #shaders #camera #abstract #blender-4x #intermediate

---

## Related Tutorials
- [How To Make This Style in Blender 5.0](./how-to-make-this-style-in-blender-50.md)
- [A New Way To Loop Animations in Blender](./a-new-way-to-loop-animations-in-blender.md)
- [Sci-Fi Grid Pattern Animation Loop - Blender Motion Graphics Tutorial](./sci-fi-grid-pattern-animation-loop-blender-motion-graphics-t.md)
- [Another Blender String Tutorial....But even Better This Time!](./another-blender-string-tutorialbut-even-better-this-time.md)
