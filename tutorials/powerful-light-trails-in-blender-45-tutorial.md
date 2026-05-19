---
title: Powerful Light Trails in Blender 4.5 (tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=965bgIUHoxA
author: Ducky 3D
ingested: 2026-05-19
blender_version: "4.5"
tags: [animation, curves, shaders, materials, motion-design, lighting, intermediate]
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
Looping topographic light-trail animation in Blender 4.5: duplicated displaced curves with a camera-parented gradient texture driving a glowing emission shader, wave texture for bright focal curves, metallic floor reflection.

### Summary
23-minute motion design tutorial creating a looping animated topographic map aesthetic with glowing light trails. Core technique is parenting a gradient texture object to the camera so it travels through the curve field as the camera moves, creating the illusion of animated trails without keyframing each curve. Part of a 4-tutorial topographic map series.

### Key Steps
1. **Duplicate curves** — create base curve (or line), duplicate array across the ground plane; position carefully for even spacing
2. **Displace curves** — add Displace modifier to curve objects; use a Texture (clouds/noise) to push curves vertically, creating topographic hill/valley shapes; tune texture scale and strength
3. **Convert to mesh** — curves need mesh conversion for Displace modifier to work correctly; or use Geometry Nodes
4. **Camera-parented gradient** — create an Empty or object, parent it to the camera; assign a gradient texture mapped to this object's local space; as camera moves, gradient sweeps through the scene
5. **Emission glow shader** — assign material with Emission shader; plug gradient result into Emission Strength; curves close to the gradient peak glow brighter
6. **Wave texture focal point** — add Wave Texture node mapped to world Y (or curve position); use it to select center curves and boost their emission, creating a bright focal line
7. **Metallic floor** — plane with Principled BSDF, Metallic=1, low Roughness for reflective ground
8. **Loop setup** — ensure camera animation is a perfect loop; gradient travels full scene width in loop duration

### Nodes / Settings
- **Displace modifier** — driven by Clouds texture; Strength and texture Scale control terrain shape
- **Shader nodes**: Gradient Texture (parented to camera), Wave Texture (scene-space), Emission, Mix Shader
- **Gradient parented to camera** — key technique: Object Texture Coordinates → object = camera-parented empty
- Wave Texture: Bands type, Scale ~5–10, mapped to Generated or Object coords on curve/mesh
- Bloom (Render Properties → Bloom) or Compositor glare for the glow effect
- Principled BSDF floor: Metallic=1.0, Roughness 0.05

### Difficulty
Intermediate

### Blender Version
4.5

### Tags
animation, curves, shaders, materials, motion-design, lighting, intermediate

---

## Related Tutorials
- [[powerful-logo-particle-flow-effect-in-blender]] — another motion design loop by Ducky 3D style
- [[sci-fi-grid-pattern-animation-loop---blender-motion-graphics-tutorial]] — grid-based motion loop
- [[you-should-try-this-blender-color-hack]] — color/shader techniques
