---
title: How I Built This Gate Animation in Blender | Scene Breakdown
source: YouTube
url: https://www.youtube.com/watch?v=upUPrc35DYw
author: Max Hay
ingested: 2026-05-19
blender_version: "4.x"
tags: [animation, mechanical, modeling, intermediate]
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
Complex-looking gate animation achieved through simple keyframed transforms repeated with timing offsets — each gate element has the same basic open/close motion keyframed individually with slight delays, creating the illusion of a sophisticated mechanical system.

### Summary
22-minute scene breakdown by Max Hay revealing that an impressive gate/portal animation is simpler than it looks: the core mechanic is just keyframed rotation/translation on each gate element, with the animation staggered across elements by a frame offset. Max walks through his blockout workflow (simple cubes first, then add details), covers how to handle the complex door-opening mechanics, and returns to the final scene for texture and lighting breakdown.

### Key Steps
1. **Blockout first** — use simple cubes to establish the gate proportions, pivot points, and motion before adding any geometric detail; verify the animation reads correctly at blockout stage
2. **Core animation** — each gate element (bar, panel, pillar segment) has the same basic keyframe animation: position or rotation from closed → open position; set over ~30 frames
3. **Stagger timing** — offset the start frame of each element's animation by a few frames (e.g. every 3 frames); this creates the domino/cascade effect of the gate opening — complex look, trivial setup
4. **Pivot points** — set each element's origin to its hinge/pivot point before keyframing; Object → Set Origin → Origin to 3D Cursor (with cursor placed at hinge)
5. **NLA Editor for reuse** — push down animations; duplicate strips; offset time for multi-gate or repeating use
6. **Texturing** — PBR textures (metal, rust, concrete) using Poliigon or free sources; Principled BSDF; UV unwrap each element individually
7. **Lighting** — dramatic spotlights with volume scatter cube for atmosphere; matches the 3-lighting-setups approach (Setup 1 style)

### Nodes / Settings
- Object → Set Origin → Origin to 3D Cursor (for hinge pivot placement)
- Keyframe: R/G/S + axis + value; I key to insert; on rotation channel
- NLA Editor: Action → Push Down; strip Start Frame to stagger timing
- PBR workflow: Poliigon textures; Principled BSDF; Normal Map node; Roughness map
- Volume scatter cube (same as 3-easy-lighting-setups-blender-tutorial): Density 0.02, Anisotropy 0.5

### Difficulty
Intermediate

### Blender Version
4.x

### Tags
animation, mechanical, modeling, intermediate

---

## Related Tutorials
- [[your-guide-to-mechanical-rigging-in-blender-robot-arm-tutorial]] — rigged mechanical animation (alternative to keyframing)
- [[3-easy-lighting-setups-blender-tutorial]] — lighting approach used in this gate scene
- [[the-complete-blender-3d-animation-course-5-hours-blender-b3d-animation]] — keyframing fundamentals underlying this technique
