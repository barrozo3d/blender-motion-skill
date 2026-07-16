---
title: Doing Surface Imperfections Right | Vray, Cycles, Arnold..
source: YouTube
url: https://www.youtube.com/watch?v=OW4L0vdo_e4
author: Lucas
ingested: 2026-07-16
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/doing-surface-imperfections-right-vray-cycles-arnold/
frame_count: 0
frame_status: pending-selection
---

# Doing Surface Imperfections Right | Vray, Cycles, Arnold..

**Source:** [YouTube](https://www.youtube.com/watch?v=OW4L0vdo_e4)
**Author:** Lucas
**Duration:** 20m53s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py doing-surface-imperfections-right-vray-cycles-arnold <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Alright, with all washed 1000 tutorials, fingerprint stains, variation, it's all roughness, but it isn't.
[0:06] Today we're gonna break habits, we're gonna talk about one of the most under-discussed,
[0:09] there I say unknown aspects of surfacing that mean to introduce to you material layering.


### Identifying the issue with the common workflow [0:19]
**Transcript (timestamped):**
[0:20] Okay, so first thing first, let's do a little run-through of the standard process for surface
[0:25] and perfection. So you take your fingerprint smab, your smudges, your stains, whatever,
[0:30] you just load it, put it through a little bit of a remap, and just plug it inside your roughness
[0:36] lot, and there you go, you have roughness. So I have a reference of fingerprints on to a glass here,
[0:41] and I want you to try to find the issue that we're gonna talk about in this video. There's no trap,
[0:46] just give it a quick thought. Before talking about the solution, let's look at a few other examples.
[0:51] Here we have the car paint example, some car door surfacing this time, and we're gonna see what's
[0:57] wrong with it later. Some mirror references here, I can zoom a little bit, and you can try to find
[1:04] the problem, and last but not least we have a phone screen reference, and maybe you just write,
[1:10] maybe you didn't, in which case it's perfectly fine, but if we take a closer look at our references,
[1:15] we can see that the behavior of fingerprints and imperfections in general is actually much
[1:21] different than what we have in 3D. In 3D, the surface imperfection displaces and distorts the
[1:26] reflection, it blurs it entirely, as you would expect from roughness actually, but we can see that
[1:32] it's not the case in real life. In fact, the fingerprint just comes over the reflection, darkens it,
[1:37] but does not actually blur it in any significant way. On our car material, we can see that there are
[1:43] some stains overlaying on top of the hood, but they're not actually blurring in displacing the
[1:47] cloud reflection behind, unlike we have in our render, as you can see the clouds actually disappear
[1:52] because they get blurred so much that the color becomes the average of the surrounding area.
[1:58] On this car door reference, we can see multiple issues at once. First off, the reflection is too
[2:03] strong, and takes on too much space onto the final image. On top of that, we can't really see any dirt
[2:09] in the core of the reflection here. We can see that our straight edge is distorted, displaced,
[2:14] and mushed by the roughness, and in the darker area, we cannot see any single dirt or particle,
[2:20] except for very very subtle darkening. The example of the mirror is particularly
[2:26] egregious. We can see that we lose all forms, shapes and data in the reflection, and everything gets
[2:31] distorted and lost in the roughness variation. Unlike on our references, where we can clearly see
[2:37] the people's faces behind the surface imperfection, here as well, the person and the light bulbs
[2:43] are perfectly fine apart from very very light and mushy, and here, her hand, her face, everything is
[2:48] completely preserved. Again, for the example of the phone here, we can see that our reflections
[2:54] and all data is lost. We cannot see the SGRI, the light bulb. Everything is lost in the variation
[3:00] of roughness, and like our references, where we can see the reflection of the room is perfectly
[3:05] clear, perfectly sharp, and is actually behind the surface imperfection in the fingerprints.
[3:10] We can clearly see here that the original reflection is completely untouched and preserved
[3:14] even through the surface imperfection. So let's try to understand what the difference is.


### What is Material Layering? [3:16]
**Transcript (timestamped):**
[3:20] Roughness shaders mimic the progressive increase in my cross-cut big disruptions and irregularities
[3:25] on the single surface. Because more disruption means more rogue rays, roughness variation looks
[3:30] like a blur, getting progressively larger and larger like so. Material layering on the other hand
[3:36] emulates how to completely isolated materials, each with their own properties, including unique
[3:41] roughness, blend into each other based on the quantity and thickness of the superior layer.
[3:46] Because you control the presence of a new material with fully isolated roughness,
[3:51] material layering ends up looking like, opacity, and changing the value of A can never
[3:56] look like combining the value of B and C together. And that is the key difference in results,
[4:02] not the identical max values, but all the in-between and how each value difference evolved from
[4:07] the previous one. While roughness variation will progressively make reflections blurrier,
[4:12] the material layering approach will progressively blend two independent results together.
[4:17] And therefore, both the approaches are correct, but only in specific situations that match what
[4:22] can be observed in real life. And our mistake in all of this is attributing more situation than
[4:28] is true to roughness variation, even though a lot of surface imperfections we do on a regular
[4:32] basis actually are fully independent materials overlap. Things like rust, scratches, corrosion
[4:38] and friction actually are variations of a surface's integrity and will be roughness variations.
[4:44] But fingerprints, stains, dust, dirt, or even chemicals are independent elements
[4:50] overlaid onto the object they interact with, and these should be material layering.
[4:55] Now I don't want you to feel like you just clicked a darkwave video,
[4:58] wrecking every rule. These are intentional features, and layering is a standard practice in VFX
[5:03] surfacing or core rendering, and the only reason everyone uses roughness for every situation
[5:08] is only because everybody else online said to use roughness and perfections for everything.
[5:13] And even though there are countless studies all describing these materials are separate layers,
[5:17] papers rendering, dusty surfaces, papers inspiring islands own material layering system,
[5:22] and generally a ton of documentation stating all the way back to gems blin in 1982,
[5:27] acknowledging these behaviors. Okay now that we've talked about that,


### Comparison [5:28]
**Transcript (timestamped):**
[5:31] watch this when I switch from roughness approached to material layering. Then we can see it's
[5:36] exactly what's happening in our references, the parts from the different map of course.
[5:39] We can see the reflection is completely preserved and only gets dimmer in behind the layer
[5:43] of surface imperfection here. We can even see the grain of the fingerprints behave exactly as it
[5:48] does in our reference. Here I can turn around the glass and we can see that it's completely
[5:52] independent from view angle or anything like that. It's just behaving properly because it's the
[5:56] correct physical approach. Everything that's happening in our reference is now happening as well
[6:00] in our 3D render. Alright let's do it again on our car hood. Remember those mushy clouds getting
[6:06] lost behind the surface imperfections? Boom, there you go, they're gone. Exactly as it happens inside
[6:12] our reference, now we can only see the seal width of our stains, there's nothing actually corrupting
[6:17] the reflections behind everything is crystal clear and now you can see that the stains behave
[6:21] properly in all conditions. Now let's take a look again at our corridor. Remember this one had
[6:27] lots of issues, there was too much reflection taking the entire space and corrupting the diffuse
[6:32] color. We cannot see the dirt and the dark areas, we cannot see the dirt on the bright areas and
[6:37] we can see on the straight lines that it's distorting the reflections too. And if we switch to
[6:41] material layering, everything is fixed. There is no more halo overlapping on top of the diffuse area
[6:47] where it's not supposed to reflect much. We can see the dirt and the dark areas, we can see the
[6:52] dirt on the bright areas and the reflections are not distorted and mushed anymore. So as you can see
[6:57] the difference is pretty huge. In the case of a mirror the upgrade is going to be particularly
[7:02] visible. If I switch from roughness variation to material layering, we can see exactly everything
[7:08] that's happening in our references again. The first reflections, perfectly clear, perfectly visible
[7:13] undistorted. The new reflections are showing you up properly, white too, that's an effect we
[7:19] haven't talked about. But fingerprints and oil and different chemicals that you used to clean your
[7:24] mirrors have a distinctive color, so they're not polluted by the original color of the reflection
[7:29] that you could see in roughness variation. And if we turn around we can see some pretty interesting
[7:34] effects. For example here I have a little bit of a light bubble and if I put my references again
[7:38] we can see that every single effect that we can notice on the reference is again transcribed in
[7:42] the other render. And if you're wondering what's happening here with the light bulb being
[7:46] mushed and distorted is that the good thing with material layering is that you can dial the
[7:50] different properties individually. So here I have a little bit of roughness variation that's
[7:54] only affecting the very bright highlights because it's so subtle. So it leaves all the original
[7:59] reflections pretty much untouched even though technically they are different but you just don't
[8:03] notice it because the property is so lightly variating. In the areas of high contrast and in
[8:08] particular areas next to lights now you can see the effects that I've given inside my shader.
[8:14] Another positive byproduct of this method is that now that our surface imperfections are
[8:18] considered as different layers sitting on top of our material is that we can have double reflections
[8:24] exactly how it's happening in real life. And the reason for that is that the surface imperfections
[8:29] are sitting onto the glass and not onto the silver layer. So the layer of surface imperfection
[8:34] is itself getting reflected at the back of the mirror to come back to our eyes.
[8:39] If you check our reference and your own mirror is actually you're always going to have
[8:43] these double reflections everywhere. It's just a very subtle effect that's very interesting
[8:47] to have realism. Okay that's but not least the smartphone example and I mean in body style I think
[8:52] you get the gist of it and you know what's going to happen but I think it's still interesting
[8:56] to see and again all the machine and lust reflections from the first layer are completely restored
[9:01] once you switch to material layering. And in fact you can check that this is true to life on your
[9:06] own smartphone. In fact when I was recording this video I decided to film my phone to show you the
[9:11] reflections and it will work the same on yours and I can turn around in the scene and you can see
[9:15] that it behaves exactly as you'd expect. Getting all those sharp first layer of reflections with
[9:19] a secondary layer of roughness on top of it and as you can see once again because of the material
[9:24] layering approach each material is completely independent and now you can see the diffuse of
[9:29] the first layer and you can also see the diffuse of the second layer so if I put my exposure right
[9:34] here now you can see the same effect as you have on your phone even though I boosted it a little
[9:38] bit here and you can always see a little bit of surface imperfection even when it's not roughness
[9:43] blurring the reflections. All right let's talking more action. Let's see how we can convert a


### Convert RGH Variation to MTL Layering [9:44]
**Transcript (timestamped):**
[9:49] standard shader using the roughness variation into a proper material layering approach.
[9:54] So I have a blank shader connected to a material layer setup with absolutely no layer for now
[9:59] when we're going to create them. The first thing you're going to do is you're going to create the
[10:03] material that corresponds to the layer that you're going to add to your surface so in my case it's
[10:08] going to be dirt and I'm just going to apply it real quick to see what it looks like. Very lightly
[10:13] saturated color something like that that looks good. I'm going to give it some reflection and I'm
[10:18] going to make it extremely rough. Now I'm going to connect it to my first layer and I'm going to
[10:25] apply my material layer. So right now there is absolutely no distribution except for solid color
[10:30] so I can dial in the overall presence of the first layer and I'm not going to touch it for now
[10:34] because it's not going to be used. What we're going to do is that we're simply going to take the
[10:38] map we use to use as a roughness variation we're going to duplicate it and we're going to add a new
[10:43] remap and you can just connect it as your layer distribution and while I you have your material
[10:49] layering setup. Okay let's do the same for our mirror and we're going to convert this into your
[10:55] proper material layer setup. I'm just going to pull up my material here and it's just a multi-material
[11:00] designer to have both the frame and the silver in the same object. I'm going to duplicate it
[11:06] and I'm just going to apply it straight away. The first thing I'm going to do is duplicate my
[11:10] glass and disconnect the roughness variation. Now if I apply it I can see I have a perfectly
[11:16] clean mirror with absolutely no variation whatsoever. I'm going to grab the map I used to use as a
[11:21] roughness variation and it's just a fingerprint texture and before anything else I'm going to create
[11:26] a blend shader which is going to be able to add multiple layers and materials together. I'm going
[11:31] to plug my glass as the base material and there we go I have a blend shader. Now what we are missing
[11:38] right now is the grease material so let's make that. I'm going to apply it instead of my glass just
[11:43] to see it real quick. So let's make some really quick grease it's going to be reflective. I'm going
[11:48] to make the diffuse color a little bit brighter and I'm going to make it refractive but not completely
[11:53] refractive because I want to see a little bit of white color inside of it. I'm going to reduce the
[11:58] reflection clarity just a little bit and now we have what we'll call a grease material. I'm going
[12:05] to plug my mirror layer back and I'm going to plug my grease inside the first layer of my material
[12:10] layer setup. Now we have an in between of the two and that's not really what we want. So I'm going to
[12:16] come back to my fingerprint texture. I could use it just like that and have an effect but in my case
[12:21] I'm going to make it a little bit more contrasty and a little bit stronger in the highlights so I'm
[12:25] going to add a remap node and remap my fingerprints. What I want to do with this is I'm going to
[12:31] make the highlights a little bit stronger and I'm going to increase the contrast not to have
[12:35] fingerprints everywhere and there we have it. The fingerprint material layer setup with every effect
[12:40] that we saw on the reference. We can see that we have some of the fingerprints visible on top of
[12:45] the first reflections. We can see a little bit of their diffuse color and some of the stronger
[12:50] fingerprints on the highlights are distorting the reflections and the reason for that is that when
[12:56] you have a 100% present material layer you will naturally see the full effect of that second layer
[13:02] as if the first base material does not exist anymore. So in my fingerprints as you can see a little
[13:08] bit of white in here I have some areas where the finger grease is at full presence and completely
[13:14] takes over the mirror reflection and now we successfully converted our roughness variation mirror
[13:20] into a material layering mirror. Okay so last but not least let's convert this smartphone screen
[13:26] just putting up my material again as you can see it's just a little bit of a fingerprint
[13:31] texture getting remapped and fed inside roughness lot. I already have my material layer setup so
[13:37] nothing crazy it's just a clean screen and a grease material. So what I'm going to do is take my
[13:43] fingerprint texture put inside a remap and plug it inside my layer one distribution.
[13:52] In the case of a smartphone what I'm also going to do is add the texture inside the
[13:56] anisotropy to account for all the millions of little tricks created by the fingerprint texture on
[14:02] your fingers that create directional tricks on the smudges and in turn that creates an anisotropy
[14:08] reflection. So I'm just going to take my texture plug it inside my anisotropy rotation and for
[14:13] the purpose of this demonstration call it a day. Add a remap node just to control the direction
[14:18] a little bit unlimited so that it's not too extreme and I'm going to add a little bit of contrast
[14:24] onto my distribution and there we go we have successfully converted our phone screen from
[14:28] roughness variation to material layering. Now if I turn around we can see all the effects that we
[14:34] can see in real life on phone screens. So we've talked about which method best suits which cases


### When to use which? [14:37]
**Transcript (timestamped):**
[14:41] but let's clarify for good measure. Roughness variation will be best suited for situations where
[14:46] the integrity of the actual surface the material is applied to varies from one spot to another.
[14:51] Actual distress modifying how even the surface is. Material layering however will be best suited
[14:57] for situations where an external material element or particle scatter is sitting onto that
[15:02] previous surface and both materials will now be active at the same time. Next time you find an
[15:08] imperfection you've never done before just look around to find whether it is single surface distress
[15:13] or multi material layering in real life. Okay so I have a little bit of a disclaimer here


### Disclaimer [15:16]
**Transcript (timestamped):**
[15:18] especially to the potential students listening to this. Roughness is amazing don't ditch it
[15:24] don't go for material layering by default actually try to do it roughness first and if you see
[15:31] that the results you get are too far from the reference then you can start considering
[15:36] layering but only if you're absolutely sure because it comes at a render cost. Now I have this
[15:42] example of a laptop and what you'll notice is that the roughness approach here is technically
[15:48] physically wrong but it would be perfectly fine if you had to recreate this laptop use roughness
[15:55] and get this result and publish this in production. Roughness is not absolute it's not going to make
[16:00] your renders unfutter realistic and the point of this tutorial is mainly talking about very short
[16:06] reflections that you can actually see gets smudged when using roughness. In the case of very soft and
[16:12] dull reflections like this laptop roughness is fine. Now I can rotate around you might start seeing
[16:18] the limitations of roughness that we've seen before and here is just this reflection on the right
[16:23] being smudged so much it reaches huge distances from the spectacular highlight and it gets brighter
[16:29] than the rest of the reflection behind but it looks a little bit white but in most angles it works
[16:35] absolutely fine look at this I mean you would never be able to tell there's a physical issue
[16:40] with this approach so here I have a side by side of roughness versus layering and rest assured no
[16:45] one but you would be able to tell the difference it's pretty much indifferential.


### Substance Conversion [16:50]
**Transcript (timestamped):**
[16:51] So if you use substance bearing to rely on and you're wondering how you would go about using this
[16:57] workflow instead you would typically have your object where they differ in material that is
[17:01] contaminating some of the different channels such as roughness or diffuse and the standard
[17:07] practice would be to export everything together with no strings attached and the conversion to a
[17:12] material layering workflow is actually very simple um instead of having the material baked in your
[17:17] original export and contributing to the diffuse color the roughness the height and whichever
[17:22] all the channel you want you would disable everything and what you would do instead is you would
[17:27] create a new channel a new user channel you could call it for example dirt and what you would do
[17:33] is you would make your original layer contribute to this user channel instead of every other channel
[17:39] then you just go to export textures and inside your template you just add a new gray output map
[17:45] and you would plug a user zero just call it dirt and there you go you have a material layering
[17:51] friendly approach workflow and export setup but that gives you is a nice related export of the
[17:56] dirt masks that you can then use as a distribution map for your dirt layer let's take a look at the


### Render cost [18:02]
**Transcript (timestamped):**
[18:04] render cost of the material layering approach i run a few tests on the examples you saw in this video
[18:10] and out of 13 different tests material layering is faster in seven of them what i found is
[18:16] material layering can be slower in some cases that are so different in look and so much closer to
[18:22] reference you don't really have a choice but to do it that way roughness variation is clearly not
[18:27] the solution for smartphone reflections so you can have to do material layering either way in those
[18:33] cases i saw both an aposent slowdown and a 42% speed up in some other cases like the laptop again
[18:41] depending on the angle the speed difference changes quite a lot when we orient ourselves towards
[18:46] the light similarly to the smartphone test we can see that material layering ends up being quite
[18:51] faster however in angles that don't reflect much light material layering can tend to be a little
[18:56] bit slower but it's not that much in one situation i had they both were identical and one thing
[19:02] that's pretty interesting is that my table renders were actually a lot faster using material layering
[19:07] noticing an insignificant slowdown on one angle but one of them in the mix of both light and
[19:13] darkness was 26% faster and a pretty huge 80% faster render in the angle oriented towards the light
[19:20] but one thing you have to understand about material layering is that it is a lot slower when
[19:25] refraction is in the equation but considering the same lights and contents being reflected and
[19:30] refracted i assume that these slowdowns in refraction situations would be quite dependent on the
[19:36] render range i knew used and a suspect if you raise approach to material layering is mostly
[19:41] responsible for these two huge slowdowns because another situation using refraction was actually a
[19:46] 60% faster and another one as well on the mirror was 6% faster and so these variations in speedups
[19:54] and slowdowns show us two things first off that material layering is highly fluctuating so you
[19:59] must run the test on your own on one frame to decide your approach beforehand and the second
[20:04] thing is that in some cases the visual difference is so huge that the render costs might be a little
[20:10] bit slower but hugely worth it when it comes to visuals obviously these are only 13 tests
[20:16] dependent on my render engine and my situations you will definitely run into different numbers
[20:22] so i highly suggest running your own tests on your own projects to see for yourself


### Conclusion [20:27]
**Transcript (timestamped):**
[20:27] and this is it we've seen what is material layering how is it done why does it exist and even
[20:33] how to convert your current setups to material layering i hope you've learned something do let me
[20:38] know if you have any thoughts or remarks in the comments and on that note i'll see you next time
[20:46] man you'll never learn the sound like you'll never man



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
