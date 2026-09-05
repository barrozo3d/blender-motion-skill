---
title: Motion Tracking Introduction
source: Article
url: https://docs.blender.org/manual/en/5.2/movie_clip/tracking/introduction.html
author: docs.blender.org (Blender 5.2 LTS official docs)
ingested: 2026-09-04
blender_version: "Blender 5.2"
tags: [tracking, camera-tracking, blender-5x, beginner]
extraction_status: complete
frames_dir: tutorials/frames/motion-tracking-introduction/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Motion Tracking Introduction

**Source:** [Article](https://docs.blender.org/manual/en/5.2/movie_clip/tracking/introduction.html)
**Author:** docs.blender.org (Blender 5.2 LTS official docs)
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Introduction ¶ Motion Tracking is used to track the motion of objects and/or a camera and, through the constraints, to apply this tracking data to 3D objects (or just one), which have either been created in Blender or imported into the application. Blender’s motion tracker supports a couple of very powerful tools for 2D tracking and 3D motion reconstruction, including camera tracking and object tracking, as well as some special features like the plane track for compositing. Tracks can also be used to move and deform masks for rotoscoping in the Mask Editor, which is available as a special mode in the Movie Clip Editor. Views ¶ In Tracking Mode there are three different views available. You can toggle between view modes using the View selector, which is located in the header. When you selected a view in the whole area of the Movie Clip editor will change. Hence, to display a curve or dope sheet view, the editor must be split into two, with one switched to the curve or dope sheet view. Manual Lens Calibration ¶ All cameras record distorted video. Nothing can be done about this because of the manner in which optical lenses work. For accurate camera motion, the exact value of the focal length and the “strength” of distortion are needed. Currently, focal length can be automatically obtained only from the camera’s settings or from the EXIF information. There are some external tools which can help to find approximate values to compensate for distortion. There are also fully manual tools where you can use a grid which is getting affected by distortion model and deformed cells defines straight lines in the footage. Within Blender you can use the Annotation tool for this – just draw a line which should be straight on the footage using poly line brush and adjust the distortion values to make the annotations match lines on the footage. To calibrate your camera more accurately, use the Grid calibration tool from OpenCV. OpenCV is using the same distortion model, so it should not be a problem. Camera and Object Motion Solving ¶ Blender not only supports the solving of camera motion, including tripod shots, but also the solving of object motion in relation to the motion of the camera. In addition to that there is the Plane Track, which solves the motion of all markers on one plane. Tools for Scene Orientation and Stabilization ¶ After solve, you need to orient the real scene in the 3D scene for more convenient compositing. There are tools to define the floor, the scene origin, and the X/Y axes to perform scene orientation. Sometimes, the video footage includes spurious jumps and tilting movements, like e.g. when using a hand-held camera. Based on some tracked image elements, the 2D Stabilization is able to detect and compensate such movements to improve the quality of the final result. On this page Introduction Views Manual Lens Calibration Camera and Object Motion Solving Tools for Scene Orientation and Stabilization



---

## Structured Notes

### Core Technique
Track 2D features in footage, reconstruct 3D camera or object motion from them, and apply the result to 3D objects through constraints — then orient the solved scene with floor, origin and axis tools.

### Summary
The orientation page for Blender's tracker, and it is honest about the hard part: **all cameras record distorted video**, and an accurate solve needs the exact focal length and the strength of that distortion. Focal length can be read automatically only from camera settings or EXIF; distortion cannot, and there is **no built-in calibration tool**. The documented in-Blender workaround is manual and clever — draw with the **Annotation** tool's poly-line brush along something that should be straight in the footage, then adjust the distortion values until the annotation matches the line. For real accuracy the page sends you to **OpenCV's grid calibration**, noting OpenCV uses the same distortion model so the values transfer. Beyond that it names the scope: 2D tracking and 3D reconstruction, **camera** and **object** motion solving including **tripod** shots, the **plane track** for compositing, tracks driving masks for rotoscoping in the Mask Editor, scene-orientation tools for floor/origin/axes after the solve, and **2D stabilization** for hand-held jumps and tilts.

### Key Steps
1. Load footage into the Movie Clip Editor and work in **Tracking Mode**, switching between its three views with the **View** selector — split the area to see a curve or dope sheet view alongside.
2. Get the **focal length** from the camera settings or EXIF where possible.
3. Calibrate distortion, because nothing does it for you: draw a poly-line **Annotation** over something known to be straight, then adjust the distortion values until they match.
4. For accuracy, calibrate with **OpenCV's grid tool** — same distortion model, so the coefficients carry over.
5. Solve **camera** motion, **object** motion relative to the camera, or a **tripod** shot; use a **plane track** where all markers lie on one plane.
6. **Orient the solved scene** — define the floor, the scene origin and the X/Y axes so compositing is workable.
7. Apply **2D stabilization** when hand-held footage carries spurious jumps and tilts.
8. Reuse tracks to move and deform **masks** for rotoscoping in the Mask Editor.

### Nodes / Settings
- **Movie Clip Editor › Tracking Mode**, three views via the View selector; Mask Editor as a separate mode.
- Solve types: camera motion, **tripod**, object motion, **plane track**.
- Calibration: focal length from settings/EXIF; distortion by **Annotation** poly-line matching, or **OpenCV grid calibration** (same model).
- Post-solve: floor / scene origin / X-Y axis orientation tools; **2D Stabilization**.
- Output path: constraints applying tracking data to 3D objects.

### Difficulty
Beginner

### Blender Version
Blender 5.2.

### Tags
`tracking`, `camera-tracking`, `blender-5x`, `beginner`

---

## Related Tutorials
- [Tracking Camera Panel](tracking-camera-panel.md) — the intrinsics and distortion models this page says you must supply.
- [Solving Camera Motion](solving-camera-motion.md) — the solve, refine and orientation tools.
- [Editing Motion Tracks](editing-motion-tracks.md) — the 2D tracking work that comes first.
- [Object Solver Constraint](object-solver-constraint.md) — applying an object solve to a Blender object.

---

> **Provenance.** Official Blender 5.2 LTS documentation, pinned to the versioned
> path (`docs.blender.org/manual/en/5.2/` and `docs.blender.org/api/5.2/`) rather
> than `latest`, so the entry keeps saying what 5.2 says after `latest` moves on.
> ⚠️ **These pages append site chrome to `<title>`** (" - Blender 5.2 LTS Manual",
> " - Blender Python API"), so `--title` is required when ingesting them.
> **Blender 5.2.1 LTS is installed on this machine** (`D:\Steam\steamapps\common\Blender`,
> build 2026-08-25), so the documented behaviour can be checked against the real
> build rather than taken on trust.
