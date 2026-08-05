---
title: Create a Photoreal Moon in minutes | 3D Tutorial | #blender secrets
source: YouTube
url: https://www.youtube.com/watch?v=iNL98QwGEmQ
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (Cycles displacement workflow, 2.9x-5.x)"
tags: [materials, shaders, displacement, rendering, cycles, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/create-a-photoreal-moon-in-minutes-3d-tutorial-blender-secrets/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Create a Photoreal Moon in minutes | 3D Tutorial | #blender secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=iNL98QwGEmQ)
**Author:** Blender Secrets
**Duration:** 2m47s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] In this video we'll recreate the Earth's moon using free textures.
[0:08] We'll also look at how to solve a common issue with textures on UV squares.


### Download textures [0:14]
**Transcript (timestamped):**
[0:14] First, download both the color texture and the height map of the moon surface from NASA's website.
[0:21] There are several download options for each. The higher resolution is especially important for the height map.
[0:27] You may want to rename these files to avoid confusion later.


### Add UV sphere [0:33]
**Transcript (timestamped):**
[0:33] In Blender, add a UV sphere.
[0:37] By default, Generate UVs is enabled, so there's no need to UV unwrap the sphere yourself.
[0:44] Right-click and choose Shade Smooth.
[0:47] Add a subdivision modifier and a displacement modifier to the sphere.
[0:53] As coordinates, choose UV.
[0:57] Load the height map as the displacement texture.
[1:01] Set its color space to non-color.
[1:05] You may have to tweak the displacement's strength value.
[1:09] Increase the amount of subdivisions to squeeze more detail out of the height map.


### Add material [1:14]
**Transcript (timestamped):**
[1:15] Switch to Material Preview in the 3D Viewport.
[1:19] In the Shader Editor, create a material for the sphere and add the color texture to it.
[1:25] It looks pretty cool, but there is an issue that you'll notice when you look closer at the poles of the sphere.
[1:31] When using an equirectangular texture on a UV sphere, you will see this ugly pinching of the texture at the poles.
[1:39] This wouldn't be an issue with a quad sphere, but fortunately equirectangular textures are meant to be used on a UV sphere.
[1:47] Fortunately, there's a simple solution.
[1:51] Instead of UV texture coordinates, set it to Generated instead.
[1:56] Then set Texture Interpolation to Smart and Production Method to Sphere.
[2:03] Unfortunately, this means the mapping of the displacement map and the color map are no longer the same.
[2:09] So remove the displacement modifier and add the height map with a displacement node instead.
[2:16] Set it to also use Smart Interpolation and Sphere Protection with Generated Mapping.
[2:22] In the Material Settings, set displacement to Displacement Only or Displacement and Bump.
[2:29] Now you can see the displacement in the Cycles rendered preview.
[2:33] As you can see, the pole pinching issue is greatly reduced.



---

## Captured Frames

- [0:50] tutorials/frames/create-a-photoreal-moon-in-minutes-3d-tutorial-blender-secrets/frame_000.jpg
- [1:10] tutorials/frames/create-a-photoreal-moon-in-minutes-3d-tutorial-blender-secrets/frame_001.jpg
- [1:25] tutorials/frames/create-a-photoreal-moon-in-minutes-3d-tutorial-blender-secrets/frame_002.jpg
- [1:35] tutorials/frames/create-a-photoreal-moon-in-minutes-3d-tutorial-blender-secrets/frame_003.jpg
- [2:00] tutorials/frames/create-a-photoreal-moon-in-minutes-3d-tutorial-blender-secrets/frame_004.jpg
- [2:30] tutorials/frames/create-a-photoreal-moon-in-minutes-3d-tutorial-blender-secrets/frame_005.jpg

---

## Structured Notes

### Core Technique
Build a photoreal Moon from free NASA color/height textures on a UV Sphere, then fix the classic equirectangular-texture pole-pinching artifact by switching from UV to Generated texture coordinates with Sphere projection (moving displacement into the shader graph as a Displacement node instead of a mesh modifier, since the two mapping methods can no longer share the same UV-based displacement).

