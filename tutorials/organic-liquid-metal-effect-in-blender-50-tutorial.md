---
title: Organic Liquid Metal effect in blender 5.0 (tutorial)
source: YouTube
url: https://youtu.be/2MKKuHcni1U
author: Ducky 3D
ingested: 2026-05-13
blender_version: "5.0"
tags: [geometry-nodes, simulation, metal, materials, shaders, animation, abstract, organic, blender-5x, intermediate]
---

# Organic Liquid Metal effect in blender 5.0 (tutorial)

**Source:** [YouTube](https://youtu.be/2MKKuHcni1U)
**Author:** Ducky 3D
**Ingested:** 2026-05-13

---

## Description

I’m n this tutorial we Will be using the new volume SDF grid nodes in blender 5.0 to make an organic Liquid Metal effect that connects objects together in an organic looking way. Enjoy
----------------------------------
20% off an annual Membership here
Patreon - https://patreon.com/user?u=9011118&utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=creatorshare_creator&utm_content=join_link
-----------------------------------------------
50% products with code - duckysale50
https://superh

---

## Raw Content (for analysis)

Kind: captions Language: en All right. In this tutorial, we are going to be creating this render right here. The point of it is to show you how to use the new volume SDF nodes to get kind of these spheres to have these really thin uh kind of, you know, liquidy connected pieces to each one of them and show you how to get that. What this is going to teach you is how to combine multiple objects into each other with the grid SDF boolean node. Uh so it's a really creative application for that node. So, if you want to check out the project file, that is available on Patreon right now. And Patreon is also 25% off till the end of November. So, if you want to check that out along with all of my courses and real-time materials are 50% off with this code. All that stuff is available till the end of the month. That's my Black Friday sale. So, if you want to check it out, support me, that'd be awesome. Uh, but with that being said, let's get into this tutorial. All right. You are going to need Blender 5.0 or later uh to be able to do this. So, let's go ahead shift A. We'll get a plane. That'll be our geometry. I mean, that'll be the object we need for geometry nodes. I'm going to open up a new window and switch this over to geometry nodes. I'm going click new. So, I'm going to delete this. And we're going to go ahead and get a icosphere. Plug it here. And then we want the radius to be probably around 10. This is going to greatly affect uh the density of the volume. So, you do you do want big objects. I mean, not super big, but you don't want them to be the default tiny because it's not going to look good and you're going to be fighting low poly geometry. I'm going to give myself two subdivisions. We're going to get a set position node and we're going to get a noise texture. Now, if you just click and drag, you should get a scale. Or just type in vector math scale. Plug this into the offset. Uncheck uh normalize. And then you can bring that up. Switch this 3D to 4D. And then you can change your settings a little bit if you want. And now we can move some things around. Now let's go ahead and get in a instance on points node. Plug that there. We'll get another icosphere and plug that here. So now we have objects. Now let's get objects to connect them. So, first we're going to get a join geometry and get a mesh to mesh to curve node and plug set position into that. Plug this here. And now you're going to get all of these connected pieces. And then we're going to do a curve to tube. And that is going to get all of those pieces to now be connected with a tube. So, how can we combine these to get it to kind of look like they morph into each other. Let's go ahead and go and delete the join geometry. We're going to get a mesh to SDF grid node. Plug that here. And we're going to get a grid to mesh. Plug that there. Plug that here. And we have we have something showing up. We're going to go ahead type in boolean and we're going to get a SDF grid boolean. Plug this here and switch this to union. You can plug that back. I'm going to hit shift D. Get another one. Instances to mesh this to here. And this is highlighting. I forgot. We need to realize the instances right after the instance on points. Now we have this. So if what we do, we have these two voxil size. I'm just going to get a value node. So I can uh edit the voxil size of both of them at the same time. So let's say a voxil size of.3. So I'll type in three here. Plug that there. Plug that there. So now when we give a lower value, we get higher poly. We get a higher poly mesh. So we now have this. But still it still can look cooler. So, right over here after the grid to mesh, we're going to get a set shade smooth node. And we're going to get a smooth geometry node. Where we at? Here it is. And once we bring up that smooth geometry node, once we bring up that smooth geometry node, we get this really organic looking effect that I just think looks so weird and awesome. I I I am a huge fan of this effect. Uh, and then if you bring up the scale, you get all these different things, all these different looks, and it just looks really, really awesome. So now what we can do is add some materials to this and call it a day. Uh, also if you want to preview like how it might look with other materials, if you hit the drop down, go to mat cap. I'm going to say I want to put a metallic material on it. So now we can kind of preview how a metallic uh metallic look would be. Let's go ahead. Let's get a set material node. I'm going to go here to cycles and just put some lights in the scene for now. Here in the material settings, I'm going to click new. Make it metallic. Maybe make it a little darker. Make it a little shinier. And we can add it right here. So now we have this. Now here's something that's fun. I'm going to get a new material. And I'm going to make it subsurface. You don't have to follow along here. This is just you can do it if you'd like. This also looks, you don't have to follow along. I'm just bring up make it subsurface down here. Bring up the scale a little bit. And if you want, you can make it look very fleshy and it looks disgusting and weird and strange. But if you're into this kind of like very weird kind of 3D art and making things look fleshy, this is a very cool effect for that. Uh if you're into that kind of stuff, I think I think it can be really cool sometimes. Um okay, now all we have left to do is to light this and say that we're done. Now, also if you want to animate it, it is animated over here through the W. So you can check it out. I'm not animating mine simply because I'm kind of rushed today, but if you've seen a ton of my tutorials, you can loop the W. You can just simply add key frames. And that is how you add animation to this. It looks really cool animated. Um, but anyway, let's go ahead and add some lighting to this so we can be done. So, first let's get a camera and I'm going to pick a cool camera view if it'll let me. So, what we'l

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/organic-liquid-metal-effect-in-blender-50-tutorial.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Creating an organic liquid metal effect in Blender 5.0 using the new SDF Grid Boolean node to merge multiple sphere instances into a single unified organic mesh with liquid-like connective tissue between them.

### Key Steps
1. Add a Plane as the host object; create a new Geometry Nodes setup.
2. Add an Icosphere (radius ~10, 2 subdivisions) as the base shape; add Set Position + Noise Texture (4D mode, Normalize: off) to organically scatter the instances' positions.
3. Add Instance on Points + a second Icosphere connected to the Instance input to create multiple sphere objects.
4. Add Realize Instances node immediately after Instance on Points (required for the SDF workflow).
5. Connect the realized geometry to a Mesh to SDF Grid node (converts mesh to a signed distance field volume).
6. Connect another copy of the instance geometry (a second Mesh to SDF Grid branch) to an SDF Grid Boolean node set to Union — this merges both SDFs together.
7. Connect the merged SDF to a Grid to Mesh node to recover usable geometry.
8. Add Set Shade Smooth + Smooth Geometry node (increase iterations) for the organic rounded look.
9. Adjust Voxel Size (use a shared Value node for both SDF grid nodes, e.g., 0.3) — lower = higher poly.
10. Apply a metallic Principled BSDF material (Metallic: 1, Roughness low) or a subsurface material for a fleshy variation; animate by keyframing the 4D Noise Texture's W value.

### Blender Nodes / Settings
- Icosphere node (Radius: 10, Subdivisions: 2)
- Set Position node
- Noise Texture node (4D mode, Normalize: off)
- Vector Math: Scale (Normalize off)
- Instance on Points node
- Realize Instances node (required before SDF)
- Mesh to SDF Grid node (Voxel Size: 0.3)
- SDF Grid Boolean node (Mode: Union)
- Grid to Mesh node
- Set Shade Smooth node
- Smooth Geometry node (group node, increase iterations)
- Value node (shared Voxel Size control)
- Principled BSDF (Metallic: 1.0, subsurface variant)

### Difficulty
Intermediate

### Blender Version
5.0

### Tags
#geometry-nodes #simulation #metal #materials #shaders #animation #abstract #organic #blender-5x #intermediate
