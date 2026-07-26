---
title: How to Create Stylized Feathers and Fur in Blender
source: YouTube
url: https://www.youtube.com/watch?v=yR8FatqgTDQ
author: SouthernShotty
ingested: 2026-07-26
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-create-stylized-feathers-and-fur-in-blender/
frame_count: 0
frame_status: pending-selection
---

# How to Create Stylized Feathers and Fur in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=yR8FatqgTDQ)
**Author:** SouthernShotty
**Duration:** 18m31s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-to-create-stylized-feathers-and-fur-in-blender <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Overview [0:00]
**Transcript (timestamped):**
[0:00] Today we're going to be looking at how to create stylized fur and feather systems in Blender's geometry nodes.
[0:04] Now by default, when you create a system like this, you get a lot of ugly artifacts and a lot of ugly shadows.
[0:09] And it requires really high polygon counts or a huge amount of density, making it not very friendly on lower-end machines.
[0:17] With this version, we can use it with low-poly objects, less density, and in Blender EEVEE to get a nice, smooth stylized result.
[0:25] So let's dive in and get started.


### Building the System [0:27]
**Transcript (timestamped):**
[0:27] So we're going to cover a few things here. We're going to create a simple little feather.
[0:30] You can do a fur piece if you like.
[0:33] And then we're going to walk through how to create this material setup, which also utilizes a random color setup to add a bit more realism and variety there.
[0:44] And then we're going to walk through utilizing the Scatter on Surface modifier with some modifications.
[0:50] We'll walk through all the modifications I made here. You can see I've highlighted them in yellow so that we can reach this final effect.
[0:57] Now I'm going to use a simple sphere for this tutorial.
[1:00] And if you want to follow along exactly, I actually recommend coming up here to your extensions and enabling the Extra Mesh objects.
[1:09] And what that's going to do is provide some extra options here under the mesh because I like to work with the round queue, set this here to the quad sphere.
[1:19] And what this does is give us a sphere that won't have any pinching when we go to smooth it or add a subdivision.
[1:26] So I'm just going to right click this and shade smooth.
[1:29] And then I'm going to search for a modifier here and do a Scatter on Surface.
[1:33] I'm going to rename this up here to Feather Ball.
[1:36] And then up here under the assets, you'll see that I have also imported a very simple feather.
[1:42] Now I'm going to walk through the material and how to create this, but I'm not going to walk through how to create this feather.
[1:46] It's literally just a subdivision onto a plane scaled up on the Z-axis slightly.
[1:51] So I'm going to keep that on my asset folder and we're going to come here to our Feather Ball and start working with our modifier settings.
[1:57] So first thing I'm going to do is come down here to the object.
[2:00] And if you're doing something like fur or feathers, I might would recommend doing a variety.
[2:05] But for the sake of this tutorial, I'm just going to do a single feather.
[2:09] So I'm just going to search for Feather there, select it, and you see we're starting to get some feather spawning.
[2:13] Now this is way too light.
[2:15] So we're going to do a 150 density.
[2:17] I'm going to click Scatter on Instances here.
[2:20] Then I'm going to twirl down the transformation here.
[2:23] I'm going to align the rotation to the Y-axis.
[2:26] And you can see here that now all of our fur is pointing downwards like we would expect it to.
[2:30] And then I'm going to come down here.
[2:32] I'm going to click on the Randomize.
[2:34] I'm going to offset the Y by a tiny amount.
[2:37] I'm just going to do like 0.005.
[2:39] And then I'm going to play with the rotations here.
[2:41] I'm going to do negative 25 on the X, 15, and 15.
[2:46] Now I want to scale these axises just a bit.
[2:49] So I'm going to do 0.15 here and make sure that uniform is checked on.
[2:53] And now you can see that we're starting to get a bit more of a ruffled feather look.
[2:57] However, this doesn't give us that stylized look.
[2:59] Instead, we have these kind of just nasty chunky intersections.
[3:02] So let's look at how we can work on fixing that by modifying the modifier stack.
[3:07] But if you don't know, the Scatter On Surface modifier is actually just a geometry note set up
[3:12] that they've included as a preset.
[3:14] We are using the default Scatter Surface modifier here.
[3:17] But if you want to check out the MoGraph Toolbox, we have a free MoGraph array
[3:22] that has a widely expanded set of features.
[3:26] And then if you pay for the full pack, you can also get additional things.
[3:30] For example, fields, fall-offs, springs, and delays.
[3:33] Perfect for animating these type of things.
[3:35] But let's dive back into the tutorial.


