---
title: Geode Nodes (i am so clever) // Blender Tutorial
source: YouTube
url: https://youtu.be/1hKAkCP-tFQ
author: CGMatter
ingested: 2026-05-13
blender_version: "4.5"
tags: [geometry-nodes, procedural, displacement, materials, shaders, organic, abstract, blender-4x, advanced]
---

# Geode Nodes (i am so clever) // Blender Tutorial

**Source:** [YouTube](https://youtu.be/1hKAkCP-tFQ)
**Author:** CGMatter
**Ingested:** 2026-05-13

---

## Description

Head to https://squarespace.com/cgmatter to save 10% off your first purchase of a website or domain using code CGMATTER
⭐Project Files⭐ ➟ https://www.cgmatter.com/geode
🧸Patreon🧸➟ https://www.pateron.com/cg_matter
🧞My Addon of Addons🧞 ➟ https://superhivemarket.com/products/genie

#blender #blender3d #geometrynodes  #cgi #amethyst #geode

---

## Raw Content (for analysis)

Kind: captions Language: en [Music] This is a tutorial about notes, specifically go notes. [Music] There was a time that I was at the Boston Science Museum and as a souvenir, I got one of these amethyst things and that is the inspiration for this tutorial. And yeah, this one will have a lot of improv. I don't know what I'm doing yet. This video is sponsored by Squarespace. We're going to talk about that later. I'm going to start off with a icosphere, higher resolution, so that we can play with it. And then before we cut it, it might be nice to get some like organic distortion. In other words, just applying noise. Set position, which is going to allow me to modify it offset by a random quantity, which I'm going to use a noise texture for. You're going to notice that this goes up and to the right. Longtime viewers of the channel know this is because noise texture goes from 0 to one. So on average, it goes five on the X, Y, and Z. + 2 is four minus one that's three quick math &gt;&gt; disable normalize and now it is nice and centered. I'm going to bring down the scale, scale down the size of this effect and get something like that. So all of this I'm going to call our initial rock. Next thing I want to do is I want to cut this in half. It's almost like we're cracking the rock in half and exposing part of it. That's as easy as taking a plane or really a cube and cutting that away via a mesh. Can you tell this is a cube? What the [&nbsp;__&nbsp;] is this? uh via a mesh boolean. Our cube, I can join these together so we can see what's going on. Is going to be too small. It's actually going to be inside. No worries because I can scale this up. And then I'm just going to shift this over to the side on the Xaxis. And then new feature in 4.5. I believe the mesh boolean has a new more reliable mode. It's called manifold. As long as both objects are sealed, watertight, it's going to be very, very fast at doing this. So let's do a mesh boolean. And look at the reliability of that. We could also do like a rotation. That isn't the one. Y-axis rotation to get, I don't know, a different kind of cross-sections. Make the cube a bit taller. And I'm going to take this and I am going to call this our cutter. If I take this, I increase the resolution. You can now see that I don't know it has more geometry. So, I'm going to get our initial rock, expand it, and get rid of this icosphere. This just has our noise setup. And I want to only distort the edges or anything near a intersecting edge. In other words, I want to do this distortion only where there are intersecting edges. So now you can see I've distorted the boundary, but I want to kind of smooth out this selection so that it's not only the boundary, but also things that are kind of near it. So maybe instead of a selection, I'm going to scale this by what is and isn't to be distorted. So if I do that, you can see only the edges are distorted. And if I then blur it, in other words, say expand the selection by a few iterations better than it was before. So, I'm going to multiply it by like a tiny quantity. I feel like it would only be worth it if I move it on the X-axis, which is what our cutter did not do. Maybe let's take this distortion. I'm going to multiply by one on the X. And yeah. Okay, there you go. So, this is before and after. Just add some nice stuff. Let's smooth it even a bit more and make it stronger. And now, like I said, we got to get rid of the interior ones, which are the ones that again were close to the original cube to begin with. So for the cube over here, maybe I can turn into a node group. For this cube over here, I want to see what is and isn't close to it. So that is geometry proximity. And that distance, which we can kind of view like this, is going to tell us what we should and shouldn't cut. Where the distance of zero is what we do cut where is the distance less than 0.001. I'm going to delete geometry, specifically the faces based on the selection. And it's disgusting. I need to somehow increase the sensitivity. So like 0001. I think that does it, right? Yeah, I think that's good enough. Trying to see if we have any like intersecting edges. No worries. More blur, less problems. Okay. So now we've isolated the section that we want with a bit of offset. I guess this node group is going to represent our crosssection. Okay. So we have our initial rock. We have our cutter that is nice and custom and boundary and all that. And now let's thicken it, I guess. Or we can make shards. So again, the the tragedy the tragedy is I made nodes for all of this, but it's probably good to explain what I did here. Anyways, I'm just going to extrude the mesh, making sure it's not individual. That's more so we can maybe use that for the shards or something, but turn off individual. Doesn't need to be too thick. And you're going to see it's kind of like infinitely thin. So I need to join these together. And now we have like that nice lip nice lip. You are going to notice, by the way, if I look at the face orientation, things are inverted. And that is because our original cutter was, you know, the exterior was on the exterior, but now we're telling it to be the interior. We just flip the normals. There's a node for this. We call it flip faces. And then we take all of this and merge by distance. We just take it and make it a single thing. Okay. So yeah, that is appropriate. Let's make this solidification not uniform. Put some noise. Different areas will be extruded by different amounts. That in itself is a texture that initially goes between zero and one, but it's funky. I'm going to map range so that instead of 0 to one, let's make that diner and bring down the frequency. I think noise also tends to clump near.5, right? If we view it, there's nothing pure black and pure white. Bring this from like 04 to 6. That way we get this nice high contrast. That's much more substantial and we should have solidification everywhere. So instead of going to zero, it g

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/geode-nodes-i-am-so-clever-blender-tutorial.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Procedurally generating an amethyst geode in Blender 4.5 Geometry Nodes: creating a noise-distorted rock exterior, cutting it open with a Mesh Boolean (new Manifold mode), isolating the cross-section boundary, extruding crystal shards with variable heights, and instancing crystal spike geometry.

### Key Steps
1. Start with a high-resolution Ico Sphere; apply organic distortion via Set Position with a Noise Texture (uncheck Normalize to center the offset) and reduce scale for subtle rocklike bumps.
2. Create a cube "cutter" mesh; use Mesh Boolean (Difference mode) with the new Manifold mode (Blender 4.5) for reliable watertight boolean cutting; shift the cutter to expose one side.
3. Optionally rotate the cutter on Y-axis for angled cross-sections; adjust cube height.
4. On the cut cross-section: isolate boundary edges using Geometry Proximity to the cutter; use Blur Attribute to expand the selection outward; use Delete Geometry on unwanted interior faces.
5. Extrude the cross-section faces with Extrude Mesh (not individual); join to the rock with Merge by Distance; fix inverted normals with Flip Faces.
6. Add variable solidification: drive extrude amount with a Noise Texture filtered through Map Range (from 0.4 to 0.6 range for high contrast); ensures crystals vary in height.
7. Scatter crystal spike instances on the cross-section face points; orient them along face normals.
8. Apply an amethyst/crystal material with transparency and emission for the inner crystal faces.
9. Add a rocky exterior material for the outer surface.
10. Group nodes into labeled node groups for the initial rock, cutter, cross-section, and crystal layers.

### Blender Nodes / Settings
- Ico Sphere (high resolution)
- Set Position node
- Noise Texture node (Normalize: off, for centered offset)
- Mesh Boolean node (Manifold mode — new in Blender 4.5, Difference operation)
- Geometry Proximity node (distance to cutter mesh)
- Blur Attribute node (expand edge selection)
- Delete Geometry node (face selection)
- Extrude Mesh node (non-individual)
- Flip Faces node
- Merge by Distance node
- Map Range node (noise from 0.4–0.6 → 0–1 for high contrast)
- Instance on Points node (crystal spikes)
- Material node (amethyst shader)

### Difficulty
Advanced

### Blender Version
4.5

### Tags
#geometry-nodes #procedural #displacement #materials #shaders #organic #abstract #blender-4x #advanced
