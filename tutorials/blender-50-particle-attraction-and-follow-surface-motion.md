---
title: Blender 5.0 particle attraction and follow surface motion
source: YouTube
url: https://youtu.be/QHJXi25OczQ
author: Zack (3D animation)
ingested: 2026-05-13
blender_version: "5.0"
tags: [geometry-nodes, simulation, particles, animation, procedural, intermediate, blender-5x]
extraction_status: complete
---

# Blender 5.0 particle attraction and follow surface motion

**Source:** [YouTube](https://youtu.be/QHJXi25OczQ)
**Author:** Zack (3D animation)
**Ingested:** 2026-05-13

---

## Description



---

## Raw Content (for analysis)

Kind: captions Language: en [music] &gt;&gt; Hi, today I will show you how to make this particle effect. Uh it's kind of pretty simple. I did a tutorial similar tutorial before. First, please let me introduce the principle. We need only two vector two force to make this effect. The first is uh attraction. So, we need a a vector like this. Like from this point to the point on the surface uh over this geometry. And we we needed to add some noise to this vector to make it look nice like these curves. And then second force is to make the particle flow along the surface over the geometry like like this. Like this effect. Yeah, like this. So, it's pretty simple, too. Uh I use a method cross. Yeah. Cross mass use I use normal and noise to make this vector and then make the particle move. So, that's the whole principle. If you you are very familiar with with this, you can understand that and ignore my tutorial. If you don't understand, you can continue. So, let's begin our tutorial. Okay, first we need some text. Maybe you can you you can use other geometry like the monkey head or something else. It depends on you. I will use the text for demonstration. So, here I have the plane and I press new. So, I use geometry nodes to create the text. So, here I will input sample. So, the string and I will turn string to curve. So, then I connect it to output. So, we have this uh this text. So, the word of sample, I needed to You can see it's empty inside. And I need to fill that. And then after that, you can see here. It's kind of kind of looks like a it's instance. So, I think I will need to realize instance. So, we have like face edge and a vertex. It's It's geometry. It's a mesh. So, then uh I think I will use extrude. So, it's pretty much and I'll change the distance to 0.1. And then you can see the downside it is it's like every face is extruded. I don't like that. I want one of them to extrude like this. So, click this. So, after that I will use join. I will fix the empty here. So, I use join to join the Yeah, to join the face here. So, it's not a empty and after that I need a flip face to fix the normal problem. The normal is uh uh is going up. It's going up. So, I want the normal to be to be going down. So, to fix that, I use the flip face. And then I use the merge by distance. Uh because for now uh like because if if you just join then uh like here like here there there is a point, but there to be honest, there are two points here. We needed to use merge by distance to merge the two points into one points. So, that's very important. And now I think it's finished. So, maybe I want more faces from the from this this text. So, for me I use the mesh to uh volume. No, not here. Sorry. Mesh to volume. Here. And you use the volume to mesh. So, we have this. And the change the box amount. It will be like this. And you use the subdivide surface. It's smoother. And we decrease this. Uh it will be like this. And I think that's good. And I use transform geometry to make it in the center. You can You can ignore this, but for me I prefer to make it in the center of the origin. Okay, like this. So, that's all we needed to do. And then hide this. Let's go to cube and change the name to particle. So, the first we needed to uh build is the particle system. So, I think the cube is too much small. Maybe we needed to make it bigger. And then give it a value to scale. Maybe five five will be okay. Then I turn mesh to volume. And the volume uh and the distribute the points in volume. So, we have points. Uh we don't need too much points for now because it's for demonstration. I I don't want it to be too heavy. So, we have so many points. And then next we will build a simulation system here. And use set position to to to make the particle move. We can add the force here in offset. So, let's begin move the and make the basic effect. First, I wanted the particle to move uh to the to the text. Uh the text is hidden. And I think I need to join them to make you see that. So, and we are and I think this is the text. Just change the name. Drag it here and join them. And now I think yeah, the sample is here. So, that's what we need. Uh uh yeah, that's what we need. Let's make more space and first we needed to define the force. The attraction force and with noise. So, we need a we need a two value. First is the the position of the point. Secondly, is the position like on the on the surface of the the geometry. Uh any any position. So, after that, I will uh subtract them to make a force. To make a new vector like this direction, so it will so, the particle will go this direction to the text. And then I add some noise to it. So, principle is very easy. Let's make it. So, first we need a position. And I use sample nearest surface. So, you can use that or you can just use a random position on the surface of the text. So, it depends on you. Here I will demonstrate you use this nearest. So, we have the nearest position and the position of the point here. And we subtract them. So, we make a new force and we make sure uh the abstract I think the absolute value is one, so I use normalize. And I use scale to make it smaller because normally in the beginning it's too much the force is too big. So, connect to offset. So, we have the force of attraction and then we use add. We will need it to add a like noise. Here I use noise. You can use other force. So, click the normalize. We We don't want it to be normalized. And and my mistake the normalize here is the same. It's just make sure the vector is uh uh the range is from zero to one. That's the function of normalize. So, here it's inside of the normalize text and I connect it color to here. And add it here. And then connect to noise. And then for now noise is too big, so we needed to make sure it's not bigger than the attraction force. So, I will change it to like a just a smaller. You can change the other value. Just make sure the value is smaller than 0.1. So, that's the first force. And now

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/blender-50-particle-attraction-and-follow-surface-motion.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Creating a particle system in Blender 5.0 Geometry Nodes where particles are attracted to a surface (text or mesh) using two vector forces: a normalized attraction force toward the nearest surface point and a cross-product-based force to make particles flow along the surface.

### Key Steps
1. Create text geometry using Geometry Nodes: add a String to Curve node, fill the curve, Realize Instances, Extrude Mesh (distance: 0.1), fix normals with Flip Face, and Merge by Distance to clean shared vertices.
2. Optionally use Mesh to Volume then Volume to Mesh with Subdivide Surface for a smoother mesh surface to attract particles to.
3. Use Transform Geometry to center the text geometry at the origin.
4. On a separate cube, scale it (e.g., 5) and use Mesh to Volume then Distribute Points in Volume to scatter particle starting positions.
5. Set up a Simulation Zone on the particle object for per-frame movement using a Set Position node.
6. For the attraction force: get the current particle Position; use Sample Nearest Surface on the target text mesh to get the closest point position; subtract particle position from the surface position and Normalize to get a unit direction vector; Scale it down (e.g., < 0.1) for gentle attraction.
7. For noise: add a Noise Texture connected to a Normalize node (range 0–1) and Scale the result to be smaller than the attraction force (< 0.1); Add the noise to the attraction vector.
8. For the surface-following force: use the Cross Product of the surface Normal and the noise vector to generate a tangential movement direction.
9. Add all three forces (attraction + noise + cross product) in the Set Position Offset socket.
10. Connect the simulation output to the group output to display the animated particles.

### Blender Nodes / Settings
- String to Curve node
- Fill Curve node
- Realize Instances node
- Extrude Mesh node (Distance: 0.1)
- Flip Face node
- Merge by Distance node
- Mesh to Volume node
- Volume to Mesh node
- Distribute Points in Volume node
- Simulation Zone (input/output)
- Set Position node (Offset socket)
- Sample Nearest Surface node
- Position node
- Vector Math: Subtract, Normalize, Scale, Cross Product, Add
- Noise Texture node (strength: < 0.1)

### Difficulty
Intermediate

### Blender Version
5.0

### Tags
#geometry-nodes #simulation #particles #animation #procedural #intermediate #blender-5x
