---
title: Finally! A VFX Workflow With Less Guesswork
source: YouTube
url: https://www.youtube.com/watch?v=G2SacOKhJto
author: InLightVFX
ingested: 2026-09-11
blender_version: "Blender 3.4+ -- inferred, no version string on screen; unified Mix node (3.4) in frame_021, Shadow Catcher pass (3.0) in frame_035"
tags: [color-management, aces, vfx, compositing, hdri, lighting, camera-tracking, nuke, davinci-resolve, photoshop, shadow-catcher, cycles, advanced]
extraction_status: complete
frames_dir: tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/
frame_count: 41
frame_status: complete
uncertainty_frames: []
grounding: key-steps-anchored (44/44 steps, 2026-09-11)
frame_selection: explicit-timestamps (supplied to select_frames.py; NOT evidence that the frames were read -- see `grounding:`)
---

# Finally! A VFX Workflow With Less Guesswork

**Source:** [YouTube](https://www.youtube.com/watch?v=G2SacOKhJto)
**Author:** InLightVFX
**Duration:** 17m12s | 11 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report — Reviewed

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- ~~WARNING: Frames captured at 360p, below the 720p this skill's policy asks for. The rescue via the default client did not beat it, so the source itself may not offer a taller stream.~~
  **SUPERSEDED 2026-09-11.** The warning's inference was wrong: the source DOES offer a taller stream. The `android` player client this skill forces in `_ytdlp_cmd()` exposes only muxed itag 18 (640x360) for this video, while `web_embedded` exposes the full ladder to 2160p. `download_video_low()` already tries `web_embedded` first, but that attempt hit a transient `CalledProcessError` on both retries and fell back to the 360p client. Re-running the same `select_frames.py --force` command succeeded on `web_embedded` (format 398). **All 41 frames in this entry are 1280x720**, verified with ffprobe; the Structured Notes below were read from those, not from the 360p set.

---


Frames captured — see "Captured Frames" section below.


### Introduction to Workflow [0:00]
**Transcript (timestamped):**
[0:00] Have you ever worked on a visual effects shot where you were just kind of guessing to get the lighting to match your footage?
[0:05] And then in compositing you're endlessly tweaking stuff to get things looking right?
[0:09] Okay, shift the gain, a little bit less blue, a little bit more gamma, what is gamma?
[0:12] Gamma to heal with the gain, lift it up, too much blue, lift it down, gain, gamma, gain.
[0:17] This is how I used to work, but not anymore.
[0:19] With my new workflow, I can confidently match the lighting between my footage and CGI elements.
[0:25] This works in different lighting conditions too.
[0:27] So I'll break down this entire workflow, which uses a few simple tools when filming,
[0:31] along with the ACES color system to achieve these great results.
[0:34] Let's jump in.
[0:39] So you can follow along, you can download this workflow graphic along with the footage,
[0:44] photo and blender assets for free at the link in the description.
[0:47] Now the success of this workflow begins with a careful filming process.


### Filming and Data Capture [0:48]
**Transcript (timestamped):**
[0:51] For my main camera, I use a Panasonic GH5 with a V-Log color space,
[0:56] which gives me very flat footage.
[0:58] And I make sure to set my white balance to a constant value so that it's not changing throughout the shot.
[1:03] I film my footage, and then right afterwards, without changing any lighting, camera settings,
[1:08] or general camera position, I'll put this color checker in the shot and take some footage of it.
[1:13] This is the X-Rite Color Checker Classic.
[1:16] You don't absolutely need a color checker, you can use a white balance card or nothing at all,
[1:21] but a color checker will provide the best reference.
[1:24] Next, I'll keep the color checker in place and set up my 360 camera close to where my CG elements will be in the scene.
[1:31] With this 360 camera, and most 360 cameras nowadays, I can shoot multiple photos at different exposures.
[1:38] So in the end, we have our main footage, footage of our color checker, and our 360 photos, including our color checker.


### Creating the HDRI Map [1:45]
**Transcript (timestamped):**
[1:45] To start, let's create our HDRI.
[1:47] First, we need to merge all our 360 photos into one image.
[1:52] Some 360 cameras come with free programs to do this, but I use Photoshop.
[1:56] I'll merge all the photos together using the Merge to HDR Pro function.
[2:01] I'll select my individual photos and then make sure to uncheck the Alignment option,
[2:05] since we know the 360 camera was stationary, and then let's let Photoshop merge these images together.
[2:11] I'll uncheck this box, hit OK, and here we have our HDRI.
[2:16] At this point, we're not going to worry about adjusting the HDRI.
[2:20] We simply save it out as a radiance file.


### Color Management with ACES [2:23]
**Transcript (timestamped):**
[2:23] Next, we want to convert both the HDRI and our footage into the same color space.
[2:28] To do this, we are going to use ACES.
[2:30] If you haven't watched my ACES tutorial, definitely give it a watch before continuing with this video,
[2:36] because I'm going to use concepts that I explained in that tutorial.
[2:40] Now, every image or video file has a certain color space with a specific color gamut and a gamma mapping.
[2:46] My GH5 footage has a color gamut called V-Gamut and a non-linear gamma mapping called V-Log.
[2:53] My 360 camera takes individual photos, which have the color gamut sRGB and a non-linear gamma mapping.
[3:01] After I merge all the 360 photos, the resulting HDRI has the same color gamut sRGB,
[3:06] but my gamma mapping is now linear.
[3:09] To match our HDRI to our footage, we want both elements to have the same color space.
[3:14] This is where ACES comes in.
[3:16] We will apply a unique ACES Input Display Transform, or IDT, to our footage and HDRI.
[3:23] This will convert both to have the same ACES color space.
[3:26] So to begin this process, I'm going to jump into the free version of Nuke,
[3:30] because Nuke is really good when it comes to color management.
[3:33] So here in Nuke, we'll go to the project settings.
[3:36] Then in this color tab, we can tell Nuke to use ACES.
[3:39] Then I'll press R in this area to read in the GH5 footage.
[3:44] If I then click on the read node, I can see this Input Transform option.
[3:48] This is where we will select the ACES IDT to convert our footage into the ACES CG color space.
[3:55] In this case, we'll select an IDT called Input Panasonic V-Log V-Gamut.
[4:00] Now how do you know what IDT to use for your camera?
[4:03] First, search Google for correct ACES IDT for your camera name with color profile name that you use.
[4:10] And just know that there are only ACES IDTs made for the most popular log and raw color profiles.
[4:17] And here's another neat check that you can do.
[4:19] Set up your camera and record footage of a scene at the correct exposure,
[4:23] plus two stops overexposed and minus two stops underexposed.
[4:28] In Nuke, I have the footage and I've selected the ACES IDT I want to test.
[4:33] Here I've split out the correctly exposed, overexposed and underexposed footage.
[4:38] If I add an exposure effect to our correct exposure and I change the adjustment to stops, I can add two stops.
[4:45] Zero plus two stops should look very similar to the original plus two stops from our camera, and they do.
[4:54] Similarly, I can apply this exposure effect here and I can subtract four stops.
[4:59] Two minus four stops should look very similar to the original minus two stops from our camera, and it's pretty close.
[5:07] Passing this test does not guarantee that you have the right IDT selected for your camera,
[5:12] but you know if you fail this test, you don't have the right IDT selected.
[5:16] Okay, back to Nuke. Next I'll read in the HDRI.


### Matching Exposure and Light [5:17]
**Transcript (timestamped):**
[5:20] And then for this input transform, I will look for an ACES IDT called Linear sRGB.
[5:26] Next we need to make the exposure and white balance of our HDRI match our footage.
[5:31] Here's how we'll do this. We have our footage and our HDRI, both with the color checker showing.
[5:36] We're going to sample the color of this gray patch in the footage and then also in the HDRI.
[5:42] We can see the RGB values of these two gray colors which are not matching.
[5:46] So I will multiply the HDRI by three values that will result in a color that will now match the other color.
[5:53] And with this multiplication applied to the entire HDRI, it will now match the footage.
[5:58] So in Nuke, let's look at our footage and we'll zoom in on this color checker.
[6:02] We can then hold Command or Control and Shift to sample the pixel values of this gray patch.
[6:08] I can see the RGB values down here.
[6:11] To record these values, I'll create a node called a sticky note and write down the values.
[6:18] Then let's view the HDRI. Zoom in on the color checker and let's now sample the same gray patch here.
[6:25] You can see these RGB values are quite different from the ones we've recorded.
[6:29] So let's add a multiply node and we'll click here to give us separate RGB controls.
[6:34] Now, starting with the red value, I'll adjust this till our HDRI is reading the same as the red value in our footage.
[6:41] Then I can do the same to match the blue and green values.
[6:46] And if you don't have a color checker, you can try matching by sampling a different part of the scene, like the concrete here.
[6:52] But now that things are matching, in theory, if I sample any part of the scene, say part of the sky,
[6:58] the color value should be exactly the same in our footage and HDRI.
[7:02] At this step, it's important that you don't add any major color grading to your footage or HDRI.
[7:08] Certain color grading adjustments like gamma will mess up the linear nature of our footage, taking away the benefits of this linear workflow.
[7:16] At this point, just stick to making adjustments using multiply operations such as gain, which keeps things linear.
[7:22] And of course, make sure to apply the same adjustments to both the footage and HDRI.
[7:27] But that's it for our work in Nuke. We've calculated these values to match our HDRI and footage, and we'll use these values as we jump into Blender.


### Setting up the Blender Scene [7:36]
**Transcript (timestamped):**
[7:36] I have Blender configured for ACES. Check the description for a tutorial on how to do this.
[7:41] I have a camera in my scene, and I've set the background to my camera footage.
[7:45] This color space option here is our ACES IDT, and so I set it to the same Panasonic IDT we selected earlier.
[7:52] I've also aligned my camera to the proper perspective for the scene.
[7:56] Next, we'll go to the shader editor and select the world option here.
[8:01] I've opened that HDRI file we created in Photoshop, and again, the color space option here is the same thing as our ACES IDT, so we select linear sRGB.
[8:10] Now we want to apply the same color correction here that we applied to our HDRI in Nuke.
[8:16] To do this, we'll add a color mix node set to multiply with our HDRI plugged in.
[8:21] Make sure the factor is turned up to 1. Then, for this bottom color, we will copy the R, G, and B values that we calculated in Nuke.
[8:35] I found this really cool Dodge Charger model for free on BlendSwap. First, I'll open this model in its own Blend file.


### Object Material Management [8:36]
**Transcript (timestamped):**
[8:42] I'm going to go through all the materials and look for any images being used.
[8:46] We want to make sure we're using the proper ACES IDT to convert all our materials properly into ACES.
[8:53] For any images which are part of the diffuse, color, or albedo of a material, we want to use the IDT Roll Matte Paint or Utility sRGB Texture.
[9:03] They do the same thing.
[9:06] For any images which drive the roughness, metalness, bump, displacement, etc., we will use the IDT named Roll Data or Utility RAW.
[9:15] They also do the same thing.
[9:17] Finally, for any parts of the materials that use an RGB color input, we need to convert this value into the ACES CG Gamut.
[9:25] Unfortunately, Blender does not yet do this for us, so we'll have to do it manually.
[9:30] I've used this website to calculate the new values, which I'll link below.
[9:34] Back in our main Blend file, I'll append the collection with our updated car model.


### Scene Lighting and Shadows [9:35]
**Transcript (timestamped):**
[9:38] Now, let's go into rendered view to see how things are looking.
[9:41] We'll notice the lighting from our HDRI is a bit off.
[9:44] We don't have the brightness and shadows that we can see in our reference footage.
[9:48] When I captured the different exposures from my 360 camera, this was the darkest exposure the camera was able to capture, and you can see the sun looks like a large blob.
[9:57] The sun should look like a very small point in our darkest exposure, just like this.
[10:01] Unfortunately, most 360 cameras cannot be equipped with the necessary filters to capture such low exposures, so here's a quick workaround.
[10:09] First, in Photoshop, I'm going to cover up the bad sun in our HDRI.
[10:13] To do this, I'll add an exposure adjustment so I can see the sun more easily.
[10:17] Then, let's add an empty layer over our background.
[10:20] Let's select a color picker and make sure we set the sample mode to current and below no adjustments.
[10:26] Then, let's go into the gradient tool and we'll go into the color settings.
[10:30] For the left value, we'll select an area just outside the sun flare, and for the right, we'll select an area a bit further from the sun.
[10:37] Then, make sure to have selected the radial gradient type and we'll drag out a gradient from the center of our sun.
[10:44] Then, let's turn the layer off and select the ellipse tool, select path for the mode, and let's draw a mask around the sun and hit mask.
[10:53] Turn the layer back on and we can select our new mask and increase the feather amount in the properties window.
[10:59] Now, we have effectively taken out the bad sun.
[11:02] Let's turn off the exposure adjustment and save out a new HDRI radiance file.
[11:07] Back in Blender, we'll swap in this new HDRI without the sun in it.
[11:12] Now, we're going to create our own sun object.
[11:14] We'll dial in this strength value later, but for now, let's eyeball it.
[11:18] Then, we'll rotate the sun to align the shadows with how they appear in our reference footage.
[11:23] You can increase the sun angle value if you want the shadows to be softer, but my reference shadows are sharp, so I'll keep this value low.
[11:32] Now, how do we know how bright the sun should be?
[11:35] What I can do is download a special EXR graphic of the color checker and bring this into Blender using the image as planes tool.
[11:43] In the material settings, our IDT is set to ACES CG, which is correct since this EXR is in ACES CG.
[11:50] I will adjust the roughness of my material to 0.8.
[11:53] Then, I'm going to position this color checker in roughly the same position and angle as the real color checker we filmed.
[12:00] Let's look through the main camera in the render view and we'll create a small render region just for our color checker.
[12:06] Oh, and let's turn off our floor plane for now.
[12:09] Let's hit render and in the render result window, if we right click and hold, we can sample the pixel values of this gray patch here.
[12:17] Here, our values are reading around 0.23.
[12:20] And remember, in our footage, our gray patch is reading around 0.28.
[12:24] So from here, we just want to increase the strength of the sun till this gray patch reads around 0.28.
[12:31] Now, let's turn our floor plane back on and our lighting is looking a lot closer to our reference.
[12:36] For our floor material, I'm going to simply project our footage onto this plane.


### Compositing Pass Generation [12:37]
**Transcript (timestamped):**
[12:41] To do this, I'll add a project UV modifier, select the default UV map, and select the camera for our projection object.
[12:48] Then for the aspect X and Y, we'll set 16 and 9 since the footage we're projecting has a 16 by 9 aspect ratio.
[12:56] We'll also add a subdivision surface modifier set to simple and place this before our UV project modifier.
[13:03] This just makes sure we have enough detailed geometry to accurately project onto.
[13:08] Next, here is the material setup.
[13:10] This node is the footage of my clean plate, again set to have that Panasonic IDT.
[13:16] Then I've added an RGB curves node to match the colors a bit more.
[13:20] And I've raised the roughness slightly on this shader node.
[13:23] This technique of projecting the footage onto the floor plane won't always work this well.
[13:28] In some cases, you might have to create your own shader to recreate the floor material.
[13:33] Now let's set this plane as a shadow catcher.
[13:35] And in the Render Passes tab, let's enable the Shadow Catcher Render Pass.
[13:39] Through the car windows, we're seeing the HDRI which doesn't look realistic.
[13:43] So I'll duplicate this floor plane, place it in the background, and uncheck the Shadow Catcher property.
[13:49] Let's duplicate this projection material and change this to an emission shader.
[13:54] And I will delete the RGB curves.
[13:56] Then we only want this plane to be visible through the windows.
[13:59] So in the Object Properties tab, we'll uncheck all the visibility options except for Transmission.
[14:05] Now we're ready to hit Render.
[14:07] Don't worry if you don't see the shadow being rendered out.
[14:10] On the final render, the shadow information will be hiding in this Shadow Pass that we enabled.
[14:15] Finally, we'll save out this render as an OpenEXR multilayer file.
[14:19] Now the beauty of all this setup is that compositing is going to be super simple.


### Compositing in Blender [14:21]
**Transcript (timestamped):**
[14:25] In a new blend file, let's go into the Compositing tab and check Use Nodes.
[14:30] We'll then read in our background footage, change some of the frame settings here,
[14:35] and again we'll set the ACES IDT to the Panasonic one.
[14:38] Then we'll also read in our car render which should have an ACES IDT set to ACES CG.
[14:44] First, let's work with our Shadow Pass which we can view by Ctrl plus Shift and clicking this node multiple times.
[14:51] This is a relatively new pass in Blender, and it's really cool because this pass not only captures the shadow darkness,
[14:57] but also the color of the shadows.
[14:59] To composite this pass properly, we'll add a Color Mix node set to Multiply,
[15:03] and we'll multiply the background footage by this pass.
[15:09] Next, we'll simply add an Alpha Over node and place our background in the top input and our car in the bottom.
[15:15] Now let's compare what we have here so far with our reference.
[15:19] I think for our first tweak our shadows should be darker.
[15:22] To do this we'll add a Gamma node to the Shadow Pass and increase the value slightly.
[15:28] Then I want to adjust the color of our car since it looks a bit too magenta.
[15:32] So we'll add a Color Balance node and adjust the Gain away from Magenta.
[15:38] Then I think our shadows could be a bit more blue, so let's add another Color Balance node,
[15:42] and here we don't want to adjust the Gain, we want to stick with only using the Gamma adjustments just like before.
[15:48] To render out our final comp, make sure your composite is hooked up to the Composite node.
[15:53] I will set an Output Type of OpenEXR and name the file Output.
[15:57] Then hit Render Animation.
[15:59] Now for the final color grading.


### Final Grade and Conclusion [16:01]
**Transcript (timestamped):**
[16:01] In DaVinci Resolve I will go into the Project Settings, and in the Color Management tab,
[16:07] I will set the Color Science to Aces and set our Output Transform to sRGB.
[16:13] I'll import the EXR of my final render, then we can right click the EXR, go to Aces Input Transform, and select Aces CG.
[16:23] This is the Aces IDT.
[16:25] Next in the Color tab I can add some nice color grading.
[16:29] Finally I'll go into the Export tab, select H.264, and I can render out my final shot.
[16:35] So there you have it, the full workflow.
[16:38] Now your homework is to go download those free assets and try adding that car to the shot in the shade.
[16:43] Now for this one you don't have to replace the sun in the HDRI because it's not visible.
[16:47] And when you have your results, send them to me on Instagram or Twitter, and I will send you my Aces Kickstart Kit for free.
[16:54] Alright, thanks for watching and subscribing, and I'll see you in the next one.
[17:07] you



---

## Captured Frames

- [0:21] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_000.jpg — goal matched cgi result
- [0:41] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_001.jpg — workflow graphic overview
- [0:53] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_002.jpg — gh5 vlog flat footage
- [1:14] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_003.jpg — xrite colorchecker classic
- [1:28] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_004.jpg — 360 camera with colorchecker
- [1:58] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_005.jpg — photoshop merge to hdr pro
- [2:05] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_006.jpg — uncheck alignment option
- [2:48] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_007.jpg — vgamut vlog colorspace diagram
- [3:19] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_008.jpg — idt conversion diagram
- [3:38] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_009.jpg — nuke project settings aces
- [3:58] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_010.jpg — panasonic vlog vgamut idt
- [4:36] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_011.jpg — exposure test split view
- [4:50] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_012.jpg — plus two stops check
- [5:23] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_013.jpg — hdri read linear srgb idt
- [5:39] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_014.jpg — gray patch sampling diagram
- [6:06] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_015.jpg — nuke sample pixel values
- [6:15] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_016.jpg — sticky note recorded values
- [6:33] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_017.jpg — multiply node separate rgb
- [7:12] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_018.jpg — gamma grading warning
- [7:44] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_019.jpg — blender camera background idt
- [8:05] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_020.jpg — world shader hdri linear srgb
- [8:20] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_021.jpg — color mix multiply rgb values
- [8:39] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_022.jpg — dodge charger blendswap
- [8:58] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_023.jpg — diffuse idt utility srgb
- [9:09] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_024.jpg — data idt utility raw
- [9:31] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_025.jpg — rgb to acescg converter
- [9:53] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_026.jpg — bad sun blob darkest exposure
- [10:49] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_027.jpg — ellipse path mask around sun
- [11:20] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_028.jpg — sun object rotate shadows
- [11:40] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_029.jpg — exr colorchecker as plane
- [12:14] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_030.jpg — sample render result gray patch
- [12:46] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_031.jpg — uv project modifier camera
- [13:13] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_032.jpg — floor material node setup
- [13:36] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_033.jpg — shadow catcher render pass
- [14:02] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_034.jpg — transmission only visibility
- [14:48] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_035.jpg — shadow pass viewed
- [15:06] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_036.jpg — multiply background by shadow
- [15:25] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_037.jpg — gamma node darken shadows
- [15:36] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_038.jpg — color balance demagenta
- [16:09] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_039.jpg — resolve aces color management
- [16:36] tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/frame_040.jpg — final graded result

---

## Structured Notes

### Core Technique
A measured, non-guesswork lighting-match workflow for live-action VFX: shoot a **ColorChecker** in the plate and in a bracketed 360 capture, merge the 360 set into an HDRI, convert both plate and HDRI into **ACES/ACEScg** with the right per-source **IDT**, then *numerically* match them by sampling the same grey patch in both and applying a per-channel **multiply** to the HDRI. The same multiply is reproduced in Blender's world shader. Sun intensity is then dialled in objectively by rendering an **ACEScg ColorChecker EXR** placed in the scene and raising the sun's Strength until its grey patch reads the same value as the real one in the plate. The result needs almost no compositing guesswork — plate × **Shadow Catcher pass**, Alpha Over the CG, and two small Color Balance tweaks.

### Summary
17m12s, InLightVFX (**Jacob J Holiday** — visible in the render path `/Users/jacobholiday/Desktop` [frame_040]). Toolchain: **Panasonic Lumix GH5** in V-Log [frame_002], a Ricoh 360 camera, **Adobe Photoshop 2023** [frame_005, frame_027], **Nuke 13.2v5** [frame_009], Blender, and **DaVinci Resolve 17** [frame_039, frame_040]. The shot puts a CG muscle car onto a concrete parking deck and is cut against the real reference throughout [frame_000].

**The whole workflow on one page** — the downloadable graphic lays out every stage with the actual numbers: footage and HDRI both pushed through an ACES IDT into ACEScg/linear-scene-referred; the footage's grey patch reads `R 0.28 G 0.28 B 0.28` and needs **no change**; the HDRI's reads `R 0.44 G 0.44 B 0.51` and is multiplied by **`0.64 / 0.64 / 0.55`** to land on the same `0.28 / 0.28 / 0.28`; only then is any colour correction applied, to both equally [frame_001].

**Why ACES:** every source carries its own gamut and gamma [frame_007]. The GH5 delivers **V-Gamut / non-linear V-Log**; the merged HDRI is **sRGB / linear, scene-referred** [frame_008]. An IDT per source converts both into one working space so a sampled value in one is directly comparable to the same value in the other.

**The objective sun.** Most 360 cameras cannot bracket dark enough — the darkest exposure still renders the sun as a large soft blob rather than a point [frame_026], which under-lights the scene. The fix is to paint the sun out of the HDRI in Photoshop [frame_027] and add a real Blender **Sun** object [frame_028], then set its strength by measurement rather than eye: render the ACEScg ColorChecker EXR [frame_029] in place and push Strength until its grey patch matches the plate's [frame_030].

**Transcript vs. what the frames show** — three corrections worth carrying:
- The narration says *"Dodge Charger"*, and the author's own collection is indeed named `Dodge Charger` [frame_028] with renders called `charger_sun_v03.exr` [frame_035] — but the BlendSwap model is a **Dodge Challenger 1970 R/T** by *ziwerliz*, CC-0 [frame_022].
- *"Roll Matte Paint"* and *"Roll Data"* are Whisper renderings of the colour-space entries **`role_matte_paint`** and **`role_data`** [frame_023, frame_024].
- The narration calls Nuke *"the free version"*, but the title bar reads `RampDemos.nkind — NukeIndie` [frame_009]; `.nkind` is **Nuke Indie**, the low-cost paid tier, not the free Non-commercial build (`.nknc`).
Also minor: ACES's *IDT* is an **Input Device Transform**, not the "Input Display Transform" of the narration [transcript 3:16].

### Key Steps
1. **Shoot the plate with a constant white balance** on a log profile — here a Panasonic Lumix GH5 in **V-Log**, giving deliberately flat footage [frame_002, transcript 0:51-1:03].
2. **Immediately shoot the ColorChecker** in the same lighting, camera settings and position — an **X-Rite ColorChecker Classic** laid in the shot. A white-balance card or nothing at all will work, but the chart gives the best reference [frame_003, transcript 1:03-1:24].
3. **Leave the chart in place and shoot the 360 brackets** from where the CG element will sit, capturing multiple exposures [frame_004, transcript 1:24-1:38]. You end with three things: the plate, chart footage, and bracketed 360 stills including the chart.
4. **Merge the brackets into an HDRI.** Photoshop ▸ **File ▸ Automate ▸ Merge to HDR Pro** [frame_005].
5. **Uncheck "Attempt to Automatically Align Source Images"** in the Merge to HDR Pro dialog — the 360 rig was stationary, so alignment can only hurt. The source list here is the Ricoh's bracket set, `R0011424.JPG` … `R0011431.JPG` [frame_006]. Take no tone-mapping options; save straight out as a **Radiance (.hdr)** file [transcript 2:11-2:22].
6. **Understand what you are converting.** Every file has a gamut and a gamma mapping [frame_007]: the GH5 plate is **V-Gamut / non-linear V-Log**, the merged HDRI is **sRGB / linear scene-referred** [frame_008, transcript 2:40-3:09].
7. **Put Nuke into ACES.** Project Settings ▸ **Color** ▸ color management `OCIO`, then swap the OCIO config from `nuke-default` [frame_009] to **`aces_1.2`** — after which the default LUT settings read working space `scene_linear (ACES - ACEScg)`, Monitor Out `sRGB (ACES)`, 8-bit `matte_paint (Utility - sRGB - Texture)`, 16-bit `texture_paint (ACES - ACEScc)` [frame_016].
8. **Read in the footage and set its IDT.** Press `R`, select the Read node, and set **Input Transform** from `Input ▸ Panasonic ▸` **`Input - Panasonic - V-Log - V-Gamut`** — the vendor list also covers ADX, ARRI, Canon, Generic, GoPro, RED and Sony [frame_010]. The Read node's other settings: `P1077048.MP4`, UHD_4K `3840x2160`, h264 [frame_012].
9. **Find the right IDT for your camera** by searching for "correct ACES IDT for `<camera>` with `<profile>`"; IDTs exist only for the more popular log and raw profiles [transcript 4:00-4:17]. [no frame: the search itself is narrated over B-roll; frame_010 shows the vendor-and-profile list you are trying to match against]
10. **Sanity-check the IDT with an exposure test.** Shoot the same scene at correct exposure, **+2** and **−2** stops, then split them out with three `FrameHold` nodes (here frames 1200 / 81 / 490 for −2 / 0 / +2) [frame_011]. Add an **Exposure** node to the correct-exposure branch [frame_012] and add two stops: it should match the camera's own +2. Then subtract four: it should match the camera's −2 [frame_012, transcript 4:38-5:07]. Passing does not prove the IDT is right, but **failing proves it is wrong**.
11. **Read in the HDRI and set its IDT** to **`Utility - Linear - sRGB`** from the `Utility` submenu. The captured Read node is `GarageSun_ColCheck_Original_v01.hdr` at **`5376 x 2688`**, single frame [frame_013].
12. **Understand the matching idea before doing it.** Both plate and HDRI contain the same grey patch; sample it in each, and if the RGB values differ, find the per-channel multiplier that makes the HDRI's match the plate's — then apply that multiply to the whole HDRI [frame_014, frame_001, transcript 5:31-5:58].
13. **Sample the plate's grey patch.** Zoom the viewer onto the chart and hold **`Cmd`/`Ctrl` + `Shift`** while clicking. Readout here: **`R 0.28380  G 0.28646  B 0.28787`** [frame_015].
14. **Record the values in a Sticky Note node.** The note reads `.283 .286 .287` [frame_016, frame_017].
15. **Sample the same patch in the HDRI:** **`R 0.44314  G 0.44718  B 0.50698`** — visibly different, and bluer [frame_017].
16. **Add a Multiply node under the HDRI Read** and expand it to per-channel RGB controls, then drive red, green and blue until the HDRI's patch reads the plate's values [frame_017, transcript 6:29-6:46]. The resulting factors are the workflow graphic's **`0.64 / 0.64 / 0.55`** [frame_001]. Without a chart, sample a neutral surface such as the concrete instead [transcript 6:46-6:52].
17. **Verify by sampling somewhere else entirely** — a patch of sky should now read the same in plate and HDRI [transcript 6:52-7:02]. [no frame: the confirming sample is narrated over a viewer the recording does not hold still; the matched end-state is shown in the workflow graphic's right-hand columns, frame_001]
18. **Do not grade with anything non-linear at this stage.** A `Grade` node's **gamma** bends a linear ramp into a curve — the waveform shows it, and the video labels it **"BAD"** [frame_018]. Stick to multiply-type operations (gain), and apply anything you do to *both* plate and HDRI [transcript 7:02-7:27].
19. **Set the plate as the Blender camera background with its IDT.** Camera Data ▸ **Background Images** ▸ Movie Clip `P1077030.MP4`, **Color Space `Input - Panasonic - V-Log - V-Gamut`**, Opacity `0.967`, Depth Back, Frame Method Stretch [frame_019]. Blender must already be configured for ACES [transcript 7:36-7:41].
20. **Load the HDRI into the world with its IDT.** Shader Editor ▸ World: `Texture Coordinate → Mapping` (Point, Rotation Z `-2.2°`) `→ Environment Texture` (Equirectangular, Single Image, **Color Space `Utility - Linear - sRGB`**) `→ Background` (Strength `1.000`) `→ World Output` [frame_020].
21. **Reproduce the Nuke multiply in the world shader.** Insert a **Mix** node (data type `Color`) between the Environment Texture and the Background, set its blend mode to **Multiply** and **Factor to 1**, and type the R/G/B factors from Nuke into the second colour input [frame_021, transcript 8:10-8:34]. (The captured node is Blender's unified `Mix` with `A`/`B` sockets, caught mid-setup at `Mix` / Factor `0.500`.)
22. **Fix the CG asset's own colour spaces — images.** Open the model on its own and walk every material. Any texture feeding **diffuse / colour / albedo** gets the IDT **`role_matte_paint`** or **`Utility - sRGB - Texture`** (identical in effect) [frame_023, transcript 8:53-9:05].
23. **Fix the CG asset's own colour spaces — data maps.** Anything driving **roughness, metalness, bump, displacement or normal** gets **`role_data`** or **`Utility - Raw`** [frame_024, transcript 9:06-9:17].
24. **Convert raw RGB colour inputs by hand.** Blender will not convert a flat RGB swatch into ACEScg for you, so run the values through **`acescolorspace.com` ▸ Convert RGB** (source and target colourspace pickers, 8-bit in/out options) and paste the result back [frame_025, transcript 9:17-9:34]. Then append the corrected model collection into the main file.
25. **Diagnose the bad sun.** In rendered view the HDRI alone under-lights the scene. The cause is visible in the darkest 360 exposure: the sun is a fat blob with a halo, not a point, because a 360 camera cannot take the filters needed for that low an exposure [frame_026, transcript 9:38-10:09].
26. **Paint the sun out in Photoshop.** Add an **Exposure** adjustment to see it, add an empty layer, set the colour picker's sample mode to *current and below, no adjustments*, then use the **Gradient tool** with a **Radial** type — left stop sampled just outside the flare, right stop sampled further away — dragged from the sun's centre [transcript 10:09-10:44]. [no frame: the gradient-tool colour-stop dialog is on screen only briefly between the captured moments; frame_027 catches the next step on the same 5376x2688 32-bit document]
27. **Mask the patch.** Turn the layer off, take the **Ellipse tool**, set its mode to **Path** (the dropdown offers Shape / Path / Pixels), draw round the sun and hit **Mask**; turn the layer back on, select the mask and raise **Feather** in Properties [frame_027, transcript 10:44-10:59]. Turn the Exposure adjustment off and save a new Radiance file.
28. **Swap the sun-free HDRI into Blender** — the world here is `HDRI_noSun_v01` pointing at `GarageSun_ColCheck_noSun_v01.hdr` [frame_020, transcript 11:07-11:12].
29. **Add a real Sun object and aim it.** Rotate it until the CG shadow direction matches the reference (the captured drag reads **`-51.73°` about global X**). Keep **Angle** low for sharp shadows — here **`0.526°`** — and Strength is eyeballed for now at `4.720` [frame_028, transcript 11:12-11:32].
30. **Bring in an ACEScg ColorChecker EXR** as a measuring instrument: the **`ACEScg - X-Rite ColorChecker Classic 2014`** file from the `colour-science / colour-nuke` repository [frame_029], added with **Images as Planes**. Its material colour space is **`ACES - ACEScg`** (correct, since the EXR already is), roughness set to **`0.8`**, and the plane is positioned at the same place and angle as the real chart [frame_031, transcript 11:35-12:00].
31. **Measure, then set sun strength.** Look through the camera in rendered view, draw a small **render region** around the chart, turn the floor plane off, and render. Right-click-and-hold in the Render Result to sample the grey patch — it reads **`R 0.21864  G 0.22477  B 0.25977`** [frame_030] against the plate's `0.28`. Raise the sun's Strength until it reads about `0.28` [transcript 12:00-12:31].
32. **Project the plate onto the floor plane.** Add a **UV Project** modifier to `Floor - Projection`: UV Map `UVMap`, **Object = Camera**, **Aspect X `16.000` / Y `9.000`** for 16:9 footage [frame_031, frame_032]. Put a **Subdivision Surface** modifier set to **Simple** (Viewport/Render `2`) *before* it so there is enough geometry to project onto [frame_032, transcript 12:41-13:08].
33. **Build the floor material** from the clean plate: Image node `P1077029.MP4` (Movie, **Color Space `Input - Panasonic - V-Log - V-Gamut`**) → **RGB Curves** (point `0.5045 / 0.46250`) for a closer colour match → **Principled BSDF** with roughness raised to **`0.743`** [frame_032]. This projection trick will not always work — sometimes the floor material has to be rebuilt by hand [transcript 13:23-13:33].
34. **Make the floor a shadow catcher.** Object Properties ▸ Visibility ▸ Mask ▸ **Shadow Catcher** [frame_033], and enable the **Shadow Catcher render pass** in the View Layer's Passes tab [transcript 13:33-13:39].
35. **Fix what shows through the car windows.** Duplicate the floor plane as `Floor - Projection.001`, move it into the background, **untick Shadow Catcher** [frame_034], duplicate the projection material (here the slot is named `Windows`), swap the shader for an **Emission** and delete the RGB Curves. Then in Object Properties ▸ Ray Visibility untick everything except **Transmission**, so the plane is only ever seen through glass [frame_034, transcript 13:39-14:05].
36. **Render and save as OpenEXR MultiLayer.** The shadow will not appear in the beauty — it is carried in the Shadow Catcher pass [transcript 14:05-14:19]. [no frame: the output-properties panel is not held on screen; the pass itself is visible as a socket on the resulting EXR in frame_035]
37. **Open a fresh file's Compositor** with Use Nodes on; read the background footage (setting frame settings and the **Panasonic IDT**) and the CG render `charger_sun_v03.exr` with **Color Space `ACES - ACEScg`**. That EXR node exposes `Combined`, `Alpha`, `Noisy Image`, `Noisy Shadow Catcher` and **`Shadow Catcher`**; `Ctrl+Shift+Click` a node repeatedly to cycle what the Viewer shows [frame_035, transcript 14:25-14:51].
38. **Composite the shadow by multiplication.** The Shadow Catcher pass carries both shadow density *and* shadow colour, so a **Mix ▸ Multiply** of the background footage by that pass is the whole operation [frame_036, transcript 14:51-15:09]. The plate node here is `P1077029.MP4`, Movie, `Frames 1000`, `Offset 1000`.
39. **Alpha Over the car.** Background in the top input, CG `Combined` in the bottom [frame_037, transcript 15:09-15:15].
40. **Compare against the reference and make two linear-safe tweaks.** Darken the shadows with a **Gamma** node on the Shadow Catcher branch, raised to **`1.300`** [frame_037, frame_038]; pull the car off magenta with a **Color Balance** node (Correction Formula **Lift/Gamma/Gain**) adjusting **Gain**; and cool the shadows with a second Color Balance using **only Gamma**, not Gain [frame_038, transcript 15:15-15:48].
41. **Render the comp** into the `Composite` node, Output Type **OpenEXR**, then Render Animation [transcript 15:48-15:59]. [no frame: the output-properties panel for this render is not held on screen; the resulting file `garageSun_comp_acesCG_final_v02.exr` appears on the Resolve timeline in frame_040]
42. **Grade in Resolve.** Project Settings ▸ **Color Management** ▸ Color science → **`ACEScc`** (the dropdown also offers DaVinci YRGB, DaVinci YRGB Color Managed and ACEScct), with the **Output Transform** set to `sRGB` [frame_039]. Import the EXR, right-click it ▸ **ACES Input Transform ▸ ACEScg** — that is its IDT [transcript 16:13-16:25].
43. **Grade and deliver.** Colour-grade on the Color page, then Deliver: Format **QuickTime**, Codec **H.264**, `1920 x 1080` at `24` fps, and render [frame_040, transcript 16:25-16:34].
44. **The homework.** Redo the shot with the car in the shade — there the sun is not visible, so the HDRI sun-replacement step can be skipped entirely [transcript 16:38-16:47]. [no frame: closing remark over B-roll of the shaded shot, no UI]

### Nodes / Settings
- **Acquisition** — Panasonic Lumix GH5, **V-Log** profile, fixed white balance [frame_002]; X-Rite **ColorChecker Classic** shot in the plate [frame_003] and left in place for the 360 brackets [frame_004]
- **HDRI merge** — Photoshop `File ▸ Automate ▸ Merge to HDR Pro` [frame_005], **"Attempt to Automatically Align Source Images" off**, saved as Radiance `.hdr` [frame_006]; result `5376 x 2688`, 32-bit [frame_013, frame_027]
- **Colour spaces in play** — plate: **V-Gamut / non-linear V-Log**; HDRI: **sRGB / linear scene-referred**; both → **ACEScg / linear scene-referred** [frame_008, frame_001]
- **Nuke** — 13.2v5, Project Settings ▸ Color ▸ `OCIO`, config **`aces_1.2`** [frame_009, frame_016]
- **Plate IDT** — `Input ▸ Panasonic ▸` **`Input - Panasonic - V-Log - V-Gamut`** [frame_010]
- **HDRI IDT** — `Utility ▸` **`Utility - Linear - sRGB`** [frame_013]
- **IDT verification rig** — one Read → three `FrameHold` nodes (`-2` / `0` / `+2`, frames 1200 / 81 / 490) + an `Exposure` node set to *stops* [frame_011, frame_012]
- **Sampling** — `Cmd`/`Ctrl` + `Shift` + click in the Nuke viewer; values recorded in a `StickyNote` node [frame_015, frame_016]
- **The measurement** — plate grey `0.28380 / 0.28646 / 0.28787` [frame_015]; HDRI grey `0.44314 / 0.44718 / 0.50698` [frame_017]; multipliers **`0.64 / 0.64 / 0.55`** [frame_001]
- **Linear-safe grading only** — multiply/gain yes, **gamma no** (a `Grade` gamma of `.5` bends the ramp; waveform + "BAD") [frame_018]
- **Blender camera background** — Background Images ▸ Movie Clip, Color Space = the plate IDT, Opacity `0.967`, Frame Method Stretch [frame_019]
- **Blender world** — `Texture Coordinate → Mapping` (Rotation Z `-2.2°`) `→ Environment Texture` (`Utility - Linear - sRGB`, Equirectangular) `→ Mix (Multiply, Factor 1)` `→ Background (1.000) → World Output` [frame_020, frame_021]
- **Asset colour spaces** — albedo/diffuse/colour → **`role_matte_paint`** or `Utility - sRGB - Texture`; roughness/metal/bump/displacement/normal → **`role_data`** or `Utility - Raw`; flat RGB values → converted at **`acescolorspace.com`** [frame_023, frame_024, frame_025]
- **The CG asset** — BlendSwap **Dodge Challenger 1970 R/T** by *ziwerliz*, Blender 2.9x, Cycles, **CC-0**, 87.4 MB; 118 objects, 990,147 verts [frame_022, frame_023]
- **Sun light** — type `Sun`, Strength `4.720` (then measured up), **Angle `0.526°`** for sharp shadows, Max Bounces `1024`; aimed by rotation (`-51.73°` about global X in the captured drag) [frame_028]
- **The measuring chart** — `ACEScg - X-Rite ColorChecker Classic 2014` EXR from the `colour-science/colour-nuke` repo [frame_029], added via **Images as Planes**, material colour space `ACES - ACEScg`, roughness `0.8`; object `ACEScg_ColorChecker2014` [frame_031]
- **Measured render sample** — `R 0.21864  G 0.22477  B 0.25977` versus the plate's `0.28` target [frame_030]
- **Floor projection** — `Subdivision` (**Simple**, `2`/`2`) *then* `UV Project` (Object = **Camera**, **Aspect `16` / `9`**) [frame_032]; material = clean plate `P1077029.MP4` → `RGB Curves` (`0.5045 / 0.46250`) → Principled BSDF, Roughness `0.743` [frame_032]
- **Shadow catching** — Object ▸ Visibility ▸ Mask ▸ **Shadow Catcher** on the floor [frame_033], plus the **Shadow Catcher render pass**
- **Windows plane** — duplicate floor, Shadow Catcher **off**, Emission shader, Ray Visibility reduced to **Transmission only** [frame_034]
- **Compositor inputs** — `charger_sun_v03.exr`, Layer `ViewLayer`, Color Space `ACES - ACEScg`, outputs `Combined / Alpha / Noisy Image / Noisy Shadow Catcher / Shadow Catcher` [frame_035]; plate node `P1077029.MP4`, Movie, `Frames 1000`, `Offset 1000` [frame_036]
- **`Ctrl + Shift + Click`** — cycle the Viewer through nodes [frame_035]
- **Comp graph** — plate `× Shadow Catcher` via Mix ▸ Multiply (`Fac 1.000`) → `Alpha Over` with the CG Combined below [frame_036, frame_037]
- **Comp tweaks** — `Gamma` node at **`1.300`** on the shadow branch; `Color Balance` (Lift/Gamma/Gain) on **Gain** to remove magenta from the car, and a second on **Gamma only** to cool the shadows [frame_038]
- **Grade & deliver** — DaVinci Resolve 17, Color science **`ACEScc`**, Output Transform `sRGB` [frame_039]; clip IDT `ACEScg`; Deliver QuickTime / **H.264** / `1920 x 1080` / `24` fps [frame_040]

### Difficulty
Advanced

### Blender Version
**No version string is visible in any captured frame.** The evidence dates it to **Blender 3.4 or newer**: the unified **`Mix`** node with `A`/`B` sockets (replacing `MixRGB`, introduced in 3.4) [frame_021], the Cycles **`Shadow Catcher`** compositor pass (3.0+) [frame_035], and the `Geometry Nodes` workspace tab (2.92+) [frame_019]. The on-screen clock reads late January 2023 [frame_027, frame_039], consistent with 3.4.x. Other applications are pinned exactly: **Nuke 13.2v5 (NukeIndie)** [frame_009], **Adobe Photoshop 2023** [frame_005], **DaVinci Resolve 17** [frame_039, frame_040].

### Tags
color-management, aces, vfx, compositing, hdri, lighting, camera-tracking, nuke, davinci-resolve, photoshop, shadow-catcher, cycles, advanced

---

## Related Tutorials
- `add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1.md` — same author; the gamut/gamma theory this workflow assumes you have already watched (named as a prerequisite at transcript 2:30)
- `add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2.md` — same author; the Resolve↔Blender ACES round trip, here replaced by a Nuke-based measurement step
- `composite-cgi-around-real-object---blender-vfx-tutorial-full.md` — same author; the view-layer/holdout/shadow-catcher side of the same compositing practice
- `composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full.md` — same author; render-pass separation for CG behind real transparent objects
