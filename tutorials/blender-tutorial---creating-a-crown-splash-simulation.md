---
title: Blender Tutorial - Creating a Crown Splash Simulation
source: YouTube
url: https://www.youtube.com/watch?v=KbAUrN0ExjM
author: Blender Made Easy
ingested: 2026-08-17
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-tutorial---creating-a-crown-splash-simulation/
frame_count: 0
frame_status: pending-selection
---

# Blender Tutorial - Creating a Crown Splash Simulation

**Source:** [YouTube](https://www.youtube.com/watch?v=KbAUrN0ExjM)
**Author:** Blender Made Easy
**Duration:** 13m20s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-tutorial---creating-a-crown-splash-simulation <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome to another Blender Made Easy tutorial. Today we're going to be creating this Crown Splash Simulation Render in Blender.
[0:06] We're going to go through the simulation, create the materials, and how to properly light this glass material.
[0:12] So let's jump into Blender and get started.


### Animation [0:14]
**Transcript (timestamped):**
[0:14] Alright, here we are in a brand new scene and this time we're not going to delete the default cube.
[0:18] Instead, we're going to be using it as our domain object.
[0:21] Now when you're creating a Crown Splash in real life, normally it's only just a couple of centimeters wide.
[0:27] If we tried to do that in Blender though, it's just not going to simulate the fluid properly.
[0:31] We need to make sure that we simulate at a very large scale.
[0:35] So for our domain object, I'm going to open up the properties tab and the only thing I'm going to change is the Z axis here.
[0:41] Instead of two meters, we're going to go a little bit lower to around like 1.7 or so, just so it's a bit shorter.
[0:47] Then in the front view, I'm going to press Shift D on this, then scale this along the Z axis so it's a bit smaller.
[0:53] This is going to be our flow object.
[0:55] We're going to drag this all the way to the bottom and then maybe scale it slightly outside of the domain.
[1:01] Let's drag everything up along the Z axis so it's sitting on the grid floor.
[1:06] Then for our collision object, we're going to be adding in a mesh and then use an icospere.
[1:11] Over in the properties down here, let's bring up the subdivisions up to a level of five here
[1:17] so that we have a very smooth icospere.
[1:19] Then we'll just go over to the properties and click and drag and we'll set this down to around three five zero three five.
[1:26] Now what we want to do is we want to animate the icospere crashing through the flow object
[1:31] and we want to skip a couple of frames for the fluid to actually settle down.
[1:35] So on frame five here with the icospere selected, I'm going to hit K and then add in a location keyframe.
[1:42] Jumping five frames later, we're going to drag this below the domain object right about there.
[1:48] Hit K again and then add in another location keyframe.
[1:53] With both of these keyframes selected here in the timeline, I'm going to hit T and then switch the
[1:57] interpolation over to linear so it moves at a constant rate.
[2:02] And that's basically all we need to do for our animation.


### Physics Settings [2:05]
**Transcript (timestamped):**
[2:06] Next, for the actual physics, let's select our domain object, jump over to the physics properties,
[2:11] click on fluid, change the type over to domain.
[2:15] And then for the domain type, we're going to switch it over to liquid.
[2:19] Now before we do anything else, let's scroll down to the cache settings here and change the
[2:23] type from replay over to modular and then make sure resumable is turned on so we can bacon the
[2:29] mesh right here later. For the end frame, we don't need a lot of frames, we only need around like
[2:35] 20 or so. So we're going to set the end frame to 20. And then we're going to scroll back up to the
[2:40] top here. So for the first setting here, the resolution divisions, this controls how good
[2:45] the simulation will look. Normally, you want a pretty high resolution here, but since we're
[2:49] dealing with a small scale simulation, we want it to look really small, we're actually going to
[2:54] leave the resolution divisions at a lower number. Let's go with 115 subdivisions. The time scale
[3:02] here, we're going to go with a value of 0.5. This will just slow down the simulation. And then for
[3:08] the time steps, maximum and minimum values, since our object is moving very quickly over the course
[3:14] of five frames, we want to turn the time steps up just a little bit to make sure everything
[3:19] simulates properly. So we're going to go with a value of eight for the maximum, and then a value
[3:24] of four for the minimum scrolling down a little bit more the flip ratio, this just adds a little bit
[3:30] more splashes to our simulation. Let's go up to 0.99 like that. The particle sampling will go up to a
[3:39] value of three, this will just increase the number of particles in our simulation. And a very important
[3:45] setting is the randomness, we're going to go all the way up to a value of two. This is just going
[3:49] to give our particles a more natural look when the collision actually happens. Another very important
[3:55] setting here is the fractional obstacles, make sure this is turned on, this will just smooth out the
[3:59] collision and make it look a little bit more accurate. If this is turned off, your simulation
[4:04] will most likely not work with the crown splash. So make sure this is turned on. Next, we're going
[4:09] to open up the mesh tab right here. And this controls all of these settings for the actual
[4:14] mesh that will be applied to the particles. Once we bake it in the up res factor, we're going to
[4:19] leave at two, the particle radius, though, we're going to go up to a value of three. Like I mentioned
[4:24] earlier, with the low resolution here, we want to make sure this looks like a very small scale
[4:30] simulation. So having the particle radius, which is basically the mesh around each particle, having
[4:35] that slightly bigger, will make it look like it's a small scale simulation. The other thing we're
[4:40] going to do is this smoothing positive will go up to five, this will just smooth out the overall
[4:45] mesh once we bake it in. And that's basically all we really need to do for our domain settings.
[4:51] For the flow object, select it, click on fluid, change the type over to flow. For the flow type,
[4:57] we're going to change it to liquid, and then we'll leave it at geometry. For the icospir,
[5:02] select it, click on fluid, this time we're going to go with an effector. And then for the sampling
[5:08] sub steps, we're going to go up to a value of five, this will just make sure it simulates properly
[5:13] because it is moving pretty quickly here. And with that done, go ahead and select all of your
[5:20] objects and press Ctrl A apply the scale so everything is set to one in the properties right
[5:26] here. Then with the domain selected, make sure you save your project and then click on bake data.
[5:32] Once the bake is done, we'll bake in the mesh and then we'll see how the overall simulation looks.
[5:36] Once the initial bake is done, you can scroll down to the mesh panel right here and bake in the mesh
[5:41] as well. Now that the bake is done, you can scroll through the timeline and see how your crown splash


### Scene Setup [5:42]
**Transcript (timestamped):**
[5:46] looks. You can see on frame 12, that actually looks pretty nice. And then you can go even
[5:51] further to get even a more chaotic render just like this. And that is looking pretty good.
[5:57] Now for the next step, we're going to jump over to the modifier tab, add in a new modifier, and we're
[6:01] going to add in a smooth modifier on top of all of the mesh here. So we can go over to deform,
[6:07] click on smooth. And then for the factor, we'll go up to a value of one. And then the repeat option,
[6:13] we're going to go all the way to let's try like eight or so. And that should help smooth out all
[6:18] of the mesh. And you can see that is looking pretty good. You can also right click and shade
[6:23] smooth as well. And now our fluid is looking pretty nice. The next part of this tutorial,
[6:29] we're going to go over the lighting and how to properly render a cool image with this crown
[6:34] splash here. So the first thing we'll do is over in the outliner, we don't want this flow object to
[6:39] show up in the render. So let's hide it from the viewport and from the render by toggling both of
[6:43] those icons. Then we'll position the camera, I'm going to go into the front view, and then hit
[6:49] control alt numpad zero to snap the camera to place. Or you can go over to view, align view,
[6:55] and then select a line active camera to view that does the same thing. Then just select it,
[7:01] and drag it backwards and find a cool position that you want to render. And I might go to frame 12,
[7:08] 13, 12, yeah, we'll go to frame 12, and then we'll zoom in probably around here or so.
[7:16] And the other thing we want to do is jump over to the object data panel with our
[7:21] camera selected. And we want to bring the focal length up much higher. And again, since we're
[7:25] trying to simulate this at a small scale, we want the focal length to be much higher, we're going to
[7:31] go all the way to around 200. And then I will zoom backwards. And now we have this sort of look.
[7:37] And that is looking pretty nice. As for the material, we're going to jump over to the material
[7:42] panel here. And then for the surface, we'll just change it over to a glass shader, the roughness
[7:47] go down to zero. And then the IOR, which is index of refraction, we're going to go up to 1.333,
[7:54] since that is the IOR of water. The other thing I want to do is over in the render engine,
[7:59] we're going to switch over to cycles, just because the glass renders a lot better in cycles, and it
[8:03] will just look overall nicer with the correct glass shader. So now let's jump into the camera
[8:10] view once again and see what this looks like. And we can't see anything, there's barely anything
[8:15] visible because it's a glass shader, and there's nothing to reflect. So first off, let's add in
[8:21] a background, I'm going to press shift A, go over to mesh, and then add in a plane, we'll rotate this
[8:26] plane at 90 degrees, and then drag it backwards about seven or so meters, we'll just type in seven.
[8:33] And then we'll scale this up pretty big. So we have this backdrop just like that.
[8:38] And now if we go into the render view, now we can actually see something a little bit more,
[8:42] you can see this is starting to look better, but we can really improve the look of this whole scene
[8:48] by just doing a couple of things. First off, for the background, I want this to be black, so we'll
[8:53] create a new material, set the base color much lower to around, not fully black, but somewhere
[8:58] around there. And then the roughness, I'm going to go all the way up to one, so there will be barely
[9:03] any reflection. The other thing I want to do is I want to position a light right behind the glass.
[9:09] This is going to give a really nice look when you look through the glass and see the light
[9:14] on the backdrop here. We'll bring up the radius just a little bit, and then for the color,
[9:20] let's go with a nice blue color somewhere around there. Now if we look through the camera view,
[9:26] you can see this is starting to look better. But now we need a light above the glass here
[9:32] to really get this to stand out. So in the side view by hitting three, we're going to press shift D
[9:37] on this lamp, place it right about here. And we'll try a strength of around 10,000 or so.
[9:44] And then we'll bring the saturation so it's not as blue, something like that.
[9:49] Let's take a look at this. And you still really can't see that much. And the reason for that is
[9:54] because there's nothing to reflect underneath here to give us that glass look. So for this,
[9:59] we'll add in a mesh and then a plane scale this plane along the X. So it's a bit skinnier. And
[10:05] then we'll drag it forward somewhere like around here or so. And now since we added that that
[10:12] should reflect some light, you can see here we now have some white light appearing just like that.
[10:18] The next thing we'll do is we will go over to the render scene panel here, scroll down to the
[10:23] color management and set the look to very high contrast. And this will really make our glass
[10:28] look a lot better. And the other very important thing that we need to add is depth of field,
[10:33] because at the moment, everything is in focus and it just doesn't look that good. So what we can do
[10:38] is we first need a focus objects, you can do this by holding shift, right click to place our cursor
[10:44] right at that location in the front there, I'm going to add in a new empty object,
[10:48] just maybe scale it down a little bit. And then with the camera selected, let's jump over to the
[10:53] camera settings, depth of field. And then for the focus object, we'll use that empty that we just
[10:58] added. And now if we go back into the rendered view, we should be able to see what that looks like,
[11:04] you can play around with the stop the lower you go with this, the more depth of field
[11:08] will appear in your scene. And you can see there that's starting to look pretty nice.
[11:14] You can also play around with the frame that you want to actually render your crown splash,
[11:18] you can see there that might look a little bit better if you don't want all of these really long
[11:23] water spouts that are going out. Over in the render scene panel, I'm going to turn on the noise in
[11:29] the viewport so we can actually see this a bit better. And then for the samples right here,
[11:34] we don't need 4000 samples, let's go down to around like 500 or so. Once you have finally set up your
[11:40] render and you're ready to go, go ahead and save your project and then hit F12 to render out an


### Alternate Scene Setup [11:45]
**Transcript (timestamped):**
[11:45] image. One other thing that I'll show you real quick, if you don't want to render out a glass
[11:50] shader instead, if you wanted to do one color of liquid, which looks pretty nice, like you saw at
[11:55] the beginning of the video, that's very easy to do. All you have to do is just select your object.
[12:00] And over in the material tab, change this back over to a principal BSDF. And then from here,
[12:06] you can just bring down the roughness set to zero. The light is now way too strong since it's not a
[12:11] glass shader. So you'll need to bring this down to maybe only like 500 or so. And you can see this
[12:16] is now the effect that you get. Now, if you wanted it to extend across across all of the
[12:22] background so you don't see this harsh cutoff here, all you would have to do is just add in a new plane
[12:27] object and bring this plane down a little bit. So it's slightly like below just like this and then
[12:34] scale it out pretty bit. And then this needs to have the same material as the other one. So go
[12:39] ahead and select that material here. And now you can see you might need to drag this up just a
[12:44] little bit. Now you can see there's not really a cutoff there, it kind of blends seamlessly. And now
[12:49] you get this sort of look. And you can play around with the color, you can do like a blue, red,
[12:54] orange, whatever you want. And you can create some really interesting renders just doing that sort


### Outro [12:58]
**Transcript (timestamped):**
[13:00] of effect. But there we go, that is how you create a crown splash simulation in Blender. If you want
[13:05] to grab the blend file for this video or any of the other videos I've ever created on this channel,
[13:09] you can find the link to my Patreon down in the description. And if you have other ideas for tutorials
[13:14] you'd like to see in the future, let me know in the comments down below. Thanks again for watching
[13:18] and I'll see you guys in the next one.



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
