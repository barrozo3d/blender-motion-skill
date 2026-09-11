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
frame_count: 19
frame_status: complete
grounding: key-steps-anchored (19/19 steps, 2026-09-11)
frame_selection: explicit-timestamps (supplied to select_frames.py; NOT evidence that the frames were read -- see `grounding:`)
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

- [1:30] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_000.jpg
- [1:50] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_001.jpg
- [2:20] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_002.jpg
- [2:33] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_003.jpg
- [3:35] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_004.jpg
- [4:05] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_005.jpg
- [4:25] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_006.jpg
- [4:40] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_007.jpg
- [5:10] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_008.jpg
- [5:25] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_009.jpg
- [5:50] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_010.jpg
- [6:02] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_011.jpg
- [6:25] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_012.jpg
- [6:52] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_013.jpg
- [7:10] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_014.jpg
- [7:40] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_015.jpg
- [8:08] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_016.jpg
- [8:28] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_017.jpg
- [8:38] tutorials/frames/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1/frame_018.jpg

---

## Structured Notes

### Core Technique
The two things ACES manages, explained from first principles: **colour gamut** (which colours a space can hold, drawn as a region on the CIE 1931 xy diagram) and **gamma** (the transfer function mapping scene luminance to stored values). ACES 2065-1 is the answer to both — a gamut that encloses all visible light and a linear transfer function — so footage of any origin can be converted in and the artist works in one space.

### Summary
9m59s of theory, no Blender work except one demonstration. Part 1 of two; part 2 covers the actual workflow in DaVinci Resolve and Blender [transcript 0:49]. The author also made a downloadable poster of these concepts [transcript 1:06].

Gamut is developed on the **CIE 1931 xy chromaticity diagram** [frame_000]: the coloured horseshoe is the **gamut of human vision** [frame_001], real colour spaces are the triangles inside it — **DCI-P3** and **sRGB** are the two drawn [frame_002] — and **ACES 2065-1** is a triangle large enough to enclose the entire horseshoe [frame_003]. That is the whole argument for ACES as a working space: any camera's gamut fits inside it, so nothing has to be discarded on the way in.

Gamma is developed on an input/output graph [frame_004]: gamma is the exponent in `y = x^γ`, and the pair together is the **gamma transfer function** [frame_005]. `γ = 1` is linear; `0.5` and `1.5` bend the line in opposite directions [frame_006], and under a non-linear curve the arithmetic stops behaving — an input of `0.5` lands near `0.71` on output [frame_007]. Linear light is why compositing works at all, and the video proves it in Blender rather than asserting it: a cube lit by two lights, world shader black, rendered once per light and once with both [frame_008], then the two single-light renders summed with an `Add` node — the result matches the both-lights render exactly [frame_009].

Human vision is non-linear — a candle changes a dark room far more than a bright one [frame_010, frame_011] — which is why display-referred devices (phone, DSLR) bake a non-linear curve into storage [frame_012]. Scene-referred formats do not: **RAW** keeps the linear values [frame_013] and **LOG** applies a reversible log curve instead [frame_014], trading file size for recoverable range. The comparison card states the trade plainly [frame_015]. Display gamma then explains the flat look: a screen applies its own curve, which pairs with a display-referred camera's curve to look normal [frame_016, frame_017] but does not pair with LOG or RAW. ACES closes the loop — 2065-1 is linear *and* all-encompassing [frame_018], so its IDT can take footage of either kind and hand the artist one predictable space.

