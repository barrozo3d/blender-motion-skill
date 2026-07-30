---
title: The Sample Sound Node is So Powerful (Blender 5.2 tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=B0KwaI0Eqqk
author: Ducky 3D
ingested: 2026-07-30
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/the-sample-sound-node-is-so-powerful-blender-52-tutorial/
frame_count: 0
frame_status: pending-selection
---

# The Sample Sound Node is So Powerful (Blender 5.2 tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=B0KwaI0Eqqk)
**Author:** Ducky 3D
**Duration:** 16m9s | 5 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py the-sample-sound-node-is-so-powerful-blender-52-tutorial <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Alright, today we are going to learn how to make anything react to music with the brand new sample sound frequencies node in Blender 5.2.
[0:08] So first I'm going to show you a very simple setup to be able to kind of extract the waveform from your audio and be able to visualize it.
[0:15] Then we're going to make two designs with this.
[0:18] We're going to make the very simple kind of flat audio waveform animations you've seen on YouTube hundreds of times.
[0:23] And then we're going to do the same thing, but circularly.
[0:27] That's really important because both require just one very important change for you to be able to do one flat and one circular.
[0:32] Lots of people want to do it circular, lots of people want to do it flat.
[0:35] So we are going to learn how to do that.
[0:37] Then I'm going to show you how to take that music information, send it to the shading and actually be able to visualize the waveform in your shader editor.
[0:44] It might sound daunting, but it's pretty simple.
[0:46] And this also won't be the last time I use this node on this channel.
[0:49] I'll be making some more fully designed creative application of this.
[0:54] Today we're just going to learn how to use it and very simple application.
[0:57] So with that being said, let's make this.
[0:59] Okay. So the first step is we're just going to head into geometry nodes, go to that workspace.
[1:04] I'm going to bring this up a little bit and we're going to head into the video sequencer, click new, add, add sound and go ahead and grab whatever sound, whatever song you want to use.
[1:14] I'm just going to place it randomly somewhere in the timeline.
[1:17] And I'm going to hit the home button just to make it a little bigger and it's still not really bigger.
[1:23] Let's see home.
[1:24] There we go.
[1:25] And then I'm going to make sure that I am at frame one and then we just put our audio at frame one.
[1:31] Now for me, I don't want to hear the song.
[1:32] It's not really important for the tutorial, but the audio is now imported.
[1:35] I'm just going to hit H and mute the audio, but it will still be perfectly usable here in geometry nodes.
[1:42] So we have, we now have this.
[1:44] Let's go ahead and then here in the viewport, I'm going to just throw a piece of geometry into the scene.
[1:50] I usually just pick a plane.
[1:51] Now we can start a geometry nodes tree.
[1:53] So first let's create the plane so that we can kind of visualize the audio and kind of jumping around here.
[1:59] I'm going to give myself like 5000 frames.
[2:03] I just want to be able to scrub through the whole song.
[2:06] Okay.
[2:07] So I'm going to delete the input and let's go ahead and import a grid just like that.
[2:13] We're going to scale it to be 10 by 10 and plug it into the output.
[2:18] I'm going to give myself maybe a hundred vertices.
[2:21] So we're going to be able to look at the audio right here.
[2:23] So let's set up the sample sound node.
[2:26] So hit shift a search up sound sample sound frequencies.


### set up sample sound frequencies node [2:27]
**Transcript (timestamped):**
[2:31] We need to set up essentially it's like texture coordinate.
[2:34] We'll compare it to that.
[2:36] And so in this case, I want to be able to apply this as like a bump map.
[2:42] So we're going to use a position.
[2:44] Now there's going to be for the flat animation, we're going to use the position node and then for the circular animation,
[2:49] we're going to use the index because it's a little bit more complicated.
[2:53] But right now let's use the position node and then I'm going to get a separate X, Y, Z to define which direction the audio is going to be mapped
[3:03] because it is a flat do we call it a float, but it's not it's not a 3D thing.
[3:09] It's a flat 2D image essentially.
[3:12] So we need to be able to define where it's going to be.
[3:15] So what I need to do now is get a map range.
[3:19] So let's go ahead and get a map range and we'll plug whatever axis I'm a pick Y and this is what's going to be the thing that actually stretches out
[3:28] and lets us view the waveform.
[3:31] Now before we can do that, we need to go right here on the sample sound frequencies node, drop down and grab your audio and then you need to get a scene time node
[3:43] and plug seconds into time so that we don't have to keyframe that when we press play on our timeline.
[3:48] He is essentially going to also press play.
[3:50] So now we have this.
[3:52] We have low and our high.
[3:54] So let's look at this and we're going to be able to use this exact setup on the circular one and here on the flat one.
[4:02] So what we need to do this min this max is going to be your high and your low end.
[4:07] So what I'm going to do here is I'm going to give my two max 15,000 that's going to be in Hertz.
[4:14] That's kind of some nerdy stuff, but based on my like nerdy audio stuff that I don't know anything about 15,000 Hertz and then we'll do 20 on the low end.
[4:24] These are going to be things that stretch out the audio.
[4:27] So last thing I need to do is get a math node for our high end.
[4:30] We're going to plug the map range into that and just give it a boost of 100.
[4:35] We'll plug that into the high and we'll plug the map range into the low.
[4:40] There we go.
[4:40] Everything is now set up.
[4:42] So what I want to do now is visualize what we're looking at.
[4:45] So I know how to make changes here.
[4:47] So what I'm going to do is I'm going to get a viewer node.
[4:51] I'm going to plug the grid into the viewer.
[4:53] I'm going to hit this computer icon and then plug the amplitude into that.
[4:57] Now when I press play, we can see something happening.
[5:00] I'm going to go to the more intense portion of the song.
[5:02] Notice this is basically a single value that is outputting.
[5:06] That's changing a lot.
[5:08] But if you zoom in here, we can see a lot of other values moving around.
[5:11] So that's where the white lot of the high end of the audio is.
[5:16] This is all low end.
[5:18] And so the from in from acts is going to move it around.
[5:22] So we can move this around like that.
[5:24] I noticed negative four is a good spot to be.
[5:27] And then on the max, that's when you can start stretching it out and actually see.
[5:32] So this side is going to be your low end, your base, your I mean the base.
[5:36] Then you have your treble and your high end parts of the audio.
[5:39] And this is when you can start making creative decisions on how much of the song
[5:43] or what part of the song you want to see.
[5:45] Last thing I want to do before we can start applying this creatively is this FFT.
[5:51] It's kind of like resolution.
[5:56] And I'm sure there's like a technically that might be technically wrong.
[5:59] But look at this.
[6:01] But if we look at it right now, default is 4096.
[6:03] If I bring it all the way to like 256, you can see that and almost looks like we scaled it up
[6:09] or zoomed in on the low end.
[6:10] We it's still seeing your high end in your low end.
[6:14] But if we go to the highest, the 332768, a lot more detail.
[6:22] It's a little slower.
[6:23] It animates a little bit differently.
[6:25] I almost wonder if it's lagging frame rate wise.
[6:27] It's not lagging.
[6:29] I keep it at the default 4096.
[6:31] Of course, if you want more data, it really depends on what you're doing.
[6:34] If it's displacement or maybe simple scaling, maybe certain amounts of detail isn't necessary for you.
[6:41] So play around with that.
[6:42] And then this I literally have no idea what window function is.
[6:45] So I'm not going to talk about it.
[6:49] But this is how to visualize audio.
[6:52] So now let's make something with it and be on our way.
[6:58] So let's go ahead and delete the viewer here on this grid.


### flat audio waveform + spectrum [7:00]
**Transcript (timestamped):**
[7:02] I'm going to give it keep it out of size of 10.
[7:04] The X, I'm going to give it 0.5 vertices of two on the X and vertices of say 40 on the Y.
[7:15] And then now I want to kind of separate all those faces so we can see them individually.
[7:19] So we need to get a split edges node and then a scale elements node so that after we split the edges,
[7:28] we can scale them down.
[7:31] And then the fun part is we're going to extrude the mesh.
[7:35] And this is what's going to be the thing that like animates up and down is this offset.
[7:39] And so we what we did was we kind of use this and created essentially like a displacement map that you can plug into things like the offset or the scale things that handle floats.
[7:53] Plug it into there and you could see it's working correctly.
[7:56] Now make sure you're on the proper axis.
[8:00] Say that I was using X, it would just kind of look like it's all scaling together.
[8:04] So if it's doing something like that, switch your axis and that'll fix it right now.
[8:10] It's really, really low to the ground.
[8:14] So what you can do is get another map range and bring up those highs and those lows together.
[8:21] And now we have this now.
[8:22] Again, this is the part where you start to make some more creative decisions and go.
[8:26] Well, there's a lot going on the low end.
[8:28] There's not a whole lot going on the high end.
[8:30] I don't know enough to like say, what do I want to boost the high end but not without me.
[8:35] So this is when you can go.
[8:36] Well, I can just kind of stretch the low end so we see more low end.
[8:42] So we see the more low end and then you can have some fun with a really nice looking waveform and you really can just sort of cut out things and just make it look good.
[8:54] And also really quick, I'm in the middle of editing this video and I realized my two minimum at 20 is incredibly, incredibly low.
[9:03] So when I boosted it up to like 800 and then got to look at the full waveform, you get a lot more scale in the lower end.
[9:13] But when it was just set to 20, this was super huge and this was really small and it looked bad.
[9:19] So if you get your two minimum close to the two maximum, the high and the low aren't going to be competing visually.
[9:27] You can actually see an even distribution of the two of them and then you can actually get to see the whole waveform and all of the fun that can go with it.
[9:36] So ignore them, 20, keep it at 15,000 and just kind of play with your minimum how high you want that to be.
[9:42] Again, I'm not, I don't know much about audio.
[9:45] I know about visuals, but this is a really great looking waveform.
[9:50] Last thing we can do from a creative standpoint is to get up the wonderful new mesh bevel node and then bring that bevel down a little bit and then bring up your segments.
[10:01] And then now we have a really good looking waveform.
[10:05] So what I'm going to do, I'm going to save this here.
[10:08] So I'm just going to slice that off.
[10:10] That's plugged into the offset and then slice this.
[10:13] I'm going to move this up and we're going to use it later to visualize the sound in the shader editor.
[10:20] But next we're going to, we're going to reuse this, but make a circular waveform.
[10:26] So let's get a, we're going to use a cylinder for this.


### circular audio waveform + spectrum [10:27]
**Transcript (timestamped):**
[10:29] I'm going to plug my cylinder into here.
[10:32] I'm going to go ahead and say, I do not want any fill.
[10:37] So now we have that.
[10:38] I'm going to bring my radius up a little bit, bring my depth down.
[10:42] I'm going to get my vertices up a little bit higher, something like that.
[10:46] And then we're going to do the same exact thing.
[10:47] We're going to split edges.
[10:53] We're going to split the edges.
[10:54] We're going to scale the elements, scale them down and then extrude the mesh just like that.
[11:04] So now we have this that we can animate.
[11:06] Let's talk about the index.
[11:09] So for right now we're using position.
[11:12] And so the, I guess we'll call it like mapping of this texture that we're creating from audio, doesn't really care too much about where the faces are located.
[11:24] It's mapping it in a different way.
[11:27] If you want to know, if you don't know about the index, essentially, let's say we hypothetically start here.
[11:32] Every one of these faces that we've now extruded, especially before we extrude it has an index starts at zero.
[11:39] One, two, three, four, five, six.
[11:41] It's in chronological order.
[11:43] So what happens is if I use a index instead of a position to map this texture, then it will map it to this circle.
[11:51] So I don't have to worry about UVs and making sure that this flat texture is mapping correctly.
[11:57] This to me is the easiest way to get this audio texture to map to a circular object properly with the knowledge that I have today.
[12:08] I'm sure there's some really cool ways to do this that I don't know.
[12:11] So what I'll do is I will just get a index node, plug it in here, and then now I will just plug this map range result right into the offset.
[12:23] And then now we have that.
[12:24] So this is when we can start doing some stuff.
[12:26] So I'm going to bring my max up, even bring my minimum up a little bit.
[12:30] And then we can kind of look at this.
[12:31] I'll go, okay, well, I want to see more of the low end over here.
[12:34] So again, we can do that same thing where we can kind of stretch this out and get a more satisfying waveform animation.
[12:44] And this is now circular.
[12:45] And you can do the same thing.
[12:46] You can bevel it.
[12:47] You can apply materials to it.
[12:49] You can just make it glow if you want.
[12:51] There's a lot of really interesting things that can be done here and it's now circular.
[12:58] Very, I mean, this is like a popular style you'd see on YouTube quite a bit.
[13:03] But now you can do it flat.
[13:04] You can do it circular.
[13:06] You know how to do it.
[13:07] Last thing I want to show you is how to get to actually visualize this audio in the shading.
[13:13] So what I'll do is I'll delete this circular situation that I created, bring this back down, plug this into the geometry,
[13:20] and then I'm just going to go ahead, move this back, plug my position into the separate,
[13:27] and then plug my map range into the extrude mesh.
[13:32] And then bring that map range information back.
[13:38] There we go.
[13:38] Something like this.
[13:40] Okay.
[13:41] So let's go ahead and look at using the shading.
[13:45] So again, if you want to follow along here, get this position plugged back in the separate XYZ,
[13:50] basically the old system that we had with this flat one.


### view audio spectrum in the shading editor [13:54]
**Transcript (timestamped):**
[13:54] So how do you, yeah, how do you visualize the audio?
[13:57] So what you'll do is use an attribute.
[13:58] So we'll get a store named attribute.
[14:03] I'm going to call it, I'm just name it S for sound.
[14:05] And I want it to do it to the faces, which means I actually don't want to do it.
[14:11] I want to do it before the mesh bevel because I don't want to actually apply to the bevel faces.
[14:19] I want to apply before we bevel the faces.
[14:22] So it's just flat.
[14:23] And then we'll plug the map range into the value.
[14:25] So now we have that plugging into that.
[14:30] Let's go ahead and get a set material node down over here.
[14:34] We'll get a new material and we'll get, we'll just get an emission and we'll plug it right into here.
[14:43] So let's head into shading.
[14:45] Now we can view this.
[14:46] So we have an attribute.
[14:47] So we need to get an attribute node in the shading.
[14:49] Its name is S and we can plug factor into color.
[14:55] And then if you want, you can go ahead and get a color ramp.
[15:00] If you plug a color ramp into this, you can start to kind of edit how this looks with the color.
[15:08] You can give it like a blue here and then over here, maybe we can go with like something like that.
[15:15] And then now you can get a mix of color when audio is moving around and you have your differences in amplitude.
[15:26] So it's really cool.
[15:28] It's very fun.
[15:29] You can make this glow.
[15:31] You can add some noise.
[15:32] I mean, I'll have a lot more tutorials on this in the future.
[15:36] So this is not the last time we'll be able to make something really cool with this, but hopefully you got something out of it.
[15:42] So there you go.
[15:43] That is a mildly long winded description on how to use this node.
[15:48] The possibilities are much larger.
[15:50] There's a lot more to do with this.
[15:52] There are maybe one or two videos on YouTube about this now.
[15:56] They're on a whole lot of videos yet.
[15:57] So I wanted to put out a video for you guys here in my channel if you want to get a baseline of how to use it before we start using it really creatively.
[16:03] So with that being said, hopefully you enjoyed it.
[16:06] Hopefully you got something out of it and I'll see you in the next tutorial.



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
