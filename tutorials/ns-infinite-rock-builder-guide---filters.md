---
title: NS Infinite Rock Builder Guide - Filters
source: YouTube
url: https://www.youtube.com/watch?v=yLhymD__KvI
author: Nick Sayce
ingested: 2026-08-12
blender_version: "4.x (see Main Controls video for title-bar reading; not independently confirmed here)"
tags: [geometry-nodes, procedural, displacement, organic, intermediate, blender-4x]
extraction_status: complete
frames_dir: tutorials/frames/ns-infinite-rock-builder-guide---filters/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Infinite Rock Builder Guide - Filters

**Source:** [YouTube](https://www.youtube.com/watch?v=yLhymD__KvI)
**Author:** Nick Sayce
**Duration:** 3m37s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Here we are, filters. There's a bit to talk about with these. So obviously the color filters are with the colors, that made more sense.
[0:13] But this is for all of the formations. Like I showed you, inside this group, there's 25 individual groups, each with all their own settings that you used to have to go in and do like this.
[0:25] You don't need to do that, no, I'm always all over it. So whatever formations are added, it's same formation one, I'm not quite sure.
[0:35] Let me delete, I'm just going to remove that and then add formation one back to that. It's coming in for some reason, I need to double check what's going on here.
[0:48] But it seems to be loading formation 16. It's kept, right, that's something I'm going to look into, don't worry.
[0:55] Okay, so we're back to formation one and I'm going to turn off the displacement color. I would like it just normal. There we go.
[1:07] And I'm also going to make that filter not so dark. That's better. Okay. So filters, whatever formation you add, it will appear in the formation list.
[1:21] We've only got formation one at the moment. So if I added formation 24, add formation 24. Now I have it in the filters list.
[1:32] And this is, as you see, displacement control, shape ramp, shape filter. The shape ramp is a color ramp, black and white.
[1:40] I might actually make that a color ramp. But you've got total control of the shapes of everything. Let me put that down to three just for speedier updates.
[1:52] And depending what you change, you know, it's never, am I selecting the right thing here? I'm on formation one.
[2:00] Let's try that again. Okay. So yeah, now I'll always do shift click rather than just clicking.
[2:10] But yeah, you can, as you can see, wildly edit the shape. If I turned under my formation 24 and just drop the mix, I have because I did the X scale on the wrong one.
[2:25] So now if I go back to formation one, I can fix what I did here, which that should be one. And now you can edit.
[2:34] And as I say, each, each part of the filter, if you go too far, obviously it becomes quite clear. It's just a mess.
[2:39] So these are never intended to be massive. You know, this is the shape I like. I'd like this to be if I was to make a big shape, this would cover the whole shape because I like this.
[2:50] It looks like the cliff face I want. There's an if a tree was tiny and was here. That's what I'm looking at.
[2:56] So I'd never go too far with with any of this mostly slight adjustments. But as you can see, there's a ton of control of every facet of every single formation, whichever one you're adding or whatever.
[3:13] So I'm going to just make 24 will do add and bring it in. That's better.
[3:21] Okay, so again, real quick, real simple. Use the filters, the whichever filter, whichever formations you've got will appear in the formation list.
[3:30] And the more you add, the more will appear cold filters done.



---

## Captured Frames

- [0:13] tutorials/frames/ns-infinite-rock-builder-guide---filters/frame_000.jpg
- [1:07] tutorials/frames/ns-infinite-rock-builder-guide---filters/frame_001.jpg
- [1:32] tutorials/frames/ns-infinite-rock-builder-guide---filters/frame_002.jpg
- [2:10] tutorials/frames/ns-infinite-rock-builder-guide---filters/frame_003.jpg
- [2:50] tutorials/frames/ns-infinite-rock-builder-guide---filters/frame_004.jpg
- [3:13] tutorials/frames/ns-infinite-rock-builder-guide---filters/frame_005.jpg

---

## Structured Notes

### Core Technique
Reshaping each individual rock "formation" inside the **Infinite Rock Builder** add-on (Nick Sayce / NS) using its per-formation Filters — a Displacement Control, Shape Ramp (color ramp), and Shape Filter (noise) — that appear dynamically in a Filters list for every formation currently added to the chain.

**Add-on disclosure:** "Displacement Control," "Shape Ramp," and "Shape Filter" are custom exposed inputs of the add-on's internal per-formation node groups (25 of them, bundled inside the main node group), not generic Blender geometry-node primitives — this video is teaching add-on UI, not stock GeoNodes.

### Summary
Part of the NS Infinite Rock Builder Guide series — covers Filters; see also Main Controls, Colours, Moss/Fresnel/Dust, Water Level Roughness, Cliff-top Flatten/Bump. Unlike the color filters (covered in the Colours video), these Filters apply to the shape/displacement of each formation. Any formation currently added to the object automatically appears as its own entry in the sidebar's Filters list; each entry exposes Displacement Control, a Shape Ramp (black-and-white color ramp controlling the displacement gradient), and a Shape Filter (a noise-based mask controlling where/how much of that displacement shows). The presenter demonstrates on Formation 1 (base) and Formation 24, editing scale/detail values to wildly distort the rock shape, then dialing values back to a restrained, natural-looking cliff-face silhouette — stressing that these controls are powerful but should be used with light, subtle adjustments rather than extreme values, and that it's easy to accidentally edit the wrong formation's filter (recommends Shift-click to select formations deliberately) when several are stacked.

### Key Steps
1. Understand the two filter types are separate: color filters (from the Colours video) control tint/patchiness of Main Colour 1/2; shape filters (this video) control the displacement/geometry of each formation.
2. Add or remove formations as needed (e.g. delete Formation 1, re-add "Add Formation 1") — whichever formations are present automatically populate the Filters list below in the sidebar.
3. Select a formation carefully: with multiple formations stacked, be deliberate (Shift-click) about which formation's filter row you're editing, since editing the wrong one produces confusing/unexpected results.
4. Open a formation's Filters row to reveal: Displacement Control, Shape Ramp (a black/white color ramp — presenter notes it could be converted to full color for finer control), and Shape Filter (a noise texture driving where displacement is stronger/weaker).
5. Lower viewport Subdivisions (e.g. to 3) while iterating for faster feedback.
6. Adjust Shape Filter scale/detail values to reshape the formation's displacement pattern — pushing values far produces chaotic, "messy" results; the presenter recommends keeping adjustments slight/subtle unless an extreme look is intentional.
7. Combine a tuned formation (e.g. Formation 24) back with the base (Formation 1) via Add Formation to get a refined, natural cliff-face-like silhouette.
8. Remember: every formation added to the chain gets its own Filters entry — the more formations stacked, the more filter rows appear to manage.

### Nodes / Settings
- Sidebar "Filters" list — one entry auto-generated per active formation
- Per-formation filter inputs: Displacement Control, Shape Ramp (Color Ramp, black/white), Shape Filter (noise texture: Scale, Detail, Roughness-style parameters)
- Distinct from the Colours video's color-specific filters (Main Colour 1/2 Filter)
- 25 total formation groups bundled inside the main "NS Infinite Rock Builder" node group, each with independent filter controls

### Difficulty
Intermediate (easy to select the wrong formation or push values too far; requires restraint and formation-management awareness)

### Blender Version
Not stated explicitly by the narrator; not independently confirmed from these frames (see Main Controls video for the title-bar reading of "Blender 4.x").

### Tags
geometry-nodes, procedural, displacement, organic, intermediate, blender-4x

---

## Related Tutorials
Part of the **NS Infinite Rock Builder Guide** series (Nick Sayce / NS add-on) — all 6 parts cross-link regardless of tag overlap since they form one continuous guide:
- [Main Controls](ns-infinite-rock-builder-guide---main-controls.md)
- [Colours](ns-infinite-rock-builder-guide---colours.md)
- [Moss / Fresnel / Dust](ns-infinite-rock-builder-guide---moss-fresnel-dust.md)
- [Water Level Roughness](ns-infinite-rock-builder-guide---water-level-roughness.md)
- [Cliff-top Flatten / Bump](ns-infinite-rock-builder-guide---cliff-top-flatten-bump.md)
