---
title: Solving Camera Motion
source: Article
url: https://docs.blender.org/manual/en/5.2/movie_clip/tracking/clip/toolbar/solve.html
author: docs.blender.org (Blender 5.2 LTS official docs)
ingested: 2026-09-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
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
