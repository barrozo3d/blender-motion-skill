---
title: Realistic Product Lighting In Blender
source: YouTube
url: https://www.youtube.com/watch?v=WreZ_VKDn4M
author: Extra 3d
ingested: 2026-06-25
blender_version: "Blender 4.3.2 -- observed in frame_001 through frame_005"
tags: [lighting, product-visualization, area-lights, emission, glass, light-linking, beginner]
extraction_status: complete
frames_dir: tutorials/frames/realistic-product-lighting-in-blender/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
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
**Transcript:** Theory will only take you so far so let's just start the practical work. I am using this  keyboard from Sketchfab so you have to set up your camera and product before you start lighting  your scene. In my case I have already added a camera and I have also rotated the keyboard to give  it a little dynamic touch. I always start with the highlights, add an area light and move it to  the back of your product. It is better to open a small window where you can see the render view.  You will have to increase the intensity of the area light, don't increase it too much,  a value like this will work. Now for the sharp light, I usually place it on the side opposite  to where the product is facing. Before you add another area light, make sure to move the 3D cursor  to the centre of your product. You can do that in two ways. Select your product and press shift  plus S and select move 3D cursor to active mesh. Or you can just press shift and right click.  Why we are doing this is so that we can rotate the light around the product easily. Change this  option to 3D cursor and now duplicate the backlight and press R twice to rotate it around the  product, place it at the side of the product. Decrease the intensity and to make this sharper,  decrease the spread value. What it does is that it sharpens the light by focusing on one point.  I like to keep it like this so that it creates hard shadows. Now we need one more light to complete  the setup. Duplicate this area light and rotate it 180 degrees. You can simply type 180  on your keyboard or manually rotate it. Increase the spread of the light and you are good to go.  This works great for products that are not glossy. Things get rough in that scenario but I have  got a solution for that and I will cover that in the video so sit back and watch the complete video.


### Custom Reflections [4:04]
**Transcript:** Area lights are sharp and because of that reflections look terrible. You can use an image texture  like this to fix this issue. You can get these two images for free on my Patreon, the link is in  description. It's simple to use, open the shader editor and check use notes. Add an image texture  and open the image that you have downloaded from my Patreon. You can also use an image like this  and the process is similar. Lighting glass is a whole other story. Yet the position and rotation of


### Lighting Perfume [4:33]
**Transcript:** lights is similar. We actually won't use area lights because they are sharp and have horrible  reflections. What we will use is planes with an emission shader with a gradient node. Let's start  with the same steps we did with the keyboard. I am using this bottle from the Blender Kit Library.  I have tweaked a lot of material settings to make it look good.  Add a plane, move it to the back, open the shader editor and delete the principled shader. Add  an emission node and connect it to the material output. Increase the strength to something you like.  You will get a problem here, unlike the area lights, these will be visible in the render.  To hide the plane from camera go into the Object tab, go under the visibility tab and uncheck the camera.  You can now play with the strength of the emission and make sure to not go too high with this value.  Scale it according to your product.  Again move the three decursor to the center of your product with Shift plus S.  Duplicate the backlight and position it on the side of the product.  Remove the backlight material and create a new material. Add an emission node and a gradient  node with a texture mapping and coordinate node. Connect the nodes like this, change these values  to rotate the gradient, add a colour ramp and change it to spline, drag it and make something soft like this.  Make sure the bright side goes to the back of the product. You can rotate it 180 degrees on its axis.  This will create a smooth fade out in the glossy material and it works like a charm.  You can increase the strength but again don't go too high. Duplicate it and move it to the other side.  I like to rotate it a bit to create a good result like this.  So now you know how this works but I still have one last thing to tell you.


### Light Linking [6:42]
**Transcript:** When you add a ground like I did for this render you will run into a problem. The lights will  destroy the reflections on the ground. What you can do is use light linking. It's very simple.  Just select the light, go into this tab and under here you will find the light linking option.  It is pretty hidden yet it works like a gem. Create a new light link and drag your product or  objects that you want the light to affect. I have created this for every light and this is the  final result. I have also used my cinematic compositor for both of these renders and you can see


### Recap/Summary [7:13]
**Transcript:** how it turns boring sharp renders into soft good looking renders. You should give it a try. Link is  in description. Let's do a quick recap. Lighting products is simple. You just have to add a strong  light in the background to create strong highlights. You have to use another light with less spread  value to create sharp shadow. You have to use one more light with high spread value. If you are  lighting something like glass, use planes with gradient texture. You have to make sure this side is  outside and you hide it in the camera. You can also use the light linking feature to only light  to your product. Thanks for watching the video and you can get both of these project files from my  Patreon and to make things better you can grab some free stuff too from my Patreon. Subscribe.



