---
title: Composite CGI Around Real Object - Blender VFX Tutorial (FULL)
source: YouTube
url: https://www.youtube.com/watch?v=fnAGtXMkRMY
author: InLightVFX
ingested: 2026-09-11
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: []
---

# Composite CGI Around Real Object - Blender VFX Tutorial (FULL)

**Source:** [YouTube](https://www.youtube.com/watch?v=fnAGtXMkRMY)
**Author:** InLightVFX
**Duration:** 17m29s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py composite-cgi-around-real-object---blender-vfx-tutorial-full <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Here's what we're after today. We want to have a CG object go around a real object in our video.
[0:05] We'll be working entirely in Blender focusing on different compositing techniques to get our ring around the pot and leaves as well as adding in the
[0:12] reflections and shadows for the complete look.
[0:15] Let's begin. Here's an overview of this video and what we'll cover. First, the obvious steps. Film your footage and solve your 3D camera.
[0:22] There are plenty of tutorials on how to do this. Now it's time to recreate our real-world scene in 3D.
[0:27] This means matching the geometry, lighting, and textures. For the geometry of this shot,


### Initial Scene Setup [0:30]
**Transcript (timestamped):**
[0:32] I'm going to recreate the box and pot since those elements will closely interact with the CG objects
[0:38] I'm going to add. And for the actual plant leaves, I warp some plain objects roughly into place.
[0:43] This doesn't have to be perfect and you'll see why later.
[0:46] Play through the shot to make sure that everything tracks well and that your objects don't slip out of alignment. For small tweaks in alignment,
[0:52] I sometimes cheat by animating the object's position or shape keys over the course of the shot. For lighting,
[0:58] I created a 360 degree HDRI with my Ricoh Theta V.
[1:02] This is how I was able to get accurate reflections in my CG object.
[1:07] Otherwise, add lights into your scene to match the light intensity, color, and shadow quality correctly. For textures,
[1:13] I used a simple BSDF shader for both the box and pot.
[1:18] Just adjust the color and roughness settings and that should get you close enough for our needs.
[1:22] I then used this picture I took of the top of the plant for the leaf texture. Finally, add in your CG object of choice.
[1:28] I added these rings. Okay, now let's talk about how to set this all up for rendering using the Cycles render engine.
[1:35] If we hit render as is, we get this, which isn't what we're after.
[1:38] We don't want our CG leaves, pot, or box to be there,
[1:42] but we do want to keep the shadows and reflections. And the ring should go behind the pot and leaves.


### Into to object, collection, view layer visibility [1:47]
**Transcript (timestamped):**
[1:47] So how do we extract and control these different elements?
[1:50] Well, we can control the visibility of these different elements within three areas in Blender Cycles.
[1:55] Object visibility, collection visibility, and view layers visibility, known as render passes. These three levels of control,
[2:03] objects, collections, and view layers get pretty complicated.
[2:06] So I made an infographic which you can find linked in the description.
[2:09] It should help you understand how objects, collections, and view layers work together to give you control over different visibility options in cycles.
[2:18] So let's start to use these three levels of control to break up our scene.


### Scene setup to render necessary elements [2:22]
**Transcript (timestamped):**
[2:22] We are going to take our current view layer and name it main objects, as we'll use it to isolate the ring objects.
[2:28] Within this view layer, we want individual control over our rings, our pot, and our box and leaves.
[2:34] We'll place them all in their own collections. To do so, select one or more objects, press M, hit new collection.
[2:41] So I end up with four collections, one for my scene camera and any lights, one for my main ring objects,
[2:47] one for my pot, and one for my box and leaves. Now if we right-click a collection and go to view layer,
[2:52] we can set the visibility of the collection and all the objects that are inside it.
[2:56] This setting is specific to the current view layer that we are in. We can set this differently for different view layers.
[3:02] You'll see in my infographic there is a section about collection visibility settings. The important setting that will help us today is holdout.
[3:09] Let's set the pot collection to holdout, and we'll see that this does exactly what we want.
[3:14] The holdout setting takes all the objects in a collection and causes them to mask or paint out any other objects that fall behind them from the camera's perspective.
[3:24] So when our ring goes behind the CG pot, it doesn't show up, but it still shows up in front. Perfect!
[3:30] We'll set our box slash leaf collection to indirect only. This will allow us to see the reflections of these objects in our ring, but not the objects themselves.
[3:39] Make sure your background is set to transparent, and if we hit render, we have the ring object that goes behind our pot and shows the reflections of our leaves and box.
[3:48] Main object view layer completed. Let's create another view layer and name it shadow.
[3:53] We want to extract just the shadows cast by our ring onto our leaves, pot, and box. So let's change some object visibility settings to do this.
[4:02] So we'll set our leaves and box to be shadow catchers, and we'll also uncheck shadow for all of them, so that these objects don't cast any shadows, but only catch them.
[4:12] An object with shadow catcher enabled will still show up in other objects' reflections.
[4:17] So just to show you, since we enabled the leaves to be a shadow catcher, if we switch back to our main object view layer, we'll see that the leaves are still set to shadow catcher here,
[4:27] which is okay, since the shadow catchers still show up in reflections. Changing object visibility settings in one view layer will change it in every other view layer as well.
[4:37] Finally, back in the shadow view layer, we'll create a duplicate of our pot collection. Turn off the original collection, and for these duplicated objects, we'll set them to be shadow catchers as well.
[4:48] If we switch back to our main object view layer, we'll see that this pot shadow collection shows up here as well.
[4:55] This is because all view layers share the same collections. So we'll simply disable it in the main object view layer.
[5:02] Finally, we'll set the ring collection to be indirect only.
[5:05] Now shadows are done. We have just the shadows cast by our rings. Shadow view layer completed.
[5:11] Now we'll create our third and final view layer and name it glossy slash diffuse. We'll turn off that pot shadow collection we made.
[5:18] In this view layer, we want to extract any light information that the ring casts onto our pot.
[5:23] So how do we extract this light information? Well, hold with me as I explain an important concept first.
[5:31] You see, our pot is neither totally smooth nor totally rough. This goes for almost all objects in the real world.
[5:38] When we set up the texture, we set the roughness at 0.15, meaning it's still on the smooth side, but has a small amount of roughness.
[5:46] Blender has a way of defining rough surfaces. They are labeled diffuse surfaces.
[5:50] Blender also has a way to define smooth reflective surfaces. They are labeled glossy surfaces.
[5:56] So our pot here is both a diffuse surface and a glossy surface. Some people might say it has both a diffuse component and a glossy component.
[6:04] So in our scene, the light rays that show our ring in the pot surface are those that leave the light source, bounce off our ring, off the pot, and then into the camera for us to see them.
[6:16] Light rays are labeled by the type of surface they bounce off last before hitting the camera.
[6:20] Since our pot is both a diffuse surface and a glossy surface, Blender separately labels some light rays as diffuse and some as glossy.
[6:29] We want to include both in our composite for maximum realism. Remember, Blender allows us to extract this light information using render passes, this being the third level of controlling what we see in our scene.
[6:41] So for this view layer, we will go to render passes tab and enable the diffuse indirect pass and the glossy indirect pass.
[6:49] Now, why did we choose the indirect option instead of direct?
[6:52] Well, these particular light rays bounce more than once in our scene, so they get the label indirect, hence diffuse indirect and glossy indirect.
[7:01] In Blender 2.8 and above, we can view what these passes look like right in our viewport by going into rendered view, hitting this drop down arrow, and selecting our desired pass.
[7:10] So here we can see what the glossy indirect pass looks like. We only want the ring to show in the reflections, so we'll set the ring collection to indirect only.
[7:19] We'll also notice the base of our pot is reflecting into the top part.
[7:22] We don't want this, since in our real world footage, this light information would already be visible, and we don't want to duplicate it.
[7:30] So I'll go into the object visibility settings for this pot base and deselect glossy.
[7:35] This will prevent the pot base from showing in the glossy surfaces of other objects.
[7:40] Now we can also switch to the diffuse indirect pass to see what that looks like.
[7:44] You can see there's a lot of light information here, and if we left this out, we might sacrifice some realism in our composite.
[7:51] Same thing here, our pot base is bouncing some light onto our main pot, which is light information that is already captured in our footage.
[7:59] So for the pot base object again, in the object visibility settings, we'll disable diffuse, which will prevent the pot base from showing in any other object's diffuse surfaces.
[8:10] Then we'll completely disable our box and leaf collection, as we do not want their contribution in this layer.
[8:16] Finally, in our render passes tab, we're going to enable the color for the diffuse. I'll explain why later.
[8:21] Glossy slash diffuse view layer completed.
[8:24] So we have all our view layers set up.
[8:26] To review, we have the main object view layer with just the default combined and Z pass.
[8:31] Perfect. We have the shadow view layer also with the default passes.
[8:35] Then we have the glossy slash diffuse view layer, which we also included the diffuse indirect, diffuse color and glossy indirect render passes.
[8:42] It's compositing time.


### Compositing time! [8:43]
**Transcript (timestamped):**
[8:47] Let's hit render image. This will render out all our view layers so we can use them in our compositor.
[8:52] Don't worry about the final image this spits out.
[8:54] Now we'll head over to our compositor tab to start combining these different elements together.
[8:59] Make sure use nodes and backdrop are on.
[9:01] I'm going to delete everything here to show you how you'd start from scratch.
[9:05] Create a composite output in viewer output node.
[9:09] We'll add an image input node and bring in the image sequence for our background footage.
[9:14] Hold control plus shift and click to view a node.
[9:18] Let's scale the background to match the render size.
[9:22] Next, let's add a render layers node.
[9:24] You should know that render layer and view layer essentially mean the same thing.
[9:29] You'll see we can use this drop down menu to select our different view layers.
[9:33] Based on the view layer selected, we have different output connections representing the render passes we enabled.
[9:38] Let's start by compositing in some shadows.
[9:41] Select the shadows view layer.
[9:43] Now, some people would just alpha over the shadows, but this doesn't really give you control over them when trying to change the color or brightness.
[9:51] Notice how this curves doesn't really change the shadow at all.
[9:55] So instead, I'll add a color mix node set to multiply.
[9:58] Drop the alpha in the factor slot, set the top color to white and bottom color to black.
[10:03] This will give us a fully black and white image.
[10:05] Let's add a color ramp to adjust the range of black and white we want,
[10:08] link in an RGB curves to add any needed color, brightness or darkness to the shadows,
[10:13] and then we'll add a color mix node set to multiply and multiply our background image by the shadows output.
[10:20] Feel free to go back and adjust the look more to your liking.
[10:23] Boom, shadows done.
[10:25] Now let's composite in the glossy slash diffuse information.
[10:28] We'll duplicate our render layers node, select the glossy slash diffuse view layer we made.
[10:33] How do we composite these different render passes into our scene?
[10:37] Well, Blender Cycles has this master equation which tells us how to reconstruct an image if we render out all the passes.
[10:45] We'll see in this equation that most of the time we are simply adding the light passes together.
[10:50] That is, using a color mix node set to add.
[10:53] Only with color passes do we multiply the previous nodes.
[10:59] Then all this is added together again to get the final combined pass.
[11:03] And remember, this combined pass is what is output by default.
[11:06] So when we choose a specific render pass, we're just breaking out a specific ingredient of that combined pass.
[11:12] Like I've said in the previous video, add and multiply nodes are the main ones we'll use when compositing.
[11:18] You'll also commonly use an alpha over node when compositing in a combined pass like our main object which has a clear alpha channel.
[11:26] Since we were going to use an add node for both the glossy and diffuse passes, it doesn't really matter which order we add them in.
[11:32] 1 plus 2 equals 2 plus 1, that sort of deal.
[11:35] Starting with diffuse, we'll add a color mix node set to multiply to multiply our diffuse indirect with our diffuse color.
[11:42] The diffuse color essentially provides important color information about the pot.
[11:46] And we're multiplying them because that's what the equation says to do.
[11:50] Then we'll add this into our overall composite.
[11:56] For the reflections, we'll simply add them into our image with the same add node.
[12:01] Note, we didn't export the glossy color pass since it's just all white and wouldn't change the composite.
[12:07] Finally, we'll add our main CG ring on top of everything.
[12:10] Duplicate our render layers node and select the main object view layer.
[12:14] Here we'll use a simple alpha over node to put this on top.
[12:17] Now how do we get those dang leaves to show in front of the ring correctly?


### Luma mattes and 2D masking leaves [12:18]
**Transcript (timestamped):**
[12:21] Our 3D pot we modeled served to mask out the ring properly around the pot.
[12:26] Now we could model in place 3D leaves to match exactly to our footage and do the same masking technique.
[12:32] But this is far more work than we want.
[12:35] Remember my lazy leaves?
[12:36] We created those just for reflections and to catch shadows.
[12:39] So instead of a time consuming 3D masking approach for our leaves, we're going to solve this using a 2D mask.
[12:46] I filmed the plant against a white wall exactly for this purpose.
[12:50] So let's go into the mask tab to create a rough mask just around the leaves.
[12:54] Animate it roughly over the course of the shot and we can name this mask leaf mask.
[12:59] There are plenty of masking tutorials, hence why I'm blowing through this.
[13:02] Back in the compositor, we'll duplicate our footage and scale node.
[13:06] We can bring in the mask node and in the drop down menu select our leaf mask.
[13:10] You'll see this is essentially a black and white sequence with white where my mask is.
[13:14] To separate just the leaves from the background, I found that a luma mat or luma key works best.
[13:20] Luminance keys create masks based on differences in brightness or luminance in your image.
[13:27] So we'll create a luminance key node and play with the settings till we have the leaves or wall isolated, only focusing on the area near the leaves.
[13:35] We'll see that the mask output for this has the leaves black and the wall white, meaning only the wall is selected.
[13:41] So we'll add an invert node to switch this.
[13:43] Finally, we can use the mask we created.
[13:46] Add a color mix node set to multiply and multiply the luma key output by the leaf mask output.
[13:51] This will cut out the luma key to our mask shape.
[13:54] Finally, I added a dilate and blur node to tighten up and soften the edges.
[14:01] From here, you'll see there is a mask output which we will now use.
[14:04] Let's add a set alpha node.
[14:06] Plug our new mask into the alpha input and put our original footage into the image input.
[14:12] The result you'll see is just our leaves and a little bit of the pot.
[14:16] Now we'll take this result, add an alpha over node, put our previous composite in the top input and the leaves on the bottom input.
[14:24] Enable that convert pre-mult box.
[14:27] We'll now see that the leaves are covering the ring, but in some places where they shouldn't be.
[14:32] Here you can see it more obviously on this frame.
[14:35] The leaves are in fact on top of everything.


### Z-depth compositing leaves [14:37]
**Transcript (timestamped):**
[14:37] So we need to figure out a way to tell Blender where this 2D mask is in 3D space.
[14:42] To do this, we are going to use z-depth compositing.
[14:45] In Blender, one of the render passes created by default is the z-pass or depth pass.
[14:51] We can take a look at this pass by creating another render layer node.
[14:54] Choose our main object view layer and connect a normalized node to the depth output.
[15:00] This z-pass is a black and white representation of how far different objects are from the camera.
[15:06] Closer objects are nearer to black and farther ones go towards white.
[15:10] Z-depth compositing takes advantage of this distance information
[15:13] in order to composite things at specific distances in our scene.
[15:17] So keep tracking with me here.
[15:19] I'm going to take this depth pass and add a color ramp node.
[15:23] If I move the sliders close together, I can create a dividing line at a specific distance away from the camera.
[15:29] If I move these sliders left or right, I can essentially select the distance at which this divide takes place.
[15:35] I can also add a gamma node and change the value to do this more easily.
[15:40] Now, if I have this mask from our leaves, and I have the z-depth mask I created,
[15:45] I can combine the two by using a color mix node set to multiply.
[15:50] When I multiply the two, anywhere that is black in either of them representing the value 0
[15:56] stays black in the output. Anything times 0 is 0.
[16:00] So where our ring shows black in our z-depth mask, since it's closer to the camera,
[16:05] it makes the leaf mask black.
[16:07] This is perfect since we don't want the leaves to show over that part of the ring.
[16:11] Now we can take this result and use this to update the alpha input of the set alpha node.
[16:17] Finally, we'll want to make sure that these leaves have the shadows we created on top of them.
[16:22] So we can take the shadows we composited before and multiply the output on top of the leaves.
[16:28] Then this all still pipes right into that final alpha over node where we can see our final result.
[16:34] So what we've just done is composited a single frame of our video.
[16:38] We can go back into our main blender view, select a different place on the timeline,
[16:42] and hit render image again to make sure our composite holds up at different points in our video.
[16:47] Once you're ready to render the entire animation in the compositor,
[16:50] make sure you plug in your final result to the composite node,
[16:54] select an output file type of PNG, and hit render animation.
[16:58] Add some final color grading afterwards, and there you go, a final product.
[17:03] You did it. Good work.
[17:04] You can download the blender project file over on my Patreon,
[17:08] and the free cheat sheet is over there as well, all linked in the description.
[17:11] You're not going to want to miss the next tutorial,
[17:13] so thanks for watching, subscribing, and I'll see you next time.



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
