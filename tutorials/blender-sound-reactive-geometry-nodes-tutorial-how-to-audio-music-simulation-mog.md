---
title: Blender Sound Reactive Geometry Nodes | Tutorial How-To Audio Music Simulation Mograph
source: YouTube
url: https://www.youtube.com/watch?v=XOsXZ1qDfSk
author: Chris P
ingested: 2026-07-20
blender_version: "3.6.1"
tags: [geometry-nodes, simulation, particles, procedural, animation, materials, shaders, motion-design, abstract, advanced, blender-3x]
extraction_status: complete
frames_dir: tutorials/frames/blender-sound-reactive-geometry-nodes-tutorial-how-to-audio-music-simulation-mog/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Sound Reactive Geometry Nodes | Tutorial How-To Audio Music Simulation Mograph

**Source:** [YouTube](https://www.youtube.com/watch?v=XOsXZ1qDfSk)
**Author:** Chris P
**Duration:** 25m51s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### What to expect [0:00]
**Transcript (timestamped):**
[0:00] In this tutorial, you will learn how to create sound reactive motion graphics like these,
[0:05] with 100% pure Blender, no add-ons or scripting required.
[0:11] We have three distinct things going on here.
[0:14] The bubbles in the center for the low frequencies, like the kick drums and bass,
[0:18] the particles for sounds in the mid-range frequencies, flying faster for louder sounds,
[0:24] and the random red laser lines for bursts in the high frequency ranges.
[0:29] Welcome Blenderheads and the 70% of viewers who are not subscribed yet.
[0:33] Huh?
[0:33] Please do me a favor and don't forget to like, subscribe and drop a comment,
[0:37] while you're watching and learning new skills for free.
[0:40] Thank you!
[0:42] If you have never seen geometry or simulation nodes in Blender before,
[0:45] I recommend the playlist linked in the card and video description.
[0:51] Now let's fire up Blender and make some cool audio-based animations.
[0:56] This is Sylvie and this tutorial has the Sylvie seal of approval.


### Bake Audio [1:01]
**Transcript (timestamped):**
[1:01] I am using Blender 3.6.1 for this and the first thing of course we want to do is get the audio in.
[1:07] But before that, it's important to set the frame rate.
[1:11] Now we're going to do the same thing as in the demo.
[1:14] We're going to have the bass, the mid frequencies and then the high frequencies.
[1:19] So we're going to use the cube for the bass.
[1:22] Now let's add an icosphere and a torus for the high frequencies.
[1:28] So essentially what we're going to do is assign the volume of our audio file,
[1:35] the bass part to the cube.
[1:37] Okay, how do we do that?
[1:39] So we go to, let's go to animation and on frame one.
[1:44] So this is important.
[1:45] You have to go shift cursor left.
[1:48] Why aren't the screencast keys showing here?
[1:51] So shift cursor left takes you to frame one and on that frame one,
[1:56] we're going to insert a location iframe.
[2:00] Okay, then we're going to take the C location.
[2:04] We can turn this into the graph editor for example.
[2:08] And we're going to take, we don't need these.
[2:10] We just want the C location on frame one and then we go to channel and here we go to channel.
[2:17] And here you can go bake a sound to f curves, which is exactly what we want.
[2:24] And then I take my desired music and in here is where basically the magic happens.
[2:30] So for the base, for the cube, we only want the base and the base we're going to take
[2:36] from frequency zero to 300.
[2:40] Let's just do that and then bake sound to f curve.
[2:44] And you can see we have some stuff in here.
[2:47] Now, of course, this audio file is a longer.
[2:51] So let's click normalize and let's see how long it is.
[2:54] And then we're just going to drag our end frame out to cover the entire song.
[3:00] Now we can see here that there's basically almost no base in the beginning of the song.
[3:04] And then there's some kick drum hits and then there's a quiet again.
[3:10] Now if I hit a spacebar to play, we can see our cube is moving and it's moving
[3:16] with the base part of our song.
[3:20] And then when the base kicks in, we can see it's moving a lot more.
[3:26] However, we can't hear anything yet, but we can fix that.
[3:29] We can go to the video editing part of Blender and bring in the same audio file.
[3:39] Plop that in.
[3:40] Where is it?
[3:42] Oh, of course, I wasn't on frame one now.
[3:44] That doesn't matter.
[3:44] I can just go frame one, move that to frame one and then go back to my animation.
[3:52] And if I hit spacebar now, I hope you can hear it a little bit in the background.
[3:57] I have the music playing and I can hear and see what's happening.
[4:02] So as I said, this is just the base.
[4:04] You can see this is reacting really quite nicely to the base.
[4:09] Now let's do the same thing with the mid range.
[4:13] So let's go back to frame one.
[4:14] This is important because of the baking because I think it starts on the frame that you're
[4:20] currently on.
[4:21] And we always want to be on frame one, so they all line up.
[4:25] Okay, so icosphere, we need a location iframe.
[4:30] We go to the C location, a channel, bake sound, take the same one.
[4:37] And let's do 300 to, I don't know, let's do 4000.
[4:43] Okay, that's will be the mid range part of the sound spectrum.
[4:50] Bake that in.
[4:52] Okay, so there is a lot more happening in the beginning here, whereas there's almost no base.
[4:58] Okay, looking good.
[4:59] Now let's do the high frequencies again, frame one, insert location.
[5:05] Go to the C location, channel, bake sound, pick the sound and let's go from 4000 to
[5:12] 20k.
[5:15] And that's it for the high frequencies.
[5:17] All right, so let's see if it works.
[5:20] Oh, let me save first.
[5:23] And then let's go back to frame one hit space bar.
[5:26] Okay, so there's a lot happening in the mid range here, a little bit in the high frequencies,
[5:32] a little bit in the low frequencies.
[5:34] But then when the base comes in, this is the base.
[5:37] And the high frequencies, the high frequencies are always a bit tricky, because there's not
[5:42] that much in the super high frequencies happening.
[5:46] And they're always overlapping a lot with the mid, but that's just how it is.
[5:51] My name is Chris and I make free blender tutorials.
[5:53] If you enjoy the content, please give the video a thumbs up and subscribe.
[5:57] Thank you.
[5:58] Back to the tutorial.
[5:59] Let's go to geometry notes, because that's what we're going to do most of the work.


### Simulation Nodes [6:02]
**Transcript (timestamped):**
[6:04] Over here, I would like to create a new collection.
[6:07] Let's call it audio and take the ecosphere to cube and the torus and just drag it into
[6:13] the audio collection.
[6:15] First thing we want to do is let's maybe take care of the base.
[6:19] Okay, so for the base animation, I had those bubbles in the center of the screen.
[6:26] Maybe let's just align our camera also again.
[6:30] We don't want to do that.
[6:32] Also again, we don't have screencast keys are showing up and RX 90 and GY bring it out.
[6:40] Look through the camera.
[6:41] This is what we're looking at.
[6:42] Now we're going to need an object for our base motion graphics.
[6:49] So let's bring an object in.
[6:50] It doesn't matter what actually does it matter?
[6:53] Probably not.
[6:54] We just let's just take an ecosphere.
[6:58] Okay, bring it forward maybe a little bit.
[7:02] And on this object here, let's call that a base.
[7:07] On the base object, we create a new geometry notes note tree.
[7:12] And in here, we're going to now take in the information of our cube pin this view.
[7:17] So now we can drag in the cube because that's our base audio information and it's stored in
[7:22] the location here, but it's only in the C.
[7:27] Component of the location.
[7:29] So we have to separate XYC and this is now the volume of the base part of our audio file.
[7:38] Cool.
[7:39] So what do we want to do?
[7:40] We want to probably go into let's look through the camera once more.
[7:46] Let's maybe scale this up.
[7:48] Also, I should have subdivided this a lot more probably.
[7:53] So let's make it a little bit rounder.
[7:57] Okay, now we're going to distribute some points onto this.
[8:01] So we want to distribute points on faces and the density is actually what we're going to plug
[8:08] in from our audio information.
[8:12] So when there's a lot of base happening, then we have more points distributed onto our ecosphere.
[8:20] Let's see if it works.
[8:21] So let's go here.
[8:22] We have the music playing.
[8:27] Okay, we can see more base and we get more points distributed.
[8:35] All right, seems to be pretty cool.
[8:38] But we want to maybe take away the really quiet parts.
[8:44] Now I didn't find a smooth solution for sort of a high pass filter,
[8:51] but we can always just do maybe a compare.
[8:55] Compare and say, okay, if our volume information is less than 0.3, then we want to switch a float
[9:10] value float float float.
[9:15] Okay, so if it's less than we want zero, if it's greater than we want this.
[9:22] Okay, and then also we should add probably a math node so we can multiply our value a little bit.
[9:32] Bring this over.
[9:33] And this is our density in a team.
[9:37] Okay, so when there's when there's almost no base happening, we have zero points.
[9:44] And only if our value is above 0.3, we get some points, we can increase this to 0.5.
[9:53] All right, all right, that's the base information.
[9:56] Now this is just a point cloud, there's nothing to render, and we can actually see
[10:00] anything if we would hit render now.
[10:03] So right away, we can do in instance on points.
[10:10] And what do we want to instance?
[10:12] Maybe an icosphere with a few subdivisions.
[10:18] All right, cool.
[10:20] So we have this now.
[10:25] Okay, now for the actual animation, we want these icospheres.
[10:29] Yeah, the icospheres to like appear when the base hits and then just shrink down to nothing.
[10:37] Okay, let's do that.
[10:39] And we have to do that in a simulation zone.
[10:44] Just a quick reminder, if you have no idea how this works, I have an entire tutorial series
[10:49] looking at the simulation zones and the simulation nodes in blender geometry nodes.
[10:55] So you should watch those videos first probably.
[11:00] All right, now let's plug this in.
[11:01] We want to simulate our geometry, the geometry in this case is like I said, just a point cloud.
[11:09] Okay, now we want the spheres to shrink down.
[11:15] For that, we need to simulate something in this zone over time.
[11:20] Let's give each sphere the information of its size, we can do that.
[11:26] But just we could capture an attribute or we could use a named attribute, but each point in a
[11:32] point cloud has more than just a position. It also knows it also has a rotation.
[11:39] And it also has a scale, which in case of a point is the radius.
[11:44] So we can go search radius, and we can say set point radius.
[11:50] And let's just start off with a radius of one.
[11:52] So we have sort of a factor between one and zero.
[11:56] Okay, we have a radius of one.
[11:58] And then over time, which is in here, the simulation.
[12:02] So whatever you plug in here is just for the first frame.
[12:05] After the first frame, you're just simulating stuff here and none of this input is used anymore.
[12:12] Okay, so in our inside of the simulation, we want to get the point radius,
[12:18] and then set the point radius to a new value.
[12:24] Let's do radius.
[12:27] Okay, we need to read the radius and we need a math node.
[12:31] And we can multiply the previous radius by I don't know, point seven.
[12:39] And then we set the point radius.
[12:41] Now, of course, this is already working, but it's not showing up because we're not using it yet.
[12:47] Because when we actually instant some icospheres onto our points out here,
[12:53] we can give it a scale and again use the radius.
[12:57] Okay, now this is actually not correct yet because on each frame, we create some points
[13:04] onto our big icosphere.
[13:06] And then we want to animate those.
[13:09] But of course, on the next frame, they're they disappeared again, because we create new points
[13:16] onto our geometry.
[13:18] So we don't actually want to plug this into our simulation like this.
[13:23] We want to add the points, the new points to the existing simulation.
[13:30] So remember, on all of these frames, this is just running in a circle here.
[13:35] This is just keeps assimilating on each frame.
[13:38] And we want to have the points from the previous frame and add these points to it.
[13:46] So we need to join geometry, the one from the previous frame, and we add the new points to that.
[13:55] And then of course, actually, we want to set our we want to set the point radius only
[14:05] on the old geometry.
[14:08] So the new geometry has a radius of one, the old geometry coming in from the previous frame
[14:14] has a radius, and we change it and set the new radius.
[14:19] And then we have join.
[14:21] And now let's see if that works.
[14:27] Okay.
[14:29] Yes, seems to be working.
[14:30] Okay, so we're distributing points.
[14:32] Now, of course, this is all a bit big.
[14:34] So we can either play with the radius, or we could let's bring this down a little.
[14:41] So we have cleaner noodles, or we could just say, okay, let's start with the radius of point five,
[14:47] maybe.
[14:51] Yep, that's exactly what we want.
[14:53] However, there's one thing now that we can't even see, but it is happening.
[14:57] And that is, let me just go back a few frames.
[15:00] Okay, so the base drum hits, we get new points, they're big.
[15:03] Then with our simulation, we decrease the size by multiplying the previous radius with point seven.
[15:10] And then they just basically disappear because they get so small.
[15:16] However, they're still there.
[15:19] So this geometry here is keeps growing and keeps growing.
[15:22] We just add points and add points on each frame.
[15:27] We don't need to do this, we could just delete some of the points once they're not visible anymore.
[15:33] Anyway, right, you don't want to just load up your geometry and our simulation with millions of points.
[15:41] So how do we do that?
[15:41] Well, we can just go geometry, delete geometry, and what geometry, what points are we going to delete?
[15:51] The ones where we need a math node.
[15:57] Can I just look for less than oh, math less than cool, where the radius of the point
[16:05] is less than, let's just say point zero one, see how that works.
[16:13] Yeah, pretty cool.
[16:15] Okay.
[16:16] And then down here, we can see we have 595 instances currently.
[16:22] If we let it run some more, now we have 727.
[16:27] Okay, let's go forward a few frames, you can see now we have 400, 300,
[16:35] okay, now we have more again, and then because when the base drum hits, and we get a lot of points.
[16:43] So maybe this value is a bit much, multiply it by two, see.
[16:51] Yep, okay, looks pretty cool.
[16:53] And we're not just adding new points.
[16:56] We're also getting rid of the points that we can't see anymore.
[17:00] Anyway, and this is all we need to make sound reactive motion graphics.
[17:06] Okay, now let me open the demo file and show you all the other parts.


### Bass Material [17:11]
**Transcript (timestamped):**
[17:11] Okay, this is my demo file and you can see here I am on the low frequency object here.
[17:19] And this is exactly the same.
[17:21] No tree would take the information from the cube.
[17:25] I called it low, but it's the cube.
[17:29] Okay, so we take the low information, the C axis, we do our high pass filter here,
[17:36] distribute the points, set the radius,
[17:41] make them smaller over time or decrease the radius over time, we delete the geometry we
[17:47] can't see anymore, we instance icospheres.
[17:50] And then back here I also set smooth, which you have to do inside of geometry notes so that
[17:55] these spheres are smooth.
[17:57] And then I also have a material.
[18:00] The material is this one, where I just assign a random factor here to get a little bit of
[18:09] variation.
[18:10] So we have some yellow and some red with this color ramp.
[18:14] And then I use the layer weight.
[18:17] And I'm sure you've seen this before.
[18:20] This is the layer of weight.
[18:22] And usually it looks like this.
[18:24] So that gives you the angle of the surface to your camera.
[18:29] And you can turn down the blend.
[18:31] So you can just get the outer, the circle basically of the sphere and you plug that through a color
[18:38] ramp.
[18:39] You can do something like this, which is pretty cool looking.
[18:43] And then I just use the emission shader.
[18:47] And I don't even know if I need this.
[18:48] Hold on.
[18:49] Do I need this?
[18:51] Oh yeah, okay.
[18:52] I use this factor here.
[18:54] That gives me just a circle to mix between the emission shader and an empty shader,
[18:59] which gives me the black inside.
[19:01] And this also gives a cool effect because it looks sort of like a cartoonish cloud.
[19:06] Because we don't get the full circles where we have overlapping spheres.
[19:10] So I think this is actually a pretty cool shader to create these sort of cartoony clouds.
[19:19] Okay, now go back to geometry notes.


### Mids [19:21]
**Transcript (timestamped):**
[19:21] Let's look at the mid.
[19:23] What have we done for the mid?
[19:25] So we're taking the C location from our mid object, which was the sphere.
[19:32] And then again, we separate high pass filter, multiply.
[19:38] And what I've done here is my mid object, this guy here, is actually an ecosphere,
[19:46] a very tiny ecosphere in the middle of the scene.
[19:50] And I can emit particles like all of these dots here by shooting them out along the normal.
[19:57] So if you have the ecosphere, you want the normal would be here and this normal would be here.
[20:04] Right, so we can emit particles like this from our original geometry, which is an ecosphere,
[20:10] by taking the normal of our ecosphere and storing this in a named attribute,
[20:16] and I called it V for velocity.
[20:19] So each of our points that we're emitting on each frame now has the velocity,
[20:26] and also store another attribute called age.
[20:29] Inside of the simulation, I take the age, I add one so on each frame,
[20:34] each particle gets older by one, right?
[20:37] So read, add store.
[20:40] Again, we have delete geometry here because we want to delete the particles once they leave
[20:46] our frame.
[20:47] So this is the camera frame here.
[20:48] I don't know if you can see this on the recording, but we don't need to make them fly out infinitely.
[20:54] Once they hit outside here, or once they reach the outside of our frame, we can delete them.
[20:59] So that's what we're doing here.
[21:00] If our age is greater than 60, we delete the points.
[21:06] And then of course, we want to move the point on each frame.
[21:09] We move each point on the V, remember, we're going to move the point on the V,
[21:15] remember V is our velocity, which is the normal.
[21:19] So we have a lot of particles flying outwards.
[21:24] And also V, let me see here, I'm scaling the normal based on,
[21:33] you can probably see this here, based on the C of our music, right?
[21:42] So particles, the V vector velocity vector is greater, longer, where the music is louder.
[21:49] And remember, we're just talking about the mid range frequencies here.
[21:53] So the louder mid range hits that we have, the longer our velocity is, which means the faster
[22:00] these particles are flying.
[22:02] And then back here, it's same thing.
[22:04] We're creating ecospheres, which are all of these little dots.
[22:07] We have set smooth, have a different material.


### Mids Material [22:08]
**Transcript (timestamped):**
[22:10] Let's look at the material real quick.
[22:13] The material uses the age to have a color ramp between age zero and age one.
[22:22] So in order to get a factor between zero and one, we have to divide the age by 60.
[22:27] Remember, we're deleting the particles after 60 frames.
[22:31] So no particle is ever older than 60.
[22:35] So we had a factor between zero and one.
[22:37] So when they're born, they're bright white.
[22:39] And then over time, we have this color ramp, emission shader, and that's it.
[22:45] So if we hit play, this is what we get.
[22:50] And you can see we have some particles flying faster and some are slower.
[22:54] And that's just the volume of our mid range audio.
[23:00] All right.


### Treble [23:01]
**Transcript (timestamped):**
[23:01] So that's that.
[23:02] And then we have the high frequencies.
[23:05] Let's look at those geometry nodes.
[23:08] High frequency.
[23:09] Hi.
[23:10] And in here, you can see I don't even have a simulation area on each frame.
[23:15] I simply create two random vectors that are just somewhere inside of my frame.
[23:22] So x minus 50 C minus 20, and they're all on the on the y zero plane.
[23:31] So we just get some random vectors.
[23:33] If we look at it from the front, and then we have two random vectors.
[23:39] And they also have different values because I plugged the frame from our animation value
[23:45] into the ID here.
[23:46] So we get two different random vectors, create a curve out of that curve to mesh based on a circle.
[23:54] And then set the material to the high material.
[23:57] The high material is just an emission shader with a very high strength,
[24:01] which gives us this sort of laser beam look.
[24:05] And down here, I'm using the audio information again, the C value from the high frequency
[24:15] info.
[24:16] And if I say if that is greater than this is again, sort of a high pass,
[24:21] then either we have zero or that value, which is the high pass.
[24:26] And I use that as the curve circle for this line.
[24:31] So essentially, we get a random line on our screen on every single frame.
[24:38] But on the frames where the high frequency audio is not very loud,
[24:44] the radius is zero.
[24:46] So we just can't see it.
[24:48] All right.
[24:48] So this doesn't even have an animation.
[24:50] This is just like laser light flickering.
[24:52] And if we put it all together and hit spacebar,
[24:56] then this is what we get.
[25:00] Now remember, we got the audio information into these three objects here by baking the audio
[25:06] and selecting a certain frequency range.
[25:10] And if you wanted to create a spectrum analyzer, you could do the same thing.
[25:16] Just, I don't know, get 10 divisions of your frequency range and then have bars scaled on the
[25:22] C and have a shader going from green to yellow to red.
[25:27] It's really very easy.


### Outro [25:29]
**Transcript (timestamped):**
[25:29] That's it.
[25:29] As always, the finished plan file for this tutorial and many, many more is available
[25:33] to download at patreon.com slash crispy.
[25:36] Thanks for watching.
[25:37] See you soon.
[25:38] Bye.



---

## Captured Frames

- [2:17] tutorials/frames/blender-sound-reactive-geometry-nodes-tutorial-how-to-audio-music-simulation-mog/frame_000.jpg
- [3:16] tutorials/frames/blender-sound-reactive-geometry-nodes-tutorial-how-to-audio-music-simulation-mog/frame_001.jpg
- [8:27] tutorials/frames/blender-sound-reactive-geometry-nodes-tutorial-how-to-audio-music-simulation-mog/frame_002.jpg
- [12:53] tutorials/frames/blender-sound-reactive-geometry-nodes-tutorial-how-to-audio-music-simulation-mog/frame_003.jpg
- [18:38] tutorials/frames/blender-sound-reactive-geometry-nodes-tutorial-how-to-audio-music-simulation-mog/frame_004.jpg
- [22:45] tutorials/frames/blender-sound-reactive-geometry-nodes-tutorial-how-to-audio-music-simulation-mog/frame_005.jpg
- [23:54] tutorials/frames/blender-sound-reactive-geometry-nodes-tutorial-how-to-audio-music-simulation-mog/frame_006.jpg
- [25:00] tutorials/frames/blender-sound-reactive-geometry-nodes-tutorial-how-to-audio-music-simulation-mog/frame_007.jpg

---

## Structured Notes

### Core Technique
Pure-Blender (no add-ons/scripting) audio-reactive motion graphics: baking three frequency bands of a music track to F-Curves via the Graph Editor's "Bake Sound to F-Curves," then feeding those baked values into three separate Geometry Nodes setups (bubble-growth simulation, outward-flying particles, flickering laser lines) driven entirely by Object Info location reads.

### Summary
Chris P (Sylvie/CrispyGoods) splits an audio track into low (bass), mid, and high frequency bands by baking each range's volume to the Z-location F-Curve of three helper objects (Cube = bass, Icosphere = mid, Torus = high). Those baked values then drive three independent Geometry Nodes systems: bubble-like spheres that spawn on a base Icosphere and shrink over time inside a Simulation Zone whenever the bass hits (with old, invisible points deleted every frame to control point-cloud growth), particles emitted along surface normals from a tiny sphere that fly faster the louder the mid-range gets (using a stored velocity attribute and an age-based delete/color system), and random red "laser" line segments generated per-frame from two random 2D vectors, visible only when the high-frequency volume passes a threshold. A cartoonish bubble-cloud shader (Layer Weight + Color Ramp + Emission/Transparent mix) and an age-based emission Color Ramp for the particles round out the look.

### Key Steps
1. **Set project frame rate first**, then bring in helper objects: a Cube (bass), an Icosphere (mid), and a Torus (high) — their sole purpose is to carry baked audio-volume data on their Z Location channel, they are not the visible motion-graphics objects themselves.
2. **Bake each frequency band**: on frame 1 (Shift+Left-Arrow to jump there), select the helper object, insert a Location keyframe, open the Graph Editor, isolate the Z Location channel, then Channel > Bake Sound to F-Curves; pick the audio file and set a Low/High frequency range for that object (e.g. 0-300 Hz for bass, 300-4000 Hz for mid, 4000-20000 Hz for high) and click Bake Sound to F-Curve. Click Normalize and extend the scene's End Frame to cover the full song length. Repeat per object, always starting from frame 1 so all three bakes stay aligned.
3. **Preview with real audio**: switch to the Video Sequencer, add the same audio file as a sound strip at frame 1, then play back in the 3D viewport/Graph Editor to confirm each object's Z Location visibly spikes with its assigned frequency band.
4. **Bass bubbles — Geometry Nodes on a "Base" object** (an enlarged, subdivided Icosphere): Object Info (the Cube) > Separate XYZ > take the Z output as the bass volume; run it through a high-pass gate (Compare "less than 0.3" driving a Switch between 0.0 and the raw value) then a Math multiply to scale it, and feed the result into Distribute Points on Faces > Density, so points only appear once bass volume crosses the threshold.
5. **Grow-and-shrink via Simulation Zone**: inside a Simulation Input/Output zone, use Set Point Radius (start at 1.0, or lower like 0.5 for a cleaner look) on the first frame; every subsequent frame, read the previous radius with a Math node (multiply by ~0.7) and re-apply it with Set Point Radius so spheres shrink over time. Critically, Join Geometry the previous frame's (shrunk) points with the newly distributed points each frame — otherwise the simulation loses all prior points on every frame instead of accumulating them.
6. **Prevent runaway point counts**: inside the simulation loop, Delete Geometry any points whose radius has dropped below a small threshold (e.g. 0.01, tuned with a Less Than math node) so invisible/fully-shrunk bubbles don't keep piling up in the point cloud forever.
7. **Instance and shade**: Instance on Points with a subdivided Icosphere (Shade Smooth applied inside Geometry Nodes) scaled by each point's radius; the "bass" material uses Object Info > Random per-instance factor into a Color Ramp (yellow-to-red) for variation, plus Layer Weight (Blend lowered) piped through a second Color Ramp to fake a rim/silhouette look, mixed between an Emission shader and a Transparent shader — the overlapping-sphere silhouette effect reads as a cartoonish glowing cloud rather than solid balls.
8. **Mid-range particles — Geometry Nodes on a tiny center Icosphere**: emit points along the object's surface Normal, store that Normal in a Named Attribute ("V" for velocity) and store a separate "age" Named Attribute; inside a Simulation Zone, increment age by 1 each frame, Delete Geometry once age exceeds 60 (keeps particles from flying forever/off-screen), and each frame move every point by its stored V vector — scaling V's magnitude by the mid-frequency volume (from Object Info > Separate XYZ > Z) so louder mid-range hits shoot particles out faster/farther.
9. **Mid-range shader**: divide the stored "age" attribute by 60 (matching the delete-at-60 lifespan) to get a 0-1 factor into a Color Ramp feeding an Emission shader, so particles are bright white when freshly born and fade/color-shift as they age.
10. **High-frequency laser lines — no simulation zone needed**: each frame, generate two random Vector positions (e.g. X range ±50, Z range ±20, Y locked to 0) using the current Frame number as the Random node's ID/Seed so the vectors change every frame; build a Curve Line between them, Curve to Mesh with a Curve Circle profile, and set the circle's radius via another high-pass gate on the high-frequency Object Info Z value (Compare greater-than a threshold, Switch between 0 and the value) — so the line mesh has zero radius (invisible) except on frames where a high-frequency transient crosses the threshold, producing a flickering "laser burst" look. Apply an Emission material with high Strength for the laser glow.
11. **Composite**: with all three systems in an "Audio" collection reacting to their respective baked F-Curves, hitting Play with the audio scrubbing/strip loaded shows bubbles pulsing on bass hits, particles flying faster on mid-range swells, and red lines flickering on high-frequency transients — no drivers, add-ons, or Python needed, purely F-Curve baking + Geometry Nodes math.
12. **Extending the idea**: the same baked-frequency-range technique scales to a full spectrum analyzer — bake ~10 frequency divisions to 10 objects, scale bars on Z from each object's value, and color them via a green-to-yellow-to-red Color Ramp.

### Nodes / Settings
- **Graph Editor > Channel menu**: Bake Sound to F-Curves (per-object, per-frequency-range: Low/High Hz bounds, Normalize checkbox).
- **Geometry Nodes (Bass/"low" tree)**: Object Info → Separate XYZ (Z = bass volume) → Compare (Less Than 0.3) → Switch (float) → Math (Multiply) → Distribute Points on Faces (Density input); Simulation Input/Output zone with Set Point Radius, Math (Multiply ~0.7 for decay), Join Geometry (previous + new points), Delete Geometry (Math Less Than ~0.01 on radius); Instance on Points (Ico Sphere, Scale = radius, Shade Smooth).
- **Bass material (Shading)**: Object Info (Random) → Color Ramp (yellow→red) for per-instance variance; Layer Weight (Blend lowered) → Color Ramp → Mix Shader between Emission and Transparent BSDF for the cartoon-cloud silhouette look.
- **Geometry Nodes (Mid tree)**: emits points along surface Normal, Store Named Attribute "V" (velocity = Normal, magnitude scaled by mid-frequency Object Info Z value) and "age"; Simulation Zone: Read age → Math Add 1 → Store; Delete Geometry (age > 60); Set Position (offset by V each frame); instances small Ico Spheres, Shade Smooth.
- **Mid material**: age attribute ÷ 60 → Color Ramp → Emission Shader (bright-to-faded over particle lifetime).
- **Geometry Nodes (High/"hi" tree)**: two Random Value (Vector) nodes seeded by the current Frame value → Curve Line → Curve to Mesh with a Curve Circle profile whose Radius is gated by Object Info (high-freq Z) → Compare (Greater Than) → Switch (0 or the value) → Set Material.
- **High material**: plain Emission shader at high Strength for a laser-beam glow.
- **Scene setup**: Video Sequencer with an audio Sound strip at frame 1 for audible/scrubbable playback while animating.

### Difficulty
Advanced

### Blender Version
Blender 3.6.1

### Tags
geometry-nodes, simulation, particles, procedural, animation, materials, shaders, motion-design, abstract, advanced, blender-3x

---

## Related Tutorials
- [Blender Tutorial: Connect The Dots with Geometry Nodes, The "Plexus" Effect](blender-tutorial-connect-the-dots-with-geometry-nodes-the-pl.md) — same era (Blender 3.4-3.6) advanced procedural/particle motion-design technique using per-frame randomization and point-cloud logic, directly comparable to this tutorial's laser-line and bubble systems.
- [Blender 5.0 particle attraction and follow surface motion](blender-50-particle-attraction-and-follow-surface-motion.md) — closely related Geometry Nodes particle-simulation technique (surface-normal-driven point emission and velocity vectors), the same core mechanism used for this tutorial's mid-frequency flying particles.
