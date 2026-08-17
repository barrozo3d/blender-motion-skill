---
title: NS Infinite Rock Builder Guide - Water Level Roughness
source: YouTube
url: https://www.youtube.com/watch?v=8ZX5DsV7eBc
author: Nick Sayce
ingested: 2026-08-12
blender_version: "4.x (see Main Controls video for title-bar reading; not independently confirmed here)"
tags: [materials, shaders, procedural, organic, beginner, blender-4x]
extraction_status: complete
frames_dir: tutorials/frames/ns-infinite-rock-builder-guide---water-level-roughness/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Infinite Rock Builder Guide - Water Level Roughness

**Source:** [YouTube](https://www.youtube.com/watch?v=8ZX5DsV7eBc)
**Author:** Nick Sayce
**Duration:** 2m11s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 177 chars (min 500). Captions unavailable or audio silent — extraction will be poor.

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Water Level Roughness
[1:00] Depending on the height of the water, the color matches the color of the water.
[1:24] If it was in a 3D shape, I would switch to 3D.
[1:32] The softness is contrasting.



---

## Captured Frames

- [0:10] tutorials/frames/ns-infinite-rock-builder-guide---water-level-roughness/frame_000.jpg
- [0:30] tutorials/frames/ns-infinite-rock-builder-guide---water-level-roughness/frame_001.jpg
- [1:00] tutorials/frames/ns-infinite-rock-builder-guide---water-level-roughness/frame_002.jpg
- [1:15] tutorials/frames/ns-infinite-rock-builder-guide---water-level-roughness/frame_003.jpg
- [1:32] tutorials/frames/ns-infinite-rock-builder-guide---water-level-roughness/frame_004.jpg
- [1:50] tutorials/frames/ns-infinite-rock-builder-guide---water-level-roughness/frame_005.jpg

---

## Structured Notes

### Core Technique
Adding a procedural water-line to a rock built with the **Infinite Rock Builder** add-on (Nick Sayce / NS): a "Water Level / Roughness" sidebar section that colors the rock below a set height with a water tint and controls how rough/soft that waterline transition looks.

**Add-on disclosure:** "Water Level / Roughness," its height/mapping controls, and the "Water Level" / "Coral Ring" color swatches are custom inputs on the add-on's node group, not stock Blender nodes — this is add-on-specific surfacing layered on top of the base rock, consistent with the rest of this series.

**Transcription note:** This video's spoken narration was very sparse (Whisper only recovered ~4 short lines across 2m11s — flagged by the ingest pipeline's own safeguard as `needs-review` due to thin transcript), so this extraction leans more heavily on reading the captured frames' sidebar panel directly than on narration, unlike the other 5 videos in the series.

### Summary
Part of the NS Infinite Rock Builder Guide series — covers Water Level Roughness; see also Main Controls, Colours, Filters, Moss/Fresnel/Dust, Cliff-top Flatten/Bump. This short video demos the "Water Level / Roughness" sidebar section: a numeric height value (with separate UV-space and 3D-space height fields, plus an Object/UV Mapping toggle and a 2D/3D switch — "if it was in a 3D shape, I would switch to 3D") sets how far up the rock the waterline sits, and a Roughness/softness value controls how sharp vs. blurred/blended that waterline transition edge looks. The color of the flooded area is set by two swatches — "Water Level" (a teal/green color shown in the demo) and "Coral Ring" (a lighter/white accent shown near the waterline, presumably for a foam- or coral-like highlight band right at the surface). Across the captured frames the waterline visibly changes height and the transition edge changes from a hard, evenly cut line to a softer, patchier blended edge as the roughness value is adjusted, and the water color additionally seems to interact with the underlying formation displacement/roughness so the flooded band isn't perfectly flat.

### Key Steps
1. Open the "Water Level / Roughness" section in the sidebar, below Moss/Fresnel/Dust and above Cliff Top Flatten.
2. Set the height field that determines how far up the rock the water line sits — the video shows both a UV-space height and a 3D-space height field, with an "Object/UV Mapping" checkbox and a 2D/3D switch to pick which one drives the effect (use 3D height when working on a true 3D shape rather than the flat plane).
3. Adjust the Roughness/softness value to control how hard-edged or blended/patchy the transition between dry rock and the water-tinted band appears.
4. Set the "Water Level" color swatch (demoed as a teal/green) for the submerged portion of the rock — the video notes the tint reflects "the color of the water."
5. Set the secondary "Coral Ring" color swatch (demoed as near-white) for an accent band at/near the waterline.
6. Because the water color is masked by the rock's own displacement, the flooded band isn't a perfectly flat cutoff — it follows the rock's surface detail for a more natural shoreline look.

### Nodes / Settings
- Sidebar section: "Water Level / Roughness" (between Moss/Fresnel/Dust and Cliff Top Flatten)
- Fields observed in the panel: a roughness/softness value, an "Object (UV) Mapping" checkbox, a "2D / 3D" switch, UV-space height and 3D-space height numeric fields, a strength-like field
- Color swatches: "Water Level" (teal/green in the demo), "Coral Ring" (near-white in the demo)

### Difficulty
Beginner (a handful of sliders/color swatches; no node authoring)

### Blender Version
Not stated explicitly by the narrator (very little narration in this video); not independently confirmed from these frames (see Main Controls video for the title-bar reading of "Blender 4.x").

### Tags
materials, shaders, procedural, organic, beginner, blender-4x

---

## Related Tutorials
Part of the **NS Infinite Rock Builder Guide** series (Nick Sayce / NS add-on) — all 6 parts cross-link regardless of tag overlap since they form one continuous guide:
- [Main Controls](ns-infinite-rock-builder-guide---main-controls.md)
- [Colours](ns-infinite-rock-builder-guide---colours.md)
- [Filters](ns-infinite-rock-builder-guide---filters.md)
- [Moss / Fresnel / Dust](ns-infinite-rock-builder-guide---moss-fresnel-dust.md)
- [Cliff-top Flatten / Bump](ns-infinite-rock-builder-guide---cliff-top-flatten-bump.md)
