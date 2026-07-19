---
title: Brand New Material Assets in Blender 5.2 LTS
source: YouTube
url: https://www.youtube.com/watch?v=QkIr1-lDPW0
author: Blender Studio
ingested: 2026-07-19
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/brand-new-material-assets-in-blender-52-lts/
frame_count: 0
frame_status: pending-selection
---

# Brand New Material Assets in Blender 5.2 LTS

**Source:** [YouTube](https://www.youtube.com/watch?v=QkIr1-lDPW0)
**Author:** Blender Studio
**Duration:** 5m26s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py brand-new-material-assets-in-blender-52-lts <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] For the first time ever, together with version 5.2, Blender now ships with a small library of material assets.
[0:06] These are part of the new online assets, which come out of the box without bloating your initial download size.
[0:12] Once you enable online access, they are available directly from the asset browser inside of Blender.
[0:17] These initial materials are a small selection for now, and more will follow in the future.
[0:22] They are also all procedural and outfitted with a bunch of parameters, so they have lots of possibilities for customization
[0:29] to make them look exactly like you need.
[0:31] In this video, I will give you a brief overview of how to get started using them.
[0:35] An additional tutorial on how to customize them in the more advanced way is over on our Blender Studio platform,
[0:41] next to all sorts of courses, assets, and production knowledge about using Blender as a studio.
[0:47] So head over there after this to learn more.
[0:50] To get started using the new materials, just open a new asset browser.
[0:54] If you have a bunch of assets yourself, you might need to select the essentials library to narrow them down.
[0:59] Then you can see that there are a whole bunch of essential assets that are included with Blender out of the box.
[1:05] Some of them are bundled with the software download, and others are available online.
[1:10] To be able to see those, you need to first have online access enabled.
[1:14] You can simply do that right here, if you haven't yet.
[1:16] And then in the materials catalog, there are a bunch of material assets,
[1:20] marked with an icon that shows that they are online.
[1:23] The library contains just a few commonly needed materials so far,
[1:27] like different types of bricks, tiles, and fabric.
[1:30] The focus here was on providing a few useful basics, but the library will grow still.
[1:35] Besides the materials, there are also a whole bunch of other new online assets,
[1:39] like grease pencil brushes, compositing filters, and base meshes.
[1:43] Using those works just the same, but here I want to focus on the materials as an example.
[1:49] To make use of these new materials, they will first need to be downloaded.
[1:53] You can easily do that by clicking on the download icon that pops up over an asset.
[1:58] To download multiple assets, you can also just select the ones you want,
[2:02] and right click to download all of them.
[2:04] And then you're good to go.
[2:05] Simply drag one onto a mesh surface in your 3D viewport,
[2:09] that will import the material data block into your file,
[2:12] and assign it to the material slot under your cursor.
[2:14] This is just the same as it already was for material assets,
[2:17] that you could have in your user library.
[2:19] Now onto the materials themselves.
[2:21] How the textures are mapped will depend on what the material is meant for and what it looks like.
[2:26] But generally, if there is a regular pattern in the material,
[2:29] it will by default use the mesh's UV map.
[2:32] The scale is generally that the unit square of the UVs is equivalent to one meter squared in the texture.
[2:38] So you might need to adjust the UVs of the mesh to work with that.
[2:42] For these initial materials, you don't need to worry about going outside of the unit square with your UVs,
[2:48] since they are not tiling and repeating textures.
[2:51] They can be extended however far you want, and there won't be any repeating patterns,
[2:55] since they are procedural in nature.
[2:57] So, but what if now we want to make any changes to the material?
[3:01] Assets from the Essentials library are at first imported into your file as packed data.
[3:06] That means Blender remembers which library they came from originally,
[3:09] and it can't be edited, like when you link data between files.
[3:14] But it's also stored or packed in your file itself.
[3:18] So you don't actually depend on that library being around when you share the file with someone else.
[3:23] So that means an Essentials material cannot directly be edited.
[3:27] First, you need to make it local.
[3:30] This is easily achieved by clicking on the button on the material that indicates that it is packed.
[3:34] When I do that, you can see how all these parameters that the material comes with
[3:39] stop being grayed out, and I can make adjustments.
[3:42] But now that packed link is broken, and the material doesn't associate with the library anymore.
[3:47] The material is truly local.
[3:49] I recommend you to go through the materials and play around with the parameters.
[3:53] For some of them, they are quite basic.
[3:55] Most materials, for example, have a way to change the overall scale of the texture,
[4:00] or the overall base color.
[4:02] For others, you can change the look of the material quite significantly,
[4:05] and fine tune them to your needs.
[4:07] These wooden boards, for example, have a quite extensive set of parameters
[4:11] to not only change the color and roughness, but even the pattern of the boards themselves.
[4:16] This level of customizability is something that you can't get from tileable textures
[4:21] that are based on static photos, and is where the procedural nature really comes in handy.
[4:26] Another feature built into some of these materials worth mentioning is displacement.
[4:31] The cobblestone material, for example, looks quite flat out of the box.
[4:35] But with displacement enabled, this can look a good bit more realistic and complex.
[4:40] Enabling displacement in the material alone is not enough to achieve this though.
[4:44] You also need to make sure that your mesh has enough vertices for the displacement to look good.
[4:49] An easy way to do this is to use a subdivision surface modifier
[4:53] and crank the level to a sufficient number.
[4:55] If you're using cycles, you can also make use of the adaptive subdivision feature,
[5:00] which will ensure a certain density of vertices, depending on how large the mesh is on screen.
[5:05] Careful though, all this subdivision can make displacement quite expensive.
[5:09] If you want to dive deeper into customizing these base materials
[5:13] and get more advanced by using shader nodes, head over to studio.blender.org
[5:17] or click the link in the description and join the Blender Studio.
[5:22] And make sure to check out the announcement for a new feature film project.
[5:25] Anyways, goodbye.



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
