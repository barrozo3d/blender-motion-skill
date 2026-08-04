---
title: Create a Photoreal Moon in minutes | 3D Tutorial | #blender secrets
source: YouTube
url: https://www.youtube.com/watch?v=iNL98QwGEmQ
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/create-a-photoreal-moon-in-minutes-3d-tutorial-blender-secrets/
frame_count: 0
frame_status: pending-selection
---

# Create a Photoreal Moon in minutes | 3D Tutorial | #blender secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=iNL98QwGEmQ)
**Author:** Blender Secrets
**Duration:** 2m47s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py create-a-photoreal-moon-in-minutes-3d-tutorial-blender-secrets <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] In this video we'll recreate the Earth's moon using free textures.
[0:08] We'll also look at how to solve a common issue with textures on UV squares.


### Download textures [0:14]
**Transcript (timestamped):**
[0:14] First, download both the color texture and the height map of the moon surface from NASA's website.
[0:21] There are several download options for each. The higher resolution is especially important for the height map.
[0:27] You may want to rename these files to avoid confusion later.


### Add UV sphere [0:33]
**Transcript (timestamped):**
[0:33] In Blender, add a UV sphere.
[0:37] By default, Generate UVs is enabled, so there's no need to UV unwrap the sphere yourself.
[0:44] Right-click and choose Shade Smooth.
[0:47] Add a subdivision modifier and a displacement modifier to the sphere.
[0:53] As coordinates, choose UV.
[0:57] Load the height map as the displacement texture.
[1:01] Set its color space to non-color.
[1:05] You may have to tweak the displacement's strength value.
[1:09] Increase the amount of subdivisions to squeeze more detail out of the height map.


### Add material [1:14]
**Transcript (timestamped):**
[1:15] Switch to Material Preview in the 3D Viewport.
[1:19] In the Shader Editor, create a material for the sphere and add the color texture to it.
[1:25] It looks pretty cool, but there is an issue that you'll notice when you look closer at the poles of the sphere.
[1:31] When using an equirectangular texture on a UV sphere, you will see this ugly pinching of the texture at the poles.
[1:39] This wouldn't be an issue with a quad sphere, but fortunately equirectangular textures are meant to be used on a UV sphere.
[1:47] Fortunately, there's a simple solution.
[1:51] Instead of UV texture coordinates, set it to Generated instead.
[1:56] Then set Texture Interpolation to Smart and Production Method to Sphere.
[2:03] Unfortunately, this means the mapping of the displacement map and the color map are no longer the same.
[2:09] So remove the displacement modifier and add the height map with a displacement node instead.
[2:16] Set it to also use Smart Interpolation and Sphere Protection with Generated Mapping.
[2:22] In the Material Settings, set displacement to Displacement Only or Displacement and Bump.
[2:29] Now you can see the displacement in the Cycles rendered preview.
[2:33] As you can see, the pole pinching issue is greatly reduced.



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
