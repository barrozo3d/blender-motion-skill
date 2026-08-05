---
title: Blender Secrets - Modeling from Photos with the Knife Tool (part 1: basics)
source: YouTube
url: https://www.youtube.com/watch?v=VzsxFT3-Kmk
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (core Knife tool/Images-as-Planes/UV workflow, 2.9x-5.x)"
tags: [modelling, materials, procedural, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-secrets---modeling-from-photos-with-the-knife-tool-part-1-basics/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Secrets - Modeling from Photos with the Knife Tool (part 1: basics)

**Source:** [YouTube](https://www.youtube.com/watch?v=VzsxFT3-Kmk)
**Author:** Blender Secrets
**Duration:** 1m31s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Using the knife tool, we can quickly turn a photo into a textured 3D model.
[0:08] First make sure the import images as planes add on is enabled.
[0:11] Then go to add, image, images as plane.
[0:17] Switch to material preview mode and go to front orthographic view.
[0:21] In edit mode, press K to activate the knife tool.
[0:24] Now you can cut out a selection.
[0:26] You can scroll the mouse wheel to zoom in and out when you need to be more precise.
[0:34] Once you've cut around what you want to keep and closed the loop, press enter.
[0:38] Select the faces that you don't need and delete them.
[0:41] Use the knife tool to cut out additional selections for extruding.
[0:46] In case there's visible stretching on the extruded parts, select those and go to a side
[0:50] view.
[0:51] Then press U and choose project from view.
[0:54] In the UV editor window, find a good spot for those UVs.
[0:58] If you like this tip, you'll also like the Blender Secrets eBook.
[1:02] With more than a thousand pages and more on the way.
[1:06] By clicking on a topic in the index, you are transported to the relevant pages.
[1:11] And clicking on the link at the bottom of the page takes you back to the index of 400
[1:15] plus topics.
[1:17] To see the corresponding video on a topic, simply click on the topic title.
[1:22] These are always free for customers both on Gumroad and Blender Market.



---

## Captured Frames

- [0:20] tutorials/frames/blender-secrets---modeling-from-photos-with-the-knife-tool-part-1-basics/frame_000.jpg
- [0:30] tutorials/frames/blender-secrets---modeling-from-photos-with-the-knife-tool-part-1-basics/frame_001.jpg
- [0:40] tutorials/frames/blender-secrets---modeling-from-photos-with-the-knife-tool-part-1-basics/frame_002.jpg
- [0:45] tutorials/frames/blender-secrets---modeling-from-photos-with-the-knife-tool-part-1-basics/frame_003.jpg
- [0:53] tutorials/frames/blender-secrets---modeling-from-photos-with-the-knife-tool-part-1-basics/frame_004.jpg

---

## Structured Notes

### Core Technique
Part 1 (basics) of a photo-modeling series: use the Knife tool directly on an Images-as-Planes photo to trace and cut out a textured 3D shape (demoed on a European building facade photo), extruding selected cuts for depth and fixing UV stretching on extruded faces via Project From View.

### Summary
Frame 000 shows the source material: a full-building facade photograph loaded via Images as Planes, viewed in Material Preview shading in Front Orthographic view — the caption confirms this exact setup step. Frame 001 shows the Knife tool (K) actively tracing an irregular decorative gable/roofline shape directly on the photo texture in Edit Mode, mid-cut with the loop not yet closed. Frame 002 shows the next step: the Delete menu open with "Faces" highlighted, removing the parts of the image plane that fall outside the traced cut. Frame 003 shows a further knife-cut selection around a row of windows, captioned "Use the Knife tool to cut out additional selections for extruding" — these will be pushed inward with E to add real depth (window reveals) rather than staying flat. Frame 004 shows the UV-fix step: the U (UV Mapping) menu open with "Project From View" highlighted — used to re-map UVs on extruded faces that would otherwise show visible texture stretching, since their new geometry no longer matches the original flat photo-plane UV layout.

### Key Steps
1. Enable the Images as Planes add-on (built into Blender, enable in Preferences); Add → Image → Images as Planes to load a reference photo as a textured plane.
2. Switch Viewport Shading to Material Preview and align the view to Front Orthographic for a 1:1 match with the photo.
3. In Edit Mode, press K to activate the Knife tool; trace around the shape you want to keep (scroll to zoom in for precision on fine details), and press Enter once the cut loop is closed.
4. Select the faces outside the traced shape that aren't needed and delete them (Delete → Faces).
5. Use the Knife tool again to cut out additional sub-selections (e.g. individual window frames) that should be extruded for real depth rather than staying flat against the photo.
6. Extrude those selections inward/outward (E) to add dimensional depth matching what the photo implies.
7. **Fix UV stretching on extruded geometry:** select the newly extruded faces, switch to a side view matching their new orientation, press U → Project From View to re-project clean UVs for those faces (rather than inheriting the stretched UVs from the original flat projection); in the UV Editor, reposition the newly projected UV islands to a good spot on the texture.

### Nodes / Settings
- **Add-on:** Images as Planes (built-in).
- **Viewport:** Material Preview shading, Front Orthographic view (for 1:1 photo tracing accuracy).
- **Edit-mode operators:** K (Knife tool), Delete → Faces, E (Extrude).
- **UV mapping:** U → Project From View (re-maps UVs for extruded geometry to avoid stretching), UV Editor for repositioning islands.

### Difficulty
Beginner to Intermediate

### Blender Version
Not specified — core Knife tool / Images as Planes / UV workflow, version-agnostic across modern Blender (2.9x-5.x).

### Tags
modelling, materials, procedural, beginner, intermediate

---

## Related Tutorials
[No existing INDEX.md entries share 2+ of these tags in a photo-to-3D Knife-tool context yet, and no "Part 2" of this series exists in the current tutorials folder — this "Part 1: basics" is the only Modeling-from-Photos-with-the-Knife-Tool entry ingested so far.]
