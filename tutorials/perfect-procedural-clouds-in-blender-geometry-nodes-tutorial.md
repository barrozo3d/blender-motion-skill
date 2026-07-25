---
title: Perfect Procedural Clouds in Blender | Geometry Nodes Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=6_vwVjODhog
author: adrien_ltn
ingested: 2026-07-25
blender_version: "Blender 4.x"
tags: [geometry-nodes, volume, procedural, cycles, rendering, materials, lighting, hdri, compositing, organic, intermediate, blender-4x]
extraction_status: complete
frames_dir: tutorials/frames/perfect-procedural-clouds-in-blender-geometry-nodes-tutorial/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Perfect Procedural Clouds in Blender | Geometry Nodes Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=6_vwVjODhog)
**Author:** adrien_ltn
**Duration:** 18m12s | 16 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey, so I recently made this short animation and in the process had to create dozens of
[0:13] photo real clouds from scratch using geometry nodes in Blender.
[0:17] So I thought in this video I'd share the whole process of creation from the geometry
[0:22] node system to how to correctly shade, render and comp clouds using Cycles.
[0:27] Now if you've ever tried playing around with clouds in Blender before, you probably ran
[0:32] into VDB files.
[0:34] These are clouds made in specialized softwares like Houdini, Embergen, PlanetSide or other
[0:40] software and then exported as .vdbs.
[0:44] They're a very solid option but don't really give you any flexibility.
[0:48] First of all you rely on other software or paid packs of VDBs.
[0:52] You can't really tweak them, can't find any stylized cloud.
[0:56] They're rarely ever animated and can also get very heavy.
[1:01] Now you can find a lot of tutorials in Blender but the techniques used often times fake the
[1:07] cloud using 2D cards, noise displacement or rely on a lot of manual modeling.
[1:13] But I needed the real deal, a fully procedural pipeline with artistic control to make any
[1:19] type of cloud I needed.
[1:21] I took a look at the underlying structure of Houdini's cloud generation pipeline and
[1:25] knew there had to be a way to make something similar in geometry nodes.


### What's Included [1:30]
**Transcript (timestamped):**
[1:30] So let me introduce Cloud Creator, a fully customizable procedural pipeline giving you
[1:35] a ton of flexibility with iterative cloud generation.
[1:38] Don't worry you can find both a free and a paid version if you click the link in the
[1:42] description.
[1:43] The free version contains the converter which allows you to take any mesh and transform
[1:48] it into a cloud but with a few differences that we'll explore.
[1:52] This Cloud Creator Pro comes with extra tools for cloud shaping, animation, shading and
[1:57] adds extra cloud presets.
[1:59] But we'll anyway see the differences as we go.


### Manual Modelling [2:02]
**Transcript (timestamped):**
[2:02] Now in Blender to make a good cloud you need nice shapes.
[2:05] This step is pretty easy, just scatter some spheres around to make a rough shape, you
[2:10] don't need to be too detailed as long as it's vaguely cloud-like.
[2:13] The way Cloud Creator works is it takes any geometry you have and procedurally converts
[2:18] them into cloud using this converter node.
[2:21] But if you don't want to model the cloud by hand or want a more procedural approach
[2:25] the Pro version uses this fully procedural generator node making the whole process a
[2:30] streamlined two step workflow.
[2:33] Cloud Creator Pro is fully compatible with the Asset Library so you can quickly drag


### Asset Library [2:35]
**Transcript (timestamped):**
[2:37] and drop the modifiers in your file when you save the Cloud Creator Pro file in your Asset
[2:42] Library directory which you can find in your Blender settings but for this video I'll
[2:47] directly open the file that comes with Cloud Creator so that way you can follow along with
[2:52] the free version in which you'll see a template ready to render.
[2:56] Now let's take a look at the Generator node.
[2:59] If you've ever tried making clouds in Houdini you'll find the settings to be very similar


