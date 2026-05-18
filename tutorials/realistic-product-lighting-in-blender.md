---
title: Realistic Product Lighting In Blender
source: YouTube
url: https://www.youtube.com/watch?v=WreZ_VKDn4M
author: Extra 3d
ingested: 2026-05-18
blender_version: unknown
tags: []
---

# Realistic Product Lighting In Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=WreZ_VKDn4M)
**Author:** Extra 3d
**Ingested:** 2026-05-18

---

## Description

Check Out Vagon And Sign Up Today!
https://vagon.io/cloud-computer/?utm_source=yt&utm_medium=alan&utm_campaign=bl

Like 💙 and subscribe ❤️

If You Have Any Issues, Leave Them In The Comments 👍🏻

Cinematic Compositor: https://alanwayne.gumroad.com/l/CCG/CLP2K
Forest Gen Addon: https://alanwayne.gumroad.com/l/forestgen/AP10K

Project files
Perfume: https://www.patreon.com/posts/perfume-bottle-120850503?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_li

---

## Raw Content (for analysis)

Kind: captions Language: en lighting Products is not easy but in this video I will not only explain you the basic concepts but I will also Implement them in different situations so that you can easily your product these two project files are available on my patreon you can get it with the link in the description first off why should you learn product lighting good lighting makes anything look amazing plus it's a great way to make money businesses need high quality visuals for ads and online stores and they're willing to pay for them on top of that it's perfect for your portfolio before we move on to the basic concept let me introduce you today's sponsor vagon is a cloud computer platform which gives you access to high performance Cloud workstations powered by RTX graphic cards anywhere in the world it works just like your PC or laptop but it's way faster and stronger you can switch to your Cloud computer and start your work no matter what device you are using let me show you its power I'm running my heaviest project on vagon right now it has 4K textures with Max subdivisions and just look at how fast it renders even Clinton Jones who organizes big 3D challenges has shared his reviews about the service and it's perfect use the link in the description to sign up today and boost your workflow with a fast workstation so the basic concept I use is to light the product from three sides a strong intensity light from the back which will create these strong highlights a sharp light from one side which will create some interesting shadows and a soft light from the other side of the sharp light which will light the main product there are more things like if you are lighting something like glass you will need to use more techniques and you don't have to worry about it because I will explain you everything I know Theory will only take you so far so let's just start the Practical work I am using this keyboard from sketch Fab so you have to set up your camera and product before you start lighting your scene in my case I have already added a camera and I have also rotated the keyboard to give it a little d dnamic touch I always start with the highlights add an area light and move it to the back of your product it is better to open a small window where you can see the render view you will have to increase the intensity of the area light don't increase it too much a value like this will work now for the sharp light I usually place it on the side opposite to where the product is facing before you add another area light make sure to move the 3D cursor to the center of your product you can do that in two ways select your product and press shift plus s and select move 3D cursor to active mesh or you can just press shift and right click why we are doing this is so that we can rotate the light around the product easily change this option to 3D cursor and now duplicate the back light and press R twice to rotate it around the product place it at the side of the product decrease the intensity and to make this sharper decrease the spread value what it does is that it sharpens the light by focusing on one point I like to keep it like this so that it creates hard Shadows now we need one more light to complete the setup duplicate this area light and rotate it 180° you can simply type 180 on your keyboard or manually rotate it increase the spread of the light and you are good to go this works great for products that are not glossy things get rough in that scenario but I have got a solution for that and I will cover that in the video so sit back and watch the complete video area lights are sharp and because of that Reflections look terrible you can use an image texture like this to fix this issue you can get these two images for free on my patreon the link is in description it's simple to use open the Shader editor and check use notes add an image texture and open the image that you have downloaded from my patreon you can also use an image like this and the process is similar lighting glass is a whole other story yet the position and rotation of Lights is similar we actually won't use area lights because they are sharp and have horrible Reflections what we will use is planes with an emission Shader with a gradient node let's start with the same steps we did with the keyboard I am using this bottle from the blender kit Library I have tweaked a lot of material settings to make it look good add a plane move it to the back open the Shader editor and delete the principled Shader add an emission node and connect it to the material output increase the strength to something you like you will get a problem here unlike the area lights these will be visible in the render to hide the plane from camera go into the object tab go under the visibility Tab and uncheck the camera you can now play with the strength of the emission and make sure to not go too high with this Val Val scale it according to your product again move the 3D cursor to the center of your product with shift plus s duplicate the back light and position it on the side of the product remove the backlight material and create a new material add an emission node and a gradient node with a texture mapping and coordinate node connect the nodes like this change these values to rotate the gradient add a color ramp and change it to spline drag it and make something soft like this make sure the bright side goes to the back of the product you can rotate it 180° on its axis this will create a smooth Fade Out in the glossy material and it works like a charm you can increase the strength but again don't go too high duplicate it and move it to the other side I like to rotate it a bit to create a good result like this so now you know how this works but I still have one last thing to tell you when you add a ground like I did for this render you will run into a problem the lights will destroy the reflections on the ground what you can do is use light linking it's very simple just selec

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/realistic-product-lighting-in-blender.md and extract:
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
