---
title: How to Build After Effects-Style Motion Graphics in Blender
source: YouTube
url: https://www.youtube.com/watch?v=-cscjxxxebk
author: Bring Your Own Laptop
ingested: 2026-08-04
blender_version: "Not specified (recent 4.x-era Geometry Nodes UI)"
tags: [geometry-nodes, procedural, motion-design, typography, materials, animation, camera, rendering, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/how-to-build-after-effects-style-motion-graphics-in-blender/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How to Build After Effects-Style Motion Graphics in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=-cscjxxxebk)
**Author:** Bring Your Own Laptop
**Duration:** 17m6s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro to Blender Motion Graphics [0:00]
**Transcript (timestamped):**
[0:00] Hello everybody, this is RobinSquares here with Bring Your Own Laptop and today we are
[0:05] making motion graphics inside of Blender.
[0:09] That's right, not After Effects, because Blender is such a capable motion graphics
[0:14] to what I wish more people knew about that.
[0:17] For example, text templates like this are usually made in After Effects, but you can
[0:23] get really far with Blender for free.
[0:27] We're making this cool procedural video title piece and it's suitable for all skill
[0:33] levels.
[0:34] But if it's the first time you're opening Blender, I would recommend you just check
[0:38] out the first Blender tutorial I made on this channel first, because there I go through
[0:42] just how to move around the software and such.
[0:45] But let's just head into Blender and get started.


