---
title: Making my lens in Blender (Bokeh, glare, chromatic aberrations)
source: YouTube
url: https://www.youtube.com/watch?v=nru_2wdBqsY
author: Robin Squares
ingested: 2026-09-04
blender_version: "Blender 5.2"
tags: [compositing, camera, rendering, cycles, lighting, materials, shaders, blender-5x, expert]
extraction_status: complete
frames_dir: tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/
frame_count: 14
frame_status: complete
uncertainty_frames: []
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Making my lens in Blender (Bokeh, glare, chromatic aberrations)

**Source:** [YouTube](https://www.youtube.com/watch?v=nru_2wdBqsY)
**Author:** Robin Squares
**Duration:** 50m44s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] I am cloning my camera in Blender, duplicating every effect as accurately as possible, so I can perfectly integrate 3D into my footage.
[0:12] I have already done all of these effects, and now it's the advanced tier.
[0:18] And I am a little bit more shaky now, because, okay, all of the previous effects I've done, I have already done those professionally on footage before.
[0:29] But now we're heading into the territory where I'm kind of figuring things out myself.
[0:35] So, it's the video where there's the biggest chance of me getting something wrong.
[0:41] If I do, I will come back to this video and I will put corrections in the Klingon subtitles.
[0:48] So, turn on subtitles and set it to Klingon, and you will see if there are any corrections made by the time you watch the video.


### Bokeh [0:56]
**Transcript (timestamped):**
[1:00] Before getting into Bokeh, one quick thing to get out of the way first is that real lenses are not perfectly focused ever.
[1:10] So, if you look at this footage, even if you find the spot that is most in focus, it's not perfectly in focus.
[1:19] It never is, and some lenses are worse than others, but it's worth just remembering that in any compositing chain, it's worth adding a little bit of blur.
[1:27] So, figure out how much your lens blurs in perfect focus and just add that blur to every render.
[1:33] Okay, Bokeh is the name for these circles that appear when you defocus a light, and it is by far the most difficult effect we're making today.
[1:44] And I'm going to show you three different methods to make them, and that's because none of the three methods are really perfect in every way.
[1:53] So, they each have some positives and some drawbacks you kind of got to figure out which one to use for which situation.
[2:01] This method is the simplest.
[2:03] Import two images into Blender, a shot with Bokeh, and that same shot in sharp focus.
[2:11] And then point a camera at the sharp version, and blur the camera with depth of field.
[2:19] Then just change the blade count and rotation to match the Bokeh.
[2:24] For most shots, this is going to be the best technique to use, because it's kind of the way cycles is meant to render Bokeh,
[2:34] but it's also the technique that looks the least real, it looks very digital, and it doesn't have the imperfections, it doesn't have cat's eyes, which we'll go over in a bit.
[2:43] So, for most projects, this is probably enough, but if you need it to look more accurate to the real Bokeh, one of the next two techniques is going to be the one you want.
[2:57] Method two builds on method one.
[3:00] So you still keep that same camera, but you just remove the blades from the depth of fields, and then you add an image plane in front of that camera.
[3:09] That image is a photo that you took of a Bokeh ball.
[3:13] So I just took a picture of a flashlight out of focus, so you just add that, and then in the shader, you want white to be completely transparent,
[3:25] and you want black to be completely opaque, you can just copy this shader setup that I use, and then you want to extrude out the edges of that image plane, just so it covers a larger area.
[3:37] And then you place that basically whole in front of your digital camera.
[3:43] I think it's worth measuring the distance between your camera lens and shutter and matching that distance for the plane to camera in Blender.
[3:50] I'm not sure though, and I also think it's correct to scale that whole just about enough to not cover any of the field of view, just so it's outside the camera's range.
[4:04] This will do two things.
[4:06] One, it will change the color and texture of all the Bokeh in your render to match the Bokeh of your camera.
[4:15] Two, it will make cat's eyes.
[4:19] So Bokeh that's close to the edge of the frame will kind of crop into these cat's eyes shapes, and that is accurate to how my lens and many lenses do produce Bokeh.
[4:32] This looks better than method one, but there are some drawbacks.
[4:36] And first and foremost, one drawback is you're putting something physically in front of your camera, which one, it'll make everything render a little bit slower.
[4:47] And two, it can come in the way of other workflows later on.
[4:52] For example, it will mess with the render passes unless you're cleverly set it up not to.
[4:58] So a way to work around that is to instead of using a texture as the circle, just model a circle.
[5:07] So an actual circular hole in a plane, and that will have the drawback of it won't contain the color and texture, but it'll still produce that cat's eye Bokeh.
[5:17] And that will combine with blades in depth of field.
[5:21] So that's another variation that you can make on this.
[5:24] Now, a quick aside, I do have a way of combining the benefits of both method one and method two, but it's very technical and a bit hacky.
[5:34] So I put that in the document that's linked below that contains all the assets as well.
[5:42] So the third method is done completely in the compositor.
[5:45] You render a completely sharp image, and then you run it through a Bokeh blur node in the compositor.
[5:52] And that takes a Bokeh image input.
[5:55] That's the image of the flashlight out of focus.
[5:58] You just put that in and that's going to blur the image with the Bokeh.
[6:02] And the Bokeh effect looks great.
[6:04] It has the exact color and texture of my real Bokeh, but it doesn't create the cat's eyes.
[6:12] So we have a workaround for that.
[6:14] What I did was I photographed that same flashlight in different areas of the screen.
[6:20] I moved it around so I could take a picture of it in the upper left quadrant and the upper right quadrant.
[6:25] I just took nine pictures in total and then I imported all of those nine pictures into Blender.
[6:32] And I used them each for different Bokeh blur nodes.
[6:35] And then I just mixed those results based on screen space.
[6:40] So one of them just shows up in the top left, one of them just shows up in the top right and so on.
[6:46] So that means that I get the correct Bokeh captured from my camera in different areas of the screen.
[6:54] This looks really good.
[6:57] And in my opinion, this is the best workflow for still images.
[7:01] But it kind of breaks with animation, at least if the camera moves.
[7:06] Because if the camera moves, then you can see how the lights change shape as they move from the center of the screen to the edge.
[7:15] And it's just not how it moves in real life.
[7:20] So these shapes don't behave correctly when moving.
[7:24] Okay, but this is all just for a flat image.
[7:26] All the Bokeh balls are the same size, which is not the case for a 3D scene.
[7:31] So for a 3D scene, we need to add an element to this.
[7:35] And that is, we need to render out a Z-depth pass.
[7:39] Z-depth, just each pixel corresponds to how far away that pixel is from the camera.
[7:45] So something that's one meter away will have a value of one, which is why it looks completely white until we map range it.
[7:52] And there is a way to convert that to Bokeh size.
[7:57] And you can do that using this math setup that I'm showing on screen right now.
[8:02] It basically pulls everything down to the point that you want in focus and then maps that to the size of the Bokeh is supposed to be.
[8:11] And if you run that through a Bokeh blur node, then things that are far out of focus will blur more and things that are in focus will blur less.
[8:21] So to summarize, method one, pure blender camera is best for most shots because it's super easy and it's the way cycles is meant to render.
[8:30] So if you're not super technical, it's going to be the easiest way to implement.
[8:34] Number two is putting a plane in front of the camera and that adds possibly texture and at least cat's eyes effects.
[8:41] And version three is the full compositor way where you use a Bokeh blur node, which honestly in my mind looks the best for a still image,
[8:50] but it can break with 3D scenes that are complex and the cat's eyes don't move quite correctly.


