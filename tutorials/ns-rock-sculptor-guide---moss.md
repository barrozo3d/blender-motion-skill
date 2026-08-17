---
title: NS Rock Sculptor Guide - Moss
source: YouTube
url: https://www.youtube.com/watch?v=Acp5-LuffVA
author: Nick Sayce
ingested: 2026-08-17
blender_version: "5.1.x (approximate, viewport title bar in captured frames; not stated verbally)"
tags: [materials, procedural, organic, product-viz, beginner]
extraction_status: complete
frames_dir: tutorials/frames/ns-rock-sculptor-guide---moss/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Rock Sculptor Guide - Moss

**Source:** [YouTube](https://www.youtube.com/watch?v=Acp5-LuffVA)
**Author:** Nick Sayce
**Duration:** 1m45s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Now we have Moss.
[0:06] Moss amount, put that up to one.
[0:09] If the cube has been randomly rotated, which we did, the, it's going to just, the moss isn't going to change with it.
[0:19] So what you do is once you're happy with an angle like that, you would want to control A and just apply your rotation and then it will put that back at the top.
[0:28] And you've got a few, you know, moss displacement requires displacement when we get there.
[0:34] In fact, if I just know, we'll get there in a minute.
[0:37] There's your colors. That's actually default to a bit too bright.
[0:41] And moss height.
[0:44] If you go, well, it's moss height, the higher the number, the higher up the rock, it will start.
[0:51] So 1.5 is just barely, barely at the top there.
[0:55] And moss distortion, if you see, it's quite bitty, quite round.
[1:01] So if you want, press 1 and now it just makes it much bittier.
[1:08] And again, that's dependent on the displacement, how much distortion you want.
[1:11] So you can see the displacement, we'll get there.
[1:13] And moss thickness, at the moment, it's quite gradated in terms of it starts quite low and slowly builds up.
[1:22] If the moss thickness was at 1, as you see, you've got a much, much sharper contrast there for the moss.
[1:32] And again, this will, when we add displacement, you'll see that.
[1:37] But for now, we don't need that on that's moss.
[1:40] Yeah, that's everything for moss. All right, we will just quickly talk about filters next.



---

## Captured Frames

- [0:06] tutorials/frames/ns-rock-sculptor-guide---moss/frame_000.jpg
- [0:19] tutorials/frames/ns-rock-sculptor-guide---moss/frame_001.jpg
- [0:44] tutorials/frames/ns-rock-sculptor-guide---moss/frame_002.jpg
- [1:01] tutorials/frames/ns-rock-sculptor-guide---moss/frame_003.jpg
- [1:22] tutorials/frames/ns-rock-sculptor-guide---moss/frame_004.jpg

---

> **Third-party add-on note:** This tutorial covers the **Moss** tab of **NS Rock Sculptor**, a paid third-party Blender add-on by Nick Sayce (NS). "Moss Amount," "Moss Height," "Moss Distortion," "Moss Thickness," and the two Moss Colour swatches are the add-on's own exposed inputs, not stock Blender shader nodes.

## Structured Notes

### Core Technique
A dedicated Moss group in the sidebar blends a two-color moss layer onto the rock, gated by a world-space height threshold (so moss favors the "top" of the rock) and shaped by distortion/thickness controls — with an explicit gotcha that a randomly-rotated object must have its rotation applied (Ctrl+A) or the moss's sense of "up" won't match the visual orientation.

### Summary
With Moss Amount raised to 1, the effect is immediately visible as a green tint over the rock. The presenter flags an important gotcha: if the rock object was randomly rotated (as done earlier in the series' Geometry/Scatter step) without applying that rotation, the moss mask still reads world-space "up" from the object's un-rotated orientation — so the moss patch won't visually align with the rock's new top; the fix is Ctrl+A → Apply Rotation so the object's local "up" matches what's on screen. Two color swatches (Moss Colour 1/2) tint the moss layer (default colors called "a bit too bright"). Moss Height sets how far up the rock the moss starts — higher values push the moss patch smaller/higher (demoed at 1.5 for a "barely at the top" sliver). Moss Distortion controls how bitty/organic vs. smooth-and-round the moss patch's edge looks — pushed to 1 for a noticeably bittier, more broken-up edge; the presenter notes this interacts with the (not-yet-covered) Displacement tab. Moss Thickness controls the sharpness of the transition from bare rock to full moss — low values give a soft gradient buildup, while Thickness at 1 produces a hard, sharply contrasted cutoff edge; this too becomes more visible once Displacement is layered in.

### Key Steps
1. Open the "Moss" section in the NS Rock Sculptor sidebar and raise "Moss Amount" (demoed at 1) to enable the effect.
2. **Gotcha:** if the rock's object rotation was randomized earlier (e.g. via the Scatter tab) but never applied, the moss's world-space height mask won't track the object's apparent orientation — select the object and press Ctrl+A → Apply → Rotation to fix this before relying on Moss Height.
3. Set "Moss Colour 1" and "Moss Colour 2" to taste — defaults run a bit bright/saturated per the presenter.
4. Adjust "Moss Height" to control how far up the rock the moss band starts; higher numeric values push the visible moss patch smaller and further toward the top (1.5 shown as a thin sliver at the very top).
5. Adjust "Moss Distortion" (press/drag to 1 in the demo) to make the moss patch's edge bittier and more organic-looking rather than a smooth round blob; note this control's visual strength depends on the Displacement setup (covered in a later episode).
6. Adjust "Moss Thickness" to control edge sharpness: low values (the default seen) produce a soft, gradually-building transition; Thickness at 1 produces a hard, high-contrast cutoff between mossy and bare rock. Also displacement-dependent for full effect.
7. Series note: Moss's Height/Distortion/Thickness controls are described multiple times as working "together with displacement" — revisit this episode's settings once Displacement is dialed in, since the two systems compound.

### Nodes / Settings
- Sidebar section "Moss" (positioned after Edge Crease, before Filters, per the panel order seen across this series: Sculpt Settings, Weight Paint, Edge Crease, Colour, Moss, Filters, Colour Ramps, Displacement, Bump, Geometry, Scatter)
- Moss Amount (0-1 enable/blend strength), Moss Displacement Amount, Moss Colour 1, Moss Colour 2, Moss Height, Moss Distortion, Moss Thickness

### Difficulty
Beginner (slider adjustments only; the rotation-apply gotcha is the only real trap)

### Blender Version
5.1.x (approximate, viewport title bar in captured frames; not stated verbally) — consistent with other NS Rock Sculptor Guide episodes from this same upload batch (2026-07-30/31).

### Tags
materials, procedural, organic, product-viz, beginner

---

## Related Tutorials
Part of the **NS Rock Sculptor Guide** series (10 episodes, all uploaded 2026-07-30) covering the NS Rock Sculptor add-on tab by tab. This episode covers the Moss tab; the presenter's own "next" topic is Filters.
- [NS Rock Sculptor Guide - Filters](ns-rock-sculptor-guide---filters.md) — same add-on/series, Filters tab (directly relevant — presenter's own forward-reference from this episode).
- [NS Rock Sculptor Guide - Displacement](ns-rock-sculptor-guide---displacement.md) — same add-on/series, Displacement tab (directly relevant — Moss Height/Distortion/Thickness are explicitly described here as compounding with Displacement, not yet covered at this point in the series).
- [NS Rock Sculptor Guide - Geometry & Scatter](ns-rock-sculptor-guide---geometry-scatter.md) — same add-on/series, Geometry & Scatter tabs (directly relevant — the random-rotation-needs-Apply gotcha traces back to that episode's Scatter step).
- [NS Rock Sculptor Guide - Colour Ramps](ns-rock-sculptor-guide---colour-ramps.md) — same add-on/series, Colour Ramps tab.
- [NS Infinite Rock Builder Guide - Moss / Fresnel / Dust](ns-infinite-rock-builder-guide---moss-fresnel-dust.md) — conceptual sibling: same author's other add-on, also has a Z-axis/height-masked Moss control, different tool/UI.
