---
title: NS Rock Sculptor Guide - Edge Crease
source: YouTube
url: https://www.youtube.com/watch?v=YEtwMhsKh1A
author: Nick Sayce
ingested: 2026-08-17
blender_version: "5.1.x (approximate, viewport title bar in captured frames; not stated verbally)"
tags: [procedural, geometry-nodes, organic, product-viz, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/ns-rock-sculptor-guide---edge-crease/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Rock Sculptor Guide - Edge Crease

**Source:** [YouTube](https://www.youtube.com/watch?v=YEtwMhsKh1A)
**Author:** Nick Sayce
**Duration:** 3m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 395 chars (min 500). Captions unavailable or audio silent — extraction will be poor.

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Edge Crease
[0:30] I'm just going to remesh the edges for any edges I can strengthen using the edge crease.
[0:54] I can't find a way to remesh the edges to follow the contours.
[1:32] I can't find a way to sharpen the edges.
[2:02] I can't find a way to sharpen the edges to follow the contours.
[2:32] I can't find a way to sharpen the edges to follow the contours.
[3:02] I can't find a way to remesh the edges to follow the contours.



---

## Captured Frames

- [0:10] tutorials/frames/ns-rock-sculptor-guide---edge-crease/frame_000.jpg
- [0:45] tutorials/frames/ns-rock-sculptor-guide---edge-crease/frame_001.jpg
- [1:15] tutorials/frames/ns-rock-sculptor-guide---edge-crease/frame_002.jpg
- [1:45] tutorials/frames/ns-rock-sculptor-guide---edge-crease/frame_003.jpg
- [2:15] tutorials/frames/ns-rock-sculptor-guide---edge-crease/frame_004.jpg
- [2:45] tutorials/frames/ns-rock-sculptor-guide---edge-crease/frame_005.jpg

---

> **Third-party add-on note:** This tutorial covers the **Edge Crease** tab of **NS Rock Sculptor**, a paid third-party Blender add-on by Nick Sayce (NS). The sidebar's "Enter Edit Mode" / "Clear All Creases" buttons are add-on-provided shortcuts wrapping Blender's own native Edge Crease (Shift+E) mesh data, not a custom add-on-only effect.

**Transcription note:** Whisper produced a degenerate, repeating-loop transcript on this video's audio (near-identical phrases at ~30s intervals — a known failure mode on thin/quiet narration), flagged `CRITICAL` by the ingest safeguard as unreliable. This extraction is based entirely on the 6 captured frames, not the transcript text, which has been disregarded.

## Structured Notes

### Core Technique
Marking specific mesh edges with Blender's native Edge Crease (accessed via an add-on-provided "Enter Edit Mode" shortcut in the sidebar) so the Subdivision Surface modifier keeps those edges sharp/faceted instead of rounding the whole rock into a uniform smooth blob.

### Summary
Captured frames show a matcap/clay-shaded rock (textures hidden to isolate pure silhouette) cut between an untouched, fully rounded subdivided blob and a version with visibly sharper, more angular corners and edges — consistent with selective edge creasing pulling the Subdivision Surface result back toward the base low-poly cube's hard edges in specific places rather than smoothing everything uniformly. One frame shows Edit Mode active with a ring of edges selected/highlighted around the mesh, implying edges are chosen manually before creasing is applied. The sidebar section itself is minimal: an "Enter Edit Mode" button (jumps directly into edge-select mode on the target object, add-on convenience wrapper) and a "Clear All Creases" button (resets any creasing back to zero) — the actual crease-weight painting/application happens through Blender's standard Edit Mode edge-select + Shift+E workflow, not a custom add-on slider.

### Key Steps
1. Open the "Edge Crease" section in the NS Rock Sculptor sidebar.
2. Click "Enter Edit Mode" (add-on shortcut) to jump directly into the object's Edit Mode with edge-select active.
3. Select the specific edges on the base mesh where you want to preserve sharpness/facets rather than let the Subdivision Surface modifier round them off — frames show a contiguous ring/loop of edges selected around part of the rock.
4. Apply Blender's native Edge Crease (standard shortcut Shift+E, drag to set crease weight) to the selected edges.
5. Exit Edit Mode to see the Subdivision Surface result respect the creased edges — the rock silhouette shows a mix of smooth rounded faces and sharper, more angular corners where creases were applied, rather than a uniformly rounded blob.
6. Use "Clear All Creases" to reset all edge crease weights on the object back to zero if you want to start over or remove the effect entirely.

### Nodes / Settings
- Sidebar section "Edge Crease" (positioned early in the panel order, after Weight Paint and before Colour, per the order seen across this series: Sculpt Settings, Weight Paint, Edge Crease, Colour, Moss, Filters, Colour Ramps, Displacement, Bump, Geometry, Scatter)
- "Enter Edit Mode" button — jumps into Blender's native Edit Mode / edge-select
- "Clear All Creases" button — resets Blender's native Edge Crease data on the object
- Underlying mechanism: standard Blender Edge Crease (Shift+E), consumed by the Subdivision Surface modifier already present in the modifier stack

### Difficulty
Intermediate (requires understanding how Edge Crease interacts with Subdivision Surface — not a slider, but a manual Edit Mode edge-selection workflow)

### Blender Version
5.1.x (approximate, viewport title bar in captured frames; not stated verbally) — consistent with other NS Rock Sculptor Guide episodes from this same upload batch (2026-07-30/31).

### Tags
procedural, geometry-nodes, organic, product-viz, intermediate

---

## Related Tutorials
Part of the **NS Rock Sculptor Guide** series (10 episodes, all uploaded 2026-07-30) covering the NS Rock Sculptor add-on tab by tab. This episode covers the Edge Crease tab.
- [NS Rock Sculptor Guide - Sculpt Settings](ns-rock-sculptor-guide-sculpt-settings.md) — same add-on/series, Sculpt Settings tab (adjacent in panel order — this episode's base mesh/Subdivision Surface level comes from there).
- [NS Rock Sculptor Guide - Geometry & Scatter](ns-rock-sculptor-guide---geometry-scatter.md) — same add-on/series, Geometry & Scatter tabs (directly relevant — that episode's decimation step explicitly warns Edge Wear/crease-adjacent detail must be applied before decimating).
- [NS Rock Sculptor Guide - Displacement](ns-rock-sculptor-guide---displacement.md) — same add-on/series, Displacement tab (its Subdivision Surface viewport-level guidance directly affects how visible edge creases read, per that episode's own notes).
- [NS Rock Sculptor Guide - Colour](ns-rock-sculptor-guide---colour.md) — same add-on/series, Colour tab.
