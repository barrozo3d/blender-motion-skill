---
title: NPR Light Accumulation (Blender 5.3 Branch Testing)
source: YouTube
url: https://www.youtube.com/watch?v=GFGIjeI539k
author: Cartesian Caramel
ingested: 2026-08-17
blender_version: "5.3 experimental/unmerged branch build (self-compiled by presenter from a pull request, not a public release; not in main 5.2/5.3 as of recording)"
tags: [shaders, materials, lighting, rendering, eevee, compositing, motion-design, abstract, advanced, expert, blender-5x]
extraction_status: complete
frames_dir: tutorials/frames/npr-light-accumulation-blender-53-branch-testing/
frame_count: 11
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NPR Light Accumulation (Blender 5.3 Branch Testing)

**Source:** [YouTube](https://www.youtube.com/watch?v=GFGIjeI539k)
**Author:** Cartesian Caramel
**Duration:** 79m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Alright, hello everyone and welcome to today's livestream where I'm going to be testing an experimental branch of Blender which has the light accumulation node.
[0:11] Now, this is experimental. It is not in the main version of Blender 5.3, of course. Maybe it will come in 5.3, I'm not sure.
[0:20] But it is a new node in EEVEE that lets us go and customize the lighting in EEVEE, which is very nice.
[0:29] So it comes with a few other little nodes, but we'll get into that, but it allows for very nice and stylized effects.
[0:35] And, oh, it's kind of on theme given the Spiderverse trailer leaked yesterday, or maybe a few days before.
[0:43] But I wanted to try out some more stylized stuff now that this branch is going.
[0:49] So, there are three new nodes, I believe, and I should actually look at the pull request again to see if I missed anything.
[0:57] But light info, shadow raycast, and light accumulation.
[1:01] So, let's go and start from the beginning with all of this.
[1:05] You have a position input which allows for stuff like this, but let's start from scratch.
[1:11] So, we have the light accumulation node. As we can see, by default, it does absolutely nothing.
[1:16] Let's go and attach a value to the diffuse light and diffuse color and set it to 1.
[1:20] We can see that everything here just turns completely white.
[1:25] And that's because we're not using the actual light info, we're just setting the value to be that.
[1:30] So, let's go and attach the color to the diffuse light and diffuse color.
[1:35] There we go. I actually need to check. I actually don't know what the difference is between all of these.
[1:40] I'm assuming it's just the different passes, but I don't know how they assemble.
[1:44] So, I should check that out.
[1:49] All that is good. I'm getting the pull request on my side monitor.
[1:56] But we have this and we also have the distance.
[1:59] So, if we go and multiply the color by the distance, or 1 divided by the distance,
[2:06] we should get an interesting look here.
[2:09] Where it looks like, wow, the lights, but with no shadows.
[2:14] So, it gives a very subsurface-scattery look.
[2:16] Let me turn off the floor because that is hiding a few things.
[2:19] But we can see each and every light is doing that, and it goes and stacks up for every new light that we have.
[2:25] So, that's a very cool effect.
[2:27] It's just, well, I'm assuming it's doing under the hood. It's just taking every single light.
[2:32] It's kind of like, if you remember, like months, maybe even a year ago,
[2:37] there was the experiment with the 4Each light zone.
[2:40] I'm assuming this is like a departure or a branch of that, in a sense.
[2:46] But with this, for every single light, it does that, and I'm assuming it just goes and accumulates or adds up all the differences.
[2:54] But to get the actual shadow for this, we need to use the shadow raycast.
[2:59] So, this, if we go and attach it to the output, we see that it just gives a value that is the shadow mask.
[3:06] So, if I hide everything besides one light, we can see that we just get the shadow raycast for there.
[3:12] And this is not in screen space, as far as I can tell.
[3:15] So, we can do very, very interesting things with this, which I'm excited to play around with.
[3:22] Let's go and scale the color by the shadow part right there.
[3:28] I actually don't know if it does like a double... actually, no, that should be fine.
[3:32] But we can see here that now, as we combine that, it now has a very well put together shadow.
[3:38] And we can see all that works as intended.
[3:41] I may need to boost the light there. Let's set it to be 5. There we go.
[3:47] Now we can see all these are working as intended.
[3:50] Now, if we turn up the radius, we can see that this gets a bit softer, but it seems to be a little bit weird with the positioning.
[3:57] Maybe that's a bug.
[3:58] This is also several days old, and I know that the person who's been working on this branch has been updating it.
[4:05] So, I'm assuming that that's just a little bug with the softness, but it's not a huge deal in this scenario.
[4:13] So, now that we have just the most basic setup for lighting and shadows,
[4:17] like you would need to put in the dot product with the normal and the direction and all that,
[4:22] which actually, yeah, let's go and do it now, because I'll be introducing other stuff.
[4:28] So, with this, let's see.
[4:31] If we take the position and subtract the current position, so we get that and get that, we get the direction.
[4:39] I'm not sure if the direction there is the same as doing this, which maybe I should go and test that.
[4:45] But, just to keep the basics, I'm going to normalize this and then dot product it with the normal of the geometry.
[4:56] So, with this, if we go and multiply, once again, I should multiply the floats altogether, but it's fine.
[5:05] If we do this and this, plug that into that, plug this into that, we should see that we get a very, you know, a much more, I don't know, early days shadow look.
[5:21] This really does look like old computer graphics, in a sense.
[5:27] I still need to figure out, because I have not looked at the documentation for this.
[5:32] So, I've just been going into this, not blind, but let's see, there's diffuse light and diffuse color.
[5:39] So, it seems like if I don't have either of them, it just doesn't look quite right.
[5:44] Or, oh, wait, wait, wait, wait.
[5:45] That's because the diffuse color, yeah, okay.
[5:50] These seem to default to white.
[5:53] If I do that and that, but no, wait.
[5:57] Well, those seem fine, but either one of those, okay, so those multiplied together.
[6:02] Apparently.
[6:05] That's, ah, okay, I think I got it now.
[6:08] So, this part isn't technically needed for that.
[6:11] Even though when I, yeah, okay.
[6:14] So, those parts kind of, they maybe multiply together.
[6:17] I need to actually take a look at that.
[6:21] Let me go and get the, yes, I'll put the pull request in the thingy.
[6:32] One second as I go and get some stuff ready to go.
[6:37] Okay, here is the PR for that, if you want to take a look at it.
[6:42] Is it only EV?
[6:44] Yes.
[6:45] This time, I'm assuming that something similar would come across for cycles, but I am not entirely sure.
[6:53] So, now we have this, and let's see if the direction will do the same thing.
[6:59] I'm assuming, oh, oh wait, it actually does.
[7:01] Okay, so we can eliminate all that.
[7:04] We just get the direction of the ray.
[7:06] Oh, yeah, it's the direction of the ray.
[7:07] That makes complete and total sense.
[7:10] So, we get the direction of the ray.
[7:11] We dot product it with the surface normal, and then we get something like that.
[7:14] So, it's a very nice and simple look for silized effects.
[7:18] I'm assuming all the NPR people will absolutely love it.
[7:22] But here's where things get very interesting.
[7:24] Oh, and also there's the softness parameter right here, which I'm actually not sure what that does, but we'll need to take a look at that.
[7:32] The position parameter.
[7:33] So, this is where things get extremely interesting because we can modify this.
[7:37] I don't think with the previous zone experiment, we were able to do this.
[7:43] But we can go and offset this just with a vector, a texture, whatever we want, and it'll still just work.
[7:49] So here, I'm just straight up moving the rays, and it seems to work pretty well.
[7:56] We still have a little bit of artifacting right here.
[7:59] I'm not sure what that's about, but if we move it slightly above, we can eliminate some of that.
[8:07] We do...
[8:09] Oh, it's...
[8:10] Okay, there we go.
[8:12] Yeah, and I'm not sure if the virtual shadow mapping will lead to any issues.
[8:16] I'm assuming that is part of it.
[8:19] But we can go and manipulate this, and it is very fascinating to do so.
[8:24] So let's go and offset the position by...
[8:28] Let's just do a simple noise texture.
[8:33] Yeah, simple noise texture.
[8:35] Turn that off, go and scale, not screen.
[8:39] Go and vector math scale.
[8:41] Go and I built this build myself.
[8:45] I don't think there is a publicly available full build out there currently.
[8:52] So we have this, and as we offset the position like that, things start to get very funky,
[8:56] which is why I needed to do the clip fix, because some of the rays go below the surface, which is not good.
[9:04] So let's go and implement that clip fix so that we can restore the rays so that they don't go below the surface,
[9:10] causing the horrific artifacting.
[9:13] So to do that, I'm going to use some nice vector math.
[9:17] We need the position and the normal.
[9:20] So I'm just going to copy what I did here, but we take the new position, subtract with the current position,
[9:27] then we need to go and vector math project.
[9:30] So we project the vector along the normal, and then we add that into there.
[9:34] So any rays that are above or below the surface will just be snapped to the surface.
[9:41] So this is not inverted, which yes, of course it was.
[9:46] I think that's working now, unless I did it horrifically wrong.
[9:52] I think that should be correct.
[9:57] Yeah, I think that's right.
[9:59] It still looks a bit broken.
[10:03] Maybe it's just offsetting far too much.
[10:07] Well, it's not clipping into the surface, so I'm going to assume that that is now working.
[10:12] Let's set that to be a bit less and then we do that.
[10:15] So we're offsetting the position, giving a more stylized look, but I think we need something a bit better.
[10:21] So let's go and use a Bornoi texture and use the color to offset it.
[10:28] So that's more snapped rather than this blobby mess.
[10:32] Let this to be 0.5, plug that into the scale.
[10:35] Go and bring this over a bit more.
[10:37] And since we already have the clip fixed there, I can just keep that there.
[10:42] I'm duplicating what I have, I'll eliminate it soon.
[10:45] So here with a Bornoi texture, we get a very nice look.
[10:49] Yeah, it looks good to me.
[10:50] We turn up the detail, we can see we get a more artistic, I don't know,
[10:55] it just gives a more like fractured glass look in a sense.
[10:59] And I can just crank that up, set the roughness and everything just to make everything look very rough.
[11:05] Though we are still getting some clipping here, which I'm not a big fan of.
[11:11] So I'll need to do I need to use potentially the true normal to make that function intended?
[11:18] It does seem to fix some of it, but not all of it.
[11:21] Because again, yeah, it is projecting the surface.
[11:27] I'll need to look into that.
[11:28] I need to find more, more ways of making that work.
[11:34] Yeah, that is that.
[11:36] That is very cool.
[11:37] So since we have that, let's go back to the previous version that I had over here and eliminate the testing part.
[11:43] Or I'll just move it down.
[11:44] Make sure to include that one.
[11:46] I'll just move it down.
[11:48] We can add it to other shaders as well, but I don't think we'll need that at this time.
[11:52] So I'm just going to go and chop that out.
[11:54] So right here, I just have basically why I had before, even though I can snap the position to the Voronoi texture here.
[12:05] I'm just going to go and turn this down a bit so that we get better colors going.
[12:10] It doesn't have the dot product in there, which maybe I should include that.
[12:14] But I'm offsetting the hue of the shadows to make it look a bit better.
[12:18] Let me go and turn off a few of these that we have something like this.
[12:24] So here, let me set this to be a little bit higher.
[12:27] So the shadow parts here, they just have the hue shifted, which just makes it look a lot better.
[12:33] And then I set the value to be whatever I want.
[12:36] So let's turn that back to six.
[12:38] Oh yeah, that looks quite good.
[12:40] That looks very, very, very good.
[12:43] But let's try some other snapped positions.
[12:46] So here I have basically, we don't need the time offset in this case.
[12:51] Here I just snap the, or no, we don't want that one.
[12:55] That one is a different variant.
[12:57] Here we just snap the position, but also offset based on white noise so that the pixels are dithered.
[13:04] And this will give a very interesting pixelated look.
[13:09] So if I eliminate the dithering to that, we just have pixelated shadows,
[13:14] which may remind you of Minecraft's vibrant visuals, which are just pixel-aligned shadows.
[13:21] And it looks good.
[13:23] The one caveat being that when you have a curved surface or something that is not aligned to the grid,
[13:29] it can be a little bit funky, but I think it still looks okay.
[13:34] And again, adding in the dithering just softens, gives some anti-aliasing for all that.
[13:41] There's a light accumulation work with the volume socket.
[13:45] I would not expect that if that did work, I would be shocked.
[13:51] So yeah, no, I don't think that, it would be interesting if it did, but I don't expect that to work.
[13:57] I assume it only works on surfaces.
[14:00] But yeah, we have that, and that looks pretty good.
[14:03] And then this other test I was working on, which is just scattering the lights, giving another very interesting look,
[14:10] and also offsetting based on snap to time.
[14:14] And it also works with motion blur.
[14:16] If you have the step method for the motion blur, if we go and render this,
[14:21] that is not the best example because I need to have only one light going.
[14:25] We can see here that the shadows are actually blended.
[14:28] If I go and turn off the motion blur and go and check out this, we can see with motion blur,
[14:35] we can see, oh wait, this is happening during a snap, though it's dithering between the two.
[14:42] But motion blur does work, and it is very nice that it does.
[14:46] I would expect nothing else, nothing else.
[14:50] But yeah, what are other fun things I've tried with this?
[14:54] Oh, yes, of course.
[14:56] Simple subsurface scattering.
[14:59] So with this, I'm just going to copy this part over here.
[15:02] I'm going to move this all back.
[15:04] So here instead of snapping and then doing the subtract, I'm just going to go and scale right here.
[15:10] So simple white noise being applied into there.
[15:13] It's not spherical white noise, but I'm going to ignore that at the moment.
[15:17] So this will give a square offset instead.
[15:20] But this gives a very subsurface scattering look.
[15:24] Where the rays, it's just a very soft, well, I guess it's not accurate because the shadows are soft when they shouldn't really be soft.
[15:35] And I just reminded myself that I could apply this with white noise affecting the color,
[15:42] which can give a very, very interesting look.
[15:45] So if we go and actually do that, we go and multiply based on the white noise color, this will look very weird.
[15:54] Where again, it looks very subsurface scattering, but again, we need tons of samples to make this work because it's all white noise.
[16:03] A while back, I was thinking about a friend asked me if I could add into the light path node.
[16:14] The sample index.
[16:18] So whenever the samples would stack, I tried this out in cycles and it did work.
[16:23] The value would go higher depending on each sample.
[16:26] Now there are reasons why I didn't make a PR for that because samples can differ based on what area of the render it's in,
[16:35] if you have like variable sampling and all that.
[16:38] But in EV, I think that could be good for effects like this where you would want to jitter the effects.
[16:44] So if we had that, if I actually implemented that, that would be potentially very good.
[16:52] You could add in your own lighting that has the kind of jitter shadow look.
[16:57] But yes, yes, yes, yes.
[17:00] So here it's all like that.
[17:02] And it's quite cool.
[17:05] And we can still have colors based on material and such, though this would have to be like a post node group.
[17:11] We have one material and then we just apply the lighting node group after everything.
[17:16] This will be incredibly useful for NPR styles.
[17:19] Oh yes, of course.
[17:21] I really, I don't know much about, um, what's it called?
[17:25] GU's Studio's branch of Blender.
[17:30] Which I know that they kept it in EV legacy for a while because of the shadows were a bit funky.
[17:37] And even with this one, the shadows can be a bit funky.
[17:40] I've noticed that they're not pixel perfect in quite a few scenarios like this.
[17:46] Let me go and turn off the, yeah, let's go and turn this off.
[17:51] There are quite a few scenarios where the shadows look very artifacting even if they're supposed to be perfectly sharp.
[17:58] But this is just with normals there.
[18:00] So getting the harsh cut off might be a bit iffy.
[18:04] Like right here, let's see.
[18:08] Yeah, it's still doing some weird stuff there.
[18:12] But yeah, I wonder how this will look for like very stylized effects.
[18:16] Let me go and get, let's see.
[18:21] The value, let me try making this a bit more fancy.
[18:26] So I'll have a white noise for the orientation or do we have the random rotation?
[18:32] No, we don't have that available right now, but I could go into geometry nodes, add in the node and then rip out the internals.
[18:39] Random rotation.
[18:42] Though we don't have the, we have that, we have that, we have the map, okay.
[18:47] So I think we should be, but we don't have rotation nodes in there.
[18:51] So that's unfortunate.
[18:57] So I'll need to make something that is not entirely great in this.
[19:02] Let me think about that.
[19:04] We have vector rotate, which maybe if we do axis in the angle, we can have the axis just be whatever the angle be.
[19:17] I forget how to actually make that work.
[19:19] So I'm just going to ignore this for the time being.
[19:22] I'm going to normalize the random color and then scale this based on, scale the strength.
[19:31] Based on the white noise texture, which I think if I were to...
[19:39] I'm trying to make a gradient that I can customize.
[19:42] So if I do this and I get a color ramp.
[19:46] And then that affects the color that multiplies that.
[19:49] I should be able to get a very interesting look to our pseudo subsurface scattering.
[19:55] But we do that and that is straight up not working.
[20:02] I wonder why, because it should be.
[20:04] Why is it going red?
[20:06] Or let's eliminate the color and strictly only have this.
[20:13] Because I don't want to worry about the colors right now.
[20:18] Now it only looks red.
[20:20] So why are you...
[20:22] Ah, there we go.
[20:23] Okay.
[20:24] Now the subsurface scattering is doing...
[20:30] Yeah, but it should be varied.
[20:33] The white noise should vary it.
[20:36] I'm doing something wrong, but I don't know what I'm doing wrong.
[20:41] I'm trying to get a kind of spherical difference to the effect.
[20:49] Is that because I forgot...
[20:51] Oh, yeah, I know that explains it.
[20:53] It's because the shadow just straight up isn't being accounted for.
[20:57] So here I'm just going to plug this.
[20:59] I'm ruining my previous setups, but that's perfectly fine.
[21:02] It's fine.
[21:04] There we go.
[21:05] So we have that and that and this part needs to plug into there instead.
[21:09] There we go.
[21:10] Not the worst.
[21:11] Only partly ruins the effect.
[21:14] And of course I need to invert that.
[21:17] So there we go.
[21:18] There we go.
[21:19] Not there eventually.
[21:22] So we have it being more red where it starts off and then as the subsurface scattering progresses, it gets more blue.
[21:29] Again, I wish we had...
[21:34] Sample value in there.
[21:36] Maybe I can mod it in.
[21:39] But I have not had time.
[21:41] There is still something I need to work on.
[21:44] For Blender 5.3 to get several notes that I want in 5.3 in by just having to have time to figure out the dependency graph.
[21:52] The dependency graph is my biggest enemy when it comes to developing for geometry notes and other stuff.
[22:00] So is this going to replace the shader tar gb node for NPR?
[22:04] Actually, probably.
[22:06] This is just a better version of it, I think.
[22:10] It's been a while since I played with shader 2 rgb.
[22:15] Like this, as far as I know, I know they're playing around with translucency and maybe even transparency because I don't even know...
[22:25] Well, transparency, we don't need to worry about with this.
[22:28] We can go and just mix that.
[22:30] So if I use a mixed shader and then transparent vstf.
[22:35] If we have this with dithering, we can see, oh yeah, I put in multiple cubes into there.
[22:40] That was for more testing.
[22:42] But yeah, as we can see, that works as well.
[22:46] And then if we change this to be blended...
[22:50] And wait for it to cook.
[22:52] Hopefully...
[22:56] Uh oh.
[22:57] Oh, apparently it may not work with blended stuff.
[23:03] Maybe it's just not implemented yet.
[23:07] Because I assume then the future that will work.
[23:12] But again, this is still a very work in progress branch.
[23:15] And then ray traced transmission.
[23:18] I know that that's not working yet from, I think, what's going on with.
[23:23] That...
[23:26] Oh, there is one of the...
[23:29] There were two fixes that I did not get into this build because I built it before those were implemented.
[23:36] One says fixed transmission power and then one was fixed light intersections.
[23:40] So there may be some errors with the light intersection and transmission and invalid links.
[23:47] So maybe I should update this.
[23:51] But yeah, it's a very, very cool branch.
[23:54] So let's go and connect that into there, do that and that.
[23:58] What are more things that I can try?
[24:00] I can try snapping the white noise here.
[24:04] And again, this still isn't accurate because the rays will be bunched up towards the corners.
[24:10] But if I do this, we can see that it is indeed...
[24:18] It is snapping a bit, but there's still a lot of dithering going on.
[24:22] As far as I know, yeah, there is no radius going on there.
[24:26] Softness, there's no softness going on there.
[24:29] Do you think we can fit caustics with this?
[24:32] Oh, I didn't even think of that.
[24:34] That is a brilliant idea.
[24:37] Let me think about that real quick.
[24:40] How would that work?
[24:43] It is possible. It is very, very, very possible, I think.
[24:49] I'm not sure if we can change the direction, but we can change the position.
[24:54] Oh, yeah, that might...
[24:58] That might actually work.
[25:02] Let's see, we can also...
[25:04] Because we have the position and the direction, we can add in textures to this.
[25:10] Which I know EV by default does not allow for textures to be implemented,
[25:15] but we can add in textures and little stencils to these lights,
[25:18] but it would affect all of them unless you gave one of them a specific color or something like that.
[25:27] And we can't detect if it's a sunlight as well.
[25:30] I keep forgetting about that.
[25:32] Let's actually try a spotlight.
[25:35] So, yeah, for stuff like caustics, yeah.
[25:39] This is why I do these streams.
[25:41] That tells me things that I do not know of automatically.
[25:45] And I'm also cutting off the distance.
[25:50] That is weird.
[25:52] Let's go and kind of reset this.
[25:54] I already have a saved version of the file, so I can do whatever I want with that.
[25:58] So we have that going on, that going on.
[26:01] Let's go and mostly reset this.
[26:05] So we have the color, we have the power, we multiply that by that,
[26:10] and then we multiply the color.
[26:13] So that should be how it is.
[26:15] Very simple, not doing unnecessary calculations.
[26:18] The shadows can have a color, which I wonder what that is for.
[26:24] I really wonder what that's for.
[26:27] Maybe it's for translucent things?
[26:30] I'm not sure.
[26:32] Yes, I should have saved the...
[26:35] Well, yeah, it's fine.
[26:39] So that's all good, but I think...
[26:42] I forget if I need to enable custom distance.
[26:46] Yeah, okay.
[26:49] Because with the power, it automatically sets a distance for that,
[26:53] but I just set a custom distance so that it can extend beyond that for more stylization.
[26:58] And then there's also the blending, which I don't know...
[27:03] Okay, that's just not being taken into account.
[27:06] I'm assuming that that's just somewhat like the position,
[27:09] and yeah, there's probably more data that can be implemented.
[27:12] But yes, with this, we have the position direction and such.
[27:15] If I get the direction, could I use that for a texture?
[27:20] So let's go and use a checker texture.
[27:22] We can go and multiply...
[27:24] Yeah, let's just go and multiply that by that as a kind of post effect.
[27:28] And then we take the direction, plug that into there, and let's see what happens.
[27:32] Oh!
[27:34] That is...
[27:36] That is interesting. Does the spotlight have a radius by default?
[27:39] No.
[27:41] Dang.
[27:44] Very interesting.
[27:47] So why is it so blurry?
[27:53] You can see it's attempting to work.
[27:59] But no, no, this is very, very incorrect.
[28:04] Let's see...
[28:07] So if I take the position and subtract that from the...
[28:12] But it doesn't give us the...
[28:15] The direction gives us the direction of the ray, not the light itself.
[28:20] So we may need to transform the rotation of the light.
[28:25] We don't have access to that yet.
[28:28] But I'm assuming there'll be a lot more light information that we can go and pull from that.
[28:35] We can make pixel sorting artifacts in space now.
[28:38] I think I did something...
[28:40] Well, I haven't done that.
[28:42] Let's just get the...
[28:44] Since we have the basic thing going here.
[28:47] Go and reattach this and...
[28:49] Which one? Let's...
[28:52] I don't think we should...
[28:54] I showed off the trippy one here.
[28:56] Let's put the clip fix into there.
[28:59] So here... Oh no, I did show that one.
[29:02] But yeah, let's go and show all this where...
[29:05] Oh no, that is severely broken. I have severely broken it.
[29:08] Oh no.
[29:10] But that's... No, that should be fine.
[29:12] It shouldn't be freaking out that much.
[29:15] Oh, because I destroyed a broke-up.
[29:20] Why did I break it?
[29:22] Okay. Don't worry about that all too much.
[29:27] That looks a bit... better.
[29:30] Of everything else. There we go.
[29:33] So you can do very trippy effects when it comes to that.
[29:36] But pixel sorting, I'll need to try that out.
[29:38] Radiance cascade?
[29:40] Oh, I have a friend who's really into Radiance Cascades.
[29:44] I'll have to ask her.
[29:48] Let's see.
[29:50] I have a kind of light bleeding that we have.
[29:53] It's very cool though with this, even though I do the clip fix,
[29:56] it only fixes it for...
[30:02] perpendicular parallel...
[30:04] perpendicular to the surface normal.
[30:06] So for parts like this, it will clip underneath,
[30:09] which isn't great.
[30:11] And I don't know if there's a way to stop that.
[30:13] I don't think there is.
[30:15] But tons of cool things.
[30:17] We just animated it and just like, oh yeah,
[30:19] it's in Spider-Verse, lovely.
[30:21] Though even though with Spider-Verse...
[30:27] with Spider-Verse, from Sing the Leaks,
[30:31] it's interesting they're doing a lot more in the compositing stage
[30:36] than I thought.
[30:38] Because the renders that we saw there were...
[30:42] they looked like normal CG animation with different great instance stuff.
[30:48] So they're taking the lighting and doing much more in the compositing stage
[30:52] than like actually affecting the light rays,
[30:54] which is much more pipelineable for a lack of a better term.
[30:58] But I found that interesting.
[31:00] They're using normal rendering for quite a bit of it
[31:04] and then doing a ton of compositing stuff.
[31:08] Which is a better way of doing it, more sustainable
[31:11] if you have to render from different engines and such.
[31:15] I think I know who you're talking about.
[31:17] Yes, you most likely are.
[31:22] One of the smartest people I know when it comes to rendering.
[31:27] Let's see...
[31:31] What was I doing again?
[31:35] Let's go over here.
[31:37] What was I doing?
[31:38] Oh right, that looks trippy.
[31:41] That is lovely. Look at that.
[31:44] Not accurate in the slightest, but we're seeing the...
[31:48] just putting the normal rays into there.
[31:51] That is very, very cool.
[31:55] Let's go... I like the reds.
[31:57] The reds look very nice and fancy.
[31:59] Look at that.
[32:01] I'm still offsetting the...
[32:03] That part. Oh, that's why it's...
[32:07] I'm a moron sometimes.
[32:09] I'm like, why is it so blurry?
[32:11] It's because I literally put in the blur.
[32:13] But yeah, that's what it looks like without it.
[32:15] So that's good.
[32:17] If you can't tell from my voice and face...
[32:20] Oh, we have 53 people here. Hello!
[32:23] What were you all doing?
[32:25] I am a bit tired today, which I know is not uncommon for me.
[32:29] It is...
[32:30] Unfortunately, me being tired is a much more common occurrence these days.
[32:35] Even more so than before.
[32:37] I need to get that fixed.
[32:39] Let's just go and turn that part up.
[32:42] So yeah, that is the normal...
[32:44] Or we can just directly plug in the direction into there and take a look at it.
[32:48] Yeah.
[32:49] And of course, we get negative...
[32:51] Oh, negative lights.
[32:53] Negative lights will work with this.
[32:56] So if we apply more of these, we can subtract light.
[32:59] Oh, that'll be very interesting.
[33:02] And if...
[33:05] Yeah.
[33:08] Let's see.
[33:10] We have the power there.
[33:12] Which the power, I assume, is just the float value for how powerful the light is.
[33:18] Which if we need to ever encode like certain light effects with an index, we can go and use that for like...
[33:26] Oh, if it's 50.03, you know, if it's equal to an arbitrary value, then just switch to this mode.
[33:34] We also have the colors for that as well.
[33:36] Do we get the alpha from the...
[33:38] Is there an alpha?
[33:40] I assume not.
[33:42] No.
[33:43] Okay, there is no alpha channel.
[33:44] That makes sense.
[33:47] So...
[33:48] I'm just going to play with the spotlight.
[33:53] So we don't...
[33:54] I don't think we have a texture coordinate for the spotlight.
[33:58] And I'm not sure we can get it because we don't have access to the rotation.
[34:04] Yeah.
[34:05] There's still information that could probably be retrieved in other ways.
[34:10] But for the spotlight, again, the angle that affects the shadow there.
[34:15] The softness, the softness is still a little bit broken there.
[34:20] And then area lights.
[34:22] We can see that when we do that.
[34:24] Oh, area lights don't seem to be supported yet.
[34:28] We can still jitter, which jitter seems to fix.
[34:31] Or is it still biased towards another side?
[34:36] But yeah, that part is still available, which keep in mind, I have jitter enabled there.
[34:41] Whenever you need actually accurate shadows, turn on jitter.
[34:44] It just...
[34:45] That's just...
[34:46] It just works.
[34:49] So for the spotlight, if we have jitter shadows and we do that, we have that available, though it's not affecting the cone.
[34:55] Which the blend there is...
[34:58] Probably supposed to be done in the shader.
[35:02] So soft fall if we don't need to worry about that.
[35:07] Yeah, that works interestingly.
[35:10] Oh, and maybe.
[35:12] I know I was white no...
[35:14] No, we can't white noise the direction.
[35:16] No, I kind of wish we could white noise the direction.
[35:19] Maybe that could be implemented later.
[35:22] I'm just spitballing here.
[35:24] Spitballing...
[35:25] There are some outdated parts of my vocabulary that I really need to...
[35:30] Update.
[35:33] Let's see...
[35:37] Hmm...
[35:39] Rotations are a must have in my opinion.
[35:41] Yeah, because again...
[35:44] Costics.
[35:46] I'm assuming with caustics we'll need the...
[35:51] And caustics work with this.
[35:53] I really don't know.
[35:59] With the shadow ray cast.
[36:01] I'm not sure if we can do caustics because it requires...
[36:07] Accumulation of the light rays.
[36:10] While this accumulates each light.
[36:14] I'm genuinely not sure.
[36:19] We manipulate the position.
[36:21] No...
[36:22] Hmm...
[36:26] Because I need to think about this in a different way.
[36:31] If we manipulate the position...
[36:36] Because this position, it's not the light position.
[36:38] This is affecting the geometry's position that it sees.
[36:42] So when we manipulate this, even by adding to it, I'm assuming...
[36:47] That's offsetting...
[36:50] Rays and therefore the direction of that.
[36:55] Because again, we can just straight up do that.
[36:58] And as we can see it is playing with the...
[37:01] I'm assuming virtual shadow maps.
[37:03] And then we can also do that and that.
[37:05] So we are changing the direction as we can see.
[37:09] I'm not sure if we can do caustics with that.
[37:15] Hmm...
[37:16] And actually, does that have a tooltip?
[37:18] No, that does not have a tooltip.
[37:20] The cutoff distance, yeah, I know what that's about.
[37:24] Yeah, I need to...
[37:27] As this develops, and this is very powerful already.
[37:31] Because we basically can put the light rays wherever we want without having to rely on...
[37:36] View direction.
[37:38] Which is very, very good.
[37:41] If we get access to the direction, then I can implement my kind of baking setup to this.
[37:47] So we can bake the shadows for certain things because it's not dependent on...
[37:53] There probably will be other errors, but it's not fully dependent on view direction.
[37:59] That is extremely interesting.
[38:05] Yeah, what else...
[38:06] What else could I try?
[38:10] I don't know.
[38:14] Textures, we still need the other thing for...
[38:17] Oh wait, no, that's what I was going to try.
[38:19] Just subtracting the light position from the geometry...
[38:25] Come on buddy.
[38:27] Oh my gosh.
[38:30] My brain and my mouse are not in sync at the moment.
[38:34] There we go, flip that around.
[38:38] So here we have a difference, yeah, it just localized to the site.
[38:42] So it's kind of like a texture, but the rotation doesn't matter.
[38:46] Which is interesting.
[38:47] We can pull the rotation data from the attribute node, but that is less than ideal.
[38:54] This node is just pulling all the way down.
[38:57] Yeah, I hope we can get that in the future.
[39:01] There's a lot of data that can just be pulled like the angle of the spotlight and stuff.
[39:07] There's a lot of information that could be pulled, I assume.
[39:14] Let's go and disable the offset.
[39:16] So yeah, we have...
[39:17] We have a lot of data that could be pulled.
[39:20] I have pulled, I assume.
[39:24] Let's go and disable the offset.
[39:26] So yeah, we have a stencil, which means that we can implement gobos.
[39:31] But as we can see, it's for all of them.
[39:35] So if I were to, say, do something like that, that is trippy.
[39:45] This is so trippy.
[39:48] I'll call you bake shadows if the node won't work in cycles.
[39:52] No, I mean, like, I have a setup where I can project a object's geometry into its UV space
[40:01] and then just render that normally in its UV space as a form of baking.
[40:05] I do that in cycles because it has the raycast node that's fully functional when it comes to stuff that's outside the view angle.
[40:12] EV, unfortunately, doesn't have that.
[40:14] But with this, I may be able to do it.
[40:20] Could you do shadows that have different colors around the edges?
[40:26] I am not sure.
[40:31] I could if I could manipulate the direction.
[40:35] If I could manipulate the direction, which that may come around in the future.
[40:40] Or is that even possible?
[40:45] Would that even be possible under the hood? I don't know.
[40:48] But if I would be able to do that, let me think about this real quick.
[40:53] I assume because when you have a light, then you change the softness.
[41:02] Right here.
[41:04] Is this changing the position of the light?
[41:08] Or the rotation?
[41:10] I'm assuming it's changing the position here, but how does it figure out that?
[41:15] Is it's not applying a kind of subsurface scattering look, which we tried out previously because it's affecting the geometry position.
[41:22] It's not offsetting the actual light position.
[41:26] Maybe that's the thing.
[41:29] This position here, it's not offsetting the light's position. It's affecting the geometry position.
[41:36] Or...
[41:38] Wait, what's the difference between the two? Wait, let me think about this.
[41:45] If I'm... Okay, I just need to think about inverting it, which my brain doesn't want to do right now.
[41:52] When we jitter the position of a spotlight, every single frame is picking a different area inside this.
[42:01] Every frame is like, oh, the light's actually over here, actually over here, actually over here, actually over here.
[42:06] Which means that it's... Yeah, no, that's possible. What am I talking about?
[42:11] The geometry, if we were to do this here, the geometry would subtract a little bit with the sample a little bit from that, a little bit from this, a little bit from that.
[42:21] So it is possible. When I white noise...
[42:24] You know, when I white noise, it should be doing basically the same thing.
[42:32] Let's give it a go and see if I'm just hallucinating.
[42:36] Which, unlike an artificial intelligence, when I hallucinate, it's...
[42:42] Actually has some logic behind it, I think.
[42:45] I'd like to imagine.
[42:48] Subtracts.
[42:50] Let's go... Wait, five, scale, play the end to there.
[42:56] So if I do this, but it's giving...
[43:01] That is a problem, because it's...
[43:07] Yeah, now, what is the difference between that and that?
[43:13] That's the shadow. Yeah, no, it's... No, no.
[43:18] We would need like an offset light position here.
[43:24] Or changing the direction. I don't know how that works.
[43:27] So at the moment, we can't do that, because it doesn't actually affect the...
[43:35] No, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, wait, sorry.
[43:38] It's because this is a spotlight, it has that harsh cutoff.
[43:47] Wait, wait, wait, wait, wait, wait, wait, wait.
[43:50] Oh, the softness of...
[43:53] Yeah, and okay, let's switch this to a point light so that's a little more understandable for my small little brain.
[43:59] Here we have that, and it does that, but it doesn't bunch up when it comes to there.
[44:04] When I do that, and then also turn the radius down to zero,
[44:08] you get the classic subsurface scattering look on the part there.
[44:12] Because some of the rays can't fire because they get blocked.
[44:19] See, also tangent to this, have you seen the recent PR adding string socket support to shader nodes?
[44:24] Yes, and I am very excited for that, because, well, mainly, strings...
[44:30] With, like, the volume node, that has a string socket and has had that for ages.
[44:35] But it was such a weird quirk of the shader nodes,
[44:39] where it's just like you have a string socket, but I don't think...
[44:43] Yeah, let's take a look at this right now, just has a nice little tangent.
[44:46] We'll look at the, of, principled volume node.
[44:49] It's like, oh, you have just a string in there, nice.
[44:52] Node group.
[44:56] Oh, wait, we do have string sockets in the node group.
[45:00] Oh, I actually did not know that.
[45:03] Hmm, how about that?
[45:05] Well, that's actually good to know.
[45:07] That is nice. I've never actually had to do that before.
[45:10] But for stuff like the attribute node and stuff like that, these need string sockets.
[45:16] Or the, um...
[45:19] The, what is it? The geometry? No, not that one.
[45:23] Tangents.
[45:26] Input tangent, yeah.
[45:28] Or the UV map with the tangent. We need that so that these are node group compatible.
[45:33] It just makes things better if you go, if you could go and put in a string for those kinds of things.
[45:40] And then the actual UV.
[45:42] But the actual UV map node, I think having a string socket in there would be nice as well.
[45:49] So just to make things more node group compatible, I have like a parallax node that is limited by which UV map you select.
[45:57] Yeah.
[45:58] Yeah.
[46:00] So if we go and make a group there, unfortunately, yeah, those are non node group compatible.
[46:07] There's a very good shift with Blender pioneered by the geometry node side.
[46:14] Or it's like, oh, you know, we need to make everything node group compatible so that things can be turned into assets.
[46:21] Because before in Blender, I think the assumption was everyone will just go to the node group.
[46:26] Everyone will go to the node editor to change their things.
[46:31] But as soon as things start to get complex, which with geometry nodes and anything that has to be done in a production, things get complex and you need to go and make it node group compatible.
[46:41] Like again, at the image texture node, and I guess the image sequence node.
[46:47] Oops.
[46:49] Or yeah, they're the same thing.
[46:52] This node needs basically a completely new version of the node to be node group compatible.
[46:59] I've looked into this, I can't do it.
[47:02] But I've I've made a couple of mock ups where it's like, okay, this node will need to be a XR compatible, you dim compatible image sequence compatible with a input for which frame it's going to be on, which that is something I really, really want to get.
[47:20] There's just so much that kind of needs to be done to make the image texture node actually to date.
[47:31] And the texture socket is one of those and it needs to be in single geometry nodes.
[47:37] So there is a lot that needs to be done.
[47:40] Like this, this would probably this is probably like five updates away, if I'm being honest.
[47:45] It is a very there's so much planning that needs to be done for this node to actually update it and bring it up to speed.
[47:53] Because I have needed this texture to be you dim compatible in geometry nodes.
[47:59] Unfortunately, it is not.
[48:01] So that node, I don't have the ability to upgrade it, but I need to figure it out.
[48:09] Anyway, we also need a string socket for image names.
[48:14] Yeah, I believe mod wanted me to try making a image import node, which would you would import a pile path and then an input a texture that would be very useful.
[48:29] I just don't have time to try to implement that, especially in the shader editor.
[48:34] I do not want to attempt to do that in the shader editor.
[48:36] I made one node in the shader editor, just one node to get the scene data, and it kicked my ass.
[48:46] It kicked my butt.
[48:48] Sorry, some of the real me just popped out for for a bit there.
[48:53] This node thoroughly kicked my butt.
[48:58] Just because getting the data, making it compatible with cycles, fixing all that stuff.
[49:06] I learned so much that I never wanted to know about Blender's internals when it came to cycles.
[49:12] It was a pain.
[49:14] There was stuff.
[49:17] I needed to put in a new struct.
[49:19] The the devs were like, oh yeah, we need a new struct for potentially more scene data in the future.
[49:24] Daring today, are we?
[49:25] Daring today, are we?
[49:32] My streams are very PG for a little Timmy watching at home.
[49:39] But yeah, it's funny.
[49:43] Clip it. No, you don't need a clip.
[49:45] I'm not a regular streamer.
[49:47] Even though we do have 50 people here, which is amazing for a Blender stream.
[49:52] That is very, very impressive for a Blender stream.
[49:57] But yes.
[50:00] So yeah, there's there's a lot of stuff that needs to be done to bring the shader editor up to date.
[50:05] Things like the compositor.
[50:06] Let's see what was added into there.
[50:08] Oh, look at that.
[50:10] I have no idea what that's about.
[50:12] Looks like a glitch.
[50:14] But the compositor.
[50:16] Let's see.
[50:18] In 5.3, they ported more.
[50:21] Oh yeah, the transform nodes.
[50:24] Separate and combine transform, which I'm actually I actually forgot that we didn't have that.
[50:29] In there.
[50:31] But this got such a huge this editor has gotten such a huge overhaul.
[50:35] It is amazing to the point where it's so good that I used.
[50:40] I did that entire Blender 5.2 update video completely in 5.2.
[50:45] Because I could add in all my fancy transitions using the compositor.
[50:49] It was amazing.
[50:51] If you use an adjustment layer, you can just go and throw things into there and it just applies the compositor stuff in the sequencer.
[50:58] It is great.
[50:59] We can do so many amazing things with the compositor and such because it's just it's so good.
[51:07] Now there are things that I have a few little.
[51:09] I have a few little like this node.
[51:15] It could use a texture socket as well and other upgrades, but that's for the future.
[51:24] That is for the future.
[51:26] Because again, the XRs, we can only access XRs in the compositor and then getting the data and opting the data can be a little bit funky,
[51:34] especially if you try doing that with Python or dynamically getting it from different file paths with it can be a pain.
[51:42] But yes, I've looked the new 3D to screen space nodes in the compositor.
[51:46] Oh yes, I remember.
[51:47] Let's see.
[51:49] On beams.
[51:51] Let's go and set it to be, let's see, active camera and then the camera info node.
[51:57] Also back when I was looking into several people tried making the camera info node back in the day.
[52:05] But it was 3D to screen space.
[52:13] Actually, how does that work?
[52:19] Oh, because they have the transform point.
[52:21] Oh, that's how it would work before.
[52:23] Oh, okay.
[52:24] So we got 3D to screen space.
[52:27] Yeah, and then we do that.
[52:28] I'm pretty sure.
[52:30] Alley to the sunbeams being consistent in their direction, but I'm actually not sure.
[52:38] So we point this to be very high in the sky.
[52:41] Yep, kind of.
[52:43] The one that gets to those kinds of angles, it can be weird.
[52:49] Actually, no, no, that's not working.
[52:54] How would that function because it would be more like this when it went there.
[53:00] So maybe it's green to 3D space.
[53:07] I forget how to actually make that work.
[53:11] Oh, actually, no, that is very much more broken.
[53:15] There should be something like that to that, right?
[53:20] I forgot someone did it and I forgot how to do it, but of course, the composer is absolutely amazing.
[53:30] I also love the, what was it?
[53:33] Tune image.
[53:35] This is a very nice node group just to make things look a lot better.
[53:39] It's just so convenient to just add it in and then do the color boost, which how do they actually do the color boost?
[53:46] Oh, you turn up the saturation.
[53:53] Oh, wait, no, that's all only when reserve colors, that's literally just turning up the saturation.
[54:03] I thought they did something a bit different when it came to that.
[54:07] Interesting.
[54:09] But it works very well with like A, G, X and Aces.
[54:15] Yeah, lots of fun stuff. You love to see it.
[54:19] But we are very off track at the moment.
[54:22] So let's go and chop this out, go back to the shader editor.
[54:26] We were talking about the light angles and making the shadows have colors.
[54:34] So...
[54:37] Hmm.
[54:41] Let's see, please say hi Rumi, hi Rumi. I loved your movie. It was very good.
[54:46] Well, the best Netflix movies I've ever seen.
[54:52] Let's see, not really the current topic, but I feel like bundle manipulation is so much better with lists, lists length and get nested bundle path and repeat zones.
[55:01] We don't have that in the compositor in shaders.
[55:05] I think, I think they are porting bundles to the shader editor.
[55:12] I'm not sure about lists.
[55:16] Yeah.
[55:19] We're testing light angle, maybe you can test it by making IS like textures.
[55:24] I don't think those work in AV.
[55:26] I'm not, I've only used IS lights a few times.
[55:31] In projects, I should use them a bit more often.
[55:36] Yeah, look how trippy this looks.
[55:41] Everything just being so customizable and weird. You love to see it.
[55:48] Let's see, let's see, let's see.
[55:51] So what else? So...
[55:54] Avoiding the subsurface scattering look will be interesting.
[55:59] Because again, we're changing the geometry position per pixel using this, which is incredible.
[56:05] We can make like x-ray effects, I think.
[56:08] Lots of very, very interesting things can happen because if I multiply this and just set it to the z-axis,
[56:14] we can see that we only get subsurface scattering on one axis and we can also make it depend on the norm.
[56:21] Oh, wait a second. If I do a vector rejection.
[56:26] If I go and do this,
[56:31] if I take the offset,
[56:37] maybe that'll work.
[56:41] If I take this and then subtract to do a vector rejection,
[56:47] I'll make it so that it'll always be parallel to the surface making it so that
[56:52] this will still be subsurface scattering-ish.
[56:57] It'll be very, very weird. So I'll only move on the local x and y and not the z.
[57:05] So here we're no longer getting. If we take a look at this, we get the...
[57:12] Let's go and turn off the checker texture for the time being.
[57:16] We get this kind of look because it's going inside the mesh.
[57:20] Doing that, but if we turn that part off,
[57:23] you can see that it looks a lot less weird. If I'm doing it correctly,
[57:27] we're projecting along the normal and then we're subtracting. Yes, that should be the case.
[57:40] Oh, wait. Is that how the clip fix should work?
[57:45] But no, if it's an arbitrary position...
[57:52] I don't know. I actually don't know.
[57:55] Maybe I just need to apply the regular clip fix in order to make it work.
[58:00] Because it's not upsetting that they're there, but it's doing that.
[58:04] And it's leading to artifacts like that because it's the...yep.
[58:15] Yeah, I think...
[58:18] I don't even see what other data could possibly be pulled into that.
[58:24] Yeah, I'll need to...
[58:26] I think we're almost at an hour, so I think this will be a good part to end the stream.
[58:32] Lots of very, very interesting stuff.
[58:36] I'm excited to see how it plays out in the future.
[58:40] Because even right now it is quite powerful.
[58:45] I want to see what else it can do.
[58:47] Oh, that's a cool pattern right there. Very unintentional, but quite cool.
[58:53] And again, that's a great...
[58:56] Oh, and also...that's the reason why...
[58:59] Oh, whoa!
[59:03] Whoa!
[59:06] That's trippy.
[59:08] And that's because...
[59:10] Oh, okay, so it just blurs it, but since it was offset just a little bit, it gives that very weird 3D effect.
[59:17] Very cool.
[59:20] Yeah, that's why that wasn't doing it.
[59:22] Because we were blurring the shadow, but not actually blurring the texture position.
[59:28] So again, that shows that...
[59:31] We're not offsetting the light position, we're offsetting the geometry position.
[59:35] In different phases.
[59:40] Oh, yeah, that is fascinating.
[59:45] And then if we can offset...
[59:47] If we get the direction input or a light position input, both of those will, I guess, make us be able to do the same thing.
[59:56] As if we get the direction, we can offset the direction, and then subtracting the position, we can go and make that basically a position.
[60:03] Yeah, so either or would work with something like that.
[60:12] Yeah.
[60:15] I mean, maybe if you place a plane parallel to a light direction, you may be able to see how the light is distributed.
[60:22] Ah, okay.
[60:25] Yeah, let's go and take a look at that, actually.
[60:28] What a nice plane.
[60:30] Oh, and this is what it looks like if you don't have...
[60:32] A material on it, because again, this is per material.
[60:37] Again, if we look at this right here, we can just see how that's going.
[60:41] And also, I should mention, because I've neglected to do this part, since we have the distance, we can go and put in something like a noise texture,
[60:50] and modulate this based on the distance from the light.
[60:54] So we get a very interesting, spherical thing happening right there, which can lead to extremely trippy effects.
[61:04] Where you have multiple lights going, and then...
[61:08] Yeah, almost like a...
[61:12] Yeah, water droplets.
[61:16] That's really cool as well.
[61:18] If we can't dither the actual distance because of the aforementioned light inputs, there's so much to attempt with this.
[61:29] I'll be looking forward to trying it more and more.
[61:35] So cool.
[61:37] Ripple caustics.
[61:39] Yeah, but then...
[61:42] I don't think these accumulate.
[61:46] In the way that you think, or in the way that caustics would require.
[61:51] But I don't think we can do caustics with this.
[61:56] Maybe. I'll need to look into that a bit more.
[62:01] And we unfortunately can't do stuff like radiance cascades, because we don't have the direction input either.
[62:08] So we need the direction input, or the light position input either, or...
[62:13] To make this function.
[62:17] So I need to do a lot more research into this.
[62:21] So let's go and delete all the other spotlights and give them back to the original part here so that we can...
[62:27] Oh, I screwed this up so much.
[62:31] Yeah, let's go and restore the original here, even though I have a save file ready to go with all that.
[62:37] Less than. We'll just go and use that to set...
[62:41] That sets the power, that sets the shadow color.
[62:45] We'll set this to be 0.3, and then offset the hue to be 0.5.
[62:50] To get some very nice looking shadows going.
[62:53] Play it so that we get the very nice...
[62:56] Look there, it looks so good.
[62:59] Look at that.
[63:01] This is just by offsetting the position based on pixels.
[63:06] We can go and make these pixels much more like this, giving a very interesting look.
[63:11] Not quite pixel sorting, because that requires sorting.
[63:16] But we get a lot of very cool stuff going on.
[63:22] So we go and turn that up a ton.
[63:26] Actually, if I were to just...
[63:29] Is this just an overcomplicated way of doing vector rejection?
[63:34] Maybe it is.
[63:37] Though, no, I'm offsetting the position there.
[63:41] The reason it's like this is because sometimes the position is pre-snapped to a position.
[63:48] And I just want to offset it afterwards, so yeah, no I need that.
[63:52] Let's see.
[64:00] Let's see.
[64:04] Do, I could go and make this much slower.
[64:10] But yeah, it is very good.
[64:12] And it seems like it's pretty good even with motion blur and stuff like that, if you use the stepped method.
[64:20] Oh, very, very cool to see.
[64:23] What else was I going to try?
[64:27] There was a sunlight that I had.
[64:29] Yeah, look at that.
[64:31] With the pixel aligned shadows.
[64:35] I should really label this.
[64:37] All these.
[64:39] But yeah, if you want really nice looking Minecraft shaders and all that, go and do that for very nice looking light effects.
[64:49] I think if I were to turn down the dithering, yeah, there we go.
[64:54] Little bit better because it offsets in the positive and negative.
[64:59] Little bit of anti-aliasing, but if I turn it off all the way, we just get perfectly pixel aligned shadows, but that also leads to some getting missed because of course, if a model is too small for it, let's do 0.1.
[65:17] I just do that, but actually that looks much better as well.
[65:23] Oh yeah, look at that.
[65:25] But these, since it's like that, since it is an angled surface, it's unfortunately weird.
[65:33] Though I could, if I wanted to transform, vector transform from the world to the object, do the snapping and then do it back, which I think these should be on point.
[65:49] And then this will be from object to world.
[65:55] So I think that's working.
[65:57] Yep, that is working.
[65:59] Or if it's aligned to the object, you can go and do that.
[66:03] Let me go and apply the scale.
[66:06] But yeah, it is possible to make it aligns like that, though for curved surfaces, yeah.
[66:13] Still doesn't work perfectly.
[66:17] Yeah, that is so good.
[66:20] So good.
[66:21] So let's go and reapply.
[66:24] Let's see, we still have, yeah, that look.
[66:30] It looks so good.
[66:32] I do think my favorite is this kind of, you know, weird pixel offset, which actually was an error because I accidentally set this to be one dimension instead of three dimensions.
[66:43] If we set this to be three dimensions, it's just the standard, yeah, that kind of standard dithering.
[66:48] Though if I had other textures, could look very, very good.
[66:56] But for now, I think it's good.
[67:02] Are you able to do a custom volume print with that?
[67:07] I'm not entirely sure what you mean.
[67:10] It doesn't work with the volume part there, which, you know, I wouldn't expect anything else.
[67:16] Because this is still, I'm assuming very early days.
[67:21] Amazing it works as well as it does.
[67:25] I know what the shadow raycast one of my friends have, has wanted a mask for that for so long.
[67:33] I don't know if it will ever be ported to cycles.
[67:36] I assume that will be a massive undertaking with the different features, of course, because the cycles has a totally different method of dealing with them.
[67:46] The lights and shadows.
[67:49] Again, what we have here is still so, so good.
[67:56] What else was I going to talk about?
[67:59] With the 4E July.
[68:01] Oh yeah, that looks good.
[68:03] Writer.
[68:05] Hey, writer, it looks better.
[68:06] But what if I were to set this to be the power of two?
[68:11] What about that?
[68:12] I'm just going to try some stylization because we are...
[68:16] Oh, look at that.
[68:19] Does that look good or terrible?
[68:20] I don't know.
[68:21] And we can invert it.
[68:24] I am always biased to like, oh, let's crank up the contrast.
[68:30] But that, let's try dot-producting the position, the direction and the normal again, yeah.
[68:38] Dot-products.
[68:39] And then I can power that instead and then multiply it.
[68:42] So that, and then we get the geometry normal.
[68:48] That into there, and then we can, yeah, just multiply that again.
[68:54] We can get some very interesting looks with this.
[68:58] So this would be like the alternative that we put into like the glossy light.
[69:04] Do stuff like that.
[69:06] And invert it.
[69:07] There's so much we can do.
[69:09] Yeah, even with the power of one, still gives a kind of, not an early 2000s look.
[69:18] We can still do whatever we want.
[69:21] Yeah, look at that.
[69:22] Wow, that feels so...
[69:24] No retro.
[69:28] I think I like it better when it's not like that.
[69:31] Just my personal tastes.
[69:33] Feels more flat, more cartoony.
[69:36] Yeah, all that.
[69:39] What does the glossy socket do in the light accumulation node?
[69:43] I'm pretty sure it just adds on top.
[69:46] So if I were to just put in this,
[69:52] boomie if that multiplies there and there.
[69:57] So that's what we're gonna do.
[69:59] We can see if that multiplies there and there.
[70:03] So if I were to do this, we can see this gives some highlights there
[70:11] based on where the light is.
[70:15] I think it adds on top.
[70:18] And then I can multiply that by the color and so on.
[70:22] But there's a glossy light and I need to review what these actually do.
[70:27] I kind of don't know.
[70:31] I have forgotten.
[70:33] Because again, we have the passes for the diffuse light, diffuse color,
[70:37] and then the specular light and specular color.
[70:42] Which actually, let me go and check.
[70:44] Yeah, let's see what these actually do.
[70:48] Really quickly.
[70:49] Oh.
[70:53] Why is that avoid?
[70:55] Oh, and what happens there accumulates in the screen space effects?
[71:00] Nice.
[71:04] So we got that in that.
[71:05] So let's change this.
[71:07] Been a while since I have done like really deep compositing.
[71:12] Oh, okay.
[71:13] So specular color, specular light.
[71:15] Okay.
[71:16] And then diffuse color and then diffuse light.
[71:18] Oh, okay.
[71:20] Right.
[71:21] So that does the indirect lighting.
[71:23] That does the.
[71:25] Yeah, the diffuse.
[71:26] Of course.
[71:27] Of course.
[71:28] Yeah, no, I'm.
[71:30] Right.
[71:31] No, I'm sorry.
[71:32] I'm sorry.
[71:33] I'm sorry.
[71:34] I'm sorry.
[71:35] I'm sorry.
[71:36] I'm sorry.
[71:37] I'm sorry.
[71:38] I'm sorry.
[71:39] Right.
[71:40] No, I'm sorry.
[71:41] My brain is just not up to speed today.
[71:44] There's a specular light and then there's a specular color.
[71:47] Of course that just multiplies.
[71:50] Yeah, of course.
[71:51] Of course.
[71:52] Of course.
[71:53] Of course.
[71:54] So with this one, this would be for now for the.
[71:57] Glossy color and then that would be multiplied by whatever and then that's the glossy light.
[72:02] Then the diffuse color just manipulates the.
[72:06] Yeah.
[72:08] I just need a color.
[72:09] So this would be the.
[72:13] RGB.
[72:14] What is the constant input?
[72:18] Color color.
[72:19] Oh, that's that's what it's called.
[72:22] Here, if we take a look at the final.
[72:25] And bind.
[72:26] There we go.
[72:28] That multiplies by that and then we get that and that's all good.
[72:33] And then the glossy color, we just get that and then that's manipulated by the.
[72:39] For now, are these added together or.
[72:44] Yeah, okay.
[72:46] Right, I'll need to look into more of that later.
[72:52] Then yeah, the diffuse color just multiplies it all by one.
[72:57] That's what it looks like normally.
[73:02] So yeah, it should be like this.
[73:07] You think and then this I was like, oh, it looks so much better because I'm setting it to be the power of two.
[73:13] Essentially.
[73:14] So let's make this right.
[73:17] We have that and that and then that is that there we go.
[73:23] And then let's delete the balls.
[73:26] Go and do that and then do that.
[73:31] So if you just want the raw part right there, you could just go and do that.
[73:36] But classically, I'm like, oh, set it to the power of two.
[73:39] It looks so much better.
[73:40] It does.
[73:41] But, you know, I should do that in here rather than just doing it there.
[73:48] So yeah, not bad, not bad for nice stylized effects.
[73:54] Okay, do the diffused and glossy sockets not change how the lighting is computed?
[73:59] I imagine it's not just for grouping what goes in what render pass.
[74:04] I'd assume so.
[74:06] I actually don't know.
[74:08] Let's go and take a look again with the diffuse color.
[74:12] If I go and put in a color color here, we can see, yeah, that manipulates that.
[74:18] So we are directly changing the passes.
[74:24] You can do this pixel style Minecraft shader when reflections on blocks are pixelated up to texture resolution.
[74:34] I am not sure.
[74:37] Maybe.
[74:39] Though it wouldn't apply to indirect.
[74:42] With all this, I don't think it would work with indirect lighting.
[74:46] Does this work with indirect lighting?
[74:49] Because, yeah, with the, you know, specular light and such.
[74:54] Yeah, this just directly puts it into the passes, which is nice.
[75:00] So if you ever want to transfer some data without using AOVs, you can do that.
[75:05] That also affects our other objects will reflect it.
[75:08] Because again, when we had this guy right here, we can see that it is really affecting it.
[75:15] Even though we're not seeing anything.
[75:18] We aren't really seeing anything.
[75:23] Yeah, wait, why aren't we seeing?
[75:25] Oh, because we're only viewing that pass on.
[75:28] It does affect the passes, which is nice.
[75:33] Yeah, that is very, very cool.
[75:36] And I think that's everything for today.
[75:40] Let's see.
[75:41] In theory, you can compute glossing the diffuse pass and vice versa to torture your composing artists.
[75:48] Yep.
[75:49] Yes, you can.
[75:50] Yes, you can.
[75:54] But with this, I guess compared to composing workflows, we're literally changing.
[75:59] Like you can't do this effect in composing.
[76:02] You just can't.
[76:03] Because you're actually affecting where the light rays are interacting.
[76:07] But if you ever need to do these kinds of effects in the compositor, you know, just output all the passes in a multi-layer EXR and call it a day, which, by the way, if you didn't know, if you want to set the default.
[76:25] The default multi-layer EXR outputs in the node here.
[76:32] Here, let me go and fix this.
[76:34] Because with the XRs for different programs, they need to have a default EXR input.
[76:40] And all you need to do for that is set this to have no name.
[76:45] Because in the EXR metadata, it would show like image dot RGBA if it's a, you know, with alpha and all that.
[76:54] But most programs look for just RGBA.
[76:57] So you just eliminate the name and I'll set that as the defaults.
[77:01] Something I learned recently.
[77:03] And now I've spread the knowledge to you all.
[77:05] If you're working in a production that needs the EXRs to be specifically laid out and have a default, you just do that.
[77:16] I love EXRs.
[77:17] And also make sure you always turn on WAA or else you will have a single frame that's like three gigabytes in size.
[77:27] Never do that.
[77:29] Always turn on compression.
[77:30] Memory is too expensive nowadays to have stuff uncompressed.
[77:35] And in industry scenarios, things are compressed.
[77:39] It's just way too much data.
[77:42] You...
[77:45] Don't have your stuff uncompressed.
[77:47] It's fine.
[77:48] Just don't have it compressed.
[77:49] It's fine.
[77:50] Most people will be viewing your stuff on YouTube anyway and that has atrocious compression.
[77:58] Anyway, anyway, anyway.
[77:59] Getting off track.
[78:00] But yes, very nice and stylized effects in this branch of Blender 5.3.
[78:06] I don't know if it's going to be in Blender 5.3.
[78:09] Again, here is the PR.
[78:12] You do need to build it yourself.
[78:14] I do have...
[78:17] I made a build and I put it on my Google Drive.
[78:20] So if you're really pressed on wanting it, just let me know and I'll probably send you the link.
[78:27] Though I should probably update it.
[78:31] But yes, it's all...
[78:32] It's very cool to see.
[78:34] I really like where Blender is going.
[78:37] And it is amazing.
[78:39] So, thank you all for watching.
[78:41] I hope you all enjoyed.
[78:43] And yeah, I will please send the link.
[78:47] I'm hesitant to put it in the YouTube chats.
[78:51] So just send me a DM on one of the platforms and I'll send it your way.
[78:55] For a limited time, if you're viewing this in the future, I probably won't because it will probably be deleted.
[79:01] Or this may be merged into Blender, so limited time only.
[79:06] But yes, I hope you all enjoyed and I'll see you all next time.
[79:09] Have a good one.



---

## Captured Frames

- [1:16] tutorials/frames/npr-light-accumulation-blender-53-branch-testing/frame_000.jpg
- [3:06] tutorials/frames/npr-light-accumulation-blender-53-branch-testing/frame_001.jpg
- [5:05] tutorials/frames/npr-light-accumulation-blender-53-branch-testing/frame_002.jpg
- [8:07] tutorials/frames/npr-light-accumulation-blender-53-branch-testing/frame_003.jpg
- [10:45] tutorials/frames/npr-light-accumulation-blender-53-branch-testing/frame_004.jpg
- [13:09] tutorials/frames/npr-light-accumulation-blender-53-branch-testing/frame_005.jpg
- [15:24] tutorials/frames/npr-light-accumulation-blender-53-branch-testing/frame_006.jpg
- [27:28] tutorials/frames/npr-light-accumulation-blender-53-branch-testing/frame_007.jpg
- [44:04] tutorials/frames/npr-light-accumulation-blender-53-branch-testing/frame_008.jpg
- [65:07] tutorials/frames/npr-light-accumulation-blender-53-branch-testing/frame_009.jpg
- [70:11] tutorials/frames/npr-light-accumulation-blender-53-branch-testing/frame_010.jpg

---

> **Experimental/unreleased feature warning:** This entire video is a live exploration of an **unmerged, experimental EEVEE branch** of Blender (self-compiled by the presenter, a Blender developer, from a work-in-progress pull request) that is NOT in any public Blender release as of recording. None of the nodes described here (Light Info, Shadow Raycast, Light Accumulation) exist in a normal Blender install — do not expect to find them without building the branch yourself. The presenter explicitly flags known bugs (softness/radius positioning issues, blended/transparent materials not working yet, transmission issues) and open unknowns (no light rotation/direction-of-light access, no way to manipulate actual light position, unclear caustics feasibility) throughout. Treat this as a forward-looking research/inspiration reference on where EEVEE's shading customization may be headed, not as a reproducible current-Blender workflow.

## Structured Notes

### Core Technique
Three new experimental EEVEE-only shader nodes — **Light Info**, **Shadow Raycast**, and **Light Accumulation** — expose per-light data (color, power, position, direction, distance, shadow mask) directly inside the Shader Editor, letting an artist manually rebuild lighting/shadowing from scratch per-material (rather than relying on EEVEE's built-in automatic shading) and freely distort the shadow ray's sampling **position** with arbitrary vectors/textures for stylized (NPR, pixelated, "subsurface-scattering-fake," glitch/trippy) looks.

### Summary
**The three core nodes:** **Light Accumulation** (a shader-output node, one instance per light, stacks/accumulates across however many lights exist in the scene) has input sockets Diffuse Light, Diffuse Color, Glossy Light, Glossy Color — setting Diffuse Light/Color to a flat value of 1 does nothing useful (turns everything white) since it isn't using real light data yet; only once real Light Info/Shadow Raycast data is plugged in does it do anything meaningful. **Light Info** outputs Color, Power, Position, Direction, Distance, Cutoff Distance, Mask, and Is Sun for the current light being accumulated. **Shadow Raycast** takes a Position input (defaulting to the real surface position) and a Softness input, and outputs a Color that is the shadow mask (not screen-space — it's a real raycast) — multiplying the light's Color by the Shadow Raycast output combines light color and correct shadowing. Basic diffuse-with-shadow lighting is rebuilt by hand: Light Info Position minus the shading point's own position, normalized, dot-producted with the surface Normal, multiplied by the light Color and by the Shadow Raycast mask — confirmed that Light Info's Direction output is literally identical to doing that subtract-and-normalize manually, so it can replace the whole calculation directly. Softness/Radius on point lights was found buggy at the time of testing (positioning artifacts), attributed to the branch being actively developed. **The key creative discovery — position offsetting:** Shadow Raycast's Position input isn't just "pass through the real surface position" — feeding it an arbitrarily offset vector (surface position + any custom vector/texture) makes the raycast originate from a different point while still shading the real surface, unlocking a huge space of stylized effects. Naively offsetting causes rays to dip below the surface, causing severe artifacting; the fix (dubbed the **"clip fix"**, and turned into a small reusable node group) is: take the offset vector, use Vector Math **Project** to project it onto the surface Normal, then subtract that projected component back out — this keeps any offset strictly parallel to the surface tangent plane, never allowing it to point into/below the surface (a form of vector rejection). **Demonstrated variants of position-offsetting, all discovered live:** (1) Noise Texture-driven offset → soft, blobby, glass-fracture-like broken shading; (2) Voronoi Texture color-driven offset → crisp, "snapped"/faceted fractured-glass look, tunable via Voronoi detail/roughness; (3) White Noise Texture-driven offset with no snapping → soft, blurry pseudo-subsurface-scattering look (very noisy per-sample, needs high sample counts since it's literally per-pixel white noise); (4) White Noise offset restricted to a single axis (e.g. Z only, via Separate/Combine XYZ) → axis-limited SSS-style softening; (5) White-noise offset used to modulate hue/color of the shadow area (mixing a warm/red tint into shadow regions via a Color Ramp on the noise) for a stylized "colored shadow" NPR look; (6) snapping the offset to a coarse grid (dividing then flooring/rounding) → chunky pixel-aligned shadows reminiscent of Minecraft shaders' block-aligned lighting, with an optional small dithering offset layered back in for anti-aliasing at the pixel boundaries (pure snapping with zero dithering looks best on axis-aligned geometry but is visibly wrong on curved/off-grid surfaces — fixed for a specific object by transforming the offset vector from World space into Object space before snapping, then back to World space afterward). **Motion blur compatibility:** confirmed to work correctly with EEVEE's "Step" motion blur method — moving lights produce genuinely blurred/dithered-between-two-positions shadow trails, not broken artifacts. **Spotlights, area lights, and textures:** spotlights expose an Angle/cone cutoff and Blend/soft-falloff, but there's no way (yet) to access the light's rotation/orientation, so a texture (e.g. Checker Texture) plugged in via the ray Direction reads as a texture "stuck to the geometry" rather than properly gobo-projected from the light's actual facing — meaning true gobo/IES-texture projection isn't achievable yet without a light-rotation input. Area lights are not yet supported by these nodes at all. Jittered shadows (EEVEE's existing jitter/soft-shadow sampling) still work underneath this system and are recommended whenever accurate soft shadows are wanted, separate from the position-offset trickery. **Negative lights work** — a light with negative power/color subtracts light through this system, opening up "light-subtraction" compositing-like effects directly in 3D. **Passes/AOV behavior:** Light Accumulation's Diffuse/Glossy Color and Light sockets write directly into the corresponding render passes (Diffuse Color pass, Specular/Glossy pass, etc.) — confirmed live by plugging a flat color into Diffuse Color and watching another (unlit, pass-viewing) object's Diffuse Color pass change, i.e. this can be (ab)used as an unconventional way to smuggle arbitrary custom data into standard render passes/AOVs without a dedicated AOV output node, at the cost of "torturing your compositing artist" (a direct quote) since it genuinely changes where light rays interact rather than being a pure post-process. **Explored but inconclusive/unresolved in this session:** whether caustics are achievable (leaning "probably not," since caustics need actual accumulation across multiple bounces/rays which this system may not provide); whether IES light textures work in EEVEE with this (untested); whether colored-fringe/chromatic-shadow-edge effects are possible (blocked by lack of a direction-manipulation input); radiance cascades (blocked, same reason); custom volume/participating-media interaction (does not work, as expected — the nodes are surface-only). The presenter also floats (not implemented) the idea of exposing a per-sample index (like Cycles' Light Path "sample count," which he separately confirmed working in Cycles but chose not to upstream due to render-region/adaptive-sampling inconsistencies) as a future EEVEE addition specifically to drive per-sample jittered stylized effects. **Tangential dev-culture notes** (not the nodes themselves, but useful context on where Blender shader/compositor tooling is heading): ongoing work to make more shader-editor nodes "node group compatible" (needing String input sockets, e.g. for Attribute/Tangent/UV Map nodes) so they survive being wrapped in reusable node groups/assets, mirroring a shift already done in Geometry Nodes; the Image Texture / Image Sequence nodes are called out as badly needing a from-scratch rework (UDIM support, node-group compatibility, string-driven frame/path selection) but are described as "five updates away" due to complexity; the Compositor's 5.2/5.3 overhaul (new Transform nodes, Separate/Combine Transform, 3D-to-screen-space nodes for camera-aware effects like sun-beam/light-ray direction, the "Tune Image" node group for quick saturation/color-boost grading compatible with AgX/ACES) is praised as dramatically improved and production-ready; a practical unrelated tip is dropped about setting a Multilayer EXR output's channel name to blank so it's read as the generic default RGBA layer by other software, and to always enable EXR compression to avoid multi-gigabyte single-frame files.

