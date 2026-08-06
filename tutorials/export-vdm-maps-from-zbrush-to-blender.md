---
title: Export VDM maps from Zbrush to Blender
source: YouTube
url: https://www.youtube.com/watch?v=KACmuXsoc30
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — uses the Draw brush's Vector Displacement checkbox and Clamp toggle, standard since Blender 2.8+"
tags: [displacement, organic, advanced]
extraction_status: complete
frames_dir: tutorials/frames/export-vdm-maps-from-zbrush-to-blender/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Export VDM maps from Zbrush to Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=KACmuXsoc30)
**Author:** Blender Secrets
**Duration:** 3m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] If you're somebody who has VDMs that you used before in ZBrush, and now you want to use them in Blender,
[0:10] or maybe you're somebody who makes VDMs and sells them on ArtStation, for example,
[0:15] then you may want to know how to export them, that you can use them in Blender as well.
[0:20] So it's pretty simple, you just go to Brush, Load Brush, and then you open the VDM ZBrush file.
[0:29] You need to have some primitive object loaded.
[0:36] And so now you can see all these VDMs here, so I can select one, and I can go to Brush, To Mesh.
[0:48] So this is the VDM brush, as a mesh.
[0:51] And now we can go to Texture, From Mesh.
[0:56] And here we have now our VDM Texture, but as you can see, there's a problem with it.
[1:00] There's this red color.
[1:04] And all around the displacement, it actually needs to be black in Blender.
[1:09] So we can go to Deformation here, and if it's red, then you need to mirror the X axis.
[1:17] So X is selected, and click on Mirror.
[1:22] And now we can do the same thing from Mesh.
[1:26] So now we have the correct Texture.
[1:28] If it's blue at the bottom, then you need to mirror it along the Y axis.
[1:33] So we can go to Export, and then Export the VDM, as an OpenEXR of course.
[1:42] There's still one more step we need to do in Photoshop, before we can use the VDM in Blender.
[1:47] So open the VDM in Photoshop.
[1:52] Then go to Image, Adjustments, Channel Mixer.
[1:56] And in the Green channel, set Green to 0, and Blue to 200.
[2:03] And in the Blue channel, set Blue to 0, and Green to 200%.
[2:09] So now we've flipped the Green and the Blue channel, and we've boosted them to 200%.
[2:14] So we can save this.
[2:21] And now in Blender, we can make a copy of the Drop Brush.
[2:27] We can open the Texture here.
[2:29] And then we need to make sure that the Clamp is turned off.
[2:33] And then we just do the usual stuff that we would do with an architecture.
[2:37] We set it to Mapping Area Plane, and of course Enable Vector Displacement.
[2:41] Set Stroke Method to Drag.
[2:44] And Falloff to Constant.
[2:47] And finally set the Strength to 1.
[2:50] And now you have your VDM in Blender.
[3:02] And now we can make a copy of the Vector Displacement.



---

## Captured Frames

- [0:20] tutorials/frames/export-vdm-maps-from-zbrush-to-blender/frame_000.jpg
- [0:41] tutorials/frames/export-vdm-maps-from-zbrush-to-blender/frame_001.jpg
- [0:56] tutorials/frames/export-vdm-maps-from-zbrush-to-blender/frame_002.jpg
- [1:09] tutorials/frames/export-vdm-maps-from-zbrush-to-blender/frame_003.jpg
- [1:38] tutorials/frames/export-vdm-maps-from-zbrush-to-blender/frame_004.jpg
- [1:52] tutorials/frames/export-vdm-maps-from-zbrush-to-blender/frame_005.jpg
- [2:33] tutorials/frames/export-vdm-maps-from-zbrush-to-blender/frame_006.jpg
- [2:50] tutorials/frames/export-vdm-maps-from-zbrush-to-blender/frame_007.jpg

---

## Structured Notes

