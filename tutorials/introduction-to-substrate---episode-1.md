---
title: Introduction to Substrate - Episode 1
source: YouTube
url: https://www.youtube.com/watch?v=P5I38f2O6W8
author: Ben Cloward
ingested: 2026-08-02
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/introduction-to-substrate---episode-1/
frame_count: 0
frame_status: pending-selection
---

# Introduction to Substrate - Episode 1

**Source:** [YouTube](https://www.youtube.com/watch?v=P5I38f2O6W8)
**Author:** Ben Cloward
**Duration:** 15m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py introduction-to-substrate---episode-1 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today, we're starting a brand new series of videos about Substrate, Unreal's new material system. Let's go!
[0:15] Alright, Substrate is Unreal's new material authoring system. It provides some major improvements over the previous material system
[0:26] and gives us a lot more flexibility in how we create and use materials. It gives us deeper and wider control and fixes limitations that the previous material system imposed.
[0:40] Because it's a broad topic, we're just going to touch on the basics today and then in future videos in this series, we'll get into more advanced topics and details.
[0:52] So these are the topics that we're going to cover today. What is Substrate and why is it a thing? How can I turn it on? And then once it's on, how can I make a material like I did before?
[1:08] Alright, so under the hood, Substrate uses most of the same graphics systems and physically based rendering techniques that Unreal has always used.
[1:19] What's different is that it exposes lower level parameters that give us more control. With this new set of parameters, we're able to create a broader range of materials.
[1:34] Unreal's previous system gave us base color, metallic, specular, and roughness parameters. And I've heard some people call this set of parameters PBR and say that Substrate is replacing PBR in Unreal.
[1:52] This is not correct. With Substrate's new set of parameters, we're still using physically based rendering. It's just that now we have access to lower level parameters that give us more control if we want it.
[2:11] Base color, metallic, and specular are higher level concepts that simplify PBR. They're like training wheels built on top of a much more complex system.
[2:25] With Substrate, Epic is exposing more of the complex internals of this system to give us more direct control and the ability to create more exotic materials that we couldn't before.
[2:41] It's still possible to use base color, metallic, and specular if we want. And I'll show you how to do that in a minute. But it's also possible to directly control the parameters underneath those. And they're called diffuse Albedo, F0, and F90.
[3:00] Additionally, Substrate gives us the ability to do material layering and blending in a much more elegant and intuitive way. We can now create more complex layered materials that have depth.
[3:16] One example of this would be a carbon fiber material with a weave pattern that also has a clear coat layer on top. And another example of this would be car paint with reflective flex internal to the material.
[3:37] I'll go deeper into all of these topics in future videos in the series, but for now, let's just say that Substrate allows us to create a much wider and deeper set of materials than we could before.
[3:51] Alright, so how can I turn it on? Starting in Unreal Engine 5.7, Substrate is enabled by default. Or you can also turn it on for your project by opening your project settings and typing Substrate in the search.
[4:12] So here we have the Substrate Materials checkbox. And all you need to do to enable Substrate in your project is check that box. And it's going to tell us, hey, any materials that you save while Substrate is enabled won't be able to render correctly if it's disabled later on.
[4:30] This is a one way trip. Once you enable it in your project, you probably don't want to disable it again because any materials that you changed after enable it will be broken.
[4:42] Alright, so we'll turn it on and it'll tell us down here that we need to restart Unreal before we can start using it. So we'll do that in a minute, but I do want to explain a couple of other things that are happening here.
[4:56] So the next setting to consider is this G-Buffer setting. We're setting the G-Buffer format and our options are either blendable or adaptive.
[5:10] So let me explain what this does under the hood.
[5:15] With Substrate off, Unreal uses a fixed G-Buffer that uses 16 bytes of VRAM per pixel on the screen. So if you're rendering your screen at 4K resolution, that G-Buffer will be using about 132 megabytes of VRAM. And that's with Substrate off.
[5:41] With Substrate's G-Buffer set to blendable like it is here, we're going to be using a fixed size of 20 bytes per pixel, which is a 20% increase over having Substrate off.
[5:56] But if you set it to adaptive like this, the G-Buffer will be able to change size depending on the complexity of your materials.
[6:06] It starts at 20 bytes per pixel, but it can go up to 80 bytes per pixel with more complex materials. So here you can see we've got 80 bytes per pixel defined as our max right now.
[6:21] So if I have a G-Buffer at 4K, that would be 663 megabytes of VRAM, which is five times more memory than if I had Substrate off.
[6:37] So this is definitely something to think about when deciding whether to use Substrate.
[6:43] When using blendable, it's a constant 20% increase in memory, but when I've got it set to adaptive, it could be as much as five times more VRAM than with Substrate off.
[6:59] Ouch!
[7:01] Now, it's important to point out here that if you do set your project to adaptive, if you build the project for a lower end platform like Android, for example, it will automatically switch your adaptive setting back to blendable for that platform.
[7:21] So for higher end platforms, it's going to use adaptive, but if you set it to adaptive on lower end platforms, it's going to fall back and use blendable instead.
[7:33] So you've got a couple of options here. You probably want to use adaptive if your project is going to be targeting high end PC.
[7:45] But if you know that you're not going to be building on high end PC, you probably want to go ahead and just use blendable.
[7:53] Alright, so those are your options. I'm going to go ahead and restart Unreal and we'll pick up right here where we left off.
[8:00] Alright, here we are back in Unreal after restarting. And you can see I've opened that same material we were looking at just a minute ago.
[8:08] And we still see the same base color metallic specular and roughness just like we did before.
[8:14] So not a whole lot has changed. But if I come down here to the bottom of the material, you can see my material has a new input here called front material.
[8:25] And this is our gateway into the world of substrate.
[8:31] So what do I do with this purple input down here?
[8:34] Well, let me zoom out a little bit. I'm going to right click in here and search for slab.
[8:40] And you can see there's a new node here called substrate slab.
[8:45] In fact, if I just type substrate here, you can see we now have access to a whole bunch of nodes that are substrate specific.
[8:57] We're going to get into more of these later on in the videos in the series.
[9:01] But for now, let's just use the slab node.
[9:05] This is our most basic setting.
[9:09] Now, previously, if I selected my root node over here, I could pick from a whole bunch of different kinds of shading models.
[9:20] And I could only select one shading model per material.
[9:24] So if I wanted to make a material that was both rock and ice, or if I wanted to make a material that was both skin and cloth,
[9:36] I was kind of out of luck because I could only pick one shading model and match that shading model to the kind of material that I was trying to make.
[9:47] But with substrate, I can mix and match those shading models using slabs.
[9:52] And like I said, we're going to get into more detail on that later on in the series.
[9:57] So for now, what I'm going to do is connect up my slab to this front material input.
[10:03] And you can see that most of the input parameters on my root material here went away.
[10:09] And that's because I have now I can use the input materials on the slab instead.
[10:16] Previously, I had base color, I had specular, I had metallic, and I had roughness.
[10:24] And now instead of those, I have diffuse albedo, f0 and f90 and roughness.
[10:31] And like I said, these parameters go a little bit deeper into the shading model than base color, specular, metallic and roughness did.
[10:42] But if I just if I'm just starting out and I haven't yet learned how to use diffuse albedo, f0, f90 and roughness,
[10:52] there is a pretty simple way of just using substrate exactly how I used to use it in the previous material system.
[11:03] I can just do a search for metal here and come down here and there's this node called substrate metalness to diffuse color f0.
[11:13] And I'm going to plop that node in.
[11:16] And what this does is it gives me the ability to input base color, metallic and specular just like I did before.
[11:25] And then it outputs diffuse albedo and f0 and I can connect those up to substrate.
[11:32] And now I can continue to work inside substrate with the same input parameters that I'm accustomed to.
[11:42] So previously we had this gold material going on.
[11:46] Let's see if we can get it back here.
[11:49] So let me copy this material color.
[11:54] OK, so now I've got the same base color set here as I did here on my previous material.
[12:01] I've set metallic to one and now I need to set my roughness to 0.15.
[12:09] So I'm going to set my roughness to 0.15 and wire that into roughness.
[12:16] And my specular, I've got it set to 0.5 over there.
[12:20] So I'll set it to 0.5 here.
[12:23] And now when I connect up my substrate slab, I've got the exact same material that I had before.
[12:31] Now, one of the things that I don't like about substrate is it increases the complexity of making a basic material.
[12:42] So with the way that I had it before, I could just set my base color to this color.
[12:48] My metallic to one, my specular 0.5 and my roughness to 0.5.
[12:53] I didn't need any nodes at all.
[12:56] But once I have a slab hooked up, now I need to hook up this substrate metalness to diffuse Albedo F0.
[13:03] And I need to define a color and create all of these values here.
[13:09] And it's just a little bit more of an involved process.
[13:13] Instead of just defining my parameters directly there, I have to create a few more nodes and wire up a few...
[13:21] A little bit more complex of a network in order to get what I had.
[13:26] But what I wanted to show you guys in this first video is just how to turn on substrate, why substrate is a thing,
[13:35] and then also just how we can get the exact same thing that we had with base color, metallic, specular and roughness.
[13:45] Now, next time in our next video, what I'm going to do is dive into this node here, the substrate metalness to diffuse Albedo,
[13:54] and show you exactly what's going on.
[13:58] Because I told you, diffuse Albedo F0, F0, these are lower level parameters,
[14:05] and they give us more flexibility than these higher level parameters, base color, metallic and specular.
[14:12] I'm going to show you what's happening inside of this node to convert our base color, metallic and specular,
[14:19] into diffuse Albedo and F0.
[14:22] I'm going to show you in the graph itself how to create what this node is doing.
[14:28] So you'll understand a little bit better what's going on under the hood,
[14:32] and what the relationship is between base color, metallic and specular, and diffuse Albedo and F0.
[14:39] That's going to be a great one, so please come back.
[14:42] We're going to be going through all of these parameters in substrate,
[14:47] and creating some much more advanced materials, and I'm excited to show you guys this stuff.
[14:53] So if you're not subscribed yet, be sure to subscribe so you get notifications when the new videos go out.
[15:01] And I'm going to be taking you through a journey learning all the inner workings of substrate, and it's going to be great.
[15:09] Thanks a lot for watching you guys, and be sure to come back next week.
[15:13] And until then, have a great week.



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
