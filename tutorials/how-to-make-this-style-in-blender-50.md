---
title: How To Make This Style in Blender 5.0
source: YouTube
url: https://www.youtube.com/watch?v=rbPOL9ibooY
author: Ducky 3D
ingested: 2026-05-19
blender_version: "5.0"
tags: [animation, curves, motion-design, shaders, compositing, intermediate]
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
**Transcript:** Has gone guys so in today's tutorial we are going to be making this animation. If you're not super comfortable with geometry nodes, don't worry. It's not a very big treat to make something really cool like this. First thing we're going to do is make a big stack of curves. Then immediately we're going to hop into the shading workspace where everything else is going to happen. So we're going to use a wave texture for the movement. We're going to randomize the position of the wave texture to get this really beautiful movement. Then using noise textures, we're going to add some really cool color. Then we're going to add some compositing to polish it off. If you want to check out the project file, that is available currently on Patreon. And this month I added a bunch of really cool tutorials that I personally just had a lot of fun working on. They're a little bit different than what I normally do. And they're just really cool. I'm working on a bigger video for here on YouTube. But for now, all of those tutorials are available exclusively on Patreon. You get everything. So check that out linked in the description. And with that being said, let's get into this tutorial. All right, so we a...



---

## Structured Notes

### Core Technique
Stacked curves with wave texture animation in Blender 5.0: a large stack of curve objects, wave texture driving position offset for organic flowing movement, randomised wave offsets per curve for the distinctive "each line has its own phase" look, noise textures for colour, compositor polish.

### Summary
18-minute motion graphics tutorial by Ducky 3D creating an animated stacked ribbon/curve effect. The key technique is using a Wave Texture (not for noise but for smooth periodic movement) on the curves' Y/Z position, with each curve having a randomised offset so the wave travels differently through each one — producing an organic flowing animation. Noise textures add a second layer of colour variation. All happens in the shader, not GeoNodes. Compositor Bloom and colour grading finish the look.

### Key Steps
1. **Stacked curves** — create a Bezier Curve or grid of horizontal lines; duplicate upward many times (Array modifier or manual duplication); Stack of ~30–50 parallel curves filling the frame
2. **Shader animation** — Shading workspace; Material for curves: Texture Coordinate (Object) → Mapping → Wave Texture; Wave Texture: Type Bands, Bands Direction Y or Z; plug Fac output into Set Position offset (via GeoNodes) or Displacement
3. **Randomise per curve** — key: each curve needs a different Wave Texture phase; use Object Info → Random output → Math (Add) → into Wave Texture Phase offset; now each curve has a unique phase = each ripples at different timing
4. **Wave settings** — Wave Texture: Scale (frequency), Distortion (adds turbulence to wave shape), Detail (sub-ripple detail), Roughness
5. **Animate wave** — keyframe Mapping → Location Y over time (or use driver: `#frame * 0.01`); wave scrolls across curves creating flowing motion
6. **Colour via noise** — second Noise Texture → Color Ramp (pick palette) → Emission Color; can use same Object Info Random for per-curve colour variation
7. **Emission strength** — moderate (5–15) so compositor bloom can add glow
8. **Compositor** — Glare (Bloom), Color Balance (contrast/saturation), Vignette for depth

### Nodes / Settings
- Wave Texture: Type Bands; Bands Direction Y; Scale 2–5; Distortion 1–3; Detail 2
- Object Info → Random → Math Add → Wave Texture Phase (per-object randomisation)
- Mapping → Location Y: animate with driver `#frame * speed` or keyframes
- Noise Texture → Color Ramp → Emission Color for colour variation
- Emission Strength 5–15 (for bloom catch)
- Compositor: Glare Bloom, threshold 0.8; Color Balance Lift/Gamma/Gain

### Difficulty
Intermediate

### Blender Version
5.0

### Tags
animation, curves, motion-design, shaders, compositing, intermediate

---

## Related Tutorials
- [[powerful-light-trails-in-blender-45-tutorial]] — similar stacked curve + wave aesthetic (Ducky 3D topographic series)
- [[a-new-way-to-loop-animations-in-blender]] — loop formula applicable to this wave animation
- [[sci-fi-grid-pattern-animation-loop---blender-motion-graphics-tutorial]] — similar noise/wave-driven motion loop
