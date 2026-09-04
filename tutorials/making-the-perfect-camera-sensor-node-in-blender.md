---
title: Making the perfect camera sensor node in Blender
source: YouTube
url: https://www.youtube.com/watch?v=e8g8h4CLUdY
author: Robin Squares
ingested: 2026-09-04
blender_version: "Blender 5.2"
tags: [compositing, camera, rendering, cycles, blender-5x, advanced]
extraction_status: complete
frames_dir: tutorials/frames/making-the-perfect-camera-sensor-node-in-blender/
frame_count: 11
frame_status: complete
uncertainty_frames: []
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Making the perfect camera sensor node in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=e8g8h4CLUdY)
**Author:** Robin Squares
**Duration:** 15m30s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] I am cloning my camera in Blender, duplicating every effect as accurately as possible so I
[0:07] can perfectly integrate CG into my footage.
[0:12] Previously I have duplicated distortion and color space.
[0:18] In this video I'm doing sensor noise, black level and vignette.
[0:24] Starting with vignette.


### Vignette [0:26]
**Transcript (timestamped):**
[0:31] Vignetting is this dark fade along the edge of the frame and it comes from the walls of
[0:38] the lens because less light reaches the edges of the frame because of ambient occlusion,
[0:46] which is why it gets darker.
[0:49] And it is so easy to replicate.
[0:52] Literally just open a white image on your computer and take a picture of it.
[0:57] Then open it up in Blender, set the color space, undistort the things I taught you in
[1:03] the previous video.
[1:09] Desaturate the image completely and then increase the exposure until the middle just
[1:16] about hits a value of 1.
[1:18] And you can check that by adding a greater than node and setting it to .999 and then
[1:26] as soon as you see it clip to white, that's when you know you've hit 1 in the center.
[1:31] And then go to image, save image and save that image for later.
[1:36] Now for all of our intermediate files that we create here, we're gonna try to stick to
[1:41] a standard image format.
[1:44] So I typically pick linear rec 2020.
[1:49] I save an EXR with DWAB compression, typically at 60% quality.
[1:58] If you want to know exactly why I picked all those settings, I have a blog post about that
[2:02] too, which is gonna be in the description.
[2:06] Okay, so here's how you use that image.
[2:08] You open up your footage in the compositor, you add that image as well, you gotta remember
[2:13] to set it to linear rec 2020 as the input color space because that's what we saved in.
[2:20] And then you divide that out from the footage.
[2:23] That means you're removing it and then you composite your 3D over it and then you multiply
[2:29] the vignette back over.
[2:30] So it's the same kind of thing.
[2:32] First divide then multiply because division and multiplication are opposites of each other.
[2:37] So we first remove it from the footage and we composite, multiply it back in.
[2:42] And remember to do all of this between distortion nodes because we undistorted the footage when
[2:48] saving this image, which means we also have to apply it to the undistorted footage.
[2:54] Make sense?
[2:55] And this by the way is an important concept with more complex shots like this one.
[3:01] Because here I move the plate around in camera space, so I have to know when do I apply vignetting
[3:07] and distortion and how does everything plug together.
[3:11] And this is the kind of stuff that you only really get a proper feel for if you do it yourself
[3:16] a couple times, which you can do with this exact shot.
[3:22] Because it is part of a VFX course that I made.
[3:27] Where we build this shot from scratch together.
[3:30] And we do much more than just green screen.
[3:32] We do motion tracking, color calibration, lighting, rendering, compositing, grading and
[3:40] much more.
[3:42] Here's the thing though.
[3:43] You don't just get this project.
[3:46] It is part of a whole VFX course made by Jacob from in-light VFX.
[3:53] And if you don't know Jacob, then for one go subscribe to his YouTube channel.
[3:59] And then you'll find out how good of a teacher Jacob is.
[4:02] I've already taken the course and I learned a lot.
[4:06] If you want to take it as well then please use my link in the description because it's
[4:09] an affiliate link.
[4:11] Meaning that if you grab it through that and I get a cut, which really helps me keep going.


