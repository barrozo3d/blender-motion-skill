---
title: Rendering From The Command Line
source: Article
url: https://docs.blender.org/manual/en/5.2/advanced/command_line/render.html
author: docs.blender.org (Blender 5.2 LTS official docs)
ingested: 2026-09-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/rendering-from-the-command-line/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Rendering From The Command Line

**Source:** [Article](https://docs.blender.org/manual/en/5.2/advanced/command_line/render.html)
**Author:** docs.blender.org (Blender 5.2 LTS official docs)
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Rendering From The Command Line ¶ In some situations we want to increase the render speed, access Blender remotely to render something or build scripts that use the command line. One advantage of using the command line is that we do not need a graphical display (no need for X server on Linux for example) and consequently we can render via a remote shell (typically SSH). See Command Line Arguments for a full list of arguments (for example to specify which scene to render, the end frame number, etc.), or simply run: blender --help See Command Line Launching for specific instructions on launching Blender from the command line. Note Arguments are executed in the order they are given! The following command will not work, since the output and extension are set after Blender is told to render: blender -b file.blend -a -x 1 -o //render The following command will behave as expected: blender -b file.blend -x 1 -o //render -a Always position -f or -a as the last arguments. Single Image ¶ blender -b file.blend -f 10 -b Render in the background (without UI). file.blend Path to the blend-file to render. -f 10 Render only the 10th frame. blender -b file.blend -o /project/renders/frame_##### -F OPEN_EXR -f -2 -o /project/renders/frame_##### Path of where to save the rendered image, using five padded zeros for the frame number. -F OPEN_EXR Override the image format specified in the blend-file and save to an OpenEXR image. -f -2 Render only the second last frame. Warning Arguments are case sensitive! -F and -f are not the same. Animation ¶ blender -b file.blend -a -a Render the whole animation using all the settings saved in the blend-file. blender -b file.blend -E CYCLES -s 10 -e 500 -t 2 -a -E CYCLES Use the “Cycles Render” engine. For a list of available render engines, run blender -E help . -s 10 -e 500 Set the start frame to 10 and the end frame to 500 . -t 2 Use only two threads. Cycles ¶ In addition to the options above, which apply to all render engines, Cycles has additional options to further control its behavior. See Cycles Render Options On this page Rendering From The Command Line Single Image Animation Cycles



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
