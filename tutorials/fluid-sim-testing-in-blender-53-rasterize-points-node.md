---
title: Fluid sim testing in Blender 5.3! (Rasterize Points Node)
source: YouTube
url: https://www.youtube.com/watch?v=qcOMsFVMMQA
author: Cartesian Caramel
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/fluid-sim-testing-in-blender-53-rasterize-points-node/
frame_count: 0
frame_status: pending-selection
---

# Fluid sim testing in Blender 5.3! (Rasterize Points Node)

**Source:** [YouTube](https://www.youtube.com/watch?v=qcOMsFVMMQA)
**Author:** Cartesian Caramel
**Duration:** 113m10s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py fluid-sim-testing-in-blender-53-rasterize-points-node <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome to today's livestream where we're in 5.3 now.
[0:06] The train is moving and we're not stopping.
[0:09] But yeah, we have two new geometry nodes in Blender 5.3 so far.
[0:13] I want, I need to start working on my nodes for 5.3 but there's just one roadblock that
[0:19] I haven't had time to work on.
[0:22] But it's like the other name nodes for like gang instance names and geometry names, all
[0:27] that kind of stuff.
[0:28] It'll all be quite useful.
[0:30] I just need to figure out that darn rename dependency.
[0:35] I'm trying to figure out for the life of me and it should work by now but for some reason
[0:39] I just can't figure it out.
[0:41] But anyway.
[0:43] So new nodes.
[0:45] Let's take a look at the geometry materials node in the spreadsheet.
[0:48] So this node, pretty simple, just gives you the materials on geometry.
[0:53] So whether it's a mesh point cloud curve or grease pencil, you can get that.
[0:57] Initially I thought, why are instances not in there?
[1:00] But it makes sense because the material data is on the geometry inside the instances, not
[1:08] the instances themselves.
[1:09] So that makes sense.
[1:11] I'm interested in making a node that can remove material slots from a piece of geometry because
[1:16] currently I don't think you can do that.
[1:19] With the replace material node, you can replace a material with nothing.
[1:26] So if I do this and then say replace that one with that, I'll go and clear the material
[1:31] with nothing but then nothing is actually just the default material.
[1:35] It doesn't eliminate the material slot.
[1:38] So I need to check if I can do that.
[1:41] I did a little bit of looking a few weeks back but I am not entirely sure.
[1:47] I know in edit mode you can't remove materials.
[1:49] I'm not sure if that's just an edit mode thing or just a removing materials as a pain.
[1:55] Our current workarounds of pseudo duplicating the mesh are just a pain.
[2:01] So you do that to automate a setup that I have.
[2:05] But yes, there's that and then there's the rasterized points node.
[2:08] Now this one, let's go and build a little sim for it.
[2:12] It's a very nice node.
[2:14] People from other, I guess, simulation platforms would know about this.
[2:22] Let's go and set it up.
[2:24] So basically it takes points and then converts them or stacks up their values into a grid
[2:30] format.
[2:31] Actually let's not do the simulation zone just yet.
[2:34] Let's just go and describe the thing.
[2:37] So we put the points here and let's get a value.
[2:39] In this case I'm just going to have a value of one so that we can see what's going on
[2:44] here.
[2:45] So with this we can see we have points evenly distributed in this little space right here
[2:51] and then they get rasterized.
[2:55] Rasterized, that's how you say it.
[2:57] If we set the count to be that, it's like that.
[3:00] But if I were to go and set the business, I want to showcase how this works in a visual
[3:06] way because I did a little bit of testing beforehand.
[3:09] Not much though.
[3:11] Yeah, that should suffice, I think.
[3:15] If we go and do this and then crank up the offset, which for some reason is that that
[3:21] would be why because I keep forgetting which one I'm clicking to view or the other one.
[3:26] Let's go and make this a bit more, I don't know.
[3:31] Let's turn the scale down because I want to clearly show like a distribution with everything.
[3:37] So if we take a look at the grid in this case, we can see that the parts where there's more
[3:41] points, it's brighter and the places where there's less points, it's darker.
[3:46] We have options for interpolation.
[3:49] If I set it to constant, we'll just see the cells themselves and that's good.
[3:55] And then to get the state up back, what we would do is use sample grid.
[4:02] Yeah, it's that one.
[4:03] It's that one, right?
[4:04] I almost forgot about that.
[4:05] I was wondering if you do linear interpolation and linear interpolation, does some data get
[4:13] canned?
[4:14] Does it get removed?
[4:16] So it's like which one would be better?
[4:18] First neighbor or constant?
[4:20] Should that be, um, I don't know, they're interpolation types.
[4:26] Actually, yeah, should this one be changed to constant to match the name?
[4:31] Not sure about that one.
[4:33] Let's see, so we can get that to put the data back in the points if need be.
[4:38] It's the low from Romania.
[4:42] So what are we cooking today?
[4:44] Some of the new nodes.
[4:45] I just want to take a look at these.
[4:47] This won't be a long stream.
[4:48] You know, that's a I say that every time and then I go past an hour, but I am rather exhausted
[4:54] today.
[4:55] I watched the Odyssey today, which, um, it was interesting.
[5:00] I didn't know what to expect with that movie, but it was interesting.
[5:04] I'd recommend it.
[5:06] But those are the delivery was in an interesting way that I didn't expect.
[5:11] But yeah, let's not get too sidetracked by that.
[5:15] So let's go in and get the position of these points.
[5:19] Let's see.
[5:20] Agamemnon, I can't say the word Agamemnon had aura.
[5:25] Yes, every time Agamemnon was on screen, I was like, yeah, no, they're just hype moments
[5:31] and oring that.
[5:32] And then he spoke and I was like, ah, ah, okay, okay.
[5:38] Um, oh, little thing about the rest race points node.
[5:42] For some reason it defaults to float when you connect it.
[5:46] But if you add it in manually or just convert it, you can get vectors.
[5:51] There's scalar and vector.
[5:52] And then it does that.
[5:53] Just keep in mind.
[5:54] Well, low bug probably be fixed really soon.
[5:57] But if you're sampling the position and stacking it with the rest race points node, you need
[6:01] the value and the position because the stack, it's not like sample nearest where it just
[6:06] gets one.
[6:07] You get all of them.
[6:09] So you would have to go and divide by the amount.
[6:13] And also I have not done a lot of research on this.
[6:16] So there's always a chance that I have done this improperly.
[6:22] So since these are rather new nodes, keep that in mind.
[6:27] This node may allow for MPM solvers in the near future, but we will have to go and take
[6:32] a look at that.
[6:34] I was doing, as one commentator did, a very, very, very fake simulation, like a water
[6:43] simulation.
[6:44] Let's go and get a velocity step node, which is a custom node group I made.
[6:48] It's up on my Gumroad page for free.
[6:51] Let's basically just a little, you know, just get the velocity.
[6:54] It's just a little helper thing so that I don't have to do this every single time because
[6:58] it annoyed me greatly.
[7:02] So right here, yeah, let's keep that there.
[7:05] So we're setting up a simulation.
[7:07] We're rasterizing the points and then getting the position, which actually I'm going to
[7:11] go and reorder these so that the lines are nice and clean.
[7:15] One to get how many points there are, one to get the positions, they stack them up, they
[7:19] do all that.
[7:20] So we get this kind of position grid.
[7:21] If we don't do the divide, we can see that some of these are much brighter than they
[7:24] should be.
[7:25] So the divide normalizes it.
[7:28] We sample that grid and then what we can do is subtract from there.
[7:33] And then this is how I did it for that very, very fake simulation.
[7:37] It was not good, but it was functional.
[7:41] It was indeed functional.
[7:44] So here I'm going to make this set the velocity and I'm going to plug this into there.
[7:49] Take a look at this.
[7:50] So we should see that this makes it so that the points go towards each other.
[7:55] This should make it so that they go away based on, yeah, and it's still discrete points.
[8:01] So this won't be like a gravity simulation.
[8:05] This is just a more efficient way of finding out if points are really close to each other
[8:10] and their relations with that.
[8:14] Yes.
[8:17] So let's say how did I actually make this work before?
[8:22] Actually forget.
[8:23] I'm going to do a little wing.
[8:26] Yeah.
[8:27] Normalize.
[8:28] Let's see.
[8:29] Let's see.
[8:30] Let's see.
[8:31] Let's do a map range.
[8:33] I'm honestly forgetting what I did because I don't think I saved the project.
[8:37] It was a quick test on my lunch break.
[8:41] Yes.
[8:42] Ah, there we go.
[8:44] So we have something along those lines even though still not phantoms.
[8:49] Oh wait, is that moving them to?
[8:50] Oh, it's moving them towards each other.
[8:52] Right, because they specifically made it do that.
[8:56] But here they're moving away and we can see the discrete grid set up because these are
[9:01] interpolated.
[9:02] I still don't know which one would be better.
[9:04] I'm assuming linear and linear is the best way to go, but it still doesn't necessarily
[9:09] feel right.
[9:10] And it does stuff like that.
[9:16] Don't particularly understand which one would be the best.
[9:21] I found that there were like a little bit of weird things happening with cubic.
[9:25] Like here we can see that there.
[9:27] That is in no way correct.
[9:29] So maybe it's a little bit.
[9:32] I probably don't understand it.
[9:34] Oh, and also I forgot to mention the voxel size you do that or you can put in a matrix
[9:40] by default.
[9:41] The matrix will just give the grid any increments of one as we can kind of you can kind of see
[9:45] it's aligning with the grid and all that.
[9:48] The voxel size is more convenience.
[9:50] Oh, wait, I forgot.
[9:51] There is another node grid.
[9:53] I'm sorry.
[9:55] Yes, the grid topology Boolean.
[9:58] But no, no, that's not the one here.
[10:01] Let me get the change log on the side.
[10:03] Let's see.
[10:06] Where are the new geometry nodes?
[10:13] Let's see.
[10:14] Grid.
[10:15] Oh, grid topology Boolean.
[10:16] Yes, that is a new node.
[10:18] There might just be a grid Boolean.
[10:20] Yeah, that's probably why I was thinking of before.
[10:24] And there are some like NERBs, input nodes, but I'm assuming those are just other inputs.
[10:29] And there's also, let's not forget, curve to mesh.
[10:36] Yeah, this now has a miter scale, which helps with like sharp corners and stuff like that.
[10:42] If you're like, I don't know, making a building and you draw like the foundation and you don't
[10:48] want it to do weird stuff on the corners, this will help with that.
[10:51] I mentioned the UVs every single time, but I hope we get that natively in there instead
[10:57] of having to do a workaround and post because that it just feels so inefficient.
[11:01] Anyway, anyway.
[11:03] So yeah, that's something that I did.
[11:06] I felt different than this because this doesn't feel quite right if I'm being honest.
[11:12] That attracts the other repels.
[11:14] But it was something something along those lines.
[11:19] And also there, I did do an attempt at grid.
[11:24] What was the divergence?
[11:26] And virgins.
[11:28] No, it wasn't divergence.
[11:29] It was.
[11:31] Oh, what was it?
[11:33] Cryptotubes.
[11:35] Yeah, a curve to tubes is a node group.
[11:41] Which means internally it will, I keep forgetting just how massive this node group is.
[11:48] Absolutely.
[11:49] Like we need those portals because this is this is can I'm not knocking the setup, but the organization.
[11:59] This is we need those reroute portals just to hide the subway system we have going on over there.
[12:10] I need to look into seeing if that's even possible because having a node that just disables rendering of the node link, depending and then making it so that you can put it in like maybe a string to say where the link is coming from and who knows.
[12:28] That's something there are there are a lot of things I need to do and I do not have a lot of time to do them.
[12:35] Let's see. Let's take a look at the actual UVs because I assume extrapolate Reyes material transfer.
[12:42] How about that?
[12:44] How do they do the material transfer material index?
[12:49] Ample index and into that.
[12:52] Oh, wait, is that how they?
[12:54] Hmm.
[12:56] I should look into these a bit more.
[12:59] Rounded caps and profile.
[13:05] Ah, here are the UVs.
[13:08] So from what I can see here.
[13:16] Ah, haha.
[13:19] Yes.
[13:21] Yes.
[13:22] So yeah, you can see how this might be a bit less efficient of half rather than having it natively inside of the node.
[13:30] But does this have different modes?
[13:33] No, apparently not.
[13:36] Yeah, basically getting rid of all that and then putting in there it would be faster. I would think my untrained eye.
[13:46] Let's go and get the what was it the?
[13:50] Let's go over to the volume nodes. Let's go.
[13:54] Gradients, that's the one.
[13:57] So this could also.
[13:59] There's also a weird thing with the transforms that you need to compensate for to make this work.
[14:06] Which is the tricky thing with this because it gives you the gradient but it's like multiplied by the voxel size.
[14:13] It gives you either an atrociously big or atrociously small thing. So you need to like divide it by the voxel length.
[14:20] If I get grid info, we can go and get the transform of this.
[14:26] And it doesn't really matter what that part is. That's fine.
[14:30] And then I could go and perhaps extract.
[14:34] X, Y, or Z.
[14:37] If I extract, I could extract the scale but this is just a more direct way of making it work.
[14:45] So this would be the X I assume so that would give us the scale.
[14:49] So if I were to go and divide this here, I'm making some new stuff right now because I'm just playing.
[14:56] Let's see what happens. So this in theory, no, that's an atrociously big value.
[15:02] Though that that seems about right like that. That seems a bit much. That seems to.
[15:07] Oh, but it also since it accumulates. No, but that's the density. It's giving us the density.
[15:14] So in theory.
[15:18] Do I extract you from there? I keep forgetting if I'm being honest.
[15:24] Keep forgetting which one I need to do.
[15:28] Anyway, anyway, anyway, let's go. I want to try to do this in a somewhat correct way, even though again, I don't know why I'm doing with this.
[15:37] I've not had time to properly research such things, but it looks like something is occurring, but we need to invert it.
[15:46] Let's say it's be negative one. This will explode.
[15:50] How about that?
[15:54] Oh, at least it's doing. Oh, I forgot a critical piece of information.
[16:04] I forgot it.
[16:08] The reason it wasn't working before is because it's not using the simulation for the rasterization.
[16:14] Oh my God. There we go.
[16:18] Oh, man. Yeah, I'm exhausted today. I've been doing a lot this week.
[16:27] I've been doing a lot.
[16:29] But yeah, we have that. We have something that doesn't use probably more efficient as well because this is working only on the grids rather than it's working on the grids,
[16:40] which is probably the way I should have done it because before this part's happening on the points because of the sample grid and everything.
[16:47] So this may be a better way of doing it. Probably is.
[16:52] And since this is setting the velocity, it's not.
[16:56] And look how fast it, wow.
[17:00] Pretty good. Pretty good.
[17:08] Yeah, though, I still wonder if some of the points should.
[17:16] The sampling here, I'm still not sure about because if these were both constant, this will be jittering.
[17:24] Yeah, as we can see there, does this one need to be trilinear?
[17:30] No.
[17:32] So I'm just testing again. I do not know what I'm doing. I am testing. I'm trying to figure this out.
[17:38] It seems like that is optimal, but something tells me something is getting lost.
[17:44] Yeah.
[17:51] Hmm.
[17:56] Let's see. Let's see. Let's see. Okay, so the question is, one, do I add in gravity and two,
[18:03] how should I affect the velocity? Because if I dampen it, I'm worried about it exploding.
[18:10] As we can see, working fairly well.
[18:18] And do we, I don't know. It has quite the springiness to it.
[18:26] Let's do SDF collision and SDF mesh.
[18:31] These are both node groups in my free node pack again, just a little helpers for the velocity and all that.
[18:40] Again, you can take a look at the internals, which this should probably actually know that is working as expected.
[18:47] Let's go and drag in, what shape should we have there? Let's just have a cube.
[18:54] Let's go and flip the normals to the inside and then set the rendering to be a wire.
[19:01] There we go. Very good. Very nice. Let's go and plug this. No, let's plug this into there.
[19:09] We put the sine distance into there. We put the normal into there. Lovely stuff. You love to see it.
[19:15] So now we can see that this is colliding.
[19:18] Lighting as well as it can. Then it does that, which is nice.
[19:24] For the forces, do I need to scale this up because of the delta time?
[19:31] I don't know. I mean, it seems to be regulating pretty well.
[19:38] And I want to add in some gravity, but I don't know if that's such a grand idea.
[19:44] But if we do this, we can see that we're getting some particle self-collisions to an extent.
[19:52] Negative 9.81 meters per second.
[19:56] We can see, yes, it's very much slowed down because...
[20:04] Right, the forces that... Well, actually, I need to scale this up by the delta time.
[20:14] Oh, because I put 0.9. There we go. I need to trust in past me because...
[20:23] They knew what they were doing. But you. You must compensate.
[20:32] So we put that in there. We can see that. Ah, look at that.
[20:38] I am still a little bit concerned.
[20:43] I mean, if I go and mute the gravity, we can see that. And that's not bad.
[20:53] You know, it's not exactly the most stable thing on the planet, but it's not bad.
[20:58] And I'm scaling up it up by delta time because this is just the gradient distance.
[21:06] Actually, you could be a scale node just because I like the colors not having to do implicit conversions.
[21:14] So if we have that, we have something along the lines of something good. Something.
[21:22] Let's see. But yes, we can see, and that is working as intended.
[21:28] We're getting a cube and it is doing that.
[21:32] I can scale it up, I can condense it, but the goal is that we are getting something that behaves somewhat like a fluid.
[21:41] So I'm going to go and scale up said cube by a lot.
[21:46] We have something like that. Maybe I have a force that tries to draw it into the center instead of what I currently have.
[21:57] Let's see.
[22:00] Position.
[22:04] Yes, let's get the length.
[22:08] In terms of moves, I am looking forward to seeing the new Spider-Man movie.
[22:12] Maybe that will inspire me to make more spider web simulations and stuff.
[22:17] I'm not excited for the Avengers Doomsday.
[22:22] I can't say that I am.
[22:25] Oh wait, no, I want this to be a scale by a negative one.
[22:29] So that, yeah, this goes to zero.
[22:34] Yeah.
[22:37] Can't say I'm excited for the next movie because it just feels like they're nostalgia baiting.
[22:44] And I'm a bit too young for that nostalgia.
[22:50] A bit too young.
[22:54] Let's see. So yeah, it's functioning.
[22:58] It seems rather stable.
[23:02] Yeah, look at that.
[23:05] And fluids are incompressible. No, no, no, no, no, no.
[23:09] Water is mostly incompressible.
[23:12] So I assume that this kind of bouncing action is exactly as intended.
[23:16] Though the divergence.
[23:20] How should the, yeah, how should I use the, um, yeah.
[23:26] Okay.
[23:28] I've seen Brand New Day twice in two days.
[23:30] My uncle is an actor. Oh, fun. Very fun.
[23:34] Yeah, the theater that I usually go to, it's not a large theater, but it has been fully packed
[23:41] for the past couple of days where there have been like no parking spaces available.
[23:46] But today, um, everyone was seeing Spider-Man, so I was able to go and see the Odyssey.
[23:53] Yeah.
[23:56] But yes, I like, I like going to the theater.
[23:59] Some, quite a few things you just need to see in the theater to get the proper atmosphere.
[24:04] Though that being said, I have seen some really good movies on a small screen,
[24:12] but the theater, it just helps you focus. You can't be distracted. You just can't.
[24:18] But yes, my movie recommendations are, well, number one obsession because that, that movie,
[24:27] that movie makes you, it is a very disturbing movie, but it is very, very good.
[24:33] Horror movies, so just to let you know going in, that was a very good movie.
[24:38] The back rooms I enjoyed, even though, you know, I have some, yeah, some gripes with, uh, not gripes, but...
[24:49] I liked the aura of it, and I really loved the architect memes, but some of the writing
[24:55] guy was kind of like, okay, but it wasn't bad. It wasn't bad.
[24:59] Not bad at all.
[25:03] Um, I'm actually forgetting, what was the, oh, Sheep Detectives was also, was surprisingly good.
[25:09] Yeah, I couldn't watch the movie that I planned to, so I watched the Sheep Detectives, and that was surprisingly good.
[25:15] Surprisingly good.
[25:18] And very, some of the best, like, animal, um, digital animals I've ever seen, some of the best I've ever seen,
[25:26] it was really, really, really good on that front.
[25:29] As someone who has worked on digital fur in movies, that made me really jealous, like, or jealous or insecure,
[25:38] one of those two, but the fur that they had on that, it was incredible.
[25:43] It just, it was so well done. I didn't think that movie would be that high budget, but they, wow, that was impressive.
[25:51] Um, let's see. Okay, I'm just staring at the simulation. Let's make it a bit more fancy.
[25:58] Um, I don't want to worry about that. Let's go and add in some noise. Just for fun.
[26:06] Okay, noise again. We have a noise over there just to displace it at the beginning.
[26:12] Well, that was the worst movie that I saw this, um, this year.
[26:17] I remember the movies, I'm not remembering all of them, but I remember most of them being good.
[26:24] Yeah, yeah, which movies, which movies did I watch? Hmm.
[26:31] Let's see. So we have that, and that's, you know, that's, that's looking good.
[26:39] Yeah, there we go. Maybe a bit too much. So let's lower it by a bit and just take a look at that.
[26:46] So, we'll just, we'll just that node. It's fairly efficient, very fairly fast.
[26:52] I could also try doing this with like, um, uh, what is it, uh, cluster by distance.
[27:00] I could probably do something similar with cluster by distance, but grids are the industry standard for doing this kind of stuff.
[27:08] Yeah, once again, I'm just going to grab something.
[27:15] Keep a list or keep all the tickets for movies that I watch. So let's, let's see.
[27:21] What movies did I watch? There was that one, that one. Oh, okay.
[27:27] Now I know which movie is the worst movie that I saw this year.
[27:35] It was the Super Mario Galaxy movie easily. It was a fun time, but man, the plot on that was,
[27:43] there was, there was barely even a plot and Super Mario Galaxy was a fundamental game to my childhood.
[27:52] Probably the favorite, the best game of my child besides Minecraft, of course.
[27:58] But man, that movie plot wise, uh, it wasn't great, but it was fun and it was very quickly.
[28:09] Let's see, Project Hail Mary, I thought was all right.
[28:12] Um, Goat was surprisingly good. That one was good, yeah.
[28:17] Then let's see, the obsession ship. Yeah, I haven't seen too many movies this year.
[28:25] I do need to see more. I do need to see more. Okay.
[28:32] Okay, okay, okay. What, what else do I need to do with this?
[28:36] Well, we're almost at 30 minutes, so maybe I can call it there.
[28:39] I know I could go for a little bit longer.
[28:42] Warming up, I'm warming up.
[28:45] So I still have the Collider, so maybe if I go and re-add in the Gravity, which I believe, yep, it's right in there.
[28:56] I could do that, add in some Gravity's there. It just very nicely falls to the ground. It bounces.
[29:04] Which, oh yeah, the XPPD Solver node, I need a look into adding bounce to that because currently it does not have that, which is unfortunate.
[29:15] Um, yeah, here, that seems pretty nice. I gotta say, oh, and also the node's quite efficient, so I could go and crank up the number here.
[29:25] Oh, so the problem here is not the number, it's that the amount of voxels goes up a lot.
[29:34] So that's what's, oh yeah, let's turn down the timings. Timings named attributes off.
[29:39] The voxel size, we're dealing with a lot of voxels. If we take a look at the viewer, we should be seeing, yeah, look at this grid.
[29:46] That's a lot of voxels. Um, viewer, viewer, viewer, viewer, viewer.
[29:53] Well, actually, no, that's not.
[29:57] It's two million voxels, okay, not the worst, not the best, but we can make it a bit more coarse.
[30:04] And it's exploding because, wow, yeah, wow, wow, wow, wow, wow, wow, wow, that's, what's this thing's telling me?
[30:11] It's actually, whoa, look at that.
[30:14] Oh, I did not expect it to, um, I didn't expect it to, like, not...
[30:23] Huh.
[30:26] Oh, look at that.
[30:28] Because most of the interactions are happening on the voxel level rather than on the individual point level.
[30:35] And of course, this is not accurate. I'm not going to making accurate sims like this.
[30:43] But since it's happening on that level, we are getting a very nice thing happening there.
[30:49] And then I could also add in collision with this box, but I'm not sure that's the best idea.
[30:54] But if I were to go and turn off our little holder right here, we should see after it explodes and stabilizes, if it stabilizes.
[31:06] Yeah, we get kind of a... I'm still seeing some artifacts right there, so maybe that's from the interpolation.
[31:13] But yeah, it explodes because things form, like, excuse-me-la. Oh, it just needs to reset.
[31:19] So yeah, we have something where there are so many points there and it explodes.
[31:24] And then it falls back down.
[31:27] And there, we have something that kind of sort of behaves like a fluid. Kind of.
[31:34] Let's go ahead and set the material. The just material one.
[31:39] Then let's go and take a look at the velocity attribute. Oh, wrong one.
[31:44] Oh, now! Wait, wait, wait, wait, wait. Now, since we have the material...
[31:55] Geometry materials node, we can go do that, get the first one.
[31:59] Yeah, let's die down, plug that into there so it'll always be the first one on this geometry.
[32:03] Now, the thing is, I saw in the curbed-a-tube node, if I...
[32:09] ...hear material index.
[32:13] If I sample that from there and then... yeah, let's see, set material index.
[32:18] Maybe that's how it's done.
[32:23] Oh!
[32:25] Unsupported? Okay, that... unsupported, really?
[32:32] I am quite surprised by such a thing.
[32:36] Anyway.
[32:39] Anyway, well, yeah, we could just do that. That seems good, fun.
[32:43] Let's go and get the attribute and have this be the velocity.
[32:49] Let's see, let's go and take a look at this and we should see something...
[32:53] Oh, we're staring at the cube.
[32:57] Let's see, so why are we not... oh, because I spelled it wrong. There we go.
[33:03] Now, we can see the velocity in its current form.
[33:08] We can see, again, the collision since I'm assuming because the collisions are being done on the point domain,
[33:14] rather than the... rather than on the voxel level, it's doing that.
[33:19] But we can see it's functioning decently.
[33:22] And let me change this from A, G, X to standard so that we can see the actual values here.
[33:28] Yeah, we have something akin to a simulation, a water simulation or something like that.
[33:35] Oh, the question is...
[33:39] I probably need to use the divergence node as well to make that work.
[33:43] But also, why do I need to... oh, right, um...
[33:48] Let's see, oh, wait, wait, wait, wait, I'm forgetting.
[33:51] Yui!
[33:55] I mean, I could just rasterize the points again.
[33:57] To go and get a...
[34:00] I mean, that looks somewhat correct.
[34:03] Yeah, because if I do this...
[34:07] Let me just get something that...
[34:11] Here's to be somewhat correct.
[34:13] But there is no volume shader, so I need to go and implement that.
[34:19] So if I go and set... wait, how do we do this again?
[34:23] Um, grid... oh, store named grid, right.
[34:27] I forgot, I forgot about that.
[34:31] And we just label this one not density, because it is just straight up the density.
[34:36] So, and I could just pass what's currently in there through there,
[34:40] and that's probably a lot more efficient because it's already being calculated.
[34:44] I remember how to do some of these things.
[34:47] Density, that's fine.
[34:52] Anything else I need to do? I don't think so.
[34:55] See, I look at that.
[34:58] It's still simulating.
[35:00] Yeah, look at that.
[35:02] And then there, we don't have a volume shader, so let's go and do that.
[35:07] So let's go and get, um, principled of volume.
[35:13] Do that, click that into there, and we should see if I go and eliminate that points.
[35:20] Uh, no, we still want to set the material, but not with the other things.
[35:26] So we just need one of those.
[35:28] Say, oh.
[35:31] Uh, and also on the volumes we need...
[35:37] Volume shadows.
[35:39] Turn off temporal reproduction because that is useless in this scenario.
[35:42] Or, not the most useful in this scenario.
[35:45] Volumes, make it one to one so that we can see.
[35:48] Boom, we have, uh, this could be good for, like, um,
[35:53] the fog, or the mist, not, not, um, the spray from the water.
[35:58] If it goes too fast, we can convert it to spray and all that.
[36:02] Yeah, now we got something along those lines.
[36:05] Now, I don't think we can go and turn this into something that looks quite like water.
[36:11] But knowing the density can be useful.
[36:18] Actually, let's turn the density down so that we can see what's going on a bit better.
[36:24] Yeah, we have something like that.
[36:27] And we could also, of course, turn, uh, grid to mesh.
[36:31] So we take the density, we go and put it in there, we go and take a look at this.
[36:35] So now we have a mesh based on said grid.
[36:40] It doesn't look like water, just straight up does not.
[36:43] But the threshold, let's set this to be, what, like, 0.5?
[36:47] I could go and turn it up more.
[36:51] Uh, but yeah.
[36:53] Volumes, again, I am nowhere, absolutely nowhere near an expert, um,
[36:59] on how this, uh, should work.
[37:03] I guess it means that we have, um, two stages to this simulation.
[37:11] We have one stage, which is the grid stage and one that's the particle stage.
[37:16] That's my understanding of most water simulations.
[37:21] It's, we don't need you either, so let's go and put that out from there.
[37:25] Oh, it used to have, yeah, it used to have that part, so yeah, let's go and put that out.
[37:31] Maybe.
[37:32] Uh, let's go and move this over, because this part, it's not really necessary.
[37:37] I just did it as a, uh, showcase.
[37:40] So this one, we'll just set it to be that one, put you into there.
[37:43] I don't know why I did that.
[37:44] And eliminate those.
[37:46] So, yes.
[37:48] So there's the particle stage and then the grid stage.
[37:52] These are our verticals.
[37:55] So two stages, they both communicate with each other to make more efficient.
[37:59] Uh, I guess collisions, because what is water, but a ton of collisions,
[38:05] billions of collisions happening at, trillions of collisions happening at once.
[38:09] We have no hope of simulating that in real time.
[38:13] So we approximate.
[38:17] Oh, the velocity grid.
[38:19] Uh, well, no, it already has the velocity.
[38:22] It doesn't, it's already saying the velocity.
[38:25] So is that, hmm.
[38:29] We get the gradient from there.
[38:32] Do I need to calculate the divergence from the gradient, divide that and then multiply that by that?
[38:40] Is that what I must do?
[38:43] Either divide or multiply.
[38:45] So let's go and experiment.
[38:47] Once we have, now that we have something that kind of works, let's go and try it out.
[38:53] This will not work initially.
[38:57] And we have that and that.
[38:59] I am worried about that, but I'm going to keep it there as, need, oh, yeah, no, no, terrible.
[39:04] Absolutely atrocious, bad.
[39:06] And there, I'm assuming that I also need to scale that by the grid dimensions.
[39:14] In this case, we're just going to use the X dimension of that.
[39:20] So we're multiplying, multiplying, it's quirky.
[39:24] That is not helping.
[39:27] Light, yeah, no, terrible, terrible, hate it bad.
[39:31] Do we divide?
[39:32] I honestly forget, I don't know what I'm doing.
[39:35] Oh.
[39:42] Something's occurring.
[39:45] That's definitely something.
[39:52] I'm going to comment on that.
[39:53] Nope.
[39:55] But it's incorrect.
[39:56] Quite incorrect.
[39:58] I think because it's because there is or is not being multiplied by the delta time.
[40:05] Nope.
[40:07] Oh, look at that.
[40:08] Yeah, look at that.
[40:09] We're getting the creation of the cosmos right there.
[40:15] Let's go back to just viewing the particles.
[40:18] Is that what actually, yeah, what is better viewing?
[40:26] Wait, look at that.
[40:30] Some weird geometric shapes right there.
[40:34] Yes, how I should have looked this up beforehand.
[40:38] I should have looked at Sebastian Lag's video on all this.
[40:43] I'm not even using the position at this point.
[40:46] I'm merely getting the density.
[40:48] And then doing that.
[40:51] Hmm.
[40:53] Let's see.
[40:58] I love your work.
[40:59] Do you know a way of adding debris on geometry nodes' hair systems?
[41:03] Like debris in the fur, leaves, twigs, etc.
[41:07] I do.
[41:12] Sorry, I just needed to do a mental check on what I can discuss about such things.
[41:20] Yes.
[41:23] You distribute points on the curves.
[41:26] So on the curves themselves, you can use like the sample curve node.
[41:31] Yeah, I know that one should work out just fine.
[41:33] Use the sample curve node to randomly distribute points with randomly distribute points on the curves.
[41:41] You can also bias it towards the beginning of the curve, end of the curve, with the curve index and all that.
[41:46] But just make sure you get the normal tangent and position so that you can turn that into transform for your instances down the line.
[41:53] And that is how you can add twigs and stuff to your geometry nodes fur.
[41:58] Or maybe use a geometry node surface deformer, which I also have on my Gummert page for free,
[42:04] to skip the fur section if you need something very efficient and just deform it with the surface.
[42:10] Both are options.
[42:18] But yes, I need to figure out what's going on here.
[42:21] What is going horrifically wrong?
[42:24] Oh yeah, no, that looks horrifically wrong.
[42:29] So here we have that.
[42:30] That's just doing that.
[42:31] What does the divergence look like?
[42:34] What's like that?
[42:35] It looks like that.
[42:36] And then it looks like that.
[42:38] It looks so much worse.
[42:40] So much worse.
[42:41] So this part here is the issue.
[42:45] And if I set this to be like the power of two or three, does that help?
[42:50] Because there's so many more dimensions at play.
[42:54] If we do that, that seems to...
[42:57] I'm just...
[42:58] I'm not going to say vibe because the connotation of that has changed.
[43:03] But I guess, you know, it doesn't really change.
[43:05] If you don't know what you're doing, you are doing things through the vibe.
[43:09] God.
[43:11] Okay, let me just go on a little mini rant this week.
[43:15] This week on Instagram, I saw a completely AI generated video of the behind the scenes of a city getting destroyed by massive wave with fake crew, fake blue screen background, fake everything,
[43:32] fake cameras.
[43:33] It got 500,000 likes.
[43:37] Now tinfoil hat time.
[43:39] I think that's being promoted by a certain company that really wants AI to become a thing.
[43:48] But isn't that just the biggest insult to the creative field or I guess film as a whole AI generating behind the scenes footage and then claiming it's like, oh, not CG.
[44:01] It's all real.
[44:02] It's like, that is the biggest insult to create AI is the biggest insult to creativity because it's just a data replicator.
[44:12] But speaking everything, everything, I do not want my movies to be AI generated.
[44:19] I don't want my songs to be AI generated.
[44:21] I don't want my art to be an AI generated.
[44:24] Its value is in the people that make it.
[44:28] I could rant about that for hours.
[44:31] I could rant about that for hours while I'm working on a very not functional thing there.
[44:40] Because of course with AI, you know, the person who orders something from an AI, they're not talented.
[44:49] That's the point.
[44:50] The point is that they're not talented.
[44:52] It just ordered something from McDonald's.
[44:55] That's the point.
[45:01] Yeah, it's truly sad.
[45:04] It is sad.
[45:06] I think the sign for me was when ArtStation got plastered with fake artist references.
[45:13] 500 images of X thing, Y thing.
[45:16] It's just like, no, that defeats the point of reference if it's AI.
[45:22] It's all about money.
[45:24] It's all about capitalism.
[45:26] It's all about capitalism.
[45:28] When you look for biological references, at least when Googling, of course, I'm not a scientist or anything.
[45:35] You have to sit through a ton of horrifically maligned and disfigured AI images.
[45:43] And then you gotta pull out the before 2022 trick.
[45:48] But it is sad just how much of the internet is becoming non-human.
[45:52] No one actually made it.
[45:54] And I'm pretty sure that most AI generated images aren't even prompted by someone.
[46:02] It's just the internet made by things that aren't conscious.
[46:07] And then there is a future where we're all just watching AI generated Netflix, because that's, you know, the only thing left.
[46:16] We're all entertained by something that can't feel.
[46:19] And that is, that's a sad future.
[46:24] But AI, I don't think it's going anywhere.
[46:27] I don't think it can go anywhere, because despite it being sloppy and stuff like that, it is better for capitalism.
[46:36] It is faster than humans can ever be.
[46:39] It can do more work than humans can ever do.
[46:42] Like that fake behind the scenes Instagram post.
[46:45] It would take months for someone to do that.
[46:47] Hours of simulations and stuff like that.
[46:50] It doesn't probably in less than a day.
[46:53] So, yeah.
[46:55] It may be the future, but it's not a future I am all too interested in.
[47:01] Because, again, I know I'm on this. I'm sorry, everyone.
[47:08] Why would you want to watch something that was made by something that doesn't feel a thing?
[47:18] Maybe it will.
[47:20] Are you making a fluid sim? No, I am ranting about AI.
[47:24] Because this week, something properly pissed me off.
[47:29] But yes, I am kind of making a fluid sim.
[47:34] Not well, because I don't really know how to make it.
[47:37] But at least something is happening. It's not stable. It's not great.
[47:42] But something... Oh, I need it. Wait, no, I need to quantize the velocity.
[47:46] That's the missing piece. I know what to do now.
[47:50] Do I multiply by the d... Yeah, no, I need to do that as well.
[47:54] Because the problem...
[47:57] I'm not setting the velocity. I need to set the velocity, but I need to put the velocity through...
[48:02] Oh, wait a minute. What did that actually work?
[48:08] Let's see.
[48:12] We need to... Oh, right, because that little bug, I need to just swap that there.
[48:18] And then, because I don't know how to actually do that part,
[48:23] let's get a minimal working version here, and then we can go and do everything else.
[48:29] I do need to organize the stages.
[48:32] Node groups, I need to put in node groups, of course.
[48:38] No, let's have the... Okay, we're node grouping this. I am not dealing with this BS.
[48:45] Okay, node. Make group. We pass in that, we get the attributes, we pass out the attributes we need.
[48:52] This is the...
[49:01] Not the divergence, the gradient. I need...
[49:07] I needed to sneeze, and I was looking for the mute button, but the sneeze went away.
[49:13] Oh, that is funny.
[49:15] And then this is the velocity. So we're doing that and that, and then we also need the density gradient.
[49:22] Then city.
[49:24] City, I'm about to sneeze again.
[49:28] I need to mute, but it's... Nope, the sneeze is coming and going.
[49:32] Let's go and delete these, because they're not actually useful at this particular moment in time.
[49:39] And of course I messed with that, so no, we want that one there, that one there.
[49:44] And this one here. So there we go.
[49:51] Let's see, let's see, let's see.
[49:54] Do-do-do-do-do-do-do.
[49:58] Do-do-do-do-do-do-do.
[50:02] So we have that, that, and that. We have the gradient, we plug that into there, the velocity, we plug that into there.
[50:09] It should work as intended. It will go and very nicely average the velocities, and then we just go and put that out there.
[50:16] So now we should be able to...
[50:20] Oh, God.
[50:23] Blender probably crashed, and because I'm assuming one of the points breached containment and made a volume grid that was the size of the universe itself.
[50:35] Recover last session.
[50:37] Crap.
[50:41] That's why... Okay, I didn't save this project, so I'm saving it right now.
[50:48] Okay, I was able to recover it. Let's see, uh... Let's see, 2026 projects. I still need to sneeze, I can feel it.
[50:56] 5.3, uh... L-Syn-V1. Yeah, that's good enough. There we go.
[51:04] We are back, resurrected from the dead.
[51:08] Oh, but just a little bit back in time.
[51:11] A small price to pay for not saving after quite a while.
[51:17] So, yes, let's go and connect these parts to the out... What?
[51:24] One there.
[51:26] This one... Yeah, okay, we'll do that, but I need to be careful because I know it explodes.
[51:33] So I am just going to connect the velocity to there and hopefully... Oh, maybe that's because of the thingy.
[51:39] So node, make group, that's good.
[51:45] Um...
[51:48] R-er...
[51:50] Asterize...
[51:53] Yeah.
[51:55] That's fine, I need to make sure that it doesn't explode because I think that was the problem.
[52:00] The problem was that it just... It did divide.
[52:05] Oh, shoot, that's why.
[52:08] That was the problem at hand.
[52:13] Let's go and divide by the density so that the velocity does not get multiplied and become more than exponential.
[52:22] Because that was bad. That was really, really bad. Let's go and save this so that if it crashes due to my incompetence, we don't have something...
[52:32] Okay, it's still unstable.
[52:35] But something is telling me... Something is telling me... Oh, let's label these outputs here.
[52:41] So group, this will be velocity.
[52:45] This will be... Oh, what did I label this?
[52:50] Gradients. Yeah.
[52:53] This one will be the density grid.
[52:58] We just need those, that's all good and great.
[53:03] So now I need to figure out why this in particular is occurring.
[53:09] I have a few suspicions, but I want to be sure.
[53:14] So I'm going to connect there to there.
[53:18] Because I want to see...
[53:21] Okay, we can see that the velocity is accelerating.
[53:25] Not good. Not good at all.
[53:28] Which means that there is not some...
[53:32] The grid swapping, something's being lost in the interpolation there and back again.
[53:39] So the question is what? What is causing this to accelerate and do that?
[53:46] I'm just going to ignore it for the time being. I'm just going to turn it down.
[53:51] There should be no gain... Oh wait, no.
[53:54] Or is that just from the noise texture?
[53:57] Putting more energy into the system.
[54:00] It's from the noise, putting more energy into the system.
[54:03] So let's go... Let's see if any energy gets created or destroyed, breaking the laws of the aerodynamics, and Zeus's law most likely.
[54:13] Zeus's law. The Odyssey was an interesting movie.
[54:20] It felt like a play production, where it didn't really feel like I was in the world per se.
[54:31] Because I can't take Matt Damon seriously. That's just something...
[54:36] I thought many of the actors were phenomenal in their roles.
[54:39] For some reason I just can't take Matt Damon or what's the other guy?
[54:44] The guy who's playing the Punisher in the other movie.
[54:46] I can't take either of them seriously in a myth based movie.
[54:54] But it was still good.
[54:58] For those of you who joined in later, we were having movie talks beforehand.
[55:02] That's a great movies this year.
[55:05] That's a great movies this year.
[55:07] So we can see without any energy being added into the system, it still looks like something is being created.
[55:15] John Berthaw.
[55:17] That's probably his name.
[55:19] I don't know why.
[55:21] Probably because they look like people I would just see near where I live.
[55:27] So I don't know why I just can't take them seriously.
[55:36] The one shot of Agamemnon walking through the ory-farming while the gates opened.
[55:42] I was like, oh yeah, no, Nolan knows how to cook.
[55:49] There was one particular shot of them unfurling the sail to one of their ships.
[55:55] I don't know why, but it just felt grand.
[55:58] Even grander than a big display in other movies.
[56:03] I don't know why.
[56:05] Just the way it was shot, it just felt grand.
[56:07] And I like that.
[56:09] And I like that.
[56:11] So why is this accelerating?
[56:13] Why energy should be lost?
[56:16] Why is energy being gained here?
[56:19] Am I missing?
[56:21] Because nothing else is connected.
[56:23] The velocity is just going into here and out.
[56:26] It's being divided.
[56:28] So it's not...
[56:31] nearest neighbor constant.
[56:33] There should be nothing.
[56:35] But there...
[56:37] Oh, even there there's something.
[56:39] Is the problem?
[56:41] That's setting the velocity.
[56:45] And to be honest, I could just set it with a...
[56:49] I could just eliminate the node group to test this even further.
[56:53] So maybe I will do that.
[56:55] Just so that there's absolutely no possibility
[56:59] of something being very screwed up.
[57:02] And then it's a position, of course, needs to be the velocity.
[57:05] That's why I have the helper node group.
[57:08] Gale.
[57:13] Yes.
[57:15] There we go.
[57:23] And then that right there, that should be good.
[57:27] So here... Yeah, there we go.
[57:29] Okay, so there's something wrong with my setup.
[57:35] Okay, good to know. Good to know.
[57:37] So we eliminate that.
[57:39] Put this over to here. We put this over to there.
[57:42] We delete you. We put you there.
[57:45] We put this down.
[57:47] So, it's not a problem with that.
[57:50] It was a problem with me.
[57:53] That could be said about a lot of things, couldn't it?
[57:57] Let's see.
[57:59] Oh, hello, Ashley. How's it going?
[58:01] I'm trying out the new Rasterize Points node
[58:04] to try to make something along the lines of a fluid simulation.
[58:08] I think, I think this, even with my little brain
[58:13] who doesn't know what it's doing.
[58:16] It should.
[58:18] Why don't I connect a few more of these?
[58:21] It would work pretty well.
[58:24] The Gradient should now be like that,
[58:27] and it is setting the velocity itself.
[58:30] May still need to scale it.
[58:32] I should really have saved the version that worked
[58:35] instead of just, um...
[58:38] You know, I want the Gradient to be in there.
[58:41] I don't want anything else to happen.
[58:43] I just want equalization.
[58:45] So, that's making it attract to the nearby points.
[58:48] That was the problem.
[58:50] I need to scale that by negative one, of course.
[58:54] I hope you're all having a fantastic time.
[58:57] Ooh!
[58:59] There we go!
[59:02] Dang, look at that!
[59:06] So, that's what I needed to do.
[59:09] Look at that! Dang, okay.
[59:12] And it's still, the part that's lagging
[59:15] is mainly just the amount of grid points we have in there,
[59:19] so I'm going to bump that up so that we have something more realistic.
[59:22] Oh! Uh, yeah, wow!
[59:25] Wow, wow, wow, wow, wow!
[59:27] It does seem like we're still getting some weird glitches here and there.
[59:32] Dang, how about that?
[59:36] And it looks stable!
[59:40] Yay, I'm so happy!
[59:42] But yeah, we're working on 100,000 points,
[59:44] and it's still working quite well.
[59:47] Look at that.
[59:49] Let's take a look at the material, which I did not.
[59:51] That's because I forgot to actually connect the thingy.
[59:54] There we go!
[59:57] Let's take a look at... oh, very bright, very, very bright.
[60:02] But yeah, we can see there are a few little issues
[60:04] where things get a little too close to each other.
[60:08] But, look at that!
[60:14] Maybe it's because this box is a little bit too close for Comfort?
[60:18] Because the box is just happening on the points themselves,
[60:22] and not the actual grid.
[60:24] So if I do that, I just create the cube of torture, apparently.
[60:30] And boom, okay.
[60:32] Look at that! Woo! I'm happy, I'm happy.
[60:36] I'm reverting to being a kid again,
[60:39] even though I am nowhere close to that anymore.
[60:44] There we go!
[60:48] Look at that!
[60:50] It's... oh, is it because it always seeks to homogenize?
[60:56] Yeah, yeah it is.
[60:59] I'm still not doing the iterative divergence or anything like that, so...
[61:05] For what we have right here, I think this is pretty good.
[61:08] Let's go and just eliminate the input noise there.
[61:11] And again, it's not the most complex setup.
[61:13] The most complex part was me just eliminating the velocity step.
[61:17] Velocity... velocity step?
[61:21] Lovely!
[61:23] So, yeah, no, that...
[61:25] Again, you need to know about the little quirk, which is...
[61:29] Let's just organize this a bit more.
[61:31] You need to know about the quirk, which is just scaling the grid gradient by the transform.
[61:38] It's a weird quirk that is with this, but...
[61:44] Once you do that, and this won't work entirely because...
[61:47] I'm just getting the x-axis.
[61:49] Well, these can be scaled arbitrarily, so this won't work in all scenarios,
[61:52] but it should be mostly, mostly fine.
[61:57] The sparkly flash wildly moving is shredding YouTube's video compression?
[62:01] Oh, that is... that's... yeah, it'll do that.
[62:07] It'll do that.
[62:08] So let's add in some more noise.
[62:10] So now that we got the velocity, which is actually...
[62:14] Some stuff is being lost.
[62:16] Oh, no, that's fine.
[62:20] Let's see.
[62:21] Let's go turn the velocity down so that it'll try to stabilize easier,
[62:27] and then we have noise moving every...
[62:29] Yeah, no, that's probably ruining the compression,
[62:31] but we can go and turn on motion blur, crank it up so that we get something that has a bit more...
[62:37] Oh, but I forgot, point motion blur doesn't quite work as well as I'd hope.
[62:44] Yeah, something is occurring.
[62:47] It's like boom.
[62:51] Yeah, no, when I actually render it, the motion blur will be better.
[62:55] I changed this to be 1024 to make it a little bit better.
[63:00] There we go.
[63:02] And then...
[63:03] Alright, I need to go and hide the cube again because of the crash,
[63:06] because I made this simulation almost infinite.
[63:11] Like an absolute genius.
[63:14] But there we go.
[63:15] So there we have that.
[63:17] So if I were to render a frame, I would see...
[63:20] That took a hot second to render.
[63:24] Why?
[63:25] Why?
[63:28] I know, why is it...
[63:30] It should be taking a fraction of a second to render.
[63:33] The shadows, it usually is.
[63:35] No, it's not that.
[63:36] Why is it taking so long to prep?
[63:38] It's only a point cloud.
[63:40] There's nothing fancy or special going on.
[63:43] Sample's too high.
[63:47] No, it should be faster than that.
[63:49] It should be even faster than that.
[63:51] Well, look how fast it resolves.
[63:53] Problem, it's very tumultuous state.
[63:57] There we go.
[64:01] Yeah, no, that...
[64:02] There's no shot on Earth.
[64:04] That's not ruining the compression.
[64:07] But let's go and mitigate that by...
[64:10] At least a little bit, by normalizing...
[64:13] Normalize.
[64:15] There, come on.
[64:17] There we go.
[64:18] Take a look at this.
[64:19] And then all that is occurring.
[64:22] Now we can do kind of, you know, galactic...
[64:25] Kind of stop.
[64:29] That does look like something.
[64:33] So now, I actually don't know why it's doing this kind of density.
[64:39] So...
[64:41] Yeah, no.
[64:44] How do we make this actually work?
[64:46] Where...
[64:54] Where it'll be a liquid that's not trying to constantly homogenize,
[64:58] but at least homogenize a little bit.
[65:01] This to negative 9.81 meters per second,
[65:05] even though, yeah, no, I need to...
[65:08] ...divide by the delta time, so divide by 24.
[65:13] Now we have that.
[65:17] Dang.
[65:19] I don't know why I'm so shocked, but it's working!
[65:25] Why is it working?
[65:27] It's actually...
[65:28] Yeah, no.
[65:30] No, I...
[65:37] Look at that.
[65:38] I mean, it's not accurate.
[65:39] We can see that it's still having major issues,
[65:42] where it spikes, but...
[65:46] Oh, maybe I just need to put a cap on the...
[65:51] ...the divide right here.
[65:53] That's probably why I need to just set a...
[65:56] ...maximum, which means choose the maximum of these two values,
[66:00] so I can't go exactly to zero, causing a gigantic spike.
[66:05] Are you becoming British?
[66:06] Yes.
[66:07] Yes, I am.
[66:08] Thank you for noticing.
[66:10] Uh, no.
[66:11] I have historically hung out with British people quite a bit.
[66:17] So that may...
[66:19] If it hasn't affected my voice in the years that I've been hanging out with them,
[66:25] I would be shocked.
[66:28] But my native accent is the most generic accent,
[66:31] because I'm right in between New York and Boston.
[66:33] So I don't get the Bostonian accent.
[66:35] I don't get the New York accents.
[66:37] I've heard both in person, and they're always hilarious.
[66:41] I just get the most average accents in America,
[66:45] in Northern America.
[66:50] Yep.
[66:53] Look at that.
[66:54] That's a proper simulation right there.
[66:56] For some reason, my computer is now firing up,
[66:59] even though the simulation is fixed.
[67:00] So for some reason...
[67:03] You know, that's still taking a bit to render.
[67:08] Look at that.
[67:10] How do I render this without it compressing horrifically?
[67:18] Brailing?
[67:19] Do I trail that?
[67:21] Actually, that would be fascinating to go and take a look at.
[67:23] So yeah, let's go and try it.
[67:26] Let's see.
[67:27] We need to go and set ID.
[67:29] I also, just noting this for later, because, well, whenever I get time,
[67:34] I need to make a sample ID node for proper parenting hierarchies.
[67:39] I need to figure out how to do that.
[67:43] Because with parenting, you can't just parent things to index...
[67:49] to their actual index, because that index can shift
[67:51] when you join new things into geometry.
[67:54] So if you were to, like, get bones from an armature,
[67:58] but then the bones change, everything's broken,
[68:00] and you need to redo that.
[68:02] But you have a consistent ID.
[68:04] You can go and... it'll just work.
[68:07] So I need to make that.
[68:09] And it's also, like, you can technically do that with the transfer attributes node.
[68:14] But having something that's a little more convenient than this monolith would be good.
[68:21] Points to curves, of course.
[68:26] And then this will just be the ID.
[68:29] And the weight will just be the index inside the ID.
[68:32] So here, what?
[68:35] That's so cool.
[68:37] Now it is 100,000 points, so that explains a lot of the issues that we have here.
[68:43] I don't know why I'm so excited about this project.
[68:45] I think it's because it assembled, and I'm over an hour as I predicted,
[68:49] in terms of the stream time.
[68:51] I don't know why this project is exciting for me.
[68:56] I think it's because I've just been very, very busy.
[69:01] Now seeing a project that worked so easily and...
[69:08] Yeah, no, it's nice. It's quite nice.
[69:12] And actually, let's go and add an empty hair thing here.
[69:18] I do not want anything on it.
[69:21] Besides, no parenting, no UVs, none of that.
[69:26] Because I want it to render the curves.
[69:29] It's a little quirk that we can't set stuff in geometry nodes.
[69:34] Oh, I straight up deleted that geometry node thing. No matter.
[69:38] It's a little quirk that we can't set an object to be the curves data type.
[69:44] Like the one that actually renders the fur.
[69:47] I should have looked into that over a year ago at this point.
[69:52] Not the biggest steal, but would be...
[69:55] My laundry list of things for 5.3 and onwards is just barreling
[70:00] and becoming more and more and more.
[70:04] But I really need to...
[70:06] Oh, no, wait, that thing still exists. Never mind.
[70:08] Well, I can delete it now.
[70:11] And I don't have the time.
[70:13] But yes, efficient rendering of that.
[70:17] So, I'm actually quite surprised with how I cannot see through this thing.
[70:25] But let's implement the age value right here.
[70:29] So, sort of an attribute age.
[70:31] Just add in the delta time to the pregusting age.
[70:35] Would be nice if I made an increment attribute node group.
[70:39] I'm just making a laundry list in my brain.
[70:44] That's not bad, because this is why I do these live streams.
[70:47] I get to talk out loud without sounding like a crazy person.
[70:51] And I get to iterate on ideas quite nicely.
[70:56] So, we have that.
[70:58] Then after, it does that.
[71:01] Ooh, look at that!
[71:04] That!
[71:06] That!
[71:08] Look at that!
[71:10] Dang!
[71:11] Sorry, I'm so... Wow.
[71:15] It just works!
[71:17] This is the smoothest project I've had in a while.
[71:21] Dang!
[71:22] Okay, okay, okay, okay!
[71:25] Let's go and store some attributes.
[71:27] So, I'm going to get the gradient based on...
[71:29] Well, actually, no, I already have that available.
[71:32] I'm going to set the radius.
[71:33] Is that curve radius?
[71:37] Radius.
[71:38] Curve radius?
[71:39] No, I want to get the parameter to affect the radius.
[71:42] So, parameter.
[71:43] We won't be rendering the actual particles.
[71:46] We'll just be doing this since the attributes transfer automatically.
[71:49] That's fine.
[71:50] And I do enjoy that we have the transfer attribute's node,
[71:53] so we no longer need to...
[71:55] Well, we have the option of not needing to rely on weird conversion alternatives.
[71:59] But in this case, we just need points to curves and all that.
[72:02] Let's use a map.
[72:03] Now, color ramp is the way to go.
[72:07] Color ramp, and then a nice multiply off of that.
[72:14] I must say that's...
[72:17] Curves, uh, strip.
[72:19] There we go.
[72:22] I...
[72:23] Geometry nodes feels very nice these days.
[72:29] Look at that!
[72:33] Wow!
[72:36] Look at all of that!
[72:37] That is...
[72:39] So nice!
[72:41] And then just set the material.
[72:46] There we go!
[72:48] And I think I'll go and lower the...
[72:50] Well, now it looks...
[72:52] Maybe I should have the limit be by length instead of by...
[72:57] Um...
[73:02] Instead of by...
[73:04] Time.
[73:07] Because I'm not going to be able to do that.
[73:10] Because this is a little...
[73:12] It's a little bit much...
[73:14] When, um...
[73:16] When it first explodes.
[73:17] But yeah, let's take a look at this, and now hopefully...
[73:20] Yeah, there we go.
[73:21] Look at that!
[73:22] It goes and initially explodes...
[73:25] And then it converges into a nice...
[73:29] Look at that!
[73:30] I am so happy with this!
[73:33] And of course, I need to try to make it a lot...
[73:36] A lot worse.
[73:38] Am I going and doing that?
[73:42] I am...
[73:43] I am happy with this!
[73:47] I'm actually happy with this, wow!
[73:50] And I think...
[73:52] Let's see...
[73:54] I'm going to go and...
[73:58] Put this point to curves inside here...
[74:02] Then delete...
[74:03] How do I...
[74:08] How do I make it so that they'll delete based on their distance rather than...
[74:15] Well, step one.
[74:16] How do I find the parent of each one?
[74:18] I could stack the Nindak...
[74:20] No, no, no, no.
[74:22] Do I just curve to points inside the simulation zone?
[74:24] It'll slow it down, but I think it might be preferable.
[74:28] It might be preferable.
[74:34] It's pretty.
[74:36] So pretty.
[74:40] Look at that!
[74:42] That is the money shot right there.
[74:44] That is going on Instagram.
[74:49] There we go.
[74:50] Look at that!
[74:52] This explodes first and then...
[74:54] Turns into that!
[74:57] I do want to put in more points, but this...
[75:00] Recently, I was looking at old renders I made from 2020.
[75:05] And I've done a lot of beef.
[75:08] That was before I was on social media or anything like that.
[75:11] And when I was looking at it, I was getting just...
[75:14] Was that a pseudo gravity I put in?
[75:18] Why did I...
[75:19] Oh, because it was...
[75:20] Yeah, that divided by however much.
[75:22] Yeah, yeah.
[75:24] And I was getting...
[75:25] What's it called?
[75:26] Maybe even a little bit jealous of my past self.
[75:31] My 18 year old self or 17 year old self?
[75:35] Because that stuff...
[75:37] Despite the circumstances I was in then...
[75:41] Those renders still hold up today.
[75:43] They were more artistic rather than technical.
[75:46] But...
[75:47] I keep forgetting that even though I do more technical than artistic renders nowadays...
[75:53] I still have an eye for making things look pretty.
[75:55] Even if it is emergent from the technical stuff I make.
[76:01] Always nice.
[76:02] Always nice to see that.
[76:03] Let's go and bump up the points to be...
[76:06] Not 100,000, because I think that'll be a bit much.
[76:10] Yeah, it's a bit much for even the trails.
[76:13] But here we can see.
[76:16] Yeah, no, well...
[76:18] I am assuming that's from the little Velocity Spikes.
[76:28] Still so cool to see.
[76:31] Yeah, isn't it weird how your past self from a few years back just feels like a different person?
[76:37] In style and in tone?
[76:40] I am happy, mostly with the person I am today and the work that I'm doing.
[76:44] Though I do miss animating and making pretty artistic renders.
[76:48] I've been focusing more on the 2D side when it comes to that.
[76:52] The 3D side, due to work, of course, is quite technical.
[76:56] Because that is my...
[76:58] Level of expertise.
[77:01] This could be used to make the surface of the sun, potentially.
[77:05] I do want to make it based on Oolang.
[77:07] So let's go and set it back to the one that I liked the most.
[77:11] Ah, yes.
[77:12] Look at that, it's so pretty.
[77:16] So pretty.
[77:18] Okay, back to the curves.
[77:20] How do I make it so that it does it based on distance?
[77:24] So I guess I'm going to...
[77:27] Points to curves, curves to points, hopefully all the attributes.
[77:34] Yeah, it'll be like this.
[77:35] This will be evaluated.
[77:37] I'll do that.
[77:41] Join them, put it there, and then put it through there.
[77:45] And then, this should still work with deleting...
[77:48] Uh oh.
[77:50] It's like, no, you can't do any more curves to points, because the curves are already points.
[77:55] Well, it is, yeah, it's more expensive, but it's not that much worse.
[78:01] And everything else is working as intended.
[78:03] So now, I can go and delete points if they are too far away.
[78:09] So, what's going to get the spline parameter, and it's the length.
[78:13] Though, I'm not sure this will...
[78:17] Because the length is just the factor multiplied, but it's not the length of each segment.
[78:22] It's the length overall.
[78:25] It's just the factor gradient multiplied by the length.
[78:28] Though, I'm not sure if this will work as intended, or if I need to use the accumulate field method.
[78:34] Well, I'll figure it out.
[78:37] It'll be fine.
[78:38] So there we can see.
[78:40] Uh oh.
[78:44] Little worried about that.
[78:48] Should I do this after?
[78:50] I should do that after, yeah.
[78:51] And then, yeah, I'll just keep one second main limits.
[78:56] And put that over there.
[79:00] Oh shoot.
[79:01] Oh shoot.
[79:02] I hope that other things have not gone horrifically wrong.
[79:12] Or does this need to be like that, because that's the new start?
[79:16] Oh yeah, that's all that was needed.
[79:19] There we go.
[79:21] The order was just incorrect.
[79:24] So let's set that to be like five.
[79:26] The max will be five.
[79:28] And then the distance here will be two.
[79:32] And also, at the very least, I need to make it so that it will not delete if the...
[79:38] It'll only delete if the index is greater than one, so that there are at least two points.
[79:44] So that...
[79:45] And that will need to occur before a deletion occurs.
[79:52] So there we go.
[79:53] Now these will be based on distance rather than time.
[80:02] Not sure if I like that, but we'll go and play around more with it.
[80:08] Because now it's harder to tell the speed.
[80:15] Folks, hmm.
[80:18] I'm half and half on it.
[80:21] Let's go and fully turn off the age deletion, because I may go and...
[80:27] Mix the gradients a bit.
[80:30] Have a little bit of both.
[80:33] Actually, no, the five-second deletion is absolutely necessary.
[80:39] Because of the points don't move.
[80:42] I want to make it so that...
[80:45] Actually, just to...
[80:47] Yeah.
[80:49] Actually, just to...
[80:53] Umm...
[80:58] Yeah, let's...
[81:00] Let's combine these so that I don't have multiple delete nodes.
[81:03] It's always best.
[81:06] I don't have to deal with that.
[81:09] So our deletion stage happens after that, which...
[81:12] The deletion doesn't necessarily have to happen after...
[81:16] The joining.
[81:18] But that's fine.
[81:20] I'm just enjoying the stop, the time, doing things...
[81:26] With geometry nodes.
[81:28] And it's also, it's a fairly light setup. I'm amazed.
[81:30] It's still not accurate.
[81:33] But...
[81:37] Pretty cool.
[81:39] Why is the gradient itself working well with this?
[81:42] I'm not even using the divergence.
[81:46] I don't know.
[81:48] Such a simple simulation.
[81:50] Such a dumb simulation.
[81:52] But it leads to such a cool result.
[81:56] That I...
[81:58] Wouldn't have thought of.
[82:01] Although...
[82:04] Hmm.
[82:05] I don't know.
[82:06] Let's go and turn back only time-based...
[82:11] Deletion.
[82:18] Oof.
[82:20] I don't know which looks better.
[82:27] Because you can tell the speed by the lengths of the arcs, which I really like.
[82:32] But...
[82:33] But...
[82:35] Seeing that full trail...
[82:41] That's also, I don't know, you get to see the pattern a lot more with this.
[82:45] That's the noise pattern.
[82:47] So, okay, I'm gonna save this in its current state because it's working quite well.
[82:54] Let's go, we don't need the initial noise right there.
[82:57] So, I'm going to go and turn up the noise to five and let's see what occurs.
[83:04] Ah, yes.
[83:07] It's ignoring gravity.
[83:09] Quite a bit.
[83:11] Oh, right, because...
[83:13] Wait a minute.
[83:15] Here, we gotta multiply this by delta time.
[83:19] We gotta scale this part by delta time.
[83:22] All the forces by delta time.
[83:27] Forces...
[83:28] And then that's just...
[83:29] That's actual distance.
[83:35] So, this will be offsets.
[83:38] Or, no, no, no, velocity.
[83:40] Velocity and then one arc, these ones are the forces.
[83:44] You add them all up, put them in there all the day.
[83:48] Yep.
[83:49] So, this needs to be 9.81, 9.1 meters per second.
[83:54] Do that.
[83:55] So, that should...
[83:59] ...things back.
[84:01] Then here, we have something along these lines.
[84:06] Yeah, I'm just gonna go and turn on this part.
[84:11] So, again, with this...
[84:15] It is...
[84:23] Must be greater than two...
[84:24] Oh, okay, they're just...
[84:27] Wait, why?
[84:29] Alright, there's a point there.
[84:31] Why isn't not making...
[84:34] Things there?
[84:35] Not sure.
[84:37] Anyway.
[84:42] Let's go...
[84:43] It's a point five.
[84:44] Wait, that's fine, that's doable.
[84:47] We have that part there, doing that.
[84:49] So...
[84:51] Let's go and have an alternative method.
[84:53] There should be 24 to match what we had previously.
[84:58] Yes, there we go.
[84:59] So, that's what we previously had.
[85:02] Let's go and have this be the position, scaled by negative one.
[85:06] I hope you're all enjoying this nice simulation.
[85:10] And everything, it's working out quite well.
[85:14] Working out surprisingly well.
[85:16] That's the forces, we do that and that's...
[85:22] Hello, will you do a tutorial on the ship going through the space fabric?
[85:26] Funny you should mention that.
[85:28] You can currently get that file on Blender's website.
[85:32] On the example files.
[85:35] They specifically...
[85:37] Oh, was it?
[85:38] Yeah, they specifically asked for that file to put on their page.
[85:41] Look at that, that's so cool too.
[85:43] Wow!
[85:44] Just one note, just one note combined with like the other grid nodes.
[85:48] All those for so much cool stuff.
[85:51] Wow.
[85:52] Thank you very much to the...
[85:55] I forget...
[85:57] Whoa!
[85:58] Sorry, I'm just...
[86:02] I'm just kind of blindsided by this.
[86:04] That is...
[86:06] I didn't expect it to work this well.
[86:10] But it is!
[86:11] Look at that.
[86:15] All kinds of things are possible now.
[86:19] Um...
[86:20] And this also means that hair self-collisions will be...
[86:26] Not easy, but easy-er.
[86:29] Do.
[86:30] Because that's how they at least...
[86:32] Pixar in the olden days would do hair-based self-collisions using volumes.
[86:39] Because it's just significantly easier to do it that way.
[86:44] And better, and better.
[86:46] And better, and better.
[86:49] Look at that!
[86:51] Let's go and weaken this initial attraction first, because I want to see more.
[86:56] Look at it!
[86:58] It's still approximated because the volumes are, you know, doing other things.
[87:06] But it just feels so...
[87:08] It just works in the famous words of Todd Howard.
[87:12] Let's go and turn this down, because right now, how many voxels are we playing with here?
[87:17] Not many.
[87:18] Well, actually a fair bit.
[87:20] I think just a point one, this will cause it to lag.
[87:23] Oh, actually no!
[87:24] Look at that!
[87:25] But yeah, with that, it's a bit less...
[87:28] Joined.
[87:30] Which I think, like, if I were to do multiple iterations, it does that.
[87:35] It's an interesting situation where the less voxels you have, the prettier it looks.
[87:41] I am not complaining whatsoever about this.
[87:44] Though I need to look into methods where I need to make a limit so that when explosions happen, it won't cause it to crash.
[87:53] If there is, like, a voxel...
[87:55] Actually, is there?
[87:58] Or maybe I could just limit the position of what's being fed into it so that the grids that come out cannot be larger than a certain extent.
[88:09] Um...
[88:10] Yeah.
[88:13] Just like, that's just the surface of the sun!
[88:16] Right there!
[88:18] Let's do that, and yeah.
[88:21] It's mainly...
[88:22] The big thing that's helping is just the velocity curling with all that.
[88:27] Oh yeah, curling a grid!
[88:29] I'm not even doing that, I'm just getting the velocity.
[88:34] And it's just emergently turning into curling.
[88:39] Very cool, very nice, I love it!
[88:44] And then we can also, instead of...
[88:46] No, I want to keep that, but also let's go and use a cross product.
[88:51] But also I need to normalize...
[88:54] Yeah, let's just normalize this, because instead of having...
[88:59] That, let's normalize it so that we just get an inwards gravity.
[89:04] In this case, if I set this to be zero...
[89:10] Is that...
[89:11] Wait, what is...
[89:12] There's very little damping happening right there.
[89:20] Why is it...
[89:24] Oh, the cash-dent reset.
[89:28] Look at that!
[89:30] Like, voids.
[89:34] That is so nice.
[89:36] So nice.
[89:41] Oh, you weren't able to find it.
[89:42] Oh, um...
[89:45] I forgot what page it's on.
[89:47] Under...
[89:49] Example...
[89:50] Example...
[89:51] Files.
[89:53] It needs to be on demo files.
[89:55] Geometry nodes.
[90:00] Geometry nodes.
[90:02] Here we are.
[90:05] Or wait, is that one...
[90:09] Oh wait, I'm not seeing...
[90:11] Oh no, it's there, it's there.
[90:13] So they chose a different...
[90:15] They chose an interesting screenshot for that one.
[90:20] Or you can like, see the wireframe.
[90:25] Huh.
[90:26] Actually, yeah, I wonder what that icon is.
[90:28] Anyway, here you go, here you go.
[90:30] It's going just put in there.
[90:32] So that is where the demo files are.
[90:34] If you look in the simulation part,
[90:36] you'll see the space fabric tear.
[90:38] It looks a little bit different, cause...
[90:39] Oh!
[90:40] They're viewing it in the preview mode, not the rendered mode.
[90:42] Yeah, that's... that's fine.
[90:46] And then there's also the sample sound frequency setup.
[90:49] Over there, I recommend picking that one up as well,
[90:52] cause I did not...
[90:54] Put that one up on Gumroad, either.
[90:57] Yeah.
[90:59] And the...
[91:01] There's going to be, in 5.3, there's going to be more simulation demos there.
[91:05] Probably.
[91:06] I don't know for certain, I don't know for certain.
[91:08] I should specify.
[91:10] What is your graphics card?
[91:12] It is a RTX 3060 Ti, or not Ti, I forget.
[91:17] Which everyone has like...
[91:18] Well, I think I have 12 gigabytes of VRAM.
[91:23] Which, these days, RAM is a little bit more than that.
[91:26] Which, these days, RAM is solid gold.
[91:28] I didn't know until I...
[91:29] I was looking at getting more storage space.
[91:34] And I can manage my storage space very well,
[91:36] cause these setups are very light,
[91:38] but I was looking into more.
[91:40] And, like...
[91:42] It's tripled in price!
[91:44] It's gotten so much more expensive.
[91:46] Oh, we're seeing some grid patterns here.
[91:49] Yeah, okay.
[91:50] So, this setup, it's not perfect.
[91:52] I think it's due to the linear linear, if I had to guess.
[91:55] But anyway.
[91:59] Let's go and do this.
[92:00] Let's set this to be 10.
[92:02] Cause what I want...
[92:09] Not, okay, it looks like we need to combine them.
[92:11] So, let's do...
[92:13] Add...
[92:14] Well, add them both together.
[92:16] I should...
[92:19] So, they're more like this.
[92:21] And so, oh, wait, no.
[92:23] Some of these...
[92:28] Some of these still leave.
[92:30] They should not be...
[92:32] I specified that rule.
[92:33] Okay, now there we go.
[92:36] I mentioned if it's greater than...
[92:38] Do the indices of these curves start at...
[92:40] What?
[92:43] If it's greater than...
[92:44] No, but that makes that happen.
[92:48] Why...
[92:49] It needs to be more than that.
[92:51] And I'm...
[92:53] I don't know what kind of question that.
[92:55] I'll look into that another time.
[92:57] Probably not even a major issue.
[92:59] I probably just skipped something.
[93:01] There we go.
[93:04] Okay, so instead of...
[93:08] Doing this, I'm going to mix the vectors.
[93:11] So, I'm going to do a mix, a normalize.
[93:15] Be that and that.
[93:18] It needs to be set to be negative one.
[93:22] Let's see.
[93:25] Let's see.
[93:27] So that and that, then we throw that into another normalize.
[93:31] And then we do that.
[93:34] Plug it into there.
[93:36] That's just to get a vector that swirls,
[93:38] but also brings it inwards.
[93:41] So there, we are going to bias it more internally.
[93:46] Let's see.
[93:49] I did set that part to negative.
[93:51] Yeah, I said that's a negative one, yes.
[94:03] Oh, I did a double negative.
[94:07] Of course that would be incorrect.
[94:11] But there we go.
[94:12] Now it looks like that.
[94:14] I could put in a bit more of a swirl into it.
[94:18] In this case, yeah.
[94:21] The velocity will start dragging it out more,
[94:24] which I'm a little bit concerned about, but it seems to be okay.
[94:27] Now if we set this to be like 24,
[94:31] add in a bit more chaos into it.
[94:36] A bit too much there.
[94:38] Let's go and turn it down.
[94:43] Let's see.
[94:44] Your rendering is way better than mine.
[94:46] GTX 1080.
[94:47] I think I had a 1060 previously,
[94:49] but that was probably a decade ago.
[94:53] Yeah.
[94:54] I've heard that the RTX 3060 is outdated by today's standards,
[94:58] which RTX probably came out like eight years ago at this point.
[95:03] Five or eight years ago.
[95:05] But with, of course, artificial intelligence
[95:09] hogging up every resource on the planet,
[95:13] it's...
[95:16] I'm not sure I want to buy a new graphics card anytime soon,
[95:20] especially because my renders are very CPU bound.
[95:25] I don't render in cycles all too often,
[95:27] and when I do, it's usually not mine.
[95:35] I'm gonna turn that up.
[95:38] Okay, now I'm just playing around with this.
[95:40] I think this is good for today.
[95:43] I think I'll just go and play with it off-stream.
[95:45] Hopefully YouTube's compression is not horrible.
[95:51] When it comes to stuff like this,
[95:52] I'm just gonna play around with a little bit of the lighting.
[95:56] Lighting.
[95:58] And also, we could still take a look at the volumes for this.
[96:03] Now, I am going to...
[96:05] Because we still already have the volumes.
[96:10] We could go and just plug that here.
[96:15] We can store the grid.
[96:19] It does do that.
[96:21] Then we can see at least the bounding grids here,
[96:24] which, oh, it's interesting how that's...
[96:26] Oh, I also need to try the grid to points node,
[96:28] because I have an...
[96:30] Yeah, look at that.
[96:32] It's like, not the fanciest smoke simulation.
[96:40] It's like, oh wait, I need to hide the points,
[96:42] which I specifically...
[96:44] It's that point radius.
[96:46] I don't really need any radius where all these are going.
[96:51] I could join the trailing into the main fold,
[96:54] but I don't think it really need to.
[96:56] But yeah, so if you want a pseudo smoke sim with particles,
[97:00] I can't say I recommend it.
[97:05] Although, I don't know.
[97:09] I do need to look into actually making smoke sims,
[97:14] because I haven't properly tried that in GeoNodes,
[97:19] but it seems more...
[97:22] Oh, no, that's where I would actually need that divergence,
[97:26] and all that sampling.
[97:28] Oh, I don't want to worry about the sampling.
[97:31] Yeah, no, I think I'm okay for now.
[97:35] I'm okay for now.
[97:37] So let's reset you.
[97:39] We'll go and chop you out of there.
[97:43] I have a set point radius before.
[97:45] No, I don't need to worry about that.
[97:47] Yeah, with a simple setup.
[97:49] The most complex part is my node groups for the collision.
[97:54] Then again, this is the internals here.
[97:58] One new node lets a lot of stuff be possible,
[98:03] even as particles that look so coherent.
[98:08] Oh, restriction totals.
[98:10] There we go.
[98:11] Did they change that?
[98:14] Probably did.
[98:16] There's other...
[98:17] Oh, right, points to grid.
[98:18] That's what I wanted to...
[98:19] Or no, grid to point.
[98:23] That's what I wanted to take a look at.
[98:26] So, and it has a value.
[98:30] But this part in particular, I just want to see...
[98:34] What it's these.
[98:35] No, I do not want to take a look at that part right there.
[98:40] Okay, show me the grid.
[98:43] And for grids, we have no grids.
[98:52] The grid?
[98:55] No, there is a grid.
[99:00] Oh, I...
[99:01] Boy.
[99:04] Okay, so those are all...
[99:06] Wait.
[99:09] It's a sparse grid.
[99:10] Of course, of course, that makes sense.
[99:13] It's always nice when...
[99:15] More efficient.
[99:18] Is it because of...
[99:20] Ah, yes, we can see here.
[99:23] By going divided by two, because these points are probably a bit much.
[99:28] Yeah.
[99:30] Here we can see the dense...
[99:32] Or no, let's set this to be to the power of point five.
[99:35] Square root.
[99:38] But there we go.
[99:39] Those are the densities for all those parts.
[99:41] Visualizing the voxels.
[99:45] So I can visualize all the things as I want.
[99:50] For the velocity, I could also go and get the velocity grid, but I have that inside there.
[99:55] I don't think we'll need that, but this means I can turn all your volumes into the Lego...
[100:02] The Lego Explo...
[100:04] You know how in the Lego movie, which was a formative movie I watched in my childhood,
[100:09] had the explosions.
[100:11] You could do that previously in Geometry Notes, but this is just more efficient.
[100:16] Probably if you were to prune the grid.
[100:20] No, because it's already pruned, I think.
[100:25] Yeah, if you go and voxelize the grid, this should make it so that everything is even.
[100:32] Oh wait, does this voxelize the grid?
[100:37] I forget.
[100:38] I forget.
[100:40] And these don't have similar values either.
[100:43] So I'm going to try putting the velocity grid there.
[100:51] I'm putting this out to here and then this one.
[100:57] That'll be a vector, that'll be a vector, that'll be a vector.
[101:00] Plug this into there.
[101:01] Let's see what we've got here.
[101:04] Nice grid.
[101:07] But it has the data that we can then store.
[101:10] Okay, fun, fun times.
[101:12] We do not need that.
[101:13] We don't need more data stored on there.
[101:15] All we need are the points, which will then subsequently be trailed into a much prettier thing.
[101:22] And then I can set the colors to be pretty...
[101:26] Length.
[101:27] Let's go and put this there.
[101:29] Let's go.
[101:30] We get the velocity length and then we can put that into...
[101:34] Let's see.
[101:36] I'll use my classic LG light pull off thing.
[101:39] Oh, it's...
[101:42] Yeah, this just makes the gradients look better.
[101:45] And also I need the curve...
[101:50] Curves info.
[101:53] So we have that, we have that, we have the length.
[101:55] I think it's the intercept.
[101:57] Let's look at that.
[102:00] We put that into there so that we get a very nice looking sharp gradient that we can multiply.
[102:05] It's the wrong side.
[102:07] Actually, if I map range, it makes it look a bit better.
[102:10] Map range and then smooth the step.
[102:13] Smoother step.
[102:15] Then emission, transparent.
[102:20] I've been hearing a lot about order independent transparency and I would like to know more about it.
[102:27] Apparently, it's a second coming of Christ when it comes to transparency based stuff.
[102:36] Oh, compositing.
[102:38] Perkot.
[102:40] Bloom.
[102:41] The composter is so useful these days.
[102:43] I've been using it for many things and it has been fantastic.
[102:49] I should store the density on these points as well because that could look very, very good.
[102:56] Let's go and change this to be a nice color.
[102:59] This is when I would switch back to like AGX because that would look even better.
[103:03] Or AGX or ACES.
[103:07] I do like ACES 1.3 more than 2.0, but...
[103:12] AGX.
[103:14] I'm still biased towards the colors of ACES 1.3.
[103:20] Yeah, I can make anything I want now.
[103:24] But I think just visualizing the velocity is better.
[103:29] Back to standard.
[103:32] And then if we take a look at this, we can say yeah, no, a bit bright.
[103:38] But I do like what we have here.
[103:41] I'll probably render out the initial one you saw before.
[103:45] But let's go and just try...
[103:47] Let's go back into the stem.
[103:50] Let's get two of them that just look good.
[103:55] That one, I won't worry about swirl for now.
[103:59] I think that's okay.
[104:01] What I want is just this to go down into there.
[104:08] Go, it just collapses in on itself and then we have a bit of noise keeping things nice and speedy.
[104:20] There we go.
[104:23] You should now to shark and make those fish react by going far.
[104:26] I could do that quite easily.
[104:28] It's just adding another force.
[104:33] So many things are possible with just a little modification to Blender.
[104:39] Just a little modification to Blender.
[104:45] There we go.
[104:48] I want to make it so that's attracted towards the center quite a bit more.
[104:51] There we go. That's better.
[104:54] Go towards the center and then the noise can take over.
[104:59] There we go. Yeah, that's a cool one right there.
[105:02] That'll be the formation of the sun or the formation of earth, something along those lines.
[105:07] I can make something like the Coriolis effect.
[105:10] Just doing a simulation on the grid, getting the nearest neighbor information.
[105:17] This is the index of Nth nearest. No, this is voxelizing the simulation.
[105:21] Since I'll be ending this stream right about now, because we're at something that looks pretty good.
[105:27] Let's let that to be like 100.
[105:29] Oh, that looks so energetic and pretty.
[105:33] I love it.
[105:37] Yes, let's take a look at the sim.
[105:39] So I'm trailing the sim to make these nice curves and all that.
[105:42] But the actual...
[105:45] Actually, let's organize this really quickly.
[105:50] Rail curves, and that needs to be a separate object, right?
[105:53] Let's just be Gn.
[105:56] Let's make it nice and green. Put that into there.
[105:59] Collision, cube, cube collision.
[106:04] And this one will be particle sim.
[106:09] Put that over into there.
[106:11] Trail curves, put that over into there.
[106:13] That's good. That's good. That is lovely.
[106:16] For the actual particle sim, just to review as we are at the end for all of you who skipped to the end of the videos.
[106:22] Not judging. I do that.
[106:26] Right here. We have a good amount of points.
[106:29] I could do a lot more short stream.
[106:31] Well, I know. I predicted that at the beginning of the stream.
[106:35] I was like, this is going to be short stream, but we all know that it doesn't stay that way.
[106:38] I just had to get warmed up back into the vibe.
[106:45] We have some particles. They have an initial position.
[106:48] This part isn't all too necessary, but this is the key.
[106:53] So we just have the velocity step.
[106:55] We set a velocity. I'm sorry. That reroutes.
[107:00] I need to do more with reroutes. There we go.
[107:04] We do a velocity step by adding enforces, but the main thing is taking the velocity rasterizing it to a grid and then putting it back onto the points and the gradient.
[107:16] So here I'm taking the velocity and the density.
[107:19] This is the density right here because it rasterizes and basically accumulates it to voxels.
[107:25] You can kind of see that here.
[107:27] We have this, the velocities and that.
[107:30] We go and get the gradient from the density, whichever parts have more density.
[107:36] They'll be repelled away by that gradient vector, but we need to scale it by the size of the voxels, which in this case, I'm just getting the X scale of the grid transform.
[107:49] This is just the fastest way of doing it.
[107:51] There's a simpler way.
[107:52] If you like separate the transforms and separate the scale, but this less nodes, it's more complicated, but it's less complicated.
[107:59] But it's less nodes.
[108:01] You don't need to worry about that.
[108:02] It just scales it based on the grid so that it doesn't go into infinity because yeah, the grids have turned in anyway.
[108:10] Anyway, anyway, anyway, I get the velocity.
[108:12] I voxelize it.
[108:13] Then I divide it by the density so that it doesn't go into infinity as well.
[108:17] Then I sample both the gradient and the velocity and then I put that into the sim.
[108:23] The density here is being output to the end purely to visualize and because I could turn that into like a pseudo smoke simulation.
[108:31] I am colliding with a cube, which isn't actually happening in this simulation, but this is using node groups from my free node group pack that's up on my Gummary page for free.
[108:43] It's simply how I do collisions with meshes all the time.
[108:48] It's just a good way as bounce as friction and it's mostly good.
[108:52] I think it's mostly good.
[108:54] But these two nodes really, really, really, really good.
[108:57] And this also works with volume based SDFs.
[109:03] So I could like sample a grid's SDF and it's normal gradient and it would work.
[109:11] So even though this was made probably a year before the volume grid notes, I had the gift of foresight and that did it.
[109:22] I see my role because I've been thinking about the Odyssey.
[109:26] You know, I don't know.
[109:28] For me, this is not part of the Odyssey, but it is related to I guess gift of foresight and bringing fire to all of us.
[109:37] Let's see.
[109:40] Oh, four minutes ago somebody reviewed my lightning bolts generator on Gumroad. Yay.
[109:46] That is an old set of it.
[109:48] So old that set up was used in Sonic 2 before it was even brought on for Sonic 3.
[109:53] I am amazed that that set up still has legs.
[109:58] Yeah.
[110:01] I'm amazed that set up still has legs.
[110:03] But yes, here we have what could be a water simulation.
[110:08] But it works as particles as well.
[110:10] I like the particle based look for it.
[110:13] So that's all that's all good.
[110:16] Can we get point velocity with this and then use it to add effect grid for smokes him.
[110:21] Basically, well, I'm not sure if I would recommend.
[110:26] I don't know.
[110:27] I've affecting a grid.
[110:28] You could do that without particles whatsoever.
[110:30] You could do that previously.
[110:32] It was just a little bit funky with how I haven't been able to figure it out.
[110:38] Mainly because of the I think I was tripped up on the grid gradients needing to scale that by the transform and then also the grid divergence and needing to scale that in a weird way.
[110:51] I don't entirely know how that is supposed to work because it is a little bit weird.
[110:57] I need to revisit it.
[110:59] I think other people have made smokes.
[111:00] The Blender developers for I am blanking on the name the last open movie project sing Singularity.
[111:09] They made a nice little fake smoke simulation using geo notes.
[111:14] And I say fake because it was an approximation, not because it was bad or anything, but it did use volumes and stuff like that.
[111:22] I'm pretty sure.
[111:24] Now we have the chance to do more complex particle Sims and inefficient and quite stunning manner.
[111:32] I do say so myself.
[111:34] And this isn't using divergence.
[111:36] So there's still more that needs to be done with this.
[111:40] But I think with particles, maybe it's still okay.
[111:43] I mean, it looks like curl noise.
[111:45] So it might be handled okay with the way I set it up.
[111:49] Yes, it worked out well.
[111:51] So we're almost at two hours.
[111:53] This went on for way too long, but I enjoyed it.
[111:56] And that's what matters.
[111:57] And hopefully you all did as well.
[111:59] Thank you all for watching.
[112:01] If you have any last questions, ask them now.
[112:05] Yeah, look at that.
[112:08] It's energy flowing from place to place.
[112:11] I do need to store the density.
[112:19] Yeah, do I sample the grid again just to get the density?
[112:23] But the whole goal of it is to have very little.
[112:27] I don't want to have to store it, if I'm being honest.
[112:35] But I kind of don't want to.
[112:37] I'll check that upstream.
[112:41] We just have these two.
[112:45] And then we do that.
[112:51] Okay, but that's all good.
[112:53] All right.
[112:55] I think that is everything.
[112:57] So thank you all for watching and I will see you all next time.
[113:01] Have a good rest of your evening or morning time zones.
[113:04] I keep forgetting about that.
[113:06] Have a good one.



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
