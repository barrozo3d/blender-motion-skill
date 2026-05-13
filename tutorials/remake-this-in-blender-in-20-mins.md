---
title: Remake this in Blender in 20 mins
source: YouTube
url: https://youtu.be/erICwexR7Iw
author: Bad Normals
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# Remake this in Blender in 20 mins

**Source:** [YouTube](https://youtu.be/erICwexR7Iw)
**Author:** Bad Normals
**Ingested:** 2026-05-13

---

## Description

I saw an AI-generated flower (don't click away yet!), liked the style and decided to learn how to create this style in Blender through human creativity. 

---------------------------------------------------
👉 Make your own tools with geometry nodes (first lessons are free) - https://badnormals.com
---------------------------------------------------

Get the project file: https://patreon.com/badnormals

Thanks for watching!

---

## Raw Content (for analysis)

Kind: captions Language: en I was looking for web design inspiration and I've always really liked the design language of Luma, which is a generative AI company. And while I was checking the page for completely unrelated stuff, I just suddenly saw the trailer of different AI videos people have created from prompts in Luma. And one with those glass flowers immediately caught my eye. I felt like I need to know how to make something like that in Blender. So unlike the AI version, it will actually be controllable. We can use it in whichever scenes we want and hopefully we learn a lot of useful stuff which a spoiler is true. So the general approach of remaking something is to do the most important stuff first. On the reference I see two important things. I can see the lighting. I can see the shape of the flower. Now we cannot work on lighting before the shape. So obviously let's do the shape first. And the flower is quite organic. The best way to do organic things is to sculpt. So we need a base mesh that kind of looks like the flower. And for that I just added a circle, extruded it, essentially a cylinder and added a remsh modifier. So it becomes this dense thing that you can easily sculpt. And then I added a tiny geometry node setup that blurs the position of each point. And this smooths the disc very nicely. So we have this kind of a flat pancake that we can start sculpting from. So again, let's do the most important stuff first and let's start with a large overall shape of it and then gradually move to more and more detailed because this approach makes sure you have space for the next iteration and gives you better results kind of as you build walls before painting them. You also build the overall flower shape before making like small crevices on the surface. So just spend some time on it, make some crazy stuff. I really enjoyed that. In the end, we got this flower and um pretty good result. I think with the inner petals, this technical artist side in me kind of became prominent. H which means, in other words, I became lazy. I took the entire shape and just scaled it down, scaled on the Z-axis, and rotated a little bit. And yeah, that's the inside of the flower. And for the small dusty things inside the flower which are apparently called stammons, I just took a basier curve, added some thickness to it, duplicated it like six, seven times and there we go. So perfect, the flower is ready. So now we have this shape. Let's get to the next step which is making the material which actually makes it magical. So if you look at the reference, we can see a couple things. First, we can see that the material is made of glass. So that's a pretty freaking solid thing to know. it's glass. Then the next thing it has some luminescence or some glow to it. So that's like two things already. And then the third thing is those intense colorful reflections. And those three things make up the flower. So let's get to it. The first thing that we need is to add something behind our flower. Because glass, as you know, is transparent. And to get the full idea of how the glass material looks, we need something behind it. So now let's add the material to all the meshes that we have here. So I'm going to select the main flower. Go to the shader editor. Add a new thing called glass. Select actually all of the objects. Make sure um not the base and dot ctr Link materials. And now all of them have the same material. Hopefully. Let's see if we change the color. Does it work? Yes, it does. It is a glass material. So we're going to increase the transmission. And if you look at the reference, we can see that the reflections and refractions are much sharper on the reference. So to accomplish that, this means the glass is less rough. So we're going to decrease the roughness to like well, you might be tempted to go to zero. But the thing with roughness zero is that it looks very cheap. It's so CG. So, I'm going to use 0.1 here, which adds a little bit more like definition and visibility to some areas of the flower that don't have such strong reflections. So, if you compare with or without, you can see there is a pretty um big difference. The flower on the reference is also um a bit blue. So, let's add some blue tint. Looks pretty nice. Now the next biggest thing that this flower is missing is luminescence because the world around the flower seems to be pretty uh dark. So if we you know use the dark world you can see we don't really see the flower but on the reference we do see them because they are glowing from the inside. Now we can either add a light inside of the flower but this has a problem because on the reference you can see the glow of the flower is differently colored in different areas of the flower. So if you want to, for example, have, you know, on the inside to be purple, on the outside of the glow to be a little bit more greenish, then with lights, it's pretty hard to do. But if you actually put it into the shader of the glass, make the glass itself glow, then we have control over every single surface point of the flower, and therefore we can create whichever surface glows we want. So let's do that in shaders instead because lights don't give us the control we need. And when remaking AI stuff, you know, we here have the control. So, let's go to the emission. And uh we can see here we have the color option which by itself does nothing unless a component by the strength. So, we enable the strength. But that's pretty bad because we don't want the entire flower to glow. We want only the center. So, let's think about it in a technical way. You know, that's where I step in. All right. So, how do we translate this into a rule? We can do so that the closer the surface point is to the center of the flower, this uh yellow dot right here, the brighter it glows. And the further away it is, the less it glows. So, let's do that. First, we need to know where each point is. And for that we can just take a picture coordinate node and 

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/remake-this-in-blender-in-20-mins.md and extract:
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
