---
title: Daily Blender Tip 135 - Tissue Add-on: Experiment 1
source: YouTube
url: https://www.youtube.com/watch?v=aoZD_EwpWmo
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — earlier-era Tissue add-on workflow (Dual Mesh, Wireframe modifier), predates the 4.3.2-confirmed version-groups-and-tissue video"
tags: [organic, procedural, displacement, abstract, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-135---tissue-add-on-experiment-1/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 135 - Tissue Add-on: Experiment 1

**Source:** [YouTube](https://www.youtube.com/watch?v=aoZD_EwpWmo)
**Author:** Blender Secrets
**Duration:** 1m56s | 14 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'TISSUE ADD-ON EXPERIMENT 1'
- **CRITICAL:** Empty transcript in chapter 'Subdivide a UV sphere, apply the modifier'
- **CRITICAL:** Empty transcript in chapter 'Add a displacement modifier'
- **CRITICAL:** Empty transcript in chapter 'Choose an interesting procedural texture.'
- **CRITICAL:** Empty transcript in chapter 'Tweak the size setting until you get something you like'
- **CRITICAL:** Empty transcript in chapter 'Experimenting with different settings for the texture...'
- **CRITICAL:** Empty transcript in chapter 'Subdivide it some more, apply the modifiers.'
- **CRITICAL:** Empty transcript in chapter 'Add a decimate modifier'
- **CRITICAL:** Empty transcript in chapter 'Tweak the settings to get new, interesting geometry.'
- **CRITICAL:** Empty transcript in chapter 'Turn on the Tissue add-on in Preferences.'
- **CRITICAL:** Empty transcript in chapter 'Add a Wireframe modifier and tweak the settings.'
- **CRITICAL:** Empty transcript in chapter 'Add more subdivisions.'
- **CRITICAL:** Total transcript only 36 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (32 chars) in 'Click on Dual Mesh in the Tissuel tool panel settings.'
- WARNING: Very short transcript (4 chars) in 'Interesting geometry! More tomorrow :-'

---


Frames captured — see "Captured Frames" section below.


### TISSUE ADD-ON EXPERIMENT 1 [0:00]

### Subdivide a UV sphere, apply the modifier [0:06]

### Add a displacement modifier [0:14]

### Choose an interesting procedural texture. [0:19]

### Tweak the size setting until you get something you like [0:25]

### Experimenting with different settings for the texture... [0:36]

### Subdivide it some more, apply the modifiers. [0:56]

### Add a decimate modifier [1:02]

### Tweak the settings to get new, interesting geometry. [1:11]

### Turn on the Tissue add-on in Preferences. [1:25]

### Click on Dual Mesh in the Tissuel tool panel settings. [1:30]
**Transcript (timestamped):**
[1:30] feature
[1:34] Anyways, get job content


### Add a Wireframe modifier and tweak the settings. [1:36]

### Add more subdivisions. [1:41]

### Interesting geometry! More tomorrow :- [1:47]
**Transcript (timestamped):**
[1:57] Cut,



---

## Captured Frames

- [0:06] tutorials/frames/daily-blender-tip-135---tissue-add-on-experiment-1/frame_000.jpg
- [0:14] tutorials/frames/daily-blender-tip-135---tissue-add-on-experiment-1/frame_001.jpg
- [0:25] tutorials/frames/daily-blender-tip-135---tissue-add-on-experiment-1/frame_002.jpg
- [0:45] tutorials/frames/daily-blender-tip-135---tissue-add-on-experiment-1/frame_003.jpg
- [1:02] tutorials/frames/daily-blender-tip-135---tissue-add-on-experiment-1/frame_004.jpg
- [1:11] tutorials/frames/daily-blender-tip-135---tissue-add-on-experiment-1/frame_005.jpg
- [1:30] tutorials/frames/daily-blender-tip-135---tissue-add-on-experiment-1/frame_006.jpg
- [1:41] tutorials/frames/daily-blender-tip-135---tissue-add-on-experiment-1/frame_007.jpg

---

## Structured Notes

### Core Technique
An early exploratory "happy accidents" pass with procedural displacement and the Tissue add-on: a subdivided sphere is displaced with a procedural texture (baked in via repeated apply-and-resubdivide passes) to build organic rock-like bumps, simplified back down with a Decimate modifier for interesting low-poly facets, then fed through Tissue's **Dual Mesh** conversion and a Wireframe modifier to produce an entirely different tangled, cage-like structure from the same base shape. First of a multi-part "Tissue Add-on Experiment" series (see "More tomorrow" sign-off), continued in Experiments 2 and 3. Note: this video's audio track is silent/near-empty; this summary is built entirely from the captured on-screen text captions and frames.

### Summary
Frame 000 shows the base setup: a smooth, evenly-subdivided UV sphere with the Tissue Tools panel open in the sidebar (Dual Mesh button, Weight Base: Vertex Color/White/Curvature/Harmonic, Vertex Color Run) and a Subdivision Surface modifier below it, captioned "Subdivide a UV sphere, apply the modifier." Frame 001 shows a Displace modifier freshly added in the modifier search list (Cloth, Collision, Dynamic Paint, Explode, Fluid Simulation, Ocean, Particle Instance, Particle System, Smoke, Soft Body options visible), captioned "Add a displacement modifier." Frame 002 shows a Marble-type procedural Texture applied through the Displace modifier (Texture preview swatch, Type: Marble, Noise Basis, Size, Turbulence, Depth, Hard/Soft toggle) — the sphere now covered in sharp angular ridges, captioned "Tweak the size setting until you get something you like." Frame 003 shows a different procedural texture swapped in — a Magic-type texture (colorful pink/yellow/green preview swatch) — producing softer, more rounded organic bumps across the sphere's surface. Frame 004 shows the shape after applying the modifiers and adding a Decimate modifier: a smoothly bumpy, blob-like rock form, captioned "Add a decimate modifier." Frame 005 shows the Decimate modifier's settings (Collapse mode, Ratio slider, Symmetry, Triangulate) reducing the bumpy shape into a faceted, low-poly rock form, captioned "Tweak the settings to get new, interesting geometry." Frame 006 shows the Tissue Tools panel's **Dual Mesh** operator just run on the faceted rock shape, transforming it into a completely different honeycomb-like polygonal structure, captioned "Click on Dual Mesh in the Tissue tool panel settings." Frame 007 shows the final result after adding a Wireframe modifier (Offset, Relative Offset, Boundary, Crease Edges, Material Offset visible in the sidebar) and more subdivisions: a dense, tangled, cage-like wire-sculpture structure, captioned "Add more subdivisions."

### Key Steps
1. Start with a UV Sphere, subdivide it (Subdivision Surface modifier) and apply it for a dense, evenly-distributed base mesh.
2. Add a **Displace** modifier and assign it a procedural Texture (Marble tried first, producing sharp angular ridges; Magic tried as an alternative, producing softer rounded bumps) — tweak the texture's Size setting until the displaced bump pattern looks interesting.
3. Experiment with different texture types/settings, subdivide further and apply the modifiers again to bake the displacement into real geometry at higher resolution.
4. Add a **Decimate** modifier (Collapse mode, adjustable Ratio) to simplify the dense bumpy geometry back down — tweaking the ratio produces different faceted low-poly "rock" results, treated as a source of new interesting geometry rather than just optimization.
5. Enable the **Tissue** add-on in Preferences if not already active.
6. In the Tissue Tools panel, click **Dual Mesh** — this converts the faceted rock shape's topology into its dual (roughly: faces become vertices and vice versa), producing a completely different honeycomb/polygonal look from the same starting shape.
7. Add a **Wireframe** modifier and tweak its settings (Offset/Thickness, Boundary, Crease Edges, Material Offset) to turn the dual-mesh result into a tangled, cage-like wire-sculpture structure.
8. Add more subdivisions for a denser, more intricate final look. Sign-off: "Interesting geometry! More tomorrow" — this experiment continues directly into Parts 2 and 3.

### Nodes / Settings
- **Modifiers:** Subdivision Surface, Displace (Texture: Marble/Magic procedural types, Size, Noise Basis, Turbulence, Depth, Hard/Soft), Decimate (Collapse mode, Ratio, Symmetry, Triangulate), Wireframe (Offset, Relative Offset, Boundary, Crease Edges, Material Offset).
- **Tissue add-on (Preferences > Add-ons):** Tissue Tools panel — Dual Mesh operator, Weight Base options (Vertex Color, White, Curvature, Harmonic), Vertex Color Run, Toggle Edit Mode.
- **Workflow pattern:** repeated subdivide → apply modifiers cycles to progressively bake displacement/decimation into real geometry at each stage.

### Difficulty
Intermediate

### Blender Version
Not specified — an earlier-era Tissue add-on workflow (Dual Mesh, Wireframe modifier), predating the channel's later "Vertex Groups, Modifiers and Tissue Add-on" video confirmed on Blender 4.3.2.

### Tags
organic, procedural, displacement, abstract, intermediate

---

## Related Tutorials
- [Vertex Groups, Modifiers and Tissue Add-on - Blender Secrets](vertex-groups-modifiers-and-tissue-add-on---blender-secrets.md) — shares organic, procedural, intermediate; the channel's later, more refined revisit of the Tissue add-on's "Convert to Dual Mesh" operator (the same Tissue Tools > Dual Mesh step used here), adding vertex-group-driven control on top.
