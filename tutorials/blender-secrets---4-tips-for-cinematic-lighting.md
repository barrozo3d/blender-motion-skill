---
title: Blender Secrets - 4 tips for Cinematic Lighting
source: YouTube
url: https://www.youtube.com/watch?v=lXvmt0QxAFY
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-secrets---4-tips-for-cinematic-lighting/
frame_count: 0
frame_status: pending-selection
---

# Blender Secrets - 4 tips for Cinematic Lighting

**Source:** [YouTube](https://www.youtube.com/watch?v=lXvmt0QxAFY)
**Author:** Blender Secrets
**Duration:** 4m34s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-secrets---4-tips-for-cinematic-lighting <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Recently, the LabN80 from CreativeShrim.com were kind enough to send me a preview of their
[0:06] new lighting course.
[0:08] The course is divided into chapters, my personal favorite being the one about the warehouse.
[0:12] I learned quite a bit from it so far, especially the part about light groups.
[0:16] The workflows they talk about are quite artist friendly and easy to follow.
[0:20] It's a great addition to the photogrammetry course they did earlier.
[0:24] If you want to get this course, please use my affiliate link in the description.
[0:27] It doesn't cost you anything extra, but it does help to support me as well, so I can
[0:31] keep providing you with Blender secrets.


### Spotlight [0:33]
**Transcript (timestamped):**
[0:34] Add a spotlight.
[0:40] Open the option panel by pressing N.
[0:43] In the View tab, enable Local Camera and select the spot as the camera.
[0:48] Under View Blog, check Lock Camera to View.
[0:51] Press 0 to enter the point of view of that light.
[0:54] Now the camera works as a spotlight at the same time.
[0:59] You can make the spot softer by adjusting the radius and blend values.
[1:03] To change the type of lamp to an area light, for example, click on the type of light in
[1:07] the Light options.


### Image Plane [1:09]
**Transcript (timestamped):**
[1:17] Import an image or video using the images as planes add-on.
[1:21] On check, show back phase in the plane's material settings.
[1:25] If your texture doesn't have an alpha channel, plug the color output into the alpha input.
[1:32] You can add an Inferred node to change which parts are transparent.
[1:37] A Map Range node helps to control the transparent parts by increasing the From Min value.
[1:44] Rotate, move and scale the plane so that it's in front of the spotlight.
[1:51] You may need to increase the power value of the light.
[1:54] To control the blurriness of the shadows, adjust the Light Radius value.
[2:02] To change the size of the spot, increase the Beam Shape Spot Size value.
[2:07] In EV, make sure that the image plane has shadow mode set to alpha hashed.
[2:13] To add a volumetric effect, add a cube around the scene.
[2:17] Plug a Volumetra Threaded node into the volume input of the cube material and lower the density.


### Gether [2:24]
**Transcript (timestamped):**
[2:27] Kevver is a must-have add-on if you often use HDR eyes.
[2:31] The add-on lets you cycle through your HDR eyes so that you can quickly and easily choose
[2:35] the best lighting for your scene.
[2:39] After installing the zip file in Preferences, you need to set the folder where you keep your
[2:43] HDR eyes.
[2:45] Then in the World tab, check the HDR Eye tab to activate Kevver.
[2:49] The first time you use Kevver, you'll have to generate thumbnails.
[2:55] Go to Render Preview.
[2:57] Now you can flip through HDR eyes and see the result in the viewport.
[3:01] Although the default values are usually fine, it can be interesting to adjust the rotation.
[3:08] To save memory, you can also create a high-res JPEG background.
[3:13] If you have both a low-res and high-res version of your HDR eye, then you can use the low-res
[3:18] HDR eye for the lighting and the high-res JPEG for reflections.
[3:26] You can try Kevver for free by downloading it from GitHub.
[3:29] If you find it useful, you can support its further development by getting it on Blender
[3:33] Market.
[3:38] To make a light pulsate, first create an emission shader for your material.
[3:44] Then in the Strength field, type this expression.
[3:49] The first number controls the speed of the pulsating light.
[3:52] The smaller this number, the faster it will pulsate.
[3:55] The second number controls the strength of the emission.
[3:59] The bigger the number, the brighter the light is.
[4:02] To avoid that the light value becomes negative, sucking light out of the scene like some kind
[4:07] of black hole, you can use this node setup.
[4:11] If you found this topic interesting and would like to know more, don't forget that you can
[4:15] find it in my Blender Secrets ebook, along with almost 2000 pages of other tips.
[4:21] To get an idea of what the ebook is like, you can download the free sample from my website.



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
