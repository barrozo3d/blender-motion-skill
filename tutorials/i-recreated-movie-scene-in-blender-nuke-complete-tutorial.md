---
title: I Recreated movie scene in Blender & Nuke | Complete  Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=iW6WF8guDMY
author: MISSING PIXEL VFX
ingested: 2026-05-18
blender_version: "Not specified"
tags: ["rendering", "compositing", "animation", "camera", "lighting", "materials", "intermediate", "advanced"]
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
Full VFX pipeline recreating a Kong: Skull Island shot using free Sketchfab assets (Kong, helicopter), Mixamo animation retargeting at epic scale (Kong at ~80m), a telephoto camera with 700m distance for cinematic compression, atmospheric volumetric lighting, and multi-pass Blender rendering composited in Nuke.

### Summary
MISSING PIXEL VFX walks through a complete VFX shot recreation from Kong: Skull Island using 100% free assets and tools. Kong and helicopter models are downloaded from Sketchfab (FBX/GLTF formats), fixed for materials, and imported into Blender. Kong is scaled to approximately 80m tall to match the film's scale. A Mixamo animation is retargeted onto Kong's rig. The helicopter is rigged with an Empty parent for the rotor blade spin animation. A telephoto camera (200–300mm focal length equivalent) is placed 700m away for the iconic scale-compression look. Atmospheric volume (Volume Scatter cube) creates the moody haze. Multi-pass rendering (Diffuse, Specular, Shadow, AO) outputs EXRs for compositing in Nuke. Nuke composite merges all passes with color correction and adds grain.

### Key Steps
1. Download **Kong model** from Sketchfab (FBX, ~6 MB) and **helicopter model** (GLTF) — both free
2. Import FBX into Blender: **File > Import > FBX** → fix any missing textures by reassigning Image Texture nodes to the correct maps
3. Scale Kong to ~80m height (S → Z → value); use a human figure (Rigify armature) as scale reference
4. Download a **Mixamo** walking/roaring animation → export as FBX → import and **retarget** the animation to Kong's rig using the NLA Editor or Action constraint
5. Parent helicopter rotor geometry to an **Empty** → keyframe Empty's Z Rotation: 0 on frame 1, 3600° on frame 100 for continuous blade spin
6. Position camera 700m away from Kong → set Focal Length: 200–400mm for telephoto compression effect that makes Kong appear impossibly large
7. Add a large **Volume Scatter cube** over the entire scene: Density 0.001–0.005; add a Sun Light at low angle for dramatic backlighting through the volume
8. Render multi-pass EXRs: enable **Render Passes** → Diffuse, Specular, Shadow, AO, Depth
9. Import all EXR passes into **Nuke** → use Merge nodes (Over, Plus) to combine passes → apply color correction, atmospheric haze grade, and film grain node

### Nodes / Settings
- FBX/GLTF Import — Scale: 0.01 (FBX) or 1.0 (GLTF) depending on source
- Kong scale — approximately 80m tall; set Scene Units to Meters for accuracy
- Mixamo animation retargeting — NLA Editor or Action constraint with Armature retarget add-on
- Empty (rotor) — Z Rotation keyframes 0→3600° over 30–60 frames for blade spin loop
- Camera — Focal Length: 200–400mm; Distance from subject: 600–800m
- Volume Scatter — Density: 0.001–0.005; Anisotropy: 0.5; large cube covering scene
- Sun Light — Energy: 5–10; low angle (-30°) for backlighting through volume
- Render Passes — Diffuse Direct/Indirect, Specular, Shadow, AO, Z-Depth; output as OpenEXR Multilayer
- Nuke composite — Merge (Over) for primary combine; Grade node for color; Grain node for film texture

### Difficulty
Intermediate

### Blender Version
Not specified

### Tags
#rendering #compositing #animation #camera #lighting #materials #intermediate #advanced

---

## Related Tutorials
- [Using Geometry Nodes for VFX in Blender](./using-geometry-nodes-for-vfx-in-blender.md)
- [Add VFX into Cinematic RAW+LOG Footage (the right way) | ACES Part 1](./add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-par.md)
- [A FULL Blender Compositor Course!](./a-full-blender-compositor-course.md)
- [Superhero Landing Tutorial 02 | Ground Destruction VFX in Blender](./superhero-landing-tutorial-02-ground-destruction-vfx-in-blen.md)
