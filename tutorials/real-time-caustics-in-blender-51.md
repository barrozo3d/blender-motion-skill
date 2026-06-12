---
title: Real time Caustics In Blender 5.1
source: YouTube
url: https://www.youtube.com/watch?v=wOyk5V7PyfA
author: Extra 3d
ingested: 2026-06-12
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/real-time-caustics-in-blender-51/
frame_count: 0
---

# Real time Caustics In Blender 5.1

**Source:** [YouTube](https://www.youtube.com/watch?v=wOyk5V7PyfA)
**Author:** Extra 3d
**Duration:** 11m6s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction [0:00]
**Transcript:** Coursetix are very hard to render and usually take ages, but in this video we're going  to create real-time caustics that not only look amazing, but also run fast.


### Overview [0:27]
**Transcript:** Now without wasting any time, let me give you a quick overview of the video. We're going  to start with the basics and if you already know them, you can skip to the next chapter  where we'll jump into the core concept of how this method works and create a basic shader.  After that, we're going to play around with procedural textures to create something like  underwater caustics. And finally in the last chapter, we'll take that first shader and  turn it into a more complex setup that generates the cool caustics you saw at the beginning  of the video. Now I am going to assume that you know some basics of blender, but if you


### Chapter 1: Basics [0:58]
**Transcript:** don't, I am just going to give you a quick overview and for those who are already good  at it, you can just skip to the next chapter. Now don't get confused by this layout, this  is just the shader editor on the left and the viewport on the right with the properties  tab. So first off, make sure you are using the Cycles Render Engine because unfortunately  this works best in Cycles only for now. Switch this to GPU compute and if the option looks  unavailable even if you have a graphics card, go to Preferences and head into the System  tab. Select any one of these according to your graphics card and save the preferences.  Now when your object is selected, you will get a new tab right here which is the Material  tab. You can create a new material for the object from here. You can also do that in the  shader editor itself, but the shader editor just gives you a lot more control over the  material. Whenever you create a new material, blender adds these two nodes by default and  both of these are connected. Whatever is connected into the output node is projected onto  the material. This node has all of the main settings that you can tweak like roughness,  colour and a bunch of other stu...


### Chapter 2: Base Shader [4:11]
**Transcript:** shader, optimize it, and then manipulate the shadow of that object in a way that creates an illusion  of course, so making a glass shader is pretty easy. You just have to add a glass shader, and that's  basically it. You can also do that with a principled BSDF shader by setting the transmission value to  Max. And if you are a pro, you can create this complex setup as well. I am just going to go with  this basic principled shader and we will continue from here. Now to optimize it, we are going to tell  Blender that the light passing through this glass object should pass through nothing, while the glass  shader still stays visible in the camera. So to do that, add a Mix shader node and place it after  the glass shader. Add a transparent shader and a light path node. Connect the transparent shader  into the second slot and connect the shadow ray into the factor.  Now if you notice something, when I change the color of the transparent shader, the shadow  reacts to it. So basically we can control the shadow from here, and now we just have to manipulate  it in a way that makes it look like caustics. Now to do that, add a geometry node.  Take the incoming and normal into dot product. Add ...


### Chapter 3: Water Caustics [6:33]
**Transcript:** Let's create water caustics with this method. By the way, this original shader is by  Polyfueled so all credits go to him. Add a Voronoid texture and if you preview it,  you will notice that it's pattern already looks something like caustics.  I already know the best settings for this so first set it to 4D. Change this to Smooth F1,  set the smoothness to 0.4 and randomness to 0.9.  Now the main trick here is to duplicate it and take the difference of both using a Mix color node.  Change the mode to Difference and make sure the factor is set to 1.  Since we are subtracting two similar textures, we will basically get nothing.  To fix that, change the smoothness of the second Voronoid texture to 0.2.  One more thing, make sure to add texture coordinates and set them to Object.  It would also be great if we use a value node to control the scale for both textures.  Now animating it is very simple. Just keyframe a value node and connect it into the W value.  Add a Multiply Math node and this value basically controls the speed of the caustics.  Add two color ramps to make it softer and brighter, just copy my settings and you'll be fine.  Now connect it into the color of the Transparent S...


### Chapter 4: Final Caustics [8:26]
**Transcript:** Now we are on the final shader which looks absolutely beautiful,  but it's also a bit harder to make. We're just going to build this on top of the base shader  we created earlier. Add a mapping node and place it here. Add a Normalize node and place it before  the mapping node. Duplicate it and set it to Add. Make sure the values are set to 0.5.  Now change the Z axis on the mapping node to minus one.  Also adjust the scale to 0.8 on the x and y axis and keep it at 1.4 on the Z axis.  Add a Mix color node, set it to Screen and make sure the factor value is set to 0.7.  Now let's add some texture to it. Add a Gradient node and a Noise texture.  Make sure to add the coordinates and set them to Object.  Decrease the scale on the Noise texture and increase the detail and roughness to Max.  Increase the distortion to something around 200 as well.  Now just duplicate the Vexerad node and connect it before the Mix color node.  Connect the texture into the second slot.  Now you have to add a Color ramp and create some fringes.  It's pretty simple. Just copy what I am doing. Change the mode to Constant and decrease the white value.  Now you have to add three fringes. Just copy the settings. ...



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
