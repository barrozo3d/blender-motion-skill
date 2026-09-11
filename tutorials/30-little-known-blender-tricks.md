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
frame_count: 29
frame_status: complete
grounding: key-steps-anchored (30/30 steps, 2026-09-11)
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

- [0:14] tutorials/frames/30-little-known-blender-tricks/frame_000.jpg
- [0:25] tutorials/frames/30-little-known-blender-tricks/frame_001.jpg
- [1:04] tutorials/frames/30-little-known-blender-tricks/frame_002.jpg
- [1:21] tutorials/frames/30-little-known-blender-tricks/frame_003.jpg
- [1:44] tutorials/frames/30-little-known-blender-tricks/frame_004.jpg
- [2:05] tutorials/frames/30-little-known-blender-tricks/frame_005.jpg
- [2:16] tutorials/frames/30-little-known-blender-tricks/frame_006.jpg
- [2:43] tutorials/frames/30-little-known-blender-tricks/frame_007.jpg
- [3:34] tutorials/frames/30-little-known-blender-tricks/frame_008.jpg
- [4:11] tutorials/frames/30-little-known-blender-tricks/frame_009.jpg
- [4:35] tutorials/frames/30-little-known-blender-tricks/frame_010.jpg
- [4:58] tutorials/frames/30-little-known-blender-tricks/frame_011.jpg
- [5:25] tutorials/frames/30-little-known-blender-tricks/frame_012.jpg
- [5:49] tutorials/frames/30-little-known-blender-tricks/frame_013.jpg
- [6:09] tutorials/frames/30-little-known-blender-tricks/frame_014.jpg
- [6:24] tutorials/frames/30-little-known-blender-tricks/frame_015.jpg
- [6:51] tutorials/frames/30-little-known-blender-tricks/frame_016.jpg
- [7:16] tutorials/frames/30-little-known-blender-tricks/frame_017.jpg
- [7:32] tutorials/frames/30-little-known-blender-tricks/frame_018.jpg
- [8:18] tutorials/frames/30-little-known-blender-tricks/frame_019.jpg
- [8:39] tutorials/frames/30-little-known-blender-tricks/frame_020.jpg
- [9:01] tutorials/frames/30-little-known-blender-tricks/frame_021.jpg
- [9:33] tutorials/frames/30-little-known-blender-tricks/frame_022.jpg
- [9:42] tutorials/frames/30-little-known-blender-tricks/frame_023.jpg
- [9:59] tutorials/frames/30-little-known-blender-tricks/frame_024.jpg
- [10:26] tutorials/frames/30-little-known-blender-tricks/frame_025.jpg
- [10:57] tutorials/frames/30-little-known-blender-tricks/frame_026.jpg
- [11:22] tutorials/frames/30-little-known-blender-tricks/frame_027.jpg
- [11:47] tutorials/frames/30-little-known-blender-tricks/frame_028.jpg

---

## Structured Notes

### Core Technique
A rapid-fire run through the video's own 30 tips, each one self-contained — the substantial ones being texture bombing via Voronoi-offset image lookup, a Substance-style "Histogram range" node group for roughness, a Filmic-Log grading sandwich in the compositor, shader AOVs, hybrid Cycles/Eevee rendering, and Dual Mesh for instant hexagons.

### Summary
12m17s, 33 chapters, **Blender 5.0.0** throughout (status bar, e.g. [frame_004]). Robin Squares delivers thirty short, mostly independent tips spanning shading, rendering, compositing and workflow. Each tip runs 10–40 seconds, so the value of this entry is as a checklist to raid rather than a single build — which is why the Key Steps below follow the video's own chapter list one-for-one instead of summarising it. Several tips the earlier transcript-written version of these notes missed entirely are recovered here from the frames: **Steal a GIF** (Trace Image to Grease Pencil) [frame_001], **Shrinkwrap an object** onto a surface with a Lattice [frame_006], **Smoothing nodes** [frame_020], **Sunlight fringe** [frame_026], and the physical albedo reference with its actual picker values [frame_022].

Three corrections the frames force on the old notes. The Shader AOV is type **Value**, not Color [frame_011]. "Batch rename files" is not Ctrl+F2 — that chapter demonstrates the third-party Windows tool **Bulk Rename Utility** [frame_014]; Ctrl+F2 is the *next* chapter, Blender's own Batch Rename [frame_015]. And the thin-film tip does not set "IOR 0" — it sets Specular **IOR Level 0.000** on a black base, with the Thin Film block's own **IOR 1.330** [frame_025].

