---
title: The Easiest Way to Texture in Blender (Adaptive, No UV Unwrapping)
source: YouTube
url: https://www.youtube.com/watch?v=AMnMbxEwa7Q
author: Grant Abbitt (Gabbitt)
ingested: 2026-07-18
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/the-easiest-way-to-texture-in-blender-adaptive-no-uv-unwrapping/
frame_count: 0
frame_status: pending-selection
---

# The Easiest Way to Texture in Blender (Adaptive, No UV Unwrapping)

**Source:** [YouTube](https://www.youtube.com/watch?v=AMnMbxEwa7Q)
**Author:** Grant Abbitt (Gabbitt)
**Duration:** 6m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py the-easiest-way-to-texture-in-blender-adaptive-no-uv-unwrapping <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Now you might think a complex object like this you'd need to unwrap it very carefully
[0:04] and if you were to change this in any way you'd have to re-unwrap it and map it to these textures.
[0:09] However, if I edit this shape, the textures just work with the object.
[0:15] And no matter how much I change it, the textures adapt and still work without any problems.
[0:20] And it's a surprisingly easy technique.
[0:22] And in this video, I'm going to take you through it.
[0:25] So I'm in a new startup file and I'll start by creating the shape so you know exactly
[0:29] how I went about that.
[0:31] If you want to skip this chapter then jump to the next where I do the texturing.
[0:34] So I'll start by deleting the default cube and then shift data add to the mesh menu and
[0:39] I'll choose a cylinder because we can create something a bit more interesting out of that.
[0:43] I'll scale it in the Z axis.
[0:44] It starts off all thin like this and let's create an interesting shape so I'll tab into edit
[0:49] mode, select the top face so 3d good face mode, select that top face, I to insert, e to
[0:54] extrude, bring it out, I to insert, e to extrude and bring that down like so.
[0:59] So I've got this simple shape like this.
[1:01] I'll add a subdivision surface modifier to it so across to the modifiers add modifier,
[1:05] type in sub and there's the subdivision surface modifier there.
[1:08] I'll add that, use three levels, same in my rendering case I want to render it out and
[1:13] we've got this sort of blobby looking shape at the moment.
[1:15] I can sharpen this up by adding some bevels on the edges so to go to edge mode, alt left
[1:21] click on an edge and shift alt left click to select several like this.
[1:25] I'll try to get that middle one in there, I'll turn on on cage so I can actually see
[1:29] that one there is what I'm trying to get and this one in the middle here.
[1:32] So I've got all the edges and I want to bevel them.
[1:34] So control be to bevel, the problem is the bevel might act a little bit unusual.
[1:38] I'll just undo that and turn off the on cage so you can see how the bevels act unusually
[1:44] so control be to bevel.
[1:45] It's going one way more than the other and if I add some loops to it you can see that
[1:49] more clearly when I do that.
[1:51] That's using the wheel of my mouse.
[1:52] So I'll press escape and I'll go back to object mode.
[1:54] What's going on here is if I press N on my keyboard, go up to item, the scale is non-uniform
[1:59] and the bevel is taking that into account.
[2:01] If I now press control A, make sure you do this in object mode, not edit mode, I can apply
[2:07] the scale.
[2:08] That's the same if I go to the object menu up here, apply and then scale.
[2:11] And you can see now my scale is all set to one.
[2:14] When I go back into edit mode now, with those edges selected, control be to bevel, move
[2:18] my mouse to the side, use the wheel of my mouse to create another cut and left click and
[2:23] I've now sharpened everything up and that's looking pretty good.
[2:25] Let's go back into object mode and we've got our weird looking shape.
[2:28] You might want to pause the video here, catch up with me if you're following along.
[2:32] Okay, so how do I do the shading?
[2:34] Well, let's go to the shading workspace.
[2:36] I'll just zoom into my object with period key to frame selected and then I'm going to add
[2:40] a new material.
[2:41] I'm going to use the node Wrangler to bring in a PBR material.
[2:45] Those are materials that have the color, the roughness, metallic and normals.
[2:48] So you'll need to have the node Wrangler add on enabled.
[2:51] It's much easier if you do it with the node Wrangler.
[2:53] So we'll go up to edit preferences under add-ons, just type in node and there's the node Wrangler
[2:58] there.
[2:59] Just make sure that's ticked.
[3:00] You can then close down your preferences and now I'll zoom out of my shader editor slightly.
[3:04] With the principal BSDF selected here, you can hold down control, shift and then press
[3:09] T and then you can bring in your PBR material and it will set it all up for you.
[3:13] Now the material I'm going to use in this case is the worn, rusted, painted PBR material.
[3:19] This is from freepbr.com and you can download this for free if you click on the worn rusted
[3:24] painted dot BL dot zip just here for Blender and you just need to unzip it.
[3:28] So back into Blender, I'm going to find that texture.
[3:32] So I'll type in worn and there is worn rusted painted.
[3:35] If I open that up, you can see there's my PBR textures.
[3:38] There's the preview of what it will look like.
[3:40] I can actually just select all of these with A, so that's selected every texture and then
[3:44] click on the principal texture setup and you'll notice it's set them all up and it's
[3:49] almost correct in there but you can see them all set up here.
[3:52] What it's doing at the moment is using the UVs and we haven't unwrap this so we need
[3:56] to set the texture coordinates so they are using a different texturing method.
[4:01] So if I zoom in again under the mapping node we change it to object.
[4:05] That will give you the most accurate representation on your object.
[4:08] The only problem is it's projecting straight down from the top so we're getting this stretched
[4:13] texture on the side.
[4:14] It's working from the top though.
[4:15] So all we need to do is zoom out a bit and make sure all of these are selected.
[4:19] See select all of these and then I can zoom into one and where it says flat just here,
[4:24] if I hover over that you can see this is the projection method.
[4:27] If I alt left click on this and change it to box you can see that it projects it from
[4:33] all different sides which is called box projection and you can also see because I held down
[4:37] alt it's changed everyone that was selected.
[4:40] Now you might notice if I zoom in a bit can we see it?
[4:43] Yes there's a line down there you can just about see it that's where the two projections
[4:47] meet so it's projecting from all the different sides of a box so front side, top, bottom
[4:53] and so forth and you do sometimes get a line where they cross over just there and we should
[4:58] be able to see this on the outside as well.
[4:59] It's quite hard to see really with this texture it's quite a good one but we can see the lines
[5:03] when we move around not particularly easy but if we concentrate on this particular line
[5:08] here hopefully you can see that one.
[5:10] If I now again hold down alt whilst clicking and dragging on the blend just here so hold down
[5:14] alt left click and drag on the blend see what happens to that line as I pull it backwards
[5:19] and forwards you can see it is blending into each other so we can box project and blend
[5:23] it together so it looks really seamless and we didn't even have to unwrap it so that's
[5:28] using the object mapping with the box projection and turning up the blend slightly and now
[5:34] if I go back into edit mode and let's say do a loop cut in here for example select these
[5:39] faces eye to inset, e to extrude, e to extrude again you can see the texture is mapping to
[5:46] it really nicely no need to unwrap and we can create all sorts of interesting wonderful
[5:51] shapes with this technique and as you can see there it's working really well I'll just
[5:55] right click and shade smooth so it works even better.
[5:58] So there we have it that is box projection and it's a really nice quick simple way to add
[6:03] textures to your objects without needing to unwrap.
[6:06] Now yes there are limitations to this if you want to export this to a game engine or
[6:10] something like that you will need to unwrap and bake out the textures so it does in a
[6:14] sense have its limitations although with this technique you can build your object see exactly
[6:18] what it's going to look like and then unwrap and then bake this result onto that unwrap.
[6:24] So hopefully you'll find this useful as always if you've got any questions then do comment
[6:27] below if you like this sort of content and this kind of teaching style then do check out
[6:31] my blender skill builder course it's currently only $10 as an early bird discount and it's
[6:36] packed full of modeling challenges so you can increase your modeling skills in blender
[6:40] to get your discount use the coupon link in the description.
[6:43] Thanks for watching and I'll see you next time.



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