### Glare [8:56]
**Transcript (timestamped):**
[9:01] Claire can refer to many different phenomena actually, but I'm referring to these streaks that come out of bright lights.
[9:10] And to replicate those, we first have to capture the streaks and there are two ways of doing that.
[9:18] First is to take a picture of a very small, very bright light.
[9:24] Second is to simulate it all in the computer.
[9:28] I prefer the second method because to get the right picture of a glare, you need a very, very small, very bright light and everything else to be completely black.
[9:41] So for me, simulating it from scratch gives a cleaner result.
[9:45] If you take a picture, remember to do it at the correct aperture.
[9:50] As you can see with my lens, as I change the aperture, that changes the physical size of the opening inside of the lens.
[9:57] Three things happen as I change it. One, it gets smaller and bigger, but also the polygon rotates around the frame,
[10:05] meaning that if I change that as I'm making a Bokeh, for example, you can see that that Bokeh rotates.
[10:12] And also, when I go completely open, the blades disappear entirely.
[10:18] So when you're capturing both for Bokeh and for glare, it's really important to capture it at the correct aperture
[10:26] and that is the same aperture that you filmed your shot at.
[10:29] Now, as I said, I want to simulate mine because capturing it in camera, I just found it really difficult.
[10:35] So to simulate it, you want to download a free software from GitHub called Real Bloom.
[10:41] In here, you put a picture of your camera's aperture and that corresponds to the shape of a Bokeh blur.
[10:48] So you just take the same picture that you used for a Bokeh ball and you put that in here.
[10:54] Then turn on normalization and compute diffraction.
[10:59] And then if you have a polygonal aperture, that will create streaks.
[11:04] If your aperture is completely round, it will not make streaks. It will make something else.
[11:09] Then press move to and click OK to move that image to the dispersion input.
[11:16] And then in the dispersion tab, you set the method to GPU, turn everything up to max and press apply dispersion.
[11:26] Now, color.
[11:28] This is your perfect glare kernel. So save that.
[11:34] That image, by the way, is saved in Linear Rec 2020 by default.
[11:38] In Blender, add a glare node and set the mode to kernel.
[11:43] Drag that kernel image into Blender, set the color space to Linear Rec 2020 and plug it into the kernel input.
[11:52] Now the image glows with your custom glare, which I think is so cool.
[11:58] And you can adjust the threshold and the smoothness.
[12:01] So if you set the smoothness to zero, then it's just going to pick a threshold to apply the glare to.
[12:07] But if you increase the smoothness, then it's going to kind of fade out as the image gets darker.
[12:12] I don't know if there's a real science of what values to pick here.
[12:15] I just pick what kind of looks like it matches my camera.
[12:18] And if like me, you see the glare kind of cutting out towards the edge, you can kind of fade it with a gradient as well as just multiply it with a gradient.
[12:25] Now in the compositing chain, glare is a little bit weird because it should be applied on the composited image where the 3D is on the plate.
[12:36] But it should be based only on the 3D because the plate already contains glare, so you don't want it to emit more glare, right?
[12:45] So that means that into the glare node, you have to put only the render, but then you have to apply it after the render is composited.
[12:54] Now let's say that your 3D light is behind your footage, like in this shot.
[12:58] What do you do?
[13:00] Then you have to start working with like stenciling out the footage and working with different glare nodes to get it all to combine correctly.
[13:08] And I'll show you a practical example of that at the very end of the series.
[13:13] I'll show how to put a whole shot together like this.
[13:16] But I think that when it gets complicated like this, the best way to learn is to work through a whole project together, which is exactly what my green screen course is for.
[13:28] You get this footage and together we transform it into this.
[13:34] That means tracking, gray card calibration, lighting, rendering, compositing, grading, bunch of stuff and more advanced things like stabilization and in-painting.
[13:49] You see, when you shoot footage with tracking markers like these, then you need a way to paint them out and blender is the perfect tool for that, which I think many people don't realize.
[14:03] The project is part of a larger VFX course on inlightvfx.com and I'll just play you the trailer and you decide if you want it or not.
[14:11] But if you do, then please grab it through my link in the description because that's an affiliate link.
[14:17] So if you use that and I get some of the money, which helps me stay afloat.
[14:22] Quick interjection. Apparently the course is going on sale very soon, I found out.
[14:29] So don't buy it yet, wait until Monday, September 7th, because then the course is going on sale for 20% off for the first 100 people to buy it.
[14:43] After the sale, the price of the course is going up.
[14:49] That's because the current price was set a long time ago when the course was a lot smaller as things are being added, it's becoming more valuable.
[14:59] So therefore the price is going up to reflect that additional value.
[15:03] So buy the course on Monday, September 7th, be among the first 100 people to buy it and you'll get it for 20% off.
[15:13] So right now go to the description, click the link and then you can sign up to get notified just as the sale starts.
[15:43] One VFX shot.
[15:47] It's about making anything you can think of.
[15:53] So this equipment will help us recreate our scene perfectly in 3D.
[15:57] Check out the control this gives us in compositing.
[16:02] Because this is set up right, we can just drag anything in and it works.
[16:07] You're going to develop the fundamentals to get consistent results.
[16:13] So come on, let's make the work you've always dreamed of.


