---
title: NS Rock Sculptor Guide   Bump
source: YouTube
url: https://www.youtube.com/watch?v=E9J_1VH2aPM
author: Nick Sayce
ingested: 2026-08-12
blender_version: "5.1.x (approximate, viewport title bar in captured frames; not stated verbally)"
tags: [procedural, displacement, organic, product-viz, beginner]
extraction_status: complete
frames_dir: tutorials/frames/ns-rock-sculptor-guide-bump/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Rock Sculptor Guide   Bump

**Source:** [YouTube](https://www.youtube.com/watch?v=E9J_1VH2aPM)
**Author:** Nick Sayce
**Duration:** 2m56s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] expedition and
[0:03] Alright, to really see the bump. We are going to want to turn all
[0:11] displacement off. There we go
[0:14] Alright and then
[0:18] Upload Source
[0:23] Now, to really see the bump. We are going to want to turn all glass
[0:26] bump and as usual in your filters you have standard bump filter you've got filters for
[0:32] for all the bumps so you can add this bit further if you please so that's just the standard bump
[0:38] that's on everything if you add this is cracks so just these chippy chippies if you go all the
[0:46] way to one you're only seeing the cracks it overrides the other one so if you want to see both
[0:51] just don't go full beams with the cracks and then you get both dusty bump again this one as well if
[0:59] you put that at one it actually hasn't done exactly what I expected yeah and the color ramps for dusty
[1:09] bump so I would maybe want more of that so I'm probably gonna go that's too far I just want a
[1:16] little bit more of that a little bit more than that and then a little bit more contrast so yeah
[1:22] that's just like a rough dusty bump is what I've called it as its purpose is cracks bump two one
[1:32] put that on one and then you've got these bigger cracks that that show through it's easier if we
[1:39] turn the dusty bump off so now yeah you've got these and both of these also are using a mask in
[1:48] the same way the displacement is so cracks bump mask is the same concept so if I you know I could
[1:56] control again areas of what I would like to the cracks that I would like to see and areas where
[2:03] I'd like it to bag her off and again that just gives it a bit more natural variation and the filters
[2:11] again they're in here too so standard bump cracks bump cracks bump two you could make those bigger
[2:17] cracks like this yeah and a tip which I do on the regs is I'll go strength two to really
[2:29] meet that out so if I but the dusty bump is mostly affected by that it makes it black
[2:35] but sometimes I'll do that because I really want it to look re-off I'll go two on the bump
[2:41] 1.5 to 2 just to really bring that bump out more and then you see it's incredibly detailed up close
[2:50] that is boom all right sweet let's go on to geometry and then we're nearly done



---

## Captured Frames

- [0:26] tutorials/frames/ns-rock-sculptor-guide-bump/frame_000.jpg
- [0:40] tutorials/frames/ns-rock-sculptor-guide-bump/frame_001.jpg
- [1:05] tutorials/frames/ns-rock-sculptor-guide-bump/frame_002.jpg
- [1:39] tutorials/frames/ns-rock-sculptor-guide-bump/frame_003.jpg
- [2:41] tutorials/frames/ns-rock-sculptor-guide-bump/frame_004.jpg

---

## Structured Notes

> **Third-party add-on note:** This tutorial covers the **Bump** tab of **NS Rock Sculptor**, a paid third-party Blender add-on by Nick Sayce (NS), not a stock Blender feature or Blender's built-in Bump node. The "standard bump", "cracks bump", "cracks bump 2", and "dusty bump" layers are add-on-specific procedural bump layers with their own Colour Ramps and masks — do not confuse them with core Blender shader Bump-map nodes.

### Core Technique
Layering NS Rock Sculptor's four independent bump-detail channels — standard bump, cracks bump, cracks bump 2, and dusty bump — each with its own strength/distance sliders, an optional mask, and (for dusty bump) a Colour Ramp, to build up fine surface micro-detail on top of the rock's main sculpt/displacement.

### Summary
A short walkthrough of the add-on's Bump tab with main Displacement temporarily disabled so the bump layers are clearly visible. Frame 000/001 show the base "standard bump" — a fine all-over grain visible across the whole rock surface in the panel's Bump section (Strength, Distance, Cracks Bump Amount, Dusty Bump Amount fields visible). Frame 002/003 show "dusty bump" pushed up and its Colour Ramp being edited (a colored dusty/mottled patchiness with visible ramp swatch in the panel) to dial in contrast. Frame 004 shows a zoomed-out rock with visible dark crack lines threading across the dusty texture — the "cracks bump" layer — with the panel's Cracks Bump / Bump Mask fields visible. Video ends noting each bump layer supports its own mask (same masking concept as the Displacement tab) to localize where cracks/dust appear, and a "strength 2, sometimes 1.5-2" push-it-further tip for a more weathered look.

