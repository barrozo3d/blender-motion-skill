---
title: Add VFX to Cinematic RAW and LOG Footage (the right way) | ACES Part 2
source: YouTube
url: https://www.youtube.com/watch?v=LssHxDCM7H4
author: InLightVFX
ingested: 2026-06-25
blender_version: "Blender 2.81.16 -- observed in frame_008"
tags: [color-management, aces, vfx, compositing, rendering, davinci-resolve, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/
frame_count: 27
frame_status: complete
grounding: key-steps-anchored (25/25 steps, 2026-09-11)
frame_selection: explicit-timestamps (supplied to select_frames.py; NOT evidence that the frames were read -- see `grounding:`)
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

- [1:12] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_000.jpg
- [1:20] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_001.jpg
- [1:32] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_002.jpg
- [2:05] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_003.jpg
- [3:38] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_004.jpg
- [4:18] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_005.jpg
- [4:42] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_006.jpg
- [5:00] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_007.jpg
- [5:38] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_008.jpg
- [5:58] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_009.jpg
- [6:35] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_010.jpg
- [6:52] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_011.jpg
- [7:32] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_012.jpg
- [7:52] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_013.jpg
- [8:12] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_014.jpg
- [8:22] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_015.jpg
- [8:30] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_016.jpg
- [8:42] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_017.jpg
- [8:48] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_018.jpg
- [9:08] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_019.jpg
- [9:25] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_020.jpg
- [9:45] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_021.jpg
- [10:02] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_022.jpg
- [10:20] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_023.jpg
- [10:45] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_024.jpg
- [11:12] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_025.jpg
- [11:28] tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/frame_026.jpg

---

## Structured Notes

### Core Technique
The end-to-end ACES round trip for adding CG to RAW/LOG footage: set DaVinci Resolve's project to an ACES colour science, bring footage in through an **IDT** and preview through an **ODT**, export EXR in ACES 2065-1, render the CG in Blender with ACES as the display device and ACEScg as the working space (tagging every incoming image with its own IDT), composite shadows and objects over the plate, and hand the result back to Resolve for grading and final delivery.

### Summary
12m17s, DaVinci Resolve 16 (Public Beta) and **Blender 2.81.16** [frame_008]. Part 2 of two — part 1 covers the gamut and gamma theory this applies. The source is a Blackmagic RAW clip, `4096 x 2160`, 24 fps, 16-bit [frame_000]; a paid "ACES Kickstart Kit" supplies the footage, HDRI and blend file [transcript 0:19].

**Resolve, in:** Project Settings ▸ Image Scaling for the frame fit [frame_001], then Color Management ▸ **Color science → `ACEScc`** (the dropdown also offers DaVinci YRGB, DaVinci YRGB Color Managed and ACEScct) [frame_002], **ACES version 1.1**, and the **ACES Output Device Transform → `sRGB`** so the preview looks normal again [frame_004, frame_006]. The **Input Device Transform** list is huge and mostly camera-and-profile specific — Canon C200/C300/C500/C700 CanonLog/CLog2/CLog3 in Daylight and Tungsten, Rec.709/Rec.2020/Cinema variants, Blackmagic Design Film/Video Gen 3 and 4, Alexa, DCDM [frame_003]. RAW converts automatically; LOG needs an IDT chosen per project or per clip [transcript 2:33-2:53].

Grading before export is deliberately minimal — white balance, exposure, offset and gain only, because other operations destroy the linear light information. The video puts **"Don't do this!"** on screen over the Color Wheels panel to make the point [frame_005]. The ODT is then disabled and the clip exported as **EXR / `RGB half (No Compression)`** [frame_007], the only format that carries the full ACES data [transcript 4:49-5:07].

**Blender:** Color Management set to Display Device **`ACES`**, View Transform **`sRGB`**, Sequencer **`ACES - ACEScg`** [frame_008]; the camera comes from fSpy [frame_009]. Scene build is a floor plane with a rough wood-matching material [frame_010], Suzanne and two spheres. The HDRI comes in via `Add ▸ Texture ▸ Environment Texture` [frame_011] and — the ACES-specific part — **every incoming image must be tagged with its own colour space** on the node: the file arrives as `ACES - ACEScg` and is switched to `Utility - Linear - sRGB` [frame_012, frame_013], since the 360 camera shoots sRGB and HDRIs carry linear scene-referred gamma [transcript 7:18-7:45]. `Ctrl+T` adds Texture Coordinate + Mapping to rotate it [frame_013].

**Render layers:** objects are sorted into collections with `M` [frame_014] — `Camera` (FSpy Camera), `Environment` (Floor), `Objects` (Sphere_Grey, Sphere_Reflective, Suzanne) [frame_016]. Two view layers, `Main Objects` and `Shadows`, each setting the *other* collection to **Set Indirect Only** via the collection's View Layer menu [frame_017]; the floor is a shadow catcher, Film ▸ **Transparent** is ticked [frame_018], and output is OpenEXR MultiLayer.

**Compositing** happens in a separate scene [frame_019] at the project resolution [frame_020]: the plate image sequence tagged `ACES` and the two CG layers tagged ACEScg, combined by two stacked **Alpha Over** nodes — plate under shadows, that under main objects — into Composite and Viewer [frame_021]. Rendering just a node graph needs a camera in that scene and the engine set to Eevee [frame_022].

**Resolve, out:** the comped EXR sequence gets an **ACES Input Transform** of its own [frame_023], the sRGB ODT goes back on, and the grade happens with the full original latitude intact — the gain slider still recovers window detail and the mirror ball's highlight [frame_024, frame_025]. Final delivery is QuickTime **H.264 at 3840 x 2160**, 24 fps [frame_026]; swapping the ODT to `P3 DCI` would target a cinema projector instead [transcript 11:00-11:18].

### Key Steps
1. **Import the footage in Resolve.** Media page; the source here is `BlackmagicRAW_Clip.braw`, **`4096 x 2160`**, `24.000` fps, 24 frames, bit depth 16, with Linear PCM audio at 48 kHz [frame_000].
2. **Fix the frame fit.** Project Settings ▸ **Image Scaling**; input and output "Mismatched resolution files" are the controls, and the narration selects *scale full frame with crop* to lose the small black bars [frame_001, transcript 1:13-1:20].
3. **Switch the project to ACES.** Project Settings ▸ **Color Management** ▸ **Color science** — the dropdown offers `DaVinci YRGB`, `DaVinci YRGB Color Managed`, **`ACEScc`** and `ACEScct`; pick ACEScc [frame_002]. Expect the image to look wrong until the ODT is set.
4. **Understand what the IDT list is.** ACES ships hundreds of **Input Device Transforms**, nearly all camera-and-profile specific — e.g. `Canon C300MkII CLog2 Daylight v1.0 Rec.2020`, `Canon C500 Daylight v1.1 DCI-P3+`, `Blackmagic Design 4.6K Film Gen 3`, `Alexa`, `DCDM` [frame_003]. Scene-referred footage usually has an exact match; display-referred footage only has coarse general transforms [transcript 2:14-2:33].
5. **Apply the IDT.** RAW is converted automatically; for LOG set it either project-wide in Color Management or per clip by right-clicking it [transcript 2:33-2:53]. The per-clip route is shown later on the comped sequence [frame_023].
6. **Set the ODT so the preview is viewable.** **ACES Output Device Transform** → `sRGB`; the dropdown also offers `Rec.709`, `Rec.709 (D60 sim.)` and `sRGB (D60 sim.)` [frame_006]. Saved state: Color science `ACEScc`, ACES version **`ACES 1.1`**, Input Transform `No Input Transform`, Output Transform `sRGB`, Process Node LUTs in `ACEScc AP1 Timeline Space` [frame_004].
7. **Grade only what is safe before export.** Colour temperature, the exposure slider, the **Offset** wheel and the **Gain** wheel are safe; everything else destroys linear light information at this stage — the video labels the Color Wheels panel **"Don't do this!"** [frame_005, transcript 4:10-4:28].
8. **Disable the ODT before exporting**, so the export lands in ACES 2065-1 rather than sRGB [transcript 4:28-4:40] [no frame: the clearing itself is not on screen -- frame_006 catches this same ACES Output Device Transform dropdown, but at the moment `sRGB` is being chosen].
9. **Export EXR.** Deliver page, Format **`EXR`**, Codec **`RGB half (No Compression)`** — the dropdown also offers RGB half with DWAA/DWAB/PIZ/RLE/ZIP compression and the RGB float equivalents [frame_007]. EXR is the only format that carries the whole ACES colour space, at the cost of file size [transcript 4:49-5:07].
10. **Set Blender's colour management.** Render Properties ▸ Color Management: **Display Device `ACES`**, **View Transform `sRGB`**, Look `None`, Exposure `0.000`, Gamma `1.000`, **Sequencer `ACES - ACEScg`** — ACEScg being the slightly smaller linear space used for CG rendering [frame_008, transcript 5:28-5:46].
11. **Bring in the camera and the plate.** The camera was solved in the free tool **fSpy** and imported (`ServantFSpy2.fspy` in the outliner) [frame_009]; the exported EXR sequence is loaded as the camera background with its colour space set to `ACES 2065-1`, which is the IDT on the Blender side [transcript 5:46-6:08].
12. **Build the scene geometry.** A floor `Plane` with a material roughly matching the wood's colour and roughness (Principled BSDF, Specular `0.500`, Roughness `0.500`) [frame_010], plus Suzanne and two spheres [frame_016].
13. **Add the HDRI.** Shader Editor ▸ World ▸ `Add ▸ Texture ▸ Environment Texture`, wired into `Background` → `World Output` [frame_011], pointing at `ServantHDRI_FINAL_Gumroad.hdr`, `Equirectangular`, `Single Image` [frame_012].
14. **Tag the HDRI with its own IDT — the step that is easy to miss.** The node's **Color Space** drop-down is the input transform for that image: it arrives as `ACES - ACEScg` and must be set to **`Utility - Linear - sRGB`**, because the 360 camera shoots sRGB primaries and HDRIs carry linear scene-referred gamma [frame_012, frame_013, transcript 6:47-7:45]. The same applies to every image texture in the scene.
15. **Rotate the HDRI.** With the Environment Texture node selected press `Ctrl+T` to add `Texture Coordinate` → `Mapping`, then drive the Z rotation to align it [frame_013, transcript 7:45-8:04].
16. **Sort the scene into collections.** Press `M` ▸ Move to Collection ▸ New Collection and name it — the video puts the shortcut on screen [frame_014]. Result: `Camera` (FSpy Camera), `Environment` (Floor), `Objects` (Sphere_Grey, Sphere_Reflective, Suzanne) [frame_016].
17. **Make the floor a shadow catcher.** Object Properties ▸ **Visibility** ▸ **Shadow Catcher** ticked on `Floor`, alongside Show in Viewports / Show in Renders / Selectable and the Ray Visibility block (Camera, Diffuse, Glossy, Transmission, Volume Scatter, Shadow) — the floor then takes shadow without rendering itself [frame_015, transcript 8:12-8:18].
18. **Split objects and shadows into two view layers.** Name the current layer **`Main Objects`** [frame_016] and set the `Environment` collection to **Set Indirect Only** — right-click the collection ▸ **View Layer ▸ Set Indirect Only** [frame_017]. Add a second view layer **`Shadows`** and set the `Objects` collection to Indirect Only instead [transcript 8:23-8:41].
19. **Render with a transparent background.** Render Properties ▸ **Film ▸ Transparent** ticked (Transparent Glass off) [frame_018]; output type **OpenEXR MultiLayer**, then render the animation [transcript 8:41-8:52].
20. **Composite in a separate scene.** New scene, Compositing workspace, **Use Nodes** and **Backdrop** on, with a `Composite` and a `Viewer` node to start (both `Use Alpha`, `Alpha 1.000`, `Z 1.000`) [frame_019]. Check the scene's own resolution and output settings — the captured state reads `1920 x 1080`, `Frame Start 1 / End 250`, `24 fps`, File Format `PNG`, while the narration asks for 4K [frame_020, transcript 9:15-9:20]; set it to match the project before rendering.
21. **Wire the composite.** Load the plate image sequence with Color Space **`ACES`** (2065-1, matching the Resolve export) and the two CG layers with **`ACES - ACEScg`** (matching the render); stack two **`Alpha Over`** nodes (`Convert Premul` off, `Premul 0.000`, `Fac 1.000`) — plate in the top socket with `Shadows` beneath, then that result in the top socket with `Main Objects` beneath — and route the last one into `Composite` [frame_021, transcript 9:22-9:46].
22. **Render the graph.** A node graph alone will not render, so add a camera to the compositing scene and set the engine to **Eevee** — the narration says one sample, the captured state reads `Render 64 / Viewport 16` [frame_022, transcript 9:46-10:00] — and set the output to OpenEXR.
23. **Back in Resolve, tag the comp.** Right-click the comped EXR sequence ▸ **ACES Input Transform** and pick the transform matching what Blender wrote (`ACEScg`) [frame_023, transcript 10:00-10:21].
24. **Re-enable the sRGB ODT and grade.** The composite now matches the original plate with the CG added [frame_024]. Because everything stayed EXR, the full latitude survives — pulling gain down recovers detail outside the window and in the mirror ball's highlight, which PNG would have clipped [transcript 10:21-11:00]. A second example clip shows the same recovery in the sky [frame_025].
25. **Deliver.** Set the ODT for the target display — `sRGB` for screens, `P3 DCI` for a cinema projector [transcript 11:00-11:18] — then Deliver page: Format `QuickTime`, Codec **`H.264`**, Resolution **`3840 x 2160 Ultra HD`**, Frame rate `24`, Quality Automatic/Best, Add to Render Queue and render [frame_026].

### Nodes / Settings
- **Resolve project** — Color science `ACEScc`, ACES version `ACES 1.1`, ACES ODT `sRGB`, Process Node LUTs in `ACEScc AP1 Timeline Space`; Resolve 16 Public Beta [frame_002, frame_004]
- **Resolve IDT list** — camera+profile specific (Canon CLog/CLog2/CLog3 by body and white balance, Blackmagic Film/Video Gen 3–4, Alexa, DCDM) [frame_003]
- **Safe pre-export grading** — colour temperature, exposure, Offset wheel, Gain wheel only [frame_005]
- **Resolve EXR export** — Format `EXR`, Codec `RGB half (No Compression)` [frame_007]
- **Blender Color Management** — Display Device `ACES`, View Transform `sRGB`, Sequencer `ACES - ACEScg`, Exposure `0.000`, Gamma `1.000` [frame_008]
- **Environment Texture** — `ServantHDRI_FINAL_Gumroad.hdr`, Equirectangular, Single Image, Color Space `Utility - Linear - sRGB` [frame_012, frame_013]
- **`Ctrl+T`** — adds Texture Coordinate + Mapping to the selected texture node [frame_013]
- **`M`** — Move to Collection / new collection [frame_014]
- **Collection ▸ View Layer ▸ Set Indirect Only** — the per-view-layer split for objects vs shadows [frame_017]
- **Film ▸ Transparent** — transparent background for the CG render [frame_018]
- **Alpha Over** — `Convert Premul` off, `Premul 0.000`, `Fac 1.000`; two stacked, plate → shadows → main objects [frame_021]
- **Compositing scene render** — camera required, engine Eevee (`Render 64` in the captured state) [frame_022]
- **Resolve delivery** — QuickTime / H.264 / `3840 x 2160 Ultra HD` / 24 fps [frame_026]

### Difficulty
Intermediate

### Blender Version
Blender **2.81.16**, read from the status bar [frame_008, frame_010]. DaVinci Resolve **16 (Public Beta)** [frame_000, frame_002].

### Tags
color-management, aces, vfx, compositing, rendering, davinci-resolve, intermediate

---

## Related Tutorials
- `add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1.md` — prerequisite theory: color gamut, gamma, display-referred vs scene-referred
- `i-recreated-movie-scene-in-blender-nuke-complete-tutorial.md` — another full VFX compositing pipeline with live footage
- `replacing-adobe-after-effects-with-blender-tutorial.md` — Blender's native compositing tools as an alternative pipeline
