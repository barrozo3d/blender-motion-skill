---
title: How to Use Blender Emission Shaders Correctly
source: YouTube
url: https://www.youtube.com/watch?v=x1IpbtQ_jO8
author: Blender Wizard
ingested: 2026-08-10
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-use-blender-emission-shaders-correctly/
frame_count: 0
frame_status: pending-selection
---

# How to Use Blender Emission Shaders Correctly

**Source:** [YouTube](https://www.youtube.com/watch?v=x1IpbtQ_jO8)
**Author:** Blender Wizard
**Duration:** 7m52s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-to-use-blender-emission-shaders-correctly <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So you only have a mission, and that's it, that's it, that's all you put on there.
[0:05] And look at the results. That is a flat neon white and there is nothing warm or cozy about that.
[0:14] And look at this lampshade. Concrete has an easier time letting light pass through than this cylinder
[0:20] of solid madness. So let me share with you some of my secret sauce to make these lights
[0:29] go from bland solid ugly colors to beautiful warm rich deep powerful lighting techniques that
[0:38] will take your renders to the next fucking level. Follow me in this journey of lighting.
[0:47] Go to your favorite place to find textures. I'm going to Pinterest today. You can use any
[0:52] website you want. But I have searched up granite, tile texture, marble, you can be really specific.
[1:01] Okay, it's just find yourself a texture that has lots of layers. It looks like the light would
[1:06] just be able to shine through there so beautifully and create so much depth. I'm using this one over
[1:13] here. So let me let me meet you back in Blender. Okay, so once you found your texture, I want you to
[1:21] create a new shader, drag out from the base color and add an image texture, right? Pretty basic stuff.
[1:28] Open up that image texture and find where you've downloaded your new texture here. Okay,
[1:37] then I want you to plug that color into the color of the emission, turn up the strength to about three
[1:44] or more, you know, whatever you want. And look at that, that already looks better. You know,
[1:52] turn that down a little bit. Look at that. The emission of this is catching the light and all
[1:59] of these little cracks just how it would in real life. Okay, so you can just stop right here. You
[2:03] can click off the video and play with this to your heart's content. Okay, but I'm going to show you
[2:08] something a little bit better. Here comes the secret sauce. Okay, drag out from the strength,
[2:14] add a math, multiply, drag out from the value, add a color ramp, add a gradient texture, plug that
[2:25] into the color ramp, quadratic sphere, control team, turn this up to about three, click and drag
[2:34] on these coordinates and type in minus point five, drag this down, kind of adjust it. Now look at this.
[2:44] Watch the difference.
[2:48] See that? Looks like there's a light inside of here now. So let me show you something else now.
[2:54] You want to take a black body node and mix it with the image texture.
[3:02] Plug that color back into the color there. It doesn't matter, whatever. Plug that into the multiply
[3:09] and drag that up. Make this 3000 kelvin. Right? Look at that glow. Look at how warm that is. Oh my
[3:19] God, it's beautiful. It's beautiful. Now you should put a light in here. Make the light bulb a little
[3:27] bit cooler than the shade here. Because in real life, the light bulb would be cooler and that
[3:35] like granite marble shade, whatever it is, it would be glowing much warmer. Think of a salt lamp.
[3:43] Right? Let's go over to this lamp. Remember this? This concrete? Well, not for much longer.
[3:50] Make a new shader. Do the same thing. Image texture. Go back to wherever you got your textures
[3:58] and find yourself like a fabric linen canvas kind of texture and just put that over the lampshade.
[4:07] Go down to the emission here and what you can actually do, grab this whole node setup,
[4:12] copy it and paste it to the new lampshader and plug all these noodles into the right sockets.
[4:18] Now look at that and also I want to show you. That's how it would look if you just
[4:23] cranked out the strength. Right? It doesn't look very good.
[4:28] See these folds? Let me go to the solid view here. You see these little folds I've added? This will
[4:34] act as the wire armature that is wrapped around these lamps. Once you have something like this,
[4:39] select all of the edge loops, add another material and click assign. Find the same texture that you
[4:49] use for the lamp and just make a copy of it. Add a translucency shader and plug the image color
[4:57] into the translucent color. Drag that little noodle right over here. So that's that. You see,
[5:02] you wouldn't have as much light around here because of that wire armature. And same thing with
[5:09] this bulb over here. You know, play with the temperature and everything. Realistically though,
[5:14] it would be a little bit cooler. You'll notice on the edges that it's equally as bright as it is
[5:21] in the middle here. So duplicate this multiply. Plug that value at the bottom. Drag out, get a
[5:32] color ramp and a layer weight. This should be inverted.
[5:43] And drag this value up a little bit. It's got to be really subtle.
[5:49] Right? But look at it now. Then you take the color and put it into the blend.
[5:57] But another thing you'll notice is that the thicker parts of the weave are emitting light.
[6:02] So we want to invert this. So duplicate your color ramp and plug it in just like so.
[6:08] So now it looks like a lampshade. Now you have something you can work with. Look at that. This
[6:12] can be in the background of your renders. This could be the main subject of your render. You can
[6:17] get really up close on this and it will always look good. However, we are not done yet. For this
[6:25] last light, I have the exact same setup as I used with the lampshade. Instead of a math
[6:32] multiply node, it's going to be a multiply add. And you want to make sure that this multiply
[6:37] is in this socket and the layer weight just goes into the value. And of course, the texture is
[6:44] driving the blend of the layer weight. Now this multiplier will adjust the strength of the layer
[6:50] weight. And this one adjusts the strength of the fake light bulb in here. Then you'll notice
[6:55] these little cracks in the marble texture that look like the light is just hitting at that perfect
[7:00] angle dispersing that light 10 times brighter. I also have a brightness and contrast node in here
[7:06] just to make it a little bit softer. Here's how it looks with the contrast turned up. And it has
[7:13] its own effect that you know, you looks nice, right? But for this one, I want it to be a little
[7:18] softer. I said that last tip for the end, but you can see here that I've added it to the first one
[7:24] that we did. This is a great way to add a quick depth to your emission textures. And I hope to see
[7:32] people getting very creative with this because there's a lot you can do. I got more to show you,
[7:37] don't you worry. In a future video, of course, if you ever find yourself with flat boring,
[7:43] emissive materials, well, let's hope it doesn't happen again.



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
