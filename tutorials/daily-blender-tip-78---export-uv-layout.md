---
title: Daily Blender Tip 78 - Export UV Layout
source: YouTube
url: https://www.youtube.com/watch?v=w-GVrw0FBXs
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Export UV Layout and Open Image workflow are version-agnostic core Blender UV/texturing tools"
tags: [uv, workflow, materials, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-78---export-uv-layout/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 78 - Export UV Layout

**Source:** [YouTube](https://www.youtube.com/watch?v=w-GVrw0FBXs)
**Author:** Blender Secrets
**Duration:** 1m55s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 25 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (25 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[1:30] It gets back for you.
[1:36] you



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-78---export-uv-layout/frame_000.jpg
- [0:25] tutorials/frames/daily-blender-tip-78---export-uv-layout/frame_001.jpg
- [0:45] tutorials/frames/daily-blender-tip-78---export-uv-layout/frame_002.jpg
- [1:05] tutorials/frames/daily-blender-tip-78---export-uv-layout/frame_003.jpg
- [1:25] tutorials/frames/daily-blender-tip-78---export-uv-layout/frame_004.jpg
- [1:50] tutorials/frames/daily-blender-tip-78---export-uv-layout/frame_005.jpg

---

## Structured Notes

### Core Technique
Exporting a mesh's **UV Layout** as an image template (**UVs > Export UV Layout**, from the UV Editor's View mode) to paint a texture precisely on the correct UV shape in an external image editor (Krita), then re-importing that painted texture back into Blender via the UV/Image Editor's Open Image — a round-trip external texture-painting workflow. Directly continues the same cylindrical cup model from [Tip 77](daily-blender-tip-77---unwrap-a-cup---follow-active-quads.md).

### Summary
Frame 000 shows the cup model in Edit Mode next to its clean, evenly-gridded UV layout in the UV Editor, captioned "Sometimes you want to paint or edit textures in external software. You need to export the UV layout." Frame 001 shows the UVs menu open with **Export UV Layout** highlighted, captioned "Click on UVs, Export UV Layout (you need to be in View mode for this)" — a small red box in the corner marks the "View" mode toggle as a prerequisite. Frame 002 shows Krita's File menu open, captioned "Now you can open this file in your favorite image editing software. I like Krita! It's free like Blender and good." Frame 003 shows Krita's canvas with a red zigzag/scribble painted over the exported UV grid template on one layer, a Layers panel showing the UV Layout layer and the paint layer, captioned "Paint some texture masterpiece and turn off the UV Layout layer before saving this texture." Frame 004 shows Blender's Open Image file browser pointed at a "textures" folder with texture_2.png selected, captioned "Back in Blender (whew, it was scary out there) we open the texture file in the UV/Image editor." Frame 005 is the closing card, captioned "The texture is already loaded so you can choose it here. Switch to texture mode to see it on the model."

### Key Steps
1. With the mesh UV-unwrapped (see Tip 77's Follow Active Quads technique), open the **UV Editor** and switch it to **View** mode (required for the export option to appear).
2. Go to **UVs > Export UV Layout** to save the UV wireframe as a template image (PNG/SVG/EPS).
3. Open that exported template in an external 2D image editor (Krita used here — free, like Blender) as a reference layer.
4. Paint the actual texture artwork on a **separate layer above** the UV template layer, using the wireframe as a guide for where texture details need to land relative to each UV island.
5. **Turn off/hide the UV Layout template layer** before flattening/saving the final texture image — it should not be baked into the exported PNG.
6. Back in Blender, use the UV/Image Editor's **Open Image** to load the newly painted texture file, then switch the viewport to **Texture** shading mode to preview it correctly mapped onto the model.

### Nodes / Settings
- **UV Editor > View mode** (required) **> UVs > Export UV Layout**.
- External tool: Krita (or any image editor) for painting over the exported UV template.
- **UV/Image Editor > Open Image** — reload the finished texture back into Blender.
- **Texture** viewport shading mode — to preview the applied texture.

### Difficulty
Beginner

### Blender Version
Not specified — Export UV Layout and the Open Image workflow are version-agnostic core Blender UV/texturing tools.

### Tags
uv, workflow, materials, beginner

---

## Related Tutorials
- [Daily Blender Tip 77 - Unwrap a Cup - Follow Active Quads](daily-blender-tip-77---unwrap-a-cup---follow-active-quads.md) — shares uv, workflow; this is the direct sequel, exporting the exact same cup model's clean UV layout (produced there via Follow Active Quads) to paint its texture externally in Krita.
