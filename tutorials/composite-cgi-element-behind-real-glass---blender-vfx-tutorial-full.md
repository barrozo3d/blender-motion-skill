---
title: Composite CGI Element Behind Real Glass - Blender VFX Tutorial (Full)
source: YouTube
url: https://www.youtube.com/watch?v=qdqV4oortP0
author: InLightVFX
ingested: 2026-09-11
blender_version: "Blender 2.81.16 -- observed in frame_001, frame_004, frame_015, frame_025"
tags: [compositing, vfx, cycles, render-passes, view-layers, holdout, shadow-catcher, glass, transmission, light-path, camera-tracking, advanced]
extraction_status: complete
frames_dir: tutorials/frames/composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full/
frame_count: 37
frame_status: complete
uncertainty_frames: []
uncited_frames: [9]  # render just launched: transparent-background tile crosses only, no content resolved
grounding: key-steps-anchored (40/40 steps, 2026-09-11)
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
Placing a CG object *behind* a real transparent object in Blender Cycles by rendering **five view layers** — `MainObject`, `Shadow`, `Reflections`, `ObjectThroughGlass` and `GlassMask` — and reassembling them in the compositor. The glass is rebuilt in CG only so it can act as a **Holdout** and as the source of a **Transmission Indirect** pass; the part of the CG object seen through the glass is a separate render pass keyed in by a purpose-built black-and-white mask made from a second, emission-shaded copy of the scene. A **Light Path ▸ Is Glossy Ray → Invert → Background Strength** trick removes the HDRI from the transmission pass so only the CG object shows through the glass.

### Summary
18m53s, **Blender 2.81.16** [frame_001, frame_004, frame_015, frame_025], Cycles, GPU Compute, `512` render samples [frame_004]. A CG mechanical keyboard is composited behind a real drinking glass on a real table: it must be seen *through* the glass with the right refraction, reflect in the table, cast shadow on it, and be masked wherever the glass covers it [frame_000, frame_036]. The plate is a 123-frame image sequence, shot range 0-122 [frame_004, frame_027]; the camera track came in through the **AE2Blend** add-on [frame_001, frame_011].

**Three levels of visibility control** run the whole tutorial — object visibility, collection visibility and view-layer visibility (render passes) — and the author (**Jacob J Holiday** / InLightVFX) supplies a one-page infographic covering all three, linked in the video description [frame_005]. The video deliberately refuses the usual "just tick these two passes" hand-wave and explains the ray labelling instead [transcript 2:20-2:53].

**Why each pass:** a ray is labelled by the **last surface it touches before the camera**, and *indirect* when it bounced more than once. Light → keyboard → table → camera is **glossy indirect** (the table reflection) [frame_016]; light → keyboard → *through the glass* → camera is **transmission indirect** (the object seen through glass) [frame_019].

**Two EXR renders, not one.** The first three layers need the HDRI world behaving normally; the last two need it suppressed, so the shot is rendered twice with `Use for Rendering` toggled and saved as two **OpenEXR MultiLayer** files [frame_025, transcript 10:46-11:14]. In the compositor these arrive as `Image` nodes with a **Layer** dropdown rather than Render Layers nodes [frame_031].

**Compositing order:** plate → shadows (multiplied in as a graded black-and-white matte) [frame_027, frame_028] → main object with Alpha Over [frame_029] → object-through-glass keyed in with the glass mask on an Alpha Over's `Fac` [frame_032] → table reflections added [frame_033] → the through-glass glossy contribution added and toned down with a grey Multiply [frame_034, frame_035].

Transcript note: Whisper renders "360 degree HDRI" as "368 degree" and "Ricoh Theta V" as "Ryko Theta V" at 0:57 — both are ASR slips, not the narration.

