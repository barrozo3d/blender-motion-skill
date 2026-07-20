---
title: How to texture REALISTIC buildings in Blender #b3d
source: YouTube
url: https://www.youtube.com/watch?v=ilaD-V8R1gI
author: CG Boost
ingested: 2026-07-19
blender_version: "Not specified (modern 4.x/5.x UI; version-agnostic workflow)"
tags: [materials, shaders, procedural, displacement, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/how-to-texture-realistic-buildings-in-blender-b3d/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How to texture REALISTIC buildings in Blender #b3d

**Source:** [YouTube](https://www.youtube.com/watch?v=ilaD-V8R1gI)
**Author:** CG Boost
**Duration:** 22m28s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, in this tutorial, I'm going to show you an overview of how to texture this realistic building.
[0:12] An all-in-one texturing workflow in Blender is something that I wanted for years.
[0:17] I just needed a pipeline that allowed me to texture anything, whether it's buildings or houses or props, pipes, streets, whatever.
[0:24] A system where I could create materials from scratch and then add on layers of realism like edgeware, dirt occlusion, grunge, graffiti, or any other features I wanted.
[0:33] And after this video, you're going to master that workflow.
[0:36] The object that we're going to be working on, essentially the canvas to present this texturing pipeline, is this awesome building created in my Urban Environments course.
[0:44] If you'd like to create the building yourself and the entire scene, you can check out the Master Urban Environments course here.
[0:50] Or you can download my building for free from the link in the description and follow along.
[0:55] Okay, so we have our building loaded up in Blender, but before we jump in, let's break down the texturing workflow so that you have a clear step-by-step idea of the process.
[1:04] First step, finding a reference.
[1:06] This stage is easy to overlook, but it's crucial to developing realistic looking materials.
[1:11] I found these images of an old building that gives me pretty great information.
[1:15] Looking at this reference, I can see what kind of materials I need and how they interact with each other.
[1:19] Second step, we need to gather the materials and textures.
[1:23] Everything used in this video will be free for you to download and use yourself.
[1:27] If you plan on gathering materials on your own, I recommend creating a checklist of things you'll need by analyzing your reference.
[1:33] Third step, we'll set up the materials, edit them to fit our needs, and blend them together to essentially create our own new material.
[1:40] Fourth step, we'll paint on damage by hand using texture painting.
[1:44] This stage is the most exciting to me personally because it allows for so much creativity.
[1:49] Fifth and final step, we'll layer on decals like graffiti, stickers, drips, mold, and additional damage that will finish everything up and contribute to a much more believable building.
[1:59] And bonus step, we'll utilize edgeware and ambient occlusion to create a more detailed secondary element.


### First Material [2:06]
**Transcript (timestamped):**
[2:06] Okay, back in the Blender, let's get our hands dirty.
[2:09] Just a quick disclaimer before we get started, this video is leaning slightly on the overview side of things, which means I won't always go in depth on every slider and button.
[2:18] And I recommend having fundamental Blender knowledge, especially in the shader editor, so that things are easier to follow along with.
[2:25] Alright, let's jump in. Select on the building, head down to material properties, hit new, and name it building.
[2:31] Now in the upper left hand corner, I'll click and drag out to create a new window, and then here, let's select shader editor.
[2:37] Okay, now I'll start by building the first material. And my objective is a rugged orange plaster.
[2:42] This material called red plaster weathered from Polyhaven will work perfectly.
[2:46] I'll drop in the diffuse, roughness, and displacement, and plug them into the principled BSDF.
[2:51] As you can see, the textures aren't working correctly yet, and that's because we haven't set up box mapping.
[2:56] Box mapping is a way to procedurally project your textures onto the object.
[3:00] The reason I'm choosing to use box mapping is because it skips the UV process, which can speed up your workflow a lot.
[3:06] To set it up, let's add in a mapping node, texture coordinate, and a value.
[3:10] Plug the texture coordinates object output into the mapping node's vector input, and plug the value into the scale of the mapping node.
[3:18] Now highlight each of your image textures, and while holding Alt, change the projection method from flat to box.
[3:24] I'd recommend turning the blend level up to 0.3 as well, so that if there are any sharp corners or seams in the textures, it will smoothen that out.
[3:31] Now I'll adjust the scale via the value node until it's the size I like.
[3:35] Now currently the texture is too dark and red to my taste, so I'll drop a hue saturation node into the diffuse line, and edit it to look more like this.
[3:43] Also currently the displacement isn't functioning, so let's plug it into a displacement node, and then into the displacement socket of the material output.
[3:50] The displacement texture will drive bump information and displacement information.
[3:54] Bump is essentially a way to fake real displacement, similar to a normal map, while real displacement is when blender literally physically deforms the mesh.
[4:03] Real displacement is dependent on your object having enough polys, typically a lot of them in order to look good, which can get really heavy in the scene.
[4:10] So instead we'll just use a bump map, which will look good enough.
[4:14] To make sure bump is working, go to material, then settings, and find surface.
[4:18] Then make sure the displacement mode is set to bump.
[4:21] Now back in the shader editor, let's lower the scale of the displacement node until it looks right.
[4:25] With everything except the material output node selected, let's hit Ctrl G to create a group.
[4:30] This will greatly assist in organizing our node tree, especially as things get more complicated down the line.
[4:35] Alright, congratulations, you just created the first material that will serve as the base for our building.
[4:40] This workflow is generally how I'll go about setting up all the other materials as well, so once you have this down, it can get pretty quick.
[4:47] Okay, now I'd like to develop the second material.


### Second Material [4:50]
**Transcript (timestamped):**
[4:50] This material is going to be a more basic orange paint to help push everything in the right direction.
[4:55] Super simple, I'll just download the beige wall material from Polyhaven, drop in my textures, add in the box mapping setup, and plug everything in.
[5:03] Now currently the material is pretty boring, so let's boost its colors and character with a hue and saturation node.
[5:10] That's much better.
[5:11] Ctrl G to group it all up, and we're ready for the next step, which is blending materials together.
[5:16] This blend is going to be very basic, and it'll follow the same setup in which we'll blend all future materials together.
[5:24] All we need is a mix shader and a mix node.
[5:26] Make sure the mix node is set to color.
[5:29] The mix shader is how we'll blend the BSDF together, and the mix node is how we blend the displacements together.
[5:36] First things first, we're going to plug the BSDF socket of the orange plaster weathered, the first material we created, into the first socket of the mix shader node,
[5:44] and the BSDF socket of the beige wall material into the second socket.
[5:48] Now we need to blend the displacements together, so plug the displacement output of the orange plaster material into the A socket of the mix node,
[5:56] and the displacement output of the beige wall material into the B socket.
[6:00] Now we have successfully mixed all the materials attributes, and as a result we've developed our own new unique material.
[6:07] While this material is looking great, it's missing character.


### Color Variation [6:10]
**Transcript (timestamped):**
[6:10] Just take a look at the difference between this, the original, and now with color variation.
[6:15] Huge difference, right?
[6:16] Color variation is a great way to add more interest to your otherwise flat materials.
[6:21] It also helps break up any tiling in the textures, which is always a realism killer.
[6:25] Adding color variation is a relatively simple process, and here's how to do it.
[6:29] Firstly, you can do it by duplicating a previously made material.
[6:33] For example, I'll just copy the orange plaster material that I created earlier, mix it in by adding another mix shader and mix node,
[6:40] then hitting the little two button on the group to make sure it's not going to change the material we duplicated it from,
[6:46] and then inside the material I'll change the colors up a bit with a hue and saturation node.
[6:50] Let's just turn the saturation down to make it more washed out than the original.
[6:54] Now for this to actually show up and to give it a realistic character,
[6:58] I'll plug a grunge texture into the mix factor of both the mix shader node and the mix node.
[7:03] All the grunge textures I'm using are available for you to download in the description below.
[7:07] Let's drag in concrete one grunge, set it up with box mapping, and then plug it into the mix factor.
[7:13] I'll also plug a color ramp in between to allow for finer control.
[7:17] After adjusting the scale of the grunge texture and the color ramp, I found this nice variation in color here.
[7:22] My advice is to make color variation additions subtle and stack a lot on top of each other to build something more complex.
[7:29] Let's do exactly that.
[7:30] Adding a new variation using the second technique, which is just a regular BSDF node,
[7:36] instead of a duplicated material.
[7:38] This BSDF will be a dark brown, and I'll plug it into the mix shader like normal.
[7:43] Then I'll add another grunge texture using concrete one again and dial it in using the color ramp.
[7:49] Now we have these nice patches of dirt that really enhance the realism.
[7:53] I'll repeat this process a few more times using different colors and different combinations of grunge textures
[7:58] until eventually I have this final base material.
[8:02] Okay, here is an overview and breakdown of the node tree so far, representing the base material with color variations.
[8:09] Here we have the red plaster in Beigewall materials.
[8:12] They are mixing together very simply via the mix shader and mix node.
[8:17] Then we introduced the first color variation, the material being a duplicated version of red plaster,
[8:23] and edited to be less saturated, and it's being mixed together with this grunge texture set up.
[8:27] Then we move on to the next color variation using the same grunge mixing technique.
[8:32] And finally, the last color variation, this time just using a BSDF instead of a material.
[8:38] Okay, so this looks pretty awesome, and it completes my workflow for building base materials for buildings.
[8:43] For this building, we're obviously going to do a lot more work, but it's really important that we nailed the basic materials first.


### Wall Paint [8:50]
**Transcript (timestamped):**
[8:50] So, jumping into the next addition to this building, I'd like to make certain walls a different color than others.
[8:57] Here's the before and after. The painted walls really help make this building unique, and that's ultimately what we are going for.
[9:03] So, how do you set this up? It's really quite simple, and it'll be our first look into texture painting.
[9:08] Now, first and foremost, texture painting requires UVs.
[9:12] When we texture paint, we're essentially creating new data on an image texture.
[9:16] Blender has to know where our paint strokes are going to be located on the mesh, and UVs is the only way to do this.
[9:22] So, let's quickly unwrap our building.
[9:24] I'll just go into edit mode by hitting tab, then hit A to select everything, then U and cube projection.
[9:31] Now I'll change the left-hand window from shader editor to UV editor.
[9:35] Here, I'll select all the UVs by hitting A, then go up to UV and hit pack islands.
[9:40] Now our UVs are ready for use.
[9:42] If you downloaded the building from the description, the UVs are actually already set up, so you don't need to worry about this process.
[9:48] Let's change it back to the shader editor and get painting.
[9:51] In order to texture paint, you need to first add in a new empty image texture.
[9:56] So, I'll just hit shift A, search, and then image texture.
[9:59] I'd like my walls to be blue, so I can name the image texture blue paint.
[10:04] Next up, I'll actually create the blue paint.
[10:06] I'll do this by duplicating the original orange plaster material, adding a hue and saturation node to the base color, and pushing it until it turns blue.
[10:14] That's it.
[10:15] Now let's add in a mix shader and plug the main materials into the top socket, and the new blue paint material into the bottom sockets.
[10:22] Now I'll take the blue paint image texture that I created and plug it into the factor of the mix shader.
[10:27] Essentially, we are mixing two materials together, and the blank image texture will act as a mask.
[10:34] I'll put it simply a mask is black and white data that can inform the separation between two materials.
[10:40] With the blue paint image texture selected, I'll head over to the object mode button and change it to texture paint.
[10:46] You can see up top here that the blue paint image texture is selected.
[10:50] That's very important.
[10:51] Now, if I just start painting, you can see it adds in the blue paint.
[10:55] I'll change this to solid view, which is the textureless preview mode, so you can visualize the fact that this is just black and white data.
[11:02] So I'd like these bottom walls to be blue, so I can just paint all of them quickly and boom, this building just became much more interesting.
[11:10] Now currently, the paint is very clean and consistent.
[11:13] There's zero imperfections here.
[11:15] The general rule of 3D is you want to add imperfections to nearly everything.
[11:20] It's a key to realism.
[11:21] So let's add in a bit of grunge to the mask, head back over to the shader editor, drop in a mix node and set the mode to subtract.
[11:30] Now you can duplicate one of the grunge texture setups we created earlier and plug it into the bottom socket of the mix node and plug the blue paint mask into the top socket.
[11:40] Turn the factor up to 1 and adjust the color ramp on the grunge texture until it starts to chip away at the paint.
[11:46] This is an area you can get really creative with and here you can see I found a subtle wear and tear of the paint.
[11:52] Much more realistic.
[11:53] Alright, here is an overview of the no tree so far featuring the new painted wall addition.
[11:59] Here we have the base material with the color variations and now with the new painted wall setup here.
[12:06] This is the painted wall mask and then here is the grunge texture which gives it imperfections.
[12:11] It's all plugged into the factor of the mix shader which is mixing together the base material and the blue paint material we just created.
[12:19] Alright, now we have made it to the second to last step in general material creation and that is hand painted damage.


### Damage [12:20]
**Transcript (timestamped):**
[12:27] Here is the building before the damage and here is after.
[12:30] Obviously the biggest boost to character and realism and also the process for adding this is incredibly flexible and fun.
[12:37] Here's how to set it up.
[12:38] First add in a blank image texture and name it damage.
[12:42] This will be the mask.
[12:43] Now let's create the material that will sit underneath the plaster where the holes of damage will be and I'd like it to be a brownish dirty plaster.
[12:51] Plaster gray 04 from Polyhaven will work perfectly.
[12:55] I'll drag in the diffuse, roughness and height and add it to the box mapping setup like before.
[13:00] Here's what the material looks like.
[13:02] Now I'll add in a mix shader and a mix node, plug the attributes of the gray plaster into the bottom sockets and the rest of the shader into the top sockets.
[13:10] Now plug the new damage mask image texture into the factor sockets of both mix nodes.
[13:16] Make sure the damage mask is selected and let's go into texture painting.
[13:21] This time instead of painting on with default settings, we're going to use a custom brush.
[13:26] You can download the brush for free from the description.
[13:29] To add the brush, let's head over to the tool button and you can find texture mask, hit new and import your brush image.
[13:39] Change the mask from mapping to view plane and then check rake.
[13:44] Then scroll down to fall off and change it to constant.
[13:48] To change the size of the brush, hit F and to change the intensity, hit shift F.
[13:53] Okay, that's all the annoying stuff out of the way, it's time to get painting.
[13:56] I generally like to wear away corners and sharp edges or really anywhere that I would imagine the building would have faced some friction,
[14:03] like perhaps where people have walked by and scraped the bottoms with their feet.
[14:07] I can't understate how much I love this process.
[14:09] I'll for sure spend a few hours honing it all in and making my building unique.
[14:14] Unless you're going for something abandoned, I would recommend not going overboard here.
[14:19] As with everything, subtlety is key.
[14:21] Alright, I finished painting my damage and here's my result.
[14:27] Okay, this is what the no tree is looking like so far.
[14:30] Here we have the base material plus the painted wall addition and now here is the new damage setup.
[14:37] Here we have the damage mask, which is plugged into the mix factors and here is the gray plaster material.


### Decals [14:44]
**Transcript (timestamped):**
[14:44] Now it's time for the final step, which is truly the stamp of realism on this building and it is decals.
[14:51] It took me forever to find the right decal workflow.
[14:55] It was always either restricted by functionality or took too long, but now I have the perfect technique and I'm excited to share it with you.
[15:02] Here's the building before the decals and here is after.
[15:05] You can see I've added dripping grunge, graffiti, dirt, etc.
[15:09] And honestly, it enhances the character so much.
[15:12] Alright, so the setup for this is actually quite simple, but it's really important to get the settings right.
[15:17] First hit Shift A, search an image texture, hit New, name it decals, set the resolution to 4096 by 4096, which is 4K,
[15:26] or 2048 by 2048, which is 2K if the 4K resolution is too heavy on your computer,
[15:32] and then under Color, make sure the alpha is set to zero.
[15:36] That part is really important.
[15:37] Now add a new principled BSDF and plug the decals image texture into the base color.
[15:42] Add a Mix Shader node, mix it into the rest of the shader, plug the principled BSDF into the bottom socket,
[15:49] and the alpha of the decals image texture into the factor.
[15:52] And that is the setup done.
[15:53] Now with the decals image texture selected, let's head into Texture Painting mode.
[15:58] Hit on Tools and scroll down to Texture and hit New.
[16:04] Now you can import any of these decals that I provided for you to download in the description.
[16:10] Make sure the mapping node is set to Stencil and hit Image Aspect.
[16:15] You can move your stencil around with Right Click, rotate with Ctrl Right Click, and scale with Shift Right Click.
[16:22] I would recommend going up to Cursor and checking Override Overlay under Texture Opacity.
[16:27] This way you can paint on the stencil without obscuring your view.
[16:31] Okay, that is all the technicals out of the way and now we can start painting on our decals.
[16:35] First things first, I like to add in drips from edges and ledges.
[16:39] For example, here I'll go to the ledge of the window and paint in drips coming down.
[16:43] Now I'll add on some dirt at the bottom, this time using a different stencil, and this added a lot of realism too.
[16:49] Have fun with this process, and again, subtlety is key.
[16:53] Now we're ready for the graffiti, which follows the same process as the grunge decals.
[16:57] Add a new stencil, this time I'll navigate to the graffiti folder and let's bring in this guy.
[17:02] I'll head to the bottom of the wall and paint this in.
[17:06] I find it fun to imagine myself as the graffiti artist and where I'd realistically want to tag.
[17:11] If there was graffiti on some wall that wasn't accessible to humans, for example, it might look unrealistic, so I try to keep that kind of stuff in mind.
[17:18] Alrighty, here is an overview of the complete node tree setup.
[17:22] Here you can see we have the base material with color variations.
[17:25] Here is the painted wall. Here is the damage.
[17:28] And finally the decals.
[17:31] Getting a closer look at the decals, we have the image texture that we created to paint on the decals, plugged into the principal BSDF,
[17:39] and the alpha of the decals image texture plugged into the factor of the mix shader.
[17:44] Alright guys, I am really happy with how this building turned out.


### Edge Wear and AO [17:45]
**Transcript (timestamped):**
[17:48] The materials feel super detailed, the damage is crisp, the decals help bring everything together.
[17:54] That's the main part of the building done, but I really want to show you the bonus step for layering on a whole new level of realism.
[18:01] And that is edgeware and dirt occlusion.
[18:04] In the course, we modeled this awesome middle eastern architectural feature called a mazrabiya, and it sits prominently here on the front of the building.
[18:12] Taking a closer look, you can see some really intricate chipping paint effects and dirt layers underneath.
[18:18] Here is the mazrabiya before and after these extra elements.
[18:21] Now just to catch you up to speed, the base material creation for the mazrabiya is identical to the building.
[18:27] First I developed wood materials and then mixed them together with other paint materials.
[18:32] Here you can see I've used a chipping paint grunge texture as the mask to replicate chipping paint.
[18:38] Once this process was finished, I started with the edgeware. I'll show you how to get this set up now.
[18:43] But quickly before we get into that, I'll give you a node tree overview of the mazrabiya's material.
[18:48] Here we have the brown planks material as well as the paint material which is mixed together with a peeling paint grunge texture.
[18:54] Alright, all caught up.
[18:56] First add a bevel node in a geometry node.
[18:59] Then add in a vector math node and set it to dot product.
[19:03] Plug the bevel into the first socket and the geometry node's normal output into the second socket.
[19:09] Now connect the dot product to a color ramp and the color ramp into a math node which is set to multiply.
[19:16] Now just use the color ramp in the multiply to dial in the edgeware.
[19:20] It's so satisfying to me for some reason.
[19:22] Here I found a really nice setup.
[19:24] Now for extra detail, plug a map range into the radius of the bevel and take one of your grunge texture setups from earlier
[19:32] and plug it into the map range.
[19:34] Now by controlling the map range, you can make your edgeware grungy and realistic.
[19:38] Now let's use this edgeware setup as the mask between two materials.
[19:42] For the mazrabiya, I used an older brown wood underneath the paint and revealed it by using edgeware.
[19:49] And here's the result.
[19:53] Okay, let's have a closer look at the node tree as well so you can properly visualize how the edgeware system works.
[19:59] Here is the base material I showed earlier and here is the new edgeware setup.
[20:03] I'm using a rough planks material to represent the edgeware and here is the actual edgeware system that is mixing it all in.
[20:12] Feel free to pause the video and copy the nodes if you need to.
[20:16] Okay, so now let's set up the dirt which is also really important for realism.
[20:21] Here's before adding the dirt and here's after.
[20:24] To add in an ambient occlusion node, unplug its color output into a color ramp.
[20:29] By controlling the distance attribute of the AO and the color ramp, you can dial in something nice.
[20:35] And then of course for extra realism, add a math node and set it to less than.
[20:39] Duplicate the grunge texture setup we used for the edgeware and plug it into the bottom socket.
[20:44] Now edit the map range until the dirt has grunge.
[20:47] Now you can use this dirt setup as the mask between the rest of the shader and a dirt material by plugging it into the factor of the mix shader.
[20:58] Okay, final node tree overview with the new dirt additions.
[21:02] Here we have the base material, the edgeware setup, and now the new dirt setup.
[21:08] Take a closer look, you can see we have the ambient occlusion node which is given a more realistic look with the grunge texture.
[21:14] And then backing out a bit, this dirt system is plugged into the factor which is mixing in this dirt material.
[21:20] The dirt material by the way is just a principal BSDF set to a brown color with a roughness turned up.


### Outro [21:26]
**Transcript (timestamped):**
[21:26] Okay, here is our complete building and I think it looks absolutely amazing.
[21:31] I really hope you guys enjoyed this video and got something out of it.
[21:34] Like I've said countless times now, this workflow is how I go about texturing any building or object in Blender.
[21:40] And once you have it dialed in, you can achieve crazy levels of realism.
[21:45] Speaking of realism, it gets even better once we add in the networks of pipes, wires, and props.
[21:52] If you'd like to learn how to create this as well, which is arguably just as important as texturing stages,
[21:57] make sure to check out the course at cgboost.com.
[22:01] In my course, we don't only model and texture the building featured in this video, but a ton of others too, each unique in their own way.
[22:09] Which eventually complete a massive city environment.
[22:13] There's truly so much packed into this course and you'll get a ton out of it no matter your skill level.
[22:19] Thanks so much for watching guys and good luck creating your buildings.



---

## Captured Frames

- [3:18] tutorials/frames/how-to-texture-realistic-buildings-in-blender-b3d/frame_000.jpg
- [8:02] tutorials/frames/how-to-texture-realistic-buildings-in-blender-b3d/frame_001.jpg
- [11:05] tutorials/frames/how-to-texture-realistic-buildings-in-blender-b3d/frame_002.jpg
- [13:39] tutorials/frames/how-to-texture-realistic-buildings-in-blender-b3d/frame_003.jpg
- [16:15] tutorials/frames/how-to-texture-realistic-buildings-in-blender-b3d/frame_004.jpg
- [17:22] tutorials/frames/how-to-texture-realistic-buildings-in-blender-b3d/frame_005.jpg
- [19:16] tutorials/frames/how-to-texture-realistic-buildings-in-blender-b3d/frame_006.jpg
- [20:44] tutorials/frames/how-to-texture-realistic-buildings-in-blender-b3d/frame_007.jpg

---

## Structured Notes

### Core Technique
An all-in-one building/prop texturing pipeline: box-mapped PBR base materials blended with grunge masks, hand-painted damage and decals via texture painting, and procedural edge wear + AO dirt as the finishing layer.

### Summary
CG Boost textures a full urban building (from their Urban Environments course, free download provided) through a layered workflow: reference → gather free PolyHaven textures → build box-mapped materials and blend them with mix shader + mix (color) pairs driven by grunge-texture masks → hand-paint wall-paint masks and damage with custom brushes → stencil-paint decals (drips, dirt, graffiti) onto an alpha-zero image texture → add procedural edge wear (Bevel + Geometry dot product) and dirt (AO node) on detailed elements like a mashrabiya. Every layer uses the same masking pattern: something black-and-white plugged into a Mix Shader factor.

### Key Steps
1. **Base material with box mapping** [frame_000, 3:18] — PolyHaven "red plaster weathered" diffuse/roughness/displacement into Principled BSDF; Texture Coordinate (Object) → Mapping → all image textures, Value node into Mapping scale; Alt-change all image textures' projection Flat → **Box**, Blend 0.3 to hide seams. Displacement → Displacement node → Material Output (Material Settings → Displacement: **Bump only** — real displacement needs heavy polycounts). Hue/Saturation to tint. Ctrl+G to group each material.
2. **Blend two materials** — Mix Shader for BSDFs + Mix node (Color mode) for displacements; plug material A into first sockets, B into second.
3. **Color variation** [frame_001, 8:02 overview] — stack subtle variations: duplicate a material group (click the "2" user count to make single-user), desaturate via Hue/Sat, then drive the Mix Shader+Mix factor with a box-mapped **grunge texture through a Color Ramp**; repeat with plain Principled BSDFs (e.g. dark brown dirt patches) and different grunge/ramp combos.
4. **Painted walls** [frame_002, 11:05] — texture painting needs UVs: Tab → A → U → Cube Projection, then UV → Pack Islands. New blank image texture ("blue paint") as mask into a Mix Shader factor blending main material vs a blue-tinted duplicate; paint the mask in Texture Paint mode (image selected in the shader editor = paint target). Add wear: Mix node set to **Subtract**, grunge setup into the bottom socket, factor 1 — chips the paint away.
5. **Hand-painted damage** [frame_003, 13:39] — blank "damage" mask into Mix Shader + Mix factors revealing an under-material (PolyHaven "plaster grey 04"). Custom brush: Tool → Texture Mask → new, imported brush image; Mask Mapping **View Plane**, **Rake** on, Falloff **Constant**; F = size, Shift+F = strength. Paint corners/edges/foot-traffic zones; subtlety is key.
6. **Decals** [frame_004, 16:15] — new image texture "decals" at 4096² (or 2048²) with **alpha set to 0** (critical); its color → new Principled BSDF → bottom of a Mix Shader, its **alpha → factor**. In Texture Paint: Tools → Texture → new, decal image, Mapping **Stencil**, hit Image Aspect; RMB move / Ctrl+RMB rotate / Shift+RMB scale the stencil; Cursor → Override Overlay to see through it. Paint drips under ledges, dirt at the base, graffiti where a tagger could reach.
7. **Edge wear** [frame_006, 19:16] — Bevel node + Geometry node → Vector Math (**Dot Product**) → Color Ramp → Math (Multiply) = wear mask; plug a grunge setup through a **Map Range into the Bevel radius** for grungy, uneven edges; use as mask revealing under-wood on painted surfaces.
8. **AO dirt** [frame_007, 20:44] — Ambient Occlusion node (Samples 16, tune Distance) → Color Ramp; Math (**Less Than**) with the edge-wear grunge (via Map Range, From Min 0.190/To Min 0.010 shown) for realistic breakup; mask into Mix Shader blending in a simple brown high-roughness Principled BSDF as dirt.

### Nodes / Settings
- Box mapping: Texture Coordinate (Object) → Mapping (Point) + Value→Scale; Image Texture Projection Box, Blend 0.3
- Material Settings → Displacement: Bump (not true displacement)
- Blend pair: Mix Shader (BSDF) + Mix/Color (displacement), factors driven by grunge → Color Ramp
- Paint-wear: Mix (Subtract) factor 1 between mask and grunge
- Custom damage brush: Texture Mask, Mapping View Plane, Rake ✓, Falloff Constant
- Decals: 4096×4096, alpha 0; stencil mapping, Image Aspect; alpha → Mix Shader factor
- Edge wear: Bevel + Geometry.Normal → Vector Math Dot Product → Color Ramp → Math Multiply; grunge → Map Range → Bevel Radius
- Dirt: Ambient Occlusion (Samples 16, Distance ~0.1) → Color Ramp → Math Less Than vs grunge Map Range
- Assets: PolyHaven red_plaster_weathered / beige_wall / plaster_grey_04; free grunge textures + brush + decals in the video description

### Difficulty
Intermediate

### Blender Version
Not specified (modern 4.x/5.x UI; workflow is version-agnostic)

### Tags
materials, shaders, procedural, displacement, intermediate

---

## Related Tutorials
- [Doing Surface Imperfections Right | Vray, Cycles, Arnold..](doing-surface-imperfections-right-vray-cycles-arnold.md) — the shading theory behind this video's layered grime/wear approach
- [30 little-known Blender tricks](30-little-known-blender-tricks.md) — texture bombing and layered smudge tips that complement this pipeline
- [3 Easy steps to make Realistic Materials](3-easy-steps-to-make-realistic-materials.md) — same realism-through-imperfection philosophy in compact form
- [Blender 5.0: How to UV Unwrap Anything](blender-50-how-to-uv-unwrap-anything.md) — proper UVs for the texture-painting steps here (cube projection is the quick version)
