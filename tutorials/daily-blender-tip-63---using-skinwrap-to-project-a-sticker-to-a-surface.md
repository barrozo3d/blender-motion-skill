---
title: Daily Blender Tip 63 - Using SkinWrap To Project A Sticker To A Surface
source: YouTube
url: https://www.youtube.com/watch?v=ZtrD7vxi6ik
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Shrinkwrap modifier + Cycles ray-visibility toggles are consistent across modern Blender versions"
tags: [modelling, materials, workflow, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-63---using-skinwrap-to-project-a-sticker-to-a-surface/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 63 - Using SkinWrap To Project A Sticker To A Surface

**Source:** [YouTube](https://www.youtube.com/watch?v=ZtrD7vxi6ik)
**Author:** Blender Secrets
**Duration:** 1m50s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 2 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (2 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] ーん



---

## Captured Frames

- [0:10] tutorials/frames/daily-blender-tip-63---using-skinwrap-to-project-a-sticker-to-a-surface/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-63---using-skinwrap-to-project-a-sticker-to-a-surface/frame_001.jpg
- [0:50] tutorials/frames/daily-blender-tip-63---using-skinwrap-to-project-a-sticker-to-a-surface/frame_002.jpg
- [1:10] tutorials/frames/daily-blender-tip-63---using-skinwrap-to-project-a-sticker-to-a-surface/frame_003.jpg
- [1:30] tutorials/frames/daily-blender-tip-63---using-skinwrap-to-project-a-sticker-to-a-surface/frame_004.jpg
- [1:45] tutorials/frames/daily-blender-tip-63---using-skinwrap-to-project-a-sticker-to-a-surface/frame_005.jpg

---

## Structured Notes

### Core Technique
Projecting a flat "sticker" image (a logo) onto a curved surface using the **Shrinkwrap-family "Skinwrap" modifier** (Target Method) rather than UV-painting or a Decal system — a heavily subdivided image plane is wrapped directly onto the target object's surface, offset slightly above it to avoid z-fighting, with Cycles Shadow/Glossy visibility disabled so the sticker plane doesn't cast unwanted shadows or reflections.

### Summary
Frame 000 shows the File > Import menu with "Images as Planes" available, over a sphere rendered with an orange/warm HDRI-lit material, captioned "Import your sticker image (your logo for example!) with File>Import>Images As Planes (this is an add-on you can activate in preferences)." Frame 001 shows the imported logo plane (a blue/colorful circular logo) positioned near the sphere with a dense wireframe grid overlay, captioned "Move it closer to the object you want to project it onto and subdivide it a number of times. Press w and choose Subdivide (5 to 10 times)." Frame 002 shows the Modifier stack with **Shrinkwrap** added (Wrap Method, Target field set to the sphere object), captioned "Add the Skinwrap modifier to the sticker plane. In Target pick the other object (the sphere in this case)." — "Skinwrap" here refers colloquially to the Shrinkwrap modifier's Target-based wrap-onto-surface behavior. Frame 003/004 show the Shrinkwrap modifier's "Keep Above Surface" option checked and an Offset field set to a small positive value, plus the Cycles Object Settings' Visibility section (Shadow and Glossy Ray Visibility unchecked), captioned "Click on 'keep above surface' and set the Offset to slightly above zero. In Cycles settings turn off Shadow and Glossy." — the logo now cleanly wrapped onto the sphere's curved surface, matching its contour. Frame 005 shows a distorted/pixelated result on a different close-up object, captioned "If the sticker is distorted, add some more geometry to the object by adding a Subdivision Surface modifier to the other object" — the target object also needs enough resolution for the projected sticker to wrap smoothly.

### Key Steps
1. Enable the **Import Images as Planes** add-on (if not already active) and use **File > Import > Images as Planes** to bring in the sticker/logo image as a textured plane.
2. Move the plane close to the target object's surface and heavily subdivide it (**W > Subdivide**, repeated 5–10 times) so it has enough geometry to conform to a curved surface without distortion.
3. Add a **Shrinkwrap** modifier to the sticker plane, set its **Target** to the object it should project onto.
4. Enable **"Keep Above Surface"** and set a small positive **Offset** so the sticker sits just above the target's surface instead of z-fighting with it.
5. In the object's **Cycles Object Settings > Visibility**, uncheck **Shadow** and **Glossy** ray visibility so the thin sticker plane doesn't cast a shadow or produce a glossy reflection artifact on the underlying object.
6. If the wrapped sticker still looks distorted/pixelated, add a **Subdivision Surface** modifier to the *target* object as well — insufficient target geometry resolution is usually the cause.

### Nodes / Settings
- **Add-on:** Import Images as Planes.
- **Modifier:** Shrinkwrap (Target = the surface to project onto; Keep Above Surface; Offset).
- **Object Properties > Cycles Settings > Visibility:** Shadow, Glossy — disabled on the sticker plane.
- Heavy subdivision (W > Subdivide, 5–10x) on the sticker plane; Subdivision Surface modifier on the target object if resolution is insufficient.

### Difficulty
Beginner

### Blender Version
Not specified — Shrinkwrap modifier + Cycles ray-visibility toggles are consistent across modern Blender versions (Cycles Object Settings Visibility panel present since 2.8x).

### Tags
modelling, materials, workflow, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover Shrinkwrap-based sticker/logo projection specifically.
