---
title: Abstract Animated Geometric Pattern | Squares | Geometry Nodes Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=7I4k8iaF7D8
author: Artemiy Galutskiy
ingested: 2026-08-17
blender_version: "Blender 5.2.0 -- observed in frame_004"
tags: [geometry-nodes, procedural, abstract, motion-design, animation, intermediate, blender-4x]
extraction_status: complete
frames_dir: tutorials/frames/abstract-animated-geometric-pattern-squares-geometry-nodes-tutorial/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Abstract Animated Geometric Pattern | Squares | Geometry Nodes Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=7I4k8iaF7D8)
**Author:** Artemiy Galutskiy
**Duration:** 6m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.

**Re-transcription verification (2026-08-19):** Audio was re-downloaded fresh and re-transcribed with three different Whisper model sizes to rule out a one-off download/decode failure. None produced coherent narration:
- `small` (original + repeat): `Mantel,` (8 chars)
- `medium`: `Did you recognize our original Layout? Please comment to let us know! Let's go to the first...` then degrades into unintelligible fragments (121 chars total)
- `large`: `Adjustment layer каким? Nicely selected Thank you.` repeated ~12x — the classic Whisper hallucination-on-silence pattern
The `medium` result's opening phrase (a generic "did you recognize our layout, comment below" channel-engagement line) is the only fragment consistent across attempts, suggesting the video has at most a few seconds of spoken intro/outro over otherwise music-only, non-narrated content — not an ingest failure. Transcript was not captured beyond that fragment on any attempt; this extraction is based entirely on the 8 captured Geometry Nodes editor frames.

### Full Content [0:00]
**Transcript (timestamped):**
[0:01] Did you recognize our original Layout? Please comment to let us know! Let's go to the first...



---

## Captured Frames

- [0:20] tutorials/frames/abstract-animated-geometric-pattern-squares-geometry-nodes-tutorial/frame_000.jpg
- [1:10] tutorials/frames/abstract-animated-geometric-pattern-squares-geometry-nodes-tutorial/frame_001.jpg
- [2:00] tutorials/frames/abstract-animated-geometric-pattern-squares-geometry-nodes-tutorial/frame_002.jpg
- [2:50] tutorials/frames/abstract-animated-geometric-pattern-squares-geometry-nodes-tutorial/frame_003.jpg
- [3:40] tutorials/frames/abstract-animated-geometric-pattern-squares-geometry-nodes-tutorial/frame_004.jpg
- [4:30] tutorials/frames/abstract-animated-geometric-pattern-squares-geometry-nodes-tutorial/frame_005.jpg
- [5:20] tutorials/frames/abstract-animated-geometric-pattern-squares-geometry-nodes-tutorial/frame_006.jpg
- [6:00] tutorials/frames/abstract-animated-geometric-pattern-squares-geometry-nodes-tutorial/frame_007.jpg

---

**Transcription note:** Music-only video, no spoken narration (Whisper returned effectively empty output, flagged by the ingest safeguard). This extraction is based entirely on reading the 8 captured Geometry Nodes editor frames.

## Structured Notes

> **Note on transcript:** A full spoken-narration transcript was not captured for this video — confirmed across three independent Whisper re-transcription attempts (small/medium/large models, see the Raw Data section above) on freshly re-downloaded audio. The video is effectively music-only with at most a few seconds of generic intro speech; quality degrades into hallucinated filler on every model size when Whisper is fed the silent/musical remainder. All notes below come from the 8 captured Geometry Nodes editor frames.

### Core Technique
A recursive quad-subdivision ("fractal squares") pattern built with a **Repeat Zone**: starting from a single Grid face, each iteration tests a Noise Texture value against a threshold (Greater Than or Equal) to decide whether that cell subdivides into 4 smaller cells or stays as-is, producing an organic, non-uniform grid of nested squares — then a second noise pass drives a color/selection mask over the result for a stylized reveal look.

