---
title: How to Create Abstract Crystal Renders in Blender
source: YouTube
url: https://www.youtube.com/watch?v=RKz3DdbybVk
author: Extra 3d
ingested: 2026-06-23
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-create-abstract-crystal-renders-in-blender/
frame_count: 4
---

# How to Create Abstract Crystal Renders in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=RKz3DdbybVk)
**Author:** Extra 3d
**Duration:** 3m34s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** In this video I'm going to tell you how to create this abstract crystal render in Blender from Scratch. I was getting a lot of requests for this, so here we go. First things first, press Shift plus A and add a UV sphere. Let's increase its scale by 2. Looks good. Let's add a subdivision modifier and increase the subdivision level by 1 or 2. Apply the scale and shade smooth the sphere. Now we need to scatter the crystals on the sphere and to do that we need some crystals. Jesus, you got crystals in here. Now we can model some crystals, but since I am lazy, I'm just going to use this free model. Link is in the description. Just download the GLB version. Just drag it in a new blender file and click the import button. After that, just unpowering the model and remove the extra stuff like the empties. Increase the scale by 10 and apply the scale. Copy it and paste it into the original file. Just move it to the side and open geometry nodes. Create a new tree and first off, add a distribute on faces node, then add an instance on points node and connect them in a series. Drag the crystal object and it will give you a new node here. Just connect it into the instances and the points will be replaced by the crystal. Now play with the scale, see density and rotation. Or just copy my settings and you will be good to go. Now add a joined geometry node and connect the input directly so we can get the sphere back again. Create a new material for the sphere and press CTRL SHIFT. While the principal node is selected and select the textures, you can find this one on Ambience CG. Link is in the description. Let's increase the scale to something close to 9. Go into the material settings and switch the mode to bump and displacement. Play with the strength to something like 0.2. I'm going to go with a darker color which will create some contrast with the crystals. Now for the crystal, first off, increase its transmission value and also remove the color texture. Just manually select the color you want, I'm going to go with this purple. Drag the color out which will give you this color wheel that we'll use later. Add a mixed shader node and a shadow ray node into the factor. We are going to use my free course shader that you can get from the link in description. Just append the node tree and add it like a normal node in the shader editor. Connect it into the second slot and connect the color wheel into the color option. Now just add a camera and set a high focal length with depth of field and add some point lights with high intensity to get something like this. I have done a lot of experimental lighting with this one so it's completely random. You can just copy my coordinates and settings if you want the same look. I have also added volumetrics with a simple cube with this shader. The problem with this is that the top point light was creating some distractions. And to fix that, I just disabled the volume option for the top point light. In the end, I have used the cinematic compositor plus to get this cool cinematic render. Thanks for watching and you can get this project file on my Patreon along with the free course tic shaders.

**Frame:** tutorials\frames\how-to-create-abstract-crystal-renders-in-blender\frame_000.jpg


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
