---
title: Solving Camera Motion
source: Article
url: https://docs.blender.org/manual/en/5.2/movie_clip/tracking/clip/toolbar/solve.html
author: docs.blender.org (Blender 5.2 LTS official docs)
ingested: 2026-09-04
blender_version: "Blender 5.2"
tags: [tracking, camera-tracking, blender-5x, advanced]
extraction_status: complete
frames_dir: tutorials/frames/solving-camera-motion/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Solving Camera Motion

**Source:** [Article](https://docs.blender.org/manual/en/5.2/movie_clip/tracking/clip/toolbar/solve.html)
**Author:** docs.blender.org (Blender 5.2 LTS official docs)
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Solve ¶ Plane Track ¶ See Create Plane Track . Solve ¶ Tripod Tripod Motion can be used for footage where the camera does not move and only rotates. Such footage can’t be tracked with a generic solver approach, and it is impossible to determine the actual feature points in space due to a lack of information. So this solver will solve only the relative camera rotation and then reproject the feature points into a sphere, with the same distance between feature and camera for all feature points. Note This is special type of camera solver and it behaves different from regular solver. It means using more tracks doesn’t imply more accurate solution. Having 5-10 tracks on frame is likely what shall be commonly used for this kind of solver. Keyframe Automatically select keyframes for initial reconstruction. This option enables complex algorithms which tries to find a keyframe pair with minimal reconstruction error and best scene scale guess. Keyframe A/B Start (A) and End (B) frame of the range used for reconstruction. Refine Specifies which parameters should be refined during solve. Such refining is useful when you are not sure about some camera intrinsics, and solver should try to find the best parameter for those intrinsics. But you still have to know approximate initial values – it will fail to find correct values if they were set completely incorrectly initially. Focal Length Refine the camera’s Focal Length . Optical Center Refine the camera’s Optical Center . Radial Distortion Refine the camera’s Radial Distortion Parameters . Tangential Distortion Refine the camera’s Tangential Distortion Parameters . Solve Camera/Object Motion See Solve Camera/Object Motion . Cleanup ¶ This panel contains operators and their settings which are needed to clean up bad tracks: tracks which are not tracked long enough or which failed to reconstruct accurately. Frames Tracks or tracked segments shorter than this number of frames will be removed. Error Tracks which have reprojection error higher than this value will be removed. Type Several actions can be performed for bad tracks: Select : They can simply be selected. Delete Track : The whole track can be deleted. Delete Segments : Bad segments of tracked sequence can be removed. Clean Tracks See Clean Tracks . Filter Tracks See Filter Tracks . Geometry ¶ 3D Markers to Mesh See 3D Markers to Mesh . Link Empty to Track See Link Empty to Track . Orientation ¶ Scene orientation tools can be used for orienting object to bundles. Floor See Set Origin . Wall See Set Floor . Set Origin See Set Floor . Set X, Y Axis See Set X/Y Axis . Set Scale See Set Scale . Apply Scale See Apply Solution Scale . Distance Distance in active scene units which is used by Set/Apply scale. Scene Setup ¶ Set as Background See Set as Background . Setup Tracking Scene See Setup Tracking Scene . On this page Solve Plane Track Solve Cleanup Geometry Orientation Scene Setup



---

## Structured Notes

### Core Technique
Solve the reconstruction — optionally letting **Refine** improve the intrinsics you were unsure of — then **Cleanup** by reprojection error and **orient** the solved scene with floor, origin, axis and scale tools.

### Summary
This page carries three of the four things the gap asked for. **Refine** decides which intrinsics the solver is allowed to adjust — Focal Length, Optical Center, Radial Distortion, Tangential Distortion — and comes with the essential caveat that it still needs **approximate initial values**: it will fail if they start completely wrong. **Cleanup** turns solve error into an operation: set a minimum **Frames** length and a maximum reprojection **Error**, then choose whether bad tracks are merely **Selected**, **deleted whole**, or have only their bad **Segments** removed. **Orientation** is the scene-scale-and-floor half — Floor, Wall, Set Origin, Set X/Y Axis, Set Scale and Apply Scale, with a **Distance** field in active scene units driving Set/Apply Scale. The **Tripod** solver is called out as behaving differently from the regular one: it solves only relative camera *rotation* and reprojects features onto a sphere at equal distance, and because of that **more tracks do not mean a better solution — 5–10 tracks per frame is the normal working range**. **Keyframe** can pick the A/B reconstruction pair automatically, searching for minimal reconstruction error and the best scene-scale guess.

### Key Steps
1. Choose the solver: regular, or **Tripod** for footage where the camera only rotates — remembering feature depth is unknowable there, so **5–10 tracks per frame is the target, not more**.
2. Let **Keyframe** auto-select the reconstruction pair (it optimises for minimal reconstruction error and scene scale), or set **Keyframe A/B** by hand.
3. Enable the **Refine** parameters you are genuinely unsure of — **Focal Length**, **Optical Center**, **Radial Distortion**, **Tangential Distortion** — having first entered approximate values, because refinement cannot recover from wildly wrong starting points.
4. Run **Solve Camera/Object Motion**.
5. **Cleanup**: set **Frames** (minimum tracked length) and **Error** (maximum reprojection error), then pick the **Type** — `Select`, `Delete Track`, or `Delete Segments`.
6. Reach for **Clean Tracks** and **Filter Tracks** for the related cleanup operators.
7. Build geometry from the solve with **3D Markers to Mesh**, or attach objects with **Link Empty to Track**.
8. **Orient the scene**: **Floor**, **Wall**, **Set Origin**, **Set X/Y Axis**, then **Set Scale** / **Apply Scale** with **Distance** in active scene units.
9. Finish with **Set as Background** and **Setup Tracking Scene** to get a compositing-ready scene in one step.

### Nodes / Settings
- **Solve**: **Tripod** (rotation only, features reprojected to a sphere; 5–10 tracks typical), **Keyframe** auto-selection, **Keyframe A/B**.
- **Refine**: Focal Length, Optical Center, Radial Distortion, Tangential Distortion — requires approximate initial values.
- **Cleanup**: **Frames** (minimum length), **Error** (maximum reprojection error), **Type** = `Select` / `Delete Track` / `Delete Segments`; also **Clean Tracks**, **Filter Tracks**.
- **Geometry**: **3D Markers to Mesh**, **Link Empty to Track**.
- **Orientation**: **Floor**, **Wall**, **Set Origin**, **Set X/Y Axis**, **Set Scale**, **Apply Scale**, **Distance** (active scene units).
- **Scene Setup**: **Set as Background**, **Setup Tracking Scene**. Also **Plane Track** (Create Plane Track).

### Difficulty
Advanced

### Blender Version
Blender 5.2.

### Tags
`tracking`, `camera-tracking`, `blender-5x`, `advanced`

---

## Related Tutorials
- [Tracking Camera Panel](tracking-camera-panel.md) — the intrinsics **Refine** adjusts, and the models behind them.
- [Editing Motion Tracks](editing-motion-tracks.md) — producing the tracks Cleanup then filters.
- [Object Solver Constraint](object-solver-constraint.md) — what an object solve is applied through.

---

> **Provenance.** Official Blender 5.2 LTS documentation, pinned to the versioned
> path (`docs.blender.org/manual/en/5.2/` and `docs.blender.org/api/5.2/`) rather
> than `latest`, so the entry keeps saying what 5.2 says after `latest` moves on.
> ⚠️ **These pages append site chrome to `<title>`** (" - Blender 5.2 LTS Manual",
> " - Blender Python API"), so `--title` is required when ingesting them.
> **Blender 5.2.1 LTS is installed on this machine** (`D:\Steam\steamapps\common\Blender`,
> build 2026-08-25), so the documented behaviour can be checked against the real
> build rather than taken on trust.