### Creating a Dot Grid with Geometry Nodes [0:50]
**Transcript (timestamped):**
[0:50] So when you open Blender, this is what you see.
[0:52] Let's just click on the cube and we open a new window and change that window type to
[0:58] the Geometry Nodes Editor.
[1:01] Geometry Nodes is Blender's procedural toolkit and it's really good for motion graphics
[1:06] stuff.
[1:07] So again, with the cube selected, let's press New at the top of the Geometry Nodes
[1:12] here and we get two nodes, one as the group input and one output.
[1:17] The input is what we had originally as an object.
[1:21] It's the cube.
[1:23] The output is what we see, which now is the cube.
[1:26] But let's just delete the input by hitting X and there it's gone.
[1:31] And now we can add anything else that we want to see.
[1:33] So let's hit Shift A inside of this window and search for Sphere, for example.
[1:39] So we can add a UV sphere or an Ico sphere for example.
[1:43] Let's just click that and add it and to show it, we have to hook it up to the output, like
[1:48] this.
[1:49] So that shows us a sphere instead.
[1:51] So what we actually want to begin with for this effect is Shift A, we want to search
[1:55] for a grid.
[1:57] So click grid and then hook it up to the output and I can just scroll in to see it here.
[2:03] Is this a grid?
[2:04] Is it a plane?
[2:05] Hard to tell, right?
[2:06] And that's because of the View Mode.
[2:07] So let's just middle mouse click on this bar up here and hit the Wireframe view.
[2:13] And now we can see that it does in fact have a grid.
[2:16] If I increase the vertices in this node, you can clearly tell that it is a grid.
[2:22] So let's increase the size of that.
[2:24] I can actually drag over both of these values and just drag it up until we have a big plane,
[2:29] around 10 meters in both directions.
[2:32] And then increase the vertices to, I don't know, 13 in each direction, something like
[2:36] that.
[2:38] And then let's place something on each point on that grid.
[2:42] So let's hit Shift A, search again and I'll search for instance on points.
[2:48] That is the node that we want.
[2:50] How do I know what node to search for?
[2:52] Aren't there a lot of them?
[2:53] There are.
[2:54] If I hit Shift A, you can see all of them in these menus as well.
[2:57] There are quite a few nodes, but it is the 80-20 rule.
[3:00] 20% of the nodes do 80% of the work.
[3:03] If you just follow a few tutorials, you'll get a sense for which ones are the most important
[3:06] ones and you can start making effects from scratch.
[3:09] Now this node has a bunch of inputs.
[3:11] And now let's set off points.
[3:13] What points do we want to place things on?
[3:15] And it is the points of the grid.
[3:17] Let's just take the output of the grid, put it into points and then view the output.
[3:22] Everything disappears.
[3:23] That's because we haven't told it what to put there yet.
[3:26] So let's add another sphere then, okay?
[3:28] Shift A, search, sphere and I'll go for a UV sphere and just input that into the instance
[3:35] and there we go, bunch of spheres.
[3:37] I can even turn back to solid mode now to see that there are a bunch of spheres overlapping
[3:43] each other.
[3:44] How do we scale them down?
[3:46] That's another node.
[3:47] So I'll move this out of the way a bit, search for transform and add a transform geometry.
[3:54] I can just click in between these to add it right in between and then I can drag over
[3:59] all three scale values and just Shift drag them to the left.
[4:05] So that scales them down nicely.
[4:08] Now let's start adding color to these things.
[4:11] We can go to the materials tab on the right hand side here and there is a default material
[4:17] already on this called material.
[4:19] We can use that.
[4:20] If we change the color of that however, you'll see nothing changes in the view.
[4:26] One reason for that, there are two.
[4:28] One reason for it is we're not in rendered mode.
[4:30] So let's move over to the view modes and hit rendered mode.
[4:34] But it's still not updated.
[4:36] The reason is when we work with geometry nodes, we need to specify the material in there as
[4:42] well.
[4:43] So I'll add another node.
[4:45] We can search for just material to get a hint for what we can add and at the top there is
[4:50] the set material node.
[4:52] So hit enter on that, add it at the very end and in this election we'll just select that
[4:57] green material and that turns everything green.
[5:00] At this point we can go and change this window mode to the shader editor to edit what that
[5:05] shader actually is.
[5:06] So currently we have this node but let's say we want random colors.
[5:11] What can we do?
[5:12] We can add a random node.
[5:13] So shift A, random and there are a bunch of random nodes.
[5:17] They all do different things, do different kinds of objects.
[5:20] The one we want now is the one under object info.
[5:24] So just add that and we can preview what that does by just dragging that to the surface.
[5:29] You can see it gives us a random value between black and white for each sphere.
[5:34] But we can map those to a different color palette.
[5:38] We do that using a color ramp node.
[5:40] Shift A, color ramp, add that right in between and here we can change the color.
[5:46] So if I just click on the left hand arrow, click on the color, we can change that to
[5:51] say blue and the right one, we can change that to red.
[5:54] Now we have a gradient going from blue to red and all of the spheres picking a point
[6:00] on that gradient.
[6:01] Let me show you a trick for how to work with color and blender though.
[6:04] Open a new window at the top here and change that to the image editor.
[6:09] And then I'll just drag in an image of a color palette that I've made.
[6:12] Just drag that into that window and now we can sample from that.
[6:17] So on the left here I can click on the color, click the eyedropper and sample that blue
[6:22] for example.
[6:23] And on the right I can sample that rightmost color which is the turquoise and say I want
[6:28] linear steps instead of a gradient.
[6:31] I can do that too.
[6:32] Change it from linear to constant and that gives me a hard line.
[6:37] So we can add more with a plus, more points and just select the other colors as well plus
[6:44] and select the yellow.
[6:45] And we can play with the ratios here too so we can have say very few of the red and turquoise
[6:52] ones, quite a lot of the blue ones and a little and a few of the few of the orange ones as
[6:58] well.
[6:59] Like this maybe.
[7:01] Might look nice.
[7:02] But you might see it has a kind of muddy yellowish color.
[7:05] It's not really picking the right color if you compare this to this.
[7:09] The reason for that is that Blender's colors by default are set up to work with photographic
[7:16] colors, not graphic design colors.
[7:19] We can change that very easily by going to the little camera icon, that's the renderer
[7:23] properties and at the very bottom we have color management.
[7:28] And here we change the view from AGX, which is a film emulation, we change that to standard.
[7:34] And you can save this as your default if you so want to, but now all the colors should
[7:39] be back to exactly what we'd expect.
[7:42] But we don't have a nice background color yet.
[7:45] And we can change that right here under world in the shade editor, that gives us the background
[7:51] color so I'll pick this cream at the very left.
[7:55] And back in object, you can also see that all of the balls are completely flat, you
[8:01] don't have any shading on them, and that's just because we haven't run the color through
[8:06] this shader that came with it.
[8:08] If we run the color into the base color and then run that to the surface, that gives us
[8:14] the shading as well.
[8:15] So now we have highlights and we have shadows, but I don't want that.
[8:19] So I'll hit X, delete that and hook it up again, just to get that graphic look.
[8:24] And if you have made it this far, then I recommend the full Blender 3D Essentials course on
[8:28] bringer on laptop.
[8:30] It goes much more in depth on all the fundamentals to do basically anything in 3D.
[8:35] But for now, let's just continue with emotion graphics stuff.
[8:38] Now we can close this window and just give ourselves some more space to work with.