### Procedural Cloud Generator [3:00]
**Transcript (timestamped):**
[3:04] as this generator is based on that same process.
[3:07] So if you select the cloud and go to the Geometry Nodes panel you'll see three modifiers.
[3:13] Let's disable all of them except the first one for now and have a look at the Generator
[3:18] which will create for us the spheres that make up the cloud.
[3:21] The first settings are relatively basic seed, length, width and overall scale which allow
[3:27] you to define the dimension of your cloud.
[3:29] Then you'll find more intricate settings like point separation which is like your sphere
[3:34] density distortion that distorts the base shape like so from the top down view and this
[3:40] flatten bottom slider.
[3:42] You'll notice there's no height setting and that's because vertical growth in a cloud
[3:46] is quite organic so to recreate that effect you'll need this displacement tab which adds
[3:52] little spheres using this iteration value and displaces them upwards with the spread
[3:57] option dictating how much it should displace them in all directions instead.
[4:02] There's also this cleanup factor which removes any stray spheres that will be far from the
[4:07] rest of the group.
[4:08] So when you put it all the way to zero it will remove everything.
[4:11] The second tab is this children tab which adds other smaller offsprings to your final
[4:17] cloud giving it more details.
[4:19] You can set the density of spheres here and adjust their scale using the scale multiplier
[4:24] and repeat the operations using this value although twice is usually more than enough.
[4:30] Now the very first setting actually allows you to pick from four different cloud presets
[4:35] for additional species of cloud.
[4:38] It's also the same setting as the cloudshade generator which allows you to draw the exact
[4:43] cloud you want so very useful for specific shapes and trails of clouds.


### Generate from Curves [4:47]
**Transcript (timestamped):**
[4:48] It's got the same settings as the cloudshade generator and also includes all the types
[4:52] of presets.
[4:53] Now whether you model the cloud or are using the generator, you can also use the cloud
[4:58] setting to create a cloud shape.
[5:00] You can also use the cloud setting to create a cloud shape.
[5:04] Now whether you model the cloud or are using the generator it's not looking too fluffy


### Converting into Volume [5:05]
**Transcript (timestamped):**
[5:09] at the moment and that's when the main cloud creator node comes along and saves the day
[5:14] the converter.
[5:16] The converter takes any geometry you have and converts it into a cloud.
[5:19] So if you're not using the generator or have a custom shape like this Suzanne monkey head
[5:24] here you can put it on and it will work like a charm.
[5:28] This node transforms your geometry into a nice volume by scattering tons of particles around
[5:34] which you can visualize better by turning viewport override on or in your rendered view
[5:39] by looking at the volume direct path.
[5:42] The first setting is your resolution which is basically your foxhole size, think of it
[5:46] as a pixel size but for volumes, so the lower the more detailed your cloud will be.
[5:52] And this is a good moment to save your files as low values can quickly crash your machine.
[5:59] With this modifier I generally recommend typing in your values rather than using the
[6:03] sliders to avoid any unwanted crashes.
[6:07] The particle size is similar to the resolution but will need individual adjustment for your
[6:12] preferred result depending on the resolution.
[6:15] Viewport override will display the points in a more readable way making it pretty handy
[6:20] at this stage.
[6:21] And so as to not kill your PC I also made this render subdivision parameter which allows
[6:27] you to keep more details at render time but please keep it low at 2 or 3 maximum as the
[6:33] number of particles will very quickly get out of control.
[6:37] Now once again we get a few tabs to help us in our journey, the first one being the noise
[6:42] serving as a nice organic deformation and with plenty of settings for you to adjust
[6:47] similarly to your usual noise you might need to play around a fair bit with these settings
[6:52] so I'd recommend lowering your resolution for the moment to something a bit less intense
[6:57] for your cloud fine-tuning your settings in the meantime.
[7:00] The flatten tab is fairly straightforward and similar to the flatten bottom setting
[7:05] from the previous modifier with an intensity slider and a height parameter 0 being the
[7:10] bottom and 1 being the top.
[7:12] And there we go, your cloud is basically ready to go.
[7:15] Now the pro version includes a few more options that we should go through though with the


