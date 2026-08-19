---
title: Create Plexus FX In Blender ( Geometry Node )
source: YouTube
url: https://www.youtube.com/watch?v=ZUiCC5iTUWs
author: Manbo Studio
ingested: 2026-08-17
blender_version: "4.x (Geometry Nodes UI matches 4.x-era layout; exact point release not stated or clearly legible)"
tags: [geometry-nodes, procedural, abstract, motion-design, compositing, animation, intermediate, blender-4x]
extraction_status: complete
frames_dir: tutorials/frames/create-plexus-fx-in-blender-geometry-node/
frame_count: 10
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Create Plexus FX In Blender ( Geometry Node )

**Source:** [YouTube](https://www.youtube.com/watch?v=ZUiCC5iTUWs)
**Author:** Manbo Studio
**Duration:** 9m55s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.

**Re-transcription verification (2026-08-19):** Audio was re-downloaded fresh and re-transcribed with three different Whisper model sizes to rule out a one-off download/decode failure. None produced coherent narration:
- `small` (original + repeat): `Build rendering` (16 chars)
- `medium`: `aja Die losses conversation Ignition Distance Montage Shading` (61 chars) — random unrelated words, not a sentence
- `large`: `Provide separate L religio web Terima kasih telah menonton!` (Indonesian for "Thank you for watching!") repeated ~20x — a textbook Whisper hallucination-on-silence loop, same failure pattern as the sibling "Abstract Animated Geometric Pattern" ingest
Larger models hallucinate progressively longer but still non-substantive filler as the audio has essentially nothing to decode — confirms this is a music-only, non-narrated video rather than an ingest/download failure. Transcript was not captured on any of the three attempts; this extraction is based entirely on the 10 captured Geometry Nodes / Shading / Compositor frames.

### Full Content [0:00]
**Transcript (timestamped):**
[0:00] (no usable speech decoded — see re-transcription verification note above)



---

## Captured Frames

- [0:30] tutorials/frames/create-plexus-fx-in-blender-geometry-node/frame_000.jpg
- [1:30] tutorials/frames/create-plexus-fx-in-blender-geometry-node/frame_001.jpg
- [2:30] tutorials/frames/create-plexus-fx-in-blender-geometry-node/frame_002.jpg
- [3:30] tutorials/frames/create-plexus-fx-in-blender-geometry-node/frame_003.jpg
- [4:30] tutorials/frames/create-plexus-fx-in-blender-geometry-node/frame_004.jpg
- [5:30] tutorials/frames/create-plexus-fx-in-blender-geometry-node/frame_005.jpg
- [6:30] tutorials/frames/create-plexus-fx-in-blender-geometry-node/frame_006.jpg
- [7:30] tutorials/frames/create-plexus-fx-in-blender-geometry-node/frame_007.jpg
- [8:30] tutorials/frames/create-plexus-fx-in-blender-geometry-node/frame_008.jpg
- [9:20] tutorials/frames/create-plexus-fx-in-blender-geometry-node/frame_009.jpg

---

**Transcription note:** Music-only video, no spoken narration (Whisper returned effectively empty output, flagged by the ingest safeguard). This extraction is based entirely on reading the 10 captured Geometry Nodes / Shading / Compositor frames, and some node-level detail (exact node names in later frames) could not be fully confirmed without narration — treat step-level specifics as a plausible reconstruction, not a verbatim transcript.

## Structured Notes

> **Note on transcript:** A spoken-narration transcript was not captured for this video — confirmed across three independent Whisper re-transcription attempts (small/medium/large models, see the Raw Data section above) on freshly re-downloaded audio, each producing only noise words or a hallucinated repeating-phrase loop. The video is effectively music-only with no usable narration; quality degrades into hallucinated filler on every model size. All notes below come from the 10 captured Geometry Nodes / Shading / Compositor frames.

### Core Technique
An animated "Plexus"-style glowing line network — the classic look of scattered points connected by thin triangulated edges — built by displacing a subdivided Grid into low-poly faceted terrain (flat-shaded, noise-driven, animated via Scene Time), then isolating that terrain's edge wireframe and rendering it with an Emission shader plus compositor Glare/Bloom for the neon look.

### Summary
Starts from a Grid primitive (searchable via Shift+A → Mesh Primitives → Grid), combined early on with Delete Geometry and an Ico Sphere/Instance on Points/Join Geometry branch — consistent with either scattering small instance geometry across the grid or preparing a secondary point set. A Math + Scene Time + Map Range chain (seen in the node-search overlay) drives a Noise Texture-based Set Position displacement that pushes the grid's vertices up and down over time, and with Shade Flat / Face-normal shading applied, this reads as a low-poly, faceted "mountain range" of triangulated peaks (frame_002-003) that continuously reshapes as the Scene Time input advances — this is the animation driver for the whole effect. The mesh is then converted toward a curve/line representation (Mesh to Curve or an equivalent edge-extraction step, referenced in the node-search overlay) so that only the triangulated edge network remains, rather than solid faces — visible in later frames as a fine wireframe of connected points forming triangles in 3D space, matching the classic "plexus" aesthetic. A Principled BSDF-based material is set up with high Emission Strength and a green/cyan Emission Color to make the line network glow. Finally, in the Compositor (visible switching from Geometry Nodes to Compositing Nodes tab), a node chain including what looks like a Glare-type node is added after the render layer to bloom/blur the glowing lines into the soft neon look seen in the final frames, viewed via a render preview (Space Bar / Render Region shortcuts shown on-screen).

### Key Steps
1. Add a Grid mesh (Shift+A → Mesh → Grid) as the base geometry inside a Geometry Nodes modifier.
2. Set up an animated displacement: combine a Noise Texture with the Scene Time input (and Map Range/Math nodes to remap values) feeding into a Set Position node, so the grid's vertex heights shift continuously as the timeline advances.
3. Apply flat/faceted shading (Shade Flat or equivalent) so the displaced grid reads as a low-poly, angular "mountain range" of distinct triangular faces rather than a smooth surface.
4. Convert the faceted mesh toward a line/curve representation that keeps only its edges (Mesh to Curve or an equivalent edge-extraction approach) so the result is a network of connected line segments rather than solid faces — this becomes the "plexus" wireframe.
5. In the Shading workspace, build a material with a bright Emission (high Strength, green/cyan-tinted color) on the resulting line/point geometry so it reads as glowing.
6. Switch to the Compositor and add a Glare-type (bloom) node after the Render Layers node to spread bright emissive areas into the soft glowing halo characteristic of a plexus/neon look, then preview via render (Space Bar / render region).
7. Because the underlying displacement is time-driven (Scene Time in the noise chain), scrubbing/playing the timeline animates the whole plexus network organically over time without keyframes.

### Nodes / Settings
- Mesh Primitives → Grid; Delete Geometry; Ico Sphere; Instance on Points; Join Geometry (seen in the node-search overlay, likely part of an alternate/secondary point-scatter branch)
- Set Position driven by a Noise Texture, combined with Scene Time (Input category) and Map Range / Math nodes for remapping the animated displacement
- Curve-related conversion: Mesh to Curve (Mesh → Curve category) and/or Curve to Mesh, used to extract the edge-network line geometry from the faceted mesh
- Shading workspace: Principled BSDF material with strong Emission (Color: green/cyan, high Strength)
- Compositor: Render Layers → a Glare/bloom-type node → Composite/Viewer, used to achieve the soft neon glow over the emissive line network

### Difficulty
Advanced (combines animated noise-driven displacement, a mesh-to-line conversion step, emission shading, and compositor bloom — several disciplines stacked together, with no narration available to confirm exact settings)

### Blender Version
4.x — Geometry Nodes editor layout and node categories shown match the 4.x era; exact point release not stated or clearly legible in the captured frames.

### Tags
geometry-nodes, procedural, abstract, motion-design, compositing, animation, intermediate, blender-4x

---

## Related Tutorials
- [Abstract Animated Geometric Pattern | Squares | Geometry Nodes Tutorial](abstract-animated-geometric-pattern-squares-geometry-nodes-tutorial.md) — conceptual sibling: another silent, music-only abstract Geometry Nodes motion-design tutorial ingested in the same batch, similarly reliant on frame-only extraction.
- [Blender Tutorial: Connect The Dots with Geometry Nodes, The "Plexus" Effect](blender-tutorial-connect-the-dots-with-geometry-nodes-the-pl.md) — directly relevant: Entagma's take on the same "Plexus" effect, using Distribute Points in Volume + a serialized pairwise-distance loop instead of this tutorial's displaced-terrain-to-line-network approach. Good alternate technique for the same visual result.
