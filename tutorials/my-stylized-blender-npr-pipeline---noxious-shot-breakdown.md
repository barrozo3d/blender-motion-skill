---
title: My Stylized Blender NPR Pipeline - NOXIOUS Shot Breakdown
source: YouTube
url: https://www.youtube.com/watch?v=51aK8POWKQA
author: Kay Hilman
ingested: 2026-08-07
blender_version: "Blender 4.1"
tags: [grease-pencil, geometry-nodes, npr, non-photorealistic, line-art, uv-projection, texture-paint, shading, cycles, eevee, aov, compositing, render-passes, pipeline, advanced]
extraction_status: complete
frames_dir: tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/
frame_count: 19
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# My Stylized Blender NPR Pipeline - NOXIOUS Shot Breakdown

**Source:** [YouTube](https://www.youtube.com/watch?v=51aK8POWKQA)
**Author:** Kay Hilman
**Duration:** 32m50s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, my name is Cy and today we're getting technical.
[0:03] We are diving deep into the exact NPR pipeline behind my short film Noxious.
[0:08] In my last video I gave a high level overview on how the workflow was developed.
[0:12] But today we are digging into the project files.
[0:14] I'm taking you step by step through one of my personal favorite shots of the film
[0:19] to show you how I made this 3D world look like a 2D illustration.
[0:23] We'll cover the 2D to 3D layout workflow,
[0:26] geometry nodes paired up with grease pencil for non flickering surface detail,
[0:31] projection mapping and painting tricks to hide stretching,
[0:34] a hybrid EEVEE and Cycles shader setup for super crisp shadows
[0:38] and I'm taking you through the custom render passes I used
[0:41] so that I have a very controllable compositing workflow.
[0:44] A quick side note before we start,
[0:46] I'm demonstrating this in Blender version 4.1
[0:50] because that was the version that I used during production in 2023 and 2024.
[0:55] If you enjoyed this breakdown, I'll do some research
[0:58] and see how we can modernize this workflow for the newer Blender 5.2 version and above.
[1:03] Without further ado, let's jump straight into the shot.


### Layout & Illustration [1:07]
**Transcript (timestamped):**
[1:08] As I had shown in my previous video,
[1:10] I always start each shot with a 3D blockout
[1:12] that I can then use as a nice reference for my illustration.
[1:15] The blockout also helps to figure out what the camera movement could be.
[1:19] I would also add in a sun as a nice reference for shadow and occlusion.
[1:23] Now normally that would be it and I would only come back to 3D once I had finished the illustration.
[1:29] But in this case, I went a bit more for a hybrid approach.
[1:33] I would illustrate parts of the scene, then model or block them out to see what works,
[1:37] go back, illustrate some more and repeat until I had finished the whole illustration
[1:42] and had all of the silhouettes ready in 3D.
[1:44] This helped me speed up the process a bit and maintain control over the overall complexity.
[1:50] In the illustration, I make sure that the colors, shadows and lines are separated,
[1:54] so that it'll be easy for me to then read the lineart as a grease pencil reference
[1:59] and use the colors for eventual projection mapping and texture painting.


### Grease Pencil & Geo Nodes [2:03]
**Transcript (timestamped):**
[2:03] Okay, so with our scene modeled and the illustration done,
[2:06] we can now use that as a reference for our grease pencil.
[2:09] For grease pencil, I use a collection modifier.
[2:12] So it's very important that the scene already has collections set up that it can easily reference.
[2:18] And in my case, I made sure that I have one big mesh collection
[2:21] that contains all of the objects in the scene that I want to be affected by the grease pencil modifier.
[2:26] And then I have separated these elements into sub-collections that I can use for our curve tool
[2:32] that we will be building together in a moment.
[2:35] But first, let's set up the grease pencil modifier.
[2:37] I'm quickly going to press Shift-8, add grease pencil and then Collection Lineart.
[2:42] And it's in the wrong collection right now, so I'm going to move it over here.
[2:45] The first thing that I already see happening is that the lines are much thicker in front of the camera
[2:50] than they are further away.
[2:52] And for noxious, it was very important to the style that the lines were consistent across the whole screen,
[2:58] no matter if they were close or further away to the camera.
[3:01] So we can quickly fix that if we go into the grease pencil settings
[3:05] and then we move down over here to the Strokes
[3:09] and we can set that from World Space all the way to Screen Space.
[3:13] And now this is way too big, so I'm going to quickly change this to 3.
[3:17] And then one other setting that I changed was inside of the geometry processing.
[3:21] I made sure that back-face-skilling was also forced.
[3:26] Great, so if I quickly change our viewport shading, so it's set to Material,
[3:32] you can already see some nice outlines showing.
[3:34] And it's even better if we set it to Flat.
[3:37] We now got the nice silhouette showing up based on our geometry.
[3:40] And all that's left for grease pencil is to draw the lines on the surfaces.
[3:45] To do that, I made a custom geometry note set up to help out.
[3:48] But first, I'll show you what I start out with.
[3:50] Basically, what I do is inside of my mesh collection, I create a new collection.
[3:56] And in this case, I'm just quickly going to call it Curves.
[4:00] And I like to make this one purple.
[4:02] I'm quickly just going to hide grease pencil so that we don't get any strange things happening.
[4:08] So now I'm going to quickly add a Bezier curve.
[4:11] And I'm going to delete all of the vertices.
[4:14] Perfect.
[4:15] So now if I quickly open up the tools here on the sidebar,
[4:18] and I set it to Draw Mode, and then I have Surface selected with the settings,
[4:25] which you can copy.
[4:26] And right now, what this does is it allows me to draw curves straight onto the surface.
[4:31] But as you can see, they're like clipping right through the mesh.
[4:37] And even though grease pencil will thicken this line,
[4:40] I still find issues where if the camera was moving around this,
[4:44] there would be some flickering happening on the grease pencil lines.
[4:47] So that's why I made a custom geometry note tool that we are going to be building together now.
[4:51] All right, so let's make this geometry note setup that can offset the curves for us.
[4:55] So I'm quickly going to change this to the geometry note editor.
[5:00] And with our Bezier curve selected, I'm going to create a new geometry note setup.
[5:04] And I'm going to call it, let's just do Curve Offset.
[5:08] Perfect.
[5:09] So I start with a resampled curve note and I set it to Evaluated.
[5:14] Resampling the curve with Evaluated removes the Bezier handle
[5:17] so we can strictly operate on the vertex positions that make up the curve.
[5:21] So let's do a curve to mesh.
[5:24] Grease Pencil reads mesh only in 4.1.
[5:28] So that's why we are converting the curve into a mesh.
[5:31] And then I want to set position so we can offset these meshes by some value.
[5:37] And right now we don't have anything to offset it from.
[5:40] And since we have drawn this right on top of something related to this lamp,
[5:47] which is a bit hard to see, but here we go.
[5:49] This is the lamp.
[5:49] I'm going to quickly drag this collection in here.
[5:52] So we have something to offset from these objects.
[5:54] They're imported as instances, but I need them as mesh so I can do a realized instances.
[6:00] So we get the geometry.
[6:02] Then I'm going to set position and then I'm going to take the normal of these meshes
[6:07] and then I'm going to offset the mesh by these normals.
[6:11] And we're going to see what happens.
[6:12] You can see that looks crazy, right?
[6:14] So if I hide this, this is without and this is with.
[6:18] So it expands these meshes and I can scale this by a value.
[6:25] So let me put that in here.
[6:27] And if I lower this amount, you can see, oh, it's getting back to its original shape.
[6:32] Now this will act as sort of a virtual offset that we won't actually display,
[6:39] but it's what we'll use for the curve to snap to.
[6:42] Let's build that real quick.
[6:43] All we need to do is do a geometry proximity.
[6:48] And what that does, it returns the closest surface position when it's set to faces.
[6:54] And we can use that position or the distance, but we can use that position on the curve
[7:01] line that we had created.
[7:03] And if I do that, and then if I preview this and we go to our little curve,
[7:07] which might be a little hard to see.
[7:10] So now you can clearly see that the curve is offset from the surface.
[7:14] And if we take our scale value over here, we can change by how much it's being offset.
[7:20] And I can't push it too much or it completely break,
[7:23] but I don't really need a lot.
[7:24] I just need it to be like offset by a little bit and it'll already be enough.
[7:28] We can use the group input node to send out some values that we can control on the modifier itself.
[7:33] So I want to have control over the amount of offset.
[7:35] I can give that a name.
[7:37] So let me select a group and then we can change this to offsets.
[7:42] What I also want to have control over is which collection we are sampling from.
[7:46] So we're going to send that out as well.
[7:48] And I want it to be a little higher.
[7:50] There we go.
[7:51] Over here on the modifier, you can see the collection that we have selected and the amount of offset.
[7:56] Perfect.
[7:57] So now I can go back to our curve and go into edit mode and I can just draw some more lines
[8:03] and they'll all stick to the surface with a slight offset that I can then control later on
[8:09] to decide how far away, like let's change this to this.
[8:13] And you can see that the lines are going a little bit further away from the surface.
[8:18] We can put the grease pencil back on and view it from our camera.
[8:22] And I'm going to draw some lines on the surface.
[8:25] And as you can see, our lines are showing up.
[8:27] That's perfect.
[8:28] Let me just dial this back a bit.
[8:29] There you go.
[8:30] And it's still showing.
[8:31] So now we do that for the whole scene based on the illustration we made and it should look something like this.
[8:38] So this is what that looks like with all of the lines drawn in onto the surfaces.
[8:43] It's pretty crazy.
[8:44] But to prove to you that this is still in 3D,
[8:47] I'm going to quickly switch this to studio lighting again.
[8:50] And there you go.
[8:51] Now, if I go out of the camera, you can see it's getting pretty crazy.
[8:54] Another important detail, right?
[8:55] One that you can see right here is that I have separate collections for certain curves.
[9:01] So that it's easy for me to manage.
[9:03] Like I can drag this one out of here and then switch it off.
[9:06] And now you can see that the bike doesn't have any of those surface details.
[9:12] And to show the difference, that's much more easy to see.
[9:16] I can also switch this to random, maybe.
[9:18] I guess the lines are a little bit harder to read,
[9:21] but let me just put that back to material and then put the curve lamps back into this collection
[9:27] and then switch it back on.
[9:29] And there you go.
[9:30] You can see the curve lines again.


### Project & Texture Paint [9:32]
**Transcript (timestamped):**
[9:32] With the Gris pencil lines looking nice in our seed, it's time to add some color.
[9:37] For this, it's very important that we closer our objects by texel density.
[9:42] What that means is I want to make sure that the objects that are in front
[9:46] get their own material so that they will have enough pixels when they sample it from their texture.
[9:52] And we wouldn't see any blockiness happening on screen.
[9:55] And the objects that are further away can be closer together in one single material
[10:00] and use one texture so that we don't use too many textures in our scene.
[10:04] And we can share the texture space in a way that is efficient
[10:09] while still maintaining quality over the overall scene.
[10:12] I guess it's similar to the way we are trying to abstract things that are further away
[10:17] in the same sense that they need to use less texel space.
[10:21] Not only will these clusters share the same material, they will also share the same UV.
[10:26] I mean, that's the whole point about these clusters.
[10:28] They all use the same texture, so they need to use the same UV as well.
[10:32] We're going to be focusing on this little bike section here.
[10:35] So I'm quickly going to hide all of these other collections.
[10:39] And we also don't want to use the grease pencil anymore.
[10:42] And I just want to look at this front lamp to make things easier for ourselves.
[10:47] Every object in the scene is going to have two UVs.
[10:51] One UV map that we will use for the texture and then one UV map will use for projection.
[10:57] The basic UV map you can see over here is just a normal regular UV map
[11:02] that you would use for any other game object, for example.
[11:06] We will use this UV map to later bake our projection onto.
[11:11] The reason I have a whole UV map is that if the camera pans around this object,
[11:16] I need to make sure that every angle is filled in with color.
[11:19] But because we don't know where each color is going to be yet,
[11:23] that's what we'll be using the projection for.
[11:25] We also create a projection UV map.
[11:27] You can simply press the plus button over here to create a new one.
[11:31] Now, the projection UV map is something that we don't create by hand,
[11:34] but we actually have a very handy modifier for.
[11:36] So if I go back into object mode and select the modifiers tab,
[11:40] you can see this UV projection modifier.
[11:42] It simply has the projection UV map that we want to target,
[11:46] an aspect ratio, which is based on the image size.
[11:49] So I just put 16 by 9 in here.
[11:51] And then I use the camera, which I called F100
[11:56] because that was based on frame 100 back then.
[11:59] To show you what that looks like, here I have our color texture imported,
[12:03] which is just the illustration without any of the line art or shading.
[12:07] It's just the base color.
[12:09] And I'm using our projection UV map that we have created
[12:12] that gets affected by the modifier.
[12:15] And then we're just sending that out as a material output.
[12:17] And if I just go out of the camera right now,
[12:19] you can already see that down here there are some strange things going on.
[12:24] We're seeing different parts of the image.
[12:26] And if I turn around the object, you can see that the projection is completely breaking.
[12:31] And we need a way to fix that.
[12:33] And like I mentioned, it is very important to cluster these objects into different materials
[12:38] so that they will all get the same amount of texel density
[12:42] because they're very close to the camera and I want them to have a lot of resolution.
[12:46] But they're currently all using the same setup where they have our color,
[12:50] illustration and the projection UV map.
[12:53] And they're all using that same modifier.
[12:55] Now, the question is how do we get this texture to be projected
[12:59] based on those UVs that we have created.
[13:01] And I actually found a very useful trick for that.
[13:04] So the first thing that I actually do is I have selected all of these objects
[13:08] and I join them together using Ctrl J.
[13:11] And what I then end up with is a bike paint mesh.
[13:15] That's what I called it.
[13:17] And it still has all of these four materials that we have created assigned.
[13:22] And you can just ignore these for now.
[13:23] These are from the other parts of the scene.
[13:25] But we're focusing on these four materials right now.
[13:28] What's important is that every single one of these materials gets a new texture.
[13:33] So if I go here and I create a new image texture
[13:38] and I can define the resolution.
[13:41] So I'd like this to be 4K.
[13:44] So I'm going to quickly do that.
[13:46] And I'm going to give this a name since we are working on the roots.
[13:49] I'm going to call this lamp roots.
[13:51] And I'm going to go to this V2 since we've already made these.
[13:54] When what's important is that I sample the color.
[13:56] That's already the main color of the object that I'm trying to go and paint later on.
[14:02] So that already saves me a bunch of time.
[14:04] So I can select this color here and we'll have a new image.
[14:07] Now this has become this color.
[14:10] But I'm going to quickly leave it like this.
[14:12] And it's important now to do this for all of these other materials.
[14:17] OK, so now I have created a texture for all of these four materials.
[14:22] And it's very important that we select this texture for the next step.
[14:25] So I'm going to go into all the materials and quickly select the texture.
[14:32] There we go.
[14:32] And then I'm going to switch this to viewport shading.
[14:36] And I have already set it up to be flat and then set the texture.
[14:40] And you can see I have selected single colors for all of these objects.
[14:44] And now we're going to be moving over to projection.
[14:47] Go into texture paint mode.
[14:49] You go and select the clone brush.
[14:52] We need to change some parameters.
[14:53] I've already set these up, but I'll walk you through them.
[14:56] Set it to clone from a specific paint slot.
[14:59] In this case, I'm just going to select lamp roots.
[15:02] And then we can select a specific texture that we want to use.
[15:05] So right now I want to use this long name, which is the color
[15:10] texture that we use to project onto the surface.
[15:13] We can use that to paint onto our UV texture.
[15:18] And then later on, fix the areas that are projected incorrectly.
[15:22] It is a little bit heavy to do this.
[15:24] So I like to switch the stroke method to a line.
[15:29] And then I can just drag one line across to see what happens.
[15:34] And there you go.
[15:35] There's also already some detail showing up.
[15:37] And we just do this across the whole object.
[15:40] And I'm making sure that I'm covering this whole object.
[15:43] It's almost like I'm just spray painting the object from one direction.
[15:47] This is a lot better than projection mapping for me, or at least baking
[15:51] with projection mapping, because now immediately I can jump in and I can see.
[15:55] All right. So one side is looking good.
[15:58] And I can just slowly start fixing the areas that need painting.
[16:02] So now I can switch to just paint mode, press shift X to sample a color.
[16:06] And I can start painting the areas that need some fixing.
[16:15] It doesn't have to be perfect.
[16:17] It's just important that whatever is seen from the camera is solved.
[16:21] Now, basically, once that is done, I can just start using these textures
[16:27] as the final output for the colors.
[16:30] So you switch all the materials back to this texture.
[16:34] And then we can use that texture for shading.
[16:37] So once all of the texture painting is done and the areas that are visible
[16:41] that needed fixing are fixed, you get something like this.
[16:45] There are still areas if I zoom around here that have some strange stretching going on.
[16:50] But since the camera won't really see that, I don't fix it.
[16:53] And I only just put time and effort into the places that need those areas to be fixed.
[16:59] For me, this is a lot more of an efficient process instead of baking it.
[17:03] I can directly start painting onto the texture and fix my errors.


### Hybrid Shading [17:08]
**Transcript (timestamped):**
[17:08] For the shading setup of all of these objects, I use a hybrid approach
[17:12] where I would have two setups inside of one material, one for cycles and then one for Eevee.
[17:18] I did this so I could use Eevee to preview my scene.
[17:22] This allows me to see if the feel of the illustration was coming along well
[17:27] before having to do any compositing.
[17:29] And then I used cycles to get the sharpest shadows.
[17:33] Eevee, back in 4.1, I had the tendency to approximate the shadows
[17:38] returning undesired results for objects that were intersecting.
[17:42] Since I had many materials that needed the same shading,
[17:45] I did all the shading in one single uber shader node.
[17:50] And as you can see, it's being used 13 times here.
[17:52] So every material uses this shader because it simply has a color input
[17:56] that's based on the texture that we made.
[17:59] It does its shading and then that gets sent out to either Eevee or Cycles.
[18:03] Let's hop into the node group to see what kind of magic it uses.
[18:06] Quite a bit of nodes, but don't let that scare you away.
[18:09] It's quite simple.
[18:10] The first block we can almost just completely ignore as it's just aligned
[18:14] to this specific scene.
[18:15] It creates some fake amine occlusion in corners based on some math.
[18:19] So it's not even real amine occlusion.
[18:22] Let's just focus on the Eevee side of things for now.
[18:24] So right here I have this basic Eevee Tune shader.
[18:28] All it does is we take a Diffuse BSDF shader to RGB and a color
[18:32] ramp that to create a sharp shadow.
[18:35] It's a really simple trick and it often already does a lot of heavy
[18:39] lifting for MPR stylization.
[18:41] Then I mix it with a color to give the shadow a slight tint.
[18:45] And then I basically do the same for the fake amine occlusion that I have created.
[18:50] Then after the amine occlusion, I create a mist effect.
[18:54] And I do this using the Vue Z depth.
[18:57] And this is like a data pass that we can read out from the camera.
[19:01] And it just tells us how far away our pixels on the screen from the camera.
[19:07] With a map range, we could easily control where this mist has to show.
[19:11] So right now I have it set to 9 starting at 9 meters from the camera,
[19:16] all the way up to about 47 meters.
[19:19] So you can basically read this as a meters.
[19:21] And then I am mapping that from zero to zero dot one so that there's not like a
[19:27] whole lot of mist happening.
[19:28] It's just a little bit.
[19:29] And then I use that as a mixed factor to control where there is some
[19:33] slight bluish tints happening.
[19:35] And that serves as a little bit of atmospheric perspective to add some more depth to the scene.
[19:41] And that's basically it for Eevee.
[19:42] So this allows me to get a nice preview of what's happening without having to
[19:45] render anything or do any compositing.
[19:48] Now for the cycle shader, it's even more simple.
[19:51] Cycles already has a nice tomb base they have built in.
[19:55] And we can use that to create some hard shadows.
[19:58] So we simply send that out and that is the cycles shader.
[20:02] This, however, doesn't give us our texture or amine occlusion.
[20:06] So how do we get those to render as well?
[20:08] And now that's what AOVs are for.
[20:11] They're essentially custom channels we can render data to.
[20:15] In my case, I simply send out the texture color named as C diffuse.
[20:20] And I send out the amiclusion as CAL.
[20:23] In this case, I put a C in front, implying custom.
[20:28] These AOVs also need to be defined as view layer passes.
[20:31] I know this might seem a bit confusing now for beginners, but once we get into
[20:35] compositing, this will hopefully make more sense.
[20:37] They're essentially just extra data or like extra images that we can send out
[20:42] together with the main rendered image.


### Render Settings [20:45]
**Transcript (timestamped):**
[20:45] Since I don't want cycles to do any heavy calculations, it's important we limit
[20:50] the render settings.
[20:51] If I switch to cycles and then go to sampling, I set the max samples to one on
[20:57] both for the light pass.
[20:58] It's important that the total balance is set to zero.
[21:01] So you can see that there is no bounce lighting happening and we just have some
[21:04] sharp and clean shadows.
[21:06] On the EV side, it's just a nice to have, since this is just for preview sakes.
[21:10] I up the shadow resolution a little bit so that they also get sharper, but, you
[21:15] know, it's not as close as cycles.
[21:17] Another important aspect to make this whole pipeline efficient is the way that
[21:21] each frame gets exported during a render.
[21:24] In my workflow, I use multiple view layers.
[21:27] They are up here.
[21:28] These all render at the same time.
[21:30] The most important ones are the mesh and the line art.
[21:34] If I switch this view layer to mesh, you can see that the lines disappear and all
[21:41] of our custom AOVs are stored on this view layer.
[21:45] We have our custom amm inclusion and custom diffuse stored as value and color
[21:51] to mirror what we have set up in our shader.
[21:53] Then for the line art, I only want the line art to show, but I do want the line
[21:58] art to be blocked by objects that might occlude the line art.
[22:02] And what I can do for that is simply use a holdout mask.
[22:06] And normally blender doesn't show these icons, but if you switch these on using
[22:12] the restricted toggles, you can switch this one on and this will make sure that
[22:17] everything that's inside of this collection acts as a holdout.
[22:20] And what you might have noticed is that these switch on and off depending on
[22:23] which view layer I'm on.
[22:25] So that's the cool thing about view layers is that these settings respond to
[22:28] which view layer you're on.
[22:30] So on the mesh, you can see that there's no holdout and the grease pencil is
[22:35] switched off and then on the line art, almost everything is on, but these are
[22:42] set to holdout.
[22:43] And since the line art don't need to have any shader AOVs, they don't get
[22:48] stored on here.
[22:49] Now let's move over to the compositor, which we use to manipulate how the files
[22:53] get exported as multi-layer EXRs.


### File Output [22:57]
**Transcript (timestamped):**
[22:57] Once all of the view layers and vendor passes are set up, it's time to combine
[23:01] them all into an output that we can use for external compositing.
[23:04] My setup for this was pretty simple, but extremely useful.
[23:08] I created a file output node, which I had set to open EXR multi-layer.
[23:13] And basically what this does is it allows me to export this sequence or this image
[23:18] sequence as EXR files.
[23:20] And I can store multiple passes on this EXR file that I can then read out into
[23:26] software like After Effects or DaVinci to then sort of split these passes out
[23:31] again and then do with them, whatever I want.
[23:34] Here you can see our render layers and they are based on the view layers with
[23:40] all of their render passes.
[23:42] The first thing I would do is I would take the image from the mesh render layer
[23:48] and then turn it black and white.
[23:49] It already is black and white, but I just need a simple value.
[23:52] So I can store that as the shadow.
[23:54] Then I can use the alpha of that image to actually become the alpha of the color
[24:00] we're going to store and the color I'm basing off of our AOV, which is the
[24:04] C diffuse or custom diffuse AOV pass.
[24:07] So this is the color of all of the objects without any shading on it.
[24:13] It's just basic.
[24:15] It's like an Albedo map.
[24:16] And we're using that together with the alpha from the image, combine it into one
[24:23] and then it's our color pass.
[24:25] So we have the color and the shadow and then AO is just simply our custom AO
[24:30] pass that we created inside of the AOV and depth is just depth.
[24:35] And then since we have our lines on a separate view layer, they only need
[24:40] to use their alpha and that's it.
[24:43] And then I would send it to a specific local path on my folder structure
[24:48] and then it would render out as a nice OpenEXR image sequence.
[24:52] To keep things as accessible as possible, I translated the compositing


### Compositing [24:53]
**Transcript (timestamped):**
[24:56] step directly into Blender's compositor as Blender 5.2 comes with some better
[25:01] compositing notes.
[25:02] This setup essentially mirrors exactly what I have done inside of After Effects,
[25:06] but I won't go into too depth with this setup as it mostly is just personal
[25:11] preferences on settings.
[25:12] But I can show you the general idea of combining your render passes into a nice
[25:16] image to start out.
[25:18] We start all the way on the left where I import our image sequence,
[25:22] which is the EXR sequence that we have set up in our file output.
[25:26] And as you can see, we can see all of our render passes that we have set up
[25:29] in the file output node.
[25:31] There is the depth pass, which trust me, there is data there.
[25:35] I know you don't see anything.
[25:36] The shadow pass, I'm in occlusion, color and lines.
[25:41] So the first thing that I focused on were the colors and the shadows.
[25:46] I do some anti-aliasing first on the shadows, which makes them a little bit
[25:51] less harsh.
[25:52] If you look over here, you can see that this is with anti-aliasing and this is
[25:58] without, it's like pixel art.
[26:00] So you want those shadows a little bit smoother.
[26:02] Now there's a whole bunch of crazy math going on here, or at least it looks like
[26:06] that, but it's actually not that complicated.
[26:08] It's mainly just making sure that, for example, this shadow is masked by the
[26:14] alpha and then I multiply the shadow, or actually I invert the shadow and then I
[26:21] multiply it with a smaller value.
[26:23] And then I can use that to mix it together with the colors.
[26:27] So if we just follow over here, we have the color, AOV pass that we have
[26:32] exported, and then we mix that together with the shadow pass.
[26:37] And I involve a little color and I know this is a custom node, but essentially
[26:41] this is the same as a mixed color node.
[26:44] And then you just have your factor, which is controlled by the shadow pass.
[26:49] And then you have, as the A input basically is color.
[26:53] We can just do that right now.
[26:54] You can see color, this and then this.
[26:59] Oh, sorry.
[27:00] And this and you almost get the same output, but I wanted to have a little bit
[27:05] more control.
[27:05] So I made my own little custom node group.
[27:09] Then I basically do the same thing for the admin occlusion pass.
[27:13] So here you go.
[27:15] I have taken that pass and I've inverted it so that only the places where the
[27:21] admin occlusion has to be shown are bright.
[27:24] And then I multiply that with a lower value and then I combine it with the image.
[27:30] And then I wanted to brighten up the areas where there was no shadow.
[27:33] So if you look over here, what I basically did is invert that shadow mask.
[27:37] And then make it a little bit less intense.
[27:40] And then in the places where there is light being shown, it has a little bit of
[27:44] orange, a little bit of warmth to make it look like there is a sun shining.
[27:49] I just wanted to make that a little bit warmer.
[27:52] So this is before and this is after.
[27:56] Then once that is done, I added in some mist and this mist is done with our death pass.
[28:03] So this is pretty similar to the setup that we have done in Eevee.
[28:07] Where we take the depth value and then we first of all, in this compositing step,
[28:13] I actually multiply it with the alpha of the image so that nothing in the background
[28:18] gets any mist.
[28:20] Then I map range it and I map range it between a value of five and 90.
[28:24] And you can just see these as meters.
[28:26] So this is five meters from the camera and this is 90 meters from the camera.
[28:30] And everything between that gets mapped to from zero to one.
[28:34] And then I use a float curve to make the fall of a little bit more smooth,
[28:39] multiply that with a lower value.
[28:41] And then I use that as the mask.
[28:44] So everything that is bright up here, that gets a little bit more blue and
[28:47] everything that is in front doesn't get any of that.
[28:50] And this is the result.
[28:51] So here is before and here is after.
[28:55] Sweet.
[28:56] Now, as you can see, the sky is still transparent.
[28:59] So what I did is I exported the sky into a separate pass that just made things a
[29:05] little bit more easy in my setup.
[29:08] And then I combined that with an alpha over.
[29:10] So everything that has alpha gets the background and everything that's not just stays as is.
[29:16] Now we still need to add in the lines, which is, I think, one of the most important parts.
[29:22] So I do that with an alpha over as well.
[29:25] And I actually try to do some displacement on those lines, but I didn't really like how
[29:31] that looks.
[29:32] But just to show you how it went, I have the line pass over here.
[29:36] And then you can just do whatever you want with this line pass.
[29:39] And then I added in some anti-aliasing again, because as you can see, the it just makes
[29:44] those lines a little bit more smooth.
[29:46] And then I combine it with the image using the alpha over.
[29:50] There it is.
[29:50] Nice.
[29:51] And then as a final little detail, I like to make the background a little bit more blurry.
[29:57] So here you can see with a de-focus node, which is a super cool node, you can make it so that
[30:02] the background kind of gets this depth of field effect in post without having to do that in
[30:07] camera.
[30:08] So just make sure that the lines and the colors and the shadows all get treated the same with
[30:14] the depth of field.
[30:16] But there was a little slight caveat to this.
[30:18] I always need to make sure that the lines in the foreground don't actually get caught by this
[30:24] depth of field, because we have to use a depth map for this to work.
[30:28] So, you know, we can obviously use our death map over here and then map range it just like we did
[30:35] for the mist or the fog.
[30:37] But I wanted to use different map range for that to have control over, over how that would work.
[30:42] I use an dilate or erode node.
[30:44] And you'll see what happens if I just quickly go to what happens after.
[30:49] Here you can see that the mask slightly expands and I do that because the line aren't slightly
[30:54] thicker than the mesh that lays underneath it.
[30:57] So the depth map needs to sort of cover for that so that the blurriness doesn't get
[31:04] overlapped or like it doesn't eat into the line.
[31:07] And I can show you what that looks like if we don't do this.
[31:10] So if I quickly mute this node, you can see that these edges get very blurry and it's almost
[31:16] like as if the line art is not only on here, but it's also somewhere in the background.
[31:23] And I don't really like how that looks.
[31:25] So I just add this to quickly fix that.
[31:29] It's like a dirty fix.
[31:30] And there are still some issues here and you could, I guess, render these lines out in a
[31:36] separate pass and then use that to mask out what needs to be blurred or what not.
[31:42] But in this case, I did not just for this simple showcase.
[31:46] And then after some color correction, we have our final image.


### Outro [31:51]
**Transcript (timestamped):**
[31:56] I know that's a pretty convoluted pipeline of hacks, but that's what makes MPR so fun.
[32:01] You get total artistic control and you get to invent your own rules to break the traditional
[32:05] 3D look. And I must admit that for some shots, the setup got even crazier, like adding separate
[32:11] view layers to handle transparent slime and figure out whether the grease pencil lines
[32:16] have to be rendered in front or behind it.
[32:18] I really hope you found something useful in this breakdown that you can use for your own
[32:21] projects. If you try out any of these techniques, then please share it online and tag me on
[32:25] X or Instagram.
[32:26] I'd love to see what you make of it.
[32:28] And if you want to see how we can modernize or upgrade this exact 2D to 3D pipeline using the
[32:34] latest blender features, then let me know in the comments.
[32:37] Drop a like if you feel like this was helpful and feel free to subscribe if you don't want to
[32:42] miss the next deep dive.
[32:43] Thanks so much for watching and see you in the next one.



---

## Captured Frames

- [0:19] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_000.jpg
- [1:12] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_001.jpg
- [2:42] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_002.jpg
- [3:34] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_003.jpg
- [5:09] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_004.jpg
- [6:12] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_005.jpg
- [7:07] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_006.jpg
- [8:38] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_007.jpg
- [11:40] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_008.jpg
- [12:24] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_009.jpg
- [15:34] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_010.jpg
- [16:45] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_011.jpg
- [18:06] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_012.jpg
- [20:02] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_013.jpg
- [21:04] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_014.jpg
- [23:13] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_015.jpg
- [24:04] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_016.jpg
- [30:02] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_017.jpg
- [31:46] tutorials/frames/my-stylized-blender-npr-pipeline---noxious-shot-breakdown/frame_018.jpg

---

## Structured Notes

### Core Technique
A complete 2D-illustration-to-3D-render NPR (non-photorealistic rendering) pipeline used on the short film Noxious: hybrid 2D/3D layout, a Geometry Nodes trick that offsets hand-drawn Grease Pencil surface curves off the mesh to kill flickering, texel-density-aware UV/projection-mapping + texture-paint cleanup, a dual EEVEE/Cycles "uber shader" for fast preview + crisp final shadows, AOV-driven custom render passes, and a full compositing breakdown (mirrored in both After Effects and Blender 5.2's compositor) that reassembles color/shadow/AO/depth/line passes into the final stylized image.

### Summary
Kay Hilman (channel: Cy) breaks down one real shot from Noxious end-to-end, in Blender 4.1 (as used in 2023-2024 production). It starts from a hybrid 2D/3D layout process — alternate between illustrating and blocking out geometry until the whole shot's silhouettes exist in 3D, keeping colors/shadows/lines as separate illustration layers so they map cleanly to later steps (frames [0:19], [1:12]). Grease Pencil then draws line art on top of that geometry via a Collection Line Art modifier (set to Screen Space so line thickness stays consistent regardless of camera distance, plus forced backface culling — frame [3:34]), but drawing curves directly on the surface causes camera-motion flicker; a custom Geometry Nodes group ("Curve Offset") fixes this by resampling the curve, converting it to a mesh, sampling the nearest surface point/normal via Geometry Proximity against a duplicated+expanded copy of the target mesh, and snapping the curve to that offset surface instead of the literal mesh (frames [5:09]-[8:38]). Coloring uses a texel-density strategy: foreground objects get individual materials/textures for pixel budget, background objects share one. Every object gets two UV maps — a normal bake-target UV and a camera-projected UV driven by a UV Project modifier pointed at the animation camera — but projection alone breaks badly once the camera moves around geometry (frame [12:24]), so the fix is to join texel-density-matched objects, give each material a fresh 4K texture sampled from the projected color, then use Texture Paint's Clone Brush (Line stroke method) to "spray" the projection onto the real UV in one pass and hand-paint only the areas the camera actually sees (frames [15:34]-[16:45]). Shading uses one reused node group with parallel EEVEE and Cycles branches: EEVEE gets a Diffuse BSDF → Shader to RGB → Color Ramp "toon" trick for a hard shadow edge, tinted, plus fake AO and a Z-depth-driven mist/atmospheric-perspective effect for fast preview (frame [18:06]); Cycles uses the built-in Toon BSDF for the sharpest possible shadow edge and gets its color/AO fed back in via custom AOVs (`C_diffuse`, `C_AO`) since the Toon BSDF alone can't carry texture data (frame [20:02]). Render settings are deliberately starved (Cycles max samples = 1, total bounces = 0) so shadows stay crisp and cheap, contrasted directly against an unlimited-bounce Cycles render (frame [21:04]). Multiple View Layers render simultaneously — a Mesh layer carrying the AOVs and a Line Art layer that uses per-collection Holdout toggles so line art is correctly occluded by geometry — and a File Output node bundles everything into a multi-layer OpenEXR (Color/Shadow/AO/Depth/Lines, frame [23:13]) for external compositing. The compositing breakdown (mirrored into Blender 5.2's compositor, frames [24:04]-[31:46]) layers: anti-aliased shadow pass multiplied/inverted onto the AOV color pass, a similarly inverted+brightened AO pass, a warm "sunlit" tint in non-shadowed areas, Z-depth-driven mist via Map Range + Float Curve, a separately-rendered sky pass composited with Alpha Over, the line pass composited last (also anti-aliased) via Alpha Over, and a final Defocus node for background depth of field — using a dilated/eroded depth mask so the blur doesn't eat into foreground line art.

### Key Steps
1. **Hybrid 2D/3D layout** — start each shot with a rough 3D blockout (+ a sun light as a shadow/occlusion reference) to ground the illustration, then alternate between illustrating parts of the scene and blocking/modeling them in 3D until every silhouette in the final illustration exists as real geometry. Keep the illustration's colors, shadows, and line art as cleanly separated layers so later steps (Grease Pencil reference, projection color source) can read them independently.
2. **Set up the Grease Pencil Collection Line Art modifier** — Shift+A → Grease Pencil → Collection Line Art, targeting a single top-level "Mesh" collection containing everything that should generate lines, with sub-collections for organizing individual curve sets. In the modifier: change Strokes space from World Space to **Screen Space** (so line thickness reads consistently near/far from camera) and set thickness (author used 3); under Geometry Processing, force **Backface Culling**. View with Material or Flat shading to see the resulting silhouette (frame [3:34]).
3. **Draw surface lines with the Curve tool** — in the target curves collection, add a Bezier curve, delete its default points, open the sidebar's Draw tool with Surface mode enabled, and draw directly onto mesh surfaces. Raw surface-drawn curves clip through geometry and flicker under camera motion, motivating the offset trick below.
4. **Build the "Curve Offset" Geometry Nodes group** (frames [5:09]-[7:07]): Resample Curve (mode: Evaluated, to drop Bezier handles and work on raw vertex positions) → Curve to Mesh (Grease Pencil in 4.1 only reads mesh, not curves directly) → feed in a **Collection Info** node (Instances output) pointed at the target surface collection → Realize Instances (needed since collection objects come in as instances) → take that mesh's Normal and **Set Position** to offset it outward along its own normals by a controllable Scale value (creates an invisible, inflated "shell" copy of the surface) → **Geometry Proximity** (Source Position: Faces) against that offset shell returns the closest-surface position for every point on the drawn curve → Set Position on the curve to snap it to that returned position. Expose the offset amount and the target collection as **Group Input** sockets so they're adjustable per-modifier instance without editing the node tree.
5. **Draw the full surface line-art pass** — with the offset modifier live, keep drawing curves in Edit Mode; they now stick to the surface with a small, tunable standoff instead of clipping/flickering. Organize curves into sub-collections per asset (e.g. per prop) so surface detail can be toggled on/off independently — useful for isolating problem assets or checking the underlying 3D form (frame [8:38]).
6. **Cluster objects by texel density before texturing** — group nearby/foreground objects that need high pixel resolution into their own material+texture; group distant/background objects to share a single material+texture. Objects in the same texture cluster must share one UV map, since they'll share one texture.
7. **Set up dual UVs + camera projection** — give every object two UV maps: a standard bake-target UV (any regular unwrap) and a second **projection UV** created via the **UV Project** modifier (UV Map target, Aspect X/Y matching the render's aspect ratio e.g. 16:9, Projector = the shot's animation camera — frame [11:40]). Feed the flat 2D illustration (color-only, no line art/shading) into a material using the projection UV to preview the projected result; note that projection looks correct only from the camera's exact view — rotating around the object reveals heavy stretching/breaking (frame [12:24]), which is expected and handled in the next step.
8. **"Spray-paint" the projection onto real UVs via Clone Brush** — Ctrl+J join the texel-density-clustered objects into one mesh (materials stay per-original-object). For each material, create a fresh image texture (author used 4K) sampled from that material's dominant color to save later fill time, and assign it as the active texture in Texture Paint mode with Flat viewport shading. Switch to the **Clone brush**, set Clone Source to "paint slot," pick the projected color texture as the clone source, and set Stroke Method to **Line** (single one-shot drag) to bake the camera-aligned projection onto the real UV in one pass per object (frame [15:34]). This reads as strictly better than baking-based projection mapping because the result is visible and paintable immediately.
9. **Hand-paint the seams** — switch to regular Paint mode, Shift+X to sample a nearby color, and manually fix only the areas actually visible from the render camera; ignore stretching/artifacts on unseen backsides — don't spend time perfecting geometry the camera will never see (frame [16:45]).
10. **Build the dual EEVEE/Cycles "uber" shader node group** (used identically across every material, ~13 instances in this shot): an EEVEE branch using **Diffuse BSDF → Shader to RGB → Color Ramp** for a hard toon shadow edge (tinted via a Mix Color node), a matching fake-AO pass (same Shader-to-RGB trick applied to a manually-baked-in AO approximation, not real ambient occlusion), and a Z-depth-driven mist effect (Map Range on the camera's Z-depth pass, e.g. 9m-47m mapped to a 0-0.1 mix factor) tinting distant areas slightly blue for atmospheric perspective (frame [18:06]). A separate Cycles branch uses the built-in **Toon BSDF** (Diffuse mode) directly, since it already produces the sharpest hard shadow available — but it doesn't carry texture color or AO, so those are exported separately via AOVs.
11. **Export color/AO through custom AOVs** — since the Cycles Toon BSDF discards texture/AO info, add **AOV Output** nodes named e.g. `C_diffuse` (custom diffuse/albedo) and `C_AO` (custom AO), and define matching AOV entries as View Layer passes so they render out alongside the beauty pass (frame [20:02]).
12. **Starve the render settings deliberately** — in Cycles sampling, set **Max Samples to 1** and **Total (light) Bounces to 0** so there's no bounce lighting and shadows stay perfectly sharp/cheap (compared directly against an unlimited-bounce Cycles render at frame [21:04]); on the EEVEE side (preview-only), just bump shadow map resolution a bit for a closer (not identical) preview match.
13. **Split rendering across View Layers with Holdouts** — run a Mesh view layer (carries all the custom AOV passes, Grease Pencil hidden) and a separate Line Art view layer simultaneously. On the Line Art layer, use the Outliner's restriction-toggle column to mark occluding collections as **Holdout** so line art is correctly hidden behind geometry that should occlude it — holdout toggles are per-view-layer, so the same collection can be holdout on one layer and normal on another.
14. **Bundle passes into multi-layer EXR** — a **File Output** node set to OpenEXR MultiLayer combines Color (AOV diffuse pass, alpha-masked by the black-and-white Mesh-layer image converted via RGB-to-BW), Shadow, AO (from the AOV), Depth, and Lines (Line Art layer's alpha only) into one image-sequence output for external compositing (frame [23:13]).
15. **Composite the passes** (mirrored between After Effects and Blender 5.2's compositor, frames [24:04]-[31:46]): import the EXR sequence and pull out its named passes → anti-alias the shadow pass (smooths harsh pixel-art-like edges) → invert + multiply-down the shadow to use as a mix factor combining it with the AOV color pass → do the same invert/multiply/combine for the AO pass → invert the shadow mask again and warm/brighten the lit areas slightly for a "sunlit" feel → build mist from the Depth pass (multiply by image alpha first so background doesn't get mist, Map Range e.g. 5m-90m, then a Float Curve for a smoother falloff, mixed in as a light blue tint) → composite a separately-rendered sky pass behind everything with Alpha Over → composite the anti-aliased line-art pass on top with Alpha Over → finish with a **Defocus** node for background depth-of-field, driven by the depth pass but expanded slightly via **Dilate/Erode** so the blur radius doesn't eat into foreground line art edges (visibly wrong without this fix, frame [30:02]) → final color correction pass (frame [31:46]).

### Nodes / Settings
- **Grease Pencil → Collection Line Art modifier**: Strokes → Screen Space (not World Space), Line Thickness, Geometry Processing → Force Backface Culling.
- **Custom "Curve Offset" Geometry Nodes group**: Resample Curve (Evaluated) → Curve to Mesh → [Collection Info (Instances) → Realize Instances → Set Position (offset along Normal, scale-controlled)] → Geometry Proximity (Faces) → Set Position (snap curve to proximity result); Group Input sockets for Offset amount and target Collection.
- **UV Project modifier**: UV Map target, Aspect X/Y (match render aspect, e.g. 16:9), Projectors = animation camera.
- **Texture Paint — Clone Brush**: Clone from paint slot, Stroke Method = Line, for one-shot projection-to-UV baking.
- **Shader node group (dual-engine)**: EEVEE branch = Diffuse BSDF → Shader to RGB → Color Ramp (toon shadow) + Mix Color (tint) + fake-AO (same trick) + mist (camera Z-depth → Map Range → mix factor); Cycles branch = Toon BSDF (Diffuse mode); routed to separate Cycles/EEVEE sockets on a Group Output / Material Output.
- **AOV Output nodes** (Cycles only): custom `C_diffuse`, `C_AO` passes, matched by View Layer Passes entries.
- Cycles sampling: **Max Samples = 1**, **Total (light) Bounces = 0** for hard, cheap shadows.
- **View Layers**: separate Mesh and Line Art layers rendered simultaneously; per-collection **Holdout** restriction toggle (per-view-layer) to occlude line art correctly.
- **File Output node**: format = OpenEXR MultiLayer; inputs Color, Shadow, AO, Depth, Lines.
- **Compositor**: Separate Color/Combine Color/RGB to BW (alpha prep), invert+multiply combine tricks for shadow/AO, Map Range + Float Curve (mist and depth-of-field masks), Alpha Over (sky pass, then line pass), **Defocus** node + **Dilate/Erode** (expand depth mask so blur doesn't eat into line art).

### Difficulty
Advanced (assumes comfort with Geometry Nodes, custom AOVs/View Layers, and node-based compositing; not a beginner Grease Pencil tutorial)

### Blender Version
Blender 4.1 (explicitly stated as the production version used in 2023-2024; the compositing section is demonstrated a second time in Blender 5.2's compositor, noted as having "some better compositing nodes" — author says a full 5.2+ pipeline modernization pass is a possible future video)

### Tags
grease-pencil, geometry-nodes, npr, non-photorealistic, line-art, uv-projection, texture-paint, shading, cycles, eevee, aov, compositing, render-passes, pipeline, advanced

---

## Related Tutorials
- [Blender Secrets - Draw Grease Pencil On Surfaces (without offset distance issue)](blender-secrets---draw-grease-pencil-on-surfaces-without-offset-distance-issue.md) — shares modelling, procedural; a shorter, more general take on the exact same problem (surface-drawn Grease Pencil clipping/flickering) that this video solves with its custom Curve Offset Geometry Nodes group — good side-by-side comparison of approaches.
- [New Compositing Effects in Blender 5.2!](new-compositing-effects-in-blender-52.md) — shares compositing, procedural, rendering, cycles; covers the newer compositor nodes this video's author references when re-implementing their After-Effects-original compositing graph natively in Blender 5.2.
- [Daily Blender Tip 99 - Drawing in 3D with Grease Pencil and Converting to Mesh](daily-blender-tip-99---drawing-in-3d-with-grease-pencil-and-converting-to-mesh.md) — shares the Grease-Pencil-to-mesh conversion concept underlying the Curve to Mesh step of this video's offset node group.
