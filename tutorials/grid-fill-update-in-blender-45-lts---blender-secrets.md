---
title: Grid Fill update in Blender 4.5 LTS - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=gS8MHAXKFQE
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 4.5 LTS (explicitly named — the new retopologize-existing-faces feature is new in this release)"
tags: [modelling, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/grid-fill-update-in-blender-45-lts---blender-secrets/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Grid Fill update in Blender 4.5 LTS - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=gS8MHAXKFQE)
**Author:** Blender Secrets
**Duration:** 1m47s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Grid Fill, which is a default feature of Blender, received a major upgrade in Blender 4.5 LTS.
[0:06] It was already an amazing tool for creating smooth surfaces and now it's gotten even better.
[0:11] When you select a hole in geometry by alt left clicking on a boundary, you can press
[0:15] Ctrl F and then press G to fill the hole.
[0:18] Or go to face, grid fill.
[0:19] The surface is filled and takes into account the curvature as well.
[0:23] You can also extrude a bunch of vertices to create an outline and then grid fill it to
[0:27] create a perfect curved surface.
[0:30] This is very useful for example when working with reference images.
[0:35] You need an even amount of vertices for this to work and ideally the same amount on opposite
[0:39] sides although that's not a requirement.
[0:42] You can enable statistics to help you see how many vertices you have.
[0:45] However, as long as it's an even number you can just select two rails of an edge loop
[0:49] and grid fill will guess the correct span and offset values for you.
[0:54] In fact this often works better than selecting the entire boundary loop.
[1:02] If you don't have an even amount of vertices add or dissolve an edge and then use the edge
[1:06] flow extension to redistribute them.
[1:10] Or use the loop tools extensions space feature to evenly space out vertices.
[1:15] And the offset allows you to rotate the geometry if necessary.
[1:18] But what's new in Blender 4.5 LTS?
[1:21] With this new update you can select existing faces and retopologize them.
[1:25] Just select the faces that you want to retopologize and then use grid fill.
[1:29] It will take angles and triangles and replaces them with quads.
[1:32] Just keep in mind that it still requires an even amount of vertices around the selection.



---

## Captured Frames

- [0:15] tutorials/frames/grid-fill-update-in-blender-45-lts---blender-secrets/frame_000.jpg
- [0:23] tutorials/frames/grid-fill-update-in-blender-45-lts---blender-secrets/frame_001.jpg
- [0:42] tutorials/frames/grid-fill-update-in-blender-45-lts---blender-secrets/frame_002.jpg
- [0:48] tutorials/frames/grid-fill-update-in-blender-45-lts---blender-secrets/frame_003.jpg
- [1:02] tutorials/frames/grid-fill-update-in-blender-45-lts---blender-secrets/frame_004.jpg
- [1:22] tutorials/frames/grid-fill-update-in-blender-45-lts---blender-secrets/frame_005.jpg

---

## Structured Notes

### Core Technique
Grid Fill turns a closed boundary loop of vertices into a curvature-aware, all-quad surface patch; Blender 4.5 LTS adds the ability to run it on a selection of *existing* faces to retopologize messy n-gon/triangle geometry into clean quads.

### Summary
Frame 000 shows a curved four-sided panel outline (already extruded from a reference shape) selected via Alt-click on its boundary, mid-caption "You can press Ctrl+F and then press G" — the fill-hole shortcut about to run. Frame 001 shows the Grid Fill result: the same outline now a smooth, evenly-gridded quad surface that correctly follows the boundary's curvature rather than filling flat. Frame 002 compares two grid-fill results side by side — a clean rectangular-grid fill on the left versus a fan-triangulated-looking fill on the right, illustrating "same amount on opposite sides, although that's not a requirement" (uneven vertex distribution still works but looks different). Frame 003 shows a freeform outline of the Statistics overlay enabled (Vertices/Edges/Faces counts visible top-left) with only two "rails" of an edge loop selected in orange at the bottom-left, per the "select two rails instead of the full boundary" tip. Frame 004 is a direct before/after comparison: "Selecting only rails" (left) versus "Selecting boundary" (right) on the same curved strip shape, both producing a clean quad grid — demonstrating the rails method often works better than selecting the whole loop. Frame 005 shows the new 4.5 feature: an existing messy patch of triangles and n-gons (rainbow-colored face-orientation overlay) about to be retopologized in place via Grid Fill, captioned "With this new update."

### Key Steps
1. **Fill a hole/boundary:** Alt+left-click a boundary edge loop to select it, then either press Ctrl+F then G, or go to Face > Grid Fill — the resulting surface follows the boundary's curvature rather than flat-filling it.
2. **Build a curved patch from scratch:** extrude a set of vertices to trace the outline you want, then Grid Fill that outline — useful for matching reference images.
3. **Vertex count requirement:** Grid Fill needs an *even* total number of boundary vertices; matching counts on opposite sides is ideal but not strictly required (enable the Statistics overlay to see live vertex/edge/face counts while working).
4. **Rails trick:** instead of selecting the full boundary loop, just select two "rails" (the two edge loops running along the patch, not the full perimeter) — Grid Fill will infer the correct Span and Offset values, and this often produces a cleaner result than selecting the whole boundary.
5. **Fixing an odd vertex count:** add or dissolve a single edge to change the count to even, then use the Edge Flow extension to redistribute vertices evenly along the loop, or use the LoopTools extension's Space feature to evenly space vertices.
6. **Offset control:** the Grid Fill operator's Offset value rotates which vertices pair with which across the fill, useful when the automatic guess doesn't align correctly.
7. **New in Blender 4.5 LTS — retopologize existing faces:** select a patch of existing faces (including messy n-gons and triangles) and run Grid Fill on the selection; it replaces that patch with clean quads, following the same curvature-aware logic — still requires an even vertex count around the selection boundary.

### Nodes / Settings
- **Operator:** Grid Fill (Face menu, or Ctrl+F > G shortcut) — parameters: Span, Offset, Simple Blending.
- **Selection:** Alt+click (select boundary/edge loop), Statistics overlay (live vertex/edge/face counts).
- **Extensions:** Edge Flow (redistribute vertices along a loop for an even count), LoopTools > Space (evenly space vertices).

### Difficulty
Intermediate

### Blender Version
Blender 4.5 LTS — explicitly named; the "retopologize existing faces" capability is stated as new in this release.

### Tags
modelling, procedural, intermediate

---

## Related Tutorials
- [Easy hole modeling for beginners - Blender Secrets](easy-hole-modeling-for-beginners---blender-secrets.md) — shares modelling, procedural; complementary hole-related technique — that video builds circular holes via bevel/LoopTools, this one fills irregular curved boundaries via Grid Fill.