### Extra Options [7:16]
**Transcript (timestamped):**
[7:19] first one being an animation speed parameter that helps to bring a bit of life to your cloud
[7:24] like so.
[7:25] It's very subtle but it really elevates the final result.
[7:28] You'll also notice three extra tabs in the pro version with wind, vortex and camera
[7:33] culling.
[7:34] The wind tab allows you to create these trails that you would find in real life or the natural
[7:39] spread that happens at the base of clouds.
[7:42] The intensity is your general multiplier while scale and detail adjust the noise pattern
[7:47] applied to that effect.
[7:49] The next settings are a bit more specific with direction you can think of these three
[7:54] inputs as x, y and z directionality so this will point towards positive x whereas that
[8:02] will point to negative y.
[8:04] You can even make the wind go in the z axis if you want and the omnidirectional tickbox
[8:11] will allow you to make it go in both sides so not just positive or negative.
[8:17] You can mix values to make it go diagonal so what I usually do is put it to 1, 1 and 0
[8:24] and tick omnidirectional on so the wind helps the cloud spread nicely in all directions
[8:30] while staying flat.
[8:32] Then you have this z padding slider which adjusts the height at which this wind effect
[8:37] takes place.
[8:38] And finally there's this flip z tickbox for the wind which will flip the wind so that
[8:44] it happens only at the top of the cloud not at the bottom.
[8:48] Like you can see in real life on these cumulonimbus clouds the vortex tab is the last shaping
[8:54] option that comes with the pro version which can be pretty useful for making stuff like
[8:59] in this image or as a cool way to add some directionality in your clouds like you might
[9:04] see in these anime cloud scapes.
[9:07] To do that add an empty, set a radius for the effect, an intensity to define the amount
[9:13] of spin and a push for an extra clean result.
[9:18] And voila!
[9:19] Now that you've got a good looking cloud your computer is probably crying and that's


### Optimisation [9:20]
**Transcript (timestamped):**
[9:23] because depending on your voxel size it can be a lot to handle especially for close ups
[9:29] so to optimize the scene and the clouds further the last tab is a camera calling optimization
[9:35] option.
[9:36] So simply input your resolution so in my case 1080 by 1920 and your focal length which you
[9:44] can find in your camera tab and now you can remove unwarranted particles with this padding
[9:49] slider here.
[9:51] Once you're happy with your cloud you have the option to bake the cloud as a still or
[9:55] as an animation.
[9:57] This can be very useful to avoid waiting for the geometry nodes calculation but the render
[10:02] subdivision option will not work with the bake so make sure you're happy with what you
[10:07] see in the viewport.
[10:08] Now to bake the cloud you click on the converter modifier, go into your geometry nodes tab and
[10:14] have a look at the very last node, set it to animation or still then press on bake and
[10:20] your result is there.
[10:22] So the converter really is the central node to this tool which is why I included it in
[10:26] the free version and that's how I also made the other effects in the video.


### Other Effects [10:30]
**Transcript (timestamped):**
[10:30] The trails coming from the plane were made by scattering spheres in geometry nodes using
[10:35] a vertex mask and a simulation zone and then converting them with cloud creator.
[10:41] As for the condensation effect it was made following the basic principles of this aerodynamic
[10:45] tutorial by CG Matter and then converting them to spheres then into a volume using cloud
[10:51] creator with a few custom attributes for density and other effects.
[10:55] My very last tip on the modifier side of things is if you used an empty volume before adding


### Volume Displace [11:00]
**Transcript (timestamped):**
[11:01] the shape generator as the base for your cloud you'll find this volume displace modifier
[11:07] which can help you add some final distortion to your cloud.
[11:10] You can create a texture by clicking on new and clicking here.
[11:14] You can adjust the type of noise, the shape and the intensity but make sure that the
[11:19] color is set to color and not grayscale as the grayscale texture leads to displacement
[11:25] only in a single axis whereas color will displace the cloud in all direction.
[11:30] So now that we have our cloud it's time to make it look good.
[11:34] If you haven't already switched to cycles you can stick to EV and get very fast renders


### Rendering [11:35]
**Transcript (timestamped):**
[11:39] but my goal is to make it look as good as possible.
[11:43] In EV you can enable volumetric shadows and get a result like so but I would argue that
[11:50] cycles result looks much more realistic.
[11:53] However if you've ever tried to render clouds in cycles before you might have encountered
[11:58] this teeny issue of insane render times which might not be an issue to you if you're just
[12:04] rendering a still frame but for animation your PC will literally catch on fire.
[12:11] So what you can do to fight back is to go in this tab and reduce this max step settings
[12:18] to anywhere between 10 and 25.
[12:21] Basically the smaller the number the faster but you might end up with these blocky artifacts
[12:27] if you go too low so just be careful about that.
[12:30] Some people also change the step size but that has created more issues than anything
[12:36] for me so I wouldn't recommend touching that.
[12:38] If you can afford it I would also up the volume light pass a bit, the higher the nicer your
[12:44] volumes but the slower the render time.
[12:47] Now to make the cloud look realistic I would say it's about 90% in the lighting and only


