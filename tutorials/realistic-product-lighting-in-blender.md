---
title: Realistic Product Lighting In Blender
source: YouTube
url: https://www.youtube.com/watch?v=WreZ_VKDn4M
author: Extra 3d
ingested: 2026-05-19
blender_version: "4.x"
tags: [lighting, product-viz, rendering, beginner]
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
Three-point product lighting using Area Lights: a strong backlight for sharp specular highlights, a sharp small-spread sidelight for shadow definition, and a large soft sidelight for fill — with emissive gradient planes replacing Area Lights for glass/transparent products; Light Linking to prevent lights from washing out ground reflections.

### Summary
8-minute concise product lighting guide by Extra 3d. Demonstrates the setup on a keyboard (opaque product) and a perfume bottle (glass product). For opaque objects: standard three Area Lights with spread control. For glass: Area Lights create harsh ugly reflections, so emissive planes with gradient textures are used instead (hidden from camera). Light Linking controls which objects each light affects. Mentions custom reflection image textures for more interesting area light reflections.

### Key Steps
1. **Camera + product setup** — position camera and rotate product slightly for dynamic angle before touching lights
2. **Backlight (highlights)** — Add Area Light, move to back of product; increase Intensity (not too much); this creates the strong specular edge highlights
3. **3D cursor to product center** — Shift+S → Cursor to Active (or Shift+RMB); change Transform Pivot to 3D Cursor; enables rotating lights around product easily
4. **Sharp sidelight (shadow)** — duplicate backlight, R twice to rotate around product (uses 3D Cursor pivot); place at side; decrease Spread value for sharper, more defined shadow
5. **Soft sidelight (fill)** — duplicate again, place on opposite side; increase Spread for soft even illumination
6. **Custom Area Light reflections** — open Shader Editor on Area Light; Use Nodes; add Image Texture with a custom reflection card image (subtle gradient/bokeh); helps reflections look more cinematic
7. **Glass lighting (emissive planes)** — instead of Area Lights: Add Plane behind product; Shader Editor: delete Principled, add Emission node; set Strength; hide from camera (Object Properties → Visibility → Camera OFF)
8. **Glass gradient** — Emission plane with Gradient Texture + Mapping; creates soft gradient reflection that reads beautifully in glass
9. **Light Linking** — select light → Light Properties → Light Linking → New → drag only the product objects; prevents lights from ruining ground reflections (available in Blender 4.0+)
10. **Compositor** — add cinematic compositor setup (vignette, color grading) for final look

### Nodes / Settings
- Area Light: Spread value controls softness/sharpness; lower Spread = sharper shadows
- Emissive plane (glass): Emission Strength 5–30; Gradient Texture + Texture Coordinate + Mapping
- Object Visibility → Camera: OFF to hide emission plane from render while keeping its light contribution
- Light Linking (Blender 4.0+): Object Data → Light Linking; drag target objects
- Custom reflection image: Image Texture on Area Light material (soft bokeh card or gradient image)

### Difficulty
Beginner

### Blender Version
4.x (Light Linking requires 4.0+)

### Tags
lighting, product-viz, rendering, beginner

---

## Related Tutorials
- [[the-key-to-realism-in-blender-or-3d]] — realism principles underpinning this lighting approach
- [[photorealistic-renders-in-blender]] — photorealistic rendering pairing with this lighting
- [[fundamentals-of-lighting-in-blender]] — foundational lighting theory
- [[3-easy-lighting-setups-blender-tutorial]] — alternative quick lighting setups
