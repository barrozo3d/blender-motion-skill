---
title: Blender 2D Animation Tutorial for Beginners (Grease Pencil Tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=5epzCprCdGc
author: Jesse J. Jones
ingested: 2026-07-20
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-2d-animation-tutorial-for-beginners-grease-pencil-tutorial/
frame_count: 0
frame_status: pending-selection
---

# Blender 2D Animation Tutorial for Beginners (Grease Pencil Tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=5epzCprCdGc)
**Author:** Jesse J. Jones
**Duration:** 50m5s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-2d-animation-tutorial-for-beginners-grease-pencil-tutorial <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] In this tutorial, we're going to go over how to animate in 2D in Blender, even if you've never touched a 3D program before.
[0:06] Blender may seem like a complicated program because of its 3D nature, but I guarantee you by the end of this, you'll be animating in it in no time.
[0:13] So let's get started.
[0:22] If you don't have Blender already, you want to go to Blender.org and click the big download button to download Blender.
[0:29] The version that we're using in this tutorial is version 3.6.
[0:32] So once you have that downloaded and installed, you'll be greeted with this welcome screen.
[0:36] So I recommend keeping all these settings to default except for the spacebar option.
[0:41] The spacebar, personally, I like to have it set to search.
[0:45] And that's useful because there's so many things in Blender that it can be hard to remember where things are.
[0:50] So instead, I could just press spacebar and search for what I'm looking for really quickly.
[0:55] So I recommend that.
[0:56] So once you have that set up, click Next.
[0:58] So that setup window only happens once.
[1:01] Usually when you start Blender, you'll see this welcome screen right here.
[1:04] So to make a 2D animation, we simply click 2D animation in this welcome screen and it'll set up a new project that's ready to animate in 2D.
[1:12] If for some reason you don't see that welcome screen and you're just in this 3D environment right here, you can always go up to File, New, and 2D animation from this menu as well.
[1:22] And that'll create a new 2D animation project.
[1:24] So to navigate around Blender, we're going to discuss two options.


### How to Navigate [1:25]
**Transcript (timestamped):**
[1:28] One for people who are using a tablet and one for people who are using a mouse.
[1:32] So if you're using a mouse, you want to use your middle mouse button, which is your scroll wheel.
[1:36] You just click that in.
[1:37] And if you click it in without pressing any hotkeys, it'll orbit around.
[1:41] So this actually takes you out of your 2D scene and puts you into a 3D perspective, which is not what we want.
[1:48] If we're animating in 2D, we want to keep things flat.
[1:50] We don't want to work in 3D.
[1:52] So to reset your camera, you can press zero on the numpad or you can press this camera button over here.
[1:58] And that'll reset the camera back to the 2D view.
[2:00] You can also use the scroll wheel to zoom in and out or you can hold down control and press middle mouse button and then click and drag to zoom in and out.
[2:08] You can also press shift and middle mouse button to pan around.
[2:12] And those are the three controls.
[2:13] Those are all you're going to need.
[2:15] You actually wouldn't really want to pan around.
[2:17] Sometimes I just do this accidentally so you can just quickly press the camera button to get back into it.
[2:22] But yeah, the important ones are shift and middle mouse to pan around and then control middle mouse to zoom in and out.
[2:28] Now, if you're using a drawing tablet, I like to set one of the buttons to be middle mouse.
[2:32] So that way I can just use my middle mouse button on my pen tablet, hold down shift and press that button to pan around, hold down control, press that button to zoom in and out.
[2:41] It's pretty easy.
[2:42] But let's say your drawing tablet didn't have any buttons on the pen.
[2:45] Well, there's an option for you.
[2:47] You can go up to edit preferences, go down to input and select emulate three button mouse.
[2:53] This will also work if you don't have a mouse with a middle mouse button on it.
[2:57] So you check that on and in older versions of blender, you had to go into this hamburger menu at the bottom left and click save preferences.
[3:04] But newer ones will have auto save preferences already turned on.
[3:07] So just something to be aware of if you're using an older version of blender.
[3:10] So once that's checked on, we just close our preferences window.
[3:13] And now to navigate, we use mouse clicks instead of pressing the middle mouse button.
[3:18] So to navigate this way, it's all with the alt button.
[3:20] So if I hold down alt just by itself and click and drag, you'll see it does the orbit that we were doing before.
[3:27] Click our camera to go back into 2D view.
[3:29] If I hold alt and shift, that'll pan around just like this.
[3:33] And if I hold alt and control, that'll zoom us in and out.
[3:36] So again, it's all done with the alt key and it just depends on what button you press after that.
[3:40] So all by itself orbits around in 3D alt shift pans around, alt control zooms in and out.
[3:47] And that's all you need to know.
[3:48] Now we can navigate and move around blender and we can get to the fun stuff.