### Lens breathing [16:22]
**Transcript (timestamped):**
[16:27] When you move the focus, the lens might zoom out a little.
[16:32] That is called lens breathing and it appears very clearly in shots with a rack focus.
[16:39] So let's figure out how to replicate it.
[16:41] I pointed my camera at a grid on my PC.
[16:44] Then I focused from the nearest possible to the furthest possible.
[16:49] And at different spots, I called out what focus distance I was at.
[16:53] 0.18, 0.17.
[16:57] Then I imported that video into Blender as a movie clip.
[17:02] In the movie clip editor, I set the distortion model values and ran it through an undistort node.
[17:10] Then I exported a frame every time I called out the distance.
[17:15] And we are at 1.
[17:21] Going down 0.5, 0.4.
[17:26] And that left me with a series of still images, each labeled with the focus distance.
[17:33] And then I made a similar set up in Blender as I had in real life.
[17:37] So a camera with the correct focal length and sensor size pointed at a grid.
[17:42] And I imported the image sequence as a camera background.
[17:46] And then I animated the camera focus to match each image.
[17:51] So if the image was taken at a focus distance of 0.2, I put 0.2 in the Blender camera.
[17:58] Now, this doesn't even change anything visually because depth of field isn't even on.
[18:04] But the reason we did it is so that we can use this slider as a driver for the focal length.
[18:11] So we copy the focus as a driver and paste it on the focal length.
[18:17] Now the two sliders are connected.
[18:20] So when the focus is at 0.2, the focal length is also at 0.2.
[18:26] But let's change that.
[18:29] Okay, open up the driver panel.
[18:31] We'll be adjusting this graph, which controls how one value translates to the other.
[18:36] So if we have a point at x.2 and move it up and down,
[18:41] now we're controlling what the focal length should be at 0.2 focus.
[18:47] And we can add multiple points.
[18:49] For now, let's keep the points in linear interpolation.
[18:54] So we start at infinity focus distance.
[18:57] So in the key frame, I type some high number, something higher than any focus distance on my lens.
[19:03] And then I type 17.5 for the value, which is the focal length that is stated on my lens.
[19:10] Then I duplicate that key frame.
[19:12] I move it over to 1, which is next on my timeline, you see that?
[19:16] And then I just move it up and down that key frame until I see that the checkerboard is sticking as I page back and forth between the key frames.
[19:26] I just wanted to stick, so the focal length will be some higher number than 17.5.
[19:31] And then I just keep doing that.
[19:33] So I duplicate the key frame again.
[19:35] I move it over to the next value that's on my timeline.
[19:39] And then I go to that key frame, page back and forth until the checkerboard is sticking.
[19:45] And this is fairly easy for my lens because it's a prime lens.
[19:50] It doesn't zoom, which means my function is a simple function.
[19:55] If you have a zoom lens, it might be a little bit more complicated.
[19:59] So I just, it's a bit finicky, you know, just go through, make sure that the checkerboard sticks for every single key frame.
[20:07] When I'm done, I usually go back over again because usually I'd slipped throughout the entire timeline a little bit, so I just readjust everything.
[20:16] And then I take the final key frame and just add one at zero, which doesn't exist on my lens,
[20:22] but I don't want the system to break, right, if someone focuses at zero.
[20:26] So I just smooth out the ending.
[20:30] So I want to set that to aligned, scale it to zero on the Y, and just smooth it out to some number that looks like it's smooth.
[20:40] And at the other end, I do the same thing.
[20:42] So the final key frame, the one at like infinity focus, and just set that to aligned as well.
[20:49] I scale it down, and then I move it over until it looks smooth.
[20:54] And then if you're a bit of a perfectionist, you can go in and you can start adjusting all the different key frames as well.
[21:01] Set them to aligned Bezia as well, and just rotate them until the curve is nice and smooth.
[21:07] I like to do that. I don't know how big of a difference it makes. I suspect not much.
[21:11] But then I have the camera set up. So I can go down and I can delete the key frames now.
[21:17] Those were just for calibration.
[21:19] Now the camera has lens breathing, meaning that as I change the focus distance, it also zooms out a little bit,
[21:28] which goes such a long way for realism.
[21:32] Let me show you two different clips.
[21:35] One without lens breathing, and one with, and you can see how much of a difference it makes.


### Chromatic aberrations [22:04]
**Transcript (timestamped):**
[22:06] You know chromatic aberrations is that color fringing that is at the edge of every single blender render made since 2005.
[22:19] Now people make that using a lens distortion node with dispersion dragged up,
[22:25] but from my testing, that is nowhere near close to what my actual camera lens produces.
[22:33] I don't know, maybe my camera lens is weird, but maybe yours is too,
[22:37] so let's figure out how to copy the exact chromatic aberration that is on our lens.
[22:42] Now when I was doing research for this video, I went outside and I filmed the sky through a canopy in the forest,
[22:47] and it had a really strong color fringing around the leaves.
[22:52] What I noticed was that as I shifted the focus of my camera, the color fringing changed as well.
[23:00] I figured out that at least in my lens, the color fringing or chromatic aberrations changes based on whether the thing out of focus is out of focus near to the focus plane,
[23:14] or far from the focus plane, and in focus the fringing disappeared entirely.
[23:19] So the color actually changes quite a lot based on that.
[23:22] I don't know if that's just this lens, but I thought that was fascinating, so let's copy that behavior.
[23:27] Okay, so I shot reference.
[23:29] I used a black and white grid on my monitor, and I shot it in a dark room to get as clear fringing as I could.
[23:37] And then I just racked focus from near to far to see how the color changes.
[23:43] Now we will do our own chromatic aberrations in the compositor.
[23:46] So let's render out a checkerboard that's similar to the one we shot, and just open those side by side.
[23:53] You have the reference, and then you have what you're working on at the very side.
[23:57] So then you know that everything you do will match the original footage.
[24:01] Now to make sure that I'm actually properly matching, I also add a blur node at the start just to blur the image to match kind of slightly the reference at each frame.
[24:13] And then at the very end, I add all of the other steps that I've gone through in this video,
[24:19] so that I know that when everything is turned on, then it'll match.
[24:24] Now the core concept here is to split up the red, green and blue channels, and then change them separately, and then recombine them.
[24:32] And the way they change in there is they can move, they can scale, they can blur, they can rotate, all different kinds of things.
[24:39] Now it gets a little bit complicated because remember, we want to be able to change this based on depth because of the focus distance difference, right?
[24:47] And not all of the effects in the compositor let you do that.
[24:51] So we need to be clever about what nodes we use in there, and only use nodes that can vary between pixels.
[24:58] So then between the split and the combine of RGB, I just make all the changes necessary to match all of the effects that I see in the reference.
[25:07] But as I said, this only works for one focus distance.
[25:11] I want it to change with the focus change.
[25:14] So I'll make something similar to what I did for lens breathing.
[25:18] I set up a value node and I animated going from negative one to positive one.
[25:23] And that represents how far out of focus is it in each direction.
[25:28] So zero is perfectly in focus, negative one is perfectly out of focus in one direction, and positive one is perfectly out of focus in the other direction.
[25:37] And I take that value and I run it through a vector curves node.
[25:43] A vector curves node will remap that to three separate values.
[25:48] And those can be plugged into any of those nodes that transform pixels.
[25:54] And that curves node goes into, say, the blur for the red channel.
[25:58] And now you have full control over how much to blur in each direction at every value that is input.
[26:07] So on the left hand side of the curve, that is what you're outputting at a value of negative one.
[26:13] And you can output, say, an x value of 10 and a y value of 20, for example.
[26:19] Then when the input is zero, that's the middle of the curve, let's set everything to zero
[26:25] because we don't want any movement when it's in sharp focus.
[26:29] Then at the other end, that is how much to blur in each direction when the input is at one.
[26:36] And that is perfectly out of focus in the other direction.
[26:40] There are a bunch of things to keep in mind at the same time here, but I think once you set it up yourself and play around with it,
[26:46] it's going to be easier to understand.
[26:48] Basically, you're just, how much out of focus is it in each direction?
[26:52] And what do you want to do with that?
[26:54] That is what you do.
[26:55] So you just use a vector curves like this for every single transform in every single channel.
[27:05] Now, once all of this is done, then you can group all of the nodes and expose that input slider,
[27:12] the one that we previously animated, just expose that in the group.
[27:16] And then that, remember, corresponds to how out of focus is something.
[27:20] So we can here reuse the setup that we used for bouquet if you made that.
[27:26] So you can also use a version of that same math setup right here, except you don't want it to be an absolute value,
[27:33] because if it was in the blur, you wanted to map between negative one and positive one.
[27:39] So if you plug a Z depth into there, you set the focus distance and you plug that into your chromatic aberrations group,
[27:45] everything should play nicely together.