### Geometry Nodes Setup [3:37]
**Transcript (timestamped):**
[3:37] Now we're going to pull up this middle screen here,
[3:39] and we're going to open a Geometry Nodes set up.
[3:42] And you're going to see here that you're not able to edit it.
[3:45] It's all grayed out.
[3:46] So what we need to do is just unpack the library.
[3:49] So if I click this unpack here, everything becomes editable.
[3:52] Now we're going to be adding three things here.
[3:54] One, we're going to add a normal modification
[3:57] so that we can get that nice, smooth, stylized look.
[4:00] Then we're going to go ahead and add some animation to our feathers.
[4:04] And lastly, we're going to add some attributes
[4:06] so we can output or randomize colors
[4:08] and get more stylized results within our shading,
[4:11] which we'll cover after this.
[4:12] Now I don't want this modifier stack to disappear,
[4:14] so I'm going to go ahead here and pen this.
[4:16] I'm also going to copy this title over here and rename this here
[4:20] so that the Geometry Nodes system also matches my modifier stack.
[4:24] Now by far, the most important part of this process
[4:27] is smoothing out the normals.
[4:29] So let's zoom in here, and we're actually going to do this
[4:32] right at the last step here.
[4:33] So I'm going to grab this group input here.
[4:35] I'm just going to move it out here
[4:37] so that we can insert some nodes here.
[4:39] So first thing we're going to do is we're going to grab this feather ball
[4:42] and I'm going to duplicate it
[4:44] because we're just going to use a sphere to reference for our normals,
[4:48] which is then going to smooth out the normals across all of these feathers.
[4:52] So I'm going to grab this, I'm going to call this normals.
[4:55] I'm going to delete the modifier stack here.
[4:57] I'm going to press forward slash here so that we can focus.
[5:00] I'm actually going to add a modifier.
[5:02] So I'm going to add a subdivision modifier one.
[5:04] I'm going to apply that.
[5:06] And then I'm going to move this here into the assets.
[5:08] So now I'm going to come back over here, hit forward slash again,
[5:12] and bring our focus back here to the object.
[5:14] Now what I want to do is tick on my assets up here.
[5:17] I'm going to grab that normals object
[5:19] and just drag that into the Geometry Nodes.
[5:22] And then we can close this again so that it's not distracting us.
[5:25] Now what we're going to do is search for a sample nearest surface.
[5:30] We're going to plug this here.
[5:32] Switch this over to a vector.
[5:34] And then we're going to plug our geometry here into the mesh.
[5:38] And so we're trying to grab the vector information from the surface here.
[5:42] And then we are going to search for a normal node.
[5:45] Bring this down here and plug our normals here into the value.
[5:49] Now if I search for a set mesh normal node, I can put this up here.
[5:53] And what I'm going to do is utilize the normals here from this,
[5:58] sampling the nearest surface size to feed into the normals
[6:02] and create a new set of normals for our object.
[6:05] So I'm going to switch this to free mode.
[6:07] And now we can set a custom normal.
[6:09] I'm going to drag this here into the custom normal and boom.
[6:12] You can see that now it's utilizing the shading normals
[6:16] from the smooth sphere that we created to apply across here,
[6:20] giving us a much smoother look and a more kind of stylized, nice finish.
[6:24] Now this was achievable before without geometry nodes.
[6:28] Utilizing a larger modifier stack of data transfers.
[6:31] However, I find this method to be much simpler and more effective.
[6:35] Now one thing I want to point out is that we're essentially using the normals
[6:37] from the sphere to shade this out and kind of give it a smooth look,
[6:41] even though there's all this geometry on top of it.
[6:43] And this works for most objects that I've tested on.
[6:47] However, if you start to get into some pretty complex character systems,
[6:50] trying to use a sphere to smooth out the normals might start to give you
[6:55] some kind of glitchy results.
[6:57] And in that case, I would recommend instead of using a sphere,
[7:00] creating an incredibly simple version of your character.
[7:03] So to keep these things organized,
[7:04] I'm just going to search for join in new frame here
[7:08] and just name this three normals.
[7:11] So let's look at how we can export a randomized color
[7:15] and add some animation here.
[7:17] We'll get started with animation first.


