---
title: Everything New in Blender 5.2 Geometry Nodes
source: YouTube
url: https://www.youtube.com/watch?v=3B9_kJEjsqc
author: Cartesian Caramel
ingested: 2026-07-18
blender_version: "Blender 5.2"
tags: [geometry-nodes, procedural, simulation, release-notes, blender-5x, feature-survey, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/everything-new-in-blender-52-geometry-nodes/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Everything New in Blender 5.2 Geometry Nodes

**Source:** [YouTube](https://www.youtube.com/watch?v=3B9_kJEjsqc)
**Author:** Cartesian Caramel
**Duration:** 5m5s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, this is Cartesian Caramel covering the Geometry node changes for Blender 5.2.
[0:05] This is a big update with many features, so let's get started.
[0:09] This release comes with a new physics system focusing on hair and cloth.
[0:13] Two new modifiers powered by the new XBPD Solver node have an added,
[0:17] cloth dynamics and hair dynamics. These are generalized systems that allow for custom forces.
[0:23] While they are still experimental, users are recommended to try them and give feedback for future releases.
[0:29] Bundles can now be attached to geometry, allowing for arbitrary data to be passed across
[0:34] modifier and object boundaries, using the new set geometry bundle and get geometry bundle nodes.
[0:40] Data attached to geometry can be seen in the spreadsheet.
[0:44] Lists are a new core data type that allows storing a sequence of arbitrary data and come with
[0:48] several new nodes. Filtalist creates a new list by evaluating index dependent fields.
[0:54] Closure to list creates new list by evaluating a closure that has an index input.
[0:58] List length outputs the length of a list. GetListItem outputs an individual item.
[1:03] Filtalist creates a new list if a boolean is true or false.
[1:07] SwartLists sorts based on a custom weight.
[1:10] The new collection children node uses lists to output the child objects and collections of a given
[1:16] collection with an option for recursion. A new sound socket type has been added.
[1:21] This is used by the new sample sound frequencies node, which uses an imported sound to output
[1:26] the amplitude as a float. It can also sample frequency ranges, which allows for creating sound
[1:31] spectrum animations. Empty objects can now have geometry nodes. This is useful for effects that
[1:38] don't require original data, and this also allows geometry nodes to be used on collection instances.
[1:44] The building blocks of the merged by distance node are now available individually as three new nodes.
[1:50] Merge points combines point or mesh vertices with the same group ID. CloserbyDistance
[1:54] creates group IDs for close points, and clusterbyConnected creates group IDs for close vertices connected
[2:00] by edges. The new meshBell node has been added, and is similar to the Bevel modifier and provides
[2:07] more detailed control. Attributes have three new nodes. Rename attribute allows renaming a
[2:13] single attribute or all attributes with a specific prefix. Get attribute names, outputs a list
[2:19] of the names of attributes in a geometry, optionally filtered by domain and data type. Transfer
[2:24] attribute can transfer an arbitrary number of attributes from one geometry to another.
[2:30] The capture attribute node now supports selection. This improves efficiency when an attribute value
[2:35] is only required by a subset of elements. Attributes can now be stored as 4D float vectors,
[2:41] though geometry nodes still only operates on 3D vectors. Curves have two new nodes. Set
[2:47] NURBS order controls how many curve points influence each evaluated point and set NURBS away
[2:52] controls the influence of each control point. Strings have four new nodes. TrimString removes
[2:59] specific characters at the star or end. ReverseString reverses the order of the characters. SplitString
[3:04] splits text into a list based on a delimiter, and setStringCase turns strings into upper or lower
[3:10] case. The value to string and string to value nodes now have a base input which specifies the
[3:16] number system used when converting two N from integers. The findInchString node can now find
[3:21] the first occurrence from the end. String fields are now supported, but keep in mind string attributes
[3:26] are not yet implemented. The default prey node group input can now be the scene frame or
[3:31] self object. Six new bundled assets have been added. 3D to screenspace transforms 3D coordinates
[3:39] from world to normalized camera space. Screen to 3D space is the inverse of this.
[3:44] Transform and project computes 2D coordinates in screenspace. Project with depth transforms
[3:49] coordinates from the viewport 3D space to screenspace and back. Principle components analyzes
[3:55] a position vector field and geometry principal components analyzes on a specific input geometry.
[4:03] In miscellaneous updates, the new instance reference node outputs the internal attribute
[4:07] which shows what geometry set index each instance is referencing. The new getGeometry component
[4:13] node extracts a single component of a geometry. The compare node now supports comparing data blocks.
[4:19] The boneInfo node now has an exists output and the viewer node can show data block names.
[4:25] Lastly, closures can now be called recursively up to a limit. A new call stack depth limit for
[4:31] geometry nodes can be configured in the user preferences. No tool inputs are remembered between
[4:36] operator invocations and can now be assigned in python. Internal fields are now de-duplicated for
[4:42] evaluation. This can speed up nodes are used multiple times like sample UV surface.
[4:47] Sampling nodes have improved performance when they can avoid conversions to the face corner domain.
[4:54] That was a lot of condensed information, but you should be able to learn it before the next
[4:58] release. I hope you all enjoyed this overview of the changes in additions to geometry nodes in
[5:02] Blender 5.2.



---

## Captured Frames

- [0:17] tutorials/frames/everything-new-in-blender-52-geometry-nodes/frame_000.jpg
- [0:34] tutorials/frames/everything-new-in-blender-52-geometry-nodes/frame_001.jpg
- [0:54] tutorials/frames/everything-new-in-blender-52-geometry-nodes/frame_002.jpg
- [1:26] tutorials/frames/everything-new-in-blender-52-geometry-nodes/frame_003.jpg
- [2:07] tutorials/frames/everything-new-in-blender-52-geometry-nodes/frame_004.jpg
- [3:04] tutorials/frames/everything-new-in-blender-52-geometry-nodes/frame_005.jpg
- [3:49] tutorials/frames/everything-new-in-blender-52-geometry-nodes/frame_006.jpg
- [4:13] tutorials/frames/everything-new-in-blender-52-geometry-nodes/frame_007.jpg

---

## Structured Notes

### Core Technique
Release survey: every Geometry Nodes change in Blender 5.2 — new XPBD physics (cloth + hair), geometry-attached Bundles, the List data type, sound sampling, and a large batch of new utility nodes.

### Summary
Cartesian Caramel's condensed rundown of GN 5.2. Headliners: an experimental **XPBD Solver** node powering new Cloth Dynamics and Hair Dynamics modifiers (generalized, custom-force-capable); **Bundles attachable to geometry** (`Set/Get Geometry Bundle`) passing arbitrary data across modifier/object boundaries (visible in the spreadsheet); **Lists** as a core data type with a node family; a **Sound socket** + `Sample Sound Frequencies` (amplitude/frequency-range float output for audio-reactive setups); GN on **Empty objects** (enables GN on collection instances); `Mesh Bevel` node (modifier-grade control with per-edge offsets and selection outputs); plus new attribute, curve NURBS, and string nodes, six screen-space/PCA bundled assets, recursive closures, and performance work (field de-duplication, faster sampling).

### Key Steps
(Feature checklist rather than steps)
1. **Physics**: `XPBD Solver` node (experimental) → Cloth Dynamics & Hair Dynamics modifiers; custom forces; demo panel: delta time 40 ms, mass 0.1 kg, stretchiness/bendiness/root bendiness.
2. **Bundles on geometry**: `Set Geometry Bundle` / `Get Geometry Bundle`; data crosses modifier & object boundaries; inspect in spreadsheet.
3. **Lists**: `Field to List`, `Closure to List` (index-input closure), `List Length`, `Get List Item`, `Filter List` (boolean), `Sort List` (custom weight); `Collection Children` node (child objects/collections, optional recursion).
4. **Sound**: sound socket + `Sample Sound Frequencies` — amplitude or frequency-range sampling → sound-spectrum animation.
5. **Empties can hold GN modifiers** — effects needing no original data; works on collection instances.
6. **Merge by Distance decomposed**: `Merge Points` (same group ID), `Cluster by Distance`, `Cluster by Connected`.
7. **`Mesh Bevel` node** — bevel-modifier-like with more control: per-side start/end offsets, miter, segments, shape, profile, and Vertex Face / Edge Face / Outer Edge / Mid Edge selection outputs.
8. **Attributes**: `Rename Attribute` (single or prefix-batch), `Get Attribute Names` (list, filterable by domain/type), `Transfer Attribute` (N attributes at once); `Capture Attribute` gains Selection; 4D float vector storage (ops still 3D).
9. **Curves**: `Set NURBS Order`, `Set NURBS Weight`.
10. **Strings**: `Trim String`, `Reverse String`, `Split String` (delimiter → list), `Set String Case`; base input on value↔string conversion; find-from-end; string fields supported (string *attributes* not yet).
11. **Bundled assets**: 3D to Screen Space, Screen to 3D Space, Transform and Project, Project with Depth, Principal Components, Geometry Principal Components.
12. **Misc**: `Instance Reference` (geometry-set index per instance), `Get Geometry Component`, Compare on data-blocks, `Bone Info` exists output, viewer shows data-block names, recursive closures (call-stack depth limit in preferences), tool inputs remembered/assignable in Python, de-duplicated field evaluation (faster Sample UV Surface etc.).

### Nodes / Settings
See feature checklist — all node names above are exact. Default group input can now be Scene Frame or Self Object.

### Difficulty
Intermediate (survey; assumes GN familiarity)

### Blender Version
Blender 5.2

### Tags
#geometry-nodes #procedural #simulation #release-notes #blender-5x #feature-survey #intermediate

---

## Related Tutorials
- [Everything New in Blender 5.2 LTS](everything-new-in-blender-52-lts.md) — the all-departments 5.2 survey; this video is the GN deep-dive companion
- [ALL 300+ Geometry Nodes in Blender](all-300-geometry-nodes-in-blender.md) — baseline node catalog to diff these additions against
- [Demystifying Geometry Nodes: The Ultimate Guide to Mastering Blender's Procedural Power](demystifying-geometry-nodes-the-ultimate-guide-to-mastering.md) — GN fundamentals
