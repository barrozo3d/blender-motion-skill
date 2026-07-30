---
title: Blender PROCEDURAL BUILDING! | Geometry Nodes
source: YouTube
url: https://www.youtube.com/watch?v=VdxTlfLLe_s
author: SharpWind
ingested: 2026-07-30
blender_version: "Not specified (recent, modifier UI matches 4.x/5.x)"
tags: [geometry-nodes, procedural-generation, architecture, modifier-stack, asset-showcase]
extraction_status: complete
frames_dir: tutorials/frames/blender-procedural-building-geometry-nodes/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender PROCEDURAL BUILDING! | Geometry Nodes

**Source:** [YouTube](https://www.youtube.com/watch?v=VdxTlfLLe_s)
**Author:** SharpWind
**Duration:** 1m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] One asset, millions of variations.
[0:02] I'm not joking, I did the math.
[0:04] Using it is as simple as it gets.
[0:06] There's your assets and in the modifier stack, there's your controls.
[0:10] In the general shape tab, you can change the building dimensions,
[0:13] as well as make one of the walls blank to connect it to other buildings.
[0:16] In the colors tab, you can change the color of the ground, middle and top floors,
[0:21] change the brick type from old to modern for variation,
[0:23] and control the four different colors of the awnings on the building.
[0:27] Floor distribution lets you change things like the amount of upper floors,
[0:30] the ring frequency and ring offset,
[0:32] but also the gap frequency and its offset for both the X and the Y axes.
[0:36] As well as the fire escape stairs frequency and offset,
[0:39] but they get overwritten by the gaps since nobody can enter this.
[0:43] The details section let you adjust the door frequency,
[0:45] the ground floor window amount, and seed,
[0:48] the upper awning amount, and seed,
[0:50] the lower awning amount, and seed,
[0:51] as well as what percentage of them are extended or contracted.
[0:55] Plus a seed for that as well.
[0:57] The roof elements let you decide how many antennas, chimneys or AC units you want on the roof,
[1:02] as well as a seed for each, but also the types of AC units.
[1:06] Zero means all of them are small, one means all of them are big.
[1:09] Just be wary that the chimneys override the antennas and the AC units override the chimneys,
[1:14] so it's probably best to start at the bottom.
[1:16] The managed section isn't meant for you to be used, it's a geometry-node thing, just ignore it.
[1:21] If you wish to customize or replace parts of the building,
[1:23] just make the parts collection visible and modify the models.
[1:27] Just note that the front-facing wall must always be oriented this way,
[1:30] and be exactly 0.5 meters away from its origin point,
[1:33] and the corners must be oriented this way,
[1:36] and each side is 0.5 meters away from the origin.
[1:38] Yeah, get it, you have a template over here.
[1:41] I wanted to keep this asset really small, so most of the materials are very, very simple and procedural,
[1:46] and there's only six textures in total for the bricks,
[1:48] and an extra one for the supports on the bottom of the lower floor section.
[1:52] And that's the asset, the first hundred people to use my code on screen will get a 20% discount.
[1:56] Thanks for watching, stay sharp.



---

## Captured Frames

- [0:06] tutorials/frames/blender-procedural-building-geometry-nodes/frame_000.jpg
- [0:10] tutorials/frames/blender-procedural-building-geometry-nodes/frame_001.jpg
- [0:16] tutorials/frames/blender-procedural-building-geometry-nodes/frame_002.jpg
- [0:27] tutorials/frames/blender-procedural-building-geometry-nodes/frame_003.jpg
- [0:43] tutorials/frames/blender-procedural-building-geometry-nodes/frame_004.jpg
- [0:57] tutorials/frames/blender-procedural-building-geometry-nodes/frame_005.jpg
- [1:21] tutorials/frames/blender-procedural-building-geometry-nodes/frame_006.jpg

---

## Structured Notes

### Core Technique
A single pre-built geometry-nodes "Building_Generator" modifier drives an entire procedural apartment-building asset — one mesh with a `GeometryNodes` modifier exposing a large set of grouped, human-readable input controls (not a from-scratch build tutorial; this is a product showcase/usage guide for an asset the creator sells).

