---
title: Daily Blender Tip 137 - Tissue Add-on: Experiment 3
source: YouTube
url: https://www.youtube.com/watch?v=8wimWMzVA9M
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — earlier-era Tissue add-on Tesselate operator, final part of the Experiment series"
tags: [organic, procedural, abstract, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-137---tissue-add-on-experiment-3/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 137 - Tissue Add-on: Experiment 3

**Source:** [YouTube](https://www.youtube.com/watch?v=8wimWMzVA9M)
**Author:** Blender Secrets
**Duration:** 2m24s | 15 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'TISSUE ADD-ON EXPERIMENT 3'
- **CRITICAL:** Empty transcript in chapter 'Create a plane, subdivide and delete these faces'
- **CRITICAL:** Empty transcript in chapter 'Duplicate the face, merge the verts and extrude it.'
- **CRITICAL:** Empty transcript in chapter 'Extrude two branches of vertices.'
- **CRITICAL:** Empty transcript in chapter 'Duplicate the face twice.'
- **CRITICAL:** Empty transcript in chapter 'Align the faces to the end of the branches'
- **CRITICAL:** Empty transcript in chapter 'In the tool panel, tissue add-on, click Tesselate'
- **CRITICAL:** Empty transcript in chapter 'With these settings, click ОК.'
- **CRITICAL:** Empty transcript in chapter 'Go back to the settings, choose the tesselated mesh'
- **CRITICAL:** Empty transcript in chapter 'Click Refresh to grow the object.'
- **CRITICAL:** Empty transcript in chapter 'Select and delete all the faces.'
- **CRITICAL:** Empty transcript in chapter 'Delete the original objects, remove double vertices.'
- **CRITICAL:** Empty transcript in chapter 'Add a remesh modifier and choose Metaball.'
- **CRITICAL:** Total transcript only 19 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (16 chars) in 'Click on Vertices.'
- WARNING: Very short transcript (3 chars) in 'To solve the gaps, add more vertices.'

---


Frames captured — see "Captured Frames" section below.


### TISSUE ADD-ON EXPERIMENT 3 [0:00]

### Create a plane, subdivide and delete these faces [0:04]

### Duplicate the face, merge the verts and extrude it. [0:09]

### Extrude two branches of vertices. [0:14]

### Duplicate the face twice. [0:18]

### Align the faces to the end of the branches [0:23]

### In the tool panel, tissue add-on, click Tesselate [0:47]

### With these settings, click ОК. [0:51]

### Go back to the settings, choose the tesselated mesh [0:55]

### Click Refresh to grow the object. [1:05]

### Select and delete all the faces. [1:13]

### Delete the original objects, remove double vertices. [1:18]

### Add a remesh modifier and choose Metaball. [1:25]

### Click on Vertices. [1:29]
**Transcript (timestamped):**
[2:00] це, nanokomiter.


### To solve the gaps, add more vertices. [2:02]
**Transcript (timestamped):**
[2:08] you



---

## Captured Frames

- [0:04] tutorials/frames/daily-blender-tip-137---tissue-add-on-experiment-3/frame_000.jpg
- [0:09] tutorials/frames/daily-blender-tip-137---tissue-add-on-experiment-3/frame_001.jpg
- [0:14] tutorials/frames/daily-blender-tip-137---tissue-add-on-experiment-3/frame_002.jpg
- [0:18] tutorials/frames/daily-blender-tip-137---tissue-add-on-experiment-3/frame_003.jpg
- [0:47] tutorials/frames/daily-blender-tip-137---tissue-add-on-experiment-3/frame_004.jpg
- [1:05] tutorials/frames/daily-blender-tip-137---tissue-add-on-experiment-3/frame_005.jpg
- [1:18] tutorials/frames/daily-blender-tip-137---tissue-add-on-experiment-3/frame_006.jpg
- [1:25] tutorials/frames/daily-blender-tip-137---tissue-add-on-experiment-3/frame_007.jpg

---

## Structured Notes

### Core Technique
The final part of the Tissue Add-on Experiment series: a single branching "unit" object (a face with two forked extruded branches, each capped with a small face) is fed into Tissue's **Tesselate** operator with "Lattice along Surface," then repeatedly **Refresh**ed so each generation of branches sprouts a new copy of the same unit — self-replicating into a full fractal tree structure. The resulting branch-line network is then cleaned up and passed through a **Remesh modifier set to Metaball**, fusing the whole tangle of thin branches into one smooth, organic blobby coral/tree-like surface.

### Summary
Frame 000 shows the starting geometry: a single subdivided plane with some interior faces deleted, viewed from an angled perspective, captioned "Create a plane, subdivide and delete these faces." Frame 001 shows one small square face isolated (duplicated from the plane, verts merged), about to be extruded, captioned "Duplicate the face, merge the verts and extrude it." Frame 002 shows that face now extruded upward into a single stalk, with the start of a fork visible at the top, captioned "Extrude two branches of vertices" — the beginning of the two-pronged branching unit. Frame 003 shows the branch unit duplicated twice more with a Y-shaped fork rotated around the vertical axis (three angled copies visible fanned out), captioned "Duplicate the face twice." Frame 004 shows the Tissue Tools panel's **Tesselate** operator being applied (Tesselate Add/Edit sections, a "Lattice along Surface" checkbox, "UV to Mesh" option), with the single branch unit now positioned at the base of a growing structure, captioned "In the tool panel, tissue add-on, click Tesselate." Frame 005 shows the payoff of clicking **Refresh** repeatedly: the branch unit has replicated itself generation after generation into a small but clearly fractal, tree-like branching cluster (Tissue Settings panel with Component/Frame fields, "New Component to be created" note), captioned "Click Refresh to grow the object." Frame 006 shows a much further-grown result: a dense, dark, leafless tree silhouette with many branching generations, viewed alongside the small original seed objects still sitting at its base, captioned "Delete the original objects, remove double vertices" — cleanup after growth is complete. Frame 007 shows the final payoff: the same branch structure now with a Remesh modifier applied and set to **Metaball**, rendering as a smooth, continuous, softly-blobby organic tree/coral form instead of thin disconnected lines, captioned "Add a remesh modifier and choose Metaball."

### Key Steps
1. Create a Plane, subdivide it, and delete some of the resulting faces to leave a partial/irregular base shape.
2. Duplicate one small face, merge its vertices down to a simplified point/quad, and extrude it upward into a stalk — this becomes the reusable "growth unit."
3. From the top of that stalk, extrude two separate branches of vertices (a fork), each capped with a small face — these capping faces are what the next generation will attach to.
4. Duplicate the capping face twice more, rotating/positioning the duplicates so the unit has multiple branch endpoints ready to keep growing from, and align these faces to the ends of the branches.
5. In the Tissue Tools panel, click **Tesselate**, enabling **Lattice along Surface** (and optionally UV to Mesh) in its settings, then confirm with OK — this sets up the base unit as a self-replicating "component."
6. Go back into the Tissue settings, choose the tesselated mesh as the component to grow, and click **Refresh** repeatedly — each click grows another generation of the branch unit onto the ends of the previous generation, compounding into a fractal tree-like structure.
7. Once enough growth generations exist, select and delete leftover flat cap faces that are no longer needed, delete the original small seed/unit objects that aren't part of the final grown structure, and remove doubled/duplicate vertices left over from the repeated tesselation process.
8. Add a **Remesh** modifier and set its mode to **Metaball** — this fuses the entire thin branching line-network into one smooth, continuous, blobby organic surface rather than leaving it as disconnected thin sticks.
9. Troubleshooting note: if the Metaball remesh produces visible gaps or disconnected regions, add more vertices/geometry to the branch network so nearby branches sit close enough for the metaball field to bridge them.

### Nodes / Settings
- **Modeling:** Plane subdivision, face duplication + vertex merge, Extrude (branch stalks), face-to-branch alignment.
- **Tissue add-on Tesselate operator:** Tesselate Add/Edit, "Lattice along Surface" option, UV to Mesh, Refresh (re-runs growth using the current component), Settings panel (Component, Frame).
- **Cleanup:** Select + Delete (stray cap faces, original seed objects), Remove Doubles/Merge by Distance (duplicate vertices from repeated tesselation).
- **Modifier:** Remesh (Mode: Metaball) — fuses a sparse branch network into one smooth organic surface; adding more vertices closes any resulting gaps.

### Difficulty
Intermediate to Advanced (self-replicating Tesselate growth is a more involved technique than the previous two Experiments)

### Blender Version
Not specified — an earlier-era Tissue add-on workflow (Tesselate operator), final part of the Experiment series.

### Tags
organic, procedural, abstract, intermediate

---

## Related Tutorials
- [Daily Blender Tip 136 - Tissue Add-on: Experiment 2](daily-blender-tip-136---tissue-add-on-experiment-2.md) — shares organic, procedural, abstract, intermediate; direct predecessor in the same experiment series, using Dual Mesh + weight-mapped Displace rather than this video's self-replicating Tesselate growth.
- [Daily Blender Tip 135 - Tissue Add-on: Experiment 1](daily-blender-tip-135---tissue-add-on-experiment-1.md) — shares organic, procedural, abstract, intermediate; first entry in the same 3-part experiment series.