### Adding Animation [7:18]
**Transcript (timestamped):**
[7:19] So we're going to come a little further back here.
[7:21] I want to do this before the randomization.
[7:24] So I'm going to grab everything here and just move it off here to the side.
[7:29] Let's begin adding some animation.
[7:31] So what we're going to do is use noise with a scene time
[7:34] to kind of divide the position here.
[7:36] So we'll come here and we're going to add a scene time node.
[7:42] And this allows us to use either seconds or frames to drive data.
[7:46] We're going to take the frame here and we're going to plug this into a divide
[7:49] math node.
[7:50] Make sure it's plugged into the top node there.
[7:52] And then we can utilize this bottom node to control the speed of the frames.
[7:57] So I want mine to move pretty slow and subtle.
[7:59] I don't want it to move every frame.
[8:00] So I'm going to divide that by something large like 350.
[8:04] Now we need to get the position data of everything here into a noise texture.
[8:08] So I'm going to drag this here.
[8:10] I'm going to look for a combined x, y, and z.
[8:13] I'm going to plug this here into the x.
[8:14] Leave these bottom values at zero.
[8:17] Here I'm going to search for a position node and put that here.
[8:20] And then we're going to search for a add vector node.
[8:23] We're going to put this here.
[8:25] So we're going to combine our position and this scene driven data with our x
[8:29] factor here.
[8:30] And then that way we'll drive the x position of our elements.
[8:34] But I don't want it to be perfectly uniform.
[8:36] Instead I want to add some noise.
[8:38] So let's just search for a noise texture here.
[8:40] And I'm just going to leave these to the default settings and just plug the vector
[8:44] here right there.
[8:46] Now what I want to do is grab another add math node.
[8:49] I'm just going to borrow this math node over here.
[8:51] Switch this to add.
[8:53] And we're going to set this to zero and the bottom here to 0.5.
[8:57] What that's going to do is use this to combine it with the vector of the noise
[9:01] to kind of offset the noise and center it onto our object.
[9:04] So we'll go here for a subtract vector node.
[9:07] And we will plug the color of our noise into the top and the add value here to the bottom.
[9:14] So now we're going to use this information we have here to drive the rotation of our feathers.
[9:20] So let's grab a rotate instances here.
[9:23] And if we drag this over our line here, we're at the perfect place in the production line
[9:29] that we can drive the kind of rotation of our feathers, which is exactly what we want to do.
[9:34] And now we've created this little animation system up here.
[9:37] So let's join this into a new frame.
[9:39] And I'm going to name that frame animation.
[9:41] And then we're going to plug that vector down here into the rotation.
[9:46] And you can see how things are moving.
[9:47] So now if we hit play, you can see how it's adding just a little bit of subtle motion here.
[9:52] And you can play with the speed of the motion here.
[9:54] For example, if I set this to 50, you'll see it goes faster.
[9:57] If I set it to 500, it goes slower.
[9:59] So I'm going to leave mine at 350.
[10:01] You can choose which axis it's rotating on, though I recommend the axe.
[10:05] And then we're going to adjust the noise texture here if you like.
[10:10] So let's take a look at how we can also output a randomized color.
[10:14] And then we're going to work on a shader.
[10:16] And I'll also show you some render settings we can change to improve this even further.