### Combine everything [27:57]
**Transcript (timestamped):**
[27:57] Okay, we've got every effect now, but separately.
[28:01] So I've done them all together, so I've made a graphic for you showing the order of operations.
[28:07] Order of operations is super important when it comes to this stuff, because just as an example,
[28:13] with a lens, the light comes into the lens, then it's warped around,
[28:20] and then on the other side, it hits the camera sensor.
[28:23] Now, I can't show you the camera sensor right now, because I'm using the camera to film over there.
[28:28] The order of that matters because let's say you add sensor noise before lens distortion,
[28:35] then you're gonna distort that noise, which by itself it's probably not gonna be super
[28:41] noticeable, but in aggregate, all of these tiny little effects are what makes the effect
[28:49] work.
[28:50] Like, none of what we've done today is super noticeable, but it's the combination of just
[28:54] caring about all the details that really matters.
[28:58] So follow the order of operations and bear in mind that I haven't quite figured out
[29:02] the bouquet and chromatic aberrations order yet, but I think what I show here is probably
[29:10] good enough for most things.
[29:12] So time to show you how to put everything together in one blend file.
[29:16] Okay, so we start of course by importing our movie clip, so let's go to the movie clip
[29:21] editor, press open and just go to where I have my EXR sequence stored.
[29:27] It doesn't have to be an EXR sequence, but mine is because I denoised it in Resolve earlier
[29:34] and then it's a good idea to export as EXR, because you keep all the data that you need.
[29:39] So first off, let's press T, set scene frames, which sets the frame range down here, and
[29:45] then you can prefetch the whole thing to load it into memory, but I don't think I have
[29:49] to waste memory doing that.
[29:50] Not while I'm recording at least.
[29:52] Let's press N and set the input color space to input Panasonic V-Log V-Gamut, which is
[29:59] one I filmed in, and then go down to track and set my camera info.
[30:04] So my sensor was MFT, that's 17.3, and then the focal length is 17.5, that's what I filmed
[30:13] in.
[30:14] And then the lens distortion model, I have that stored in a document, which is right
[30:20] here, so I'll copy over the first value, paste here, second value, I think you can
[30:28] paste without clicking, right?
[30:29] Yeah.
[30:30] And then third value, copy and then Ctrl V to paste it.
[30:35] So nothing changes yet, but we'll use that later on.
[30:38] And then let's just add that to the compositor with a Shift A, Movie, not Mui V, Movie clip,
[30:46] and in the dropdown of that we can pick the only movie clip we have, Ctrl Shift Left Click
[30:51] to preview it, there it is.
[30:54] And I have already made a little basic setup here just to composite this over the beauty
[31:01] render, which is this.
[31:04] So if I put this into the footage processing, what it does is it first of all, it positions
[31:10] it in 3D space to fit a bit better, then it cuts out part of me so that it can be composited
[31:17] over the 3D right here.
[31:19] I didn't do a great job cutting me out because well, I did the keying inside of Blender, so
[31:23] don't be too harsh on me.
[31:25] And then it's just a matter of alpha overing a couple times and then multiplying the shadow
[31:29] capture over, so the shadow capture is what's doing this.
[31:33] So the shadow capture is this render output right here and then that just multiplies over
[31:39] the footage and that integrates it a lot better.
[31:43] And then let's just take a look at our cheat sheet.
[31:45] So it says step one, Camera Color Space to Work in Color Space, and we have already done
[31:51] that.
[31:52] We set that up in here, remember?
[31:53] So the next step is Black Level Subtraction.
[31:57] And we do that using a Mix Color node, just add that right in here and set it to Subtract.
[32:04] And we subtract a value that I also have stored, which is 0 on both red and blue, but a little
[32:10] bit on green.
[32:11] And make sure that you're in the right view model here, so it's the linear value of green.
[32:17] That just brings all of my footage down to actual pure black.
[32:21] So previously it was like this, and now it's like this.
[32:24] I don't know if you can really tell the difference through YouTube, but I can see that it's now
[32:28] much closer to pure black.
[32:30] And then on the cheat sheet, we just follow that line down from Black Level Subtract and
[32:34] we see that on the other end, but on the same level, we have a Black Level Add.
[32:40] So in the graph, we do that right here.
[32:43] Just duplicate it over here, bringing the output into it and setting it to Add instead
[32:50] of Subtract.
[32:51] So now we've like completed a tier of compositing.
[32:53] I'll just add a frame around that with F and type in Black Level.
[32:58] And if I zoom into like a dark area here, you can possibly tell that if I mute all of
[33:03] that previously it was black and now it's like kind of dark green, whatever.
[33:07] And the next step is Undistort.
[33:08] So let's bring all of this down and over a bit and add a Movie Distortion node right
[33:15] here.
[33:16] And since I input my distortion values right here, I can just pick that footage from the
[33:21] drop down and the effect is that it undistorts.
[33:25] So check this out.
[33:26] Mute, Unmute.
[33:27] So it undistorts the footage.
[33:29] And then again, on the opposite side, we have to Redistort on that.
[33:33] So we just follow the line on the cheat sheet and see that it says Redistort and that happens
[33:38] right here.
[33:39] So let's set it to Distort and that means that when we view that, that distorts the
[33:45] final composite.
[33:46] So you see it tucks in the corners a little bit.
[33:48] But we don't want it to do that because currently we're still not on the right resolution.
[33:53] You can see this is not what I want my final resolution to be.
[33:57] So I need to force it to be a correct resolution.
[34:00] And I just do that with a Mix Color node.
[34:03] I put it into the second input of the Mix Color.
[34:06] Into the first input I just put the original footage right here.
[34:10] Because that sets the resolution to be the original footage.
[34:14] And then just complete the chain, like so.
[34:18] And that completes the tier called Distortion.
[34:23] This is why I like working in these layers so that you can clearly see that at the same
[34:27] stage where we remove an effect, we add it back later.
[34:31] The next step is the Vignette.
[34:33] Let's bring all of this over just a tad.
[34:36] I'll bring in my Vignette image, which looks like this.
[34:41] Let me show it's Linear Rec 2020.
[34:44] And I include that with a Mix Color node set to Divide.
[34:51] Which is right here.
[34:55] Add that there and preview it.
[34:57] And currently we're seeing that it's very bright along the edges.
[35:01] Now it shouldn't be, which is the first sign that I think I shot this with a different
[35:06] lens than what I'm trying to emulate right now.
[35:09] So let's just pretend I shot this with the correct lens.
[35:14] And I'll just adjust this.
[35:15] Just bring it down.
[35:17] Because the lens I used clearly didn't have as strong of a Vignette.
[35:22] But it's around like 0.25.
[35:24] So here I can see that it actually does remove the Vignette.
[35:28] And then at the end we multiply in the Vignette.
[35:32] So plonk it in there.
[35:35] Set it to Multiply.
[35:36] Bring along the Vignette.
[35:38] And this time I'll just set it to Full Strength just to emulate the actual lens that I really
[35:42] want to use.
[35:43] That adds a pretty strong Vignette around the whole thing.
[35:47] Next up is Lens Breathing that is done in Render.
[35:50] And I didn't have a focus pull here, so that's irrelevant for this shot.
[35:54] And then it's Bokeh Blur or Depth of Field.
[35:57] Now I didn't render with Depth of Field.
[35:59] This is completely sharp, this render.
[36:01] So I'll have to add a Depth of Field to it.
[36:04] But that is done only to the render.
[36:06] So let's bring the render out here.
[36:08] And let's add it.
[36:09] First, let's add the overall blurriness.
[36:15] As you can see, even the part of the footage that is most sharp is still pretty blurry.
[36:21] I know that I'm supposed to be in focus here.
[36:24] I set the focus distance pretty close to me.
[36:26] I don't think anything else is particularly more in focus.
[36:29] So I need to first just max the overall blurriness with just a blur node.
[36:33] So blur.
[36:35] And I'll add that actually to the shadow first, so I can compare this shadow part to
[36:39] this part and just see.
[36:41] Is it 2 pixels?
[36:43] Is it 3?
[36:45] I think maybe 3?
[36:47] What about 4?
[36:49] I think 3 is pretty much accurate.
[36:53] And then let's just add that to both of the outputs of both the shadow pass and the beauty
[36:59] pass.
[37:00] And then we can add the depth of field.
[37:02] And I do that with either a Bokeh blur node, or I can use the segment Bokeh node group
[37:10] that I made.
[37:11] So this is where I just added a bunch of different blurs from this node here, which you can download
[37:17] in the description, which has all the different angles of Bokeh that you can plug into different
[37:23] Bokeh blur nodes on different segments of the screen.
[37:26] So that just does that.
[37:29] And I'll just do it to the beauty render, but it needs a defocus value, because I don't
[37:34] want to defocus everything the same.
[37:38] That just looks dumb.
[37:39] So I have this Z depth output, which just gives me a depth.
[37:43] I have a Z depth to blur node.
[37:46] So I've input the Z depth into here, and then preview that, and set the max blur to 1 and
[37:53] the minimum blur to 0.
[37:55] You can see I can span the focus distance here, and I know that my focus was roughly
[38:00] on me, which is, I think, probably like there-ish.
[38:06] Let me just plug that into the defocus of the segment Bokeh.
[38:10] We can say that the maximum blur size, I don't think I'm going to need anything more than
[38:14] 30, and this is just fail safe.
[38:17] And then the blur size, let's zoom in here.
[38:22] And compare to the final composite.
[38:24] I think it has to be more blurry than this.
[38:29] So more than 0.1, maybe 0.5.
[38:31] Oh, I didn't connect it correctly.
[38:33] Okay, connected to the chain first before testing.
[38:36] There we go, okay.
[38:37] But still more than 0.1, maybe 0.3.
[38:41] That's pretty blurry.
[38:43] Maybe too much.
[38:47] Maybe go down to 0.2.
[38:50] That looks a bit better, I think.
[38:53] I think that's right.
[38:54] Let's bring this over here and group it all into a frame called Blur.
[38:59] And then according to Archiejeet, there is chromatic aberrations still on the same level.
[39:04] So I'll add a chromatic aberration, not the one that comes with grades, my color grading
[39:10] toolkit, but this one, chromatic aberrations, which is for camera emulation.
[39:16] Now this as well, you can defocus in one direction and get these purple halos, and then in the
[39:22] other direction we get these orange yellow ones.
[39:25] And that is also based on Z-depth.
[39:27] But it does use another node.
[39:28] It uses the ton sigmoid node, which you can also download.
[39:33] The math isn't complicated.
[39:35] By the way, the Z-depth to blur also, it's not complicated.
[39:38] But it just remaps the Z-depth into a proper range for defocusing here.
[39:45] And then we need to add a subtraction.
[39:47] So math, put it in here and just subtract the same focus distance as I used here.
[39:54] So I want the same thing to be in focus.
[39:56] So I'll actually add a value node and just copy that distance onto there and use it as
[40:02] the input for both of these nodes.
[40:09] Now you can see the chromatic aberrations are different on this side of the focus plane
[40:13] than from that side of the focus plane.
[40:15] Let's just decrease it so that it's not insane like it is now.
[40:20] Is this still a bit too much?
[40:22] It is, isn't it?
[40:23] So 0.1 to 0.04 maybe?
[40:28] 0.03?
[40:29] That's more correct.
[40:32] And again, I don't think I can actually use this as reference.
[40:35] No, I can't because I did use a different lens which doesn't have nearly the same amount
[40:41] of chromatic aberrations.
[40:42] So ignore this.
[40:44] Ignore this.
[40:45] Something accurate to my lens would be something like this.
[40:48] So now we have this complex chromatic aberrations where it's purple here, but then it's orange
[40:53] here.
[40:54] Oh, I love it.
[40:55] Then next up is the compositing which I already have done right here.
[40:57] It's typically done with just a couple alpha over nodes or even one alpha over node and
[41:02] maybe a multiply for the shadow pass.
[41:06] And then we go down.
[41:07] So we multiply the vignette, that's what it says, and then we distort, that's what
[41:11] it says too.
[41:12] But then there's one more thing and that is the glare.
[41:14] So let's make some space for glare here.
[41:17] Now glare honestly, it can get a bit complex, but let's just start.
[41:21] So let's add a glare node, set it to use a kernel, set the quality to high, and set
[41:29] the kernel type to color.
[41:31] Then I'll bring in the glare kernel that I made from real bloom.
[41:35] Control shift left click shows that and we can just temporarily increase the viewport
[41:40] exposure to see that properly and set the input to linear rec 2020.
[41:46] And here you can see it is actually clipping at the edge of the frame, which can show in
[41:50] some cases using the glare.
[41:52] So I like to clamp that down and I do that with an image coordinates node, bring out
[41:58] the uniform and set it through a length node and then just bring down the exposure again.
[42:06] So I can view what that did.
[42:07] That just adds the circle.
[42:09] Invert that using an invert color node.
[42:14] And there we go.
[42:14] And now we can just mix color that just multiply it over the glare kernel.
[42:23] So now it's fading out properly towards the edge.
[42:25] So you never see that clipping.
[42:28] And let's use that as the input of the kernel and group at all calling it kernel.
[42:35] And see what happens if I just add that to the entire comp.
[42:39] You know, honestly, not too bad.
[42:41] And for something like this, I think it's actually kind of ideal because you can see
[42:46] that my shirt is glaring and the sky is glaring and everything's just cohering properly.
[42:51] But technically speaking, there is already glare in here and there might be a little bit
[42:56] less than what we'd expect because I filmed this for the wrong lens, which is a better lens.
[43:01] But let's let's just do this properly.
[43:03] Right.
[43:04] So the render should be glaring onto the footage.
[43:08] So let's just do that first.
[43:10] So we'll bring in only the render and then bring that into the kernel.
[43:15] And the output of that should be only the render glaring and it is.
[43:19] Let's just adjust that while we're here.
[43:21] So I kind of want to increase the smoothness to bring along some of that highlight down here.
[43:26] And then maybe just because this is so strong, let's maybe bring down the threshold as well.
[43:32] Maybe point five and then bring down the smoothness.
[43:37] Just to get some glare both up here and down there and then just decrease the strength
[43:42] because it's way too strong.
[43:46] And then once we're happy with it, we can just mix that, mix color that over the entire comp.
[43:53] Just output the glare and add it over everything.
[43:56] And what we can see here is we can see this ghosting.
[44:02] And that is because the input that we use for the glare is not distorted like everything else is.
[44:07] So we actually have to duplicate the distortion node and put it here to distort everything
[44:12] that comes down in here.
[44:14] And that looks really, really good.
[44:16] I like this.
[44:17] I like this glaring right here.
[44:19] I might actually want to decrease the exposure of the entire comp.
[44:23] Just a tad.
[44:25] So okay, so now I have glare coming from the render casting over the footage,
[44:28] but I needed to go the other way around too.
[44:30] So glaring from me going over to the CG.
[44:37] But I don't want to glare that over itself as well because it's already doing that.
[44:41] Like some glare here is probably glowing over to this area.
[44:46] So I need to do something clever here.
[44:48] So now we can make a version of all the footage that can glare.
[44:51] So what will I need?
[44:52] I'll definitely need the footage, but I'll only need the part that isn't obstructed by the CG
[44:58] because if all of this glows, well, that isn't...
[45:00] We don't want these cars to glow because they don't even show, right?
[45:04] So let's figure out how to get that out.
[45:07] So we'll need definitely the alpha channel of the CG, I think.
[45:12] So let's go for a separate color.
[45:16] I keep saying separate and get the alpha channel from that.
[45:20] That gives me the whole, but if I apply that to the footage, I can actually do that.
[45:24] Now, so just a set alpha node and use the footage as input and the alpha from here.
[45:31] For one, I think it's inverted.
[45:33] Yes, it is.
[45:34] So let's invert that with a...
[45:36] Oh, let's just go for an invert color.
[45:38] That's the easiest way.
[45:39] But it does cut out my head because that is a separate layer, right?
[45:44] So that's from the foreground layer.
[45:46] So I'll also need the separate color node again from the foreground to get that alpha channel.
[45:53] And then I can just add those together.
[45:55] So add, let's just go for a math add node.
[46:00] Add those together.
[46:02] That gives me a complete alpha.
[46:04] Oh, but those are overlapping weirdly.
[46:06] So let's actually set them to maximum instead to keep only the brightest parts of each and then plug
[46:13] that into the alpha to get a version of the footage that shows.
[46:18] And then I think probably we should use this version of the footage, shouldn't we?
[46:21] The one with a shadow applied because that's the new version of the footage.
[46:25] So this is plate cut out.
[46:29] So now we can use this as a glare source.
[46:32] So let's actually let's duplicate the glare.
[46:35] I'll need some more space down here.
[46:38] So GY moves that down and make a new glare node.
[46:43] Which doesn't use this image, but uses this.
[46:48] So now I have a version of the footage that glares as well.
[46:52] And I can adjust the power and stuff, but let's let's just keep it on the same for now and then mix that over.
[46:59] But of course, I don't want to add it to everything because I don't want to add glare from the shirt to the shirt
[47:06] because it's already glaring onto itself in the plate.
[47:10] All right, so I need to only apply outside of the footage.
[47:14] And that is basically the opposite of this mask.
[47:18] It's just this mask inverted.
[47:20] So I envy invert color and bring that down and plug that into a factor.
[47:31] So that it only glares outside and that should make my shirt glow onto the CG behind it.
[47:42] How good is that?
[47:43] I really should have worked a bit better on the cut out, shouldn't I?
[47:46] In any case, all of this here is now the finished glare setup.
[47:51] So F, glare.
[47:53] And then from our cheat sheet, we can see that the next step is re-noising.
[47:58] And I did de-noise the footage in resolve beforehand.
[48:02] So the footage is de-noised right here.
[48:05] So all I need to do is to add a sensor noise node, which is the one that I made in a previous video.
[48:11] Just different lighting levels.
[48:13] Just plonk that right in here.
[48:15] Sensor noise.
[48:16] Is it weird to put one node in a frame?
[48:18] Do you guys do that?
[48:20] Anyway, I think that should, if I preview that.
[48:24] That does add noise to everything.
[48:26] So more noise here than here.
[48:28] That seems correct.
[48:29] If I mute that, that's before and then after.
[48:36] That does look pretty accurate to my camera, doesn't it?
[48:39] It does.
[48:43] Now, did I add still images or sequences to this?
[48:47] They are sequences, so they do animate, don't they?
[48:49] If I go one frame forward, let's see if that noise animates.
[48:53] It does.
[48:54] Okay, that's great.
[48:57] And then at the end of the cheat sheet, we see we got to go from working color space to display.
[49:01] And that is, in fact, what we're doing already down here.
[49:05] So this is where we pick the way we want to go to display.
[49:09] So we can go for a filmic, for example.
[49:11] Maybe a higher contrast, maybe even darker.
[49:13] Oh, that's not Chronos.
[49:15] That does not work.
[49:16] A GX?
[49:18] Filmic.
[49:18] I do think the ASUS tone mapping actually looked really good for this scene.
[49:23] It's kind of desaturated.
[49:24] But this is really an artistic choice.
[49:28] Anyway, so this is just a naive composite.
[49:31] And then with all the camera emulation, I think the camera emulation looks really good.
[49:36] If you skipped over any of the previous videos, go back and watch those to see
[49:39] how to make each of these nodes.
[49:41] And then good luck making your own camera.
[49:45] So that is the final flow.
[49:47] And if you notice that it's fake, it's probably not because of the camera emulation, I would say.
[49:52] It's probably because of my sloppy 3D work and masking.
[49:56] Other than that, I think the camera emulation holds up pretty well.
[50:00] And that's because of a combination of techniques that I showed in this video
[50:04] and some techniques that I show in the green screen course.
[50:08] For example, you'll notice that from the original footage, I zoomed out a bit
[50:13] to get a nicer framing for the shot.
[50:16] And that's a bit of a more advanced technique that I go through in the course, among others.
[50:22] If you liked this video, you'll like the course.
[50:26] Link below.



