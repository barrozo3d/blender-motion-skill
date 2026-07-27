---
title: Blender Finally Did It!!
source: YouTube
url: https://www.youtube.com/watch?v=KNqV2wJgxVM
author: Ducky 3D
ingested: 2026-07-27
blender_version: "5.2"
tags: [geometry-nodes, procedural, displacement, animation, lighting, rendering, cycles, motion-design, abstract, volume, intermediate, blender-5x]
extraction_status: complete
frames_dir: tutorials/frames/blender-finally-did-it/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender Finally Did It!!

**Source:** [YouTube](https://www.youtube.com/watch?v=KNqV2wJgxVM)
**Author:** Ducky 3D
**Duration:** 16m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Alright, today we are going to be making this animation right here.
[0:04] Now, first I want to address the title.
[0:06] Uh, for some, definitely looks like clickbait, but for me, this is genuinely how I feel about this brand new feature that Blender just released.
[0:15] It's not glamorous, it's very boring, and it's the brand new bevel node in geometry nodes.
[0:20] Before 5.2, if you wanted to have an object in geometry nodes that has a bevel, you have to make it externally, and then drag it into geometry nodes,
[0:27] and then you can use it as an instance.
[0:30] Um, that's not that big of a deal, but it does have its limitations.
[0:34] Um, on Patreon, I kind of expanded on those limitations, and we are able to make a really cool animation with it.
[0:40] I will touch on that in this video as well.
[0:43] So we're going to make this animation as an excuse to show you that it's a new feature.
[0:48] We're going to use it in this animation, and we don't need to make anything externally and drag it into geometry nodes anymore.
[0:54] So again, we're going to make this animation.
[0:57] If you want the project file, you can check it out on Patreon, along with all the other really cool tutorials and things on Patreon as well.
[1:02] Um, but again, we're going to check out this new node.
[1:04] Make sure you're using the new 5.2 and let's do this.
[1:08] Okay, we're going to be using geometry nodes.
[1:10] So just go ahead and shift A.
[1:12] Let's go ahead and bring in a plane here and go straight to the geometry nodes workspace.
[1:16] Click new, and we're going to delete the input and let's go and get a cube.
[1:22] Now, if you've never touched the new bevel node, I'm about my assumption is if you're watching this video, you probably have.
[1:28] But we are going to touch on it very briefly.
[1:30] It's not very confusing.
[1:32] So we're going to go ahead and type in the mesh bevel here in geometry nodes.
[1:36] It's going to do that.
[1:37] Now you have these four things right here that correlate to the parts that we are beveling.
[1:44] So if you want to bevel it like the normal bevel modifier, you would just click and drag and do that.
[1:50] Or you would plug a value node into all these sockets.
[1:53] You can control them all at once.
[1:55] You do have your classic segments right here.
[1:59] You have shape.
[2:00] So you can bring it in.
[2:01] You can bring it out.
[2:03] And you can also use curves as your profile.
[2:06] So really, really simple.
[2:08] I'm going to bring my segments back to one.
[2:10] Another cool bit is the meter.
[2:14] The spread.
[2:14] This is a pretty cool bit.
[2:16] In that animation I mentioned that's on Patreon.
[2:18] That bit that's moving is me animating the meter.
[2:22] Mitter.
[2:23] I think it's mitter.
[2:23] It's not meter.
[2:25] I don't know.
[2:25] But you can animate it in some really, really cool ways.
[2:29] And so let's say I take this.
[2:31] I do want to talk about one more feature before we make the full animation.
[2:34] So let's go ahead.
[2:35] Let's get another bevel node.
[2:36] Let's say you made this sort of abstract kind of hard surface shape.
[2:39] I want to bevel it so you could just put another mesh bevel on it and go, okay, cool.
[2:44] I want to do something like this and then bring up my segments.
[2:48] Now that looks nice.
[2:50] I'm going to bring this up a little bit higher.
[2:54] One thing you have is these selections.
[2:56] So you have this.
[2:58] So if you get a delete geometry, set it to faces, you can actually see what it's doing.
[3:05] So if you plug the top one vertex face into the selection, you're getting it to delete
[3:10] these little corners, edge face kills those guys right there.
[3:16] And then outer edge is my favorite, which we did.
[3:19] This one's really cool because if you do this sort of double mesh bevel situation, you get
[3:24] a really cool kind of wire frame situation I like.
[3:27] And then mid edge, don't know what it does.
[3:30] Someone's going to have to tell me what that does.
[3:32] But if you use this quick little setup, you get something pretty sweet like this.
[3:38] I think it's awesome.
[3:38] So that is your very quick, very basic overview of a very basic feature.
[3:45] I'm going to go ahead and take my cube and bypass all of these.
[3:49] We're going to delete this.
[3:51] So on this guy here on the Y, I'm going to make him pretty wide.
[3:55] Just like that.
[3:56] He's too tall.
[3:58] So something like this.
[4:00] All right.
[4:00] So this is sort of the base canvas.
[4:03] We're going to go ahead and now get a mesh to volume.
[4:06] So shift A.
[4:08] Mesh to volume.
[4:10] And then we're going to distribute.
[4:11] So distribute points in volume.
[4:16] And we're going to go from a random to grid.
[4:19] So this is a pretty sweet feature.
[4:21] Gives you a really quick grid.
[4:22] The smaller this number, the more instances you have.
[4:26] So it's very, very sensitive.
[4:28] So if you go to like point one, super dense, very, very fast.
[4:34] If you go even farther, you're going to crash your computer.
[4:37] But you can if you want.
[4:38] I'm going to do like point two.
[4:41] No.
[4:44] Point one might look kind of awesome.
[4:46] Let's do point one.
[4:51] Point one four.
[4:53] Okay.
[4:54] That's a little more reasonable.
[4:55] Your numbers might be different.
[4:57] Your numbers might not.
[4:59] Okay.
[4:59] So now we have points.
[5:00] If I were to look at this in cycles, it would just be all of these little circles,
[5:04] which is cool in cycles, points come out to these perfectly smooth circles.
[5:09] You can do circles if you want.
[5:10] I am going to get an instance on points node.
[5:16] Plug it here, get a cube.
[5:18] And this is the point where we don't have to make anything externally.
[5:21] So we can get a cube, plug it into the instance, and then click and drag it on the X, Y, and Z
[5:28] to scale it down a little bit.
[5:30] Another quick tip.
[5:31] This is kind of hard to look at.
[5:34] Right here in your, your viewport, you can turn on cavity.
[5:39] And outline.
[5:40] And it makes it a little bit easier to look at.
[5:41] Now these cubes would need to be beveled in order to, you know, to look a little better.
[5:46] I'm going to try to get their size to be right where I want it to be.
[5:50] So again, we just get a bevel node, mesh bevel.
[5:54] We're going to give them all point zero two.
[5:59] Give them a few segments.
[5:59] Let's do point zero one.
[6:02] There we go.
[6:03] I'm going to give them three segments and we can do a set shade smooth to finish it out.
[6:09] And again, and it's all of its beauty.
[6:13] We got to do all of this in geometry nodes.
[6:16] So that's the whole point of today's video.
[6:18] Us to look at this and have some fun and celebrate this victory.
[6:23] Now, all of the fun animated parts are going to be come, are going to come from the scale.
[6:28] So let's get a color ramp and a noise texture.
[6:32] I get made fun of sometimes for using color ramps.
[6:34] I know you should probably use a map range.
[6:39] I just love the color ramp.
[6:42] Let's use a noise texture and then go ahead and plug your factor into the color ramp.
[6:48] So if you bring the white portion in, it's going to scale these guys back to their full scale.
[6:54] White, fully white is a value of one.
[6:57] So that's going to give them back to their main spot.
[7:00] And you can bring this in and start to scale out.
[7:03] Now, this is kind of ridiculous.
[7:06] So you can bring your scale down till we get something like this.
[7:10] And then we can bring these nodes closer together to decide, you know, how do we want
[7:16] that transition to look?
[7:18] But this looks pretty cool.
[7:21] My, my advice from a design perspective is try to get it to where you were.
[7:27] There's moments in this model where there's these big long flat sections because the
[7:33] lighting will cast across it and it will look really cool.
[7:37] So try to have a balance of like these big ports, parts where the noise is eating
[7:41] through the cubes and then big flat portions.
[7:44] Anything in between that probably looks fine, but it could look better.
[7:47] So that's, that's my design advice for your choices.
[7:51] Let's go ahead and get this texture to move.
[7:53] So in geometry nodes, you have to kind of custom make your own mapping setup.
[7:58] So get a position node, plug that into the vector and then get a vector math node.
[8:04] This is basically a position.
[8:06] So now we have this, you can move it like here.
[8:10] So if you look at this and then you can do the opposite direction, we are going to animate
[8:17] this here, but we're going to make it loop.
[8:21] And that's a little bit more tricky.
[8:22] It's a video.
[8:23] I actually talked about this trick in a video a few days ago, which apparently is not novel.
[8:29] This trick, it was novel to me.
[8:31] So let's take these, these three guys here.
[8:35] Let's go ahead and loop this animation first and then we can light it and we can be on our way.
[8:40] So let's get a mixed color node right here.
[8:45] If you take these two guys, just duplicate them, plug that position in the top vector.
[8:51] And again, make sure you plug factor not color back into it.
[8:55] So let's bring this factor to the left.
[8:57] And then in your preferences in the animation, be sure you are on linear.
[9:05] Otherwise it will not loop.
[9:07] And we want this to loop because loops are cool.
[9:09] So let's go ahead, decide your settings now.
[9:12] In fact, decide your settings before you do this duplicating.
[9:15] I'm happy with my settings here.
[9:16] So I don't need to duplicate it.
[9:20] But go ahead and decide how you want it to look.
[9:22] You can edit the color ramp.
[9:25] Literally whenever, because there's just one, but these, these noise sections need to be exactly the same.
[9:31] Okay, let's go back hover over here in the timeline to go back to frame zero.
[9:36] I'm going to hit I on this ad.
[9:39] I on the factor go to the end of the timeline, bring this over hit I.
[9:42] And then I'm going to give this a value of 25.
[9:48] Hit I, there we go.
[9:49] We'll go to the end of the timeline and then hit I on this ad.
[9:55] Go back to frame zero and do negative 25.
[10:01] Let's make sure that loops.
[10:02] It does.
[10:03] So there we go.
[10:04] Now we have this sort of like rain, sort of an abstract interpretation of rain.
[10:11] If you want to look at it kind of pretentiously.
[10:14] Before we finish this out with lighting, I want to add one little element in as just sort of a design as kind of a design choice.
[10:23] I'm going to give myself a little bit more space in the color app.
[10:31] There's not enough like gaps.
[10:35] There we go.
[10:37] Cool.
[10:38] So what I want to do is just get a bunch of like lines cutting through it.
[10:42] So what I'll do is I'll get a joint geometry.
[10:45] I'm going to do this a bit quicker.
[10:46] You don't have to do this part if you don't want to.
[10:49] So we'll get a joint geometry and first let's get a grid.
[10:53] We'll plug this grid right here.
[10:56] You can see he showed up right there in the middle.
[10:58] So wherever your anchor point is, that's where he's going to be.
[11:00] Tech will not technically, but I didn't move my anchor point.
[11:03] And then we're going to get a transform geometry node and rotate it.
[11:09] Looks like it needs to be rotated on the X by 90 degrees and then scale it up
[11:15] until he kind of peeks out the top.
[11:16] So right about there.
[11:21] And then if I look at the wireframe view here in the vertices of the grid, you
[11:27] can start adding some vertices.
[11:29] This is not going to be an exact science in a perfect world.
[11:31] They would line up with all the cubes, but we're going to delete stuff anyway.
[11:35] Okay.
[11:35] So give myself some space.
[11:37] We're going to get an instance on points node and we are going to instance a cylinder.
[11:47] So let's go ahead and give us some space.
[11:49] We'll plug this into the instance and then we need to rotate it on the X by 90 degrees.
[11:57] Radius needs to come down to 0.01.
[12:00] So now we have all of these guys.
[12:03] And then the depth.
[12:06] Just get it to scale the whole thing.
[12:09] So now we have this, which is overwhelming.
[12:13] So one thing I'm going to do just to make this look a little bit more balanced
[12:16] is delete some of them.
[12:17] So we're going to get a delete geometry and we can tell it to delete the instances
[12:23] because we instanced all of these cylinders.
[12:26] So if you get a random value node and you set that to Boolean, you can tell it
[12:31] to delete just the instance that you're not deleting faces because then that would look bad.
[12:37] So you can bring it down till you just get a couple of these and it kind of anchors
[12:44] this whole thing.
[12:45] And I think it makes it look really cool.
[12:49] So now we're done animating and modeling.
[12:52] Now we can light it.
[12:53] Now the lighting is really simple, but it's super, super beautiful.
[12:57] So let's go back to the layout.
[12:59] I'm going to hit the tilde key.
[13:01] It's right in front of the tab key.
[13:04] I'm going to go to the right here.
[13:05] I'm going to shift a and get my speaker.
[13:07] Did I say speaker?
[13:09] I meant camera.
[13:10] I'm going to hit G in middle click.
[13:15] And then I'm going to set my composition.
[13:18] So something like this and then like this.
[13:20] Now, the reason I'm making this choice is because we're going to have a big light here at the back.
[13:27] So I want to have us light that sort of casts across the bottom.
[13:33] Whenever it has these flat moments like this right here, and then we'll have a big accent color light right here.
[13:40] And so the lighting is super simple.
[13:42] We're going to get a shift A and get a plane.
[13:45] I'm going to hit R, Y, 90.
[13:49] And then we're going to move it back a little bit to something right here and then scale it just like that.
[13:57] So I'm going to be using cycles to view this.
[14:00] This plane, I'm going to give it a new material and make it a emission material and then bring up the brightness a little bit.
[14:08] And I'm just going to keep it white and then I'm going to do a render region.
[14:12] Just for me, you don't have to.
[14:14] So now we have this and then I just want some interesting color, just an accent light to really make it look cool.
[14:21] So first here in the world settings, we're going to bring the brightness down to black.
[14:25] And then let's get that light.
[14:27] So we're going to go get a light, an area light, and then right down here, the area light settings, just make it a disc.
[14:34] And then I'm going to hit G to kind of move it around.
[14:40] And then I'm going to point it.
[14:42] I'm going to hit R twice and point it at the corner of my viewer.
[14:49] Let's make it orange.
[14:51] Bring up the exposure and then bring the spread down to you can kind of see this circle.
[14:59] And then I'm going to hit R and get that to just kind of hit it right there.
[15:04] So the gradient is soft.
[15:06] The more you bring that spread down, the harder that gradient is going to be.
[15:09] Just make it soft enough and then you can bring that exposure down or up as much as you want.
[15:13] Also, you can make it blue or green.
[15:17] Again, I'm going to make mine a nice orange.
[15:21] And we are totally done.
[15:23] Now, from a rendering standpoint, if you go here to the camera icon, you can really crunch this.
[15:30] Make sure your caustics are off here and you bring your transparent down, your volume down, your transmission, keep everything else at one.
[15:38] So all of these down to zero.
[15:40] And then I'm going to turn on my denoiser.
[15:45] I'm going to make sure the denoises on and 300 on the samples.
[15:49] And renders pretty quick with those settings for me.
[15:51] That was three seconds on the render.
[15:53] So if there is any noise or there is any weirdness, I have some flexibility.
[15:58] But at 1080p, this renders pretty well and pretty quick.
[16:02] So this is our final look.
[16:07] And I just think it's really cool and I love it.
[16:09] And we got to have an excuse to use the new Bevel node, which I'm obsessed with.
[16:12] Thank God it's finally out.
[16:13] So if you want to export this, go here to the printer icon.
[16:17] Go ahead, I'm going to keep it at 1080p.
[16:18] Go ahead and create a folder and select that folder here.
[16:22] Export out a PNG sequence and then you can go to render, render animation and you'll be totally done.
[16:27] So there you go.
[16:28] That was a long winded excuse to talk about the Bevel node that I've been asking for for a freaking long time.
[16:35] Apparently I've been so vocal about it that when I was at Blender Conference in Los Angeles three years ago, two years ago, someone brought it up to me.
[16:43] So I didn't know how much I complained about it.
[16:44] But it's finally here and I don't have to complain about it anymore.
[16:48] Again, if you want to check out that bonus tutorial on Patreon, we made a really cool animation.
[16:53] So if you want to check all that out, that is linked in the description.
[16:56] And with that being said, I'll see you in the next one.



---

## Captured Frames

- [1:36] tutorials/frames/blender-finally-did-it/frame_000.jpg
- [2:44] tutorials/frames/blender-finally-did-it/frame_001.jpg
- [4:57] tutorials/frames/blender-finally-did-it/frame_002.jpg
- [6:09] tutorials/frames/blender-finally-did-it/frame_003.jpg
- [7:10] tutorials/frames/blender-finally-did-it/frame_004.jpg
- [11:47] tutorials/frames/blender-finally-did-it/frame_005.jpg
- [13:57] tutorials/frames/blender-finally-did-it/frame_006.jpg
- [16:02] tutorials/frames/blender-finally-did-it/frame_007.jpg

---

## Structured Notes

### Core Technique
Using Blender 5.2's new native **Mesh Bevel** node inside Geometry Nodes (no more external-bevel-then-instance workaround) to build a volume-distributed cube grid whose scale is driven by an animated, looping noise texture — an abstract "digital rain" block animation, finished with two-light Cycles lighting.

### Summary
Ducky3D demonstrates the brand-new Mesh Bevel node in Blender 5.2's geometry nodes (previously bevels for instanced geometry had to be modeled externally and dragged in). After a quick overview of the node's sockets (Miter Spread, Segments, Shape, Selections: Vertex/Face, Edge/Face kill, Outer Edge, Mid Edge), he builds a full animation: a wide cube is converted to a volume, points are distributed on a grid, cubes are instanced on those points and beveled/shade-smoothed in place, then a Noise Texture → Color Ramp drives per-instance scale (via Position + Vector Math) to create a rippling "eaten away" block effect. The scale animation is made to loop by keyframing the Color Ramp factor input (0 → 25 → back to 0 with -25, Linear interpolation) rather than the color. A secondary grid of thin instanced cylinders (randomly culled via a boolean Random Value into Delete Geometry on Instance) is layered in as accent "rain lines." The scene is lit with a large white emission plane (rim/base light) plus a colored (orange) disc Area Light with low Spread for a soft gradient, rendered in Cycles at 300 samples with denoising, and exported as a PNG sequence.

### Key Steps
1. Add a Plane → enter Geometry Nodes workspace → new node tree → delete default Group Input link → add a **Cube** node.
2. Add a **Mesh Bevel** node on the cube's Mesh socket; briefly demo controls: Start/End Left/Right Offset, Miter Spread, Segments, Shape (concave/convex via curve), and Selection sockets (Vertex of Face / Edge of Face kill / Outer Edge / Mid Edge) feeding a Delete Geometry (Faces) to preview each selection's effect. "Outer Edge" selection on a double Mesh Bevel setup gives a wireframe look.
3. Bypass the demo bevel chain; reshape the base Cube wide on Y (flat "canvas" shape).
4. Add **Mesh to Volume** → **Distribute Points in Volume** (mode: Grid, not Random) with Spacing X/Y/Z ≈ 0.140 and Threshold 0.100 to get a dense, evenly spaced point grid.
5. Add **Instance on Points** → instance a **Cube**, scale instances down (X/Y/Z) to leave gaps; enable viewport Cavity + Outline for readability while sizing.
6. Add **Mesh Bevel** (Offsets ≈ 0.02, Segments 3) + **Set Shade Smooth** on the instanced cube mesh to finish each block's look.
7. Drive per-instance scale: **Position** node → **Vector Math** → **Noise Texture** (Scale 6.6, Detail 2, Roughness/Lacunarity/Distortion tuned) → **Color Ramp** (factor, not color, into scale) so white = full scale (1.0), black = scaled to ~0.
8. Loop the animation: duplicate the Position/Vector Math chain and blend via a **Mix Color** node with two Factor keyframes; keyframe the Color Ramp/Mix **Factor** value (not the color stops) at frame 0 = 0, later frame = 25, then back at frame 0 = -25 at the far end; set Interpolation to **Linear** in Preferences/Animation before keying or it won't loop cleanly.
9. Add a secondary layer: **Join Geometry** ← a **Grid** (rotated 90° on X, scaled to peek through the top) feeding **Instance on Points** with a thin **Cylinder** (rotated 90° X, Radius 0.01, Depth scaled) for "rain line" accents.
10. Thin out the cylinder instances with **Random Value** (Boolean) → **Delete Geometry** set to delete **Instances** (not Faces) for a balanced, non-overwhelming density.
11. Lighting: switch to Cycles. Add a large **Plane** behind the subject, give it an **Emission** material (white, boosted strength) as a soft base/rim light; set World background strength to black (pure black background). Add an **Area Light** (shape: Disc), rotate to point at a corner, tint orange, raise Exposure, lower **Spread** for a harder gradient edge (raise Spread for softer).
12. Render settings: disable Caustics; set Transparent/Volume/Transmission bounces toward 0 (keep others at 1); enable the Denoiser; Samples ≈ 300 (renders in ~3s at 1080p in the demo). Export via the printer/output icon as a PNG sequence, then Render → Render Animation.

### Nodes / Settings
- Mesh Bevel (Geometry Nodes) — Start/End Left/Right Offset, Miter → Spread, Segments, Shape, Profile (curve), Selections (Edges / Vertex of Face / Edge of Face / Outer Edge / Mid Edge)
- Mesh to Volume (Density 1.000, Voxel Amount 64000, Exterior Band Width 0.2m in the example)
- Distribute Points in Volume — mode **Grid**, Spacing X/Y/Z ≈ 0.140, Threshold 0.100
- Instance on Points, Cube, Set Shade Smooth
- Position → Vector Math → Noise Texture (Scale 6.600) → Color Ramp (RGB, Linear interpolation) → instance Scale
- Mix Color node (for the loop-blend trick), keyframed Factor input, Linear F-Curve interpolation
- Grid + Transform Geometry (rotate 90° X) + Join Geometry for the accent-line layer
- Cylinder instances, Radius 0.01, Random Value (Boolean) → Delete Geometry (domain: Instance)
- Cycles render: Denoiser on, ~300 samples, Caustics off, Transparent/Volume/Transmission bounces ~0
- Lighting: Emission-material Plane (base/rim light) + Area Light (Disc, orange tint, low Spread, raised Exposure), World strength = black

### Difficulty
Intermediate — no simulation, but requires comfort with geometry nodes fields (Position/Vector Math), volume distribution, instance-domain deletion, and keyframing node-socket values with correct interpolation for a seamless loop.

### Blender Version
5.2 (built specifically to showcase the new native Mesh Bevel node in Geometry Nodes, unavailable before 5.2).

### Tags
geometry-nodes, procedural, displacement, animation, lighting, rendering, cycles, motion-design, abstract, volume, intermediate, blender-5x

---

## Related Tutorials
- **A New Way To Loop Animations in Blender** (`a-new-way-to-loop-animations-in-blender.md`) — Ducky 3D; this is the exact loop trick referenced directly in the transcript ("I actually talked about this trick in a video a few days ago"), applied here to the Color Ramp/Mix factor keyframes.
- **Blender 5.0's NEW Audio Visualisation is INSANE!** (`blender-50s-new-audio-visualisation-is-insane.md`) — MTR Animation; shares geometry-nodes, animation, volume, motion-design, blender-5x, intermediate.
- **Glass Cell Division Effect in Blender 5.0** (`glass-cell-division-effect-in-blender-50-tutorial.md`) — Ducky 3D; shares geometry-nodes, animation, motion-design, abstract, blender-5x, intermediate; similar "new 5.x node replaces the old workaround" framing.
- **You Should Make Glass Animations in Blender 5.1** (`you-should-make-glass-animations-in-blender-51.md`) — Ducky 3D; shares animation, motion-design, abstract, rendering, cycles, blender-5x, intermediate.