### Key Steps
1. Add a **Light Accumulation** shader node (used as/near the material output) — by itself it does nothing until fed real per-light data.
2. Add a **Light Info** node for per-light Color/Power/Position/Direction/etc., and a **Shadow Raycast** node for the shadow mask (Position input, Softness input, Color output).
3. Rebuild basic lit+shadowed diffuse shading manually: (Light Info Position − shading point Position), Normalize, Dot Product with surface Normal, multiply by Light Info Color, multiply by Shadow Raycast Color (the shadow mask) — or substitute Light Info's Direction output directly for the subtract-normalize step, since they're equivalent.
4. To art-direct shadow shape/character: feed Shadow Raycast's Position input a modified vector (surface position plus any offset from a texture, noise, or custom vector math) instead of the raw surface position.
5. Always pair a custom position offset with the **clip fix**: Vector Math Project (project the offset vector onto the surface Normal) then Subtract that projected component back out of the offset — prevents the offset ray from dipping below the surface and causing severe shading artifacts. Package this as a reusable node group.
6. For a fractured-glass/broken look: drive the offset with a Noise Texture (soft/blobby) or a Voronoi Texture's color output (crisp/snapped, tune via Voronoi Detail/Roughness).
7. For a pseudo-subsurface-scattering look: drive the offset with a White Noise Texture (expect heavy per-pixel noise requiring high sample counts); restrict to one axis via Separate/Combine XYZ for a more controlled, axis-limited softening.
8. For colored/stylized shadows: use the same offset-driving noise (or a separate one) to blend a tint color into the shadow region via a Color Ramp and a Mix Color node, rather than leaving shadows neutral gray/black.
9. For pixel-aligned "Minecraft shader" style shadows: divide the offset/position by a grid-cell-size value, floor/round it, multiply back — snaps the shadow raycast origin to a coarse grid; layer a small amount of dithering (unsnapped noise mixed back in lightly) for anti-aliasing at grid boundaries; for off-axis geometry, transform the position from World space into Object space before snapping, then back to World space afterward, to keep the grid aligned to the object rather than the world.
10. Confirm motion blur compatibility by setting the Render Properties Motion Blur method to "Step" (not the default) before testing moving lights with this system.
11. For spotlight/gobo-style texturing: plug a texture (e.g. Checker Texture) into a chain fed by the ray Direction — understand this currently reads as texture-mapped-to-geometry rather than a true light-relative gobo projection, since there is no light-rotation input yet.
12. To use negative lights for light-subtraction effects, just set a light's Power/Color to negative values as normal — this system respects and accumulates them correctly.
13. To redirect custom shader data into standard render passes/AOVs (e.g. for a compositing pipeline), plug arbitrary values into Light Accumulation's Diffuse Color / Glossy Color sockets — they write directly into the corresponding Diffuse/Specular passes.
14. (Unrelated compositor tip mentioned mid-stream) When outputting Multilayer EXR, leave the output node's channel/layer name blank so external software reads it as the generic default RGBA layer; always enable EXR compression to avoid excessive file sizes.

