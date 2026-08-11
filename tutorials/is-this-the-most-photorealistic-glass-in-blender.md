---
title: Is This the Most Photorealistic Glass in Blender?
source: YouTube
url: https://www.youtube.com/watch?v=c95-5gg3kOs
author: Blender Wizard
ingested: 2026-08-10
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/is-this-the-most-photorealistic-glass-in-blender/
frame_count: 0
frame_status: pending-selection
---

# Is This the Most Photorealistic Glass in Blender?

**Source:** [YouTube](https://www.youtube.com/watch?v=c95-5gg3kOs)
**Author:** Blender Wizard
**Duration:** 14m18s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py is-this-the-most-photorealistic-glass-in-blender <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Most artists struggle with creating photorealistic glass, but by the end of this video, you'll know exactly how to create glass just like this in Blender.
[0:09] Make sure you download the project file from my gumroad. Link in the description.
[0:13] Alright, we mustn't wait any longer. Let's dig in.
[0:16] Okay, so turn the color value up to 1, and you want to turn the transmission up to 1, and the roughness down.
[0:26] But not all the way, just barely.
[0:29] Okay, next you want to turn the thin film thickness up to 65 mm.
[0:35] And you want to bring the clear coat strength up to 1, and the roughness to 0.25.
[0:42] And you want to bring the tint up a little bit in the green area, but it is very sensitive, so keep it at a low value like 0.005 for the saturation.
[0:55] Now come over here. If you will notice just how perfect that refraction is, it is so smooth. This is like water.
[1:03] So we're going to want to break that up with a little bit of noise over here.
[1:06] So get two noise textures, as shown here, and change the scale to 2, and the distortion to 0.5.
[1:15] For the bottom noise texture, change the scale to 3, and the distortion also to 0.5.
[1:21] So now you want to mix the two together, and set the blending mode to Add.
[1:27] Now add a bump node. Plug that into the normal. Plug the mixed color into the height of the bump map.
[1:35] Also plug the bump map into the clear coat normal as well.
[1:38] Next, change the distance to 0.005, and the strength to 0.5.
[1:44] And already you will notice just how natural that looks, hey? So much more realistic.
[1:51] Next, you want to add your mapping and texture coordinates.
[1:55] And you want to plug the normal of the texture coordinate into the vector of the mapping node.
[2:00] And make sure the mapping node is only plugged into the top noise texture.
[2:05] But look at this. You'll notice the noise is now following the geometry of the mesh.
[2:12] Okay, cool. Now we want another noise texture.
[2:16] Duplicate the mapping node, and plug that into the noise texture.
[2:21] Then get the generated of the texture coordinate, and plug that into the mapping node.
[2:25] Turn the scale of the noise texture to 4, and the distortion to 0.5.
[2:30] And on the mapping node, change the scale of the Z to 45.
[2:33] Now mix your new noise texture with the ones that you already created.
[2:38] Change the blend mode to add, and turn the factor down to something really low like 0.005.
[2:46] That way you'll get this really subtle effect of metal being pressed against the glass,
[2:53] just to try and shape it. You know, it's microscopic detail, but boy does it ever look fantastic.
[3:00] I mean, golly. So tasty.
[3:03] That was weird. Back to business.
[3:05] So add two noise textures, and change the scale of the first one to 75.
[3:12] Make the distortion 0.15, and for the second one, make the scale 30.
[3:21] Make the roughness 0.75, and the distortion to 0.65.
[3:27] Mix the two together, and change the blend mode to multiply.
[3:32] Duplicate the bottom noise texture, and change it from FBM to heterotrain.
[3:37] Next you're gonna want to turn up that scale up to 90.
[3:40] Turn the detail to 0.2, and the distortion to 0.45.
[3:46] Then add your mix node, and change the blend mode to multiply.
[3:51] Now add a gradient texture, and drag out that little noodle from the gradient texture, and add a mapping node.
[3:58] Great. Now take the generated coordinates and plug that into the mapping node.
[4:02] Turn the rotation to 90 degrees on the Y axis.
[4:06] Now add a color ramp in front of your gradient texture.
[4:10] Then flip the colors just like this.
[4:13] Bring that guy down a little bit. There you go, buddy.
[4:15] Now mix the color ramp with your multiply node you just made, and change the blend mode, LZO to multiply.
[4:21] Now mix your add color node with the multiply color node, and set this one to add as well,
[4:26] and make this a very low number like 0.05.
[4:29] Now the bottom of the glass looks all rough and bump-like.
[4:33] Look at that refraction.
[4:35] I could scream right now, but it's 3 AM, so I won't.
[4:38] Now I'm gonna do some efficient noodle managing that does fuck all, except for waste time.
[4:43] Perfect. Nonsense complete.
[4:46] Now we're gonna put these all in a little group, and rename it to refraction.
[4:51] Now it's time to do the caustics over here.
[4:54] Oh man, get ready. This is gonna be a good one.
[4:57] So let's scoot this over here, just make some room.
[5:00] Add a principal BSDF, turn on the thin wall, turn the roughness all the way down,
[5:06] turn the base color value up to 1, and the transmission to 1.
[5:10] Then add a mix shader between the two principal BSDFs.
[5:13] You can already see. Oh, look at that. A little light is shining through.
[5:18] But we want to get a light path node and plug its shadow ray into the factor of the mix shader.
[5:25] Next, we are going to add a geometry input node, and drag out from the pointiness, and add a color ramp.
[5:32] And just play with the values a little bit.
[5:36] Add another color ramp on top of that, flip the colors and adjust the values, and make the black a medium gray.
[5:43] And make sure pointiness is plugged into both color ramps.
[5:46] Mix them together, and set the blending mode to multiply.
[5:49] Add an invert color node, and plug the multiply into the color.
[5:54] Also, make sure you flip the noodles for the principal BSDFs, so that your glass and your caustics can render properly.
[6:03] Now plug the invert color into the base color of the principal BSDF.
[6:07] Go ahead and preview that multiply node so you see what's going on here.
[6:11] And adjust the colors until you see white on all of the edges of the mesh.
[6:18] That's what you see me trying to figure out right here.
[6:21] It's a little bit tricky, but you'll get it.
[6:24] I know you will.
[6:25] But we're basically trying to tell blender where to let light in, and where to keep shadows.
[6:34] Right?
[6:35] So, you know, when you get it all figured out, this is what you want it to look like.
[6:40] You got all the edges all nice and bright, where as it gets to more of the flat solid parts of the glass,
[6:47] it just gets a little bit, a little bit dimmer.
[6:51] So, you can now see the shadow of the glass, but you want to make the white value of the color ramps set to 2.
[6:59] That way, we're letting the most amount of light through.
[7:03] Right?
[7:03] So, we're just going to preview the entire material now.
[7:06] Look at those caustics.
[7:08] And now we're going to add a noise texture.
[7:11] And we're going to plug the normal of that geometry noodle right into that noise.
[7:15] Then you're going to set the scale to 6.9.
[7:19] That's right.
[7:20] Next, the roughness to 0.75.
[7:26] And duplicate the noise texture.
[7:29] Set the scale to 10 and mix them together.
[7:33] Change the factor to 0.65.
[7:35] Drag out from that little noodle and add a color ramp.
[7:40] Don't worry about the values right now.
[7:42] Just mix it with your multiply node and change the color to darken.
[7:46] And change the factor to 0.35.
[7:50] Now, you can worry about the values of the color ramp.
[7:54] So, turn one value down to about 0.75 and adjust it until it looks something like this.
[8:03] So, now preview your glass material and look at those caustics.
[8:08] Don't you just want to eat that?
[8:10] Next, we're just going to group all of these nodes together and rename them to...
[8:15] You guessed it, caustics.
[8:19] Next, add another geometry node.
[8:21] Drag out from the pointiness and add a color ramp.
[8:24] Then duplicate that color ramp and plug the pointiness into the factor.
[8:28] And you want to play with the values until you get the same effect that you got with your caustics mask.
[8:32] So, use both color ramps to make sure you're highlighting every edge.
[8:36] Once you have that, mix them together and set the blending mode to add.
[8:39] And you'll notice it's not showing up on the top edge, so just adjust it.
[8:43] And make sure it shows up around the glass a little bit as well.
[8:47] Because you still want to see the scratches across the entire thing, not just the edges.
[8:52] Next, get two image textures and I'll put a link to where you can find these down in the description.
[8:57] It'll be over on SketchUp and you can just search up Scratched Metal.
[9:00] Okay, so let's drag these right over here.
[9:03] Mix these two together and set the blend mode to add.
[9:08] And the model is UV unwrapped, so it should look good just straight out of the box.
[9:12] Next, you want to add a mapping node, duplicate it, and plug it into both of the image textures.
[9:18] Okay, now you want to add a texture coordinate and put the UV into the vector of the mapping node.
[9:25] Then you want to set the scale for the top mapping node to 0.25.
[9:30] Set the bottom one to 0.35.
[9:32] Next, change the type from point to texture for both mapping nodes.
[9:37] And duplicate this color ramp and plug it in here.
[9:40] Make sure the color space for the image textures are set to sRGB.
[9:44] Otherwise, the contrast will be way blown out and you won't be able to see the texture.
[9:48] Then adjust the color ramp so you get some black showing, but mostly dark gray.
[9:53] You'll see that these scratches are kind of on an angle and I want them to be facing straight up.
[9:58] So I'm just going to rotate this texture until it looks like the scratches are pointing straight up.
[10:05] Okay, so now I'm going to just adjust the contrast of these scratches so I can retain the most amount of the texture
[10:12] while still being able to let some of the actual glass show through.
[10:16] So now you want to mix both of these masks together and set the blemote to overlay.
[10:21] So now you can see that all of the scratches are on the edge of the mesh here.
[10:25] And I'm going to adjust my bottom color ramp so then you can see the scratches on the entire mesh.
[10:31] Look at that, look at how crunchy that looks.
[10:33] Oh my God, it's so good.
[10:35] And you can see the map working on the inside of the mesh here.
[10:38] Look at that.
[10:39] Oh my goodness, wow.
[10:41] I'm going to freak out.
[10:42] Anyways, adjust the values until they look something like this.
[10:47] Next, add an invert color node and put it in front of the overlay node.
[10:51] Make sure you plug that noodle into the color.
[10:53] Next, add a translucent BSDF and a metallic BSDF.
[10:59] Turn the roughness node to 0.45 and turn the base color and edge tint to a value of 1 and the saturation all the way down.
[11:09] Now create an add shader and plug both the metallic and translucent into it.
[11:14] Also make sure the translucent color value is also at 1.
[11:17] Now mix these shaders with your glass and caustics material and plug your scratches mask into the factor of the mixed shader and plug it into the material output.
[11:26] Now, if necessary, you can adjust the color ramp strength of your scratch material.
[11:32] And for the sake of this tutorial, you want to make sure the scratches cover the edges and around the glass.
[11:38] But this is personal preference.
[11:40] You can decide to do anything you want.
[11:43] Once you've achieved your desired effect, go ahead and select all of these nodes and join them together.
[11:50] Rename this Scratches.
[11:53] Now this looks pretty good, but you're not done yet.
[11:57] Add an image texture and open up a Fingerprints Texture Mask.
[12:02] You should have one in the project file, but you can use your own.
[12:05] Add a color ramp.
[12:07] Move this over a little bit and plug the value into the roughness of the clear coat, the roughness of the principal BSDF and the metallic.
[12:18] Now you get fingerprints and smudges all over your glass.
[12:22] You can adjust the color ramp slightly to get a stronger effect or a more subtle effect.
[12:28] You may notice the smudges are really big, so change the scale of the mapping node to around 4.
[12:35] But if you have the project file, I've already scaled it up, so you won't have to worry about that.
[12:40] But that already looks so much better.
[12:42] You can tell somebody's grimy little paws were all over this thing.
[12:46] You get to preview the entire shader and review your work, but stick around because this next tip is absolutely crucial and will make or break your realism.
[12:57] Go into your glass shader and turn the Anisotropy all the way up and the Anisotropy rotation to 0.25.
[13:05] Then add a tangent node and plug that into the tangent and switch it from Radial to UV Map and select the UV Map.
[13:14] This tells Blender, hey, these smudges are actually streaks and you can see how the light is following those thumb prints.
[13:21] And this is much more realistic than just slapping a roughness texture on there and calling it a day.
[13:28] Look at your phone right now. You'll probably notice smudges that react in this exact way.
[13:33] Bravo!
[13:34] Pat yourself on the back.
[13:35] Today you learned how to create photo-realistic glass in Blender that gives results like this with only two spotlights.
[13:43] Yeah, yeah, you might be thinking, oh, that's an HDRI, but no, this scene is completely dark except for two spotlights.
[13:50] Look at that. So freaking wondrous, isn't it?
[13:54] Subscribe and turn on post notifications so that you do not miss an upload of mine.
[13:58] I also had Ryomon suggest that I do a transparent plastic material as well, so be on the lookout for that and feel free to suggest any material that you'd like to see me try.
[14:08] And I'll feature your idea in my next upload.
[14:10] Enjoy this glass spinning for a little bit longer, okay? It took a long time to render this.
[14:14] Okay, bye.



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
