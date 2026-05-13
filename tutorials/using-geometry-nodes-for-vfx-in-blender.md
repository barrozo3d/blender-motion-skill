---
title: Using Geometry Nodes for VFX in Blender
source: YouTube
url: https://youtu.be/PgRax5MeZgY
author: Jacob Zirkle
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# Using Geometry Nodes for VFX in Blender

**Source:** [YouTube](https://youtu.be/PgRax5MeZgY)
**Author:** Jacob Zirkle
**Ingested:** 2026-05-13

---

## Description

In today's tutorial, we're going to be learning some geometry nodes for this cool VFX shot in Blender. Learn everything from lighting your CGI to compositing it all together! Work along with me using the free assets I provide below! Let's learn Blender VFX together ;)

🌴FREE VFX ASSETS AND FOOTAGE🌴
https://vfxoasis.com/

▬ DOWNLOADS ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
🤩Download the assets here: https://vfxoasis.com/product/vfx-integration-footage-with-camera-tracking-and-hdri/

▬ LINKS ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Camera Tracki

---

## Raw Content (for analysis)

Kind: captions Language: en By the end of this tutorial, you'll know everything that you need to know to make this cool effect using geometry nodes for this visual effects shot. Join me and let's learn together. So, for today's shot, we're going to need three main things. First, of course, is the footage. And then, we need a 3D asset in order to materialize. And then, finally, we need an entry in order to light the scene. Lucky for you, I'm going to provide all three down in the description below that you can use for free. I just launched my visual effects asset library called Visual Effects Oasis. And on there, you can find a pack that contains all three of our things that we need for this specific shot. Just use the code Oasis on the screen now at checkout, and you should be able to get the entire pack totally for free. Again, the link is in the description down below. So, make sure to go ahead and download it. And let's go hop in the tutorial. Okay, so here is our scene right here. I did do a few things just to set us up. Uh, first of all is the camera tracking. We have a moving camera, so we do need to go ahead and track that. I have plenty of camera tracking tutorials. I'll link some of mine down below as well in the top right of the screen right now. Also, this plane that we have in our scene, first of all, it's set to be a shadow catcher. So, an object visibility shadow catcher over here. And then also, I have a texture onto it. All it is is just a movie clip. So, that's the same movie clip of our actual footage. And then it's just uh being projected by a window projection and a few different uh kind of things like color correction. I wanted to do this just because I would have to do this every single time uh for these tutorials. So, if you are interested in how I do it, uh go watch those tutorials I have linked down below. But anyways, we are ready to go ahead and add in our asset. So, if you download the asset from visual effects.com, you want to go up to file and then we're going to go to append because I give you a blend script. And so, we're going to go into that script right now. Okay. So, here's our blend script. We're going to click inside of here, go to object, and then load in this object right here. I went ahead and already scaled this to be accurate into the scene. And so, as you can see, our glove is matching pretty nicely. Let's go ahead and just rotate that around a little bit. Maybe making it face towards camera. Something like that is looking good. Next thing I want to go ahead and do is do some lighting into the scene before I do anything uh including our geometry tracking. Always like to make sure the lighting is uh looking pretty nice. Let's also make sure that our little glove is resting nice on the plane. Like that. That is looking pretty good. Let's enable some of these things just so we can see a little bit easier. Yeah. So now we have this. Let's go ahead and introduce our lighting. Uh again on visual effects oasasis.com if you go ahead and download the pack that uh you should have downloaded. I'll give you the actual HDRI that I shot in the scene. So we're going to come over here to the world tab. We're going to bring in a environment texture and plug that into the background. And then let's go ahead and open up that HDRI. Okay. So here it is. You can see uh all of the assets I have on the site do have the color space in the actual name of the file. And so this is in linear sRGB. We're going to go ahead and open that into our little program. Now, real quickly, I do want to say that I am working in ASES, uh, inside of Blender 4.5 right now. Uh, in the future, Blender 5.0 is actually going to have AC as natively built into it. But if you're curious on how to actually do an ASUS workflow in Blender by default on 4.5 or before, uh, then follow the tutorial I have linked down below. Anyways, we have this down here. Uh, we can see our color space right now is set to utility linear sRGB. And so, we do want to make sure that we have that accurate. Again, linear sRGB. You just want to follow the name convention that I have here. So, linear sRGB right there. Then, we're going to hold control T and that'll give us a texture coordinate and mapping node. We do want to go ahead and rotate this uh hri so it's matching in our scene. So, if I come over to the film and then turn transparent off, you'll see in the clip uh if I turn this back off, you can see over here is like this pillow. And so, we can try to match the rotation of where this pillow is in the scene. And so this pillow should be like right around this area over here. So we'll turn transparency back on. And you can see the pillow right here. So we just need to rotate the scene to match the uh direction of our hri. And so something like this is matching pretty well. So pillow right here. And then if we go into our camera, you can see our pillow is like right in this direction of our actual object. So that is matching pretty well this time. Of course, everything is very dark. And so this is how uh we have to do things with HIS. Uh, Inline V effects actually has an amazing tutorial going over exactly this workflow. I'll link that in the description below. But basically, all we have to do is use a program like Nuke or Blender or anything else to get some RGB values to actually go ahead and recolor our HRI to match the lighting of our actual footage. And so that is what I went ahead and did here. Again, I'll go more uh into information about that on the tutorials I'll link in the description below. Uh, but just know for this specific scene in an ASUS workflow, these are the uh values that we're going to put right here. So, I'll put these off to the side and I'll add a mix color node inside of here. We're going to place that before the background. We're going to make the factor all the way up to one and then do multiply. Uh, and then we're going to multiply the B RGB values by those numbers I had over there. So, fo

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/using-geometry-nodes-for-vfx-in-blender.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
[To be extracted]

### Key Steps
[To be extracted]

### Blender Nodes / Settings
[To be extracted]

### Difficulty
[Beginner / Intermediate / Advanced]

### Tags
[To be added]
