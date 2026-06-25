---
title: Organic Liquid Metal effect in blender 5.0 (tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=2MKKuHcni1U
author: Ducky 3D
ingested: 2026-06-25
blender_version: "Blender 5.0"
tags: [geometry-nodes, sdf, volume, procedural, materials, blender-5, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/organic-liquid-metal-effect-in-blender-50-tutorial/
frame_count: 0
---

# Organic Liquid Metal effect in blender 5.0 (tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=2MKKuHcni1U)
**Author:** Ducky 3D
**Duration:** 10m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** All right, in this tutorial, we are going to be creating this render right here. The point of it is to show you how to use the new volume SDF nodes to get these spheres, to have these really thin liquidity connected pieces to each one of them and show you how to get that. What this is going to teach you is how to combine multiple objects into each other with the grid SDF Boolean node. So it's a really creative application for that node. So if you want to check out the project file that is available on Patreon right now, and Patreon is also 25% off till the end of November. So if you want to check that out, along with all of my courses and real-time materials, are 50% off with this code. All that stuff is available till the end of the month. That's my Black Friday sale. So if you want to check it out, support me. That'd be awesome. But with that being said, let's get into this tutorial. All right, you are going to need Blender 5.0 or later to be able to do this. So let's go ahead, Shift-A. We'll get a plane that'll be our geometry. That'll be the object we need for geometry nodes. I'm going to open up a new window and switch this over to geometry nodes. I'm going to click new. So I'm going to delete this and we're going to go ahead and get a icosphere, plug it here, and then we want the radius to be probably around 10. This is going to greatly affect the density of the volume. So you do want big objects. I mean, that's super big. But you don't want them to be the default tiny because it's not going to look good. And you're going to be fighting low poly geometry. I'm going to give myself two subdivisions. We're going to get a set position node. And we're going to get a noise texture. Now, if you just click and drag, you should get a scale or just type in vector math scale. Plug this into the offset uncheck normalize. And then you can bring that up. Switch this 3D to 4D. And then you can change your settings a little bit if you want. And now we can move some things around. Now, let's go ahead and get an instance on points node. Plug that there. We'll get another icosphere. And plug that here. So now we have objects. Now, let's get objects to connect them. So first, we're going to get a join geometry and get a mesh to mesh to curve node. And plug set position into that. Plug this here. And now you're going to get all of these connected pieces. And then we're going to do a curve to tube. And that is going to get all of those pieces to now be connected with a tube. So, how can we combine these to get it to kind of look like they morph into each other? Let's go ahead and go and delete the join geometry. We're going to get a mesh to SDF grid node. Plug that here. And we're going to get a grid to mesh. Plug that there. Plug that here. And we have we have something showing up. We're going to go ahead type in Boolean. And we're going to get a SDF grid Boolean. Plug this here and switch this to union. You can plug that back. I'm going to hit shifty. Get another one. Instances to mesh. This to here. And this is highlighting. I forgot. We need to realize the instances right after the instance own points. Now we have this. So, what we do, we have this two voxel size. I'm just going to get a value node so I can edit the voxel size of both of them at the same time. So, let's say a voxel size 0.3. So, I'll type in 0.3 here. Plug that there. Plug that there. So, now when we give a lower value, we get higher poly. We get a higher poly mesh. So, we now have this. It still can look cooler. So, right over here, after the grid to mesh, we're going to get a set shade smooth node. And we're going to get a smooth geometry node. Where we at? Here it is. And once we bring up that smooth geometry node, once we bring up that smooth geometry node, we get this really organic looking effect that I just think looks so weird and awesome. I am a huge fan of this effect. And then if you bring up the scale, you get all these different things, all these different looks, and it just looks really, really awesome. So, now what we can do is add some materials to this and call it a day. Also, if you want to preview like how it might look with other materials, if you hit the drop down, go to mat cap, I'm going to say, I want to put a metallic material on it. So, now we can kind of preview how a metallic, metallic look would be. Let's go ahead. Let's get a set material node. I'm going to go here to cycles and just put some lights in the scene for now. Here in the material settings, I'm going to click new, make it metallic, maybe make a little darker, make a little shinier, and we can add it right here. So, now we have this. Now, here's something that's fun. I'm going to get a new material. And I'm going to make it subsurface. You don't have to follow along here. This is just, you can do it if you'd like. This also looks, you don't have to follow along. I'm just bringing up make it subsurface, down here, bring up the scale a little bit. And if you want, you can make it look very fleshy, and it looks disgusting and weird and strange. But if you're into this kind of like, very weird kind of 3D art and making things look fleshy, this is a very cool effect for that. If you're into that kind of stuff, I think it can be really cool sometimes. Okay, now all we have left to do is to light this and say that we're done. Now, also, if you want to animate it, it is animated over here through the W. So, you can check it out. I'm not animating mine simply because I'm kind of rushed today. But if you've seen a ton of my tutorials, you can loop the W. You can just simply add keyframes. And that is how you add animation to this. It looks really cool animated. But anyway, let's go ahead and add some lighting to this so we can be done. So first, let's get a camera. And I'm going to pick a cool camera view if it'll let me. So what we'll do is just pick a camera angle that you might think is cool. Really, you can rotate it once we get going. So I'm going to hit camera control 0, snap it to view and then maybe zoom in a little bit. This will look pretty cool. So let's go ahead and add some lighting and some volume to this. So first off, let's get a light. Let's get something that looks really cool. So I'll bring it up pretty high. I'll scale it up. And then let's just go ahead and get a render region while we're here. Give it a power of like 500, make it a disc, bring the spread in a little bit, bring the world brightness to black. And then volume, volume to a principled volume, and then just give it a little bit. And then now we can go back to our light and fine tune. This look, so I'm going to make it even brighter. We can move this guy around until we have something cool. I'll say even if we move this more like that into the light, we'll have opportunity for some cool things. All right, I'd say this looks pretty cool. Again, like I mentioned, sub-surf looks really cool in this scenario. So if you get something like this, make it look really weird and fleshy. It's cool. I think, I mean, it looks definitely gross, but in a very, very cool CG kind of way. At this point, we can go back to the shader editor and add some roughness if we want. So let's say get a color ramp, add this to the roughness, get a noise texture, add that, hit Ctrl T to get that mapping in the texture coordinate. This is completely like free reign at this point of what you want to do. If you tail of 12, bring that up. Let's get another one of these to kind of stack that roughness and bring the size down, and then you can bring these things in. And you get something pretty cool, pretty quick. Say bring this down a little bit. Bring this color up. And like I said, all kind of completely free reign, what you think might be cool, what you want to do. And that's pretty much it. That's how you create this really cool effect. And you can style it however you want. This is the final result for my render today. Again, there's a lot of just cool things that you can do with this technique. You can definitely fly a camera through this and make it look like a weird world. A lot of cool things. There you guys go. I hope you learned something. Hope you enjoyed it. Hope you use this for something really cool. Like I mentioned, the project file is available on Patreon right now. So if you can check that out and you can join annually for 25% off till the end of the month. And all my other stuff is 50% off. So if you want to check all that out, you can up with that being said, I'll see you guys in the next one.



---

## Structured Notes

### Core Technique
Organic liquid metal / blob effect using Blender 5.0 SDF Grid nodes: Icosphere instances + connecting tube curves both converted to SDF grids, merged with SDF Grid Boolean (Union), then converted back to mesh — the Union operation makes all geometry merge smoothly into each other like liquid metal.

### Summary
Ducky 3D demonstrates the Blender 5.0 SDF Grid workflow (Mesh to SDF Grid → SDF Grid Boolean → Grid to Mesh) to create an organic blob/liquid metal effect where spheres and the connecting tubes between them all smoothly merge. Icosphere (radius 10, 2 subdivisions) noise-distorted with Set Position + 4D Noise Texture (not normalized, offset) → Instance on Points with second Icosphere. Two SDF grid streams are combined: (1) the realized sphere instances; (2) the original icosphere mesh → Mesh to Curve (creates edge connections) → Curve to Tube → realized. Both go through Mesh to SDF Grid (shared voxel size ~0.3) → SDF Grid Boolean (Union) → Grid to Mesh → Set Shade Smooth → Smooth Geometry. Voxel size controls poly density (0.15 = high poly). Animation: keyframe 4D Noise W value (0 → large number over 60–120 frames). Materials: metallic PBR (Roughness ~0.1) or Subsurface (fleshy look). Roughness variation with stacked Noise Textures → Color Ramp on roughness channel.

### Key Steps
1. **Base icosphere:** New GeoNodes on plane. Delete Group Input. Icosphere (radius 10, subdivisions 2) → Set Position → Noise Texture (4D, uncheck Normalize, plug into Offset → combine XYZ scale). Adjust scale/roughness of noise.
2. **Instance spheres:** Instance on Points (instance = second Icosphere) → Realize Instances.
3. **Create connecting tubes:** From Set Position output → Mesh to Curve → Curve to Tube. This creates tube geometry along the icosphere's edges connecting all the sphere instances.
4. **SDF pipeline — spheres:** Realized sphere instances → Mesh to SDF Grid (voxel size 0.3, share via Value node).
5. **SDF pipeline — tubes:** Curve to Tube → Realize Instances → Mesh to SDF Grid (same voxel size).
6. **Boolean union:** SDF Grid Boolean (mode: Union) → plug sphere SDF into input, tube SDF into second input → Grid to Mesh.
7. **Smooth:** Grid to Mesh → Set Shade Smooth → Smooth Geometry (increase factor until organic).
8. **Voxel control:** Value node → connect to both Mesh to SDF Grid voxel size inputs. Lower value = higher resolution (try 0.15–0.3).
9. **Material (metallic):** Set Material → Principled BSDF → Metallic 1.0, Roughness ~0.1, color dark gray.
10. **Roughness variation:** Shader Editor → Noise Texture (scale high, detail high) → Color Ramp → Roughness. Stack second Noise Texture (different scale) for micro-variation.
11. **Lighting:** Area disc light (power 500, spread reduced), world black. Add Principled Volume for atmosphere (small density).
12. **Animation:** In GeoNodes Noise Texture node → keyframe W value (4D mode) from 0 to large number over desired frame range.

### Nodes / Settings
- Icosphere: radius 10 (large = better SDF density), subdivisions 2
- Noise Texture: 4D type; Normalize OFF; output Vector → Set Position offset
- Instance on Points → second Icosphere as instance
- Realize Instances (required before Mesh to SDF Grid)
- Mesh to Curve (on icosphere geometry → creates connecting edge paths)
- Curve to Tube → Realize Instances
- **Mesh to SDF Grid**: voxel size ~0.3 (lower = higher detail, heavier)
- **SDF Grid Boolean**: mode = Union (merges all geometry smoothly)
- **Grid to Mesh** → Set Shade Smooth → Smooth Geometry
- Shared Value node for voxel size on both SDF Grid nodes
- Animation: Noise Texture W value keyframed (4D) for morphing animation
- Mat cap preview: dropdown → Mat Cap for quick metal preview before full material
- Area light: disc shape, spread reduced, power 500

### Difficulty
Intermediate — short tutorial (10 min); requires Blender 5.0 for SDF nodes; low node count but high-impact result

### Blender Version
Blender 5.0 (Mesh to SDF Grid, SDF Grid Boolean, Grid to Mesh are new in 5.0)

### Tags
#geometry-nodes #sdf #volume #procedural #materials #blender-5 #intermediate

---

## Related Tutorials
- `glass-cell-division-effect-in-blender-50-tutorial.md` — also uses SDF Grid / Points to SDF approach (5.0)
- `geode-nodes-i-am-so-clever-blender-tutorial.md` — Mesh to Volume → Volume to Mesh for organic form
- `how-to-make-this-style-in-blender-50.md` — Blender 5.0 GeoNodes motion graphics companion
- `math-x-blender-50-unlimited-power.md` — complex GeoNodes procedural math companion