### Key Steps
1. **Film the plate and solve the camera.** The track arrives in Blender through the **AE2Blend** add-on panel (Scale `100.00`, Marker 1 / Marker 2, Distance `1.00`, Calculate Scale) [frame_001, frame_011]; timeline runs `1-120` in the viewport file and `0-122` at render [frame_001, frame_004].
2. **Rebuild the set geometry.** A `Plane` (`FloorForGlass`) for the surface and a `Cylinder` modelled into the glass, positioned against the backdrop under "1. Match geometry" — `Scale 0.098` uniform, nudged along global Z to sit on the plane [frame_001]. Scrub the shot; if the CG floats, first check it is resting on the plane, then suspect the camera track [transcript 0:45-0:57].
3. **Match the lighting with a 360° HDRI.** World ▸ Surface `Background`, Color `hdri-1.hdr`, Strength `1.000` [frame_003, frame_021]. Shot on a Ricoh Theta V (the transcript's "368 degree" and "Ryko" are ASR slips) [transcript 0:57-1:11].
4. **Match the table texture** with a plain Principled BSDF — colour changed and roughness dialled to match [transcript 1:11-1:22]. [no frame: the table material is narrated over the viewport, only the glass material is opened on screen — see frame_002]
5. **Build the glass shader.** Principled BSDF with **`Transmission 1.000`**, **`Roughness 0.033`**, `Specular 0.500`, `IOR 1.450`, `Clearcoat Roughness 0.030`, Base Color white [frame_002, frame_024]. For the real glass's surface irregularity, drive the **Normal** input with `Texture Coordinate → Mapping` (Point, Scale Z `0.300`) `→ Noise Texture` (3D, Scale `15.000`, Detail `0.100`, Distortion `0.000`) `→ Normal Map` (World Space, **Strength `0.005`**) [frame_002]. Tweak in rendered view until the HDRI distorts through the CG glass the way it does through the real one [transcript 1:22-1:34].
6. **Add the CG object.** Here a mechanical keyboard model from BlendSwap — `Keyboard.001` under a `KeyboardParent`, 174,831 verts / 155,238 faces [frame_003, frame_006].
7. **Set up Cycles.** Render Properties ▸ Cycles, Feature Set `Supported`, Device **`GPU Compute`**, Path Tracing, Render `512` / Viewport `32` [frame_004]. Set Film ▸ Transparent and render once: everything is CG, which is not what is wanted [transcript 1:47-1:58].
8. **Learn the three levels of control** before touching anything — object visibility, collection visibility, view layers/render passes. The author's infographic maps all three: scene hierarchy with per-view-layer pass checkboxes, the light-pass matrix (diffuse / glossy / transmission / subsurface × direct / indirect / color), collection visibility and object visibility [frame_005, transcript 1:58-2:53].
9. **Sort objects into four collections.** Select each and press **`M` ▸ New Collection**: `Collection` (Camera), `MainObject` (Keyboard.001 + KeyboardParent), `Table`, `Glass`. Scene camera is `Camera.001`; scene units are Imperial [frame_006].
10. **Name the current view layer `MainObject`** — the topbar's view-layer field reads `MainObject` where it read the default `View Layer` before [frame_001, frame_006], and the EXR's layer dropdown later confirms the same spelling [frame_029]. It renders the CG keyboard alone [transcript 2:57-3:05].
11. **Holdout the glass in that layer.** Right-click the `Glass` collection ▸ **View Layer ▸ Set Holdout** — the submenu also carries `Disable from View Layer` (`E`), `Enable in View Layer` (`Alt E`), `Set Indirect Only` and the Clear entries [frame_008]. Note the sibling **Visibility** submenu is a different, non-view-layer control set [frame_007].
12. **Set `Table` to Indirect Only** in the same submenu, so the table shows up indirectly in the keyboard without rendering itself [frame_008, transcript 3:48-3:54]. Rendering now gives the keyboard minus whatever the glass covers [transcript 3:54-4:00].
13. **Add a view layer named `Shadow`.** The same four collections appear, because all view layers share one collection list [frame_010, transcript 4:01-4:11].
14. **Make the table a shadow catcher.** Object Properties ▸ Visibility ▸ **Shadow Catcher** on the `Table` object [frame_010, transcript 4:16-4:21].
15. **Holdout the glass again, then strip its ray visibility.** The glass still casts a shadow while held out, so select it and **uncheck Ray Visibility ▸ Shadow, Diffuse and Glossy** — leaving Camera, Transmission and Volume Scatter on [frame_011, frame_012]. The real glass already contributes those in the plate, so the CG copy must not add them twice [transcript 4:28-4:52].
16. **Set `MainObject` to Indirect Only in this layer**, leaving only the shadow the keyboard throws, with the glass masking it [transcript 4:52-5:00]. [no frame: this click lands on the same collection ▸ View Layer ▸ Set Indirect Only entry captured in frame_008]
17. **Add a view layer named `Reflections`** for the keyboard's reflection in the table surface [frame_013].
18. **Duplicate the table collection.** Right-click ▸ **Duplicate Collection** gives `TableReflection` / `Table.001`; disable the original, because that one is now a shadow catcher and must stay one [frame_013, frame_015, frame_018]. On the duplicate, turn **Shadow Catcher off** so it renders normally [transcript 5:28-5:39].
19. **Holdout `MainObject` and `Glass` in the Reflections layer** — what remains in rendered view is the table carrying shadows and reflections [frame_014, transcript 5:39-5:51].
20. **Enable the Glossy Indirect pass.** View Layer Properties ▸ **Passes**: Data keeps `Combined` + `Z` (Alpha Threshold `0.500`, Cryptomatte Levels `6`), and in the **Light** block click **`Glossy ▸ Indirect`** [frame_015]. The reasoning: the reflection rays go light → keyboard → table → camera, so glossy (last surface is partially reflective) and indirect (more than one bounce) [frame_016, transcript 6:00-6:35].
21. **Preview the pass.** Tick `Render Single Layer`, render, and use the Image Editor header's **Slot / View Layer / Pass** dropdowns to inspect it [frame_017]; in 2.81+ the same is available live in rendered viewport through the shading popover's **Render Pass** menu [frame_023]. Untick `Render Single Layer` afterwards [transcript 6:40-7:06].
22. **Add a view layer named `ObjectThroughGlass`.** Keyboard and glass collections stay fully visible; disable the `TableReflection` duplicate [frame_018].
23. **Enable Transmission Indirect (and Glossy Indirect) on it.** The rays that matter go light → keyboard → *through* the glass → camera: last surface is a transmitting one, and it bounced more than once [frame_019, frame_020, transcript 7:28-8:12]. Glossy Indirect is enabled here too and used at the very end to add sparkle [transcript 8:06-8:13].
24. **Kill the HDRI inside the glass.** The transmission pass shows the whole HDRI environment refracting through the glass [frame_020]. In the **World shader editor**, add a **Light Path** node and an **Invert** node (`Fac 1.000`): wire `Is Glossy Ray → Invert → Background ▸ Strength` [frame_021]. The HDRI disappears from the transmission pass while still lighting the scene; disconnect these nodes again for the first three view layers [transcript 8:28-8:56].
25. **Add a fifth view layer named `GlassMask`.** Duplicate the `MainObject` collection to `MainObject.001` (keeping `Keyboard.000` and its bezier-circle parts) and turn the original off [frame_022]; duplicate the table collection to `TableEmission` / `Table.002`, disable the other two table collections and make sure the shadow catcher is off [frame_023].
26. **Assign a flat Emission shader to every material on those duplicates** — Surface `Emission`, Color white, Strength `1.000`, replacing e.g. the original `plastic.top` Mix Shader / Diffuse BSDF setup [frame_022, frame_023].
27. **Enable Transmission Indirect and Glossy Indirect on the GlassMask layer too**, and keep the Light Path world hookup connected for it [frame_025]. Its transmission-indirect output is a clean black-and-white image of exactly where the CG object shows through the glass [frame_023, transcript 9:31-9:50].
28. **Clean up the shared collection list.** Because collections were added as the layers were built, go back through the earlier view layers and **untick the box to exclude** the collections they do not need — the tooltip reads *Exclude from View Layer* [frame_024, transcript 9:54-10:11].
29. **Render twice and save two multilayer EXRs.** Untick `Use for Rendering` on the last two layers, disconnect the Light Path nodes, render the first three and save as **OpenEXR MultiLayer**; then invert the selection — enable only `ObjectThroughGlass` and `GlassMask`, reconnect the Light Path nodes, render and save a second EXR [frame_025, transcript 10:46-11:14].
30. **Open the Compositor** with Use Nodes and Backdrop on, delete everything, and add `Viewer` + `Composite` nodes. Load the plate as an **Image Sequence** (`Frames 123`, `Start Frame 0`, `Offset -1`, Auto-Refresh, Color Space `sRGB`) through a **Scale** node set to `Render Size / Stretch`; `Ctrl+Shift+Click` any node to view it [frame_027, frame_028].
31. **Load the first EXR as an Image node.** Because it is a multilayer EXR, the node gets a **Layer** dropdown (here listing the layers written into that file) and exposes whatever passes each layer carried [frame_027, frame_031].
32. **Composite the shadows.** With the node on **Layer `Shadow`**, drop its **Alpha** into the `Fac` of a Mix ▸ **Multiply** (top colour white, bottom black) to get a true black-and-white shadow image [frame_027], then **Color Ramp** (stop 1 at `Pos 0.745`) for range, **RGB Curves** (`Fac 1.000`, point `X 0.47222 / Y 0.49375`) for colour and brightness, and a Mix ▸ Multiply against the plate [frame_028, transcript 13:01-13:30].
33. **Alpha Over the main object.** Duplicate the image node, switch it to **Layer `MainObject`**, and feed `Combined` into an **Alpha Over** (`Convert Premul` off, `Premul 0.000`, `Fac 1.000`) on top of plate + shadows [frame_029, transcript 13:32-13:45].
34. **Try, and reject, the obvious ways of adding the through-glass pass.** Load the second EXR on **Layer `ObjectThroughGlass`** and take its `TransInd` output: a Mix ▸ Add looks wrong, an Alpha Over does almost nothing because the pass has black baked in with no alpha, and a **Luminance Key** on the black background keys badly [frame_030, transcript 14:07-14:37].
35. **Use the glass mask instead.** Duplicate the image node and switch the **Layer** dropdown to `GlassMask` — the dropdown lists `Composite`, `GlassMask` and `ObjectThroughGlass` [frame_031]. Run it through a **Color Ramp** (stop at `Pos 0.966`) to crush the mask to solid black and white, and plug that into the **`Fac`** of an Alpha Over whose inputs are the composite so far and the `TransInd` output [frame_032, transcript 14:47-15:17].
36. **Add the table reflections.** Switch another image node to **Layer `Reflections`** and `Add` its **`GlossInd`** output into the composite — the equation says glossy indirect is added, and it looks right [frame_033, transcript 15:23-15:41]. Duplicating the Add node strengthens the effect if more is wanted [transcript 15:41-15:47].
37. **Add the through-glass glossy sparkle.** Take the `GlossInd` output of the `ObjectThroughGlass` layer, Add it in using the same black-and-white mask in the `Fac` input, and tone it down with a Mix ▸ **Multiply** against a chosen grey [frame_034, frame_035, transcript 15:47-16:22].
38. **Read the equation behind all of it** — `docs.blender.org ▸ manual ▸ render ▸ layers ▸ passes` [frame_026]: light passes **add**, colour passes **multiply**, the sum is Combined; Add, Multiply and Alpha Over are the only nodes needed [transcript 12:04-12:58].
39. **Render the sequences and swap the stills for them.** Re-enable `Use for Rendering` on the first three layers only, restore the normal HDRI, put a **Render Layers** node into the `Composite` node (whatever feeds Composite is what gets written), set an OpenEXR MultiLayer sequence output and Render Animation; then do the same for the last two layers with the Light Path world hooked up, to a different folder. Point every image node at the new sequences and re-pick each layer [transcript 16:34-17:44]. [no frame: this pass is narrated over fast-forwarded screen recording, with no panel held long enough to read]
40. **Final render.** Hook the finished composite into the `Composite` node, set output to **PNG**, and Render Animation — fast, since it only re-composites [frame_035, transcript 17:44-18:05]. The Image Editor's pass dropdown set to `Composite` shows the finished frame [frame_036].

### Nodes / Settings
- **Render engine** — Cycles, `Supported`, `GPU Compute`, Path Tracing, Render `512` / Viewport `32` [frame_004]
- **View layers (5)** — `MainObject`, `Shadow` [frame_010], `Reflections` [frame_013], `ObjectThroughGlass` [frame_018], `GlassMask` [frame_022]
- **Collections** — `Collection` (Camera), `MainObject`, `Table`, `Glass` [frame_006], plus the duplicates `TableReflection`/`Table.001` [frame_015, frame_018], `MainObject.001` [frame_022] and `TableEmission`/`Table.002` [frame_023]
- **`M`** — Move to Collection / New Collection [frame_006]
- **Collection ▸ View Layer submenu** — `Disable from View Layer` (`E`), `Enable in View Layer` (`Alt E`), `Set Indirect Only`, `Clear Indirect Only`, `Set Holdout`, `Clear Holdout` [frame_008]
- **Collection ▸ Duplicate Collection** — the way to keep one object in two states across layers [frame_013]
- **Exclude from View Layer** — the outliner checkbox, for collections a layer does not need at all [frame_024]
- **Object Ray Visibility on the glass** — `Shadow`, `Diffuse`, `Glossy` all off; `Camera`, `Transmission`, `Volume Scatter` on [frame_012]
- **Shadow Catcher** — on the `Table` object in the Shadow layer [frame_010]; off on the duplicated table in Reflections [frame_015]
- **View Layer ▸ Passes panel** — Data (`Combined`, `Z`, Alpha Threshold `0.500`, Cryptomatte Object/Material/Asset, Levels `6`, Accurate Mode on) and Light (Diffuse / Glossy / Transmission / Subsurface × Direct / Indirect / Color, Volume Direct / Indirect, Emission, Environment, Shadow, AO) [frame_015]
- **Passes enabled** — `Glossy Indirect` on Reflections [frame_015]; `Transmission Indirect` + `Glossy Indirect` on ObjectThroughGlass [frame_020] and on GlassMask [frame_025]
- **`Use for Rendering` / `Render Single Layer`** — the per-layer toggles that split the shot into two EXR renders [frame_018, frame_025]
- **Viewport Shading ▸ Render Pass** — live per-pass preview in rendered view (2.81+): General (Combined, Emission, Background, AO), Light (all direct/indirect/color rows), Data (Normal, UV, Mist) [frame_023]
- **Glass material** — Principled BSDF, `Transmission 1.000`, `Roughness 0.033`, `Specular 0.500`, `IOR 1.450`, `Clearcoat Roughness 0.030` [frame_002, frame_024]
- **Glass normal detail** — `Texture Coordinate → Mapping` (Point, Scale Z `0.300`) `→ Noise Texture` (3D, Scale `15.000`, Detail `0.100`) `→ Normal Map` (World Space, Strength `0.005`) [frame_002]
- **World** — Environment Texture `hdri-1.hdr` (Linear, Equirectangular, Single Image) → Background (`Strength 1.000`) → World Output [frame_021]
- **HDRI-out-of-glass trick** — `Light Path ▸ Is Glossy Ray → Invert (Fac 1.000) → Background ▸ Strength` [frame_021]
- **Glass mask source** — duplicated object + table collections with every material replaced by `Emission` (white, Strength `1.000`), read through the Transmission Indirect pass [frame_022, frame_023]
- **Compositor image nodes** — multilayer EXRs arrive as `Image` nodes with a **Layer** dropdown (`Composite` / `GlassMask` / `ObjectThroughGlass` in the second file) [frame_030, frame_031]
- **Plate node** — Image Sequence, `Frames 123`, `Start Frame 0`, `Offset -1`, Auto-Refresh, `sRGB`; **Scale** `Render Size / Stretch` [frame_027, frame_028]
- **Shadow chain** — Alpha → Mix `Multiply` (white/black) → `Color Ramp` (`Pos 0.745`) → `RGB Curves` (`X 0.47222 / Y 0.49375`) → Mix `Multiply` against the plate [frame_027, frame_028]
- **Alpha Over** — `Convert Premul` off, `Premul 0.000`, `Fac 1.000`; used plain for the main object [frame_029] and with the mask in `Fac` for the through-glass pass [frame_032]
- **Glass mask crush** — `Color Ramp` at `Pos 0.966` [frame_032]
- **Reflection add** — `Reflections ▸ GlossInd` into a Mix `Add` (`Fac 1.000`) [frame_033]; the `ObjectThroughGlass ▸ GlossInd` added the same way and multiplied down by a grey [frame_034, frame_035]
- **Rejected approaches** — Mix `Add`, plain `Alpha Over` and `Luminance Key` on the transmission pass all fail because the pass has black baked in with no alpha [frame_030]
- **Documentation** — `docs.blender.org/manual/latest/render/layers/passes` [frame_026]
- **Output** — two OpenEXR MultiLayer sequences, then a PNG sequence out of the Composite node [frame_036]

### Difficulty
Advanced

### Blender Version
Blender **2.81.16**, read from the status bar [frame_001, frame_004, frame_015, frame_025]. The viewport Render Pass preview is called out as Blender 2.81+ [frame_023, transcript 6:51-7:02].

### Tags
compositing, vfx, cycles, render-passes, view-layers, holdout, shadow-catcher, glass, transmission, light-path, camera-tracking, advanced

---

## Related Tutorials
- `composite-cgi-around-real-object---blender-vfx-tutorial-full.md` — the companion shot from the same author: the same three levels of visibility control, solving occlusion with Holdout and Z-depth instead of transmission passes
- `add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2.md` — same author; the same view-layer/holdout/shadow-catcher split wrapped in an ACES colour pipeline
- `add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1.md` — same author; the colour-gamut and gamma groundwork under any live-action comp
- `replacing-adobe-after-effects-with-blender-tutorial.md` — Blender's compositor as a standalone 2D toolset
