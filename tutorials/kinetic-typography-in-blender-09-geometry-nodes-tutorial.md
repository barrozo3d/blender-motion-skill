---
title: Kinetic Typography in Blender | 09 | Geometry Nodes Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=D3t_ysgEqxQ
author: Artemiy Galutskiy
ingested: 2026-09-04
blender_version: "Blender 5.2"
tags: [geometry-nodes, typography, motion-design, animation, procedural, eevee, blender-5x, advanced]
extraction_status: complete
frames_dir: tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/
frame_count: 17
frame_status: complete
uncertainty_frames: []
frame_selection: evenly-spaced (no narration; no transcript to anchor against -- see Structured Notes)
---

# Kinetic Typography in Blender | 09 | Geometry Nodes Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=D3t_ysgEqxQ)
**Author:** Artemiy Galutskiy
**Duration:** 17m18s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 136 chars (min 500 for 1038s). Captions unavailable or audio silent — extraction will be poor.

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Blender, geometry nodes, UV unwrap, HDRI, compositor, grease pencil, VDB, displacement, bevel, boolean,
[0:14] create difficultyfirmingers.
[17:14] you



---

## Captured Frames

- [0:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_000.jpg
- [1:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_001.jpg
- [2:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_002.jpg
- [3:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_003.jpg
- [4:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_004.jpg
- [5:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_005.jpg
- [6:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_006.jpg
- [7:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_007.jpg
- [8:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_008.jpg
- [9:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_009.jpg
- [10:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_010.jpg
- [11:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_011.jpg
- [12:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_012.jpg
- [13:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_013.jpg
- [14:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_014.jpg
- [15:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_015.jpg
- [16:40] tutorials/frames/kinetic-typography-in-blender-09-geometry-nodes-tutorial/frame_016.jpg

---

## Structured Notes

### Core Technique
Kinetic typography built entirely in Geometry Nodes: `String` → `String to Curves` produces per-word/per-letter instances, which are sliced against a `Grid` and driven through a `Repeat` zone with `Sample Index` and `Set Instance Transform`, animated from a single exposed modifier `Value` and an `Empty` read via `Object Info`.

### Summary
> **This tutorial has no narration.** The video is a silent screencast set to music, and
> the ingest's transcript floor flagged it CRITICAL — 136 characters recovered against a
> 500-character minimum for its 1038-second runtime, with Whisper emitting only
> fabricated fragments. **Everything below is read from captured frames alone; there are
> no `[transcript]` citations in this entry because there is nothing reliable to cite.**
> Frame selection is evenly spaced rather than content-anchored, for the same reason.

The build recreates the Studio Dumbar kinetic-typography look — the on-screen result reads
`DUMBAR STYLE` `[frame_009]`. Text is generated procedurally from a `String` node rather
than a Text object, converted to curve instances, then sliced into horizontal bands by a
low-resolution `Grid` so each letter can be striped and offset independently. A `Repeat`
zone with `Sample Index` on the Instance domain drives per-band transforms, an `Empty` fed
through `Object Info` acts as the animation controller, and a `Bake` node freezes the
result for playback. Colour comes from `Color Ramp` nodes into the material, and the whole
animation is driven from one `Value` socket exposed on the Geometry Nodes modifier.

### Key Steps
> Sequence below is inferred from the visible state of the node graph across evenly-spaced
> frames. Individual parameter values are recorded only where a frame shows them; no
> ordering claim is made for work that happened between samples.

1. **Generate the text procedurally.** A `String` node feeds `String to Curves` (outputs `Curve Instances`, `Line`, `Word`, `Pivot Point`; `Size 1 m`, font `Bfont Regular`, with Alignment / Spacing / Text Box sub-panels) `[frame_000]`. Using a String node rather than a Text object is what makes the rest of the setup driveable.
2. **Build a slicing grid.** A `Grid` at `Size X 12.3 m` × `Size Y 1 m` with `Vertices X 3`, `Vertices Y 3`, combined with `Transform Geometry`, `Separate XYZ`, an `Integer` of `80`, and `Subtract` / `Multiply` vector math `[frame_002]`. The low vertex count plus large X size is what produces the wide horizontal bands visible in the final letters.
3. **Instance and stripe the letters.** By mid-build the graph has grown substantially and the viewport shows letterforms composed of horizontal strips `[frame_006]` `[frame_009]`, with the scene reporting 82 objects and ~33,126 vertices `[frame_009][frame_011]`.
4. **Drive per-instance transforms.** `Sample Index` set to the `Instance` domain (`Vector` output, `Clamp` available, with `Geometry` / `Value` / `Index` inputs) feeds a `Set Instance Transform` `[frame_011][frame_009]`.
5. **Use an Empty as the controller.** `Object Info` (`Original`/`Relative` toggle, `As Instance`) reads an object named `Empty`, supplying `Transform` / `Location` / `Rotation` / `Scale` into the transform chain `[frame_009]`. The Empty is a separate scene object animated on the timeline `[frame_015]`.
6. **Wrap the per-band work in a `Repeat` zone.** A `Repeat` input/output pair carries `Geometry` and `Instances` through the striping logic `[frame_009]`.
7. **Bake the result.** A `Bake` node labelled `Baked Frame 1` with `Animation` / `Bake` controls sits in the chain, freezing the instance evaluation for playback `[frame_009]`.
8. **Colour via Color Ramps.** Two `Color Ramp` nodes drive the material — one in `RGB`/`Linear` with an orange-to-green stop at `Pos 0.604`, another white at `Pos 1.000` — fed by a `Subtract` node at `Value 1.000`, outputting to `Color` and `Alpha` `[frame_016]`.
9. **Expose one animation control.** The Geometry Nodes modifier surfaces a single `Value` socket (`0.000` at the sampled frame), which is what the animation is keyed on `[frame_016]`.
10. **Play back at 25 fps.** The final animation runs on a 250-frame timeline; at frame 175 the letters have dissolved into vertical strips of green and orange `[frame_016]`.

### Nodes / Settings
- **`String`** → **`String to Curves`** — outputs `Curve Instances`, `Line`, `Word`, `Pivot Point`; `Size 1 m`, font `Bfont Regular` `[frame_000]`
- **`Grid`** — `Size X 12.3 m`, `Size Y 1 m`, `Vertices X 3`, `Vertices Y 3` `[frame_002]`
- **`Integer`** — `80` `[frame_002]`
- **`Transform Geometry`**, **`Separate XYZ`**, **`Subtract`**, **`Multiply`** (Vector Math) `[frame_002]`
- **`Sample Index`** — domain `Instance`, `Vector` output, inputs `Geometry` / `Value` / `Index` `[frame_011]`
- **`Set Instance Transform`** — `Instances`, `Selection`, `Transform` `[frame_009]`
- **`Object Info`** — reading `Empty`, `Original`/`Relative`, `As Instance` `[frame_009]`
- **`Repeat` zone** — carrying `Geometry` and `Instances` `[frame_009]`
- **`Bake`** — labelled `Baked Frame 1`, with `Animation` and `Bake` controls `[frame_009]`
- **`Color Ramp`** ×2 — `RGB`/`Linear`, orange-green stop at `Pos 0.604`; white at `Pos 1.000`; driven by `Subtract` `Value 1.000` into material `Color` / `Alpha` `[frame_016]`
- **Modifier interface** — one exposed `Value` socket (`0.000`) driving the animation `[frame_016]`
- **Render** — EEVEE; Viewport `Samples 16` with `Temporal Reprojection` on; Render `Samples 64` with `Shadows` on; Display `sRGB` `[frame_000][frame_002][frame_009]`
- **Scene scale** — 82 objects, ~33,126 verts / 18,512 faces / 31,946 tris at completion `[frame_009][frame_011]`

> **Coverage limits, stated plainly.** With no narration and 17 evenly-spaced samples of a
> 17-minute build, this entry captures the node vocabulary and the shape of the technique
> but **not** the intermediate wiring between samples. Anyone rebuilding this should treat
> the Key Steps as a map, not a recipe, and expect to work out the connections themselves.
> The video is worth re-ingesting if a caption track ever appears.

### Difficulty
Advanced

### Blender Version
Blender 5.2.0 — read from the status bar in `[frame_000]`, `[frame_002]` and `[frame_009]`. No narration, so no spoken version claim exists to compare against.

### Tags
geometry-nodes, typography, motion-design, animation, procedural, eevee, blender-5x, advanced

---

## Related Tutorials
- [Create Text in Geometry Nodes! (Blender Tutorial)](create-text-in-geometry-nodes-blender-tutorial.md) — the same `String` → `String to Curves` foundation this build starts from, with narration; the better first stop if this entry's frames-only steps are too sparse to follow
- [[tut-what-makes-splinecurves-more-complicated---p16-geometry-nodes-beginners-50]] — `String to Curves` emits curve *instances*, and this episode explains the instance-vs-realized rule and curve types that govern what can be done with them downstream
- [Can Blender Still Compete (Motion Graphics)](can-blender-still-compete-motion-graphics.md) — another instance-heavy motion-design build in the same Blender 5.2 generation; shares geometry-nodes, motion-design, blender-5x
