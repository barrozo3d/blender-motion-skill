---
title: Mastering Complex Textures in Blender
source: YouTube
url: https://www.youtube.com/watch?v=GejnTuB2GNQ
author: rileyb3d
ingested: 2026-08-17
blender_version: "4.x (viewport title bar visible in captured frames, exact point release not fully legible)"
tags: [materials, shaders, procedural, rendering, product-viz, motion-design, intermediate, advanced, blender-4x]
extraction_status: complete
frames_dir: tutorials/frames/mastering-complex-textures-in-blender/
frame_count: 9
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Mastering Complex Textures in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=GejnTuB2GNQ)
**Author:** rileyb3d
**Duration:** 30m4s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone, welcome. We're gonna be modeling a notebook and the goal here is to cover some basic modeling, some texturing and
[0:07] hopefully we'll get to some texture baking and blender. This is intended to be like a low-poly kind of game asset notebook and
[0:15] let's just get right into it. The only thing I've done so far is I've looked up the overall dimensions of a notebook and it came up with


### Modeling [0:17]
**Transcript (timestamped):**
[0:22] seven and a half by
[0:24] 9.75 inches. I added plain and in the end panel if you go to item you could see that I just typed in
[0:31] seven and a half inches and 9.75 inches here and
[0:36] that gave me our conversion. By the way, if you ever don't know what I'm pressing look at the bottom left
[0:41] you'll see my keys there. We're gonna go into edit mode and extrude this up and let's create this
[0:47] smooth shape here. Now there are a lot of ways you could do this. I am going to select this face here
[0:54] and hit shift S.
[0:56] This is to move around the 3D cursor and we're gonna go cursor to selected that moves it to the center of that face and
[1:03] in object mode and hit shift A to add and go to circle. Now we don't need 32 vertices.
[1:09] Let's just go with 12. We'll scale this down and rotate it on X 90 degrees.
[1:14] I'm just gonna do my front view here and I'm just eyeballing this and let's move this along the Y axis and snap it here.
[1:22] This is the snapping menu up here.
[1:24] I just have vertex, hold down shift, edge and face selected so I can snap to anything at any time.
[1:30] I just have to hold down control while I'm moving that around. G for grab, Y for the Y axis,
[1:36] snap to that face right there.
[1:38] It's very quick and intuitive once you're used to it.
[1:42] Just gonna clean up some of these vertices or delete them. I'm gonna extrude on Y and snap to this
[1:49] vertices over here and then let's just grab this object and
[1:55] delete that face to make way for that.
[1:58] Let's just go ahead and join both these objects with control J back in edit mode.
[2:03] These vertices are separated from each other. So like everything with A, M, merge by distance and
[2:10] as you can see that removed zero vertices. Didn't really do anything. We can actually decrease this.
[2:16] Let's decrease it to point zero one meters and as you can see that found four vertices.
[2:22] Let's grab the remaining. I don't think we'll be able to grid fill. Hit control F grid fill.
[2:28] No, and that's because we need one more vertices here. Let's try that again.
[2:33] Beautiful.
[2:34] Do that one more time. Now we have that curved edge there for our notebook.
[2:39] We want to inset the pages though. So what I'm gonna do is
[2:43] I'm just gonna select everything that would be a page and by the way to do that selection that I just did.
[2:50] Just select one hold down shift control select the other corner.
[2:54] It'll select everything in between which is really nice.
[2:56] So just press I and we'll bring this in there.
[3:00] Then we're gonna do a quick alt E extrude faces along normals and just push them in a bit.
[3:06] That's looking great. We have kind of the rough shape of our notebook. We can continue on.
[3:11] Let's right click and hit shade auto smooth.
[3:14] Now what that's done is added a modifier the smooth by angle modifier.
[3:19] 30 degrees you could see we're getting a really sharp edge there on the spine, which is no good.
[3:23] If we increase that even slightly, right?
[3:26] It's like 30.1 it takes care of that. The only other area I want to clean up is these corners here.
[3:33] Let's just add a bevel with control B and add one extra loop there with my scroll wheel.
[3:39] That's pretty nice.
[3:40] Let's get into some very very quick basic UV unwrapping.


### UV Unwrapping [3:41]
**Transcript (timestamped):**
[3:44] Go to edit mode and I'll just select this edge here kind of on the inside.
[3:51] Why am I selecting this? Well to me this is kind of a natural place where we would have a seam.
[3:57] So select all those edges hit you mark seam.
[4:00] Now if we unwrap this right now, let's just go unwrap conformal.
[4:04] That's pretty good. That worked out nicely.
[4:06] However, we're not utilizing nearly the UV space that we could be.
[4:11] But we have a really big problem.
[4:13] The problem is we have this solid chunk right here.
[4:17] This as you could see in our model represents the whole page material.
[4:22] And the reason this is a problem is because that is so long and narrow.
[4:26] It's stopping anything else from being scaled up.
[4:29] We can manually come in here and scale this up, which is really nice.
[4:34] That's one of the options that we have.
[4:35] So let's just move this down to the bottom and scale this up here.
[4:40] Now what this is doing is the pages and the cover now have what's called a different textual density.
[4:47] In our case, that's going to be totally fine.
[4:50] So now as you can see, we have a great UV unwrapped.


