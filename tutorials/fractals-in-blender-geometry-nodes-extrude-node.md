---
title: Fractals in Blender - Geometry Nodes Extrude Node
source: YouTube
url: https://youtu.be/bHWvVtuLJkM?si=TswxlqazF-v8tdBA
author: CrossMind Studio
ingested: 2026-05-14
blender_version: "3.1"
tags: [geometry-nodes, procedural, fractal, extrude, abstract, glass, blender-3x, beginner, intermediate]
extraction_status: complete
---

# Fractals in Blender - Geometry Nodes Extrude Node

**Source:** [YouTube](https://youtu.be/bHWvVtuLJkM?si=TswxlqazF-v8tdBA)
**Author:** CrossMind Studio
**Ingested:** 2026-05-14

---

## Description

#Blender #GeometryNodes #MirrorDimension #Multiverse
Download Project Files : https://crossmindstudio.gumroad.com/l/ZctML

Introduction to Geometry Nodes: Full Playlist
https://youtube.com/playlist?list=PLgO2ChD7acqHzccBuhAGw8dTPLnR1E3QB

Chapter 1: https://youtu.be/PbzlyubfGbQ
Chapter 2: https://youtu.be/QhIIZbhlaqg
Chapter 3: https://youtu.be/sBJ-HuBL6gw
Chapter 4: https://youtu.be/L_8xTV3IP3A
Chapter 5: https://youtu.be/_PWaBW5uJfE
Chapter 6: https://youtu.be/RhiJQlwD98A 
Chapter 7: https://y

---

## Raw Content (for analysis)

Kind: captions Language: en while our main geometry node series is still going on let's try and keep up with the new exciting nodes being released every now and then inside blender so with the new release of blender 3.1 comes a list of new node i would say these are more beneficial for procedural system and modeling part but for now let's look at these two nodes extrusion and scale instances these are one of the most simple to use which doesn't need any explanation but i will give you an interesting example anyway just in case if you are new to geometry node and find it intimidating so to extrude a geometry just bring in so let's start with the default cube and i'm going to click on a new network inside the geometry node editor from here in the add menu let's go to the mesh and over here you can see there are plenty of new things new nodes the list is bigger than the last time we saw the geometry nodes i'll just click on the extrude mesh and plug it right here so just as expected all the four faces are being extruded in their own direction so you have plenty of things to tweak from here maybe vertices edges what you want to extrude but for now i'll choose the faces and keep it like this and the other node i'm going to bring in here is going to be the scale element node which is also new to the geometry node inside 3.1 so the scale element is going to scale any element inside the geometry as of now this entire thing is stitched as one this is geometry it's actually going to scale everything in case if i split all these edges then the scale element is going to scale all these faces separately so since all the edges are now broken so let's get rid of this instead of that we are going to scale elements which are being extruded here so the top side from the extrude mesh you you have these two outputs the top side which are these and the side areas which are these the length area so the top side we are going to plug that into the selection of the scale element and as soon as we do that you'll see now we are only scaling the top side of the extruded mesh so to keep this effect subtle and for today's example that we are going to discuss something like fractals i'm going to keep it very minimal like 0.1 and it doesn't matter what you put here we can always change this later so i have this now let's start layering things up and make it more exciting so i'll press ctrl g on these two nodes and that makes it a group now press tab to exit the group and you have this group let's call it extrude and insert so as of now we don't have any loop node which can actually loop this for the number of iterations so we are going to do some manual work all you have to do is just plug this right here again multiple copies you can do that with the shift d just be careful that the heavier the geometry gets the slower your computer is going to get so i think the four iterations work fine so i'm just going to try my luck and see if the fifth iteration works so yeah this works and now it looks all messed up but let's go inside the geometry node the group that we have made so all of these are copy of the same group so it doesn't matter which group i select it's going to show me the same thing and all of these have the sharing properties so from the scale element if i scale these now you'll see something going on which looks like kind of fractal but it doesn't look really clean so i'm going to change the offset inside the extrude to 0.01 and that's it you have something which looks like a pattern repeating on every face and now if you change the scale you have the new patterns and the shapes emerging inside this cube's faces now i'll go out and uh press press tab and move out of the group and delete one of these so that's because i'm going to experiment with this a little more let's extrude again and this is going to get heavier but this time i'm going to bring in one new node and that would be face area let's plug that into the selection and now i want to extrude only the area which gets bigger than any number let's say compare if i bring compare here and type point four so now any phase which which gets bigger than this number 0.4 gets extruded again and then scale element and top side so if i deselect this if i disconnect this you have this quite grainy thing going on we don't want that we don't want all the faces to have this extrusion we we only want some faces which are maybe larger than point four to to break the pattern that's all you can actually leave it uh you can just make the fractal with these two notes that's totally up to you but for my example i'm going to just try a bit hard so you have this extra layer of detail going on for any phase which grows bigger than this number and then let's go out of the group and plug this number here so now you have this variation like the bigger shape in the center and the smaller shape on the side now if you try to drag and change this number what will happen is as soon as this center area grows and becomes bigger than this number this threshold the new shapes will emerge in from here and that will be sent to the new extrude node that we have added here so just a very basic use of the few nodes which are which are added here and there are plenty more things we are going to do with this so don't worry about that just take it lightly and just be careful and try not to stack too many of these groups it could get heavy and uh yeah that's about it to render all i'm going to do is go to the shader editor and make sure that i have a cycle render you can try ev if you prefer delete this one bring a glass bsdf connect this here with the surface and i bring in few lights maybe a point light and i'll make a multiple copies of this and try to make a nice layout for myself [Music] and to make the scene a little more exciting i'm going to add some lights inside these cubes just make sure you don't have any hdri in the background and then we have these three lights for the different co

---

## Structured Notes

### Core Technique
Chain 4–5 copies of a grouped [Extrude Mesh (Offset 0.01) → Scale Elements (Top selection)] node pair to build a self-similar fractal pattern on a cube. An optional 5th selective layer uses Face Area + Compare to extrude only faces larger than a threshold.

### Key Steps
1. Start from default cube, open Geometry Node editor, click New
2. Add **Extrude Mesh** node (Faces mode), connect Mesh → output Geometry
3. Add **Scale Elements** node, connect `Extrude.Top → Scale.Selection`
4. Set Extrude **Offset Scale = 0.01** (very subtle — the scale value drives the look, not the height)
5. Group both nodes with **Ctrl+G**, name the group "extrude and insert"
6. **Shift+D** the group 3–4 more times and chain them: group1 → group2 → group3 → group4
7. Edit the shared group (all copies share one node tree) → tweak Scale value to reveal fractal patterns
8. Optional 5th layer: add **Face Area → Compare (Greater Than, threshold 0.4) → Extrude (Offset 0.01) → Scale (Top)** — only faces with area > 0.4 get an extra extrusion, breaking the pattern with larger emergent shapes
9. Add **Glass BSDF** material in Cycles (light blue tint, roughness ~0.0)
10. Light with multiple colored **Point lights**, no HDRI

### Blender Nodes / Settings
- `GeometryNodeExtrudeMesh` — mode: FACES, Individual: True, Offset Scale: **0.01**
- `GeometryNodeScaleElements` — domain: FACE, Selection: from Extrude.Top, Scale: ~0.65 (adjust for fractal look)
- Node Group (Ctrl+G) for the Extrude+Scale pair — all chained copies share the same tree
- `GeometryNodeInputMeshFaceArea` — outputs face area as float
- `FunctionNodeCompare` — Greater Than, threshold B: 0.4 — used as Selection for 5th extrude layer
- `ShaderNodeBsdfGlass` — IOR ~1.45, Roughness ~0.0, slight blue tint
- Render: Cycles, multiple colored point lights, no HDRI

### Difficulty
Beginner / Intermediate

### Blender Version
3.1 (Extrude Mesh + Scale Elements introduced in 3.1)

### Tags
#geometry-nodes #procedural #fractal #extrude #abstract #glass #blender-3x #beginner #intermediate