### Creating the Shader [10:20]
**Transcript (timestamped):**
[10:20] So adding randomized for the color is super simple.
[10:23] We just need to capture an attribute.
[10:24] And we can actually just do that right here next to all the animation that we did.
[10:29] So let's store a named attribute.
[10:32] So I'm just going to drag this over the line there.
[10:35] And I don't want this to be part of the frame.
[10:36] This is something that happens a lot.
[10:38] You can do alt P or search for remove from frame.
[10:40] And we're going to change this to a color value and a instance.
[10:45] Because what we're trying to do is capture the color of all the individual instances
[10:49] of the feathers.
[10:50] And that's why it important that it comes down here before it's been realized
[10:54] so that we can get that information.
[10:56] So we just need to come up with a name here.
[10:58] I'm going to do ran color for random color.
[11:01] And then I'm going to drag this value off here.
[11:04] And I'm going to look for a random value node.
[11:07] Now I'm going to switch this to a float value.
[11:09] And I'm going to leave it at 0 to 1, which is just going to be white to black.
[11:13] And then I'm going to leave that into the value here.
[11:16] So at this point, we're actually done with the geometry nodes.
[11:20] So we're going to switch over to the shader editor here and start working on our feather shader.
[11:25] So I'm going to grab the feather ball here, click new material.
[11:28] And I'm going to name this feather mat for material.
[11:32] And I'm going to come up here to my assets.
[11:34] I'm going to grab that feather and I'm going to add that same material there.
[11:38] Now we're going to do a few things on this material.
[11:41] But before we get too far, I actually want to show you how that random color attribute is working.
[11:45] So if I grab color attribute here and just plug in ran color, which is what we called it.
[11:51] And then we plug that color here into the base color.
[11:53] And if I switch over to material preview, you can see how that is randomizing the color of all of our instances.
[11:59] But we'll unplug that for now because we're going to do a few other things to our feather.
[12:02] And in fact, I'm going to grab the feather asset we had, forward slash on that so we can zoom in and start working on some noise texture here on our feather.
[12:10] Now I want to do a couple things here with the material.
[12:13] One, I want to create a gradient from one side of the feather to the other.
[12:16] I want to add some nice little lines for a feather texture.
[12:19] I want to randomize the color of all the feathers.
[12:22] And then I want to add an artificial rim light here.
[12:25] So we're going to look at how to do all of that.
[12:27] So first I'm going to focus in here on the feather.
[12:30] We're going to get started with the gradient first.
[12:32] I'm going to add a gradient texture here.
[12:35] I'm going to set it to linear and let's take a look at what that looks like.
[12:39] It's going the wrong direction.
[12:40] So here's a pretty simple trick.
[12:42] Now, if you have no Wrangler add on enabled, you can grab this and hit control T and you'll get a texture coordinate and mapping node.
[12:48] And I'm just going to plug in the UV here.
[12:51] And then I'm going to move this over, look for a separate X, Y and Z.
[12:56] Going to click this here and then I can change the direction of the linear gradient just by plugging that into the vector.
[13:02] Now I can control that with a gradient ramp.
[13:05] So if I add a color ramp here, I can then control how intense that gradient is.
[13:10] So I'm going to set mine here to be spline, which is going to give me a much softer fall off and drag this down ever so slightly.
[13:17] Now I'd like to add a feather texture.
[13:19] So I'm just going to use a simple noise texture.
[13:21] Hope you grab a noise texture here.
[13:24] I'm going to change my scale to two and this value down here, the distortion value to 1.1.
[13:31] And let's take a look at that.
[13:33] And you can see we're starting to get some swirls there.
[13:35] And I want to stretch those out so that we kind of get those feathered lines.
[13:38] I'm going to hit control T with this selected here.
[13:40] I'm going to switch this over to UV and then I'm going to take the X scale and scale this by five.
[13:45] And now we're kind of getting a stretched mark there.
[13:48] So now I want to mix those two colors together, which is pretty simple.
[13:51] So I'm going to grab this here, move this up.
[13:53] I'm also just going to go ahead and grab a color ramp, move this here.
[13:57] That'll allow me to control that if I don't like the end result.
[14:00] So let's combine these two colors together.
[14:02] We'll use a mix color node.
[14:04] So search for mix color.
[14:06] I'm going to leave it at mix and I'm just going to plug the top ramp there into the A slot and this into the B slot.
[14:13] Let's take a look at that.
[14:14] I'm going to lower the factor here and now you can see we're kind of starting to get a blend between the two.
[14:19] So now let's add that random color factor.
[14:22] Here you can see that it is red because this is just a single feather and we need instances for it to work.
[14:28] So let's zoom out here, grab the feather ball here.
[14:31] And what I'm going to do is move this over here and we're going to plug this random color into a color ramp.
[14:39] Now, currently I'm not going to change anything, but we can use this if we like to change the color values.
[14:45] So I just like having that there for control.
[14:47] But instead, what I'm going to do is mix this into another color node, plug this down here into the B,
[14:54] plug this one up here into the A, and then I can kind of change how much that is laying on top of itself there.
[15:01] So I'm going to set it to something like 0.25.
[15:04] And then next I want to add some rim lighting and also some color to these feathers.
[15:09] So I'm going to grab another color ramp here, put it here at the end and just choose some colors here.
[15:16] I'm going to go for kind of a orangish look.
[15:19] So I'm just going to put kind of a bright orange there and maybe a slightly darker orange there.
[15:25] And things are starting to come together.
[15:27] So let's take a look here.
[15:29] I'm actually going to plug in our VSDF node again here.
[15:32] I'm going to turn the roughness value up to 1 and then I'm going to make sure Metallica set to 0.
[15:39] And I want to add a rim light here.
[15:41] So I'm going to search for a layer weight, bring this over here.
[15:45] I'm going to leave it at 0.5 and everybody yells at me because they always call this Fresnel, but it is Fresnel.
[15:52] And so I'm going to drag the Fresnel off into the color ramp factor and take a look at that.
[15:58] And what I'm trying to do is kind of create a rim light.
[15:59] So I'm going to drag this down ever so slightly.
[16:02] And a nice thing here is that we can grab a hue and saturation value.
[16:07] We'll put this here and this will allow us to change the hue, color and brightness of our feathers.
[16:12] And we can use this to create an artificial rim light.
[16:15] So I'm going to plug this into the factor and then we're just going to adjust a few values here.
[16:19] So I'm actually going to leave the color and saturation the same and instead just kind of brighten the color.
[16:23] And so if I press 5 there, you can see now it looks like we're getting a stylized light behind our feathers.
[16:29] Now I want to point out one thing I noticed is that we had all that work to mute these normals here and make sure everything blends together.
[16:39] But because we've added a gradient, we've essentially brought some of that separation back visually, losing some of our stylized look.
[16:46] So I recommend playing with the gradient ramps here, maybe reducing the amount of the ramp there and you'll kind of get that smooth look back in.
[16:54] But if you have too much of a gradient ramp, you're essentially just kind of creating false shadows, which is what we did all that hard work to get rid of.