### Material Assignment [4:53]
**Transcript (timestamped):**
[4:53] Let's do some quick material assignments.
[4:56] I want to have a little bit more geometry.
[4:59] Let me see if I can figure out what's going on here.
[5:01] Ah, yes. Okay.
[5:03] So we do not have a quad on the top and bottom cover.
[5:08] And that's because the way we inset this or the way we bevel these corners,
[5:12] we ended up with eight vertices.
[5:14] That's what we call an end gone. It's more than four.
[5:17] Really easy fix. There's a few ways you could do this.
[5:19] One way, let's just delete that face on the top and the bottom.
[5:23] Then let's select that edge loop here and let's try to do a grid fill.
[5:28] Beautiful. That worked great.
[5:30] And now we have quads.
[5:32] Let's do the same thing down here.
[5:34] Control F grid fill.
[5:35] Now what I wanted to do is hit control R and add a loop cut over here
[5:40] because I want the spine to have a completely different material than the cover.
[5:45] So the first material we can call pages, the next material,
[5:48] let's just call cover and the last material, spine.
[5:52] The spine will make black pages will make our cover will make gray pages will leave white.
[6:00] Now let's do some material assignments here.
[6:02] Let's select everything and just make everything the cover.
[6:06] And then let's select from here to here.
[6:09] And I'm going to grab everything in between.
[6:11] And I know I have some pages that we don't need,
[6:13] but we'll we'll get rid of those in a second.
[6:15] You'd always press C for circle select, which is really, really handy.
[6:19] Let's make this our spine.
[6:21] And now let's come through here, select our pages is kind of the last thing.
[6:27] And again, holding down control shift is a great way to select everything in between
[6:33] two faces that you select.
[6:35] And that will be our pages.
[6:38] So that's looking great as far as material assignment goes.
[6:40] Now we have UVs.
[6:42] We have material assignments.


