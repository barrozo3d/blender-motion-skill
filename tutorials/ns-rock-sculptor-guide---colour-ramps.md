---
title: NS Rock Sculptor Guide - Colour Ramps
source: YouTube
url: https://www.youtube.com/watch?v=vm4QsOascts
author: Nick Sayce
ingested: 2026-08-17
blender_version: "5.1.x (approximate, viewport title bar in captured frames; not stated verbally)"
tags: [materials, procedural, organic, product-viz, beginner]
extraction_status: complete
frames_dir: tutorials/frames/ns-rock-sculptor-guide---colour-ramps/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Rock Sculptor Guide - Colour Ramps

**Source:** [YouTube](https://www.youtube.com/watch?v=vm4QsOascts)
**Author:** Nick Sayce
**Duration:** 1m39s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] This gives you a heck of a lot of control. If I added dust filters, always my favorite,
[0:12] I don't know why. If I added some dust, I'm just going to roughen that up, I don't like
[0:16] that bad and I don't want it that hard. Just a dusting. There we go. So now, let's say I
[0:25] like that, but I want it to be more bitty. There's too much of it. So I'm going to go
[0:30] into the color ramps. Let me close the filters, color ramps. And I need dust color ramp. So if I
[0:38] bring the black up, just like color ramps, as you can see, that way you can create much smaller
[0:44] patches of dust or more, you know, you can just muck around with the color ramp. And that's the
[0:51] same for the main color ramp as well. Let me just bring that right down. The main color ramp is also
[0:59] in there. Right at the top. So you can do, you know, mess around with that as well. Just like you
[1:08] would any other color ramp. A useful tip, you can add more if you want. I would, so if I wanted
[1:15] some variation, I'll just plop another pip in there and then give it some different color,
[1:21] maybe something a bit more obvious. And now I've got three colors. So you can just, you know, add
[1:26] away if you like. But yeah, this is very useful for the displacement when we get there, which is
[1:34] next. And again, you'll, you'll, she'll see why. All right, sweet color ramps in the bag.



---

## Captured Frames

- [0:12] tutorials/frames/ns-rock-sculptor-guide---colour-ramps/frame_000.jpg
- [0:38] tutorials/frames/ns-rock-sculptor-guide---colour-ramps/frame_001.jpg
- [0:59] tutorials/frames/ns-rock-sculptor-guide---colour-ramps/frame_002.jpg
- [1:15] tutorials/frames/ns-rock-sculptor-guide---colour-ramps/frame_003.jpg
- [1:21] tutorials/frames/ns-rock-sculptor-guide---colour-ramps/frame_004.jpg

---

> **Third-party add-on note:** This tutorial covers the **Colour Ramps** tab of **NS Rock Sculptor**, a paid third-party Blender add-on by Nick Sayce (NS). "Dust Colour Ramp" and "Main Colour Ramp" are the add-on's own exposed Color Ramp nodes in its sidebar panel, not a from-scratch manual Blender shader setup.

## Structured Notes

### Core Technique
Fine-tuning the size/distribution of the add-on's Dust and Main color/detail masks by editing their dedicated Color Ramp stops directly in the sidebar, and adding extra ramp stops to introduce additional color variation.

### Summary
Short follow-on to the Filters video: after roughening up the rock with a Dust filter, the presenter opens the sidebar's "Colour Ramps" section to fine-tune how that dust reads. Both the "Dust Colour Ramp" and the "Main Colour Ramp" (found at the top of the same section) behave like any standard Blender color ramp — dragging the black/white stops closer together or further apart shrinks or grows the size/density of the patches they mask (dust patches become "bittier" and smaller as the black stop moves right). The presenter also demonstrates adding a third color stop ("plop another pip in there") to the Main Colour Ramp and assigning it a distinct, more obvious color via the color picker, producing three-color variation on the rock surface instead of a two-color gradient. Closes by flagging that these same ramps become directly relevant to the upcoming Displacement tab.

### Key Steps
1. With a Dust filter already added (from the Filters tab) and looking too heavy/hard-edged, open the sidebar's "Colour Ramps" section (collapse Filters first to make room).
2. Locate "Dust Colour Ramp" — drag its black stop further right (closer to the white stop) to shrink dust patches into smaller, bittier specks; drag it left to spread dust more broadly.
3. Locate "Main Colour Ramp" at the top of the same Colour Ramps section — it works identically to the Dust ramp (drag stops to resize color-region distribution) and controls the primary color masking, independent of the Dust ramp.
4. To add color variation: click into empty space along the ramp gradient bar to insert an extra color stop ("pip"), then open the color picker (HSV wheel + RGB/Hex fields) and assign it a distinct, clearly different color from the existing two stops.
5. Repeat freely — any number of stops can be added to build up more complex multi-color variation across the rock surface.
6. Note for later: these same Colour Ramp controls are reused/relevant when working in the Displacement tab (covered next in the series).

### Nodes / Settings
- Sidebar section "Colour Ramps" (located below Filters in the NS Rock Sculptor panel order: Sculpt Settings, Weight Paint, Edge Crease, Colour, Filters, Colour Ramps, Displacement, Bump, Geometry, Scatter)
- "Dust Colour Ramp" — standard Color Ramp widget (black/white stops shown in captured frames), masks the Dust filter's patch size/density
- "Main Colour Ramp" — standard Color Ramp widget, sits above Dust Colour Ramp in the same section, masks primary color distribution; supports adding extra stops via the standard Blender color-ramp "+" / click-to-add-stop interaction, each stop set via the built-in HSV color picker

### Difficulty
Beginner (dragging existing ramp stops and adding new ones via the standard color picker — no node authoring)

### Blender Version
5.1.x (approximate, viewport title bar in captured frames; not stated verbally) — consistent with other NS Rock Sculptor Guide episodes from this same upload batch (2026-07-30/31).

### Tags
materials, procedural, organic, product-viz, beginner

---

## Related Tutorials
Part of the **NS Rock Sculptor Guide** series (10 episodes, all uploaded 2026-07-30) covering the NS Rock Sculptor add-on tab by tab. This episode covers the Colour Ramps tab; the presenter's own "next" topic is Displacement, which directly reuses this episode's Dust Colour Ramp as its Displacement Mask.
- [NS Rock Sculptor Guide - Displacement](ns-rock-sculptor-guide---displacement.md) — same add-on/series, Displacement tab (directly relevant — its Displacement Mask is built from a Colour Ramps-tab ramp, i.e. this episode's content).
- [NS Rock Sculptor Guide - Geometry & Scatter](ns-rock-sculptor-guide---geometry-scatter.md) — same add-on/series, Geometry & Scatter tabs.
- [NS Rock Sculptor Guide - Bump](ns-rock-sculptor-guide-bump.md) — same add-on/series, Bump tab.
- [NS Infinite Rock Builder Guide - Colours](ns-infinite-rock-builder-guide---colours.md) — conceptual sibling: same author's other add-on, also uses Color Ramp-driven color masking, different tool/UI.
