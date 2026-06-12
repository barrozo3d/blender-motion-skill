---
title: Real time Caustics In Blender 5.1
source: YouTube
url: https://www.youtube.com/watch?v=wOyk5V7PyfA
author: Extra 3d
ingested: 2026-06-12
blender_version: "Blender 5.1"
tags: [shaders, caustics, glass, cycles, voronoi, transparent-shader, light-path, procedural-textures, extra-3d, intermediate]
extraction_status: complete
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
**Fake real-time caustics via shadow manipulation** — instead of expensive light simulation, control the shadow cast by a glass object using a Transparent shader + Light Path node, then shape that shadow with Voronoi textures to look like caustic light patterns. Cycles only. Two variants: animated water caustics (Voronoi 4D + Smooth F1) and complex geometric caustics with Gradient/Noise distortion.

### Summary
11-minute tutorial by Extra 3d on creating fast, good-looking caustics in Blender 5.1 (Cycles). Key insight: real caustics are expensive because they require actual light path bending; this method fakes it by replacing the shadow ray with a procedurally-textured transparent shader. The shadow becomes controllable — animate a value node to make it flow. The Voronoi 4D Smooth F1 trick (subtract two Voronoi textures with different smoothness values) is the core of the water caustic look.

### Key Steps

**Requirements:**
- Cycles render engine (not EEVEE — shadow ray trick is Cycles-only)
- GPU Compute enabled in Preferences → System

**Base Shader Setup (Glass + Shadow Override):**
1. Create glass object → Material → Shader Editor
2. Add **Principled BSDF** → set **Transmission** to 1.0 (or use Glass BSDF)
3. Add **Mix Shader** after the glass shader
4. Add **Transparent Shader**
5. Add **Light Path** node → connect **Is Shadow Ray** into Mix Shader **Factor**
6. Transparent Shader into **second slot** of Mix Shader
7. Result: shadow ray passes through Transparent shader (not the glass) — controllable shadow color

**Water Caustics (Chapter 3):**
1. Add **Voronoi Texture**:
   - Dimensions: **4D**
   - Feature: **Smooth F1**
   - Smoothness: **0.4**
   - Randomness: **0.9**
2. Duplicate it → set second Voronoi Smoothness to **0.2**
3. Add **Mix Color** node → Mode: **Difference**, Factor: **1**
4. Connect both Voronoi textures → Difference node (subtracting similar = edges/veins appear)
5. Add **Texture Coordinate** → set to **Object**
6. Add **Value** node for unified scale control on both
7. Add **Multiply Math** node → connect Value → Voronoi **W** input (animates caustics)
8. Add two **Color Ramps** to soften and brighten
9. Connect result into **Transparent Shader color** → shadow becomes caustic pattern

**Animation:** Keyframe the Value node connected to W (controls time position in 4D texture)

**Final Complex Caustics (Chapter 4) — built on top of base shader:**
1. Add **Mapping** node
2. Add **Normalize** node (duplicate it → set duplicate to Add, values 0.5)
3. Mapping node Z scale: **-1**, XY scale: **0.8**, Z: **1.4**
4. Add **Mix Color** → Mode: **Screen**, Factor: **0.7**
5. Add **Gradient** + **Noise texture** (same Object coordinates, low scale, detail+roughness=Max, distortion≈200)
6. Duplicate the vector node → connect before Mix Color
7. Add **Color Ramp** → Mode: **Constant**, add fringes with narrow white bands (3 fringes)

### Nodes / Settings

**Water Caustics — Core Node Chain:**
```
Voronoi (4D, Smooth F1, smooth=0.4, rand=0.9)
Voronoi (4D, Smooth F1, smooth=0.2, rand=0.9)  ← duplicate
  → Mix Color (Difference, factor=1)
  → Color Ramp (soften)
  → Color Ramp (brighten)
  → Transparent Shader (Color input)

Light Path (Is Shadow Ray) → Mix Shader (Factor)
Glass/Principled → Mix Shader (slot 1)
Transparent Shader → Mix Shader (slot 2)
Mix Shader → Material Output

// Animation:
Value Node → Multiply → Voronoi W
// Keyframe Value node to animate caustics movement
```

**Requirements:**
```
Render Engine: Cycles
GPU Compute: Preferences → System → CUDA/OptiX/HIP (select GPU type)
```

### Difficulty
Intermediate — requires shader node knowledge; Cycles-only limitation important to note

### Blender Version
Blender 5.1 (technique works in earlier versions too — Cycles shadow trick is long-standing)

### Tags
shaders, caustics, glass, cycles, voronoi, transparent-shader, light-path, procedural-textures, extra-3d, intermediate

---

## Related Tutorials
- `tutorials/remove-noise-from-volumetrics-in-blender-50.md` — Other Extra 3d Blender 5.x tips
- `tutorials/replacing-adobe-after-effects-with-blender-tutorial.md` — Voronoi texture motion graphics
