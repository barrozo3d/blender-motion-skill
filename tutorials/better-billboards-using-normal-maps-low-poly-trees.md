---
title: Better Billboards using Normal Maps (Low Poly Trees)
source: YouTube
url: https://www.youtube.com/watch?v=Ix-KT9a4PSo
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 3.4.1 -- observed in frame_000"
tags: [materials, shaders, procedural, rendering, cycles, lighting, organic, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/better-billboards-using-normal-maps-low-poly-trees/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Better Billboards using Normal Maps (Low Poly Trees)

**Source:** [YouTube](https://www.youtube.com/watch?v=Ix-KT9a4PSo)
**Author:** Blender Secrets
**Duration:** 1m34s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- WARNING: Thin transcript: 1057 chars. Notes may be shallow — consider --whisper-model small.

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In a previous video we used billboards to create a low poly forest with image planes.
[0:08] But did you know that you can take things to the next level by incorporating normal maps?
[0:12] These will allow your 2D trees to respond dynamically to lighting direction.
[0:17] Add an area light above a tree model, scale it up and give it enough power.
[0:23] In front orthographic view, match the camera to the viewport with CTRL ALT 0.
[0:29] Use a square scene format.
[0:31] Set camera to orthographic.
[0:35] Adjust the orthographic scale to frame the tree in the camera view.
[0:39] In Cycles enable transparent and rendered image.
[0:45] Save it as a PNG image with an alpha channel.
[0:50] Set viewport shading to solid and turn off overlays.
[0:54] Turn on matcap shading, set color to object and choose the normal colors matcap.
[1:00] Disable outline and any other viewport shading options.
[1:04] Under color management, set view transform to standard.
[1:08] Now render the normal map with the viewport render image.
[1:12] And save it.
[1:15] After we load these textures on a plane, when we rotate the HDRI you can see that the shadow
[1:21] is on the tree change.



---

## Captured Frames

- [0:22] tutorials/frames/better-billboards-using-normal-maps-low-poly-trees/frame_000.jpg
- [0:44] tutorials/frames/better-billboards-using-normal-maps-low-poly-trees/frame_001.jpg
- [0:56] tutorials/frames/better-billboards-using-normal-maps-low-poly-trees/frame_002.jpg
- [1:10] tutorials/frames/better-billboards-using-normal-maps-low-poly-trees/frame_003.jpg
- [1:18] tutorials/frames/better-billboards-using-normal-maps-low-poly-trees/frame_004.jpg

---

## Structured Notes

### Core Technique
Bake a 2D billboard tree (image-plane impostor) as two textures — a transparent color render and a matcap-derived normal map — so the flat billboard responds to scene lighting direction like real 3D geometry instead of looking flat/pasted-on.

### Summary
A follow-up to an earlier billboard/image-plane low-poly forest tutorial, adding dynamic lighting response via a normal map. Frame 000 shows a scaled-up, high-power Area Light placed above a full 3D tree model to light it for the bake. Frame 001 shows the first bake target: an F12 render still of the tree with a transparent (checkered) background — the color/alpha billboard texture. Frame 002 shows switching Viewport Shading to Matcap, Color set to Object, with the "normal" matcap selected — this recolors the tree by surface-normal direction (arrow calls out the Object color dropdign). Frame 003 shows the View menu open with "Viewport Render Image" being invoked to capture that matcap view as the normal-map bake, alongside Color Management's View Transform set to Standard (arrow highlights it) — critical so sRGB/Filmic tonemapping doesn't distort the normal-map colors. Frame 004 shows the final payoff: the baked billboard plane lit under a rotating HDRI/Sun, now showing directional shading and shadow falloff across the "tree" that changes as the light rotates, just like real geometry.

### Key Steps
1. Start from a real 3D tree model (not the billboard yet) — this is the bake source.
2. Add an Area Light above the tree, scale it up, and increase its Power enough to evenly light the model for a clean bake.
3. Switch to Front Orthographic view and snap the camera to match the viewport exactly with Ctrl+Alt+Numpad0.
4. Set the render Output format to a square resolution; set the camera to Orthographic and adjust its Orthographic Scale so the tree fits the frame.
5. **Bake pass 1 (color/alpha):** in Cycles, enable Film → Transparent, render the image (F12), and save it as a PNG with an alpha channel — this is the billboard's diffuse/opacity texture.
6. **Bake pass 2 (normal map):** switch Viewport Shading to Solid, turn off all overlays, enable Matcap shading, set matcap Color mode to Object, and pick the "normal" matcap (colors the surface by normal direction: blue = facing camera, red/green = facing sideways/up). Disable Outline and any other viewport shading extras that would contaminate the bake.
7. Under Color Management, set View Transform to Standard (not Filmic/AgX) so the matcap's RGB values map directly to normal-vector values without tonemapping distortion.
8. Use View → Viewport Render Image to capture this matcap-shaded view as a still, and save it — this becomes the normal map texture.
9. Load both baked textures (color+alpha, normal) onto a flat billboard plane's material (alpha for transparency/cutout, normal map plugged into the Normal input of the Principled BSDF). Rotating the HDRI/environment lighting now visibly changes shading and shadow direction across the flat billboard, matching how real 3D geometry would respond.

### Nodes / Settings
- **Lighting:** Area Light (scaled up, high Power) for the bake pass.
- **Camera:** Orthographic projection, square render resolution, Orthographic Scale tuned to frame the subject, Ctrl+Alt+Numpad0 to align camera to viewport.
- **Render (Cycles):** Film → Transparent enabled for the color/alpha bake.
- **Viewport Shading:** Solid shading, Matcap enabled, Color = Object, matcap = "normal"; Outline and other overlays disabled.
- **Color Management:** View Transform = Standard (not Filmic/AgX) during the normal-map capture.
- **Capture method:** View → Viewport Render Image (not F12) for the matcap/normal-map bake, vs. F12 render for the color/alpha pass.
- **Shader (implied downstream use):** billboard material's Principled BSDF Normal input fed by the baked normal-map texture; Alpha from the color bake for cutout transparency.

### Difficulty
Intermediate

### Blender Version
Not specified — Cycles-based workflow with matcap viewport shading and modern Color Management naming (Standard/Filmic/AgX terminology), consistent with Blender 3.x-5.x.

### Tags
materials, shaders, procedural, rendering, cycles, lighting, organic, intermediate

---

## Related Tutorials
- [5 Lighting SECRETS in Blender](5-lighting-secrets-in-blender.md) — shares lighting, cycles, rendering, shaders, intermediate; complementary lighting-fakery techniques.
- [How to Texture Realistic Buildings in Blender](how-to-texture-realistic-buildings-in-blender-b3d.md) — shares materials, shaders, procedural, intermediate; same baked-detail-onto-flat-surface philosophy.