### Core Technique
A cross-application pipeline for converting ZBrush Vector Displacement Map (VDM) brushes into a format Blender's sculpt Draw brush can use as a Vector Displacement stamp — including a required color-channel remap in Photoshop, since ZBrush and Blender encode displacement-direction color channels differently.

### Summary
Frame 000 shows ZBrush's Load Tool dialog with a VDM brush thumbnail selected, the starting point for extracting a purchased or self-made VDM brush. Frame 001 shows a plain cube primitive loaded in ZBrush, the required blank canvas the VDM gets converted onto via Brush > To Mesh. Frame 002 shows the resulting VDM texture (Brush > Texture > From Mesh) displayed in ZBrush's texture palette — dominated by a reddish-pink background color, flagged in the transcript as the "problem" that needs fixing. Frame 003 is a near-duplicate of the texture-palette view, confirming the red cast is a real, verifiable state before mirroring. Frame 004 shows the texture palette's Deformation-adjacent import/export flyout open, the step where the corrected texture gets exported as an OpenEXR. Frame 005 shows the Photoshop payoff: the VDM's Green and Blue channels swapped and boosted to 200% via Channel Mixer, producing the blue/green/orange normal-map-like image Blender actually expects. Frame 006 shows the final Blender-side setup: a fresh cube in Sculpt Mode with the corrected VDM loaded as the active brush texture (visible in the tool settings thumbnail, top right). Frame 007 shows the applied result — the same cube now sculpted with the VDM stamp via the Draw brush, its top face deformed into the shape encoded in the vector displacement map.

### Key Steps
1. **Extract the VDM brush in ZBrush:** Brush > Load Brush, open the VDM .ZBP file; load a primitive object (e.g. a cube) into the canvas as the surface to stamp onto.
2. **Convert the brush to a usable texture:** with the VDM brush selected, go to Brush > To Mesh to get the VDM as real mesh geometry, then Texture > From Mesh to bake that geometry back out as a VDM texture map.
3. **Fix the background color (critical, ZBrush-specific):** a freshly-baked VDM texture often has a red (or blue) background where Blender expects pure black. If it's red, go to Deformation, select the X axis and click Mirror, then redo Texture > From Mesh; if the bottom reads blue instead, mirror along Y instead. This corrects the axis mismatch between ZBrush's and Blender's VDM conventions.
4. **Export from ZBrush:** Export the corrected VDM texture as an OpenEXR file (required for the precision vector-displacement data needs).
5. **Remap color channels in Photoshop (required step, not optional):** open the exported VDM in Photoshop; go to Image > Adjustments > Channel Mixer; in the Green output channel set Green to 0 and Blue to 200%; in the Blue output channel set Blue to 0 and Green to 200% — this swaps and boosts the Green/Blue channels to match Blender's Vector Displacement color convention; save the result.
6. **Set up the brush in Blender:** duplicate the Draw brush; load the Photoshop-corrected texture as its brush texture; make sure Clamp is turned OFF on the texture; set Mapping to Area Plane; enable the brush's Vector Displacement option; set Stroke Method to Drag and Falloff to Constant; set Strength to 1.
7. **Apply:** stamping this brush onto a mesh in Sculpt Mode now reproduces the original ZBrush VDM sculpt as real Blender displacement.

### Nodes / Settings
- **ZBrush:** Brush > Load Brush, Brush > To Mesh, Texture > From Mesh, Deformation panel (Mirror X/Y), Export as OpenEXR.
- **Photoshop:** Image > Adjustments > Channel Mixer (Green channel: Green=0/Blue=200%; Blue channel: Blue=0/Green=200%).
- **Blender Sculpt Brush settings:** Texture (Clamp disabled), Mapping = Area Plane, Vector Displacement (enabled), Stroke Method = Drag, Falloff = Constant, Strength = 1.

### Difficulty
Advanced

### Blender Version
Not specified — relies on the sculpt Draw brush's Vector Displacement checkbox and texture Clamp toggle, both standard since Blender 2.8+.

### Tags
displacement, organic, advanced

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library cover ZBrush interop or Vector Displacement Maps yet.
