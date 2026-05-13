---
title: 3D Smoke (Blender Geometry Nodes)
source: YouTube
url: https://youtu.be/Vqe4jBf3wx4
author: Seanterelle
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# 3D Smoke (Blender Geometry Nodes)

**Source:** [YouTube](https://youtu.be/Vqe4jBf3wx4)
**Author:** Seanterelle
**Ingested:** 2026-05-13

---

## Description

.blend file: https://seanterelle.gumroad.com/l/geometry_nodes_smoke

---

## Raw Content (for analysis)

Kind: captions Language: en Hello everybody and welcome to this geometry nodes tutorial in Blender 5.0 using the new volume grid nodes. Newish. It's been a while since they came out actually, but nonetheless, we're going to be making this 3D smoke with geometry nodes. So, let's get into it. The basic structure of this whole thing is that we're going to have a simulation zone here represented by this cube. Then we've got an emitter which is going to be Suzanne. They've got their own geometry nodes networks that I'll explain. And um basically we're going to set up a domain which is going to be this cube uh just subdivided into a bunch of little voxal cubes. And then we are going to do something really similar to the 2D fluid simulation tutorial that I had a long time ago. um where we're using uh a couple different fields uh velocity, divergence, pressure, and then a density field which we're actually calling smoke uh here. Uh that that's smoke. The smoke field is what you actually see. And then we're um essentially creating forces uh enforcing incompressibility in the fluid and watching the density or the smoke evolve over time. Um so that's our basic setup. We have our uh initialization here. We have our simulation here. And then a little bit of uh post-processing just removing grids making the uh voxil data structure slightly more efficient before we bake so that our baked output can be as small in memory as possible. So first things first is our domain setup. First thing we're going to do is create these simulation grids. We're going to do that with the volume cube node just to create an initial volume. Um we're going to use the inputs from our parameters node group which is also right out here. So the reason we create a node group like this is just so that we can reference these sort of global values that we want um in multiple places without having to drag a bunch of noodles around. So we create that volume cube with the min and max bounds that are uh defined in our parameters node group. In this case I think it's yeah just -2 to positive2. [snorts] And then also using the solver resolution. You can press ctrl h to uh hide or show all the different outputs of a specific node group. That's why these are actually the same but they look different. Um and so the solver resolution we're going to set to just something relatively small like 64 in this case. So that if I do turn off the baked output with M for just masking that then we can still run this relatively relatively quickly. If we go down to something like 32 um it'll run in uh it'll run faster. But anyway 64 is fine. And then the cool thing about that is that if I simulate um the solver resolution at 64. What we're going to do later is we're going to use the smoke resolution at a high resolution so that you get more detail and you don't see all these little blocky cubes here. But the cool thing is I can run at this like relatively interactive rate where you know when it when it bakes I can see it running as fast as it will in the final render. And then if that will give me a really good idea of what the higher resolution output will look like. And I can illustrate that by just uh unmasking the bake node. And you can see that the shapes match up pretty much perfectly. It's just in the 64 version where the um smoke resolution is also 64, it looks more blurry. So, working this way will give you an idea of what your effect will actually look like without taking forever to bake because it takes a lot longer when you bump up the smoke resolution to something like 256, like 128 or 256. Okay, so create a volume cube. we get the density which is the default uh grid value um or grid attribute or whatever you want to call it that it creates. We're going to remove that because we don't need it. We're actually going to call it smoke. We're going to voxalize the grid. And the reason why we're doing this is that the underlying data structure for these volume grids is called openvd. And it will do some um memory optimization where contiguous blocks of voxels that are adjacent to each other that have really similar similar values um will be just referenced as one thing with uh their own individual bounds. And that's all well and good. But for what we're doing, we want all of the voxels available so that we can calculate the [snorts] um like divergence and pressure and enforce incompressibility in the way that we want. Um and we just don't want any of that optimization right away or during the simulation. And then we'll use the topology from that voxalized grid to initialize all of the other grids that we need for our simulation. So we've got velocity, divergence, and pressure. velocity is a vector grid. The other two are float grids. So we just use this field to grid node which will take in a topology input which will define like what does the grid that you're creating actually look like in terms of its um bounds like its minimum and maximum points as well as uh the topology of the voxels. So in this case, it's just a bunch of voxels at the resolution that we set here, but in other cases, it could be optimized voxal topologies like we just talked about. So now we have all of our grids in the same topology, and then we're going to add our smoke grid. So the way we do that is we're the reason we're doing this separately is because uh we're going to want it to be a different resolution. So here, press Ctrl H. instead of having solver resolution, we use smoke resolution. And right now, I've just got it set to 64 um so that we have like an interactive frame rate. But if I set it something something higher like 128 and it's going to take longer to simulate here, but you can see how you get a little bit more detail. And so you can just ramp that up to get more and more detailed smoke with the same solver resolution, which is really cool because then you can, like I said, get that really good idea of what your simulation is going to look like before you ac

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/3d-smoke-blender-geometry-nodes.md and extract:
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
