---
title: How to make Godrays in Blender ( NO PLUGINS )
source: YouTube
url: https://www.youtube.com/watch?v=alDV81qXQtA
author: Vlabs
ingested: 2026-08-02
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-make-godrays-in-blender-no-plugins/
frame_count: 0
frame_status: pending-selection
---

# How to make Godrays in Blender ( NO PLUGINS )

**Source:** [YouTube](https://www.youtube.com/watch?v=alDV81qXQtA)
**Author:** Vlabs
**Duration:** 2m8s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-to-make-godrays-in-blender-no-plugins <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Blender Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
