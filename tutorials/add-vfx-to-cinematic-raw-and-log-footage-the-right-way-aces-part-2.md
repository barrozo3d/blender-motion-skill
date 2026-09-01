---
title: Add VFX to Cinematic RAW and LOG Footage (the right way) | ACES Part 2
source: YouTube
url: https://www.youtube.com/watch?v=LssHxDCM7H4
author: InLightVFX
ingested: 2026-06-25
blender_version: "Blender 2.81 -- observed in frame_002"
tags: [color-management, aces, vfx, compositing, rendering, davinci-resolve, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Add VFX to Cinematic RAW and LOG Footage (the right way) | ACES Part 2

**Source:** [YouTube](https://www.youtube.com/watch?v=LssHxDCM7H4)
**Author:** InLightVFX
**Duration:** 12m17s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


### <Untitled Chapter 1> [0:00]
**Transcript:** Aces is a powerful free color management pipeline that makes adding VFX to raw and log footage  super easy for artists like you and me.  In the previous video we learned about color gamut and gamma.  We'll be applying these concepts in this video as we dive into the Aces workflow in  DaVinci Resolve and Blender.  So join me and let's continue.  So you can follow along, I've put together an Aces Kickstart Kit on Gumroad.  This includes this clip of raw footage, this 360 degree HDRI of our scene, and the Blender  file for this shot.  The kit starts at $2, but you can pay more if you're feeling generous.  Your purchase goes a long way in supporting the careful planning and quality that I try  to bring to every tutorial.  Your support is needed and of course very appreciated.  Okay, first off we'll get all the software setup properly.


### SOFTWARE SETUP [0:49]
**Transcript:** DaVinci Resolve is free, so download it.  Next you'll need to setup Aces in Blender.  For that I'm going to direct you to my friend Mario Costa Deis as he has a great video explaining  how to do this.  It's pretty simple and with that we're ready to roll.  Inside Resolve we'll create a new project, we'll head over to the Media tab and import  our raw footage.  Let's go to the Edit tab and drag this clip into the timeline.  To get rid of these small black bars we'll go into the project settings, image scaling  and click Scale Full Frame with Crop.  We'll quickly switch to our master settings and make sure our resolution is set to 4K  if you'd like to work in 4K.  Then we'll head to the Color Management tab.  Here we'll change our project Color Workspace to Aces CC.  Once we hit Save we'll see that our footage looks different.  This is because we've entered the Aces workspace.  Don't worry about the picture looking bad.  The first step in the Aces workflow is to transform the color gamut of our footage into  the Aces 2065 color gamut.  We also have to transform the gamma of our footage into the Aces 2065 linear gamma.  Aces makes this conversion simple with what is called an input device transform.  We'll call it an IDT for short.  As part of Aces there are tons of different IDTs to select from.  Most of these IDTs are made for a specific camera and color profile.  Per scene-referred footage that is raw and log footage, there's often a custom IDT you  can pick.  But with display-referred footage there are fewer custom IDTs and rather some general  ones that are less accurate.  Aces because display-referred formats get rid of a lot of light information from the  original scene, making the conversion into Aces less viable.  With most raw footage, Aces automatically converts the raw data into the Aces 20651 color gamut  and linear gamma.  For log footage, we need to manually select an IDT.  With this log clip here, I can either assign an IDT for the whole project in the Color  Management tab or I can right-click each clip and select the IDT this way.  The IDT is converting the color space of our log footage, Adobe RGB, to the Aces 20651  color space.  And the IDT is also converting the log gamma of our footage to be linear.  The IDT is kind of like the great neutralizer of all different footage types.  In theory, if we shoot footage of a scene on multiple different cameras with different  color profiles, raw, log, and otherwise, the IDT should make these all look exactly the  same.  I'm assuming that we have the same white balance and exposure for all cameras.  Pretty cool, huh?  Okay, back to resolve.  Right now, everything still looks bad.  So let's go into the Color Management again and we'll see this setting called Output Device  Transform.  Let's choose SRGB for now and we'll hit Save.  Now our footage looks good or normal.  Essentially, the Output Device Transform or ODT provides a way to convert from the huge  color gamut and gamma of Aces 2065 to the color gamut and gamma of whatever display device  we want to show or preview our work on.  We're choosing SRGB since most computer screens use the SRGB color space and associated display  gamma.  To summarize, the Aces IDT and ODT help us easily enter and exit the Aces workflow.  Now we can head to the color tab and at this point we can do any needed color correction,  but be very careful.  Most color operations will destroy our linear light information.  At this stage, we just want the white balance and exposure to look correct.  So changes to the color temperature, this exposure slider, the offset wheel and the gain  wheel are all safe.  Avoid any other changes.  I left the color for this clip untouched and with that, we're ready to export our footage,  but before we do so, we need to disable the ODT.  This will ensure that we're exporting our footage in the Aces 2065 color space and  not SRGB.  Again, don't worry about the footage looking bad.  We'll go into Resolves, Export tab and make sure that the in and out points are set  to our desired clip, then we'll select EXR for the format in RGB half for the codec.  We use EXR as while working in Aces since this is the only file type that can store all  the information for the Aces color space.  This does result in larger file sizes, one downside of this workflow.  So let's hit add to render hue and start render.  If you want, you can set the ODT to SRGB and create an H.264 clip that you can use for  camera tracking.  For this shot, since it's not moving, I just used the free program F Spy to line up  my camera's perspective and then I brought that camera into Blender.  Now we're ready to jump into Blender.  If you set up your workspace correctly following Mario's tutorial, you should see Aces listed  as the display device in the color management tab.  Make sure your view transform is set to SRGB and your sequencer to Aces CG.  Aces CG is a linear color space with a slightly smaller gamut than Aces 2065 and it's used  for CG rendering.  We have our camera lined up here and in the camera tab will import the EXR sequence we  exported from resolve.  This color space setting we can think of as the IDT and we'll set it to Aces 20651 since  this is the color space we exported from resolve.  Now the footage and Blender should look similar to how it did in resolve with the SRGB ODT  selected.  For me, it's not a perfect match but you'll see in the end it winds up matching.  Let's now add some objects.  For the scene geometry, all we need is a plane for the floor.  We'll give it a material to very roughly match the woods, roughness and color.  Then I also added a monkey object and these two balls.  Obviously you can probably add something more exciting.  For accurate lighting and reflections, I created this 360 degree HDRi.  We'll bring it in by going to the shader editor, selecting the world shader and adding  an environment input and selecting the HDR file.  There is one important thing that's different at this point with Aces.  Any outside images we use from say an HDRi to an image texture will need to be converted  into the Aces color space in order to look correct.  This again is done by using the IDT which can be selected using this color space option  on the node.  I won't go into full details as Mario Cossadez has another awesome video dedicated to this  topic which I'll link in the description.  I know the color space my 360 camera uses is SRGB.  And all HDRi's have a linear scene-referred gamma.  So I click this color space dropdown and I'll look for the utility linear SRGB input transform.  You may need to zoom out the node graph and go back into the menu for it to show up.  Hopefully you can find it it's probably pretty small.  Now we need to rotate our HDRi to be aligned properly.  So I'll click this image node and hit CTRL-T to create these mapping nodes.  Go to the render properties and under film we'll disable transparent.  If we enter the rendered view we can now see the HDRi and I can change this Z value  to rotate it into correct alignment.


### RENDER SETUP [8:06]
**Transcript:** Now let's create some different collections to organize the objects in our scene.  We'll have a collection for our camera, another collection for our floor, and one for  any added objects.  Finally for our floor we'll go into the object tab and set it to be a shadow catcher.  We'll now set up some render layers so we can render the objects separately from their  shadows.  We'll name this current layer main objects.  Let's set the floor collection to indirect only.  You can see this makes it so that our floor shows only indirectly in the main objects.  Then we'll create another render layer naming it shadows.  We'll set the main objects collection to indirect only so we only see the shadows.  Once we have our render layer set up we'll make sure our background is set to transparent  and set the output type to open EXR multi-layer and we'll hit render animation.  For compositing we'll create a separate scene and go into the compositing tab make sure  use nodes and backdrop are enabled and make sure you have a viewer node and composite  node to start out.  Next we'll bring in our background footage which is the EXR sequence from resolve.  Remember to set the color space to ACES 20651.  Then we'll bring in our CG render layers.  For our CG elements we'll set the color space to ACES CG since we used ACES CG for rendering.  Let's quickly make sure the scene is set to the correct 4K resolution.  We'll add the shadows by selecting the shadow view layer, adding an alpha over node and  putting our background footage in the top slot and shadows in the bottom.  Then we'll do the same thing for our main objects by duplicating this render layer node, selecting  the main object layer and adding an alpha over node with our composite in top and objects  in the bottom.  Make sure the final composite goes into the composite node and there we go.  Now to export this we need to create a camera in this scene and set the renderer to EV  with one sample.  This is just a weird workaround that allows us to render just this composite graph.  Set an output type of open EXR and we'll hit render animation.  Back in resolve we'll import this final EXR sequence.  We'll right click it and set an IDT of ACES CG.  Now we can enable the SRGB ODT to preview our final composite.  If we compare this to our original footage you should see that the colors are the same,  just the VFX is added of course.  From here you can use resolve's powerful color grading tools.  Since we only used EXR files for this workflow we retain all the light information from the  original raw footage.  So if I bring down my gain slider here you'll see I still have all that light information  outside the window and you can also see the incredible dynamic range in the highlight  of our mirror ball.  If I had used PNG instead of EXR these highlights would be clipped in the detail lost and in  this robot clip for example you can see just how much sky detail I can bring in with  some adjustments.  Now when you're done with coloring you're ready for a final export.  We'll make sure the ODT is set for the correct display device which will most often be  SRGB for computer screens.  But you can just as easily export for a movie theater projector by selecting P3 DCI.  Pretty cool.  We'll create an H.264 file for our final render.  Get ad render queue and render that sucker out and there you go you have gone through  the complete ACES workflow.  Pat yourself on the back great work.  If this tutorial was of some value to you go over and grab that ACES Kickstart kit maybe  think of it as buying the cup of coffee so that we can continue to make cool stuff like  this together.  Thank you again to Mario Cossadez and Daniel Bielka for sharing their wealth of knowledge  on this workflow so that I can get it correct for you all.  And thank you for watching.  Seriously, I'm glad to have you here and I'll see you in the next video.


### Proverbs 16:18 [12:15]


---

## Captured Frames

- [1:40] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_000.jpg
- [3:30] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_001.jpg
- [5:30] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_002.jpg
- [7:00] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_003.jpg
- [9:00] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_004.jpg
- [10:30] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_005.jpg

---

## Structured Notes

### Core Technique
Full ACES VFX compositing pipeline: export LOG/RAW footage from DaVinci Resolve as EXR (ACES 2065-1 linear, ODT disabled) → import into Blender with ACES config → render CG objects over real footage with a shadow catcher → composite in Blender → export EXR → back to Resolve for final grade + H.264 output.

### Summary
Part 2 of InLightVFX's ACES series. Practical walkthrough of the complete workflow: in DaVinci Resolve, set Color Workspace to ACES CC, apply an IDT per-clip (for log footage), set ODT to sRGB for preview, then disable ODT and export as EXR (RGB half) for Blender. In Blender (with ACES config), set display device to ACES, view transform sRGB, sequencer ACES CG; import EXR footage with color space ACES 2065-1; import HDRI with IDT "utility-linear-sRGB"; match camera via F-Spy; build minimal scene geometry; use a shadow-catcher floor plane with render layers (main objects + shadows) to separate CG from shadow; composite in a second Blender scene using Alpha Over nodes; export composite as EXR. Back in Resolve, import composite EXR (IDT: ACES CG) and enable ODT (sRGB) to preview; color grade safely with gain/offset/temperature; export final H.264 with SRGB or P3 DCI ODT.

### Key Steps
1. **DaVinci Resolve — Project setup:** New project → Color Management → Color Workspace = `ACES CC` → save.
2. **Apply IDT to LOG footage:** Right-click clip → select appropriate IDT (e.g. `Adobe RGB` for the example LOG clip); for RAW footage Resolve auto-applies the conversion. The two source clips are visible in the Media Pool [frame_001]: `A007_04061039_C036.mov` (the LOG clip) and `BlackmagicRAW_Clip.braw` — so the RAW case is specifically **Blackmagic RAW**, in project `ACES Main`.
3. **Preview:** Color Management → Output Device Transform = `sRGB` → footage now looks correct.
4. **Color correction (safe only):** Adjust color temperature, exposure, offset, and gain wheels only; avoid all other operations (they destroy linear data).
5. **Export EXR:** Disable ODT (set to None) before exporting; Export → Format: `OpenEXR`, Codec: `RGB Half`; render. (Optionally export an H.264 with ODT enabled for camera tracking reference.)
6. **Camera match:** Use F-Spy (free) to align camera perspective from a still frame; import camera into Blender via **File → Import → fSpy (.fspy)** — the entry in the Import submenu, which requires the fSpy Blender importer add-on [frame_002].
7. **Blender — ACES config:** Render Properties → Color Management → Display Device: `ACES`, View Transform: `sRGB`, Sequencer: `ACES CG`.
8. **Import footage:** In Camera tab, add background footage (EXR sequence) → Color Space: `ACES 2065-1`.
9. **HDRI:** World Shader Editor → Environment Texture node; select HDRI file; Color Space dropdown → `utility-linear-sRGB` IDT. Use `Ctrl+T` to add Mapping nodes; rotate via Z value.
10. **Scene geometry:** Floor plane as shadow catcher (Object Properties → Visibility → Shadow Catcher); add CG objects (monkey, balls, etc.) with rough material matching scene.
11. **Render layers:** Collection for floor (Indirect Only on main layer), collection for objects (Indirect Only on shadow layer); transparent background; output = `OpenEXR Multi-Layer`.
12. **Compositing scene:** New Blender scene (created as `Scene.001`, 1920×1080 at 100%, aspect 1.000 [frame_004]) → Compositing tab; import background EXR (color space: ACES 2065-1); import CG multi-layer EXR (color space: ACES CG); Alpha Over: background + shadows → Alpha Over + main objects → Composite node. Add temp camera + EEVEE 1 sample to enable Render Animation.
13. **Back in Resolve:** Import composite EXR → IDT: `ACES CG` → enable SRGB ODT → compare to original footage (colors should match). Color grade for final look. The composite comes back as an **EXR image sequence**, not a single file — `o_ServantSequence_Comped_v[10001-10024].exr`, cut on V2 above the original `.braw` on V1 [frame_005].
14. **Final export:** ODT = `sRGB` (or `P3 DCI` for cinema) → Render H.264.

### Nodes / Settings
- DaVinci: Color Workspace = `ACES CC`; IDT per clip (log-specific, e.g. `Adobe RGB`); ODT = `sRGB` for preview, `None` for export; Format: OpenEXR RGB Half
- Blender **2.81** [frame_002]: Display Device = ACES; View Transform = sRGB; Sequencer = ACES CG
- Cycles setup shown alongside: Feature Set `Supported`, Device `GPU Compute`, Integrator `Path Tracing`, samples Render **128** / Viewport **32** [frame_002]
- Background EXR color space node: `ACES 2065-1`
- HDRI environment texture color space: `utility-linear-sRGB`
- Ctrl+T (Node Wrangler) on image/env node → auto-creates Mapping + Texture Coordinate nodes
- Shadow Catcher: Object Properties → Visibility → Shadow Catcher checkbox
- Render Layers: Main Objects (floor = Indirect Only) + Shadows (objects = Indirect Only)
- Composite: two Alpha Over nodes stacked (background → shadows → objects)
- EXR output (ACES CG) → Resolve IDT: `ACES CG`
- Final ODT: `sRGB` for monitors, `P3 DCI` for cinema projectors

### Difficulty
Intermediate — requires DaVinci Resolve + Blender ACES config; multi-step pipeline spanning two applications; Part 1 concepts are prerequisite.

### Blender Version
**Blender 2.81** — read from the status bar, `v2.81.16` [frame_002]. This entry
previously said *"Any (with ACES color config installed)"*, which was an
inference from the transcript; the footage dates the workflow precisely.

⚠️ **The version is not incidental for this tutorial.** 2.81 predates Filmic
being replaced by AgX (4.0), predates the compositor's `Mix` → `Mix Color`
rename, and predates the current Color Management panel layout. The
Display Device / View Transform / Sequencer settings in Key Step 7 are described
as they appear in 2.81. An ACES config is still required (see the Mario Cossadez
tutorial linked in the original video description).

**DaVinci Resolve 16 (PUBLIC BETA)** — read from the application's own status
bar [frame_001, frame_005]. The Resolve half of this workflow is likewise
described as it stood in 16.

### Tags
#color-management #aces #vfx #compositing #rendering #davinci-resolve #intermediate

---

## Frame verification (2026-09-01)

| | |
|---|---|
| **Corrected** | `blender_version` was *"Any (with ACES config installed)"* — an inference. The status bar reads **v2.81.16** [frame_002]. For a colour-management tutorial this is load-bearing: 2.81 predates AgX, the `Mix Color` rename and the current Color Management panel. |
| **Added** | **DaVinci Resolve 16 PUBLIC BETA**, project `ACES Main` [frame_001, frame_005]; the RAW example is **Blackmagic RAW** (`BlackmagicRAW_Clip.braw`) beside the LOG `.mov` [frame_001]; fSpy arrives through **File → Import → fSpy (.fspy)** [frame_002]; Cycles at GPU Compute, 128/32 samples [frame_002]; the compositing scene is `Scene.001` at 1920×1080 [frame_004]; the composite returns as an EXR **sequence**, `[10001-10024]` [frame_005]. |

⚠️ **`frame_000` (1:40) and `frame_003` (7:00) are mistimed picks** — both land on
talking-head shots. 2 of 6 here, against the ~25% rate plan batch D3c measured for
chapter-anchored picks. This file's chapters are unusually coarse (`SOFTWARE SETUP`
spans 0:49–8:06), which is exactly the condition that makes an interpolated moment
a guess.

---

## Related Tutorials
- `add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1.md` — prerequisite theory: color gamut, gamma, display-referred vs scene-referred
- `i-recreated-movie-scene-in-blender-nuke-complete-tutorial.md` — another full VFX compositing pipeline with live footage
- `replacing-adobe-after-effects-with-blender-tutorial.md` — Blender's native compositing tools as an alternative pipeline
