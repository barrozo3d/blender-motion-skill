---
title: NS Infinite Rock Builder Guide - Colours
source: YouTube
url: https://www.youtube.com/watch?v=1ezIk-0qoDg
author: Nick Sayce
ingested: 2026-08-12
blender_version: "4.x (see Main Controls video for title-bar reading; not independently confirmed here)"
tags: [materials, shaders, procedural, organic, beginner, blender-4x]
extraction_status: complete
frames_dir: tutorials/frames/ns-infinite-rock-builder-guide---colours/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Infinite Rock Builder Guide - Colours

**Source:** [YouTube](https://www.youtube.com/watch?v=1ezIk-0qoDg)
**Author:** Nick Sayce
**Duration:** 4m18s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Colors, let's do colors. There's a lot, a lot you can do with the colors. We're going to go through it. I'm going to put that down to two just so we can see El Rapido updates.
[0:16] Alright, so two colors, main color one, main color two, aptly named, and they both come with color ramps. The reason I've left these here in your shader editor, you don't ever need to touch this.
[0:29] That's all. You can if you want, but I wouldn't recommend it. Not when it's all here. You can Control Shift click if you've got Node Wrangler, of course. Click on one of the things just to check what that filter looks like.
[0:44] I'm going to make it a bit more obvious. In fact, I'm just going to turn off that for the second. Yeah, so you've got total control of the cut. I'm doing the wrong one.
[0:57] What is this? Look that. Okay, this is good. So NS Infinite Rock Builder 0.002 up here in target material. I ain't got the right one selected. So I must simply must select Rock Builder two.
[1:11] So now this is the one we're editing. Okay, so that gives you an idea of how the color has been because obviously when there's a formation, it's difficult to see what the color is doing.
[1:24] And then this main out, just Control Shift, click that. Excuse the plane. It's terrible because the sub divs off. Really bad.
[1:34] There's too much detail for a low thing. So I'm just going to wait. Is this just one formation? What have I done? Oh, that's why. Let's just go back to this for now.
[1:47] And this is I don't want one. Okay, so now we can clearly see the color. And that's the filter for that. You've also got main color two. And this one you can see it's not not being displayed because this.
[2:06] Oh, I didn't mention the filter. Sorry. Main color has a filter as well. So you can play with how that displays if you want it bitty or, you know, little dusty bits like that. That filters there.
[2:18] And main color two has its filter underneath. Color one two mix is what you use to get to see this one. This is set up for screen because there's a black, which means the black gets ignored.
[2:31] Only this. So if I put that to say a yellow and then under mix it's set to screen. And then once I slide that in, I get my little yellow patches. And again, main color two filter. So you can make that as large or as small as you like.
[2:49] And you can again Control Shift, click that just to have a butchers at us working and then Control Shift, click that to come back.
[2:58] So we've mixed both. You could just have main color two, but I wouldn't. What's the point? You can do the same thing with main color one.
[3:07] So yeah, you've got the filters color one two mix. OK, and Mars Snow. I'm undecided about this. It doesn't depending on your shape. It can do strange things.
[3:19] So must. Yes, good. Right. Must print out. That's in dust. We don't need to deal with that.
[3:26] Disp color. So this matches the displacement. So this color mix. If I slide that in. If you look, Control Shift, click.
[3:37] It's attempting to follow the displacement, whether it almost like an ambient occlusion type thing.
[3:47] You see. So the more I add the darker that gets, I think it backs on my own ads.
[3:53] And that just a bit more authentic, you know, as the outer edges have been weathered.
[3:59] So on the inner bits, a little bit dark and a little bit dirty.
[4:03] That's this color and this color mix. That I believe is, yeah, that's all the colors. That's everything done.
[4:13] Wicked. That was quicker than I thought. We should move on to filters.



---

## Captured Frames

- [0:16] tutorials/frames/ns-infinite-rock-builder-guide---colours/frame_000.jpg
- [0:57] tutorials/frames/ns-infinite-rock-builder-guide---colours/frame_001.jpg
- [1:24] tutorials/frames/ns-infinite-rock-builder-guide---colours/frame_002.jpg
- [1:47] tutorials/frames/ns-infinite-rock-builder-guide---colours/frame_003.jpg
- [2:31] tutorials/frames/ns-infinite-rock-builder-guide---colours/frame_004.jpg
- [3:26] tutorials/frames/ns-infinite-rock-builder-guide---colours/frame_005.jpg

---

## Structured Notes

### Core Technique
Coloring a rock built with the **Infinite Rock Builder** add-on (Nick Sayce / NS) using the add-on's pre-wired Shader Editor node group inputs — two main colors (each with its own color ramp + noise filter) mixed together, plus a displacement-following color and a moss/snow mask — without ever needing to build shader nodes from scratch.

**Add-on disclosure:** All group inputs referenced here (Colour 1, Colour 2, Colour 1-2 Mix, Disp Colour, Moss/Snow, Dust Shape, Main Out) belong to the add-on's custom "NS Infinite Rock Builder" node group in the Shading workspace, not stock Blender shader nodes. Treat this as add-on-specific UI, distinct from a hand-built Principled BSDF graph.

### Summary
Part of the NS Infinite Rock Builder Guide series — covers Colours; see also Main Controls, Filters, Moss/Fresnel/Dust, Water Level Roughness, Cliff-top Flatten/Bump. With the rock's material node group selected in the Shading workspace (must pick the correct numbered material instance, e.g. "Rock Builder 2", since each rock/plane can carry its own), the viewer is shown the "Colour 1" and "Colour 2" group inputs, each driven by a Color Ramp and each with its own noise-based Filter controlling how bitty/dusty the color patches look. Ctrl+Shift-click (Node Wrangler) on any node previews just that node's output in the viewport. Colour 1 and Colour 2 are combined via a "Colour 1-2 Mix" node set to Screen blending (so black areas are ignored/transparent), letting Colour 2 appear as small tinted patches over the Colour 1 base. A separate "Disp Colour" mix follows the geometry's displacement/AO-like intensity, darkening recesses for a weathered, dirtied look at the rock's inner crevices. "Moss/Snow" and "Dust Shape" inputs exist but are only briefly acknowledged as further optional color layers, not deep-dived in this video.

### Key Steps
1. Reduce viewport Subdivisions temporarily (e.g. to 2) for faster live updates while tweaking colors.
2. Switch to the Shading workspace and select the rock object; confirm the correct material is targeted in the shader editor header (e.g. "NS Infinite Rock Builder 0.002" / "Rock Builder 2") — an easy mistake is editing the wrong numbered instance when multiple rocks/materials exist in the scene.
3. Locate the add-on's node group inputs: "Main Colour 1" and "Main Colour 2," each wired through its own Color Ramp — these do not need to be touched/rewired, just their ramp colors edited.
4. With Node Wrangler installed, Ctrl+Shift-click any node to preview that node's output alone in the viewport; Ctrl+Shift-click "Main Out" again to return to the full shaded result.
5. Each main color also has a "Filter" input (a noise-driven mask) that controls how large/small and how bitty/dusty that color's patches appear on the surface.
6. The two colors are combined by a "Colour 1-2 Mix" node — set to Screen blend mode so black in the mask is ignored, letting only the masked (non-black) areas of Colour 2 tint over Colour 1; drag the mix factor in to reveal small patches of the second color.
7. Set Colour 2 to a contrasting color (e.g. yellow) to clearly see the Screen-mix patches appear as the mix slider increases.
8. Use "Disp Colour" to blend in a color that follows the rock's own displacement pattern — functions like a built-in ambient-occlusion/dirt pass, darkening the inward/recessed areas of the rock as the mix increases, adding a naturally weathered, grimier look to inner crevices vs. outer (presumably more exposed/eroded) edges.
9. Repeat the same Ctrl+Shift-click node-preview trick to check any individual color/filter/mix stage in isolation before committing to a final blend.

### Nodes / Settings
- Add-on's Shading workspace node group inputs: Main Colour 1, Main Colour 2 (each with a Color Ramp + Filter/noise input), Colour 1-2 Mix (Screen blend mode), Disp Colour, Moss/Snow, Dust Shape, Main Out
- N-panel sidebar sections visible alongside Colours: Filters, Moss / Fresnel / Dust, Water Level Roughness, Cliff Top Flatten, Bump
- Workflow tool: Node Wrangler add-on, Ctrl+Shift+Click for single-node viewport preview

### Difficulty
Beginner (purely adjusting pre-built color ramps/mix factors/filters — no node authoring)

### Blender Version
Not stated explicitly by the narrator; not independently confirmed from these frames (see Main Controls video for the title-bar reading of "Blender 4.x").

### Tags
materials, shaders, procedural, organic, beginner, blender-4x

---

## Related Tutorials
Part of the **NS Infinite Rock Builder Guide** series (Nick Sayce / NS add-on) — all 6 parts cross-link regardless of tag overlap since they form one continuous guide:
- [Main Controls](ns-infinite-rock-builder-guide---main-controls.md)
- [Filters](ns-infinite-rock-builder-guide---filters.md)
- [Moss / Fresnel / Dust](ns-infinite-rock-builder-guide---moss-fresnel-dust.md)
- [Water Level Roughness](ns-infinite-rock-builder-guide---water-level-roughness.md)
- [Cliff-top Flatten / Bump](ns-infinite-rock-builder-guide---cliff-top-flatten-bump.md)