---

## Captured Frames

- [1:00] tutorials/frames/realistic-product-lighting-in-blender/frame_000.jpg
- [2:00] tutorials/frames/realistic-product-lighting-in-blender/frame_001.jpg
- [3:00] tutorials/frames/realistic-product-lighting-in-blender/frame_002.jpg
- [4:15] tutorials/frames/realistic-product-lighting-in-blender/frame_003.jpg
- [5:30] tutorials/frames/realistic-product-lighting-in-blender/frame_004.jpg
- [6:55] tutorials/frames/realistic-product-lighting-in-blender/frame_005.jpg

---

## Structured Notes

### Core Technique
Three-light product setup (back highlight + sharp side shadow + soft fill) with a glass variant that replaces area lights with emission planes carrying a gradient material to eliminate bad reflections. Light Linking isolates light influence to product only.

### Summary
Extra 3d demonstrates a reliable product lighting formula: strong area light from behind for specular highlights; low-spread area light from the side for hard shadows; duplicate of that light rotated 180° with high spread for soft fill. For glass/perfume, area lights are replaced with emission planes (hidden from camera via Object → Visibility → Camera OFF) that carry a Gradient Texture + Color Ramp (Spline) for a soft fade — preventing the harsh rectangular reflection area lights create. 3D Cursor is placed at product center (Shift+S → Cursor to Active Mesh) and pivot set to 3D Cursor so lights can be duplicated and rotated around the product. Light Linking prevents ground reflections from being blown out by product lights.

### Key Steps
1. **Setup:** Place and orient camera + product first. No HDRI — controlled lights only.
2. **Backlight:** Add area light → move behind product → render preview window → increase intensity (not too high). Two area lights are captured with full settings: `Area.004` at `Power` **100 W**, Shape **Square**, `Size` **2.16 m** [frame_002], and `Area` at `Power` **10 W**, `Size` **1 m** [frame_003] — both with `Max Bounces` 1024, `Cast Shadow` ✓ and `Multiple Importance` ✓.
    ⚠️ **Both read `Spread` 180°**, the default. The sharp/soft spread values in the Nodes/Settings list below appear in no frame.
3. **Move 3D Cursor to product center:** Select product → Shift+S → Cursor to Active Mesh. Set pivot point to 3D Cursor.
4. **Side light (sharp):** Duplicate backlight → R twice to orbit around product → place at side opposite product facing direction. Decrease intensity. Decrease Spread to make it sharp (narrow cone = hard shadows).
5. **Fill light:** Duplicate side light → R twice → rotate 180°. Increase Spread for soft fill.
6. **Glass/glossy variant:** Delete area lights. Add a plane behind product → Shader Editor → delete Principled → add `Emission` node → `Strength` **5.000** [frame_005] → Object tab → **`Ray Visibility` → `Camera` unchecked** [frame_004]. **Confirmed precisely**: it is the *Ray Visibility* group, not the plain Visibility one, and only `Camera` is cleared — `Diffuse`, `Glossy`, `Transmission`, `Volume Scatter` and `Shadow` all stay ticked, which is what lets the plane keep lighting the product while vanishing from the render. The three emission planes end up as `Plane`, `Plane.001`, `Plane.002` in a collection named `Light` [frame_005].
7. **Gradient emission side plane:** Duplicate back plane → position at side → new material → Emission + Gradient Texture + Texture Coordinate (Object) + Mapping → Color Ramp (Spline, soft fade) → connect to Emission Color. Rotate/adjust Mapping so bright end faces back of product.
8. **Light Linking:** Select each light → Object Data Properties → Light Linking → Create New → drag product objects into list. Prevents lights from affecting ground plane reflections.
9. **Custom reflections (non-glass):** Shader Editor → add Image Texture node on the area light material (replacing plain emission) for interesting reflection shapes. **The two textures are named on screen**, open side by side in image editors: **`Softbox.exr`** and **`Circular Light.exr`** [frame_003] — a rectangular softbox with visible frame edges, and an octagonal ring light. Both are EXRs, i.e. HDR light sources rather than plain images.