### Final Tweaks [17:00]
**Transcript (timestamped):**
[17:00] Now there's a few render settings we can change here in EV to make this look even a little better.
[17:04] So let's take a look at those.
[17:05] So this effect actually looks best without ray tracing on.
[17:09] You can see if I add ray tracing, it starts to kind of add those shadows back in and we're getting that weird separation.
[17:15] However, if you want to have ray tracing on, then what I recommend doing is coming here under your settings here and coming down to your fast GI approximation.
[17:23] And you can either turn that off, which will kind of bring you back to your stylized look.
[17:27] Or if you really want that global illumination, you can change a few settings here to make it a little less intense.
[17:33] So right now we have a lot of rays bouncing around, but if you turn this down to like one ray and like four rays right here, and then you bring the thickness down to something like point one and the bias up to something like point two five,
[17:47] you end up getting a much smoother look.
[17:49] So if you're utilizing this to create fur or feathers, I recommend making these changes in EV.
[17:54] If you want to duplicate this, you can create multiple feather systems on your object and you can come down here to the instancing and change the
[18:03] size of your feathers.
[18:05] And so you can create a cluster of small fur like short fur, big fur, you know, small feathers, big feathers, fluff feathers, whatever.
[18:14] And then you can utilize the density mask here and come over to your vertex groups and actually weight paint in different types of feathers and links of fur in various areas to get a much more kind of controlled and realistic result,
[18:27] which is what you would see, for example, in a final game render.



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
