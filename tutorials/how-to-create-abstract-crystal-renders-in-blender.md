---
title: How to Create Abstract Crystal Renders in Blender
source: YouTube
url: https://www.youtube.com/watch?v=RKz3DdbybVk
author: Extra 3d
ingested: 2026-06-23
blender_version: "Not specified"
tags: [geometry-nodes, materials, shaders, procedural, glass, lighting, volume, compositing, abstract, intermediate]
extraction_status: complete
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
Scattering an imported crystal mesh across a UV sphere with Geometry Nodes (Distribute Points on Faces → Instance on Points → Join Geometry), then dressing it with a transmissive purple glass shader, a bump/displacement rock material, volumetrics, and cinematic lighting/compositing.

### Summary
Builds an abstract "crystal planet" render from scratch: a subdivided UV sphere acts as the base, a free GLB crystal model is scattered over its surface via Geometry Nodes, and the original sphere geometry is re-joined underneath so it reads as rock. A free shader (author's "course shader") drives the crystal material, combined with a Mix Shader + Shadow Ray node for the transmissive purple look. The scene is finished with a high focal-length camera with depth of field, multiple point lights, a volumetric cube, and the Cinematic Compositor+ for final color grading.

### Key Steps
1. `Shift+A` → add a UV Sphere, scale it up by 2.
2. Add a Subdivision Surface modifier, level 1–2; apply scale; Shade Smooth.
3. Import a free crystal GLB model (link in original video description) into a new file; unparent it, delete extra empties, scale by 10, apply scale; copy into the main scene file.
4. Open the Geometry Nodes editor on the sphere, create a new node tree.
5. Add **Distribute Points on Faces** → **Instance on Points**, connect in series; drag the crystal object in as the instance source and connect to the Instances socket.
6. Tune Distribute Points density, plus per-instance Scale and Rotation, to control crystal coverage.
7. Add a **Join Geometry** node and feed the original sphere mesh back in alongside the instanced crystals, so the underlying rock sphere is visible between crystals.
8. Rock material: Ctrl+Shift-click an Ambience CG texture onto the Principled BSDF (loads base color + the rest of the PBR set via Node Wrangler), scale ~9, switch displacement mode to Bump **and** Displacement, strength ~0.2, with a darker base color for contrast against the crystals.
9. Crystal material: raise Transmission, remove the color texture, pick a manual purple base color, and route that color into a Mix Shader whose factor is driven by a Shadow Ray node; append the author's free "course shader" node group into the second Mix Shader slot.
10. Camera: high focal length lens with Depth of Field enabled.
11. Lighting: several point lights at high intensity (manual/experimental placement); disable the **Volume** option on the point light positioned above the volumetric cube to stop it blowing out the volumetrics.
12. Volumetrics: a simple cube with the crystal/course shader applied, used purely for its volume scatter contribution.
13. Compositing: Cinematic Compositor+ (paid add-on) for the final grade.

### Nodes / Settings
- Geometry Nodes: `Distribute Points on Faces` → `Instance on Points` → `Join Geometry` (rejoining base sphere mesh)
- Modifiers: Subdivision Surface (level 1–2)
- Shading: Shade Smooth on sphere
- Shader editor: Principled BSDF (rock material, Bump+Displacement, scale ~9, strength ~0.2); crystal material uses Transmission + manual Base Color → Mix Shader (factor driven by Shadow Ray node) → custom appended "course shader" node group
- Camera: high focal length + Depth of Field
- Lights: multiple Point Lights, high intensity; Volume option toggled off on the light above the volumetric cube
- Volumetrics: cube mesh with the crystal/course shader for volume scatter
- Compositing: Cinematic Compositor+ (paid add-on, not a native Blender node)
- External assets: free crystal GLB model + Ambience CG PBR texture (both linked in original video description, not captured here)

### Difficulty
Intermediate — Geometry Nodes scattering is simple (3-node setup), but the lighting/shader/volumetrics dressing requires prior Blender material and compositing experience, and the final look depends on two external paid/free resources (course shader, Cinematic Compositor+).

### Blender Version
Not specified in transcript or frames (UI style in frames is consistent with Blender 4.x).

### Tags
#geometry-nodes #materials #shaders #procedural #glass #lighting #volume #compositing #abstract #intermediate

---

## Related Tutorials
- `another-blender-string-tutorialbut-even-better-this-time.md` — shares glass/procedural/intermediate tags and similar abstract crystalline aesthetic
- `art-stream-27-nodes-nodes-nodes-blender-geometry-nodes.md` — shares Distribute Points on Faces scattering technique for abstract/procedural geometry
