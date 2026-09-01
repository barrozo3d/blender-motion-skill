---
title: 30 little-known Blender tricks
source: YouTube
url: https://www.youtube.com/watch?v=5_Jy97TzZuM
author: Robin Squares
ingested: 2026-07-19
blender_version: "Blender 5.0.0 -- observed in frame_004"
tags: [materials, shaders, procedural, compositing, rendering, cycles, eevee, geometry-nodes, cloth, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/30-little-known-blender-tricks/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# 30 little-known Blender tricks

**Source:** [YouTube](https://www.youtube.com/watch?v=5_Jy97TzZuM)
**Author:** Robin Squares
**Duration:** 12m17s | 33 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Match materials [0:00]
**Transcript (timestamped):**
[0:00] I am Robin, these are tips, let's not overthink it.
[0:05] Say you want to match this material to that material.
[0:09] Sample the wrong color, sample the right color, set it to divide, and then divide that by
[0:14] the base color.
[0:16] And there you go, materials match.


### Steal a GIF [0:18]
**Transcript (timestamped):**
[0:19] You can steal any GIF, just drag it into Blender, right click, press trace image to
[0:24] grease pencil, set the mode to sequence, and GIFs are not protected by copyright law,
[0:30] so right.


### Texture bombing [0:32]
**Transcript (timestamped):**
[0:32] Ever heard of texture bombing?
[0:34] Add a texture coordinates node, plug it into a Voronoi texture, and then add a noise texture
[0:40] as well, and mix that very faintly into the vector, which is going to warp the Voronoi.
[0:46] Take a UV map into an image texture and scale it down using a mapping node, and here's
[0:51] the issue.
[0:52] You can see that it's clearly the same image repeating over and over again.
[0:56] Here's what you do, vector math, plug that Voronoi thing into the vector math with add,
[1:03] and then that will offset the texture per cell.
[1:06] You can even rotate it with a vector rotate as well.
[1:09] And now you cannot tell that it's the same texture just repeated over and over again.


### Moody Pinterest [1:13]
**Transcript (timestamped):**
[1:16] Cosmos.so is Pinterest, but moody.
[1:20] You can also filter out AI images, which is really handy nowadays.
[1:24] Yes, that is not a Blender tip.
[1:27] Get click baited.


### Instant Cycles renders [1:28]
**Transcript (timestamped):**
[1:30] Bake the diffused light to a new texture and then set the base color to black, and then
[1:35] multiply that texture by the base color of the material.
[1:39] Plug it into emission, this object will now render instantly, with no sacrifice in quality,
[1:47] and you can even change the texture afterwards.
[1:50] So what's the catch?
[1:53] You can't move the light or the object anymore.


### Open a folder [1:58]
**Transcript (timestamped):**
[1:58] Nothing's free.
[1:59] Alt clicking on the folder icon opens that folder in Windows.
[2:04] On Mac, who knows.
[2:07] I want this model on here.
[2:10] So I place a lattice on the bottom, bind the object to that lattice, and then shrink wrap


### Shrinkwrap an object [2:11]
**Transcript (timestamped):**
[2:15] the lattice to the surface.
[2:20] A quick composition tip here.


### Composition tip [2:21]
**Transcript (timestamped):**
[2:22] The image is about what's in the middle.
[2:26] So this image is about the lighthouse.
[2:29] But when we shift it over, it's not quite just about the lighthouse anymore.
[2:33] Now it's about the lighthouse's relation to the ocean.
[2:37] If we shift to the other side, now it's about the path leading up to the lighthouse.
[2:43] If we zoom out and move it over a bit, now it's about how small the lighthouse is in
[2:50] the world.
[2:51] That is big, right?
[2:52] Over here it's about the spit of land, basically, and the lighthouse is just like coincidental
[2:57] to it.
[2:58] It's actually a really good technique to look for what's in the middle and you know
[3:01] what the image is about.


### GPU refresh [3:02]
**Transcript (timestamped):**
[3:03] When your computer has been on for a full day, viewports lag and renders crash.
[3:08] We start your GPU on Windows by pressing the Windows button, Ctrl-Shift-B, you will
[3:13] hear R, and the screen will blink and you're good as new.
[3:18] It's even safe to do this in the middle of a render.


### Roughness control [3:20]
**Transcript (timestamped):**
[3:22] This setup replicates Substance Designer's Histogram Range node.
[3:26] And it's so, so good for adjusting roughness.
[3:30] Top Value node basically adjusts the roughness level, and the bottom one adjusts the variation
[3:38] in it.
[3:39] So it's basically kind of like a brightness contrast, but tailor made for roughness channels.


### Get more tips [3:46]
**Transcript (timestamped):**
[3:46] That's 10, 20 more to go.
[3:48] And by the way, all these tips are from my newsletter, which is free, comes out every
[3:53] week.
[3:54] If you like my videos, I think you'll like that too.


### Cloth topology [3:56]
**Transcript (timestamped):**
[3:58] These fabrics have the exact same cloth settings, but they look different from each other.
[4:04] Turn a subdivided plane 45 degrees and then cut out your shake then.
[4:09] Fix the edges with a quick merge by distance.
[4:12] This cloth will fall with more like interesting folds than like a default straight topology
[4:18] cloth.
[4:19] You can also try a decimated plane for like a wrinkly look.


### Realistic smudges [4:24]
**Transcript (timestamped):**
[4:25] When adding grime to glass, don't just add a roughness map, instead make a completely
[4:31] separate shader that looks like fatty smudges and then mix that over.
[4:36] You'll get much more realistic material layering.
[4:39] This goes for all glossy materials, not just glass, but like chrome, etc.


### Custom render passes [4:44]
**Transcript (timestamped):**
[4:45] You can actually make any texture into a render pass.
[4:48] Just add an AOV output node in the shader and plug it in there.
[4:52] And then in the view layer properties, add a shader AOV with exactly the same name.
[4:59] Very useful for compositing.
[5:01] And yes, Geometry nodes can output attributes to shaders, which can then be AOVs.
[5:07] It gets kind of ridiculous.


### Better color grading [5:10]
**Transcript (timestamped):**
[5:11] In the compositor, put all of your color grading between two convert color space nodes.
[5:16] One going from working color space and two Filmic Log and then back.
[5:22] Anything you put in between those will look so much better than if you didn't.
[5:27] If you want some lovely grading presets, I made a toolkit called Grades.
[5:32] It does film emulation, grading has a bunch of presets.
[5:36] Link is where you'd expect.


### Text editor [5:38]
**Transcript (timestamped):**
[5:40] Blender has a text editor.
[5:42] I use this to communicate when I work in a team.
[5:46] You can put like to-do lists, changelogs, mild insults.
[5:51] And even in any node editor, you can add a frame and then add text into that frame to
[5:56] explain your nules.


### Batch rename files [5:58]
**Transcript (timestamped):**
[5:59] When you render 200 images with the wrong name, download bulk rename utility.
[6:06] It looks insane.
[6:08] I know, but you only need this tiny window.
[6:11] This is search and replace.
[6:14] It's free for personal use, absolute life saver.


### Batch rename objects [6:19]
**Transcript (timestamped):**
[6:20] F2 renames an object.
[6:23] Control F2 batch renames.
[6:25] And you have find and replace here too.


### Render fog fast [6:29]
**Transcript (timestamped):**
[6:29] Fog renders super slow in cycles, but it renders real quick in Eevee, so let's use the best
[6:36] of both worlds, eh?
[6:38] Put the fog in a new collection and set it to indirect only.
[6:42] Then make a new scene as a linked copy.
[6:46] Turn off indirect only.
[6:48] Set this scene to render with Eevee and output a volume pass.
[6:54] Then render both scenes, one with cycles, one with Eevee.
[6:59] And pull both renders into the compositor.
[7:02] Mix them with blend mode add.
[7:04] It looks pretty similar to a pure cycles render, but it renders in a fraction of the time.


### Align weird angles [7:09]
**Transcript (timestamped):**
[7:10] Make a triangle, snap it to 3 points on a model, and then parent the model to the triangle
[7:15] vertices.
[7:16] It sticks.
[7:18] So snap the triangle points to something else and thereby align whatever to whatever.


### How to number your shots [7:23]
**Transcript (timestamped):**
[7:23] When you number your shots, don't go shot 1, shot 2, shot 3.
[7:30] Column shot 10, shot 20, and shot 30.
[7:34] Because then, when you need to insert a new shot in between, you can call that 25 without


### Help choose my next video [7:41]
**Transcript (timestamped):**
[7:41] breaking everything.
[7:42] That's 20.
[7:43] You're still here.
[7:45] Maybe you want to give me some feedback.
[7:46] I have made a long list of video ideas.
[7:50] And I want to know which ones you're interested in.
[7:53] So go to the link below to cast your vote.
[7:56] In my experience, the audience knows best.


### Make any texture tile [8:00]
**Transcript (timestamped):**
[8:01] You can make any image into a tiling image.
[8:04] Put the texture on a plane, unwrap that plane, and pick a square section of the texture in
[8:09] the UV editor.
[8:11] And then make a 3x3 grid of the plane using array modifiers.
[8:15] Now you go to texture pink mode, and in the tools you have a clone stamp tool.
[8:20] This clone stamp tool works by sampling from where the 3D cursor is, and painting where
[8:24] you click.
[8:25] So you can shift right click to place your 3D cursor around, and then it's a matter
[8:29] of just painting out the edges and making sure that things flow smoothly over into each
[8:33] other.


### Smoothing nodes [8:34]
**Transcript (timestamped):**
[8:34] When you're done, you can bake it to a new texture and save it to your drive.
[8:40] This geometry notes setup smooths geometry.


### What noise threshold? [8:44]
**Transcript (timestamped):**
[8:45] When rendering, use noise threshold.
[8:47] That ensures an even level of quality across the entire image.
[8:52] But what noise threshold to choose?
[8:54] I made you a cheat sheet.
[8:56] So 0.01 is good for most cases, if denoised.
[9:02] 0.0025 is good for higher end production, if denoised.
[9:07] If you download the cheat sheet, there's also a bonus tip for you at the bottom.
[9:12] Something that everyone who renders professionally should know.


### How black, how white? [9:15]
**Transcript (timestamped):**
[9:16] The material color slider goes all the way from black to white, but real objects don't,
[9:23] except for like Vanta black and Justin Bieber's teeth.
[9:27] This shirt is about 0.2, and white printer paper is around 0.9.
[9:33] So for realistic objects, try to stay like within that range.


### Node search [9:38]
**Transcript (timestamped):**
[9:39] When your node graph gets thick, press ctrl f to search.
[9:44] It even finds where you've used attributes and stuff.
[9:47] Save your renders as EXRs with DWAB compression at 60% quality.


### Save your render as... [9:48]
**Transcript (timestamped):**
[9:54] It is way smaller than PNG and way higher quality than JPEG.
[10:00] Heck, even zip compression, which is lossless, is still way, way smaller than PNGs.
[10:07] For Tons sake, don't render PNG.


### Stronger thin film [10:09]
**Transcript (timestamped):**
[10:11] Thin film is awesome, but it's not obvious how to make it stronger, because that would
[10:17] break the laws of physics.
[10:19] So let's make a black material with IOR 0.
[10:23] In thin film, set the thickness somewhere between 50 and 1000.
[10:28] Now set up a repeat zone with an ad shader like this.
[10:32] The iterations will boost the thin film effect.
[10:35] Mix the result with your base material and now adjust the thickness to cycle the color
[10:39] spectrum.


### Sunlight fringe [10:40]
**Transcript (timestamped):**
[10:41] When you light an interior with a sun, here's a pretty cool trick.
[10:45] You can use nodes on that sun and then add a color node and put that into a group.
[10:51] Then duplicate the sun and invert the color of that sun.
[10:55] So you're now back to pure white.
[10:58] But now increase the angle of one of the suns and you'll see a little colored fringe around
[11:04] the edge of the light.
[11:07] Then control that color inside of the node group you just made.


### Break up flat colors [11:11]
**Transcript (timestamped):**
[11:12] In a very large texture, add a large scale noise as well and split it into R, G and B.
[11:18] Add a hue saturation value node and then plug the red, green and blue channels into the
[11:23] respective slots and remap the ranges to suit your liking.
[11:28] And then enjoy the large scale variation across the whole surface.


### Instant hexagons [11:32]
**Transcript (timestamped):**
[11:33] Select a grid and in Geometry Nodes add a dual mesh node.
[11:37] Instant hexagons as long as you skew it a little bit with a skew tool.
[11:42] Dual mesh on an icosphere is instant force field shield.
[11:47] Dual mesh on a decimated Suzanne, creature scales.
[11:50] And that is 30.


### Goodbye [11:51]
**Transcript (timestamped):**
[11:52] If you loved the video, please let me know.
[11:54] If you hated it, let me know that too.
[11:57] It hurts my feelings but it's good for the algorithm.
[11:59] Speaking of the algorithm, it thinks you will enjoy this video next.



---

## Captured Frames

- [1:04] tutorials/frames/30-little-known-blender-tricks/frame_000.jpg
- [3:32] tutorials/frames/30-little-known-blender-tricks/frame_001.jpg
- [4:12] tutorials/frames/30-little-known-blender-tricks/frame_002.jpg
- [4:55] tutorials/frames/30-little-known-blender-tricks/frame_003.jpg
- [7:02] tutorials/frames/30-little-known-blender-tricks/frame_004.jpg
- [8:25] tutorials/frames/30-little-known-blender-tricks/frame_005.jpg
- [10:31] tutorials/frames/30-little-known-blender-tricks/frame_006.jpg
- [11:44] tutorials/frames/30-little-known-blender-tricks/frame_007.jpg

---

## Structured Notes

### Core Technique
A rapid-fire collection of 30 workflow, shading, compositing, and rendering tricks — the highest-value ones being texture bombing (per-cell texture offset via Voronoi), a Substance-style "histogram range" roughness control group, hybrid Cycles+Eevee fog rendering, shader AOV render passes, and Dual Mesh instant hexagons.

### Summary
Robin Squares runs through 30 short, mostly independent tips spanning shading (texture bombing, material matching by color division, layered smudge shaders, thin-film boosting via repeat zones, large-scale color variation via noise→HSV), rendering (noise-threshold cheat sheet, EXR/DWAB output, baked-emission "instant renders", hybrid Cycles/Eevee fog compositing), compositing (Filmic Log grading sandwich, shader AOVs), and workflow (Ctrl+F2 batch rename, F2 rename, Ctrl+F node search, lattice shrinkwrap, triangle-parent alignment, shot numbering by tens). Each tip is 10–40 seconds; the video is a checklist to raid rather than a single build.

### Key Steps
1. **Match materials** — sample wrong + right colors, Divide the two, multiply/divide into base color to align two materials' albedo.
2. **Texture bombing** [frame_000, 1:04] — Texture Coordinate → Voronoi, mix a faint Noise into the vector to warp cells; then Vector Math (Add) offsets an image texture per Voronoi cell (optional Vector Rotate per cell) so tiling repetition disappears.
3. **Instant Cycles renders** — bake diffuse light to a texture, set base color black, multiply baked texture by base color, plug into Emission; renders instantly but light/object become static.
4. **Histogram-range roughness control** [frame_001, 3:32] — node group replicating Substance Designer's Histogram Range: Level (0.520) and Range (0.500) Value nodes feed Subtract/Add into a clamped Map Range (From 0–1) on the roughness input — "brightness/contrast tailor-made for roughness".
5. **Cloth topology** [frame_002, 4:12] — rotate a subdivided plane 45°, cut your shape, Merge by Distance; diagonal topology falls with more interesting folds; a decimated plane gives a wrinkly look.
6. **Shader AOV render passes** [frame_003, 4:55] — add AOV Output node in the shader (e.g. name "grunge"), add a matching Shader AOV in View Layer properties; Geometry Nodes attributes can feed shaders → AOVs.
7. **Filmic Log grading sandwich** — in the compositor, wrap all color grading between two Convert Colorspace nodes (working space → Filmic Log → back).
8. **Hybrid fog rendering** [frame_004, 7:02] — fog collection set to Indirect Only in the Cycles scene; linked-copy scene renders the volume pass in Eevee; Mix (Add) the two Render Layers in the compositor for near-Cycles quality at a fraction of the time.
9. **Make any texture tile** [frame_005, 8:25] — texture on unwrapped plane, 3×3 Array modifier grid, Texture Paint clone stamp (samples from 3D cursor, Shift+RMB to place it) to paint out seams, then bake to a new texture.
10. **Stronger thin film** [frame_006, 10:31] — black material with IOR 0, thin film thickness 50–1000, Repeat Zone with Add Shader inside to boost the effect through iterations, mix over the base material.
11. **Instant hexagons** [frame_007, 11:44] — Geometry Nodes Dual Mesh on a grid (skewed slightly) = hexagons; on an icosphere = force-field shield; on a decimated Suzanne = creature scales.
12. **Workflow one-liners** — Alt-click folder icon opens it in Explorer; Win+Ctrl+Shift+B restarts the GPU driver (safe mid-render); F2 rename / Ctrl+F2 batch rename with find-and-replace; Ctrl+F searches node graphs; number shots 10/20/30 to leave insertion room; realistic albedo stays ~0.2 (dark cloth) to ~0.9 (printer paper); save renders as EXR with DWA(B) compression instead of PNG.

### Nodes / Settings
- Texture bombing: Texture Coordinate, Voronoi Texture, Noise Texture (faint vector mix), Mapping, Image Texture, Vector Math (Add), Vector Rotate
- Histogram range group: Value ("Level" 0.520), Value ("Range" 0.500), Subtract, Add (both clamped), Map Range (Float, Clamp, From Min 0.000 / From Max 1.000) → Roughness; scene used Cycles GPU Compute, Noise Threshold 0.0100, Max Samples 4096
- AOV pass: AOV Output (Name: "grunge", Color) after Mapping/Image Texture (Box projection, Blend 0.200) + Map Range; View Layer Properties → Shader AOV (same name)
- Fog composite: two Render Layers (Cycles scene + Eevee linked-copy scene, volume/indirect-only split), Mix node set to Add
- Thin film boost: Principled thin film thickness 50–1000, IOR 0 black base, Repeat Zone (Iterations) containing Add Shader
- Color variation: Noise Texture (large scale) → Separate Color → Hue/Saturation/Value per R/G/B channel
- Grading: Convert Colorspace (working → Filmic Log) … grading nodes … Convert Colorspace (Filmic Log → working)
- Render output: EXR, DWAB compression, ~60% quality (or lossless ZIP) instead of PNG; noise threshold 0.01 (general, denoised) / 0.0025 (high-end, denoised)
- GeoNodes: Dual Mesh (Keep Boundaries option visible) on Grid / Icosphere / decimated mesh

### Difficulty
Intermediate

### Blender Version
Not specified (thin film + shader repeat zone imply 4.5+; modern 4.x/5.x UI throughout)

### Tags
materials, shaders, procedural, compositing, rendering, cycles, eevee, geometry-nodes, cloth, intermediate

---

## Related Tutorials
- [Doing Surface Imperfections Right | Vray, Cycles, Arnold..](doing-surface-imperfections-right-vray-cycles-arnold.md) — same layered-smudge-shader philosophy for glossy surfaces (tip 13) and roughness-map theory
- [Perfect Textures in Blender - Works Every Time](perfect-textures-in-blender---works-every-time.md) — shares materials/shaders/procedural/rendering/cycles tags; complementary texture-realism workflow
- [3 Easy steps to make Realistic Materials](3-easy-steps-to-make-realistic-materials.md) — shares materials/shaders/procedural/cycles tags; realistic-material quick wins in the same spirit
- [A FULL Blender Compositor Course!](a-full-blender-compositor-course.md) — deep dive for the compositing tips here (grading sandwich, AOVs, render-layer mixing)
