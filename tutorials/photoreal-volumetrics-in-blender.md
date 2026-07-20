---
title: Photoreal Volumetrics in Blender
source: YouTube
url: https://www.youtube.com/watch?v=0xZby2ObL6o
author: Nico Linde
ingested: 2026-07-18
blender_version: "Not specified (modern 4.x/5.x UI; version-agnostic)"
tags: [volume, materials, shaders, lighting, hdri, rendering, cycles, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/photoreal-volumetrics-in-blender/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Photoreal Volumetrics in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=0xZby2ObL6o)
**Author:** Nico Linde
**Duration:** 4m55s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Photo realistic volumetrics in lenders are actually very easy to do, if you know what you want and you know what you're doing.
[0:08] And the best thing is it's free and super quick to set up.
[0:11] But before we dive into the details, I cannot stress enough that volumetrics aren't going to save a bad scene.
[0:18] To prove to you that it really doesn't take much to make one, let's make one, very quickly.
[0:23] I created the mountain using the built-in A&T landscape add-on.
[0:26] This lickrock preset is my absolute favourite as it creates exactly the look I'm almost always going for.
[0:34] For the ground, I used another preset, but this time I chose large terrain because, well, I wanted a large terrain.
[0:40] Dextering landscapes is where, in my opinion, most people ruin their render right away because they are using procedural textures.
[0:47] That's great for games, and if you really know what you're doing, that's fine.
[0:51] But in most cases, I'm going for a different approach.
[0:53] And that is very quick and dirty.
[0:56] The internet is full of great pictures of all sorts of mountains and terrains.
[1:00] And when it comes to photorealism, nothing is going to be the real world.
[1:04] So as long as you don't introduce any crazy camera moves which you shouldn't do anyway,
[1:08] you can totally get away with projecting an image onto your geometry and tweaking your bees using proportional editing.
[1:14] I did the same for the ground using an aerial photo that was shot using a drone.
[1:18] To set the mood, I used a simple HDRI.
[1:21] Since we are going to use a lot of fog and haze later, the sky doesn't have to be perfect.
[1:26] Adding in a human silhouette to get a sense of scale really goes a long way.
[1:30] This particular one is a simple image I created in my journey.
[1:35] After adding a camera and adjusting the materials, we can finally talk about the reason you clicked on this video.
[1:41] Volume matrix.
[1:42] And there are three types that I use.
[1:45] Atmospheric haze, radians and VGBs.
[1:48] Method 1 is the basic haze.
[1:50] To add simple fog or haze, most people including me use a simple cube.
[1:55] Creating a new material, delete the principal bees de f shader and add a principal volume shader.
[2:00] The overall intensity is defined by the density and the emission.
[2:05] The key here is to use very small values like 0.001.
[2:09] To make it easier to control, I add a simple value node set to something like 0.001
[2:15] and feed that into the mouth node set to multiply.
[2:19] Then I plug that into the emission strength and density slot.
[2:24] Now I can easily control the overall fog amount with one slider.
[2:29] To blend everything together, I plugged an RGB node into the color and emission color slot.
[2:34] Now I can sample a color from the sky which instantly makes the whole thing more realistic.
[2:39] I usually use at least two of these cubes in my scenes.
[2:43] One overall haze and one in the distance to mimic the effect of atmospheric haze.
[2:48] If you look at reference photos, you often see that fog sort of piles up at the ground and fades away at the top.
[2:54] And for that, we are going to use ground fog.
[2:57] The easy approach to this would be to simply duplicate the cube and move it down.
[3:02] But instead, let's not.
[3:03] For smooth gradient, we'll add exactly that.
[3:06] A gradient node, controlled by a mapping node and a color ramp.
[3:09] Adjust the rotation and scale and that's really all you need.
[3:13] Bonus tip.
[3:16] If you want your mountains to look really high, duplicate the ground fog and rotate it so that the peaks of the mountains are covered in fog.
[3:24] But to really sell the effects, we need to add one more layer or realism.
[3:28] And for that, we are going to use clouds.
[3:30] If you want to make your clouds in blender, knock yourself out.
[3:33] But I'm going to use free VDBs.
[3:35] Jenga VFX has great and most importantly free packs you can get on their website.
[3:40] I recommend saving them to your asset browser because once you've used them, you are going to use them a lot.
[3:46] The material setup is almost identical to the one that I used for the basic haze.
[3:50] The only difference is that you need to plug in an attribute node into the emission color.
[3:55] Otherwise, you are going to light up the entire cloud.
[3:58] If you like using VDB like me, make sure to uncheck custom range in the render settings.
[4:03] Otherwise, the volumes in the distance are not going to show up in the render.
[4:07] The fun thing about these clouds is that you cannot only use them as clouds, but also as ground fog or haze.
[4:13] This helps to break up that overly smooth look you are getting from the gradient node.
[4:17] Little bonus tip.
[4:19] If you want to add movement to these clouds, try mixing in a noise texture and animating the location in the mapping node.
[4:26] It's not perfect, but very performance friendly and gets the job done most of the time.
[4:30] So after adding a few meshes in the foreground, tweaking the mountains and clouds and finally animating the camera,
[4:36] I got this, which isn't very exciting, so in the composite I added in some rain and snow as well as some colligrating and sound effects.
[4:45] And that's it.