### Lighting [12:51]
**Transcript (timestamped):**
[12:53] 10% in the shader and for the lighting HDRIs are your best friend.
[12:58] These files will provide you a solid base lighting that will do most of the heavy lifting for
[13:03] you with all the realistic details of a sky environment baked in them.
[13:08] Simply grab one from a website like HDRiheaven and go to the world tab in your shader editor
[13:15] and plug it into an environment texture.
[13:18] The default cloud creator file will already have 3 HDRIs I downloaded from HDRiheaven
[13:24] for you to play around with, a daytime, an overcast and a sunset one.
[13:29] Shader wise I've created this fast material for cloud creator which looks very similar


### Materials [13:30]
**Transcript (timestamped):**
[13:34] to the default volume scatter shader but with a few tweaks to make it even better.
[13:40] It's very similar to what you may find in a lot of YouTube tutorial however cloud creator
[13:44] pro comes with the fast material and another fancy material which comes with a ton of extra
[13:51] setting.
[13:52] It's got a top and a bottom colour with a z offset gradient handy to make your cloud
[13:57] look stormy or reflecting the light of whatever is underneath it as well as a billowy factor
[14:03] that adds this like puffiness to your cloud and noise which you can fine tune with the
[14:08] different scale settings in the billowy parameters section.
[14:12] There's also this shadow setting which allows you to control separately the amount of shadows
[14:18] inside of the cloud almost like an ambient occlusion.
[14:21] Then you'll see this optional wind dispersion tab which helps control the density of the
[14:26] volume if you've enabled the wind spread in the geometry nodes.
[14:30] You want to try to match this with the wind setting and for that you can use the z padding
[14:34] to change the height, the blur to diffuse it and the intensity to make it less dense.
[14:39] And like in the geometry nodes you can also flip the effect on the z.
[14:43] And finally there's this halation tab that helps mimic this fringing rainbow like effect
[14:49] you get sometimes around the very edges of clouds.
[14:52] The coverage dictates how much it wraps around the cloud and the mix is like an intensity
[14:58] slider whilst the colour offset allows you to shift the hue of the fringing effect.
[15:03] Pushing the coverage to 1 is very much extreme but putting it between 0.3 and 0.6 gives you
[15:10] a unique style that looks very pleasing.
[15:13] And there you go you've got a fluffy cloud although there is a final step compositing.


### Compositing [15:18]
**Transcript (timestamped):**
[15:18] Now you can choose whatever compositing software you want even blenders built in compositors
[15:23] and you want to make sure that when rendering you enable the volume direct and indirect passes
[15:29] as these can be life saving especially for adding more detail to the final image.
[15:35] I'm not going to be going too much into detail over the comp process as it would be a bit
[15:41] over this video's reach but generally speaking if you're doing your comp in an external
[15:45] software like muke or da Vinci Resolve I would recommend rendering an exos in this format.
[15:52] You can check out this video that talks about the different types of file formats and why
[15:57] this format specifically might be the best, the link for it will be in the description
[16:02] and playing around with the overall softness of the image to get a natural look.
[16:06] You can see that adding volume direct and indirect passes really brings a lot of detail
[16:11] to your final image.
[16:12] Also in order to drastically save on time when rendering animations specifically you
[16:18] can render the clouds on their own layers separately, that way you can render only every
[16:24] other frame or even if the motion is subtle enough every 3, 5 or even 10 frames if it's
[16:30] a still shot.
[16:31] Using the step setting under the frame range and then creating in between frames in software
[16:37] like flow frames will fill the gaps and make it all look smooth and that's what I did for
[16:42] many shots like this one only rendering every 10 frames in this case or every 2 frames in
[16:48] this shot because the camera motion was quite intense.
[16:52] So just to recap, with Cloud Creator Pro you'll find the 3 modifiers compatible with the asset


### Outro [16:55]
**Transcript (timestamped):**
[16:57] library, with the extra presets, animation, shaping and wind features in both of the shaders
[17:03] as well as a template file with 3 realistic clouds and 4 stylized clouds as well as 2
[17:09] separate files for you to explore and see how the tool works in different environments.
[17:14] Cloud Creator Lite is completely and totally free and still comes with the standard converter
[17:20] So feel free to download either versions on Gumroad following the link in the description,
[17:24] I'll keep updating the tool with the feedback I receive.
[17:27] Feel free to send me any of your creations as always and let me know if you have any issues
[17:32] either in the comment section or on my Instagram, you can consider subscribing if you like what I
[17:38] do and I just wanted to thank everybody for the insane feedback on my previous felt tool.
[17:43] I've released a small Blender 4.5 update for the Pro version, honestly the stuff you people
[17:49] have created with felt maker is insane. I'm super happy to see many people doing such cool stuff
[17:55] with it, I'm super honored to be here, these videos take an insane amount of time to make,
[18:00] so I need to figure out a way to make them a bit faster, maybe not always do a tool or something,
[18:06] anyways that's all I have for you, thanks a lot, bye!



