---
title: Beginner Geometry Nodes - Helix Twist [Blender Tutorial]
source: YouTube
url: https://www.youtube.com/watch?v=Y4qk49lryRk
author: Seanterelle
ingested: 2026-07-28
blender_version: "Blender 5.2.0 LTS -- observed in frame_000"
tags: [geometry-nodes, procedural, animation, materials, shaders, rendering, cycles, motion-design, abstract, organic, beginner]
extraction_status: complete
frames_dir: tutorials/frames/beginner-geometry-nodes---helix-twist-blender-tutorial/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Beginner Geometry Nodes - Helix Twist [Blender Tutorial]

**Source:** [YouTube](https://www.youtube.com/watch?v=Y4qk49lryRk)
**Author:** Seanterelle
**Duration:** 26m1s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello, today we're going to be making this Helix Twist animation in Blender using geometry nodes.
[0:05] The setup is pretty simple, so it's good for beginners and without further ado, let's get into it.
[0:09] Go ahead and open Blender, A to select all, X to delete, and then Shift A to add in a new default cube,
[0:15] and then drag out over here to create a new pane and go into the geometry node editor
[0:20] and hit New to create a new geometry nodes network.
[0:23] First, we're just going to create our basic shape, so we'll need a curve line.
[0:27] That's just going to be a straight line going up like that.
[0:31] And then we're going to want to do Curve to Mesh,
[0:37] and we're going to create a bunch of Helix lines that are going to end up being curves, which we then mesh at the end.
[0:44] And so the way that we're going to do that is use a Curve Circle,
[0:48] and let's set it to 6 because we're going to want 6 individual helixes going around this line,
[0:55] and press 5 to go into Orthographic Mode on your numpad.
[1:00] Then what we're going to do is, if I just put this into the Profile Curve, we'll get this Helix.
[1:06] We can set the scale down to something a lot smaller,
[1:10] but I just want these individual points because I just want these vertical lines.
[1:14] And so the way that we're going to do that is we're going to actually do Curve to Points.
[1:22] So we get the points, but then nothing happens because the input to this Profile Curve needs to be a curve.
[1:28] And so we're going to do Points to Curves,
[1:33] and then this will give us basically what we had before.
[1:36] We need to make sure to set this to Evaluated, except for we're missing that edge.
[1:41] But if we use this Curve Group ID, we can actually get individual curves for each of the individual points that we have in this Curve to Points node.
[1:51] So what we'll do is we'll just use the index as the Curve Group ID.
[1:56] And now we just have those vertical lines.
[1:58] To create the Helix, we just want to take this Profile Curve and then have it sort of spin around that center curve that we created in the beginning,
[2:07] the curve line that we created in the beginning.
[2:09] And so the way we can do that is by controlling the twist of the curve line.
[2:13] So if we set Curve Tilt, controlling the Tilt,
[2:20] we'll set that there.
[2:21] So if I move that tilt around, you see how everything rotates.
[2:25] And so we'll want to set that tilt based off of the point along this original curve line.
[2:32] And that point along that original line is called the Factor.
[2:37] And we can do that in the Spline parameter.
[2:40] But actually, let's do it by length so that no matter how long this is,
[2:45] we always get the same amount of spiraling or spinning.
[2:48] And we'll multiply that length by some number.
[2:52] And you'll see that it's not really working.
[2:54] And that's only because we have these two points at the beginning of the end.
[2:58] So we'll need to pop in a Resample Curve node that will add points to the curve.
[3:04] And we'll set that to length and something pretty small like 0.001.
[3:08] So now we get this Helix and we can control how much it spins around.
[3:14] And then if I change the length, the spin stays the same.
[3:19] If we had set this to Factor and I moved that up,
[3:22] it would change the amount of rotations per unit of length.
[3:27] Now to make this sort of wrap in on itself,
[3:30] we can also control the curve scale based off of the parameter.
[3:37] So if I put that factor in there,
[3:41] then what you're going to have is it'll get larger to the end.
[3:45] It'll be 1.00 and it'll be 0.00 at the beginning of the curve line here.
[3:51] And so what we want to do is map this so that it looks like sort of like this curve,
[4:00] which brings everything together and then animate the point at which it goes from being farther out to being closer in.
[4:09] So the first thing that we can do is we can do a map range node.
[4:16] And so we'll just take this value and we're mapping from the minimum that this value is to the maximum
[4:21] that this value is to this new min and max.
[4:24] So this is 0.001 and so instead we'll do let's say 1.00 to 2.00 and we'll set the original scale of this.
[4:37] Well, yeah, let's set this to like 0.1.
[4:41] So we can go like that.
[4:44] And then if we add, you can see that the point at which it comes together changes.
[4:53] And this is a little abrupt.
[4:56] So what we'll do is smooth it out using a power node.
[5:02] You can just set that to something a bit larger.
[5:07] And if we change this max to something larger than that, then it'll move farther out.
[5:13] The higher we set the power, the more abrupt the coming together of the curves will be.
[5:20] So we can do something like that.
[5:22] Maybe you can kind of see this coming together.
[5:28] And I'm going to go up here and I'm going to set this to be negative 5.
[5:34] So that, actually, I think I want it to be positive 5.
[5:38] So as it comes together, you get that curve.
[5:43] Now, you'll notice that the size of everything, I can unclamp that if I want, but it's really,
[5:54] gets really big.
[5:55] And that's going to be odd when we do the meshing because it's going to stretch everything out.
[5:59] And if we want to put any sort of like texture onto the material, it's just going to stretch.
[6:03] So what we're going to do is we're going to fit a guide curve to this.
[6:07] So the way that we'll do that is we will make a new curve, it's curve line.
[6:14] We're also going to resample that.
[6:17] 0.001 will work, although we'll probably put that a little bit higher by the end of it.
[6:24] And then we'll want to do another curve to mesh.
[6:29] It's basically the same as this one, except for we're not going to have to worry about setting the scale or the twist.
[6:36] We'll use the same exact profile curve.
[6:39] We put in a viewer node.
[6:42] You can see what we have here.
[6:44] And then what we're going to do is we're just going to sample our source curve with the shape and the animation.
[6:55] At the same length as this curve that will fit.
[7:00] So that along the length, like this curve that we have right here will always stay the same length.
[7:07] And it'll just move along the guide curve based off of its animation.
[7:11] So that's a simple, easy way of ensuring that you'll always have the same length.
[7:14] So we can sample curve and we'll do it by length.
[7:20] And we want to get the spline parameter and use the length of this curve.
[7:29] So this field will run through the sample curve node and use the target output here once we connect this all up.
[7:37] And we're going to set position and we're going to say position.
[7:43] And this won't quite work and I'll show you why.
[7:46] So if I turn off that, nothing is happening correctly.
[7:49] One because this is mesh so we need to convert it back to a curve.
[7:55] And then we also there's multiple splines within this curve and that's what this curve index is doing.
[8:03] So what we're going to have to do is use a curve of, oops, curve of point node set to curve index.
[8:14] And I'm still not seeing anything because I haven't yet converted this back to a curve.
[8:26] And because we use the curve to mesh node here and then this spline parameter means nothing in the context of the mesh.
[8:33] So I just convert it back to a curve and now the length actually corresponds to the length along this curve and we set it.
[8:39] And now we have this.
[8:40] So you can see how it cuts off here.
[8:43] And if I do my animation, it wraps together just how we want it to.
[8:48] So next let's mesh our output curve and then let's tune some of the parameters to get the look that we want and then create the animation.
[8:57] So the way that we'll do that is we'll do another curve to mesh node.
[9:02] Profile curve will just be a curve circle and we'll pop that in there.
[9:08] The radius is going to be way too big.
[9:09] Let's set it in the scale here.
[9:11] So we'll just tune that until it looks pretty good.
[9:15] Let's do point zero five for now.
[9:17] That'll do.
[9:18] And let's fill the caps.
[9:21] So now if we move our little animation parameter in this add node, that looks pretty nice.
[9:27] I kind of want this to be a bit longer though.
[9:29] So what I'll do is I'll lengthen that and let's see.
[9:34] We can just lengthen this curve until we can go all the way up here.
[9:41] Oh, it's reached the end.
[9:42] So this curve actually needs to be a bit longer too.
[9:46] How about that?
[9:46] Let's make it about that long.
[9:49] That looks like some nice candy type thing.
[9:55] Okay, so now we have our basic animation and now we just need to animate it based off of the frame.
[10:02] The way that we'll do that is we'll use a scene time node using frame.
[10:08] You can control H to show and hide parameters that are user unused.
[10:12] When you search and just do frame, it automatically pulls in the scene time with just the frame exposed.
[10:18] And we'll map range because what we want to do is take the frame from let's say zero to something like 250.
[10:30] Just the end of the frame range here.
[10:31] We'll probably do it a bit before and then we'll do it to the min and max that are the start and end locations of our animation.
[10:38] So the start, let's say we can have them come together at the beginning kind of quickly.
[10:43] So we'll start with 0.4 and then we'll go all the way up until it's kind of finished.
[10:52] Let's just do ctrl-c and ctrl-v.
[10:57] So negative 9.6 and if we put that in there, then over the course of our animation of this entire frame range,
[11:06] it'll go from being apart to being folded together or twisted together.
[11:11] But we want the animation to be not so linear because right now it's just a linear animation between these two values.
[11:20] So I'm going to pop in a power node and let's set that to, let's set it way higher.
[11:32] Oh, so one of the problems here is we have clamp set so that this will only go between these two values.
[11:41] So we need to uncheck that.
[11:51] Oh, you know what?
[11:54] I'm going about this all wrong.
[11:56] So actually we should map this to 0 and 1 and then we should use a mix node to mix to, yeah, yeah.
[12:09] Okay, so what's happening here is the exponent on these values is not mapping the way we want
[12:15] because the power node is going to work best on a range from 0 to 1.
[12:20] So instead of mapping range to our min and max values, we'll use a mix node and this will have our min and max
[12:30] and that will be driven by a factor of 0 to 1.
[12:33] So if I put that in here, then you can see you'll use that factor to go there.
[12:38] So if we just map this 0 to 1 and plug that in here and we'll have the same animation that we had before,
[12:45] except now if we use this power node, then we'll want to set this to something like 0.2 actually.
[12:51] That's maybe too much.
[12:53] Then it'll start quicker and then slow down.
[12:57] I'm going to skip through this section because it's really just me figuring out the right tuning for the animation.
[13:02] That looks good and when we come back, I'll go through the parameters that I changed.
[13:07] Okay, so I just tuned the parameters a bit until I got something that I liked.
[13:12] Set that power to about 0.5.
[13:14] I tuned my mix values from this value to this value and I also messed with this power value a little bit.
[13:21] So now it sort of very quickly at the beginning comes together and then slows down and just comes together.
[13:28] I couldn't help myself and I'm tuning more parameters, but now we're just going to skip it and be done with it.
[13:34] Yeah, so that'll work.
[13:36] And you can play with these parameters and tune it just how you'd like.
[13:40] And that's pretty much it for the animation.
[13:43] Now we can do a little bit of setup to prepare it for rendering.
[13:47] So first things first is we need a material.
[13:50] So at the end, we'll set in a, or put a pop in a set material node.
[13:54] We'll just set that to this default material.
[13:57] I'll drag in a new panel up there, shader editor, select that material.
[14:03] And then if we go into cycles, I'm going to set that to GPU and Z to go to rendered mode.
[14:09] And then let's add just the directional light, sunlight rotated a bit just so we can see what we're working with here.
[14:18] And then we'll set the, just set the exposure a bit higher, maybe add in the ground plane and put that down just a little bit.
[14:29] Then we can see what we're working with.
[14:31] I'll add really simple materials to this ground plane.
[14:35] I'll do shift alt Z, which basically just toggles this button for overlays.
[14:41] And you can see everything here.
[14:43] Maybe I'll add a camera with shift A and then view a line view line active camera to view.
[14:51] Then I'll lock into place, move it out.
[14:53] I want this to be really zoomed in maybe like 512 or we could just set it to orthographic, but either way.
[15:03] And then let's set our aspect ratio.
[15:06] We'll do like mobile render here.
[15:07] So instead of 1920 by 1080, I'll be 1080 by 1920.
[15:14] And we'll just zoom in there until it is nice and centered at the end.
[15:22] Looks pretty decent.
[15:27] Then what I'm going to want to do is it's moving really quickly at the beginning.
[15:32] And in general, it's going to look way better if we add in some motion blur.
[15:36] So we can just enable that here.
[15:38] Then when we do a render, we'll get that nice motion blur.
[15:43] Set that out.
[15:43] I don't need my max sample so high.
[15:46] Let's just set these for test render to something like 32.
[15:50] Keep everything else the same.
[15:52] I'd hit use GPU there.
[15:54] Who someone texted me?
[15:56] Okay, render image.
[16:00] Yep.
[16:02] And then what we're going to want to do is just set some parameters in the geometry nodes editor
[16:08] to drive the color and some of the material properties here.
[16:12] So all I'm going to do for that is before this curve to mesh node,
[16:17] I'm going to store named attribute.
[16:22] And this is going to be integer attribute.
[16:26] We're going to have two of these.
[16:26] So these are going to be, we use basically just saving the values from this curve to point node.
[16:34] So I want the curve index and we'll just name this, name this curve index and then duplicate that
[16:40] and then do an index in curve.
[16:45] So what these are going to allow us to do is change the color between these different individual elements
[16:53] as well as maybe we can do a gradient from the beginning to the end of each one.
[16:58] So to use that in the shader editor, we pop in an attribute node and we can just control C,
[17:04] control C and control V the names, shift D to duplicate, control C, control V.
[17:13] So if we want to see that, we can just pop that into the color and go to preview node.
[17:19] So you can see how the curve index starts at zero and then it goes up until it's bright.
[17:25] We can always put in like a Voronar texture and use that as the coordinate vector.
[17:35] It's really just factor there so we can set this to 1D.
[17:39] And you'll see the different colors for each of the individual strands.
[17:43] I'm blowing up.
[17:46] Then index and curve, if we put that into the viewer, you'll see we actually don't want index and curve at all.
[17:56] I don't know why I thought that was what we wanted.
[17:59] We actually want a float parameter and it's just going to be curve fact.
[18:06] And this is going to be spline parameter and then the factor.
[18:10] So I was just wrong about what that was and we'll control C and control V.
[18:15] And then you get that.
[18:17] So what we can do is let's say this is the base color.
[18:22] Put that into our principled BSDF.
[18:25] And then we can use a mixed color node if we want this to be closer to some target color.
[18:30] You can set it from mix to color.
[18:32] Say we want it to be kind of like red, like a red candy thing.
[18:37] Set the factor down a bit.
[18:41] We can do that.
[18:42] We can also set it to just hue and then we can do a separate one that is also saturation and just control those a little bit individually.
[18:54] This is reminding me of some sort of candy and so we're definitely going to need subsurface scattering.
[19:00] So bring that weight up to one.
[19:02] Set the radius to be just equal and we can scale that up or down.
[19:08] Let's do 0.01.
[19:11] It's looking pretty good.
[19:12] One other thing is that we have these really hard edges on the caps here.
[19:16] So we'll want a bevel node and put that into the normal here.
[19:24] So let's see.
[19:26] One good way to check this is you can just use it on a glossy BSDF to make sure that it's got the parameters that you want.
[19:37] Let's way too big.
[19:38] Like 0.01.
[19:40] Okay.
[19:41] We'll set this to 0.0025 and then set the samples to something like 16 maybe even 32.
[19:55] It could be 0.005.
[19:59] I like that.
[20:00] So we'll set that in there and put that in here.
[20:07] I'm also going to add a sheen to this.
[20:10] No, not a sheen.
[20:11] A coat.
[20:12] Low roughness.
[20:14] We'll not add too much in there.
[20:16] Just give it a little bit there.
[20:19] I'm going to go into my color management settings.
[20:22] A GX is good.
[20:24] We're going to do high contrast.
[20:26] Then we're going to change our sun to have a much larger angle.
[20:32] So it's softer shadows there.
[20:34] Something that that looks pretty good.
[20:36] We'll duplicate the sun.
[20:39] Maybe rotate it a bit.
[20:41] And well, we could put this kind of directly behind.
[20:46] I'll just rotate it a bit and then I'll bring the angle down so we have this little shadow here.
[20:52] That's going to look pretty cool.
[20:54] That'll work.
[20:58] That'll work.
[21:00] Let's do that.
[21:04] And that's starting to look pretty good.
[21:06] One other extension that we can do is maybe we want to put some sort of texturing.
[21:10] Oh, actually, we haven't used our curve fact node yet.
[21:13] And we're going to speed through things again because we ended up not using the curve fact node.
[21:18] It didn't look good and you don't need to watch me try and figure that out for two minutes.
[21:23] I'll just give that time back.
[21:24] Okay, bye.
[21:24] And let's just not use that node.
[21:30] So that'll be our setup there.
[21:32] Okay.
[21:33] So the other trick I wanted to show you is let's say we wanted to add some sort of texture on the surface of this.
[21:39] Maybe little glossy specs.
[21:43] So what we could do is we could do a mixed shader and then do a Voronoi texture.
[21:49] And just, well, let's look at this.
[21:53] And what we would do is we'd mix it base off of this.
[21:55] So we use less than something like 0.1 and scale that up a bunch.
[22:02] And you see you get all these little specs and then you'd mix it here with a glossy BSDF.
[22:12] And set that roughness kind of low.
[22:15] So it's a little shiny.
[22:17] And I don't know, that looks pretty cool.
[22:18] I like it.
[22:19] But the problem is that it moves and it moves because the geometry is moving.
[22:26] So you need some sort of unmoving reference, ideally from the end state of the geometry.
[22:37] But it's kind of weird to get because you don't create this geometry until you use this curve to mesh node
[22:43] and the curves that are the input guide geometry are moving.
[22:47] So instead, what we can do is we can use a bake node.
[22:52] Just pop that in there.
[22:54] Go to the end of our frame.
[22:56] Hit Bake.
[22:57] Now that's a still.
[22:59] And then we'll just sample that by index.
[23:03] And we'll get the position.
[23:06] So get the position at index.
[23:11] And then store name attribute vector.
[23:15] Type that in.
[23:16] And this will be end position.
[23:19] And so this index corresponds to the index here.
[23:22] So we're sampling this baked animation at the same point index as the point index here.
[23:29] So then that'll just correspond to the same vertices of the mesh over time.
[23:34] And this is still bouncing around everywhere.
[23:37] But then if we pop in a attribute node and we use our end position as the input here,
[23:46] then that doesn't happen anymore.
[23:48] And it stays stable.
[23:49] Yay.
[23:52] So now we have our animation.
[23:58] And all that's left is to light things and play around with the textures more.
[24:02] Probably want to change the color of this background.
[24:06] I don't know.
[24:06] We can change it to a lot of things.
[24:08] That looks decent.
[24:11] Might want to up the resolution here.
[24:14] So let's say, well, first of all,
[24:21] those are too big.
[24:23] So let's do like 0.03.
[24:27] That's too small.
[24:28] 4.47.
[24:32] OK.
[24:32] That looks pretty good.
[24:34] And then we're also going to, I'd say the resolution is pretty nice.
[24:40] You could make it bigger.
[24:41] You could go 64 if you wanted.
[24:44] We'll get some more.
[24:44] Oh, well, if you do change anything about the geometry,
[24:49] you're going to want to make sure to go to the end again and then rebake your position.
[24:54] You can actually bake it from anywhere.
[24:57] It would work just as well if you baked it here.
[24:59] I believe.
[24:59] Yeah, I'm just going to bake it at the end.
[25:03] And make sure to go for when everything is tightly packed to tune this.
[25:09] Maybe 4.5.
[25:12] 4.45.
[25:13] I want them to be just barely touching,
[25:15] but I don't want them to touch too much because then you can get some artifacts.
[25:20] So I'd say that's looking pretty nice.
[25:22] Pretty happy with that.
[25:24] Like I said, you can always tune materials and compositing and everything forever.
[25:31] But you can also just hit render and wait to see your result and be happy because that's why we do this.
[25:42] Anyway, I hope you enjoyed this tutorial.
[25:45] I hope you learned something.
[25:47] And above all, I hope you had fun.
[25:50] Till next time.
[25:52] Oh, you can get the project files in Patreon if you want to check that.
[25:55] But yeah, till next time.
[26:00] Bye.



---

## Captured Frames

- [1:00] tutorials/frames/beginner-geometry-nodes---helix-twist-blender-tutorial/frame_000.jpg
- [3:10] tutorials/frames/beginner-geometry-nodes---helix-twist-blender-tutorial/frame_001.jpg
- [9:20] tutorials/frames/beginner-geometry-nodes---helix-twist-blender-tutorial/frame_002.jpg
- [11:00] tutorials/frames/beginner-geometry-nodes---helix-twist-blender-tutorial/frame_003.jpg
- [16:00] tutorials/frames/beginner-geometry-nodes---helix-twist-blender-tutorial/frame_004.jpg
- [20:35] tutorials/frames/beginner-geometry-nodes---helix-twist-blender-tutorial/frame_005.jpg
- [21:04] tutorials/frames/beginner-geometry-nodes---helix-twist-blender-tutorial/frame_006.jpg
- [23:50] tutorials/frames/beginner-geometry-nodes---helix-twist-blender-tutorial/frame_007.jpg

---

## Structured Notes

### Core Technique
Drive a set of strand curves to wrap around (and unwrap from) a central axis by animating Curve Tilt and Curve Scale off each strand's Spline Parameter Factor, then mesh the result with Curve to Mesh — producing a "candy/rope twist" that folds together and apart over the timeline, finished with a bake-node trick to keep surface textures stable despite the moving geometry.

### Summary
A from-scratch Geometry Nodes build of a multi-strand helix that twists together into a rope/candy shape and untwists apart, animated by frame. Six vertical strand curves are generated from a Curve Circle profile, individually separated via Curve Group ID, then spun around a central Curve Line by driving Curve Tilt with the strand's length-based Spline Parameter Factor. Curve Scale (also driven by that factor, remapped through Map Range and a Power node) makes the strands taper together at one end. Because the raw twisted curve stretches unevenly, a second, evenly-resampled "guide curve" is built and the twisted shape is resampled onto it via Sample Curve, keeping strand length constant for clean texturing. The guide is meshed with Curve to Mesh (Curve Circle profile, capped), and the fold/unfold animation is driven by Scene Time > Frame remapped through a Mix node and Power node for eased, non-linear timing. The second half covers rendering setup (GPU Cycles, mobile-aspect camera, motion blur) and shading a glossy, subsurface-scattering "candy" material colored via stored per-strand Curve Index / Spline Parameter attributes, plus a Bake node trick that freezes the mesh's end-state vertex positions so procedural surface textures (e.g. Voronoi specks) don't swim as the geometry animates.

### Key Steps
1. **Base shapes:** Add a default cube, delete it, open a Geometry Nodes editor, create a new node tree. Add a Curve Line (the central spin axis) and a Curve Circle set to 6 points (one point per strand) feeding a Curve to Mesh node as the Profile Curve to preview the raw helix.
2. **Separate strands:** Convert the Curve Circle to points (Curve to Points), then Points to Curves so each point becomes its own curve; set the new curve's evaluated Curve Group ID to the point Index so each of the 6 strands is an individually-controllable spline (frame_001 shows the resulting per-strand curve set, viewed orthographic).
3. **Twist via Tilt:** Feed the profile curve's Curve Tilt from the central Curve Line's Spline Parameter, using Length (not Factor) so the twist rate stays constant regardless of curve length; multiply length by a twist-rate constant. Add a Resample Curve (by Length, ~0.001) on the central line first — without it, tilt only has 2 points to interpolate and the twist looks broken.
4. **Taper together:** Drive Curve Scale from the same Spline Parameter Factor, remapped through a Map Range node (e.g. 0.001→1 mapped to 1.0→2.0, base scale ~0.1) and smoothed through a Power node (power ≈5) so the strands come together abruptly at one end and stay open at the other (frame_002/frame_003 show the resulting twisted "candy" shape at two different lengths).
5. **Guide-curve resample (constant-length fix):** Because the twisted curve stretches unevenly (bad for meshing/texturing), build a second plain Curve Line, resample it finely, run its own Curve to Mesh with the same profile curve (no twist/scale needed), then use Sample Curve (by Length, using the twisted curve's own Spline Parameter length as the source) to project the twisted curve's shape/animation onto the guide curve at constant length. Requires converting the sampled mesh output back to a curve and re-deriving Curve Index via a Curve of Point node, since Spline Parameter is meaningless on a mesh.
6. **Final mesh:** Curve to Mesh the guide curve with a small Curve Circle profile (scale ≈0.05), Fill Caps on; lengthen the central line and guide curve as needed to get a longer, "candy-like" spiral (frame_002 vs. frame_003).
7. **Frame-driven animation:** Add a Scene Time node (Frame output), Map Range it from the scene frame range to the fold-together start/end factor values; replace the direct Map Range easing with a 0–1 Map Range feeding a Mix node (between the min/max target values) plus a Power node (~0.2–0.5) for a fast-start/slow-finish ease — Power nodes only behave correctly on a 0–1 input range, hence the extra remap.
8. **Render setup:** Set Material > Set Material node with a default material, switch Shading workspace, enable Cycles + GPU, add a Sun light (rotated for angle), raise exposure, add a ground plane, add a camera (View > Align Active Camera to View), set a mobile aspect ratio (1080×1920), enable Motion Blur, and lower render samples (~32) for test renders (frame_004 shows the first clay-vs-rendered test render, split-screen).
9. **Per-strand color attributes:** Before the final Curve to Mesh, add two Store Named Attribute (Integer) nodes to bake "curve index" (from Curve to Points' index) and a Float "curve fact" (Spline Parameter Factor) onto the geometry so the Shader Editor can read them via Attribute nodes for per-strand coloring/gradients.
10. **Candy shading:** Principled BSDF fed by an Attribute node (per-strand index) mixed toward a target hue via a Mix Color node (Hue/Saturation), Subsurface weight = 1 with small radius (~0.01) for the translucent candy look, a Bevel node into the Normal input to soften the hard cap edges (~0.0025–0.005, 16–32 samples), and a small Coat layer with low roughness (frame_005/frame_006 show the final glossy pink/red twisted-candy result under two Sun lights for soft dual shadows).
11. **Stabilizing surface texture (Bake trick):** For non-moving surface detail (e.g. glossy Voronoi specks mixed via a Mix Shader), a Bake node freezes the mesh at the end frame; Sample Index reads the baked end-state Position per vertex, stored via a Store Named Attribute (Vector) as "end position"; an Attribute node then feeds that fixed position into the texture coordinate input so procedural textures stop swimming as the animated geometry moves (frame_007 shows the loose/apart animation state with the bake-related node graph visible). Re-bake any time the base geometry changes.

### Nodes / Settings
- **Curve generation:** Curve Line, Curve Circle (6 points, used as Profile Curve), Curve to Points, Points to Curves, Curve Group ID = Index.
- **Twist control:** Curve Tilt driven by Spline Parameter (Length mode) × twist-rate constant; Resample Curve (By Length, ~0.001) required before tilt for smooth interpolation.
- **Taper control:** Curve Scale driven by Spline Parameter Factor → Map Range (e.g. 0.001–1 → 1.0–2.0, base scale 0.1) → Power node (~5).
- **Constant-length guide fix:** second Curve Line → Resample Curve → Curve to Mesh (same profile) → Sample Curve (By Length, using source Spline Parameter length) → convert mesh back to Curve → Curve of Point node (Curve Index) to re-derive per-strand index.
- **Final mesh:** Curve to Mesh with Curve Circle profile (scale ≈0.05), Fill Caps enabled.
- **Animation drive:** Scene Time (Frame) → Map Range (0–1) → Mix node (start/end fold values, e.g. 0.4 to a large negative value) → Power node (0.2–0.5 for ease).
- **Attributes for shading:** Store Named Attribute (Integer) ×2 — "curve index" and per-point index; Store Named Attribute (Float) — "curve fact" (Spline Parameter Factor).
- **Shading:** Principled BSDF; Attribute node (curve index) → Mix Color (Hue/Saturation) for per-strand tint; Subsurface weight = 1, radius ≈0.01; Bevel node (0.0025–0.005, 16–32 samples) → Normal input; Coat layer, low roughness.
- **Texture-stabilizing bake:** Bake node → Sample Index (Position) → Store Named Attribute (Vector, "end position") → Attribute node feeding texture coordinate of a Voronoi-driven Mix Shader (glossy specks, Glossy BSDF, low roughness).
- **Render:** Cycles, GPU compute, Motion Blur enabled, ~32 test samples, mobile aspect ratio 1080×1920, Sun lights (large angle for soft shadows), AgX color management with high-contrast look.

### Difficulty
Intermediate — labeled "beginner" by the author, but the constant-length guide-curve resample trick (step 5) and the Power-node-needs-0–1-range fix for animation easing (step 7) are non-obvious gotchas that go beyond a first Geometry Nodes tutorial. The core twist/taper mechanic (steps 1–6) is genuinely beginner-friendly.

### Blender Version
Not stated explicitly in the transcript. Node editor styling (muted node colors, classic dark theme) is consistent with Blender 3.x/early 4.x rather than the newer 5.x node-color scheme seen in other library entries.

### Tags
#geometry-nodes #procedural #animation #materials #shaders #rendering #cycles #motion-design #abstract #organic #beginner

---

## Related Tutorials
- **Blender Tutorial - Procedural Rope in Geometry Nodes** (`tutorials/blender-tutorial-procedural-rope-in-geometry-nodes.md`) — same core domain (interlocking spiral/strand curves built with Geometry Nodes, animated organic twisting), shares #geometry-nodes #procedural #organic #animation tags; a good next step for more advanced multi-strand curve rigs.
- **Curves Just Got Easier in Blender 5.0** (`tutorials/curves-just-got-easier-in-blender-50.md`) — shares the per-strand attribute-driven coloring/texturing approach (Spline Parameter / per-spline Random attributes read in the Shader Editor) and #geometry-nodes #materials #shaders #motion-design #procedural #abstract tags, useful for extending this tutorial's per-strand shading trick.
