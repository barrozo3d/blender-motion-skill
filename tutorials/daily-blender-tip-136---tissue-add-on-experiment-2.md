---
title: Daily Blender Tip 136 - Tissue Add-on: Experiment 2
source: YouTube
url: https://www.youtube.com/watch?v=HabMke3KDFc
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — earlier-era Tissue add-on workflow, direct continuation of Experiment 1"
tags: [organic, procedural, displacement, abstract, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-136---tissue-add-on-experiment-2/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 136 - Tissue Add-on: Experiment 2

**Source:** [YouTube](https://www.youtube.com/watch?v=HabMke3KDFc)
**Author:** Blender Secrets
**Duration:** 1m54s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'TISSUE ADD-ON EXPERIMENT 2'
- **CRITICAL:** Empty transcript in chapter 'Paint a Weight Map on the sphere...'
- **CRITICAL:** Empty transcript in chapter 'Add a displacement modifier and a texture...'
- **CRITICAL:** Empty transcript in chapter 'Use the Weight map on the displacement modifier.'
- **CRITICAL:** Empty transcript in chapter 'Apply the modifier and add a decimation modifier.'
- **CRITICAL:** Total transcript only 63 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (37 chars) in 'Add a wireframe modifier.'
- WARNING: Very short transcript (26 chars) in 'Add a subdivide modifier...'

---


Frames captured — see "Captured Frames" section below.


### TISSUE ADD-ON EXPERIMENT 2 [0:00]

### Paint a Weight Map on the sphere... [0:06]

### Add a displacement modifier and a texture... [0:14]

### Use the Weight map on the displacement modifier. [0:20]

### Apply the modifier and add a decimation modifier. [0:28]

### Add a wireframe modifier. [1:10]
**Transcript (timestamped):**
[1:30] Highlight,
[1:34] Diffuse,
[1:38] Diffuse,
[1:42] Diffuse,


### Add a subdivide modifier... [1:43]
**Transcript (timestamped):**
[1:46] Diffuse,
[1:50] Diffuse,
[1:54] Diffuse,



---

## Captured Frames

- [0:06] tutorials/frames/daily-blender-tip-136---tissue-add-on-experiment-2/frame_000.jpg
- [0:14] tutorials/frames/daily-blender-tip-136---tissue-add-on-experiment-2/frame_001.jpg
- [0:20] tutorials/frames/daily-blender-tip-136---tissue-add-on-experiment-2/frame_002.jpg
- [0:28] tutorials/frames/daily-blender-tip-136---tissue-add-on-experiment-2/frame_003.jpg
- [1:20] tutorials/frames/daily-blender-tip-136---tissue-add-on-experiment-2/frame_004.jpg
- [1:45] tutorials/frames/daily-blender-tip-136---tissue-add-on-experiment-2/frame_005.jpg

---

## Structured Notes

### Core Technique
Direct continuation of Experiment 1: instead of letting a procedural texture displace the whole sphere uniformly, a hand-painted **Weight Map** (Vertex Group) restricts the Displace modifier to specific regions — and that same weight map continues to control later modifiers (Decimate, Wireframe) even after the mesh has been run through Tissue's Dual Mesh conversion, showing that vertex-group masking survives topology-changing operations. Note: this video's audio track is silent/near-empty; this summary is built entirely from the captured on-screen text captions and frames.

### Summary
Frame 000 shows the first step: a UV sphere in Weight Paint mode with a blue-and-yellow-green painted weight pattern across its surface (Draw tool, Weight 1.000, Radius 35px), captioned "Paint a Weight Map on the sphere..." Frame 001 shows a Displace modifier added with an image/procedural Texture type dropdown open (Blend, Clouds, Distorted Noise, Environment Map, Image or Movie, Magic, Marble, Musgrave, Noise), on a smooth red sphere, captioned "Add a displacement modifier and a texture..." Frame 002 shows the displacement now clearly confined to only part of the sphere's surface (organic craters/bumps on roughly half the sphere, the rest still smooth), the Displace modifier's Vertex Group field populated, captioned "Use the Weight map on the displacement modifier." Frame 003 shows the Tissue Tools panel with **Dual Mesh** applied to the displaced sphere (Weight Base options: Vertex Color, Area, Curvature, Harmonic; Vertex Group field), producing a cellular honeycomb pattern concentrated in the same weighted region, captioned "Apply the modifier and add a decimation modifier." Frame 004 shows a Wireframe modifier applied on top (Boundary, Crease Edges, Replace Original, Material Offset visible), the honeycomb pattern now rendered as a raised wire-mesh relief still following the original painted weight region, captioned "You can still use the weight map for this modifier." Frame 005 shows the Add Modifier search list open (Bevel, Boolean, Build, Decimate, Edge Split, Mask, Mirror, Multiresolution, Remesh, Screw, Skin, Solidify, Subdivision Surface, Triangulate, Weld, Wireframe options visible) over the finished honeycomb-relief sphere, captioned "Add a subdivide modifier..."

### Key Steps
1. In Weight Paint mode, paint a Weight Map (Vertex Group) directly onto a UV sphere, marking the region(s) that should receive the upcoming effect.
2. Add a **Displace** modifier and assign it a procedural or image Texture.
3. Assign the painted Weight Map to the Displace modifier's **Vertex Group** field — displacement now only affects the weighted region instead of the whole sphere, leaving the rest of the surface smooth/undisturbed.
4. Apply the Displace modifier to bake the partial displacement into real geometry, then add a **Decimate** modifier to simplify/refacet the result.
5. Run Tissue's **Dual Mesh** operation on the decimated shape — the resulting honeycomb/cellular topology naturally stays concentrated in the same region that was originally weighted and displaced, since Dual Mesh operates on whatever geometry is present.
6. Add a **Wireframe** modifier on top — importantly, **the same original weight map can still be assigned to this modifier too**, continuing to localize its effect (wire thickness/coverage) to the same painted region even after the mesh has gone through Displace → Decimate → Dual Mesh.
7. Add further Subdivision for a denser, more refined final relief pattern.

### Nodes / Settings
- **Weight Paint:** Draw tool (Weight, Radius, Strength), creates a Vertex Group usable across multiple later modifiers.
- **Modifiers:** Displace (Texture type: Blend/Clouds/Distorted Noise/Environment Map/Image or Movie/Magic/Marble/Musgrave/Noise, Vertex Group field), Decimate, Wireframe (Boundary, Crease Edges, Replace Original, Material Offset, Vertex Group field), Subdivision Surface.
- **Tissue add-on:** Dual Mesh operator (Weight Base: Vertex Color/Area/Curvature/Harmonic, Vertex Group field) — confirmed to respect/propagate the same vertex-group masking used elsewhere in the stack.

### Difficulty
Intermediate

### Blender Version
Not specified — an earlier-era Tissue add-on workflow, direct continuation of Experiment 1.

### Tags
organic, procedural, displacement, abstract, intermediate

---

## Related Tutorials
- [Daily Blender Tip 135 - Tissue Add-on: Experiment 1](daily-blender-tip-135---tissue-add-on-experiment-1.md) — shares organic, procedural, displacement, abstract, intermediate; direct predecessor in the same experiment series, that one using unweighted whole-sphere displacement before Dual Mesh + Wireframe.
- [Vertex Groups, Modifiers and Tissue Add-on - Blender Secrets](vertex-groups-modifiers-and-tissue-add-on---blender-secrets.md) — shares organic, procedural, intermediate; the channel's later, more refined revisit of exactly this weight-map-drives-Tissue-and-modifiers technique, confirmed working on Blender 4.3.2.
- [Daily Blender Tip 137 - Tissue Add-on: Experiment 3](daily-blender-tip-137---tissue-add-on-experiment-3.md) — shares organic, procedural, abstract, intermediate; direct sequel in the same experiment series, moving from Dual Mesh + weight-mapped Displace to self-replicating Tesselate growth and a Metaball Remesh.
