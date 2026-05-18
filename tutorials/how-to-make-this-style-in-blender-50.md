---
title: How To Make This Style in Blender 5.0
source: YouTube
url: https://www.youtube.com/watch?v=rbPOL9ibooY
author: Ducky 3D
ingested: 2026-05-18
blender_version: "5.0"
tags: ["geometry-nodes", "animation", "motion-design", "materials", "shaders", "eevee", "compositing", "abstract", "blender-5x", "beginner", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/how-to-make-this-style-in-blender-50/
frame_count: 0
---

# How To Make This Style in Blender 5.0

**Source:** [YouTube](https://www.youtube.com/watch?v=rbPOL9ibooY)
**Author:** Ducky 3D
**Duration:** 18m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Has gone guys so in today's tutorial we are going to be making this animation. If you're not super comfortable with geometry nodes, don't worry. It's not a very big treat to make something really cool like this. First thing we're going to do is make a big stack of curves. Then immediately we're going to hop into the shading workspace where everything else is going to happen. So we're going to use a wave texture for the movement. We're going to randomize the position of the wave texture to get this really beautiful movement. Then using noise textures, we're going to add some really cool color. Then we're going to add some compositing to polish it off. If you want to check out the project file, that is available currently on Patreon. And this month I added a bunch of really cool tutorials that I personally just had a lot of fun working on. They're a little bit different than what I normally do. And they're just really cool. I'm working on a bigger video for here on YouTube. But for now, all of those tutorials are available exclusively on Patreon. So check that out linked in the description. And with that being said, let's get into this tutorial. All right, so we a...



---

## Structured Notes

### Core Technique
Creates a stacked-ring motion graphics animation using 120 Curve Circles on a Mesh Line in Geometry Nodes, animated by Wave and Noise Textures through stored Spline Parameter attributes, rendered in Eevee with an 8mm ultra-wide camera for the distinctive zoomed-through-ring effect.

### Summary
Ducky 3D builds a looping animation of stacked Curve Circles (rings) that ripple with wave-like motion. In Geometry Nodes, a Mesh Line generates 120 points along the Z axis; each point instances a Curve Circle (UV Sphere-style ring). The Spline Parameter (Factor) attribute is stored and used in the shader to drive a Wave Texture for the animated up-down displacement, randomized per ring by a Random Value node so each ring moves slightly differently. A Noise Texture drives color variation across the rings. All visual work happens in the shader rather than Geometry Nodes, keeping the GN setup minimal. An 8mm focal length ultra-wide camera looking through the center of the stack creates the distinctive tunnel/portal composition. Eevee renders fast with Emission materials and a Glare Bloom compositor node for the glow effect.

### Key Steps
1. Add a **Plane** → Geometry Nodes → click New → delete Group Input
2. Add **Mesh Line** node → Count: 120; Offset: 0,0,0.05 (Z spacing between rings)
3. Add **Instance on Points** → Object: a **Curve Circle** (Radius: 1–2 m, set as a separate object in the scene)
4. **Store Named Attribute** — Name: "index"; Domain: Point; Value: **Index** node — stores ring number for shader access
5. In Shader Editor on the instanced Curve Circle: add **Attribute** node → Name: "index" → divide by ring count → use as input to **Wave Texture** (Bands, Phase Offset = this value × scale) for per-ring phase offset
6. Add a **Random Value** (Float) → seed by index attribute → add to Wave Texture Phase for organic randomness
7. Route Wave Texture result to **Set Position** Z offset via the shader's geometry output — or use it directly as the displacement
8. For color: add a **Noise Texture** with index-offset → **Color Ramp** (vivid palette) → **Emission** shader, Strength: 3–10
9. Camera: set Focal Length to **8mm** → position above/below ring stack looking through the center tunnel
10. In Compositor: add **Glare** node (Bloom type) for the signature glow around bright rings

### Nodes / Settings
- Mesh Line — Count: 120; Offset Z: 0.05 m (controls ring spacing)
- Curve Circle — Radius: 1.5–2.5 m; Fill Mode: None (just the ring curve)
- Instance on Points — Object: Curve Circle; Realize Instances: off
- Store Named Attribute — "index" = Index node; Domain: Instance
- Wave Texture — Bands type; Scale: 2–5; Phase Offset: driven by per-ring index attribute
- Random Value — Min: 0; Max: 6.28 (full 2π); Seed: index; added to Wave Phase for randomization
- Noise Texture (color) — Scale: 1–3; Color → Color Ramp (vivid gradient)
- Emission shader — Strength: 3–15; World set to black
- Camera — Focal Length: 8mm; positioned at center/top of ring stack
- Eevee — Bloom: on; Compositor Glare Bloom: Threshold 0.5; Strength 0.5

### Difficulty
Beginner

### Blender Version
5.0

### Tags
#geometry-nodes #animation #motion-design #materials #shaders #eevee #compositing #abstract #blender-5x #beginner #intermediate

---

## Related Tutorials
- [A New Way To Loop Animations in Blender](./a-new-way-to-loop-animations-in-blender.md)
- [Sci-Fi Grid Pattern Animation Loop - Blender Motion Graphics Tutorial](./sci-fi-grid-pattern-animation-loop-blender-motion-graphics-t.md)
- [Powerful Light Trails in Blender 4.5 (tutorial)](./powerful-light-trails-in-blender-45-tutorial.md)
- [You Should Try this Blender Color Hack](./you-should-try-this-blender-color-hack.md)