---

## Captured Frames

- [3:40] tutorials/frames/perfect-procedural-clouds-in-blender-geometry-nodes-tutorial/frame_000.jpg
- [4:38] tutorials/frames/perfect-procedural-clouds-in-blender-geometry-nodes-tutorial/frame_001.jpg
- [5:40] tutorials/frames/perfect-procedural-clouds-in-blender-geometry-nodes-tutorial/frame_002.jpg
- [8:20] tutorials/frames/perfect-procedural-clouds-in-blender-geometry-nodes-tutorial/frame_003.jpg
- [9:12] tutorials/frames/perfect-procedural-clouds-in-blender-geometry-nodes-tutorial/frame_004.jpg
- [10:14] tutorials/frames/perfect-procedural-clouds-in-blender-geometry-nodes-tutorial/frame_005.jpg
- [12:18] tutorials/frames/perfect-procedural-clouds-in-blender-geometry-nodes-tutorial/frame_006.jpg
- [14:05] tutorials/frames/perfect-procedural-clouds-in-blender-geometry-nodes-tutorial/frame_007.jpg

---

## Structured Notes

### Core Technique
Fully procedural photoreal clouds in Geometry Nodes (no VDBs): a Houdini-style sphere-scatter → points → volume pipeline packaged as the "Cloud Creator" tool (free Converter + Pro Generator/shaders), rendered in Cycles with volume-step and render-pass optimizations.

### Summary
Adrien Lambert (adrien_ltn) walks through his Cloud Creator geometry-nodes tool, built by replicating Houdini's cloud generation pipeline in Blender: a Generator modifier scatters/displaces spheres into cloud silhouettes (4 cloud-species presets, curve-drawn shapes supported), a Converter modifier turns *any* geometry into a particle-scattered volume with noise/flatten/wind/vortex shaping, and dedicated volume shaders add billowy detail, gradient colors, and edge halation. The back half covers making Cycles volumes render fast (Max Steps 10–25, volume light bounces), HDRI-first lighting, volume direct/indirect passes in comp, and rendering clouds on separate layers at frame steps (every 2–10 frames) interpolated with Flowframes.

### Key Steps
1. **Build the base shape** — scatter spheres into a rough cloud silhouette by hand, or (Pro) use the `AL_CloudCreator_Generator` modifier: pick a cloud species preset, set `Seed` / `Length` / `Width` / `Scale`, then tune `Point Separation` (sphere density), `Distortion` (top-down shape warp), and `Flatten Bottom`. There is deliberately no height setting — vertical growth comes from the Displacement tab (`Iterations` adds small spheres displaced upward, `Spread` displaces omnidirectionally, `Cleanup` at 0 removes everything, 1 keeps strays). A `Children` tab adds smaller offspring spheres (`Density`, `Scale Mult`, repeat ≤2).
2. **Curve-drawn clouds** — the cloud-shape/curve generator variant shares the same settings and presets and lets you draw exact shapes and trails.
3. **Convert to volume** — enable the `AL_CloudCreator_Converter` modifier (free version): scatters particles through any input geometry (works on a Suzanne). `Resolution` = voxel size (lower = more detail — **type values instead of dragging sliders; low values crash machines; save first**), `Particle Size` adjusted per resolution, `Viewport Override` for readable point display, `Render Subd` keeps render-time detail (keep at 2–3 max).
4. **Shape the volume** — `Noise` tab for organic deformation (lower resolution while tuning), `Flatten` tab (intensity + height, 0=bottom 1=top). Pro adds: animation speed for subtle life; `Wind` tab (Intensity ~20, Scale, Detail, Direction as X/Y/Z weights — use 1,1,0 + `Omnidirectional` for flat all-direction spread; `ZPadding` sets effect height; `Flip Z` for top-only trails like cumulonimbus); `Vortex` tab driven by an Empty (`CTRL: Empty`, `Radius` 2.0, `Intensity` 3.0, `Push` 0.5) for anime-style swirl.
5. **Optimize** — `Camera Culling` tab: input render resolution (e.g. 1080×1920) + camera focal length, then cull off-screen particles with the padding slider. Bake as Still or Animation via the last node in the converter's node tree (bake ignores `Render Subd` — match viewport first).
6. **Extra distortion** — if the base was an empty volume, a `Volume Displace` modifier sits in the stack; create a new texture and set it to **Color, not grayscale** (grayscale displaces on one axis only).
7. **Render in Cycles** — EEVEE + volumetric shadows works, but Cycles is more realistic. Fix render times: Render Properties → Volumes → `Max Steps` between **10 and 25** (too low = blocky artifacts); leave `Step Rate` alone; raise volume light bounces if affordable.
8. **Light with HDRIs** — "90% lighting, 10% shader." World shader → `Environment Texture` with an HDRI (Poly Haven); template ships with daytime/overcast/sunset HDRIs.
9. **Shade** — Fast material ≈ improved `Volume Scatter`; Pro "Fancy" material adds `Top`/`Bottom` colors with `Z Offset` gradient, `Billowy Factor` (puffiness noise with its own scale settings), `Shadows` (internal AO-like control), `Wind Dispertion` (match GN wind: `Zpadding`, `ZBlur`, `Intensity`, `FlipZ`), and `Halation` (edge rainbow fringing — `Coverage` 0.3–0.6 sweet spot, `Mix`, `Color Offset`).
10. **Composite** — enable **Volume Direct + Volume Indirect** passes; render EXRs for Nuke/Resolve; render clouds on their own layer at a frame `Step` (every 2–10 frames depending on motion) and interpolate with Flowframes to save massive render time.