### Texturing [6:43]
**Transcript (timestamped):**
[6:43] Let's get to some actual texturing now.
[6:46] So let's start with the really easy one.
[6:47] Let's start with pages.
[6:49] Pretty simple.
[6:50] What we're going to do is drop down a noise texture.
[6:53] And you can always hit control shift and click on a node to solo the effect of that note.
[7:00] So that's what I just did there.
[7:01] And you could see this noise texture stretching across these pages.
[7:05] Now, because we have nice clean UVs, we can actually use those.
[7:09] So let's hit control T to set up some mapping.
[7:11] And instead of generating a noise texture, let's use our UV map for that.
[7:16] Then if we increase the scale, you could start to see that nice noise texture.
[7:20] I want to scale this down on two of the three dimensions, X, Y and Z. X could be zero.
[7:26] If we increase Y, we'll have more pages in there, maybe 15 or so.
[7:31] Let's use this.
[7:32] We're going to go into a bump.
[7:34] So let's just plug it into normal temporarily.
[7:36] And let's type in bump and drop that in between those and have this drive the height.
[7:42] And we could use the same texture to go into the base color.
[7:45] And that's a good starting point for the actual cover.
[7:48] I'm going to add a noise texture.
[7:50] So let's just solo this to see what's going on here.
[7:53] If I change this, we can go down here and try to find one that works well for what we're going for.
[7:59] What I'm going for is kind of your standard mead composition, like college ruled notebooks.
[8:06] We had to order them every year for school.
[8:08] That's kind of the pattern I'm going for.
[8:10] So to get there, I'm just going to increase this scale by default.
[8:14] This is pretty darn close.
[8:16] I want to clamp this down to just black and white.
[8:19] So to do that, not a color ramp, I'm going to use a map range node, which is really,
[8:25] really useful.
[8:25] And what we could do is instead of going from a minimum of zero to one,
[8:29] we can clamp down that from maximum.
[8:32] As you can see that clamps down and gets rid of a lot of those gray areas.
[8:36] We could also clamp up on the black.
[8:39] It's very, very crispy, very defined edges.
[8:42] And we could even grab both of these and kind of come up or down a little bit.
[8:46] If we want more black or more white, I think something like that works well.
[8:52] Now this is just the base layer for our texture.
[8:55] Nothing stopping us from coming in here and layering on more wear and tear edge details.
[9:01] That's the beauty of texturing is layering.
[9:03] That's the most important concept, in my opinion, when it comes to textures,
[9:07] a great resource for image textures.
[9:10] I really like textures.com.
[9:12] You do have to pay monthly for this.
[9:13] Just literally typed in book covers and you have all of these options.
[9:18] One that catches my eye is this one.
[9:20] We'll open that up in a new tab.
[9:21] I'm looking for some edge wear.
[9:24] This one up here, that could be nice, potentially great.
[9:27] Let's go back to Blender.
[9:28] Let's start to work with these.
[9:30] So I'm going to open up that new image and I'm going to drag it into Blender.
[9:35] And that will bring in an image node.
[9:37] If we solo this, we could see the mapping.
[9:40] And this isn't going to line up perfectly.
[9:42] You can see our UV space down here.
[9:45] That's fine.
[9:46] We can actually adjust this with some mapping nodes.
[9:48] So just hit Ctrl T to get that texture mapping.
[9:51] And we can start to kind of scale this.
[9:54] So I'm going to scale this one axis at a time.
[9:58] Something like that should be fine.
[10:00] We can also move it on X.
[10:01] Let's come into edit mode and make sure it's open here in our UV editor.
[10:07] And I'm going to cheat some things just a little bit.
[10:10] What we could do, I just went to vertex selection.
[10:14] Let's select these and let's start to scale them on X.
[10:19] Now we're just looking at the straight image texture.
[10:21] We want to actually layer this in to what we have here.
[10:24] So how can we do that?
[10:26] One thing we could do is we could use a mixed color node.
[10:29] And we could use this as the second input.
[10:31] All this is doing is it's just mixing between two values.
[10:34] We have input A, input B, and we have a factor.
[10:38] Now this isn't very useful.
[10:40] One little trick is we could use the same image texture here
[10:44] to drive the factor as well.
[10:47] And then we could drop down our trusty map range node.
[10:50] Just probably my most used node, by the way.
[10:53] And we could start to play with the effect by clamping you down
[10:57] in certain areas.
[10:58] As you can see, I'm bringing up the darks.
[11:01] So something like that could be fine.
[11:03] If we wanted to desaturate this, we could drop down a hue saturation value node.
[11:07] Okay, wrong place.
[11:09] There we go.
[11:10] Drop it in here.
[11:11] Now saturation could be like 0.3.
[11:13] I don't want that yellow coming through necessarily.
[11:17] Now let's let's layer in something else.
[11:19] Let's drop our other image texture that we have.
[11:22] Why not?
[11:22] And let's do something similar.
[11:24] Let's focus that one.
[11:25] But let's let's use our own mapping.
[11:28] Kind of do the same thing we were doing before.
[11:29] Let's scale it on X individually.
[11:32] Now let's focus on Y.
[11:34] So let's drop down another mixed color node.
[11:37] Put this into the B value again.
[11:40] And let's just use that as a factor.
[11:43] Let's drop down our map range again.
[11:46] And see what we can get away with.
[11:48] I want to kind of bring in some of that edge stuff that we have going on.
[11:53] Cool.
[11:54] Now I haven't messed with the roughness at all.
[11:58] Keep that in mind.
[11:59] That comes next.
[12:00] Let's just do another hue saturation value here.
[12:03] And let's just desaturate this a little bit.
[12:05] Let's keep it a little bit warm.
[12:07] Kind of like some paper is coming through there.
[12:10] Let's just show you what we've done.
[12:12] If we take all of this and mute it with M,
[12:15] you could see how much that layering has done for our notebook already.
[12:20] Let's start to play around with the roughness value.
[12:23] Let's start the equation with this guy right here.
[12:27] This noise texture.
[12:28] Let's plug it straight into the roughness.
[12:30] And that's going to be very, very glossy.
[12:32] So let's drop down another map range.
[12:35] And instead of zero to one, zero is totally glossy.
[12:38] We can bring this up.
[12:40] So it's maybe a max or a minimum of 0.3.
[12:44] However, we definitely want to layer in more than that.
[12:46] So let's drop down a mix color node.
[12:49] And let's just do something crazy.
[12:51] Let's take the final result from the color.
[12:53] And let's mix that in as the factor, let's say.
[12:57] And if this was perfectly rough, you could see that starts to bring in roughness here.
[13:02] Let's just let's see what happens when we use it for this map range.
[13:07] Oops, not there.
[13:08] Let's go right there.
[13:12] See what's going on here.
[13:14] Let's make this pretty rough.
[13:17] Feel like this notebook would be kind of rough and beating up a bit.
[13:22] And then let's do one final map range for the final roughness.
[13:28] There you go.
[13:28] It's mostly rough.
[13:30] So you look at that.
[13:30] Has a little bit of variation.
[13:32] I think something like that works nicely.
[13:34] Node graphs are always a little bit messy, right?
[13:37] We're going to hopefully bake this down so that we don't have this big mess in the end.
[13:41] It'll be nice and clean.
[13:43] Okay, now, normal map.
[13:45] One thing I did want to do is I wanted to drop down a bevel node
[13:49] since we're going to be baking this out.
[13:51] And this is a nice way to handle the sharp edges here.
[13:54] Let's just crank up the samples and do a really low distance,
[13:59] hardly noticeable in the final.
[14:00] That's not the only normal information we want.
[14:03] We could also use everything we've done so far as a normal map.
[14:08] Let's just start with the base color that we have.
[14:11] So let's go in here and use this base color.
[14:14] Let me clean it up a little bit.
[14:16] Let's use this as the height information.
[14:18] Now I want to add this label.
[14:21] We're going to go mix shader here.
[14:24] So this is in the end.
[14:26] We have this whole shader and we're going to mix in a totally new shader.
[14:30] Let's grab our image that I found online for this label.
[14:34] Just search for a composition notebook label.
[14:36] We'll find a good one.
[14:37] And let's use the alpha of that for the factor on the mix shader.
[14:41] Immediately, this doesn't look right.
[14:43] Let's drop in another principled shader and let's drag that in for the second input.
[14:48] And just so we can clearly see what's going on, if it wasn't obvious already,
[14:51] let's turn that red.
[14:52] And now let's play with the mapping here, control T.
[14:56] And as we increase the scale, you can see there's our label.
[14:59] The problem is this is repeating over and over again.
[15:03] Let's change this from repeat.
[15:05] Let's try clip.
[15:07] We'll do the trick for us, I think.
[15:09] Let's move this into position.
[15:11] Now this is stretched a little bit because it wasn't a square image.
[15:14] So I'm just going to have to scale that a little bit.
[15:17] Just eyeball it.
[15:18] And let's place this about here.
[15:20] And let's use that same label here for the actual base color.
[15:25] And there you go.
[15:25] Right now, this is a PNG with transparency.
[15:28] That's how we're getting this alpha value.
[15:30] Let's drop down a mix color node.
[15:33] And I searched for twangpaper on textures.com.
[15:36] And I found a nice one.
[15:37] Let's use that.
[15:39] And let's bring this into maybe the factor on this mix shader node.
[15:44] Let's solo this.
[15:46] Okay.
[15:47] Yeah, we're going to have to play around here a little bit.
[15:52] Let's go.
[15:53] It's also set to repeat.
[15:55] Let's set it to clip.
[15:56] Now it is a little finicky to try to author textures like this with the mapping.
[16:02] So I'm just going to widen this a little bit.
[16:05] Yeah, something like that.
[16:07] What exactly are we doing here?
[16:09] We're using this to drive the factor.
[16:12] Let's drop down a map range node.
[16:14] And again, if we clamp values, you could see what we can accomplish here.
[16:19] All right.
[16:19] This is very, very powerful.
[16:20] Again, the map range node, definitely my most used node ever.
[16:24] It really comes in clutch all the time.
[16:26] Super useful.
[16:26] We could always flip or invert the result here.
[16:30] So we're eating away the edges.
[16:32] I think I like that more just because I want,
[16:35] I want to see composition book kind of recognize this.
[16:39] And yeah, we can play around with these values,
[16:41] find out how much of this we want to eat away,
[16:43] how strong we want the effect to be.
[16:45] Even in the parts where it's still there,
[16:47] you're kind of seeing through this really, really rubbed off to the point
[16:51] where you could see the notebook underneath it.
[16:52] Yeah, I think that's really nice.
[16:54] However, the base color, I'm going to drop down a mixed color node.
[16:59] I'm going to change this to color.
[17:01] And I'm just going to yellow that up a little bit.
[17:04] Maybe I'll grab this same color that we have over here.
[17:07] And we can decide how strong we want that to be.
[17:10] Yeah, I think something like that.
[17:13] Now you could layer in all kinds of stuff.
[17:16] One trick that I like to do,
[17:17] let me just grab something real quick.
[17:19] I like to keep masking tape handy.
[17:23] All right.
[17:23] This is a cool way to add custom little notes on your props.
[17:27] I get rip this off, take a piece here.
[17:30] I'm going to need to find a pen in a second.
[17:32] Couldn't find a pen, found some charcoal.
[17:35] Anytime I could pick up, you know,
[17:36] piece of paper writing utensil in the real world
[17:39] and write something out,
[17:40] that's just going to be much more authentic.
[17:42] That's going to transfer over really well for a texture.
[17:45] So give me a second.
[17:46] I will just write down something.
[17:48] Let's see what we can write here.
[17:52] And let me just take a picture.
[17:53] All right.
[17:53] So we're in Photoshop for better for worse.
[17:56] You can do the same thing in a infinity photo.
[17:57] I'm just going to eyeball this.
[17:59] I'm going to go to quick object select.
[18:01] Let's see if this picks up what we want.
[18:03] Come here and let's just crop down on this.
[18:08] Just export.
[18:09] Let's just do another mixed shader.
[18:11] I know there are decal plugins.
[18:13] I try to go as vanilla blender as I can for my tutorials,
[18:17] just so that people can follow along without buying stuff.
[18:21] Every now and then there is something I just really recommend that you buy.
[18:25] Like UV pack master.
[18:26] That's great for UVs.
[18:28] Let's change this.
[18:29] Same as the other ones.
[18:30] Let's change it to clips.
[18:31] We don't repeat here.
[18:33] And we're going to really have to play with this scale.
[18:36] And again, I am just going to eyeball the proper dimensions.
[18:40] We really should be exporting textures on a square aspect ratio.
[18:45] So we don't have to eyeball things to do what we should have done before.
[18:49] Let's crop this, but let's tell it to be one by one square.
[18:53] This is going to be a lot cleaner.
[18:54] So let's export that again.
[18:55] I hit control shift alt W to export quickly in Photoshop.
[18:59] That's quite a shortcut.
[19:01] Then let's just go solid and then render view so it refreshes itself.
[19:05] And now this should actually be the same number all the way through.
[19:11] There's no guessing.
[19:12] We can rotate it without a screwing up the aspect ratio.
[19:15] That's just going to be a lot nicer to work with.
[19:18] Okay, we want this to have some interesting texture here.
[19:22] So let's go to the roughness channel.
[19:24] Let's drop down a map range.
[19:26] Again, I use it all over the place.
[19:28] It's very, very useful.
[19:30] Let's use this as a bump.
[19:32] And I'm going to go back and do this for the label too.
[19:35] We forgot to do any of this.
[19:36] So let's find a good value here, something like that.
[19:40] Just subtle.
[19:41] Yeah, let's take the factor here, do a mix color,
[19:45] and let's take the actual tape color as the factor.
[19:48] Drop a map range in there and see what kind of nonsense we can get up to here.
[19:55] Something like that.
[19:57] It's kind of fading in a little bit.
[19:59] I like that.
[20:00] So yeah, this masking tape technique,
[20:02] it's one I use all the time on real world client projects.
[20:05] I just used it on this real engineering YouTube channel video,
[20:08] and it just adds some nice authenticity to your props.
[20:12] All right, now our pages by comparison are looking extremely white.
[20:17] Let's just go to textures.com.
[20:19] I'm just searching for grunge.
[20:21] I'm just trying to find some general kind of grungy textures,
[20:24] some kind of breakup noise, something like this should work.
[20:27] This is a free one you can go download.
[20:29] And let's drop this into the pages.
[20:32] Let's drop down a mix color node and let's just mix that in.
[20:36] Play with the mapping a little bit.
[20:38] Again, if we go maybe down a little bit on X upon Y,
[20:43] just make it flat, more flat, something like that.
[20:47] Yeah, oh, I like that.
[20:48] Let's have this drive a factor for a color value,
[20:51] and let's have this be nice and yellow.
[20:55] And let's drop down a map range.
[20:57] Let's just drive all the yellow with this.
[21:00] Some areas will be much more yellow.
[21:02] Let's increase this scale overall, but more so on Y.
[21:06] This should also change the values.
[21:09] Let's duplicate this and let's have this one be the value.
[21:15] Have the same factor, and let's have this just be darker.
[21:18] Yeah, I think I like that a lot.
[21:21] And let's use that same thing for the overall roughness.
[21:25] Let's drop down a map range so we can control that.
[21:29] Bring this up so it never gets quite so glossy.
[21:32] Cool.
[21:33] Now finally, let's work on this spine.
[21:36] Let's add another texture and let's grab the same cover texture.
[21:40] Let's duplicate this though.
[21:42] So now it's a new texture.
[21:44] It's its own thing.
[21:46] And we'll just call this one spine two for a second.
[21:49] Let's delete the other spine.
[21:50] Well, actually, let's select the ones that belong to the spine
[21:55] and now assign spine two.
[21:57] And now we can delete that and let's just call this one spine.
[22:00] Okay, now this is just using what we had over here.
[22:04] Obviously, that's not what we want to go for.
[22:06] Since this is a new texture, I'm just trying to reuse a lot of what we had.
[22:11] We don't need this mix shader or this mix shader
[22:14] because that was all the label and the little sticker thing
[22:18] or the piece of tape that we put down.
[22:19] So let's get rid of all of this.
[22:21] We just don't need it.
[22:23] This is the main thing I want to bring in right now.
[22:26] So let's get rid of all of this noise.
[22:29] Everything that's going on here.
[22:31] Let's just delete everything except for the bevel.
[22:34] We can keep that.
[22:35] So let's just plug in this spine to start.
[22:38] All right.
[22:38] Let's drop down a huge saturation value node.
[22:42] Let's decrease the value, maybe increase the saturation.
[22:45] Let's use this texture as the roughness.
[22:47] We're definitely going to need a map range.
[22:49] That is glossy as hell.
[22:51] We don't want that.
[22:53] Let's clamp way down on the lights.
[22:55] Hey, that's pretty nice.
[22:57] See if we can get away with that same texture for the height on the bump node.
[23:01] So far, I'm just using basically one image texture to drive base color,
[23:05] the roughness, the normal.
[23:07] You can really get a lot out of one texture,
[23:10] which is one technique I just love, love to use.
[23:13] Yeah, I think that's great.
[23:14] Now, one thing we could do to clean this up and make it even better
[23:17] is right now we have these huge shader node networks.
[23:20] There's a lot that's being computed.
[23:22] There's a lot of images.
[23:23] What if we wanted to bake this down to a simple set of maps,
[23:26] something we could take into a Godot engine or Unreal Engine
[23:30] so that we could turn this into a game asset?


