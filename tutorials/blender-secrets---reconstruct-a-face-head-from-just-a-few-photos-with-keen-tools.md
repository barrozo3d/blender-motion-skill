---
title: Blender Secrets - Reconstruct a Face / Head from just a few photos with Keen Tools Face Builder
source: YouTube
url: https://www.youtube.com/watch?v=rUh2cEWAIgk
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — KeenTools FaceBuilder 2021.2.0 shown installing, consistent with Blender 2.9x-3.x era UI"
tags: [organic, modelling, materials, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---reconstruct-a-face-head-from-just-a-few-photos-with-keen-tools/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - Reconstruct a Face / Head from just a few photos with Keen Tools Face Builder

**Source:** [YouTube](https://www.youtube.com/watch?v=rUh2cEWAIgk)
**Author:** Blender Secrets
**Duration:** 1m30s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'Add pins'
- WARNING: Thin transcript: 655 chars. Notes may be shallow — consider --whisper-model small.

---


Frames captured — see "Captured Frames" section below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Face Builder lets you reconstruct a human head from only a couple of photos.
[0:09] Download and install the add-on, check the license agreement box and install the core.
[0:13] In the option panel, open the Face Builder tab and click on Create New Head.


### Create a new head [0:14]
**Transcript (timestamped):**
[0:18] Then click on Add Images.
[0:22] This gives you a camera for each image and a button for each camera.


### Align face [0:26]
**Transcript (timestamped):**
[0:27] Click on Align Face to automatically match the object to the image.
[0:31] Do this for each camera angle.
[0:34] To find June, add pins manually by clicking on the model.
[0:38] Then drag the pin to the corresponding place on the photo.
[0:41] Repeat this until the head model is perfect.
[0:47] When you're done, click on Exit Pin Mode and Create Texture.


### Add pins [0:50]


---

## Captured Frames

- [0:13] tutorials/frames/blender-secrets---reconstruct-a-face-head-from-just-a-few-photos-with-keen-tools/frame_000.jpg
- [0:22] tutorials/frames/blender-secrets---reconstruct-a-face-head-from-just-a-few-photos-with-keen-tools/frame_001.jpg
- [0:34] tutorials/frames/blender-secrets---reconstruct-a-face-head-from-just-a-few-photos-with-keen-tools/frame_002.jpg
- [0:41] tutorials/frames/blender-secrets---reconstruct-a-face-head-from-just-a-few-photos-with-keen-tools/frame_003.jpg
- [0:55] tutorials/frames/blender-secrets---reconstruct-a-face-head-from-just-a-few-photos-with-keen-tools/frame_004.jpg

---

## Structured Notes

### Core Technique
Reconstructing a photorealistic 3D human head model (geometry + texture) from just a handful of reference photographs, using the paid third-party add-on **KeenTools FaceBuilder** — the add-on auto-aligns a generic head mesh to each photo via facial-feature detection, refined with manually-placed "pins" that snap the model precisely to each photo, then bakes a texture from the aligned photo set.

### Summary
Frame 000 shows the add-on installation step in Blender Preferences: the FaceBuilder 2021.2.0 add-on entry expanded, its End-User License Agreement checkbox checked, and "Install Online" mid-download (52.1%) — since the add-on's core library can't ship bundled with the plugin due to Blender license restrictions. Frame 001 shows a freshly created "FaceBuilderHead" object: a neutral, generic 3D head mesh in Object Mode with the FaceBuilder side panel open (Camera, Views, Add Images, Model, Pins, Wireframe, Highlight head parts, Texture, Blendshapes, Create/Export options). Frame 002 shows the Align Face step in progress: a reference photo of a woman's face/head loaded as background, an orange pink/purple wireframe head mesh already reasonably well-matched to it, "Align Face" highlighted with a red arrow in the sidebar, and Pin Mode's on-screen legend (Esc: Exit, Left Click: Create Pin, Right Click: Delete Pin, Tab: switch). Frame 003 shows manual pin refinement: a close-up on the eyes/eyebrows region with red pin markers placed directly on key facial landmarks (eyebrow arches, eye corners, nose bridge) against the reference photo, fine-tuning the mesh alignment beyond what auto-Align-Face achieved. Frame 004 shows the final baked result: a realistic, textured 3D head model with the person's actual skin tone, facial features and hair visible, the Texture panel open in the sidebar (Resolution 2048×2048, UV: Butterfly, Create Texture, Hide Texture, Export, Advanced options like Angle Strictness, Expand Angle) — the finished photogrammetry-style reconstruction.

### Key Steps
1. **Install the add-on:** download and install KeenTools FaceBuilder in Blender's Add-ons preferences; check the End-User License Agreement box, then click Install Online (or Install from File / Download) — the add-on's core library is fetched separately due to Blender's licensing restrictions preventing it from being bundled directly.
2. **Start a new head:** in the N-panel, open the FaceBuilder tab and click **Create New Head** — this generates a generic base head mesh (named "FaceBuilderHead") ready to be matched to photos.
3. **Load reference photos:** click **Add Images** to load a handful of photos of the subject's face/head from different angles — this automatically creates a matching Camera for each photo, with a corresponding button to switch between camera/photo views.
4. **Auto-align per photo:** for each camera/photo, click **Align Face** — this automatically matches the generic head mesh's proportions and orientation to that specific photo using facial-feature detection. Repeat this for every camera angle loaded.
5. **Manual refinement with Pins:** where the automatic alignment isn't perfect, click directly on the model to place a **pin**, then drag that pin to the corresponding exact point on the underlying photo — pins act as point-to-point correspondence constraints that pull the mesh into more precise alignment. Repeat placing and adjusting pins (on eyebrows, eye corners, nose, mouth, etc.) across each camera view until the head model's shape convincingly matches all the reference photos.
6. **Finish and bake a texture:** once alignment is satisfactory, click **Exit Pin Mode**, then **Create Texture** to bake a photorealistic texture map (options include Resolution, UV layout method e.g. Butterfly, and Advanced blending controls like Angle Strictness and Expand Angle) — this projects and blends the color information from all the aligned photos onto the model's surface, producing a finished, textured, photorealistic head reconstruction.

### Nodes / Settings
- **Add-on:** KeenTools FaceBuilder (paid, third-party) — Preferences installation (EULA checkbox, Install Online/From File/Download).
- **FaceBuilder panel:** Create New Head, Add Images (auto-creates a Camera per image), Align Face (per-camera auto-match), Pins (manual point-to-point correspondence, click-and-drag on model vs. photo), Exit Pin Mode, Model/Wireframe/Highlight head parts display options.
- **Texture baking:** Create Texture (Resolution, UV method e.g. Butterfly, Advanced: Angle Strictness, Expand Angle, Equalize Brightness/Color, Autofill), Export/Hide Texture.
- **Blendshapes panel:** present in the UI (Create/Export as FBX options visible) though not demonstrated in this short video.

### Difficulty
Intermediate (mostly guided by the add-on's UI, but photo selection/coverage and manual pin refinement require some skill to get a clean result)

### Blender Version
Not specified — KeenTools FaceBuilder 2021.2.0 is shown installing; UI styling is consistent with the Blender 2.9x-3.x era.

### Tags
organic, modelling, materials, intermediate

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover KeenTools FaceBuilder or photo-based face reconstruction.