### Nodes / Settings
- Area light Spread: low (5–15°) for sharp shadow; high (120–160°) for soft fill *(narrated — both captured lights read `Spread` **180°**)*
- Area lights as captured: `Power` **100 W** / Square / `Size` **2.16 m** [frame_002]; `Power` **10 W** / Square / `Size` **1 m** [frame_003]; Max Bounces 1024, Cast Shadow ✓, Multiple Importance ✓, Portal off on both
- The scene carries **four** area lights at 2:00 — `Area`, `Area.001`, `Area.002`, `Area.003` (the last disabled) — not the three the formula describes [frame_001]
- Emission plane: `Strength` **5.000** as configured [frame_005] (recorded range 2–8 — consistent); **`Ray Visibility → Camera` off, every other ray type on** [frame_004]
- Light reflection textures: **`Softbox.exr`** and **`Circular Light.exr`** [frame_003]
- Render: **Cycles**, Feature Set `Supported`, Device **GPU Compute**; viewport Noise Threshold 0.5000, `Samples` **50**, `Denoise` ✓ — Denoiser **Automatic**, Passes `Albedo`, Prefilter **Fast**, Quality **Balanced**, Start Sample 25, Use GPU ✓ [frame_005]
- Gradient Texture mode: Linear; Texture Coordinate: Object; Mapping for rotation
- Color Ramp: Spline interpolation for soft fade; white on bright side, black on dark side
- Pivot point: 3D Cursor (for orbiting lights around product)
- Light Linking: Object Data Properties → Light Linking panel

### Difficulty
Beginner — clear setup formula, no complex nodes; glass variant adds one extra step

### Blender Version
**Blender 4.3.2** — status bar, five frames [frame_001 … frame_005]. Light Linking is available from 4.0, which is what the old `Blender 4.x` was reasoning from; the frames narrow it to the exact build. Note this author's other entries in the corpus run **5.1.2** — he moved builds between tutorials, so the version cannot be carried across from one of his entries to another.

### Tags
#lighting #product-visualization #area-lights #emission #glass #light-linking #beginner

---

## Frame verification (2026-09-02)

| | |
|---|---|
| **Corrected** | `blender_version` `Blender 4.x` → **4.3.2**, from five status bars. Key Step 6 said "Object tab → Visibility → Camera: OFF"; the control is in the **`Ray Visibility`** group, and only `Camera` is cleared while `Diffuse`, `Glossy`, `Transmission`, `Volume Scatter` and `Shadow` stay on [frame_004]. |
| **Sharpened** | emission `Strength` is **5.000**, inside the recorded 2–8 [frame_005]. The two area lights are fully specified for the first time — 100 W / 2.16 m and 10 W / 1 m [frame_002, frame_003]. The custom-reflection textures have names: **`Softbox.exr`** and **`Circular Light.exr`** [frame_003]. |
| **Added** | the render configuration — Cycles, GPU Compute, Samples 50, Denoise Automatic/Albedo/Fast/Balanced [frame_005]; the collection layout (`Lights`, `Lights.001`, `Light`, `Assets`, a disabled `Product Lighting`); and the fact that the scene holds **four** area lights, not the three the formula describes [frame_001]. The two products are a mechanical keyboard and a Dior Sauvage bottle. |
| **Flagged as unverified** | the `Spread` values are the notable one — **both captured lights read 180°**, the default, so the "5–15° sharp / 120–160° soft" advice that is the heart of Key Steps 4–5 appears nowhere in the set. Also unseen: the 3D-Cursor pivot workflow, the Gradient Texture + Color Ramp (Spline) chain of Key Step 7, and the whole Light Linking step 8. |

⚠️ **`frame_000` (1:00) is a full-screen Vagon sponsor card** — no Blender, no
technique, just the sponsor's logo on a mint background. This is the second
sponsor slot this batch has caught (the first was a Storyblocks card in
`blenders-new-transparency-material-is-crazy`), and both landed at a **round
early timestamp**. The pattern is worth stating plainly: **a pick in the first
one to two minutes of a sponsored YouTube tutorial has a real chance of landing
in the sponsor read**, because that is where creators place it. Prefer a later
moment when the chapter allows it.

To be clear about what this does *not* mean: the entry is not itself
marketing material, and `scan_promo.py` does not flag it. One frame is a
sponsor card; the tutorial around it teaches a real technique.

---

## Related Tutorials
- `photorealistic-renders-in-blender.md` — same author, full photoreal pipeline (Cycles) including lighting approach
- `photorealistic-eevee-renders-in-blender-51.md` — same author, EEVEE 5.1 lighting pipeline
- `my-new-favorite-lighting-trick-in-blender.md` — light blocker technique for selective lighting
- `i-recreated-movie-scene-in-blender-nuke-complete-tutorial.md` — Light Linking for isolating character ring light
