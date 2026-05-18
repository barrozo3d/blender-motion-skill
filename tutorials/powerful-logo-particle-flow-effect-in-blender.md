---
title: Powerful Logo Particle Flow Effect in Blender
source: YouTube
url: https://www.youtube.com/watch?v=TTGcr-45jCE
author: Ducky 3D
ingested: 2026-05-18
blender_version: "Not specified"
tags: ["geometry-nodes", "particles", "particles-reveal", "animation", "logo-animation", "typography", "materials", "shaders", "motion-design", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/powerful-logo-particle-flow-effect-in-blender/
frame_count: 0
---

# Powerful Logo Particle Flow Effect in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=TTGcr-45jCE)
**Author:** Ducky 3D
**Duration:** 16m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** How's it going guys? So today we are gonna be creating this in Blender. It's really cool and it is part of the series I'm doing here on YouTube about using Blender like it's Photoshop, like it's After Effects and creating Text Effects, Things on Images and this is a really cool one. First we'll use the Text tool, pick a font, get our text to say whatever we want it to and then we can head into Geometry Nodes and distribute some points on that text. After that it's pretty easy. We'll just do a small set of noise textures to display it and then get some of the parts to display and some of the parts to not display so we can still read the text but get this really interesting displacement. After that we will just use the noise texture to shade the particles and we'll be totally done. Here on YouTube I have several other tutorials in this theme about using Blender like it's Photoshop, like it's After Effects and running Images and logos and text through it to make some cool stuff. So check out the playlist below for more tutorials in this theme and over on Patreon I have a couple exclusive tutorials in this series so you can learn even more stuff. Check out all that and it's the end of ...



---

## Structured Notes

### Core Technique
Converts text or logos into a dusty particle flow effect using Geometry Nodes: Distribute Points on Faces with selective two-Noise-Texture displacement — some areas stay readable while others stream away — with particles colored procedurally via Noise Texture + Color Ramp in an Emission shader.

### Summary
Ducky 3D treats Blender like Photoshop/After Effects to create a text/logo particle effect. A text object (or SVG logo import) is converted to a mesh face; Distribute Points on Faces places ~10,000 tiny particles on it. Two Noise Textures control which particles stay readable and which disperse: the first Noise creates a displacement mask (particles in dark areas of the mask move far away, particles in bright areas stay in place), mixed via a Mix Vector node so some text regions remain legible while others stream into dust. A second Noise Texture drives the Emission color of each particle through a Color Ramp, giving the dust a gradient color range (gold, orange, white, etc.). The tiny particles are rendered as small spheres (Point instances or tiny Icosphere instances).

### Key Steps
1. Add a **Text Object** (Shift+A → Text) → Tab into edit mode → type desired text → set Font in Object Data Properties; or import an SVG logo (File → Import → SVG)
2. With text selected: **Object → Convert → Mesh** to convert text curves to a mesh
3. In Edit Mode: select all faces → **Face → Fill** to ensure faces exist for particle distribution
4. Add **Geometry Nodes** modifier → New → add **Distribute Points on Faces**: Density: 10,000+; Seed: 0
5. Add first **Noise Texture** → **Color Ramp** → use Color Ramp as a mask: white areas = particles stay, black areas = particles displace
6. Add **Set Position**: Offset driven by **Mix Vector** node — Input A: zero vector (no move), Input B: **second Noise Texture** × large offset (5–10 m); Factor: Color Ramp mask from step 5
7. For color: add third **Noise Texture** → **Color Ramp** (gold/orange/white gradient) → **Emission** shader, Strength: 3–10; assign to particle instances
8. Add **Instance on Points** → Object: tiny **Icosphere** (Radius: 0.005–0.02) for the particle shape; or use **Points** directly if rendering in Cycles with Shader to RGB
9. Animate the displacement by keyframing the Noise Texture **W** value (or an Offset vector) from 0 to 1 over the timeline for the streaming effect
10. Render in Cycles or Eevee; add **Glare Bloom** in compositor for glow

### Nodes / Settings
- Text Object — converted to Mesh; Face fill required for Distribute Points on Faces
- Distribute Points on Faces — Density: 8,000–15,000; Seed: varies
- Noise Texture 1 (mask) — Scale: 2–5; output → Color Ramp (threshold at ~0.5) → boolean mask
- Mix Vector — Factor: Color Ramp mask; A: zero offset; B: Noise 2 × displacement strength (5–15 m)
- Noise Texture 2 (displacement) — Scale: 1–3; W animated 0→1 for streaming motion
- Noise Texture 3 (color) — Scale: 3–8; Color Ramp (gold/white/orange palette)
- Emission shader — Strength: 3–15; Color: from Noise 3 Color Ramp
- Instance on Points — Icosphere Radius: 0.005–0.02 m for particle size
- Compositor Glare — Fog Glow type; Threshold: 0.8; adds glow to bright emission particles

### Difficulty
Intermediate

### Blender Version
Not specified

### Tags
#geometry-nodes #particles #particles-reveal #animation #logo-animation #typography #materials #shaders #motion-design #intermediate

---

## Related Tutorials
- [Create Text in Geometry Nodes! (Blender Tutorial)](./create-text-in-geometry-nodes-blender-tutorial.md)
- [Blender Tutorial - Eternals Gold Wireframe Animation](./blender-tutorial-eternals-gold-wireframe-animation.md)
- [Powerful Light Trails in Blender 4.5 (tutorial)](./powerful-light-trails-in-blender-45-tutorial.md)
- [Art Stream #27: Nodes, nodes, nodes! [Blender / Geometry Nodes]](./art-stream-27-nodes-nodes-nodes-blender-geometry-nodes.md)
