---
title: NS Infinite Rock Builder Guide - Moss / Fresnel / Dust
source: YouTube
url: https://www.youtube.com/watch?v=thzYTUEyrKI
author: Nick Sayce
ingested: 2026-08-12
blender_version: "4.x (see Main Controls video for title-bar reading; not independently confirmed here)"
tags: [materials, shaders, organic, procedural, beginner, blender-4x]
extraction_status: complete
frames_dir: tutorials/frames/ns-infinite-rock-builder-guide---moss-fresnel-dust/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Infinite Rock Builder Guide - Moss / Fresnel / Dust

**Source:** [YouTube](https://www.youtube.com/watch?v=thzYTUEyrKI)
**Author:** Nick Sayce
**Duration:** 2m1s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Mus, Fresnel, Dust
[0:05] So, let's start with ambient dust. This is basically ambient occlusion. You can see it darkening up the cracks.
[0:18] In a similar way to that displacement color, it does discolor. So that's the ambient dust mix.
[0:26] I should have called it ambient dirt.
[0:28] Fresnel, so if you had no Fresnel, they're not shiny at all. They're very bland, very rough.
[0:36] But if you add 0.6, you see it just brightens up, makes it a bit almost like they'd be slidier.
[0:43] Slidier rocks if you were to try and climb it.
[0:46] The moss, crank that in, and then you get on the Z axis, and it depends on the formation, whether or not this wants to do that.
[0:58] But yeah, that's the intention. You get a bit of moss on the upper parts of the rocks.
[1:05] Dust shape, so yeah, this is the ambient occlusion. So did I add it? Yep, ambient dust.
[1:10] So I could bring it further out, make the darker patches even darker if I pull this back.
[1:19] It should start creeping out of the wall. It's not creeping out of the wall at all. What's going on here?
[1:24] Right, that's not working. Every time I do a video, there's something I come across that I was not aware is no longer functioning.
[1:32] So I'm going to deal with that. Oh, no, there it is. It is functioning.
[1:36] See, you see, it's really darkened up those edges.
[1:42] Even further back, it's going to just darken up the whole thing. So for that contrast, you say, thank God it does work.
[1:50] There's no reason I shouldn't work. It does work. Ha-ra! Sweet.
[1:55] Alright, that is those three done. Let's move on to water level roughness.



---

## Captured Frames

- [0:05] tutorials/frames/ns-infinite-rock-builder-guide---moss-fresnel-dust/frame_000.jpg
- [0:36] tutorials/frames/ns-infinite-rock-builder-guide---moss-fresnel-dust/frame_001.jpg
- [0:58] tutorials/frames/ns-infinite-rock-builder-guide---moss-fresnel-dust/frame_002.jpg
- [1:36] tutorials/frames/ns-infinite-rock-builder-guide---moss-fresnel-dust/frame_003.jpg
- [1:42] tutorials/frames/ns-infinite-rock-builder-guide---moss-fresnel-dust/frame_004.jpg

---

## Structured Notes

### Core Technique
Adding surface realism to a rock built with the **Infinite Rock Builder** add-on (Nick Sayce / NS) via three quick sidebar controls: an ambient-occlusion-style "Ambient Dust" darkening mix, a Fresnel shininess slider, and a Z-axis-driven moss overlay.

**Add-on disclosure:** "Ambient Dust Mix," "Fresnel," and "Moss" are exposed inputs of the add-on's custom node group in the N-panel sidebar, not stock Blender shader/geometry nodes — this is add-on-specific surfacing, layered on top of whatever formation/color setup is already in place.

### Summary
Part of the NS Infinite Rock Builder Guide series — covers Moss / Fresnel / Dust; see also Main Controls, Colours, Filters, Water Level Roughness, Cliff-top Flatten/Bump. This is the shortest video in the series (~2 minutes) and covers three small but impactful controls together: (1) Ambient Dust — effectively a built-in ambient-occlusion pass that darkens cracks/crevices for a grimier, dust-caught-in-recesses look (the presenter notes it should probably have been named "Ambient Dirt"); pulling the mix further creates stronger contrast between deep shadowed cracks and exposed rock. (2) Fresnel — with no Fresnel the rock reads flat/bland/matte; adding around 0.6 brightens edges viewed at glancing angles, giving a subtly shinier, "slidier"-looking rock surface. (3) Moss — cranking the moss amount blends in a green mossy tint that's masked by world-Z-axis (height), so moss tends to appear on the upper/top-facing parts of the rock, though the presenter notes the effect's visibility depends on the specific formation's shape.

### Key Steps
1. Open the sidebar's "Moss / Fresnel / Dust" section (below Filters and Colours) on a rock that already has at least one formation and material set up.
2. Increase "Ambient Dust Mix" to darken recessed/cracked areas of the rock, similar in effect to the Disp Colour control from the Colours video but framed here as a grime/ambient-occlusion pass; pushing it further increases the contrast between shadowed cracks and the rest of the surface.
3. Set the "Fresnel" value (demoed around 0.6) to add glancing-angle brightness/shininess to the rock; at 0 the surface looks completely flat and rough.
4. Increase the "Moss" amount to blend in a green tint; the moss mask is driven by the object's Z axis (world height), so it's designed to appear preferentially on upper-facing surfaces — note this depends on the formation's actual geometry, so it doesn't guarantee moss lands exactly where expected on every shape.
5. Treat all three as fast "finishing" sliders layered on top of the formation shape and color work from the earlier videos in the series, rather than as foundational steps.

### Nodes / Settings
- Sidebar section: "Moss / Fresnel / Dust" (sits alongside Filters, Colours, Water Level Roughness, Cliff Top Flatten in the same N-panel)
- Ambient Dust Mix (AO-style darkening of crevices, demoed pulled progressively higher)
- Fresnel (shininess at glancing angles; demoed at ~0.6)
- Moss (green tint blended in via a Z-axis/height-based mask; formation-dependent visibility)

### Difficulty
Beginner (three independent sliders, no node authoring, quick to demo)

### Blender Version
Not stated explicitly by the narrator; not independently confirmed from these frames (see Main Controls video for the title-bar reading of "Blender 4.x").

### Tags
materials, shaders, organic, procedural, beginner, blender-4x

---

## Related Tutorials
Part of the **NS Infinite Rock Builder Guide** series (Nick Sayce / NS add-on) — all 6 parts cross-link regardless of tag overlap since they form one continuous guide:
- [Main Controls](ns-infinite-rock-builder-guide---main-controls.md)
- [Colours](ns-infinite-rock-builder-guide---colours.md)
- [Filters](ns-infinite-rock-builder-guide---filters.md)
- [Water Level Roughness](ns-infinite-rock-builder-guide---water-level-roughness.md)
- [Cliff-top Flatten / Bump](ns-infinite-rock-builder-guide---cliff-top-flatten-bump.md)