### How to Draw [3:51]
**Transcript (timestamped):**
[3:51] So when you first start a 2D scene, it'll start you so that you can draw right away.
[3:55] You can start drawing strokes just like this.
[3:57] And it's even working with the pressure sensitivity on my tablet.
[4:00] If for some reason your pressure sensitivity is not working with your tablet.
[4:04] One thing you can check out is going under edit preferences and under input again under tablet.
[4:10] You can try changing this tablet API.
[4:12] Sometimes Windows, Inc. or one of these other ones may work.
[4:15] So if you're not getting pressure sensitivity, that's where I would check first.
[4:19] So anyways, we can draw right away as soon as we're in a 2D animation scene.
[4:23] If you want to change what brush you're using, you can click this little icon next to pencil.
[4:27] And that'll show all of the different brushes that blender has by default.
[4:30] So mess around with these.
[4:32] My favorite one is this rough pencil right here because it gives kind of a jaggedy kind of fun look.
[4:36] It almost looks like a brush pen.
[4:38] If you want to undo anything that you're doing, you can press Ctrl Z or you can press Ctrl Shift Z to redo it.
[4:44] To change your brush size, you can go up to this radius menu right here.
[4:47] Click and drag and drag that up and that'll make your brush bigger.
[4:51] You can also use the hot key of F as in frame.
[4:54] So if you press F once and then you just move your mouse, it'll make your brush bigger just on the fly.
[4:59] So that's a really easy way to change your brush size.
[5:02] You can also turn on and off pressure sensitivity with this button right here.
[5:05] So if I have that turned off, you'll see my pressure sensitivity doesn't work.
[5:09] Turn it back on and I get pressure sensitivity again.
[5:12] Strength is kind of like the opacity of the brush.
[5:14] So I could turn strength down to about 50% and you'll see we'll have a 50% opacity brush just like that.
[5:21] You can also turn on pressure sensitivity with strength.
[5:24] So that way the lighter you press, the lighter it is and then the harder you press, the darker your brush gets.
[5:29] You'll see it does some kind of weird overlapping things and that's just kind of an introduction that
[5:34] this is a 3D program that's using 3D elements to create 2D animation.
[5:39] So not everything's going to work like it does in Clip Studio Paint or any other raster program.
[5:44] So it's just about learning the quirks just like with any software.
[5:48] You learn the quirks and then you learn how to work with them.
[5:51] So that's the brush tool.
[5:52] The next tool we have down here is the paint bucket tool and we're actually going to get to that later.
[5:57] We're going to talk about filling in and coloring our animation once we have an animation to color.
[6:02] So we'll come back to color but the next one after that is the eraser.
[6:05] So the eraser is pretty straightforward.
[6:07] I'll just draw a few different lines here.
[6:09] Select the eraser.
[6:11] So if we use the eraser as it comes by default, you'll see it has this really soft kind of edge to it.
[6:16] And just like with the brush, if we want to change what kind of eraser we're using, we click on this icon next to the name right here.
[6:22] And you'll see all the different erasers that we have.
[6:24] Let's select eraser hard and then go back to erasing and you'll see it's not as soft as it was before.
[6:29] And again, you can press F to change how big or how small your eraser is.
[6:34] Up here are some pretty important options.
[6:36] There's dissolve, point and stroke.
[6:39] So dissolve is what we have by default.
[6:41] Just works like a normal eraser.
[6:42] For point mode, I'm just going to show that these lines are not made out of pixels.
[6:47] They're made out of curves and points.
[6:49] So if we select our eraser and select point, that's what point is doing is it's actually erasing all those different points.
[6:55] Even though it gets a similar result, it's working a bit different than the first dissolve eraser.
[7:00] So that's what point is for.
[7:02] For stroke, pretty straightforward.
[7:04] It erases an entire stroke.
[7:05] All you have to do is just click on it.
[7:07] Now for overlapping lines, if we were to draw a shape just like this and we had some overlapping lines,
[7:12] we can use this scissor tool to just draw a little circle around the overlapping line just like that.
[7:17] And it erases overlapping lines with the scissor tool.
[7:20] Pretty useful.
[7:21] So next down here are your geometry tools.
[7:24] So all of these tools, you can change with the same brush settings as you had before.
[7:28] So you can change what type of brush you want to use with your line tool.
[7:31] So to use these geometry tools, you draw with them once and it'll leave these yellow points on here that you can click and move after you've placed it.
[7:41] So if you need to edit it a little bit, once you're happy with it, you press enter or you can draw with it and then press middle mouse button to finish off your drawing.
[7:49] So same thing with the circle.
[7:50] I can draw a circle.
[7:51] Use these yellow points to move the circle around and press middle mouse button to draw that circle.
[7:56] If I hold down shift, I can keep proportions on.
[7:58] So that way if I want a perfect circle, I just hold down shift and then press middle mouse button and there's our perfect circle.
[8:04] So that's how you use the geometry tools.


### Blender Modes (Important!) [8:06]
**Transcript (timestamped):**
[8:06] So let's draw something just to illustrate one last concept before we get into animation.
[8:11] And this one's very important, so stick around.
[8:13] So if I were to draw something and I wanted to manipulate it, like let's say I wanted to move this smiley face and maybe move it over to the center.
[8:21] So you'll see there's no lasso tool necessarily.
[8:24] You can't really make a selection and that's because we're in draw mode.
[8:27] So if I click this draw mode drop down right here, you'll see a bunch of different modes that blender has.
[8:33] Now this is very important to know.
[8:34] Draw mode is pretty straightforward.
[8:37] It's the mode where you do all of your drawing in object mode is how you move entire objects.
[8:43] So if you look over here onto our outliner here, you'll see all the things that are inside of our scene.
[8:49] So we have a grease pencil object here called stroke and then we have our camera.
[8:54] That's everything that we have in this scene.
[8:56] So if we wanted to move our entire grease pencil object, we would go up to here, change from draw mode to object mode.
[9:04] And now you can see all of our tools have changed.
[9:06] Let's select the move tool first and I can click off of the smiley face to deselect it.
[9:12] And as soon as I click on the smiley face, you'll see this little widget pop up with arrows and little boxes.
[9:18] This is how we move entire objects around.
[9:21] So even though he's made of different strokes and he may even have like fills and different effects on him,
[9:26] he is one grease pencil object as we can see in the outliner here.
[9:30] So in object mode with the transform tool, I can click on this box, just move them around freely,
[9:36] or I can use these arrows to move them along specific axes.
[9:40] The hot key for this is G for grab.
[9:44] That's how I always think of it.
[9:45] I just say G for grab if I want to move something around.
[9:49] And again, this only works in object mode.
[9:51] If I were to go back into draw mode and press G for grab, it doesn't do anything because I'm in the wrong mode.
[9:57] So if I want to move objects around, I want to go into object mode and then G for grab.
[10:03] You also have the rotate tools here so you can rotate him along the y axis.
[10:08] If you did it along the z axis, you can see he's rotating in actual 3D.
[10:13] So maybe that's something you want to do.
[10:16] And same with the x axis.
[10:18] This is also in 3D.
[10:19] So that might not be what you want to do, but that is an option because this is a 3D program.
[10:24] So let's control Z to undo that.
[10:26] Also, the hot key for rotate is R.
[10:28] So if you just press the hot key of R, it'll start rotating.
[10:31] And for rotations, the closer you are to this rotation point, the more dramatic it's going to rotate.
[10:36] If you want to do a really subtle rotation, you want to move your mouse a little bit further away from the anchor point.
[10:42] And then you can do really fine-tune rotations that way.
[10:45] And then just press enter when you're happy with that rotation.
[10:49] And then you've got scale right here.
[10:50] So scale again, you can click this box to scale your object proportionally.
[10:56] Or you can click one of these axes to scale him left or right.
[10:59] And the hot key for that is S for scale.
[11:02] And that's our transform tools under object mode.
[11:05] The other mode that's really important to know is edit mode.
[11:08] So if I wanted to move specific strokes inside of this grease pencil object,
[11:12] what I would want to use is edit mode.
[11:14] And under edit mode, we can see these buttons over here.
[11:18] So the really important ones to know are point mode and stroke mode.
[11:22] So point mode is how we can edit very specific points on our stroke.
[11:25] So we can take strokes and move them.
[11:27] Again, it's the same hot keys as before, G for grab.
[11:30] So if I selected some points, use G for grab.
[11:33] I can move them.
[11:33] I can use R for rotate.
[11:35] I can use S for scale if I want to.
[11:37] And that's how to move specific points.
[11:39] Not super useful, but that may come in handy.
[11:41] What's probably more useful is stroke edit mode.
[11:44] So that way you can select an entire stroke like his eyeball here, for example,
[11:48] is just me drawing in a circle in the same spot a lot.
[11:51] So it's one big stroke.
[11:53] So I can rotate it with R.
[11:55] I can G for grab.
[11:57] I can S for scale.
[11:58] So that's how you move individual strokes is under edit mode and stroke mode.
[12:03] So point mode wasn't super useful, right?
[12:05] If we wanted to just move points around, it's not very accurate and kind of clumsy.
[12:10] What we want to do instead of doing that is go into sculpt mode.
[12:14] So sculpt mode is very cool.
[12:16] Sculpt mode, you get all these different sculpting options.
[12:19] And I would recommend playing around with them.
[12:21] The only one I'm going to show you here is this push mode right here.
[12:24] So again, I can use the hot key of F to change how big my stroke is.
[12:28] And with push mode, I can literally push my lines around this way.
[12:32] So if I wanted to just move things around and kind of get lines exactly where I wanted them,
[12:37] I can use this sculpt mode to kind of push lines into place exactly where I want them.
[12:42] All right, I feel bad for this guy.
[12:44] So let's move on.


