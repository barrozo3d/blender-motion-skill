---
title: Finally! A VFX Workflow With Less Guesswork
source: YouTube
url: https://www.youtube.com/watch?v=G2SacOKhJto
author: InLightVFX
ingested: 2026-09-11
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/finally-a-vfx-workflow-with-less-guesswork/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: []
---

# Finally! A VFX Workflow With Less Guesswork

**Source:** [YouTube](https://www.youtube.com/watch?v=G2SacOKhJto)
**Author:** InLightVFX
**Duration:** 17m12s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py finally-a-vfx-workflow-with-less-guesswork <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Blender Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
