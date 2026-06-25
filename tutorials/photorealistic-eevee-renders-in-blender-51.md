---
title: Photorealistic Eevee Renders In Blender 5.1
source: YouTube
url: https://www.youtube.com/watch?v=AoGPxjgqVYE
author: Extra 3d
ingested: 2026-06-25
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/photorealistic-eevee-renders-in-blender-51/
frame_count: 0
---

# Photorealistic Eevee Renders In Blender 5.1

**Source:** [YouTube](https://www.youtube.com/watch?v=AoGPxjgqVYE)
**Author:** Extra 3d
**Duration:** 14m58s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction [0:00]
**Transcript:** Let me ask you a simple question. Which one of these is rendered in EV?  Almost all of you will say that this is cycles and this one is rendered in EV, which is partially  correct. But what if I tell you that both of these are rendered in real time with EV?  As you can see this is running in EV in real time. Since Blender introduced EV, it has  always been in the shadows for not producing realistic results, until they introduced  ray tracing, which flipped the whole situation and made it possible. You might be thinking  that if ray tracing does the work, why should you watch this video? You are correct, but  this checkbox most of the time won't get you the results you are looking for. And this  video is exactly about how to achieve photorealism with EV.  In this video, we will not only go through the basics, but we will also do some practical  work.


### Overview [1:09]
**Transcript:** Here is a quick overview of the video. In the first chapter, we will go through the  basic theory of how EV works and what the workflow is going to be like. You can skip  this chapter if you want to directly start with the settings. In the second chapter,  we will start with this basic scene, which I made using these assets that I found on  CG Trader, which is also our sponsor today. CG Trader is basically an online marketplace,  where you can get high quality 3D models very easily. It has over 2 million 3D models, making  it one of the largest sources for high quality and custom 3D content. I will talk more about  it later in the video. For now, we will basically apply the concept and workflow in this chapter  and make this scene look good. In the third chapter, we will focus on light and reflection  probes, which are just a way to improve the lighting by baking the lighting data, and  the reflection probes basically improve the reflections of glossy materials. In the  fourth chapter, we will go through a complex scene in which we will improve some basic  shaders, like glass and translucent materials. And finally, in the last chapter, we will  test the workflow and re-light a complete scene. I hope you watch till the end so that you  don't miss the free gifts that you will get along the way.


### Chapter 1: Basic Concepts [2:23]
**Transcript:** So when you open Blender, the render engine is set to EV by default. Most of the time,  we switch this to Cycles, which gives accurate results because it is a path tracer that  simulates accurate lighting and reflections. Now, before I delete the cube, let's understand  how rendering works, so Cycles is basically a path tracing render engine. Let's say  a ray is generated from this camera, and it goes and intersects with a surface in its  direction. Let's call this the primary ray. Now, a secondary ray will be generated, which  will bounce off randomly until the rendering equation is solved. This allows Cycles to  achieve accurate light simulation, but it comes at a computational cost.  On the other hand, EV has no light bounces, it is just flat by default. But EV has evolved  over the last few years, and now it has ray tracing. Now, compared to path tracing, which  doesn't stop until the rendering equation is completed, ray tracing is pretty smart.  And what it does is that it directs the secondary ray to the light source, and if that ray hits  the light, this point is lit. If something blocks the shadow ray, that point is in shadow.  This allows it to be fast and get similar results, but it's still not enough. There are many  issues with this, but the major issue is that it's based on screen space method, which  basically works on the basis of what the camera sees. You can see the change when I move the camera.  But don't worry, to fix this, we are going to use light probes, which are basically cubes with  small dots in them. And these dots store the lighting data that affects the objects within these  dots. This method, combined with ray tracing, solves the issue. This is obviously just the base  of the workflow, and there is more to it when it comes to the practical stuff.


### Chapter 2: Practical Workflow with CGTrader Assets [4:11]
**Transcript:** So, for the first demonstration, I am going to go with this scene. Let me first break it down for  you. I have this basic plane with this wood texture that I got from Polyhaven, along with this HDRI.  Starting with the assets, I have added this statue that I got for free on CG Trader, and I scattered  this art studio collection, which I also found on CG Trader. Now, before we continue, let me tell you  more about today's sponsor, which is CG Trader. CG Trader is an online marketplace, where you can  find millions of high quality 3D models. It is a great place to get 3D models. You just have to  search for what you want, and the results will show up. You can filter out the format and just select  any model you want. When you open it, you will find most of the information about the model.  You can check the reviews about the creator and the model. You can look for the polycount and  geometry, and you can also ask the creator any questions before buying. Once you are done, you can  easily download it and open it in your software. The best thing is that CG Trader gives out great  discounts and offers, and for you guys, CG Trader is giving you a 10% discount for any item,  including items that are already on sale. So, what are you waiting for? Just use the code  extra 3D10, and claim the 10% discount right now. The link is in description.  Now let's get back to the video. I have also added this area light along with some volumetrics  nothing fancy. You can get the base project file for free on my Patreon to follow along.  Now before we change anything, first go into edit, preferences, go into the system tab,  and change the back end mode to vulcan. Save preferences, and it will also ask you to restart,  so restart blender as well. Once that's done, the first step of the workflow is to enable ray tracing,  and you can see it basically does a lot of the work. Now before we do the settings,  let me explain you how the world settings work. So basically, in EV, the environment doesn't work  how it works in cycles. You basically have to tell which part of the HDRI will act as light sources.  You basically control that with the threshold value. Now currently the scene has a very sharp light,  I really don't want that. I'm just going to increase the threshold to 10, which will make it softer.  You can basically test it and play with the settings until you get something you want.  Now let's talk about the settings. So first off, ray tracing does the work, but you still have to change  the settings. The first is resolution. Change this to 1x1 for full resolution. Increase the precision  value and the thickness to 1. Under the denoising tab, disable the second option, which basically ruins  the materials. After that, disable the fast GI approximation.  If you go up, you will find samples, increase those. I'm just going to go with 120 for the final render.  In the shadows tab, you can increase the shadow rays to improve the shadows. You can go with 4,  which will do the work. After that, the area light is currently also affecting both sides of the  render. To better explain this to you, let me show you this example. So this is without jittered  shadows, as you can see the mesh is barely stopping the shadow, and it's creating this weird effect.  To fix this, go into the light settings and check jittered shadows.  Decrease all three values to their minimum.  To make this work in the viewport, you have to check this box as well.  Now, since you have to do this for each light, just select all and change the setting only for one light,  while pressing the alt key, which will change for all.  This human model is also from CG Trader, make sure you use the code to get the discount,  and the link is in description. You can see it improves the shadows a lot.  Before we move on, if you scroll down and go under the film tab, you will find overscan.  Enable that, it basically renders extra, and then crops later on, and this helps a lot since  ray tracing is based on screen space method. Now let's talk about the probes. So basically,  this scene won't be affected by it that much, but still we are just going to cover the basics.  So I am just going to add a volume probe, and roughly scale it so it fits my scene.  Go into the Data tab, and first off, increase the grid resolution. I usually go with something  like 16 or maybe 20. Also increase the resolution to 120 or 80, depending on your system.  Mark the world contribution option as well, make sure it's always checked,  and once you're done with the settings, you have to now disable the objects that you don't want  to be baked, such as any animated object, so just disable that. As you can see, there are no  animated objects, or the objects that are supposed to move, so I'm just going to leave that.  But if you have to disable something, you can just uncheck the render button, and it will just  disable it. I am using this volumetrix for the scene that I am going to disable, because volumetrix  do not look good after baking. After clicking the bake button, wait a few seconds.  Once it's done, I can now switch back on the things that I disabled like the volumetrix,  and here it is. The biggest problem with EV is that it also has no ambient occlusion.  Now what is that? It's basically a shadow between the edges of any object. Let me just show you  how to get it. Go into the passes tab, and enable the ambient occlusion pass, to see the effect,  open the compositor, and create a new workspace. Connect the ambient occlusion pass into the viewer  node. Make sure to enable the viewport compositing. Now you can adjust the strength of it by adjusting  this value. A value ranging from 0.2 to 1 works perfectly. To mix this with the main render,  just add a mix colour node, and connect it with the main render, and switch the mode to multiply.  You will face two more problems. First the background will turn dark, and the depth of field  won't work correctly either. So first enable the environment pass, and connect it in the compositor  with an alpha over node. You have to enable transparent as well to make this work.  By the way, I got this idea from Pirani Arts. I hope I am pronouncing the name right. He basically  gave the idea in the video, but didn't show how to do it. But still that idea opened my mind, so  credit goes to him, link is in the description. Now to fix the depth of field problem,  just scroll down until you find the depth of field tab, and make sure to check jitter.  There won't be any change right now, but it will show after the render.


### Chapter 3: Light & Reflection Probes [11:00]
**Transcript:** Now if we apply the workflow in an indoor scene, it will work fine until you enable the background  light which will cause world bleeding. Now this issue has been an EV since it was introduced.  Blender Guru has explained this in his video, and I was like this is ugly, this is terrible.  And he has also told a method to fix this by using light probes, but the problem with that is,  it only works for simple shaped indoors, and it is also a pain to set up. So I have a better  improved method, which is to just disable the background world while baking the lights,  and once it's baked, just enable it again. So let's do this from scratch. Add a volume probe,  and make sure it covers your scene. Change the settings by increasing the resolution,  and marking the world checkbox.  Now before you bake, disable the background world, but it will make the scene dark.  To fix this, add an area light at the places like windows or doors, and set a similar color,  and set strength accordingly. This will help fake the environment light. Now it would be better  if you put these in a separate collection to keep the scene organized. Just bake the lighting now,  and once that's done, enable the background world, and also disable the area lights that we made  for the baking purpose. And that's it. Now let's talk about the reflection probes. These are pretty  simple. You just have to make sure it roughly fits the mesh, and you are done. There is really not  much about it. By the way, I got this room model for completely free on CG Trader, which is awesome.  Make sure to check out CG Trader with the link in description, and for you guys this complete  project file will be available on my Patreon for completely free, so enjoy.


### Chapter 4: Advanced Materials [12:49]
**Transcript:** Let's improve some materials. Let's start with the Translucent Shaders, so basically  thin objects get lit by the light from the backside as well. The Translucent Shader doesn't work  correctly in EV, so we have to use subsurface scattering for that. This method is from Glare  Balik Sandroff, who is a legend himself. I have linked his video in the description. Just watch  that. Nobody explains better than him. This trick works for human skin as well. Just watch his video.  About the glass shader, you just have to change one setting, which is to just enable ray trace  transmission. And that's it. Now I can talk more about the materials, but this video has already  got so long, and I have to cover other things as well. So I will make a video about it in the future.  Only if this video gets 10,000 likes, which is impossible.


### Chapter 5: Full Scene Relighting [13:37]
**Transcript:** Now we are on the final chapter, and let's review the basics.  I have this abandoned house scan that I found on CG Trader. You can grab it for a very low price  using the discount code, check the link in the description. Now I have basically applied the  workflow here. I have changed all of the main settings. I have used a volume probe without the  background light, and with an extra area light to fake the background world. I have also added  ambient occlusion. And that's it. You will get the hang of it when you try this on multiple scenes.  Now the fun part, let's add some fisheye effect in the camera. Now you can do this easily in cycles,  with the panoramic lens type, but it doesn't work with EV. Instead decrease the focal length,  and go into the compositor. Add a lens distortion node, and increase the distortion a little bit.  Check the fit box, and you will be good to go. Another thing I did was this hand held camera animation,  which is basically with the help of this add-on. I have linked it in the description. Add some  final touches in the compositing, play with the exposure, and you will be good to go. I have a  complete video about photorealism so you can watch that out.



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
