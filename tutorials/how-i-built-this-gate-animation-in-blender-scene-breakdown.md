---
title: How I Built This Gate Animation in Blender | Scene Breakdown
source: YouTube
url: https://www.youtube.com/watch?v=upUPrc35DYw
author: Max Hay
ingested: 2026-05-18
blender_version: "Not specified"
tags: ["animation", "motion-design", "camera", "compositing", "rendering", "materials", "shaders", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/how-i-built-this-gate-animation-in-blender-scene-breakdown/
frame_count: 0
---

# How I Built This Gate Animation in Blender | Scene Breakdown

**Source:** [YouTube](https://www.youtube.com/watch?v=upUPrc35DYw)
**Author:** Max Hay
**Duration:** 22m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** In this video, I'm going to show you a quick breakdown of how I made this animation right here. So we'll start in this flat file, I'll just quickly show you around and then we'll jump into a new empty file where I'll show you how I made the complex door opening animation here. That's actually a lot simpler than it looks here, but we'll go into that. And then we'll come back to this file for an overview on the textures and lighting and just how I'm dealing with all that. So yeah, it should be a fun one. Hopefully enjoy the video and yeah, we'll just get into it. Okay, so there is a lot going on here, but I'm going to open up a new file with a really basic block block out version of this and just show you my basic process that I was following to create this effect. And everything in here is basically following that idea that I'm about to show you, which is basically just keyframing it and making it move in a really simple way. This is kind of just a lot of the same thing repeated over and over again. And hopefully when we return here in a few minutes, this should make a lot more sense. There's a lot of stuff happening here that is making this harder to look at, especially with the ov...



---

## Structured Notes

### Core Technique
Breaks down a complex sci-fi gate opening animation by showing that the visual complexity comes entirely from layered materials and particles on top of very simple location keyframes — the gate panels slide outward with Mirror modifier for symmetry, and staggered timing creates sequential choreography.

### Summary
Max Hay demonstrates that intimidating-looking animations are often built from simple building blocks. The gate animation uses basic location keyframes (G → X/Y → value → Enter) for each panel, with the Mirror modifier ensuring left/right symmetry from a single set of keyframes. Staggered frame offsets (every 5–10 frames later per panel) create the sequential reveal effect. The Graph Editor is used to ease in/out each movement for smooth motion. The visual richness comes from the shader layer: emissive wireframe texture, glowing edge emission, and a particle system emitting sparks at the gate seam — all of which run independently of the animation rig. Lighting uses Area Lights with emissive surface colors to match the neon palette.

### Key Steps
1. Block out gate geometry: simple rectangular panels in edit mode → apply **Mirror modifier** on the X axis for symmetrical left/right panels
2. Set keyframes on each panel's X Location: frame 0 (closed position), frame 30 (open position) → I key → Location
3. Open **Graph Editor** → select all F-curves → T → select **Ease In/Out** interpolation for smooth deceleration
4. Stagger timing: select the second row's keyframes in the Graph Editor → G → X → shift them 8–10 frames right; repeat for each successive row for the sequential gate reveal
5. For the look: assign an **Emission** shader to the edge geometry with high Strength (10–50) in the gate panel material for glowing edges
6. Add a **Wireframe modifier** or use the Wireframe node in the shader for the emissive grid pattern on gate surfaces
7. Add a **Particle System** at the gate seam center: Hair type, render as **Object** (small icosphere), low gravity, high initial velocity for spark burst on opening frame
8. Add **Area Lights** colored to match the neon palette (cyan/blue) at low position behind the gate for dramatic backlight

### Nodes / Settings
- Mirror modifier — Axis: X; Bisect: on to clip center geometry
- Location keyframes — frame 0: closed; frame 20–30: fully open; ease in/out interpolation
- Graph Editor — G + X to shift keyframe timing for stagger; Ease In/Out (T menu)
- Emission shader — Strength: 10–50 for bright neon glow; connected to gate edge geometry
- Wireframe node (shader) — Pixel Size: on; used to generate edge highlight mask
- Particle System — Number: 500–2000; Lifetime: 20–40; Velocity: Normal 2–5 for spark burst
- Area Light — Size: 2–4 m; Energy: 200–1000 W; Color: cyan/blue for sci-fi palette

### Difficulty
Intermediate

### Blender Version
Not specified

### Tags
#animation #motion-design #camera #compositing #rendering #materials #shaders #intermediate

---

## Related Tutorials
- [Mastering Blender's Graph Editor](./mastering-blenders-graph-editor.md)
- [Creating an Underground Scene in Blender (Step by Step)](./creating-an-underground-scene-in-blender-step-by-step.md)
- [How to Make Cyberpunk Scenes in Blender](./how-to-make-cyberpunk-scenes-in-blender.md)
- [3 Easy Lighting Setups | Blender Tutorial](./3-easy-lighting-setups-blender-tutorial.md)
