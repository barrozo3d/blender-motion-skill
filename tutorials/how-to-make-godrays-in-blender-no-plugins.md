---
title: How to make Godrays in Blender ( NO PLUGINS )
source: YouTube
url: https://www.youtube.com/watch?v=alDV81qXQtA
author: Vlabs
ingested: 2026-08-02
blender_version: "Not specified"
tags: [volume, lighting, cycles, rendering, beginner]
extraction_status: complete
frames_dir: tutorials/frames/how-to-make-godrays-in-blender-no-plugins/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How to make Godrays in Blender ( NO PLUGINS )

**Source:** [YouTube](https://www.youtube.com/watch?v=alDV81qXQtA)
**Author:** Vlabs
**Duration:** 2m8s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] You want to turn your render from this into this? Same scene, same model, same camera.
[0:07] The only difference is volumetrics. I'm going to show you exactly how to create cinematic lighting using volumetrics in Blender.
[0:15] I'm using Cycles for this example. To create cinematic volumetric fog in Blender, start by adding a cube that will act as your volume container.
[0:24] Press Shift plus A, Mesh, Cube. This cube will hold the atmosphere in your scene. Press S to scale and make sure it's large enough to cover your scene.
[0:35] With the cube selected, go to the Material Properties tab and click New to create a new material. Select the Principled BSDF node and delete it by pressing X.
[0:46] Next, press Shift plus A in the shader editor and search volume scatter. Connect its volume output to the volume input of the material node.
[0:56] Make sure you connect it to volume, not surface. Now adjust the settings. Lower the density to something subtle, around 0.01 to 0.05, depending on how thick you want the fog.
[1:11] Smaller values create a soft cinematic haze, while higher values create heavy fog. You can also increase Anisotropy to around 0.3 to 0.6 to enhance light scattering and create stronger god rays.
[1:26] These values completely depend on your scene. My settings will look different from yours, so don't copy numbers blindly. Adjust them based on what looks good in your render.
[1:41] To add more depth and realism, I'll create another volumetric layer, specifically for the surface atmosphere, with lower density. Same as before, just make the numbers lower.
[1:57] After adjustments, it will look something like this. Hope you learned something new from this. Try it in your own scene and see how much of a difference volumetrics really make.



---

## Captured Frames

- [0:24] tutorials/frames/how-to-make-godrays-in-blender-no-plugins/frame_000.jpg
- [0:46] tutorials/frames/how-to-make-godrays-in-blender-no-plugins/frame_001.jpg
- [1:00] tutorials/frames/how-to-make-godrays-in-blender-no-plugins/frame_002.jpg
- [1:26] tutorials/frames/how-to-make-godrays-in-blender-no-plugins/frame_003.jpg
- [1:50] tutorials/frames/how-to-make-godrays-in-blender-no-plugins/frame_004.jpg

---

## Structured Notes

### Core Technique
Using a large cube fitted with a `Volume Scatter` shader (no Principled BSDF surface) as a whole-scene "volume container," in Cycles, to produce cinematic atmospheric haze and god rays — no plugins/add-ons required, just native volumetric shading.

### Summary
A very short, no-plugin recipe for turning a flat-lit Cycles render into one with visible light shafts/god rays and atmospheric depth. The technique adds one (or two) large cube(s) that encompass the whole scene, gives each a material whose Surface input is left empty and whose Volume input is fed by a `Volume Scatter` node, then tunes Density (how thick the fog reads) and Anisotropy (how strongly light scatters/how visible the god rays are) to taste. A second, lower-density volume cube layered on top is suggested for extra depth (a "surface atmosphere" layer distinct from the denser base fog). The author repeatedly stresses that the specific numeric values are scene-dependent and should be tuned visually rather than copied.

### Key Steps
1. Add a cube large enough to encompass the entire scene (Shift+A → Mesh → Cube, then S to scale it up) — this acts as the volume/fog container.
2. With the cube selected, go to Material Properties → New to create a material.
3. Select the default `Principled BSDF` node and delete it (X) — the material should have no surface shader.
4. In the Shader Editor, Shift+A → search **Volume Scatter** → add the node.
5. Connect the Volume Scatter node's output to the material output node's **Volume** input (explicitly not Surface).
6. Tune **Density**: ~0.01–0.05 for a subtle cinematic haze; higher values produce heavier/thicker fog.
7. Tune **Anisotropy**: ~0.3–0.6 to increase forward light scattering and make god rays/light shafts more pronounced.
8. Optional — add a second volume cube for extra depth: a separate, lower-density "surface atmosphere" layer on top of the base fog volume, using the same Volume Scatter setup with smaller Density values.
9. Adjust all values by eye per-scene — the author explicitly warns against copying exact numbers, since the right settings depend on lighting setup, scene scale, and desired look.

### Nodes / Settings
- **Render engine:** Cycles (explicitly stated; not tested/described for Eevee).
- **Object setup:** one (or two, layered) large cube(s) enclosing the scene, acting purely as volume containers.
- **Shader nodes:** `Volume Scatter` wired into the material output's **Volume** socket (Surface socket left empty — the default `Principled BSDF` is deleted).
- **Key parameters:** Volume Scatter **Density** (0.01–0.05 typical for haze, higher for heavy fog), **Anisotropy** (0.3–0.6 for stronger god-ray scattering).

### Difficulty
Beginner — only two node types involved (delete Principled BSDF, add Volume Scatter) and two tunable parameters; no geometry nodes, simulations, or add-ons required.

### Blender Version
Not specified (Cycles Volume Scatter node and workflow shown are stable across recent Blender versions).

### Tags
volume, lighting, cycles, rendering, beginner

---

## Related Tutorials
- `tutorials/how-i-made-realistic-storm-clouds-in-blender.md` — also covers god rays via a Volume Scatter cube, there combined with an interior spotlight for the light source; useful complement showing a specific light-rig pairing for this same volume-cube technique.
- `tutorials/tutorial-how-to-make-a-volumetric-projector-in-blender-45.md` — a related but distinct approach: sets the World Shader itself to Volume Scatter (density ~0.1) as scene-wide fog rather than a dedicated cube, then projects an animated video texture through a spotlight for colored god rays.
- `tutorials/3-easy-lighting-setups-blender-tutorial.md` — a spotlight + volume scatter fog lighting recipe (dramatic rim-highlight rig), same underlying Volume Scatter fog technique applied to a specific lighting setup.
- `tutorials/remove-noise-from-volumetrics-in-blender-50.md` — if this Volume Scatter technique produces noisy renders on Blender 5.0+, this entry's fix (enable Legacy Ray Marching under Render Properties → Volume) directly applies.