### Setting Up the Camera View [8:39]
**Transcript (timestamped):**
[8:44] I'll split this window in half as well.
[8:47] At the bottom, I'll have a window to work in.
[8:50] And at the top, I'll use that window to preview what it'll look like.
[8:53] So in this top view, I'll turn off the viewport overlays.
[8:57] I'll move this little window out of the way.
[9:00] And I'll move into the camera view because that is where we render from.
[9:05] So in the bottom window here, I'll click the camera.
[9:07] And in the top window, I'll click the little camera icon on the right that moves into that
[9:12] camera for that view.
[9:14] And then I can turn off the navigation overlays as well just to clean it up even more.
[9:19] And I can see as I move the camera around, if I use the move tool, you can see that top
[9:23] view follows.
[9:25] So let's go into just the object properties of the camera where we see rotation.
[9:31] I'll select all three of those at the same time, hit zero, and that makes it point straight
[9:36] down.
[9:37] And then I can just move it over to roughly the middle.
[9:39] Actually, I can do that exactly with a zero on location two.
[9:44] And just move it up.


### Filling the Screen & Animating Text [9:49]
**Transcript (timestamped):**
[9:49] And roughly what scale do I want this at?
[9:52] Let's say...
[9:53] It can be a bit hard to see in that small window sometimes, but control or command space on
[9:58] that window maximizes it.
[10:00] Is that a good size for the dots?
[10:02] Let's move it even further up, I think.
[10:05] Like that.
[10:06] And then this is the great part of working procedurally, is if we now go back to the geometry nodes,
[10:12] now we can increase the size and the vertices to cover the screen.
[10:16] Increase the size to go to the edge, size Y as well, and then increase the vertices until
[10:22] I have enough dots to cover it.
[10:25] Excellent.
[10:26] And now let's work on the interaction with the text.
[10:30] I want these dots to grow big when they're close to text and small when they're far
[10:35] away, so that we can make that effect of the text running through the dots.
[10:41] So first, let's add the text.
[10:43] Let's select A in my working window down at the bottom and add a text object.
[10:49] And it's kind of small to begin with, but we can see it if we zoom in here.
[10:53] And I can increase the size of that in the font panel.
[10:56] So go to font and change the size, just increase that until it's fairly big.
[11:01] I wanted to cover parts of this.
[11:03] And it only goes to 10, but you can type higher numbers, so 15, 20, that looks good, I think.
[11:10] Let's also pick a nice font by hitting the little folder icon.
[11:13] I can search for the fonts on your system.
[11:15] I search for a rounded, aerial rounded, that's perfect.
[11:20] And then let's animate that font.
[11:21] You can animate it however you want.
[11:23] You can scale it, for example.
[11:25] Scale it from small to big if you want.
[11:28] You can rotate it around.
[11:31] That might look cool.
[11:32] I'm just going to move it from right to left.
[11:35] Just super simple.
[11:36] So I'll increase the size of my timeline a little bit.
[11:39] Go to the object properties, and also I'll grow this up a little bit too so you can see
[11:43] it better.
[11:44] And I want a keyframe location X.
[11:47] That is what moves it from side to side.
[11:48] You can see that as I drag it here.
[11:50] So at the start of the timeline, I want it on the very right hand side.
[11:55] I'll click the little dot to set a keyframe.
[11:58] And then move to the end of the timeline and drag the location X over to the left and set
[12:03] a keyframe.
[12:04] And then if I play the animation, it should move through.
[12:10] And that's perfect.
[12:11] So it's a bit too slow for me.
[12:13] Let's see, when do I want it to end?
[12:15] Somewhere around here.
[12:16] I'll just move that keyframe over here to make it complete faster.
[12:20] Let's see if that helps.
[12:22] Yeah, that's better.


### Refining the Text Animation Timing [12:24]
**Transcript (timestamped):**
[12:26] So now I have a bunch of dead space on the right here.
[12:28] I want the animation to end on frame 144.
[12:31] So I have 144 here.
[12:34] And then let's make the spheres react to the text.
[12:38] This is such a good part.
[12:39] And we'll have the render preview open as well.
[12:42] So click on the spheres and open the Geometry Nodes window.
[12:46] Here's what we need.
[12:47] We need the text in there.
[12:48] Let's just click the text in the outliner on the right and drag it in.
[12:52] And I can show you, if we preview this text, here's what happens.
[12:56] It shows the text in the wrong spot and it doesn't move.
[13:00] So what gives?
[13:01] Well, we have to set it to relative because by default it doesn't show where the text
[13:06] really is with all the animation and stuff until we have relative there.
[13:10] So now it follows along.


