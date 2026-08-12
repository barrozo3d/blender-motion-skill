---
title: NS Rock Sculptor Guide - Geometry & Scatter
source: YouTube
url: https://www.youtube.com/watch?v=BePg_iEbaM4
author: Nick Sayce
ingested: 2026-08-12
blender_version: "5.1.x (partially legible in viewport title bar in captured frames; not stated verbally)"
tags: [procedural, displacement, particles, organic, product-viz, beginner]
extraction_status: complete
frames_dir: tutorials/frames/ns-rock-sculptor-guide---geometry-scatter/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Rock Sculptor Guide - Geometry & Scatter

**Source:** [YouTube](https://www.youtube.com/watch?v=BePg_iEbaM4)
**Author:** Nick Sayce
**Duration:** 5m29s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] GEOMETRY
[0:03] So geometry!
[0:05] This is really...
[0:06] I'm still thinking of a way of adding this to the Scatter...
[0:09] ...of having user presets, because at the moment there's only four that I made.
[0:14] I'll find a way to you to populate that.
[0:17] But let's say I'm happy with this, and I would like to do something like scatter it.
[0:24] In fact, the displacement...
[0:26] when you decimate geometry, it's going to lose quite a bit of the displacement. It's not going to
[0:31] look exactly the same. But the only real reason I think anyone would decimate is to do exactly what
[0:37] I did, which is to make the scattering the pebbles. When you've got lots of little ones,
[0:41] you don't want this much geometry. That's not even a lot. That's pretty low poly anyway.
[0:49] So yeah, decimate. So if you go down to geometry, every time by the way,
[0:57] when you, I never mentioned that, when you're sculpting, each time you sculpt,
[1:01] you can set how big the voxels are and how many target faces once you quad-remesh. So this will
[1:08] be a thousand faces because that's what I set it at. But you can play with them to get more
[1:13] resolution or less resolution because you can get away less and play with those. But the decimate
[1:18] rock, I normally go down to about 0.1 or 0.2. I'm going to do 0.2. So it looks like that. And then
[1:24] if I click decimate because it's already got a subdivision, it's going to apply that. So the
[1:29] first one will take a little bit longer. I'm talking like two seconds. That's that. And then if we check,
[1:36] it's mangled it, which is fine. And I'll decimate it again. I would even consider decimating it
[1:43] a third time. And it's pretty much retained the shape. But as you can see, that is way less
[1:51] geometry. It's horrific. It's horrific topology. Mind you're trying to loop cut. What happens if
[1:59] you're trying to loop cut? No. But as I say, the reason you're doing that is because you want
[2:06] lots of them in a scene. They still look pretty much exactly the same. The only thing that might
[2:13] be different is if you've got edgeware, if I show you what happens if I put edgeware on this,
[2:19] it'll just turn the whole thing because it has no idea where the edges are. Because look at it.
[2:25] It's horrible. So yeah, if you're decimated and it turns white, that's why it doesn't like edgeware.
[2:35] Maybe I wouldn't know. There's so little you can do when it's like that. You can't text your
[2:39] paint. Just do that if you want to make small pebbles. And I might as well in that one
[2:46] show you the scatter. This will be geometry and scatter. So let's say, yeah, I want to scatter.
[2:54] So let me go over to that. You need something to scatter on. So let's just pull up a plane.
[3:00] I'm going to apply those transforms. You can press control eight. And then I'm going to just
[3:08] crank that up. Okay. And now if I click pebbles one and scatter,
[3:18] and obviously they are tiny. So the bottom here, you've got number and scale. So I'm probably going
[3:25] to put that up one. There we go. And it's have three threads. And because they've already been
[3:32] decimated, they don't take much render. So that's that. And then you've got your vertex groups.
[3:42] So if I get rid of that, and I just did a bit of white painting, let's say, you know, you just
[3:48] you'll do put a rock in the middle. Oh, I've never seen that error.
[3:53] Hmm. But then I've never been in white paint and added a preset. I'm sure that's fine.
[3:58] So yeah, I just want some pebbles around him. I guess that's probably a bit much.
[4:05] There you go. And then just smooth it up some watch.
[4:12] And let's scatter pebbles to and then select the group and also for length.
[4:21] And just making bigger point six and 2000. And we got a rock pile.
[4:30] There we go. That's I think that's everything. Yeah, that is we're there. We're done. We got through.
[4:39] Right. Have fun with this. I cannot stop using it. I love using this. It's so easy to make stuff.
[4:47] So easy to make any. I tried mimicking real bold, doesn't it? Turned out to be pretty useful.
[4:54] As a actually as a tip, I discovered this because I was mucking around. I wasn't expecting this to
[4:59] happen. I wanted this to be white. So all I did for that, if I look, this is rock 31.
[5:05] We're in rock 31. So in my colors, sorry, my color ramps for edge where I just
[5:13] swapped them. So instead of black, you know, the left white. And there we go. That's another
[5:18] little pro tip. Sweet wicket. Have fun with this. I hope you do as much as I am. And I'll see you in
[5:25] the next one. Bye bye.



