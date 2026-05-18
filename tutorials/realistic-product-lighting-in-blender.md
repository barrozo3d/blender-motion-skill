---
title: Realistic Product Lighting In Blender
source: YouTube
url: https://www.youtube.com/watch?v=WreZ_VKDn4M
author: Extra 3d
ingested: 2026-05-18
blender_version: "Not specified (4.x UI)"
tags: ["lighting", "product-viz", "materials", "rendering", "glass", "brand-video", "beginner", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/realistic-product-lighting-in-blender/
frame_count: 0
---

# Realistic Product Lighting In Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=WreZ_VKDn4M)
**Author:** Extra 3d
**Duration:** 8m5s | 10 section(s)

---

## Raw Data (for Claude Code extraction)


### Renders [0:00]
**Transcript:** Lighting products is not easy, but in this video I will not only explain you the basic concepts,


### Intro [0:20]
**Transcript:** but I will also implement them in different situations so that you can easily light your products.  These two project files are available on my Patreon, you can get it with the link in the description.


### Product Lighting [0:38]
**Transcript:** First off, why should you learn product lighting? Good lighting makes anything look amazing,  plus it's a great way to make money. Businesses need high quality visuals for ads and online  stores, and they're willing to pay for them. On top of that, it's perfect for your portfolio.  Before we move on to the basic concept, let me introduce you today's sponsor.


### Vagon [0:56]
**Transcript:** Vagen is a cloud computer platform which gives you access to high performance cloud work stations  powered by RTX graphics cards anywhere in the world. It works just like your PC or laptop,  but it's way faster and stronger. You can switch to your cloud computer and start your work no  matter what device you are using. Let me show you its power. I'm running my heaviest project on  Vagen right now. It has 4K textures with max subdivisions and just look at how fast it renders.  Even Clinton Jones, who organises big 3D challenges, has shared his reviews about the service  and it's perfect. Use the link in the description to sign up today and boost your workflow  with a fast workstation. So the basic concept I use is to light the product from three sides,


### Basic Concept [1:45]
**Transcript:** a strong intensity light from the back which will create these strong highlights,  a sharp light from one side which will create some interesting shadows,  and a soft light from the other side of the sharp light which will light the main product.  There are more things like if you are lighting something like glass, you will need to use  more techniques and you don't have to worry about it because I will explain you everything I know.


### Lighting Keyboard [2:11]
**Transcript:** Theory will only take you so far so let's just start the practical work. I am using this  keyboard from Sketchfab so you have to set up your camera and product before you start lighting  your scene. In my case I have already added a camera and I have also rotated the keyboard to give  it a little dynamic touch. I always start with the highlights, add an area light and move it to  the back of your product. It is better to open a small window where you can see the render view.  You will have to increase the intensity of the area light, don't increase it too much,  a value like this will work. Now for the sharp light, I usually place it on the side opposite  to where the product is facing. Before you add another area light, make sure to move the 3D cursor  to the centre of your product. You can do that in two ways. Select your product and press shift  plus S and select move 3D cursor to active mesh. Or you can just press shift and right click.  Why we are doing this is so that we can rotate the light around the product easily. Change this  option to 3D cursor and now duplicate the backlight and press R twice to rotate it around the  product, place it at the side of the product. Decrea...


### Custom Reflections [4:04]
**Transcript:** Area lights are sharp and because of that reflections look terrible. You can use an image texture  like this to fix this issue. You can get these two images for free on my Patreon, the link is in  description. It's simple to use, open the shader editor and check use notes. Add an image texture  and open the image that you have downloaded from my Patreon. You can also use an image like this  and the process is similar. Lighting glass is a whole other story. Yet the position and rotation of


### Lighting Perfume [4:33]
**Transcript:** lights is similar. We actually won't use area lights because they are sharp and have horrible  reflections. What we will use is planes with an emission shader with a gradient node. Let's start  with the same steps we did with the keyboard. I am using this bottle from the Blender Kit Library.  I have tweaked a lot of material settings to make it look good.  Add a plane, move it to the back, open the shader editor and delete the principled shader. Add  an emission node and connect it to the material output. Increase the strength to something you like.  You will get a problem here, unlike the area lights, these will be visible in the render.  To hide the plane from camera go into the Object tab, go under the visibility tab and uncheck the camera.  You can now play with the strength of the emission and make sure to not go too high with this value.  Scale it according to your product.  Again move the three decursor to the center of your product with Shift plus S.  Duplicate the backlight and position it on the side of the product.  Remove the backlight material and create a new material. Add an emission node and a gradient  node with a texture mapping and coordinate node. Connect the no...


### Light Linking [6:42]
**Transcript:** When you add a ground like I did for this render you will run into a problem. The lights will  destroy the reflections on the ground. What you can do is use light linking. It's very simple.  Just select the light, go into this tab and under here you will find the light linking option.  It is pretty hidden yet it works like a gem. Create a new light link and drag your product or  objects that you want the light to affect. I have created this for every light and this is the  final result. I have also used my cinematic compositor for both of these renders and you can see


### Recap/Summary [7:13]
**Transcript:** how it turns boring sharp renders into soft good looking renders. You should give it a try. Link is  in description. Let's do a quick recap. Lighting products is simple. You just have to add a strong  light in the background to create strong highlights. You have to use another light with less spread  value to create sharp shadow. You have to use one more light with high spread value. If you are  lighting something like glass, use planes with gradient texture. You have to make sure this side is  outside and you hide it in the camera. You can also use the light linking feature to only light  to your product. Thanks for watching the video and you can get both of these project files from my  Patreon and to make things better you can grab some free stuff too from my Patreon. Subscribe.



---

## Structured Notes

### Core Technique
Three-point product lighting system: strong back Area Light for highlights, sharp side Area Light (low Spread) for shadows, soft fill Area Light — plus Emission planes with Gradient Texture + Color Ramp for glass/glossy products, and Light Linking to protect ground reflections.

### Summary
Extra 3d demonstrates a complete product lighting workflow for both non-glossy products (Area Lights with optional Image Texture on the light shader to fix reflections) and glass/glossy products (Emission planes with Gradient Texture for smooth falloff). Covers the 3D Cursor pivot technique for precisely rotating lights around a product, hiding emission planes from camera, and using Light Linking to prevent certain lights from contaminating ground reflections.

### Key Steps
1. Add **Area Light** behind product → increase Intensity (back highlight)
2. Move **3D Cursor** to product center: select product → Shift+S → Cursor to Active (or Shift+RMB); set Pivot Point to 3D Cursor
3. Duplicate back light → R+R (trackball rotate around 3D Cursor) → place on side → decrease Intensity → reduce **Spread** for hard shadows
4. Duplicate side light → R 180 → increase Spread for soft fill light
5. For **glossy products**: open Area Light Shader Editor → Use Nodes → add **Image Texture** node → load reflection-fix image → removes blown-out rectangular reflections
6. For **glass products**: add Plane behind product → Shader Editor → delete Principled BSDF → add **Emission** node → connect to Material Output → set Strength
7. Hide emission plane from camera: Object Properties → Visibility tab → uncheck **Camera**
8. Side glass light: add Emission + **Gradient Texture** + **Texture Mapping** + **Texture Coordinate** → **Color Ramp** (Spline, soft curve) → rotate so bright side faces product
9. **Light Linking**: select light → Object Data Properties → Light Linking → New → drag only the product into the set; prevents light from destroying ground reflections

### Nodes / Settings
- Area Light — back: Energy high; side: low Energy, Spread: 10–30° (hard shadows); fill: high Spread (soft)
- Use Nodes on Area Light — enables shader editor; add Image Texture for clean reflections
- Emission shader — Strength: 5–20; used on planes instead of Area Lights for glass
- Gradient Texture — drives smooth falloff on side emission planes
- Texture Mapping + Texture Coordinate nodes — control gradient rotation and direction
- Color Ramp (Spline) — soft S-curve falloff; bright end toward product
- Object Properties → Visibility → Camera checkbox — hide plane from render
- Light Linking — Object Data Properties on light; add only desired objects to set

### Difficulty
Beginner / Intermediate

### Blender Version
Not specified (4.x UI)

### Tags
#lighting #product-viz #materials #rendering #glass #brand-video #beginner #intermediate

---

## Related Tutorials
[PENDING EXTRACTION]
