---
title: Tracking Camera Panel
source: Article
url: https://docs.blender.org/manual/en/5.2/movie_clip/tracking/clip/sidebar/track/camera.html
author: docs.blender.org (Blender 5.2 LTS official docs)
ingested: 2026-09-04
blender_version: "Blender 5.2"
tags: [tracking, camera-tracking, camera, blender-5x, advanced]
extraction_status: complete
frames_dir: tutorials/frames/tracking-camera-panel/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Tracking Camera Panel

**Source:** [Article](https://docs.blender.org/manual/en/5.2/movie_clip/tracking/clip/sidebar/track/camera.html)
**Author:** docs.blender.org (Blender 5.2 LTS official docs)
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Camera ¶ This panel contains all settings of the camera used for filming the movie which is currently being edited in the Clip editor. Different predefined settings can be used here and can be chosen from the panel header. But such settings as distortion coefficients and principal point are not included in the presets and should be filled in even if camera presets are used. Sensor Width Is the width of the CCD sensor in the camera. This value can be found in camera specifications. Pixel Aspect Is the pixel aspect of the CCD sensor. This value can be found in camera specifications, but can also be guessed. For example, you know that the footage should be 1920×1080, but the images themselves are 1280×1080. In this case, the pixel aspect is: 1920 / 1280 = 1.5. Lens ¶ Focal Length The focal length with which the movie was shot. It can be set in millimeters or pixels. Optical Center Defines the optical center (also known as the principal point ) of the lens used by the camera. In most cases this coincides with the center of the image, but certain lenses may have an offset optical center. Refer to the specifications of camera or lens used if needed. The values are given in normalized image coordinates. Lens Distortion Mathematical function to convert distorted to undistorted coordinates. Polynomial : Polynomial radial distortion. Uses three distortion coefficients: K1, K2, and K3. Division : It defines high distortions, which makes this model suitable much better for cameras with fisheye lenses. Use two distortion coefficients: K1, K2. Nuke : Distortion model used by the Nuke compositor. Use two distortion coefficients K1, K2. Brown : Brown-Conrady is one of most advanced mathematical lens distortion models. Used to model both radial and tangential distortion. Can use up to four radial distortion coefficients: K1 - K4 and up to two tangential distortion coefficients: P1 and P2. Coefficients Coefficients are used to compensate for lens distortion when the movie was shot. Currently these values can be tweaked by hand only (there are no calibration tools yet) using tools available in Distortion mode. To do this tweak K1 until the solving is the closest to the known focal length (but also take grid and annotations into account to prevent “impossible” distortion). Radial Distortion Coefficients (K1 - K4) The coefficients in lens distortion models work independent from each other. Positive values will give a barrel distortion while negative values give a pincushion distortion. With a mixture of both negative and positive coefficients you can define more complicated mustache distortions or other complex distortions, that are less common but not rare. Example of radial distortion for positive and negative K coefficients. ¶ Tangential Distortion Coefficients (P1, P2) Works independent and allow to compensate for situations when the sensor is not perpendicular to a group of lens. The optical center (also called principal point) will be shifted (distorted) from the center of the sensor. P1 is used to compensate for sensor rotation in Z (vertical) axes, while P2 is for compensating sensor rotation in X (horizontal) axes. Such distortions can be found in sources from cameras with a sensor stabilization system. Example of tangential distortion for P coefficients. ¶ On this page Camera Lens



---

## Structured Notes

### Core Technique
Supply the real camera's intrinsics — **sensor width, pixel aspect, focal length, optical centre** — and choose a **lens distortion model** with its coefficients, because the solve is only as accurate as these are.

### Summary
The page behind the "refining intrinsics, lens distortion" half of the gap, and it opens with a warning that costs people solves: **camera presets do not include the distortion coefficients or the principal point**, so those must be filled in even when a preset is used. Four distortion models are offered and they are not interchangeable — **Polynomial** (radial, coefficients K1–K3), **Division** (K1, K2; explicitly better suited to fisheye), **Nuke** (K1, K2; the model the Nuke compositor uses — the one to pick when the plate is round-tripping through Nuke), and **Brown** (Brown-Conrady, the most advanced: up to four radial coefficients K1–K4 *and* two tangential P1, P2). The coefficient behaviour is stated plainly: **positive radial values give barrel distortion, negative give pincushion**, and mixing signs models moustache distortion. **Tangential** coefficients compensate for a sensor that is not perpendicular to the lens group — P1 for sensor rotation in Z, P2 for rotation in X. There is **no calibration tool**: the documented method is to tweak K1 until the solve lands closest to the known focal length, while watching the grid and annotations so you do not dial in an "impossible" distortion.

### Key Steps
1. Enter **Sensor Width** from the camera specifications.
2. Set **Pixel Aspect** — from the specs, or derived: footage that should be 1920×1080 delivered as 1280×1080 gives 1920 / 1280 = **1.5**.
3. Set **Focal Length** in millimetres or pixels.
4. Set **Optical Center** (the principal point) in normalised image coordinates — usually the image centre, but some lenses are offset; check the lens specs.
5. ⚠️ If you use a camera **preset**, still fill in **distortion coefficients and principal point** yourself — presets do not carry them.
6. Choose the **Lens Distortion** model: **Polynomial** (K1–K3), **Division** (K1, K2 — fisheye), **Nuke** (K1, K2 — matches the Nuke compositor), **Brown** (K1–K4 radial plus P1, P2 tangential).
7. Tune **radial** coefficients knowing positive = barrel, negative = pincushion, and mixed signs = moustache or more complex distortion.
8. Use **tangential** P1 / P2 where the sensor is not perpendicular to the lens — P1 for Z rotation, P2 for X.
9. Calibrate by hand: adjust **K1** until the solve is closest to the known focal length, cross-checking against the grid and annotations in **Distortion mode** so the result stays physically plausible.

### Nodes / Settings
- **Sensor Width**, **Pixel Aspect** (derivable from delivered vs intended resolution).
- **Lens**: **Focal Length** (mm or px), **Optical Center** / principal point (normalised image coordinates).
- **Lens Distortion** models: **Polynomial** (K1, K2, K3), **Division** (K1, K2 — fisheye), **Nuke** (K1, K2), **Brown** (K1–K4 radial, P1–P2 tangential).
- **Radial coefficients**: positive → barrel, negative → pincushion, mixed → moustache.
- **Tangential coefficients**: P1 (sensor rotation in Z), P2 (sensor rotation in X).
- ⚠️ Presets exclude distortion coefficients and principal point. No calibration tool — hand-tune K1 against the known focal length in **Distortion mode**.

### Difficulty
Advanced

### Blender Version
Blender 5.2.

### Tags
`tracking`, `camera-tracking`, `camera`, `blender-5x`, `advanced`

---

## Related Tutorials
- [Solving Camera Motion](solving-camera-motion.md) — the **Refine** options that let the solver improve these same intrinsics.
- [Motion Tracking Introduction](motion-tracking-introduction.md) — the Annotation and OpenCV calibration routes.

---

> **Provenance.** Official Blender 5.2 LTS documentation, pinned to the versioned
> path (`docs.blender.org/manual/en/5.2/` and `docs.blender.org/api/5.2/`) rather
> than `latest`, so the entry keeps saying what 5.2 says after `latest` moves on.
> ⚠️ **These pages append site chrome to `<title>`** (" - Blender 5.2 LTS Manual",
> " - Blender Python API"), so `--title` is required when ingesting them.
> **Blender 5.2.1 LTS is installed on this machine** (`D:\Steam\steamapps\common\Blender`,
> build 2026-08-25), so the documented behaviour can be checked against the real
> build rather than taken on trust.