### Black level [4:18]
**Transcript (timestamped):**
[4:23] When I render in cycles, black is completely black.
[4:28] But when you look at this footage from my camera you can see that black isn't quite
[4:33] black.
[4:34] I don't know how well that comes through the YouTube compression.
[4:36] The matter of fact is mostly because of what's called sensor noise floor.
[4:40] Every single sensor has a different noise floor.
[4:43] Not just for your camera model but your specific camera because all sensors are calibrated
[4:49] slightly differently.
[4:50] So you actually have to figure out what the noise floor is for your specific camera.
[4:55] To do that just take a picture with the lens cap on.
[4:58] Completely black picture.
[4:59] And then open that up in blender and set the input color transform.
[5:05] Then just add a color node.
[5:07] Select the eyedropper and just run it around the image.
[5:11] Just drag it over the image.
[5:13] Then you can click on that color and you see the R, G and B values will be slightly different.
[5:18] My green is a bit higher than the others for example.
[5:21] And that's your black level.
[5:22] Now worth bearing in mind, black level is going to be different depending on what color
[5:27] space you're in.
[5:28] But keep your tongue straight throughout all this.
[5:31] So this value is going to change depending on your ISO level on your camera.
[5:37] ISO is a setting.
[5:39] It boosts the analog signal of the sensor.
[5:43] And since it's going to be different based on what ISO you're on, you also have to sample
[5:47] this at the same ISO level that your shot is on.
[5:51] So we subtract that color and remember to use the same color as sampled with your ISO
[5:57] level.
[5:58] So you subtract that.
[6:00] That brings your black level to actual pure black.
[6:05] And then you composite your 3D which also is on pure black.
[6:10] And then you add back in the black level.
[6:12] So use a mixed color node set to add same color value.
[6:16] Where in the chain does this go?
[6:18] We are starting to have so many different effects that just going through it per effect.
[6:22] It's going to be a bit tedious.
[6:24] So I'm going to save that for the end.
[6:26] When we have all the puzzle pieces on the table, I'm going to tell you what order everything
[6:30] is in.
[6:31] For now, let's skip to the next one which is...


