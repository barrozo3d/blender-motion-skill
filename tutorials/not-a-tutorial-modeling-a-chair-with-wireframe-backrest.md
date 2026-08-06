---
title: Not a tutorial: Modeling a chair with wireframe backrest
source: YouTube
url: https://www.youtube.com/watch?v=IgZqPjHr0eI
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — silent screen recording, no version indicator visible"
tags: [modelling, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/not-a-tutorial-modeling-a-chair-with-wireframe-backrest/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Not a tutorial: Modeling a chair with wireframe backrest

**Source:** [YouTube](https://www.youtube.com/watch?v=IgZqPjHr0eI)
**Author:** Blender Secrets
**Duration:** 8m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 3 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (3 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[8:00] HAN



---

## Captured Frames

- [0:20] tutorials/frames/not-a-tutorial-modeling-a-chair-with-wireframe-backrest/frame_000.jpg
- [1:20] tutorials/frames/not-a-tutorial-modeling-a-chair-with-wireframe-backrest/frame_001.jpg
- [2:30] tutorials/frames/not-a-tutorial-modeling-a-chair-with-wireframe-backrest/frame_002.jpg
- [3:40] tutorials/frames/not-a-tutorial-modeling-a-chair-with-wireframe-backrest/frame_003.jpg
- [4:50] tutorials/frames/not-a-tutorial-modeling-a-chair-with-wireframe-backrest/frame_004.jpg
- [6:00] tutorials/frames/not-a-tutorial-modeling-a-chair-with-wireframe-backrest/frame_005.jpg
- [7:10] tutorials/frames/not-a-tutorial-modeling-a-chair-with-wireframe-backrest/frame_006.jpg
- [8:10] tutorials/frames/not-a-tutorial-modeling-a-chair-with-wireframe-backrest/frame_007.jpg

---

## Structured Notes

### Core Technique
**Not a narrated tutorial** — as its own title states, this is a silent ~8m22s speed-modeling/timelapse screen recording (no voiceover, no captions, no chapter markers — the transcript was not captured because the video has no spoken audio to transcribe) showing the full process of modeling a simple chair: bent-tube metal legs, a rounded seat, and a smooth, dome-shaped backrest whose surface is checked/refined via a dense quad topology grid (the "wireframe backrest" of the title) before final subdivision smoothing. Extracted faithfully from the visible frame progression since there is no narration to transcribe.

### Summary
Frame 000 shows Blender's User Preferences Theme tab open over an empty scene — the very start of the recording, likely incidental UI setup rather than modeling content. Frame 001 shows two bent, curved tube shapes (chair-leg profiles) freshly modeled, not yet joined to a seat. Frame 002 shows the legs joined into a four-legged base with a boxy rectangular seat blank on top, a Loop Cut (Ctrl+R) operation in progress. Frame 003 shows an early version of the chair with a rounded seat disc and a tall, smooth dome-shaped backrest already taking shape. Frame 004 shows the same chair with an Add Modifier search menu open (Cast, Cloth, Collision, Dynamic Paint, Explode, Fluid, Hook, etc. visible under Simulate/Generate categories) — a modifier being added to the backrest/seat mesh. Frame 005 shows a close, dense **quad wireframe grid** covering the backrest surface — this is the literal "wireframe backrest" referenced in the title, likely a Wireframe modifier or dense retopology pass used to check/refine the surface's edge flow before final smoothing. Frame 006 shows the backrest again in a smoothed, subdivided wireframe-overlay view, now clearly dome/oval shaped and well-flowing. Frame 007 shows the final rendered chair: a rounded backrest, circular seat, and four slightly-angled bent-tube metal legs, viewed in a clean studio-lit shading mode.

### Key Steps
Reconstructed from the visible frame progression only (no audio to confirm exact operator sequence):
1. Model the four **chair legs** as bent tube/pipe shapes (likely via a curve-to-mesh or Skin-modifier-style workflow, similar in spirit to other BlenderSecrets tube-modeling tips).
2. Build a rectangular seat blank and use **Loop Cut (Ctrl+R)** to add supporting geometry for later shaping.
3. Shape the seat into a rounded disc and build a tall, dome-like **backrest** shape above it.
4. Apply modifiers (visible: an Add Modifier search including Cast/Cloth/Explode/etc. — exact modifier used is unclear from the frame alone) to refine the backrest's surface deformation.
5. Check/refine the backrest's underlying **quad topology** via a dense wireframe grid overlay — ensuring clean, evenly-flowing edge loops before final smoothing (the source of the video's "wireframe backrest" title).
6. Apply final smooth shading/subdivision to produce the finished, polished chair render.

### Nodes / Settings
- Not confidently identifiable without audio — visible tools include **Ctrl+R** (Loop Cut) and an **Add Modifier** search panel (category unclear from the frame). The backrest's dense quad grid is the video's namesake "wireframe" stage.

### Difficulty
Intermediate

### Blender Version
Not specified — silent screen recording, no version indicator visible. The title bar references a "Mendake project Nen Dome Deco april 2019" .blend file, suggesting a personal/client project timelapse rather than a version-specific feature demo.

### Tags
modelling, procedural, intermediate

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover this silent chair-modeling timelapse's specific technique.
