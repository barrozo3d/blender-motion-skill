---
title: Motion Tracking Introduction
source: Article
url: https://docs.blender.org/manual/en/5.2/movie_clip/tracking/introduction.html
author: docs.blender.org (Blender 5.2 LTS official docs)
ingested: 2026-09-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
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
