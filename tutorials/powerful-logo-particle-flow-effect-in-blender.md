---
title: Powerful Logo Particle Flow Effect in Blender
source: YouTube
url: https://www.youtube.com/watch?v=TTGcr-45jCE
author: Ducky 3D
ingested: 2026-05-19
blender_version: "4.x"
tags: [geometry-nodes, motion-design, text, shaders, particles, intermediate]
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
Logo/text particle flow effect: convert text to points in Geometry Nodes, displace points with animated noise textures showing only some particles to preserve legibility, shade with matching noise for a flowing particle aesthetic.

### Summary
16-minute motion design tutorial from Ducky 3D's "Blender as Photoshop/After Effects" series. Converts a text object to scattered points using Geometry Nodes, applies two noise textures — one for XY displacement and one to mask which particles are visible — so the text remains partially readable while particles flow around it. Noise texture also drives the particle shading color.

### Key Steps
1. **Text setup** — Add Text object (`Shift+A → Text`); choose font; set text content in Edit Mode
2. **Geometry Nodes** — Add GeoNodes modifier to text object; use `Distribute Points on Faces` (or `Distribute Points in Volume`) to scatter points across the text surface
3. **Displace points** — `Set Position` node with `Noise Texture` plugged into Offset; tune Scale and Strength to get flowing displacement
4. **Visibility mask** — second `Noise Texture` → `Color Ramp` → use result to drive `Delete Geometry` or `Set Point Radius` to 0; parts below threshold disappear, keeping some text readable
5. **Instance geometry** — small `Ico Sphere` or cube instanced on the visible points for the particle look
6. **Shader** — noise texture in shader (same or similar to GeoNodes noise) driving emission color; creates consistent color-flow matching the displacement

### Nodes / Settings
- `Distribute Points on Faces` — scatter source, density controls particle count
- `Set Position` + `Noise Texture` — displacement; Scale for texture size, Strength for displacement amount
- Second `Noise Texture` → `Color Ramp` → masking/visibility control
- `Delete Geometry` — removes points below noise threshold
- `Instance on Points` with small mesh (icosphere/cube)
- Shader: `Noise Texture` → `Color Ramp` → `Emission` for glowing particle color
- Animate noise `W` value (4D noise offset) for flowing motion without moving particles

### Difficulty
Intermediate

### Blender Version
4.x

### Tags
geometry-nodes, motion-design, text, shaders, particles, intermediate

---

## Related Tutorials
- [[powerful-light-trails-in-blender-45-tutorial]] — same author (Ducky 3D), topographic loop series
- [[sci-fi-grid-pattern-animation-loop---blender-motion-graphics-tutorial]] — noise-driven motion loop
- [[blender-tutorial---eternals-gold-wireframe-animation]] — logo/text animation technique
