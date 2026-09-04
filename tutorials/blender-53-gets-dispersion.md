---
title: Blender 5.3 gets dispersion!
source: YouTube
url: https://www.youtube.com/watch?v=Q9irGPAcUDE
author: Christopher 3D
ingested: 2026-09-04
blender_version: "Blender 5.3"
tags: [materials, shaders, glass, rendering, cycles, blender-5x, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-53-gets-dispersion/
frame_count: 10
frame_status: complete
uncertainty_frames: []
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender 5.3 gets dispersion!

**Source:** [YouTube](https://www.youtube.com/watch?v=Q9irGPAcUDE)
**Author:** Christopher 3D
**Duration:** 12m11s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] If you saw my last video on OpenPBR, I mentioned that developers are retrofitting the Principled BSDF
[0:06] with features from OpenPBR where it makes sense to do so.
[0:10] Blender 5.3 just received one of these major additions.
[0:14] Dispersion has been added directly to the transmission channel with two new controls that let you adjust how this function operates.
[0:22] These are the ABBA number and dispersion scale parameters.
[0:27] Dispersion simulates a much more realistic way that light refracts.
[0:31] In the real world, light doesn't bend uniformly using a single index of refraction.
[0:36] White light is a continuum of wavelengths across the visible spectrum, roughly 380 to 750 nanometers,
[0:43] because each wavelength travels through a transparent material at a slightly different speed, the rays separate.
[0:50] This variation in the index of refraction bends each wavelength onto a slightly different path,
[0:56] producing that characteristic rainbow effect.
[0:59] The degree to which a material disperses light is governed by a physical measurement called the ABBA value, or ABBA number.
[1:07] This number describes how much the core refractive index spreads across the visible spectrum.
[1:12] The ABBA number is named after the German physicist Ernst ABBA,
[1:17] who introduced it as a simple way to quantify a material's dispersion,
[1:21] meaning how strongly its refractive index changes with wavelength.
[1:27] Here is the key rule to remember.
[1:29] The ABBA scale is inverse.
[1:31] A high ABBA value means a tiny spread of index of refraction values, which creates less dispersion.
[1:38] A low ABBA value means a wide spread of IOR values, which creates more dispersion.
[1:44] Most optical materials, like glass, plastics, crystals used in rendering or optics, fall roughly in the 20 to 100 range.
[1:53] Very high dispersion materials start around 20 to 30.
[1:57] Common mid-range dispersion materials fall in the 30 to 60 range,
[2:02] and lower dispersion materials go up to 60 to 95, with a few outliers near or slightly above 100.
[2:12] For instance, common glass is in the middle with an ABBA number of about 55.3.
[2:18] It'll produce just a small to average amount of dispersion.
[2:22] It'll produce just a nice, small bit of detailed dispersion in the glass that'll provide realism,
[2:28] but it won't give you an excessive rainbow effect.
[2:31] So, in the principle of BSDF, you still set your standard base index of refraction.
[2:37] For instance, 1.52 for common glass.
[2:40] The ABBA value then tells the engine how much to vary the index of refraction across the spectrum away from your target number.
[2:48] Because the ABBA numbers are laboratory measured, they're documented for almost every real-world material.
[2:55] You don't have to guess, although you can certainly push those values for artistic effects.
[3:00] As a general rule of thumb, higher density materials usually have higher index of refraction numbers and lower ABBA values,
[3:08] meaning more pronounced dispersion.
[3:11] If you look at this chart, you'll notice a general trend.
[3:14] As the index of refraction goes up, ABBA values often drop, increasing dispersion.
[3:21] But there are important exceptions.
[3:23] Diamond has a significant index of refraction of 2.417, but its ABBA value is actually around 55.
[3:30] It gets its famous internal fire or sparkle, not because its ABBA value is super low,
[3:36] but because its extreme refractive index bends light so intensely
[3:40] that even a moderate ABBA value spreads the spectrum across dramatic angles.
[3:46] Now that we've covered the fundamentals of what dispersion is,
[3:49] we need to address a major issue you might run into if using default clamping values,
[3:54] a noticeable green cast or tint that often appears inside of refractive glass.
[4:00] So what's causing this green tint and how do we fix it?
[4:04] To understand the problem, we have to look at how cycles handles dispersion under the hood.
[4:09] Internally, cycles doesn't use the quick and dirty trick that legacy shader add-ons relied,
[4:15] simply splitting the RGB channels into three hard offsets.
[4:19] Instead, it uses a quasi-spectral approximation based on the ABBA number.
[4:25] It simulates wavelength-dependent light transport, calculates the correct refraction angle for that specific wavelength,
[4:32] and converts the result back into RGB using a CIE color matching function.
[4:39] This approach allows cycles, which is at its heart an RGB renderer,
[4:43] to simulate spectral calculations in order to produce smooth, continuous spectral dispersion.
[4:49] But here's where the problem starts.
[4:51] When cycles convert spectral wavelength data into RGB using the CIE standard observer functions,
[4:58] some red and blue rays can translate into significant floating-point RGB spikes.
[5:04] Because these high-energy spikes easily shoot past your clamp threshold,
[5:08] cycles more readily truncates the red and blue ends of the spectrum,
[5:13] leaving the green wavelengths to dominate the scene.
[5:16] What's more, the human visual system is far more sensitive to green wavelengths,
[5:21] which is part of the reason that mid-range green values can be apparently lower than red and blue values,
[5:27] yet still dominate.
[5:28] If we look at the human eyes luminosity curve,
[5:31] our visual sensitivity peaks right in the green spectrum around 550 nanometers.
[5:38] In fact, when Ernst Abbe developed the ABBE number to quantify dispersion in glass,
[5:43] he specifically anchored his calculations around the reference wavelengths
[5:47] that bracket this exact visual peak.
[5:50] So this gives you some context for why your dispersive mediums
[5:54] may look greenish when the clamping value is too low.
[5:58] By default, Blender has historically set indirect clamping to tan,
[6:02] which is far too aggressive for spectral dispersion.
[6:06] Back in the early days of cycles, aggressive clamping was necessary to manage fireflies.
[6:11] But with modern advanced denoising technology,
[6:15] that default clamp value of 10 really does more harm than good
[6:19] by choking your dispersion rays.
[6:22] It also reduces light in the scene overall, resulting in energy loss.
[6:27] So it's important to rethink the clamping value.
[6:30] A value of 50 is often going to be sufficient to reduce the green tint quite a bit.
[6:35] But even higher values might be better for a given scene,
[6:39] and under some circumstances, turning clamping off entirely might be warranted.
[6:45] What's important to note is that when you raise the clamping value,
[6:48] you'll notice that a fair amount of light energy was being terminated too early
[6:52] with the default lower values,
[6:54] and resetting clamping to a higher value
[6:57] will result in overall more accurate light transport.
[7:02] So let's just come over here and take a look at this really quick.
[7:04] So you can see here, I have the principal BSDF,
[7:08] and under transmission, we now have dispersion scale and the obin number.
[7:13] So in this case, dispersion scale, just turn it to one as the default.
[7:18] That means it's in full effect.
[7:20] The scale allows you to take it and say,
[7:22] if you only want dispersion to have about 50% strength, set it to .5.
[7:28] So I usually just set it to one and then you set the obin number here.
[7:33] Now, in order for the clamping, so right now I've got the default clamping of 10.
[7:37] You can see there's sort of greenishness going on.
[7:40] So you come under render properties,
[7:45] and then you come down to light paths,
[7:48] and you see where it says clamping, indirect light.
[7:52] You want to change this value, and I find that 50 is often a pretty good value.
[7:57] When you start the initial rendering, it's still going to look kind of green.
[8:02] So just let it accumulate enough samples for that greenishness to start going away.
[8:08] And if you're finding that you're still seeing it,
[8:11] then you can start playing with going with higher values.
[8:17] So let's take a look at some examples now.
[8:19] I've got these bathroom objects in this scene.
[8:22] You can see that there's this kind of odd coloration,
[8:25] although we can see a little bit of dispersion on the top of the glass.
[8:29] This is with the default clamping of 10.
[8:32] If we go ahead and change the clamping up to 50, we get that.
[8:36] So we cycle back and forth,
[8:39] and you can see the difference between those two different clamping values.
[8:43] Now, if we go ahead and just turn off clamping altogether, then we get this.
[8:48] So in this particular case, turning off clamping really brought out all the illumination.
[8:55] 50 is only a starting point.
[8:57] It could be that you're going to have some fireflies that show up,
[9:01] and you need to try a value for clamping of say 50 or even 200 to eliminate them possibly.
[9:09] Here's another example. You can see these bathroom objects.
[9:12] This is with the default clamping of 10, how green they are.
[9:16] But as soon as we go to clamping of 50, we get that.
[9:20] It removes most of it.
[9:22] Now, here's an interesting situation where if I go up to clamping of say 75,
[9:27] we see almost no difference in this particular scene.
[9:30] So it really doesn't benefit us to turn off clamping.
[9:34] In fact, I want to show you next an example where turning off clamping would actually be counterproductive.
[9:41] So here's an example that doesn't have dispersion, but we want to talk about clamping and turning off clamping as a potential option.
[9:49] This is with the default 10.
[9:51] If we go to clamping of 50, you can see that that scene lightened up.
[9:58] And now let's go to 100 for clamping.
[10:01] And you can see it brought in a little bit more brightness.
[10:05] Now let's just turn off clamping altogether.
[10:09] And look at what happens.
[10:12] Take a look at these splotches up on the cabinet on the right side.
[10:16] You can see some other kind of light splotchy areas.
[10:19] That is when you turn off clamping.
[10:21] It introduces fireflies that can be so strong that the denoiser just produces artifacts because of their inclusion.
[10:29] So let's talk about render times for a minute because I know some people are going to ask how much of a penalty is there for using dispersion.
[10:36] And surprisingly, it's actually not too bad.
[10:40] Here's this material test to render it 2K without dispersion.
[10:44] Two minutes and 10 seconds.
[10:46] When I turned dispersion on, it rendered in two minutes and 32 seconds.
[10:51] So not too bad for the extra overhead incurred to render that.
[10:56] Here's this simple scene without dispersion turned on.
[10:59] It took three minutes, 52.
[11:01] When we turn on dispersion, we get four minutes and 17 seconds.
[11:06] So a little bit longer, but it's really not too bad for what you're getting in terms of the extra complexity of dispersion.
[11:13] And then finally, here's a little bit more of a complex interior scene with all this refraction without dispersion.
[11:20] It was 33 minutes, 48 seconds.
[11:22] And with dispersion, it was 37 minutes, 48 seconds.
[11:27] So you get just a sense for the differential, the extra time needed to render dispersion.
[11:32] It's really not too bad considering the complexity of that rendering process.
[11:39] Now, one final note on rendering.
[11:42] Dispersion may require the use of higher sample counts.
[11:45] Splitting light into individual spectral paths spreads energy across more pixels,
[11:50] making caustics and refractive materials harder to converge.
[11:55] Modern denoisers are smart enough to resolve spectrally dispersed samples into clean white light.
[12:01] But giving them a higher sample count can help to prevent blotchy, muddy caustics,
[12:07] and ensure sharp, accurate surfaces.



---

## Captured Frames

- [3:16] tutorials/frames/blender-53-gets-dispersion/frame_000.jpg
- [5:33] tutorials/frames/blender-53-gets-dispersion/frame_001.jpg
- [7:10] tutorials/frames/blender-53-gets-dispersion/frame_002.jpg
- [7:50] tutorials/frames/blender-53-gets-dispersion/frame_003.jpg
- [8:33] tutorials/frames/blender-53-gets-dispersion/frame_004.jpg
- [8:46] tutorials/frames/blender-53-gets-dispersion/frame_005.jpg
- [10:14] tutorials/frames/blender-53-gets-dispersion/frame_006.jpg
- [10:22] tutorials/frames/blender-53-gets-dispersion/frame_007.jpg
- [10:47] tutorials/frames/blender-53-gets-dispersion/frame_008.jpg
- [11:29] tutorials/frames/blender-53-gets-dispersion/frame_009.jpg

---

## Structured Notes

### Core Technique
Using the native `Dispersion Scale` and `Dispersion Abbe Number` controls added to the Principled BSDF transmission channel in Blender 5.3, and raising Cycles' indirect light clamp to stop that clamp from truncating the spectrum into a green cast.

### Summary
Blender 5.3 retrofits OpenPBR-style dispersion directly into the Principled BSDF's transmission channel, replacing the old trick of splitting RGB into three hard IOR offsets. Cycles instead runs a quasi-spectral approximation driven by the Abbe number and converts back to RGB through a CIE colour matching function. The practical catch is that Blender's historical indirect clamp of `10.00` truncates the red and blue spectral spikes this produces, leaving green to dominate — so the feature ships looking wrong until the clamp is raised. Covers the physics, an IOR/Abbe reference table for real materials `[frame_000]`, the clamp fix with a worked counter-example where disabling clamping entirely is harmful, and measured render-time overhead.

### Key Steps
1. **Set the base IOR as usual.** Dispersion does not replace the index of refraction — you still set it normally (1.52 for common glass), and the Abbe number then tells the engine how far to vary IOR across the spectrum away from that target `[transcript 2:31-2:47]`.
2. **Set `Dispersion Scale`.** Found under Principled BSDF, Transmission, alongside `Weight`. `1.000` is full effect; `0.5` gives roughly 50% strength `[frame_002]` `[transcript 7:13-7:28]`.
3. **Set `Dispersion Abbe Number`.** Shown at `55.000` for glass `[frame_002]`. **The scale is inverse**: a *high* Abbe value means a narrow IOR spread and *less* dispersion; a *low* value means a wide spread and *more* `[transcript 1:29-1:43]`. Most optical materials fall in roughly 20–100 `[transcript 1:44]`.
4. **Look the value up rather than guessing.** Abbe numbers are laboratory-measured and documented for nearly every real material `[transcript 2:48]`. The on-screen table `[frame_000]` gives IOR / Abbe pairs: Fluorite 1.434/95, Fused Quartz 1.458/68, Crown Glass 1.517/64, Rock Crystal 1.550/67, Emerald 1.580/60, Topaz 1.620/61, Dense Flint Glass 1.690/34, Peridot 1.700/47, Lead Crystal 1.700/33, Spinels 1.720/61, Sapphire/Ruby 1.760/72, Garnet 1.800/35, Zircon 1.900/36, Cubic Zirconia 2.170/32, Diamond 2.417/55, Moissanite 2.650/20.
5. **Understand the diamond exception.** The general trend is that higher IOR pairs with lower Abbe and more dispersion, but diamond's famous fire comes from its extreme IOR (2.417) bending light so intensely that even a moderate Abbe of 55 spreads the spectrum across dramatic angles `[transcript 3:23-3:45]` `[frame_000]`.
6. **Fix the green cast by raising the indirect clamp.** Render Properties, Light Paths, Clamping, `Indirect Light` — default `10.00` `[frame_003]`. Set it to `50` as a starting point `[transcript 7:52-7:56]`.
7. **Let samples accumulate before judging.** The render still looks green early in the sampling; the cast resolves as samples build `[transcript 7:57-8:07]`.
8. **Compare, do not assume more is better.** The A/B progression on the same scene: `10` `[frame_004]`, `50` `[frame_005]`, `100` `[frame_006]`. Beyond a point there is almost no visible difference, so turning clamping off buys nothing `[transcript 9:22-9:30]`.
9. **Know when disabling clamping backfires.** With clamping `OFF`, fireflies return strongly enough that the denoiser produces artifacts — visible as light splotches on the cabinet, arrowed on screen `[frame_007]` `[transcript 10:12-10:28]`. This example has no dispersion at all; it is purely about the clamp.
10. **Budget the overhead.** Material test at 2K: `2:10` without dispersion `[frame_008]` versus `2:32` with `[transcript 10:44-10:50]`. Simple scene `3:52` to `4:17` `[transcript 10:56-11:01]`. Complex refractive interior `33:48` to `37:48` `[transcript 11:20-11:27]`.
11. **Raise samples for dispersive materials.** Splitting light into spectral paths spreads energy across more pixels, making caustics and refractive surfaces harder to converge; higher sample counts prevent blotchy, muddy caustics even though modern denoisers resolve dispersed samples into clean white light `[transcript 11:42-12:07]`.

### Nodes / Settings
- **Principled BSDF, Transmission** — `Weight 1.000`, `Dispersion Scale 1.000`, `Dispersion Abbe Number 55.000` `[frame_002]`
- **Render Properties, Light Paths, Clamping** — `Direct Light 0.00`, `Indirect Light 10.00` (the default that causes the green cast; raise to `50`+) `[frame_003]`
- **Render Properties, Light Paths, Caustics** — `Filter Glossy 0.00`, `Reflective` on, `Refractive` on `[frame_003]`
- **Render engine** — Cycles, `GPU Compute`, `Noise Threshold 0.1000`, `Max Samples 1024`, `Min Samples 0` `[frame_002]`
- **Material shown** — `Dispersion Glass` on object `External Sphere` / `Sphere.002` `[frame_002]`
- **Reference data** — IOR/Abbe table for 16 materials `[frame_000]`; photopic vision sensitivity curve peaking near 550 nm `[frame_001]`

> **Terminology — the transcript is mostly wrong here, but not uniformly.** Whisper
> renders the term as "ABBA number" for the whole first half and once as "obin number"
> `[transcript 7:08]`, then spells it correctly at `[transcript 5:38]` ("Ernst Abbe
> developed the ABBE number"). The controls are named **`Dispersion Scale`** and
> **`Dispersion Abbe Number`** `[frame_002]`, after the German physicist Ernst Abbe.
> Same pattern with the clamp default: Whisper writes "indirect clamping to tan"
> at `[transcript 5:58]` but "that default clamp value of 10" at `[transcript 6:15]`.
> The field reads `10.00` `[frame_003]`. Worth noting for anyone tuning the transcript
> floor — a term can be mangled in one pass and clean in another within the same file,
> so a single correct occurrence is not evidence the rest are reliable.
>
> **One unresolved disagreement.** The narration says common glass has an Abbe number of
> "about 55.3" `[transcript 2:12]`, but the on-screen chart lists Crown Glass at **64**
> `[frame_000]` — 55 is the value on Diamond's row. Both are recorded; the chart is the
> more reliable witness per the frame-over-transcript convention, and the demo material
> is in fact set to `55.000` `[frame_002]`.

### Difficulty
Intermediate

### Blender Version
Blender 5.3.0 Alpha — read from the title bar (`Material Object 01 _ dispersion.blend — Blender 5.3.0 Alpha`) and the status bar in `[frame_002]` and `[frame_003]`. Narration says only "Blender 5.3" `[transcript 0:10]`.

### Tags
materials, shaders, glass, rendering, cycles, blender-5x, intermediate

---

## Related Tutorials
- [THIN WALL, the incredible new Principled BSDF feature in Blender 5.2](thin-wall-the-incredible-new-principled-bsdf-feature-in-blender-52.md) — the other recent Principled BSDF addition from the same OpenPBR retrofit effort; shares materials, shaders, rendering, cycles, blender-5x
- [You Should Make Glass Animations in Blender 5.1](you-should-make-glass-animations-in-blender-51.md) — the glass/refraction case dispersion most improves; shares glass, materials, shaders, rendering, cycles, blender-5x
- [Photoreal Volumetrics in Blender](photoreal-volumetrics-in-blender.md) — the other place Cycles clamping and sample counts decide whether a render converges cleanly; shares materials, shaders, rendering, cycles
- [Making my lens in Blender (Bokeh, glare, chromatic aberrations)](making-my-lens-in-blender-bokeh-glare-chromatic-aberrations.md) — approaches chromatic aberration as a measured *lens* artefact in the compositor rather than a *material* one at shading time; shares rendering, cycles, materials, shaders

> **Gap noted:** this video opens by referencing the author's previous video on
> OpenPBR `[transcript 0:00]`, which is not in this library. Ingesting it would give
> this entry its missing upstream context.