### How to Animate [12:45]
**Transcript (timestamped):**
[12:45] So now that we know how to draw, let's animate something.
[12:47] I always like doing a bouncing ball just because it's something that everybody can do.
[12:51] So we're going to grab our circle tool here, select the pencil icon up here and select
[12:55] what kind of pencil you'd like to use for it and just draw a circle on the top third of the screen.
[13:01] Again, you can hold down shift to make sure it's a perfect circle.
[13:04] And then when you're happy with your circle, either press middle mouse button or enter
[13:08] and that'll confirm our circle drawing.
[13:10] So down here in this window is our timeline.
[13:12] This is where our animation is going to happen and where all of our keyframes are going to go.
[13:16] So this blue line right here is our playhead.
[13:19] This is what frame we're currently on.
[13:21] So we can click and drag to move from left to right in our timeline.
[13:25] Right now we're on frame number one and you can see we have these diamond shapes here
[13:29] indicating that we've drawn our first frame and you can see that there's two layers.
[13:33] There's a lines layer and a fills layer.
[13:35] We'll come back to that once we get onto coloring, but just understand that we're drawing on our lines
[13:40] layer right now and we've drawn our first frame right here.
[13:43] And right now our timeline is 250 frames long, which for a bouncing ball, that's a little bit much.
[13:49] So what we can do is we can change the length of our animation down here on the bottom right.
[13:54] We can change our start position, but most importantly, we can change our end position.
[13:58] So I'm going to set our end position to something like 20 and press enter.
[14:01] And that way our animation is only 20 frames long and we need to zoom in because right now we're still zoomed out to 240 frames.
[14:09] So to zoom in on the timeline, you simply just grab the right side of the scroll bar right here and just drag it to the left to zoom in.
[14:16] And if you want to zoom out again, you just click and drag on the right side and drag it to the right.
[14:21] So let's take our playhead and drag it over to frame number two and we're going to do our next frame.
[14:26] So down here next to your play button is this little circle right here.
[14:31] This is called automatic keying.
[14:32] So the way it works is whatever changes you do, it's going to automatically create a key frame.
[14:38] So for example, I could take my circle tool here and just draw another circle just slightly lower than the one we have already.
[14:45] Just like this.
[14:46] And when I press enter, you'll see our previous circle gets grayed out.
[14:50] So this is the onion skin.
[14:51] This is what's showing our previous and next frames.
[14:55] So right now it's showing our previous frame number one and then we just drew our frame number two.
[15:00] So auto keying this button down here automatically created a key in our timeline of our new circle drawing.
[15:07] So we could go down to frame three, do that again, just draw the same circle, but have it go just a little bit farther beyond what we did last time.
[15:15] Something like that.
[15:16] And you can see I'm starting to stretch it out.
[15:18] So now we have three frames of animation.
[15:20] You can also if you don't want to redraw your frame, you can also use the edit tools to manipulate your drawing to add a new key frame.
[15:27] So let's do that for this frame.
[15:29] So we're going to change from draw mode down to edit mode.
[15:32] So again, remember the edit mode is what allows us to transform our points in our drawing.
[15:37] So you can see we're on frame four right now.
[15:39] There's no key frame.
[15:41] But if I were to select all of my points, go to the move tool down here and then move it down on the z axis just like this.
[15:48] And then I can also take my scale tool here and scale it both on the x axis and the z axis.
[15:54] So it stretches out just like that.
[15:56] You can see it's created another key frame.
[15:58] It also created another fill key frame, but we'll clean that up later.
[16:02] So that's how you can manipulate your drawings is using the edit mode and that'll also create a key frame with auto key on.
[16:08] So one thing you may want to do is edit your onion skins, like change how many there are or change the color of them.
[16:14] And the onion skin settings are going to be under here under this green squiggly.
[16:18] A lot of really useful grease pencil settings are going to be under this green squiggly here.
[16:22] So if we go down to where it says onion skinning, you can change the opacity here and here you can change the number of onion skin.
[16:28] So I can increase this to three on both sides and then I can see three drawings before and three drawings after.
[16:34] You can also change the colors down here and I don't really like these colors personally.
[16:39] Usually the colors I like to do are more of a red for my before drawings and then a green for my after drawings.
[16:45] I kind of think of it like a traffic light.
[16:47] It's like green for go and red for stop or backwards.
[16:51] And that's how you change your onion skin settings.
[16:53] So let's finish our bouncing ball animation.
[16:56] Let's go one more frame, move it down pretty far again, scale it up and then squish it in for a good stretch drawing just like that.
[17:03] And then for frame number six, we're going to have it impact the ground.
[17:07] So for this one, it's going to be squashed on the ground, right?
[17:10] So let's go back into our draw mode, grab our circle tool.
[17:13] We're on our next frame and just drag a ball that's being squashed out just like this.
[17:18] Press enter to confirm it.
[17:19] And now we have the first half of our bouncing ball animation.
[17:22] So it starts out slow and then picks up speed, stretches out and then squashes to impact the ground.
[17:28] Let's talk about how to manipulate keyframes.
[17:31] So we created these extra keyframes for our fills, right?
[17:34] We want to get rid of them.
[17:35] So let's do that right now.
[17:36] I'm going to click and drag a selection around them and I'm going to press X to delete them.
[17:41] So when I press X, this menu will pop up.
[17:43] I'm just going to select delete keyframes just like that.
[17:46] I can also drag a selection and click and drag to move keyframes around if I want to change the timing of something.
[17:52] And here for this example, we want the ball to bounce back up using these same frames, right?
[17:58] But in reverse order.
[17:59] So the way we do that, the way we can copy frames is select the frames we want to copy and press shift D to duplicate.
[18:07] And then move your mouse to where you'd want them to be and then click to confirm your selection.
[18:11] So now we have our keyframes copied, but there's a problem.
[18:14] They're going in the wrong order.
[18:16] So with keyframes, just like other stuff in Blender, you can press the same hotkeys.
[18:20] So for example, I can use G to grab and that means I can also use S to scale.
[18:25] So you can see if I move to the beginning of the selection and press S to scale, I can scale the timing of these keyframes.
[18:31] It's pretty cool.
[18:32] And what that also means is we can type in numerical values.
[18:36] So if I press S to scale and then press negative one and then press enter to confirm, it has now scaled these keyframes in the negative direction.
[18:45] So now they move in the opposite direction.
[18:48] And again, I can use G for grab and just move it right where I want it to be, finishing the rest of our bouncing ball.
[18:53] Pretty cool.
[18:54] And again, our animation is too long.
[18:56] Frame number 11 is just going to be a copy of frame number one.
[18:59] So let's have our animation and on frame number 10, we're going to go down here to the end of our animation.
[19:05] Set that to 10.
[19:07] And now if we play our animation, you can see we've created our bouncing ball.
[19:10] Pretty cool.
[19:11] Now it might be playing a little bit fast and there's a couple things we could do about that.
[19:15] So right now this animation is happening on what we call ones.
[19:19] There is a new drawing for every one frame, right?
[19:22] But in a lot of traditional animation, animation is done on twos.
[19:26] So each one of these drawings would be exposed for two frames.
[19:30] So one thing we can do is change our animation from being on ones to being on twos.
[19:35] So let's set our animation to be 20 frames instead of 10.
[19:39] Select our keyframes and remember how we use scale to modify our keyframes.
[19:43] We could do that here.
[19:45] So if I press S and then two, that will scale our keyframes by two times.
[19:50] So now our keyframes are on twos.
[19:52] Pretty cool.
[19:53] So now if we play our animation again, you can see our animation slowed down and feels a little bit nicer.
[19:58] So that's one way you can animate on twos.
[20:00] And now that we finished an animation, let's export it.