### Sensor noise [6:33]
**Transcript (timestamped):**
[6:39] Sensor noise is this nasty looking grain.
[6:42] It is worse at higher ISO levels and in dark areas.
[6:47] On a digital camera, the noise is caused by little electrical fluctuations in the camera's
[6:52] electronics.
[6:54] As much as I loathe the look of it, it's there.
[6:59] So we have to replicate it.
[7:00] I went outside and I pointed my camera at a white wall.
[7:04] I knocked it out of focus and exposed up.
[7:09] I'm doing it outside because if there is a slight mismatch between my camera frame rate
[7:16] and the refresh rate on my monitor or a light inside, then you might get subtle flickering.
[7:24] We just want to remove all the possibilities for that kind of stuff.
[7:28] I just went outside in the sunlight which doesn't have any flickering.
[7:33] Then record three or four different light levels from lens cap, black to pure white.
[7:40] Because noise is slightly different from dark to light.
[7:44] We want to capture a good range of different light levels.
[7:48] It's fine if each shot isn't perfectly evenly colored, but it should be close to even.
[7:54] For example, this shot which is a rock out of focus is fine, but it's verging on not fine.
[8:02] Try to find quite evenly colored surfaces.
[8:06] And again, noise changes with your ISO.
[8:09] Try to use the same ISO as the footage that you're matching.
[8:13] Now to extract the noise from the footage.
[8:16] We bring the footage into the Blender compositor and set its color space.
[8:20] Do not undistort.
[8:23] Because you know, the light comes through the camera lens, it's distorted and then
[8:27] it hits the camera sensor.
[8:29] So the noise, the sensor noise is not distorted by a lens.
[8:34] So we should not distort it now either.
[8:37] Okay, but now we need to denoise the footage.
[8:40] So we need a clean version of the image to compare to the noisy version of the image.
[8:46] You might think that you could just use a denoise node in Blender.
[8:49] You would be forgiven for thinking that, but as I add a denoise node, nothing happens.
[8:55] And that's because the denoise node in Blender is not made for this kind of noise, it's
[8:59] made for render noise, which looks different.
[9:01] So we gotta do this the old fashioned way.
[9:05] Which is to mix frames together.
[9:07] So here's what you do.
[9:08] You just copy the clip and then you offset the frame by one.
[9:13] And then you just mix those two together.
[9:15] If you have the node wrangler add on enabled, I think it's control shift right click drag
[9:19] between them and that will just mix those two together.
[9:22] And if you compare the result of that to any of the two frames, you'll see that the noise
[9:26] is effectively halved.
[9:27] So let's just do this over again.
[9:31] So I just select all that, I duplicate it over and then holding down alt and moving
[9:37] the frame, that'll move the frames of both of those nodes at the same time.
[9:41] So then I pick the next couple frames and mix the result of those groups together.
[9:46] And I just keep doing that.
[9:48] So I duplicate all of that, alt clicking on the frame number to bump all of those frames
[9:55] up and then mix that together.
[9:56] And I do that over and over again.
[10:00] I think I ended up with 32 different frames.
[10:07] And in any case, at the very end, the noise is almost completely gone.
[10:12] But we want it as gone as we can possibly get it.
[10:15] So I add a blur node at the end as well.
[10:18] Now the blur node is a little bit iffy to add because we really, really want to keep
[10:23] the background the same and only remove the noise.
[10:27] So only blur if it doesn't significantly affect your background as well.
[10:33] The background needs to be very even for blurring to work.
[10:37] And I only blur a tiny amount, like at most 4 pixels.
[10:42] And by the way, this process of blending together different frames of the footage can be automated
[10:47] in other compositing software like Fusion.
[10:51] But it's kind of fun to see how far you can get in Blender and it doesn't take that
[10:54] much work.
[10:55] Okay, so I do this for all my different lighting ranges.
[10:59] And then I save out the result of each of them because this whole chain takes a while
[11:04] to calculate.
[11:05] So it's worth just saving the resulting image.
[11:08] And then I bring all of those saved images back in.
[11:12] And now I have a noise free version of every shot and I have a noisy version of every shot.
[11:19] Let's compare those together using a divide node in the mix color that is.
[11:25] I never remember which goes at the top.
[11:27] I think the noisy version goes at the top and the noise free version goes at the bottom,
[11:32] but you'll see that on screen, the correct version now.
[11:34] And the result of that is what we call a noise delta.
[11:38] The result is the noise itself, isolated.
[11:44] So let's render out a few frames of each of them.
[11:47] I just set my frame range and then I render out just some noise deltas from every single
[11:52] lighting range.
[11:54] And now I have the noise that is applied to darkness, middle and light.
[11:59] Okay, so now to apply that to the composite.
[12:03] This is a point where Blender is not quite up to the task because, again, previously when
[12:10] we've applied all of these effects, we have first removed it from the original footage
[12:16] and then composite it and then applied it.
[12:19] Blender cannot remove noise from the footage as we have discovered.
[12:24] So the typical workflow here is to denoise the footage in another software, bring it
[12:29] in composite and then multiply the noise over.
[12:33] We do it with a multiply node.
[12:35] Now if you really don't want to use another software, you can also multiply this noise
[12:41] over only the render before overlaying it onto the entire thing.
[12:47] But that does create problems later on with the order of operations.
[12:52] Because then, once we go to distort the footage along with the render, then we distort the
[12:58] noise as well, which is incorrect.
[13:00] So I really would recommend that you go to another software, you denoise the footage,
[13:05] bring it into Blender, possibly in Linear Rec 2020.
[13:10] Then you composite everything and then you multiply the noise over.
[13:14] Now remember, we captured noises at different lighting levels.
[13:19] So here's what we can do.
[13:20] We can multiply each of those sequences separately.
[13:23] So now we have a version of the footage with a lot of noise, one with a medium amount of
[13:27] noise and one with very little noise.
[13:30] Those correspond to different lighting levels.
[13:33] So we can mix them using the lighting levels.
[13:36] And we do that in the compositor with a separate color node.
[13:39] You set that to YCBCR.
[13:42] And from that node, the Y output corresponds to the luminosity of your footage.
[13:49] That is basically the lightness.
[13:51] And then we can use that specifically to mix between these noise versions.
[13:57] So we know that in the very dark, say maybe below 0.1, we want to use the noisy version
[14:04] and then above, I don't know, 2, we use the very bright version.
[14:10] What are the exact values that you want to use?
[14:13] You can actually find out by sampling the footage that you filmed originally.
[14:19] So all of those noise samples were taken at different lighting levels.
[14:22] So you can just run an eyedropper over each of those and you'll see what lighting level
[14:27] you captured at.
[14:29] And that is the lighting level that is appropriate to mix that noise in.
[14:33] And that might get a bit complicated, so you can also just use artistic license.
[14:38] But if you do it like this, then the noise that you apply will basically perfectly match
[14:47] the original footage.
[14:49] And it will have replicated your specific camera's noise response to lighting.
[14:54] And now we're done with the intermediate stage and you have three new effects that
[14:58] you can slap on your footage.
[15:00] Vignette, sensor noise and black level.
[15:03] The next video is the advanced tier where we'll go through Bokeh, glare, lens breathing
[15:11] and chromatic aberrations.
[15:13] And at the very end, I'll put it all together in one big graph to show you how it all connects.
[15:19] Okay, so we start of course by importing our movie clip.
[15:23] So let's go to the movie clip editor, press open and just go to where I have my EXR sequence
[15:29] stored.