### PBR Bake for Games [23:32]
**Transcript (timestamped):**
[23:32] Well, let's do that next.
[23:33] Now, the first thing we want to talk about is optimizing the actual mesh,
[23:37] the geometry that we have.
[23:38] Right now, this entire notebook is made up of 102 vertices, 200 triangles.
[23:45] Now, that is not bad.
[23:47] Honestly, we could get away with that.
[23:49] Let's just, for the sake of it, see what it would take to make a low poly version of this.
[23:54] So let's call this one book underscore high, because that's our high poly.
[24:00] Let's duplicate it, move it over here, and let's call this one, you guessed it,
[24:05] book underscore low.
[24:08] And for this one, let's just go to object mode and let's have a look around.
[24:12] Now, the key here is we want to dissolve any edge loops that do not contribute to the object's silhouette.
[24:19] What do I mean by that?
[24:20] Well, if we dissolve this one, for example, see how drastically that changes the shape of this book?
[24:27] That's no good.
[24:27] We don't want to dissolve that one.
[24:29] That is contributing to the object's silhouette.
[24:32] What about this one?
[24:33] That one, we could definitely get away with dissolving.
[24:35] Doesn't really contribute to the silhouette.
[24:37] This is a case where the high poly is already pretty low poly.
[24:41] However, I do want to show you the process of baking from a high poly object to a low poly.
[24:45] So we're going to roll with it, even though we're going from
[24:48] 200 triangles to 172 triangles.
[24:51] It's not really a big deal.
[24:53] Now, something else we want to do on this mesh is we want to triangulate the mesh.
[24:57] So you could come over here, add a modifier and add the triangulate modifier.
[25:01] Come here to wireframe.
[25:02] You could see that that has indeed triangulated that mesh.
[25:05] The reason we want to do that is because a game engine like a dough, unity, unreal,
[25:10] they all triangulate your mesh before they render it in the game engine.
[25:15] In fact, cycles even triangulates your mesh before it throws it into a render.
[25:20] So what we could do by triangulating it now is to lock in the triangles so that they're not
[25:26] randomly generated in the engine, which might cause shading artifacts if it generates different
[25:31] triangles from what we use for baking.
[25:34] So yeah, that'll be applied when we export this object, but we are good to go.
[25:38] So let's save this.
[25:39] We have it labeled high and low.
[25:41] Let's clear the location of that so they're right on top of each other.
[25:44] I'm going to be baking with an blender.
[25:46] It works for me.
[25:47] You can use something like substance or marmoset tool bag.
[25:50] Those tools are much more specialized.
[25:52] They're much faster and they offer a little bit more flexibility.
[25:55] However, I tend to prioritize staying within one software package just because it saves
[26:00] me a lot of time from switching back and forth between things.
[26:03] So you just have to know how to get it to work, how you need it.
[26:06] Okay, with that out of the way, let's make sure our low poly has good UVs and it does.
[26:11] These are fine.
[26:12] Let's roll with what we already have.
[26:14] We haven't really changed things, but you do want to make sure your low poly has UVs.
[26:18] A few things to take note here.
[26:19] Because we lost that loop, we lost that material assignment that we needed with the high poly.
[26:24] So we're going to have to do a high to low bake, which is exactly what I wanted to show you.
[26:29] Save everything, go to object mode.
[26:31] And this is the second add-on that I want to show you.
[26:35] This is absolutely essential in my opinion if you are baking objects like this.
[26:39] It is called simple bake.
[26:41] It's very, very useful.
[26:42] We're going to do a PBR bake.
[26:44] In the bake objects, we want to add the high poly object because that's what we're baking.
[26:50] However, we want to say bake to target.
[26:53] So the target is the low poly object.
[26:56] So we're adding book high as the bake object and book low is the actual target.
[27:01] Next, we want to auto generate a cage.
[27:04] So just press this button and that's going to give you this nice little cage.
[27:08] You can increase or decrease the cage margin.
[27:11] That's pretty squirrely even when I hold down shift.
[27:14] So we might have to come in here manually.
[27:16] We want this as close to the originals we can get it because these are essentially the exact
[27:21] same shape.
[27:22] We could have this be incredibly small.
[27:25] Let's leave ray distance, multiplier, all that stuff by default.
[27:29] Usually it works.
[27:29] Let's go to PBR Bakes.
[27:31] What do we want?
[27:32] We want diffuse.
[27:33] We want roughness.
[27:35] We don't need any of this.
[27:36] Let's grab normal.
[27:38] We don't need metalness.
[27:39] We don't have any metal.
[27:40] Let's just call it good there.
[27:41] Texture settings.
[27:42] Let's talk about resolution.
[27:43] You could go really high, something like 4k.
[27:46] I think we could get away with 2k.
[27:48] Just to be safe, we could bake at 3k and output at 2k.
[27:52] That just gives us a little bit more crispiness in our maps.
[27:55] And UV settings are good.
[27:58] We don't want to auto detect UDEMs because we know we don't have them.
[28:01] And we don't need to generate a new UV map or anything like that.
[28:04] So let me say if always save one thing under export settings,
[28:09] let's actually export our maps.
[28:11] And I'm going to find a place on disk where I can export these.
[28:14] And yeah, let's just bake to target.
[28:18] So this isn't as fast as something like Marbset Toolbag.
[28:22] Marbset Toolbag is so fast with baking.
[28:25] Substance also very fast.
[28:27] But again, I'm taking into account all the time that I'm saving by using only Blender.
[28:33] I'm not jumping from software to software.
[28:35] So that was real time as I talked.
[28:37] All those images are now baked.
[28:39] So what we could do is we could turn off the auto-generated cage.
[28:44] Let's turn off the high poly object.
[28:46] And let's just look at our low poly here.
[28:49] If this worked right, we can get rid of all of these materials.
[28:52] And let's just create a new one called Book Baked.
[28:57] All right.
[28:57] And let's go to where we have the textures.
[29:00] And as you can see, we have everything baked down to one set of maps.
[29:04] Here's our base color, our normal, and our roughness.
[29:07] And the shader editor just hit Control-Shift-T for a principal texture setup.
[29:12] And we could just grab all of those at once.
[29:15] And it'll set them up automatically, which is really cool.
[29:17] And there you go.
[29:18] 2K maps, not quite as high resolution as the procedural materials, obviously.
[29:22] Let's bring that back just so we can compare the two.
[29:25] But this is a really nice set of maps.
[29:28] We have base color.
[29:29] We have roughness.
[29:30] We have normal.
[29:31] This could be taken into any game engine that you want.


