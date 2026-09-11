---
title: Composite CGI Element Behind Real Glass - Blender VFX Tutorial (Full)
source: YouTube
url: https://www.youtube.com/watch?v=qdqV4oortP0
author: InLightVFX
ingested: 2026-09-11
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/
frame_count: 37
frame_status: complete
uncertainty_frames: []
frame_selection: explicit-timestamps (supplied to select_frames.py; NOT evidence that the frames were read -- see `grounding:`)
---

# Composite CGI Element Behind Real Glass - Blender VFX Tutorial (Full)

**Source:** [YouTube](https://www.youtube.com/watch?v=qdqV4oortP0)
**Author:** InLightVFX
**Duration:** 18m53s | 13 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Here's what we're after today. We want to put a CG object behind some real glass object in our video.
[0:06] We'll be working entirely in Blender with a focus on how we can separate and composite the necessary elements to make this look as
[0:14] photorealistic as possible.


### Scene Setup [0:16]
**Transcript (timestamped):**
[0:16] Here's an overview of what we'll cover in this video.
[0:21] First, the obvious steps. Film your footage and then solve your 3D camera in Blender.
[0:27] There are plenty of tutorials on how to do this. Now it's time to recreate our real-world scene in 3D.
[0:33] This means matching the geometry, lighting, and textures. For the geometry of this shot,
[0:38] I'll make a plane for where our objects sit.
[0:41] Then I'm going to model the glass and place it in our scene as closely as possible.
[0:45] Play through the shot to make sure that everything tracks well and that your objects don't slip out of alignment.
[0:50] If there are some alignment issues, make sure your CG object is resting on the plane and not floating above somewhere.
[0:57] If it still looks bad, your camera track might be off. For lighting, I created a 368 degree HDRI with my Ryko Theta V.
[1:05] Otherwise, add lights in your scene to match the light intensity, color, and shadow quality correctly.
[1:11] For textures, you'll want to recreate the table surface. In my case,
[1:15] I used a simple BSDF shader, changed the color, and dialed in the roughness to match as closely as possible. For the glass,
[1:22] I used a principled glass shader, turned down the roughness some, and used a noise texture in the normal input.
[1:28] I tweaked this in rendered view until my HDRI background was being distorted similarly to the original footage.
[1:34] Finally, add in your CG object of choice. In my scene, it's this awesome keyboard model from BlendSwap.com.
[1:42] Okay, let's talk about how to set all of this up for rendering using the Cycles engine.
[1:47] Make sure your background is set to transparent, hit render, and you'll get this.
[1:51] A fully CG shot, which is not exactly what we're after. So how do we extract just our CG object, shadows,
[1:58] refractions, and reflections? Well, we can control the visibility of these different elements within three areas in Blender Cycles.
[2:06] That is object visibility,
[2:09] collection visibility, and view layer visibility, known as render passes. Now these three levels of control,
[2:16] objects, collections, and view layers, they get pretty complicated when you add them all together.
[2:20] And it's often at this point in a tutorial when you'll hear someone say,
[2:24] If it sounds confusing, you don't have to worry about it as long as you just choose those two passes there,
[2:28] and then we're ready to jump into our render settings here. I understand why people often gloss over this part.
[2:35] It's really complicated, and it really takes a long time to explain. To compromise,
[2:40] I made an infographic, which you can find linked in the description.
[2:44] It should help you understand how objects,
[2:46] collections, and view layers work together to give you control over different visibility options in Cycles.
[2:53] Let's start to use these three levels of control to break up our scene.


### View Layer [2:57]
**Transcript (timestamped):**
[2:57] We are going to take our current view layer and use it to render out just our CG object.
[3:02] So we will name the view layer Main Object. Now within this view layer,
[3:05] we want to control the visibility of our main CG keyboard object, our table, and our glass.
[3:11] So we'll place them all in their own collections.
[3:14] Select each object, press M, hit New Collection.
[3:19] So I end up with four collections, one for my scene camera and any lights, one for my main object, the keyboard,
[3:26] one for my table, and one for my glass. Now if we right-click a collection and go to View Layer,
[3:32] we can set the visibility of the collection and all the objects that are inside it.
[3:37] You'll see in my infographic there is a section about these collection visibility settings. For our purposes,
[3:43] we want to set the glass collection to hold out, which will mask out wherever our glass is.
[3:48] Then we'll set the table collection as indirect, meaning it will show indirectly in our keyboard.
[3:54] Now if we hit render, we have just our main object without any part of it that goes behind the glass.


### Shadow Layer [4:00]
**Transcript (timestamped):**
[4:01] Main Object View Layer completed. Let's create another view layer and name it Shadow.
[4:05] You'll see we have the same collections in this layer as before. All view layers share the same collections.
[4:11] Now we want to extract just the shadows cast by the keyboard onto the table.
[4:16] We'll go to our table object and in the properties tab under visibility, we'll make it a shadow catcher.
[4:21] This is part of the object visibility control I was talking about. Again, we want our glass to mask out the shadow,
[4:28] so we'll set that collection to hold out. Now even though our glass is set to hold out, it will still cast a shadow.
[4:34] So I'm going to go to my glass object visibility settings and disable shadow.
[4:39] I'll also disable diffuse and glossy while I'm here. Now my glass object will not show up in any shadows,
[4:46] diffuse surfaces, or glossy reflection surfaces, which is good because our real glass already shows up in those ways.
[4:52] Finally, we'll set our main object collection to indirect only, so we only see the shadows it makes. Now shadows are done.
[4:59] We have just the shadows masked out by the glass. Shadow View Layer completed.


### Reflections Layer [5:02]
**Transcript (timestamped):**
[5:05] Let's create yet another view layer and name this one reflections. In this view layer,
[5:10] we'll capture the reflections of our CG object on the table surface. To start,
[5:14] we are going to duplicate the table collection we have, right-click, duplicate collection, and turn the original one off.
[5:21] We're doing this because the original table object is now set to a shadow catcher, and we don't want to change that.
[5:28] So now in this duplicate collection, we'll also have created a duplicated table object.
[5:33] We'll go back into the object visibility tab and disable the shadow catcher so that it shows up normally.
[5:39] Now we'll set our main object and glass collections to set holdout, and
[5:44] in our render view,
[5:45] we should see nothing but the table with shadows and reflections on it. To get just the reflections of the keyboard in the table,
[5:52] we'll enable certain render passes for this view layer.
[5:55] Remember, this is our third level of controlling what we see in our scene. In the render passes tab,


### Glossy Indirect [5:56]
**Transcript (timestamped):**
[6:00] let's enable the glossy indirect pass. So why did we choose this? Allow me to illustrate.
[6:06] The light rays which show the reflection of our keyboard in our table are the rays that leave our light source,
[6:13] bounce off our keyboard, bounce off the table, and into the camera. These particular light rays would be labeled glossy light rays,
[6:21] since the last surface they interact with before hitting the camera is a partially glossy or reflective surface.
[6:28] And since our light rays bounce more than once, we choose indirect. Altogether, we get glossy indirect.
[6:35] See this section of the infographic linked in the description for more information.
[6:40] Now if we enable render single layer, and we render this view layer alone, in the render view window,
[6:45] we can then toggle down and view what this glossy indirect render pass looks like.
[6:51] Note, in Blender 2.81 and above,
[6:54] you can view different render passes in the viewport by going into rendered view and toggling this menu to view different passes.
[7:02] Since we're done setting up this view layer, we'll uncheck render single layer in the view layer tab. Reflections view layer, check.


### Reflections View Layer [7:07]
**Transcript (timestamped):**
[7:09] Let's create another view layer and name it object through glass.
[7:13] Now in this view layer, we want our keyboard and glass collection to be fully visible like they are by default.
[7:19] We'll disable that duplicate table collection we made. To get just the keyboard showing through our glass,
[7:25] we'll again enable certain render passes for this view layer.
[7:28] So let's go to the render passes tab, and we'll enable the transmission indirect pass. In the viewport,
[7:34] I can see what this looks like. So why did we choose this?
[7:38] Well, we want to extract just the light rays in our scene that leave our light source,
[7:42] bounce off our keyboard, go through our glass object, and into the camera.
[7:47] These particular light rays would be labeled transmission light rays, since the last surface they interact with before hitting the camera is this
[7:55] transparent transmitting glass surface. And we chose indirect since these light rays bounce more than once.
[8:03] Altogether, we get transmission indirect.
[8:06] In addition, we'll enable the glossy indirect pass, which looks like this. I'll mention why we're doing that later.
[8:13] Now looking at our transmission indirect pass, there's one problem.
[8:17] We're seeing our HDRI environment reflecting throughout the glass. If you're not using an HDRI,
[8:23] you still might be seeing the gray of your world shader throughout the glass.
[8:28] To solve this, in the world shader editor,
[8:30] we can add a light path node and add an invert to the isGlossy array and plug this into the strength of the background.
[8:38] Now you'll see we no longer have the HDRI background showing in our transmission indirect pass.
[8:44] So when we render out this object through glass view layer, we'll have these nodes connected to have this effect.
[8:50] But for the other view layers we've already made, we'll disconnect this so that the HDRI behaves like normal.


### Glass Mask View Layer [8:57]
**Transcript (timestamped):**
[8:57] Object through glass, view layer, check.
[9:00] Finally, I'm going to add just one more view layer. Name this one glass mask.
[9:05] Just follow what I'm doing and I'll explain why later.
[9:08] In this layer, we're going to duplicate our main object collection, turn the original one off.
[9:14] For this duplicated object, we'll set all the materials to a default emission shader.
[9:19] We'll duplicate the table collection, turn off the other two ones we have,
[9:25] make sure the shadow catcher is disabled, and assign the table the same emission shader.
[9:31] In our render passes tab, we will again enable the transmission indirect and glossy indirect passes.
[9:37] And here's what the transmission indirect pass looks like.
[9:41] This render pass will serve as our black and white mask when we're compositing in the glass.
[9:46] Note, for this view layer, we will also want to have that world shader limitation hooked up.


### Render Passes [9:51]
**Transcript (timestamped):**
[9:52] Glass mask view layer completed.
[9:54] Now we have our five view layers set up.
[9:59] Since all view layers share the same collections, and we added more collections as we went,
[10:04] we'll have to go back through our earlier view layers and completely disable the unneeded collections from those layers.
[10:11] Just unclick the box to completely disable a collection.
[10:18] Also to review, as far as render passes go, our main object view layer will output the combined and Z pass,
[10:25] which are enabled by default, which we want. This is good.
[10:28] The same for our shadow layer.
[10:30] Our reflection layer will also output the glossy indirect pass we enabled.
[10:34] Our object through glass layer will output the default passes, in addition to the transmission indirect pass,
[10:41] and glossy indirect pass we enabled.
[10:43] And our glass mask layer will output the same.
[10:46] Now we have to render out our first three layers on their own, since we need the world shader enabled as normal.
[10:52] We'll disable the last two layers by unchecking Use for Render.
[10:57] Then hit render.
[11:00] Save out this image somewhere as an OpenEXR multilayer file.
[11:04] Then only enable the two last few layers we made, hook up that light path node in our world shader,
[11:11] render, and save another OpenEXR multilayer file.


### compositor [11:16]
**Transcript (timestamped):**
[11:18] Now we'll head over to our compositor tab to start combining these different elements together.
[11:23] Make sure Use Nodes and Backdrop are on.
[11:27] I'm going to delete everything here to show you how we'd start from scratch.
[11:31] Create a Viewer node and Composite Output node.
[11:34] We'll add an Image input node and bring in the image sequence for our background footage.
[11:40] Let's distort this to match the render size.
[11:43] Hold Ctrl Shift and click to view a node.
[11:47] Next we'll add another Image input node.
[11:49] We'll open our first EXR file.
[11:52] We can see that we can switch between each of the first three view layers here.
[11:57] Based on the view layer selected, we have different output connections representing the render passes we enabled.


### master equation [12:04]
**Transcript (timestamped):**
[12:04] So how do we composite all these different render passes into our scene?
[12:08] Well, Blender Cycles has this master equation that is used, which tells us how to reconstruct an image if you render out all the passes.
[12:17] We'll see in this equation that most of the time we are simply adding the light passes together.
[12:22] That is, using a color mix node set to add.
[12:26] Only with color passes do we multiply the previous nodes.
[12:30] Then all this is added together again to get the final combined pass.
[12:35] And remember, this combined pass is what we output by default.
[12:39] So when we enable certain render passes, we're selecting specific ingredients of this combined pass.
[12:46] In summary, this add and multiply node are the main ones we'll use when compositing.
[12:51] You'll also commonly use an alpha over node when compositing in a combined pass, like our main object, which has a clear alpha channel.


### compositing [12:59]
**Transcript (timestamped):**
[12:59] We'll start by adding in some shadows.
[13:01] There are lots of ways to composite shadows.
[13:04] I'll add a color mix node set to multiply, drop the alpha into the factor slot, set the top color to white, and bottom color to black.
[13:12] This will give us a fully black and white image.
[13:14] Let's add a color ramp to adjust the range of black and white we want.
[13:18] Link in an RGB curves to add any needed color or brightness or darkness to the shadows.
[13:23] Then we'll add a color mix node set to multiply, and multiply our background image by the shadows output.
[13:29] Boom! Shadows done.
[13:32] Next, we'll add our main object on top of the shadows.
[13:35] Duplicate our previous image input node, and select the main object view layer.
[13:41] Then we'll simply use an alpha over node to composite it on top of the background and shadow.
[13:51] Next, let's add the object showing through the glass.
[13:54] Add an image input node and open up that second EXR file we rendered out.
[13:59] Select the object through glass view layer.
[14:02] Remember, we want to work with the transmission indirect render pass we created.
[14:07] Now, how do we put this on top of what we have already?
[14:10] Well, maybe we use a color mix node, set it to add, and try to add it in.
[14:15] No, that doesn't look quite right.
[14:19] What about an alpha over node?
[14:23] That doesn't do much, since our transmission indirect pass has that black background baked in with no alpha.
[14:30] We could try to key out the black background with the luma key node,
[14:34] but those results look pretty bad.
[14:37] What would be ideal would be to have some sort of black and white mask
[14:41] that shows us exactly where our CG object shows through our glass, and masks out everything else.
[14:47] Well, you'll remember that we made this, so let's use it.
[14:51] We'll duplicate our image input node and switch to the glass mask layer we created.
[14:55] Let's add a color ramp to make sure we crush the black and white values enough.
[14:59] We'll put this mask as the factor input node, and then add a color mix node.
[15:04] We'll duplicate the factor input in our alpha over node.
[15:07] Our image we've composited so far will be the first input,
[15:10] and the object through glass will go into the second input, taking from the transmission indirect output.
[15:17] Phew! Good job.
[15:19] Take a deep breath, and let's continue.
[15:23] Now, let's put in the reflection.
[15:25] Duplicate our image input node, select the reflection view layer.
[15:29] Now, how do we composite this in?
[15:32] In our equation here, we usually add the glossy indirect pass.
[15:36] So we'll try that, and it seems to look good.
[15:39] And yes, this is the correct choice.
[15:41] And if you want more glossiness than this gives you, duplicate the add node like this.
[15:47] Now, there's one final element that I added in to help sell the total effect.
[15:52] And that comes back to the glossy indirect pass that we created with our object through glass view layer.
[15:58] So let's duplicate that previous node, and we'll add in the glossy indirect information.
[16:03] Again, using our black and white mask in the factor input.
[16:10] And to tone this down, I'll add another color mix node set to multiply and pick a gray value that looks good.
[16:22] Now, we have a composite that looks awesome.
[16:25] Feel free to add in notes to tweak sharpness and to work with color to improve the overall realism.
[16:34] And to render out the final sequence, select use for render for our first three view layers only.
[16:40] Make sure our HDRI is correct.
[16:42] And in the compositor, we'll have to make sure our composite node has a render layers node going into it.
[16:48] This is because whatever is hooked up into this composite node is what is saved out when we hit render animation.
[16:55] And we want to save out our render layers.
[16:58] Set an output for the correct frame range and select open EXR multilayer sequence.
[17:03] Let that render out by hitting render animation.
[17:07] Then we'll turn off these first three layers and only render out our object through glass and glass mask view layers.
[17:14] Make sure to change that HDRI and render out another open EXR multilayer sequence to a different location.
[17:21] Now in the compositor, everywhere we have those image input nodes, we'll switch out our new open EXR sequences instead of just those single frames.
[17:33] In the same way, we can select the correct view layer and replace the connections for each node.
[17:44] Now that this is all said and done, we're ready to make a final render.
[17:54] Make sure the final composite is hooked up to the composite node, set an output type of PNG, hit render animation, and this should go pretty fast.
[18:03] Outputting final PNGs of the entire composite we made.


### outro [18:06]
**Transcript (timestamped):**
[18:07] So there you have it. Thank you for following along.
[18:10] Congratulations if you made it this far.
[18:12] If you'd like, you can download the Blender project file over at my Patreon linked in the description.
[18:19] These tutorials take a while to put together and I hope to do a lot more.
[18:23] And so I'd be honored to have your financial support in doing that.
[18:26] More than that, if you like this tutorial, please give it a like, share it with your friends, subscribe for when more do come out.
[18:34] And until then, bye bye.
[18:36] I am holding my phone with a sock over it so that you can have impeccable audio for this tutorial. You are welcome.



---

## Captured Frames

- [0:02] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_000.jpg — goal cg behind real glass
- [0:42] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_001.jpg — model glass and plane
- [1:24] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_002.jpg — principled glass noise normal
- [1:37] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_003.jpg — blendswap keyboard model
- [1:49] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_004.jpg — full cg render problem
- [2:45] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_005.jpg — visibility infographic
- [3:23] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_006.jpg — four collections outliner
- [3:45] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_007.jpg — glass collection holdout
- [3:51] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_008.jpg — table indirect only
- [3:57] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_009.jpg — main object layer render
- [4:18] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_010.jpg — table shadow catcher
- [4:41] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_011.jpg — glass disable shadow diffuse glossy
- [4:57] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_012.jpg — shadow layer result
- [5:17] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_013.jpg — duplicate table collection
- [5:41] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_014.jpg — main glass holdout reflections layer
- [6:02] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_015.jpg — enable glossy indirect pass
- [6:16] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_016.jpg — glossy ray path diagram
- [6:48] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_017.jpg — viewport pass toggle glossy
- [7:31] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_018.jpg — enable transmission indirect
- [7:46] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_019.jpg — transmission ray path diagram
- [8:19] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_020.jpg — hdri through glass problem
- [8:35] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_021.jpg — light path isglossy invert background
- [9:17] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_022.jpg — emission shader duplicated objects
- [9:39] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_023.jpg — glass mask transmission pass
- [10:13] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_024.jpg — disable unneeded collections
- [10:55] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_025.jpg — use for render exr save
- [12:11] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_026.jpg — cycles master equation
- [13:08] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_027.jpg — shadow multiply white black
- [13:22] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_028.jpg — colorramp rgbcurves shadow
- [13:45] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_029.jpg — alpha over main object
- [14:33] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_030.jpg — luma key attempt bad
- [14:57] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_031.jpg — glass mask colorramp crush
- [15:11] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_032.jpg — mix mask factor through glass
- [15:37] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_033.jpg — add glossy indirect reflection
- [16:05] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_034.jpg — glossy through glass masked
- [16:23] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_035.jpg — final composite look
- [18:03] tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/frame_036.jpg — final png output

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
