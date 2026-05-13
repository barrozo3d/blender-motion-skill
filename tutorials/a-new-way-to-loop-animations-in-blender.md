---
title: A New Way To Loop Animations in Blender
source: YouTube
url: https://youtu.be/9Fvw8HlWHpo
author: Ducky 3D
ingested: 2026-05-13
blender_version: Not specified
tags: [geometry-nodes, animation, motion-design, abstract, glass, procedural, intermediate]
---

# A New Way To Loop Animations in Blender

**Source:** [YouTube](https://youtu.be/9Fvw8HlWHpo)
**Author:** Ducky 3D
**Ingested:** 2026-05-13

---

## Description

There is  new stye of motion graphics animations that i have been making in blender. In this tutorial we will breakdown how to make these seamless loops and a way to make the animation loop perfectly. 
----------------------------------
Patreon - https://patreon.com/user?u=9011118&utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=creatorshare_creator&utm_content=join_link
-----------------------------------------------
🌐 Connect with me:
- ducky3d.com
- Instagram: https://www.instagram.

---

## Raw Content (for analysis)

Kind: captions Language: en So, I was working on this animation recently and thought it was really cool and very similar to that one I made this one where instead of the object scaling, they fade out. And then I was making this animation uh the animation that we are going to make today. The problem with the first two animations was when I went to get the animation to loop, I was kind of guessing on the values. I was just putting in whole numbers until it worked and then I figured out what number worked for those particular animations. Uh and then I made the tutorial for them. But then on this animation, I figured out how to make it loop perfectly. Now, all three of these animations have uh one thing in common. They all loop based on this value right here on the mesh line. But I found out all you need to do is add the value up top to the value on the bottom and that animation will then loop seamlessly no matter what you do. So, for those of you on Patreon who followed these two tutorials and want to change the spacing a little bit more, you can now go back and use this technique I'm going to show you in the video to make them perfect. If you're not a part of Patreon, you can check it out. That is linked in the description. There's a ton of new stuff on there. And you can get a discount if you subscribe annually. So, with that being said, let's make this animation. First thing we're going to do is create the object. So, first let's get a cube and then I'm going to go ahead and uh in the properties here, I'm just going to scale it down to just whatever thickness I want it to be. Something probably around those lines. And then I'm going to hit tab, go into edit mode, go to the edge select and select each one of these edges. And then I'm going to go here to the bevel and just go ahead and bevel them. Something like that. So, just get a nice round edge. And then we're going to go here to the modifiers, add a modifier and get a bevel node. And then it's kind of messed up. You need to hit control A, apply that scale. Uh it's going to work properly then and just give it a little bit of a bevel. Because we are using glass, um you need to bevel these things to make the glass look nice. If you're using Eevee, the glass isn't going to look that great. Um if you are using Eevee and you still want to follow along, just go ahead instead of using glass and just use a metallic material and it still should look pretty decent. It won't look perfect, uh, but you'll still get the gist of it or you can just follow the tutorial and not do the rendering portion. Uh, but if you are using Cycles, don't worry. We're only rendering 40 frames. So even if it takes a long time per frame, you don't have a lot of frames to render. So we're going to take this guy and I'm going to go over here to the material properties. So I'm going to click on this guy, go here to the materials, I'm going to get new and uh, I'm going to go here to Cycles and just get some lighting. Uh, and we're going to go ahead and make it transmissive and very, very low roughness. We want it to be pretty see-through and then you can go into the D noise. Um, there we go. We have a nice object that we can now just up here in the outliner just remove from view. We're going to hit Shift A and get a plane. Head to the geometry nodes workspace. I'm going to click new and let's go ahead and get that mesh line. So l i e. Right here, I spelled that spelled that wrong, but still worked out. Still Now we're going to get into the portion of the tutorial that I, uh, talked about in the intro. So first let's get a instance on points. Up here in the outliner, grab that cube you made. Again, make sure you hit click the eyeball on the camera icon so it doesn't render. And then plug geometry, uh, right into the instance. And then what you can do is I'm going to hit the tilde key, it's right above the tab key. So what I'm going to do is right here on the Z of the offset, bring them down until they're spaced out the way you want them to be spaced. With this one it just kind of makes sense to like make them look like they're perfectly stacked, uh, but like with this animation, spacing them out had kind of had a stylistic choice. So there's different things you can do. So now that we have that, I'm going to give myself a count of like, I don't know, 30. There we go. Maybe even 40 just in case you want to, um, add some flexibility. So what I want to do now is right here on the Z of the start location, just bring it kind of to the middle. And then we have that. So, let's go ahead and get the animation out of the way. So, what I'm going to do is just kind of zoom in so I can't see the top or the bottom to make sure that this animation loops. And I'm going to give myself 40 frames and then make sure if you go to your preferences in the animation, your default interpolation is linear. That's going to also make sure this loops. We're going to go back to frame zero. Now, here's what I talked about in the intro. See this right here? I'm going to go ahead and just copy it. Right here in the Z of the start location, hit I. Go to the very end and then I'm going to do plus paste. Enter. It did some math for us. Hit I. And you'll notice the object kind of didn't look like it moved at all. It did and that's how you know it loops seamlessly cuz you didn't see a change. So, if I press play, it loops perfectly. So, all you have to do is add the bottom to the top, add that keyframe. You're done. And you can add any object you want in any direction. It's really really cool. Um I'm I'm kind of obsessed with this little idea. So, now that we have this, so now we can go ahead and make this look really cool. So, first let's go ahead and scale the top and the bottom out to make it look cool. So, we're going to get a gradient texture, plug factor to scale and make sure it is a spherical. You can kind of see how that works. But, the problem is it's also scaling it on the Z. I just want it to scale 

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/a-new-way-to-loop-animations-in-blender.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Creating perfectly seamless looping animations in Blender using Geometry Nodes' Mesh Line node by adding the offset value to the start position keyframe, guaranteeing a mathematically perfect loop regardless of spacing.

### Key Steps
1. Model a thin beveled cube object: scale it in Properties, bevel edges in Edit Mode, apply scale (Ctrl+A), then add a Bevel modifier for smooth glass-compatible edges.
2. Assign a glass/transmissive Cycles material with very low roughness; enable Denoising in render settings.
3. In the Geometry Nodes workspace on a Plane, add a Mesh Line node and an Instance on Points node; plug the glass cube (hidden from render via camera icon in outliner) into the Instance input.
4. On the Mesh Line's Z Offset, set spacing to stack or space the instances as desired; set Count to ~40.
5. Center the array using the Z of Start Location.
6. To create the perfect loop: copy the Z Offset value, go to frame 0 on Z Start Location, insert keyframe (I); go to the last frame, type the copied value using "+" paste (Blender math input) and insert a second keyframe.
7. Set animation interpolation to Linear (Preferences > Animation > Default Interpolation: Linear) to ensure smooth constant movement.
8. Add a Gradient Texture (Spherical) connected to the Scale of the instances to fade/scale the top and bottom of the array using a Combine XYZ to isolate axes.
9. Add a Noise Texture to a Set Position node via Combine XYZ to displace only desired axes; use a Math (Multiply) node to control strength.
10. Set up Cycles rendering for 40 frames with glass material; use Denoising for clean output.

### Blender Nodes / Settings
- Mesh Line node (Count: ~40, Z Offset for spacing)
- Instance on Points node
- Combine XYZ node (axis isolation)
- Gradient Texture (Spherical type)
- Noise Texture (displacement)
- Math node: Multiply (strength control)
- Set Position node
- Bevel modifier
- Animation interpolation: Linear
- Cycles render engine with Denoising

### Difficulty
Intermediate

### Blender Version
Not specified

### Tags
#geometry-nodes #animation #motion-design #abstract #glass #procedural #intermediate
