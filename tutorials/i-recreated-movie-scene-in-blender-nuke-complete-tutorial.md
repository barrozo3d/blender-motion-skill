---
title: I Recreated movie scene in Blender & Nuke | Complete  Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=iW6WF8guDMY
author: MISSING PIXEL VFX
ingested: 2026-05-19
blender_version: "4.x"
tags: [vfx, compositing, rendering, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/i-recreated-movie-scene-in-blender-nuke-complete-tutorial/
frame_count: 0
---

# I Recreated movie scene in Blender & Nuke | Complete  Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=iW6WF8guDMY)
**Author:** MISSING PIXEL VFX
**Duration:** 44m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hello friends welcome back. Today we are going to recreate the shot in blender and nuke and I'm going to use all the free assets and I will also provide the renders and the project file. With that you can learn something new. Before I start this video I want to say something first. Thanks a lot everyone. Last week my channel crossed 4000 subscribers. I know this number sounds very less but for me it's another step towards this success so I'm really happy with that. They love me. Let's go and start it. First we'll download all the assets we need. I'll go to Sketchfab. I will search for Kong and we have this element. This is really good for the short. I'm going to download this as a fix because it's not heavy. I think this is only 6 MB so I'll just download it and we will also search for help us. I'll try to attach it. This is really good model and I'm going to use this one too. I download and this time I'm going to download this as GLTF. The power jet place is too heavy so I think this is going to work here. Once I download the assets I will bring them into blender and check if the texture and everything is working fine. If not I will just fix it and then I'm going to use it for fur...



---

## Structured Notes

### Core Technique
Professional VFX pipeline recreating a movie scene: free Sketchfab assets (Kong, helicopter) imported into Blender for 3D CG elements, rendered with multi-pass EXR output, then composited in Nuke with environment plates and colour grading for a production-quality result.

### Summary
44-minute complete VFX pipeline tutorial by MISSING PIXEL VFX. Downloads free Sketchfab assets (King Kong character, helicopter model), imports into Blender, sets up camera, lighting and materials for the CG elements, renders multi-pass EXR, then takes everything into Nuke for compositing with a background plate. Full render + composite workflow covering the gap between Blender and professional comp software. Project files and renders provided free.

### Key Steps
1. **Asset sourcing** — Sketchfab.com: search Kong → download as FBX (light file); search helicopter → download as GLTF; free assets only
2. **Import into Blender** — File → Import → FBX/GLTF; check textures loaded correctly; fix any material issues; scale assets to match scene
3. **Scene assembly** — position Kong and helicopter relative to each other; add camera matching the reference movie shot angle; use reference image in viewport (N-panel → View → Background Images)
4. **Lighting** — HDRI matching reference shot environment; add Sun/Area lights to reinforce key light direction; render preview frequently to match reference
5. **Materials** — Principled BSDF; if imported textures are wrong type (roughness/normal), fix node connections; add displacement for ground/surface detail
6. **Render passes** — View Layer Properties → enable: Combined, Diffuse (Direct/Indirect/Color), Glossy, Shadow, Z-depth; Output: OpenEXR MultiLayer; renders all passes in one file
7. **Nuke compositing** — import EXR MultiLayer (Read node → auto-detects all passes); import background plate; grade background to match CG lighting; Alpha Over to combine CG over plate; use ZDefocus or ZBlur node with Z-depth pass for depth of field; colour grade full composite
8. **Nuke colour grade** — Grade node for lift/gamma/gain per channel; ColorCorrect for hue/saturation; match CG colour temperature to background plate; add grain

### Nodes / Settings
- Blender: HDRI world + Sun Light for primary illumination; Shadow Catcher on ground plane
- EXR MultiLayer output: enables per-pass isolation in Nuke
- Nuke: Read node (auto-loads EXR multi-pass), Shuffle node to extract individual passes, Grade/ColorCorrect, ZDefocus, Alpha Over, Merge (Over)
- FBX import: Blender File → Import → FBX; GLTF: File → Import → GLTF
- Asset check: always verify textures and materials after import; look for broken Normal/Roughness channel connections

### Difficulty
Intermediate

### Blender Version
4.x

### Tags
vfx, compositing, rendering, intermediate

---

## Related Tutorials
- [[add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2]] — similar multi-pass Blender→compositor workflow using ACES
- [[a-full-blender-compositor-course]] — Blender compositor alternative if Nuke not available
- [[superhero-landing-tutorial-02-ground-destruction-vfx-in-blender]] — VFX scene composition in Blender only
