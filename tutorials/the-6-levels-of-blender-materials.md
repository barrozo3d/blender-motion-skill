---
title: The 6 Levels of Blender Materials
source: YouTube
url: https://www.youtube.com/watch?v=RfPro3hlOMg
author: Kaizen
ingested: 2026-09-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/the-6-levels-of-blender-materials/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: []
---

# The 6 Levels of Blender Materials

**Source:** [YouTube](https://www.youtube.com/watch?v=RfPro3hlOMg)
**Author:** Kaizen
**Duration:** 17m29s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py the-6-levels-of-blender-materials <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Level 1 - The Principled BSDF [0:00]
**Transcript (timestamped):**
[0:00] So, Level 1. Boot Blender, click in your object, add a material, and nothing changes.
[0:06] In the background, Blender added a material with a Principled BSDF node to your object.
[0:11] It's an incredibly powerful node and with the right setup, it can create practically
[0:14] any material in 3D, but in its default state it's unassuming. You can change the color,
[0:20] lower the roughness, you can even make it look like metal. You see, this is only the first level
[0:25] of the 6 levels of building materials in Blender. It's the most basic version and although
[0:29] simple, it's the first real step towards unlocking the real power that comes with the final levels.
[0:34] But, you're just level 1 now, so let's begin with some easy examples.
[0:41] Rough Plastic, set the roughness anywhere from 0.3 to 0.8, add some transmission to have
[0:46] light pass through, and done. Soapy Bubble, roughness to near 0, IOR to 3, transmission to 1,
[0:53] and in the Thin Film tab, set the thickness to roughly 500 noon meters and the IOR to 1.6.
[0:59] Done. Carpaint Material, give it a nice color, crank up the metallic to 1, the roughness to
[1:04] something relatively rough like 0.25, and then add a coat of 1 to get that nice glossy top layer.
[1:10] Now you probably already knew these basic examples, so let's level up instead.


### Level 2 - Adding Layers [1:13]
**Transcript (timestamped):**
[1:15] By adding layers of detail, we can add depth and realism to materials. The simplest way of doing
[1:20] this is by adding so-called texture nodes to your materials and connecting their outputs to inputs
[1:26] on the principal PSDF node. There's plenty different texture nodes, but in most cases,
[1:30] a Voronoi, Noise, Wave, or Gradient Texture will suffice. But let's get back to our last material,
[1:36] the Carpaint. One standout feature is clearly missing, that sort of speckled look that metallic
[1:42] Carpaint has. That automatically limits your no choice to either a Noise or a Voronoi texture
[1:48] since those give those tiny details. The Noise texture, set to a large skill like 1000,
[1:53] gives plenty tiny detail to use. And since these speckles should catch in the stored light,
[1:58] it makes sense to convert the output to normals using a normal Mab node with low strength.
[2:03] And this does bring you pretty close. But Carpaint looks more flaky, sharp-edged speckles,
[2:10] not soft. So let's give the Voronoi a go instead. Same scale and detail, but just to get those sharp
[2:16] and angular shapes. And there you go, much, much better. When it comes to layers of detail,
[2:21] it's usually not one, but two, three, or any higher number that can really help make your


### Level 3 - Controlling Your Materials [2:27]
**Transcript (timestamped):**
[2:27] material pop. Now, most textures, when not using their color outputs, output a value range of 0
[2:34] to 1, meaning any point here is either black, white, or any gray value in between. In this case,
[2:40] you're using that data to control the normals. But if you were to pluck those black and white
[2:44] values into the roughness, for example, they're pretty bad values. No material is fully reflected,
[2:50] for example, not even a mirror. So a roughness value of zero makes no sense. And the same can be
[2:56] said for a roughness value of one, two. The fix is pretty simple. You simply need to tune those
[3:02] values. So instead of zero to one, you need to change these values using something like a color
[3:07] ramp or a map range node. These are perfect nodes for adding granular control to value ranges like
[3:13] those coming out of texture nodes. You can use both the map range and the color ramp to get
[3:18] the exact same result. In terms of calculating the final shader, though, I know that map ranges
[3:23] tend to compute a little bit faster than color ramps. However, I'm much more of a visual person
[3:28] than a mathematical one. So, you know, seeing the colors in the color stops just makes a little bit
[3:33] more sense to me. Anyways, your Voronoi texture to get those flaky shapes is outputting colors,
[3:38] which by taking the color ramp get converted to black and white values. If you then take these
[3:43] values and then change them from black and white or zero and one to gray values equal to numbers
[3:49] like for example, 0.5 and 0.8 or 0.6, you get a much less contrasted spectrum of gray tones.
[3:55] By also dragging in these color stops, you get additional control and nice clean shapes, which
[4:00] really changes the overall effect of the speckles to become much more natural, in my opinion.
[4:04] It's really perfect for a carpet. For this material, there's really only one layer to tune
[4:09] as of now, but for other materials, there might be lots of layers, each requiring individual
[4:14] tuning to get the perfect look or even multiple nodes and textures combined just to get one good
[4:19] looking material property as you'll see in one of the later levels. But in this case,
[4:24] it's a simple addition that really makes a big difference overall. And you're still just in level
[4:29] three, which is only about halfway to creating those real smart and pro materials inside of
[4:34] Blender. Now, just like there's levels to building materials, there's also levels to managing a
[4:39] business. And that's where Odu today's video sponsor will level up your workflow. Odu is an
[4:43] all in one management platform offering over 45 seamlessly integrated apps all designed to meet
[4:49] your business needs, whether it's customer relation management, invoicing, hosting your website,
[4:55] or even simply tracking your projects. Odu has an app for it. And they're all connected to each
[5:00] other and jump over to the e-commerce apps who launch your web shop as orders come in, invoices
[5:05] are created automatically, and your infantry stays up to date. One connected system, everything you
[5:10] need to sell online. I personally really like that Odu is easy to use. It's very customizable without
[5:16] feeling overwhelming. And it's automatically tailored to my location, which is great for someone
[5:20] who works with a lot of international companies. Adding Odu into your business can be as small or
[5:26] as big as you want it simply using it to offload one task like accounting or adding dozens of
[5:31] applications to streamline your entire company's pipeline. Plus, and this might just be one of the
[5:36] best features, it's super affordable with the first application being free for life, including
[5:41] unlimited hosting and support and regionally tailored prices for all apps besides that first one.
[5:46] So please make sure to check out Odu through the link in the description to start leveling up your
[5:50] business. And thank you to Odu for sponsoring this video. Now let's go to level four. And this is


### Level 4 - Surface Imperfections [5:53]
**Transcript (timestamped):**
[5:56] where things get a lot more interesting. It's where you leave the basic stuff behind and start
[6:00] adding in more complex effects. Things like so called service imperfections. And it's the single
[6:06] reason that this material looks so much better than this one. So for our car paint material,
[6:11] maybe our car has been driving through the mud and we need mud to appear on top of the paint.
[6:17] Since you already have your principal BSDF set up to be a nice shiny metallic car paint,
[6:22] you can't simply add dirt to that shader. But although it might look like it, the node that
[6:27] started this material, the principal BSDF doesn't have to be the only so called shader node within
[6:34] your material, you can actually use multiple shader nodes by adding in a second principal BSDF,
[6:39] you can effectively build multiple shaders into one again using a noise texture doubling that up
[6:45] with another noise texture for some variation and taking the output through two different color
[6:49] ramps one for the color using multiple dirt like colors and one for the normals to create some nice
[6:54] bump, you get a simple but effective dirt shader. And as the final detail, you can add some variation
[7:00] between wet and dry parts by using another set of textures to control the roughness. That means we
[7:05] have two shaders set up the car paint and the dirt to combine the two, you can add one of two nodes
[7:11] and add shader or a mix shader node. The add shader combines the two by adding all the values of your
[7:17] materials and outputting that combined value as the new material. You can even chain in multiple
[7:23] of them and combine a lot of different shaders. This is for example, how you get a glass shader
[7:28] with a cool chromatic dispersion effect. But if you use an add shader here, you'd see that it's
[7:33] not what you're looking for. The material should have parts of paint and parts of dirt, not a
[7:38] combination of the two. To do this, you need a mix shader node that allows for far more control over
[7:44] the effect using textures once again. So by taking a noise texture and plugging that into the factor
[7:50] of the mix shader, there appears a separation between the two shaders. The texture that you just
[7:54] introduced now behaves as a mask. And since the material can really only be either paint or dirt,
[8:01] not both, you don't want any mixed values. So by adding a color ramp or map range node, as explained
[8:08] in level three, you're able to dial everything in to get the right look. Okay, let's take a second
[8:13] here. So far, all of your material changes have been fully procedural, which means that they're
[8:18] all mathematically generated in the background by blender. The great thing about this is that a
[8:23] procedural material can easily be applied to any object without looking better distorted, unlike
[8:29] image texture based materials. Plus, generally speaking, they're quite light on your computer
[8:34] when it comes to rendering, which is a big bonus. However, there's certain effects like for example,
[8:39] scratches or fingerprints that although could be generated procedurally are just easier to do
[8:45] through image textures. And you can find these all around the internet. But I can also really
[8:50] recommend you an add on called realistic touch, which allows you to drag and drop over 200 seamless
[8:56] imperfections with additional controls. It's just a very easy way to add surface imperfections. In its
[9:02] most basic form, though, you'd simply add a preferably seamless imperfection texture and
[9:07] plug it straight into your roughness to get some easy extra realism in your materials. Now for
[9:12] the car paint material, you could use a scratch texture like this one. And instead of plugging it
[9:17] into the roughness, which is actually below our top code, you'd want the imperfections to appear
[9:22] in the top code where they would naturally be in the real world. So you plug it in the code roughness
[9:27] instead to make sure that only the top layer is affected. Nice, you're getting somewhere. But
[9:32] what if I told you that overall, this would still be considered a dumb material? First of all, the


### Level 5 - Smart Materials [9:37]
**Transcript (timestamped):**
[9:39] dirt is just everywhere. And the same is the case for the scratches. Dirt would mostly be present
[9:44] on the bottom or the lower region of the car. Since that's where the road is. And scratches would be
[9:48] mostly present in parts that stick out more, since those are more likely to catch damage while driving.
[9:54] So what if you could have this material do all those things automatically for you, no matter
[9:58] the model that you use? That would be a pretty smart material. So the shader needs to be fed the
[10:04] information that parts of the mesh that are concave or sticking inward should have less
[10:09] damage than parts that are convex or sticking out. And this is where something called attributes
[10:14] come into play. Attributes are data points usually attached to your geometry that can be used inside
[10:20] the shader to control material properties. A great example of some of the default attributes that you
[10:25] can use can be found using the geometry node, which you shouldn't confuse with geometry nodes.
[10:31] This contains various attributes like the position factor, the tangent or the pointiness.
[10:36] And this last one, pointiness, can actually be used to find the convex and concave parts of a mesh
[10:42] automatically. It's pretty solid, but it doesn't work in EV. Luckily, there's now better ways to
[10:48] generate attributes since the introduction of geometry nodes. So to make a proper smart
[10:53] material, you actually have to leave the shading workspace and hop on over to geometry nodes.
[10:58] Here you want to create a so called store named attribute node to simplify that. This just means
[11:04] that you're storing certain data with a certain name. That's really all it is. In this case,
[11:09] the data that you want to store is the signed edge data that can be found using the edge angle node.
[11:15] And for the name, you can simply put in anything you'd like, like, for example, edge angle, or if
[11:20] you really want to make it smart, something like subscribe to Kaisen maybe. And that's it. You now
[11:27] have your attribute ready to use in the shader by adding an attribute node in the shader editor,
[11:32] typing in that same name, making sure spelling is correct. And if I preview it,
[11:36] well, there it is. Plus, it also works in EV. So now we can do the exact same for our car paint
[11:44] shader, again, adding in a geometry node system, adding the store named attribute,
[11:48] inputting the edge angle data, and then using that as an attribute in our shader. And now,
[11:53] just as with the mix shader, you can use this black and white output as a sort of mask to control
[11:58] where the scratches appear. By default, the edge angle outputs can cave as black and convex as white,
[12:04] meaning that the inside parts will be masked off, which is exactly what you'd want in this scenario.
[12:08] In other cases, you might need to invert it. And you can once again use the map ranger color
[12:13] rem node to do so. Use the attribute and combine it with the scratch texture through a mixed color
[12:18] node. This simply allows control over how the colors are mixed. The top should be black effectively,
[12:23] meaning nothing should appear. And the bottom can be the scratch texture. And the factor is the
[12:28] attribute that we just created, used as a mask to control which parts don't or do have scratches.
[12:34] And voila, you now have masked off scratches that automatically apply to the parts of any mesh that
[12:40] stick out. But what about the dirt? Well, it's a bit different because now you want to have an
[12:45] effect that uses sort of the proximity between objects to generate a black and white mask.
[12:51] Luckily, there's this beautiful, albeit somewhat computationally expensive ambient occlusion node.
[12:57] Often it's mostly white or grayish if you preview it. But once again, you can dial in these values
[13:02] using a color ramp, for example, by doing so certain parts of the mesh immediately become darker,
[13:08] which is perfect, right? Because these are the exact same areas that would catch more dirt because
[13:13] of lack of exposure to wind or rain and where dust and dirt are just more likely to accumulate. So
[13:20] take the color ramp output, plug it into the mixed shader factor, and you get accurate mixing between
[13:25] the two shaders. And to make it look even better, you can add variation to the ambient occlusion by
[13:30] taking a noise texture and plugging the factor output into the distance value of the ambient
[13:35] occlusion to get some varying distance values. Obviously, you can use color ramps or map ranges
[13:40] here too to add additional control to this effect. And using these automatic masking techniques is
[13:46] what really takes this from a pretty dumb material to a smart material. But although the material
[13:52] now procedurally adapts to any mesh, it's far from easily reusable, which is what I would consider
[13:58] a professional smart material to be able to do. Now a lot of tweakable values like for example,
[14:04] the color of this shader aren't directly available through the material properties, color,
[14:09] buffiness, or even the code values are some of them that you can access through this menu,
[14:13] which is amazing for when you're using this material in a non shader based workspace. But
[14:19] what if you want control over the scratches or the dirt or even simply the scale of the speckles
[14:25] in the metallic carpet? Well, it is possible, but it's such a tedious process to find these
[14:31] specific settings and features in this giant heap of possible sliders and data fields. That might not
[14:37] sound like a huge problem, but imagine having to do it hundreds of times for dozens of different
[14:42] materials. It's pretty annoying. And it's why when you buy a professional shader, it will always
[14:46] have these controls available to you. So adding in these reusability controls is the real final
[14:52] level of creating a smart material in blender. After this, you're left with basically any
[14:58] professional shader or material you might buy or find online. To do it, you want to decide on any


### Level 6 - Making Your Materials Re-usable [15:00]
**Transcript (timestamped):**
[15:04] and all values that you'd like to control. For the sake of this video, though, let's keep it limited
[15:09] just for the first attribute node goes into the base color using the color output. And let's call
[15:15] it that too. Base color. The next one goes in the normal map strength using the factor output. The
[15:20] third one also using the factor output, since you only want black and white values here can be plugged
[15:25] in the map range node that controls the noise texture for the ambient occlusion and called
[15:30] something like AO control. And finally, the fourth again with the factor output plugged into the
[15:36] skill of your Voronoi texture called a four O skill, for example. And by doing all that, you
[15:42] should have basically ruined your material, which kind of makes sense because none of these attributes
[15:46] are referenced anywhere and so blender can't really find them. And therefore it breaks the
[15:51] material. Let's hop on over to jump tree notes again. And this is where the final magic happens.
[15:56] Here, simply add in a couple more store named attribute notes, obviously one for each value
[16:02] that you just decided on that you want to control. And while you read it, you can simply copy over
[16:08] the names to by just switching between workspaces hovering over a field like the name control C
[16:13] and then pasting it in the other name filled with control V. And finally make sure that the store named
[16:18] attribute containing your base color is using color data, not float values, which are again,
[16:23] just black and white values. Now you can take the color value and connect it to your group input
[16:28] node. Now press N to open up the geometry node editor, select the value that just got added in
[16:33] the group sockets and rename it to base color for convenience. You can do the same as well with all
[16:38] the other values, obviously respecting their individual names. The final thing should look
[16:43] something like this, meaning you have now exposed these values within the geometry nodes modifier,
[16:48] allowing you to control each value directly through the modifier tab without switching
[16:53] workspaces. To me, this is what truly makes for a level six professional smart material.
[16:59] And although these are some very basic examples of how to use attributes, I hope that they show
[17:04] you that through attribute manipulation, you can add extensive controls eventually resulting in
[17:10] complex shaders like this final carpet and then I mean, but if all of this is a lot and you feel
[17:14] like you're not able to learn blender really, check out this video and maybe find out why you're
[17:19] stuck instead of growing your skills.



---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Blender Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
