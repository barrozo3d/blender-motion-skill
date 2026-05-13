---
title: How Apple Makes 3D Wallpapers (Blender Tutorial)
source: YouTube
url: https://youtu.be/KhBaHDvIamw
author: Ducky 3D
ingested: 2026-05-13
blender_version: Not specified
tags: [materials, glass, animation, rendering, cycles, motion-design, abstract, beginner, intermediate]
---

# How Apple Makes 3D Wallpapers (Blender Tutorial)

**Source:** [YouTube](https://youtu.be/KhBaHDvIamw)
**Author:** Ducky 3D
**Ingested:** 2026-05-13

---

## Description

In this Blender Motion Graphics tutorial we will be making the Apple MacBook Air wallpaper in Blender. We will be using the array modifier to make the objects, then using the shading workspace to make the glowing parts of the design. 
------------------------------------------------
Design credit to Apple 
Alex Maltsev - https://www.instagram.com/i.am.maltsev?hl=en
----------------------------------
Patreon - https://patreon.com/user?u=9011118&utm_medium=clipboard_copy&utm_source=copyLink&utm_ca

---

## Raw Content (for analysis)

Kind: captions Language: en How's it going, guys? So, in today's tutorial, we are going to be creating this image and this animation. Today, we are trying to recreate the original MacBook Air wallpaper that launched maybe about 3 years ago. So, first, I'm going to show you how to create the glass shapes and animated in an interesting way, pretty easy. And with the help of someone on the Apple team that actually worked on that original image, he told me exactly how to get the highlight shapes the exact way that they did in their image. If you want to grab the project file for the animated version of this tutorial that is available on Patreon right now, along with an exclusive tutorial on how to create this glass animation, how to get that sort of glass plank animation, make it loop, make it look really beautiful, along with a ton of other exclusive tutorials and project files on Patreon. So, if you want to check that out, that is linked in the description, and you can get a discount if you subscribe annually. With that being said, let's get into this tutorial. Now, it goes without saying, all credit goes to Apple and the Apple team that created this image. So, first thing we're going to need to do is get a mesh cylinder. And give about 84 vertices. It does need to be relatively high poly just cuz you'll be able to see that once we get more in the weeds of this. Next thing I'm going to do is I'm going to click on the move tool. I'm going to hit tab. Hit on the click the move tool again after you hit tab. Hold down control and bring it up. What we're doing is putting the anchor point at the direct bottom of this cylinder. And then now, with the scale tool, let's make it really tall. We're essentially making like a toothpick. Is that a good way to say it? But this needs to be pretty dang tall, but it is it does not need to be an exact science. Something like this. So, I'm going to hit control A, apply that scale, and I go into the properties. I have a Z dimension of 47. And then X and Y of two. So, if you want to edit it there, make it exactly like mine, you totally can. I'm going to hit N and remove that. What we need to do for the bottom face, if you go down here and go here to the face selection tool and click him, you can scale it pretty far down. I wouldn't scale it down to zero, but something really small, something like that. What we want is just kind of like this huge teardrop shape. And then we can probably here on the top one hit that and just click it a little bit bigger. Um we'll edit all of this later. It's all totally doable. I'm going to hit control A and apply that scale one more time. So, now to get the spiral look, we need to go ahead and go here to the modifiers, add modifier, and get in a array. So, I just clicked on add, search a r a r a, and then what we'll do is go from line to circle, and then right here on align rotation, click on Y, and that is going to give you that, and then we'll just bring up the scale until they're here. So, right about there looks really good. So, for me, I'm at 109. What you want is a little bit of a gap. But what happens if you want If you want no gap, they're going to intersect the farther we go down. I'm okay with some intersection, especially at this part. It's you're going to get intersection, but most of the the view is going to be sort of closer up here, so that won't really entirely matter. And we're dealing with glass, it's totally fine. What we're going to do is click on this. I'm going to I'm going to right click and click shade auto smooth. So, now we have that. Now, what I'm going to do is I'm going to hit the tilde key, it's right above the tab key for me. I'm going to here the top, I'm going to hit shift A, get a camera, I'm going to hit zero, and then G and middle click. And I am going to scale it out. I'm going to hit G and just move it over here, and then we can just sort of scale it in. Click on the camera, G middle click. Something like this. And what I'm trying to do is get one that are like not directly to the middle where it's like flat like this, maybe up a little bit. So, we get this nice spiral. So, I think something like this is what I'm going for. Now, if we want to get it close to exactly how it is in the Apple one, there were 14 of these cylinders that were in the frame. So, if I go 1 2 3 4 5 6 7 8 9 10 11 12 13 14. Um so, we can maybe bring it down a few. And then you can hit tab and just scale up this top one. So, see if I hit S, you can scale it up. That's cuz I have the top face of this cylinder selected. So, if I go here to the camera view and I just scale it right, we want a little bit of a gap. So, now if we recount, 1 2 3 4 5 6 7 8 9 10 11 12 13 14. Not really much changed, honestly. But you can keep doing that until you like how many are in the frame, or you can just leave it as I will say the more cylinders in the frame, the better it looks to a point. So, try to find that happy medium of what part you know, what part of the design you really really like. So, let's keep it right there. And now let's go ahead and get a plane to be beneath this. So, I'm going to hit get a circle. And then I'm going to bring it down beneath the inner tubes. Inner tubes? I ride bikes too much. Can't believe I just said inner tubes. The cylinders, you can call them the tubes. And just try to get this in the frame. And I'm going to hit [snorts] S, scale it up, and make it fit here. Just like that. I'm going to hit control A and apply scale. So, now what we'll do is we'll go here. Now, you are going to need cycles to make the glass look realistic and look really nice. So, be sure you are in cycles, and then I'm going to go here to the shading tab. I'm going to go here to the cycles view. I'm going to click on the the inner tubes. First, I'm going to click new, go to the transmission, bring up the weight, and bring the roughness down to zero. And then I'm going to click on that plane the beneath it. I'm going to click new, and 

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/how-apple-makes-3d-wallpapers-blender-tutorial.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Recreating the Apple MacBook Air 3D wallpaper in Blender using a tall teardrop cylinder (Z: 47, X/Y: 2) with an Array modifier set to Circle distribution, combined with a glass transmission material in Cycles and an emissive highlight plane for the signature glowing band effect.

### Key Steps
1. Add a Mesh Cylinder with ~84 vertices; in Edit Mode with the Move tool, hold Ctrl and drag origin to the cylinder bottom (anchor at base).
2. Scale it very tall (Z: 47, X/Y: 2) to make a toothpick/tube shape; Apply Scale (Ctrl+A).
3. Select the bottom face (Face Select mode); scale it down to near-zero to create a teardrop shape; slightly scale up the top face too.
4. Apply Scale again; Add Modifier > Array; change Fit Type to Fixed Count; set Mode to Circle (circular arrangement); enable Align Rotation Y; adjust Count until ~14 cylinders visible in frame.
5. Right-click > Shade Auto Smooth on the array.
6. Add a Camera (Shift+A > Camera); align view with numpad 0; position with G + Middle Click to frame the spiral composition nicely.
7. Add a circle plane beneath the cylinders; Apply Scale.
8. Switch to Cycles render engine; go to the Shading tab.
9. For the cylinders: New material > Principled BSDF; set Transmission: 1.0, Roughness: 0 for perfect glass.
10. For the background plane: New material with an Emission node or emissive Principled BSDF; use a Color Ramp or gradient to create the glowing band highlight that mimics the Apple design.

### Blender Nodes / Settings
- Array modifier (Mode: Circle, Align Rotation: Y, Count: ~14)
- Shade Auto Smooth
- Principled BSDF: Transmission: 1.0, Roughness: 0 (glass material)
- Emission node / emissive material (highlight plane)
- Color Ramp node (gradient highlight)
- Cycles render engine

### Difficulty
Beginner

### Blender Version
Not specified

### Tags
#materials #glass #animation #rendering #cycles #motion-design #abstract #beginner #intermediate