---

## Captured Frames

- [1:20] tutorials/frames/making-the-perfect-camera-sensor-node-in-blender/frame_000.jpg
- [1:52] tutorials/frames/making-the-perfect-camera-sensor-node-in-blender/frame_001.jpg
- [2:15] tutorials/frames/making-the-perfect-camera-sensor-node-in-blender/frame_002.jpg
- [5:09] tutorials/frames/making-the-perfect-camera-sensor-node-in-blender/frame_003.jpg
- [6:12] tutorials/frames/making-the-perfect-camera-sensor-node-in-blender/frame_004.jpg
- [8:52] tutorials/frames/making-the-perfect-camera-sensor-node-in-blender/frame_005.jpg
- [9:15] tutorials/frames/making-the-perfect-camera-sensor-node-in-blender/frame_006.jpg
- [10:02] tutorials/frames/making-the-perfect-camera-sensor-node-in-blender/frame_007.jpg
- [10:20] tutorials/frames/making-the-perfect-camera-sensor-node-in-blender/frame_008.jpg
- [11:28] tutorials/frames/making-the-perfect-camera-sensor-node-in-blender/frame_009.jpg
- [13:40] tutorials/frames/making-the-perfect-camera-sensor-node-in-blender/frame_010.jpg

---

## Structured Notes

### Core Technique
Measuring three *sensor*-side camera artefacts — **vignette**, **black level** and **sensor noise** — from calibration footage shot on the actual camera, and applying each as a remove-then-restore pair in the compositor so CG can be integrated in between.

### Summary
The intermediate tier of a lens-cloning series (distortion and colour space came before; bokeh, glare, lens breathing and chromatic aberration come after, in **"Making my lens in Blender"**). Each effect follows the same shape: capture it once from the real camera, divide or subtract it out of the plate, composite the CG into the now-clean image, then multiply or add it back. The sharpest lesson is a boundary: vignette is a *lens* artefact and must be handled inside the undistort/redistort bracket, while sensor noise happens *after* the lens and must never be undistorted. Blender cannot denoise real sensor noise at all — its Denoise node targets render noise — so the noise-free reference is built by mixing ~32 offset copies of the footage in a binary cascade.

### Key Steps

**Vignette** `[transcript 0:26-3:20]`
1. **Understand the cause.** Darkening toward the frame edge, caused by the lens walls occluding light — effectively ambient occlusion inside the barrel `[transcript 0:31-0:46]`.
2. **Capture it.** Photograph a plain white image on a monitor with the real camera `[transcript 0:52-0:56]`.
3. **Prepare the plate.** Load in Blender, set the input colour space, and **undistort** it using the previous video's method `[transcript 0:57-1:03]`.
4. **Normalise it.** Desaturate fully, then raise exposure until the centre just reaches a value of 1. Verify by adding a **`Greater Than`** node set to `0.999` — the moment the centre clips to white, you are at 1 `[transcript 1:09-1:30]`.
5. **Save in a consistent intermediate format** — the author standardises on **Linear Rec.2020**, EXR with **DWAB compression at ~60% quality** `[transcript 1:36-1:57]`.
6. **Apply it.** Load the saved vignette alongside the footage, **setting its input colour space to Linear Rec.2020 to match what was saved** `[transcript 2:06-2:19]`. Then **divide** it out of the plate, composite the CG, and **multiply** it back over `[transcript 2:20-2:36]`.
7. **Mind the bracket.** All of this must happen *between* the distortion nodes, because the vignette image was saved undistorted and therefore applies to undistorted footage `[transcript 2:42-2:53]`.

