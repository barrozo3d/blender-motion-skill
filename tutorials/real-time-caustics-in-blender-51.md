---
title: Real time Caustics In Blender 5.1
source: YouTube
url: https://www.youtube.com/watch?v=wOyk5V7PyfA
author: Extra 3d
ingested: 2026-06-25
blender_version: "Blender 5.1"
tags: [shaders, caustics, cycles, glass, materials, procedural, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/real-time-caustics-in-blender-51/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
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
**Transcript:** don't, I am just going to give you a quick overview and for those who are already good  at it, you can just skip to the next chapter. Now don't get confused by this layout, this  is just the shader editor on the left and the viewport on the right with the properties  tab. So first off, make sure you are using the Cycles Render Engine because unfortunately  this works best in Cycles only for now. Switch this to GPU compute and if the option looks  unavailable even if you have a graphics card, go to Preferences and head into the System  tab. Select any one of these according to your graphics card and save the preferences.  Now when your object is selected, you will get a new tab right here which is the Material  tab. You can create a new material for the object from here. You can also do that in the  shader editor itself, but the shader editor just gives you a lot more control over the  material. Whenever you create a new material, blender adds these two nodes by default and  both of these are connected. Whatever is connected into the output node is projected onto  the material. This node has all of the main settings that you can tweak like roughness,  colour and a bunch of other stuff. Now to add any new node, press Shift plus A and search  for any node. Since we want a glass material, search for glass and select it. Just disconnect  the default node and connect the glass shader into the output.  If you notice it, the node that is going into the surface of the output is a green point  and almost all nodes with this point are named similarly at the end. You can connect any  node from this list into the surface, but not all of them will work correctly. It will  still show an output, just not in the right way. Anyways, if you search for a mixed shader node  and add it, you can mix two shaders with a factor value. So let's say I have two materials,  one red and one blue. If I move the factor value to one, the blue shader takes over,  and if I move it completely to zero, the red shader will be visible. You can control this  factor value with black and white textures as well. Talking about textures, blender has some  procedural textures that we will use later in the video. For now, I am just going to add a  Voronoid texture. You can preview it with Control Shift click. This only works if you enable the  node Wrangler, add on in the preferences, just make sure to save the preferences.  You can control the scale and other options for the texture. Just like we mix the base shaders,  you can do the same with textures as well, but you just have to add a mixed color node instead of  the mixed shader. And the cool thing about this is that it has different modes that give you more  options. You can also add a color ramp node, which basically has two handles that you can use  to adjust the texture to your liking. Finally, textures require coordinates to project properly  onto the surface. You can add those by selecting the texture and pressing Control plus T.  We will use the object coordinates because they will be the same for all objects. We just have to  make sure all objects have the correct scale, which you can do by pressing Control plus A  and applying scale. Now let's start with the base shader. In this chapter, we will create a glass


### Chapter 2: Base Shader [4:11]
**Transcript:** shader, optimize it, and then manipulate the shadow of that object in a way that creates an illusion  of course, so making a glass shader is pretty easy. You just have to add a glass shader, and that's  basically it. You can also do that with a principled BSDF shader by setting the transmission value to  Max. And if you are a pro, you can create this complex setup as well. I am just going to go with  this basic principled shader and we will continue from here. Now to optimize it, we are going to tell  Blender that the light passing through this glass object should pass through nothing, while the glass  shader still stays visible in the camera. So to do that, add a Mix shader node and place it after  the glass shader. Add a transparent shader and a light path node. Connect the transparent shader  into the second slot and connect the shadow ray into the factor.  Now if you notice something, when I change the color of the transparent shader, the shadow  reacts to it. So basically we can control the shadow from here, and now we just have to manipulate  it in a way that makes it look like caustics. Now to do that, add a geometry node.  Take the incoming and normal into dot product. Add a color ramp and adjust it like this.  This is our base level. You can add a Mix color node and set it to multiply.  Now you can change the color in the second slot which will affect the color of the shadow.  You can also use a Voronoid texture with the color output to get this beautiful effect,  but we will improve it later in the end so you don't have to worry about it right now.  One more thing before we move on, let's say your object is something like a bottle  and it has a label, which basically should not create caustics right.  So to avoid that, just add a Mix color node here and connect the label mask into the factor.  Change the color in the second slot to black and you will be good to go.  You might need to use the Invert node depending on the label mask you have.


### Chapter 3: Water Caustics [6:33]
**Transcript:** Let's create water caustics with this method. By the way, this original shader is by  Polyfueled so all credits go to him. Add a Voronoid texture and if you preview it,  you will notice that it's pattern already looks something like caustics.  I already know the best settings for this so first set it to 4D. Change this to Smooth F1,  set the smoothness to 0.4 and randomness to 0.9.  Now the main trick here is to duplicate it and take the difference of both using a Mix color node.  Change the mode to Difference and make sure the factor is set to 1.  Since we are subtracting two similar textures, we will basically get nothing.  To fix that, change the smoothness of the second Voronoid texture to 0.2.  One more thing, make sure to add texture coordinates and set them to Object.  It would also be great if we use a value node to control the scale for both textures.  Now animating it is very simple. Just keyframe a value node and connect it into the W value.  Add a Multiply Math node and this value basically controls the speed of the caustics.  Add two color ramps to make it softer and brighter, just copy my settings and you'll be fine.  Now connect it into the color of the Transparent Shader and you're good to go.  Let's add some color as well. Add a Mix color node and connect it after the color ramp.  Set it to Multiply and increase the Strength to 1.  Now just drag this color and it will open up a color wheel.  A small trick here is to make the color value brighter by adding a value of 10 here.  And that's pretty much it.


### Chapter 4: Final Caustics [8:26]
**Transcript:** Now we are on the final shader which looks absolutely beautiful,  but it's also a bit harder to make. We're just going to build this on top of the base shader  we created earlier. Add a mapping node and place it here. Add a Normalize node and place it before  the mapping node. Duplicate it and set it to Add. Make sure the values are set to 0.5.  Now change the Z axis on the mapping node to minus one.  Also adjust the scale to 0.8 on the x and y axis and keep it at 1.4 on the Z axis.  Add a Mix color node, set it to Screen and make sure the factor value is set to 0.7.  Now let's add some texture to it. Add a Gradient node and a Noise texture.  Make sure to add the coordinates and set them to Object.  Decrease the scale on the Noise texture and increase the detail and roughness to Max.  Increase the distortion to something around 200 as well.  Now just duplicate the Vexerad node and connect it before the Mix color node.  Connect the texture into the second slot.  Now you have to add a Color ramp and create some fringes.  It's pretty simple. Just copy what I am doing. Change the mode to Constant and decrease the white value.  Now you have to add three fringes. Just copy the settings.  Now add another Color ramp and set the mode to E's.  Bring the black handle closer towards the white and mix these two Color ramps with a Mix color node.  Add a Multiply node and change the value to 2.  Now for the color, add a Mix color node and set it to Multiply.  Increase the factor to 1. You can control the color from this value now.  Now we can improve this even further with Chromatic Dispersion,  which is a little complex so I have made this free project file that contains both this shader  and the Corsics shader. You can get it from my Patreon for free.  You just have to append the material or copy it into your project file.  Thanks for watching and make sure to click that subscribe button.



---

## Captured Frames

- [2:00] tutorials/frames/real-time-caustics-in-blender-51/frame_000.jpg
- [3:30] tutorials/frames/real-time-caustics-in-blender-51/frame_001.jpg
- [5:10] tutorials/frames/real-time-caustics-in-blender-51/frame_002.jpg
- [7:20] tutorials/frames/real-time-caustics-in-blender-51/frame_003.jpg
- [9:30] tutorials/frames/real-time-caustics-in-blender-51/frame_004.jpg

---

## Structured Notes

### Core Technique
Fake caustics in Cycles by manipulating the shadow of a transparent glass object: Mix Shader + Transparent Shader controlled by the Shadow Ray (Light Path) makes the shadow invisible, then procedural textures color the Transparent Shader output to simulate a caustic light pattern. No actual caustic rendering — runs in real time. Original method by Polyfueled.

### Summary
Extra 3d shows how to create fast-rendering caustics in Cycles 5.1 without raytraced caustics. The core trick: Glass/Principled shader → Mix Shader; Transparent Shader goes into slot 2; Light Path → Shadow Ray → Mix Shader factor — the object's shadow now passes through as pure transparent. From there, the Transparent Shader's color becomes the "caustic pattern." Base pattern: Geometry → Incoming + Normal → Dot Product → Color Ramp. Water caustics upgrade: two Voronoid 4D textures (Smooth F1, smoothness 0.4 vs 0.2, randomness 0.9) → Mix Color Difference; animate W value via keyframe + Multiply. Advanced caustics layer: Mapping + Normalize → Duplicate Add (0.5) → Z axis −1, XY scale 0.8 Z 1.4 → Mix Color Screen (0.7); Gradient + Noise (distortion 200) → Color Ramp Constant (3 fringes) + Color Ramp Ease → Mix + Multiply ×2. Free project file includes chromatic dispersion variant.

### Key Steps
1. **Engine:** Set render to Cycles + GPU Compute.
2. **Base glass shader:** Add Glass shader (or Principled BSDF Transmission = 1) → Material Output Surface.
3. **Shadow pass-through:** Add Mix Shader after glass. Add Transparent Shader into Shader slot 2. Add Light Path → Shadow Ray → Mix Shader Factor. Shadow becomes transparent and controllable.
4. **Test color:** Change Transparent Shader Color → shadow reacts. This is the caustic canvas.
5. **Base caustic pattern:** Geometry node → Incoming + Normal → Dot Product node → Color Ramp (adjust contrast). → Mix Color (Multiply) → Transparent Shader Color.
6. **Label exclusion (bottles):** Add Mix Color before Transparent Color input; plug label mask → Factor; second Color = black. (Use Invert if needed.)
7. **Water caustics:** Add Voronoid Texture (4D, Smooth F1, Smoothness 0.4, Randomness 0.9). Duplicate it → set second Smoothness to 0.2. Mix Color (Difference, Factor=1) of both = subtle pattern. Texture Coordinate Object + shared Scale Value node.
8. **Animate caustics:** Add Value node → keyframe from 0 to large number → plug into both Voronoid W. Add Multiply Math (speed control).
9. **Soften/brighten:** Two Color Ramps; adjust to taste → connect to Transparent Shader Color.
10. **Color tint:** Mix Color (Multiply) → Factor 1; Color Value = 10 for bright, saturated caustic color.
11. **Advanced caustics (complex):** Add Mapping + Normalize nodes in chain. Duplicate Normalize → Add node (values 0.5). On Mapping: Z axis = −1; Scale X=0.8, Y=0.8, Z=1.4. Mix Color Screen (factor 0.7) of two streams.
12. **Noise fringe layer:** Gradient Texture + Noise Texture (Texture Coord Object; scale low; detail max; roughness max; distortion 200). Color Ramp Constant (3 fringes, decrease white value). Color Ramp Ease (move black handle right). Mix Color of both Color Ramps. Multiply ×2.
13. **Final color:** Mix Color (Multiply, Factor 1) → control caustic color from this value.

### Nodes / Settings
- Voronoid Texture: 4D; Feature: Smooth F1; Smoothness: 0.4 (first) / 0.2 (second); Randomness: 0.9
- Mix Color (water): Difference mode, Factor 1.0
- Noise Texture (advanced): Scale low; Detail max; Roughness max; Distortion 200
- Color Ramp 1: Constant mode; 3 fringes; white value reduced
- Color Ramp 2: Ease mode; black handle moved toward white
- Mapping (advanced): Z = −1; Scale X 0.8, Y 0.8, Z 1.4
- Mix Color Screen: Factor 0.7
- Speed Multiply: controls W animation speed
- Color value: 10 (for bright, vivid caustic color)

### Difficulty
Intermediate — multi-layered shader logic; base version is approachable, advanced version requires careful node routing

### Blender Version
Blender 5.1 (Cycles only; method works in 4.x as well; tutorial uses 5.1 label)

### Tags
#shaders #caustics #cycles #glass #materials #procedural #intermediate

---

## Related Tutorials
- `real-time-caustics-in-blender-51.md` — this tutorial
- `you-should-make-glass-animations-in-blender-51.md` — glass shader companion
- `photorealistic-renders-in-blender.md` — Cycles full pipeline including material approach
- `my-new-favorite-lighting-trick-in-blender.md` — light manipulation via shader tricks (related concept)
