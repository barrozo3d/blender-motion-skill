---
title: How to Blend Separate Objects in Blender. Easy Method!
source: YouTube
url: https://www.youtube.com/watch?v=KGf58mE5fZI
author: Kenan Proffitt
ingested: 2026-07-26
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-blend-separate-objects-in-blender-easy-method/
frame_count: 0
frame_status: pending-selection
---

# How to Blend Separate Objects in Blender. Easy Method!

**Source:** [YouTube](https://www.youtube.com/watch?v=KGf58mE5fZI)
**Author:** Kenan Proffitt
**Duration:** 14m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-to-blend-separate-objects-in-blender-easy-method <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this video, we're going to take a look at blending two separate objects, materials
[0:03] and all, without using any booleans, just a simple geometry node setup.
[0:08] So let's jump into Blender and check it out.
[0:12] So here's my setup inside of Blender.
[0:14] It's just a simple rock pillar and ground.
[0:17] And I have two very simple materials on them that I got from Texture Haven.
[0:23] We'll revisit the materials here in a minute.
[0:25] The first thing's first is let's set up the geometry nodes setup to blend these two objects
[0:30] together and then we'll blend the materials together.
[0:34] So let's go into geometry nodes.
[0:37] And this is the object, this pillar rock thing that we have here.
[0:41] This is the object that we're going to use to create the node network.
[0:44] So with that selected, just create a new GeoNodes network.
[0:47] And of course, you can use any object that you want to blend with something else.
[0:53] And what we're going to do is first of all add in a proximity, a geometry proximity node.
[0:58] And just drop that down here.
[1:01] And then we want to take the proximity of the ground to the object.
[1:06] So to do that, we can actually just grab the ground from our outliner there and drag it
[1:10] in as its own node.
[1:11] And make sure you change it to relative instead of original.
[1:15] And take the output of that into the geometry of that geometry proximity.
[1:19] And so now we can click our geometry and shift click that node, control shift click
[1:25] that node.
[1:26] We can see the proximity of our first object to the other there.
[1:30] And that's exactly what we want to transform the geometry or displace it.
[1:35] So we can use a very fancy displace geometry node on top of our little node network here.
[1:42] So this is just information from the ground in relation to this object.
[1:48] And then sort of this line up here is like what we're actually doing to the pillar.
[1:52] So we're displacing it right now.
[1:53] You can see it looks really exciting.
[1:56] All right.
[1:59] Thanks for watching everyone.
[2:00] Okay, so let's take the distance output here and put that into the offset distance of our
[2:07] displace geometry.
[2:09] And now it looks really great.
[2:11] But if we take this strength way down to like 0.1, something reasonable, then you can see
[2:17] we're actually displacing something that looks like intentional.
[2:22] But we want to have greater control over this.
[2:25] So let's drop in a map range node right after this distance output there.
[2:31] Now we're adjusting like the range from the actual ground up to the object.
[2:35] If I control shift click our geometry and then control shift click this, you can see
[2:40] how we're adjusting that gradient.
[2:43] So now we have a gradient, which is sweet.
[2:46] Now let's take the output of that into the offset distance, delete that viewer node.
[2:51] And now if we crank up the strength, you can see that the top part of our rock is displacing
[2:56] in where it meets the ground.
[2:58] It's not.
[2:59] And we actually want to reverse that.
[3:00] You can reverse it in the map range node.
[3:02] But what I like to do is add a color ramp node, which is similar to what the map range is
[3:07] doing, but it gives us a little more flexibility.
[3:10] So I like to reverse these.
[3:12] And now we can sort of visualize that deformation there a little bit better.
[3:17] And you can sort of carve out a shape that you want as well.
[3:21] Now it's worth noting that we're not actually doing any sort of Boolean operation or any
[3:26] actual merging of the points.
[3:29] This is all just a hack, just a trick.
[3:32] So you could move on to just the blending of the materials, but I found that whenever
[3:37] you do a little bit of displacement on the object, you get a much more realistic result.
[3:43] Now another thing you can do is displace the ground.
[3:46] It does require joining the two objects together at the end of this, which there would be some
[3:51] cases where you don't want to do that.
[3:54] But the effect I think is worth it once you do choose to displace the ground.
[3:58] By the way, this is dynamic.
[4:00] It displaces based on proximity.
[4:02] So wherever you move this rock, that's where you're going to get that little bit of displacement
[4:06] right near the base where it hits the ground.
[4:09] If I crank this up, you could see the effect more.
[4:12] So you see you can get, you know, you can do some cool effects with things like that.
[4:19] Okay, so we just want a little bit of displacement right near the edge.
[4:23] Maybe kind of carve it up like that.
[4:26] Let's go ahead and do the exact reverse of that only on the ground.
[4:29] And like I said, this is the part that's optional.
[4:31] You might not want to do this because you'll have to join them together.
[4:35] But let's just go ahead and do it.
[4:37] So let's take our ground geometry output.
[4:40] We already have it in the scene and we're just going to do the exact same thing.
[4:43] Feed that into a displaced geometry.
[4:45] But we're going to displace it based on the proximity of the rock.
[4:49] So let's take all of these nodes here and we can just shift D, duplicate them.
[4:55] And we'll take the geometry input into the actual geometry proximity and just feed it
[5:01] in like that.
[5:02] And let's take this color output into the offset distance and we'll view that.
[5:10] Now you can see we have a little, the exact reverse of what we did there, a little blip
[5:15] up on the ground.
[5:16] So there's without it and there's with it.
[5:19] And now this is the part that in some cases breaks a procedural aspect of a geo node setup
[5:24] because it joins these two together.
[5:26] And I mean, everything stays procedural, but it makes it so that there's a few more
[5:32] steps to do if you wanted to just take this setup and make it repeatable on any object.
[5:37] Now it's sort of dependent on the two objects.
[5:41] So just be mindful of that if you do choose to go this route.
[5:44] But you can see how the displacement on the ground and the displacement on the pillar,
[5:49] it really helps when you have both.
[5:51] You start blending them to the two together.
[5:53] It really helps integrate without any sort of boolean.
[5:56] You sort of get like a little sticky situation there.
[5:59] Now you might want to tone up this up or down on the ground depending.
[6:05] And then you turn up the strength.
[6:07] And you could see how you could get really sort of interesting results with this type
[6:14] of effect, but we want just a little bit, just a little bit of displacement in there.
[6:17] So before we do the material part, let's go ahead and do the final blending of these
[6:21] two by setting a custom normal that'll merge these two together and really make the effect
[6:27] look good.
[6:28] So let's do a sample nearest surface node, really cool node.
[6:34] And what we can do is just take the displaced geometry output right into that.
[6:39] And we want to sample the nearest surface node, which would be the pillar based on the normal
[6:45] of the object.
[6:46] So take the normal into the sample position of that node and change this to vector.
[6:53] And really important.
[6:55] When you do that, this value appears and you want to make sure you actually plug it
[7:00] into the value, not the sample position node.
[7:02] I've gotten that confused.
[7:05] So when you change it to vector, which is what we need, take the normal output into the value.
[7:09] All right, now we need a geometry proximity node.
[7:13] And we'll take that same output into the geometry proximity.
[7:17] And we need a mixed node.
[7:20] And this is going to be a vector, so mixed vector node.
[7:23] And we'll take the sample nearest surface into the A and then just the regular normal
[7:29] into the B right there.
[7:32] And now this geometry proximity, this distance value is going to be the factor of these two.
[7:37] And now we need a set normal node, so shift A and set mesh normal.
[7:43] And we'll feed that in to our timeline here and we'll choose free.
[7:46] Okay, and you see this custom normal slot, what we can do is just take the result, the
[7:52] mixture that we've created here into that custom normal and magic.
[7:57] You see it's all blended together.
[8:02] No booleans here.
[8:05] Pretty cool.
[8:10] You can of course drop in a map range node and adjust those values there, depending on
[8:15] what you're seeing is looking like.
[8:17] All right, so now we have the blending of the geometry.
[8:20] We just need to blend the materials because right now if we go to material mode, you can
[8:23] see it just looks like a rock that's really out of place right on the dirt.
[8:27] And we want to blend these together so that you don't have that harsh seam.
[8:31] Thankfully, we have all the data we need right here with this output.
[8:34] So what we can do is just take this color output into a store named attribute node.
[8:40] And we can just drop that anywhere in here and just connect it up with our rest of our
[8:49] timeline here, store named attribute.
[8:52] We're just taking this value from our map range node and we're going to store it.
[8:57] And we can call this value blend or you can call it whatever you want.
[9:02] I'll call it blend.
[9:03] Okay, now let's jump into our shader editor.
[9:07] And you'll notice I have these two materials.
[9:09] I have this dirt, this rock face material, and I have this muddy tracks material.
[9:15] And we want to blend both of these together.
[9:17] Well, you can do this with any material.
[9:19] It's very simple.
[9:20] We're just going to use that store named attribute as the mixture of these two materials.
[9:25] So let me just grab everything up into this material output node right here.
[9:31] So our principal would be SDF and our displacement.
[9:35] So everything that makes up my shader right before my material output.
[9:38] And this is a really easy way to mix materials.
[9:42] With all that material selected, I'm just going to press Ctrl G and group that material.
[9:47] And if I tab out, you'll notice we still have displacement and BSDF.
[9:52] If you want other things like normal and things like that, then you can just feed it up in
[9:55] the material output.
[9:57] For our purposes, I'm just going to worry about the BSDF and displacement.
[10:01] And now this node group, I can give this a name, just name it muddy.
[10:05] Okay, and I'm going to do the same with my rock material.
[10:09] I'll just grab everything up until here, Ctrl G, tab out, and I'll name this rock.
[10:17] Really original.
[10:18] All right, now I'm going to create a brand new material.
[10:22] And I'll just call this, you know, blended.
[10:26] Okay, I'm just going to delete that principal BSDF.
[10:30] Now the benefit of grouping the other two materials is in the shader editor, if you
[10:34] press Shift A now and go to group, look at that.
[10:38] We have muddy and rock, our two material groups.
[10:41] So we can just add both of these right into our new master material.
[10:46] And it's nice and clean and tidy.
[10:48] And now all we have to do is just mix the BSDF.
[10:52] So let's do a mix shader for the principal BSDFs, mixing these two, bam.
[11:00] And then a mix vector for the displacement because those are vectors.
[11:06] And just make sure you do the A and B in the same, and I didn't mess it up right there.
[11:12] Make sure you do A and B in the same slot as the BSDF, or it'll look weird.
[11:17] Feed that into the displacement of the material output on your blended materials.
[11:22] Now you've probably been able to figure out that the factor of these mixtures is going
[11:26] to be our stored attribute that we called blended.
[11:31] So just drop in an attribute node and type the same name, which was blend, taking the
[11:36] factor and feeding it into the factor of this mix shader.
[11:40] Now to see how it looks, we need to assign that blended material to our object here.
[11:47] And we really only need to do it before this joint geometry because it just has to be applied
[11:50] to the rock.
[11:51] So let's add a set material node, and actually you could just set it anywhere, but easy enough
[11:57] to do it here.
[11:58] That blended material, and there you go.
[12:01] It's blended, but the incorrect direction, the opposite.
[12:06] And that's easy.
[12:07] You could reverse the color ramp, or in the shader editor, you can just reverse the A
[12:11] and B really simply.
[12:17] And that's the benefit of mixing it like this, where you can simply adjust things.
[12:20] Okay, so now we're not really seeing the gradient, but it is there.
[12:24] If we look closely, you can adjust it right here, and that'll adjust the material.
[12:30] But we're also adjusting our sort of geometry displacement.
[12:34] So I think what I'm going to do is just make my own color ramp for the material.
[12:39] So we'll just shift D, duplicate this color ramp, and kind of do a separate from what's
[12:44] affecting our geometry here.
[12:46] So just cut that connection, and now it's only affecting the geometry this color ramp
[12:51] is.
[12:52] And now this one will just affect the store named attribute.
[12:57] And we can adjust how high up this material goes.
[13:02] And now everything should be set up where you can move this rock around, rotate it, sink
[13:11] it down.
[13:12] It looks like it's just part of the dirt mound.
[13:16] Move it around.
[13:20] If you take it all the way out of the dirt, it's just a nice clean rock.
[13:23] The closer we get, it starts to bleed welled into the mud mound.
[13:32] And you can see what it's doing with the geometry.
[13:36] Blending nicely, no booleans or anything.
[13:38] So there you go.
[13:39] That's how to blend two objects in Blender using geometry nodes.
[13:42] I hope this was useful.
[13:43] I'll, of course, make this file available to all my Patreon members.
[13:47] Thank you so much, all of you, for supporting.
[13:49] I had a bunch of people sign up recently, took a small break from YouTube, but I'm back
[13:54] and I really appreciate everyone supporting me there on Patreon.
[13:57] It really means a lot.
[13:58] It helps me keep making these videos.
[14:00] So thanks so much.
[14:01] Check out this file.
[14:02] You can grab it if you want to do that.
[14:05] And send me a message there on Patreon.
[14:07] Leave a comment on this video on YouTube.
[14:09] I read all the comments and I try to respond to as many as I can.
[14:12] But thanks so much for watching, everyone.
[14:14] I will see you next time.



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