### Summary
Starts from a single Grid node (1 face) feeding a Group Input/Output pass-through. A Subdivide Mesh + Separate Geometry (Face domain, Selection/Inverted outputs) pair splits geometry into "keep as-is" vs. "subdivide further" branches, recombined via Join Geometry and cleaned with Merge by Distance. This selection/subdivide/rejoin logic is placed inside a **Repeat Zone** (Blender 4.0+ looping construct, seen as "Repeat Input"/"Repeat Output" nodes with an Iterations field) so the same subdivide-or-keep decision runs multiple times recursively, each pass driven by a Noise Texture sampled per-cell and compared via "Greater Than or Equal" against a threshold — cells where the noise exceeds the threshold get subdivided into 4 smaller squares next pass, others stay large. After several iterations this produces the video's signature dense, non-uniform grid of variously-sized nested squares (visible mid-tutorial as a black-and-tan tiled square pattern). A second pass applies a different Noise Texture through a Color Ramp and another Greater Than or Equal compare to select a scattered subset of cells for an orange highlight/fill color, layered over the white grid-line pattern — visually turning the clean recursive grid into a more painterly, randomly-highlighted composition. A brief World shader (Background node) frame suggests a simple background pass for rendering, not a core part of the pattern logic. The final captured frame shows an animated dark brush-stroke-like shape wiping/revealing across the orange-and-white grid — consistent with the "Animated" part of the title, likely a masked reveal driven by an animated Empty/curve distance or a moving noise/gradient texture, though the exact driver node wasn't legible in the available frame.

### Key Steps
1. Add a Grid node as the base geometry (single face, later subdivided procedurally rather than via the Grid's own resolution fields).
2. Feed the grid through Subdivide Mesh and Separate Geometry (Face domain) to split cells into two streams based on a selection boolean; recombine with Join Geometry and clean overlapping points with Merge by Distance.
3. Wrap that subdivide/select/rejoin logic inside a **Repeat Zone** (Repeat Input → ... → Repeat Output, with an Iterations field) so it runs recursively across multiple passes rather than being manually duplicated node-by-node.
4. Drive the per-pass subdivide decision with a Noise Texture sampled per-cell, compared via a "Greater Than or Equal" node against a threshold value — cells above the threshold subdivide into 4 smaller cells on the next iteration, cells below stay as their current size.
5. After the Repeat Zone, add a second Noise Texture → Color Ramp → Greater Than or Equal chain to select a scattered subset of the final cells and assign them a highlight color (orange, in the demo), layered over the base white grid-line look.
6. Optionally set a simple World Background shader color/strength for render context.
7. For the animated reveal seen in the final frame: layer an animated mask (an Empty-driven distance field, a moving Noise/Gradient Texture, or similar time-varying input) over the pattern's color/visibility to wipe the design in over time — exact node chain not clearly legible in the available frame, but the overall approach (time-varying texture coordinate or distance-to-object feeding a Compare/Color Ramp) is the standard technique for this kind of animated procedural reveal.

### Nodes / Settings
- Grid, Subdivide Mesh, Separate Geometry (Face domain), Join Geometry, Merge by Distance
- Repeat Zone (Repeat Input / Repeat Output, Iterations field) — Blender 4.0+ feature, drives the recursive subdivision
- Noise Texture (2D, with Scale/Detail/Roughness/Lacunarity/Distortion fields visible) → Greater Than or Equal (per-iteration subdivide decision)
- Second pass: Noise Texture → Color Ramp → Greater Than or Equal (final color/selection mask)
- Integer, Add, Compare-family nodes used for auxiliary index/threshold math feeding the Repeat Zone
- World shader: Background node (Color, Strength)

### Difficulty
Intermediate to Advanced (Repeat Zones and recursive noise-driven subdivision are a non-trivial Geometry Nodes pattern; no narration to lean on makes replication harder without pausing on the node graph)

### Blender Version
4.x — the Repeat Zone node is a Blender 4.0+ feature, so this is a hard lower bound; exact point release not stated or clearly legible in the frames.

### Tags
geometry-nodes, procedural, abstract, motion-design, animation, intermediate, blender-4x

---

## Related Tutorials
- [Create Plexus FX In Blender (Geometry Node)](create-plexus-fx-in-blender-geometry-node.md) — conceptual sibling: another silent, music-only abstract Geometry Nodes motion-design tutorial ingested in the same batch, similarly reliant on frame-only extraction.
- [Math X Blender 5.0 - Unlimited Power](math-x-blender-50-unlimited-power.md) — directly relevant Repeat Zone technique: builds an Apollonian Gasket fractal via the same recursive-iteration pattern (Repeat Zone + per-iteration Math/Compare logic) this tutorial uses for its recursive quad-subdivision squares.
