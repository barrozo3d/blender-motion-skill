---
title: NS Infinite Rock Builder Guide - Cliff-top Flatten / Bump
source: YouTube
url: https://www.youtube.com/watch?v=VwaeyQtmgw8
author: Nick Sayce
ingested: 2026-08-12
blender_version: "Blender 5.1.2 -- observed in frame_000"
tags: [geometry-nodes, procedural, displacement, organic, intermediate, blender-4x]
extraction_status: complete
frames_dir: tutorials/frames/ns-infinite-rock-builder-guide---cliff-top-flatten-bump/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Infinite Rock Builder Guide - Cliff-top Flatten / Bump

**Source:** [YouTube](https://www.youtube.com/watch?v=VwaeyQtmgw8)
**Author:** Nick Sayce
**Duration:** 4m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Clif Top Flatten
[0:30] Shift-click, left goes up, right goes down, set how much rounding off
[0:46] Put grass and stuff, object UV, bump, zero bump, reclose,
[1:14] standard bump, bump one and this is bump one
[1:30] and you can check exactly what it's doing by control shift, don't worry about that, it's because I've hidden that.
[1:38] Bump out, oh yeah I forgot I should have mentioned that but it's pretty clear where the height of the cliff Latin is,
[1:43] so if you control shift click bump out you can see what bump is coming through.
[1:49] So this is bump one, if I then slide in bump two you get that one, if I slide in bump three you get that one
[1:58] and you can have all three if you like, just you know, there you go, that's all three bumps.
[2:06] It's pretty tough to tell once it's on the rock but if I control shift click it's there, I can assure you.
[2:16] Okay, strength and distance, if you put it up to two I always do this sometimes and it goes very black
[2:23] but don't worry this time. I'm just trying to think if there's anything else that I need to explain,
[2:33] I've already built a rock thing, yeah so just remember that when build, if you're making a scene and you need a cliff face,
[2:42] obviously you're not going to use, well you could just use one plane but you see it would be tiny, you can scale it up I guess,
[2:49] but build it on the plane first, mix all your formations, get your colours, get your bump, get everything sorted,
[2:57] then build your shape, bear in mind that if you go, as I say, this is default to UV mapping,
[3:03] once you go to object you're going to need to lower the scale straight away, certainly not at point three
[3:09] and probably lower the strength a bit, I don't know, point four or something
[3:13] and then when you take that onto your new shape, it should be the right scale, if that makes sense,
[3:21] it should make sense, it needs to make sense, but yeah that's it, that is the herb in a probably 15, 20 minute nutshell,
[3:34] I don't think there's anything else that I need to mention, if you do, if you made a bunch of, no, I'm thinking of the wrong thing,
[3:44] ignore it, we're done, maybe we should leave with a cool picture, you know, a cool shot, wicked, yeah, that's it, enjoy using it,
[3:55] it's super easy and it's super quick and it's way better than trying to sculpt this or finding images,
[4:03] because you can make as much of it as you want, love it Jabi, I've been Nick, you've been you, enjoy, I'll see you in the next one, bye.



---

## Captured Frames

- [0:30] tutorials/frames/ns-infinite-rock-builder-guide---cliff-top-flatten-bump/frame_000.jpg
- [1:14] tutorials/frames/ns-infinite-rock-builder-guide---cliff-top-flatten-bump/frame_001.jpg
- [1:49] tutorials/frames/ns-infinite-rock-builder-guide---cliff-top-flatten-bump/frame_002.jpg
- [1:58] tutorials/frames/ns-infinite-rock-builder-guide---cliff-top-flatten-bump/frame_003.jpg
- [2:16] tutorials/frames/ns-infinite-rock-builder-guide---cliff-top-flatten-bump/frame_004.jpg
- [3:44] tutorials/frames/ns-infinite-rock-builder-guide---cliff-top-flatten-bump/frame_005.jpg

---

## Structured Notes

### Core Technique
Flattening the top of a rock built with the **Infinite Rock Builder** add-on (Nick Sayce / NS) so it can hold set-dressing (grass, props) via Shift-click rounding controls, plus layering up to three independent fine-detail Bump passes on top of the base displacement — the final video in the series, closing with general build-order advice.

**Add-on disclosure:** "Cliff Top Flatten" and the "Bump 1/2/3" + "Flatten Height Check"/"Bump Out" nodes are part of the add-on's custom node group (visible directly in the Shading workspace node graph in the captured frames), not stock Blender geometry/shader nodes.

### Summary
Part of the NS Infinite Rock Builder Guide series — covers Cliff-top Flatten / Bump; see also Main Controls, Colours, Filters, Moss/Fresnel/Dust, Water Level Roughness. Cliff Top Flatten levels off the upper surface of the rock (useful for placing grass/props with Object-based UV mapping) — Shift-clicking left vs. right on its control raises or lowers the flatten height, and a separate slider sets how rounded-off the transition edge is. The video then covers Bump, a set of up to three independent fine-surface-detail bump layers (Bump 1, 2, 3) that can each be mixed in individually or stacked together; the presenter demonstrates isolating each with Ctrl+Shift-click node preview (Node Wrangler) on the "Bump Out" node to prove the detail is there even when it's subtle on the full-shaded rock, plus a Strength/Distance pair (shown at ~2) that controls how pronounced the bump is (warns it can go very dark/black if pushed too far). The video — and the series — closes with general workflow advice: always build and dial in formations, colors, and bump on the flat plane first, then transfer the setup to a custom sculpted shape; remember that switching from the default UV-based plane mapping to Object-based mapping on a custom shape requires re-lowering both Scale (e.g. to ~0.3) and Strength (e.g. ~0.4) to compensate, matching the same object-mapping scale caveat raised in the Main Controls video.

### Key Steps
1. Open "Cliff Top Flatten" in the sidebar; Shift-click the control — left raises the flatten height, right lowers it.
2. Use the accompanying rounding slider to set how soft/rounded the transition edge between the flattened top and the rest of the rock is.
3. Use a flattened top surface as a base for set-dressing (e.g. placing grass) when using Object-based UV mapping.
4. Open the "Bump" section: three independent bump layers (Bump 1, Bump 2, Bump 3) can each be mixed in on their own or combined together for compounded fine detail.
5. To verify bump detail that's hard to see on the fully shaded rock, Ctrl+Shift-click (Node Wrangler) the "Bump Out" node in the Shading workspace to preview it in isolation (shows as a grayscale "Flatten Height Check"/bump map texture).
6. Adjust Strength and Distance together to control how pronounced the bump appears on the surface; pushing Strength up (e.g. to 2) can blow out the shading to near-black — use with care.
7. Series-closing workflow advice: always build on the default flat plane first — dial in formation mix, colors, and bump there — before transferring the setup onto a custom sculpted rock shape, since it's far easier to judge and adjust all parameters on a simple, undistorted plane.
8. When moving the setup to a custom shape (Object-based mapping instead of the plane's default UV mapping), immediately re-lower both the Overall Scale (e.g. ~0.3) and Strength (e.g. ~0.4) to compensate for the mapping change, echoing the same scale/strength correction shown in the Main Controls video.

### Nodes / Settings
- Sidebar section: "Cliff Top Flatten" (Shift-click direction control + rounding amount)
- Sidebar section: "Bump" — Bump 1 / Bump 2 / Bump 3 mix-in layers, plus Strength and Distance
- Shading-workspace node group internals visible in frames: "Flatten Height Check" and "Bump Out" outputs, previewed via Node Wrangler (Ctrl+Shift+Click), feeding into "Main Out"
- General object-mapping caveat: UV (plane default) vs. Object mapping (custom shapes) requires re-scaling Overall Scale and Strength

### Difficulty
Intermediate (mostly slider adjustments, but the flatten/rounding interaction and the object-mapping scale correction require understanding the underlying mapping mode)

### Blender Version
Not stated explicitly by the narrator; not independently confirmed from these frames (see Main Controls video for the title-bar reading of "Blender 4.x").

### Tags
geometry-nodes, procedural, displacement, organic, intermediate, blender-4x

---

## Related Tutorials
Part of the **NS Infinite Rock Builder Guide** series (Nick Sayce / NS add-on) — all 6 parts cross-link regardless of tag overlap since they form one continuous guide:
- [Main Controls](ns-infinite-rock-builder-guide---main-controls.md)
- [Colours](ns-infinite-rock-builder-guide---colours.md)
- [Filters](ns-infinite-rock-builder-guide---filters.md)
- [Moss / Fresnel / Dust](ns-infinite-rock-builder-guide---moss-fresnel-dust.md)
- [Water Level Roughness](ns-infinite-rock-builder-guide---water-level-roughness.md)