**Black level** `[transcript 4:18-6:32]`
8. **Understand the cause.** Cycles renders true black; a real sensor does not, because of its **noise floor** — which differs per individual camera body, not just per model `[transcript 4:23-4:53]`.
9. **Measure it.** Take a photo with the lens cap on, open it in Blender, set the input colour transform `[transcript 4:55-5:04]`.
10. **Sample it.** Add a `Color` node, use the eyedropper across the black frame; the R, G and B values come out slightly different (the author's green sits higher) — that is the black level `[frame_003]` `[transcript 5:05-5:21]`.
11. **Two things change it.** The value depends on the **colour space** you are working in, and on the camera's **ISO**, since ISO boosts the analog sensor signal. Sample at the same ISO as the shot `[transcript 5:22-5:50]`.
12. **Apply it.** **Subtract** that colour to bring the plate to true black, composite the CG (also on true black), then **add** it back with a `Mix Color` node set to `Add` using the identical value `[transcript 5:51-6:15]`.

**Sensor noise** `[transcript 6:33-14:53]`
13. **Capture the noise.** Point the camera at a white wall, defocus, and overexpose. Shoot **outdoors** — indoor lighting or a monitor can beat against the camera's frame rate and introduce flicker `[transcript 7:00-7:32]`.
14. **Capture a range.** Three or four different light levels from lens-cap black to pure white, because noise differs between dark and light. Surfaces should be close to evenly coloured `[transcript 7:33-8:05]`.
15. **Match ISO** to the footage being matched `[transcript 8:06-8:12]`.
16. **Do NOT undistort the noise.** Light is distorted by the lens *before* it reaches the sensor, so sensor noise is not lens-distorted and must not be treated as if it were `[transcript 8:20-8:36]`.
17. **Blender's `Denoise` node will not help.** Adding it does nothing here — it is built for render noise, which looks different `[transcript 8:40-9:01]`.
18. **Build the clean reference by frame-mixing.** Duplicate the clip, offset it by one frame, and mix the two — noise halves. Repeat in a binary cascade, `Alt`-dragging the frame number to bump paired nodes together, up to roughly **32 frames** `[frame_006]` `[transcript 9:05-10:11]`.
19. **Finish with a small blur** — at most about **4 pixels**, and only if it does not visibly affect the background, which must be very even for this to be safe `[transcript 10:15-10:41]`.
20. **Cache the result.** The cascade is slow to evaluate, so save each light level's clean plate out and re-import `[transcript 10:55-11:11]`.
21. **Extract the noise delta.** `Mix Color` set to **`Divide`**, noisy version over noise-free version — the result is the isolated noise `[frame_009]` `[transcript 11:12-11:43]`. The author flags his own uncertainty about which input goes on top and defers to the on-screen version `[transcript 11:25-11:33]`.
22. **Render out noise deltas** for each lighting range `[transcript 11:44-11:58]`.
23. **Accept the workflow limitation.** Because Blender cannot remove noise from the plate, the recommended route is to **denoise the footage in other software**, bring it back (Linear Rec.2020), composite, then **multiply** the noise over `[transcript 12:03-13:13]`. Multiplying noise onto only the render is possible but breaks the order of operations, since the subsequent distortion would then distort the noise too — which is wrong `[transcript 12:35-12:59]`.
24. **Blend the noise levels by luminance.** `Separate Color` set to **`YCbCr`**; its `Y` output is luminosity, and that drives the mix between the dark, medium and bright noise versions `[frame_010]` `[transcript 13:33-13:56]`.
25. **Find the thresholds empirically.** Eyedropper each original noise sample to read the light level it was captured at; that is the level at which it should be mixed in. Artistic license is offered as the alternative `[transcript 14:13-14:38]`.

### Nodes / Settings
- **`Greater Than`** — set to `0.999`, used to confirm the vignette centre has reached a value of 1 `[transcript 1:18-1:30]`
- **Intermediate file standard** — **Linear Rec.2020**, EXR, **DWAB** compression at ~60% quality `[transcript 1:44-1:57]`
- **Vignette application** — `Mix Color` `Divide` before compositing, `Multiply` after, both inside the undistort/redistort bracket `[transcript 2:20-2:53]`
- **Black-level source** — clip `Black 400ISO`, input colour space **V-Log V-Gamut**, `Alpha: Straight`, Movie type `[frame_003]`
- **`Color` node** — holds the eyedroppered black-level value; R/G/B differ slightly `[frame_003]`
- **Black-level application** — subtract before, `Mix Color` set to `Add` after, same value both sides `[transcript 5:51-6:15]`
- **Noise plates** — `clone_noisePlate_*_black_##.exr` and `*_darkGray_##.exr` as **64-frame image sequences**, plus `clone_noise_plate_denoised_0.02.exr` / `_0.1.exr` as single images; all `Linear Rec.2020`, `Premultiplied` `[frame_009]`
- **Noise delta** — `Mix Color` set to **`Divide`**, `Clamp Factor` on, `Factor 1.000` `[frame_009]`
- **Noise application** — `Mix Color` set to **`Multiply`** `[frame_010]`
- **`Separate Color`** — mode **`YCbCr`** (options: `RGB`, `HSV`, `HSL`, `YCbCr`, `YUV`); `Y` used as the luminance mask `[frame_010]`
- **`Denoise` node** — explicitly *not* usable for sensor noise `[transcript 8:40-9:01]`
- **Blur** — at most 4 px, conditional on an even background `[transcript 10:33-10:41]`
- **Render** — Cycles, GPU Compute, `Max Samples 4096` `[frame_003]`; Color Management varies by task — `AgX / High Contrast` at exposure `6.490` while inspecting noise `[frame_006]`, `Filmic / Medium Contrast` for the composite `[frame_010]`

> **Series position, stated by the source.** This is the intermediate tier: distortion
> and colour space were covered previously `[transcript 0:12-0:17]`, and the next video is
> the advanced tier covering "Bokeh, glare, lens breathing and chromatic aberrations"
> `[transcript 15:03-15:12]` — which is
> [Making my lens in Blender](making-my-lens-in-blender-bokeh-glare-chromatic-aberrations.md),
> already in this library. That video's 15-step order-of-operations graphic is where these
> three effects get their positions: black level subtract/add at steps 2 and 14, divide/
> multiply vignette at 5 and 10, and de-noise/re-noise at 3 and 13.
>
> **Transcript tail bleed.** The final lines `[transcript 15:19-15:29]` ("we start of
> course by importing our movie clip… movie clip editor, press open… EXR sequence") are
> the opening of the *next* video, carried over as an end-card teaser. They describe
> content documented in the sequel's entry, not this one.
>
> **Affiliate promo** at `[transcript 3:22-4:16]` (InLightVFX course) is excluded — the
> same course promoted in two other entries in this library.

### Difficulty
Advanced

### Blender Version
Blender 5.2.0 — read from the status bar in `[frame_003]`, `[frame_006]`, `[frame_009]` and `[frame_010]`. Never stated in narration.

### Tags
compositing, camera, rendering, cycles, blender-5x, advanced

---

## Related Tutorials
- [Making my lens in Blender (Bokeh, glare, chromatic aberrations)](making-my-lens-in-blender-bokeh-glare-chromatic-aberrations.md) — the direct sequel, named as such by this video; its 15-step order of operations places all three effects documented here
- [I made the VFX tool Blender was missing... (Full Workflow)](i-made-the-vfx-tool-blender-was-missing-full-workflow.md) — supplies the undistort/redistort bracket this video's vignette step must sit inside; shares compositing, camera, rendering
- [A FULL Blender Compositor Course!](a-full-blender-compositor-course.md) — the compositor fundamentals underneath the divide/multiply and subtract/add pairs; shares compositing, rendering
