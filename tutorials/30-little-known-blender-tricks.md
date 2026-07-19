---
title: 30 little-known Blender tricks
source: YouTube
url: https://www.youtube.com/watch?v=5_Jy97TzZuM
author: Robin Squares
ingested: 2026-07-19
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/30-little-known-blender-tricks/
frame_count: 0
frame_status: pending-selection
---

# 30 little-known Blender tricks

**Source:** [YouTube](https://www.youtube.com/watch?v=5_Jy97TzZuM)
**Author:** Robin Squares
**Duration:** 12m17s | 33 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py 30-little-known-blender-tricks <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Blender Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