### Connecting Text to the Dot Grid [13:13]
**Transcript (timestamped):**
[13:13] And then we need a Geometry Proximity Nodes.
[13:16] So Geometry Proximity.
[13:19] And we put the text into there.
[13:21] So every single dot will see how far away am I from a point on the text.
[13:27] And the output here is the distance.
[13:30] So we can map that range.
[13:33] Map range.
[13:34] This gets a little bit technical, but I'm sure you can follow along if you try it yourself.
[13:38] So all we want here is we want to say when the distance is zero, that means the dot is


### Mapping Dot Size to Text Proximity [13:42]
**Transcript (timestamped):**
[13:47] right on top of the text, how big do I want the dot to be?
[13:51] And that is one.
[13:53] So from minimum zero to minimum one.
[13:56] And then when it's one meter away, how big do I want it then?
[13:59] Let's say zero.
[14:01] And then let's just plug that result into the scale on instance on points.
[14:07] Which is the node that put the spheres around, right?
[14:09] So we use that.
[14:12] And then we preview the output.
[14:15] And you can see what we have is the dots are reacting to the text.
[14:19] How cool is that?
[14:21] And now let's just go in and we can change and just tweak the values to our liking.
[14:25] So I don't want it to go to complete nothing.
[14:28] I don't want it to go to zero.
[14:30] Let's just increase the size a little bit until we get tiny little dots on a grid.
[14:37] And then I feel like it's fading out a bit too long.
[14:40] So instead of looking a whole meter away, let's just decrease that and see that we
[14:45] can decrease the fade.
[14:47] I'll decrease it to something like that.
[14:50] What do we want to say?
[14:51] What do we want to say to the world?
[14:53] Let's hit tab on the text to edit it.
[14:57] And what do we want to say?
[14:58] Let's see.
[15:01] That I think is a pretty good one.


### Rendering the Final Animation [15:06]
**Transcript (timestamped):**
[15:07] Now we're showing the text underneath here.
[15:09] You can barely see it at the bottom there.
[15:12] Let's hide the text as well.
[15:14] I'll just put it into its own collection with a new collection button.
[15:18] Put it into there and just call that hide and disable that collection.
[15:22] It'll still work, but the text itself won't show.
[15:25] I think the time has come to render it out.
[15:28] Let's go to the output tab, set the resolution.
[15:31] That's good for me.
[15:32] Set the output folder, my temporary, that's okay.
[15:36] And instead of rendering an image, I want to render a video which under encoding is
[15:41] going to be not a Matroska, but an MPEG4 and the quality perceptually lossless.
[15:48] And just to make sure that you'll render at the full speed your computer can, let's
[15:51] go to your preferences and under system, you should set up a render device.
[15:56] If you're on Mac, it's a good idea to set it to metal.
[16:00] If you have an RTX card, set it to optics.
[16:03] And if you have a GTX card, set it to CUDA.
[16:05] And then you're ready to render.
[16:07] So just go to the render menu and hit render animation.
[16:12] And it'll run through and make the video for you.
[16:14] And that's our video.
[16:15] How cool is that?
[16:16] I think it's so cool how capable Blender is as a motion graphics tool, at least if
[16:22] you use geometry nodes like this.
[16:24] You could make all kinds of things like plant, text, UI, animation and particle systems.
[16:31] If you had fun with this, then I recommend you check out the Blender 3D Essentials course
[16:35] on bringeronlaptop.com.
[16:37] It's taught by me, it goes through all the basic stuff that you need to do basically
[16:41] anything inside Blender, not just motion graphics, but modeling, texturing, rendering,
[16:48] all of that stuff.
[16:49] It prepares you for work in 3D.
[16:51] And don't forget to subscribe to this channel as well, so that we are sure to see each other
[16:55] in the next video.



---

## Captured Frames

- [4:05] tutorials/frames/how-to-build-after-effects-style-motion-graphics-in-blender/frame_000.jpg
- [6:52] tutorials/frames/how-to-build-after-effects-style-motion-graphics-in-blender/frame_001.jpg
- [8:19] tutorials/frames/how-to-build-after-effects-style-motion-graphics-in-blender/frame_002.jpg
- [10:22] tutorials/frames/how-to-build-after-effects-style-motion-graphics-in-blender/frame_003.jpg
- [11:20] tutorials/frames/how-to-build-after-effects-style-motion-graphics-in-blender/frame_004.jpg
- [12:22] tutorials/frames/how-to-build-after-effects-style-motion-graphics-in-blender/frame_005.jpg
- [14:19] tutorials/frames/how-to-build-after-effects-style-motion-graphics-in-blender/frame_006.jpg
- [16:14] tutorials/frames/how-to-build-after-effects-style-motion-graphics-in-blender/frame_007.jpg

---

## Structured Notes

