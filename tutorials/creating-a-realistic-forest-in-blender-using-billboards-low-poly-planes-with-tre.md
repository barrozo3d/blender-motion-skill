---
title: Creating a Realistic Forest in Blender using Billboards (low poly Planes with tree images)
source: YouTube
url: https://www.youtube.com/watch?v=mSdzwRcFJM0
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (EEVEE referenced by name, not EEVEE Next; UI matches Blender 3.x/4.x particle system layout)"
tags: [particles, camera, organic, beginner]
extraction_status: complete
frames_dir: tutorials/frames/creating-a-realistic-forest-in-blender-using-billboards-low-poly-planes-with-tre/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Creating a Realistic Forest in Blender using Billboards (low poly Planes with tree images)

**Source:** [YouTube](https://www.youtube.com/watch?v=mSdzwRcFJM0)
**Author:** Blender Secrets
**Duration:** 1m54s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- WARNING: Thin transcript: 1053 chars. Notes may be shallow — consider --whisper-model small.

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Buildboards are a very low poly wave to add background detail.
[0:07] They are basically images that always face the camera.
[0:13] As you can see, they only work from the camera view.
[0:19] You can import a PNG image with transparency using the images as planes add-on.
[0:24] In EEVEE, remember to change the transparency mode.
[0:29] Then add a Track 2 constraint to the plane.
[0:33] As the target of the constraint, choose the camera.
[0:41] In this case, 2 should be set to Z and up should be set to Y.
[0:54] Now that we know how to make billboards, let's use them to create a forest.
[1:00] Make sure the origin of the image plane is at its bottom.
[1:03] If you have multiple planes with images, select them all and add them to a new collection
[1:07] by pressing M.
[1:12] Hide that collection and add a particle system to a ground plane or terrain that you've
[1:16] created.
[1:17] Set it to Hair.
[1:22] Under Render As, choose Collection.
[1:25] Choose the collection with the image planes as the instance collection.
[1:29] Change the size and size randomness for more variation.
[1:33] Enable object rotation.
[1:40] Now as you can see, the particles follow the camera.



---

## Captured Frames

- [0:00] tutorials/frames/creating-a-realistic-forest-in-blender-using-billboards-low-poly-planes-with-tre/frame_000.jpg
- [0:19] tutorials/frames/creating-a-realistic-forest-in-blender-using-billboards-low-poly-planes-with-tre/frame_001.jpg
- [0:29] tutorials/frames/creating-a-realistic-forest-in-blender-using-billboards-low-poly-planes-with-tre/frame_002.jpg
- [0:54] tutorials/frames/creating-a-realistic-forest-in-blender-using-billboards-low-poly-planes-with-tre/frame_003.jpg
- [1:12] tutorials/frames/creating-a-realistic-forest-in-blender-using-billboards-low-poly-planes-with-tre/frame_004.jpg
- [1:22] tutorials/frames/creating-a-realistic-forest-in-blender-using-billboards-low-poly-planes-with-tre/frame_005.jpg
- [1:29] tutorials/frames/creating-a-realistic-forest-in-blender-using-billboards-low-poly-planes-with-tre/frame_006.jpg
- [1:40] tutorials/frames/creating-a-realistic-forest-in-blender-using-billboards-low-poly-planes-with-tre/frame_007.jpg

---

## Structured Notes

### Core Technique
Camera-facing "billboard" image planes (Images as Planes + Track To constraint) instanced across a terrain via a Hair particle system, to fake a dense background forest cheaply.

### Summary
Frame 000 shows the payoff: a misty mountain valley whose midground/background trees are entirely billboards, invisible as flat cards from the render camera. Frame 001 shows the setup step — importing tree PNGs (with alpha) via the Images as Planes add-on, using "Offset Planes" to place several at once. Frame 002 shows a single tree billboard selected with its Object Constraint panel open, ready for the Track To constraint. Frame 003 confirms the same valley payoff shot from a second angle. Frame 004 shows two billboards (a pine and a palm) grouped for the "Trees" collection, with Filmic color management visible in the sidebar. Frame 005 shows the ground plane in edit-mode-like wireframe with a Hair particle system's Emission/Advanced panel open (Number 30000, Hair Length 4m, Segments 5), Render As set to Path, still pre-collection. Frame 006 shows the same particle system reconfigured to Render As Collection, Instance Collection "Trees", with Scale Randomness enabled — viewport shows thousands of orange bounding boxes standing in for the not-yet-rendered billboards. Frame 007 shows the final result: a full instanced pine forest filling the ground plane in viewport shading.

### Key Steps
1. Import each tree image (PNG with alpha) via `Shift+A > Image > Images as Planes`; enable "Offset Planes" to import multiple images as separate, spaced-out planes in one operation.
2. In EEVEE, open the plane's Material Settings and set the Blend Mode (transparency mode) so the PNG's alpha channel renders correctly instead of showing a black/opaque quad.
3. Add a `Track To` constraint to each billboard plane; set Target = Camera, To = Z, Up = Y, so the flat plane always rotates to face the render camera.
4. Before finishing each billboard, make sure its object origin sits at the base/bottom of the image (not the center) so it "plants" correctly on the ground later.
5. Select all finished billboard planes and group them into a new Collection with `M > New Collection` (named e.g. "Trees"); hide that collection from the viewport so the raw billboards aren't visible as loose objects.
6. On the ground/terrain mesh, add a Particle System and set its type to `Hair`.
7. Under the particle system's Render panel, set Render As = `Collection` and pick the billboard collection ("Trees") as the Instance Collection.
8. Tune Scale and Scale Randomness for natural size variety, and enable Object Rotation (and Object Scale) so instanced billboards aren't all identical.
9. Result: the particle system scatters camera-facing billboard trees across the whole terrain, producing a full background forest at a fraction of the cost of real 3D tree geometry.

### Nodes / Settings
- Add menu: Image > Images as Planes (`Import Images as Planes` operator), option: Offset Planes (batch-import multiple images as separate planes)
- Material Settings (EEVEE): Blend Mode set for alpha transparency on the PNG plane material
- Object Constraint: Track To — Target: Camera, To: Z, Up: Y
- Particle System (Hair type) Emission panel: Number ≈ 30000, Hair Length ≈ 4 m, Segments: 5 (seen mid-setup before switching Render As)
- Particle System Render panel: Render As = Collection, Instance Collection = "Trees", Scale, Scale Randomness (enabled), Object Rotation (enabled), Object Scale (enabled)
- Collection: "Trees" (holds the individually-constrained billboard planes, hidden from direct render)

### Difficulty
Beginner

### Blender Version
Not specified in transcript or frames — references "EEVEE" generically (not EEVEE Next) and the particle-system panel layout (Advanced Emission section, Hair Length/Segments fields) matches Blender 3.x/4.x.

### Tags
particles, camera, organic, beginner

---

## Related Tutorials
- [Procedural Grass in Blender Geometry Nodes](procedural-grass-in-blender-geometry-nodes-fast-viewport-se.md) — shares particles, organic, beginner; same "cheap background scatter that reads correctly from camera" goal, just via Geometry Nodes instancing instead of a legacy Hair particle system + billboard constraint.
