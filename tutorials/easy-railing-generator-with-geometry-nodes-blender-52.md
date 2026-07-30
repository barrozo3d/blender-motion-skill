---
title: Easy Railing Generator with Geometry Nodes | Blender 5.2
source: YouTube
url: https://www.youtube.com/watch?v=deAw5dU5Wfs
author: Max Hay
ingested: 2026-07-30
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/easy-railing-generator-with-geometry-nodes-blender-52/
frame_count: 0
frame_status: pending-selection
---

# Easy Railing Generator with Geometry Nodes | Blender 5.2

**Source:** [YouTube](https://www.youtube.com/watch?v=deAw5dU5Wfs)
**Author:** Max Hay
**Duration:** 28m37s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py easy-railing-generator-with-geometry-nodes-blender-52 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] In this video, I'm going to show you a procedural fence generator in geometry nodes.
[0:04] This is a very beginner-friendly, easy system you can make if you don't have a lot of experience with geometry nodes
[0:09] that you can use so that you'll never have to manually hand-place railings or fences again.
[0:16] So here's an example of this working. You can see anywhere you extrude this point, it'll just auto fill in fences,
[0:22] so you can do that either just with this point you extrude, or you can just separate out an edge on an existing object,
[0:27] slap the modifier on and it'll just auto fill in just like that.
[0:31] So it's really useful for any kind of industrial scene or any scene with fences or anything like that.
[0:35] So this will not be too advanced, I'm going to try and keep it beginner-friendly.
[0:38] I'm still learning a lot of this stuff myself, so this is just kind of one of the first things that I made that I found was useful.
[0:44] So in this one, I'll show you how to model this little fence thing.
[0:46] We're going to use that and then create this really basic geometry node system so that you can move these points around and get the fence to follow it.
[0:53] And then after that, once we have the system set up, I'll show you how to make it more customizable after you've built everything.
[0:58] There's kind of a section later in the video of me just doing a little bit more like,
[1:03] a little bit of the next step, a bit more advanced stuff and just talking about some of this thing
[1:06] that I've already made and showing you some cool tools that are kind of crazy and just giving you some ideas of other things you can play with.
[1:12] That's less of a tutorial, more just me like sharing some interesting things I've made with it and some things you can try to.
[1:19] That's later on, but let's get to the tutorial and hopefully this is useful.
[1:24] Okay, let's start this up at the first level here.
[1:26] I'm just going to really quickly model a little fence object that we can use first and then we'll jump into geometry nodes and use that to instance it along a pathway.


