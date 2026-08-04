---
title: Blender Secrets - How to merge 3D Scans and bake the Texture as Color Attributes
source: YouTube
url: https://www.youtube.com/watch?v=AxDXWgFDwLA
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-secrets---how-to-merge-3d-scans-and-bake-the-texture-as-color-attributes/
frame_count: 0
frame_status: pending-selection
---

# Blender Secrets - How to merge 3D Scans and bake the Texture as Color Attributes

**Source:** [YouTube](https://www.youtube.com/watch?v=AxDXWgFDwLA)
**Author:** Blender Secrets
**Duration:** 4m1s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-secrets---how-to-merge-3d-scans-and-bake-the-texture-as-color-attributes <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Let's say you have two 3D scans and you want to merge them into one object without losing
[0:07] any textures.
[0:09] Make sure the objects both have enough geometry.
[0:13] If not, add a Subdiff modifier and apply it.
[0:17] With dense scans, however, it's a good idea to remove double vertices to avoid issues
[0:21] later.
[0:23] To do this, press M in Edit Mode and choose By Distance.
[0:28] Use a boolean cutter to remove any parts that you don't need.
[0:38] Apply the boolean modifier and remove the bounding box.
[0:44] Move and rotate the objects to overlap as desired.
[0:50] You can use proportional editing to adjust the way the objects overlap.
[0:55] Select proportional editing by pressing O and scroll the mouse wheel to change its
[1:00] influence radius.
[1:03] It's important that both objects have the same UV map name.
[1:07] Otherwise one of the objects will lose its texture after you join them.
[1:11] The name doesn't matter as long as it's the same for both objects.
[1:16] Select both objects and press Ctrl and plus on the numpad to join them using bool tool.
[1:22] Now they are merged into one object.
[1:24] I recommend inspecting the model on the inside.
[1:27] If the intersecting parts are not removed, try enabling whole tolerant on the modifier.
[1:34] Apply the boolean modifier and remove the bounding box.
[1:38] Duplicate this object and hide the original.
[1:42] Switch to scope mode.
[1:44] I like to use a madcap, it just makes it easier to see what you're doing.
[1:48] Enable Dintopo with constant detail.
[1:51] You can sample part of the model to get its resolution.
[1:55] Dintopo allows us to sculpt on the seam more easily, but it removes all texture information,
[2:00] which is why we are using a duplicate object.
[2:03] Use the clay strips brush and smooth to blend the two parts together.
[2:09] To get the colors back from the texture, we can bake the original texture to color attributes,
[2:14] formerly known as vertex colors.
[2:17] Hide a color attribute to the duplicate.
[2:23] In the Outliner, run hide and select the original textured mesh.
[2:28] Hold Ctrl and select the duplicate as well.
[2:31] Please note that if you do this selection order in the 3D viewport, you must hold Shift instead
[2:36] of Ctrl.
[2:37] In the Cycles Bake menu, for the bake type, select the texture channel you wish to bake
[2:41] from.
[2:42] In my case, I had the texture setup as an emission shader on the original mesh, so I
[2:46] have to choose Emit.
[2:48] But if your original texture is plugged into the diffuse channel, choose Diffuse and disable
[2:53] Direct and Indirect so there is no influence of lighting.
[2:57] Check Selected to Active to bake from the original textured mesh to the duplicate.
[3:02] As Output, choose Active Color Attribute.
[3:06] Make sure you are in Object Mode and click Bake.
[3:09] When it's done, hide the original mesh again.
[3:13] To see the colors in Object or Scoped Mode, enable Color Attribute in the Viewport Shading
[3:18] options.
[3:20] In case the bake didn't work perfectly, try increasing the extrusion value.
[3:24] This works like a bake cage.
[3:27] Make sure the objects are still selected in the right order and click Bake again.
[3:32] In my experience, an extrusion value of 0.2 often works well.
[3:37] You can use the Paint tool in Scoped Mode to paint on the mesh.
[3:41] By pressing S, you sample the color under the cursor.
[3:46] A low brush strength value helps to blend the colors more gradually.
[3:51] For more scoped tips, check my Scoped Playlist or get my Blender Secrets ebook.
[3:55] There is also a free sample if you want to check that out first.



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