### How to Render [20:01]
**Transcript (timestamped):**
[20:03] To export our animation, we want to go into our output options, which is up here,
[20:08] which kind of looks like a little printer to me.
[20:10] So here is where you're going to change all of your animation settings, the resolution, the frames per second,
[20:15] all of that stuff, how long the animation is.
[20:18] So I'm going to keep this all by default.
[20:19] You can see my settings here.
[20:21] And then down here in the output folder, I'm going to click the folder icon to browse to where I want to save it.
[20:27] Go into that folder and press accept.
[20:29] And then for the file format, instead of a PNG sequence, we want to set that to be an FF MPEG video.
[20:36] So this one right here, one more setting we probably want to edit is our encoding setting.
[20:41] So if we click this arrow to twirl down our encoding settings, you can change your output quality and stuff like that.
[20:47] I would just leave this as default.
[20:49] The thing I would recommend changing though is the container.
[20:52] So that's what file extension your animation is going to be exported as.
[20:55] And most likely what you're going to want to use is MPEG for.
[20:59] So that'll export it as an MP4 file, which is pretty useful in most cases.
[21:03] So once our output settings are set, we don't need to set them again.
[21:06] And to render our animation, we simply go up to render and then click render animation.
[21:11] And you'll see blender go through all of your frames and render them.
[21:14] And once it's done with that, you can actually take this window and just close it out and then navigate to your folder.
[21:20] And there's our animation.
[21:21] Pretty cool.
[21:22] So very quickly, that's how we create an animation and then export it as a video and blender.
[21:27] Let's go over some more advanced features now like how to color in our animation, how to add shading, how to animate a camera,
[21:34] and also how to import audio and do lip sync.
[21:36] So the animations we're making in this tutorial are pretty simple.
[21:40] If you'd like to learn more, I have a full on animation course, which you can check out in the link below.
[21:45] My animation course teaches you how to animate characters with believable emotions and expressions.
[21:50] And every topic gets straight to the point with no time wasted and includes example files.
[21:55] So you can follow along.
[21:56] Great for people with short attention spans or very busy lives.
[21:59] So if that sounds appealing to you, make sure to check out my full on animation course in the link below.
[22:04] Okay, back to the tutorial.
[22:05] So to fill in our animation, we're going to select our paint bucket tool.


