---
title: NS Rock Sculptor Guide - Filters
source: YouTube
url: https://www.youtube.com/watch?v=9jrj0IG7Xe8
author: Nick Sayce
ingested: 2026-08-17
blender_version: "5.1.x (approximate, viewport title bar in captured frames; not stated verbally)"
tags: [procedural, displacement, organic, product-viz, beginner]
extraction_status: complete
frames_dir: tutorials/frames/ns-rock-sculptor-guide---filters/
frame_count: 4
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Rock Sculptor Guide - Filters

**Source:** [YouTube](https://www.youtube.com/watch?v=9jrj0IG7Xe8)
**Author:** Nick Sayce
**Duration:** 1m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- WARNING: Thin transcript: 871 chars. Notes may be shallow — consider --whisper-model small.

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] There's a lot of filters, and I've put them on the dropdown list.
[0:07] Pretty much everything you think you need to edit, you can edit in here.
[0:11] So there's a bump, the bump filter,
[0:12] There's a crack bump, displacement, displacement mask.
[0:17] There's a whole bunch of filters in there, you just pick it from the list as and when
[0:21] you need it, and there's all your bits and bobs.
[0:24] whatever filter it's attached to, you can edit all of these.
[0:29] So if I just very quickly put some bump on,
[0:31] let's just do the dusty bump because that's very clear.
[0:37] So if I choose dusty bump filter, now I've got control of all of that.
[0:46] So yeah, as I say, if you think, oh man, I wish I could edit the filter,
[0:50] have a look in the filters, it's probably in there.
[0:52] And if you're thinking, oh man, I wish I could edit the color ramp, that's next.
[0:57] Yeah, filter is pretty simple. All right, so wait, color ramps next.



---

## Captured Frames

- [0:07] tutorials/frames/ns-rock-sculptor-guide---filters/frame_000.jpg
- [0:17] tutorials/frames/ns-rock-sculptor-guide---filters/frame_001.jpg
- [0:37] tutorials/frames/ns-rock-sculptor-guide---filters/frame_002.jpg
- [0:46] tutorials/frames/ns-rock-sculptor-guide---filters/frame_003.jpg

---

> **Third-party add-on note:** This tutorial covers the **Filters** tab of **NS Rock Sculptor**, a paid third-party Blender add-on by Nick Sayce (NS). The "Choose a Filter to Edit" dropdown and every filter listed in it (Roll, Main Colour, Bump variants, Displacement, Displacement Mask) are the add-on's own exposed parameter groups, not stock Blender nodes.

## Structured Notes

### Core Technique
A single "Choose a Filter to Edit" dropdown in the sidebar exposes editable parameters for every filter/effect layer the add-on offers — bump variants, displacement, displacement mask, and color — so the user doesn't need to hunt through separate panels for each one.

### Summary
Very short overview video: rather than each effect (bump, cracks, displacement, color) living in its own separate sidebar section, NS Rock Sculptor centralizes them behind one "Choose a Filter to Edit" dropdown list. The presenter opens the list — showing entries including a Main Colour Filter, several Bump variants (Grain Bump, Cracks Bump, Cracks Bump 2, Dusty Bump), Displacement Filter, and Displacement Mask — and picks "Dusty Bump Filter" as a clear example, revealing its own parameter set (Scale, Seed, Weight, Distortion) plus a Displacement group below it (Strength, Distance, Cracks Bump Amount, Cracks Bump Amount 2, Custom Bump 2 Amount). The takeaway is purely navigational: whatever effect the user wants to tweak, it's very likely reachable through this one dropdown rather than scattered across tabs. Closes by forward-referencing the Colour Ramps tab as the next logical place to look if a filter's underlying ramp needs editing.

### Key Steps
1. Open the "Filters" section in the NS Rock Sculptor sidebar tab.
2. Click "Choose a Filter to Edit" to open the dropdown — it lists every filter/effect layer the add-on exposes (seen in frames: Roll Filter, Main Colour Filter, Grain Bump Filter, Cracks Bump Filter, Cracks Bump 2 Filter, Dusty Bump Filter, Displacement Filter, Displacement Mask, among others).
3. Select an entry (e.g. "Dusty Bump Filter") to reveal its own dedicated parameter block below the dropdown: Scale, Seed, Weight, Distortion.
4. Below the selected filter's own parameters, a further "Displacement" group is shown with Strength, Distance, Cracks Bump Amount, Cracks Bump Amount 2, and Custom Bump 2 Amount fields — these interact with/layer on top of whichever bump filter is active.
5. General workflow rule: if a desired control isn't obviously visible elsewhere in the add-on's panel, check this Filters dropdown first — most per-effect parameters live here.
6. If the underlying color/gradient of a filter needs editing rather than its strength/scale, that's handled in the separate Colour Ramps tab (covered in its own video).

### Nodes / Settings
- Sidebar section "Filters" → "Choose a Filter to Edit" dropdown (centralized filter-parameter picker)
- Filters observed in the dropdown list: Roll Filter, Main Colour Filter, Grain Bump Filter, Cracks Bump Filter, Cracks Bump 2 Filter, Dusty Bump Filter, Displacement Filter, Displacement Mask
- Dusty Bump Filter's own parameters: Scale, Seed, Weight, Distortion
- Adjacent Displacement group parameters shown alongside a selected bump filter: Strength, Distance, Cracks Bump Amount, Cracks Bump Amount 2, Custom Bump 2 Amount

### Difficulty
Beginner (purely a UI-navigation overview — no node authoring, just locating existing sliders)

### Blender Version
5.1.x (approximate, viewport title bar in captured frames; not stated verbally) — consistent with other NS Rock Sculptor Guide episodes from this same upload batch (2026-07-30/31).

### Tags
procedural, displacement, organic, product-viz, beginner

---

## Related Tutorials
Part of the **NS Rock Sculptor Guide** series (10 episodes, all uploaded 2026-07-30) covering the NS Rock Sculptor add-on tab by tab. This episode is a navigational overview of the Filters dropdown; the presenter's own "next" topic is Colour Ramps.
- [NS Rock Sculptor Guide - Colour Ramps](ns-rock-sculptor-guide---colour-ramps.md) — same add-on/series, Colour Ramps tab (directly relevant — presenter's own forward-reference; ramps referenced here are edited there).
- [NS Rock Sculptor Guide - Displacement](ns-rock-sculptor-guide---displacement.md) — same add-on/series, Displacement tab (directly relevant — this episode's "Displacement Filter"/"Displacement Mask" entries and Cracks Bump Amount fields are the same controls covered in depth there).
- [NS Rock Sculptor Guide - Bump](ns-rock-sculptor-guide-bump.md) — same add-on/series, Bump tab (directly relevant — the Dusty Bump/Cracks Bump filters demoed here are the same bump channels covered in depth there).
- [NS Rock Sculptor Guide - Geometry & Scatter](ns-rock-sculptor-guide---geometry-scatter.md) — same add-on/series, Geometry & Scatter tabs.
