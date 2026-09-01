---
title: Blender Secrets - 4 tips for Cinematic Lighting
source: YouTube
url: https://www.youtube.com/watch?v=lXvmt0QxAFY
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 3.3.0 -- observed in frame_000"
tags: [lighting, hdri, materials, shaders, volume, cycles, eevee, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---4-tips-for-cinematic-lighting/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - 4 tips for Cinematic Lighting

**Source:** [YouTube](https://www.youtube.com/watch?v=lXvmt0QxAFY)
**Author:** Blender Secrets
**Duration:** 4m34s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


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

## Captured Frames

- [0:47] tutorials/frames/blender-secrets---4-tips-for-cinematic-lighting/frame_000.jpg
- [1:32] tutorials/frames/blender-secrets---4-tips-for-cinematic-lighting/frame_001.jpg
- [2:16] tutorials/frames/blender-secrets---4-tips-for-cinematic-lighting/frame_002.jpg
- [2:57] tutorials/frames/blender-secrets---4-tips-for-cinematic-lighting/frame_003.jpg
- [3:44] tutorials/frames/blender-secrets---4-tips-for-cinematic-lighting/frame_004.jpg

---

## Structured Notes

### Core Technique
Four cinematic-lighting tricks: aiming a spotlight through the camera view for precise placement, using an image plane as a light-shaping gobo/cutter in front of a spot, fast HDRI browsing with the Gaffer add-on (mis-transcribed as "Kevver"/"Gether" in the auto transcript — confirmed from the on-screen HDRI panel in frame 003), and driving an emission shader's strength with an expression to make a light pulsate.

### Summary
Frame 000 shows tip 1: the N-panel's View tab with Local Camera enabled and a Spot light selected as the active local camera, letting the artist press Numpad0 to see exactly what the spotlight illuminates (car showroom scene, two camera angles compared side by side). Frame 001 shows tip 2's node setup: an Image/Video texture (leaves footage) plugged into a Principled BSDF's Alpha input, used on an Image-as-Planes object positioned in front of a spotlight to cast a leaf-shaped gobo pattern to fake dappled light. Frame 002 shows the same gobo idea extended with a volumetric cube: a Volume Scatter node (Density 0.470) driving the cube's Volume output, producing visible light shafts/haze through the leaf-shadowed beam in the render on the right. Frame 003 confirms the HDRI add-on is **Gaffer**: its Lights panel (World tab) shows a browsable grid of HDRI thumbnails ("HDRi 01 Hdri Background Lighting Kit") for one-click swapping, demoed on a car render. Frame 004 shows the start of tip 4 (pulsating light): an Emission shader node on a cube with Strength at its default 1.000, about to have a driver expression added to the Strength field via right-click → Add Driver (Ctrl key hint visible) — the exact expression text and the anti-negative-value node setup mentioned in the transcript were not legible in the captured frame or spoken in the audio.

### Key Steps
1. **Spotlight-as-camera aiming:** add a Spot light; open the N-panel → View tab; enable Local Camera and pick the spotlight as the local camera; under View Lock check Lock Camera to View; press Numpad0 to enter the light's point of view for precise aiming. Soften the spot with the Radius and Blend values; switch Light type in the Light properties if a softer Area light suits the shot better.
2. **Image-plane gobo:** import a video/image via the Images as Planes add-on; enable Show Backface in the plane's material; if the source has no alpha channel, plug its Color output into the Alpha input (add a MapRange node and raise From Min to fine-tune which parts read as transparent). Position/scale the plane in front of the spotlight; raise the light's Power as needed; adjust Light Radius to control shadow softness and Beam Shape Spot Size for beam width. In EEVEE, set the plane's Shadow Mode to Alpha Hashed so the alpha cutout casts a correct shadow silhouette.
3. **Volumetric light shafts:** add a large cube enclosing the scene, give it a material with a Volume Scatter node plugged into Volume, and lower Density for a subtle haze that reveals the gobo-shaped beam.
4. **Gaffer add-on for fast HDRI swapping:** install the Gaffer .zip via Preferences, set the folder containing your HDRIs; enable it under World → HDRI tab; the first run needs to Render Preview to generate thumbnails, after which you can flip through HDRIs live in the viewport. Default rotation is usually fine but is adjustable. For memory efficiency, pair a low-res HDRI (for lighting) with a separate high-res JPEG background (for reflections only).
5. **Pulsating light via driver expression:** create an Emission shader for the material; right-click the Strength field → Add Driver, and enter a two-parameter sine-style expression (first number = pulsation speed — smaller is faster; second number = emission strength — bigger is brighter). To prevent the expression from ever going negative (which would subtract light from the scene), an additional node/clamp setup is used, but neither its exact formula nor the clamp node graph were verifiable from the available transcript or captured frame — revisit this tutorial's video directly if exact driver syntax is needed.

### Nodes / Settings
- **Lights:** Spot (Radius, Blend, Beam Shape Spot Size, Power), Area (as a spot alternative).
- **Shading:** Principled BSDF (Alpha input fed by image/video Color for gobo cutout), MapRange (From Min to tune alpha threshold), Volume Scatter (Density) on an enclosing cube for light shafts, Emission shader (Strength driven by expression).
- **Add-ons:** Images as Planes (built-in), Gaffer (third-party, free on GitHub / paid on Blender Market — fast HDRI browsing with auto-generated thumbnails).
- **Render:** EEVEE Shadow Mode = Alpha Hashed for gobo planes; Local Camera / Lock Camera to View for spot-as-camera aiming.
- **Animation:** Driver expression on Emission Strength for pulsating light (exact expression not captured — see Key Steps note).

### Difficulty
Intermediate

### Blender Version
Not specified — EEVEE (Alpha Hashed shadow mode, "Global Ex..." HDRI world panel) and Cycles-compatible node setups shown; UI consistent with modern Blender 3.x-4.x.

### Tags
lighting, hdri, materials, shaders, volume, cycles, eevee, intermediate

---

## Related Tutorials
- [5 Lighting SECRETS in Blender](5-lighting-secrets-in-blender.md) — shares lighting, volume, cycles, rendering→shaders, intermediate; near-identical gobo/god-ray/HDRI toolkit from a different author, strong complementary reference.
- [Better Billboards using Normal Maps (Low Poly Trees)](better-billboards-using-normal-maps-low-poly-trees.md) — shares lighting, cycles, materials, shaders, intermediate.
