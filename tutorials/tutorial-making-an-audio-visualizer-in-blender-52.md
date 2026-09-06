---
title: Tutorial: Making an Audio Visualizer in Blender 5.2
source: YouTube
url: https://www.youtube.com/watch?v=kO_vPohvF-k
author: Ducky 3D
ingested: 2026-09-06
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/tutorial-making-an-audio-visualizer-in-blender-52/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: []
---

# Tutorial: Making an Audio Visualizer in Blender 5.2

**Source:** [YouTube](https://www.youtube.com/watch?v=kO_vPohvF-k)
**Author:** Ducky 3D
**Duration:** 21m5s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py tutorial-making-an-audio-visualizer-in-blender-52 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Alright, how's it going guys? So in today's tutorial, we are going to be making this audio visualizer right here.
[0:06] Music
[0:14] So it's got a bunch of moving parts, you can see a pretty complicated screen set up here.
[0:18] It's going to begin by just setting up the style and the look in geometry nodes.
[0:22] Then we're first going to animate the moving part of the material.
[0:26] Then after that, we are going to set up the audio reactive aspect of this animation, combine the two of them and make a really cool animation.
[0:33] This is part of a series of audio visualizers that I'm putting out here on YouTube, so feel free to subscribe and check out more of these.
[0:40] Really quick, I want to shout out the motion graphics course that I just released.
[0:43] It is the third edition of my intro to motion graphics course.
[0:47] It's been updated with a new course structure and a lot more content.
[0:50] The first half is going to teach you all the basics that you're going to need to know in order to make interesting and beautiful motion graphics.
[0:56] And then the second half is going to combine all of that knowledge and show you how to combine those bits to make beautiful animations in Blender.
[1:04] So if you want to check those out, it is 25% off right now with this code.
[1:08] Check it out linked in the description.
[1:10] With that being said, let's get into this tutorial.
[1:12] Alright, we are going to need Blender 5.2 to follow along with this.
[1:17] And I'm just going to pre-warn you there's construction happening next door to me.
[1:20] I may not be able to edit it all out, so hopefully it's not too annoying.
[1:24] But it's not going to stop either.
[1:26] So first off, let's go ahead and hit shift A and get a plane.
[1:30] And then I'm going to go ahead and make my windows now.
[1:33] So we're going to get two windows for now.
[1:35] We're going to make a third in a little bit.
[1:37] So keep this one on the viewport.
[1:38] I'm going to switch this one to the Geometry Nones editor.
[1:41] I'm going to click new and I'm going to delete the input and we're going to get a grid.
[1:47] Get this grid, plug it here and I'm going to go ahead and make it 16 by 9.
[1:56] And then for the faces, make them also 16 by 9.
[2:00] That's going to fill them up really nicely and make them square, which is just the shape
[2:05] that I'm going for.
[2:06] But you can go ahead and make them any shape that you want based on the amount of vertices here.
[2:11] I'm going to go ahead and split the edges so that I can get a scale elements, scale
[2:19] elements node and bring that scale down.
[2:21] And now we are going to have these squares.
[2:24] Now the next thing I want to do, first off, I'm going to make them a little bit bigger.
[2:28] I'm going to get a extrude mesh node.
[2:32] And now we have some extrusion.
[2:34] I'm going to bring it down just a bit and bevel it.
[2:38] So we'll get that mesh bevel node, new favorite node.
[2:41] Give it six segments.
[2:44] I'm going to just keep it at the default bevel.
[2:46] If you want to change it, you can click and drag and change the bevel if you would like.
[2:52] And then last thing, set shade smooth node.
[2:57] And let's go ahead and get a material going as well.
[2:59] So set material right over here.
[3:02] Let's go ahead and grab that material.
[3:06] And then here in the render settings, we're going to go from cycles to EV, the world settings,
[3:11] bring it down to black.
[3:13] And then I'm going to hit the Tilt key, go to the top and get a camera.
[3:17] I'm going to hit zero, G in middle click, bring it up.
[3:21] Now it's going to be a little bit, you can kind of notice that you can see the side here,
[3:25] but the walls here, so it's a bit of a fisheye effect.
[3:28] To completely eliminate that and make this look the way I want, click on the camera in
[3:32] the outline, click camera here and go here to orthographic.
[3:36] And then get that orthographic scale somewhere around there.
[3:40] And then now you can see, you can see the flat part of everything.
[3:42] There is no perspective.
[3:44] So that's what I want.
[3:46] Perfectly flat.
[3:47] You click back on the cubes.
[3:48] We're all ready.
[3:49] Now we just went ahead and basically modeled this whole system.
[3:54] And there's not a whole lot we need to do now.
[3:56] So we'll just leave this alone and create some space over here.
[3:59] And we're going to create two attributes that are going to create the materials that we're
[4:03] going to see that we're going to animate and make audio reactive.
[4:07] So I'm going to hit shift A and get store named attribute.
[4:12] And I'm going to duplicate it.
[4:14] And then just for hierarchy, I'm going to move one here and one there because they are
[4:18] going to need, they are going to need a, their own kind of string of nodes here and here.
[4:25] And that's just going to make it easy to look at.
[4:27] So let's name one song.
[4:29] Of course you can name it whatever you want.
[4:32] I'm going to name this one noise.
[4:35] So let's design the noise first, visualize it in the shading and then make our audio
[4:39] reactivity.
[4:41] So I'm going to go ahead and view this in EV.
[4:44] You're not really going to be able to see anything.
[4:47] So now we can have that.
[4:49] We're going to open up a brand new window and make it the shader editor.
[4:56] I'm going to delete the principle.
[4:57] We're going to get an emission node.
[5:00] Plug it into surface.
[5:02] So now we can see all of this.
[5:04] So again, let's focus on the noise.
[5:06] So let's bring this over a little bit, create a noise texture that we can see.
[5:10] So let's first get a color ramp so we can manipulate it.
[5:14] Bring it here.
[5:16] And we're going to get a noise texture.
[5:20] Plug color into noise.
[5:22] Sorry, plug color into factor.
[5:25] And then let's get a position node and two vector math nodes.
[5:29] So the position node is going to allow us to manipulate this texture with vector math.
[5:34] So get our vector math node and we're creating a mapping node.
[5:37] If you're familiar with shading, so duplicate this and make this one multiply and click
[5:44] and drag.
[5:45] Make it one.
[5:46] Now you didn't see anything happen.
[5:47] Preferably I like to make changes that we can see, helps you learn.
[5:50] So let's go up here in the shader editor, grab an attribute node.
[5:54] If you've never used a store named attribute, we're basically creating values.
[5:59] Black and white, the noise texture is creating a black and white value, but it's existing
[6:02] in geometry nodes and I want to be able to make it in geometry nodes, but view it in
[6:08] shading and that's what an attribute is going to do.
[6:10] So this noise, the fact that we have a material over here, we're calling it noise.
[6:16] You can call it smiley face.
[6:17] You can call it high.
[6:18] If you name it noise, you can plug it into the color.
[6:23] And if I play with this, you can see, okay, we can now see the noise texture.
[6:27] The problem now is I want the values that the noise texture is creating to apply to
[6:35] the faces themselves, which is why we applied it right after the grid before the split edges.
[6:41] I forgot to make a note of that verbally.
[6:45] Create your attributes before you split the edges so that when I change this point to face,
[6:51] it's going to apply that noise and scale it to the faces and it's going to look really
[6:56] nice.
[6:57] So if I switch this over to like 4D, you can see nice.
[7:00] This is a noise texture.
[7:02] So now let's animate this and make it look the way that I have in my original animation.
[7:09] So what we're going to do is bring this, the detail to zero, and that's going to just make
[7:12] the animation look a little bit cleaner.
[7:14] From a scale perspective, I'm going to put 0.35 and then that's pretty cool.
[7:20] Now on the end, the end is going to let you move it left to right, up and down, and the
[7:26] multiply is going to be a kind of scale.
[7:30] So that's going to let you stretch and squash the material.
[7:34] And so my settings that I did was 0.2 here and 4 here.
[7:41] So now when we animate it around, you get some really, really cool stuff and it makes
[7:45] it a bit obvious that this is a texture, this is a material.
[7:49] There are things that are gradient to it that you can see and appreciate.
[7:55] So now we can move this around again, the multiply, leave it, we're not going to animate
[7:58] the multiply.
[7:59] We will, however, animate this ad.
[8:01] So I'm going to animate this with a scene time node.
[8:06] So scene time, we're going to plug seconds, but we can't plug seconds in the vector because
[8:14] it's just going to, it's going to go haywire.
[8:16] So we need to do a combine x, y, z so that we can plug it specifically into the x.
[8:24] Now it's going to move.
[8:25] It's a little too slow for me.
[8:27] So in order to control it, you get another math node set to divide.
[8:34] And then the smaller this number, the faster it's going to go.
[8:36] So if you do 0.1, it's going to do that.
[8:39] So let's try 0.2.
[8:40] 0.2 looks pretty good.
[8:43] And then I'm going to give myself 5000, 5000 frames.
[8:48] We haven't introduced music yet, but that's okay.
[8:50] So we now have this animating forever over 5000 frames, and it looks really cool.
[8:59] Let's go ahead and animate the material itself.
[9:03] So let's bring up the shading, the emission on the shading.
[9:07] And let's go ahead, get a mixed color node.
[9:12] Plug the factor into the factor, make a black, keep b white.
[9:19] We're going to get a layer weight node and plug facing into b.
[9:24] And let's get a color ramp and do a quick little hack.
[9:27] I like the, I like the layer weight.
[9:29] I like what it's doing.
[9:31] However, I want this to be gray.
[9:33] I want these to be white.
[9:34] So you can just get a color ramp and switch it to b spline.
[9:37] It's going to kind of wash it out.
[9:40] And it's going to look really nice.
[9:41] So this is how we have it now.
[9:43] It gives a little bit of depth.
[9:45] The layer weight creates this edge effect, and we really like that.
[9:48] So now that we have that, we can do one more mixed color.
[9:51] So I'm just going to duplicate this and plug it here, plug that into the factor.
[9:55] And we're going to get, we're going to get a color ramp, plug it into b, and a noise
[10:03] texture, and then plug factor here.
[10:08] And then you'll see, we have some cool stuff.
[10:11] I'm going to be my detail to zero scale up.
[10:14] And then this is how you can incorporate more than one color and sort of wash it across
[10:20] a scene.
[10:21] So we'll get a nice color here.
[10:22] This is a really dark scene right now.
[10:24] So let's just bring up that brightness.
[10:26] And then you can get another color that's representing this, these dark points and go with like kind
[10:32] of green.
[10:33] And now you have two colors animating in the scene.
[10:38] Now there's no compositing it.
[10:40] We'll do that a little bit later.
[10:42] So right now we have a nice looking scene and it's animating through.
[10:45] We have multiple colors.
[10:47] Do whatever color you want.
[10:48] Now let's create some audio reactivity.
[10:52] Arguably the coolest part of this whole tutorial, the part that I like the most.
[10:55] So I'm going to just move the shading over a little bit.
[10:58] And let's create the store name attribute.
[11:03] That's going to create our song.
[11:04] So let's get a sample sound frequencies node.
[11:09] So I'm going to bring my cursor back to frame one.
[11:11] I'm going to go here to the video sequencer, hit this drop down and click scene.
[11:17] Make sure it frame one.
[11:18] I'm going to go ahead and add sound and then go ahead and grab a song.
[11:22] I'm going to get a song that I use Epidemic Sound for all my video editing.
[11:27] So I'm just going to get a song.
[11:30] Hopefully you guys can hear that.
[11:32] So that we are using that song.
[11:34] Cool.
[11:35] And then you can bring this down and remember I got 5000 frames.
[11:38] I think the song is more than 5000 frames.
[11:41] Looks like it's like close to seven, seven and a half.
[11:48] So that's cool.
[11:49] Now let's just minimize this.
[11:51] We don't really need to see much of him.
[11:54] So sample sound frequencies.
[11:56] We can go ahead, hit this drop down, grab the song.
[11:59] Let's plug a color amp into the value and then plug amplitude into factor.
[12:09] We are really losing a lot of space here.
[12:11] So let's get a scene time node and plug seconds into time.
[12:18] So we don't have to key frame that.
[12:19] It would be kind of ridiculous.
[12:20] What I'm going to do is scatter the values that the sample sound frequencies node creates
[12:28] with a noise texture.
[12:30] So let's go ahead.
[12:32] Let's get a noise texture.
[12:35] Let's get a map range that's going to help us stretch out all those frequencies and let's
[12:40] get a math node for our high end.
[12:44] So plug a result in here value 100.
[12:48] Plug the factor into the value that I'm going to click normalize and then plug this into
[12:54] high and plug result into low.
[12:59] Now these, this next thing I'm going to type in, I can't explain.
[13:03] I'm not a musician nor am I an audio engineer.
[13:06] I just know these are the frequency frequencies that work for this.
[13:11] Feel free to educate me in the comments.
[13:13] I would love to know.
[13:14] So 15,020.
[13:19] So this, I think this is your low and this is your high from a frequency standpoint.
[13:23] These two right here are going to allow you essentially in this context, this one is going
[13:29] to show how much low end the higher the number, the more low end values that will be created.
[13:34] So how much more reactivity in the values.
[13:37] And then this one's going to allow us to see how much low end.
[13:40] So when you hear like a kick drum, we can go how much of that low end kick drum can
[13:45] we see and we'll, and I'll show you how that works, but that's what we're kind of thinking
[13:49] about here.
[13:50] This will not change.
[13:52] This is the paintbrush right here.
[13:54] So we're done on this.
[13:56] I'm going to give it on the noise texture.
[13:58] I'm going to give it a detail of zero and a scale of three and we're going to make it
[14:02] for D because we are going to animate it a little bit later.
[14:05] So let's go ahead, bring the shading window back.
[14:09] And we have a brand new attribute to look at.
[14:11] So let's go ahead, grab this attribute.
[14:14] I'm going to duplicate it and I'm going to type in song and then don't follow along here.
[14:20] You can if you want to, if you have the node Wrangler, I don't want to enable hit control
[14:23] shift click.
[14:25] Okay.
[14:26] So it's working.
[14:28] That's awesome.
[14:29] Now it is not assigning it to the faces.
[14:33] So go to the attribute that's called song and switch it to face.
[14:39] So there's a couple of things I want to do too much low and see everything that's bright.
[14:44] You can see when that kick drum and the song, that's, it's overwhelming and it would make
[14:49] the scene not look good from a design perspective.
[14:52] So what I'm going to do is in geometry nodes, the attribute called song, I'm going to find
[15:00] the map range.
[15:02] And in my settings, I did negative point one and then a max of point five.
[15:13] And then honestly, I want even less than that.
[15:18] Cool.
[15:22] And then again, the more of this guy, the more, so let's go back here.
[15:35] All right, cool.
[15:38] It looks great.
[15:39] So now we have some values that we can plug into the shading.
[15:43] So what are we going to do?
[15:45] Let's forget about geometry nodes, the geometry nodes here, we're just going to move that
[15:50] over.
[15:51] Let's plug the emission back into the surface so we get this beautiful scene.
[15:54] And we are going to plug in fact, there's too much.
[15:59] I want more negative space.
[16:01] So let's go back to the noise texture that's plugged into the noise attribute and bring
[16:04] this in a little bit.
[16:08] That looks a lot better.
[16:10] Okay.
[16:11] So the attribute that we were just looking at the audio reactive attribute is going to
[16:16] be plugged into the strength.
[16:18] So what that's going to mean is every time one of these faces that has that attribute
[16:23] assigned to it is going to control the brightness.
[16:26] So let's go ahead, take the song attribute and we're going to plug the factor into the
[16:31] strength.
[16:32] It's going to disappear.
[16:34] It's just not strong enough.
[16:35] You can see a little bit in there.
[16:37] So let's go ahead.
[16:40] Let's go here.
[16:41] Let's go to a spot that has some kick.
[16:42] So I go back here.
[16:46] Okay, cool.
[16:47] Let's get a map range.
[16:49] This map range is going to control the brightness.
[16:53] The maximum is how bright it gets in the minimum is how, what is the brightness of the darkest
[16:59] part?
[17:00] So let's bring that max up and I'm going to bring that minimum up a little bit.
[17:03] And this is the part where we can introduce a little bit of compositing because when we
[17:08] start to get things to glow, that is going to be like the most intense, uh, loudest part
[17:13] of the song.
[17:14] So we'll be able to look at the glow in context to the audio as, as we're editing it.
[17:21] So let's go ahead and add some really cool compositing.
[17:25] So get a new window, get the compositor going.
[17:28] I'm going to click new.
[17:31] I'm going to get in a fog glow.
[17:36] Give it a strength of three.
[17:39] And then let's get a, and then now let's go ahead.
[17:42] I'm going to, right over here.
[17:43] I'm going to hit this drop down and click always so we can see, okay, a little bit of
[17:47] glowing is happening.
[17:48] I'm going to show you guys how I like to do fog glow and blender.
[17:52] Well specifically in EV is I'm going to bring the size.
[17:56] First off, I'm going to make the brightness a little bit more.
[17:58] We can see some glowing here.
[18:00] Let's see if I can find a spot in the song with more.
[18:06] There we go.
[18:07] That looks really good.
[18:08] So I'm going to bring the size farther down.
[18:09] So we get one glow that's really, really tight to the objects.
[18:14] And then we're going to get another fog glow.
[18:18] That's a little bit bigger and wider spread.
[18:20] So give it a strength of three, just like this one.
[18:22] And then the size be pretty big.
[18:26] So now we go, okay, looks great.
[18:29] Honestly looks horrible.
[18:30] So we can bring down a little bit that max.
[18:34] Now it's going to lag pretty aggressively.
[18:37] So we need to bring both of these to a quality of low.
[18:42] You can change it when you're done editing.
[18:46] So here that looks like that's the brightest it'll go.
[18:51] So I'm just going to bring the max up a little bit.
[19:01] Okay, so for me at this point in the song, there's just not enough of these low end
[19:07] glowing kick drums.
[19:10] So what I'm going to do is on the map range in the geometry notes workspace that's controlling
[19:14] the sample sound on the map range on the from minimum, I think this top slider, I'm going
[19:23] to give myself more.
[19:25] Maybe a few more now.
[19:31] Okay, that looks awesome.
[19:35] We're almost done.
[19:36] First thing I'm going to take a film grain node.
[19:38] I'm going to put it here.
[19:39] It's going to get really grainy.
[19:41] I'm going to go from super eight to 70 millimeter cinema animated.
[19:46] So that's going to give it a little bit of a gritty look, make it look a little bit more
[19:48] natural.
[19:50] This minimum here on the map range that's connected to the emission, I'm going to bring
[19:54] that up so that the other objects are a little bit brighter.
[20:02] I think these colors are kind of lame, but we can live with them for now.
[20:07] So there we go.
[20:08] We have that.
[20:09] We are pretty much done with this tutorial.
[20:12] You can now make tweaks and changes as you would like to.
[20:18] I'm going to go here to my camera, bring my orthographic scale out a little bit more.
[20:22] Fog glow, we can go from low to medium on both of these.
[20:27] And then, yeah, we can maybe bring that from max down a little bit as well.
[20:32] And there we go.
[20:33] We now have a beautiful, a bit laggy, but audio reactive.
[20:42] And there you go.
[20:43] You have something pretty cool that I hope you can walk away with and make something
[20:47] really neat with.
[20:48] So there you go.
[20:49] Hope you enjoyed it.
[20:50] Hope you learned some stuff that you can apply to some other animations and make some
[20:52] really cool audio visualizers.
[20:54] Again, check out my course linked in bio.
[20:57] And for those of you on Patreon, this project file is available to you right now.
[21:00] So if you want to check that out, all that stuff linked in my bio.
[21:03] I'll see you guys in the next one.



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
