---
title: For Beginners: Easiest Modeling Technique (long version)
source: YouTube
url: https://www.youtube.com/watch?v=YCd_tS_3BTU
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/for-beginners-easiest-modeling-technique-long-version/
frame_count: 0
frame_status: pending-selection
---

# For Beginners: Easiest Modeling Technique (long version)

**Source:** [YouTube](https://www.youtube.com/watch?v=YCd_tS_3BTU)
**Author:** Blender Secrets
**Duration:** 37m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py for-beginners-easiest-modeling-technique-long-version <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] A year ago I posted this video, which shows the method of quickly creating a 3D model with Quad Topology.
[0:06] It's quite a simple technique, but I think because the video is quite short, a lot of beginners became confused.
[0:11] And that's why I've decided to make this a longer version with more explanation.
[0:15] So this video consists of two parts. First I'll go over the basics of every modeling technique used in the video.
[0:21] And then the second part is the modeling of the robot scene in a thumbnail with voiceover and duration.
[0:26] I just want to make sure you understand that this is just a fun modeling technique for quick ID generation.
[0:31] I'm not saying that this is how you should model robots or anything else.
[0:34] In fact, if you want to use a proper workflow, I recommend that you first create some drawings
[0:39] or a really rough blockout because drawing is the fastest way to create ideas.
[0:44] And that way you can quickly go through the bad ideas and then pick the good one
[0:47] without having invested lots of time in 3D modeling.
[0:51] Then you can create a 3D blockout. And for this blockout version,
[0:54] you can use all the modeling shortcuts and methods that you can come up with,
[0:58] like Booleans with terrible topology. It's all fine.
[1:01] And then as the final stage, you can start making the production ready model
[1:05] with proper topology and all that.
[1:07] So if you want to learn more about that entire workflow, check out my hard service modeling course.
[1:12] However, the method described in this video is also fine.
[1:15] And sometimes I think it's fine to just have some fun making 3D stuff.
[1:19] The advantage of this technique is that it's fun and fast and you get all quads topology.
[1:24] So it's easier to add some cool sci-fi details with alpha brushes in sculpt mode
[1:29] and to do things like adding panel cuts.
[1:31] Keep in mind that to make pro level 3D art takes many, many, many hours
[1:36] and there are no real shortcuts.
[1:38] So in other words, if you're looking to make a serious piece for your portfolio
[1:41] or for a game or animation that you're making,
[1:43] then definitely use the method from my hard service modeling course.
[1:47] And if you just want to have some fun and model a quick robot in less than an hour
[1:51] and learn some modeling basics while you're doing it, then keep watching this video.
[1:54] So with that long disclaimer out of the way, let's continue
[1:57] and look at all the modeling techniques used in this process.
[2:01] First of all, the way this works is by adding two different subdivision modifiers to a cube.
[2:06] The first one is set to simple and the second one is set to catmul-clark.
[2:12] Now some quick explanation about both of these algorithms.
[2:15] Catmul-clark is the default method of subdividing in Blender.
[2:19] It not only doubles the amount of geometry, it also makes the model more smooth.
[2:24] By default, Blender won't display all this new geometry,
[2:27] but if you disable optimal display, you can see it.
[2:30] However, I recommend that you keep optimal display turned on.
[2:35] The simple subdivision algorithm only doubles the amount of geometry without smoothing it.
[2:41] By combining these, you get this result.
[2:43] Note that it's important that the simple subdivision is above the catmul-clark one.
[2:48] You can see the difference if I swap them.
[2:50] Oh, and by the way, you can move modifiers in the stack
[2:53] by clicking on this and dragging them up or down.
[2:56] In object mode, right click on the cube and choose shade smooth.
[3:00] Now the model looks better.
[3:02] You can also click on the viewport shading dropdown and choose a matte cap.
[3:07] That way it looks a bit more interesting in the viewport.
[3:10] This is not a texture or a material, it only affects how you see things
[3:14] in the 3D viewport of Blender.
[3:17] When you increase the levels of the simple subdiv modifier,
[3:20] you'll get a more blocky shape.
[3:22] However, I recommend keeping it at a level of one
[3:25] and adding sharper corners later by adding geometry to them manually.
[3:30] Don't worry, we'll look at how to do that later in the video.
[3:32] By adding a mirror modifier, you make sure that whatever you do on one side
[3:37] also happens on the other side.
[3:39] However, it's always best to drag the mirror modifier to the top
[3:43] and enable bisect on the mirror modifier.
[3:46] Bisect basically adds a loop in the middle,
[3:48] although you don't see it with optimal display enabled,
[3:51] and it removes the other half so you don't end up with any overlapping geometry.
[3:56] Alternatively, you can add a loop cut with control R in edit mode
[4:00] and manually delete half of the object.
[4:03] If you do decide to delete half of the geometry,
[4:06] you don't need to use the bisect option.
[4:08] But in my example, I'm just going to use bisect.
[4:11] When you switch to edit mode, you can edit the geometry.
[4:14] However, as you can see in edit mode, you don't see only the smooth model,
[4:19] but also the original unsmoothed geometry.
[4:22] By enabling the on cage button, that's this button here,
[4:27] you can work directly on the smooth model in edit mode.
[4:30] Make sure optimal display is also enabled to make it look more clean
[4:34] and so that you're not distracted by all the extra geometry.
[4:38] Let's look at some basics of modeling.
[4:40] In edit mode, you can select vertices, edges, and faces.
[4:46] If you select a face and then press E, you can extrude it.
[4:51] You can also use the extrude tool from the tool panel for this,
[4:54] but I think it's worth learning these shortcuts.
[4:56] As extrude is such a common tool that you're going to be using it a lot.
[5:00] If you don't see the tool panel, press T to toggle its visibility.
[5:04] You can drag on it to expand it and to see the names of the tools.
[5:08] As you can see, extrude is a very powerful tool because it quickly adds more geometry.
[5:12] You just move the mouse to determine how far to extrude,
[5:15] and then you left click to confirm.
[5:18] But be careful, if you right click, you only cancel the transformation of the extruded part.
[5:23] In other words, you only cancel moving the extruded face, but not the extruding by itself.
[5:29] That means that you now have got the vertices that are in the same location as where you extruded from.
[5:33] So you've got double geometry in that case.
[5:36] So make sure you press Ctrl Z to undo if you want to cancel an extruded face.
[5:41] After extruding, you can scale down the selected extruded face,
[5:45] by pressing S and moving the mouse.
[5:48] Or you can rotate it by pressing R.
[5:51] This is especially useful in combination with one of the X's of the 3D world, the X, Y and Z axis.
[5:58] For example, press R and Y to rotate on the Y axis.
[6:03] Or R and X or R and Z.
[6:06] You can achieve the same by using the rotate tool and dragging the red, green or blue handles.
[6:13] A very similar tool is the inset tool.
[6:16] In fact, in some other 3D software, inset and extrude are just one tool.
[6:22] Press I and move the mouse.
[6:24] You've now created inset geometry.
[6:26] By pressing S for scale, you adjust its size.
[6:30] Or you can adjust the strangely named thickness value in this panel.
[6:34] By the way, if you adjust the depth value, you'll see that it's really the same as extrude.
[6:40] In fact, if you inset by pressing I and then press Ctrl and move the mouse,
[6:44] you actually extrude the selected face.
[6:47] If you select more than one face and inset it,
[6:50] you can toggle whether you want to inset both together or individually by pressing I again.
[6:56] Or you can toggle the individual box in the tools options.
[7:00] By the way, if you accidentally close this panel because you clicked somewhere, press F9.
[7:05] I recommend if you're a beginner that you use E for extrude and I for inset.
[7:10] And then later, when you're more experienced,
[7:12] you can just use the inset tool for both insetting and extrusion
[7:16] as it's a bit more advanced and has more options that way.
[7:20] Another very powerful tool is loop cut and slide.
[7:23] Usually this is referred to in tutorials as add a loop or add an edge loop
[7:28] because that's what it does. It adds a loop of edges.
[7:31] The keyboard shortcut for this is Ctrl R.
[7:34] You left click to confirm adding the loop of edges.
[7:37] And then you can move the mouse to position the new loop.
[7:40] Then left click again to confirm its placement.
[7:43] Here too, you can still adjust it in its own option menu.
[7:46] You can also add more than one loop by increasing the number of cuts either in this panel
[7:51] or after Ctrl R by scrolling the mouse wheel up.
[7:54] But in this video, we'll only ever add one loop.
[7:57] So just leave that number of cuts at one.
[8:01] Adding loops means that you have smaller faces to extrude
[8:04] and it also gives you more geometry to manipulate.
[8:07] For example, you can go to edge selection mode and select an edge
[8:12] or several edges by holding shift and then move them by pressing G.
[8:17] You can also use the move tool in its green, blue or red handles
[8:20] or press G and then X or G and Y or G and Z to move only on those axes.
[8:27] And you can also scale the selection with S and rotate with R.
[8:31] You can do the same thing with vertices by going to vertex selection mode.
[8:36] Adding loops is also useful for making edges sharper.
[8:40] The closer edges are together, the sharper that corner will be.
[8:43] That's how the smoothing algorithm works in subdivision modeling.
[8:48] When you've added a loop and you want to move it at some later point,
[8:51] the way to do so is by sliding it.
[8:54] To slide a loop, select the loop by Alt and Left clicking on it
[8:59] or go to select, select loops, edge loops and then press G twice.
[9:04] Now when you move the mouse, you slide the selected loop
[9:07] along the geometry that it's on.
[9:09] As you can see, sliding a edge loop makes the corners that it's moving closer to sharper.
[9:14] Just make sure that you don't bring it too close.
[9:17] If you want to remove a loop, select it with Alt and Left click
[9:21] and then press Ctrl X to dissolve it or go to mesh,
[9:24] delete, dissolve edges or just press the D on your keyboard and choose dissolve edges.
[9:30] Those are the very basics of modeling, but here are a couple more things.
[9:33] The loop tools extension is essential for modeling a blender,
[9:36] so make sure that you install it.
[9:38] You can find it in preferences by searching for the loop tools extension in the extensions tab.
[9:43] After installing it, you can right click on a selection in edit mode
[9:47] and for example, make it circular.
[9:49] Another super handy thing you can do with loop tools is easily flatten a selection.
[9:54] But if you want to flatten something along a specific axis,
[9:57] you can also press S to scale then the axis that you want to scale on
[10:01] and then zero on the numpad and enter.
[10:03] So for example, S, Z, zero and enter to flatten a selection on the Z axis.
[10:09] If you want to quickly create a nother piece of the model that already has all these modifiers,
[10:14] select a face or several faces and press Shift D to duplicate them
[10:19] and then extrude the selection to give it some thickness.
[10:22] Press Ctrl and plus on the numpad to grow the selection and then G to move it if necessary.
[10:28] Oh and by the way, if you want the viewport to look like this, besides enabling a mattecap,
[10:32] you can enable cavity and then play with the settings until it looks good to you.
[10:37] Just like with the mattecap, this is not a material or a texture
[10:40] and it only looks this way in the 3D viewport of Blender.
[10:43] Before we continue, I should mention that instead of the first simple subdivision modifier,
[10:48] you can also replace that one with a bevel modifier for a similar result.
[10:52] The advantage of that is they have a bit more control over the corner sharpness,
[10:56] so that's definitely also a useful way to do it.
[10:59] In my opinion, the downside is that you cannot enable on-cage,
[11:03] so you cannot really see exactly what you're doing in edit mode.
[11:06] So it really depends on what you personally prefer.
[11:09] However, I find that once you've extruded more geometry,
[11:12] the bevel method becomes less reliable.
[11:14] So I recommend using the double subdivision modifier method instead.
[11:19] If you like, you can also display the wireframe in object mode
[11:23] by enabling it on the object itself in viewport display options
[11:26] or globally in the viewport overlays.
[11:29] However, I don't recommend doing this because you might get confused
[11:33] and think that you're in edit mode when you're in fact in object mode.
[11:36] And those are all the modeling tools that you will need for this easy, fast modeling technique.
[11:41] So now let's look at an example project.
[11:44] At the end of the video, we'll look at a few more advanced methods of adding finer detail.
[11:50] So this is the part where I show you how to model this specific example.
[11:55] As you can see, I have two 3D viewport windows open, both with the default cube.
[12:00] I just had the one on the right open so that I could record a time lapse of the process.
[12:05] That's all.
[12:06] So the window on the left is the one that I'm actually working in.
[12:11] And I'm adding a subdiv modifier and I'm setting it to simple.
[12:15] So that's the first one.
[12:16] It's just adding more geometry.
[12:17] And then I'm adding another one set to Cadmium Clark.
[12:20] And then I want right click and choose shade smooth.
[12:23] So now the cube looks more smooth.
[12:25] So in this case, I decided to turn on wireframe display in object mode.
[12:30] I don't actually recommend that you do this, but I just did it in this example to show the wireframe.
[12:35] And here I'm showing you the difference.
[12:37] If you turn off optimal display, then you see all that extra geometry.
[12:42] But I recommend that you just keep optimal display turned on.
[12:46] And then I'm adding a mirror modifier and I'm dragging it up and enabling bisect.
[12:51] And as you can see in edit mode, we can still see the original geometry
[12:54] unless we turn on on cage, which is this triangular icon.
[12:58] And as you can see now, you see this optimal display.
[13:01] It's very clean and there's no distracting extra geometry to look at.
[13:05] And so in edit mode with face selection mode, if I want to move a face on a specific axis,
[13:11] I just press for example, on G and X to move it only on the X axis or G and Y to move it on the Y axis
[13:20] and G and Z to move it on the Z axis.
[13:23] And instead of face selection mode, you can also use edge selection mode
[13:26] and then just move edges and adjust the shape like that.
[13:31] And now I'm going to add some extra geometry by pressing control R,
[13:36] which is the way to add a loop cut.
[13:39] And then I'm just adjusting this specific edge by sliding it on the Y axis.
[13:45] And here I'm extruding this by pressing E.
[13:48] And then again in edge selection mode, I'm just manipulating some edges,
[13:53] just moving them on the Y axis and the Z axis here.
[13:57] And same with this one, I'm just moving it up on the Z axis.
[14:00] And yeah, because we have such a clean display of the geometry,
[14:04] because optimal display is enabled and on cage is enabled,
[14:09] we can manipulate the geometry very easily and we're not distracted by any geometry that we don't
[14:14] need to see.
[14:15] And now I'm just selecting these two faces and pressing E to extrude and then S to scale down.
[14:21] And again, E to extrude.
[14:23] And then I'm just scaling it to zero on the X axis
[14:27] and just moving and scaling on the specific axis just to manipulate the shape.
[14:34] And rotating it on the Y axis here and selecting some more faces and extruding with E
[14:41] and then scaling down on X.
[14:43] And as you can see, we're very quickly getting a interesting shape.
[14:47] Let's select these two and insert them with I and then extrude inwards with E.
[14:53] And you're getting this kind of interesting intake.
[14:56] And when we switch to object mode, you see actually all the geometry that is being generated.
[15:01] So you can kind of inspect what you're creating in object mode,
[15:05] because wireframe is turned on.
[15:07] But I actually don't recommend leaving wireframe turned on for an object,
[15:12] because it can be confusing.
[15:14] It can look like you're in edit mode and you might press a button that you're expecting to do something
[15:20] in edit mode, which will do something else in object mode.
[15:23] So here I used loop tools flatten, as you can see, just to flatten those faces.
[15:28] And now I'm just manipulating that shape by moving some edges on the Z axis
[15:34] and just selecting these faces and inserting them once more with I
[15:38] and just scaling that a bit.
[15:40] And then with E extruding that again and scaling the extrusion down slightly.
[15:46] And I'm going to select one face in front here and extrude it with E and then scale it on the Z axis
[15:53] with S and Z and also move it on the Z and then on the Y axis.
[15:58] And then we're going to just move some edges here.
[16:01] And so it's very easy to very quickly manipulate the shape just by moving some edges or some faces.
[16:08] And let's extrude this part here.
[16:10] So I'm extruding this on the Z axis and then scaling it down on the Z axis as well.
[16:15] That flattens it.
[16:17] And then we can kind of rotate this from the side view here
[16:20] and just manipulate it by scaling it and rotating it and moving it
[16:25] to get a more interesting shape there for these, I don't know, neck guards, I guess.
[16:31] Now here I'm actually going to select this and then shift D and duplicate it.
[16:36] And then I'm going to press G and X to move it on the X axis to move it away from the model.
[16:43] And so now I have a piece of geometry which has still all of these modifiers.
[16:48] But when I press B and then choose separate by selection, I actually turn it into a separate
[16:55] object. Now we have a separate object and in edit mode we can extrude it to give it some thickness.
[17:02] And the reason that that other object now has so many edges is just because we're seeing that one
[17:08] in object mode and we're seeing the small arm piece in edit mode.
[17:13] In edit mode, you're only seeing the simplified geometry, the optimal display.
[17:18] And when something is not selected, you're seeing all the geometry that's there.
[17:22] And so I'm just manipulating the shape and moving some edges.
[17:26] And then control R, adding a loop and sliding it so that that part becomes a bit sharper there.
[17:32] And the same thing on the other side. So and then I'm just going to select some of these edges
[17:39] at the top here and then double G and sliding them and then we can extrude these faces.
[17:45] And I'm just going to adjust the shape a bit more by selecting and sliding some edges with
[17:50] G and G. So double G and I will slide it along that geometry.
[17:55] And I'm just selecting this face and moving it on the y-axis a bit just to give it a bit more of
[18:00] a rounded shape here in the front and then extruding those faces and scaling that down,
[18:06] moving that selection on the x-axis. And let's take these two faces here on the side and
[18:11] insert them with I and scale that down a bit and then extrude it inwards. So we get this kind of
[18:17] hole here. And let's take these two and extrude them as well and scale it down on the z-axis.
[18:23] Then we flatten it and then we just scale it down and let's move these edges and let's switch to
[18:29] vertex mode. So we can just manipulate this one vertex here to bring that a bit closer on the x-axis.
[18:36] And sometimes you just need to have only the vertex selection mode so you can do a bit finer
[18:42] work. And here at the bottom I want to extrude some faces but first I'll add another loop with
[18:47] control R and then I can just select this part and insert that and then I can extrude it inwards
[18:54] and then shift D and duplicate that part and separate by selection to create a new object.
[19:00] And then we can extrude and we can add thickness that way. And then we can just of course manipulate
[19:06] it in the same way as all the other objects. So scale, rotate and move on specific axes.
[19:13] And this is very low poly now so just control R adding another loop and sliding it.
[19:18] And then I can select these two faces and extrude them and maybe scale that down a bit and move it
[19:25] on the z-axis. And every time you extrude an inset you create more smaller faces that you can
[19:31] manipulate and extrude or inset. So it's really kind of an iterative process where you kind of
[19:36] organically create these shapes and you go from big to small. So here I'm just manipulating some
[19:43] vertices to have a bit more control over the shape and just like with edges you can double G
[19:49] and slide these vertices along that geometry. And to flatten these three faces I'm scaling them to
[19:55] zero on the y-axis and that flattens them. And so now we're in object mode and in object mode you
[20:02] just click on object to select it. You can also select two objects and then go to edit mode and
[20:07] you can manipulate both of them at the same time. And now to create the head I'm just selecting these
[20:13] faces here, shift D duplicating them and moving them up on the z-axis a bit and then pressing
[20:20] P and choosing separate by selection to create a new object. And then in edit mode we can select
[20:26] these faces and press E to extrude them in order to create some thickness. And by the way you don't
[20:32] have to separate things into separate objects but it can be useful because it is a bit more efficient
[20:41] and especially if you're going to add detail with sculpting then it really helps in terms of keeping
[20:47] the scene optimal especially if you don't have a very good computer if you just work on one object
[20:54] at a time. And so here I'm just thinking a bit about how I'm going to edit the head because I'm
[21:00] just sort of improvising the shape. So I'm just adding some more geometry and manipulating some
[21:05] edges and just control r adding more loops. And so I'm just moving some edges and trying to create
[21:12] an interesting shape. And here I actually applied the mirror modifier and just remove that middle
[21:18] edge there. And that allows me to extrude a bit more easily in the middle of the object here.
[21:24] And so here I'm extruding this part in the front and then I'm also going to make a selection in
[21:29] the back and first inset that and then just move that a bit. And you can see how similar extruding
[21:37] and insetting is. It's pretty much the same thing really. So here I'm creating some kind of interesting
[21:44] head shape and extruding this part in the back. And of course scanning that down and manipulating
[21:51] some edges to make sure that the silhouette looks better. And so I usually use gg so double g
[21:59] to slide edges along the surface. And yeah, just double g sliding and then moving along the z axis
[22:06] this edge and in vertex selection mode moving some vertices or you can also scale them towards
[22:12] each other. And because I don't have a mirror modifier anymore, when I manipulate one side,
[22:18] then as you can see it doesn't change the other side. However, we can turn on x symmetry and
[22:24] then if you make a change on one side, it will also happen on the other side. You just have to
[22:28] make sure you choose the correct axes. For example, now we're using the x axis. And here I'm just
[22:35] insetting and extruding again. As you can see, most of this is just insetting and extruding parts.
[22:42] There's really not much more to it than that. Unfortunately, for some reason,
[22:46] symmetries only works with geometry that is already there. So if you inset or you extrude,
[22:51] then for some reason it won't do that on the other side. And that is why here I symmetries it.
[22:58] And normally symmetries is a tool that you find in this menu here. However, I've added it to my
[23:05] quick favorites. So now when I press Q, I can just choose symmetries and it will be right there.
[23:12] And it will work on all of the selected geometry. So you have to make sure
[23:16] that the geometry you want to symmetries is selected. So I will press A and then choose
[23:21] symmetries. And sometimes you have to change the direction like I had to do here. So now the mesh
[23:26] is symmetrized and it is also added a loop in the middle, as you can see. And here I am insetting
[23:32] and extruding inwards. So I'm creating this kind of helmet shape. And I'm creating another object
[23:37] by selecting these two faces and shift the duplicating them, and then separating by selection
[23:43] and extruding that part just to create something to put inside of the helmet of the head. And it
[23:48] looks like it's a bit off center. So I'm just selecting everything in edit mode and then G and
[23:55] X to move it slightly more to the center there. And then in object mode, I'm just moving it up.
[24:00] Now here I want to actually select the two faces at the back of this object. So what I do is I select
[24:07] the two faces in the front, press Ctrl and plus on the numpad to grow the selection. So now only
[24:14] those two in the back are not selected. And then I press Ctrl and I, which inverts the section and
[24:20] that way the two faces at the back are selected. So now I can manipulate them. So I'm just moving
[24:26] them on the Y axis and on the Z axis. And so now I can manipulate this shape a bit more by selecting
[24:34] some edges and moving them. And again, I'm selecting two faces here and shift D duplicating them,
[24:41] separating by selection and then extruding that part in order to get some thickness.
[24:47] And here to create a bit more interesting of a helmet shape, I'm just selecting this edge and
[24:51] moving it on the Y axis. That way it's a bit more curved in the front. And as you can see in my
[24:57] object mode, quick favorites menu, I also have the mirror modifier. So you can actually add
[25:03] modifiers with your quick favorites. And so I'm adding a mirror modifier back to this face part.
[25:09] And then of course, dragging it up to the top of the stack and enabling bisect. And there's
[25:14] something wrong in the middle here, but I think it's solved easily by just moving it a little bit.
[25:19] And then it will merge because the merge option is enabled. And so now I'm just manipulating that
[25:25] shape a bit more and in setting and extruding some parts. And that always works better with the
[25:32] mirror modifier on it, because then you don't need to symmetrize it manually. And so here I'm
[25:37] rotating these cheeks along the Z axis just to make the shape a bit more fitting for the helmet
[25:45] around it. And I don't like the shape from the side. So I'm just going to adjust this helmet a
[25:50] bit more. So I'm just going to select these faces and move them on the Z axis down like this.
[25:56] And I'm going to just select these two edges and scale them away from each other on the X axis to
[26:01] make that part a bit thicker. And then we can inset and extrude this inwards to create some kind of
[26:06] air intake or something. And we can do the same thing here. But first, I'm just moving this inwards
[26:12] a bit to create a bit more space. Then we can select these faces and inset them and extrude
[26:18] inwards and just move that extrusion a little bit to the side. And we have another air intake on the
[26:24] side of the head there. So I'm imagining this is the kind of technology from the 80s science fiction
[26:30] where there are a lot of capacitors and wires and stuff that need to be air cooled. And that's why
[26:35] it has a lot of air intakes. And here I'm just extruding the front of the helmet a bit more just
[26:41] to make it look more interesting. And we can create some air intakes here as well by insetting it
[26:47] and extruding inwards with E. And we need to always move that inset a bit because it will
[26:53] inset along the normal direction, which is usually not what you want in this case.
[26:58] So just move it with G and then some X's like G and X, G and Z, G and Y. Now you don't have to do
[27:05] this, but what I did is select everything and then control A and choose visual geometry to mesh.
[27:12] That applies all of the modifiers. And as you can see, it gives you a lot of geometry. And that just
[27:18] makes it a bit easier to do smaller details. And here I'm just turning off all those
[27:25] wireframe displays on all these individual objects. And as you can see, I added a shiny
[27:30] matcap to the objects there. So I've added a sub diff modifier back to this helmet part.
[27:36] And I'm just sliding some edge loops now to make those corners sharper. So the closer
[27:42] edge loops are together or vertices are together, the sharper that part will be.
[27:47] I'm just double G and sliding these parts and then just making that part a bit sharper.
[27:54] And here I'm just turning on cavity to make sure that I can see the corners better.
[27:59] And another thing you can do is if you select an edge loop, you can bevel it with control B
[28:04] and then scroll up to increase these segments. And then you can select the loop in the middle
[28:09] and get it down with alt S. That creates a kind of a panel cut. And here I'm doing the same thing.
[28:15] So I'm selecting a loop, control B to bevel it. And it still remembers the amount of segments.
[28:20] And then select that middle loop and alt S and get it down. And that's how you can get these
[28:25] interesting panel cuts. Here I'm adding a couple more loops around it just to make it more sharp.
[28:32] So having this kind of quad apology makes it really easy to select those loops.
[28:36] And here I'm also doing the same thing again. So adding a couple of loops here
[28:41] and control B beveling it, selecting the one in the middle and then just alt S and scaling it down.
[28:47] So to add a bit more detail to the front of the face here, I'm selecting and insetting and then
[28:52] extruding this part and extruding it one more time and then insetting it one more time to make that
[28:58] part a bit more sharp. And here I'm adding a loop just to make that sharper as well. And then adding
[29:05] some loops and scaling the middle one down and then adding loops around it to make the corners
[29:10] sharper. So I've added a panel cut around that as well. And here I'm beveling one vertex with
[29:17] control shift B. So shift control B. And then you can change the shape first of all to make it
[29:24] more circular. And you only need two segments and you can use a loop to circle or you can just
[29:30] change the shape like that. And then I'm connecting these vertices by pressing J and
[29:36] insetting the circle part and extruding it inwards to create a nice circular hole there.
[29:43] And to make it a bit more circular, I'm using loop tools circle because I manually made it
[29:48] round in it. They didn't really work out. So now it looks better, I think. And to create a bit more
[29:55] detail in the front here, I'm also just selecting these faces and then insetting it with I and
[30:01] extruding it inwards and extruding one more time. And then we get another kind of intake for the
[30:07] front of the helmet there and adding a loop to make it a bit sharper. And adding another loop
[30:13] and then scaling that one inwards so that we get another panel cut there. And so now I'm switching
[30:20] to sculpt mode. And I'm just appending some alpha brushes from my hard surface sculpting course.
[30:27] So these are already pre-made brushes that I made specifically for that course.
[30:33] But if you don't have the course, you can find alpha brushes that are free quite easily online
[30:39] if you just search on Gumroad, for example, or ArtStation, then you can probably find a lot of
[30:45] free hard surface alphas. And I made a video describing how to use those as well that you
[30:51] can watch on YouTube. And as you can see, we need a lot more resolution on this object.
[30:56] So I'm just going to subdivide this multi-rust modifier that I put on it. And I still need to
[31:02] subdivide it more. So for these kind of things, for these alpha brushes, you really need a lot of
[31:08] resolution. You can see here, I turned on the statistics, you can see that this object alone has
[31:14] more than 3 million vertices. You can see that when we move the camera, it disappears.
[31:20] And that's just a blender's way of keeping it more efficient. And it looks like I forgot to
[31:26] turn on symmetry. And so placing alpha brushes is pretty easy. You can change the radius with F.
[31:33] You can rotate with Ctrl F. And you can change the intensity with Shift F. And that's really
[31:39] all you need. And then you just place them on the surface somewhere. So I'm just placing some
[31:44] alphas. And as you can see that really quickly adds more detail. You just have to make sure that you
[31:49] turn on X symmetry if you want it to be symmetrical. And I think it's really fun to experiment with
[31:56] these alphas because it's just so satisfying to see all that detail being generated. The cool thing
[32:02] about these alpha brushes, besides obviously that you can quickly generate a lot of detail,
[32:07] is that you just have to make them once. If you make them yourself, so of course you don't have
[32:12] to, you can just buy them. But if you make them yourself, you have them forever. So you just need
[32:17] to make the ones. And then you can add that detail to any surface forever, any model you make.
[32:23] And in Scott mode, to switch to another object, you press Alt Q. And as you can see the
[32:27] multi-res detail on the middle object there on the torso disappeared. But it's still there.
[32:34] It's just hiding it to make it more efficient because that's like more than three million
[32:38] vertices. And so now I'm subdividing this part to 700,000 vertices and adding some detail to that.
[32:46] And in the viewport, you don't see the multi-res detail on the other object unless you turn on
[32:52] the viewport levels. But when you render it, you do see it, of course. So that's just Blender's way
[32:58] of making sure that you can use all these millions and millions of vertices quite efficiently even
[33:04] on an old computer. And here I'm just adding a few more details to the shoulder part here.
[33:11] So if you're placing something and you're not happy with the placement, you can always press
[33:15] Escape. That is the fastest way to exit an alpha brush. But if you've already placed it and you
[33:21] want to undo it and just press Ctrl Z, it just takes a few more seconds to undo it. So if possible,
[33:28] press Escape, if it's not to date, and if it's to date and you want to undo it, then just press
[33:33] Ctrl Z. But I've made several videos also on YouTube about alpha brushes, and I'll put the
[33:39] links to those in the description so you can check that out. And so here I'm Alt Q and selecting
[33:46] that part, the face part. And I'm adding a multi-res modifier and just subdividing it immediately
[33:52] because I know I will need several levels. And I'm going to add some detail to that. And as you
[33:58] can see, it's still not high enough for a solution. So I need to increase the levels to four.
[34:03] And that's already better. If you turn on smooth shading, that also helps that makes it that you
[34:10] don't require quite as many levels of subdivision, because it's kind of faking that smoothness.
[34:17] So you don't quite see those jagged edges. But as you can see, I really need more sublif levels
[34:23] here, and especially for these little details like these bolts. Keep in mind in Blender that
[34:29] symmetry is turned on per object. So you might be happily sculpting on an object,
[34:34] thinking that x symmetry is turned on when it actually isn't. So you really need to check that
[34:40] every time. And so here I'm going to try and render this. So what I'm doing is I'm turning up the
[34:46] levels of the viewport display of the multi-res modifier. So we can see the multi-res detail on
[34:52] all of the objects at the same time. And of course, you can go much further at much more detail,
[34:58] but I'm just quickly going to make a render here. So I didn't spend too much time on it.
[35:02] And so I've appended the drag and drop materials from my materials course here,
[35:07] because it's just easier. You can just slap them on anything. You don't need to UV unwrap it or
[35:13] anything like that. So here I'm just enabling an HDRI. And that little checkbox you saw here,
[35:20] the HDRI checkbox and this panel where you can cycle through HDRIs is the Gaffer add-on,
[35:26] which is a free add-on. And all these HDRIs are also free. And it's quite great. It's by
[35:32] polyhaven.com. I think that's how it's still called. I'll put a link to that in the description
[35:37] shown. I've made a couple of videos about it as well, but it's very easy. You just install it,
[35:41] and you can check that box and get amazing lighting just for free. These materials are intended for
[35:48] cycles, by the way, because some of the edge detection shaders and stuff like that don't work
[35:52] in EV. Normally they're a bit faster if you turn on GPU, but it looks like I forgot to turn on GPU
[35:59] here. But it's just CPU rendering the viewport, which of course is very slow. And I'm just sort of
[36:06] experimenting, dragging and dropping. So with these materials, just a quick plug for my course.
[36:11] These materials, you can just drag and drop on anything. You don't need to UV unwrap it. So they're
[36:16] perfect for sculpted objects, objects with lots of engons, high topology, low topology,
[36:22] doesn't matter. They will always work. And you just need to drag and drop them. And if you don't
[36:26] like it, you can drag and drop another material right on it, and it will just replace it. So
[36:32] I cannot make it more easy to use than that. That's really the most easy to use. And that course
[36:37] also shows you exactly step by step how to make those materials and how to make textures, how to
[36:44] yeah, how to do everything you need to know to make those kind of materials really.
[36:49] And normally they're not this slow, but I forgot to turn on the GPU. So they're a bit slower now.
[36:55] So I made these materials because I was just tired of always having to do this work in Substance
[37:00] Painter. Although I always enjoyed using Substance Painter, but I just find it a little bit difficult
[37:06] to use because yeah, you always have to export your model, and you have to UV unwrap it, even if
[37:13] it's a crappy, decimated sculpt, you still have to UV unwrap it for Substance Painter or the smart
[37:19] materials won't work. And so I decided to make these materials that are true smart materials,
[37:25] where they really don't need a UV map or anything like that. You can just drag and drop them and
[37:31] they will just work always. And I don't have to exit the blender. And that was my motivation making these.



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