### Wrap Up [29:34]
**Transcript (timestamped):**
[29:34] So there you have it.
[29:35] Do me a favor.
[29:36] Please consider going and supporting me on patreon.com.
[29:41] That's how I fund this channel and these free tutorials that I'm making for you.
[29:45] And go ahead and send me a message on there and show me your results.
[29:48] I can give you some feedback if you asked for it.
[29:51] Or I could just say, good job.
[29:52] Because if you made it through this video, that's quite a feat.
[29:55] This was a long one.
[29:56] I hope you learned some things along the way.
[29:59] Thanks for watching.
[30:00] And I'll see you in the next one.



---

## Captured Frames

- [1:38] tutorials/frames/mastering-complex-textures-in-blender/frame_000.jpg
- [3:44] tutorials/frames/mastering-complex-textures-in-blender/frame_001.jpg
- [5:19] tutorials/frames/mastering-complex-textures-in-blender/frame_002.jpg
- [8:19] tutorials/frames/mastering-complex-textures-in-blender/frame_003.jpg
- [10:44] tutorials/frames/mastering-complex-textures-in-blender/frame_004.jpg
- [14:26] tutorials/frames/mastering-complex-textures-in-blender/frame_005.jpg
- [24:12] tutorials/frames/mastering-complex-textures-in-blender/frame_006.jpg
- [27:01] tutorials/frames/mastering-complex-textures-in-blender/frame_007.jpg
- [29:00] tutorials/frames/mastering-complex-textures-in-blender/frame_008.jpg

