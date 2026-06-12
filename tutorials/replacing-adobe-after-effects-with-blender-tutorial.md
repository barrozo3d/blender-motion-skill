---
title: Replacing Adobe After Effects with Blender (tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=ZK92Uuhiesg
author: Ducky 3D
ingested: 2026-06-12
blender_version: "Blender 4.x+"
tags: [motion-graphics, 2d-animation, voronoi, wave-texture, shader-animation, masking, after-effects-alternative, procedural, ducky-3d, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/replacing-adobe-after-effects-with-blender-tutorial/
frame_count: 0
---

# Replacing Adobe After Effects with Blender (tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=ZK92Uuhiesg)
**Author:** Ducky 3D
**Duration:** 16m42s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** How's it going guys? Today we are going to make this animation. It's really cool and it's completely made from basic textures. This tutorial is part of a series of tutorials where we're using Blender in a similar way that we would use Photoshop or After Effects. The theme of today's is creating beautiful animations just from 2D textures and giving it kind of a 3D feel and animating it in a really cool, interesting way. So if you want to check out more from this series, there's a YouTube playlist linked in the description. So here's the steps that we're going to go through to make this animation. First we're going to get just a basic Voronoid texture. Then we'll get a wave texture combined those so that it twists the Voronoid texture in a circular way. Then we're going to get three masks. We're going to create an outer mask. We're going to create an inner mask. And then we're going to create a third mask to have variations in lighting and be able to animate that as well. After that all we'll need to do is spin the canvas, animate all of the nodes so that they move, and we will be done. If you like the subject, there's actually bonus content from this using Blender like After Effects...



---

## Structured Notes

### Core Technique
**2D shader animation as After Effects replacement** — use a Voronoi texture distorted by a Wave texture (in circular/twist mode) to create a dynamic swirling pattern on a flat plane. Layer three procedural masks (outer boundary, inner cutout, lighting variation) on top and animate all texture nodes to make the whole thing spin and flow. No rigging, no AE, just shader nodes.

### Summary
16-minute tutorial (part of Ducky 3D's "Using Blender like After Effects" series) for making a beautiful looping 2D animation entirely from procedural shader nodes. The core trick is using a Wave texture as a warp/distort input for a Voronoi texture, creating a circular swirling look without any mesh deformation. Three procedural masks control the shape and lighting variety. The canvas spins and all nodes animate for a finished loop. Part of a broader series using Blender as a motion graphics tool.

### Key Steps

**Overview Flow:**
```
Voronoi Texture (base pattern)
  ↕ distorted by
Wave Texture (circular warp)
  ↕ masked by
Outer Mask + Inner Mask + Lighting Variation Mask
  ↕ animated by
Spinning canvas + node value animation
```

**Step 1 — Base Voronoi Pattern:**
1. Plane mesh → Material → Shader Editor
2. Add **Voronoi Texture**
3. Add **Texture Coordinate** → Object → into Voronoi Vector input
4. Adjust Scale for desired cell density

**Step 2 — Wave Texture Warp (circular twist):**
1. Add **Wave Texture**
2. Set Wave texture **Type: Rings** (creates circular/radial pattern)
3. Connect the Wave output into a **Vector Math** or **Mapping** node that feeds into the Voronoi Vector
4. This causes Voronoi cells to twist/distort in circular rings

**Step 3 — Three Masks:**
- **Outer Mask**: ring or gradient that vignettes the edges (keeps animation inside a circle)
- **Inner Mask**: smaller circle cutout in the center (creates ring/donut shape)
- **Lighting Variation Mask**: animated gradient that fakes highlight/shadow variation as canvas spins

**Step 4 — Combine & Animate:**
1. Use **Mix Color** or **Multiply** nodes to apply masks to the Voronoi pattern
2. Add **Mapping** node on overall coordinates → keyframe Z Rotation to spin the canvas
3. Keyframe individual texture **Scale** or **Phase** values over time for flow animation
4. Loop by making last frame match first frame values

### Nodes / Settings

**Core Shader Structure:**
```
Texture Coordinate (Object) →
  Wave Texture (Rings, animated phase) →
    [used as distortion vector] →
      Voronoi Texture (distorted by wave) →
        [pattern]

Gradient (circular outer mask) → [mask]
Gradient (inner circular cutout) → [mask]  
Wave/Noise (lighting variation) → [mask]

Pattern × Outer Mask × Inner Mask → Mix Color →
  Lighting Variation applied as multiply →
    Emission Shader → Material Output

// Animation:
Mapping Z Rotation: spin canvas (0° → 360° over N frames)
Wave Phase: animate for flow
Voronoi Scale or W: animate for variation
```

### Difficulty
Intermediate — requires familiarity with shader nodes and animation keyframing

### Blender Version
Blender 4.x+ (part of a series; Ducky 3D content is typically current-version compatible)

### Tags
motion-graphics, 2d-animation, voronoi, wave-texture, shader-animation, masking, after-effects-alternative, procedural, ducky-3d, intermediate

---

## Related Tutorials
- `tutorials/real-time-caustics-in-blender-51.md` — Another Voronoi texture technique
- `tutorials/my-circle-problem-in-blender-tutorial.md` — Ducky 3D wave texture on curves (related technique)
- `tutorials/a-powerful-lighting-node-in-blender-50.md` — Ducky 3D compositing glare