---

## Captured Frames

- [0:53] tutorials/frames/ns-rock-sculptor-guide---geometry-scatter/frame_000.jpg
- [1:36] tutorials/frames/ns-rock-sculptor-guide---geometry-scatter/frame_001.jpg
- [2:19] tutorials/frames/ns-rock-sculptor-guide---geometry-scatter/frame_002.jpg
- [3:18] tutorials/frames/ns-rock-sculptor-guide---geometry-scatter/frame_003.jpg
- [4:21] tutorials/frames/ns-rock-sculptor-guide---geometry-scatter/frame_004.jpg

---

## Structured Notes

> **Third-party add-on note:** This tutorial covers **NS Rock Sculptor**, a paid third-party Blender add-on by Nick Sayce (NS), not a stock Blender feature. Its panel tabs (Sculpt Settings, Edge Crease, Colour, Moss, Filters, Colour Ramps, Displacement, Bump, Geometry, Scatter — visible in the frame captures) are custom add-on UI, not core Blender node groups or modifiers. Do not confuse its "Geometry" and "Scatter" controls with stock Blender Decimate/particle workflows when consulting this entry — the add-on wraps them in its own presets and vertex-group logic.

### Core Technique
Decimating a sculpted NS Rock Sculptor rock down to a low-poly "pebble" mesh, then using the add-on's built-in Scatter tab (a wrapped particle-system workflow) to instance that pebble across a target surface with vertex-group-painted density control.

### Summary
Short overview of the last two tabs in the NS Rock Sculptor panel: Geometry and Scatter. Frame 000 shows a smooth-shaded decimated rock with its "Rock Distance Mask" vertex group highlighted in orange in the panel's vertex group list. Frame 001 shows the same rock after repeated decimation passes — visibly mangled, faceted low-poly topology with an orange-highlighted band, illustrating the "horrific topology" the video warns will break loop cuts. Frame 002 shows the blotchy white/pink discoloration that results from applying the add-on's Edge Wear (Edge Crease) effect to already-decimated geometry — the add-on can't resolve real edges on mangled topology, so Edge Wear reads as broken white patches. Frame 003 shows the Scatter tab's initial result: a plane with barely-visible, tiny scattered pebble dots (default scatter scale is too small). Frame 004 shows the final payoff — a dense, properly scaled rock pile built by layering two pebble presets with increased Number and Scale values.

### Key Steps
1. In the **Geometry** tab, decimate a finished sculpted rock (already quad-remeshed with a target face count set during sculpting, e.g. ~1000 faces) using the Decimate operator at roughly 0.1–0.2 ratio.
2. Click Decimate again (2-3 total passes) to progressively strip geometry for background/scatter use — the silhouette holds up reasonably well through 2-3 passes, but topology becomes unusable for further edits (no clean loop cuts, no texture painting).
3. **Warning:** decimating loses displacement fidelity — fine for small scattered pebbles, not for hero/close-up rocks.
4. **Warning:** apply the add-on's Edge Wear/Edge Crease effect *before* decimating, not after — on decimated geometry it can't find real edges and turns the surface white/blotchy (see Frame 002).
5. Switch to the **Scatter** tab. Add a plane as the scatter target, apply its transforms (Ctrl+A), and scale it up to the working area size.
6. Select a saved rock preset (e.g. "Pebbles 1" — the add-on only ships ~4 presets at time of recording; author says more will be added) and click Scatter to instance it via the add-on's particle-system wrapper on the plane.
7. Increase the Scatter tab's Number and Scale fields at the bottom of the panel — the default scatter is too small/sparse to see.
8. Paint a Vertex Group on the target plane (Weight Paint mode) to control where rocks scatter — e.g. leave a blank/low-weight area in the middle for a clear path.
9. Add a second preset ("Pebbles 2") with its own vertex group, and tune Length, Scale (~0.6), and Number (~2000) to build up a dense, layered rock pile combining both pebble types.
10. Pro tip mentioned: unexpected add-on results can become deliberate looks — e.g. swapping the black/white ends of the Edge Wear Colour Ramp on one rock ("Rock 31") inverted the wear pattern into a usable alternate look, discovered by accident.

