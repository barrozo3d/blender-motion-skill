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
**Transcript:** Kind: captions Language: en Now, you might think a complex object like this, you'd need to unwrap it very carefully. And if you were to change this in any way, you'd have to reunwrap it and map it to these textures. However, if I edit this shape, the textures just work with the object. And no matter how much I change it, the textures adapt and still work without any problems. And it's a surprisingly easy technique. And in this video, I'm going to take you through it. So, I'm in a new startup file and I'll start by creating the shape so you know exactly how I went about that. If you want to skip this chapter, then jump to the next where I do the texturing. So, I'll start by deleting the default cube and then shift A to add to the mesh menu and I'll choose a cylinder because we can create something a bit more interesting out of that. I'll scale it in the Z axis so it starts off all thin like this. And let's create an interesting shape. So, I'll tab into edit mode. Select the top face. So, three to go to face mode. Select that top face. I to insert, E to extrude, bring that out. I to insert, E to extrude, and bring that down like so. So, I've got this simple shape like this. I'll add a subdivision surface modifier to it. So, across to the modifiers, add modifier, type in sub, and there's the subdivision surface modifier there. I'll add that. Use three levels. Same with my render in case I want to render it out. And we got this sort of blobby looking shape at the moment. I can sharpen this up by adding some bevels on the edges. So, two to go to edge mode. Alt left click on an edge and shift alt left click to select several like this. Try and get that middle one in there. I'll turn on on cage so I can actually see it. That one there is what I'm trying to get. And this one in the middle here. So, got all the edges and I want to bevel them. So, controlB to bevel. The problem is the bevel might act a little bit unusual. I'll just undo that and turn off the on cage so you can see how the bevel's acting unusually. So, control B to bevel. It's going one way more than the other. And if I add some loops to it, you can see that more clearly when I do that. That's using the wheel of my mouse. So I'll press escape and I'll go back to object mode. What's going on here is if I press N on my keyboard, go up to item, the scale is non-uniform and the bevel is taking that into account. If I now press Ctrl+ A, make sure you do this in object mode, not edit mode, I can apply the scale. That's the same if I go to the object menu up here, apply, and then scale. And you can see now my scales all set to one. When I go back into edit mode now with those edges selected, controlB to bevel. Move my mouse to the side. Use the wheel of my mouse to create another cut and left click. And I've now sharpened everything up. And that's looking pretty good. Let's go back into object mode. And we've got our weird looking shape. So you might want to pause the video here. Catch up with me if you're following along. Okay, so how do I do the shading? Well, let's go to the shading workspace. I'll just zoom into my object with period key to frame selected. And then I'm going to add a new material. I'm going to use the node wrangler to bring in a PBR material. Those are materials that have the color, the roughness, metallic, and normals. So, you'll need to have the node wrangler add-on enabled. It's much easier if you do it with the node wrangler. So, we go up to edit preferences. Under add-ons, just type in node. And there's the node wrangler there. Just make sure that's ticked. You can then close down your preferences. And now I'll zoom out of my shader editor slightly. With the principled BSDF selected here, you can hold down control, shift, and then press T. And then you can bring in your PBR material and it will set it all up for you. Now the material I'm going to use in this case is the worn rusted painted PBR material. This is from free PBR.com and you can download this for free if you click on the worn rusted painted.bl.zip just here for Blender. And you just need to unzip it. So back into Blender, I'm going to find that texture. So I'll type in worn. And there is worn rusted painted. If I open that up, you can see there's my PBR textures. There's the preview of what it will look like. I can actually just select all of these with A. So that's selected every texture and then click on the principled texture setup. And you'll notice it's set them all up. And it's almost correct in there. But you can see them all set up here. What it's doing at the moment is using the UVs and we haven't unwrapped this. So we need to set the texture coordinates so they are using a different texturing method. So if I zoom in again under the mapping node, we change it to object. that will give you the most accurate representation on your object. The only problem is it's projecting straight down from the top. So, we're getting this stretched texture on the side. It's working from the top, though. So, all we need to do is zoom out a bit and make sure all of these are selected. So, select all of these and then I can zoom into one. And where it says flat just here, if I hover over that, you can see this is the projection method. If I alt leftclick on this and change it to box, you can see that it projects it from all different sides, which is called box projection. And you can also see because I held down alt, it's changed every one that was selected. Now, you might notice if I zoom in a bit, can we see it? Yes, there's a line down there. You can just about see it. That's where the two projections meet. So, it's projecting from all the different sides of a box. So, front, side, top, bottom, and so forth. And you do sometimes get a line where they cross over just there. And we should be able to see this on the outside as well. It's quite hard to see really with this texture. It's quite a good one. But we can see the lines when we move around. Not particularly easy. But if we concentrate on this particular line here, hopefully you can see that one. If I now again hold down alt whilst clicking and dragging on the blend just here. So hold down alt, left click and drag on the blend. See what happens to that line as I pull it backwards and forwards. You can see it is blending into each other. So we can box project and blend it together so it looks really seamless and we didn't even have to unwrap it. So that's using the object mapping with the box projection and turning up the blend slightly. And now if I go back into edit mode and let's say do a loop cut in here for example. Select these faces. I to insert E to extrude. E to extrude again. You can see the texture is mapping to it really nicely. No need to unwrap. And we can create all sorts of interesting, wonderful shapes with this technique. And as you can see there, it's working really well. I'll just right click and shade smooth so it works even better. So there we have it. That is box projection. And it's a really nice quick simple way to add textures to your objects without needing to unwrap. Now, yes, there are limitations to this. If you want to export this to a game engine or something like that, you will need to unwrap and bake out the textures. So it does in a sense have its limitations. Although with this technique, you can build your object, see exactly what it's going to look like, and then unwrap and then bake this result onto that unwrap. So hopefully you'll find this useful. As always, if you've got any questions, then do comment below. If you like this sort of content and this kind of teaching style, then do check out my Blender skill builder course. It's currently only $10 as an early bird discount, and it's packed full of modeling challenges so you can increase your modeling skills in Blender. To get your discount, use the coupon link in the description. Thanks for watching and I'll see you next



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