### Nodes / Settings
- `AL_CloudCreator_Generator` (frame [3:40]): Cloud Species `Fractus` (dropdown also `Humilis`, `Mediocris`, `Congestus` — frame [4:38]); Length 1.0, Width 0.25, Point Separation 0.1, Distortion 1.0, Flatten Bottom 0; Displacement: Displacement 2.0, Spread 0.3, Cleanup 1.0; Children: Density 10.0, Scale Mult 0.7.
- `AL_CloudCreator_Converter` (frames [5:40], [8:20]): Resolution 0.1 m, Particle Size 0.5, Render Subd 1; tabs Noise / Flatten / Wind / Vortex / Camera Culling / Manage. Wind: Intensity 20, Direction (1,1,0), Omnidirectional ✓, ZPadding 0.1.
- Vortex (frame [9:12]): CTRL Empty.001, Intensity 3.0, Radius 2.0, Push 0.5.
- Bake: converter node tree → last node → Still/Animation → Bake (frame [10:14]).
- Cycles: Render Properties → Volumes → Max Steps 10–25 (frame [12:18]); Step Rate Render 1.0 untouched; GPU Compute.
- `CloudCreator_Fancy_Mtl` (frame [14:05]): Density 0.6, Z Offset 0.35, Billowy Factor 0.6, Shadows 0.95; Wind Dispertion: Zpadding 8.458, ZBlur 2.5, Intensity 0.005, FlipZ ✓; Halation: Mix 0.285, Color Offset 0.653.
- Volume Displace modifier: texture color mode = Color (not grayscale).
- Render passes: Volume Direct + Volume Indirect; EXR output for external comp.
- Frame-step trick: Output → Frame Range `Step` 2–10 + Flowframes interpolation.

### Difficulty
Intermediate

### Blender Version
Blender 4.x (creator mentions a Blender 4.5 update for the Pro tools)

### Tags
geometry-nodes, volume, procedural, cycles, rendering, materials, lighting, hdri, compositing, organic, intermediate, blender-4x

---

## Related Tutorials
- `tutorials/how-i-made-realistic-storm-clouds-in-blender.md` — the DIY version of this pipeline (mesh→volume→points→noise→volume cycling, HDRI lighting, god rays); shares geometry-nodes, volume, cycles, hdri, organic.
- `tutorials/3-easy-lighting-setups-blender-tutorial.md` — HDRI + volume scatter lighting recipes that pair with the "90% lighting" advice here; shares lighting, hdri, volume, cycles.
- `tutorials/a-full-blender-compositor-course.md` — covers the volume direct/indirect render-pass reconstruction workflow this tutorial relies on in comp; shares compositing, rendering, lighting.
- `tutorials/3d-smoke-blender-geometry-nodes.md` — geometry-nodes volume grid simulation for animated volumetrics; shares geometry-nodes, volume.