### Modeling the Railing [1:30]
**Transcript (timestamped):**
[1:35] Okay, so let's just jump in and add a cylinder.
[1:38] We don't need that many vertices.
[1:39] 24 is probably good.
[1:41] The default I think was 32.
[1:42] I just dropped it down to 24.
[1:44] So that's good there.
[1:45] Let's just make some room for this.
[1:47] Let's s shift z and just make that a lot thinner.
[1:51] Take these top vertices, move it down like one meter maybe.
[1:55] What I can do is put the cursor down right here.
[1:57] I'm just in front view and I can go and take the spin tool.
[2:00] Let's just grab that top face front view and then just set the steps.
[2:04] I think the default is like 12.
[2:05] You don't need that many, probably eight is good.
[2:09] You can just take the spin tool to make sure this is on this gizmo thing and then just choose the axis here.
[2:14] So why in this case?
[2:15] Move that out, hold control to snap it and we can just extrude that out again.
[2:20] Let's just do a mirror modifier after that.
[2:23] Move this over, turn on clipping and then that'll kind of connect the ends together.
[2:29] We can just kind of move it like there.
[2:31] Let's make it a little shorter.
[2:33] Let's take this now and let's just shift D that.
[2:37] Pull it down here.
[2:38] Let's just grab little thing, move it over like this and you can customize this to whatever shape
[2:43] you want but something like that.
[2:45] Okay, if you want you can even go in.
[2:46] If you messed up the thickness, let's just apply that mirror modifier and there's a face right
[2:51] there.
[2:52] I got a delete.
[2:53] If you messed up the thickness, you're going to select everything and press alt S.
[2:57] Bring that down, press S one more time for even scaling.
[3:01] So that's probably good there.
[3:03] Let's apply scale and I'm going to set the origin to the bottom.
[3:07] So the easiest way to do that is just select these two faces, shift S and then cursor to selected.
[3:12] Then turn on effect only origins and then press shift S and then selection to cursor
[3:18] that would normally move it but since we've turned on effect only origins,
[3:21] it'll just move the origin point to perfectly between those two faces.
[3:24] Okay, you can also just manually put it near the bottom.
[3:27] It doesn't matter that much.
[3:29] So I put the origin point at the bottom middle of the fence.
[3:33] We might need to have it set up so it's off to one side like this.
[3:36] So I might end up moving that over but there we go.
[3:38] There's the fence object we're going to use.
[3:39] Let's jump into geometry nodes and start getting this to work.
[3:42] So just to quickly show what I'm trying to make here,
[3:45] my idea is say we're working on like a platform or building or whatever
[3:50] and we have some interesting shape.
[3:52] It would be nice to be able to just take like this edge here if I just select all this
[3:57] and like duplicate that, separate it to a new selection
[4:01] and then just have this fence post just perfectly,
[4:05] you know, go along that line and create fences all the way around.
[4:09] Another way to use this is like if I had a single point,
[4:12] which you can get from adding like a cube here, right, and then merge at center.
[4:18] It would be nice to have a single point that I could extrude like this along a pathway
[4:22] and then just have it again, auto fill in fences everywhere that that goes.
[4:26] So let's make that.
[4:28] Let's just get rid of all this here and let's just start this from scratch.


### Setup [4:29]
**Transcript (timestamped):**
[4:31] So let's go cursor down here.
[4:33] Let me add any mesh here.
[4:35] Doesn't matter.
[4:35] So let's just do a plane, go to edit mode, select everything
[4:39] and then hit M and merge at center.
[4:42] Okay, so it's a little hard to see what's going on because it's a tiny little dot,
[4:45] but if you go into vertex select mode and then just kind of grab this here,
[4:50] you can actually extrude this vertex and go along the x axis.
[4:55] Let's extrude it along the y axis back on the x.
[4:58] So it's just vertices connected by edges with no faces here.
[5:02] This is a bit weird if you never use that, but there we go that we're doing that, right?
[5:05] So let's just make this a little larger and let's start getting this actually going here.
[5:10] So I can just kind of move this into place.
[5:12] Let's just jump into geometry nodes and let's get this going.


