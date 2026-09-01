---
title: Add VFX into Cinematic RAW+LOG Footage (the right way) | ACES Part 1
source: YouTube
url: https://www.youtube.com/watch?v=aJF2sAjRsy0
author: InLightVFX
ingested: 2026-06-25
blender_version: "Any (theory only)"
tags: [color-management, aces, vfx, compositing, theory, beginner]
extraction_status: complete
frames_dir: tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Add VFX into Cinematic RAW+LOG Footage (the right way) | ACES Part 1

**Source:** [YouTube](https://www.youtube.com/watch?v=aJF2sAjRsy0)
**Author:** InLightVFX
**Duration:** 9m59s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** As you progress as a VFX artist, at some point you'll probably work with Log or RAW footage.  This footage looks flat out of the camera which leads to high quality cinematic images.  The cameras that can shoot this type of footage keep getting more affordable and more popular.  So how do we add VFX into flat, log or RAW footage?  The answer is ACES.  ACES is a free color management pipeline.  Now what that means will make more sense as we go on.  Now basically ACES enables artists to easily incorporate VFX into high quality, log and  RAW footage.  ACES is quickly becoming the industry standard workflow.  It's being adopted not only by big studios but also independent artists like you and me.  And it's for all these reasons and more that I think you should learn ACES.  One of the main things ACES does is handle the color gamut and gamma of our footage.  In this video we'll learn all about what this means.  In part two we'll look at the ACES workflow using DaVinci Resolve and Blender.  But for now if you don't understand color gamut and gamma, join me and let's dive in.  For this video I created this poster that goes over these concepts.  So make sure to download it and follow along linked in the description.  First up, color gamut.


### Color Gamut [1:15]
**Transcript:** We use the term color gamut when talking about color spaces.  Now what the heck is a color space?  Well if we look up color space on Google we'll see most of the images are of this chart.  This chart was actually created in 1931 but as you can see it's still widely used today  to visualize color spaces.  Let's break this chart down.  First there's this whole color region you see here.  This represents all the possible colors that the average human eye can see out in nature.  As such we call this the visible color space and the boundary of this space is labeled  as the gamut of human vision.  So we can think of gamut as meaning the total range or boundary of a certain color space.  Cameras capture images and video by representing the real world with a subset of colors from  a certain color space.  Display devices then represent these images using a color space that could be the same or  different.  These different color spaces used for capturing and displaying images can be mapped onto  our diagram with triangles.  We use a triangle to mark the color gamut or range of a color space.  All the colors inside the triangle gamut are the ones able to be captured or displayed.  So how does all of this apply to aces?  Well part of aces includes the main aces color space which is called aces 20651.  And as you can see the gamut of this color space encompasses the entire visible spectrum  of light.  This is why aces is so powerful.  Remember when I said that aces is able to handle the color gamut of whatever footage  we throw at it?  Well here's what I mean.  Because the aces color gamut is so huge aces is able to use footage filmed in a variety  of smaller gamut and transform that footage into the aces color space.  And this is super helpful for artists because we can just focus on doing VFX in aces.  And never again have to worry about what type of footage we're handed.  Now it's not exactly that simple but it is really nice.


### Linear Gamma [3:13]
**Transcript:** So now we understand color gamut which mainly deals with color and describing a certain  range of colors.  If gamut describes color, gamma we can think of as having to do with brightness and luminance.  Let's look at a different graph to understand.  Now don't freak out, you've seen this type of graph before with RGB curves.  Our x-axis will represent luminance input level.  So zero on the x-axis means complete black and one means complete white.  The y-axis will represent the output values.  Let's draw a straight line represented by the function y equals x.  Now gamma is actually just a value and this value is taken as the exponent of our input.  This gamma value is part of what is called a gamma transfer function.  If we set the gamma value to 1, then our line here stays the same.  Our input luminance values are not changed by the gamma function.  This is called a linear gamma or more specifically a linear transfer function.  With a linear transfer function, if we add two luminance inputs say 0.25 plus 0.25, we  get an expected output of 0.5.  Two times as luminous.  The math works as expected.  If we set the gamma value to 0.5 or 1.5, we'll see that our line becomes a curve.  This is what we call a non-linear gamma curve or non-linear transfer function.  We can see that if we have an input of 0.25, we get 0.5 on output.  If we then add 0.25, we get 0.7.  So math from input to output with non-linear transfer functions is a little weird.


### Linear Light [4:48]
**Transcript:** Now in nature, in the real world, light waves interact in a linear relationship.  If you double the luminance input of a light source, we get double the output.  Blender and most 3D software is set up to use linear calculations by default when rendering  and compositing.  Let me show you why this is helpful.  We have a scene here with two lights on either side of the cube and the world shader set  to black.  I can render the scene with both lights on and get this image.  Or I can render an image with just one light on and a second image with the other light  on.  And if I add these two images together in compositing, you'll see it looks exactly  like the image with both lights on.  The reason this math works so well is because we're using linear light calculations.  Which again is how light works in the real world.  This is also why multi-pass compositing is possible, which is the technique I've shown  in other videos.  So now let's talk about humans.  Our eyes perceive brightness from the world around us non-linearly.  Let me provide an example to explain this.  Say you're in a completely dark room and then you let a candle.  Your eyes perceive a big change in brightness.  But if we're in a bright environment and we light the candle, our eyes see very little  change to the brightness of the environment, even though the change in luminance, the  candle, is the same.  As you can see, our eyes are more sensitive to changes in brightness of darker shades.  So we say that our eyes perceive brightness non-linearly.


### Cameras [6:12]
**Transcript:** Now let's talk about cameras and gamma.  There are two different methods for how cameras store the linear light information from the  real world, display referred and scene referred.  Cameras like your phone or basic DSLR, store light values using the display referred method.  To have smaller file sizes, these devices record less light information from the scene.  The information that is collected has a non-linear transfer function applied.  This optimizes the image, brightening the dark shades, where our eyes are most sensitive.  Higher end cameras that shoot RAW video are able to store light information with the  scene referred method.  These cameras record more light information and therefore are able to store the RAW linear  light information from the scene, unmodified.  This creates much larger files to store all these light values.  Also in the scene referred category is log footage.  With log footage, the linear light values from the scene have a special log transfer  function applied to them.  While log footage does not capture the exact scene like RAW, log stores enough light information  where we can use aces to reverse engineer what the original light values were.  The benefit of log is smaller file sizes than RAW, while retaining more light information  than display referred formats.  To summarize, display referred footage discards a lot of the original light information,  optimizing and storing only what's needed for display.  Scene referred footage more accurately represents the scene in what the original real light values  were.  Scene referred RAW and log footage leads to more accurate VFX compositing because of the  extra light information that is captured.


### Gamma [7:52]
**Transcript:** Next up, gamma and displays.  All display devices, from a computer monitor to a movie theater projector, display images  with a certain gamma function applied to them.  Say we're putting some display referred footage on a computer screen.  The screen displays all images with a default nonlinear gamma curve applied.  Combined with the gamma originally applied by the camera, our image now appears normal.  Our optimized display referred image is gamma corrected to look normal.  This is why log and RAW footage often looks flat, since the default computer screen  gamma does not pair correctly with the gamma of the footage.  Finally, how does gamma apply to aces?  While aces 2065 is a linear color space.  This means we work with linear luminance values that reflect the real world.  This is convenient for us VFX artists since we already work in linear color spaces for  accurate rendering and compositing.  The cool thing about aces is that it can take either display referred or scene referred  footage and convert it to be represented in the aces linear color space.  As artists, this means that we can just focus on doing VFX in aces and theoretically never  have to worry about the gamma of the footage that we're using, which is super nice.  So there you go, that's the concepts of color gamut and gamma.  Now I know those are kind of tricky concepts to grasp onto, but don't worry, in part  two, we'll dive into aces, into vinci resolve, and blender, and hopefully you'll start to  see the big picture of all of this.  Before I go, I need to give a big thanks to Mario Cossadez and Daniel Birka.  Those two guys helped me work through a lot of the information I presented in this video,  and they also have some fabulous blender-related resources on aces, which I'll link in the  description.  Don't forget to download the free poster for color gamut and gamma, and other than that,  I'll see you in part two.



---

## Captured Frames

- [1:50] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_000.jpg
- [3:50] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_001.jpg
- [5:20] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_002.jpg
- [6:50] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_003.jpg
- [8:30] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_004.jpg

---

## Structured Notes

### Core Technique
Theory-only Part 1: understanding color gamut (why ACES 2065-1 can contain all camera color spaces) and gamma (linear vs non-linear transfer functions, display-referred vs scene-referred footage) as the conceptual foundation for the ACES VFX pipeline covered in Part 2.

### Summary
InLightVFX explains the two core concepts behind ACES before touching any software. **Color gamut:** the CIE 1931 diagram maps all visible colors; cameras capture a triangular subset of that gamut; ACES 2065-1 has a gamut so large it encompasses all other camera color spaces, which is why any footage can be converted into it. **Gamma:** a transfer function exponent applied to luminance values; a gamma of 1 = linear (math works as expected — doubling luminance doubles output); non-linear curves (camera profiles, display gamma) cause unexpected arithmetic. Blender/3D software uses linear calculations so adding two render passes equals rendering them together. Human vision is non-linear (more sensitive to changes in shadow). **Camera types:** display-referred (phones, basic DSLRs) apply a non-linear transfer to compress dynamic range; scene-referred RAW stores linear light values directly (large files); scene-referred LOG applies a log function to represent original light values in smaller files. ACES can reverse-engineer all three into its linear color space via IDTs. Part 2 shows the actual workflow in DaVinci Resolve and Blender.

### Key Steps
1. **Color gamut** — understand that camera sensors capture a triangular subset of all visible colors; ACES 2065-1's gamut encompasses all visible light, making it the universal container for any footage.
2. **Gamma = transfer function** — gamma value is an exponent applied to luminance; gamma 1 = linear (y=x); any other value = non-linear curve.
3. **Linear light math** — with linear gamma, adding two images in compositing equals rendering with both lights; this is why multi-pass compositing works. **This is demonstrated in Blender, not just asserted** [frame_002]: two `Render Layers` nodes pointing at view layers `Light1` and `Light2` (scene `Scene`, slot 3) feed a `Mix` node whose blend-mode dropdown is open on the additive group — `Lighten`, `Screen`, `Color Dodge`, `Add` — with a `Viewer` node (`Use Alpha` on, `Alpha` 1.000, `Z` 1.000) showing the result.
4. **Human vision** — non-linear sensitivity (candle in dark room vs. bright room); cameras and displays account for this with non-linear gamma.
5. **Display-referred cameras** — apply non-linear transfer to reduce file size; loss of dynamic range; poor base for VFX compositing.
6. **Scene-referred RAW** — stores linear light values; large files; best source for VFX.
7. **Scene-referred LOG** — log transfer function applied to linear values; smaller than RAW, recoverable via ACES IDT; good VFX source.
8. **ACES role** — its IDT converts any footage's color gamut + gamma into ACES 2065-1 linear; artists then work purely in ACES without worrying about source formats.

### Nodes / Settings
⚠️ **Corrected 2026-09-01.** This section previously read *"No Blender nodes — this is a theory/concepts tutorial"*. That was written from the transcript, and it is wrong: the *Linear Light* chapter carries a working compositor demo [frame_002].

- `Render Layers` ×2 — one per view layer (`Light1`, `Light2`), each rendering a single light
- `Mix` — blend mode dropdown; the additive modes (`Lighten`, `Screen`, `Color Dodge`, `Add`) are what make the two single-light renders reconstruct the both-lights render
- `Viewer` — `Use Alpha` enabled, `Alpha` 1.000, `Z` 1.000

The node is named **`Mix`**, not `Mix Color`, so the demo footage predates Blender 4.0 [frame_002]. That dates the *footage*; the concepts are version-independent.

Key terms:
- ACES 2065-1 — the main ACES linear color space; gamut encompasses all visible light
- IDT (Input Device Transform) — converts source footage color space + gamma into ACES
- ODT (Output Device Transform) — converts from ACES to display device color space (e.g. sRGB)
- Linear gamma — gamma = 1; luminance math is predictable; used in 3D rendering
- Display-referred — camera applies non-linear encoding; optimized for display, not VFX
- Scene-referred (RAW / LOG) — stores original scene light values; better for VFX

### Difficulty
Beginner — no software required; pure theory; helpful prerequisite for Part 2.

### Blender Version
Any — the concepts are version-independent. The one piece of Blender footage in the video is pre-4.0, dated by the compositor node still being called `Mix` rather than `Mix Color` [frame_002].

### Tags
#color-management #aces #vfx #compositing #theory #beginner

---

## Frame verification (2026-09-01)

| | |
|---|---|
| **Corrected** | *"No Blender nodes — this is a theory/concepts tutorial"* was false. The *Linear Light* chapter contains a real compositor demo [frame_002], and it is the one place the video proves rather than states its central claim. |
| **Confirmed** | the CIE-style gamut-of-human-vision plot on 0–1 axes [frame_000]; the gamma formula written on screen as **y = x^(gamma value)**, plotted as the linear y=x diagonal [frame_001]; the *Scene-Referred, RAW* transfer plotted as a straight line from origin [frame_003]. |

⚠️ **`frame_004` (8:30) is a mistimed pick** — it lands mid-wipe on b-roll of a
room, with the caption caught half-transitioned ("Ga… RAW"). Chapter-heading
picks miss at a measured ~25% (plan batch D3c); this is one. It grounds nothing
and is left recorded rather than quietly re-rolled.

---

## Related Tutorials
- `add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2.md` — practical implementation of these concepts in DaVinci Resolve + Blender
- `i-recreated-movie-scene-in-blender-nuke-complete-tutorial.md` — professional compositing workflow with similar multi-pass techniques
- `replacing-adobe-after-effects-with-blender-tutorial.md` — Blender compositing context for VFX integration