---

## Captured Frames

- [2:19] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_000.jpg
- [3:25] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_001.jpg
- [4:19] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_002.jpg
- [6:40] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_003.jpg
- [8:02] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_004.jpg
- [11:00] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_005.jpg
- [11:22] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_006.jpg
- [11:48] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_007.jpg
- [18:38] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_008.jpg
- [24:30] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_009.jpg
- [25:50] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_010.jpg
- [28:05] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_011.jpg
- [33:18] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_012.jpg
- [37:10] tutorials/frames/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations/frame_013.jpg

---

## Structured Notes

### Core Technique
Physically matching a real camera lens in Blender by measuring its bokeh, glare, lens breathing, chromatic aberration and vignette from reference footage, then rebuilding each as a compositor stage applied in a strict 15-step order of operations.

### Summary
Rather than approximating lens artefacts with Blender's stock controls, this builds each effect from measurements of one specific lens (17.5 mm prime, MFT sensor) so CG integrates against footage shot on it. Three separate bokeh methods are compared with explicit trade-offs, glare is generated as a custom convolution kernel in the external tool RealBloom, lens breathing is driven by a focus-to-focal-length driver curve calibrated against a filmed focus rack, and chromatic aberration is rebuilt per-channel with depth-varying vector curves. The payload is the order of operations `[frame_011]`: a 15-stage chain where every effect removed from the plate before compositing is re-added after it.

