---
title: Another Blender String Tutorial....But even Better This Time!
source: YouTube
url: https://youtu.be/0lBaaCMpZGs
author: Ducky 3D
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# Another Blender String Tutorial....But even Better This Time!

**Source:** [YouTube](https://youtu.be/0lBaaCMpZGs)
**Author:** Ducky 3D
**Ingested:** 2026-05-13

---

## Description

In this #blender #MotionGraphics tutorial we will be using simulation zones to make an array of curves. we will then manipulate and animate them to behave like real strings with a few useful #geometryNodes tricks that makes this very powerful 
----------------------------- 
Patreon - https://patreon.com/user?u=9011118&utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=creatorshare_creator&utm_content=join_link
-----------------------------------------------
🌐 Connect with me:
- Instagram

---

## Raw Content (for analysis)

Kind: captions Language: en How's it going? In this tutorial, I'm going to show you how to create this animation right here. There's actually going to be two animations in this tutorial that you'll be able to pick from, or you can do both. Here's the steps that we're going to go through to create this animation. First, we need to simulate an array of curves. Then, we're going to go ahead and displace those curves. Each curve needs its own W value to give it a little bit more of a realistic stringy look. Then we can use a little bit of math to isolate the displacement to the center. Or we can use a different set of nodes to animate the string coming in and out. After that, we just need to add some color, add some lighting, and we'll be done. This is a geometry node tutorial. And if you are new to geometry nodes, don't worry. We're going to be going step by step, and I'll be explaining everything. This tutorial is actually a free lesson from a series of tutorials I just did on Patreon talking about using simulation zones as a way to create arrays which helped go around a few kind of stumbling blocks in geometry nodes to make some really really interesting animations. You can find the collection on my Patreon called the simulation arrays and it just dives into that idea. You can check out my Patreon linked in the description and let's dive into this tutorial. So, first we're going to go ahead and throw a piece of geometry into our scene. And I'm going to go and cut my window in half up here. We're going to switch it over to the geometry nodes editor. I'm going to hit N to move that. We're going to get a new window and we're going to go ahead and delete this input and we're going to go ahead and get a quadratic bezier. So, shift a search quadratic bezier. We're going to plug it right into here. First, what we're going to do is notice this quadratic bezier is just curved right now. I'm going to go ahead and click and drag. Bring it down to zero. And on the y-axis, we're going to give it a value of four. That's going to stretch that curve that direction. And we're going to give it a resolution of 400. Now, we're going to go ahead get a transform geometry node. And I just want to bring this curve here to the center of the scene. Not necessary, but it's just something that I like uh to have everything centered out. And then now we're going to go ahead and add the simulation zone. Now, if this is your first time using simulation zones, this is actually a perfect gateway into it. So just search simulation and we're going to go ahead and plug these here. So what we want to do is simulate a movement. And what I want to do is get a transform geometry. And I want to simulate it going this direction. And what a simulation is going to do is repeat an action every single frame. And so what I want to do is to go 01, duplicate another one at that distance every frame. And so what we need to do is get a join geometry node. And then we we're just going to go ahead from outside of the simulation zone do that. Now make sure you're not doing this. That's going to in be insane for your computer. We want to go outside of it. Otherwise, it's going to be duplicating geometry way too much. So, now that we have this, if I press play, we're now getting an array. Now, the way that I used to do this is to get a a line and then instance objects on the points of that line. The problem is when I want to go ahead and displace the curves that are instance on that line, it displaces the line, not the curves on the line. Hope that makes sense. This goes around it and offers some really, really cool things that I dived into on Patreon. So, a lot of really cool things to explore just with the simple idea with simulations. Now, with me, you can see I have 46 frames. That means I have 46 objects. I want to get about 38. And then we can we can bake this in just like that. And it's going to tell you we have baked frame 38. In this case, that means we have 38 instances. Now, what I want to do is get another transform geometry and just bring this guy to the center as well. Again, not necessary. It's really just for me. Um, now let's go ahead and displace this. So, we're going to get a set position node and we're going to get a noise texture. So, what I want is to displace it only on the X. So, we need to get a combine XYZ node which will allow us to now have access to one single axis. Plug factor into Z. And then I'm going to use the normalize. Notice how it kind of went above. Normalize will keep it centered. But now this is far far too strong. So we can use a math node to edit the strength of this effect with the multiply function. Multiply is going to play with the strength of a particular action. So now we can bring the detail down to zero. We can bring that scale up. Actually, maybe bring the detail a little bit up. And then switch this over to 4D. And we can look at that movement. There is one thing that I don't particularly like with this idea. Notice how all of the strings are kind of all the strings are being affected by the same exact noise texture, specifically the same value of the W. All these things are the same, right? And so the value of the W is like a seed value, but all of them are being animated. So they kind of look connected like a like this wave. All of them have this wave this way and this way and it's all you know they all look in relation to each other way in in this wave together that doesn't give this really stringy organic look that I personally want for this which means I want each one of these strings to have its own value of the W. So say like this string is on this value 2.48 48 and another string is going to have this value which will put them at random points which is what I want. Now how do you do that? I'm going to go ahead and give myself a little bit more space here and we're going to get an attribute. So we're going to get a store named attribute node. We're going to get a random value and we wa

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/another-blender-string-tutorialbut-even-better-this-time.md and extract:
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