---

## Structured Notes

### Core Technique
A full low-poly game-asset pipeline for a composition notebook: real-world-scale modeling with snapping/grid-fill, clean UV unwrapping, layered procedural + scanned-image shader work (the video's central lesson — "layering" is the single most important texturing concept), then a high-to-low-poly PBR bake (via the SimpleBake add-on) to collapse the whole complex shader graph into a clean, game-engine-ready Base Color/Roughness/Normal map set.

### Summary
**Modeling:** A Plane is scaled to real-world notebook dimensions (7.5 × 9.75 in, typed directly into the N-panel Item tab, which auto-converts to meters) and extruded up. The rounded spine is built by snapping a 12-vertex Circle (rotated 90° on X, scaled down) to the model using Blender's snap menu (Vertex/Edge/Face targets all enabled, held with Ctrl while moving) rather than manual eyeballing, then joining the objects (Ctrl+J), Merge by Distance (tightened to 0.01m to actually catch nearby-but-not-coincident verts) to weld seams, and Grid Fill (Ctrl+F) to close the resulting curved edge loop cleanly. Pages are inset (I) and pushed in along their normals (Alt+E → Extrude Faces Along Normals) for a page-stack look. Shade Auto Smooth (right-click) adds a Smooth by Angle modifier — tuning its angle just above the spine's actual angle (e.g. 30.1° vs. default 30°) removes an unwanted hard-shaded seam. A small Bevel (Ctrl+B, one extra loop) softens the remaining hard corners. **UV unwrapping:** a manually-marked seam (U → Mark Seam) plus Unwrap (Conformal) gives a workable base UV layout, but the long, thin page-block UV island wastes space and blocks other islands from scaling up — manually rescaling/repositioning UV islands (accepting a deliberately different texel density between pages and cover, called out as fine for this use case) is presented as a legitimate, common practical fix over trying to get a "perfect" automatic unwrap. **Material assignment cleanup:** an 8-vertex n-gon left over from beveled corners (not a quad) is fixed by deleting the face and Grid-Fill-ing it back in; an extra edge loop (Ctrl+R) separates the spine from the covers so it can carry its own material. Three materials are assigned via edge-loop/face selection tricks (Ctrl+Shift-click to select everything between two picks; C for circle-select): Pages (left white), Cover (grayed), Spine (blackened). **Texturing — the core lesson (layering):** Pages get a Noise Texture mapped via the object's own UV map (Ctrl+T for a Mapping node, feeding UV instead of Generated) with non-uniform scale (X flattened to 0, Y scaled up for "more pages") driving both Base Color and, through a Bump node, surface Height. For the Cover, a Noise Texture (browsed live via the node's built-in noise-type dropdown, soloed with Ctrl+Shift-click) approximates a college-ruled "Mead composition notebook" marbled pattern, then a Map Range node (explicitly called the presenter's most-used node throughout the video) clamps the noise to crisp black/white rather than a smooth gradient by pulling in the min/max thresholds from both ends. On top of that procedural base, downloaded reference images (sourced from textures.com — book-cover photos and dedicated "edge wear" textures) are dragged in as Image Texture nodes, each with its own Mapping node (Ctrl+T) set to **Clip** (not Repeat, to avoid tiling artifacts on a single unique surface) and manually scaled/positioned per-axis (sometimes further nudged by scaling UV vertices in the UV Editor) to line up with the model's UV space. Each image layer is blended in with a Mix Color node, frequently reusing the SAME image (or a Map Range-processed version of it) as the mix Factor as well as input B — a compact trick for driving both the visual blend and its intensity mask from one texture — and desaturated via a Hue/Saturation/Value node (lowered Saturation) to avoid clashing color casts between layered photo sources. Roughness is built the same layered way: a base Noise Texture piped through Map Range (0 → non-zero minimum, since 0 is "totally glossy"), then further Mix Color nodes blend in roughness contribution from the same color-layer results (e.g. using the final color mix as a driving factor for a rougher/more-worn value), finished with one last Map Range pass to set the overall min/max roughness range. A Bevel input node is added before the Normal socket to physically round hard baked edges (high Samples, tiny Distance — barely visible but important for clean bakes); the same layered color/height information doubles as extra Normal detail through a Bump node chained after the Bevel. **Compound label/sticker technique:** a downloaded "composition notebook label" PNG (with alpha) drives a Mix Shader between the base notebook shader and a second full Principled BSDF (temporarily tinted red to visualize its extent while positioning), using the label image's own Alpha output as the mix Factor, with its Mapping node set to Clip and manually scaled/positioned (accounting for non-square source image distortion) to sit correctly on the cover; the same label image doubles as that second shader's Base Color. A second downloaded "worn paper" texture is layered on top via another Mix Color + Map Range chain (inverted so wear "eats into" the edges of the label rather than the middle, revealing the notebook material underneath at the torn/rubbed edges) for an authentically peeling-label look. **Physical-reference texturing trick:** the presenter physically tears a piece of real masking tape, hand-writes a note on it with charcoal (no pen on hand), photographs it, cleanly cuts it out in Photoshop (Quick Object Select), and re-exports it cropped to an exact 1:1 square aspect ratio specifically so it can be scaled/rotated in Blender without guessing at non-square distortion — brought in as yet another Mix Shader layer (Clip mapping, careful scale/position), with its own Roughness/Bump contribution mapped in via Map Range, described as a real technique the presenter uses on paid client work for authenticity. Pages are finished with a downloaded "grunge"/breakup-noise texture layered via Mix Color, driving a yellowing color tint (warm color mixed in via Map Range-controlled factor), a separate darker "Value" pass duplicating the same factor logic, and a Map Range-controlled Roughness contribution. The Spine reuses (duplicates) the Cover's core Noise-Texture-driven node chain but strips out all the label/tape/mix-shader layers specific to the cover, demonstrating how one procedural base texture chain can economically drive Base Color, Roughness, AND Bump/Normal simultaneously with minimal extra nodes — flagged as a favorite, highly reusable technique. **PBR baking for game engines:** the full node-graph-heavy shader is optional to keep at final delivery — it can instead be baked down to a compact, portable PBR map set. Mesh optimization first: duplicate the model into `_high` and `_low` versions; on the low-poly, dissolve only edge loops that don't affect the silhouette (demonstrated: one loop drastically changes the shape and must stay, another barely matters and can go) — in this case only a small triangle-count reduction (200→172 tris) since the source was already fairly low-poly, but the workflow is shown in full regardless. A Triangulate modifier is added to the low-poly (not applied until export) because game engines — and even Cycles internally — triangulate meshes before rendering, so pre-triangulating avoids shading-artifact mismatches between the mesh triangulated for baking vs. re-triangulated differently at runtime. Both objects are zeroed to the same location (so the high-poly geometry sits inside/matching the low-poly for accurate ray-cast baking) and the low-poly's existing UVs are reused (confirmed still valid, since it's a near-identical topology). The **SimpleBake** add-on (explicitly recommended as essential for this kind of object-to-object baking workflow) is configured with the high-poly as the Bake Object and the low-poly as the Bake Target/"Bake to Target," an auto-generated ray-cast Cage (with a manually tightened Cage Margin, since the auto value was too aggressive/unstable — "squirrely" — for two near-identical shapes), default Ray Distance, and a PBR Bake selection of Diffuse + Roughness + Normal (Metalness skipped, no metal in the asset). Texture Settings: bake at 3K, output at 2K, for slightly crisper downsampled results than baking straight at 2K; UDIMs left off since none are used; Export Settings enabled to write the maps to disk automatically during the bake. After baking, the low-poly's material is replaced with a single fresh material, and Blender's built-in **Ctrl+Shift+T** "Add Principled Texture Setup" shortcut is used to batch-select and auto-wire all three baked image files (Base Color, Roughness, Normal) into a clean, minimal Principled BSDF setup in one action — yielding a portable 2K map set ready for import into Godot, Unity, or Unreal.