### Summary
Frame 000 shows the base setup: a UV Sphere with the Add Modifier menu open, Displace highlighted — about to add displacement on top of an already-present Subdivision modifier. Frame 001 shows the resulting Displace modifier's settings: Coordinates = UV, Direction Normal, Strength 0.062, Midlevel 0.500, stacked below a Catmull-Clark Subdivision (Levels Viewport/Render 6). Frame 002 shows the first full result: the sphere now has both the crater height-map displacement and the color texture applied via a Shader Editor graph (Image Texture → Base Color of a Principled BSDF), looking convincingly moon-like from this angle. Frame 003 shows the actual problem described in the transcript, captured perfectly: a dramatic starburst/pinwheel distortion where all texture detail converges into a single point at the sphere's pole — the classic equirectangular-on-UV-sphere pinching artifact. Frame 004 shows the fix in progress: a Texture Coordinate → Mapping node chain with the Mapping node's Projection type set to **Sphere** (highlighted), feeding the color texture — pinching is visibly reduced here compared to frame 003 but the displacement (still UV-mapped via modifier) is now mismatched. Frame 005 shows the final payoff: a close-up Cycles-rendered crater surface with no visible pinching, natural-looking bump/displacement, and a Shader Editor graph now including a Displacement node chain (Base Color / height map both wired through Generated + Sphere-projected coordinates) feeding the Material Output's Displacement socket.

### Key Steps
1. Download both a color texture and a height map of the Moon's surface from NASA's website — grab the height map at the highest resolution available, since detail there matters most; consider renaming both files for clarity.
2. Add a UV Sphere in Blender (Generate UVs is on by default, so no manual unwrap is needed at this stage); Shade Smooth it.
3. Add a Subdivision Surface modifier, then a Displace modifier below/above it as needed; set the Displace modifier's Coordinates to UV; load the height map as its texture and set that image's Color Space to Non-Color (height data isn't color data); tweak the Strength value to taste, and increase Subdivision levels to resolve finer height-map detail.
4. Switch Viewport Shading to Material Preview; in the Shader Editor, build a material with the color texture plugged into Base Color.
5. **Identify the pole-pinching problem:** an equirectangular (2:1 lat/long) texture on a UV Sphere shows ugly pinching/distortion right at the poles — this is a known mismatch, since equirectangular textures are technically meant for UV spheres (a Quad Sphere wouldn't have this specific issue but isn't equirectangular-compatible the same way).
6. **Fix — switch to Generated + Sphere-projected coordinates:** on the color texture's mapping, change Vector coordinates from UV to Generated; set Texture Interpolation to Smart and the Mapping node's Projection Method to Sphere.
7. Because this breaks the shared mapping between the color texture and the modifier-based UV displacement, remove the Displace modifier entirely and instead bring the height map into the Shader Editor as a Displacement node, feeding Material Output's Displacement socket — set it to use the same Smart Interpolation + Sphere Projection + Generated Mapping as the color texture so both stay aligned.
8. In the Material Settings panel, set Displacement to "Displacement Only" or "Displacement and Bump" so Cycles actually renders true geometric displacement (visible in the Cycles rendered preview) rather than just a normal-map-style bump. The pole-pinching artifact is now greatly reduced.

### Nodes / Settings
- **Modifiers (initial approach, later replaced):** Subdivision Surface (Catmull-Clark), Displace (Coordinates=UV, Direction=Normal, Strength, Midlevel) — this modifier is removed once switching to shader-based displacement.
- **Shading:** Principled BSDF (Base Color = color texture), Texture Coordinate → Mapping (Vector Type: UV vs. Generated; Projection: Sphere) → Image Texture (Interpolation: Smart), Displacement node → Material Output Displacement socket.
- **Material Settings:** Displacement mode = Displacement Only / Displacement and Bump (required for Cycles to render true geometric displacement from the shader graph).
- **Texture setup:** height-map Color Space = Non-Color.
- **Source:** NASA's public Moon color-texture and height-map downloads (multiple resolution options).

### Difficulty
Intermediate

### Blender Version
Not specified — Cycles-based displacement workflow with modern Mapping node Projection types, consistent with Blender 2.9x-5.x.

### Tags
materials, shaders, displacement, rendering, cycles, intermediate

---

## Related Tutorials
- [Blender Secrets - Blender GIS (Extra Bonus Tutorial)](blender-secrets---blender-gis-extra-bonus-tutorial.md) — shares materials, rendering, cycles; same channel, complementary real-world-data-to-3D-terrain technique (satellite/height-map displacement, applied to Earth terrain instead of the Moon).
- [Blender Secrets - 4 tips for Photoreal Lighting](blender-secrets---4-tips-for-photoreal-lighting.md) — shares materials, shaders, cycles, intermediate; same channel, complementary photoreal-rendering fundamentals.