### Geometry Nodes (main tutorial) [5:13]
**Transcript (timestamped):**
[5:15] So I'm going to press new.
[5:16] Let's do first of all, I'm going to do a mesh to curve.
[5:21] So right right now, for add that, this is just a mesh, right?
[5:24] It's just vertices and edges.
[5:26] It's just that there's no faces, right?
[5:27] If I were to extrude this and connect this together and fill this in with a face,
[5:32] it's still just a regular mesh.
[5:34] It's just that we don't have any faces.
[5:35] It's just vertices and edges, right?
[5:37] So our geometry here coming in is a mesh.
[5:39] So we need to go mesh to curve because there's certain things that we can do in here to a curve
[5:48] that we cannot do to a mesh.
[5:50] For example, I'll show you like resampling the curve in a second, but
[5:53] there's certain operations that are exclusive to curves.
[5:56] And that's why we want to add this is so that our incoming geometry, which is mesh,
[5:59] is now converted into a curve after this point.
[6:03] Okay, so for example, what we can do after this is take like,
[6:06] I'm going to do an instance on points just to show you this.
[6:08] You've probably seen this before.
[6:10] Let's do a cube and let's just plug that into the instance.
[6:15] So what we can do is, for example, you know, anywhere I extrude a new point,
[6:19] there's going to be a new cube, but say I wanted to fill in this empty space here
[6:25] with evenly spaced things like fences.
[6:27] What we can do is like a resample curve node right before or right after it goes mesh to
[6:33] curve.
[6:33] So now it's a curve, let's go right there.
[6:35] You can see I can switch this to length.
[6:38] Let's increase that.
[6:39] So say every two meters, you want a new instance, right?
[6:42] Now anywhere I extrude this, it's going to resample that curve and add in new points every two meters.
[6:48] So that's something that you can't do if it's a mesh, right?
[6:51] So you have a mesh going into this, it doesn't work.
[6:53] You have to convert it to a curve for that to work, right?
[6:56] Okay, so that's why we're just going to be a lot of mesh to curve and all that.
[6:59] So it's right.
[7:00] Hopefully that makes sense.
[7:01] Let's delete this and this is kind of just to show what we're doing here.
[7:04] We don't actually need this cube in here.
[7:05] So I'm going to actually unplug that.
[7:08] Let's keep this set up.
[7:08] So we've got the mesh to curve, the resample curve, and then the instance on points.
[7:13] So we have points where we don't have anything to instance.
[7:17] We can take an object info node and just take the eyedropper and click our fence here,
[7:23] our cylinder fence.
[7:25] And then what I can do is plug the geometry of that into the instance.
[7:29] Okay, so you can see where we're going with this, right?
[7:31] If I just make sure I apply scale and everything, you can see anywhere I extrude this,
[7:35] obviously the orientation is not correct, but we'll fix that.
[7:40] Anywhere I extrude this, we're going to get new fences.
[7:42] So that's kind of how this is going to work.
[7:44] Okay, so let's fix.
[7:45] First of all, the spacing is not good because we're overlapping there.
[7:50] So we probably need to increase this until that gets to the point where it's kind of like
[7:56] not perfectly overlapping, right?
[7:58] So that would probably work there.
[8:00] We don't really care if it's 100% perfect as long as it's like pretty good.
[8:04] That's good enough for me in this case.
[8:05] So that works.
[8:07] Next, we need to fix the orientation so that it just goes, you know,
[8:12] following the line direction that I'm creating here.
[8:15] So obviously this is not what we want here.
[8:17] Let's try and do that.
[8:19] So first of all, let me just grab this here.
[8:21] I'm going to just probably just delete that and then just reconnect this.
[8:25] And I'll just move this down here just to have an example of like where we're having errors here.
[8:31] Okay, so there is a node here called curve tangent, which since we've we have the incoming mesh
[8:39] geometry, we're going to mesh to curve and we're resampling still the curve.
[8:44] At this point right here, we can take the curve tangent, which is basically,
[8:49] as far as I understand it, the curve tangent is just like we have our curve here.
[8:53] It's just like a 90 degree offshoot of the curve at any point.
[8:56] I think that's all it is.
[8:58] So we can use that to help orient our fences and use that to drive the rotation of these.
[9:05] I could be wrong on that explanation, but that's as far as I have seen people explain it.
[9:09] But anyways, curve tangent, I need to run this through something before we go into the rotation
[9:14] though, because otherwise it's not really going to do what we want.
[9:18] You need a node here called a line rotation to vector.
[9:22] Okay, used to be called a line or the vector.
[9:23] There we go.
[9:24] A line rotation to vector.
[9:25] So this is going to go into the vector that goes into the rotation.
[9:29] And we just need to choose the right axis.
[9:31] So click around here.
[9:33] Zed is obviously not right.
[9:35] Y is obviously working, but the wrong way.
[9:39] And then X is pretty much doing what we want with the exception of the corners.
[9:43] So we'll fix that in a second as well.
[9:45] So we have that going.
[9:47] There we go.
[9:48] It's it's working, but it's the corners are not correct.
[9:51] Okay, there is a node we can add called split edges.
[9:56] This only works.
[9:57] You can see it only works for a mesh though.
[9:59] If I do it here, it's not going to do anything, right?
[10:00] We are going curve and then split edges.
[10:02] It's trying to take a mesh input.
[10:03] It's not going to work.
[10:04] We have to do it at the beginning, where while it's still a mesh input coming in here,
[10:08] before it gets converted to a curve.
[10:10] So let's put that right here.
[10:11] You can see now the corners are actually even, which is what we want.
[10:16] So the only issue here is remember I said the origin point is in the middle of this,
[10:20] and I might have to move it to the edge.
[10:22] Well, let's actually do that.
[10:23] So let's go to edit mode.
[10:24] Let's just GX and let's just move that over.
[10:27] One side of the other doesn't matter which one here.
[10:29] It's just moving to the left side.
[10:31] So the origin point that orange dot from which it rotates from is on the left side of this
[10:35] and extends all the way out here like that.
[10:37] I just realized I forgot to explain what this split edges is doing, why that's important here.
[10:41] So without it, this is now, this entire thing is getting converted into one continuous curve
[10:51] with every point being still connected as a path in that, or like as a part of that curve rather.
[10:57] So what the split edges does is instead of like being made up of like connected vertices,
[11:05] it's kind of like if you took an edge like this, if I just turn off the modifier,
[11:09] and then you had just another edge there and then another separate edge there.
[11:14] And it's splitting each edge apart from so that they're not connected on the ends like that.
[11:21] That's kind of what it's doing.
[11:22] If you can kind of visualize it like this.
[11:24] So what that means is if I do the split edges, let's turn this back on.
[11:29] Every edge is getting split, which means when it gets converted to a curve,
[11:33] now what used to be every edge is now its own separate curve.
[11:37] So there's not, it's not going to bend around the corner like it was before, right?
[11:42] So this is from before, I don't need that.
[11:45] So one thing I mean to do here is kind of remove one of these from every corner.
[11:52] Every time, you know, we have a corner, we're having a problem.
[11:56] If I could just subtract one from the corner, that would actually be great.
[11:59] The way to do that, there's actually an endpoint selection node.
[12:05] So anytime you see a selection input, we can determine what gets included and what gets excluded
[12:11] with any driver that goes in there.
[12:13] So we can take like the endpoint selection, let's plug that in.
[12:17] So you can see that's actually doing what we want, except it's only that.
[12:21] So how do we flip it around?
[12:23] We need to invert that.
[12:24] There's a boolean not node.
[12:27] So it's this selection, but actually not that.
[12:31] It's everything except that and that's what we want.
[12:34] You can see here, if I just take this out for a second, the endpoint selection,
[12:38] the higher you increase this, it's going to just increase and select more and more points along
[12:44] the curve.
[12:45] So the more I increase it, more points are included.
[12:48] If I go down here, right, and we can start from the other side too.
[12:52] So you can actually just use this to say, let's go start size one.
[12:57] I'm going to have this in our selection, but let's invert it.
[12:59] So we're going to go not boolean.
[13:02] And let's just try and mess with this and see if we can get to the point where that looks correct.
[13:07] So start size zero and size one.
[13:10] So looks like, yeah.
[13:14] So that's all I needed to do.
[13:16] Okay, just to make this endpoint selection really clear, in case I was confusing for you,
[13:19] what this is doing, if I just take out the split edges, no, so remember now,
[13:23] this is going to be one continuous curve all the way along here.
[13:27] The endpoint selection, it just is selecting points to include or exclude depending on if
[13:33] you have the not here.
[13:34] So let's just take it out.
[13:35] So it's probably the endpoint selection directly in here.
[13:38] This is now saying we're going to include zero.
[13:40] So if I start increasing the start size, it's going to go point number one is now included in
[13:45] the curve, right?
[13:46] Increase another one point number two is now included in the curve three, four, etc.
[13:51] Again, since this is one continuous curve, the higher I go here now, it'll go all the way up to
[13:55] the very end of the curve, and that'll stop.
[13:59] If I have it with split edges, though, and I'll do that again, where it's a mesh,
[14:04] then that goes to a curve.
[14:06] If I do it there, it's going to do it for each independent segment of that curve or
[14:14] spline, I guess, of the curve, then it'll do that for each that each each point on each
[14:20] individual curve has a value or integer assigned to it.
[14:25] And this you can use to select which ones get included or not.
[14:29] So that's why we're just using that and saying, okay, let's just, you know, have this on zero,
[14:33] and then we'll include just that end one, which is the problem one, flip that around.
[14:38] And there we go.
[14:40] So you can see it's just like one too many.
[14:43] You can just get rid of that one and now we have it working.
[14:49] And the reason that I've got the origin at the bottom now is because or on the left side is
[14:53] because you can see if it's in the middle, we're getting kind of like this.
[14:57] So just move it over to the left side and then it should line up properly.
[14:59] You can see it's still lined up with the end of this curve here.
[15:03] So there's that anywhere I extrude this, we're going to get new fences now.
[15:07] And you can see how useful that is.
[15:09] So sweet.
[15:12] Okay, I might just increase the resample curve resolution here.
[15:16] It's a little bit tricky to get the exact right spacing sometimes, but
[15:22] yeah, if you want just a super easy one, there you go.
[15:24] It's like this is as simple as it gets.
[15:26] It's just a few nodes.
[15:27] And what you can do now is say we're working on, you know, we have our building and it's like,
[15:33] oh, I want actually fences going around here.
[15:36] Let's just take like a face, scale that out.
[15:39] Let's take these edges along here.
[15:40] So just these four edges.
[15:43] Let's let's just duplicate that.
[15:45] I'm going to just separate selection.
[15:47] It's actually grabbed the face in the middle too, but we can actually just go in and delete only faces.
[15:53] So delete only faces.
[15:56] So we just have an edge like that, right?
[15:59] That actually looks pretty similar to what we were just working with with our
[16:03] just mesh line here, right?
[16:06] So I should be able to just take this modifier and just put it on this as well.
[16:10] So let's just try that.
[16:11] Let's go in here.
[16:12] Let's just add a geometry nodes modifier and then I'll just hit the drop down and just pick that one.
[16:18] Right?
[16:19] Let's apply scale so it actually does it properly.
[16:21] And look at that.
[16:22] We have instant fences following whatever shape I've added there.
[16:27] So it's actually really useful to just instantly just add railings or fences wherever you want.
[16:31] Right?
[16:32] Now here's the thing.


