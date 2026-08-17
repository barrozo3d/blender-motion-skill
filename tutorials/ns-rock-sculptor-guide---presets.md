---
title: NS Rock Sculptor Guide - Presets
source: YouTube
url: https://www.youtube.com/watch?v=XbdMfva0fPA
author: Nick Sayce
ingested: 2026-08-17
blender_version: "5.1.x (approximate, viewport title bar in captured frames; not stated verbally)"
tags: [procedural, displacement, organic, product-viz, beginner]
extraction_status: complete
frames_dir: tutorials/frames/ns-rock-sculptor-guide---presets/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Rock Sculptor Guide - Presets

**Source:** [YouTube](https://www.youtube.com/watch?v=XbdMfva0fPA)
**Author:** Nick Sayce
**Duration:** 2m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Alright, welcome to another guide video for another Radon. I just done called the NS Rock Sculptor,
[0:12] which does exactly what it says on the tin, it sculpts rocks and the procedural material
[0:18] that comes with it makes it look more rocky. And I'm just going to go through these each
[0:24] bit one by one and I'll timestamp the lot so you can just bump, I'll jump to the bits
[0:30] you need and I'll try and keep the order and I shall start with the presets because that
[0:38] will make sense in a minute. So presets, click that and there's all your presets as 32. There
[0:44] might be more if I make more. But this is what you've got so far and all you've got to do
[0:49] is pick one and then click load select preset and that will come with the
[0:57] version of the rock sculptor that I've already fiddled with and any displacement modifiers that
[1:04] come with it and this one does come with a displaced modifier. So yeah, it's real quick,
[1:11] really easy to bring in anything, any old, any one of the rocks, some of them are just, you know,
[1:17] just easy, easy to mess with shapes, some of them are a bit more detailed than others.
[1:24] But overall, you've got 32 to pick from. And the good thing is that once you pick a rock,
[1:32] you could just use it or you can carry on editing it. So this is where this is important,
[1:39] the active material. So the reason being, if you've got more than one version of the rock
[1:45] sculptor in the scene, so let's say I plopped in now, let's put in rock 17. So I've now got two
[1:53] versions of the same material, got rock 17 and rock 21. If I was looking at rock 17, and I wanted to
[2:04] mess around with the colors and the displacement and everything at the moment, because it's active
[2:10] material is rock 17, I can change anything about this rock, and it's only going to affect this rock.
[2:17] If I wanted to go back and relook at this one and change that some more, this is no longer
[2:23] connected because it still is rock 17. So you just pick rock 21, which that one is. And now,
[2:29] if I make changes to this one, excuse me, there you go. So the presets are just the base shapes
[2:37] really, a kind of style, you can just keep messing around with a shape, you've loaded up and make it
[2:44] your own. You can even if you want to sculpt it some more, but we're going to get to sculpting next.
[2:53] Yeah, that's it. So the presets will move on to this one, sculpt settings.



---

## Captured Frames

- [0:38] tutorials/frames/ns-rock-sculptor-guide---presets/frame_000.jpg
- [0:49] tutorials/frames/ns-rock-sculptor-guide---presets/frame_001.jpg
- [1:53] tutorials/frames/ns-rock-sculptor-guide---presets/frame_002.jpg
- [2:10] tutorials/frames/ns-rock-sculptor-guide---presets/frame_003.jpg
- [2:29] tutorials/frames/ns-rock-sculptor-guide---presets/frame_004.jpg

---

> **Third-party add-on note:** This tutorial covers the **Presets** tab of **NS Rock Sculptor**, a paid third-party Blender add-on by Nick Sayce (NS) — and doubles as the series' own intro video (the presenter explicitly opens the whole guide series here before working through the other tabs one by one). "Load Selected Preset" and the 32-thumbnail preset grid are add-on-provided, not stock Blender.

## Structured Notes

### Core Technique
A thumbnail grid of 32 (at time of recording) pre-authored rock presets — each bundling a specific Rock Sculptor mesh/material state plus any Displace modifier it was built with — that can be dropped into the scene via "Load Selected Preset" as a one-click starting point, then freely continued/edited using the rest of the add-on's tabs.

### Summary
This episode functions as the series' own introduction: the presenter explains NS Rock Sculptor procedurally sculpts rocks and ships a matching procedural material, then walks through starting with Presets specifically because "it'll make sense in a minute" — i.e. it's the natural entry point before the other, more granular tabs. Selecting a thumbnail from the 32-preset grid and clicking "Load Selected Preset" instantiates that preset's full saved state: mesh shape, material, and any Displace modifier it was authored with (confirmed in-frame via a "Rock Displace" modifier already present on the loaded object). Some presets are simple/easy starting shapes, others carry more built-in detail. The key conceptual point covered is **active material isolation**: loading two different presets (demoed as "Rock 17" and "Rock 21") into the same scene creates two independent Rock Sculptor material instances — each object keeps its own separate material data, so editing color/displacement/etc. on whichever object is currently selected/active only affects that one object, not the other, even though both originated from the same add-on. This sets up the rest of the series: presets are just starting shapes/styles, meant to be sculpted and refined further using the tabs covered next (starting with Sculpt Settings).

### Key Steps
1. Open the "Presets" section in the NS Rock Sculptor sidebar tab.
2. Browse the thumbnail grid (32 presets shown, labeled "Rock 1" through "Rock 32"-ish, more may be added over time) — each thumbnail is a small rendered preview of that preset's rock.
3. Click a thumbnail to select it, then click "Load Selected Preset" to instantiate it in the scene — this brings in the preset's mesh shape, its full material setup, and any Displace modifier it was originally built with.
4. Load a second (different) preset into the same scene if desired — each loaded preset creates its own independent object with its own independent material data (not a shared/linked instance), even though all presets come from the same add-on.
5. Understand "active material" scoping: whichever object is currently selected/active in the scene is the one that further edits (color, displacement, filters, etc. from other tabs) will apply to — switching selection to a different loaded preset switches which object's material you're now editing, and changes do not cross-contaminate between separately-loaded presets.
6. Treat presets as a starting point, not a final result — continue refining a loaded preset's shape using the Sculpt Settings tab (covered next in the series) or any other tab (Colour, Filters, Displacement, etc.) exactly as if you'd built the rock from scratch.

### Nodes / Settings
- Sidebar section "Presets" (referenced as the natural starting point of the whole add-on/series; sits alongside Sculpt Settings, Weight Paint, Edge Crease, Colour, Moss, Filters, Colour Ramps, Displacement, Bump, Geometry, Scatter)
- 32-thumbnail preset grid (labeled Rock 1-32+) + "Load Selected Preset" button
- Each preset bundles: mesh/sculpt state, full material (Colour/Filters/Colour Ramps setup), and (for at least some presets) a pre-configured "Rock Displace" modifier
- Confirmed in outliner/modifier-stack frames: independently-named objects ("Rock 17," "Rock 21") each carrying their own separate material data-block after loading multiple presets

### Difficulty
Beginner (browsing a thumbnail grid and clicking one button; the active-material concept requires understanding but no technical skill)

### Blender Version
5.1.x (approximate, viewport title bar in captured frames; not stated verbally) — consistent with other NS Rock Sculptor Guide episodes from this same upload batch (2026-07-30/31).

### Tags
procedural, displacement, organic, product-viz, beginner

---

## Related Tutorials
Part of the **NS Rock Sculptor Guide** series (10 episodes, all uploaded 2026-07-30) covering the NS Rock Sculptor add-on tab by tab. This episode doubles as the series intro and is the natural first stop; the presenter's own "next" topic is Sculpt Settings. **This completes all 10 episodes of the NS Rock Sculptor Guide series.**
- [NS Rock Sculptor Guide - Sculpt Settings](ns-rock-sculptor-guide-sculpt-settings.md) — same add-on/series, Sculpt Settings tab (directly relevant — presenter's own forward-reference; this is how a loaded preset gets further sculpted/refined).
- [NS Rock Sculptor Guide - Geometry & Scatter](ns-rock-sculptor-guide---geometry-scatter.md) — same add-on/series, Geometry & Scatter tabs.
- [NS Rock Sculptor Guide - Colour](ns-rock-sculptor-guide---colour.md) — same add-on/series, Colour tab (directly relevant — the active-material-isolation concept demoed here with presets is the same mechanism covered there with color edits).
- [NS Rock Sculptor Guide - Displacement](ns-rock-sculptor-guide---displacement.md) — same add-on/series, Displacement tab (directly relevant — some presets ship with a pre-built Rock Displace modifier, as covered there in depth).
- [NS Infinite Rock Builder Guide - Main Controls](ns-infinite-rock-builder-guide---main-controls.md) — conceptual sibling: same author's other add-on, also built around numbered preset "formations" that can be loaded and further customized, different tool/UI.
