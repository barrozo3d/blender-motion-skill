---
title: Offset Edge Slide - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=y7EuYx9CaTU
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Shift+Ctrl+R Offset Edge Slide is a long-standing core shortcut, version-agnostic"
tags: [modelling, procedural, beginner]
extraction_status: complete
frames_dir: tutorials/frames/offset-edge-slide---blender-secrets/
frame_count: 4
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Offset Edge Slide - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=y7EuYx9CaTU)
**Author:** Blender Secrets
**Duration:** 1m33s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] If you want to add edge loops on either side of this middle edge loop,
[0:03] one way you can do that is by pressing Ctrl R and then just moving each edge loop to where you want.
[0:08] However, this is not super precise. If we look at the edge lens, by enabling this here,
[0:13] and then selecting these two edges, you can see that they have different lengths.
[0:16] So let me just dissolve these two edges and turn this off.
[0:20] And another way to do it is by alt and left clicking on this middle edge loop,
[0:23] and then pressing Ctrl B to bevel. And then either you can scroll the mouse wheel up once
[0:28] or press plus on the numpad or press the S key and move the mouse slightly to the right to add
[0:33] another edge loop in the middle. And this is added to edge loops on either side of the middle edge
[0:37] loop. However, as you can see, it has also changed the shape slightly. So let me just want to do that.
[0:42] So to avoid the shape changing, when I'm beveling, I can press P for profile and then move the mouse
[0:47] wheel. And this, as you can see, changes the profile of the bevel. So if I either move the
[0:51] mouse all the way to the right in this case, or press one for the profile of one, then I get
[0:56] the original shape. However, the most efficient and easiest way to do this is to use the keyboard
[1:00] shortcut Shift Ctrl R. And this edge, you can see, adds two edge loops around the selected one.
[1:05] And this is called offset edge slide. And I can open this menu here. And here, as you can see,
[1:09] I can still change the offset factor. And I can hold Shift if I want to be more precise.
[1:13] And there are some options here. So for example, we have correct UVs. And this helps to protect
[1:19] the UV map. However, in this case, I think there is absolutely no difference. The UVs are protected
[1:24] either way. Oh, that's good. If you like this kind of tip, check out my Blender book,
[1:27] which contains over 600 Blender tips, all in one convenient and destruction free place.



---

## Captured Frames

- [0:08] tutorials/frames/offset-edge-slide---blender-secrets/frame_000.jpg
- [0:33] tutorials/frames/offset-edge-slide---blender-secrets/frame_001.jpg
- [0:56] tutorials/frames/offset-edge-slide---blender-secrets/frame_002.jpg
- [1:05] tutorials/frames/offset-edge-slide---blender-secrets/frame_003.jpg

---

## Structured Notes

### Core Technique
Comparing three ways to add two symmetric edge loops on either side of an existing middle loop — manual Ctrl+R (imprecise), Bevel with profile correction (works but reshapes the surface unless tuned), and the dedicated Shift+Ctrl+R "Offset Edge Slide" shortcut (fastest, most precise, no shape distortion).

### Summary
Frame 000 shows the first (imprecise) method: two manually-placed Ctrl+R loop cuts flanking the center edge loop of a pentagon-roofed cube shape, with the Loop Cut and Slide redo panel open (Number of Cuts: 2, Smoothness, Falloff). Frame 001 shows the Bevel method's problem: beveling the selected middle edge loop (Ctrl+B, orange highlighted band) has added two new loops but visibly reshaped/rounded the surface compared to the original flat panel. Frame 002 shows the fix: the same Bevel operation with its Profile Shape set to 1 (redo panel: Width Type Offset, Segments, Profile 1.000, Loop Slide) — restoring the original flat shape while still keeping the two new loops. Frame 003 shows the recommended method's result: Shift+Ctrl+R (Offset Edge Slide, confirmed by the on-screen "Ctrl+Shift+R" shortcut badge) cleanly adding two evenly-spaced, undistorted loops around the selected middle edge loop in a single step.

### Key Steps
1. **Method 1 (manual, imprecise):** press Ctrl+R twice to add two separate loop cuts, then manually slide each one to sit next to the existing middle loop. Problem: without a numeric/precise placement, the two new edges end up different distances from center — verifiable by enabling the Edge Length overlay (Mesh Analysis / Item panel) and comparing the selected edges' lengths.
2. **Method 2 (Bevel the middle loop):** Alt+click the middle edge loop to select it, then Ctrl+B to bevel; scroll the mouse wheel up once (or press Numpad+, or press S and nudge the mouse slightly) to add exactly one loop on each side of the selected one. Drawback: beveling can visibly reshape/round the surrounding surface. Fix: during the bevel, press P for Profile and adjust with the scroll wheel, or type 1 for Profile Shape 1 (or drag the mouse fully to one side) to restore the original flat shape while keeping the added loops.
3. **Method 3 (recommended — Offset Edge Slide):** with the middle edge loop selected, press **Shift+Ctrl+R** — this adds two new evenly-offset loops around the selected one in a single, non-distorting operation. Open the operator's redo panel to adjust the Offset Factor numerically (hold Shift while dragging for finer precision). The redo panel also includes a "Correct UVs" option to protect the UV map during the operation — though in the demonstrated case, UVs were unaffected either way.

### Nodes / Settings
- **Loop Cut and Slide:** Ctrl+R (manual placement, Number of Cuts, Smoothness, Falloff).
- **Bevel:** Ctrl+B (Segments via scroll wheel/Numpad+/S; Profile Shape via P or typing a value, e.g. 1 for flat).
- **Offset Edge Slide:** Shift+Ctrl+R (Offset Factor, hold Shift for precision, Correct UVs option).
- **Diagnostics:** Edge Length overlay/Mesh Analysis (comparing selected edge lengths for precision-checking).

### Difficulty
Beginner

### Blender Version
Not specified — Shift+Ctrl+R (Offset Edge Slide) is a long-standing core Blender shortcut, version-agnostic.

### Tags
modelling, procedural, beginner

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover the Offset Edge Slide operator specifically.