### Key Steps
1. **Match the camera first.** Movie Clip editor, Track, Camera: Sensor Width `17.300`, Focal Length `17.50 mm`, Lens Distortion model `Polynomial`, `K1 -0.126`, `K2 0.234` `[frame_012]`. Set clip input color space to Panasonic V-Log V-Gamut `[transcript 29:52]`.
2. **Bokeh method 1, pure Blender camera.** Enable Depth of Field, set Focus on Object, then match `Blades` and `Rotation` to the real aperture. Aperture panel reads `F-Stop 2.8`, `Blades 0`, `Rotation 0`, `Ratio 1.000` `[frame_000]` — blades still at the circular default at that moment, changed to match afterwards `[transcript 2:19]`. Easiest and how Cycles is designed to render bokeh, but looks digital and produces no cat's eyes `[transcript 2:24-2:43]`.
3. **Bokeh method 2, physical plane.** Remove the DoF blades, place an image plane of a photographed out-of-focus flashlight directly in front of the camera. Shader is Image Texture into Transparent BSDF into Material Output, image set `Linear Rec.709` / `Premultiplied` `[frame_001]`, white fully transparent and black fully opaque `[transcript 3:13-3:25]`. Extrude the plane's edges wide enough to fall outside the field of view `[transcript 3:50]`. Adds real bokeh colour and texture plus cat's-eye cropping toward frame edges `[frame_002]`, at the cost of slower renders and broken render passes `[transcript 4:36-4:52]`. Modelling an actual circular hole instead of using a texture keeps the cat's eyes and loses the colour, but survives passes `[transcript 4:58-5:17]`.
4. **Bokeh method 3, compositor.** Render sharp, then feed a Bokeh Blur node whose Bokeh input is the flashlight photo. To recover cat's eyes, photograph the flashlight in nine screen positions, drive nine Bokeh Blur nodes, and mix them by screen space using a `Screen segment` node group (`Vertical 1/2`, `Horizontal 1/2`, `Feather 0.130`) `[frame_003]`. Best for stills; breaks under camera motion because the shapes morph incorrectly as lights cross the frame `[transcript 7:01-7:20]`.
5. **Drive bokeh size from depth.** Convert the Z-depth pass to blur size with a Subtract, Absolute, Multiply, Minimum chain, exposing `Focus distance 0.677`, `Blur size 1.400`, `Max blur 100.000`, into a Bokeh Blur node (`Mask 1.000`, `Extend Bounds`) `[frame_004]`.
6. **Capture the aperture at the right f-stop.** Aperture blades physically rotate and disappear wide open, so bokeh and glare references must be shot at the same aperture as the plate `[transcript 9:57-10:29]`.
7. **Generate a glare kernel in RealBloom v0.8.0** `[frame_005]`. Load the aperture photo, enable `Logarithmic Normalization`, press `Compute`. The transcript calls this simply "normalization" `[transcript 10:54]`; the control is labelled *Logarithmic Normalization* `[frame_005]`. Working space is `Linear BT.2020 I-E`, input `Linear BT.709 I-D65`, output `Linear BT.2020 I-E`. A polygonal aperture yields streaks; a circular one does not `[transcript 10:59-11:04]`.
8. **Apply dispersion.** `Move To` into the Dispersion input, then Dispersion tab: `Amount 1.000`, `Edge Offset 1.000`, `Steps 1024`, `Method` set to `GPU` `[frame_006]`. The transcript's "turn everything up to max" `[transcript 11:20]` corresponds to those values. Save the result — it is written in Linear Rec.2020 `[transcript 11:34]`.
9. **Use the kernel in Blender.** Add a Glare node, mode `Kernel`, quality `Medium`, `Strength 1.000`, `Saturation 1.000`; import the kernel image and set its color space to `Linear Rec.2020` `[frame_007]`. Feed the Glare node *only* the CG render, but composite its result over the whole frame — the plate already contains its own glare `[transcript 12:25-12:45]`.
10. **Lens breathing via driver.** Film a focus rack against a grid calling out focus distances, export a still per called distance, rebuild the setup in Blender, and animate camera focus to match each still `[transcript 16:41-17:51]`. Copy focus as a driver onto focal length, then shape the driver curve — focus distance is the input, focal length the output `[frame_008]`. Key infinity focus at the lens's marked `17.5` `[transcript 19:03]`, then add keys per timeline distance, nudging each until the checkerboard stops sliding `[transcript 19:16-19:45]`. Flatten both ends (aligned handles, Y scaled to zero) so focus at 0 does not break the rig `[transcript 20:16-20:49]`. Delete the calibration keyframes when done `[transcript 21:11]`.
11. **Chromatic aberration per channel.** Split with Separate Color (`RGB`), transform each channel independently, recombine with Combine Color `[frame_009]`. Only nodes that can vary per-pixel are usable, since the effect must respond to depth `[transcript 24:47-24:58]`. Work side by side against the shot reference, with a blur node at the head of the chain to match reference softness `[transcript 24:01-24:13]`.
12. **Make it depth-varying.** Animate a value from -1 to +1 representing how far out of focus a pixel is and in which direction (0 is sharp), run it through a `Vector Curves` node (`X`/`Y`/`Z`, `Factor 1.000`) and feed the outputs into each channel's transform or blur `[frame_010]`; the exposed control is a `Defocus level` value, shown at `-0.930` `[frame_010]`. Group the network, expose that input, and drive it from the same Z-depth math used for bokeh, but signed rather than absolute `[transcript 27:26-27:39]`.
13. **Assemble in the documented order** `[frame_011]`: 1 camera color space to working, 2 black level subtract, 3 de-noise, 4 undistort, 5 divide vignette, 6 lens breathing (in render), 7 bokeh blur or DoF, 8 chromatic aberrations, 9 composite CG over plate, 10 multiply vignette, 11 distort, 12 glare, 13 re-noise, 14 black level add, 15 working color space to display. Steps 2-5 are done to the plate before compositing, 6-9 only to CG elements, 11-13 to the finished shot.
14. **Black level tier.** Mix Color set to `Subtract` with a per-channel value (0 red, 0 blue, a small linear green offset) at the head, mirrored by an `Add` at the tail `[transcript 31:57-32:51]`.
15. **Distortion tier.** A `Movie Distortion` node in `Undistort` mode using the tracked clip's polynomial values `[frame_012]`, mirrored by a `Distort` at the tail; force final resolution with a Mix Color fed the original footage in its first input `[transcript 33:53-34:18]`.
16. **Vignette tier.** Divide by the vignette image (`Linear Rec.2020`, strength around `0.25` for the lens actually used) early, multiply it back at full strength late `[transcript 34:36-35:46]`.
17. **Overall softness.** No real lens is perfectly sharp, so add a baseline blur to every render. Matched here at `Size X/Y 3.000 px` `[frame_013]`, reached by eye against the plate `[transcript 36:41-36:49]`, applied to both beauty and shadow passes before the `Segment bokeh` node group adds depth of field `[frame_013]`.