### Key Steps
1. Model to real-world scale by typing exact dimensions into the N-panel Item tab on a Plane (auto-converts units), then extrude/shape by hand.
2. Build curved details (e.g. a spine) with snapping (enable Vertex+Edge+Face snap targets, hold Ctrl while moving) rather than eyeballing; join separate pieces with Ctrl+J, weld with Merge by Distance (tighten the distance threshold if 0 vertices are found initially), and close resulting n-gon loops with Grid Fill (Ctrl+F, sometimes needing an extra vertex added first).
3. Inset (I) and Extrude Along Normals (Alt+E) to fake stacked-page depth; apply Shade Auto Smooth and nudge its angle threshold slightly above a problem edge's real angle to remove unwanted hard shading seams; add a light Bevel (Ctrl+B) with one extra loop to soften remaining hard corners.
4. UV unwrap with a manually marked seam (U → Mark Seam) and Unwrap (Conformal); manually rescale/reposition individual UV islands afterward to make better use of UV space, accepting non-uniform texel density between different parts of the model where appropriate.
5. Fix any leftover n-gons (e.g. from bevels) by deleting the face and Grid-Fill-ing it back to quads; add extra edge loops (Ctrl+R) to isolate regions (like a spine) that need their own material; assign materials via chained selection tricks (Ctrl+Shift-click between two picks, C for circle-select).
6. Build each material as layered procedural + photo-reference textures: start with a Noise Texture mapped through the object's own UV (Ctrl+T Mapping node set to UV instead of Generated) with non-uniform scale per axis; clamp/crisp the result with a Map Range node (the single most-reused node in the whole workflow) instead of a Color Ramp.
7. Layer in downloaded reference photos (textures.com or similar) as Image Texture nodes, each with an individual Mapping node set to Clip (never Repeat, for a one-off unique surface), scaled/positioned per axis to align with the UVs; blend each in via Mix Color, frequently reusing the same image (optionally through its own Map Range) as both the B input and the mix Factor; desaturate mismatched color casts with Hue/Saturation/Value nodes.
8. Build Roughness the same layered way: base Noise Texture → Map Range (clamp the minimum above 0, since 0 = fully glossy) → further Mix Color layers driven by the same color-layer results, finished with one final Map Range for the overall min/max range.
9. Add a Bevel input node before the material's Normal socket (high Samples, tiny Distance) to soften hard edges for a cleaner bake, and route the layered color/height information through a Bump node chained after it for extra surface detail.
10. For a label/sticker: bring in a PNG with alpha, use its Alpha output as a Mix Shader factor between the base material and a second full Principled BSDF (temporarily tinted a bright color to see its placement while positioning), map with Clip and manually scale/position (correcting for non-square source aspect ratio); layer a second "worn/torn" texture on top via Mix Color + Map Range (invert if you want wear eating in from the edges rather than the center) to reveal the base material peeking through at torn spots.
11. For extra realism, physically create and photograph a real-world reference (e.g. torn masking tape with handwriting), crop it in an external editor to an exact square aspect ratio before re-importing, so it can be freely scaled/rotated in Blender without unintended stretch — layer it in via another Mix Shader with Clip mapping, and drive its own Roughness/Bump contribution through Map Range.
12. For a part that shares another part's core texture identity (e.g. spine vs. cover), duplicate that material's core Noise-Texture-driven node chain and strip out the parts-specific extra layers (labels, stickers, mix shaders) — one procedural texture chain can economically drive Base Color, Roughness, and Bump/Normal all at once.
13. To prepare for baking: duplicate the model into `_high` and `_low` copies; on the low-poly, dissolve only edge loops that don't affect the object's silhouette (test each candidate loop individually before committing); add a (not-yet-applied) Triangulate modifier to the low-poly to lock in consistent triangulation ahead of the game engine's own runtime triangulation; zero both objects to the same location; confirm/reuse valid UVs on the low-poly.
14. Use the SimpleBake add-on: set the high-poly as Bake Object and the low-poly as the Bake Target ("Bake to Target"); auto-generate a ray-cast Cage and manually tighten its Cage Margin if the auto value is unstable; select PBR passes to bake (Diffuse, Roughness, Normal — skip Metalness if nothing in the asset is metallic); set bake resolution higher than the output resolution (e.g. bake 3K, output 2K) for extra crispness; enable Export Settings to write maps to disk automatically; run the bake.
15. On the low-poly, delete the old procedural material, add a fresh empty material, and use Ctrl+Shift+T ("Add Principled Texture Setup") to batch-select the baked image files and auto-wire them into a clean minimal Principled BSDF — producing a portable map set for any game engine.