### Key Steps
1. Temporarily disable the rock's main Displacement so the Bump layers alone are visible while tuning.
2. **Standard bump** — the base fine-grain bump applied to the whole rock; adjust Strength/Distance.
3. **Cracks bump** — adds chippy crack detail; at full strength (1.0) it overrides/hides the standard bump, so keep it below 1.0 if you want both visible simultaneously.
4. **Dusty bump** — adds a mottled dust-like bump; tune via its own Colour Ramp (author found the default ramp positions didn't match his expectation and needed nudging — more contrast, ramp stops moved closer together for a subtler dusting).
5. **Cracks bump 2** — adds a second, larger-scale crack pattern (bigger cracks than the first cracks layer); easier to judge with dusty bump temporarily switched off.
6. All bump layers (cracks bump, cracks bump 2) support a **mask** input, same concept as the Displacement tab's mask — paint/control where cracks appear vs. stay smooth, for natural variation instead of uniform coverage across the whole rock.
7. Pro tip: pushing Strength to ~1.5-2 (author says "I'll go 2 on the bump") gives a noticeably more weathered, detailed close-up look; note this mostly affects dusty bump and can push it toward solid black if overdone, so use selectively on hero/close-up rocks.

### Nodes / Settings
- **NS Rock Sculptor Bump tab fields (confirmed in frame captures):** Strength, Distance, Cracks Bump Amount, Dusty Bump Amount, Cracks Bump 2 Amount, Dusty Bump Colour Ramp, Cracks Bump Mask Ramp.
- **Layer stack (in order of coverage/dominance):** standard bump -> cracks bump (overrides standard at 1.0) -> cracks bump 2 (independent, bigger-scale cracks) -> dusty bump (own Colour Ramp for contrast).
- **Masking:** same per-layer vertex-group/mask mechanism as the add-on's Displacement tab, reused here for cracks bump and cracks bump 2.

### Difficulty
Beginner (short overview; main prerequisite is owning the paid add-on and having a base sculpt/displacement already set up from earlier steps in the series).

### Blender Version
Not stated verbally; viewport title bar in the captured frames is partially legible and appears consistent with the same Blender 5.1.x build seen in the Geometry & Scatter episode of this series.

### Tags
procedural, displacement, organic, product-viz, beginner

---

## Related Tutorials
Part of the **NS Rock Sculptor Guide** series (10 episodes, all uploaded 2026-07-30) covering the NS Rock Sculptor add-on tab by tab. This episode covers the Bump tab; the author says Geometry comes next after this in his recording order.
- [NS Rock Sculptor Guide - Geometry & Scatter](ns-rock-sculptor-guide---geometry-scatter.md) — same add-on/series, Geometry & Scatter tabs (next tab after Bump per the author's own sequencing in this video).
- [NS Rock Sculptor Guide - Displacement](ns-rock-sculptor-guide---displacement.md) — same add-on/series, Displacement tab (shares the masking concept this episode references directly).
- [NS Rock Sculptor Guide - Colour Ramps](ns-rock-sculptor-guide---colour-ramps.md) — same add-on/series, Colour Ramps tab (directly relevant — this episode tunes the Dusty Bump Colour Ramp).
- [NS Rock Sculptor Guide - Filters](ns-rock-sculptor-guide---filters.md) — same add-on/series, Filters tab.
- [NS Rock Sculptor Guide - Moss](ns-rock-sculptor-guide---moss.md) — same add-on/series, Moss tab.
- [NS Rock Sculptor Guide - Colour](ns-rock-sculptor-guide---colour.md) — same add-on/series, Colour tab.
- [NS Rock Sculptor Guide - Edge Crease](ns-rock-sculptor-guide---edge-crease.md) — same add-on/series, Edge Crease tab.
- [NS Rock Sculptor Guide - Sculpt Settings](ns-rock-sculptor-guide---sculpt-settings.md) — same add-on/series, Sculpt Settings tab.
- [NS Rock Sculptor Guide - Presets](ns-rock-sculptor-guide---presets.md) — same add-on/series, Presets tab.
- [NS Infinite Rock Builder Guide - Main Controls](ns-infinite-rock-builder-guide---main-controls.md) — conceptual sibling add-on by the same author (Nick Sayce), same rock/procedural theme, different tool.
