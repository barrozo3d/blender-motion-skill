---
title: Blender Secrets - Modeling Sci-Fi Greebles on a Sphere (using Annotate Tool)
source: YouTube
url: https://www.youtube.com/watch?v=IeLNfxeEqz0
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (core Annotate/Snapping/Shrinkwrap/Solidify workflow, 2.9x-5.x)"
tags: [modelling, procedural, sci-fi, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---modeling-sci-fi-greebles-on-a-sphere-using-annotate-tool/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - Modeling Sci-Fi Greebles on a Sphere (using Annotate Tool)

**Source:** [YouTube](https://www.youtube.com/watch?v=IeLNfxeEqz0)
**Author:** Blender Secrets
**Duration:** 1m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Enable the annotate tool and set placement to service so you can draw on other objects.
[0:10] Then draw your design.
[0:15] Hold CTRL if you want to erase instead of drawing strokes.
[0:19] Alternatively, you can hold D to draw annotation strokes with the left mouse button and erase
[0:25] by holding D and using the right mouse button.
[0:28] Turn on snapping and set it to face and enable project individual elements.
[0:33] Add any mesh primitive and merge it to one vertex.
[0:37] Then extrude at vertex to create an edge.
[0:39] Turn on in front to make sure you can see what you're doing.
[0:42] Check the retopology videos on this channel for more tips about the modeling part.
[0:47] Finally add a shrink wrap modifier with the sphere as the target and apply it.
[0:51] Then you can add some thickness with the solidify modifier.
[0:57] If you like this tip, you'll also like the Blender Secrets ebook.
[1:01] With more than a thousand pages and more on the way.
[1:05] By clicking on a topic in the index, you're transported to the relevant pages.
[1:10] And clicking on the link at the bottom of the page takes you back to the index of 400
[1:14] plus topics.
[1:16] To see the corresponding video on a topic, simply click on the topic title.
[1:21] These updates are always free for customers both on Gumroad and Blender Market.



---

## Captured Frames

- [0:15] tutorials/frames/blender-secrets---modeling-sci-fi-greebles-on-a-sphere-using-annotate-tool/frame_000.jpg
- [0:35] tutorials/frames/blender-secrets---modeling-sci-fi-greebles-on-a-sphere-using-annotate-tool/frame_001.jpg
- [0:40] tutorials/frames/blender-secrets---modeling-sci-fi-greebles-on-a-sphere-using-annotate-tool/frame_002.jpg
- [0:48] tutorials/frames/blender-secrets---modeling-sci-fi-greebles-on-a-sphere-using-annotate-tool/frame_003.jpg
- [0:53] tutorials/frames/blender-secrets---modeling-sci-fi-greebles-on-a-sphere-using-annotate-tool/frame_004.jpg

---

## Structured Notes

### Core Technique
Sketch a sci-fi panel-line/greeble design directly onto a curved surface (a sphere/dome, demoed as a robot head) with the Annotate tool as a visual guide, then manually build real edge geometry over that sketch snapped to the surface, and finally conform + thicken it with Shrink Wrap and Solidify modifiers.

### Summary
Frame 000 shows the payoff of the Annotate step: a network of blue annotation strokes sketched directly onto a green sci-fi robot dome/head, forming a branching panel-line/greeble design with circular node markers — exactly matching the described "draw your design" step, on a colorful example asset with purple and green mechanical detailing. Frame 001 shows the actual edge-modeling stage: a mesh primitive (visible as a default cube corner, bottom right) already merged to a single vertex (Merge menu open, "At Center" highlighted) positioned at the start of the traced annotation line on the sphere, about to be extruded to build real geometry along the sketch. Frame 002 shows the "In Front" Viewport Display option being enabled on a Circle object (arrow pointing at the checkbox) so the in-progress wireframe geometry stays visible through the sphere while modeling. Frame 003 shows the Add Modifier menu with **Shrinkwrap** highlighted — added once the traced edge-loop shape is built, to conform it exactly to the sphere's curved surface. Frame 004 shows the final Solidify modifier (Mode Simple, Thickness 0.05m, Offset 1.0, Rim Fill) giving the shrink-wrapped panel-line shape real physical thickness, turning the flat traced line into a raised 3D greeble detail.

### Key Steps
1. Enable the Annotate tool and set its Placement to **Surface** so strokes stick to the actual object surface rather than a flat 3D-cursor plane — this lets you draw directly on a curved sphere/dome.
2. Draw the panel-line/greeble design freehand on the surface; hold Ctrl to erase strokes instead of adding them (or alternatively hold D + LMB to draw and D + RMB to erase).
3. Enable Snapping, set Snap Target to Face, and enable Project Individual Elements — this is what lets newly created geometry conform to the curved sphere as you build it.
4. Add any mesh primitive and merge all its vertices to one (M → At Center) to get a single starting vertex; extrude that vertex repeatedly to trace real edge geometry directly over the annotated sketch lines, building up the branching panel-line network as actual mesh.
5. Enable "In Front" under the object's Viewport Display settings so the in-progress wireframe stays visible even when it's behind/inside the sphere — critical for seeing what you're doing while tracing. (The author points to this channel's separate retopology videos for more general modeling tips relevant to this tracing process.)
6. Once the traced edge network is complete, add a Shrinkwrap modifier targeting the sphere and apply it — this snaps the entire traced shape precisely onto the sphere's curved surface.
7. Add a Solidify modifier to give the flat, shrink-wrapped line shape real thickness, turning it into a proper raised 3D greeble/panel-line detail.

### Nodes / Settings
- **Grease Pencil tool:** Annotate (Placement = Surface, Ctrl to erase, or D+LMB draw / D+RMB erase).
- **Snapping:** Snap Target = Face, Project Individual Elements.
- **Edit-mode operators:** M → At Center (merge to single vertex), Extrude (build edge geometry along the annotated sketch).
- **Viewport Display:** "In Front" toggle (see wireframe through the sphere while modeling).
- **Modifiers:** Shrinkwrap (target = sphere, applied to conform traced geometry to the curved surface), Solidify (Mode Simple, Thickness, Offset, Rim Fill — gives the traced line real thickness).

### Difficulty
Intermediate

### Blender Version
Not specified — core Annotate/Snapping/Shrinkwrap/Solidify workflow, version-agnostic across modern Blender (2.9x-5.x).

### Tags
modelling, procedural, sci-fi, intermediate

---

## Related Tutorials
[No existing INDEX.md entries share 2+ of these tags in an Annotate-tool-for-modeling context yet — this is the first "Annotate tool as a modeling guide" tutorial extracted from the BlenderSecrets backlog.]