### Nodes / Settings
- Modeling: N-panel Item dimension entry, snap menu (Vertex/Edge/Face + Ctrl), Merge by Distance (tunable threshold), Grid Fill, Inset (I), Extrude Along Normals (Alt+E), Shade Auto Smooth (Smooth by Angle modifier, tunable angle), Bevel (Ctrl+B)
- UV: Mark Seam (U), Unwrap (Conformal), manual per-island rescale/reposition
- Shading core: Mapping node (Ctrl+T, Generated vs. UV, Clip vs. Repeat), Noise Texture (browsable noise-type dropdown), Map Range (clamping/remapping — the tutorial's single most-used node), Mix Color, Hue/Saturation/Value, Bump, Bevel (shader input node), Mix Shader (label/sticker/tape layering, Alpha-driven factors)
- Baking prep: `_high`/`_low` duplicate naming convention, silhouette-preserving edge-loop dissolve, Triangulate modifier (unapplied until export), zeroed transforms between high/low pairs
- Add-on: **SimpleBake** — Bake Objects (high) / Bake to Target (low), auto-generated Cage + Cage Margin, Ray Distance, PBR Bake selection (Diffuse/Roughness/Normal/Metalness), Texture Settings (bake vs. output resolution, UDIM toggle), Export Settings (auto-write to disk)
- Shortcut: Ctrl+Shift+T "Add Principled Texture Setup" for batch-wiring baked textures

### Difficulty
Advanced (a full production pipeline — modeling, UVs, deeply layered procedural+photo shader authoring, and a two-mesh high-to-low PBR bake with a specialized add-on — explicitly a long-form, non-beginner tutorial)

### Blender Version
4.x — Blender's UI in the captured frames (including the Cycles/EEVEE render properties layout and the SimpleBake add-on panel) is consistent with the 4.x era; exact point release not fully legible.

### Tags
materials, shaders, procedural, rendering, product-viz, motion-design, intermediate, advanced, blender-4x

---

## Related Tutorials
No directly related tutorials yet in the library for PBR game-asset texture baking or layered procedural+photo material authoring workflows — flag for cross-linking if another texture-baking, SimpleBake, or game-asset-pipeline tutorial is ingested later.
