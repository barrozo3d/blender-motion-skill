---
title: (Spoilers) Spiderman Tornado Webs Test (Blender 5.3)
source: YouTube
url: https://www.youtube.com/watch?v=ufaZPxkiwtM
author: Cartesian Caramel
ingested: 2026-08-09
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/spoilers-spiderman-tornado-webs-test-blender-53/
frame_count: 0
frame_status: pending-selection
---

# (Spoilers) Spiderman Tornado Webs Test (Blender 5.3)

**Source:** [YouTube](https://www.youtube.com/watch?v=ufaZPxkiwtM)
**Author:** Cartesian Caramel
**Duration:** 112m52s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py spoilers-spiderman-tornado-webs-test-blender-53 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] and welcome... wait... okay the stream's running, okay.
[0:03] Hello everyone and welcome to today's livestream where I'm going to attempt to recreate
[0:08] the Spider-Man Web Tornado effect from the new movie.
[0:12] I saw the new movie Spider-Man brand new day and it was good, I really enjoyed it.
[0:18] Um, so I want to try this out. So let's start with step one,
[0:22] which is to do some analysis. How does this effect actually work?
[0:26] Because I... my gut is telling me that this might not be all too simulated.
[0:31] So let's take a look at it at speed, hopefully... oh yeah no, it's lacking because of the proxies and
[0:37] all that. Let's take a look, he descends and then it does that. But from what I'm seeing here,
[0:44] it seems like these parts, they're not wobbling as much as I would expect. There seem to be...
[0:49] I also... my memory is failing me, but I think this might have changed a lot between
[0:57] the trailer and the movie because it seems a lot simpler than I would originally think.
[1:02] I'm going to do a simulated method because that's why I want to try, but just from looking at this,
[1:07] it seems like there are squares, kind of squares that have the webbing in between them,
[1:13] and then in this case they seem to... like with this one right here, it just seems to mix the
[1:18] positions between there and there. I'm assuming if this is how the final effect looks, that this
[1:23] was for artistic effect because there's the parts that go down there. Do they go through there?
[1:34] Let's see, they're the ones who go through there and then how do they attach to that?
[1:41] Yeah, I think they might have... this is just a wild guess, but I'm assuming that they chose
[1:48] where the webs would end up and then mix them to the original position with maybe a bit of
[1:57] simulation on top. That's what I'm guessing. I'm going to try, and especially right here,
[2:06] it looks like interesting. So that part goes there and it goes around.
[2:18] That's very interesting. Maybe it is... I don't know. Maybe it's simulated, maybe it's not.
[2:30] All right, but let's get to work on actually making the effect.
[2:34] So let's go and check all this, make sure everything's there. Okay, so how would I go
[2:39] and recreate this effect? So step one, let's go and create an empty. This empty will be the
[2:44] direction of our spinner that fires. So let's go and make this single arrow.
[2:53] No, let's make it arrows and let's make it so that's the z-axis of course.
[2:57] No, actually no x-axis because it'll be going down and spinning around. Okay, let's go and bring
[3:02] this up to... let's do six meter... yeah, six meter seems fine. So we're going to simply do that,
[3:11] then bring it down to zero because we're going to imagine that all spider-man here face plants
[3:18] 720 degrees so that does three spins. So taking... nope, it needs more. Let's go and multiply that by
[3:25] two. Just by two. There we go. Just do that. Okay, basic animation that is good enough for now.
[3:37] So let's set up our collider. So I'll make this a collider collection and we'll just put this
[3:45] right here. I'm going to invert the normals so that here let's go and turn back face calling on
[3:52] so that we can see the internals. Let's go and shift Z. Maybe about... yeah, that seems to be good.
[3:58] A decent size for the room and back face calling now contributes to what you can select,
[4:04] which is both good and maybe a bit annoying. But yeah, that's fine there. I almost want to turn
[4:10] this into an octagon because I think that might make the effect a bit better. Yeah, that'll be good.
[4:16] So basically we're going to make webs fire and then attach to there and then when they hit... okay.
[4:23] So the simulation is going to be... we're going to make particles, vertices fire from this location.
[4:29] They attach to the walls when they hit, they freeze, they stick to the walls, they don't move anymore.
[4:34] And that's good. But they're attached by edges and when they're attached by edges, they shrink to
[4:41] give the kind of web effect. Okay, this will be interesting. I've done pseudo web effects before,
[4:47] but I've never done it in this way where it's like a continuous dream that goes. Or is it even?
[4:56] Is it... well, we'll try multiple methods. Okay, we don't want geometry nodes on the actual empty,
[5:01] we don't want geometry nodes on the collider. We want a new thing here, which maybe... do I want
[5:07] this as a curves? Well, we'll deal with that later. Let's go and add in an empty or a mesh plane.
[5:17] Let's do this the way it's... let's use a mesh plane because it doesn't require original data.
[5:22] As we can see here, there's no geometry input, just a geometry output. That's not there,
[5:28] that's labeled as collider. Nope, this is GN, geometry nodes. Oh, come on, caps, GN. Let's go
[5:35] and set this to be green, this one to be orange, and this one to be blue. Actually, no, that one
[5:43] should be red. You know, spider-man colors and all that. So that's good. And since we have our
[5:51] object right there, let's go and get everything running. So we want our empty in here, set this
[5:56] to be relative, so that we get the orientation in such. Now we're going to rotate a vector.
[6:02] In this case, I'll be there and we want this on the x-axis. That'll be our velocity. So let's set
[6:07] up our simulation to make it so that we have points. We're going to make these edges, but for
[6:12] now, it'll just be points that go and spawn into a simulation and then attach to the walls when it's
[6:18] needed. So here, I will be using a join geometry node. Maybe initially, I'll go and set the initial
[6:27] velocity. So there we have that. So this to be a velocity. We'll do this, we will need this to be
[6:34] random eventually, but not quite yet. I'm going to set the ID because we want each of these points
[6:41] because we'll be adding in new particles every single time. We want every single point we add to
[6:46] have a unique ID. So we'll use a hash value, but this, I should mention, this isn't necessarily
[6:53] guaranteed to be a unique value because with hashes, there is a very, very, very, very, very
[7:00] low chance that they have the same ID, but so low that I'm going to treat it as if it'll never be
[7:08] the case. Let's go and use the scene time node, set this to be frame. So that part will be hashed.
[7:13] Actually, that should be float and that should be index. There we go. Because even though with the
[7:18] frames we're used to them being integers, they are technically floats because there could be
[7:22] subframes even though we don't really use them in this case. So that's that we have the velocity.
[7:28] And now I can put in a random value to rotate this velocity vector and all that. Let's go and scale
[7:35] this up. So that's more like 100 meters per second. And we'll do this. Great. So now we have particles
[7:41] spawning in. Where's our particles? Oh, we need to attach it to the output. There we go. So now we
[7:49] should see there are particles forming. And because I am a genius, I forgot to actually set the
[7:57] position. So now we have them spawn again, and they have the velocity that we want simple enough.
[8:02] Now let's go and make it so that these actually simulate. So I'm going to be using some node
[8:07] groups that I made previously like velocity step, and SDF collision, and SDF mesh, all these are
[8:15] available for free on my gummer page just because they're node groups that are very reliable. And I
[8:22] love them. So in this case, we have that and that we need to separate chill, we don't need to separate
[8:27] children. But it's probably a bit better realize instances. So we have all that. So now we have
[8:35] our velocity and the collision. So in this case, particles will fire from the center, hit the walls,
[8:40] and then fall. Right now they're bouncing, we do not want them to bounce will turn bouncing to zero
[8:46] friction to one. Now this still won't be perfectly accurate. And also I should mention, we want this
[8:55] to happen at the end, at the end, we want the new particles to be attached last, so that they don't
[9:04] move. They'll start at their their origin. And the next frame will go and do that.
[9:10] Thing is, we want the original one. Yeah, no, I think that is as expected. So here we can see
[9:16] they're there and then the next frame they're away a bit much. Let's turn it down to 10 meters per
[9:22] second. So we can see does that then it spins around. That's good. That's okay. Maybe I could add
[9:28] in some subframes into the spawning so that we don't get this very not this very regular result.
[9:37] But anyway, let's go and make it so that these parts stick. So with this, let's see, I don't want to
[9:45] have node groups for all this, but we may need to get to that stage because the simulation
[9:50] might be, you know, just a little bit complex. Let's make this Boolean and store the is hit value
[9:57] because this will tell these particles when to freeze once they hit the balls, I want them to
[10:02] freeze unless maybe we'll make it so that randomly they'll freeze. Okay, now this will be
[10:09] freeze so that they will not collide anymore, and they will not have a velocity step. And I forgot
[10:15] to connect the delta time. There we go. So named attribute if there is that was not supposed to
[10:24] occur. If there's not freeze, then that goes into there and also over to there. If it doesn't freeze,
[10:34] then continue doing what you're supposed to. Or actually, no, we want the freeze. Actually,
[10:41] yeah, that that should occur. Okay, so that is as expected. So now once they hit, they should, okay.
[10:51] And then here, this should only happen if there is not a freeze. So here, they attach, then they
[10:58] freeze good. That is as expected, that is working. So there we go. It just goes spins around and that
[11:05] happens. Okay, so now we need to make it so that not bad. Collision. And then that's the velocity
[11:16] step. There we go. So we have that part. So how do we make it so that these parts actually connect
[11:23] and still look good? That is the question. Let's add in a few more things. I want this to be maybe
[11:31] three points per there. Then here, I want to set the position to be offset randomly. So we scale this
[11:41] by a random value between one and 24. I could plug in the delta time into there, but that may be
[11:49] annoying. So I'm going to mainly put in the frame rate. And this is simply to make it so that it
[11:56] staggers the... Wait a minute. Oh no, I want to divide it by, yeah. Either be nothing or that. There
[12:09] we go. So here, if maybe incorrect with this, but we should see that they're now staggered.
[12:27] Should be, yeah, that divided by... Oh, wait a minute, wait a minute. No.
[12:34] I need to... Sorry, I'm forgetting what to do in this case. It should be one multiplied by that
[12:45] much and then scaled by the delta time. Yeah, one divided by 24. There we go. Okay, so there we go.
[12:54] That's what I was mostly looking for. Now, it's still interpolated, so that might be a little bit.
[13:01] We're not going to worry about that. Just a little bit of staggering. Okay, and this is new
[13:13] particles. So how do we make it so that these actually look webbed? How do we do it? Because
[13:20] there are multiple methods we can do. Initially, I was thinking, what if I just have a grid and
[13:25] delete random points and then instance that into there and then send them flying? That might work
[13:31] well. That might actually work well. I'm not sure. I am not sure. Let's give it a shot though. So for
[13:44] our web, maybe I'll have a new collection for web. There's multiple ways. If we want to go with a more
[13:50] art-directable approach, why? Yeah. Oh, that seems to be a bug. That should...
[13:59] Ah, there we go. Okay, I don't know why that was being weird. Web,
[14:02] ice, little experiment here. So here, let's add in a new geometry node thing right here.
[14:10] I may want to... let's hide everything else just so that we can focus. I'm going to make a
[14:17] hmm... a primitive grid. I'll set this to be 100 even though we will want to manipulate this later on.
[14:26] Maybe 25 on both. 50 on both. 15, 25. Yeah, that seems to be good. That's to be 0.5.
[14:36] And we're going to delete random vertices with this. So delete geometry,
[14:41] random value, and then we'll go and do...
[14:48] something like that. We just want some holes in there, and then we want to delete
[14:52] only faces. So now we just have this wire. And you may wonder, well, that doesn't look very organic.
[15:00] But if we use set position, and then we blur the position, blur attributes.
[15:07] Oh, and make sure that's a vector. We can see that this starts to look a bit more
[15:14] like our reference here, where it's like that. There are just a bunch of interconnected parts,
[15:20] and then all that happens. So potentially, I can make this work. That looks very regular,
[15:28] which maybe this was probably a really good idea. I need to go and triangulate.
[15:33] So that's...
[15:35] triangulate. This will be a fixed or fixed alternate.
[15:41] Then we'll go and do this, and then I'll automatically make it so that will be more
[15:45] like that. So we're seeing that this kind of web look, it's looking better,
[15:50] much more organic, but we can make it even better. By randomly...
[15:55] I actually, well, this even worked. Subdivide mesh.
[16:03] Yeah, how am I going to do this? Because I want to selectively subdivide
[16:08] certain parts, certain segments of this. I could separate geometry.
[16:18] Oh, wait, this might be a good idea.
[16:20] Let's see. So this we're going to make an int. This will just be the previous
[16:27] ID so that we can merge it. Darp index. That will be fine. Index. There we go.
[16:36] So we're going to separate the edges randomly based on a given value. Only subdivide those
[16:42] parts, join them back in, and then I could just merge my distance. That would have been simpler.
[16:48] Oh well. I could also recursively subdivide this. I could do it again and again,
[16:55] but let's use merge points and we will merge by their previous ID.
[17:03] I could just set their... I don't know, it's fine. But here we should see...
[17:09] Uh... what? Oh, that is... bad. What did I do wrong?
[17:22] What did I do wrong? Is that ID? Let's make that the index.
[17:29] That's... and did that... okay. Uh, oh.
[17:38] Uh... ID?
[17:45] Hmm. I mean that gives an organic shape, but not the organic shape.
[17:52] Okay, I'm just going to go and merge my distance because it seems to be a bit easier.
[17:57] There's probably something I did wrong, but I am working at speed and I do not want to slow down,
[18:03] so we have that part right there, that part for the quote-unquote subdivision quote-unquote,
[18:08] and that seems to work. I could have a repeat zone to do it again and again and again,
[18:16] but I'm not sure that's necessary. And I could subdivide it one more time.
[18:20] Hmm, I don't know, that's not looking as good as I was hoping.
[18:30] Yeah, no, what if I didn't know? Maybe I should do recursive subdivision instead.
[18:39] Or is triangle subdivision an option where I just go...
[18:43] That could work. Or I inset it, scale it to zero. Oh yeah, no, that could work as well.
[18:49] Let's go in extrude mesh, which in this case we need to do it before all the geometry gets completely obliterated.
[18:59] So something like this, and then I can use scale elements to just easily scale down the segments.
[19:04] This note is a bit weird nowadays, because it's like... yeah.
[19:10] Um, let's set that to be individual, yes, that'll work, and then merge by distance.
[19:18] So with that, we should see. We get a pattern like this, but we only want it to be on a subset of elements.
[19:24] So something like that, and then we can do it again and again and again and again to make it all work.
[19:30] Or we can do this and let's take a... oh, oh, oh.
[19:34] That does not look as good as I was hoping for, unfortunately.
[19:42] But there is something going on, so let's let it run its course.
[19:49] Hmm, can't say... okay. I think I'm getting a bit distracted in the web design.
[20:04] What I would need to do, like subdivide parts and then put stuff there, or... wait a minute.
[20:11] When this happens, I selectively delete certain edge segments. Maybe that could work.
[20:17] Hmm.
[20:23] That could work. I'm experimenting, and experimenting is fun.
[20:29] Uh, science, so it needs to be... or...
[20:34] and then it does that as well. Can't exactly dissolve, or this needs to be an and.
[20:43] Oh, I did not think of that, did I?
[20:47] That's not the edge domain, is it?
[20:51] It has to be in the side and random. Let's do that.
[20:57] Uh, we can't have... well, maybe loose edges could... okay, now we're getting lost in the weeds with all this.
[21:03] So, let's go back and, um, let's go back and actually run the thing and actually make connected stuff and all that.
[21:14] And we have this and it's running.
[21:18] What I want to happen?
[21:21] Maybe every time it fires, I instance in the web type,
[21:26] where the start will always be where the sky is, and then the ends will stick and everything in between won't stick.
[21:35] Let's give it a shot. Let's give it a shot. Let's see what happens.
[21:38] So, we have this and then we're going to...
[21:43] do I instance on points or should I just literally grab the thing into there and then transform?
[21:53] Transform geometry. We have our geometry. We transform it to have the that and that there. The scale I want to keep separate.
[22:02] We keep that random. We have that there. Make it very, very small.
[22:07] And I want to also store data on the start and end to see if that'll work.
[22:13] Let's go and plug that in and see what happens because I'm assuming
[22:18] something really...
[22:20] uh...
[22:22] Blame. That's why I meant to grab.
[22:25] So, here we can see that our webs are working perfectly. Look at that. They're spawning in. They're sticking to the poles.
[22:32] Perfection.
[22:34] But no, what I need to do is set some vertices on the start and end.
[22:40] Both be...
[22:43] basically...
[22:47] This side will stick to the end. The start will stick to the beginning.
[22:51] So, this will all come together fairly soon. I just need to make sure. So,
[22:57] let's go and store two named attributes. This will be end. This will be start.
[23:05] And I should reverse these, of course. Should these be bullions or floats? I think floats would be good.
[23:13] It's a bit more wiggle room in the end.
[23:17] So, that happens. So, I'm doing this before the blur. So, this will be separate x, y, z. I'm assuming, yes.
[23:25] x-axis. Let's go and set this to be less than. So, the start will be if it's less than this.
[23:29] So, let's go and take a little look with the viewer node, which we cannot see because of attribute text and all that.
[23:40] So, if it is greater...
[23:44] Oh, no, wait. I had that the right way originally.
[23:49] So, here what I want to be is like that.
[23:52] So, those parts, I just want to select a little bit.
[23:56] But, YouTube compression probably really hates that.
[24:01] We have the start and then we have the end.
[24:04] And I know this is being stored as that, but we may need to make it a bit softer for some of the stuff, but it should be fine.
[24:13] There we go. So, we have the start and the end. So, now let's go back into our simulation.
[24:19] And let's make it so that
[24:22] number one, let's go and move you back.
[24:26] Only the ends will freeze.
[24:29] So, we have the end and this has to be or... no, this needs to be an AND node.
[24:36] So, only if it hits AND it's an end will it freeze.
[24:42] So, with this we should see.
[24:44] There we go. We have a cascade, quite the cascade.
[24:49] And then at the start we need to make it so that the position will always be stuck to the start.
[24:55] So, let's go and do that.
[24:57] Set position.
[25:00] Start. Let's go and plug that into there. And then this will just set the position.
[25:05] Start position is. Now we're starting the node spaghetti already. Not good. Not good. Very bad.
[25:11] Let's go and remove that. So, here we should see.
[25:15] Oh, no.
[25:17] Ah, oh no. That did not function.
[25:22] Oh, no. Why did that not...
[25:28] Let's take a look. Oh, that hurts. That hurts so much.
[25:33] Okay, so apparently the start is incorrect. Let's take a look at here and see why.
[25:40] False false false false. Ah, then true. Now there are parts that are true.
[25:47] Was it just not enough?
[25:51] Let's go and take a look at this.
[25:55] Okay, now I guess it just wasn't enough.
[25:58] So, now that we have tons of webs firing, and to be honest it is way too much.
[26:03] That's way too much in terms of webs firing. But the ends are doing their job and everything else.
[26:10] I think I do need to make it so that I subtract.
[26:14] Because right now they're just firing forward, which leads to this ugly stuff. It's not spreading.
[26:20] So, I think I need to add in some random velocity or random orientation.
[26:25] So, let's go and rotate rotation.
[26:29] Right here. Make it low. I keep forgetting the difference between the local and global.
[26:36] Wow. Why did I have trouble saying that?
[26:39] Let's go and scale it. Scale it by .1. Change the seed values. Just do that.
[26:45] You never want it. Always add zero. So, here we can see that we get a very square looking.
[26:52] I am surprised by that. Wow. I'll edit that.
[26:56] But with that, we just need to do the last part with all this. Or a second to last part.
[27:03] Which is to add in the shrinkage.
[27:06] Rinkage.
[27:06] Rinkage.
[27:10] Seeing all those numbers shown in the viewer gave me a heart attack.
[27:13] Yeah. Yep. I should turn that off.
[27:17] So, here we have the dart pin. Yeah.
[27:24] So, we have that. And all we need to do is edit the velocity.
[27:29] So, that there is the attraction force. Just do it right there. That might be good.
[27:35] Actually, yeah. That might be good. Because I would need to edit the velocity anyway.
[27:39] So, I will go and take the position. Blur it. Subtract it. And call it a day.
[27:49] So, we just do that. And to add that into the forces. So, I need to scale this by
[27:57] to the power of two.
[28:04] Need to invert that. But here we should see at least actually divided by two.
[28:15] That's a bad idea. Bad idea. Bad idea. Bad idea. Or is it? It's not resisting gravity whatsoever.
[28:24] I am detecting at least some.
[28:32] No, I think I might need to do this the regular way.
[28:40] And I think I also need to up the scattering here. So, oh my gosh. I mean, something is occurring.
[28:50] It might not be great, but at least something is. So, it's like...
[28:57] Oh, that is indeed rough. So, I think I need to go and revise our webs a little bit.
[29:05] I think the main thing is I need to make it so that there are more attachment parts at the end.
[29:12] And then also delete more parts at the end. So, it's a bit more frayed.
[29:20] Okay, let's see if I can make this actually work. Oh, we don't need to subdivide the mesh like the
[29:25] elf. No, we probably will. But I'll do that after. Okay, so, step one. I need to go and delete
[29:36] geometry randomly based on Boolean value. And this will be based on the x-axis. So,
[29:43] I need to use a nice map range to go and map to the range of the deletion. So, it looks
[29:49] kind of like that, yes. So, we can see it's kind of looking a bit more web-like.
[30:04] Or maybe we just need more
[30:07] extrusions over there. I don't know. We may need to reshape that. And to be honest,
[30:16] maybe I could just, yeah, maybe I just need to delete more overall.
[30:21] That's more like, there we go. That's a lot more web-like. And then just add more loose ends.
[30:27] There. Oh, yeah, yeah, yeah, yeah, wait, wait, wait, wait, wait. So, let's go and extrude mesh.
[30:34] This will work. This will work. This will work. And then we also, yeah, yeah, we can make this
[30:39] contribute to the end. So, this will be a vertices offset will be random like this. Because what I
[30:46] want, excuse me.
[30:54] What I, random value? Oh, that's why. Yeah, no, it is happening, but it's getting blurred into oblivion.
[31:04] So, it's like that. We can't really see that. Maybe I need to do it like twice.
[31:10] But now we have little other attachment webs. And this will be
[31:16] or top. So, it'll be that or that will contribute. So, let's take a look at our simulation once again.
[31:26] We should see that some parts just kept. Oh, that is funny.
[31:32] Maybe I should use like a shortest edge path for that. Okay, another thing that I'm going to do,
[31:38] I'm going to change this because as we can see, we can't render our webs accurately. So, let's go and
[31:50] I need, sorry if you could hear background noise.
[31:58] Okay, let's go to curves. Let's do D here because to get a curves object, it assumes when you add it,
[32:06] it will always be attached to another object, which we do not wish for. I just want a blank curve
[32:12] object. So, that should be up there. You should be last. This makes it so that we
[32:18] could render the curves as strands. So, that is good. We have the curves there and we're going
[32:26] to transfer our geometry node set up to those curves just so that we can render the stuff.
[32:32] Let's go and get some geometry nodes because I didn't label it. This will be web sim 2.
[32:39] One. Web sim. There we go. It's good. Web sim. So, we have that and we just need to convert
[32:49] this to curves mesh to curves. So, now we can see we can now render all that. If we do go and render
[32:57] and make EV compile because this is a new version of Blender 5.3, but this can be done in any
[33:04] version of Blender and all that. We can't see because backface calling is not enabled with the
[33:12] shader. So, let us go and go into the shader editor and wait 15 billion years. It's not that bad.
[33:21] Backfacing and we will set the alpha if it is not backfacing using a 1 minus.
[33:29] Transparent shadows are on. So, now we can see inside. Yay.
[33:36] So, now we need to do other things like turn off temporal reprojection, turn on ray tracing,
[33:40] set this to be one of one denoising, turn off bilateral filter and then set this to be two
[33:46] meters. So, there we go. We have that. It goes around. So, now we, yeah, there's way too much
[33:52] stuff going on, but something is occurring. We're getting that kind of web tornado action
[33:57] totally. Let's go to Geometry nodes, the material, make a new material. I want this to be,
[34:04] I don't, it needs to be alpha blended even though I just like alpha, well, alpha blend has its
[34:09] purpose, but it makes it so that something, well, actually no, alpha blend is perfect for the scenario.
[34:15] So, let's change this to be blended. Now, we have this, it's good. We can set the opacity to be
[34:27] okay. Here we go. So, now we have something like this. Let's make it more metallic.
[34:33] Turn the roughness down. We will be adding textures, but this is just an initial thing to see what's
[34:38] going on. This looks like such a mess because it is. But this does kind of bring into question
[34:50] another thing. We need to update our little tension thing. I'm not using the XPBD solver
[34:57] just because, but some damping is in order. Okay. Kind of, we're getting a bit of the action that
[35:10] we want here. Let's go and make this a little easier to see because this is really, really hard to see.
[35:16] That copy it to, there we go. There we go. So, we have that and that and then that occurs.
[35:26] That happens. So, if we look at this, it's
[35:33] one second while I go and get a relevant HDRI.
[35:37] Let's go environment texture open. Let's get the environment textures. Which one would be good?
[35:46] Do we go with metro Nord is always good, but I'm thinking lead and hall markets.
[35:53] One. That is not, this looks terrible. Atrocious.
[36:02] I, yeah. Right now, it just looks like we're painting it with some sort of weird fur,
[36:14] which means that the force, yeah, the string force is not working.
[36:21] So, we have to redo it, which won't be bad.
[36:24] We're just blurring the position, which function is intended,
[36:32] even if it's at the end point. But we need to make it, if it is a frozen path out, won't do the blurring.
[36:39] So, we need to do the blurring after hit. So, let's go and do another set position.
[36:44] This will be make it a group. Do not need these inputs here.
[36:50] Besides, maybe, yeah, we need it so that it's not frozen to do this.
[36:58] So, we need to, I'm forgetting, I made it a node group because I feel like
[37:06] it needs to, I need to do something different. Oh, God.
[37:15] I think we have too many vertices flying.
[37:20] That is, that is funny. So, let's set it to be there. Let's go and turn up the velocity to be higher.
[37:36] What did I do?
[37:44] This is, this is really something, isn't it? Really something.
[37:51] Let's turn it down a bit more.
[37:55] Like that, it looks like I'm just casting something while here. It's too, what's the problem? What is,
[38:05] it's, what's its deal?
[38:10] Because these parts, it, hmm,
[38:14] I know I need to reset the velocity after, but something, it's just, it's all wrong.
[38:21] Do I need to just heavily reduce this so that there's only a few of the little things that happen?
[38:32] Not strong enough because it's not, oh, it's not, yeah, it's not affecting the velocity, of course.
[38:38] So, in this, we need to store the old position and then use that to affect the velocity. So,
[38:46] store the old position, do that, then we recalculate the velocity afterwards.
[38:51] I always hate when I need to do that.
[38:56] Or, since this is an offset, here, let's go and again, if you are not frozen,
[39:07] um, this will be velocity. I just need to compare. Yeah, no, okay, that'll work.
[39:16] Sure, attributes.
[39:20] Need to just subtract.
[39:25] And then I just increment the velocity based on that so that I don't need to do anything different.
[39:31] Hopefully, and then I can port in the delta time from there just to make it a bit better.
[39:37] Fail. No, I want you to divide that by that so that it actually affects it.
[39:47] That's that. I know this is an, uh, is annoying me a bit. How spaghetti-ified this is becoming,
[39:57] but hey, we are dealing with, what?
[39:59] What?
[40:02] If you are not frozen, then that affects the, oh, boy.
[40:11] Do that to that and then I contribute it to there. Yay, finally.
[40:16] Da-da-da-da-da.
[40:22] Cause, oh, there we go. Okay.
[40:26] It's, what is, let's make this like five.
[40:36] It's, it's just wrong. It's just wrong. Do I need to make it so that the damping goes up based on
[40:51] the, I don't, I am annoying myself
[40:58] to an extent. So this rotation we need to random, randomize. I want it to be constant.
[41:12] The ID is being randomized per frame, but this one I want to be one value for the whole thing. So
[41:19] go and we can collapse all these, put it into there. Let's see. Let's see.
[41:30] Okay. I think the problem is that it's discrete steps, but we are getting the web, the web style,
[41:36] the web action. So yeah, it doesn't feel like
[41:43] maybe the velocities need to be different. We only set the velocities at the ends and it
[41:51] drags the rest of the stuff forward. So let's go and get the end stuff there. I know this is
[41:59] getting spaghettified and I hate it, but it is what it is. And we may need to blur this. So let's go
[42:07] and blur without affecting the original part. So we do the one minus trick to the blur so that
[42:14] the gradient, for those of you who don't know, when we have this, can we, I forget, we can't see
[42:23] what's going on. You're just going to have to trust me on this. Well, let's use attribute text.
[42:29] So here, if we do this, set the way in all this, this means that the original part of the gradients
[42:37] the ones here will not change and it'll just spread out like that. Oh, wait a minute. Actually,
[42:45] no, that's fine. The original gradient won't change. It'll just spread without averaging the
[42:50] original. That's what I meant to say. So with that, we just blur it a bit for the velocity. So here, we
[42:58] can see it is not it's not doing great with the dragging. We can see that some parts because they
[43:08] apparently are disconnected get dragged. So that's be more like 10. I want it to be yeah, okay, we
[43:19] need to just a lot just and that's too slow. It's too fast. Welcome to the wonderful world of working
[43:30] with simulations. Okay, I think one of the things is that
[43:49] I think I need to add in the little bit of trickery that I used before, which was when it hits
[43:53] a value increments and spreads across the web, which causes it to collapse almost as if it was a
[43:59] chemical reaction, acting like okay, we hit now it causes a trigger and it shrinks to be honest,
[44:06] if Spider-Man actually existed, that would be needed for the swinging because you know,
[44:11] did to go up a lot without just climbing the rope. So I'll keep this in mind. I'm still not
[44:23] entirely happy with it. So and another thing, we need to make this bigger because this is
[44:31] very lackluster in its current state. Let's go and bring it up by let's see it was six meters. So we'll
[44:38] make this yeah, that tall will go and bring our empty, which I should bring it into there.
[44:46] We're gonna go and bring it up by 10 meters. So and then we're going to make this linear. So just
[44:55] that is a very slow descent. I know he's descending slowly in the original thing,
[45:00] but let's take a look. Okay, go in this jumps, he jumps down, he pulls himself down. So it's not
[45:08] only gravity. It's not even not even that fast. Doesn't even go that far. It's just like or we just
[45:17] need to make this part faster. Yeah, that seems to be enough. Just this part where it's pinned.
[45:28] Is it because the pinning
[45:32] isn't affecting the thing? Actually, I can. Yeah, I could also put the pinning in here, can't I?
[45:39] Um, yeah, just take the old position and the new position.
[45:45] Put them together all the day.
[45:50] Yeah, no, why was that even there? It just needs to be there and there.
[45:55] That and that take that out and there. So yeah, the pinning should happen in there so that it
[46:01] accurately and actually affects said velocity.
[46:07] Now that and that we have at the position, the subtraction and all that. So I just need to
[46:14] I just need to add in another one here. So let's despa, getify all this. Just another set position.
[46:23] And then we go and put the start thing into there. So
[46:27] a group input and then this one will just be
[46:32] position and then the start value will be that. So we get to eliminate some of the weird stuff in
[46:39] there. Just do all the position setting in one step and of course it does not work exactly as intended.
[46:46] That because the
[46:56] Do I need to set the velocity to be different as well? Should it just zero out?
[47:04] Actually, yeah, no, that should happen. If you're at the start, no velocity for you.
[47:10] And this should all happen afterwards anyway, so I'm going to bring this back.
[47:19] I should work on the shader so that it actually looks good. But I'm saving that for after
[47:30] start and everything there. What is going on?
[47:33] And what is causing it to cascade? Oh, I screwed up something here.
[47:44] Now that's being divided by that, but that's doing that. There we go.
[47:53] Yeah, screwed up a little bit, but we deal with that.
[47:56] And it's that I may need to rework this because it's not a constant stream,
[48:04] but it's okay. It's not great, but it's okay.
[48:10] So here if it's not frozen, then it does that. Yes,
[48:15] they need to up it even more. And I think I'd still want to subdivide the stuff a bit more. So that
[48:20] does that. Do we make it so that it's not discrete steps?
[48:27] And also, yeah, how would we actually make this look good? I have an idea
[48:34] because I just need to store on the actual web thing here on the setup. Let's go and make this
[48:40] actually somewhat organized. So we have that, we have that, we have that, we have that.
[48:45] Put that in there. I do need to name these, but it's fine. So with the set position,
[48:49] we're going to also store the rest position. So let's go and store a named attribute vector.
[48:58] This will be rest underscore position position. There we go. Position.
[49:12] There we go. So shader editor.
[49:14] Nope, wrong one. This will be attributes. Let's rerun the sim so that the stuff's actually in
[49:21] there. Let's go and save this. Rest position. So let's go and add in some noise. How do I make
[49:30] this in two dimensions is fine. I will also need to set a random value per web so that we can
[49:38] randomize it so that it doesn't look the same. Before the alpha, how do we make this look good?
[49:44] So map range. Let's go and take a look at this and see what needs to occur.
[49:51] So we have something like this. We set the detail to be 12 is all you need for 90,
[49:59] 5% of the effects that you ever make in your life.
[50:02] So something like that. So we have our little web highlights here.
[50:09] We can do that and lower it so that looks more like this. So that looks a bit web like.
[50:16] I still need to add in the tension by attachment age.
[50:23] So yeah, there's something like that. So do we just plug that into the alpha?
[50:32] We have something like this.
[50:36] Something low and then when that... Oh, I can feel... Okay, wait, wait, wait.
[50:40] Since we're in Eevee next, turn the shadows down as much as you can.
[50:48] Go. Still, it doesn't look good. Maybe it's because with curves, we need to change it to...
[50:56] Oh, there we go. Yeah, that explains a lot. What these curves, if they're strand, it's like
[51:04] they don't have any actual thickness or it can be cylinder. So that's why that's why. So
[51:12] strip and cylinder. Cylinder is the most accurate and all that. Of course, that's why I was looking
[51:20] wrong. These... I'm not gonna vary, even though I should vary the thickness a lot. Sure, I will.
[51:29] But we can see here at least on the... Oh, no, the alpha layers. Shadows.
[51:39] Order independent transparency would be nice.
[51:43] And I know I need to make it so that fires in both directions. I'm just
[51:49] waiting on that. And it still needs to be a constant stream, which it really doesn't do that at all.
[51:58] Do I need to take the velocity of the thing into account of our spinner? Probably 100%.
[52:09] Though I don't need to because I can just bake it.
[52:19] Of course, because the traction force is so... It just collapses before it gets to its destination.
[52:28] Maybe that's... It just needs to attach and then... Yeah.
[52:39] That's the problem, isn't it?
[52:43] The parts that should attach just never do a thing.
[52:48] So maybe I just need to severely reduce or completely ignore. So if it's not freeze,
[52:56] if it's freeze OR ends, then it will not do the shrinkage.
[53:06] We do that and that. Just simple logic and all that.
[53:14] Oh, god.
[53:19] I mean...
[53:25] It's a very finicky effect.
[53:29] I'm enjoying this. This is fun. Just need to reduce that. Oh my goodness.
[53:36] Just like that and then... Oh, maybe it... Wait, maybe I just need to fully reduce this part.
[53:42] Yeah, okay, there we go. So it casts and then... Okay, there we go.
[53:49] So now... Oh, wait, there we go. Look at that.
[53:56] Look at that. There we go. It's perfect. Not quite, but, you know, close to it.
[54:05] And it still doesn't look like a complete steady stream of webs.
[54:11] But...
[54:15] And it's still very, very discreet chunks.
[54:19] Because it doesn't... It's not one consistent stream. So maybe, maybe.
[54:35] Okay, and I also need to put in a switch to tell it when to stop spewing web.
[54:40] Bullion. Don't laugh at that. Don't laugh at that. Let's see.
[54:53] So we have that and then we turn it off, turn it back on, turn it off. There we go.
[54:59] So yeah, it's still very discreet chunks.
[55:05] Let's also go and turn up the roughness for the background. Oh god, why did...
[55:10] I was hitting all the wrong things, but yeah, there we go. So, with this, it's just...
[55:19] So...
[55:22] I think I'm going to turn this part off.
[55:27] Oh, do we make this not look...
[55:33] Yeah, now I need...
[55:34] I need...
[55:38] I need this stuff to affect it just a little bit.
[55:48] And I still need two of them, so I need to double the webs that are occurring, that are happening.
[55:53] I think occurring a lot because it sounds fancy.
[55:57] So I just need to duplicate you, join geometry, and rotate.
[56:08] Man.
[56:09] That, that, and that, and then this will be one, and that'll be 180. Right there.
[56:15] Absolute perfection.
[56:19] And it doesn't work.
[56:21] Idiot should be...
[56:22] Yeah, no, it should work.
[56:24] Oh wait, no, that's, that's why. Okay.
[56:27] So, the problem is that I'm just using the rotation as that when it should be the rest position, maybe modified by that.
[56:41] That's, that's the problem. I should take the rest position, rotate it, or no, no, no, no, no, no.
[56:48] No, no, no, no, no, no, no.
[56:49] No, no, no, no.
[56:50] I need to take the position subtracted by the location, and then that is our start velocity.
[56:58] So it's more consistent.
[57:01] Nice scale it.
[57:02] Should normalize it.
[57:07] And then we do that.
[57:08] So we have that and that.
[57:09] We'll set that to be five or ten.
[57:13] All of that.
[57:16] Okay.
[57:17] Okay, okay.
[57:18] I see it.
[57:18] I see it.
[57:21] So I could just go and transform this a little bit more.
[57:26] So we don't need, yeah, no, we don't need that either.
[57:28] We just need to plug this into there.
[57:35] It's still, yeah, it's still fairly discreet steps there.
[57:40] And we will go and still, oh wait, oh boy.
[57:44] Oh, let's set that to be, no, that's just an ad.
[57:48] There we go.
[57:50] We have this.
[57:53] Nice, nice, nice.
[57:55] Okay.
[57:55] So just look at that.
[57:57] Okay, okay, okay, okay, okay, okay.
[58:02] Now it looks so non-discreet that I think I need to slow down the empty spinning.
[58:10] I guess, whores beyond my comprehension.
[58:12] Oh yes, yes.
[58:14] Speaking of Spider-Man, brand new day.
[58:19] I am amazed that the movie turned out as well as it did.
[58:25] And we're getting, yes, there we go.
[58:27] Oh, look at that pattern.
[58:29] I'm not sure you can see it with YouTube compression.
[58:32] Look at that pattern.
[58:35] Okay.
[58:37] Oh wait, I need to fix the rest position because it does not start out there.
[58:50] Yeah, it was a good, I've been very burnt out on Marvel movies.
[58:57] And recent memory, wait, yeah, that's how it should be.
[59:06] But with that, I am shocked that they were able to make it as good as it was.
[59:14] Yeah.
[59:18] So let's take a look again and it's looking,
[59:23] still very,
[59:31] yeah, very much like that.
[59:32] We can always scale position on the Y.
[59:37] There, yeah, there we go.
[59:38] Yep, yep, yep.
[59:44] I think that works.
[59:46] Just need to make it perhaps a little bit more consistent.
[59:49] Am I still doing the jittering when the staggering?
[59:56] I am.
[60:00] Also scale that with the ends.
[60:09] And maybe I should randomize the rotations of the parts more.
[60:16] Spin them a bit more.
[60:18] This also, I need to go and rotate it on the X by 180 too.
[60:23] Let's go and take a look at this.
[60:27] I just don't want it to be completely the same.
[60:32] That ends, oh no, now it just looks mirrored.
[60:36] So we have that and that.
[60:38] I could always,
[60:39] hmm.
[60:47] It's fine.
[60:48] It's fine.
[60:50] It's fine.
[60:51] Completely fine.
[60:54] So now I just need to make some parts a little bit more consistent.
[60:58] Oh, I forgot.
[60:59] I need to store the random per web units.
[61:05] Yeah, yeah, yeah.
[61:10] All right, let's go and store that.
[61:17] I should go and make this its own node group, but oh well.
[61:22] So let's go and store named attribute.
[61:24] Let's make this an int.
[61:26] Let's make this a WID for web ID.
[61:30] Let's go and use scene time frame.
[61:33] Yeah, that'll be fine.
[61:35] I just need to use it to give a random value per thing.
[61:39] Yep, attributes.
[61:41] Do, do, do, do, add.
[61:46] And I do it.
[61:47] Yeah, I could just use this normally.
[61:48] Just need to make sure that it's not an even increment so that it doesn't, you know,
[61:53] cause up, yeah, any obvious repetition because it's an index.
[61:59] I'll go up by one.
[62:00] Because it's an index, I'll go up by one.
[62:01] So to avoid float point precision errors and what the frick.
[62:06] There we go.
[62:07] Okay.
[62:09] So few things.
[62:10] I think I need to set this to be the power of two to get a better fall off.
[62:14] So let's use a mix node to go and set the end points here.
[62:19] Let that be zero.
[62:20] Set this to be to the power of two or three or four.
[62:25] The cadence is probably sounding pretty annoying right now.
[62:29] I apologize.
[62:34] Good.
[62:34] Yeah, let's style this in a bit more because of roughness.
[62:40] It could turn that up.
[62:42] Cause yeah, that's more of what I'm going for.
[62:44] I need to turn up the specularity for those parts as well.
[62:49] So here I'm going to use this to turn up the specular IOR.
[62:56] So with this one, see, I'm going to crank it up.
[63:08] Is it because it's metallic?
[63:12] Yes.
[63:12] Yes, it was.
[63:14] And now I think we have a good glistening look.
[63:17] I'm going to turn off shadows because it's slowing things down.
[63:21] And we're going to wait for that to recompile.
[63:23] Oh, it's already done.
[63:24] Hmm.
[63:25] How about that?
[63:25] So now I can zoom in without, oh no, that still lags.
[63:32] Hmm.
[63:34] I can also set a random radius for all this
[63:39] based on the ID, which will probably make it look a little bit better.
[63:43] And maybe thin the webs a bit more.
[63:45] That may be, maybe good.
[63:50] Yep.
[63:54] Look at that.
[63:56] I'm pretty happy with this.
[63:58] It's still very messy.
[64:01] I think I need to go into, let me think here.
[64:07] The blurring happens there and there.
[64:10] I could make this a lot better if I set the weight to be that,
[64:15] just like how it is there.
[64:17] Does that help or hurt?
[64:20] With this, I think this needs to be not.
[64:27] There we go.
[64:27] Let's go and send that into there.
[64:30] Okay.
[64:31] So that should make the blurring more accurate.
[64:35] And now I could also dial it in.
[64:38] So I can mix between it being fully there.
[64:42] We don't need the not because since it's now a mix, it can do that.
[64:47] So I can set this to be 0.1 and it can do that.
[64:53] That still affects it a little bit, but of course that's way too little.
[64:59] I still need to make that happen if it's not frozen
[65:01] because I assume that these are being torn from the wall.
[65:04] Yep.
[65:05] Of course.
[65:06] So I still need that to make it so that they're not affected at all.
[65:15] If they are frozen, they're not frozen.
[65:19] They just do that.
[65:22] So there we go.
[65:23] That's looking more consistent.
[65:28] Maybe a bit too much.
[65:29] So let me go and lower it even more.
[65:32] Still want it to be somewhat...
[65:41] Let's see.
[65:42] Just dialing it in.
[65:44] It does look like webs, right?
[65:46] Pretty sure.
[65:49] Yeah.
[65:49] I may just need to...
[65:52] Since the scattering is no longer completely obliterating everything.
[65:56] And also that light bothers me.
[66:01] It should be a spotlight for aura purposes.
[66:05] Yes.
[66:06] Yes.
[66:10] There we go.
[66:11] Yeah, not bad.
[66:14] So just like...
[66:17] That works.
[66:20] Hard to tell with YouTube compression.
[66:21] Oh, I didn't even think of that.
[66:24] Yeah.
[66:25] Sorry, everyone, for making perhaps the worst...
[66:28] Oh, yeah.
[66:30] Potentially the worst thing on the planet for compression.
[66:37] Yep.
[66:43] We don't eat that one.
[66:45] So it's just...
[66:49] Yep.
[66:51] So now we have that kind of double helix look.
[66:54] Although webs are still going down.
[66:57] Just like in the movie.
[67:00] Good.
[67:01] I'd say that's pretty good.
[67:03] So one hour...
[67:05] Oh, one hour exactly.
[67:06] Well, not exactly.
[67:10] Let's see.
[67:12] Give me one moment, fellas.
[67:13] I'm getting...
[67:14] Fellows.
[67:15] Fellas.
[67:15] I should never say that again.
[67:18] One minute, everyone.
[67:20] I don't...
[67:20] That fellas sound so old.
[67:22] I need to take a call.
[67:23] Never mind, it was spam.
[67:27] Of course.
[67:34] My vernacular is very much in the, oh,
[67:36] somewhat fancy person range.
[67:42] Folks, that's the best thing about this.
[67:45] I think it's a little bit of a...
[67:47] I don't know, I don't know.
[67:48] I don't know.
[67:49] I don't know.
[67:49] I don't know.
[67:50] I don't know.
[67:51] I don't know.
[67:51] I don't know.
[67:52] Folks, that's way too far.
[67:55] Way too far.
[67:56] Okay, do I also blend the sides a bit?
[68:00] Yeah.
[68:01] Just a little bit of lighting.
[68:03] I should have brick on the sides.
[68:04] Do I have a nice and convenient brick texture lying around?
[68:11] And also, I'm going to keyframe the Webstop.
[68:15] This should be...
[68:16] Yeah, let's just make that group input for...
[68:22] Web on.
[68:25] Fire.
[68:25] Yeah, that'll be good.
[68:28] All right, there.
[68:29] I'll be like that.
[68:31] All right, and then...
[68:35] There we go.
[68:37] Webs on.
[68:39] Web stops, but even with the webs off,
[68:41] it'll still attach to the center so that
[68:44] if there was an animated character,
[68:46] it can go up just like in the movie,
[68:48] then off to the side.
[68:49] Yep, that is good.
[68:50] Shader editor, gonna go to the world.
[68:52] Going to use the is camera ray thing.
[68:57] Camera ray, there we go.
[68:59] I need to make it so that the sampling here is cubic.
[69:04] Just to make it better.
[69:06] And there we go.
[69:08] I'd say.
[69:10] I'd say that's pretty good.
[69:12] Maybe I need to make the webs thinner.
[69:13] Maybe I need to give them random radii.
[69:16] Actually, yeah, let's do that next random radii.
[69:19] That is on the post visuals.
[69:22] So right here.
[69:24] Set curve radius.
[69:26] Let's set this to be a random value.
[69:30] And the idea will make sure that's nice and...
[69:32] Oh my God!
[69:35] Yes, I do want my webs to look like clouds.
[69:38] That's exactly what I want.
[69:40] Is that enough?
[69:43] Oh wait, it's...
[69:45] Huh?
[69:47] Oh, it did the exact same values.
[69:53] Okay, so now I could just try to make my computer die
[69:58] by turning up the resolution.
[70:03] Okay, so now I can just try to make my computer die
[70:09] by turning up the resolution.
[70:15] Though it's not really adding much.
[70:21] Not really adding much.
[70:26] Yeah, we can't even see that difference there.
[70:30] Though, yeah, we'll keep you around.
[70:34] Because yeah, there we go.
[70:36] So we have the webs and then all that.
[70:42] There we go.
[70:43] So all I need is the brick texture,
[70:44] maybe a bit better lighting and that's ready to go.
[70:48] It does...
[70:49] It does look like a constant stream.
[70:56] Don't say to me you're not using next curve render.
[71:00] I am using the cylinder.
[71:04] So, oh, additional subdivision.
[71:07] I am a moron.
[71:08] I completely forgot that.
[71:10] Wait, no, that won't do anything here
[71:11] because these aren't the other splines.
[71:14] So setting the radius to be random won't do anything.
[71:20] But if you can't set the curve radius in the shader,
[71:25] that would be useful.
[71:35] Yeah, I think strip would be fastest,
[71:38] but it seems to be real time, so I'm not going to worry about it.
[71:40] Now, if you were going to use a curve to mesh,
[71:43] this would be the worst thing on the planet.
[71:46] But you don't want that.
[71:47] Webs are basically...
[71:49] I could add like little fun intertwined parts.
[71:55] There is a lot more I could put in there.
[71:58] Like right now, these are just horizontal like that.
[72:00] So I should invest in curve info.
[72:06] If we can access the UB map.
[72:10] Tangent norm.
[72:11] Hmm, not sure.
[72:12] I don't think we have access to the curve tube data.
[72:16] I think we're locked out of it, which would suck.
[72:23] Got the tangent normal, which we can see that changes.
[72:25] So no, I don't...
[72:27] Uh, texture coordinate.
[72:30] Let's see if we have that.
[72:32] Let's also save because I haven't done that in a while.
[72:34] But what a lovely cascade right there.
[72:38] UB map, nothing there, nothing there.
[72:40] Generated no, window normal.
[72:42] Yes, generated.
[72:45] Yeah, I don't think...
[72:49] Geometry, position, normal, tangent,
[72:56] and I'm still using the...
[72:57] No, no, all that should be fine.
[73:01] Uh, no, no, incoming parametric.
[73:11] Hmm, yeah.
[73:13] About what I expected.
[73:16] What is going on there?
[73:18] Oh, wait, no, that might just be because of the alpha?
[73:22] Yeah, no, we...
[73:25] I don't...
[73:26] This doesn't look like a cross gradient to me.
[73:30] So I think we just don't have access to that data.
[73:35] Cylinder type.
[73:38] Unfortunate.
[73:40] Don't think.
[73:41] Am I missing something?
[73:43] If it was going to be something, it would be parametric, right?
[73:47] A cylinder, that, no, those are both basically the same.
[73:53] Angents, normal.
[73:59] That's okay.
[74:00] That is alright.
[74:02] I'm only mildly annoyed by that.
[74:06] But I think unless you're zooming in this close, you will not see it.
[74:11] It could instance more things to make it higher quality, but...
[74:14] It's not like I'm working on a movie.
[74:16] That's...
[74:19] I am off work today.
[74:25] Doesn't need to be movie quality.
[74:30] So it looks like a constant stream even though it isn't.
[74:33] We got what we wanted.
[74:38] Eventually.
[74:41] So now we need to get to the next level.
[74:43] So now we need to add in more colliders.
[74:46] So I have a human here.
[74:49] So, oh wait, but now I need to make it so that
[74:54] the webs, when they're frozen, stay connected to the collider as it moves.
[75:00] That could be a cool thing.
[75:01] We're at one hour and 15 minutes.
[75:02] We can go for two hours today.
[75:04] I'm waiting on some stuff.
[75:08] So collider, if we include that, we can see that this poor soul
[75:13] will have some webs attached.
[75:18] Actually, since they are so sparse,
[75:22] can I make the webs even thinner?
[75:25] I think I should.
[75:27] Let's go and do a nice molt.
[75:29] Should have done this originally.
[75:31] Set that to be one and maybe point one and this one will be point zero zero one.
[75:43] There we go.
[75:50] So that does that.
[75:51] It makes it super, super thin, which I think is good.
[75:57] And then I can just turn the opacity up.
[76:03] Spaders and blender are real pain.
[76:06] It depends.
[76:07] It really, really depends.
[76:09] Turn up the specularity a ton.
[76:12] Even more that it's like, yeah, it's thin, but you can still, that might be too thin.
[76:20] I could still make it metallic, but I don't think that's a good idea.
[76:25] And that's, um, I can't say I'm a fan of that.
[76:31] So let's change this to closer to what it was.
[76:35] Let's set to point two five.
[76:38] Maybe I need to change the roughness.
[76:42] Make it look thicker.
[76:46] Brightness.
[76:46] No.
[76:49] Hmm.
[76:51] Hmm.
[76:53] Hmm.
[76:55] Hmm.
[76:59] That it's.
[77:01] Hmm.
[77:03] Hmm.
[77:11] Then get to point one.
[77:12] It's all looked at at this point, which takes up the most amount of time every single time.
[77:23] We're not getting the highlights there anymore.
[77:27] What should they even be highlights?
[77:30] I mean, I think the thickness for this is good.
[77:33] That that's acceptable web thickness.
[77:40] And there we go.
[77:45] Also, for the people who are here, I'm just wondering,
[77:49] I'm lightly considering restart or maybe doing another.
[77:54] Uh, I don't know.
[77:56] It's been a while since I've did a, like a discord version of this where I work
[78:03] and do all that.
[78:04] That's how I originally started, like a couple years ago.
[78:08] I'm feeling potentially a little nostalgic.
[78:10] So I'm, hmm, might be might be a good idea.
[78:13] I'm not sure.
[78:17] Other YouTube streams are more accessible.
[78:21] So I am very undecided.
[78:24] And I think
[78:34] Hmm.
[78:36] Zero five.
[78:39] Really want the web now.
[78:40] Now they're they're too dim, which I can solve with making them thicker.
[78:49] It's almost almost there.
[78:51] Then we can see on the last for all that that part's good.
[78:54] When you see when it ends, it's just bonk.
[78:59] And the thing is, I don't even need to make them static when at the end there.
[79:07] Here we go.
[79:08] Okay.
[79:09] I am happy with that.
[79:11] I am happy with that.
[79:20] And do I need to modify it?
[79:21] So if this has moving colliders, I, yeah,
[79:28] moving collider.
[79:28] So maybe I should go and sample the velocity
[79:34] so that it can all move around.
[79:36] But I don't know.
[79:42] And for the cherry on top, just to make it hilarious,
[79:47] let's go and parent the human to the empty and just do that.
[79:54] Not even posing the arms, just doing that so we can see.
[79:58] Yep.
[80:00] There there's Spider-Man.
[80:02] Bonking his head on the bottom of the world.
[80:06] And let's go.
[80:14] I forget I need to make this local.
[80:18] Yeah, there we go.
[80:20] X out of there new and let's just make him red like spoiled a man.
[80:26] Like oh yes, or man.
[80:28] Okay.
[80:28] When I was in the theater, as soon as the credits were through,
[80:32] I didn't stay for the end of the credit scene because I heard it was to do with
[80:36] Avengers Doomsday and I do not care about that movie.
[80:40] There was a kid who played the polyester man at it and I was disappointed but also
[80:51] happy because I was like, you know what, that's a perfect thing to end the movie on.
[80:55] Polyester man.
[80:57] It was so good.
[80:58] It was it was so cringe but so beautiful at the same time.
[81:07] All right, let me go and yank some textures.
[81:10] I think a nice brick texture would look good.
[81:14] EBR.
[81:15] Oh wait, let me let me go and full screen this again.
[81:18] Hmm.
[81:20] Hmm.
[81:20] Hmm.
[81:21] Hmm.
[81:21] Hmm.
[81:21] Floors cracked asphalt.
[81:24] No, I used that one's too classic.
[81:30] Road lanes.
[81:31] No, city grounds.
[81:32] No, I don't think it's good.
[81:34] Road lanes.
[81:35] No city grounds.
[81:36] No, stones.
[81:39] Brushed to concrete.
[81:41] Oh, maybe that'll look good.
[81:43] And the displacement map.
[81:47] So let's attach you to here.
[81:48] Oh, oh god.
[81:50] I will hew HSV it.
[81:53] Tri-plana.
[81:56] Tri-plana UVs.
[81:58] Plug that into there.
[82:00] Put that into there.
[82:02] Put that into a nice bump map heights.
[82:05] Put that into there.
[82:07] Do an HSV node.
[82:10] You just make it so that's, that looks bad.
[82:14] Atrocious.
[82:15] Absolutely terrible.
[82:17] Hate it with my entire being.
[82:20] There we go.
[82:21] Let's set that to be 0.1.
[82:23] Better.
[82:23] Not great.
[82:27] Maybe I just need the bump map.
[82:30] You know, just a little thing right there.
[82:34] Let's set it to be 0.01.
[82:37] And set that to be 1.
[82:41] Wow.
[82:42] Oh, no way.
[82:44] Set it to be non-colored data.
[82:47] Oh, I love that new menu.
[82:50] That was probably in the older version, but it's fine.
[82:55] That's good.
[82:57] Oh, great.
[82:59] That's good.
[83:01] Oh, that looks a lot better.
[83:02] Yep.
[83:04] Maybe turn the hue by a little bit.
[83:06] Yeah, there we go.
[83:07] Oh, yeah, no, that looks good.
[83:10] That is acceptable.
[83:15] All right, let's go and get the camera ready for placement.
[83:17] And I'll call this project this one and a half hour project.
[83:21] Pretty much done.
[83:24] So we can have, yeah, no, no, no, no.
[83:27] Yo, let's go and...
[83:28] Move it up so we can see.
[83:36] Now I just need to put more humans in the mix.
[83:47] And that will be perfect.
[83:50] Just a few more.
[83:52] Just like, oh, yay.
[83:54] Oh, no.
[83:55] I think the humans might detract from the effect.
[84:05] Yeah.
[84:08] Come on.
[84:10] There we go.
[84:11] Okay, so for the backgrounds, Shader World.
[84:16] Oh, yeah, I think that's fine.
[84:18] I will try out some different things.
[84:24] I need to get the entire tube in here.
[84:28] And then maybe, oh, maybe I could also do that to get like a POV shot.
[84:33] Oh, that could look cool.
[84:36] Cause, yeah, the...
[84:43] That's not bad either.
[84:45] I think I like that a bit more.
[84:50] Maybe, yeah, maybe more like that.
[84:54] And maybe I could go and duplicate this, make it a bit smaller,
[84:59] turn up the blend a lot, and then turn up the light a lot.
[85:04] I really want that.
[85:05] Yeah, there we go.
[85:12] Yo, Spider-Man.
[85:15] Yay.
[85:16] Oh, yeah, the Spider-Man movie.
[85:18] I...
[85:19] It felt very New York.
[85:21] Very New York to me.
[85:22] Like, there were so many times during the movie where I was like,
[85:25] oh, yeah, no, I've been there.
[85:26] Yep.
[85:28] It just, it just felt like New York.
[85:30] It was very nice.
[85:31] And the end credits just being shots of New York.
[85:34] Very, very nice.
[85:35] Very nice.
[85:45] It's still so funny.
[85:49] I don't think...
[85:50] Could I make...
[85:51] Okay, let me...
[85:54] Spider-Man do a flip?
[85:55] Okay.
[85:56] There, well, you got two of them there.
[86:00] Let's see.
[86:02] Let's go with a damped track,
[86:04] because that's better than the original track,
[86:06] because it doesn't make me go absolutely insane.
[86:10] Let's go and set it to be negative Z.
[86:15] Let's do that.
[86:16] That's good.
[86:17] And then there.
[86:18] Okay.
[86:18] So do I move...
[86:19] I think the static camera is probably better.
[86:24] Then we need to make it a bit less effective.
[86:30] I can be more like that, yeah.
[86:34] And then, yeah, probably just making the animation a bit better.
[86:40] But I'd say that's acceptable.
[86:42] It's still not great.
[86:45] But it's not terrible.
[86:47] For version one, that is good.
[86:55] I should move the arms up though,
[86:57] because that...
[86:58] It adds to the humor.
[87:00] It adds to the humor.
[87:04] That's good.
[87:05] Let's go to the empty...
[87:09] Zero out both of those, move it up.
[87:12] Zero out both of those, move it up.
[87:14] Over to the side.
[87:17] Now it should be on that side.
[87:18] Yeah, there we go.
[87:20] So just like that.
[87:22] Then...
[87:28] Then maybe like this.
[87:30] That looks absolutely awful.
[87:36] That looks so bad.
[87:37] Oh, I haven't even thought about motion blur.
[87:43] That has a consistent ID.
[87:44] Motion blur may work.
[87:48] Yeah.
[87:49] And maybe I should lock off...
[87:52] Oh yeah, maybe I should just um...
[87:57] Fuck that parents.
[88:00] And then do a...
[88:02] A child of constraints.
[88:04] Copy...
[88:06] Copy location constraint.
[88:08] Let's make this the empty.
[88:11] There and then...
[88:14] Offset original.
[88:15] Yeah, that'll be good.
[88:21] That looks so bad, but it's so funny.
[88:24] Whee!
[88:30] There we go.
[88:30] It's not bad.
[88:31] It's not bad.
[88:33] It's a nice...
[88:35] I'd say it's a decent version of the effect,
[88:37] even though it needs more randomization.
[88:39] I need to just make it so that there are more versions of the web that gets ejected
[88:48] and all that.
[88:50] But you know what?
[88:52] For an hour and a half, that is not bad at all.
[89:02] The way it just donks at the bottom.
[89:04] It's perfect.
[89:05] It's perfect.
[89:08] It's just perfect.
[89:12] Yeah.
[89:15] I am happy with this effect.
[89:19] All right, um...
[89:22] New particles.
[89:22] We have the collision.
[89:25] And this needs to be the web...
[89:28] Attention...
[89:31] How do you spell tension again?
[89:32] I think it's like that.
[89:34] L-web.
[89:37] Yo, so there's that.
[89:38] There's the delta time, which I...
[89:42] I don't have time to...
[89:46] I don't have time to develop for Blender nowadays.
[89:50] Time nor motivation, unfortunately,
[89:53] due to other things that are taking up time.
[89:55] If I had time, I would look into making the portal reroutes,
[90:00] because I need that.
[90:02] I need that.
[90:04] I also need to look into that name dependency,
[90:06] but unfortunately, again, time.
[90:08] There's not enough...
[90:09] I have too much and too little time at the same time.
[90:12] Does that make sense?
[90:14] Does that make sense?
[90:16] Yeah, it probably makes sense.
[90:17] Okay, so let's do...
[90:18] This is visual.
[90:20] And let's go over to our web.
[90:23] Figments.
[90:26] Let's go and do more.
[90:28] So this will be...
[90:32] Enchant...
[90:36] This will be...
[90:42] Data.
[90:44] In data.
[90:45] Yeah, in...
[90:47] In data.
[90:47] This one will be...
[90:50] Raise.
[90:52] And then this part will be...
[90:55] Subdivide...
[91:01] Selective.
[91:02] Subdivide.
[91:04] Random.
[91:06] This one will be...
[91:11] Red.
[91:13] Very creative naming on my part,
[91:15] but it's okay.
[91:18] Just the rest position.
[91:19] So yeah, that is decent.
[91:21] Why is it lagging?
[91:27] Oh yeah, now it is firing so many webs,
[91:30] so yeah, no, it'll lag.
[91:33] Um, yeah, no, that's good.
[91:42] I...
[91:42] The background there.
[91:44] Can't say I'm all too happy with that.
[91:48] Maybe it just needs a nice noise texture to boost it.
[91:52] Make it look a little bit better.
[91:53] So 2D, we're just going to go and
[91:56] straight up mix between the two.
[91:58] Float, mix.
[92:01] Do that, set this to be 12,
[92:03] set that to be there.
[92:04] And shadows are still to say,
[92:06] well, no, shadows weren't the problem,
[92:07] so I can turn those back on.
[92:09] That wasn't what was causing it to lag.
[92:11] Ooh, but we get some nice shadows.
[92:13] Ooh, yeah, no, it turns out adding shadows
[92:15] makes it look better.
[92:19] Okay, so what we need is you,
[92:21] a mix between you and you.
[92:23] I think something like that could be good.
[92:24] Maybe just reduce it a bit.
[92:31] Yeah, that seems to be decent.
[92:38] Just making it a bit rougher.
[92:42] A bit too much.
[92:46] It's decent.
[92:48] Oh, the roughness, that.
[92:51] That is what is tripping me up.
[92:55] The even roughness, of course.
[92:58] Another noise texture,
[92:59] just to make it look a bit more splotchy.
[93:02] One, let's go and hone it in,
[93:04] more like this, more like that.
[93:05] Do that, I think .6 would be good for the range there.
[93:11] Yeah.
[93:13] Yeah.
[93:16] Something like that.
[93:18] Take a look at this.
[93:25] It looks bad.
[93:28] Turn that by a little bit.
[93:36] Color management, do we need to aces this?
[93:42] Potentially.
[93:46] Aces usually looks better in some scenarios.
[93:51] And then top lights.
[93:55] Boost that.
[93:58] Oh, it's facing us.
[93:59] That's why it doesn't look great.
[94:02] Never have, well, now back lights exist.
[94:05] In this case, lights are not preferable.
[94:13] Maybe I should have them like side lights on all the sides and everything.
[94:33] This is 2.0.
[94:36] Yeah, they're about the same size stick with 1.3.
[94:42] It's okay.
[94:44] It's okay.
[94:51] Maybe it's just this texture that isn't,
[94:53] I'll go and play with that another time.
[94:57] You know, I'm not vibing with that concrete texture.
[95:03] Almost stone arches, no, I don't need that.
[95:06] That's all.
[95:08] Scliffside, damage plaster, facades, image plaster, that could be a good one.
[95:16] Oh, wait, you have no, that'll work out very nicely.
[95:23] Then for that one, you need to go over to damage plaster and then do that.
[95:31] Hey, that might work well.
[95:35] Maybe, possibly.
[95:41] Still, oh wait, actually, yeah, no, I like that.
[95:45] I like that.
[95:53] Up in with the, yep, nope, that works.
[95:57] And I think I should cube projection this and then just use the UV map.
[96:04] The less you rely, yeah, industry standard, well,
[96:08] kind of industry standard, just use the regular old UV maps to do UV map stuff.
[96:14] So UV editing, let's go and scale it up by 20.
[96:21] To do as little as possible.
[96:26] Yeah, no, that's all right.
[96:27] Just the lighting's still a bit messed up.
[96:39] Looking good.
[96:41] That could be better.
[96:42] Jesus.
[96:46] Nope.
[96:48] No, no, no, no, let's see.
[96:50] Nitro, no, um.
[96:51] No, I think that one has the vibe.
[96:59] Maybe I just need to change.
[97:05] Or what if it was completely dark?
[97:07] No, that's terrible.
[97:08] I hate it.
[97:11] Yeah, just the lighting.
[97:16] I'm usually known for good lighting, so I need to.
[97:22] Heep it's, I need to make it, no.
[97:27] I'll do that when I need to waste more time.
[97:37] That's maybe .5, then mixing more noise into it.
[97:41] Noise, I, hmm.
[97:52] I think it is acceptable.
[97:58] Uh, as long like they have consistent ideas, so there shouldn't be any weird motion blur
[98:04] stuff that causes it to, of destruct.
[98:07] Let's go and set this to be a video.
[98:12] Coding.
[98:16] Yo, that is as expected.
[98:18] See, I think that's good.
[98:26] Maybe I just, let me try out some more lighting here.
[98:32] So maybe I just need to do something along these lines where it is like.
[98:38] Oh, compositing.
[98:49] Of course, I completely forgot.
[98:53] I need the balloon.
[98:59] Always.
[99:00] Well, that adds basically, it added basically nothing.
[99:08] But we can go and, I don't know.
[99:12] That's too much.
[99:13] That's like that.
[99:16] That could work.
[99:22] And then let's not forget you.
[99:26] And let's not forget you.
[99:29] Oh no.
[99:32] Uh, shift L, object data.
[99:34] There we go.
[99:38] I would, I'm not going to question that.
[99:43] Where is that?
[99:47] Hmm.
[99:49] Hello to everyone in the chat.
[99:51] We're wrapping up today's stream just adding in a bit of.
[99:59] Lighting that I am still on very unsure about.
[100:04] Oh, actually that, not the worst.
[100:10] Oh, that's supposed to be like a skylight.
[100:12] Yeah, I forgot.
[100:15] Just like that.
[100:16] And then it's just, I'll bet you can't, you can't see anything like that.
[100:24] Hmm.
[100:24] That's not bad.
[100:27] Changing the colors here might also contribute.
[100:34] There I go again with, oh, I need to do everything in camera instead of doing a molecule of color
[100:39] correction.
[100:41] Because as we know, color correction is fake.
[100:45] Not a real, it's not real.
[100:51] Hmm.
[100:55] No, but we can't, it's not highlighting the webs when it happens.
[100:58] So.
[101:01] That's easy to zero.
[101:02] That makes it so that we can, the purpose is to see the webs.
[101:05] Maybe I can fire it up from the bottom.
[101:09] So let's copy use that used to be that.
[101:11] R X1 80.
[101:15] Turn it up by quite a bit.
[101:18] Oh.
[101:22] Wait a minute, what, what if that actually worked?
[101:27] Then we just narrow into, wait a minute.
[101:32] 180.
[101:35] Oh.
[101:45] Not against that.
[101:51] Just the top roof.
[101:52] I'm, can't say I'm the biggest fan of there.
[101:55] Okay, then curves, RGB curves.
[102:05] Turn the red down so that we get a nice teal.
[102:10] I don't know, I need a workshop this.
[102:13] Workshop this, oh my gosh.
[102:16] Jader editor, the background.
[102:26] Now I'm, I'm no longer loving.
[102:31] Oh, wait, no, I like it better when it's.
[102:35] Modgenus.
[102:40] And I could turn up the shadows if I'm wanting to black my computer.
[102:46] Samples, oh, there's no a seconds limit for Eevee.
[102:50] And did that get put in there?
[102:51] Just dun dun dun dun.
[103:08] Now I feel like that's better.
[103:10] Uh, let's go and bring, even make you a little bit wider.
[103:17] Times the ball, that's.
[103:19] No, we also need to move you over to the side a little so that when it goes down,
[103:26] you don't completely occlude everything.
[103:31] Yeah, it's, it's the top roof.
[103:34] I'm gonna void it.
[103:37] Voiding the roof.
[103:40] New material.
[103:42] It's a missive.
[103:44] The emission, if it's bright, like a skylight.
[103:48] That's not good.
[103:50] If it's the void.
[103:54] That's also bad.
[103:59] Oh, that's, I don't know why I'm just, I need to work on, I need to work on that separately
[104:08] off stream because I think I'm trying to make it perfect.
[104:12] And as we know, perfection is always attainable.
[104:19] And I will attain it.
[104:36] Hmm.
[104:43] I still love it just face planting on the floor.
[104:48] So good.
[104:51] So good.
[104:52] All right.
[104:54] Oh, we're at one hour and 45 minutes.
[104:56] I think that's good.
[104:58] Still not happy with the walls.
[105:01] Them being solid feels better than them with texture.
[105:09] Them being solid feels better.
[105:11] Maybe it's just like just a little, just a little bit of texture.
[105:16] Yeah, that just a little bit of detail.
[105:18] I think that's good.
[105:20] Then I could just make things a little, is it the red?
[105:23] Just something, is it the lighting?
[105:25] Is it the red?
[105:26] Something is just off.
[105:30] Completely black it out.
[105:33] Just have a little bit of gray.
[105:40] Okay, maybe, maybe it was that that was causing some of the weird stuff.
[105:44] Also, I need to make sure that, you know, it's not just my monitor making things look more gray.
[105:54] Maybe it is doing that.
[105:56] Object.
[105:58] That down.
[106:01] Turn it up.
[106:10] Let's see.
[106:12] We have that.
[106:13] Hmm.
[106:14] All right, now we're, we have a good result.
[106:17] It looks somewhat similar to, you know, what we have.
[106:23] Well, you only see it for a little bit.
[106:26] It looks somewhat similar to that, though the kind of secondary webs that seem to fire,
[106:31] like those fire and then there's the secondary ones that fire from the beings.
[106:37] I think, actually, let's take a look at that guy.
[106:40] What happens?
[106:44] Well, that's, it spawns in with that and then with that guy.
[106:47] Like, oh no, it,
[106:51] that was kind of hit there.
[106:55] I'll need to, yeah, maybe there will be a version two of this.
[106:59] We can see here there's not even like major highlights on the webs there.
[107:04] Looks rather static.
[107:07] The shape.
[107:08] Oh no, are those, those might be the webs from the previous hit that those might not be the spinning.
[107:16] Nope, those are the spinning webs.
[107:20] Yeah, actually look at the shape there.
[107:25] I mean, they're they organic webs, which probably explains why they look a lot more messy and wavy
[107:30] than the other ones.
[107:32] So yeah, maybe.
[107:33] Maybe, but there is so much varying thickness.
[107:40] Oh yeah, and there's some highlights in there.
[107:42] So yeah, varying thickness.
[107:45] That is, that's a difference.
[107:47] That's the big, big difference.
[107:52] Yeah, yeah, yeah.
[107:53] Okay.
[107:55] Just need to change that up a bit.
[107:56] I'm still not happy with that.
[107:57] That background is annoying me for some reason.
[108:00] The lighting, the lighting is just wrong.
[108:08] Is it because I were to delete all that?
[108:13] Don't know.
[108:19] Hmm.
[108:20] And actually, I've been missing the reference all this time as well.
[108:32] But yeah, there's the skylight, which I kind of remembered.
[108:36] And then there's that.
[108:40] So maybe I just need to make it like a pseudo prison with like bars on the sides and then that goes back.
[108:46] More if I did.
[108:47] Yeah, no, the shape's okay.
[108:49] It's also funny that they spoiled this, but it is a very hype moment,
[108:53] but it is the climax of the film, the climax of the climactic fights.
[108:59] Or yeah, and it's just like, well, here it is in the trailer.
[109:04] Here it is in the trailer.
[109:07] Is it the red of this guy that's bothering me?
[109:14] Does it need to be like a little metallic?
[109:19] Give it a little bit of a sheen.
[109:21] Oh yeah, yeah, yeah.
[109:23] That helps.
[109:26] Make it look just a little bit more like the Spider-Man.
[109:39] Fun.
[109:39] All right.
[109:40] Thank you all for watching.
[109:41] I hope you all enjoyed this little look into just making a little
[109:47] I was just making a little little effect.
[109:51] I think it turned out well.
[109:53] I still have a few little issues with it that I can fix up.
[109:58] It's just the lighting.
[109:59] What is up with the lighting?
[110:04] Yeah, I remember you doing a shockwave effect.
[110:07] And I was wondering if you were willing to create the gene
[110:11] psychic field effect, psionic field effect.
[110:14] Let's see.
[110:19] Yeah, I forget if I ever made a shockwave effect.
[110:23] I probably did.
[110:24] And yes, I know I should put the hands there.
[110:27] Actually wait, is it firing in the wrong?
[110:30] No, it's firing in the right direction.
[110:32] I find it funny or if he's just eight posing and then hits the ground like that.
[110:36] Because that's funny.
[110:41] That's funny.
[110:43] Uh, but to be honest, that effect, it's not difficult.
[110:48] It was interesting how it was affecting the water and stuff like that.
[110:51] That was an interesting thing.
[110:53] But it's just a little bit of compositing with RGB and all that.
[111:00] So I to be honest, it's just it wasn't it wasn't that complex.
[111:07] So I think you just need to add in like a lens distortion node.
[111:13] And then just have noise with the scene.
[111:15] Yeah, I could hear because I don't know when to stop streaming.
[111:20] If I'm remembering it correctly, I know that they did not knocking the effect whatsoever because,
[111:25] you know,
[111:30] uh, I forget if it was it was a bit like side to side as well, if I'm correct.
[111:36] But yeah, it's just stuff like that, even though a bit more complex,
[111:40] but for most people who need to do it,
[111:45] it is not.
[111:49] It's not the most complex thing to do.
[111:52] Sorry, I'm getting distracted.
[111:56] So yeah, something like that make that fit.
[111:59] Maybe it should be more.
[112:02] Yeah, you should probably like you use UV displacement to for the RGBs and maybe even more in between
[112:10] to make that work.
[112:12] Yeah, little thing, not the most complex effect.
[112:15] Even when it's on the sphere, it's still doing very similar stuff.
[112:19] I would imagine they didn't even have like a dispersion shader.
[112:22] I imagine it was just a sphere with noise and then they used that to do to
[112:28] guide the compositing.
[112:31] That's why I'd imagine.
[112:34] Around here,
[112:37] let's turn it down.
[112:39] I really fiddle with just the little little things here when I really don't need to.
[112:45] All right, thank you for watching.
[112:47] I'll see you next time.
[112:48] Have a good one.



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
