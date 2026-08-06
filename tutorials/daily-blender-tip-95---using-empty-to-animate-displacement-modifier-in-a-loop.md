---
title: Daily Blender Tip 95 - Using Empty To Animate Displacement Modifier In A Loop
source: YouTube
url: https://www.youtube.com/watch?v=FIYZk64PsWY
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Displacement modifier with Empty texture coordinates, Follow Path constraint, and Linear key interpolation are version-agnostic core Blender features"
tags: [procedural, animation, materials, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-95---using-empty-to-animate-displacement-modifier-in-a-loop/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 95 - Using Empty To Animate Displacement Modifier In A Loop

**Source:** [YouTube](https://www.youtube.com/watch?v=FIYZk64PsWY)
**Author:** Blender Secrets
**Duration:** 1m51s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 22 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (22 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] Sex Nebula in modeling



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-95---using-empty-to-animate-displacement-modifier-in-a-loop/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-95---using-empty-to-animate-displacement-modifier-in-a-loop/frame_001.jpg
- [0:45] tutorials/frames/daily-blender-tip-95---using-empty-to-animate-displacement-modifier-in-a-loop/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-95---using-empty-to-animate-displacement-modifier-in-a-loop/frame_003.jpg
- [1:30] tutorials/frames/daily-blender-tip-95---using-empty-to-animate-displacement-modifier-in-a-loop/frame_004.jpg
- [1:45] tutorials/frames/daily-blender-tip-95---using-empty-to-animate-displacement-modifier-in-a-loop/frame_005.jpg

---

## Structured Notes

### Core Technique
Driving a **Displacement modifier**'s Clouds-texture coordinates with an **Empty** object instead of the object's own transform — since the Empty's position/rotation directly shifts where the noise texture samples the surface, animating the Empty along a circular **Path** (with Follow Curve) produces a continuously evolving, organic surface displacement that loops seamlessly when the key interpolation is set to **Linear**.

### Summary
Frame 000 shows a subdivided sphere/cube base mesh with the Add Modifier menu open, captioned "Subdivide your default cube a few times. Add a displacement modifier with a cloud texture." Frame 001 shows the resulting object now visibly bumpy/lumpy from the cloud-textured displacement, shaded smooth, captioned "Set the cube to smooth shading and add another subdivide modifier under the displacement modifier" — extra subdivision after displacement smooths out faceting on the deformed surface. Frame 002 shows the bumpy sphere with an Empty (axis cross) placed at its center, captioned "Add an empty to the scene. In the displacement modifier choose the empty for the texture coordinates." — reassigning the Displacement modifier's Texture Coordinates source from Object/Generated to the Empty. Frame 003 shows the same sphere with a faint circular path line around it, captioned "Now the empty position and rotation influence the displacement. Now a path and let the empty follow it" — adding a Curve for the empty to travel along via a Follow Path constraint, so its motion becomes the trigger for changing displacement pattern. Frame 004 shows the finished bumpy sphere with a mottled, cloud-like texture, mid-animation. Frame 005 shows the Dope Sheet with the animation keys, captioned "Set the key interpolation type to linear in the Dope sheet so the animation loops at constant speed" — Linear interpolation avoids the ease-in/ease-out speed changes that Bezier keys would otherwise introduce, keeping the seamless loop's playback speed constant.

### Key Steps
1. Subdivide a base mesh (cube/sphere) a few times, then add a **Displacement** modifier with a **Clouds** procedural texture for organic bumpy surface detail.
2. Set the object to **Smooth Shading** and add a second **Subdivision Surface** modifier positioned *below* the Displacement modifier in the stack, to smooth out faceting on the newly-displaced geometry.
3. Add an **Empty** to the scene, then in the Displacement modifier's **Texture Coordinates**, change the source from the default (Object/Generated) to this **Empty** — the empty's transform now directly controls where in the noise texture the displacement samples from.
4. Add a **Curve** (circular path) and give the Empty a **Follow Path** constraint targeting it, so animating the path-following motion continuously moves the empty (and therefore the sampled texture region) over time.
5. In the **Dope Sheet**, select all animation keys and set their **Interpolation** to **Linear** (instead of the default Bezier ease-in/ease-out) — this keeps the loop playing at a constant, unchanging speed so the animation cycles seamlessly.

### Nodes / Settings
- **Modifier stack order:** Displacement (Clouds texture, Texture Coordinates = Empty) → Subdivision Surface (smooths post-displacement faceting).
- **Object:** Empty — assigned as the Displacement modifier's texture coordinate source.
- **Constraint:** Follow Path — animates the Empty along a Curve, driving continuously-changing displacement.
- **Dope Sheet:** Key > Interpolation Mode > Linear — for constant-speed seamless looping.

### Difficulty
Intermediate

### Blender Version
Not specified — Displacement modifier with Empty texture coordinates, Follow Path constraint, and Linear key interpolation are version-agnostic core Blender features.

### Tags
procedural, animation, materials, intermediate

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover using an Empty as a Displacement modifier's texture coordinate source.