### Customization with Modifier [16:33]
**Transcript (timestamped):**
[16:34] Sometimes you might want to adjust things like the scale or how many,
[16:39] you know, this resample curve length amount, right?
[16:42] The thing is I want to be able to keep this system the same.
[16:46] The cool thing about geometry nodes is you can take any,
[16:49] any thing here like any like the length parameter.
[16:52] We can take that.
[16:53] We can run it out into the input and that actually adds it into now the modifier.
[16:58] And the reason that's actually useful is because now these are the same
[17:02] system still, right?
[17:02] If I make a change to one, it'll affect both.
[17:05] But since it's on a modifier now, these are independent controls per
[17:12] object that you're doing this on.
[17:13] Right?
[17:14] So if it's like this one, I want to say change the endpoint selection.
[17:18] We can actually run that out to the modifier.
[17:20] And like if I want to have, you know, something like this, I can do that on here and not have it on this one.
[17:26] Or maybe I want it, you know, maybe I want to have an extra one on this
[17:31] because I thought it looked cool or whatever.
[17:32] This is a bad example, but you get the idea, right?
[17:35] A better one would be probably the scale or say the object itself.
[17:40] Like we can take this out to the modifier.
[17:42] Let's just set the object to our cylinder.
[17:46] I've lost the other thing here.
[17:49] So I think it's, what is it?
[17:50] Plane.
[17:51] Yeah.
[17:51] Let's just choose object cylinder and we could import any other models.
[17:56] So for example, let's go in here.
[17:57] I think I have some fence or railing object right that we can take like this one.
[18:04] Let's just import this model and we can have the same system, except I can be like, okay,
[18:09] this one, I don't really feel in this railing.
[18:11] Let's not do this.
[18:12] Let's go eye dropper.
[18:14] Let's click this one instead and then let's adjust the length on here just so it fits better.
[18:19] And I'll just move the again, move the origin point to one side so that it, you know, fits in better.
[18:26] Okay, cool.
[18:27] And then maybe I'll make this a little smaller actually.
[18:29] So let's just move this in a bit.
[18:32] Let's do that in X-ray mode.
[18:34] Let's take these vertices here and just right click dissolve that.
[18:39] Okay, let's apply scale.
[18:40] And then now you can see I can adjust these controls, but this one is still the same spacing
[18:45] as before and has the same object that I originally wanted, right?
[18:48] And this one can be different.
[18:50] So that's the really cool thing about this is,
[18:52] the independent control you get from the modifier.
[18:58] So it's like, you know, if I want to have just, let's just do a different fence here.
[19:01] Let's separate that selection out and then we can just go, okay, this one,
[19:05] I want this one to be this fence and let's just adjust the length.
[19:09] And there we go, right?
[19:10] Let's just go a little less and then just adjust this here.
[19:15] And let's get another thing in here like this.
[19:18] And you can see you never have to model manual fences again.
[19:22] It's a little different for like curved stairways and stuff.
[19:24] That's harder, but for stuff like this, there you go.
[19:27] Super simple fence generator.
[19:29] And you can see how just useful that is.
[19:32] So there's, you can take this so far.
[19:33] There's so much crazy stuff you can do with it.
[19:35] This is like the most basic example I could show.
[19:39] But for like a really, for a beginner project for your first like generator kind of thing
[19:44] with geometry nodes, this is a great one to try.
[19:48] Because this is a super common setup you'll see with like
[19:50] curved tangent into the align rotation vector going into the rotation.
[19:54] So that the rotation is proper and then just doing mesh to curve and resampling the curve,
[20:00] all that, that's like really helpful stuff.
[20:03] And then you'll find it like that's useful in like much larger systems.
[20:07] So yeah, hopefully give this a try if you haven't used it.
[20:10] I'm kind of just doing a beginner geometry nodes tutorial in this one because
[20:15] I have not even really talked about geometry nodes at all on my channel until now.
[20:19] So I'm going to be trying to do a lot more of these kind of tutorials later on.
[20:23] One last thing you should know as well, if you want to actually convert this to an
[20:27] actual mesh and start like doing modeling on top of this or whatever,
[20:31] if you try and apply this, it's not going to let you just do just how to realize instances
[20:37] node at the very end of this.
[20:38] And now you'll be able to apply it.
[20:39] And now it's actual real geometry, just like any other model that you've ever used.
[20:45] So that's all you need to do.
[20:46] Just throw in the realized instances and that lets you actually apply the modifier.


