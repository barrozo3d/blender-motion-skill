---
title: Blender Secrets - 4 tips for Photoreal Lighting
source: YouTube
url: https://www.youtube.com/watch?v=do_S94ZXLSc
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-secrets---4-tips-for-photoreal-lighting/
frame_count: 0
frame_status: pending-selection
---

# Blender Secrets - 4 tips for Photoreal Lighting

**Source:** [YouTube](https://www.youtube.com/watch?v=do_S94ZXLSc)
**Author:** Blender Secrets
**Duration:** 4m27s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-secrets---4-tips-for-photoreal-lighting <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### IES lights [0:00]
**Transcript (timestamped):**
[0:00] IES files are text files that describe how specific lights look in real life.
[0:07] They are essential for realism in architectural visualization.
[0:11] You can find thousands of them for free online.
[0:15] Once you've downloaded some IES files, add a point light.
[0:21] Click on Use nodes in the light settings.
[0:24] Make sure you've selected Cycles as IES lights don't work in EEVEE.
[0:29] In the shader editor, press Shift A for the Add menu and find the IES texture node.
[0:35] Set it to external and load an IES file in the node.
[0:39] Then connect it to the strength input of the point light.
[0:44] To make the shape of the light distribution more pronounced, you can lower the radius
[0:48] of the light.
[0:49] But be careful, as a radius of zero can produce some artifacts.
[0:53] I found that the value of 0.02 or 0.03 is a safe range that doesn't produce artifacts
[1:00] but still looks sharp.
[1:03] This kitchen scene was made mostly with assets from Polygon.
[1:07] I've personally used Polygon a lot for doing client work and I was always able to find
[1:11] what I needed, especially for architectural scenes.
[1:14] Besides materials, they also have detailed 3D scanned models, like all this delicious
[1:19] looking food.
[1:20] However, I couldn't find any 3D scanned donuts.


### Textures [1:24]
**Transcript (timestamped):**
[1:30] Add a spotlight and enable Use nodes in the shader editor.
[1:35] Switch to Rendered View and increase the intensity of the spotlight.
[1:39] Select the Emission node of the spotlight and press Ctrl T to add texture nodes.
[1:46] Add an image or a video texture.
[1:48] In case you're using a video texture, open the Option panel by pressing N.
[1:53] Then click the Match Movie Length icon next to the frame value.
[1:58] Enable Auto Refresh as well.
[2:00] Use Normal Texture Coordinates.
[2:03] In Cycles, you should now see the textured light.
[2:06] To adjust the blurriness, change the Light Radius value.
[2:10] To have the texture cover a wider area, increase the Beam Shape, Spot Size value.


### Sun [2:17]
**Transcript (timestamped):**
[2:22] Set Render Engine to Cycles.
[2:25] In the World tab, set Color to Sky Texture.
[2:29] Set it to Nishita with the Sun Disk enabled.
[2:32] Right away, you get this nice sky background and lighting.
[2:37] Sun rotation changes the horizontal position of the sun.
[2:41] To make sure there is no light leaking, I added a Solidify modifier to the room.
[2:47] To create a sunset timelapse, you can set keyframes for the sun elevation value.
[2:52] Just be sure to set the keyframes to Linear.
[2:55] Sun Size affects the softness of the shadows.
[2:58] The bigger the sun, the softer the shadow.
[3:05] The Air, Dust and Ozone values control how much the air quality influences the light.
[3:11] Increasing the Air value gives more dramatic sunsets.


### HDRI [3:16]
**Transcript (timestamped):**
[3:20] To set up an HDRI manually, go to the World tab.
[3:24] Click on the yellow dot next to Color.
[3:27] Choose Environment Texture.
[3:29] Click on Open and choose an HDRI file.
[3:34] You can get a lot of free HDRIs from Polyheaven.com.
[3:38] Now if you switch to Render Preview, you can see that the HDRI is visible in the background
[3:43] and lighting the scene.
[3:45] If you don't want to see and render the HDRI in the background, you can go to the Render
[3:49] tab and check Transparent under the Film Options.
[3:53] In that case, choose a file format which supports transparency, like PNG or EXR, and check RGBA.
[4:04] If you found this topic interesting and would like to know more, don't forget that you can
[4:08] find it in my Blender Secrets ebook, along with almost 2000 pages of other tips.
[4:14] To get an idea of what the ebook is like, you can download the free sample from my website.



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