### Summary
SharpWind demonstrates the control panel of a paid procedural building asset for Blender. The whole building — brick facade, window rows, awnings, fire escapes, roof details — comes from one geometry-nodes modifier organized into six collapsible sections in the modifier stack: General Shape, Colors, Floor Distribution, Details, Roof Elements, and Manage. Each section exposes sliders/seeds so a huge number of building variations can be produced from one asset without touching the node tree itself. The video is a feature walkthrough for buyers, not a from-scratch node-building tutorial.

### Key Steps
1. Apply the `GeometryNodes` modifier (named `Building_Generator`) to the asset's base object — this is the only setup step; everything else is parameter tweaking.
2. **General shape** section: set `Width`, `Depth`, `Height`, and `BlankWallSelector` (an index picking which wall, if any, is left blank/flat so the building can butt up against a neighboring one).
3. **Colors** section: pick `Ground Floor Color`, `Floors Color`, `Top Color` via a standard Blender color-wheel picker (Linear/Perceptual + RGB/HSV toggle, Hue/Saturation/Value/Alpha fields, hex input), plus four independent `Awning Color 1-4` swatches; also a brick-type toggle between "old" and "modern" brick variants for extra visual variety.
4. **Floor Distribution** section: control upper-floor count, ring frequency/offset and gap frequency/offset (both X and Y axes), and fire-escape stair frequency/offset — note fire-escape placement is overridden wherever a gap already exists (gaps mean no wall to attach stairs to).
5. **Details** section: `Door Frequency`, `Ground Floor Window Amount` + its `Seed`, `Upper Awning Amount` + `Seed`, `Lower Awning Amount` + `Seed`, and separate percentage/seed controls for how many awnings appear extended vs. contracted.
6. **Roof Elements** section: counts (and per-type seeds) for antennas, chimneys, and AC units, plus an AC-unit size slider (0 = all small, 1 = all big). Overlap priority is roof-element-type dependent: chimneys override/replace antennas, AC units override chimneys — so the creator recommends configuring roof elements bottom-up (antennas first) to avoid pieces disappearing under higher-priority ones.
7. **Manage** section is explicitly internal/geometry-nodes bookkeeping — not meant to be touched by the user.
8. To customize beyond the exposed parameters: make the `Parts` collection visible and edit the source models directly, respecting strict placement conventions — the front-facing wall piece must keep its authored orientation and sit exactly 0.5m from its own origin; corner pieces likewise must keep their orientation and each side must be 0.5m from origin (the asset ships with a template object showing the expected pivot/orientation setup).
9. Materials are intentionally minimal for asset-file-size reasons: mostly simple procedural shaders, with only 6 total brick textures plus one extra texture for the lower-floor support elements.

### Nodes / Settings
Not a raw node-tree tutorial (the node graph itself is never shown) — the reusable pattern is the *organization*: group modifier-stack inputs into named, collapsible panel sections (General Shape / Colors / Floor Distribution / Details / Roof Elements / Manage) so a complex geometry-nodes asset stays usable without opening the node editor. Modifier panel fields observed: Width, Depth, Height, BlankWallSelector (General shape); Ground Floor Color, Floors Color, Top Color, Awning Color 1-4 (Colors); upper-floor/ring/gap/fire-escape frequency+offset pairs (Floor Distribution); Door Frequency, Ground Floor Window Amount/Seed, Upper/Lower Awning Amount/Seed, Lower Awnings Extended + Extension seed (Details).

### Difficulty
Beginner (as a user of the asset — just modifier-parameter tweaking, no node authoring required). The underlying node tree itself would be Advanced/Expert to build from scratch, but that construction isn't shown.

### Blender Version
Not specified on screen; modifier-panel styling is consistent with recent Blender 4.x/5.x.

### Tags
geometry-nodes, procedural-generation, architecture, modifier-stack, asset-showcase

---

## Related Tutorials
- `tutorials/easy-railing-generator-with-geometry-nodes-blender-52.md` — another parametric-architecture geometry-nodes asset (railings), shares tags: geometry-nodes, procedural-generation, architecture.
