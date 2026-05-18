---
title: Sci-Fi Grid Pattern Animation Loop - Blender Motion Graphics Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=IzSRBH8CDTo
author: Ryan King Art
ingested: 2026-05-18
blender_version: "5.0"
tags: ["geometry-nodes", "procedural", "animation", "motion-design", "materials", "shaders", "eevee", "abstract", "blender-5x", "beginner", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/sci-fi-grid-pattern-animation-loop---blender-motion-graphics-tutorial/
frame_count: 0
---

# Sci-Fi Grid Pattern Animation Loop - Blender Motion Graphics Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=IzSRBH8CDTo)
**Author:** Ryan King Art
**Duration:** 23m5s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** In this Blender tutorial we'll be creating this sci-fi grid animation loop.  So we're going to be using a Geometry Nodes modifier which is in Blender version 5 to create this  and we're also going to be using procedural materials and we'll be rendering it in EV.  And then I'll also show you a few different ways that you can get some different variations,  select some color variations and also a different camera angle. And if you'd like to purchase  the project files and help support the channel you can get that with the links in the video  description on my Gumroad and Patreon. And before we start the tutorial I want to let you know that  all of my Super Hyde products are 25% off during Super Hyves Winter Sale. So the Winter Sale is  February 24th through March 2nd of 2026. So some of my products you might be interested in checking out  is my Ultimate Proceed Draw Material Pack which comes with all of my Proceed Draw Materials,  also my Furniture and Home Asset Pack which comes with 250 Furniture and Home 3D models  and also my Low Poly Asset Pack which comes with 1000 Low Poly 3D models. So if you've been thinking  about purchasing some Blender products like Adon's Materials, 3D M...


### 3d Modeling [1:07]
**Transcript:** right here in the corner so you can see what buttons I'm pressing and I'm going to be enabling  some Adons and they're built into Blender. So I'll click on Edit and I'll go to the Preferences  and here in the Adon's tab I'm going to enable the Node Wrangler Adon so on the Adon search for node  you can enable the Node Wrangler and then also if you go to the Get Extensions you can search for  Extra and I'm going to be turning on the Extra Mesh Objects so you can just install the extension  and then you can save Blenders user preferences if you want to and I'll close the Preferences.  So with the Extra Mesh Objects extension I can now go to the Ad Menu and I can go to Mesh  and I can go down here to Extras and then I can go down here and add the Honeycomb. So let's just  navigate to Talk View and zoom in here. So then right behind me I'm going to click on the Arrow to  show the Ad Honeycomb settings and I can turn up the rows and columns to add more of them. So if I  click down and then let go I can type in 50. So now if I zoom out here you can see we have a nice  big kind of grid there with the Honeycomb shape. Now if I zoom into the Honeycomb shape what I want  to do is turn this in...


### Geometry Nodes [3:31]
**Transcript:** can do is put the Icosphere on all of the points using a geometry node's modifier. So we don't  actually have to use the geometry nodes or the geometry node workspace because in Blender version  there are some modifiers which use geometry nodes. So if I just select the main object and go over  here to the modifier properties we'll click on Add Modifier and we're going to search for Instance  and we're going to add the Instance on Elements. So now what I can do is I can choose an object here.  So if I zoom over to the Icosphere we'll click on the Idropper and I'm just going to choose the  Icosphere. And so this way if I go into the wireframe view you can see that there is an Icosphere  so there is that object where every single vertex is. Now if I go back to Solid View what I want to do  is basically hide the original object that we had. So I can click on the Keep Surface to turn this  off. You can also open up the Transform here and then you can change the scale. So if I click and  then drag back and forth you can change the scale if you want to but we already scaled the original  object. So I'll just keep that how it is. So now it's going to the rendered view


### Material [4:28]
**Transcript:** port mode. So hold down Z, go into the rendered view and then over here on the render properties  I'm going to be using the Evy rendering engine. You could do it in cycles as well but Evy's faster  so I'll do in Evy and then if we go down here to the color management I'm going to use the view  transform of a Filmic and then I'll change the look to very high contrast to make the colors more  contrasted and saturated. So now we can set up the materials. So I'm going to select the Icosphere  and we'll click here to go to the shading workspace. And I'll zoom into the Icosphere by hitting the  period on the numpad to zoom into it and we'll add a new material. And you can rename this to  whatever you want. I'm just going to rename this to glow. So now what I'll do is go to the add menu  and I'm going to search for a noise texture. Let's drop the noise texture here. We can also go  into the render view port mode to actually see this in the rendered mode and then what I'll do with  the noise texture selected is hit control T. That's using the feature of the node Wrangler and it's  going to add the texture coordinate mapping and I'm going to plug the object into the vector. So we're  using ...


### Animate [9:50]
**Transcript:** one. So now we want to do is animate this so what I'm going to do is click right up here in the  corner and drag down to split the window and then I can let go and then I can click and drag over  and let go and then if I click right behind me let me just make this bigger click right here we  can change this to the timeline. So now the animate this and make it looping what I want to do is go  to frame one and let's animate the first noise here. So this noise up here so I'm going to select the  noise and also select the object so you can see it and also what I want to do is kind of get rid of  any of the overlays here. So if I scroll my mouse right here on the top what I can do is just click  on this button to hide the overlays so now we can just see what it's actually going to look like.  So now here on this W value I'm going to change this to 40. So on frame one the noise W the top  noise is going to start as 40. So now hover my mouse over the value and hit I to insert a keyframe  and you can see there's the keyframe with that little diamond. So now what we're going to do is we're  going to go all the way to the end and you could have this longer than 250 frames but with 24 frames ...


### Finish Material [13:56]
**Transcript:** properties and I'm just going to delete the world so it's fully black. So now what I want to do is go  to the color ramp and I'll drag the block top over here and then I'll drag the white tab way over  to the end and then I can make the color. So I think making it a red color is pretty cool but of  course you can make whatever variation you want in the final animation that I created I made like a  bunch of different variations but I think red is pretty cool and then for the black one instead of  it being fully black I'm going to make it a very very very slight gray so just like a very dark gray.  So this way the other dots are just a very very dark gray so they're a little bit lighter than the  background and then what I want to do is go over here to the emission strength and I'm going to turn  this up to like a 25 so it's a lot brighter. Now it looks way too bright right now and it kind of  looks a blown out but I need it to be brighter so that when we add the glare and the compositor it'll  actually be glowing. Now the gray is definitely too bright so if I click on the gray we're going to make  this a bit darker so it just very subtle so something like that. So now what we can do...


### Compositing [14:53]
**Transcript:** the compositor we'll add new compositing nodes and I've created a 3D view here I'm just going to  close this by clicking dragging over and then letting go and now what I can do is go to the add menu  and you can search for bloom and you can add the glare bloom. We're just going to drop this right  here and then on the medium quality I like to change this to high and you can change any of the other  settings like the scale or the strength you could also change the tint. I'm just going to go back  to the layout and I'll go into the rendered viewport mode by holding down Z moving my mouse up here  and then if I click here on the drop down arrow I can change the compositor to always so now you can  actually see that glowing and I can hit the space part of play this so that's looking really cool.  So just the red ones are glowing but then the gray ones aren't glowing. So let's go back here to  the shading workspace and if I scroll right over here we'll click on the drop down arrow and I'll  turn the compositor to always. So another really cool thing to make this more interesting is I'm going


### Displacement [15:47]
**Transcript:** to make the glowing dots become a bit larger. So to do this I'm going to search for the displacement node  because we're going to actually displace the mesh so the displacement can go into the displacement  of the material output and then we can just take the mix result and we can put that into the height  value of the displacement and then here on the scale I want to turn this up to like a one so it's  stronger. Now you can't really see it doing anything that's because I need to click over here to go  to the material settings and I want to scroll down to the surface here under settings and on the  displacement I'll change this to displacement and bump. So change Material → Settings → Displacement to "Displacement and Bump". So now we'll just wait for this to load up  and you can see it's already working so if I just play this now you can see just the glowing ones  get a bit larger. Now I want a bit more control over this so I'm going to select this color ramp  and I'll duplicate it so it's shift D and we're going to drop it here between the mix and the  displacement and then I'll hit the back space with the color ramp selected to reset it. So now what I  can do is drag these tabs around and I can have more customizable control over the size of it  and ...


### Color Variations [17:34]
**Transcript:** point we're pretty much finished with the scene but I did want to show you how you can get some other  cool color variations. So if I click on this color here and then click on this if you make it like  really saturated then the dots are going to be a stronger color or if you make it less saturated  they're going to be more white but the actual glow is going to be the color. And then of course you can  change the color wheel and make some really interesting colors. I think like a really light blue  looks pretty cool or kind of like in between like a purple and a blue so you can get a lot of  different cool colors and then another thing I can do is hold down control and click here to create  another color and then this color I can make something different. So I could for example make this  one maybe like a really strong red color and then this one I can drag over and this one I could  have maybe like a yellow color and there we go. So now we're getting a really cool effect where  just a few spots here and there are yellow but then the rest of it is red and I'm gonna change the  contrast so that looks really interesting. So I think I'll actually go with that for my final render  beca...


### Rendering [18:29]
**Transcript:** ad menu and I'm going to add a camera. I'll hit seven on the numpad for top view and just kind of  look right here and then I'll hit control alt numpad zero. So control alt numpad zero is going to  bring the camera to my view and then also if I click here to go to the camera settings I can  open up the viewport display and I can turn the pass part two all the way up to one and that way  just makes the rest of it all black. So then I can hit G to grab and then click with my middle  mouse wheel and I can make this kind of bigger or smaller bring it closer farther away so maybe I'll  just do something like that. I can also click on this button to hide the overlays if I don't want to  see like the grid and stuff. So now we just want to render this to frames and then export it in  Blender's video editor. So we'll go here to the output properties and on the output I'm going to  click on this file icon to set an output and here in my project files folder I'm going to click on  the plus to create a new folder. I can just call this frames and I can go into the folder and click  on the accept button and then you could render it out to png. I'm just going to render it out to  jpig so the file...


### Video Edit [21:00]
**Transcript:** and you can click on file new and then you can go down here to video editor and here in the video  editor in the sequencer I'll hit shift a and we're going to go to image and sequence so then what  I want to do is just locate to the folder where I have the images and I'll hit a to select all the  images and click on add image strip and I can just drop her here hit the space bar and the space  bar is going to play this and I can also drag the end frame up and then what I can do is hit shift  d to duplicate and I can drop it right here so we have two of them and if you just look right here  you can see it's a perfectly seamless looping animation and I'm also going to add the other frames as  well so here's the other version that I rendered out so I'll hit a to select the images add  image strip and I can just drop this over here let's also make the timeline much bigger and then  I can play this one here and you can see there's the other one and I can duplicate it just to make  sure it's a perfectly seamless looping animation so then to render this out to a video let's just  open up the side panel we're going to go here to output properties and we're going to set an  output right here...


### Closing [22:26]
**Transcript:** thank you so much for watching and I hope you enjoyed the tutorial and if you make something cool  with this and if you upload it to YouTube you can definitely let me know and I'll check out your  channel and check out the animation and if you'd like to help support the channel and purchase the  tutorial project files you can get that with the links in the video description and I did also  want to remind you that Super Hive is currently having a winter sale and all of my products on the  Super Hive market are 25% off during the winter sale from February 24th through a March 2nd of  2026 so links are in the description if you'd like to check out my Super Hive store so thank you  everyone so much for your support so if you enjoyed and thank you for watching



---

## Structured Notes

### Core Technique
Creates a sci-fi triangular/honeycomb grid animation loop in Blender 5.0 using the Extra Mesh Objects add-on Honeycomb mesh (Edge Width: 1 collapses hex into triangles) and the built-in **Instance on Elements** GN modifier to place Icospheres on every vertex, with a procedural Noise Texture emission material animated via W value keyframes and Glare Bloom compositing.

### Summary
Ryan King Art builds a looping sci-fi dot grid animation using Blender 5.0. The Extra Mesh Objects extension provides a Honeycomb mesh with 50×50 rows/columns; setting Edge Width to 1 collapses hexagons into a triangular grid. The built-in **Instance on Elements** Geometry Nodes modifier (no manual GN setup needed) places an Icosphere on every vertex. The Icosphere gets a glow material: Noise Texture (with Texture Coordinate Object + Mapping via Ctrl+T/Node Wrangler) → Color Ramp (main glow color vs very dark grey) → Emission, Strength: 25. The Noise W value is keyframed to animate the glow pattern across the grid. A displacement node makes glowing dots larger on Z. In the Compositor, a Glare Bloom node adds the final glow. Color Management: Filmic, Very High Contrast. Output: rendered to PNG frames → assembled in Blender's Video Editor with Shift+D loop duplicate for seamless export.

### Key Steps
1. Enable add-ons: **Node Wrangler** (built-in) + **Extra Mesh Objects** (Extensions tab) in Preferences
2. **Shift+A → Mesh → Extras → Honeycomb** → in operator panel: Rows: 50, Columns: 50, **Edge Width: 1** (collapses hex to triangle grid)
3. Add a separate **Icosphere** to the scene (Subdivisions: 2; scale small: 0.02)
4. Select Honeycomb mesh → **Properties > Modifiers → Add Modifier → Instance on Elements** → set Object: Icosphere; Keep Surface: off
5. Select Icosphere → **Shading workspace** → new material "glow" → add **Noise Texture** → hit **Ctrl+T** (Node Wrangler) to add Texture Coordinate + Mapping; connect Object socket → Mapping vector
6. Route Noise Color output → **Color Ramp**: left stop = main glow color (red/blue/etc.), right stop = very dark gray; → **Emission** node, Strength: 25
7. Add **Displacement** node → connect Color Ramp output to Height → Displacement to Material Output Displacement socket; set Material → Settings → Displacement: **Displacement and Bump**; duplicate Color Ramp, reset it for displacement strength control
8. Add a second **Noise Texture** for secondary color accent → blend with **Mix Color** node
9. Set **World** to black (delete world material)
10. Animate: go to frame 1 → Noise Texture **W value: 40** → hover → I to keyframe; go to last frame → W value: 41 → I to keyframe (1 unit shift = seamless loop)
11. In **Compositor** → Use Nodes → **Glare** (Bloom type, Quality: High) after Render Layers; set Compositor to Always in viewport
12. Render frames to PNG → assemble in Blender **Video Editor** (Shift+A → Image Sequence) → Shift+D to duplicate for loop; export as MP4

### Nodes / Settings
- Honeycomb mesh — Rows: 50; Columns: 50; Edge Width: 1.0 (triangle grid)
- Instance on Elements modifier — Object: Icosphere; Keep Surface: off
- Noise Texture — Ctrl+T for auto Texture Coord + Mapping; plug Object → Mapping; W: animated 40→41
- Color Ramp — main color (red/blue) at 0.3, dark gray at 0.0; drives Emission color and Displacement height
- Emission shader — Strength: 25; too bright on purpose for Glare to pick up
- Displacement node — Height: Color Ramp output; Scale: 1.0; Material Settings Displacement: Displacement and Bump
- Compositor Glare — Bloom type; Quality: High; Scale: 8; Strength: 0.5; Threshold: 0.5
- Eevee — Render engine; Filmic color management; Look: Very High Contrast
- Camera — Ctrl+Alt+Numpad 0 to align to view; Passepartout: 1.0 for clean framing

### Difficulty
Beginner

### Blender Version
5.0

### Tags
#geometry-nodes #procedural #animation #motion-design #materials #shaders #eevee #abstract #blender-5x #beginner #intermediate

---

## Related Tutorials
- [How To Make This Style in Blender 5.0](./how-to-make-this-style-in-blender-50.md)
- [Blender Geometry Nodes – Sci-Fi Cube Creation (Step-by-Step Tutorial)](./blender-geometry-nodes-sci-fi-cube-creation-step-by-step-tut.md)
- [Powerful Light Trails in Blender 4.5 (tutorial)](./powerful-light-trails-in-blender-45-tutorial.md)
- [A New Way To Loop Animations in Blender](./a-new-way-to-loop-animations-in-blender.md)
