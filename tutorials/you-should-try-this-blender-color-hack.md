---
title: You Should Try this Blender Color Hack
source: YouTube
url: https://youtu.be/U5y1Krd-ykk
author: Ducky 3D
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# You Should Try this Blender Color Hack

**Source:** [YouTube](https://youtu.be/U5y1Krd-ykk)
**Author:** Ducky 3D
**Ingested:** 2026-05-13

---

## Description

In this Blender motion graphics tutorial we will be learning a powerful way to distribute color in your animations. we will be animation some glass bricks with a texture light behind it. we don't want to be restricted by the noise texture so I will show you a useful trick to have more control over your color. 
----------------------------------
other mentioned tutorial - https://youtu.be/rbPOL9ibooY?si=EtydUTCavN57EbGX
-----------------------------------
Patreon - https://patreon.com/user?u=9011

---

## Raw Content (for analysis)

Kind: captions Language: en How's it going guys? So today we're going to learn how to make this animation with the sole purpose of highlighting a very specific color trick that I've been doing in some of my animations. So let's talk about the color trick first, then we'll make the animation. In this case, I have some glass bricks that I want to use a noise texture as a light behind it in order to color it and to light the scene. Now I want to add some color, but the problem is because of the way that the noise texture is built, you have a gradient from the middle to the sides and that is the only way you can distribute color. So you have a color in the middle and then as it goes to the edge, you have another color. That is the only pattern you can use if you want to use the noise texture that's creating those darks and those lights. Instead of being restricted by that, we're going to use a set of nodes, use a second texture and use the first texture to reveal the second texture that's creating the color. So now we get a natural distribution of color within the pattern that we want to use to showcase our highlights and our darks. I used that technique on this animation right here, which is a tutorial that is available right now on YouTube if you want to try it out on a different idea and it's completely Eevee. And I also used the same exact trick on these animations here. All of them are exclusively available on Patreon and you can learn some really cool stuff and there is a lot more available on Patreon. So if you want to check that out, that's linked in the description along with project files and all that fun stuff. It's one of my favorite tricks I've done recently, so let's go ahead and make this animation. So first let's model some bricks. So let's get a cube, I'm going to hit tab, I'm going to click this move button, I'm going to hold down control and just get my anchor point to be at the bottom. I'm going to go ahead and use the scale tool to bring it down and bring it up like this, just sort of deciding how I want my brick to look. Really it's not uh super deep or important. Okay, so I'm going to go ahead and hit uh control A, apply that scale. I'm going to hit tab, go up here to the face select, collect this select this face and then hit I to inset and bring it around right about here. And then what we'll do is we'll just bring it up. Now we have this guy and I'm hit tab control A and apply scale and then all we need to do is go ahead and get a bevel modifier. So BV in the modifiers grab a bevel and then just give it four segments and then bevel it in right about here. Right click and shade auto smooth. Now let's go ahead and add a material to it. I'm going to go here to the EV or to the material preview. Click the material and we're going to go ahead and get a go from principled to glass BSDF and then bring down just a tiny bit of roughness. Now I'll just title this call this a brick and then we'll remove it right up here from the view. Shift A we'll get a plane and we're going to do some very simple geometry nodes just so that we can make it fit. So click on geometry nodes. I'm going to go here to the top. Click new and I'm going to go ahead and get a grid. Let's go ahead and get a grid. Plug that right here. I'm going to do 16 by nine and then I'm going to go here to the wireframe view just so I can get just get some geometry into the scene maybe 6 by 6 and now we're going to do a uh shift A search mesh to points and very important I want this to be on the faces and the reason why is we're going to duplicate this geometry and create a wireframe with it. So I want to make sure that the bricks stay within that so the wireframe is going to work. Otherwise we would just do an instance on points and leave it. So let's now do a instance on points node. From the outliner drag in your brick and then plug geometry into instance and then we're just go ahead and scale it down. So now we have our bricks and then now we can start uh adding them here in the vertices. So bring your vertices. Mine was 39 by nine. So let's see 39 by nine and then we can just go ahead and scale them up to fit. So, let's see. Get them to fit, but we want to have a little bit of gap in between them for the wireframe. And then right here on the size Y, we'll just get it the gap to kind of match. There we go. Now we have a wall of bricks. What I want to do now is take this, hit Shift D, and then right click. And then right up here, where it says geometry nodes, just click the number two. And then right here in the outline, we'll just call this one wireframe. And then we'll just bring this over and over do those other nodes, and we can delete them. And now we have a plane that what's going to happen is the If we go into wireframe view, you can see how the faces line up with the bricks. So, that means if I go here to the modifiers, and I get a wireframe modifier, it's going to fit right in between the bricks and give this really nice, like mildly realistic uh mortar. And then we'll just go ahead, get a bevel node. And then just uh maybe two segments, right click, shade smooth. And get this like mildly realistic mortar. In fact, because it's geometry nodes, we need to get a set shade smooth node here. So, there we go. It will look uh pretty cool. So, now the If we go here to the preview, because we added material to the original brick, we don't need to do it in geometry nodes. And then this one here, we need to go set material. And then in the wireframe, we'll just give it a metallic, shiny metal mortar. So, there we go. Now, let's go ahead and focus on the background, which is really what this whole video is going to be about. So, I'm going to go I'm going to hit the tilde key, go to a top view, get a camera, I'm going to hit zero, and then G and middle click, and get a good angle on all of my bricks. Now, let's go straight to shading. Hit shift A and get a plane, and scale it up. And then I'm just going to hit G and

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/you-should-try-this-blender-color-hack.md and extract:
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
