---
title: Daily Blender Tip #43 - Import Images As Planes Add-On
source: YouTube
url: https://www.youtube.com/watch?v=d028uL7ZRXE
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Import Images as Planes ships as a bundled add-on since early Blender 2.x"
tags: [materials, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-43---import-images-as-planes-add-on/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip #43 - Import Images As Planes Add-On

**Source:** [YouTube](https://www.youtube.com/watch?v=d028uL7ZRXE)
**Author:** Blender Secrets
**Duration:** 2m53s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 19 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (19 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[2:30] KDE Nino,
[2:41] restraint



---

## Captured Frames

- [0:10] tutorials/frames/daily-blender-tip-43---import-images-as-planes-add-on/frame_000.jpg
- [0:35] tutorials/frames/daily-blender-tip-43---import-images-as-planes-add-on/frame_001.jpg
- [1:00] tutorials/frames/daily-blender-tip-43---import-images-as-planes-add-on/frame_002.jpg
- [1:25] tutorials/frames/daily-blender-tip-43---import-images-as-planes-add-on/frame_003.jpg
- [1:50] tutorials/frames/daily-blender-tip-43---import-images-as-planes-add-on/frame_004.jpg
- [2:15] tutorials/frames/daily-blender-tip-43---import-images-as-planes-add-on/frame_005.jpg
- [2:35] tutorials/frames/daily-blender-tip-43---import-images-as-planes-add-on/frame_006.jpg
- [2:48] tutorials/frames/daily-blender-tip-43---import-images-as-planes-add-on/frame_007.jpg

---

## Structured Notes

### Core Technique
Enabling and using the bundled-but-inactive-by-default **Import Images as Planes** add-on: once activated, Shift+A gains an "Images as Planes" entry that imports any image directly as a textured plane with its shader nodes (including transparency for PNGs) already wired up automatically — useful for quickly compositing 2D elements like smoke/dust into a 3D scene.

### Summary
Frame 000 shows the intro: an empty viewport, captioned "I just wanted you to know about this great add-on which comes with Blender, you just need to activate it." Frame 001 shows Blender's User Preferences > Add-ons tab with the search field containing "images as planes" and "Import-Export: Import Images as Planes" listed as a result, captioned "Press CTRL+ALT+U to open the User Preferences. Search for 'images as planes'." Frame 002 shows the same add-on entry with its checkbox area highlighted (red box) and the "Save User Settings" button also highlighted, captioned "Check the box to activate it, and click 'Save User Settings' so it's still activated next time you use Blender." Frame 003 shows a File Browser import dialog with an image file ("smoke.png," 802 KB) selected in a Downloads folder, captioned "Now if you press SHIFT+A you can add 'images as planes'. It will open the import menu. Find the image." Frame 004 shows the imported result: a plane in the viewport displaying a puffy white smoke/cloud PNG with visible transparency (checkered background showing through), and its auto-generated Shader Editor node graph on the right, captioned "What's really cool is that even with transparent images, the nodes are set up automatically." Frame 005 shows a Material Output node in a mostly-empty Shader Editor over a dark viewport, captioned "So you can import for instance some smoke image and add it to your scene" — beginning to composite the smoke plane into an existing 3D scene. Frames 006-007 show the finished composite: the smoke/dust PNG plane placed inside a photorealistic, sunlit, dusty abandoned-room 3D render, blending convincingly with the scene's atmosphere and lighting — demonstrating a practical use case for the imported image plane.

### Key Steps
1. Open User Preferences with **Ctrl+Alt+U** and search "images as planes" in the Add-ons tab.
2. Check the add-on's checkbox to activate it ("Import-Export: Import Images as Planes" — it ships bundled with Blender but starts disabled), then click **Save User Settings** so it stays active in future Blender sessions.
3. With the add-on active, **Shift+A** now includes an **Images as Planes** entry, which opens a File Browser to pick an image file.
4. Select an image (e.g. a PNG with alpha, like a smoke/cloud graphic) to import — it's added to the scene as a plane object with a material and shader node graph already fully wired up automatically, including proper alpha transparency handling for PNGs, with no manual node setup required.
5. Practical use case shown: import a smoke/dust PNG this way and position it within an existing 3D scene (e.g. a photorealistic interior render) to quickly add atmospheric detail without modeling or simulating actual smoke.

### Nodes / Settings
- **Add-on:** Import Images as Planes (bundled with Blender, disabled by default — Preferences > Add-ons > Import-Export category).
- **Import:** Shift+A > Images as Planes (File Browser for image selection).
- **Auto-generated shader graph:** Image Texture node (with alpha) wired into Material Output automatically — no manual node setup needed.

### Difficulty
Beginner

### Blender Version
Not specified — Import Images as Planes ships as a bundled (but disabled-by-default) add-on since early Blender 2.x releases.

### Tags
materials, beginner

---

## Related Tutorials
- [Creating a Realistic Forest in Blender using Billboards (low poly Planes with tree images)](creating-a-realistic-forest-in-blender-using-billboards-low-poly-planes-with-tre.md) — shares beginner; that video's whole particle-scattered-billboard technique depends on the Import Images as Planes add-on introduced here.
- [Daily Blender Tip 114 - Easily Add Camera Movement To A 2D Painting](daily-blender-tip-114---easily-add-camera-movement-to-a-2d-painting.md) — shares materials, beginner; another practical application of Images as Planes, there for a faked-parallax camera-move effect on a 2D painting.
