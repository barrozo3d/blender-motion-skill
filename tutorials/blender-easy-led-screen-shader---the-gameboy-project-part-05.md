---
title: BLENDER Easy LED screen shader - THE GAMEBOY PROJECT PART 05
source: YouTube
url: https://www.youtube.com/watch?v=BhJfdQn5Sf4
author: Pierrick Picaut
ingested: 2026-07-21
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-easy-led-screen-shader---the-gameboy-project-part-05/
frame_count: 0
frame_status: pending-selection
---

# BLENDER Easy LED screen shader - THE GAMEBOY PROJECT PART 05

**Source:** [YouTube](https://www.youtube.com/watch?v=BhJfdQn5Sf4)
**Author:** Pierrick Picaut
**Duration:** 11m46s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-easy-led-screen-shader---the-gameboy-project-part-05 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone, this is Pierrick from P2Design. In this video, we will be creating the material for the LED screen of our Game Boy. Let's get started!
[0:10] Let's create a new material slot and create a new material that we will call LED.
[0:16] And then in Edit mode, we will assign it to the right geometry next to the screen.
[0:23] I will make the base material darker and I will drastically reduce the roughness so that we have clear reflection upon it.
[0:30] This will act as being our base plastic upon which we will add some emission.


### Emission [0:35]
**Transcript (timestamped):**
[0:36] The idea is to make the core of the LED shinier or more emissive than the outside.
[0:43] While it might not be physically correct, I prefer to add the emission upon the current shader.
[0:50] It will also be easier to use a separated emission shader mixed with an add shader node than to use the integrated emissive input from the Principled BSDF.
[1:02] The add shader doesn't allow us to play with any factor, you just have to plug in the emission and the Principled BSDF shader.
[1:11] Now to get this kind of physical gradient between the core of the LED and its outside, we will use a geometry-based input.
[1:21] So we will go into Input and Layer Weight. Here we will be able to play with the Fresnel on the Facing Output.
[1:30] I generally prefer to use the Facing Output because the gradient is more obvious and we will add a converter color ramp to play with its contrast and its color.


### Converter Color Ramp [1:36]
**Transcript (timestamped):**
[1:41] The idea is to then plug in the color into the color of our emission and then create a nice gradient from a bright yellow to a dark red.
[1:52] Or if you want to use any other color for your LED, you are free to choose whatever color you want.
[1:59] The benefit of adding it upon our Principled BSDF is that we keep the bright reflection from the environment onto the LED and it kind of looks like plastic or something like this.
[2:13] While it might not be physically correct because we are not using any refraction or stuff like this, it does look good and this is the most important thing.
[2:23] We are playing with visual. The target is not the mean but the result.
[2:28] You can then adjust the strength of the emission shader to your will.
[2:33] Next, we will create a new material slot to make the transparent cover of the screen.
[2:39] So as usual, we will create a new material and assign it into Edit Mode to the corresponding geometry.
[2:47] We will push the transmission to 1 to make it perfectly transparent.
[2:52] Then you need to lower the roughness or the transparency will be kind of blurry.
[2:58] And then playing with the alpha, we can slightly reduce the amount of reflectivity or specularity in a way.
[3:08] This will make the underlying LED screen easier to read later on.


### Create the Led Screen [3:15]
**Transcript (timestamped):**
[3:15] Then to create the LED screen, as usual, create a new slot and create a new material.
[3:22] Then assign it to the underlying plane.
[3:25] We will first build some kind of backlight effect onto the screen.
[3:31] Then we will build the grid and finally add the smiling face upon it.
[3:36] Since the face texture won't be generated but we will use a picture,


### Create Uvs [3:41]
**Transcript (timestamped):**
[3:41] we need to create UVs for our screen.
[3:45] To do so, we will enter in Edit Mode, open the UV Image Editor.


### Uv Image Editor [3:48]
**Transcript (timestamped):**
[3:50] You can see that we have already existing UVs but they are wrong because these are the auto-generated UVs we add during the modeling.
[4:00] So it doesn't really follow the current geometry and we will have a lot of distortion if we use this.
[4:06] To make our life easier, instead of trying to fix those UVs, we will re-unwrap the plane.
[4:13] Since we are working on a flat surface, it will be easier to select it, press U to open the Unwrap menu and Project From View.
[4:23] One of the important things is to be in Front View with Autographic Mode,
[4:28] so that when we will use the Project From View, Lender will take a snapshot of the current geometry
[4:34] and project it into our UVs.
[4:37] Using the bound option will stretch the UV so that it fits the UV space.
[4:44] That could be the right move if we were to paint directly onto the surface
[4:49] because we have the best textual density, meaning that we are not losing any space
[4:55] between the size of our UV island and the texture space.
[5:01] But since we will be using an existing picture, this will create distortion
[5:06] because since our screen is not perfectly square, stretching it to fit a perfectly square surface is not good.
[5:14] So what I can do is try to resize it or project it from view
[5:20] and then scale it homogeneously onto the surface so that it does fit the vertical boundaries of the UV space.
[5:28] From there we can start working on our shader.
[5:31] So this is going to be a pure emission shader because we don't want any reflectivity on this screen surface.
[5:39] So I will add a shader emission shader and I will get rid of the principle BSDF.
[5:45] We can turn it to a base screen to begin.
[5:48] The first thing I want to create is the backlight effect.


### Backlight Effect [5:51]
**Transcript (timestamped):**
[5:53] To do so we will kind of recreate a vignette around our screen.
[5:58] From a shader perspective what we want is to have a brighter color in the middle
[6:04] and a darker one in the outside.
[6:06] So we will add a texture gradient texture.
[6:10] By default it is set to linear but we want some kind of spherical or round shape.
[6:16] So let's choose quadratic sphere and add a converter color ramp to be able to play with the contrast.
[6:24] If we kind of increase the contrast to try to read this gradient
[6:29] we can see that it starts on the lower left corner
[6:33] and this is not what we want.
[6:35] We want it to start in the middle of our screen.
[6:38] By default an unplugged texture is using the UV coordinate of the mesh
[6:44] and we've just created those UVs.
[6:47] So we will have to play with those coordinates to move the current position of the center of the gradient
[6:55] into the center of the mesh or the center of the UVs.
[7:00] To do so select the gradient texture and press Ctrl T.
[7:03] This will automatically generate two nodes, one mapping node and one texture coordinate node.
[7:11] By playing with the location value we will be able to move the origin of our UVs
[7:18] or the origin of our gradient onto the grid.
[7:23] You can see that if I offset the X value I will see my gradient moving to the right into the viewport.
[7:31] So whenever you're beginning with this it's always a bit abstract.
[7:36] What you have to know is that the UV grid grows from 0 to 1.
[7:40] So if you use values between minus 1 and plus 1 you should be able to offset whatever texture onto your UVs.
[7:49] So I will use the UV coordinates and set the X and Y value to minus 0.5.
[7:57] Then we can play with the contrast moving the different flag of the color ramps so that we get a nice vignette effect.
[8:04] I like to switch it to B spline so that I have a smoother gradient.
[8:09] Now to generate our grid or pixel effect we will be using another procedural texture.
[8:15] We will use the brick texture.
[8:17] We will set both input color to white so that we have pure white pixels and a black line between them.
[8:26] And then we will plug in our UV coordinates to make sure that it maps properly.
[8:34] To make your nodes cleaner you can add a layout re-root.
[8:38] This is just a point that will allow you to reshape your nodes connection.
[8:43] Then to create a square shaped grid we need to set the brick width and row 8 to the same value.
[8:50] So here I will use 0.5 and I will disable the offset by setting it to 0.
[8:57] Then playing with the global scale will allow you to increase the number of pixels on screen.
[9:03] So what I've used in the end was a value of 15.
[9:07] Here I'm cranking it up to 20 or 25 but it's too much and it will get just blurry and we won't really get the effect if you render your animation or your product with this.
[9:21] Now that we have created our grid we need to mix it with our gradient.
[9:27] So I will use a color mix color.
[9:30] I will Ctrl Shift to click it to see the result.
[9:33] Then I can use it to drive the strength of my emission shader.
[9:38] I will then increase the factor to 1 and switch from mix to multiply so that our vignette effect gets multiplied upon our grid effect.
[9:49] What would be great now is to be able to control the strength of the emission shader adding a converter math node and set it to multiply.
[10:01] If we increase the value upon 1 we will multiply the strength of the light and so increase its intensity.
[10:10] The last thing we need to do now is to put a smile onto this screen.
[10:15] But first I will clean up a bit my nodes by selecting the brick texture and press Ctrl H.
[10:22] This will hide the unused or unconnected sockets and it will make the node cleaner.


### Node Cleaner [10:27]
**Transcript (timestamped):**
[10:29] You can re-enable them by pressing Ctrl H again.
[10:33] To load our happy face texture I will press Shift A and add a texture image texture.
[10:40] Since an unplugged texture node is always using the UVs I don't need to add the texture mapping nodes prior to this one.
[10:49] Then I will just open my texture and Ctrl Shift to click to check it.
[10:54] And then as we did before for the grid and the gradient texture I will add a color mix color.
[11:02] Set it to multiply and put it just after the first mix color.
[11:08] You can duplicate the mix color it's exactly the same.
[11:12] From there you can play on the size of the grid for your pixel.
[11:17] You can play with the color of the emission shader or you can play also with the strength of the emission shader.
[11:24] This is the end of this video I hope you've liked it. As usual please like and subscribe. Cheers!
[11:38] Thanks for watching!



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
