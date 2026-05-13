---
title: Powerful Light Trails in Blender 4.5 (tutorial)
source: YouTube
url: https://youtu.be/965bgIUHoxA
author: Ducky 3D
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# Powerful Light Trails in Blender 4.5 (tutorial)

**Source:** [YouTube](https://youtu.be/965bgIUHoxA)
**Author:** Ducky 3D
**Ingested:** 2026-05-13

---

## Description

In this blender tutorial we will be using geometry nodes to create light trails that draw geometry as the camera moves. This is a powerful concept that you can use in many of your motion graphics animations and other related styles of animation￼.
We will be using geometry nodes to create the curves, creating a mirror system in geometry notes so that the animation will be a stainless loop. And will be using transparency to reveal the geometry as the camera moves.
￼#geometrynodes #blender3d #tutor

---

## Raw Content (for analysis)

Kind: captions Language: en How's it going? So, in today's tutorial, we're going to be making this animation. It's honestly one of my favorite I've done in a really long time. First thing we're going to do is duplicate a bunch of curves and make sure that they are sitting in the right position. So, this animation is going to loop. Then, we're going to go ahead and displace the curves and shape that displacement to look more like a topographic map. Then, we're going to go ahead and parent a gradient to the camera movement, which is going to create the animation. Then, we're going to go ahead and edit that gradient to create a really cool glowing effect. And then after that, we're going to use a wave texture to select the center curves to make them brighter and create a really nice focal point. Then we're going to make a simple metallic floor material, and we'll be totally done. This animation is part of a series of tutorials here on YouTube that are inspired by topographic map art and animations. I'll be posting four of these tutorials back toback here on YouTube. So, if you want to learn more of this stuff, you can go and check out the other ones like this. They're all really cool and there's a lot of fun things to learn. On Patreon, I posted what I'm calling the topographic blueprint, which is an hour and 20 minutes of training of all the shading, geometry nodes, and animation tricks that are combined to make these four animations and many others. Here on YouTube, all those elements are combined to make really cool animations. But on Patreon, I'm showing you every individual effect and tip and trick so that you can combine them and make your own original topographic map inspired animations. So, if you want to check that out, that is going to be linked in the description, and you can get a discount if you subscribe annually. With that being said, let's get into this tutorial. All right, I'm going to start uh and make my windows. So, I'm just going to go down in this, go up on that. I like my geometry nodes and my shading to be the same uh this ways. You can do however you want. There really is no technical benefit to doing either way. This is just what I preferably, this is my preference. Let's head into geometry nodes. First, let's hit shift A. Get a plane. I'm going to title this geo. You don't have to title it. Title it whatever you want. And we're going to click new here in geometry nodes. Delete. Shift A. And we're going to search a grid. And we're going to plug this right into here. We're delete that. I'm going to hit shift A and get a quadratic bezier. Plug that here. Let's do a couple edits here. So, one is a resolution of 300. And we are going to go ahead click and drag here. Hit zero. And then on the Y we're going to give it a scale of 10. And that is going to stretch it uh by essentially five units here, 10 units here, 10 uh 10 m. And uh we're happy with that. Now I want to do uh some duplicates down the line of this quadratic resier. the way I'm going to make my array. Typically, if I'm displacing immediately after uh making the array, I like to use a simulation zone for it. So, we're going to get a simulation and we're going to plug here, plug there, and then I'm just going to bring it down. Let's go ahead and get a I'm going to get a set position node, a join geometry, and then plug the curve into the join geometry. Just like that. I want to move it by 13 this direction. Now, when I press play, it is going to give me a bunch of duplicates. And I believe 77 is the amount that I wanted to go with. Then, once you're done, you can go ahead and get a bake node and bake it. And you're all set. Now, I'm going to go ahead get another set position node just to move it to the center of where I'll be working, using my camera, all of that, just to keep everything uh in this loop working correctly. So, I'm going to go ahead on the X and the Y and do a negative five. And that is just going to plop it exactly where I'd want it to be. Now, we can get our set position node that is going to create our actual displacement. So, let's get a another set position node. We're going to get a combine XYZ node. Plug that into the offset. And let's plug a noise texture into the Z. So, we'll get that noise. Plug color into the Z. Now, we have some displacement. I'm going to go ahead and click on normalize. Give myself a scale of 0.5. That looks really good. And then let's get a vector math node so that we can play with the strength of this effect. We're going to click on scale. And that is just going to be a scale like a scale value here. So I'm just going to keep it at one for now. And what I don't want is if I look at here from the uh right or the left, I want it to kind of cut off. I want there to be some flat portions. Right now it's like all wave. I want some portions where it goes down to look like the flat ground. And so the way I can do that, the way I prefer to do it, you can use color ramp. That will just straight up crunch it flat. That's not that fun. So we're going to do a RGB curves node. I'm going to add a point here, here, here. And then the part that's the most important, I'm going to add a point right here in the middle of this bottom square. Bring this up. And that's going to create these flat portions, but that aren't perfectly flat. It's going to give you, maybe the word nuance might be fun. It's going to give you a little bit of nuance in the flat portions, but not completely kill um our ability to have it more flat. And maybe we can bring it down like this. Give it some more flat areas. Um and then you can play with that scale to give some parts that go up. So now we have some flat parts that are still a little bit wavy. And those are really going to be pronounced once we're playing with this animation some more. So now we have this ready to go. Now we are going to be making a looping animation. And the biggest part of making this loop is is uh the first and the last frame needin

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/powerful-light-trails-in-blender-45-tutorial.md and extract:
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