### Nodes / Settings
- **NS Rock Sculptor add-on panel tabs** (custom N-panel UI, confirmed in frame captures): Sculpt Settings, Edge Crease, Colour, Moss, Filters, Colour Ramps, Displacement, Bump, Geometry, Scatter.
- **Geometry tab:** Decimate operator / ratio field (~0.1–0.2), repeatable.
- **Scatter tab:** rock preset picker (e.g. Pebbles 1, Pebbles 2), Scatter button, Number field, Scale field, Length field, per-preset Vertex Group assignment.
- **Vertex Groups referenced:** "Rock Distance Mask" (visible on the base rock in Frame 000/001) and separate Weight-Painted groups per scatter target used to mask scatter density.
- **Edge Wear / Edge Crease:** driven by a Colour Ramp (black/white positions swappable for inverted wear look).

### Difficulty
Beginner (short, low-complexity overview — main prerequisite is owning the paid add-on and having a sculpted rock ready from earlier steps in the series).

### Blender Version
Not stated verbally; viewport title bar in the captured frames is partially legible and appears to read Blender 5.1.x. Treat as approximate — cross-reference other NS Rock Sculptor Guide episodes from the same upload batch (2026-07-30) for corroboration.

### Tags
procedural, displacement, particles, organic, product-viz, beginner

---

## Related Tutorials
Part of the **NS Rock Sculptor Guide** series (10 episodes, all uploaded 2026-07-30) covering the NS Rock Sculptor add-on tab by tab. This episode covers the Geometry and Scatter tabs specifically.
- [NS Rock Sculptor Guide - Bump](ns-rock-sculptor-guide---bump.md) — same add-on/series, Bump tab.
- [NS Rock Sculptor Guide - Displacement](ns-rock-sculptor-guide---displacement.md) — same add-on/series, Displacement tab.
- [NS Rock Sculptor Guide - Colour Ramps](ns-rock-sculptor-guide---colour-ramps.md) — same add-on/series, Colour Ramps tab (directly relevant to the Edge Wear color-ramp tip in this episode).
- [NS Rock Sculptor Guide - Filters](ns-rock-sculptor-guide---filters.md) — same add-on/series, Filters tab.
- [NS Rock Sculptor Guide - Moss](ns-rock-sculptor-guide---moss.md) — same add-on/series, Moss tab.
- [NS Rock Sculptor Guide - Colour](ns-rock-sculptor-guide---colour.md) — same add-on/series, Colour tab.
- [NS Rock Sculptor Guide - Edge Crease](ns-rock-sculptor-guide---edge-crease.md) — same add-on/series, Edge Crease tab (directly relevant — this episode shows Edge Wear failing on decimated geometry).
- [NS Rock Sculptor Guide - Sculpt Settings](ns-rock-sculptor-guide---sculpt-settings.md) — same add-on/series, Sculpt Settings tab (covers the quad-remesh target face count referenced in this episode).
- [NS Rock Sculptor Guide - Presets](ns-rock-sculptor-guide---presets.md) — same add-on/series, Presets tab (relevant to the "only four presets" comment in this episode).
- [NS Infinite Rock Builder Guide - Main Controls](ns-infinite-rock-builder-guide---main-controls.md) — conceptual sibling add-on by the same author (Nick Sayce), same rock/procedural theme, different tool (formation-chain rock builder vs. sculpt-based Rock Sculptor).
