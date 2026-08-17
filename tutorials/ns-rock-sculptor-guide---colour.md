---
title: NS Rock Sculptor Guide - Colour
source: YouTube
url: https://www.youtube.com/watch?v=NaimTlxwn2Q
author: Nick Sayce
ingested: 2026-08-17
blender_version: "5.1.x (approximate, viewport title bar in captured frames; not stated verbally)"
tags: [materials, procedural, organic, product-viz, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/ns-rock-sculptor-guide---colour/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Rock Sculptor Guide - Colour

**Source:** [YouTube](https://www.youtube.com/watch?v=NaimTlxwn2Q)
**Author:** Nick Sayce
**Duration:** 5m13s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:01] Now there's a lot of options in color and they're all the color is all connected to the filters but is also connected to the color ramps and as I said, I'm going to try and keep this in order, so we'll just do the colors to start.
[0:17] color one and color two, that's kind of, I'm going to do real garish colors so you
[0:21] can really see the differences. So that's the, in fact, before we get to these,
[0:28] I'm just going to turn off, don't worry about this, I'm just going to turn off the filters,
[0:32] we are actually going to have to discuss some filterage. Right, so now we've just got the
[0:39] main color, the base color, which is now blue and purple, and color two, sorry, orange and
[0:48] brown, you purple, you then got dirt, color and dust color, and these are connected to the filters,
[0:57] so we have to talk about it, this one is going to be colors and filters. So once you've got your
[1:03] colors, you can pick a dust color, you go into filters, pick it from this dirt filter and dust,
[1:09] we'll just do dust for now, and that's the amount. So if I slide in the dust, and that is white,
[1:15] we can make it whiter, and all their controls, again for the filter are here, so your roughness,
[1:23] all that, all that shenanigans, it's a noise filter clearly, and so what you can do with this,
[1:31] you can really start to layer, wrong one, and start to layer some some colors over one another,
[1:37] and it gives it that much more random rocky feel, and we can add some dirt, and bearing in mind dirt
[1:45] is based on a multiply, color ramp, mix color, and dust is going through screen, so only these two
[1:53] colors are necessary, but dark colors for dirt, light colors for dust, so now if we go to the dirt
[1:59] filter, we can bring that in, I'm not sure, let's pick something clearly, all right, you can kind of
[2:08] see at the bottom there, but again the filters are all here as well, so we don't need the roughness,
[2:14] we can probably scale it up a bit, yeah, so that's those two filters, and there are filters for
[2:24] everything, and so we can, that's actually strange, I don't know why that's coming out, let me just check
[2:30] the color ramp of dirt, dirt, dirt, that's very strange, oh that's why,
[2:40] okay yeah, so again you will be messing with the the color ramps, when we get there,
[2:47] all right, so let's not have such a horrible color, you get it now, there we go, all right,
[2:55] so and then you've got edge wear, and there's two, there's edge wear and edge wear top,
[3:00] depending on the edges, I mean this one is not so clear, let me make dark colors,
[3:08] that's probably why it's harder to see them, and let me turn off the dust filter so that we can just
[3:15] see, it's edge wear, so edge wear is currently set to a bright yellow, I want that white, okay,
[3:24] and now those harsh edges that we added, they've got a bit of, a bit of dust I guess you could call it,
[3:32] and the reason there's two is because if I add, if I just had edge wear, this is at the very bottom
[3:38] of the color pile, and the color ramps will affect this, we'll get to that, in fact let me just make
[3:44] it so it is a bit more visible, otherwise you won't be able to see exactly what I'm talking about,
[3:53] 0.53, nope too far, oh and I, I mothed up, I picked the wrong pip, I want the white one, 0.53,
[4:06] might be better at 0.52, okay so that's there, if I then added some dirt, which is a darker color,
[4:17] well actually that's why it's kind of broken, because without it, without the dirt,
[4:22] it's unbroken edges, but if I added dirt, it's then multiplying over those edges, so it breaks it,
[4:30] which again makes it more natural, but sometimes you want, you don't want it broken, so there's edge
[4:34] wear at the bottom, at the first bottom of the chain, and there's an edge wear at the top of the
[4:39] chain, so if you wanted it better, that's now unbroken, so that's why there's two edge wheels,
[4:46] ambient occlusion, you know what that does, it's not going to be visible till we do some displacement,
[4:52] so it doesn't matter if that's on or off, roughness is, that's obvious, you want a shiny rock,
[4:59] do that, ambient occlusion distances, again if you know about ambient occlusion,
[5:05] just how far into the objects and away from the cracks, it will appear, but that right there is color done.



---

## Captured Frames

- [0:39] tutorials/frames/ns-rock-sculptor-guide---colour/frame_000.jpg
- [1:09] tutorials/frames/ns-rock-sculptor-guide---colour/frame_001.jpg
- [1:59] tutorials/frames/ns-rock-sculptor-guide---colour/frame_002.jpg
- [3:15] tutorials/frames/ns-rock-sculptor-guide---colour/frame_003.jpg
- [4:06] tutorials/frames/ns-rock-sculptor-guide---colour/frame_004.jpg
- [4:39] tutorials/frames/ns-rock-sculptor-guide---colour/frame_005.jpg
- [4:52] tutorials/frames/ns-rock-sculptor-guide---colour/frame_006.jpg

---

> **Third-party add-on note:** This tutorial covers the **Colour** tab of **NS Rock Sculptor**, a paid third-party Blender add-on by Nick Sayce (NS). Every swatch/slider named here (Colour 1/2, Dirt Colour, Dust Colour, Edge Wear Colour, Ambient Occlusion Colour, Edge Wear, Edge Wear Top, Roughness, Ambient Occlusion Distance) is the add-on's own exposed input, not a from-scratch manual Blender shader graph — and this tab is explicitly wired into both the Filters and Colour Ramps tabs, so this episode treats all three together.

## Structured Notes

### Core Technique
The base two-color rock (Colour 1/Colour 2) is layered with Dirt and Dust color passes that route through the Filters tab (Dirt = Multiply blend, Dust = Screen blend, hence "dark colors for dirt, light colors for dust"), plus a separate Edge Wear system with two independent swatches — one at the bottom of the color stack, one at the top — that read differently depending on whether Dirt is breaking up the wear pattern beneath them.

### Summary
The densest and most interconnected episode in the series: the presenter explicitly says color is tied to both Filters and Colour Ramps, so this covers all three together. Colour 1 and Colour 2 form the base rock gradient (demoed in garish blue/orange for visibility). Dirt Colour and Dust Colour are separate swatches that only become visible once their corresponding filter (Dirt Filter, Dust Filter) is added from the Filters tab and dialed in with Amount/Scale/Roughness controls — dust reads via a Screen blend (so light colors show best) while dirt reads via a Multiply blend (so dark colors show best), and their apparent size/shape is additionally shaped by the Colour Ramps tab (a visibly wrong ramp state produces a broken/ugly result the presenter has to fix live). Edge Wear Colour and a related Ambient Occlusion Colour swatch tint the add-on's automatic edge-highlighting; there are two separate Edge Wear controls — "Edge Wear" (bottom of the color-blend chain) and "Edge Wear Top" (top of the chain) — because their position in the stack changes how later multiply-based effects (like Dirt) interact with them: Edge Wear at the bottom gets broken up/interrupted by a subsequently-added Dirt multiply, while Edge Wear Top sits above that interaction and stays a clean, unbroken highlight. Roughness and Ambient Occlusion Distance close out the tab; Ambient Occlusion won't be visually meaningful until the (later) Displacement tab adds real geometric detail for it to occlude.

### Key Steps
1. Open the "Colour" tab; note upfront that color, filters, and colour ramps are all interconnected in this add-on — expect to bounce between tabs.
2. Set the base "Colour 1" and "Colour 2" swatches — these are the primary two-tone gradient across the whole rock.
3. To use Dirt or Dust: first set their color swatches ("Dirt Colour", "Dust Colour") here in the Colour tab, then switch to the Filters tab and add/select the corresponding filter (Dirt Filter or Dust Filter) to actually make them visible — each filter exposes its own Amount, Scale, and Roughness (noise) controls.
4. Remember the blend-mode rule: Dust uses a Screen blend (light/white colors read best, dark colors vanish), Dirt uses a Multiply blend (dark colors read best, light colors vanish) — pick swatch colors accordingly.
5. If a dirt/dust pass looks visually "broken" or wrong, check the corresponding Colour Ramp (Colour Ramps tab) — an unintended ramp-stop position is a common cause and is directly responsible for how patchy/bitty the color reads.
6. Set "Edge Wear Colour" and "Ambient Occlusion Colour" swatches; use bright/contrasting test colors first (e.g. yellow) to confirm they're working, then dial in a final subtle color (e.g. white) once positioning is confirmed.
7. Understand the two Edge Wear slots: "Edge Wear" sits at the very bottom of the color-blend stack, so later multiply-based passes (like Dirt) will visibly break up/interrupt its pattern once added — this reads as more natural, weathered wear. "Edge Wear Top" sits above that interaction point, so it stays clean and unbroken regardless of what's added beneath it — use this one when you want guaranteed crisp edge highlights.
8. "Roughness" sets overall shininess (self-explanatory per the presenter); "Ambient Occlusion Distance" sets how far into cracks/crevices the AO effect reaches — but AO's visual impact is minimal until real displacement geometry exists (Displacement tab, later episode).

### Nodes / Settings
- Sidebar section "Colour" (positioned after Edge Crease and before Moss/Filters per the panel order seen across this series: Sculpt Settings, Weight Paint, Edge Crease, Colour, Moss, Filters, Colour Ramps, Displacement, Bump, Geometry, Scatter)
- Base swatches: Colour 1, Colour 2
- Dirt Colour, Dust Colour (each requires its matching filter — Dirt Filter / Dust Filter — enabled in the Filters tab to become visible; Dirt = Multiply blend, Dust = Screen blend)
- Edge Wear Colour, Ambient Occlusion Colour
- Sliders: Edge Wear, Edge Wear Top (two independent positions in the color-blend stack — bottom vs. top), Roughness, Ambient Occlusion Distance
- Cross-referenced tabs: Filters (Dirt/Dust filter Amount/Scale/Roughness), Colour Ramps (shapes dirt/dust patch distribution)

### Difficulty
Intermediate (requires understanding blend-mode interaction — Multiply vs. Screen — and stack order/position effects between Edge Wear and Dirt, not just slider values)

### Blender Version
5.1.x (approximate, viewport title bar in captured frames; not stated verbally) — consistent with other NS Rock Sculptor Guide episodes from this same upload batch (2026-07-30/31).

### Tags
materials, procedural, organic, product-viz, intermediate

---

## Related Tutorials
Part of the **NS Rock Sculptor Guide** series (10 episodes, all uploaded 2026-07-30) covering the NS Rock Sculptor add-on tab by tab. This episode is the most cross-referenced in the series — it explicitly ties Colour to both Filters and Colour Ramps.
- [NS Rock Sculptor Guide - Filters](ns-rock-sculptor-guide---filters.md) — same add-on/series, Filters tab (directly relevant — Dirt/Dust colors set here only become visible once their filter is enabled there).
- [NS Rock Sculptor Guide - Colour Ramps](ns-rock-sculptor-guide---colour-ramps.md) — same add-on/series, Colour Ramps tab (directly relevant — shapes the size/distribution of the dirt/dust color passes set here).
- [NS Rock Sculptor Guide - Displacement](ns-rock-sculptor-guide---displacement.md) — same add-on/series, Displacement tab (directly relevant — Ambient Occlusion set up here has no visible effect until real geometric displacement exists).
- [NS Rock Sculptor Guide - Moss](ns-rock-sculptor-guide---moss.md) — same add-on/series, Moss tab (adjacent color-layering system in the same panel order).
- [NS Rock Sculptor Guide - Edge Crease](ns-rock-sculptor-guide---edge-crease.md) — same add-on/series, Edge Crease tab (adjacent in panel order, precedes Colour).
- [NS Rock Sculptor Guide - Presets](ns-rock-sculptor-guide---presets.md) — same add-on/series, Presets tab (directly relevant — the active-material-isolation concept demoed there with loaded presets is the same mechanism this episode demos with color edits).
- [NS Infinite Rock Builder Guide - Colours](ns-infinite-rock-builder-guide---colours.md) — conceptual sibling: same author's other add-on, also layers multiple color inputs via Color Ramps and blend modes, different tool/UI.
