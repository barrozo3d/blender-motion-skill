---
title: Can Blender Still Compete (Motion Graphics)
source: YouTube
url: https://www.youtube.com/watch?v=bDHdUT2oiZE
author: Ducky 3D
ingested: 2026-09-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/can-blender-still-compete-motion-graphics/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: []
---

# Can Blender Still Compete (Motion Graphics)

**Source:** [YouTube](https://www.youtube.com/watch?v=bDHdUT2oiZE)
**Author:** Ducky 3D
**Duration:** 19m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py can-blender-still-compete-motion-graphics <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Five years ago, I made a video on if Blender can be used for motion graphics.
[0:03] Now, being able to say yes to that question has gotten a lot easier with the way that Blender has
[0:09] developed. With where Blender is at right now, I think it's a lot easier to answer that question
[0:14] by now comparing it to something that's considered an industry standard like Cinema 4D.
[0:19] So what I'm going to do today is show you how to remake a really cool render that has made Cinema
[0:25] 4D. And from that, you can decide how that workflow might be able to fit into the toolset that
[0:30] you want to have with your own work. The original artwork is made by Tendril Studio, which is an
[0:36] incredible studio. I've been seeing their work for years. They make amazing stuff. So I'm going to
[0:40] link them in the description, check them out. They're really, really cool. So a full credit goes to
[0:44] them. In my opinion, the biggest problem that Blender has right now with being as good as something
[0:50] like Cinema 4D is that it doesn't have a dedicated MoGraph workspace like Blender has with sculpting
[0:56] or shading or even simulations. So as a motion designer specifically in Blender, you really have
[1:01] to be good at learning a ton of different tools and then being able to combine those and make
[1:07] really cool animations. I just released a course that shows you exactly how to solve that problem.
[1:13] It's eight and a half hours long and it's 25% off for the month that it is released. The first
[1:19] half of the course is going to teach you the fundamentals, all those different tools in Blender
[1:23] that you would need to combine to make really cool animations. And then the second half takes
[1:28] those fundamentals and applies them to 10 separate animations. If you want to check that out, it is
[1:33] linked in the description and you can use this code to get 25% off at checkout. With that being said,
[1:38] let's get into this tutorial. So again, this is the image that we are going to be remaking. The
[1:43] biggest hurdle to getting this to look pretty close to it is figuring out how to get all those
[1:48] intersecting like cubes to look like they're melting together. And then the material is pretty
[1:53] straightforward. We're just mixing glass and like a principled. And then the background,
[1:56] the lighting, we're going to deviate a little bit. Just wanted to have some fun with that. But
[2:00] the melting is what we are going to attack here in Blender first. So we're going to be in Blender
[2:06] 5.2. I'm going to go ahead, just get a piece of geometry to start it out with. Let's head to
[2:10] geometry nodes. Let's click new. Let's delete the input and get a grid. So we're going to take this
[2:18] grid. I'm going to scale it. We'll do 10 by six and give it about 15 on the vertices. Now let's go
[2:27] ahead and displace it. So we're going to get a set position node. We're going to get a vector math
[2:34] node. And we're going to set that to multiply so we can strengthen the displacement that we add it to.
[2:39] And then let's get a noise texture for the displacement. So grab this plug factor into
[2:45] vector and then bring that up and make sure you normalize it. So now we can displace all of those
[2:50] cubes and get them to kind of randomly go up and down. This is a pretty simple design aspect of this.
[2:56] Now we're going to do is get a, going to distribute points on faces node. So now we have all of these
[3:03] points. We're not going to need this many. I'm going to go ahead and copy my scene. I'm going to do
[3:06] a 2.4 on how many points we need. And let's do an instance on points to actually add those cubes.
[3:13] Instance on points, search up a cube and we'll plug that right into the instance. Now we have
[3:20] all these eyes. We'd actually melt this now. They're all intersecting. That's really what we want is
[3:24] cubes that are intersecting, but I want to add some design. I want to randomize the scale with them
[3:28] and they need to be stretched out quite a bit. I'm going to highlight these and hit G and move them
[3:32] up. Let's go ahead and get a combined XYZ node, plug it into the scale, and then you can just go
[3:39] ahead and get them all back to be one. Let's go ahead and get two random value nodes. We need to
[3:45] add a random value node to their thickness and then a random value node to be how tall they are.
[3:51] So just go ahead and throw that one in there, duplicate the random value, put it in the Z,
[3:56] and then first let's go ahead and randomize how big they're going to be. And then we can go ahead
[4:01] and randomize how tall they're going to be. And now we get this right here. Now I mentioned intersection
[4:07] is what I'm going for here. So what I don't want is any of these to be a value of zero. So get the
[4:13] value of zero. So get the ones that are a value of zero, just kind of stretch out a little bit,
[4:18] and then also on the width or the thickness, bring that up as well. So we can do something like that.
[4:27] And now we have something that looks pretty good. We have a good amount of density here.
[4:31] I'm going to go ahead and now get a delete geometry node and set it to instance.
[4:39] We're going to get a random value node and set it to Boolean. So we just get a slider and plug
[4:43] that into selection. It is going to randomly delete some of our instances. So we can have some,
[4:48] so we can have a little bit of control of the density over here just as a single slider. And
[4:52] you can make that decision if you want. You might want the design to breathe a little bit. It really
[4:57] just depends on what we are going for for your final animation. So now I'm going to go ahead and
[5:02] set up my camera before we do any more modeling. Because usually at this point is where I'm starting
[5:07] to think about composition. So I'm at the tilde key and go to the front, get a camera. I'm going to
[5:12] set the focal length to 100, which is kind of insane. But I do like how it looks. I'm going to hit
[5:18] G in middle click, move it out. And then we can start to hit R twice and point this guy.
[5:31] However, I think might look cool. And then we can start to again stretch it out.
[5:38] Maybe scale it up. And then here on the displacement, I'm going to stretch that out as well. I want a
[5:44] couple of these guys to kind of poke out adds a little bit of contrast to the scale and the size
[5:50] and everything we're kind of looking at. There we go. We've now got a bunch of sticks that are
[5:55] intersecting that we can now melt together and make a really cool effect. So how do we do that kind
[6:00] of melting effect first? In order to do it first, we're going to need to realize all these instances.
[6:06] So we just get a realize instance node and it's going to remove the ability of anything out here
[6:10] to recognize that these are individual objects, it's going to treat them like one big object.
[6:14] So now we're going to get a mesh to SDF grid. This is a pretty new node. You may have not seen it
[6:20] before. And then we're going to do a grid to mesh so we can convert it back from an SDF to geometry
[6:26] information. So we'll get a grid to mesh node plug that there and plug that there. It's back.
[6:34] Now as we essentially converted it to a volume so that all those intersected pieces are just sort
[6:39] of connect to each other, molded to each other. And then the voxel size, be really careful when
[6:45] you're bringing that value farther down because this is essentially a subdivision and it can get
[6:50] heavy incredibly fast like it's doing right now. So it also does add this sort of natural bevel
[6:56] to the sides as well. And then you can do a set shade smooth. And now we are done. This is the
[7:04] melting effect that we want to achieve from the reference from tendril looks pretty cool. Again,
[7:11] it's not an exact there's has a little bit. There's looks like it has a few less objects,
[7:16] has a little bit more room to breathe. Mine's a good bit more dense, but we're getting pretty close.
[7:22] I'm going to go ahead and scale this down and then bring it up. So we can kind of appreciate
[7:27] all of the geometry that we're dealing with here. Something like this. Nice. So this is what we're
[7:33] doing now. Now we're going to go ahead and light it and shade it. Now this is a pretty heavy scene.
[7:38] So what I'm going to do is I'm going to bring this down, bring this down and bypass
[7:43] all of that melting. And we can just worry about shading it and then we can look at it as a melted
[7:48] object as we go, but it's going to bog your scene down. So first, let's go ahead and get a set
[7:53] material node right over here, create a new material and then grab it in that node. And now we can
[8:00] head over to shading. So let's go here to the shading. Just like that. I'm going to view it in
[8:05] cycles. You can totally view it in EV though the final render will be in cycles. So I'm going to
[8:10] grab this here and then hit the dropdown scene, world scene lights. So we don't have to import
[8:14] a light just yet. Now what we need to do is combine a glass material with the default
[8:20] principle BSDF. And we're going to bring that roughness down, make it nice and shiny. So what
[8:24] we're going to do is get a mix shader node. So what we're going to do is get a mix shader node.
[8:33] We're going to get a glass BSDF and plug it right there. So now we have some glass and we have just
[8:41] like we'll call it plastic. And then here on the glass, I'm going to bring just a little bit of
[8:46] roughness just to tad to make it feel a little bit better. Let's go and now get a color ramp and
[8:52] a noise texture. So color ramp, noise texture. And then I'm going to hit control T if you have the
[8:58] node Wrangler add on enabled comes with blender by default. And I'm going to use the object coordinate,
[9:02] plug the factor here and plug the color into the factor. Now they're mixing together. So if you
[9:08] bring this in like that, bring this in like that, you're mixing those two things together. Now it
[9:12] looks like ship camouflage. So we're going to scale that noise texture up, bring that value down.
[9:19] And then there we go. Now we have nice material mixing together. And you can decide how you want
[9:28] that material to look the higher the farther apart these two, the smoother that is going to look.
[9:34] So you can kind of make that decision how you want it to behave. Mine are going to be about
[9:40] separation about that much. And then 3d switch it to 40 on the noise texture. So you can play
[9:46] with the seed and decide where do you want that plastic and that glass material to show up. However,
[9:52] we will be animating it on the Z. So it doesn't really matter. It's going to move. All right,
[10:00] now let's go ahead and tackle the lighting, which is one of my favorite parts of this.
[10:05] So first, let's do the background. I'm going to go back here to a shade flat shaded view
[10:09] and go here to the layout. I'm going to hit shift A, get a plane, and I'm going to hit Rx90.
[10:19] Bring that plane far enough back to where there's a decent gap. I'm going to go here to the camera
[10:24] view. I'm going to scale this up like this and then scale it here. I'm going to hit control A and
[10:31] apply that scale. And then I'm going to hit shift A, empty plane axis. And we're going to use this
[10:38] to control the gradient. So bring that plane axis close to the plane, though it's not an exact
[10:44] science, it will control how big and small our gradient circle that we're going to add next is.
[10:49] So let's head back to shading. I'm going to go here to cycles. And then I'm going to click on
[10:55] scene world scene lights, make sure that we're in the default lighting setup, which is no lights
[10:59] right now. So click on the plane in the shading editor, I'm going to click new, delete the principle.
[11:05] Let's get a emission node, plug that into the surface. Now we have something that looks pretty
[11:09] cool already. I'm going to give it a strength of 30. Looks pretty nice. Now we're going to get a
[11:14] gradient texture and very important hit control T or search up a mapping node, texture coordinate,
[11:20] use the object coordinate and grab the empty as your object, plug color into color and switch
[11:27] linear to spherical. And if you click on the empty over here in the outline, hit S, you can start to
[11:33] see a nice gradient. I'm going to hit, I'm going to click on the plane, hit control A and apply
[11:37] that scale. I can't remember if I already did. Now normally this is the part where I add a color
[11:41] ramp to make the gradient smoother. I have recently learned if you get a math node,
[11:47] switch it over to power, that math node can actually be the thing that smooths out the gradient. It's
[11:55] a much better way than using a color ramp that switch over to B spline because it's pretty limited
[12:00] and I've never actually enjoyed using it. But if you bring that exponent really high and then play
[12:06] with the empty, you get a really, really nice gradient and then you can just scale it up to
[12:12] something like this. And then to add color, I'm going to get a mixed color node, plug the power
[12:17] into the factor A, zero, B, whatever color you want this background to be. So I'm going to do
[12:24] something like this. And now we have a nice background. You can bring that strength up if you
[12:29] want anything you want to do. Now this guy has no lighting on him. And you can see, you can still
[12:36] kind of see some detail, that's because the world brightness is gray. It needs to be black. So now
[12:41] we have something that's actually pretty cool like that. Before we add a light, I do want to go back
[12:47] to geometry nodes, look at the render and actually, actually possibly delete here on the random value
[12:54] right above the delete geometry, possibly delete a few so that we can get the glass to kind of
[13:00] see through some of this light. So if you bring very few, you start to see something like this.
[13:08] I'm going to make a couple changes. So I'm going to bring this down a little bit.
[13:14] And then I'm going to bring up the max size to something like this. I just want to be able to
[13:19] see a little bit of glass. And then I'm going to bring up the random seed of the random value that's
[13:26] just editing the length of this guy. I'm going to hit G and move it up. That should add nice. So I
[13:33] want to be able to see some of a little bit more of the glass. So let's go ahead and add a light.
[13:38] So let's go to the layout, go here to the render, I'm going to hit shift A, light, area light, and
[13:45] then I'm going to hit G and bring it up so that it's going to hit it at an angle. So G and then
[13:50] I'm going to hit R twice to point it right at my object. Here in the light settings, I'm going to
[13:58] bring it from a square to a disc and then hit S to scale it up. And then what you can do is just
[14:04] bring up the exposure. And there we go. Now we have this. I'm going to bring down that spread a
[14:10] little bit so that we have this nice fade right here. And then you can play with how the light
[14:16] is going to affect it. One of the really great, great trick is if the gradient is here, the dark
[14:21] portion of the gradient is here, light it there and then leave some negative space where you're
[14:26] not going to light it where the lit part is. So you get this really interesting balance of values
[14:32] and it's a really beautiful modern look. So now I'm going to bring that exposure down a little bit,
[14:36] something like this, and then I'm going to hit shift D and have this light
[14:43] hit it, hit the back of my object. Sorry, I was really zoomed out and I'm going to scale it up
[14:51] so that now we get a really nice, what do you call it, like a key light. Just want to hit some
[14:58] highlights here in the back and then you can bring up the brightness a little bit as well. So now you
[15:02] get a really nice look here. Now it doesn't look that great. Let's go back to geometry nodes and
[15:08] add the set shade smooth to the set material so we can look at it as the melted part of the render.
[15:16] So it doesn't look too bad. Maybe we can bring back some of those deleted objects. It's going to be
[15:21] really heavy. So I'm going to bring my density from like 2.4 to like 2.6, maybe 3.
[15:29] Maybe add some density.
[15:37] And then maybe I can rotate this guy a little bit too, just adjusting my composition as we go.
[15:43] So now all we need to do is animate this material. I'm going to do it in EV
[15:49] or the material preview section. We can go here to the shading and I'll show you how
[15:53] to animate this material. Of course, it's going to be done in the location right here. But first,
[15:59] see how that looks. We could animate it like that. It could look fine. The shape of the noise just
[16:05] doesn't change or move and that's a little boring and kind of lame. So what we can do to kind of
[16:11] disrupt how stagnant that material moves is just go ahead and get a mix color node.
[16:19] We're going to set it from mix to multiply. And then all I'm going to do is just duplicate this
[16:26] noise texture, duplicate this mapping and plug the object into it and then plug that into the vector,
[16:32] plug that here. And then I'll just need to go and readjust my color amp because that's going to
[16:37] change some things. But what's going to happen now is if I bring the multiply over to something
[16:43] like this, again adjust your color amp because it disrupts, is when I go ahead and take this mapping
[16:50] node, which is not this mapping node, very important for the movement, when we move that around,
[16:55] now the noise texture is going to move rather than not moving at all. So you just get a subtle
[17:00] movement and I just think it's better. I'm going to go back to the cycles preview just to make sure
[17:05] I'm getting enough glass in my scene. And that's really, really important to make this look really
[17:13] cool and highlight that this is a mix of glass and principled. And then now all we need to do is loop
[17:21] this movement. So again, I'm going to go back to EVE. So in order to loop these, what we're going to
[17:26] do is I'm going to go ahead, this noise texture, this mapping node, I'm going to hit control shift,
[17:30] D, duplicate the textures, not just the mapping node, we're going to get a mix color node.
[17:37] And I'm going to plug, keep this factor on B, plug the factor here into A. Again, go here.
[17:44] And then again, in your edit, your preferences, make sure that in your animation tab, your default
[17:49] interpolation right here is linear. Otherwise it won't loop here on the mix, bring the factor to the
[17:54] left, hit I, here on the mapping right here, where it says Z X Y Z on the location, hit I there,
[18:00] go to the end, bring the factor to the right, hit I on the Z of our mapping, 25, hit I. Now that we're
[18:08] at the end of the timeline, I'm going to hit I on this, go to frame zero and do negative 25, hit I.
[18:15] And if we press play, we're going to get a very slow motion. I'm going to go look at this in cycles.
[18:21] And it is moving really slowly. If you want to be quicker, right now we're using a value of 25
[18:25] and negative 25. If you want to be faster, try like a value of 60 and negative 60.
[18:31] I do prefer the slower motion. I think it's more satisfying. So if we go back here to the layout,
[18:38] let's just go ahead and see how it looks as a final render as a final image. This
[18:43] is what we're going to get. I think it's really cool. It's really beautiful. Again,
[18:47] shout out to Tendril Studio for the design that I'm basically copying. So go ahead and check them
[18:53] out. It's a really, really cool design. We are finished with this animation. If you want to look
[18:58] at my render settings, my samples are at 300. I'm just doing a regular D noise rendering at 1080p,
[19:03] render, render animation, and then export it out to any file you want. So there you go. The question
[19:10] is Blender, an industry standard for motion graphics, is an incredibly hard question to answer.
[19:15] It's not a black and white yes or no, but hopefully looking at it like this going,
[19:20] hey, this animation was made in Cinema 4D. Can we duplicate it in Blender? And what does that
[19:25] workflow look like? Because really the end result doesn't tell the whole story. What's the workflow?
[19:30] So does that workflow fit with the studio, fit with freelancing? Yes or no? Let me know in the
[19:35] comments. But that is it. Again, if you want to check out my brand new course that is linked in
[19:39] the description. And again, you can get 25% off. I hope you enjoyed this tutorial. There's more to
[19:44] come. See you in the next one.



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