---

## Captured Frames

- [0:26] tutorials/frames/photoreal-volumetrics-in-blender/frame_000.jpg
- [1:08] tutorials/frames/photoreal-volumetrics-in-blender/frame_001.jpg
- [2:15] tutorials/frames/photoreal-volumetrics-in-blender/frame_002.jpg
- [3:06] tutorials/frames/photoreal-volumetrics-in-blender/frame_003.jpg
- [3:20] tutorials/frames/photoreal-volumetrics-in-blender/frame_004.jpg
- [3:50] tutorials/frames/photoreal-volumetrics-in-blender/frame_005.jpg
- [4:03] tutorials/frames/photoreal-volumetrics-in-blender/frame_006.jpg
- [4:36] tutorials/frames/photoreal-volumetrics-in-blender/frame_007.jpg

---

## Structured Notes

### Core Technique
Three-layer photoreal volumetrics: cube-based atmospheric haze with a single-slider density/emission rig, gradient-driven ground fog, and free VDB clouds — all using tiny Principled Volume densities (~0.001) and sky-sampled colors.

### Summary
Nico Linde's fast volumetric recipe on a mountain scene (A.N.T. Landscape add-on: "lichen rock"-style preset for the mountain, "large terrain" for the ground; photo/aerial-image projection instead of procedural texturing, plus proportional-editing tweaks, an HDRI, and a human silhouette for scale). Three volume types: overall haze, distance haze, and VDB clouds. Key rig: Value node (≈0.001) → Math Multiply → both Density and Emission Strength of a Principled Volume, with one RGB color (sampled from the sky) into Color + Emission Color — one slider controls all fog. Ground fog uses Gradient + Mapping + Color Ramp instead of a second cube; VDB clouds (JangaFX free packs) need an Attribute(density) node into emission color and "custom range" unchecked in render settings so distant volumes render.

### Key Steps
1. Terrain: A.N.T. Landscape presets; texture by projecting real photos (mountain photo / drone aerial for ground) — no crazy camera moves; tweak with proportional editing. HDRI for mood; human-silhouette image card for scale.
2. Haze cube: new material → delete Principled BSDF → `Principled Volume`. Tiny values are key (~0.001).
3. One-slider rig: `Value` (0.001-ish) → `Math: Multiply` → into **both Density and Emission Strength**; `RGB` node → Color + Emission Color, color-picked from the sky. Use ≥2 cubes: overall haze + a distance cube for atmospheric depth.
4. Ground fog: same cube material + `Gradient Texture` controlled by `Mapping` + `Color Ramp` (adjust rotation/scale) — fog piles at the ground, fades up. Bonus: duplicate and rotate so peaks poke through fog to sell mountain height.
5. VDB clouds: free JangaFX packs; save to Asset Browser. Same material, but plug an `Attribute` node (density) into **Emission Color** — otherwise the whole cloud lights up uniformly.
6. Render settings: **uncheck Custom Range** (volumes) or distant VDBs won't render.
7. VDBs double as ground fog/haze to break the gradient's smoothness. Movement: mix a Noise Texture and animate the Mapping location (cheap, usually convincing).
8. Finish in compositor: rain/snow, color grading, sound.

### Nodes / Settings
- `Principled Volume` — Density ≈ 0.001–0.01, Emission Strength via shared multiplier
- `Value` → `Math: Multiply` → Density + Emission Strength (single-slider control)
- `RGB` (sky-sampled) → Color + Emission Color
- `Gradient Texture` + `Mapping` + `Color Ramp` — ground fog falloff
- `Attribute` (name: density) → Emission Color for VDBs
- Render settings: Volumes → Custom Range OFF
- A.N.T. Landscape add-on; JangaFX free VDB packs; Asset Browser

### Difficulty
Intermediate

### Blender Version
Not specified — modern 4.x/5.x UI; version-agnostic (Cycles implied for volumetric render).

### Tags
#volume #materials #shaders #lighting #hdri #rendering #cycles #intermediate

---

## Related Tutorials
- [3 Easy Lighting Setups | Blender Tutorial](3-easy-lighting-setups-blender-tutorial.md) — shares #volume #lighting #hdri
- [Perfect Textures in Blender - Works Every Time](perfect-textures-in-blender---works-every-time.md) — same author; environment-integration philosophy
- [Blender Tutorial - Create a Beautiful River Landscape in Blender | Free Addon](blender-tutorial-create-a-beautiful-river-landscape-in-blend.md) — shares landscape/HDRI workflow
