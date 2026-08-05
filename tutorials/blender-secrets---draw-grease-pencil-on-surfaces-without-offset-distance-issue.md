---
title: Blender Secrets - Draw Grease Pencil On Surfaces (without offset distance issue)
source: YouTube
url: https://www.youtube.com/watch?v=xLAlFoRPTPM
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (core Grease Pencil/Curve workflow, 2.9x-5.x)"
tags: [modelling, procedural, materials, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---draw-grease-pencil-on-surfaces-without-offset-distance-issue/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - Draw Grease Pencil On Surfaces (without offset distance issue)

**Source:** [YouTube](https://www.youtube.com/watch?v=xLAlFoRPTPM)
**Author:** Blender Secrets
**Duration:** 1m53s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] To draw on top of an object using grease pencil, add a blank grease pencil object.
[0:08] Switch to draw mode.
[0:11] To see the stroke more clearly, you can change the base color of the grease pencil material.
[0:17] Set stroke placement to surface.
[0:19] The offset value determines the distance between the strokes and the surface.
[0:24] If the value is zero, your strokes will overlap with the object.
[0:29] A small value like 0.01 keeps it just above the surface.
[0:35] The offset distance is also influenced by zooming in and out on the object.
[0:42] To avoid this, press 5 on the numpad.
[0:46] This toggles between perspective and orthographic view.
[0:50] In orthographic view, zooming in and out has no influence on the offset distance.
[0:56] Press 5 again when you want to toggle back to perspective view.
[1:00] Press Tab for edit mode.
[1:03] After drawing strokes on the surface, you can make the strokes more smooth by right-clicking
[1:07] and choosing smooth.
[1:09] Repeat it a few times with Shift R until it looks smooth enough.
[1:16] You can turn the grease pencil object into curves.
[1:22] Disable the visibility of the grease pencil object in the Outliner.
[1:27] Select the curve which is called GP underscore layer.
[1:30] In edit mode, right-click again and choose Decimate Curve to reduce the complexity.
[1:35] I usually decimate to around 10% or 0.1.
[1:40] Finally, add thickness to the curve by increasing the depth value and increase its resolution.



---

## Captured Frames

- [0:18] tutorials/frames/blender-secrets---draw-grease-pencil-on-surfaces-without-offset-distance-issue/frame_000.jpg
- [0:45] tutorials/frames/blender-secrets---draw-grease-pencil-on-surfaces-without-offset-distance-issue/frame_001.jpg
- [1:05] tutorials/frames/blender-secrets---draw-grease-pencil-on-surfaces-without-offset-distance-issue/frame_002.jpg
- [1:25] tutorials/frames/blender-secrets---draw-grease-pencil-on-surfaces-without-offset-distance-issue/frame_003.jpg
- [1:45] tutorials/frames/blender-secrets---draw-grease-pencil-on-surfaces-without-offset-distance-issue/frame_004.jpg

---

## Structured Notes

### Core Technique
Draw ornamental surface patterns (e.g. engraved goblet filigree) directly onto a 3D object with Grease Pencil's Surface stroke placement, avoiding the classic zoom-dependent offset drift by working in Orthographic view, then convert the finished drawing into a beveled 3D curve mesh.

### Summary
A short, clean demonstration on a red goblet/chalice model. Frame 000 shows the Stroke Placement dropdown open with "Surface" selected (arrow pointing at it) — the key setting that snaps drawn strokes onto the actual object surface instead of a fixed 3D plane. Frame 001 shows the numpad-5 orthographic toggle in use (green "[5]" key hint) on the same goblet, illustrating the fix for offset drift while zooming. Frame 002 shows the payoff: a dense, fully-drawn ornamental swirl pattern covering the entire goblet surface, drawn directly in Draw Mode. Frame 003 shows the "Convert Grease Pencil" operator's redo panel (Type: Bezier Curve, Bevel Depth, Bevel Resolution, Normalize Weight, Radius Factor) right after conversion — the strokes are now curve geometry sitting just above the surface with a thin bevel already applied. Frame 004 shows the finished, thickened, and presumably decimated curve pattern — a crisp raised-relief ornamental engraving fully wrapped around the goblet, viewed in Edit Mode on the "GP_Layer" curve object with full Bevel (Round profile, Depth, Resolution, Fill Caps) settings visible in the sidebar.

### Key Steps
1. Add a blank Grease Pencil object and switch to Draw Mode.
2. Optionally change the Grease Pencil material's Base Color to something high-contrast so strokes are easier to see against the object.
3. Set Stroke Placement to **Surface** — this is what makes strokes snap directly onto the 3D object rather than floating on a fixed plane.
4. Tune the Offset value: 0 makes strokes overlap/z-fight with the surface; a small value like 0.01 keeps strokes drawn just above it, avoiding clipping.
5. **Avoid offset drift while zooming:** the offset distance is affected by camera zoom in Perspective view. Press Numpad5 to switch to Orthographic view before drawing — in Orthographic, zooming in/out no longer changes the apparent offset distance. Press Numpad5 again to toggle back to Perspective when done.
6. Draw the pattern directly on the surface in Draw Mode.
7. Tab into Edit Mode, right-click → Smooth on drawn strokes to clean up jitter; repeat with Shift+R for a stronger smoothing pass.
8. **Convert to curve geometry:** convert the Grease Pencil object into curves (Object → Convert → Curve equivalent for Grease Pencil) — this produces a new curve object named "GP_Layer". Hide the original Grease Pencil object's visibility in the Outliner once converted.
9. Select the GP_Layer curve, enter Edit Mode, right-click → Decimate Curve to simplify the (often very dense) converted stroke geometry — the author typically decimates to around 10% (0.1).
10. Give the pattern physical thickness by increasing the curve's Bevel Depth, and raise its Resolution for a smoother round cross-section.

### Nodes / Settings
- **Grease Pencil (Draw Mode):** Stroke Placement = Surface, Offset (small value like 0.01), material Base Color for stroke visibility.
- **View:** Numpad5 (toggle Orthographic/Perspective — critical for consistent surface-offset behavior while zooming).
- **Edit Mode operators:** right-click → Smooth (Shift+R to repeat), right-click → Decimate Curve (~10%/0.1 typical), Convert Grease Pencil → Curve (Type: Bezier Curve, Bevel Depth, Bevel Resolution, Normalize Weight, Radius Factor).
- **Curve settings:** Bevel (Round profile, Depth, Resolution, Fill Caps) for final stroke thickness.

### Difficulty
Beginner to Intermediate

### Blender Version
Not specified — core Grease Pencil + Curve workflow, version-agnostic across modern Blender (2.9x-5.x).

### Tags
modelling, procedural, materials, beginner, intermediate

---

## Related Tutorials
- [This Blender Shader is the Secret to Magical 3D Art](this-blender-shader-is-the-secret-to-magical-3d-art.md) — shares materials, procedural, intermediate; also uses a Grease Pencil line-art rig as part of its effect.
