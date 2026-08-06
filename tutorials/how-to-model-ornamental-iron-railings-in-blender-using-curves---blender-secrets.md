---
title: How to model ornamental iron railings in Blender using Curves - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=_1OLudY5qQY
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 5 (explicitly named: \"the new array modifier from Blender 5 with the curve method\")"
tags: [procedural, modelling, organic, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/how-to-model-ornamental-iron-railings-in-blender-using-curves---blender-secrets/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How to model ornamental iron railings in Blender using Curves - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=_1OLudY5qQY)
**Author:** Blender Secrets
**Duration:** 37m33s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this tutorial we'll be creating this kind of cast iron ornamental railing from start to finish.
[0:05] If you're interested in learning all about curves and modeling ornamental detail,
[0:09] check out my Blender Secrets book with over 2000 pages of Blender tips.
[0:13] The link for that is in the description or on the card that you will see on the screen now
[0:17] and in the pinned comment.
[0:19] And now let's look at how to make this kind of cast iron railing.
[0:22] I recommend starting with either a reference image or if you don't have a reference image,
[0:28] at least make a quick annotation.
[0:30] So let's do that real quick.
[0:31] I'm going to go to the side view, I'm just three for the right orthographic view.
[0:37] And I'm just going to press D so that I can draw an annotation.
[0:41] So I just want to have this kind of general curly shape.
[0:44] Let me just erase part of that.
[0:47] What I want actually is that it is flat at the bottom.
[0:52] Maybe something more like this.
[0:54] I'm just going to erase this part.
[0:57] So yeah, a really crappy quick drawing, but just to get the idea.
[1:02] And maybe actually I want it to be a bit longer here.
[1:07] Something like this.
[1:09] As long as here it is on the same plane because it will hit the wall there.
[1:14] So to create this shape, I will add a curve.
[1:17] So shift A, the basic curve, as you can see already has kind of that shape that we need.
[1:23] So I'm just going to rotate it on the y-axis.
[1:25] I can press minus to flip the direction and enter back to the side view.
[1:32] And let's move this and adjust the handles.
[1:38] You can rotate it and you can move it.
[1:41] And let's just select all right click and sub the fight.
[1:45] That creates another control point.
[1:47] And actually the annotation makes it a bit difficult to see the
[1:52] black curve on the dark gray background.
[1:54] So let's change that.
[1:56] Let's go to view and let's go to annotations.
[2:01] And this is our annotation, as you can see.
[2:03] And we can just change the opacity to super low, something like point one or point two.
[2:09] Then we can see the curve a bit better.
[2:11] And we can change the background to be a little bit less dark gray if you want.
[2:16] So just go to background, custom, and then you can change it here.
[2:20] You can make it darker or lighter if you want.
[2:23] So let's make it a little bit lighter.
[2:25] And let's see, that makes our curve easier to see, as you can see.
[2:30] And here we clearly need more details.
[2:32] I'm going to select both of these and right click and sub the fight.
[2:36] That gives us one more here.
[2:38] I'm just going to sub the fight here.
[2:42] And move this one down.
[2:44] And then here we need a few more curves.
[2:47] First, let me just move this handle in.
[2:51] Now you can extrude by pressing E.
[2:56] And I'm just going to do that.
[2:57] Or you can hold control and right click.
[2:59] That also extrudes.
[3:01] So let me just do that and just control click here.
[3:05] And let me rotate it a bit.
[3:07] Control and click.
[3:09] And now to fix the result, you can select these vertices and scale them up or down with S,
[3:14] rotate them with R and move them with G.
[3:17] And here it looks like I, because I was showing the extruding and all that, I accidentally created
[3:23] one too many points.
[3:25] So when it happens, you can just press control X to dissolve it.
[3:29] And then you just get the one that is left over.
[3:38] So that's just a bit of fine tuning.
[3:41] And here I want to have a nice round shape.
[3:45] So what I'm going to do is I'm going to add a curve circle that's already nice and round.
[3:51] And just rotate it and put it here.
[3:56] And we can just use that to see if our curve is nice and round.
[4:00] So for example, here it could be a bit better.
[4:05] And that just serves as a kind of reference for the roundness of the curve there.
[4:11] And I can just delete that reference.
[4:13] And let's remove this annotation as well.
[4:16] We don't really need it anymore.
[4:18] And I just want to make sure that on this line here, the curves meet the curve.
[4:23] And I can just move it around and move it around.
[4:26] And I can just move it around and move it around.
[4:28] And I can just move it around and move it around.
[4:31] And here the curves meet the wall.
[4:34] So I'm just going to move this back.
[4:37] And here, here, this one, I'm just bringing that in.
[4:41] I'm just going to select this, scale it to zero on the z-axis,
[4:46] and then just move it down slightly.
[4:49] And I'm not really happy with the shape here yet.
[4:52] So I'm just going to fine tune it a bit.
[4:54] And so after tweaking the curve a bit more, we get something like this.
[5:05] Now, obviously, this is infinitely thin.
[5:08] It's just a curve, and we need to give it some thickness.
[5:11] Now, there's a simple way to give thickness to curves.
[5:14] And that is in the geometry here.
[5:17] You can just give it depth.
[5:20] But that is always going to be around.
[5:23] It says so here after all.
[5:25] So let's just leave it at zero, and let's create a bell object instead.
[5:29] And so what I'm going to do is I'm going to press Shift A,
[5:33] and I'm going to add a mesh plane.
[5:36] So cut it down a bit to the thickness that you want to give to the curve.
[5:40] And let's move it out of the way so that it is not overlapping here.
[5:44] Then it's just a bit easier for us to see what we're doing.
[5:47] And I'm going to go to Edit Mode, and I'll switch to Vertex Selection Mode
[5:51] by pressing 1, and I'll press X and then choose Only Faces.
[5:55] So I'm not going to delete faces that will just make everything disappear,
[5:59] but only faces that way we keep the vertices.
[6:02] Now, I still cannot pick this object as the bevel curve,
[6:06] because it is not a curve.
[6:08] It is a mesh, so we need to convert it to a curve.
[6:11] But first, I want to show you what would happen if we were to create a curve.
[6:14] First, I want to show you what would happen if we were to add a Subdiv modifier to this.
[6:20] So with Ctrl 2, I added two levels of subdivision, and it is now very round.
[6:25] And we don't want it to be round.
[6:27] We want it to be kind of square, but with some nice beveled edges.
[6:32] So what I'll do is I'll select all these vertices,
[6:34] and I'll press Shift, Ctrl, and B to bevel.
[6:38] And I'll just left click, and then here in this panel, we have some options.
[6:43] First, I want to have two segments, and I want to set the profile shape to one.
[6:48] That way it is more sharp at the corners.
[6:51] And now if we were to add two levels of subdivision,
[6:53] you can see that the corners are a bit beveled.
[6:57] They're not as round and they're not perfectly sharp either.
[7:00] So now we have a nice bevel object, and I can just remove this.
[7:04] I just need to convert this to a curve.
[7:06] So to do that in object mode, right click and convert to curve.
[7:11] And now as you can see, we still have those vertices, but it is a curve object.
[7:16] So now I'm going to go here and through the curve panel and in the bevel object,
[7:20] not the taper object.
[7:22] Be careful, that's a big difference.
[7:25] We choose the plane it's called, but let me just rename it to bevel object,
[7:30] just to keep things clear.
[7:31] So now this bevel object has been entered in this field here under the bevel object.
[7:37] Now if this doesn't look like this, but it is flat,
[7:40] it could be that for example, this object is differently rotated.
[7:45] And then you just need to rotate it on the x axis 90 degrees
[7:50] and apply the rotation.
[7:51] Then you will get something like this.
[7:53] If it is all red like this, that is because face orientation is enabled,
[7:58] which shows us the flipped faces.
[8:01] In that case, take the bevel object and rotate it 180 degrees and apply the rotation.
[8:08] That flips the faces on this object.
[8:11] And you can always also apply the rotation and scale on this object,
[8:16] but it won't really make that much difference.
[8:18] Now here we still have a hole.
[8:20] If we click on fill caps, we fill those holes or caps.
[8:25] And also here, as you can see, that hole has been filled.
[8:31] And now we have our nice curve with thickness.
[8:34] And as you can see, it has a nice bevel going.
[8:38] We actually have quite a lot of resolution on this curve.
[8:41] So we can probably reduce that a bit.
[8:44] Maybe not too much, but let's maybe set it to 10.
[8:49] And we can add a sub-diff modifier to it with two levels.
[8:54] And that's shaded smooth also.
[8:57] Now it's very nice and smooth.
[9:00] Now I might want to have an array of this.
[9:02] So if I press shift D and an x move it and then repeat that a few times
[9:08] by pressing shift R, then we get a bunch of copies.
[9:11] The problem with that, of course, is if I tweak one of these now,
[9:15] it only tweaks that one.
[9:16] It won't affect the other ones.
[9:19] So it is a bit better to use an array.
[9:23] We can find that in our modifiers.
[9:26] And let's drag it up.
[9:28] And let me just drag this out a bit.
[9:31] So it's set to the line.
[9:32] I want five of them, but I want them to be
[9:36] a little bit further spaced from each other like this.
[9:40] Let's just make it minus five.
[9:43] And there you go.
[9:44] Now we have a nice array.
[9:46] And by the way, if you want this to look a bit more interesting,
[9:48] you can set it to a matcap.
[9:50] And you can choose, for example, this metal matcap.
[9:54] That already looks quite nice.
[9:56] Now I would like to add some horizontal railings to this as well.
[10:00] So just some spokes that go horizontally like this.
[10:04] And the challenge with this, of course,
[10:06] will be to follow the exact rotation of this curve.
[10:10] But fortunately, we can use the new array modifier for that.
[10:15] So first, let's create those horizontal spokes.
[10:18] So I'm just going to take one vertex here where it is nice and flat.
[10:21] Just take this one, shift T to duplicate it.
[10:24] I'm just going to move it on the y-axis for a moment
[10:27] so I can easily access it.
[10:30] And it's pointing in this direction now.
[10:32] So I'm just going to rotate it rz90 so that it's pointing in that direction.
[10:37] And I'm just going to press P to separate it from the rest of this stuff.
[10:42] And now it's become invisible,
[10:44] but it's actually still here in the outliner.
[10:45] And I'm just going to go to object mode.
[10:47] Let's call that the horizontal curve.
[10:49] And let's go back to edit mode.
[10:51] And I'm just going to extrude it on the x-axis all the way till there.
[10:55] As you can see, we have the array going on it in that direction.
[10:58] But don't worry about that for now.
[11:00] I'm just going to go to the top view and just make sure that we extrude it to where we want.
[11:08] And here I'm going to select this one, shift S cursor to select it,
[11:12] to have the cursor on that vertex.
[11:14] And then I'm going to set the origin to the 3D cursor
[11:17] just to make sure that the origin is exactly there.
[11:20] And I would recommend doing that when you're working with curves
[11:23] and things like arrays,
[11:25] that it is easier to align things the way you want
[11:27] if the origins are in predictable places.
[11:30] So I'm just going to move this on the y-axis
[11:32] so that it's kind of overlapping with this.
[11:34] And I want it to be a little bit smaller than these spokes.
[11:38] So I'm just going to go to edit mode, press A to select all,
[11:41] and then for the option panel and here, let's see, where are we?
[11:46] We have the mean radius.
[11:47] We can just decrease that a bit.
[11:49] I'm holding shift to make sure it doesn't go too fast.
[11:53] Just something like this so there is no overlapping geometry.
[11:56] And in object mode, we can move it back slightly.
[12:00] And in real life, this is pretty much what that would look like.
[12:03] Okay, so that's the first one.
[12:05] And I want it to be following this curve.
[12:09] So we still have the array modifier.
[12:11] And currently it is doing the wrong thing.
[12:14] But actually we can set it to curve.
[12:17] And then we can, it disappeared now,
[12:19] but we can select a curve object.
[12:21] And this is still a curve object.
[12:23] Let's see what happens.
[12:25] Nothing happens.
[12:26] And here in the modifier, we have some error messages.
[12:29] No curve selected input geometry has unsupported type mesh.
[12:34] And that is strange.
[12:35] I'm not sure if that is a bug in Blender,
[12:37] but this is definitely still a curve.
[12:39] It is not a mesh that I converted to a curve or something.
[12:42] But for some reason, it doesn't work.
[12:43] And I did some testing and it is because it has a bevel object.
[12:47] It has this bevel object, which was converted to curve from a mesh.
[12:52] So I'm just going to take this curve,
[12:53] shift T, duplicate it and move it to the side,
[12:55] where it's easier to select.
[12:58] I'm going to remove it's array modifier.
[13:00] And I'm just going to remove the bevel object.
[13:05] And the subdev modifier.
[13:07] You have to remove both of those
[13:09] so that you really have just a pure curve.
[13:11] There's nothing special about this curve.
[13:13] It's just a pure curve.
[13:15] And let's rename it.
[13:17] I just renamed it to guide curve so that it's easy to recognize.
[13:21] And I'll click on our horizontal curve.
[13:24] I'm just going to pick the guide curve.
[13:28] And as you can see, now the array is working.
[13:30] It's not working exactly the way we want, obviously,
[13:33] but it is working.
[13:34] And that's just possible only with this perfect curve,
[13:37] which doesn't have any modifiers or anything.
[13:40] So now we just need to change the rotation.
[13:43] So let me just experiment till we get what we want.
[13:47] This is almost what we want.
[13:48] They're following the general shape of the curve,
[13:52] but not its rotation.
[13:53] So let me just change the up axis.
[13:56] And that looks like that's the one that we want.
[13:58] And then all we have to do is change the amount.
[14:01] Oh, let's just say, actually, something like this is what I want.
[14:05] I don't want to have this one here.
[14:08] And what we can do is just take the guide curve
[14:12] and just select some vertices and delete them.
[14:15] And then we can just take this guide curve and move it on the x-axis
[14:19] so that those horizontal ratings are where we want them to be.
[14:24] And this one, let me see if we can move it now.
[14:28] So we probably have to take this guide curve
[14:32] and in edit mode, move this forward just a little bit on the y-axis like that.
[14:37] And yeah, that is the result that I was looking for.
[14:40] Before we continue, let's look at a couple of ways
[14:43] to put objects along a curve.
[14:45] Now, this is the way that we've been placing the horizontal bars so far.
[14:49] This is the new array modifier from Blender 5 with the curve method.
[14:54] And then we've picked our guide curve.
[14:56] And as you can see, these cubes, even though, as you can see in edit mode,
[15:00] they have plenty of geometry and they can definitely deform.
[15:03] They are staying rigid.
[15:05] They keep their original shape as they are placed along the curve.
[15:08] But here, in this other example, you can see that these cubes deform
[15:13] as they are placed along the curve.
[15:15] They are following the curvature.
[15:17] And you can see it especially when there's more curvature like this.
[15:21] And they're exactly the same cube,
[15:23] just the way they are placed along the curve is different.
[15:25] So we're using also the new array modifier, but it is just set to line.
[15:30] We're just pretending here that we don't have the curve option,
[15:33] which used to be the case in the old array modifier.
[15:36] And we're placing the offset along the x-axis.
[15:38] But we're also adding another modifier, the curve modifier,
[15:41] and it uses the guide curve.
[15:44] And by using an array modifier and a curve modifier separately,
[15:47] you get this effect where the object that is instant along the path has been deformed.
[15:53] Now, very important to make this work.
[15:55] This guide curve has the origin there,
[15:58] in exactly the same place where the origin of this cube is.
[16:02] That is pretty important for making it work.
[16:04] Both objects need to have their origin in the same location.
[16:08] So it's best that you just place,
[16:10] let me just turn off the modifiers,
[16:11] you just place the cube at the base of the curve.
[16:16] And then we are using the x-offset and the x-deform axis.
[16:21] And it's important that the rotation is applied of both of these objects,
[16:25] so that everything matches up.
[16:27] If you don't put these objects in the same location,
[16:29] it might look something like this, and it will be a bit confusing.
[16:33] So that's the best practice for using this.
[16:36] Now, why am I explaining these two methods?
[16:38] For the horizontal bars of the object,
[16:41] we want them to not deform,
[16:43] but for some details, we do want it to follow the path shape.
[16:48] One more thing I need to tell you about this,
[16:50] is that the resolution of the curve is pretty important here.
[16:53] Let me just show you if I turn this down.
[16:55] You see that if the resolution of the curve is too low,
[16:58] then the deformation of the objects is quite ugly.
[17:01] So the more resolution you have there, the better.
[17:04] So now that we know the different ways to put an array along a curve,
[17:08] we can start adding those details in between the spokes.
[17:12] But first, I want to make those spokes a little bit thinner.
[17:15] So I'm going to select all of this,
[17:18] and I'll change the mean radius.
[17:20] And don't worry about the array getting messed up.
[17:24] We can easily fix that later.
[17:25] So let me just set it to 0.65.
[17:28] That seems like a good width.
[17:31] And the same for these horizontal ones.
[17:35] Let's go with 0.55.
[17:38] And then we just need to fix this array.
[17:44] Something like minus 7.7.
[17:47] And I'm just going to use the annotation tool to sketch something.
[17:53] And what I'm looking at is some reference material
[17:57] from a book that I have with ornament designs.
[18:05] Yeah, something like this is fine.
[18:08] And now I'm just going to shift A and add a single vert.
[18:14] We have to make sure we're in edit mode, single vertex selection mode.
[18:18] And where is it?
[18:18] It was probably created along where my 3D cursor is.
[18:23] And I'm just going to make sure that the annotation is not quite as strong
[18:27] so that I can actually see what I'm doing.
[18:29] And then I'm just going to extrude
[18:32] that one.
[18:35] And make duplicates and extrude that one as well.
[18:41] And we don't need that annotation anymore.
[18:43] And I'm just going to convert this to curves.
[18:47] And let's add two levels of subdivision.
[18:50] And we can start to kind of tweak this.
[18:57] And I'm just going to kind of tweak the shape
[18:59] and have proportional editing on.
[19:02] So after a bit of tweaking, this is the basic shape of the curve.
[19:28] And then we're just going to use the same bevel object.
[19:33] So I'm just going to go in here.
[19:36] And I'm going to go in bevel, choose object, and then pick the bevel object.
[19:43] And of course, we have to go into edit mode
[19:45] and change the radius because now it's way too big.
[19:48] Do something like this.
[19:51] Oh, and let's fill the caps.
[19:54] There you go.
[19:54] And of course, smooth shading.
[19:58] And that's better.
[19:59] And so let's try and put this where we want it.
[20:04] First of all, I am going to put the origin here.
[20:07] So I'll select the vertex, shift S cursor to select it.
[20:13] Set origin to 3D cursor.
[20:15] So now the origin is here.
[20:18] And let's select our guide curve.
[20:22] That one is here.
[20:23] And I'm just going to select this here vertex.
[20:27] Also cursor to select it.
[20:30] And I'm going to set the origin to the 3D cursor there.
[20:32] Fortunately, that didn't do anything else.
[20:36] And I'm just going to take this shift S selection to cursor.
[20:40] And let me just show you that a bit better.
[20:42] Selection to cursor.
[20:43] So now it is here and it is exactly in the same position.
[20:48] And let me just give this a name.
[20:50] So now this interior decoration piece and the guide curve have their origin
[20:55] exactly in the same place.
[20:56] And that's what we want.
[20:58] And so you remember from the previous lesson
[21:01] that now we have to give this first an array modifier.
[21:06] And let me just drag that up here.
[21:09] And we're not going to change anything right now.
[21:11] I'm just going to add also a curve modifier.
[21:16] And I'm going to pick from the outliner the guide curve.
[21:20] And so initially we get this, which is of course not what we want.
[21:25] So let's try some different orientations here.
[21:31] And this looks like it might work.
[21:34] But we don't want it on the X axis.
[21:38] We want this on the Z axis.
[21:41] So this generally will be the same as this.
[21:45] So if it's Z here, then it will be Z here.
[21:48] And if it's X here, then it will be X here.
[21:50] Okay, so let's move it over here.
[21:53] Let's just press G and Z and move it until it touches this part here.
[22:02] And then G and Z to move it up.
[22:06] And then I will actually I'm going to scale it up
[22:09] because what I want is for this first one to fit perfectly in here.
[22:15] And we are just going to have to scale it a bit
[22:19] and move it a bit until it fits perfectly.
[22:21] So what I want is to have these
[22:26] swirly parts touch the spokes.
[22:29] And I think we need to scale it up a little bit more.
[22:32] Something like this.
[22:35] Looks pretty good.
[22:36] Move it on the X axis as well.
[22:40] So that here it also fits perfectly.
[22:42] And then here we need to extend it a bit in edit mode.
[22:46] So just go to the original and select these and
[22:50] GZ just move them down a tad.
[22:53] And away they sort of come out of that spoke.
[22:57] So this looks very good to me.
[22:58] I'm just going to fix the array value here.
[23:02] And then the other ones should also start to fit perfectly.
[23:13] Let's add a couple more.
[23:16] And it seems to get buried a little bit.
[23:18] So maybe we need to adjust this value very carefully to something like that.
[23:24] And let's check here.
[23:25] Yeah, that looks pretty good.
[23:28] So now it fits perfectly within those spokes.
[23:31] And yeah, let's see what else.
[23:33] I kind of want to fix something here.
[23:36] Let me see if I go to edit mode.
[23:39] And let's go back to our original.
[23:42] So here it overlaps in a kind of ugly way.
[23:44] So I want to scale this down a tad.
[23:58] And this I'll make it a little bit smaller as well.
[24:04] And then I'm just going to add a mirror modifier to this.
[24:10] Let's bring that all the way to the top.
[24:13] And let's add a empty.
[24:15] Let's just add it in the world origin empty plane access.
[24:21] And let's use that as the mirror object.
[24:24] And then we can move that empty so that we can place the mirror exactly as we want.
[24:36] And another thing we can do is we can just shift D and duplicate this,
[24:40] move it on the X axis.
[24:43] And we can flip it around.
[24:45] And let's press R, Z, 180 on our numpad and enter.
[24:49] And then we can adjust placement of this.
[24:55] And then we have this result.
[24:57] So now we have these nice decorative elements inside.
[25:00] And I just want to fine tune this a little bit.
[25:03] I don't really like the way that looks.
[25:05] So I'm just going to go to edit mode.
[25:07] And let's go to the front or rear view.
[25:09] And we can go to X-ray mode and just kind of adjust this.
[25:14] And we can just turn off the array for a moment.
[25:17] Then it will go a bit faster.
[25:20] And this one, maybe we can just scale it to a very small point.
[25:25] I wouldn't recommend setting it to zero because then you get this kind of rendering error.
[25:30] So maybe 0.01 or 0.001.
[25:35] And then we kind of taper it like that.
[25:53] And maybe here we also just taper it to 0.001.
[25:59] And then we gradually taper it for the rest of it as well.
[26:04] And it gets well.
[26:05] We are tapering or you might as well do all of these points.
[26:13] First, no changes were made to this one.
[26:16] So I'm just going to delete it, shift D, and duplicate it on the X-axis.
[26:25] And we'll turn the array back on.
[26:28] So it's better to do changes in edit mode without having the array modifier turned on.
[26:34] That way it will go a bit faster.
[26:36] All right, so this is starting to look nice and detailed.
[26:39] So next I would like to add some decorations on the side.
[26:43] But before we do that, I want to make sure that we really fine tune the thickness of all of these individual elements.
[26:50] And right now we're using a single bevel object, this one, for the thickness of all of these.
[26:56] So of the side spokes, the horizontal spokes, and the surrounding bits in between.
[27:00] But to be able to control their shape and their thickness, I want to have three separate bevel objects.
[27:07] So let's call this one horizontal and then we'll make a duplicate.
[27:12] Then we call bevel object vertical.
[27:14] And then we make one more duplicate.
[27:18] Then we call bevel object swirls.
[27:20] So let's look at these first.
[27:22] I want to have these a bit flatter.
[27:25] So I'm just going to make sure we have the correct bevel object selected.
[27:30] You see the name while you're hovering over it when you're picking it.
[27:36] So let's pick the vertical ones.
[27:39] And let's adjust the shape a bit.
[27:40] So let's press S and Y.
[27:46] And as you can see, we are making it a bit flatter.
[27:48] Let me just do that really extremely.
[27:50] You can see it's becoming flat.
[27:52] I don't want it to be that flat.
[27:54] But just a little bit more flat, something like this.
[27:59] And then of course I need to adjust the horizontal ones as well.
[28:02] This already has the correct bevel object, which is this one.
[28:06] You can see the name here as well.
[28:09] And I'm going to press S, Y, and just very carefully adjust it.
[28:13] It looks like we have to scale in the X direction instead.
[28:17] If this is going very sluggishly, I recommend that you just temporarily turn off the array modifier.
[28:23] So something like this.
[28:24] I just wanted to fit in between the vertical spokes.
[28:27] That's all.
[28:28] And now for this one, let's pick the swirls bevel object.
[28:34] And let me just zoom in a bit.
[28:36] And I want to press S and Y.
[28:38] And let's see if that's the correct.
[28:41] No, we have to press S and X for the correct axis.
[28:46] And just make sure that they don't go too far out of this horizontal spoke.
[28:52] And it looks like this is about right.
[28:54] And that's just the adjustment I wanted to make.
[28:56] And I'm just going to delete this one and then shift D and move them on X to about here.
[29:03] And with that, I have adjusted their shape.
[29:07] And I'm just going to take these bevel objects.
[29:09] And I am going to stack these empty as well.
[29:12] And I'm going to place them in a new collection.
[29:14] So I press M in a new collection.
[29:16] And just call that control objects.
[29:19] And I'm going to turn that collection off.
[29:22] We don't need to see it.
[29:24] And we're just going to rename that to vertical curves.
[29:27] So we have the horizontal curve, vertical curve, guide curve, and the interior decoration.
[29:32] And so now let's draw the swirls on the side.
[29:34] So I'm going to go to the side view.
[29:36] And first, let's just use the annotation tool.
[29:41] So just by holding D, and I'm just going to roughly draw what I want.
[29:45] Sometimes it's easier to just use short strokes.
[29:49] And I want something that is roughly like this, but it needs to meet in the middle there.
[30:03] It's just a guide for drawing the curves.
[30:07] So I'm just going to go ahead and reduce the opacity of that.
[30:11] I just want to barely be able to see it.
[30:14] Otherwise, when I adjust the curves, it will be just a bit too difficult to see what I'm doing.
[30:18] And so I'm just going to add another curve.
[30:20] It doesn't matter.
[30:20] Just a busy curve.
[30:22] And let me just move it up here so you can see it.
[30:25] So this is the new curve.
[30:26] I'm going to tap into edit mode A to select all, X to delete vertices.
[30:31] So you can see there's nothing left, just the origin point.
[30:34] And let me just go back to the side view.
[30:36] And we are in edit mode.
[30:37] But here we have a draw tool.
[30:40] So not the annotate tool, but the draw tool.
[30:43] And this is only available when we have the curve selected in edit mode.
[30:47] So now what I'm going to do, because I have this curve pen tool,
[30:51] I can just draw curves, as you can see.
[30:54] And so I'm going to just use the annotation and just carefully draw what I had there.
[31:01] And it doesn't need to follow it perfectly because we can still adjust it.
[31:06] I don't need to do it fast.
[31:07] You can just really take your time.
[31:09] I am using a graphics tablet screen for this.
[31:12] I'm drawing on my screen, which is quite nice.
[31:16] I have to say, I did finally get used to using this kind of screen instead of a wake-up tablet.
[31:23] If you don't have that kind of screen or you don't have a wake-up tablet,
[31:25] you can just extrude vertices with your mouse.
[31:29] That's also fine.
[31:30] I just wanted to show you one more way to do this.
[31:34] And I'm going to click on select box.
[31:35] And first of all, with this method, sometimes Blender creates this kind of strange handles type.
[31:42] So what you really want is these kind of handles, just a Bezier handle.
[31:47] And you don't really want this.
[31:49] So what you can do is you can either select it and control X and dissolve it.
[31:53] And if you want to replace it, you can just subdivide these.
[31:56] And then we get the kind of handle that we want.
[31:59] Or rather than deleting and then replacing it, what you can do is just select it and press it.
[32:04] And then you can get this menu with handle types.
[32:09] And then what you want is aligned.
[32:12] Okay, so you get this kind of green handle and you can scale it up, rotate it,
[32:17] and just everything that you would normally do with that kind of handle.
[32:22] And so what we're going to do now is we're first going to quickly go and see that we have the right
[32:26] handles everywhere.
[32:27] It's pretty easy to see this kind of pinching that is not what you want.
[32:31] So V aligned, and then we just rotate it and scale it a bit.
[32:36] Whoops, don't scale it too far.
[32:39] But generally it does a pretty good job of automatically setting them all to aligned.
[32:47] And here's the last one.
[32:50] So now I'm just going to quickly adjust these.
[32:52] And I'm actually just going to delete this annotation so I can see even better what I'm
[32:57] doing.
[32:57] And I just want to make sure they're all nice and round.
[33:01] And it may be important to know that you can scale these handles and you can rotate them,
[33:06] but you can also select one of these ends and then just move with G.
[33:11] And that also scales it in and out.
[33:13] So sometimes you get it where it's like this, where one end is really short and the other is really long.
[33:18] You typically don't really want that.
[33:20] You want it to be kind of in balance like this.
[33:22] That way it's easier to control.
[33:24] And here it's a little bit difficult to create a nice bend.
[33:29] And it will be easier if you just select two of these and then
[33:33] subdivide.
[33:33] So right click and subdivide.
[33:34] And you have one more control point.
[33:36] The more control points you have, the more control you have, obviously,
[33:40] but also the more work it is to adjust them all.
[33:43] So you have to kind of find a balance there.
[33:52] I'm also making sure that it is all aligned with the edge here.
[33:57] You can see in the grid there's this light gray line.
[34:00] And I kind of want everything to touch that line.
[34:20] Okay, this is the result after fine-tuning the curve.
[34:24] You might notice that I extruded some more points here and there
[34:29] just to make the swirls a bit more swirly.
[34:32] And yeah, this is generally something that I'm happy with.
[34:35] And I'm just going to quickly go and rename it to side curves.
[34:42] Kind of take one of these control points, duplicate it,
[34:46] and call that the bevel object for the sides.
[34:50] Then we have some control over that as well.
[34:52] And let me just select it here in the busy curve bevel object field.
[35:00] And then we can start to play with this.
[35:04] So let me just scale it on the y-axis.
[35:08] And also on the x-axis.
[35:10] And something like this.
[35:12] Maybe we can be thinner.
[35:16] And of course, we need to fill the caps, not on this object, but on this object.
[35:21] And this kind of reveals where some places it is still not so perfect.
[35:27] So first of all, let me just add a sub-diff modifier to this that makes it a bit smoother,
[35:33] shade smooth.
[35:34] And then let's go back to the side view.
[35:37] And then we can do some final tweaking to make it look even better.
[35:42] Because of course, we don't want to overlap these here.
[35:44] So we just need to adjust the shape so that they're just kind of lightly touching.
[35:50] And that seemed like a lot of work.
[35:51] But this kind of final, just fine tuning is where things actually become good.
[35:57] Because here there's almost no control points.
[35:59] So I'm just going to set the fight this one more time so that I have a bit more control there.
[36:05] Same here.
[36:10] It's really the fine tuning where something becomes good.
[36:13] I'm doubling a bit in game design now.
[36:16] And there's a saying in game design.
[36:19] First 90% of making game is making it playable.
[36:22] And the second 90% is making it good or something along those lines.
[36:27] Which is just to say that it might feel like you're almost done when you've set up the very basics.
[36:33] But that's actually when the fine tuning starts.
[36:36] Then again, at some point you need to know when it's enough.
[36:40] And just let go.
[36:42] I mean, you can work on something forever and it will never be perfect.
[36:46] But it needs to be good enough at least.
[36:49] So this is the result.
[36:52] Let me just check how it's placed.
[36:55] All right.
[36:57] And I think we can just shift the NGP that.
[36:59] I mean, we could also use a mirror, but it's fine.
[37:03] We can more quickly just move it like this.
[37:07] And that's it for modeling this ornamental cast iron railing.
[37:11] If you're interested in learning all about curves and modeling ornamental detail,
[37:14] check out my Blender Secrets book with over 2000 pages of Blender tips.
[37:18] The link for that is in the description or on the card that you will see on the screen now.
[37:22] And in the pinned comment.
[37:24] Thanks a lot for watching.
[37:25] I hope you enjoyed the video and that you learned some new valuable techniques
[37:29] that you can use for your own creations.
[37:31] And I hope to see you in the next one.



---

## Captured Frames

- [0:41] tutorials/frames/how-to-model-ornamental-iron-railings-in-blender-using-curves---blender-secrets/frame_000.jpg
- [7:00] tutorials/frames/how-to-model-ornamental-iron-railings-in-blender-using-curves---blender-secrets/frame_001.jpg
- [9:50] tutorials/frames/how-to-model-ornamental-iron-railings-in-blender-using-curves---blender-secrets/frame_002.jpg
- [15:00] tutorials/frames/how-to-model-ornamental-iron-railings-in-blender-using-curves---blender-secrets/frame_003.jpg
- [22:15] tutorials/frames/how-to-model-ornamental-iron-railings-in-blender-using-curves---blender-secrets/frame_004.jpg
- [24:10] tutorials/frames/how-to-model-ornamental-iron-railings-in-blender-using-curves---blender-secrets/frame_005.jpg
- [30:40] tutorials/frames/how-to-model-ornamental-iron-railings-in-blender-using-curves---blender-secrets/frame_006.jpg
- [36:55] tutorials/frames/how-to-model-ornamental-iron-railings-in-blender-using-curves---blender-secrets/frame_007.jpg

---

## Structured Notes

### Core Technique
A full cast-iron ornamental railing built entirely from Curve objects: a custom beveled-square Bevel Object gives the curly main curve its metal-bar thickness, Blender 5's curve-mode Array modifier scatters straight/vertical spokes, a separate Array+Curve-modifier combo deforms decorative swirl elements to follow the main curve's shape, and hand-drawn Bezier curves (via the Curve Pen tool) become the side ornamentation.

### Summary
Frame 000 shows the very first step: an empty Right Orthographic viewport with the Annotate tool (D) active, about to sketch a rough reference curl shape freehand since no photo reference was used. Frame 001 shows the custom Bevel Object being built: a small square mesh plane with a Subdivision modifier (Catmull-Clark, 2 viewport levels) open in the sidebar — before the beveled-corner treatment that keeps it "square with nice beveled edges" rather than fully round. Frame 002 shows the payoff: five identical S-shaped curly bars viewed with a chrome/metal Matcap enabled (Matcap picker open), each showing the custom bevel's faceted-but-softened cross-section and an Array modifier in the sidebar — the base repeating railing unit. Frame 003 is the two-cube comparison demo from the "ways to put objects along a curve" explainer: a flat pink/blue-shaded cube (rigid, undeformed, Array modifier set to Curve method) on the left versus a similarly shaded cube warping to follow a curve on the right (Array set to Line + separate Curve modifier) — same geometry, different placement method, with the Array modifier's Curve Object field visible in the sidebar. Frame 004 shows an "Interior Decoration" swirl element mid-placement inside the vertical/horizontal spoke grid, its Array and Curve modifiers open in the sidebar (Curve Object: GuideCurve, Deform Axis) being scaled and positioned to nest perfectly between the spokes. Frame 005 shows the finished swirl-filled panel: repeating interior decoration curls running vertically inside the spoke grid, viewed from a slight low angle to show depth. Frame 006 shows the side-ornamentation curve being hand-drawn with the dedicated Curve Pen tool (visible in the left toolbar, distinct from the Draw/Annotate tool) over a faint blue annotation guide, in Right Orthographic Edit Mode — the resulting Bezier curve's Resolution Preview U and Geometry (Taper Object, Radius) fields visible in the sidebar. Frame 007 shows the fully assembled railing section: main curly bars, horizontal/vertical spoke grid, nested interior swirl decorations, and the hand-drawn side scrollwork all combined and subdivision-smoothed into the final cast-iron look.

### Key Steps
1. **Reference/plan:** in Right Orthographic view, use the Annotate tool (D) to freehand-sketch the target curl shape (or use a photo reference if available) — this is just a rough visual guide, not exact geometry.
2. **Build the main curl as a Curve:** Shift+A add a Bezier curve, rotate/flip its direction (minus key) to roughly match the sketch, then edit control points — move handles, Right-click > Subdivide to add more control points where more detail is needed, Ctrl+X to dissolve an accidentally-added point; lower the Annotation layer's opacity (View > Annotations) and lighten the viewport background (View > Background > Custom) for better contrast while tracing; optionally add a temporary Curve Circle as a roundness reference to check the curl reads as properly circular, then delete it once done.
3. **Give the curve thickness via a custom Bevel Object (not the curve's own Geometry > Bevel Depth, which only produces round cross-sections):** add a mesh Plane sized to the desired bar thickness, in Edit Mode delete only its faces (X > Only Faces, keeping vertices/edges), select all and Shift+Ctrl+B bevel with 2 segments and Profile Shape 1 for sharp-but-softened corners (test with a temporary 2-level Subdivision modifier to preview roundness, then remove it), then in Object Mode right-click > Convert to Curve to make it a valid Bevel Object.
4. **Apply the Bevel Object:** on the main curl curve, go to Curve Properties > Geometry > Bevel, set Object to your converted bevel mesh (careful: not the similarly-placed Taper Object field) — troubleshooting notes: if the result is flat instead of a solid bar, the bevel object may need a 90° X rotation (apply the rotation after); if it renders solid red, Face Orientation is showing flipped normals — rotate the bevel object 180° and apply rotation to fix; enable Fill Caps on the curve to close the open ends; reduce the curve's Resolution Preview U if it's needlessly dense, and add a Subdivision modifier (2 levels) + Shade Smooth for a polished result.
5. **Repeat the curl with a straight Array modifier** (Shift+D duplicate + Shift+R repeat is mentioned but discouraged since edits to one copy won't propagate) — instead add an Array modifier, set Count and a negative X Factor/offset to space multiple curls evenly; a metal Matcap makes the in-progress result easier to judge visually.
6. **Two ways to place objects along a curve (critical distinction):** (a) **Array modifier set to Curve method** with a Curve Object assigned — instances stay rigid/undeformed, following the curve's path positions only (used for the straight horizontal/vertical spokes); (b) **Array modifier set to Line + a separate Curve modifier** referencing the same guide curve — instances actually deform/bend to match the curve's curvature (used for elements that should visibly bow with the railing's shape). For method (b), both the instanced object and the guide curve must have their Origin at the same location (use Shift+S > Cursor to Selected, then Object > Set Origin > Origin to 3D Cursor, on a matching vertex on each) and have Rotation applied, or the deformation misaligns; a low-resolution guide curve produces visibly faceted, ugly deformation, so keep curve Resolution high for this method.
7. **Guide curve requirement for curve-mode arrays:** the Curve Object picked by an Array modifier's Curve method must be a "pure" curve with no modifiers, Bevel Object, or Subdivision applied to it — Blender throws a "No curve selected / input geometry has unsupported type mesh" error otherwise, even though the object genuinely is a curve, because its own Bevel Object (originally a mesh-turned-curve) confuses the check. Fix: duplicate the working curve, strip its Array/Bevel Object/Subdivision modifiers entirely, and use that stripped copy purely as a path reference (renamed e.g. "Guide Curve").
8. **Horizontal spokes:** take one flat/level vertex from the main curl, Shift+D duplicate, rotate it to point along the intended spoke direction, P > Separate by Selection to pull it into its own object; extrude (E) along the horizontal axis to the desired railing width; reduce its Bevel Object's Mean Radius so spokes read visibly thinner than the main curl bars; set its Array modifier to Curve mode referencing the (stripped) Guide Curve, adjusting the Array's "up axis"/orientation setting until the spokes' rotation follows the guide curve correctly rather than just its position.
9. **Interior decorative swirls between spokes:** sketch a fresh small swirl shape with a single vertex extruded/duplicated into a curl, convert to Curve, apply the shared Bevel Object then override its own Radius since scale differs; align its Origin to a matching guide-curve vertex (same 3D-cursor technique as step 6); add Array (Curve method) + Curve modifier (Deform Axis = Z, matching the guide curve's own up-axis) referencing the Guide Curve; scale/position it in Edit Mode and Object Mode until the swirl nests exactly between the spokes and its ends touch the spoke bars; extrude/adjust individual points afterward so the tips visibly emerge from behind the spoke rather than floating.
10. **Tapering and symmetry:** taper thin decorative tail-points down to a very small but non-zero scale (e.g. 0.001, never exactly 0 — a true-zero scale causes a rendering error) rather than deleting them, for a natural pointed end; use a Mirror modifier with a separate Empty as the Mirror Object (rather than the default local origin) so the mirror plane can be repositioned independently; alternatively, Shift+D duplicate a decorative element, flip it with R,Z,180,Enter, and manually reposition — faster for one-off placement than setting up a full mirror rig.
11. **Separate Bevel Objects per element category:** once several curve types exist (main/vertical spokes, horizontal spokes, interior swirls), duplicate the shared Bevel Object into three named variants (e.g. "Bevel Object Vertical," "Bevel Object Horizontal," "Bevel Object Swirls") so each category's cross-section shape/flatness can be tuned independently (S,Y or S,X to squash the bevel mesh flatter or thinner) without affecting the others — hover over the Bevel Object picker to confirm which curve is currently using which bevel by name; temporarily disabling a busy Array modifier while adjusting its Bevel Object's Edit Mode geometry keeps the viewport responsive.
12. **Organizing helper objects:** select all non-visible "control" objects (Bevel Objects, Empties, Guide Curves) and press M > New Collection (e.g. "Control Objects"), then disable that collection's viewport visibility to declutter the outliner/viewport once the rig is working.
13. **Hand-drawn side scrollwork:** sketch the target shape first with the Annotate tool at low opacity as a tracing guide; add a curve object, in Edit Mode select-all + X delete all vertices to leave just an empty curve, then use the dedicated **Curve Pen** tool (distinct from Annotate, only available with a curve selected in Edit Mode) to draw new Bezier points directly — works well with a graphics tablet/pen display, but mouse-based extrude-per-vertex works too; watch for Blender occasionally creating undesired "Vector" handle types instead of smooth Bezier handles — fix by selecting the point and Ctrl+X (dissolve, then re-subdivide) or press V for the Handle Type pie menu and choose Aligned; balance handle lengths on both sides of a point (drag one end with G) rather than leaving one long/one short, for predictable control; Right-click > Subdivide adds more control points on tricky tight bends, trading more manual adjustment work for more shape control. Iteratively fine-tune all curve handles — the author notes this final fine-tuning pass, not the initial blockout, is where the result actually becomes good.
14. **Finishing the side scrollwork:** duplicate one of its own control points to make a fourth dedicated Bevel Object for the side curves, scale it thin on both axes, enable Fill Caps, add Subdivision + Shade Smooth, then nudge individual curve points in X-Ray/front view so adjacent scroll loops lightly touch without overlapping; mirror or duplicate+flip to complete symmetric side panels.

### Nodes / Settings
- **Curve tools:** Bezier curve (Shift+A), Curve Pen tool (Edit Mode only), Handle Type pie menu (V: Aligned/Vector/Free/Automatic), Subdivide (Right-click), Extrude (E or Ctrl+RMB).
- **Curve Properties > Geometry:** Bevel > Object (custom Bevel Object, not Taper Object), Fill Caps, Resolution Preview U.
- **Modifiers:** Array (Count Method: Fixed/Fit Curve; Curve method with Curve Object field — Blender 5's new curve-mode array; classic Line method + separate Curve modifier for deforming instances; Relative/Constant Offset), Curve modifier (Deform Axis must match the guide curve's own up-axis), Subdivision Surface (Catmull-Clark, viewport levels), Mirror (custom Mirror Object via an Empty).
- **Mesh-to-curve bevel-object recipe:** mesh Plane → Edit Mode delete Only Faces → Shift+Ctrl+B bevel (2 segments, Profile Shape 1) → Object Mode right-click > Convert to Curve.
- **Alignment tools:** Shift+S (Cursor to Selected), Object > Set Origin > Origin to 3D Cursor — required to match origins between a deforming object and its guide curve.
- **Other:** Annotate tool (D, View > Annotations opacity), View > Background > Custom (viewport contrast), Matcap shading, M (Move to Collection, for organizing control objects), R,Z,180,Enter (quick 180° flip).

### Difficulty
Intermediate to Advanced (curve-based modeling, Array/Curve modifier interplay, and freehand Bezier drawing are all non-trivial skills combined here)

### Blender Version
Blender 5 — explicitly named ("This is the new array modifier from Blender 5 with the curve method").

### Tags
procedural, modelling, organic, intermediate, advanced

---

## Related Tutorials
No other extracted BlenderSecrets tutorials in this library currently cover curve-based Bevel Objects, the Array modifier's curve-mode, or the Curve Pen tool in similar depth.