### Nodes / Settings
- **Camera (object data)** — Type `Perspective`, Focal Length `17.5 mm`, Lens Unit `Millimeters`, Clip Start `0.1 m` / End `1000 m`, Depth of Field on, Focus on Object, Aperture `F-Stop 2.8`, `Blades 0`, `Rotation 0`, `Ratio 1.000` `[frame_000]`
- **Movie Clip, Track, Camera** — Sensor Width `17.300`, Pixel Aspect `1.00`, Focal Length `17.50 mm`, Optical Center `0.000/0.000`, Lens Distortion `Polynomial`, `K1 -0.126`, `K2 0.234` `[frame_012]`
- **Bokeh plane shader** — Image Texture (`Linear Rec.709`, `Premultiplied`, Single Image, Flat, Clip) into Transparent BSDF into Material Output `[frame_001]`
- **Bokeh Blur** — inputs Image, Bokeh, Size, `Mask 1.000`, `Extend Bounds` `[frame_004]`
- **Z-depth to blur size** — Subtract, Absolute, Multiply, Minimum, with `Focus distance 0.677`, `Blur size 1.400`, `Max blur 100.000` `[frame_004]`
- **Screen segment (node group)** — `Vertical 1`, `Vertical 2`, `Horizontal 1`, `Horizontal 2`, `Feather 0.130` `[frame_003]`
- **Segment bokeh (node group)** — Result output, segment count `3`, `Defocus 0.000`; paired Blur node at `X 3.000 px` / `Y 3.000 px` `[frame_013]`
- **Glare** — mode `Kernel`, quality `Medium`, `Strength 1.000`, `Saturation 1.000`; kernel image color space `Linear Rec.2020` `[frame_007]`
- **Separate Color / Combine Color** — mode `RGB`, `Alpha 1.000` `[frame_009]`
- **Vector Curves** — `X`/`Y`/`Z` tabs, `Factor 1.000`, fed by a `Defocus level` value node (`-0.930` as shown) `[frame_010]`
- **Movie Distortion** — mode `Undistort`, mirrored by `Distort` late `[frame_012]`
- **Mix Color** — `Subtract` / `Add` for black level, `Divide` / `Multiply` for vignette `[transcript 31:57, 34:44]`
- **RealBloom v0.8.0** — Diffraction: `Logarithmic Normalization` plus `Compute`; Dispersion: `Amount 1.000`, `Edge Offset 1.000`, `Steps 1024`, `Method GPU`; working space `Linear BT.2020 I-E`, input `Linear BT.709 I-D65`, output `Linear BT.2020 I-E` `[frame_005][frame_006]`
- **Render / output** — Cycles, GPU Compute, Noise Threshold `0.0100`, Max Samples `4096`, Denoise plus Temporal Animation Denoiser on, Motion Blur on `[frame_003]`; `3840x2160`, `24 fps`, OpenEXR `RGBA` `Float (Half)` `DWAA (lossy)` quality `90%` `[frame_010][frame_012]`
- **Color Management** — Display `sRGB`, View `AgX`, Look `High Contrast`, Exposure `0.000`, Gamma `1.000` `[frame_009]`
- **External** — RealBloom (free, GitHub) for glare kernel generation `[transcript 10:35]`

### Difficulty
Expert

### Blender Version
Blender 5.2.0 — read from the status bar in `[frame_000]`, `[frame_009]` and `[frame_012]`; never stated in narration.

### Tags
compositing, camera, rendering, cycles, lighting, materials, shaders, blender-5x, expert

---

## Related Tutorials
- [A FULL Blender Compositor Course!](a-full-blender-compositor-course.md) — foundational compositor coverage this builds on; shares compositing, rendering, lighting, materials, shaders
- [I Recreated movie scene in Blender & Nuke | Complete Tutorial](i-recreated-movie-scene-in-blender-nuke-complete-tutorial.md) — the same plate-integration problem approached across two compositors; shares compositing, camera, lighting, rendering
- [Using Geometry Nodes for VFX in Blender](using-geometry-nodes-for-vfx-in-blender.md) — CG-over-plate VFX workflow; shares camera, compositing, lighting, rendering
- [Creating a Japanse city from a photo using fSpy](creating-a-japanse-city-from-a-photo-using-fspy.md) — matching a real camera's parameters to footage; shares camera, cycles, lighting, rendering