### How to Color [22:06]
**Transcript (timestamped):**
[22:09] And we also want to make sure that down here right now we can see our lines layer is selected because it's yellow.
[22:15] We want to select our fills layer.
[22:16] It's really good practice to keep your fills on a separate layer for a lot of reasons.
[22:21] One of them being is we're going to shade later and we're going to use our fill layer to use as a mask for doing our shading.
[22:27] So we've got our fills layer selected.
[22:29] We've got our paint bucket tool selected.
[22:31] And to change our paint bucket color, there is this drop down here that changes what's called our material or what our fill is.
[22:38] There's these ones created by default and we could select this gray solid fill right here and then click our circle to fill in.
[22:45] But when you click to fill in your circle, nothing happens.
[22:48] You actually have to click again to confirm your selection and that can get pretty annoying.
[22:52] There's actually a setting to turn that off so that that doesn't happen with our paint bucket selected.
[22:57] If we go into our tool options, which is this screwdriver and wrench icon right here and we go down into brush settings.
[23:04] It says brush even though we're using a paint bucket and then we go into advanced and turn off visual aids.
[23:09] If we turn that off now when we click once to fill, it'll just fill with one click.
[23:14] So it makes it super easy.
[23:15] So let's do that for our first frame and then our third frame will click to fill in right here.
[23:21] And you'll see because we have auto key frame turned on, it'll make a new key frame with that new fill in.
[23:27] So even though our old fill is showing, we can still click our circle on this frame and it'll get rid of our old fill and replace it with the one that we just did and make a new key frame for it.
[23:38] So that's cool and all, but let's say we don't want the gray color here.
[23:42] The gray is kind of boring.
[23:43] So to change your colors in grease pencil, we want to go into our material properties and that's going to be this beach ball right here.
[23:51] Remember, we had this drop down with all of our different colors.
[23:54] So that's what these are.
[23:55] That's under the beach ball under all of our materials.
[23:58] So we were drawing with our black solid stroke and filling in with our gray solid fill.
[24:03] There's some here that we don't really need so we can select them and press minus to get rid of them.
[24:08] Let's make a new color from scratch.
[24:10] So to do that, we're going to click the plus button to create a new material.
[24:14] It'll create a new material slot, but it won't actually create a new material until we click this new button right here.
[24:20] So that's created a new material and here is where you set it, whether you want it to be a stroke, which is for the pencil tool, or you want it to be a fill, which is for our paint bucket.
[24:30] So let's select fill.
[24:32] Let's set the style to solid though.
[24:33] You can change it to gradients and texture here and we'll change the base color to something like a light blue color like this.
[24:40] And if we want to rename this material, we can just click in its name right here and call it blue center.
[24:45] And now when we go into our paint bucket tool and click this drop down, you'll see our new material that we created.
[24:50] So select that and now you can fill it in on each one of these frames with our blue color.
[24:55] Now you can imagine this might be pretty tedious filling in every single frame and luckily for us, there's actually a quicker way to do this.
[25:02] So let's undo all of our colors.
[25:04] So if we wanted to fill in multiple frames of animation, we would use this option up here, multi frame.
[25:10] So if we turn on multi frame, the next thing we need to do is select how many frames we want multi frame to work with.
[25:16] So I'm going to drag a selection around our entire animation.
[25:20] And then if I click with multi frame turned on, you'll see it didn't fill in every single ball.
[25:25] I just clicked inside this ball around here.
[25:28] It's only filled in where I clicked.
[25:30] So what you would actually want to do is use what's called inverted fill.
[25:34] So if you see up here, there's a plus and a minus icon.
[25:37] So plus just means where you click is where it gets filled in.
[25:40] The minus means if you click outside of your object, it's going to fill everything inside of your object in with the minus button turned on with inverted fill turned on.
[25:49] Instead of clicking inside the ball, I want to click actually outside of the ball outside of any of this animation.
[25:55] And that'll fill in the whole object.
[25:57] And since we had all of our frames selected with multi fill turned on, it's filled in all of our colors just like that.
[26:03] Just in one fell swoop.
[26:04] Super easy, super convenient.
[26:07] So really quickly before moving on, something kind of weird about filling in, I wanted to make sure to go over is if you have a shape with holes in it, like, let's say we were to draw a shape that was like a blender donut.
[26:18] So that's on my lines layer.
[26:20] And then I grab my paint bucket.
[26:21] I select the fills layer and I select my fill in color and I click to fill this shape.
[26:26] You'll see it fills in all the holes as well.
[26:28] So in order to fix this, we actually have to make a new color with this holdout option turned on.
[26:33] So that's what holdout is for is for creating transparencies.
[26:37] So to do that, all I need to do is create a new material with this plus button and I'm in my material slot, which is the speech ball right here.
[26:44] So create a new material, click plus new to create it, double click on it to rename it.
[26:49] We can call it something like erase and make sure it's set to fill and then select holdout.
[26:53] The color here doesn't matter.
[26:55] But once we select holdout and we're on our erase material, we can fill in with our paint bucket tool on this hole right here.
[27:01] And that'll get rid of any holes inside of your object.
[27:04] So pretty useful to know.
[27:05] But back to our bouncing ball.


### How to Add Shading [27:07]
**Transcript (timestamped):**
[27:07] So now that we have our bouncing ball all filled in, let's do some shading on it.
[27:10] So down here in our timeline, we've got multiple layers, right?
[27:13] We've got our lines layer and our fills layer.
[27:15] So we can actually add a new layer by clicking the plus button up here and you'll see it'll add a new layer called GP layer.
[27:21] We can double click on it and call it shadow.
[27:24] And if we want to change the order of these layers, we can use these up and down arrows to move the selected layer up or down.
[27:31] So that's created a new layer for our bouncing ball.
[27:34] But all three of these layers exist in one object, this stroke object, which is our grease pencil object.
[27:40] You can think of the grease pencil object as kind of a group and inside of this group, it has as many different layers as you want.
[27:47] This stroke layer is actually our entire bouncing ball animation.
[27:51] It's the fills.
[27:51] It's the lines.
[27:52] It's the shadow that we're going to do.
[27:54] If we wanted to do a separate quote unquote layer, we could create a new grease pencil object and anime
[28:01] in that and you could think of that as another layer.
[28:03] We'll talk about creating and animating separate grease pencil objects later, but continuing on with shading.
[28:09] We've made a new layer inside of our bouncing ball called shadow and we want to make a new shadow color.
[28:14] So I'm going to click the beach ball right here and under our materials.
[28:18] We're going to press plus to create a new material.
[28:20] And if you want to create a duplicate of a color you've already made, what you would do is instead of clicking new, you would click this beach ball logo right here and select the color you want to duplicate.
[28:30] So we'll select blue and technically this is the same color.
[28:34] So if I were to change this blue and say make it darker, it's going to do that for our original blue color as well.
[28:40] And probably a good time to mention that if I were to edit this blue color, the one we filled in with our ball, even if it were filled in on a thousand different frames.
[28:48] If I were to change this color to say like a green, it does it across the whole animation.
[28:52] So any updates you make to this material, it's going to affect wherever you use that material to fill it in.
[28:58] So anyways, with this duplicated color that's still connected to the original, what we want to do is we want to separate it from the original color.
[29:05] And we do that by clicking these two paper icons.
[29:08] It's kind of like a copy symbol.
[29:09] And once we do that, it'll add a little number.
[29:11] That's how you know that it's a separate color now.
[29:14] So now I can select this color, move it a bit more towards the blue here and then darken it a little bit to make the shadow color.
[29:20] And you can see this color is now separate from the original here.
[29:23] And to rename it, we can either click in here or double click up here.
[29:27] We'll call it ball shadow.
[29:29] And we want to make sure that it's a fill and not a stroke.
[29:32] And then we want to take our pencil tool, not our fill tool.
[29:35] And when we draw with a fill, it almost works like a lasso tool.
[29:38] So this can be kind of fun to mess around with and, you know, try to draw with bill tools.
[29:43] But anyways, let's draw a shadow for our first frame of our ball.
[29:47] We'll just do a little C shape like this and then a C shape going the other way, just like that.
[29:53] And we can also go into sculpt mode and something to be aware of.
[29:56] It's going to affect all of your layers.
[29:58] So you want to make sure to lock the layers with this lock icon, the ones that you don't want to edit.
[30:04] So that way we can just edit our shadow with our sculpt tools this way.
[30:07] So get that looking how you want it to look.
[30:09] And we're going to manipulate this shadow on all of these layers.
[30:12] So I'm going to keep my lines layer and my fills layer locked since we don't want to edit those while we're modifying our shadow animation.
[30:19] And obviously the shadow is going beyond the borders here.
[30:22] So remember how I was saying we want to keep our fills separate.
[30:25] So this is why what we can do with this shadow layer is go into our layer properties, which is this window over here.
[30:31] We can change the blend modes to be multiply if we wanted to set it to a multiply blend mode or anything like that.
[30:37] Add is really good for highlights if you wanted to add highlights to your animation.
[30:41] But we'll just set it to regular for now.
[30:43] Also under these layer properties, for some reason, each one of these layers has used lights turned on.
[30:49] You should turn that off on every single layer actually.
[30:51] That just means it's going to be affected by lights in your scene, which for a 2D animation, you probably don't want.
[30:57] It might end up making your animation darker than you want it to be.
[31:01] So make sure use lights is turned off for all of your layers.
[31:03] And then if we scroll down on our shadow layer, we'll see this mask option right here.
[31:08] So if we click the check mark on mask and then click the arrow to twirl it down, we can add a layer to use as a mask for our shadow.
[31:15] So we're going to click the plus button and we're going to select our fills layer.
[31:19] And the reason it's looking lighter than we probably think it should is because of our onion skin.
[31:23] Our onion skin is overlapping it.
[31:25] So we can actually turn on and off our onion skin using these little bouncing ball icons.
[31:30] If we turn those off, that'll turn off our onion skins just like that.
[31:33] You can also turn off your onion skin by turning on and off this overlay button, which looks like two intersecting circles.
[31:39] And now we can see what our shadow looks like.
[31:41] So you could see it's using the fill as a mask to cut off all the extra here.
[31:45] So you could go through and go to our second frame and go into draw mode, select our pencil and draw a new shadow by hand, just like that.
[31:54] But the easier thing to do here would actually be to go into edit mode, right?
[31:58] So if we go into edit mode, we can move the points of our shadow here.
[32:01] So I can actually select all of my points, go to my move tool, or I can press G for grab and then press Z to keep it on the up and down axis just like this.
[32:10] And that change that I made in edit mode has made a new key on frame number three.
[32:14] So I didn't have to redraw anything.
[32:16] I could just move my mask manually just like that.
[32:19] And same thing as we did before, we can use our scale tool and scale it along with our ball just like this.
[32:24] And just keep going frame by frame, editing our shadow on each one of these frames here.
[32:29] And then again, we can reuse the frames that we already did and duplicate and reverse them over here.
[32:35] So again, to do that, I'm going to select the frames we want to copy, which are these ones right here.
[32:39] Press shift D to duplicate, move them over, drag our playhead to where we want the scale to pivot at.
[32:45] I'm going to move my playhead towards the end here and we're going to press S to scale and then negative one.
[32:50] And then press enter.
[32:51] Then again, G for grab to move it back into place.
[32:54] And that way we've inverted our scale.
[32:56] So now our keyframes move back in reverse.
[32:59] And there we've shaded our animation.
[33:01] Super easy, super cool.