### More Examples & Expanding the System [20:49]
**Transcript (timestamped):**
[20:49] So here's a railing and platform generator I was working on earlier.
[20:54] This is a lot more advanced and honestly, I don't really know this or like I can't explain this
[21:00] yet in a way that is quick.
[21:02] Like there's a lot going on here.
[21:04] I don't actually understand all of what's happening here enough to even explain it properly
[21:09] in a video anyways.
[21:10] So I'm still quite new to this, but here's an example of some of the crazy things you can do
[21:13] if you want to like this is basically built on this core concept, but just kind of with
[21:19] some extra steps to make it fit certain shapes.
[21:23] But it's not it's like the same thing just with more systems on top of it.
[21:27] Here's an example of like how you can use this to make really crazy things.
[21:31] So I can just take you can see here there.
[21:33] Here's the underlying geometry.
[21:35] I can take this edge and like extrude that out like this, get any size platform I want.
[21:39] And the tiling is all figured out and everything.
[21:42] So you can see where I move this edge.
[21:43] It'll just figure out the spacing for that.
[21:46] I could take this edge here, extrude that.
[21:48] And then if I move it up, it'll auto detect that it's a curve and it'll add stairs.
[21:52] I can extrude this anywhere, right, and just make any kind of platform that I want.
[21:58] And then like I showed with running certain parameters out into the modifier,
[22:02] that's where you get stuff like this where you can do like, okay, let's say I don't even
[22:06] want railings.
[22:07] I just want the platforms by themselves or let's say I want these to be a bit smaller
[22:12] and I want a bit of random rotation, which I've added in here.
[22:14] So random rotation, I can turn that on, adjust the amount, everything.
[22:18] Let's turn the railings back on and let's change the type to this square version.
[22:23] We can adjust things like the railing height, the frequency,
[22:27] which is the same exact thing I was just showing with the resampled curve.
[22:30] That's literally that right there.
[22:33] You know, it's literally just that and then just mesh to curve and then fill in the curve
[22:38] back to a mesh with like a square or a circle.
[22:41] And then you can change the amount of like sub bars here, change the spread.
[22:47] So you can really customize this to like any kind of shape that you whatever want for like
[22:52] a railing or whatever.
[22:53] This is kind of a weird example of this, but you can see it's very, I made it to be like very
[23:00] yeah, customizable to any shape you want, but you can also switch this to
[23:05] flat instead of graded if you want that.
[23:07] And then it's all just built on just like really low-poly stuff.
[23:10] So you can just quickly grab things, move it around, say I want another thing this way.
[23:15] Let's pull this out, bring this down into stairs, extrude that.
[23:20] Yeah, it's just, it's a lot of fun.
[23:22] So it's not perfect.
[23:23] You can't do like curves, curve stair.
[23:26] Oh, apparently you can.
[23:28] I didn't even know you could do that.
[23:29] All right.
[23:29] Well, that's interesting.
[23:31] Normally that does not work.
[23:33] So all right then.
[23:35] That's crazy.
[23:36] I didn't even know you could do that, but what definitely does not work is like curved.
[23:41] What?
[23:43] Wait, why is that actually working?
[23:44] Hang on a second.
[23:45] That's not supposed to do that, but I'll take it.
[23:49] Oh, it's because I have, if I switch this from flat to graded,
[23:54] then it breaks.
[23:55] Okay.
[23:55] Yeah.
[23:55] So you can see there's the limitations.
[23:58] But yeah, I didn't even know that would actually work like this.
[24:00] So that's cool.
[24:02] But yeah, you can see this is, it's a lot of fun to just mess with this and just
[24:06] create like crazy style platforms.
[24:08] Like there's so much, once you have it built, it's so fun and to just be able to go and use this.
[24:13] But yeah, I'm sorry.
[24:14] I can't do a tutorial on this yet.
[24:15] I don't understand what I even did here.
[24:18] And honestly, Sweeper3D, a lot of you guys know him, helped me figure out like a lot of this
[24:23] tile scaling and stuff.
[24:25] So maybe in the future I'll do a video on this, but yeah, there's like multiple groups in here.
[24:28] It's a lot.
[24:29] But this is just an example.
[24:31] This was very fun for me to make.
[24:32] Like I didn't struggle with this.
[24:34] It was just like, I was excited to do it.
[24:37] But it's basically just based on this core concept of like, you take a mesh line and you do stuff
[24:41] to it and you can like, we can do things like if we take the mesh line, say I can, I can take like,
[24:48] okay, the mesh to curve right here before we resample or let's do it after we resample it.
[24:52] But before we instance on points, we can go mesh to curve and I can plug that in here or sorry,
[25:00] curve to mesh is what I meant to add because we're going curve, I want it back to a mesh.
[25:04] Plug that in for the profile.
[25:06] I can actually add a curve circle, just like you would normally do in like the curve settings.
[25:12] Let's do a lower resolution and let's plug that into the profile.
[25:15] If I just looked at what this is, you can see it's that maybe on this one, I don't want the split
[25:21] edges though.
[25:22] So let's just run this.
[25:23] Let's actually do another thing here.
[25:25] Let's just take this, this, I'll just reconnect these.
[25:29] Let's take the incoming geometry, skip the split edges, plug that.
[25:34] Into this curve.
[25:35] So we've just done the same thing except no split edges.
[25:38] You can see now we're getting that there and then I can do like a instead of a resample curve.
[25:43] I just want to call it filet curve.
[25:44] So we can do filet curve right here or fill it.
[25:47] I don't know how you call it.
[25:49] So we probably want that there before the resample or not even with it.
[25:55] Change the thing, the poly is basically a bevel on here.
[25:58] We can do that.
[25:59] We can change the size of this.
[26:01] So lower that down.
[26:02] And then let's just reconnect that up.
[26:06] So like we can go join geometry, plug that at the end, plug this thing in here.
[26:10] And then anywhere I extrude our point here, we have like a little pipe or whatever following
[26:17] this.
[26:18] So I can lower that down, lower down the radius.
[26:20] But you can see that's an example of how you can get like a railing to perfectly follow
[26:25] your curve.
[26:26] And these instead of like this, we could have a cube and that could be our instance.
[26:32] And I can just move this up.
[26:34] So let's do a set position, move that up a little bit.
[26:37] And then let's do a transform geometry to scale it up on the Z axis.
[26:41] So scale Z right there.
[26:43] I'll just increase this.
[26:46] And you can see now if I take this railing, let's do a transform geometry on the railing
[26:51] and just let's just reset that.
[26:53] Move the Z up, right?
[26:57] I can even run that in parallel with another one.
[27:00] So we can do a join here, join it with this, transform this one and just move it down a
[27:06] little bit from there.
[27:07] You can see that's how you would make like a fence, right?
[27:11] You can probably take out the split edges and you can see that's like another way to
[27:17] do this is just do that.
[27:18] So that's kind of like a little bit of a little bit of a little bit of a little bit of a little
[27:22] So that's, that's kind of what that platform generator is built around is that idea there
[27:26] of just like curve line.
[27:29] Turn that curve, sorry, mesh line, and then turn that mesh into a curve.
[27:34] Do some operations to the curve like the fillet curve to bend the corners,
[27:38] the resample curve to get evenly spaced posts or whatever.
[27:43] And then it's just kind of done that along the outside here but it's literally just that.
[27:48] And then the stairs were harder.
[27:50] I haven't really figured out a great way to even do that that is
[27:53] That viable like this is barely working. You can see as I just expand that too far
[27:58] The space on emerge by distance so that like doesn't really work too well
[28:01] But yeah anyways, I just kind of want to show you some of the interesting things that I've been kind of thinking about with geometry nodes
[28:06] I've been learning a lot with this so there's gonna be more stories coming for that
[28:09] But yeah, there's just some some ideas for you to play with for like
[28:13] Just stuff that is normally very annoying to make you can make it actually really fun and like
[28:19] Make it in a way that you never have to manually just add fences one by one ever again. So yeah
[28:26] Hopefully this is going on too long. So hopefully this video is useful
[28:28] Thank you for watching and I'll see you and hopefully I'll try to get a tutorial out soon for something more interesting on geometry nodes



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
