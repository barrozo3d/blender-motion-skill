---
title: Blender Secrets - Auto Masking Cavities in Sculpt Mode
source: YouTube
url: https://www.youtube.com/watch?v=RbqpANWvTWY
author: Blender Secrets
ingested: 2026-08-04
blender_version: "3.4+ (Auto Masking Cavity feature is explicitly new in 3.4)"
tags: [organic, procedural, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---auto-masking-cavities-in-sculpt-mode/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - Auto Masking Cavities in Sculpt Mode

**Source:** [YouTube](https://www.youtube.com/watch?v=RbqpANWvTWY)
**Author:** Blender Secrets
**Duration:** 1m48s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- WARNING: Thin transcript: 902 chars. Notes may be shallow — consider --whisper-model small.

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] When using Blender 3.4 or later, you have access to the Auto Masking feature in Scope
[0:12] mode.
[0:13] Find it in the drop-down menu in Scope mode or via the shortcut ALT-A for its Pi menu.
[0:19] You can overwrite this general setting for each brush under the Advanced Auto Masking
[0:23] options.
[0:30] Enabling cavity allows you to easily paint darker tones in skin creases or pores, for
[0:35] example.
[0:41] You can invert the effect by checking cavity inverted.
[0:52] Factor controls how strong the Auto Masking is and blur how sharp or blurry the mask is.
[0:59] It's also useful when you only want to scope in certain areas.
[1:02] With the cavity option checked, a Create Mask option is available.
[1:07] This creates a mask based on cavities.
[1:09] You can further edit this mask with the Normal Mask tool.
[1:17] Use the Smooth or Sharpen Mask options repeatedly to further adjust the mask as needed.
[1:23] One interesting use case of this is to bring out more details in 3D scans.



---

## Captured Frames

- [0:15] tutorials/frames/blender-secrets---auto-masking-cavities-in-sculpt-mode/frame_000.jpg
- [0:35] tutorials/frames/blender-secrets---auto-masking-cavities-in-sculpt-mode/frame_001.jpg
- [0:55] tutorials/frames/blender-secrets---auto-masking-cavities-in-sculpt-mode/frame_002.jpg
- [1:07] tutorials/frames/blender-secrets---auto-masking-cavities-in-sculpt-mode/frame_003.jpg
- [1:23] tutorials/frames/blender-secrets---auto-masking-cavities-in-sculpt-mode/frame_004.jpg

---

## Structured Notes

### Core Technique
Blender 3.4+'s Sculpt Mode Cavity Auto Masking: automatically constrains sculpt-brush strokes (or a generated mask) to only affect surface recesses/creases, letting you paint texture, color, or detail selectively into cavities without manually masking them.

### Summary
A short but content-dense tip using a detailed T-Rex sculpt as the example. Frame 000 shows the Auto Masking dropdown menu (also reachable via Alt+A pie menu) with the Auto-Masking flyout open, showing options: Topology, Face Sets, Mesh Boundary, Face Sets Boundary, Cavity, Cavity (Inverted), View Normal, Area Normal. Frame 001 shows the Advanced Auto Masking panel in the tool/brush settings sidebar with Cavity checked and a "Create Mask" button appearing next to it, plus Factor and Blur sliders below — this is the per-brush override of the general setting. Frame 002 is a 3-panel comparison showing the direct visual effect of the Factor slider on Cavity (Inverted) masking at 1.0, 0.5, and 0.1 — higher factor = stronger, more contrast-heavy cavity restriction; lower factor = softer, more of the surface allowed through. Frame 003 shows the resulting "Mask From Cavity" operator panel (Mode: Mix, Mix Factor 1.000, Settings: Scene) after clicking Create Mask — the T-Rex's skin cavities are now masked, visible as the sculpt brush (Inflate filter shown active) only affecting the recessed scale creases. Frame 004 shows refining that generated mask further with the Mesh Filter tool set to Sharpen Mask (Strength 1.000, Iterations 6) — sharpening the cavity mask's edges for a crisper result.

### Key Steps
1. Requires Blender 3.4 or later. Open Sculpt Mode's Auto Masking dropdown (or press Alt+A for the pie menu) and enable Cavity for a global auto-masking setting.
2. Override this per-brush under the brush's Advanced → Auto Masking options if a specific brush needs different cavity behavior than the general setting.
3. With Cavity enabled, brush strokes are automatically constrained to surface recesses/creases — useful for painting darker tones into skin creases, pores, panel-line grime, or similar detail work without hand-masking.
4. Check Cavity (Inverted) to flip the effect — constrain strokes to raised/convex areas instead of recesses.
5. Tune Factor (overall strength of the cavity restriction — higher = more contrast/stronger limiting) and Blur (how sharp vs. soft the mask edge reads) to taste.
6. With Cavity checked, a "Create Mask" button becomes available — click it to bake a standalone Mask (Mask From Cavity operator: Mode Mix, Mix Factor) based on the current cavity settings, rather than just constraining live brush strokes.
7. Further refine that generated mask using the Mask tool's Mesh Filter options — Smooth Mask and Sharpen Mask, applied repeatedly (Iterations), to soften or crispen the cavity mask boundary as needed.
8. A noted practical use case: bringing out extra surface detail on 3D scans by cavity-masking and selectively re-sculpting/re-texturing the recessed areas.

### Nodes / Settings
- **Sculpt Mode Auto Masking:** Topology, Face Sets, Mesh Boundary, Face Sets Boundary, Cavity, Cavity (Inverted), View Normal, Area Normal (dropdown or Alt+A pie menu).
- **Advanced Auto Masking (per-brush):** Cavity, Cavity (Inverted), Factor, Blur, Custom Curve, plus a "Create Mask" button when Cavity is enabled.
- **Mask From Cavity operator:** Mode (Mix), Mix Factor, Settings (Scene).
- **Mask refinement:** Mesh Filter → Smooth Mask / Sharpen Mask (Strength, Iterations, Auto Iteration Count).

### Difficulty
Beginner to Intermediate

### Blender Version
Blender 3.4+ (Auto Masking Cavity feature explicitly stated as new in 3.4)

### Tags
organic, procedural, beginner, intermediate

---

## Related Tutorials
- [3D Sculpting on the go with XPPen Magic Drawing Tablet (Nomad Sculpt)](3d-sculpting-on-the-go-with-xppen-magic-drawing-tablet-and-visiting-ghibli-museu.md) — shares organic, beginner; same channel, complementary sculpt-workflow subject.
- [4 new retopology tips to discover! - Blender Secrets](4-new-retopology-tips-to-discover---blender-secrets.md) — shares organic, beginner, intermediate; same channel.