### How to Resize or Adjust Scene [33:03]
**Transcript (timestamped):**
[33:03] If we wanted to make some changes to this entire animation, the way we would do that is to go into object mode.
[33:10] So remember how I was saying that all of these layers exist within this one stroke object, this one grease pencil object?
[33:16] Well, that's what object mode does is it modifies this entire grease pencil object and everything inside of it.
[33:23] So under object mode, I can actually take my scale option here.
[33:26] This is important.
[33:27] If you don't want to create keyframes while doing these edits, make sure auto keyframe mode is turned off.
[33:32] So if you want to do a global change like scaling the animation down like this and you want that to happen throughout the whole animation,
[33:39] make sure that auto keyframe mode is turned off so you don't accidentally create a keyframe.
[33:44] And now our animation is tiny.
[33:46] Let's undo that.
[33:47] One thing that can be kind of weird for new people to blender is how to rotate something along a different pivot.
[33:54] There's no clear way to move this pivot.
[33:56] It's just in the center of our animation.
[33:59] So for example, if we wanted to rotate it from this point down here, how would we do that?
[34:04] Well, that's where 3D cursor comes in.
[34:07] So 3D cursor is a blender concept that is super important and super useful and we don't have the time to get into all the uses for it.
[34:16] But for something like this where we want to change the pivot is one use that the 3D cursor can have.
[34:21] So we don't see our 3D cursor right now.
[34:23] We need to go up to our overlays up here, which is this drop down and we select 3D cursor.
[34:28] We can now see this little outline here, this little dotted outline.
[34:32] So to move this 3D cursor to a new spot, we want to shift and right click.
[34:36] That's how you can set your 3D cursor to be in different spots.
[34:39] So shift and right click.
[34:41] So it's where you want to pivot your rotation.
[34:43] Go to your rotation tool and it's not going to work yet because we have to change where our rotation is happening from.
[34:49] And that's under this option right here.
[34:51] See these little two circles joining each other.
[34:54] If we click this drop down, this is where we can change where our manipulation is.
[34:58] So this is where our rotation is happening at.
[35:00] So this works for our move tools or scale tools.
[35:03] It works for everything.
[35:04] So by default, it's at median point, which just means the center of everything you have selected.
[35:09] And for a lot of the times that's going to be useful.
[35:11] Sometimes these other options will be useful as well.
[35:13] It just depends on what you're doing.
[35:15] But for this case, we want to set that to 3D cursor.
[35:17] So once we do that, our rotation moves to where our 3D cursor is and we can rotate from that pivot point.
[35:24] So now our animation has been rotated that direction.
[35:26] So now we can move to our 3D cursor.
[35:28] You can press shift S and you could just say cursor to world origin and just select that there.
[35:33] And that'll reset the 3D cursor back to where it was at the beginning.
[35:37] And then when you're done with it, you can either leave it on or you can turn it off by clicking the drop down under overlays and turning off 3D cursor.
[35:43] And that's how you rotate something from a different pivot.
[35:46] After you're done, you may want to change your edit objects from 3D cursor back to median point just so we don't forget.
[35:52] Another thing that may be helpful to know is how to blip something horizontal.
[35:56] How we were scaling by negative one on the timeline down here.
[36:00] We also want to make sure our cursor is where we want to do the edit.
[36:03] So we want to make sure our cursors in the camera view.
[36:05] So if I were to press S for scale and then type negative one, it's actually just going to invert the whole thing.
[36:11] So that's not what we want to do if we want to flip horizontal.
[36:14] We want to flip it along this red line right here, right?
[36:17] If we think of this as a stripper pole, we want it to flip around the red stripper pole, not the blue one, right?
[36:24] And these colors are pretty standard.
[36:25] Red usually means X, blue is usually Z and then green is usually your Y axis.
[36:32] You can also see that up here.
[36:33] You can see where your Y axis, your X axis and your Z axis are.
[36:38] So if we wanted to flip this horizontal, keeping the stripper pole idea in mind, we'd have to press S for scale,
[36:43] X to rotate it on the X axis and then type negative one.
[36:48] So I'll do that one more time.
[36:49] S for scale, X to do it on the X axis and then negative one.
[36:54] And that's flipped it horizontal.
[36:55] And typing commands like that is super duper useful.
[36:58] You can do it for any of those edits.
[37:00] So if I were to type R for rotate and then press the numbers 90, it's now rotated it 90 degrees.
[37:06] If I were to do that the other way, I'd type R for rotate and then negative 90 to rotate it 90 degrees the other way.
[37:12] So if you want to do a really precise rotation, that's one way that you can do it.
[37:16] So that's how to globally modify and edit your animation.