### Core Technique
A Geometry Nodes dot-grid whose per-point scale is driven by proximity to an animated text object, so the dots reveal/hide the text as it slides across — a fully procedural, After Effects-style kinetic-typography effect built entirely with native nodes (no add-ons).

### Summary
Builds a grid of UV spheres via Instance on Points, colors them with a random-per-instance value remapped through a Color Ramp (sampled from a flat graphic-design palette image), then adds a Text object animated across the screen on Location X. A Geometry Proximity node measures each dot's distance to the text mesh, and a Map Range node converts that distance into an instance scale (0 at 1m away → 1 at the text surface), so dots shrink to nothing right where the text passes and grow back elsewhere. Ends with color-management and render/output settings for exporting the animation as a video.

### Key Steps
1. Cube → new Geometry Nodes modifier → delete Group Input → `Shift A` → **Grid** → wire to Group Output (Wireframe view mode to confirm it's a grid, not a plane); increase Size X/Y and Vertices X/Y to cover the camera frame (final: Size ~55.2×30.2m, Vertices ~50×13).
2. `Shift A` → **Instance on Points** (Points ← Grid), **UV Sphere** → Instances input, **Transform Geometry** node inserted before Instance on Points to scale spheres down (drag all 3 Scale values together).
3. Material tab → assign default material → switch viewport to **Rendered** shading → add a **Set Material** node inside the Geometry Nodes tree itself (materials assigned in Object mode don't show unless also set in the node tree).
4. Shader Editor on the sphere material: **Object Info → Random** output → **Color Ramp** → Base Color of Principled BSDF. Color Ramp stops are sampled with the eyedropper from a flat palette reference image opened in a separate Image Editor window; interpolation set from Linear to **Constant** for hard color bands instead of gradients: adjust each stop's position to control the ratio of each color.
5. Render Properties → Color Management → View Transform: **AGX → Standard** (AGX is a filmic emulation that mutes graphic-design flat colors; Standard restores true sRGB hex-accurate color). World shader background color set separately in the Shader Editor's World tab.
6. Add Text object (`Shift A` in 3D viewport), increase Font Size (type values >10 manually, e.g. 15–20), pick a rounded font via the font-file browser icon. Keyframe **Location X** at the timeline start (text off-screen right) and end (text off past left) to animate it sliding through; drag the keyframe's frame number left to shorten/tighten the timing, and set the scene end frame to match (e.g. 144).
7. In the spheres' Geometry Nodes tree: drag the Text object into the tree as an input node, set it to **Relative** (Transform Space) so its animated position registers — otherwise the proximity read is static and wrong. Add **Geometry Proximity** (target = text) → outputs Distance → **Map Range** (0m distance → scale 1, ~1m distance → scale 0, tune the far value to control fade width) → plug result into Instance on Points' **Scale** input.
8. Hide the text mesh itself once the effect reads correctly: move it into its own Collection and disable that collection's viewport/render visibility (geometry nodes still reference it fine; it just stops rendering as a visible mesh).
9. Output tab: set resolution and output folder; Output Properties → File Format → video container (MPEG-4, not Matroska), quality "Perceptually Lossless". Preferences → System → set render device to the GPU backend (Metal/OptiX/CUDA) before Render → Render Animation.

### Nodes / Settings
- Geometry Nodes: Grid, Instance on Points, Transform Geometry, Set Material, Geometry Proximity, Map Range
- Shader nodes: Object Info (Random output), Color Ramp (Constant interpolation), Principled BSDF (Base Color only — Base Color piped straight to Surface, bypassing the BSDF's own shading, for a flat/graphic look)
- Grid: Size X/Y ~55.2×30.2m, Vertices X/Y ~50×13 (tuned to exactly cover the camera frame)
- Color Management → View Transform: Standard (not AGX)
- Render output: MPEG-4 container, Perceptually Lossless quality; GPU render device (OptiX/CUDA/Metal)

### Difficulty
Intermediate — no simulation or advanced math, but chains 6+ Geometry Nodes concepts (instancing, proximity, remapping) that a beginner wouldn't yet know to combine.

### Blender Version
Not specified in video or frames (UI matches a recent 4.x-era Geometry Nodes layout; no version splash or About dialog shown).

### Tags
geometry-nodes, procedural, motion-design, typography, materials, animation, camera, rendering, intermediate

---

## Related Tutorials
- [Fluid sim testing in Blender 5.3! (Rasterize Points Node)](fluid-sim-testing-in-blender-53-rasterize-points-node.md) — shares `geometry-nodes` tag; different domain (fluid/particle rasterization vs. instance-on-points typography) but same instancing/attribute-driven-scale pattern.
