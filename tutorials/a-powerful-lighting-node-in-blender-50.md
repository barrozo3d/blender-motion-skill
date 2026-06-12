---
title: A Powerful Lighting Node in Blender 5.0
source: YouTube
url: https://www.youtube.com/watch?v=BoCCxy9ec0g
author: Ducky 3D
ingested: 2026-06-12
blender_version: "Blender 5.0"
tags: [compositing, glare, sun-beams, glow, lighting, motion-graphics, eevee, cycles, ducky-3d, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/a-powerful-lighting-node-in-blender-50/
frame_count: 0
---

# A Powerful Lighting Node in Blender 5.0

**Source:** [YouTube](https://www.youtube.com/watch?v=BoCCxy9ec0g)
**Author:** Ducky 3D
**Duration:** 16m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** How's it going guys? So today we're going to talk about glow and glare and specifically sun beams. And in my opinion, the best way to use it in your motion graphics, how to make it shine. Now, I'm showing two animations here, roughly the same concept of lights moving up and down with the camera. Both of them are using the sun beams, but in completely different ways. One of them we're going towards subtlety, where you can kind of barely see that we're even using the beams. And then another one where the sun beams are basically the full star of the show. It's really going to come down to concept. The concept with the glass bricks, really it's the glass bricks that are shining and we're merely using the sun beams as a way to have more fun with the light and add a subtle detail. With this animation, the animation is almost designed around the sun beams to really make the sun beams shine and make them look really cool. So that's something that I'm always thinking about when it comes to using this glare. So today we're going to make this animation right here and we're going to lean toward really designing an animation around using it. So I'm going to show you guys how I get my glare to l...



---

## Structured Notes

### Core Technique
Using Blender's Compositing **Glare node** (Sun Beams mode) as a key design element in motion graphics — covering two distinct approaches: subtle accent (barely visible beams that enhance existing light) vs. feature element (animation designed specifically around the sun beams as the hero).

### Summary
16-minute motion graphics tutorial by Ducky 3D on designing animations around the Glare node's Sun Beams mode in Blender 5.0. Core insight: the success of sun beams depends on concept-first thinking — are the beams an accent or the star? Demonstrates both approaches with two complete animations: glass brick scene (beams as subtle detail) and a second scene where the camera and light movement is choreographed to make beams the focal point. Covers how to get glare to look good (threshold, streak length, angle offset) and how to animate lights for best beam effect.

### Key Steps

**Design Philosophy First:**
- Decide upfront: are beams an accent OR the hero?
- If accent: keep beams subtle, design the object/environment first
- If hero: design camera movement, light animation, and scene specifically to showcase beams

**Setting Up the Glare Node (Compositing):**
1. Render → Compositor (check Use Nodes)
2. Render Layers node → Glare node → Composite
3. Glare node → Type: **Sun Beams**
4. Key parameters:
   - **Threshold**: controls which bright pixels generate beams (lower = more beams from dimmer areas)
   - **Streaks**: number of beam rays
   - **Angle Offset**: rotation of beams
   - **Fade**: how quickly beams fade toward tips
   - **Iterations**: quality/length of beams

**Getting Good Sun Beams:**
- Light source needs to be visible/bright in the frame — beams emit from bright pixels
- Moving the light left/right changes beam angle dramatically
- Camera movement toward/away from light changes beam intensity
- Animate **Threshold** or **Fade** to pulse the beams

**Two-Animation Workflow:**
- Subtle approach: low threshold, short streaks, let scene geometry be the focus
- Hero approach: high contrast light source, long streaks, animate camera circling the light

### Nodes / Settings

**Compositor Glare Node — Sun Beams:**
```
Node: Glare
  Type: Sun Beams
  Threshold: 0.5–1.0    (lower = more pixels generate beams)
  Streaks: 4–8          (number of beam rays)
  Angle Offset: 0°–45°  (rotation)
  Fade: 0.8–0.95        (tip fade-off speed)
  Iterations: 3–5       (quality)
  Mix: -1 to 1          (blend between original and glare)
```

**Tip — Blending Glare:**
```
// Use Mix node to blend Glare output back over original render:
Render Layers → Glare → Mix node (Add or Screen) → Composite
// Gives finer control than Glare Mix parameter alone
```

### Difficulty
Intermediate — compositing setup is straightforward; getting it to look good requires design sense and iteration

### Blender Version
Blender 5.0

### Tags
compositing, glare, sun-beams, glow, lighting, motion-graphics, eevee, cycles, ducky-3d, intermediate

---

## Related Tutorials
- `tutorials/remove-noise-from-volumetrics-in-blender-50.md` — Other Blender 5.0 rendering tips
- `tutorials/my-circle-problem-in-blender-tutorial.md` — Ducky 3D animation workflow