### How to Import Images [37:19]
**Transcript (timestamped):**
[37:19] All right.
[37:19] So now that we have our animation all finished, let's talk about importing a background and animating a camera for your scene.
[37:25] So to import a background into Blender, it's super, super simple.
[37:28] First off, let's go out of draw mode and go into object mode since we're going to be working with some objects.
[37:33] And to import an image, we actually have to turn on what's called an add-on.
[37:37] So to find your add-ons for Blender, that's going to be under edit, preferences, and then go into add-ons.
[37:43] And a lot of these are super duper useful.
[37:45] I would recommend checking out videos on Blender add-ons that may be useful to turn on.
[37:49] But the one that we're going to turn on is called import image as planes.
[37:54] So go up to your search bar and search for the word image.
[37:57] And you'll see this.
[37:58] This should be checked on by default, but it's not.
[38:00] So we're going to click the check mark to enable it and then close this out.
[38:04] So now to import a background into your scene, all you need to do is go up to file, import, and go down to image as planes.
[38:10] And then select your image and press import, and it'll import your image.
[38:15] You may need to press S to scale it up if you need to, and G for grab to reposition it.
[38:19] And now we have a background for our scene.
[38:21] If you wanted to add some cool parallaxing to it, we can use our middle mouse button to orbit around our scene.
[38:26] So you can see what our scene looks like in 3D.
[38:29] And I'm still in object mode because we're editing objects, right?
[38:32] So that enables me to use my grab tool, my move tool, and I can move it along this y-axis right here to move it back into space.
[38:39] So if we click our camera button to go back into our camera, we may need to resize it so that it matches the camera again.
[38:45] But now our background's a little bit further back into space.
[38:48] So we won't see this affecting anything until we actually animate our camera.
[38:52] So let's do that.


### How Animate the Camera [38:53]
**Transcript (timestamped):**
[38:53] So to animate an object, and you can do this with the camera or with your grease pencil object or your background.
[38:59] This is how you would motion tween anything in Blender.
[39:01] First, we're going to select the object we want to animate.
[39:04] In this example, we're going to select the camera here.
[39:06] So to add our first keyframe for our camera animation, we want to add the first keyframe on frame number one.
[39:12] So our playhead is on frame number one right now.
[39:15] And it may be a little bit hard to see, but there's this little dropout menu right here.
[39:20] It's a little arrow that you can click on to bring up this transform window.
[39:23] You can also press the hot key of N to turn that on and off.
[39:26] And that gives us all of our transformation values, our rotation values, our scale values for the object we have selected.
[39:32] So we're going to be animating with the transform options on our camera.
[39:36] So our camera's selected.
[39:37] We have our transform window open.
[39:39] We're going to right click in our location information here and go to insert keyframes.
[39:44] And you'll see all of our values turn yellow.
[39:46] And that means there is a keyframe on this frame.
[39:48] If we drag our playhead to another frame, you'll see it turns green showing that there's a motion tween happening here, but this is not a keyframe.
[39:56] So let's go down to frame 20 and we can add our next keyframe in a couple of different ways.
[40:00] One is we can turn back on our auto keyframe button right here.
[40:04] Use middle mouse to orbit around.
[40:06] Use control middle mouse to zoom out.
[40:08] Grab your camera and then drag it along this y-axis here to just push it forward.
[40:13] And if we go back into our camera view, you can see that we've zoomed in a little bit.
[40:16] And if we drag our playhead back and forth, you can see we now have a camera move.
[40:20] Another way we could have done it if we undo that is make sure auto keyframe is turned on and then just drag one of these sliders until it's at a value that you're happy with.
[40:29] And you'll see only that value will turn yellow because it's the only one we edited with auto keyframe turned on.
[40:34] So that's another way you can animate a camera.
[40:36] Next, we'll go over how to animate lip sync in Blender.