### Key Steps
1. **Match materials** — sample the wrong and right colours, feed both into a **Divide** node (`Color`, `Divide`, Clamp Result off, Clamp Factor on, Factor `1.000`) and route the result into the Principled BSDF's Base Color; the Roughness input keeps its `concrete_raw_pa…` image [frame_000].
2. **Steal a GIF** — `Object ▸ Trace Image to Grease Pencil`: Target Object `New Object`, Radius `0.010`, Color Threshold `0.500`, Turn Policy `Minority`, Mode `Single` or **`Sequence`** (Sequence is what turns an animated GIF into animated Grease Pencil), plus a Trace Frame field [frame_001].
3. **Texture bombing** — `Texture Coordinate` → `Voronoi Texture` (3D, F1, Euclidean, Normalize on) → `Vector Math (Add)` offsets the image lookup per Voronoi cell; a `Mapping` node at Scale `0.010 / 0.010 / 0.010` sets the cell size, and the image (`mossy_cliff_rock_basecolor.png`) is set to **Box** projection with **Blend `0.100`** so the per-cell copies merge [frame_002].
4. **Moody Pinterest** — collect reference on **Cosmos** rather than Pinterest; the grid view shown is the one to build boards in [frame_003].
5. **Instant Cycles renders** — bake the lighting down: Render Properties ▸ **Bake**, `Bake Type: Diffuse`, `View From: Above Surface`, Influence Contributions **Direct ✓ Indirect ✓ Color ✗**, `Target: Image Textures` with `Clear Image` on, Margin `Adjacent Faces` at `16 px` [frame_004]. The baked texture then drives an Emission shader, so the frame renders instantly but the lighting is frozen.
6. **Open a folder** — Alt-click a path's folder icon to open it in Explorer; the render output here is an EXR sequence `0001.exr…0040.exr` under `…\Blender\tmp\render` [frame_005].
7. **Shrinkwrap an object** — give a **Lattice** a **Shrinkwrap** modifier with `Wrap Method: Nearest Surface Point`, `Snap Mode: On Surface`, `Target:` the mesh to hug, `Offset 0 m`, then move the lattice along an axis (`G`, `Z`) to slide the deformed object across the surface [frame_006].
8. **Composition tip** — before lighting, write the one sentence the image is about ("IMAGE IS ABOUT: Path to Lighthouse") and cut anything that does not serve it [frame_007].
9. **GPU refresh** — `Win+Ctrl+Shift+B` restarts the graphics driver without killing Blender, safe to use mid-render [no frame: the chapter at 3:02–3:20 is talking head only; the shortcut has no on-screen demonstration].
10. **Roughness control** — a **"Histogram range"** node group rebuilding Substance Designer's operator: a `Level` Value node (shown mid-drag at `-0.410`) and a `Range` Value node (`0.500`) feed a `Subtract` and an `Add` (both **Clamp** on), which drive a **`Map Range`** (Float, Linear, Clamp on, From Min `0.000`, From Max `1.000`) into Roughness — brightness/contrast tailor-made for a roughness map [frame_008].
11. **Cloth topology** — rotate a subdivided plane 45°, cut the shape, then `M ▸ ` **Merge ▸ By Distance** to weld the cut edge; the diagonal topology folds more interestingly than a square grid [frame_009].
12. **Realistic smudges** — layer the smudges as their own shader: a `Fingerprints004_OVERLAY_VAR1_3K` image (Linear, Flat, Repeat, sRGB) → **Color Ramp** (position `0.186`) → **Mix Shader** `Factor 0.500` blending a **Glass BSDF** (`Multiscatter GGX`, Roughness `0.045`, IOR `1.500`) over the base material [frame_010].
13. **Custom render passes** — add an **AOV Output** node in the shader named `grunge`, then a matching **Shader AOV** in View Layer Properties, type **`Value`**; the pass then appears in the Render Result's pass dropdown alongside Combined and Depth [frame_011].
14. **Better color grading** — sandwich the grade between two **Convert Colorspace** nodes: `Working Space → Filmic Log`, then `Hue/Saturation/Value` (Hue `0.500`, Saturation `1.556`, Value `1.000`) and `Brightness/Contrast` (Bright `3.560`, Contrast `16.210`), then `Filmic Log → Working Space` back out [frame_012].
15. **Text editor** — keep scene notes inside the file using Blender's built-in **Text Editor** (TO DO / CHANGES lists, notes to whoever opens it next) [frame_013].
16. **Batch rename files** — for files on disk, **Bulk Rename Utility** (third-party, Windows): pick the files, use its RegEx / Replace / Remove / Numbering panels, Preview, Rename — 160 files renamed in one pass here [frame_014].
17. **Batch rename objects** — inside Blender, `Ctrl+F2` opens **Batch Rename**: scope `Selected`/`All`, data type `Objects`, `Type: Find/Replace` with Find and Replace fields and a Case Sensitive toggle; the dialog reports the count ("Rename 93 Object(s)") [frame_015].
18. **Render fog fast** — render the volume in **EEVEE** and everything else in **Cycles**, then combine: the Render Engine dropdown (EEVEE / Workbench / Cycles) is switched per scene, with Cycles here at Viewport Noise Threshold `0.1000` / Samples `500` and Render Noise Threshold `0.0250`, Max Samples `8138`, Min Samples `200` [frame_016]. Mix the two Render Layers with an Add node in the compositor.
19. **Align weird angles** — select **three vertices** forming a triangle on the angled face, then parent/align to that triangle to get a working axis on geometry with no sensible orientation [frame_017].
20. **How to number your shots** — name shots in tens (`Shot_010`, `Shot_020`, `Shot_03…`) so a new shot can always be inserted between two existing ones [frame_018].
21. **Make any texture tile** — put the texture on an unwrapped plane, build a 3×3 grid with **two Array modifiers** (`Array`, `Array.001`), then in **Texture Paint** use the **Clone** brush (Size `133 px`, Strength `1.000`, sampling from the 3D cursor) to paint the seams out, and bake the result to a new texture [frame_019].
22. **Smoothing nodes** — insert a **Bump** node (Invert off, Strength `1.000`, Distance `0.010`, Filter Width `0.100`) into the Principled BSDF's Normal input to soften the hard edges a crack/detail map leaves in the shading [frame_020].
23. **What noise threshold?** — the cheat sheet: **`0.01`** for low-end production, ~45× faster render time, and a decent animation denoise [frame_021].
24. **How black, how white?** — real albedo has a much narrower range than people assume. Blender's own picker on the reference objects: a black dress shirt reads **Value `0.200`, hex `#333333FF`**; a sheet of printer paper reads **Value `0.900`, hex `#E5E5E5FF`** (both HSV, Perceptual) [frame_022].
25. **Node search** — `Ctrl+F` searches a node graph by name, which is the only way to navigate trees like the `MT_track` Geometry Nodes tree shown, several hundred nodes wide [frame_023].
26. **Save your render as…** — the format chart: **EXR (DWAB)** sits at the top for quality while landing near JPG/WebP/AVIF on file size; PNG is the worst trade in the set, large *and* lower quality than EXR (DWAB); TIFF is largest [frame_024].
27. **Stronger thin film** — on a **black** Base Color material set Specular **`IOR Level 0.000`** with `Multiscatter GGX`, then open the **Thin Film** block and drive its thickness (in nm) with **IOR `1.330`** [frame_025]. Repeat the shader through a Repeat Zone with an Add Shader inside to intensify the iridescence, then mix over the base.
28. **Sunlight fringe** — on a Sun lamp (`Strength 100.000`, `Exposure 0.000`, Normalize on, **`Angle 0.526°`**, Temperature `6500 K`), enable **Use Nodes** and drive the light's colour through an **Invert Color** node (Factor `1.000`) into **Emission** (Strength `1.000`) → Light Output, to get the coloured fringe at the shadow terminator [frame_026].
29. **Break up flat colors** — large-scale variation instead of a flat albedo: a **Noise Texture** (3D, fBm, Normalize on, Scale `0.170`, Detail `10.000`, Roughness `0.966`, Lacunarity `2.000`, Distortion `0.000`) → **Separate Color** (RGB) drives `Brightness/Contrast` (Contrast `0.200`) and `Hue/Saturation/Value` on the base texture, so two copies of the same rock read as different rocks [frame_027].
30. **Instant hexagons** — a Geometry Nodes tree of exactly one node: `Group Input → ` **Dual Mesh** (`Keep Boundaries` off) ` → Group Output`. On a grid it gives hexagons; on a **Decimate**d Suzanne, as shown, it gives creature scales [frame_028].