### Key Steps
1. **Start from the CIE 1931 xy chromaticity diagram** — the chart every colour-space discussion uses, plotting x against y from 0.0–0.8 with the spectral wavelengths (460–620 nm) marked around the curved edge [frame_000, transcript 1:21].
2. **The coloured region is the gamut of human vision** — every colour the average eye can see in nature; its boundary is what "gamut" means, the total range of a colour space [frame_001, transcript 1:37-1:49].
3. **Real colour spaces are triangles inside it.** Anything inside a triangle can be captured or displayed by that space; anything outside cannot. **DCI-P3** (dashed) and **sRGB** (dotted) are the two shown, sRGB visibly the smaller [frame_002, transcript 2:12].
4. **ACES 2065-1 is drawn as a triangle that encloses the whole horseshoe** — including regions outside human vision [frame_003]. That is why any footage can be transformed into it without clipping the source gamut [transcript 2:29-2:47].
5. **Switch to the luminance graph for gamma.** X is **luminance input**, 0.0 = black, 1.0 = white; Y is output [frame_004, transcript 3:23-3:39].
6. **Gamma is an exponent, and the pair is a transfer function.** `y = x¹` plots as a straight diagonal — **linear gamma** [frame_005, transcript 3:39-3:58].
7. **Linear arithmetic behaves.** With `γ = 1`, `0.25 + 0.25` gives `0.5` on output — twice the luminance, as expected [transcript 4:04-4:14, frame_005].
8. **Non-linear gamma bends the line.** `y = x^0.5` bows above the diagonal, `y = x^1.5` below it [frame_006, transcript 4:14-4:32].
9. **Under a curve the arithmetic stops behaving.** On the `x^0.5` curve an input of `0.5` reads out near `0.71`, so adding inputs no longer adds outputs [frame_007, transcript 4:32-4:44].
10. **Why this matters in 3D: real light is linear, and so is Blender.** Double the input, double the output; Blender renders and composites linearly by default [transcript 4:47-5:02] [no frame: spoken premise delivered over the previous graph, with nothing new on screen -- the claim is demonstrated instead in steps 11-12].
11. **The proof, built in Blender.** A cube with a light either side, the **World surface set to black** (HSV `0.000 / 0.000 / 0.000`, Strength `1.000`) so nothing else contributes; the scene is organised into collections `Elements` (Camera, Cube, Plane), `BothLights` (`Blue`, `Orange`), and `Light1` / `Light2` [frame_008, transcript 5:02-5:12].
12. **Add the two single-light renders and you get the both-lights render.** Three `Render Layers` nodes on scene `Scene` (slot 3) reading view layers **`Both On`**, **`Light1`** and **`Light2`**; the last two feed an **`Add`** node (`Clamp` off, `Fac 1.000`) into a `Viewer` (`Use Alpha` on, `Alpha 1.000`, `Z 1.000`). The sum matches the `Both On` thumbnail — which is also why multi-pass compositing works at all [frame_009, transcript 5:12-5:36].
13. **Human vision is non-linear.** A candle lit in a dark room is a large perceived change; the same candle in a bright environment barely registers, though the luminance added is identical — we are more sensitive to change in the dark end [frame_010, frame_011, transcript 5:36-6:10].
14. **Display-referred cameras** — a phone or a basic DSLR — record less light information and apply a non-linear transfer function on the way in, brightening the shadows where the eye is most sensitive, for smaller files [frame_012, transcript 6:12-6:34].
15. **Scene-referred, RAW** stores the linear light values unmodified — the transfer function is the straight diagonal — at the cost of much larger files [frame_013, transcript 6:39-7:01].
16. **Scene-referred, LOG** applies a log transfer function instead: the curve rises steeply and flattens, so shadow detail is kept without RAW's file size, and ACES can reverse it to recover the original light values [frame_014, transcript 7:01-7:24].
17. **The trade, stated side by side.** *Display-Referred*: "discards light information", "optimizes and stores only what's needed for good display". *Scene-Referred*: "collects more light information to better represent original scene" — which is what makes it the better VFX source [frame_015, transcript 7:24-7:48].
18. **Why LOG and RAW look flat on a monitor.** Every display applies its own gamma curve; that curve is designed to pair with the curve a display-referred camera already applied, and the two cancel to look normal [frame_016, frame_017, transcript 7:52-8:20]. LOG and RAW carry a different curve, so the pairing fails and the image reads flat [transcript 8:20-8:28].
19. **ACES closes both halves at once.** ACES 2065-1 is a **linear** colour space — the transfer function is `y = x` — whose gamut still encloses all visible light [frame_018, transcript 8:28-8:44]. Its input transform converts display-referred or scene-referred footage into that one space, so the artist stops worrying about the source format [transcript 8:44-9:06].

### Nodes / Settings
- **CIE 1931 xy chromaticity diagram** — x 0.0–0.8, y 0.0–0.9, spectral locus labelled 460–620 nm [frame_000]
- **Gamuts drawn**: gamut of human vision (the horseshoe) [frame_001], **DCI-P3** (dashed), **sRGB** (dotted) [frame_002], **ACES 2065-1** (solid triangle enclosing the horseshoe) [frame_003]
- **Transfer functions**: `y = x¹` linear [frame_005]; `y = x^0.5` and `y = x^1.5` non-linear [frame_006]; `0.5 → ~0.71` on the `x^0.5` curve [frame_007]; Scene-Referred RAW = straight line [frame_013]; Scene-Referred LOG = log curve [frame_014]; display gamma curve [frame_016]
- **Blender demo scene** — World Surface `Background`, Color HSV `0.000 / 0.000 / 0.000`, Strength `1.000`; collections `Elements` / `BothLights` (`Blue`, `Orange`) / `Light1` / `Light2` [frame_008]
- **Blender compositor demo** — three `Render Layers` (view layers `Both On`, `Light1`, `Light2`; scene `Scene`, slot 3) → `Add` (Clamp off, `Fac 1.000`) → `Viewer` (`Use Alpha`, `Alpha 1.000`, `Z 1.000`) [frame_009]
- **Camera categories** — display-referred (DSLR / phone) [frame_012]; scene-referred RAW [frame_013]; scene-referred LOG [frame_014]

### Difficulty
Beginner — concept-only; no Blender operation is required to follow it, and the single Blender section is a demonstration rather than a build.

### Blender Version
Any (theory only). The one Blender section shows a generic Render Layers / Add / Viewer compositor setup with no version-specific UI [frame_008, frame_009].

### Tags
color-management, aces, vfx, compositing, theory, beginner

---

## Related Tutorials
- `add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2.md` — practical implementation of these concepts in DaVinci Resolve + Blender
- `i-recreated-movie-scene-in-blender-nuke-complete-tutorial.md` — professional compositing workflow with similar multi-pass techniques
- `replacing-adobe-after-effects-with-blender-tutorial.md` — Blender compositing context for VFX integration
