---
title: Blender 3.0 Tutorial - Creating a Glowing River
source: YouTube
url: https://www.youtube.com/watch?v=YwDj4bs4bSY
author: Blender Made Easy
ingested: 2026-08-17
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-30-tutorial---creating-a-glowing-river/
frame_count: 0
frame_status: pending-selection
---

# Blender 3.0 Tutorial - Creating a Glowing River

**Source:** [YouTube](https://www.youtube.com/watch?v=YwDj4bs4bSY)
**Author:** Blender Made Easy
**Duration:** 14m48s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-30-tutorial---creating-a-glowing-river <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Creating the River [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome to another Blender Made Easy tutorial. Today I'll be showing you how to create this glowing river using Mantaflow and foam particles.
[0:09] To get started we need a river for the fluid to go through. This can easily be created with the Landscape add on, so make sure you go over to your preferences and enable it.
[0:18] Next, delete the default cube and then press Shift A and we'll add in a mesh and then a landscape.
[0:24] Before you do anything else make sure you open up this menu and here is where we can change the preset over to a river. Now we have a basic river to play around with.
[0:33] There are a lot of settings on the left side that we will change, but the first thing that we need to do is turn off water plane. Since we're having a fluid simulation we don't need a water plane in the scene.
[0:44] Next up let's go up to the top. There are two sizes right here, the mesh size and then the size down here. You can think of the mesh size as the actual size of the mesh and then the size right here is for the displacement texture.
[0:56] Let's set both of the mesh size up to a value of 5 for each both the X and the Y.
[1:02] Next up, the texture is currently in the wrong position so let's bring up the X a little bit until it matches the edges just like that.
[1:10] And as for the Y we will drag this up as well to stretch out the river. The distortion allows you to change how the river is going to look. The higher you bring this up the more distorted it'll be.
[1:21] We're going to bring this down a little bit so the river is not so distorted. The depth value is the detail for the texture. If you drag this down it's going to make the texture look a lot more low poly.
[1:32] If you drag it up though it's going to stop at a certain point because it's based on the resolution divisions.
[1:38] The height settings controls the height of the texture. If I drag this up it's going to bring up the texture quite a bit. We're going to bring this all the way up to a value of 1.
[1:47] And the offset controls the width of the river. Let's go up to a value of negative point 1 and enter.
[1:54] You can see the top of our landscape is completely flat. Let's change that by bringing up the max height. Let's go up to a value of 1 so it doesn't clamp down on the top of the river.
[2:05] Finally the amount at the bottom controls how many layers it'll have in the river. If you drag this value up you're going to have repeating patterns. I'm going to bring it down to a value of 1.
[2:15] Play around with the settings until you are happy with the results and once you are done with them you can move on. Here are the exact settings that I used for this tutorial.


### Domain Settings [2:23]
**Transcript (timestamped):**
[2:24] Now that we have our river in place let's go ahead and add in the domain object and the flow objects. I'm going to press shift A and add in a new cube and scale it to match the size of the river.
[2:36] Another thing that we're going to do is select the river and then rotate it just slightly so the water flows downwards. So jump into side view and press R to rotate it and rotate it just very slightly so it's at a downward angle.
[2:50] And then make sure the domain size fits the entire thing. Something like this will work perfectly fine. And as for the flow object let's add in a new plane.
[2:59] I'm going to rotate this plane 90 degrees along the x axis and then place it in the back of the river. Scale it down and then place it over here. You also want to make sure it's not too big or you're going to have too much water in your scene.
[3:11] So roughly around this size is pretty good. Another thing to note is you don't want to have it too close to the domain edge or the flow object is not going to work properly. So make sure there is a little bit of a gap between the edge and the flow and you should be good.
[3:27] Now that all of our objects are in place let's go ahead and select the domain, select fluid and set the type over to domain.
[3:35] We're going to set the domain type over to liquid and before you change anything else let's scroll down to the bottom and change a couple of settings in the cache.
[3:43] First off I'm going to change the type over to modular so we can actually bake it in. And I'm also going to set the end frame to 400.
[3:50] The reason for this is because it takes around 150 frames for the fluid to reach the end of the river and I don't want to render those extra frames. I only want to render the fluid as it's all the way at the end.
[4:02] So setting the end frame to 400 will give us a lot of extra frames to render it out.
[4:08] I'm also going to turn on is resumable and then make sure you set the format volume from open VDB over to Unicash.
[4:15] We're going to be enabling speed vectors in the mesh and Unicash is the only format that allows that.
[4:21] With that done we're going to set the resolution divisions up at the top to 256.
[4:26] And for the time scale we're going to bring it down to a value of 0.5 just so it slows down the simulation quite a bit.
[4:33] Next up underneath the border collisions we're going to turn off the front and the bottom.
[4:38] If these are enabled the fluid will start to bunch up in the domain and then fill up the entire thing.
[4:43] With it turned off the fluid will disappear as if there is no domain object right there.
[4:49] For the liquid settings we're going to bring up the narrow bandwidth up to a value of 6.
[4:54] This is going to give us a thicker band of particles which means more fluid.
[4:58] Then you want to make sure that fractional obstacles is enabled and this will make sure the fluid does not stick to the collider as much.
[5:04] Next up we're going to open up the particles and then we're going to enable foam particles.
[5:09] I've tested out spray foam and bubbles and I found that foam looks the best in this situation.
[5:14] So make sure foam is enabled and there are a couple of settings that we're going to change.
[5:18] If you take a look at this simulation on screen you're going to notice some flickering along the particles.
[5:24] And the reason for this is just because Mantaflow is not the best fluid simulation there is some glitches in the particles and that's why you get that flickering.
[5:33] After about 20 simulations and a couple of headaches I found that there is not a great way to get rid of that flickering
[5:40] but there is a couple of things that you can do to reduce it.
[5:43] One of the things is to turn off the potential radius and the particle update radius.
[5:48] These will help smooth out the grid of particles.
[5:50] I found that a value of 4 works pretty well to get rid of some of the flickering.
[5:55] Another thing that you could do is go up to the top and turn up the time steps.
[5:59] I found that this sometimes works but then sometimes it doesn't and this is also going to increase the bake time
[6:05] so I'm just going to leave it at a value of 4 and 1 for the time steps.
[6:09] Finally we're going to add in a couple more particles along the wave crest.
[6:13] This is going to increase the number of particles along the edges and the wave crest of the fluid.
[6:18] We're going to bring this up to a value of 300.
[6:23] Finally we're going to enable mesh and then open up this panel.
[6:26] We're going to leave the up rest factor at a value of 2 and this will help smooth out the fluid.
[6:31] And we're also going to bring down the particle radius.
[6:34] This is the radius around each particle.
[6:37] Every single particle in the scene is going to have a radius of a mesh.
[6:41] This means that it's going to connect all of them and that is how the mesh is created.
[6:45] If you bring the radius up higher it's going to be a very blotchy looking mesh
[6:50] and if you bring it lower it's going to be a lot sharper.
[6:53] So we're going to bring this lower to a value of 1.2 and enter.
[6:57] Then also enable speed vectors.
[6:59] This is going to allow us to add motion blur later in this tutorial.


### Inflow & Effector [7:02]
**Transcript (timestamped):**
[7:03] With that done we're going to select our flow object, select fluid and set the type over to flow.
[7:08] For the flow type we're going to select liquid and then for the flow behavior we're going to choose inflow.
[7:14] Open up the flow source and since we are using a plane we need to make sure is planar is enabled.
[7:21] I also want to give the fluid a little bit of initial velocity so check that box
[7:25] and then underneath the y we're going to go up to a value of negative 0.5 and enter.
[7:31] This way the fluid will shoot out along the negative y direction and then go along the river.
[7:36] And since we rotated this plane we need to press ctrl a and apply the rotation.
[7:41] Next up we're going to select our river, add in a fluid and set the type over to effector.
[7:47] And then make sure is planar is enabled because this is a plane object.
[7:52] And that is basically all we really need to do.
[7:55] At this point we can select our domain and then bake it in.
[7:58] Make sure you save your project before you do this.
[8:01] The liquid particles look good so let's go ahead and bake in the particles next and then we will bake in the mesh as well.


### Creating the Foam [8:11]
**Transcript (timestamped):**
[8:11] The fluid simulation has finished baking and here is the result that we get.
[8:16] This is looking pretty good so far and you're going to notice that the fluid fully reaches the end at around 160.
[8:22] So what we're going to do is set the start frame of the timeline up to a value of 170.
[8:27] Next up we need to add in an object to be the particles.
[8:30] At the moment they are all just points in 3d space and they don't have any mass.
[8:34] So let's go ahead and add one in.
[8:36] We're going to press shift a and add in a cone object.
[8:39] Before you do anything else open up this panel and set the number of vertices down to a value of 3.
[8:44] Since there is going to be a lot of particles we need to make sure we have the least amount of geometry so it doesn't lag our scene.
[8:51] Scale this down quite a bit and then move it over to the right side and scale it down even more.
[8:56] We're going to assign this to be the particles so go ahead and select the domain and jump over to the particle system tab.
[9:02] You can see two particle systems.
[9:04] We don't need the liquid particles so make sure that is disabled in the viewport.
[9:08] Then select your foam particles.
[9:11] Before you do anything else you can see the number of particles is quite high.
[9:15] So let's open up the viewport display and set the number in the viewport down to a value of 1%.
[9:21] This will really increase our viewport display as you can see here and now we can move around pretty easily.
[9:26] We're going to choose render as halo to render as object.
[9:30] Then for the instant object select the cone in the drop down menu.
[9:34] Make sure that you zoom in and check the size of it.
[9:37] As you can see they are quite small and I think that is pretty good.
[9:40] But you might want to do some testing with this to see if it will look good in the rendered view.
[9:45] For now I'm just going to leave it as it is.
[9:47] One thing to note is with the viewport display even if you have it at 1% for the viewport it will also show up as 1% in the rendered view.
[9:56] So what we need to do is turn it off in the viewport and then bring the amount all the way back up to 100%.
[10:03] Now you can see they are not in the viewport and we can still move around but it's not going to affect the performance as we are working in our scene.


### Materials [10:09]
**Transcript (timestamped):**
[10:09] With that done we are ready to create a material.
[10:12] Go ahead and select your cone in the outliner and then give it a new material.
[10:16] We're not going to need the principle shader so delete it and then press shift A and add in a shader and an emission shader.
[10:22] Here is where you get to set the color of the light in the river.
[10:25] I thought a blue light looked pretty cool so we're going to bring it up to a nice blue color.
[10:30] As for the strength of this, this is also something you're going to want to play around with.
[10:34] If you don't have a lot of particles in your scene you're going to want to turn the strength up.
[10:38] But if you have a lot of particles you want to keep the strength at a value of about 4 or 5.
[10:43] Since we have a lot of particles let's go with a value of 5 and we'll see what that looks like in the rendered view.
[10:49] Next up let's select the domain which is the fluid itself.
[10:52] We're going to give this a new material by clicking new.
[10:55] We're going to delete the principle shader and then press shift A and add in a glass shader.
[11:00] Take the BSDF and plug it into the surface and then set the IOR to a value of 1.333.
[11:07] This is the IOR of water.
[11:09] As for the color we're going to drag it just very very slightly up to a nice blue.
[11:15] The other thing that we're going to add is some volume inside the water itself.
[11:19] Since we are creating a river it's not going to be perfectly clear.
[11:23] There's going to be some dirt and other stuff inside the water.
[11:26] So let's add in a new shader.
[11:28] We're going to go to the principled volume shader and we're going to choose the principled volume shader and place it right here.
[11:35] Let's go into render view to see what it looks like and I'm also using cycles for this scene.
[11:40] Take the principled volume and plug it into the volume of the material output.
[11:44] We're going to set the density of this to a value of 0.5 and as for the color we're going to go with a nice blue color somewhere around here.
[11:52] Here is a test render and as you can see the particles are still looking a little bit too big for my liking.


### Adding Vector Blur [12:12]
**Transcript (timestamped):**
[12:18] So what I'll do is I'll exit out of this window and select the domain and go over to the particle system tab.
[12:24] The scale of them we're going to bring down to a value of 0.03 and I think that should be pretty good.
[12:30] Also make sure you come over to the render layers panel right here and enable both the vector and the Z pass.
[12:37] Since we enabled speed vectors in the domain we need to make sure these are enabled so we can add in motion blur.
[12:46] With that done let's render this one more time and see what it looks like.
[12:49] The render has finished and here is the result.
[12:52] As you can see this is looking a lot better.
[12:54] Here is the previous version and here is the second version.
[12:57] If you still think it's too big or if there are too many particles just bring down the size or the amount in the viewport display and it'll also affect the render.
[13:05] For now though let's exit out of this window and jump over to the compositing workspace.
[13:09] I'll show you real quick how to add in motion blur.
[13:12] Check use nodes and then press n equals off that panel and we also don't need the bottom panel as well.
[13:18] Over here you can see we have a depth and a vector pass.
[13:22] If you saw my motion blur fluid tutorial a couple weeks ago you'll know exactly what we're going to do.
[13:26] I'm going to add in a filter and then a vector blur node and place it right here.
[13:31] Let's take a look at this by control shift left clicking on this to add in a viewer node.
[13:37] What we're going to do is take the depth plug that into the Z and the vector into the speed of the vector blur.
[13:44] Once this renders we can see exactly what this looks like.
[13:47] As you can see this is quite a lot of motion blur and I think that's a bit too much so let's bring it down to a value of about 0.4.
[13:54] You can also bring down the samples to a value of 16 and this will help improve render time so it doesn't have to calculate 32 samples.
[14:01] You might have a drop in quality just the tiniest bit but I think it's worth it to decrease the render time.


### Outro [14:06]
**Transcript (timestamped):**
[14:07] And there we go that is basically all you really need to do.
[14:10] At this point you can play around with the size of the particle like I mentioned earlier.
[14:14] You can play around with the strength and the amount of particles and get the desired look that you want.
[14:20] You can also add in some glare in the compositor to give a nice glow to the entire river but I'll leave that all up to you guys.
[14:27] Thank you very much for watching this tutorial and if you created something cool from it I would love to see what you create so make sure to send it to me on Instagram at BlenderMateEZ.
[14:36] I hope you all are excited for the new year and I look forward to creating a lot more tutorials and content for you guys.
[14:42] Thanks again for watching and I will see you in the next one.



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