### Nodes / Settings
- **Light Accumulation** (shader node, EEVEE-only, experimental): Diffuse Light, Diffuse Color, Glossy Light, Glossy Color inputs → Shader output; one node instance accumulates per light in the scene
- **Light Info** (experimental): Color, Power, Position, Direction, Distance, Cutoff Distance, Mask, Is Sun outputs
- **Shadow Raycast** (experimental): Position, Softness inputs → Color (shadow mask) output; not screen-space, a real raycast
- Standard nodes used heavily alongside them: Vector Math (Subtract, Normalize, Dot Product, Project — the last being the core of the "clip fix"), Noise Texture, Voronoi Texture, White Noise Texture, Color Ramp, Mix Color, Separate/Combine XYZ, Checker Texture
- "clip fix" node group: Position/Normal inputs → Add/Project/Subtract chain → clipped offset Vector output
- Render setting relevant to testing: Motion Blur method = Step (for verified motion-blur compatibility)
- Compositor tangent references: 3D-to-2D / Screen Space node, Camera Info node, Transform / Separate-Combine Transform nodes, "Tune Image" node group, Multilayer EXR output node (blank name = default RGBA layer), EXR compression setting

### Difficulty
Expert (live R&D on an unreleased Blender branch by the feature's own tester/developer — assumes deep existing familiarity with the Shader Editor, vector math, and EEVEE's rendering model; not reproducible without building the experimental branch yourself)

### Blender Version
An experimental, self-compiled Blender **5.3 branch build** from an unmerged pull request — explicitly NOT part of any public Blender 5.2/5.3 release as of recording; may or may not eventually merge into a stable Blender version.

### Tags
shaders, materials, lighting, rendering, eevee, compositing, motion-design, abstract, advanced, expert, blender-5x

---

## Related Tutorials
No directly related tutorials yet in the library covering experimental/NPR shading branches or manual per-light shadow-ray manipulation — flag for cross-linking if another EEVEE NPR, toon-shading, or experimental-branch tutorial is ingested later.