### Nodes / Settings
- **Divide** (Color, Clamp Factor on, Factor 1.000) for material matching [frame_000]
- **Trace Image to Grease Pencil**: Radius 0.010, Color Threshold 0.500, Turn Policy Minority, Mode Single/Sequence [frame_001]
- **Texture bombing**: Texture Coordinate → Voronoi Texture (3D, F1, Euclidean, Normalize) → Vector Math (Add) → Image Texture (Box projection, Blend 0.100); Mapping Scale 0.010 [frame_002]
- **Bake**: Diffuse, Above Surface, Direct+Indirect without Color, Image Textures target, Clear Image, Margin Adjacent Faces 16 px [frame_004]
- **Shrinkwrap** on a Lattice: Nearest Surface Point, On Surface, Offset 0 m [frame_006]
- **Histogram range** group: Value "Level" (−0.410 mid-drag), Value "Range" (0.500), Subtract + Add (both Clamp), Map Range (Float, Linear, Clamp, From 0.000–1.000) → Roughness [frame_008]
- **Smudge stack**: Fingerprints overlay image → Color Ramp (pos 0.186) → Mix Shader (0.500) with Glass BSDF (Multiscatter GGX, Roughness 0.045, IOR 1.500) [frame_010]
- **Shader AOV**: AOV Output named `grunge`, View Layer Shader AOV type **Value** [frame_011]
- **Grading sandwich**: Convert Colorspace (Working→Filmic Log) → HSV (0.500 / 1.556 / 1.000) → Brightness/Contrast (3.560 / 16.210) → Convert Colorspace (Filmic Log→Working) [frame_012]
- **Batch Rename** (Ctrl+F2): Selected/All, Objects, Find/Replace, Case Sensitive [frame_015]
- **Cycles sampling** seen in the fog chapter: Viewport NT 0.1000 / 500 samples; Render NT 0.0250, Max 8138, Min 200 [frame_016]
- **Texture Paint Clone** brush: Size 133 px, Strength 1.000, over a 3×3 Array/Array.001 grid [frame_019]
- **Bump**: Strength 1.000, Distance 0.010, Filter Width 0.100 → Principled Normal [frame_020]
- **Albedo reference**: 0.200 / #333333FF (black shirt), 0.900 / #E5E5E5FF (printer paper) [frame_022]
- **Output format ranking**: EXR (DWAB) > TIFF > PNG > AVIF > WebP > JPG on quality; EXR (DWAB) near JPG/WebP/AVIF on size, PNG and TIFF far larger [frame_024]
- **Chrome thin film**: black Base Color, Metallic 0.000, Roughness 0.500, IOR 1.500, Specular Multiscatter GGX with IOR Level 0.000, Thin Film thickness in nm, Thin Film IOR 1.330 [frame_025]
- **Sun**: Strength 100.000, Angle 0.526°, 6500 K, Normalize on; light nodes Invert Color (1.000) → Emission (1.000) → Light Output [frame_026]
- **Colour break-up**: Noise Texture (3D fBm, Scale 0.170, Detail 10.000, Roughness 0.966, Lacunarity 2.000) → Separate Color (RGB) → Brightness/Contrast (0.200) + Hue/Saturation/Value [frame_027]
- **Dual Mesh** (Keep Boundaries) as a one-node Geometry Nodes tree, after a Decimate modifier [frame_028]

### Difficulty
Intermediate

### Blender Version
Blender 5.0.0 — read from the status bar in the Blender-UI frames (e.g. [frame_004], [frame_008], [frame_015]).

### Tags
materials, shaders, procedural, compositing, rendering, cycles, eevee, geometry-nodes, cloth, intermediate

---

## Related Tutorials
- [Doing Surface Imperfections Right | Vray, Cycles, Arnold..](doing-surface-imperfections-right-vray-cycles-arnold.md) — same layered-smudge-shader philosophy for glossy surfaces (tip 13) and roughness-map theory
- [Perfect Textures in Blender - Works Every Time](perfect-textures-in-blender---works-every-time.md) — shares materials/shaders/procedural/rendering/cycles tags; complementary texture-realism workflow
- [3 Easy steps to make Realistic Materials](3-easy-steps-to-make-realistic-materials.md) — shares materials/shaders/procedural/cycles tags; realistic-material quick wins in the same spirit
- [A FULL Blender Compositor Course!](a-full-blender-compositor-course.md) — deep dive for the compositing tips here (grading sandwich, AOVs, render-layer mixing)
