---
title: Composite CGI Around Real Object - Blender VFX Tutorial (FULL)
source: YouTube
url: https://www.youtube.com/watch?v=fnAGtXMkRMY
author: InLightVFX
ingested: 2026-09-11
blender_version: "Blender 2.81.16 -- observed in frame_005, frame_008, frame_013, frame_019"
tags: [compositing, vfx, cycles, render-passes, view-layers, holdout, shadow-catcher, z-depth, masking, camera-tracking, advanced]
extraction_status: complete
frames_dir: tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/
frame_count: 28
frame_status: complete
uncertainty_frames: []
grounding: key-steps-anchored (32/32 steps, 2026-09-11)
frame_selection: explicit-timestamps (supplied to select_frames.py; NOT evidence that the frames were read -- see `grounding:`)
---

# Composite CGI Around Real Object - Blender VFX Tutorial (FULL)

**Source:** [YouTube](https://www.youtube.com/watch?v=fnAGtXMkRMY)
**Author:** InLightVFX
**Duration:** 17m29s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


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

## Captured Frames

- [0:02] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_000.jpg — goal shot ring around real pot
- [0:40] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_001.jpg — lazy leaf proxy geometry
- [1:15] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_002.jpg — bsdf box pot roughness
- [1:36] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_003.jpg — naive render shows problem
- [2:38] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_004.jpg — four collections in outliner
- [3:11] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_005.jpg — pot collection holdout
- [3:33] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_006.jpg — box leaf indirect only
- [3:44] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_007.jpg — main objects layer render
- [4:05] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_008.jpg — shadow catcher object visibility
- [5:07] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_009.jpg — shadow view layer result
- [6:44] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_010.jpg — render passes diffuse glossy indirect
- [7:06] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_011.jpg — viewport pass dropdown glossy
- [7:36] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_012.jpg — pot base disable glossy
- [8:03] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_013.jpg — pot base disable diffuse
- [9:22] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_014.jpg — background image scale node
- [9:59] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_015.jpg — shadow mix multiply factor alpha
- [10:42] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_016.jpg — cycles master equation
- [11:38] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_017.jpg — diffuse indirect x diffuse color
- [12:14] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_018.jpg — alpha over main ring
- [12:56] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_019.jpg — leaf mask in mask tab
- [13:30] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_020.jpg — luminance key settings
- [13:56] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_021.jpg — dilate blur mask chain
- [14:26] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_022.jpg — alpha over premult leaves wrong
- [14:56] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_023.jpg — z depth normalize node
- [15:26] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_024.jpg — colorramp gamma depth divide
- [15:47] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_025.jpg — multiply zdepth by leafmask
- [16:24] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_026.jpg — shadows multiplied over leaves
- [17:00] tutorials/frames/composite-cgi-around-real-object---blender-vfx-tutorial-full/frame_027.jpg — final composited result

---

## Structured Notes

### Core Technique
Wrapping a CG object *around* a real one in Blender Cycles by splitting the shot into three view layers — **Main Objects**, **Shadow** and **Glossy/Diffuse** — using **collection Holdout** to let stand-in geometry mask the CG, **Indirect Only** to keep an object's reflections without the object, **Shadow Catcher** to harvest only its shadows, and **Diffuse/Glossy Indirect render passes** to harvest only the light it throws. Foreground detail too fiddly to model (plant leaves) is recovered in 2D with a **Luminance Key + animated mask**, then placed correctly in depth with **Z-depth compositing** — multiplying the leaf matte by a Color Ramp'd depth pass so the leaves stop covering the parts of the ring that are in front of them.

### Summary
17m29s, **Blender 2.81.16** [frame_005, frame_008, frame_013, frame_019], Cycles, GPU Compute. A chrome ring orbits a real potted plant: it must pass *behind* the pot and leaves, pick up their reflections, cast shadows on them and bounce light into the pot [frame_000, frame_027]. Footage is a tracked 1920x1080 image sequence (`plantBG3_######.jpg` / `pngSeqHD_####`, 156 frames, shot range 26-139) [frame_014, frame_019].

**The three levels of visibility control** the video is built around: **object visibility** (Object Properties ▸ Visibility ▸ Shadow Catcher / Holdout / Ray Visibility) [frame_008, frame_013], **collection visibility** (right-click ▸ View Layer ▸ Set Holdout / Set Indirect Only / Disable from View Layer) [frame_005] and **view-layer visibility**, i.e. render passes [frame_010, frame_017]. A companion infographic is linked in the video description [transcript 2:06-2:09]. One gotcha stated outright: object visibility settings and the collection list are **shared by every view layer** — only the per-collection *view layer* settings and the enable checkbox are per-layer [transcript 4:27-5:02, frame_011].

**Scene prep** is the ordinary matchmove work — match geometry (a stand-in box and pot, plus deliberately sloppy warped planes for the leaves) [frame_001], match lighting (a 360° HDRI shot with a Ricoh Theta V), match textures (Principled BSDF, colour and roughness only) [frame_002]. The leaf proxies are intentionally rough because they exist only for reflections and shadow catching — their silhouette is solved in 2D later [transcript 0:38-0:43, 12:35-12:46].

**Compositing** follows the Cycles pass equation from the manual: light passes **add**, colour passes **multiply**, everything sums to Combined [frame_016]. Shadows are converted to a controllable black-and-white matte rather than alpha-over'd [frame_015, frame_017], the pot's diffuse-indirect is multiplied by diffuse-colour before being added [frame_017], reflections are added straight in, and the ring goes on with Alpha Over [frame_018]. The leaves come from a Luminance Key on the original plate, cut down by an animated mask [frame_019, frame_020, frame_021], tidied with Dilate/Erode and Blur [frame_023], and finally depth-sorted against the ring [frame_024, frame_025, frame_026].

### Key Steps
1. **Shoot and track the plate, then rebuild the set.** Recreate only what interacts with the CG — here a box and a pot as grey proxy geometry, "1. Match geometry" [frame_001]. Scrub the whole shot to confirm nothing slips; small drift can be cheated with animated object position or shape keys [transcript 0:46-0:57].
2. **Make the leaf proxies deliberately rough.** Plane objects warped roughly into the leaf shapes — accuracy is not needed because they only ever serve as reflection and shadow-catching surfaces [transcript 0:38-0:43]; the real silhouette arrives later as a 2D matte [frame_021].
3. **Match the lighting with a 360° HDRI** shot on a Ricoh Theta V — the reason the CG ring's chrome reflects the real room [transcript 0:58-1:07]. [no frame: the HDRI and world setup are narrated over B-roll, never shown as a panel]
4. **Match textures with a plain Principled BSDF.** Colour and roughness only — `PotMaterial` is set by HSV `H 0.111 / S 0.553 / V 0.633`, IOR `1.450`, Transmission `0.000`, with **Roughness 0.15** called out in narration as the value that matters later [frame_002, transcript 5:38-5:46].
5. **Set the render engine.** Render Properties ▸ **Cycles**, Feature Set `Supported`, Device **`GPU Compute`**, Integrator `Path Tracing`, Render samples `128` / Viewport `32`, Film Exposure `1.00`, Pixel Filter `Blackman-Harris` at `1.50 px` [frame_003].
6. **Render once as-is to see the problem.** Everything renders — CG pot, box and leaves included — and the ring sits in front of the pot instead of orbiting it [transcript 1:35-1:46]. [no frame: the faulty render is shown only as a full-screen beauty frame indistinguishable from the finished shot at still resolution; frame_007 shows the corrected version of the same layer]
7. **Sort every object into its own collection.** Starting from a flat outliner (`Camera`, `CameraParent`, `Box`, `leaf-layer1/2/3`, `Pot`, `PotBase`, `RingMirror`, `RingWhite1/2/3`) [frame_004], select and press **`M` ▸ New Collection**. Result: four collections — `Camera`, `Rings`, `Pot`, `Box&Leaves` [frame_008].
8. **Name the current view layer `Main Objects`** — the layer that will carry the ring alone [frame_004].
9. **Holdout the pot.** Right-click the `Pot` collection ▸ **View Layer ▸ Set Holdout** [frame_005]. Holdout makes everything in that collection punch a hole through whatever falls behind it from camera, so the ring disappears where it passes behind the pot and survives where it passes in front [transcript 3:14-3:29]. The same submenu carries `Disable from View Layer`, `Set Indirect Only` and the matching Clear entries; the sibling **Visibility** submenu (Isolate / Hide / Disable in Viewports / Disable in Renders) is the *other*, non-view-layer kind of control [frame_006].
10. **Set `Box&Leaves` to Indirect Only** — the same right-click ▸ View Layer submenu, one entry above Set Holdout [frame_005] — so the box and leaves show up in the ring's reflections without rendering themselves [transcript 3:30-3:38].
11. **Turn on a transparent background and render the layer.** Render Properties ▸ Film ▸ **Transparent** [frame_010]. The Main Objects layer now outputs the ring alone on alpha, already masked by the pot and carrying the room's reflections [frame_007].
12. **Add a second view layer named `Shadow`.** Set the leaves and box to **Shadow Catcher** in Object Properties ▸ Visibility, and **uncheck Ray Visibility ▸ Shadow** on them so they catch shadow without casting any [frame_008, transcript 4:02-4:12]. A shadow catcher still appears in other objects' reflections, which is why leaving it enabled does not hurt the Main Objects layer [transcript 4:12-4:27].
13. **Duplicate the pot collection for the shadow layer.** Right-click ▸ Duplicate Collection gives `PotShadow`; turn the original `Pot` off in this layer and make the duplicates shadow catchers too. Because all view layers share the same collection list, `PotShadow` also appears in Main Objects and must be disabled there [frame_011, transcript 4:37-5:02].
14. **Set `Rings` to Indirect Only in the Shadow layer** — the output is then nothing but the shadows the ring throws onto pot, leaves and box, over alpha [frame_009, transcript 5:02-5:10].
15. **Add a third view layer named `Glossy/Diffuse`** and disable `PotShadow` in it [frame_011]. Its job is the light the ring bounces *into* the pot.
16. **Understand why the pot needs two passes.** At Roughness `0.15` the pot is both a diffuse and a glossy surface, and Cycles labels a light ray by the last surface it hits before the camera — so the ring's contribution arrives split across both. These rays bounce more than once, hence *indirect* [transcript 5:31-7:01]. [no frame: this segment is an animated ray diagram, not a Blender panel]
17. **Enable the passes.** View Layer Properties ▸ Passes ▸ Light: **Diffuse Indirect**, **Diffuse Color** and **Glossy Indirect** — the render-layers node then exposes `DiffInd`, `DiffCol` and `GlossInd` sockets [frame_017, transcript 6:41-8:21]. In 2.81+ each pass can be previewed live in rendered viewport via the pass dropdown; at low sample counts it is extremely sparse and noisy [frame_012], which is why render samples go up to **`512`** for this layer [frame_010].
18. **Set `Rings` to Indirect Only here too** (same collection ▸ View Layer ▸ Set Indirect Only entry [frame_005]), so only the ring's *reflection* lands in the pot, not the ring itself [transcript 7:10-7:19].
19. **Stop the pot base from double-lighting the pot.** Select `PotBase` and in Object Properties ▸ Visibility ▸ Ray Visibility **uncheck `Glossy` and `Diffuse`** — that light is already present in the real footage and would otherwise be added twice [frame_011, frame_013, transcript 7:19-8:10]. Completely disable `Box&Leaves` in this layer as well.
20. **Render all layers and open the Compositor.** Use Nodes and Backdrop on; an `Image` node loads the plate as an **Image Sequence** (`Frames 156`, `Start Frame 0`, `Offset -1`, Auto-Refresh on, Color Space `sRGB`), a **Scale** node set to **Render Size / Stretch** fits it, and `Composite` + `Viewer` nodes take the output. `Ctrl+Shift+Click` a node to preview it [frame_014].
21. **Composite the shadows as a matte, not as alpha.** Add a Render Layers node on the `Shadow` layer and drop its **Alpha** output into the **Fac** of a `Mix` node set to **Multiply**, with the top colour white and the bottom black — that produces a true black-and-white shadow image that curves can actually grade [frame_015, transcript 9:43-10:05]. Then a **Color Ramp** (stop at `Pos 0.218`) sets the black/white range, an **RGB Curves** (`Fac 1.000`, curve point `X 0.49444 / Y 0.47188`) tints and balances it, and a second **Multiply** mix multiplies the plate by it [frame_017].
22. **Read the Cycles pass equation before wiring the light passes.** From the manual: `(Diffuse Direct + Diffuse Indirect) x Diffuse Color + (Glossy Direct + Glossy Indirect) x Glossy Color + (Transmission Direct + Transmission Indirect) x Transmission Color + Emission + Environment = Combined` — light passes **add**, colour passes **multiply** [frame_016]. Add, Multiply and Alpha Over are the only nodes needed.
23. **Add the diffuse and glossy contribution.** Duplicate the Render Layers node onto `Glossy/Diffuse` [frame_017], multiply `DiffInd` by `DiffCol` with a Mix ▸ Multiply, then `Add` that into the composite; `GlossInd` is added straight in with another `Add` (no glossy colour pass was exported — it is pure white and would change nothing) [frame_026, transcript 11:35-12:07].
24. **Alpha Over the ring on top.** A fourth Render Layers node on `Main Objects` feeds an **Alpha Over** node — appropriate because a Combined pass carries a real alpha channel [frame_018, transcript 12:07-12:17].
25. **Rotoscope the leaves in 2D instead of modelling them.** Masking workspace ▸ Mask mode: draw a loose bezier mask around the leaf cluster, keyframe it roughly across the shot, and name it `Leaf` [frame_019]. The plant was filmed against a plain white wall specifically so this would work [transcript 12:46-12:50].
26. **Pull a luminance key on the plate.** Duplicate the footage + Scale pair, add a **Mask** node pointing at `Leaf` (Feather on, `Scene Size`) and a **Luminance Key** node (`High 1.000 / Low 0.000` at default, then dialled in until the wall separates near the leaves) [frame_020]. The key selects the wall, so an **Invert** node (`RGB` on, `Fac 1.000`) flips it to select the leaves [frame_021].
27. **Cut the key down to the mask.** A Mix ▸ **Multiply** of the inverted luma matte by the mask output confines the key to the leaf region — the backdrop then shows a clean leaf silhouette [frame_021]. Tighten it with **Dilate/Erode** (`Mode: Step`, `Distance -1`) and a **Blur** (`X 2 / Y 2`, `Size 1.000`) [frame_023].
28. **Turn the matte into pixels.** A **Set Alpha** node takes the matte into `Alpha` and the original plate into `Image`, yielding just the leaves (and a sliver of pot) on transparency [frame_023, frame_026]. Alpha Over it under the composite with **Convert Premul** ticked — at which point the leaves correctly cover the ring in places, and wrongly cover it everywhere else [frame_022, transcript 14:16-14:36].
29. **Build a Z-depth mask.** Another Render Layers node on `Main Objects` — the view-layer dropdown lists all three layers [frame_023] — with its **Depth** output into a **Normalize** node, then a **Color Ramp** with the two stops pushed close together to make a hard dividing line at a chosen distance (captured mid-drag at `Pos 0.618`, settling at `Pos 0.255`) [frame_024, frame_026]. Nearer is black, farther is white; a **Gamma** node makes fine adjustment easier [transcript 15:35-15:40]. The isolated result is the front half of the ring in black on white [frame_025].
30. **Multiply the leaf matte by the depth mask.** Anything black in either input stays black, so wherever the ring is in front of the leaves the leaf matte is knocked out — exactly the wanted result. Feed this into the Set Alpha node's `Alpha` input [frame_026, transcript 15:40-16:16].
31. **Put the shadows back on top of the leaves.** Multiply the earlier shadow output over the isolated leaves before the final Alpha Over, so the ring's shadow falls on them too [frame_026, transcript 16:16-16:33].
32. **Check other frames, then render.** Scrub to a different frame and re-render to confirm the comp holds; plug the final node into **Composite**, set output to **PNG**, and Render Animation. Grade afterwards [frame_027, transcript 16:34-17:03].

### Nodes / Settings
- **Render engine** — Cycles, Feature Set `Supported`, Device `GPU Compute`, Path Tracing, samples `128` / viewport `32` early on [frame_003], raised to `512` for the noisy indirect passes [frame_010]
- **Film ▸ Transparent** — required for every CG layer [frame_010]
- **Collection ▸ View Layer ▸ Set Holdout** — stand-in geometry masks CG behind it, per view layer [frame_005]
- **Collection ▸ View Layer ▸ Set Indirect Only** — contributes reflections/bounce without rendering itself [frame_005]
- **Collection ▸ Visibility submenu** — Isolate / Hide / Disable in Viewports / Disable in Renders; the non-view-layer control set [frame_006]
- **Object Properties ▸ Visibility** — `Shadow Catcher`, `Holdout`, and Ray Visibility toggles `Camera / Diffuse / Glossy / Transmission / Volume Scatter / Shadow` [frame_008, frame_013]
- **`M`** — Move to Collection / New Collection [frame_004]
- **View layers used** — `Main Objects` (Combined + Z) [frame_007], `Shadow` (Combined + Z) [frame_009], `Glossy/Diffuse` (+ Diffuse Indirect, Diffuse Color, Glossy Indirect) [frame_011, frame_017]
- **Collections used** — `Camera`, `Rings`, `Pot`, `Box&Leaves`, `PotShadow` (5 total, matching the scene stats) [frame_008, frame_011, frame_019]
- **Principled BSDF `PotMaterial`** — HSV `0.111 / 0.553 / 0.633`, Roughness `0.15`, IOR `1.450`, Transmission `0.000` [frame_002]
- **Image node** — Image Sequence, `Frames 156`, `Start Frame 0`, `Offset -1`, Auto-Refresh, Color Space `sRGB`; **Scale** node `Render Size / Stretch` [frame_014]
- **`Ctrl+Shift+Click`** — preview any node through the Viewer [frame_014]
- **Shadow chain** — Mix `Multiply` with Alpha into `Fac` (white over black) → `Color Ramp` (`Pos 0.218`) → `RGB Curves` (`X 0.49444 / Y 0.47188`) → Mix `Multiply` against the plate [frame_015, frame_017]
- **Cycles pass equation** — light passes add, colour passes multiply, summed to Combined [frame_016]
- **Leaf matte chain** — `Mask` node (`Leaf`, Feather, Scene Size) + `Luminance Key` (`High 1.000 / Low 0.000`) → `Invert` (`RGB`, `Fac 1.000`) → Mix `Multiply` → `Dilate/Erode` (`Step`, `Distance -1`) → `Blur` (`X 2 / Y 2`, `Size 1.000`) → `Set Alpha` [frame_020, frame_021, frame_023]
- **Alpha Over** — `Convert Premul` on for the premultiplied leaf plate; `Fac 1.000` [frame_018, frame_022]
- **Z-depth chain** — `Depth` → `Normalize` → `Color Ramp` with stops crushed together (`Pos 0.255`, shown mid-drag at `0.618`), optional `Gamma`, then Mix `Multiply` against the leaf matte [frame_024, frame_025, frame_026]
- **Plate** — `plantBG3_######.jpg` / `pngSeqHD_####`, `1920 x 1080`, shot range frames `26-139` of 156 [frame_005, frame_019]
- **Camera** — `45.56 mm`, Clip Start `0.328'` / End `3281'`, driven by `CameraParent` [frame_005]
- **Final output** — PNG sequence out of the Composite node, graded afterwards [frame_027]

### Difficulty
Advanced

### Blender Version
Blender **2.81.16**, read from the status bar [frame_005, frame_008, frame_013, frame_019]. The per-pass rendered-viewport preview used throughout is called out as Blender 2.8+ only [transcript 7:01-7:10].

### Tags
compositing, vfx, cycles, render-passes, view-layers, holdout, shadow-catcher, z-depth, masking, camera-tracking, advanced

---

## Related Tutorials
- `composite-cgi-element-behind-real-glass---blender-vfx-tutorial-full.md` — the companion shot: same three levels of visibility control, but transmission-indirect through real glass instead of holdout around a real pot
- `add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2.md` — same author, same view-layer / holdout / shadow-catcher split, wrapped in an ACES colour pipeline
- `add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1.md` — same author; the colour-gamut and gamma groundwork under any live-action comp
- `replacing-adobe-after-effects-with-blender-tutorial.md` — Blender's compositor as a standalone 2D toolset
