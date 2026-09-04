---
title: I Combined 5 HDRIs in Blender
source: YouTube
url: https://www.youtube.com/watch?v=MvJEnsMX4DU
author: roe.num77
ingested: 2026-09-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/i-combined-5-hdris-in-blender/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: [13.2]
---

# I Combined 5 HDRIs in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=MvJEnsMX4DU)
**Author:** roe.num77
**Duration:** 16m8s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- WARNING: Caption cross-check: 1 Whisper span(s) have NO counterpart in YouTube's 153-cue auto-caption track. Whisper fabricates over silence where Google's ASR usually emits nothing, so these are the spans worth listening to first. NOT a verdict — auto-captions have their own errors, and disagreement means 'look here', never 'Whisper is wrong'. Spans: 13.2-27.6s "high- curriculum,拜拜."

---


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py i-combined-5-hdris-in-blender <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] chemistry nodes, BSDF, Vocal, Control 1,
[0:13] high- curriculum,拜拜.
[0:57] Have you ever known that you can combine 5 completely different HDRi's in Belender
[1:04] and make one unique environment?
[1:07] In this tutorial I will show you how to blend all 5 together and have full control over
[1:13] the final look.
[1:14] Let's jump into Belender.
[1:16] So this is the shot that is so special to me and I like it a lot.
[1:20] Before I start making the lighting system, since we are going to replicate this shot,
[1:25] I select the camera and I want to tell you a camera tip.
[1:29] If we head over to the camera panel, here you can see that the camera type is set on
[1:33] panoramic and the panorama type is set on fisheye equi-solid.
[1:39] So if we exit the camera view, this is our lighting system.
[1:47] And you can see that it looks just insane.
[1:51] But inside the camera view it is even more insane.
[1:55] Because of the camera type which is set on panoramic.
[1:58] So let's start making our lighting system.
[2:01] Open a new window here and switch it into shader editor and set it on word.
[2:08] Because this is a brand new scene, it's ok to make a word.
[2:12] Now we have access to the nodes to adjust our lighting system.
[2:15] The next step is to import the HDRi's.
[2:18] So press shift A and search for environment texture and plug it into the background node.
[2:27] Then I click on open and I import an ERS HDRi.
[2:31] This one that I am using is from render crate.
[2:34] It looks pretty cool already but it is definitely too bright.
[2:39] And the colors are washed off a little bit and I need them to pop up a bit more.
[2:46] So to do that on the background node we can decrease the strength.
[2:49] For example from 1 to 0.3.
[2:53] Yeah that is just much better.
[2:55] We got a much better result.
[2:57] Now select the environment texture and press ctrl T to bring up these two.
[3:04] Texture coordinate and mapping node.
[3:06] By the help of them now we can rotate the HDRi.
[3:11] And here is a cool tip.
[3:13] In the final render I have slightly animated the z axis so that the ERS slightly rotates
[3:20] and it looks just insane.
[3:23] So over here if you tweak the z axis you can see what it does.
[3:27] It is just so cool.
[3:30] So for this one I like to keep the rotation on 0 without any change because it already
[3:35] looks pretty cool.
[3:37] Now I select the three of them, press F to set them into a frame and I label it as ERS
[3:43] atmosphere.
[3:46] Then duplicate them and let's add our second HDRi.
[3:56] This one is a Nebula HDRi and it looks just insane.
[4:01] So let's rename the frame to Nebula.
[4:04] Now we duplicate the setup again and add the third HDRi.
[4:11] This one is also a Nebula HDRi.
[4:15] So I rename the frame to Nebula 2.
[4:18] Duplicate the setup again and let's add the fourth HDRi.
[4:31] This is a starry one.
[4:32] It has so many stars.
[4:34] So let's rename it to a star.
[4:38] Let's start combining.
[4:39] So plug the ERS atmosphere into the background node.
[4:43] And I guess we can adjust it a bit.
[4:46] One handy node that always come in handy is the Hue Saturation value.
[4:52] With the Hue property we can tweak the colors.
[4:56] The saturation if increased can make the colors pop more.
[5:01] And value if increased will brighten up the colors.
[5:06] So here is the before and here is the after.
[5:09] I like it more now.
[5:10] It looks more natural.
[5:12] Now there is a very cool trick to tweak the RGB colors separately.
[5:17] And this is so cool.
[5:19] So we press Shift A and search for separate color.
[5:23] Then after that we add the combined color.
[5:28] Here you can see there is red, green and blue.
[5:31] So plug the colors respectively.
[5:34] Then to tweak the values you can introduce a mass node.
[5:39] Switch it into multiply and set the bottom value on 1.
[5:43] And drop it on the red channel.
[5:47] The red channel multiply by a value of 1 means no changes.
[5:51] But if we increase that you can see what it does.
[5:56] Or decrease it.
[5:58] So duplicate the mass node and drop it on the other channels as well.
[6:04] I like to decrease the red and the green channel a bit so that it will be more of a bluish color.
[6:11] So for the red and green channel I set the value on 0.9.
[6:18] Let's take a look before, after.
[6:21] Not that much of a big change but it adds a lot.
[6:25] Let's combine the first two HDRI.
[6:27] So the key node is the mixed color.
[6:30] Drop it on the connection and plug the Nebula into B input.
[6:36] It already looks pretty cool.
[6:39] But I like to adjust the Nebula as well.
[6:42] First let's tweak the rotation of it.
[6:51] So I like to place it like so.
[6:53] Because I do love this part to be kinda in the middle.
[6:57] It looks just insane.
[6:59] Now I introduce a hue saturation to give it some adjustment.
[7:09] So it is much brighter now.
[7:11] Then the same setup.
[7:13] Separate color and the combined color.
[7:18] And here is a very cool trick.
[7:21] On the Nebula I don't really like these red spots.
[7:25] So if I disconnect the red channel, see that.
[7:28] Yeah this feels much better.
[7:30] Then we can introduce the same mass node.
[7:41] Just see now how much more it interacts with the air's atmosphere.
[7:46] It is just much better.
[7:48] Then to combine them better, on the mixed color node there is this factor property.
[7:54] Where by a value of 0 we can only see the first HDRI.
[8:00] And a value of 1 means we can only see the second HDRI.
[8:05] As a default it is set on 0.5.
[8:08] And I guess it is just too much for a second HDRI.
[8:12] So I decrease it a little bit.
[8:14] For example 0.3 maybe could work better.
[8:18] Yeah this is better now.
[8:20] Now it is also much more organic.
[8:23] Now let's bring the third HDRI into the game.
[8:26] So duplicate the mixed color and drop it after the first one.
[8:35] And plug the Nebula 2 into the B input.
[8:40] Let's set the factor on 1 to have a better look at it.
[8:44] For this HDRI because it is a bit different from Nebula 1.
[8:48] We should do a trick so that it can be combined or in another world it can be dissolved into
[8:55] the previous HDRI.
[8:57] So for that we switch the mixed color from mix to lighten.
[9:03] Lighten means remove the black and keep only the white.
[9:07] For example if I switch it into multiply it means remove the white and only keep the
[9:15] black.
[9:16] We should definitely decrease the factor to see less of Nebula 2.
[9:22] So again 0.3 I guess could work just fine.
[9:26] Yeah this is pretty fine.
[9:29] And then I like to give it some rotation adjustment.
[9:36] Then I like to keep the brightest spot over here.
[9:39] Much better and it definitely could use some minor color adjustments.
[9:44] So to have an easier life let's plug it directly into the background note.
[9:49] I like to adjust the colors the way it will be kinda a blueish Nebula.
[9:54] In that case it will interact better with the previous HDRI.
[9:58] So here I introduce a color ramp.
[10:03] And for the white slider I pick a blue tint color.
[10:09] Here is the before and here is the after it is better now.
[10:13] Big difference then why not adding a hue saturation.
[10:24] So here is without Nebula 2 and here is with Nebula 2.
[10:29] It definitely adds a lot.
[10:31] Well this space looks pretty good but something is definitely off and that is the stars.
[10:38] If we take a closer look we can see some stars but we expect to see more while in a space
[10:46] and here comes our stars.
[10:48] And here is a spoiler this will add a lot.
[10:52] So we again add our good friend the mix color.
[10:56] Drop it after the second one and let's place it here.
[10:59] Then plug the stars into B input.
[11:03] Let's set the factor on one to see it better.
[11:06] On this star HDRI we only need the stars meaning only the bright parts.
[11:12] So we again switch the mix color into lighten.
[11:18] And now it is interacting with the previous HDRIs pretty well.
[11:23] Let's again decrease the factor and set it on 0.3 but we cannot see the stars that much
[11:30] now.
[11:32] And here we can introduce another hue saturation where we have the value property and if we
[11:40] increase it significantly we can brighten up the stars significantly just see how cool
[11:47] it looks now.
[11:48] And then I want to adjust the colors a bit more this time.
[11:52] Let's plug it directly into the background node and again we add the same setup.
[11:58] Separate color and combine color.
[12:03] This star HDRI has a small nebula as you can see and I like to tweak the color of it and
[12:10] I just play around with different values.
[12:16] This will now interact much better with previous ones.
[12:23] Now I do like to place this small nebula over here.
[12:28] We can easily achieve that by rotating it.
[12:43] Let's just compare.
[12:45] Here is without it.
[12:49] Here is with it.
[12:50] Big big difference.
[12:52] This is just much better now.
[12:54] So this is actually done but since I promised you to combine 5 HDRIs here I pick a very
[13:02] hard one to combine.
[13:04] You may say this is not good at all but by tweaking it properly we can just dissolve
[13:11] it into the previous HDRIs.
[13:14] And that's a very prominent nebula with so much saturated colors.
[13:19] So let's add another mix color.
[13:24] For this one I switch the mix color into a screen or the light end will also work the
[13:29] same.
[13:30] Then it needs some serious color adjustment.
[13:34] So again like before we just start adjusting it.
[13:37] So first a hue saturation could work just fine.
[13:51] Then a separate color and combined color.
[13:55] Let's take a look at it separately.
[13:58] And for that again I disconnect the red channel.
[14:10] Now you can see that.
[14:12] So here is without it and here is with it.
[14:19] That just adds a lot.
[14:21] Just look at this nebula.
[14:22] Everybody will think this is just one single HDRI.
[14:26] But we have combined 5 different HDRIs and we can tweak them separately and that is just
[14:32] a very powerful system.
[14:35] Now that we are here let me also teach you my old trick for lighting systems.
[14:40] So duplicate the background node and move it down then plug it over here.
[14:46] Add a mix shader and make the connection like so.
[14:51] Then here is the trick.
[14:52] Add a light pass.
[14:57] And on this node plug is camera ray into the factor on the mix shader.
[15:05] Nothing has happened but with this setup now the top background node controls the amount
[15:11] of light emitted from the HDRI.
[15:14] But the HDRI itself doesn't get brighter or darker.
[15:19] And the bottom background node controls the lightness of the HDRI itself.
[15:27] And it doesn't affect the light that is emitted from the HDRI and that is a very powerful
[15:32] trick.
[15:34] Or for example if we add a sky texture and plug it over here you can see that the space
[15:42] station is not being lit up by the HDRI.
[15:46] It is being lit up by the sky texture.
[15:49] Or if we plug it over here our lighting system changes but the lighting is being emitted
[15:57] from the HDRI.
[16:00] I mean these HDRIs.
[16:02] So that was it and I hope you have enjoyed and learned so many things.
[16:06] So see you next time.



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
