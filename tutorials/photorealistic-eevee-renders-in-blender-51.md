---
title: Photorealistic Eevee Renders In Blender 5.1
source: YouTube
url: https://www.youtube.com/watch?v=AoGPxjgqVYE
author: Extra 3d
ingested: 2026-06-25
blender_version: "Blender 5.1.0 -- observed in frame_002, frame_003, frame_004, frame_006"
tags: [rendering, eevee, ray-tracing, lighting, light-probes, workflow, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/photorealistic-eevee-renders-in-blender-51/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Photorealistic Eevee Renders In Blender 5.1

**Source:** [YouTube](https://www.youtube.com/watch?v=AoGPxjgqVYE)
**Author:** Extra 3d
**Duration:** 14m58s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction [0:00]
**Transcript:** Let me ask you a simple question. Which one of these is rendered in EV?  Almost all of you will say that this is cycles and this one is rendered in EV, which is partially  correct. But what if I tell you that both of these are rendered in real time with EV?  As you can see this is running in EV in real time. Since Blender introduced EV, it has  always been in the shadows for not producing realistic results, until they introduced  ray tracing, which flipped the whole situation and made it possible. You might be thinking  that if ray tracing does the work, why should you watch this video? You are correct, but  this checkbox most of the time won't get you the results you are looking for. And this  video is exactly about how to achieve photorealism with EV.  In this video, we will not only go through the basics, but we will also do some practical  work.


### Overview [1:09]
**Transcript:** Here is a quick overview of the video. In the first chapter, we will go through the  basic theory of how EV works and what the workflow is going to be like. You can skip  this chapter if you want to directly start with the settings. In the second chapter,  we will start with this basic scene, which I made using these assets that I found on  CG Trader, which is also our sponsor today. CG Trader is basically an online marketplace,  where you can get high quality 3D models very easily. It has over 2 million 3D models, making  it one of the largest sources for high quality and custom 3D content. I will talk more about  it later in the video. For now, we will basically apply the concept and workflow in this chapter  and make this scene look good. In the third chapter, we will focus on light and reflection  probes, which are just a way to improve the lighting by baking the lighting data, and  the reflection probes basically improve the reflections of glossy materials. In the  fourth chapter, we will go through a complex scene in which we will improve some basic  shaders, like glass and translucent materials. And finally, in the last chapter, we will  test the workflow and re-light a complete scene. I hope you watch till the end so that you  don't miss the free gifts that you will get along the way.


### Chapter 1: Basic Concepts [2:23]
**Transcript:** So when you open Blender, the render engine is set to EV by default. Most of the time,  we switch this to Cycles, which gives accurate results because it is a path tracer that  simulates accurate lighting and reflections. Now, before I delete the cube, let's understand  how rendering works, so Cycles is basically a path tracing render engine. Let's say  a ray is generated from this camera, and it goes and intersects with a surface in its  direction. Let's call this the primary ray. Now, a secondary ray will be generated, which  will bounce off randomly until the rendering equation is solved. This allows Cycles to  achieve accurate light simulation, but it comes at a computational cost.  On the other hand, EV has no light bounces, it is just flat by default. But EV has evolved  over the last few years, and now it has ray tracing. Now, compared to path tracing, which  doesn't stop until the rendering equation is completed, ray tracing is pretty smart.  And what it does is that it directs the secondary ray to the light source, and if that ray hits  the light, this point is lit. If something blocks the shadow ray, that point is in shadow.  This allows it to be fast and get similar results, but it's still not enough. There are many  issues with this, but the major issue is that it's based on screen space method, which  basically works on the basis of what the camera sees. You can see the change when I move the camera.  But don't worry, to fix this, we are going to use light probes, which are basically cubes with  small dots in them. And these dots store the lighting data that affects the objects within these  dots. This method, combined with ray tracing, solves the issue. This is obviously just the base  of the workflow, and there is more to it when it comes to the practical stuff.


### Chapter 2: Practical Workflow with CGTrader Assets [4:11]
**Transcript:** So, for the first demonstration, I am going to go with this scene. Let me first break it down for  you. I have this basic plane with this wood texture that I got from Polyhaven, along with this HDRI.  Starting with the assets, I have added this statue that I got for free on CG Trader, and I scattered  this art studio collection, which I also found on CG Trader. Now, before we continue, let me tell you  more about today's sponsor, which is CG Trader. CG Trader is an online marketplace, where you can  find millions of high quality 3D models. It is a great place to get 3D models. You just have to  search for what you want, and the results will show up. You can filter out the format and just select  any model you want. When you open it, you will find most of the information about the model.  You can check the reviews about the creator and the model. You can look for the polycount and  geometry, and you can also ask the creator any questions before buying. Once you are done, you can  easily download it and open it in your software. The best thing is that CG Trader gives out great  discounts and offers, and for you guys, CG Trader is giving you a 10% discount for any item,  including items that are already on sale. So, what are you waiting for? Just use the code  extra 3D10, and claim the 10% discount right now. The link is in description.  Now let's get back to the video. I have also added this area light along with some volumetrics  nothing fancy. You can get the base project file for free on my Patreon to follow along.  Now before we change anything, first go into edit, preferences, go into the system tab,  and change the back end mode to vulcan. Save preferences, and it will also ask you to restart,  so restart blender as well. Once that's done, the first step of the workflow is to enable ray tracing,  and you can see it basically does a lot of the work. Now before we do the settings,  let me explain you how the world settings work. So basically, in EV, the environment doesn't work  how it works in cycles. You basically have to tell which part of the HDRI will act as light sources.  You basically control that with the threshold value. Now currently the scene has a very sharp light,  I really don't want that. I'm just going to increase the threshold to 10, which will make it softer.  You can basically test it and play with the settings until you get something you want.  Now let's talk about the settings. So first off, ray tracing does the work, but you still have to change  the settings. The first is resolution. Change this to 1x1 for full resolution. Increase the precision  value and the thickness to 1. Under the denoising tab, disable the second option, which basically ruins  the materials. After that, disable the fast GI approximation.  If you go up, you will find samples, increase those. I'm just going to go with 120 for the final render.  In the shadows tab, you can increase the shadow rays to improve the shadows. You can go with 4,  which will do the work. After that, the area light is currently also affecting both sides of the  render. To better explain this to you, let me show you this example. So this is without jittered  shadows, as you can see the mesh is barely stopping the shadow, and it's creating this weird effect.  To fix this, go into the light settings and check jittered shadows.  Decrease all three values to their minimum.  To make this work in the viewport, you have to check this box as well.  Now, since you have to do this for each light, just select all and change the setting only for one light,  while pressing the alt key, which will change for all.  This human model is also from CG Trader, make sure you use the code to get the discount,  and the link is in description. You can see it improves the shadows a lot.  Before we move on, if you scroll down and go under the film tab, you will find overscan.  Enable that, it basically renders extra, and then crops later on, and this helps a lot since  ray tracing is based on screen space method. Now let's talk about the probes. So basically,  this scene won't be affected by it that much, but still we are just going to cover the basics.  So I am just going to add a volume probe, and roughly scale it so it fits my scene.  Go into the Data tab, and first off, increase the grid resolution. I usually go with something  like 16 or maybe 20. Also increase the resolution to 120 or 80, depending on your system.  Mark the world contribution option as well, make sure it's always checked,  and once you're done with the settings, you have to now disable the objects that you don't want  to be baked, such as any animated object, so just disable that. As you can see, there are no  animated objects, or the objects that are supposed to move, so I'm just going to leave that.  But if you have to disable something, you can just uncheck the render button, and it will just  disable it. I am using this volumetrix for the scene that I am going to disable, because volumetrix  do not look good after baking. After clicking the bake button, wait a few seconds.  Once it's done, I can now switch back on the things that I disabled like the volumetrix,  and here it is. The biggest problem with EV is that it also has no ambient occlusion.  Now what is that? It's basically a shadow between the edges of any object. Let me just show you  how to get it. Go into the passes tab, and enable the ambient occlusion pass, to see the effect,  open the compositor, and create a new workspace. Connect the ambient occlusion pass into the viewer  node. Make sure to enable the viewport compositing. Now you can adjust the strength of it by adjusting  this value. A value ranging from 0.2 to 1 works perfectly. To mix this with the main render,  just add a mix colour node, and connect it with the main render, and switch the mode to multiply.  You will face two more problems. First the background will turn dark, and the depth of field  won't work correctly either. So first enable the environment pass, and connect it in the compositor  with an alpha over node. You have to enable transparent as well to make this work.  By the way, I got this idea from Pirani Arts. I hope I am pronouncing the name right. He basically  gave the idea in the video, but didn't show how to do it. But still that idea opened my mind, so  credit goes to him, link is in the description. Now to fix the depth of field problem,  just scroll down until you find the depth of field tab, and make sure to check jitter.  There won't be any change right now, but it will show after the render.


### Chapter 3: Light & Reflection Probes [11:00]
**Transcript:** Now if we apply the workflow in an indoor scene, it will work fine until you enable the background  light which will cause world bleeding. Now this issue has been an EV since it was introduced.  Blender Guru has explained this in his video, and I was like this is ugly, this is terrible.  And he has also told a method to fix this by using light probes, but the problem with that is,  it only works for simple shaped indoors, and it is also a pain to set up. So I have a better  improved method, which is to just disable the background world while baking the lights,  and once it's baked, just enable it again. So let's do this from scratch. Add a volume probe,  and make sure it covers your scene. Change the settings by increasing the resolution,  and marking the world checkbox.  Now before you bake, disable the background world, but it will make the scene dark.  To fix this, add an area light at the places like windows or doors, and set a similar color,  and set strength accordingly. This will help fake the environment light. Now it would be better  if you put these in a separate collection to keep the scene organized. Just bake the lighting now,  and once that's done, enable the background world, and also disable the area lights that we made  for the baking purpose. And that's it. Now let's talk about the reflection probes. These are pretty  simple. You just have to make sure it roughly fits the mesh, and you are done. There is really not  much about it. By the way, I got this room model for completely free on CG Trader, which is awesome.  Make sure to check out CG Trader with the link in description, and for you guys this complete  project file will be available on my Patreon for completely free, so enjoy.


### Chapter 4: Advanced Materials [12:49]
**Transcript:** Let's improve some materials. Let's start with the Translucent Shaders, so basically  thin objects get lit by the light from the backside as well. The Translucent Shader doesn't work  correctly in EV, so we have to use subsurface scattering for that. This method is from Glare  Balik Sandroff, who is a legend himself. I have linked his video in the description. Just watch  that. Nobody explains better than him. This trick works for human skin as well. Just watch his video.  About the glass shader, you just have to change one setting, which is to just enable ray trace  transmission. And that's it. Now I can talk more about the materials, but this video has already  got so long, and I have to cover other things as well. So I will make a video about it in the future.  Only if this video gets 10,000 likes, which is impossible.


### Chapter 5: Full Scene Relighting [13:37]
**Transcript:** Now we are on the final chapter, and let's review the basics.  I have this abandoned house scan that I found on CG Trader. You can grab it for a very low price  using the discount code, check the link in the description. Now I have basically applied the  workflow here. I have changed all of the main settings. I have used a volume probe without the  background light, and with an extra area light to fake the background world. I have also added  ambient occlusion. And that's it. You will get the hang of it when you try this on multiple scenes.  Now the fun part, let's add some fisheye effect in the camera. Now you can do this easily in cycles,  with the panoramic lens type, but it doesn't work with EV. Instead decrease the focal length,  and go into the compositor. Add a lens distortion node, and increase the distortion a little bit.  Check the fit box, and you will be good to go. Another thing I did was this hand held camera animation,  which is basically with the help of this add-on. I have linked it in the description. Add some  final touches in the compositing, play with the exposure, and you will be good to go. I have a  complete video about photorealism so you can watch that out.



---

## Captured Frames

- [1:40] tutorials/frames/photorealistic-eevee-renders-in-blender-51/frame_000.jpg
- [3:10] tutorials/frames/photorealistic-eevee-renders-in-blender-51/frame_001.jpg
- [6:00] tutorials/frames/photorealistic-eevee-renders-in-blender-51/frame_002.jpg
- [9:00] tutorials/frames/photorealistic-eevee-renders-in-blender-51/frame_003.jpg
- [11:40] tutorials/frames/photorealistic-eevee-renders-in-blender-51/frame_004.jpg
- [13:10] tutorials/frames/photorealistic-eevee-renders-in-blender-51/frame_005.jpg
- [14:10] tutorials/frames/photorealistic-eevee-renders-in-blender-51/frame_006.jpg

---

## Structured Notes

### Core Technique
Complete EEVEE photorealism workflow for Blender 5.1: Ray Tracing + Vulkan backend + specific ray tracing settings + Volume/Reflection probes + AO in compositor + materials fixes for glass/translucency; indoor world bleeding fix; fisheye workaround via compositor Lens Distortion.

### Summary
Extra 3d walks through making EEVEE match Cycles quality in Blender 5.1. Ray tracing alone isn't enough — specific settings must be configured. Backend: Vulkan (Preferences → System). Core RT settings: Resolution 1×1, Precision 1, Thickness 1; disable second Denoising option; disable Fast GI; raise samples to 120; shadow rays 4; Jittered Shadows per light (Alt+click to apply to all at once); Overscan ON in Film. World: raise HDRI threshold (default→10) for softer HDRI light. Volume Probe: grid resolution 16–20, resolution 80–120, World contribution ON; disable animated objects and volumetrics before baking. Indoor world bleeding fix: disable BG world → add area lights at windows → bake → re-enable world + disable fake lights. AO: enable AO pass → compositor Multiply with main render (strength 0.2–1). Background transparency fix: enable Environment pass + Alpha Over + Transparent ON. DoF jitter checkbox. Glass: enable Ray Trace Transmission in material. Translucent: use SSS instead. Fisheye in EEVEE: lower focal length + compositor Lens Distortion (Fit ON).

### Key Steps
1. **Vulkan backend:** Preferences → System → Backend Mode → Vulkan. Save + Restart.
2. **Enable ray tracing:** Render Properties → Ray Tracing → ON. **The set captures this as a genuine before/after pair**: the `Raytracing` checkbox is **unticked** at 6:00 [frame_002] and **ticked** at 11:40, with `Method` on `Screen-Trac…` [frame_004].
3. **Ray tracing quality:** Resolution 1×1; Precision 1; Thickness 1.
4. **Denoising:** Disable second option (ruins materials).
5. **Fast GI:** Disable Fast GI Approximation.
6. **Samples:** ⚠️ **"120" appears in no frame.** Render `Samples` reads **64** at 6:00 [frame_002] and **128** at 11:40 [frame_004] — so the value was raised, but to 128. Viewport `Samples` moves the other way, **16** → **0** [frame_002, frame_004], with `Temporal Reprojection` on throughout.
7. **Shadows:** Shadows panel. ⚠️ The only frame showing it reads `Rays` **1**, `Steps` **6** — **and the mouse is sitting on the `Rays` field as a horizontal drag cursor** [frame_004], i.e. captured in the instant before the change. "Rays = 4" is the target, not the state. Also visible: `Volume Shadows` unticked at `Steps` 16, shadow `Resolution` **1.000**, and Advanced → `Light Threshold` **0.010**.
    **Viewport `Jittered Shadows` is confirmed as a before/after**: unticked at 6:00 [frame_002], ticked at 11:40 [frame_004]. Per light: all three values to minimum; Alt+click to apply to all lights simultaneously *(narrated — no light data panel is in shot)*.
8. **Film Overscan:** Film tab → Overscan → ON.
9. **World threshold:** ⚠️ **What the World actually contains is a two-shader trick the entry never described** [frame_006]: Surface = **`Mix Shader`**, its `Factor` driven by **`Light Path → Is Camera Ray`**, mixing two `Background` shaders — the visible one at `Strength` **10.000** with a white `Color`. That is the "10" in this step, and it is a camera-ray split (one background for the camera, another for lighting), not an "HDRI threshold" slider.
10. **Volume probe:** Add → Light Probe → Volume. Scale to fit scene. Data tab, as configured [frame_003]: `Resolution X/Y/Z` **20 / 20 / 20**, `Bake Samples` **2048**, `Surfel Resolution` **80**, Capture `Distance` **20 m**, Contributions → **`World` ✓**. The probe block above it, never recorded: `Intensity` 1.000, `Normal Bias` **0.30**, `View Bias` 0.00, `Facing Bias` **0.50**, `Validity Threshold` **0.40**, `Dilation Threshold` **0.50**, `Radius` 1.00. The button is labelled **`Bake Light Cache`**. Disable volumetrics and animated objects, bake, then re-enable.
11. **Indoor world bleeding fix:** Before baking: disable Background World shader. Add area lights at windows (same HDRI color/warmth) in a separate collection — **the author's own collections are named `Lights For Baking` and `For Bake`**, sitting beside the normal `Lights` collection [frame_004, frame_006], which is about as direct a confirmation of this step as an outliner can give. Bake. Re-enable world + disable fake lights.
12. **Reflection probe:** Add → Light Probe → Reflection Cube. Scale to fit glossy object. Confirmed structurally: the outliner carries a **`Reflection Probes`** collection alongside a `Light Probe` entry [frame_004].
13. **AO in compositor:** Render Properties → Passes → Ambient Occlusion ON. Confirmed — the `Render Layers` node exposes `Image`, `Alpha`, **`Environment`** and **`Ambient Occlusion`** sockets, all four wired [frame_006]. The mix node is a Color `Multiply` with `Clamp Factor` **✓** and `Factor` **1.000** — the top of the recorded 0.2–1 range, not a mid value. Enable Viewport Compositing. Two further compositor nodes were never recorded: a **`Glare`** node in `Fog Glow` mode (Threshold / Smooth / Strength / Saturation / Tint / Size) and a node **Group** named `Compositor Nodes` at `Node Width` 140. 
14. **Background/DoF fixes:** Enable Environment pass → `Alpha Over` node in compositor — present, with `Factor` **1.000**, mode `Over`, `Straight Alpha` unticked [frame_006]. Enable Transparent in Render Properties. DoF: enable Jitter checkbox *(narrated)*.
15. **Glass material:** Material Properties → enable Ray Trace Transmission.
16. **Translucent material:** Use Subsurface Scattering instead of Translucent shader. ⚠️ **The frame covering this chapter is a picture-in-picture of someone else's video** — "Better(!) Eevee Subsurface Scattering Translucency Hack", paused at 0:48 / 2:05 with the YouTube player chrome visible [frame_005]. The SSS values on screen (`Random Walk`, `Weight` 1.000, `Radius` 0.800 / 0.800 / 0.100, `Scale` 2.45 m, `Anisotropy` 0.000) belong to **that** tutorial, not this one, and its Blender is a different build. Cited here only as the referenced source.
17. **Fisheye in EEVEE:** Decrease focal length. Compositor → Lens Distortion node → increase distortion → check Fit.

### Nodes / Settings
- Backend: Vulkan (Preferences → System)
- Ray Tracing: ON; Resolution 1×1; Precision 1; Thickness 1
- Denoising: second option disabled
- Fast GI: disabled
- Samples: Render **64** → **128**; Viewport **16** → **0**, Temporal Reprojection on [frame_002, frame_004]. "120" appears in no frame
- Shadows: `Rays` **1**, `Steps` **6** at capture (drag cursor on the field), Volume Shadows off / Steps 16, Resolution 1.000, Light Threshold **0.010** [frame_004]; viewport Jittered Shadows off → on [frame_002, frame_004]; Alt+click = apply to all lights *(narrated)*
- Film: Overscan ON
- World: **`Mix Shader`** with `Factor` = **`Light Path | Is Camera Ray`**, mixing two `Background` shaders, visible one at `Strength` **10.000** [frame_006]
- Volume Probe: Resolution **20/20/20**, Bake Samples **2048**, Surfel Resolution **80**, Capture Distance 20 m, `World` ✓; biases 0.30 / 0.00 / 0.50, Validity 0.40, Dilation 0.50 [frame_003]
- Collections `Lights For Baking` and `For Bake`, plus a `Reflection Probes` collection [frame_004, frame_006]
- Render Layers passes wired: `Image`, `Alpha`, `Environment`, `Ambient Occlusion`; Multiply with Clamp Factor on at `Factor` **1.000**; `Alpha Over` at Factor 1.000 / `Over` / Straight Alpha off [frame_006]
- Also in the compositor, unrecorded until now: a `Glare` node in **Fog Glow** mode, and a node Group named `Compositor Nodes` [frame_006]
- DoF: Jitter checkbox ON
- Material → Ray Trace Transmission (glass); SSS for translucent
- Lens Distortion (compositor): Fit ON for fisheye

### Difficulty
Intermediate — no modeling; pure settings configuration; covers all key EEVEE photorealism pain points

### Blender Version
**Blender 5.1.0** for the working session — status bar, four frames [frame_002, frame_003, frame_004, frame_006]. ⚠️ **Two other version strings appear in this set and belong to other footage**: `5.0.1` in the opening scene showcase [frame_001], and `4.5.2` inside a picture-in-picture of a different creator's video [frame_005]. Read the version off a frame here without checking what the frame *is*, and you get the wrong answer two times in seven.

### Tags
#rendering #eevee #ray-tracing #lighting #light-probes #workflow #intermediate

---

## Frame verification (2026-09-02)

| | |
|---|---|
| **Confirmed** | `Blender 5.1` is right for the working session — **5.1.0** in four status bars. Ray tracing, viewport Jittered Shadows, the Environment and AO passes, `Alpha Over`, the `Reflection Probes` collection and the separate bake-lights collection are all visible and match. |
| **Corrected** | the final sample count is **128**, not 120 — and the set contains its own before shot at **64** [frame_002, frame_004]. Key Step 9's "HDRI threshold: 10" describes something that is not a threshold: the World is a **`Mix Shader`** split by **`Light Path → Is Camera Ray`** between two Backgrounds, the visible one at `Strength` **10.000** [frame_006]. The AO multiply runs at `Factor` **1.000**, the top of the recorded range. |
| **Added** | the full Volume Probe configuration — Resolution 20/20/20, Bake Samples **2048**, Surfel Resolution 80, Capture Distance 20 m, and six bias/threshold fields never recorded [frame_003]; EEVEE `Light Threshold` 0.010 and the Volume Shadows/Resolution row [frame_004]; a `Glare` node in **Fog Glow** mode and a `Compositor Nodes` group [frame_006]; and the author's collection names `Lights For Baking` / `For Bake`, which confirm Key Step 11's advice in his own words [frame_004, frame_006]. |
| **Flagged as unverified** | the Vulkan backend switch, RT Resolution/Precision/Thickness, the second denoising option, Fast GI, Film Overscan, per-light Jittered Shadow values, Transparent, the DoF Jitter checkbox, Ray Trace Transmission, and the Lens Distortion fisheye step. None appear in any frame — no Preferences window, no material panel and no Film panel is ever on screen. |

⚠️ **This set is the counterexample to reading a version off any frame.**
Three different Blender versions appear across seven frames:

| frame | reads | whose Blender |
|---|---|---|
| frame_001 (3:10) | **5.0.1** | the author's, in an earlier scene-showcase segment |
| frames 002/003/004/006 | **5.1.0** | the author's working session — the correct value |
| frame_005 (13:10) | **4.5.2** | **someone else's** — a picture-in-picture of the referenced video |

`frame_005` is a YouTube player, chrome and all, paused at 0:48 / 2:05 on
"Better(!) Eevee Subsurface Scattering Translucency Hack". Its SSS numbers are
real but they document *that* tutorial. A version-region crop taken blind would
have returned 4.5.2 or 5.0.1 here — **two of seven frames give a wrong answer,
and neither looks wrong in isolation.** Check what the frame *is* before
trusting where the digits sit.

ℹ️ **`frame_000` (1:40) is a CGTrader search page** — browser, not Blender. It
grounds where the scene's assets came from and nothing else.

---

## Related Tutorials
- `photorealistic-renders-in-blender.md` — companion Cycles photorealism workflow guide
- `how-to-render-faster-in-blender-cycles.md` — Cycles optimization counterpart
- `fundamentals-of-lighting-in-blender.md` — lighting theory foundation
- `real-time-caustics-in-blender-51.md` — EEVEE caustics companion (5.1)