### How to Animate Talking Characters [40:39]
**Transcript (timestamped):**
[40:39] All right.
[40:40] So we're back in Blender.
[40:41] We're just going to start from scratch to create our lip sync scene from the splash screen.
[40:45] I'm going to click 2D animation or I can also go up to file new and 2D animation.
[40:51] So down here is our layers for the current grease pencil object that we have selected.
[40:56] And we can actually double click on this grease pencil object to rename it.
[40:59] I'm going to call it character one and I'm on my lines layer.
[41:02] I'm going to draw the first character on the right here drawing everything except for his mouth.
[41:07] So here's character number one as a grease pencil object.
[41:10] So to add a new grease pencil object, I need to get out of draw mode.
[41:14] So draw mode enables me to draw on whatever layer I have selected in my outliner up here.
[41:19] So I need to get out of draw mode by clicking this drop down up here and go into object mode since I want to create a new object and
[41:26] press shift a to create a new object.
[41:28] This is how you can add 3D objects.
[41:30] So things like cylinders, cubes, but we want to go down to grease pencil and we want to add a blank of grease
[41:37] pencil object that we can draw ourselves.
[41:39] You can add a stroke, but it adds a stroke for you and it just gives you like an extra step of something to delete.
[41:44] So I like to add a blank grease pencil object whenever I do this and we're going to go up to our outliner on the top right here.
[41:50] Double click on this and I'm going to rename it to character two and you can see with this new grease pencil object.
[41:56] It doesn't give us our default layers down here on the bottom left.
[41:59] We actually have to make our own.
[42:01] So we can double click this layer and call it line and we can click this plus button up here to add a new layer.
[42:06] Click this down arrow to move it underneath line like this and then double click on it to rename it to fill.
[42:12] And if we select line again, now we have it set up so we can go back to draw mode and it's just the same as our first character.
[42:18] We did so he's all set up just like our original grease pencil object, but it's as its own separate object over here.
[42:24] Also, you can kind of think of it as another layer of something to animate.
[42:28] So we're going to draw our second character here on the left.
[42:31] But now we have our two characters, one on the left and one on the right.
[42:34] So if we want to move or adjust these characters, we want to go into object mode and then we can select what character we want to move and then use G for grab.
[42:42] Move them into place.
[42:43] Select the other character G for grab.
[42:45] We can also use S for scale.
[42:47] And that's how you would move and edit your characters.
[42:49] So let's go into character one.
[42:51] We'll go back into draw mode and we'll make a new layer down here by clicking the plus button and we'll double click on that layer and call that the mouth layer.
[42:59] And we'll draw in his first mouth, which is going to be a closed mouth.
[43:03] All right.
[43:04] So now that we have our characters drawn out and ready to animate, let's import our sound that we want to animate to.
[43:10] So to import sound into Blender, we actually have to go into a different window here.
[43:15] So to change any of these windows, it's this top left button up here.
[43:19] So you can see if I click this top left button, it gives me all of these different options of what I can change this window to.
[43:25] This top left button is actually on each one of our different windows up here.
[43:30] So you can see my outliner has that top left button.
[43:33] This layers property has that button.
[43:35] I wouldn't recommend messing with these unless you know what you're doing.
[43:39] So just follow along here.
[43:40] So here we want to change it from dope sheet dope sheet is what we're using right now with all the keyframes and everything.
[43:46] We're actually not using timeline.
[43:48] I know that might be a little bit confusing if you're coming from something else.
[43:51] The dope sheet is what we've been animating in so far.
[43:54] So we want to change this from dope sheet to video sequencer.
[43:57] So select video sequencer right here and then up here at the top we click add and then sound navigate to where your sound file is.
[44:04] Select it and then click add sound strip.
[44:07] And if we play our animation, have you ever had a dream that you can hear a sound clip play and same thing as before you can press G to grab if you want to move it around.
[44:16] Or you could just click and drag it to move it if you want to change the timing on this audio here.
[44:21] So now that we have our audio imported, we're going to go back into our dope sheet here.
[44:25] Make sure we've got character one selected go into draw mode.
[44:28] So if we scrub through with our play head, you'll see that no audio is happening.
[44:33] And in order to lip sync, it's pretty helpful if we can scrub through our audio and hear what sounds are being said.
[44:38] So to enable scrubbing in your scene, you want to go down to this playback drop down right here and turn on audio scrubbing with this check mark right here.
[44:46] So now if we scrub through, you can hear the audio that we're going to animate to.
[44:52] So let's do that.
[44:53] I'm going to put up a mouth chart right here so you can see different mouth positions for different sounds.
[44:58] This is a rough guide and I would really recommend acting out your scene in front of a mirror, especially if you don't know what kind of mouth shape to draw.
[45:06] This can be a really helpful exercise.
[45:08] So we're going to go through and just draw mouth shape after mouth shape and lip sync our audio.
[45:13] So let's go to the first sound that we hear.
[45:16] And again, we can drag this scroll bar to just zoom in a little bit might make it a little bit easier.
[45:23] So here I can hear his mouth start to open.
[45:25] So with auto key frame turned on, all I have to do is start drawing and it'll erase that frame for me and make a new key frame on my mouth layer.
[45:33] But if I want to copy a mouth shape, for example, this open mouth shape, I can press control C to copy and control V to paste it.
[45:40] So I'm going to speed up this section right here.
[45:42] So basically I'm just scrubbing through listening to what audio is happening at specific frames and drawing the different mouth shapes for those pieces of audio.
[45:51] And I'm going to go through from left to right until I've got all of my lip sync all finished copying and pasting mouths if I need to.
[45:57] One last thing I always like to recommend doing with lip sync is after you've done your first pass of lip sync and that looks pretty good.
[46:06] Have you ever had a dream that you would you could you do you would you want one last finishing touch that I think always looks really nice is to select all of your lip sync and just move it back to frames.
[46:19] One, two, just like that. And if we play it again, have you ever had a dream that you would you could you do you would you want you could do anyways, it looks better.
[46:30] It tends to look better. That's optional. You don't have to do that. But it's something that I like to do personally.
[46:35] Let's animate a blink for our character on the left.
[46:38] So in order to edit this second character, we need to get out of draw mode on our first character.
[46:43] So let's select object mode so we can select a different object.
[46:47] And the object we're going to select is character number two, which is this guy.
[46:50] And then we go back into draw mode to start drawing on this character.
[46:54] So because we have auto key turned on still, all we have to do is take our eraser tool erases eyes and just draw in a half blink just like this.
[47:03] Go down two frames, erases eyes again.
[47:05] That's created another key frame.
[47:07] And then we draw in his closed eyes.
[47:09] Go to more frames, have his eyes just starting to open from here.
[47:13] Copy is halfway open eyes from here by control C to copy that key frame two frames over from our last one.
[47:19] Paste that key frame here and then go to our first key frame on frame number one.
[47:23] Copy that and then paste it two frames forward just like that.
[47:26] And there we have a blink.
[47:29] Easy as that.
[47:30] And if we wanted to copy this blink and have it in multiple spots, we just select all of those key frames control C to copy go to where we'd like to put it and press control V to paste.
[47:40] And that's a really simple way to keep this other character who's not talking alive for the scene.
[47:44] So now our scene looks like this.
[47:45] Have you ever had a dream that you would you could you do you would you want you this is so dumb you you do.
[47:54] So again, to export our animation, we want to go into our output properties, which looks like a little printer right here.
[48:01] And all of these first settings should be kept as default unless you want to change the resolution or the frames per second.
[48:06] The things we want to edit are down here under output.
[48:09] So first of all, we want to select the folder where we want to export it to select that folder by clicking accept.
[48:15] And the file format we want it to be an FF MPEG video and to save it as an MP4 that's going to be under encoding.
[48:22] So for the container to make an MP4 video, we want to select MP4.
[48:27] And then one last setting we want to edit is down here where it says audio codec no audio.
[48:32] We want to make sure to select one of these to save as audio.
[48:35] I'm just going to select MP3 for this one and then leave the rest of the settings as default.
[48:40] And then once that's set up, we don't need to edit this again.
[48:42] And anytime we want to render our animation, we just go up to render and click render animation.
[48:47] And then our final animation looks like this.
[48:50] Have you ever had a dream that you would you could you do you would you want you you could do so you want you ever had a dream that.
[49:01] All right. That's it.
[49:03] Thank you so much for watching my tutorial.
[49:05] If you found this video helpful, be sure to give it a like.
[49:07] It helps out the video and the channel a lot.
[49:09] If you haven't subscribed yet, make sure you subscribe because there's plenty more animation tutorials coming along the way.
[49:15] And lastly, I'd like to thank my Patreon supporters who helped me do what I love to do and share animation with all of you, especially my big booty supporters.
[49:22] Thank you, Jay Alexander, Nate Bennett, Randy Hack, Sean B Simmons, Sherm Cohen, Taylor B, Tiffany Beckley and Angela Zamora.
[49:30] I can't thank you guys enough.
[49:31] It helps me do what I love doing and I'm glad I get to share it with all of you.
[49:35] So thank you so much for the support.
[49:37] I really appreciate it.
[49:39] Anyways, that's it for me.
[49:40] Keep on animating and I'll see you next time.
[49:42] Bye bye.



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
