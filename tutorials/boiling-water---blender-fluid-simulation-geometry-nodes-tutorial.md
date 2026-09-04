---
title: Boiling Water - Blender Fluid Simulation + Geometry Nodes Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=MRGgqR1N_b8
author: CGMatter
ingested: 2026-09-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/boiling-water---blender-fluid-simulation-geometry-nodes-tutorial/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: []
---

# Boiling Water - Blender Fluid Simulation + Geometry Nodes Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=MRGgqR1N_b8)
**Author:** CGMatter
**Duration:** 22m13s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py boiling-water---blender-fluid-simulation-geometry-nodes-tutorial <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today I want to talk about boiling water, and more specifically how to get the best result in all of Blender YouTube tutorials.
[0:06] And I'm gonna show you two different methods to do this.
[0:09] One is the obvious, like, I'm gonna simulate it, approach, which is great, it has all these bubbles and whatever.
[0:14] But it takes a long time to compute, and it's hard to edit.
[0:17] The second method, which I'm more excited about, is how to fake it in geometry nodes, to the point where it looks really good, at least to my eye, but also runs in real time.
[0:26] This video is sponsored by Squarespace, it's the best way to make a website.
[0:30] Mine, which is cgmatter.com, is made and hosted with Squarespace, and there are three features that I really like about it.
[0:36] The first one is the integrated payment Squarespace payments.
[0:39] This lets me take the monthly subscription part of my website, and the payments work right through Squarespace.
[0:45] Speaking of that area, there's a lot of assets, whether that be like images or videos or whatever, and Squarespace's asset library lets you store it in the same platform.
[0:54] And finally, if you're writing a lot of stuff, stuff that you would say is predictable documentation, whatever, there is integrated AI.
[1:01] So, you can head over to Squarespace, there's a 14-day free trial, so you can make your website, and when you're ready to take that website and launch it,
[1:08] I have a link down below in the description to save 10% off your first purchase of a website or a domain.
[1:14] Starting off with, like, the obvious simulation approach, I'm gonna have a cylinder.
[1:18] That cylinder can be a really high resolution, and this will represent our water.
[1:23] So, I'm gonna fill this up with fluid.
[1:25] But, if I do that, it's just gonna fall forever, so I'm also gonna add a collider.
[1:29] I'm gonna duplicate this, get rid of the top, so it's a open container, and then the thickness modifier is called the solidify modifier, so something like that.
[1:38] Maybe we should make the container a bit taller so we don't get any spillover.
[1:41] To get this to behave like a fluid, run the quick liquid command, it just does a whole bunch of things for you.
[1:47] If I click play, it just falls to the ether, because it doesn't know to collide with our collider.
[1:51] So, take the collider, and then for physics, I'm gonna say it's a fluid, but not a normal fluid, a effector, which is a collision effector.
[1:59] Hit play, and it still, unfortunately, goes through, and that's because I guess I didn't make this thick enough.
[2:04] Whatever.
[2:05] Take the surface thickness, and bring it up to something above zero, I'll do 0.1.
[2:09] And just like that, our water stays stationary, because there's nothing to go through.
[2:13] But, because there's nothing to go through, there's no interest, right?
[2:16] Just to show that this does work, I'm gonna add a force, that's gonna be a turbulence.
[2:21] This turbulence is just gonna say, kinda mess it up a little.
[2:24] Make the strength like 20, and now we got the thing.
[2:27] Heh, let's make it way softer.
[2:29] Okay, so this is kinda the basis for our boiling water, and we need to increase the detail and add certain things to it.
[2:36] For the domain, which is kinda the fluid object, and this tells us where it is and isn't simulating.
[2:41] I'm just gonna kinda constrain this to what we do care about, cause there's no reason to waste compute on areas that we do not care about.
[2:48] And then additionally, for the fluid, I'm gonna take its resolution, and double it.
[2:52] Which means it'll be 8 times slower, because it's times 2, in 3 dimensions.
[2:56] Finally, I do not want meshing, at least not yet, because I just wanna see how my particles behave.
[3:02] They're doing a thing, but if you think about how water boils, it creates bubbles on the bottom, which then rise up to the surface.
[3:09] So there is no kind of turbulence force, it doesn't exist.
[3:12] I need a different way to move these particles.
[3:14] Let's make a very basic bubble system.
[3:16] I'm gonna create a plane, and this is gonna be a very fast geonode setup.
[3:21] It's going to basically spawn a bunch of points that will rise up and create bubbles, and then loop back to the bottom.
[3:27] First of all, distribute points on faces, so we have some points to work with.
[3:30] They then need to move upwards, so set position, buy some z-coordinate that is gonna be changing over time.
[3:37] Let's do a combine xyz, so I can isolate the z-component.
[3:41] And for that, I'm gonna use a time node connected to the seconds, and now this rises over time.
[3:47] Great. Not only will I use this time component, but I will add a random offset, so that they all kinda start at different positions.
[3:54] That's great, but now they kinda go up forever, so I need them to loop back around, maybe to like a 0 to 1 interval.
[4:01] So if you go up here, just kinda loop back to the beginning and repeat.
[4:04] This is done through using something like a fraction, which gets rid of the integer component.
[4:10] And now we have an infinite bubble system.
[4:12] Yay. It needs to go a bit higher so that it reaches the top of this.
[4:16] I'm just gonna multiply this by something a bit bigger than 1.
[4:19] These need to spawn bubbles.
[4:20] I will instance on every single one of these a very sparse collider, so maybe a icosphere of level 2,
[4:27] a smaller version of this, and maybe a bit of randomization, so not every bubble is the same size.
[4:33] So there we go.
[4:34] Finally, to have this kind of treat as a collider, cause instances don't like push fluid or whatever.
[4:40] I'm gonna take this, and then I'm going to realize these instances.
[4:44] So now this is actual geometry data.
[4:45] This is also going to be a fluid, not a flowing fluid, but a effector.
[4:51] That is a collision effector.
[4:52] And now if we look at this, there is no more turbulent force, so these particles that are moving are exclusively because of these bubbles that are coming up.
[5:00] This isn't that accurate, mostly because of the resolution, but also because these are moving so fast.
[5:06] Every single frame that moves so much that it doesn't have time to calculate how much fluid is pushed upwards.
[5:11] A few things we can do.
[5:12] I'm gonna take the frame rate, bring it up to 30, and then for our bubble object in the physics,
[5:17] I'm gonna take the sub steps saying, how much are you going to divide a frame, and let's bump it up to 2,
[5:23] which is actually plenty for something like this.
[5:25] And boom, the fluid just kind of shoots up.
[5:28] And if it's like too intense, take our bubble object and take the radius of these bubbles,
[5:33] how much fluid do they offset, and by making it smaller, it should work.
[5:37] Okay, we have a very basic system.
[5:39] Final trick is in our fluid.
[5:41] It's using flip fluids, which is just an algorithm for moving particles,
[5:45] but these particles can have like more things going on.
[5:48] Right now we don't have any spray that comes off, we don't have any foam, we don't have any bubbles.
[5:52] This will create many more kinds of particles.
[5:55] Like, I don't know if you can tell, but there's particles that are kind of rising from the bottom,
[5:59] and it just kind of looks more interesting.
[6:01] And now that we have our setup, you take the resolution,
[6:03] and unfortunately when you double this, it's gonna get so slow.
[6:06] It's horrible, but it's also so great.
[6:08] See, like this is taking forever, forever.
[6:11] But if we're confident in our setup, which I'm not, but let's say we are confident,
[6:15] I can do a hundred frames of simulation, where for this, I can take the cache or the baking,
[6:22] and say, don't do it as I play, but we're actually gonna bake, which is what this all means.
[6:26] Additionally, I only want to go for a hundred frames, because this is a final result.
[6:30] We do in fact want the meshing.
[6:32] I'm gonna hit bake, and I'll see you in five years when this is done.
[6:36] This is why I don't like the simulation approach.
[6:38] Okay, and just like that, we have our simulation, which is not only the mesh.
[6:42] That again, I don't think it's violent enough,
[6:43] which is why I'm not loving this needing to resimulate every time.
[6:46] But we not only get that, we also get our particles that we can do stuff with.
[6:51] If we take a closer look at our fluid, you can see there's these four particle systems
[6:55] that correspond to spray foam bubbles and then the main liquid particles.
[6:59] But how do we access this particle information and do stuff with it?
[7:02] Very simply, I'm gonna add a object that's gonna be a proxy object,
[7:07] and I'm gonna compress this down to a single vertex, so M at center.
[7:11] So now there is a single vertex.
[7:13] The way you access the particles, and it's a little weird, is in the modifiers.
[7:17] Gonna look for particle instance.
[7:19] This will let me take a object.
[7:21] Specifically, I'm gonna take the liquid domain.
[7:24] I can extract any particle system that I care about.
[7:27] So here is the bubble system.
[7:29] You can see they're kind of rising to the surface.
[7:31] That makes sense.
[7:32] We also have the foam system that rests on the surface,
[7:35] because that's where you get that like white water.
[7:37] We got our liquid, which is the whole thing, and we get spray,
[7:39] which is anything that kind of shoots outwards.
[7:42] What you end up doing is having four objects, one for each particle system.
[7:45] Kinda silly, but this one will be our spray.
[7:48] Let's make just two copies.
[7:50] This one can be our bubbles.
[7:51] This one can be our foam, making sure to update what this looks at.
[7:56] And with these, I'm gonna put them in a collection.
[7:58] So new collection, I'll call it particles.
[8:01] And I'm not actually gonna look at all of this like particle nonsense inside of here.
[8:05] I'm gonna bring them into one bigger geometry node situation.
[8:08] Finally, let's make a object that will put everything together.
[8:12] So I'll call this everything.
[8:13] Object info.
[8:15] First thing is I want my fluid, which is my liquid domain.
[8:18] We get the mesh here.
[8:19] Make three different copies.
[8:21] Each one is gonna be for its own particle system.
[8:23] This one can be bubbles.
[8:24] This one can be spray, and this one can be foam.
[8:28] Join these bad boys together and view it.
[8:30] And you can see we have all kinds of particles to do stuff with.
[8:33] I can instance a tiny little sphere treated as a bubble for everything,
[8:38] whether it be foam, the bubbles, whatever.
[8:39] Instance on these points, which are really vertices, but that's fine.
[8:43] A tiny, tiny, tiny little icosphere, so that it doesn't take much computation.
[8:47] This is gonna have a much, much tinier radius, and I'll also use a random value,
[8:51] so they're not all the same and even tinier.
[8:54] And then finally, I'm gonna join them together with the liquid.
[8:57] And the rest of this is really just kind of making materials.
[9:01] So we're gonna have a water material.
[9:03] We're gonna have a bubble material.
[9:05] By the way, all project files are gonna be on my website,
[9:07] both for this version and the GeoNodes version,
[9:10] which is what I'm more excited about.
[9:11] This is gonna get the water material,
[9:14] and this is going to get the bubble material.
[9:17] Here, I've done a basic HDRI lighting setup.
[9:20] Doesn't really matter.
[9:20] What does matter is for the water,
[9:22] the fastest way to make it is you bring up the transmission.
[9:25] That means it's see-through and bring down the roughness,
[9:28] not to zero, but something like basically zero.
[9:30] This is what makes a shiny, make it fully white.
[9:34] I'm also gonna show my container,
[9:36] which can have its own basic metallic material,
[9:38] so nothing too fancy.
[9:40] And then for the bubble material, I don't know.
[9:42] We could do anything.
[9:43] So you can see if I make this red, you can see these like little bubbles.
[9:46] I guess they should also be transmissive in a way,
[9:49] but maybe also thin film.
[9:50] I'm not sure.
[9:51] I'm gonna make them transmissive, lower roughness.
[9:53] I know one thing is that bubbles have a very low IOR.
[9:57] IOR is index of refraction.
[9:59] It's how much light bends.
[10:00] It's very, very close to one, so even like 1.05,
[10:04] whereas water has a very well-known index of refraction,
[10:07] which is 1.33.
[10:08] And if you take a look at this with and without bubbles,
[10:11] they definitely add something,
[10:13] but they are creating these kind of black areas,
[10:16] and the reason for this is there's so much transmission
[10:18] that the light beam needs to go through many bubbles in ray tracing.
[10:23] We can correct for this, but most of them come from the foam,
[10:27] I believe is the problem.
[10:28] So maybe this one kind of goes through its own particle situation over here.
[10:32] I'm just gonna turn this into a node group
[10:34] that basically takes a particle system and creates bubbles,
[10:37] make a copy of this, put this inside of here,
[10:39] and then this one is gonna get its very own material
[10:42] that I will call foam.
[10:44] This can be like a very diffuse thing,
[10:46] so it doesn't suffer from the light ray, whatever.
[10:48] Foam, join it in, and now you can see we can control the foam
[10:51] that is on the surface, which in isolation,
[10:54] it's very cool to look at how this, you know,
[10:56] does the thing and outlines the bubbles.
[10:58] A final kind of trick of the trade when it comes to water
[11:01] is you can get extra detail for free using normal mapping.
[11:05] Nothing too fancy.
[11:06] I'm gonna use a noise texture.
[11:07] That noise texture is gonna be the height of a bump node.
[11:11] So if I view this, you can see we have the normals,
[11:13] but it's not really affecting it.
[11:15] Take the distance, which is saying how high
[11:17] off of the surface does it affect and bring it up.
[11:19] And now I think you could see the difference.
[11:21] I'm gonna bring up the scale.
[11:22] So this should be subtle, but also distorted,
[11:25] I think is what looks best.
[11:26] This is what makes it look swirly.
[11:28] And if I connect this to the normal and view it,
[11:31] this is the before and this is the after.
[11:33] It just adds a stupid amount of detail kind of for free.
[11:36] And that is the simulation method,
[11:38] which in theory looks better,
[11:40] but it takes way longer to make.
[11:42] We have been going so long that I actually took a day in between
[11:45] to record this part.
[11:46] So it's a long tutorial, but as promised,
[11:48] I wanted to show a second method for making boiling water,
[11:51] which you could make look nearly as good.
[11:53] And in some cases, you might think it looks better.
[11:55] It is real time.
[11:56] You can control it.
[11:57] You don't need a hit simulate and then wait forever and hope
[11:59] that it looks good.
[12:00] It's fully geometry nodes and it goes over some cool concepts.
[12:03] I'm gonna do something a bit strange,
[12:05] which is not starting with a cylinder.
[12:07] In fact, I'm gonna start with a circle using a mesh circle mode.
[12:11] We'll make this like 200 vertices and fill it with a end gun.
[12:15] A lot of what I'm about to do is using custom nodes from my free,
[12:19] again, free pack that you can get at CGMatter.com.
[12:22] There's instructions to do it.
[12:23] You don't need to pay.
[12:24] You don't need to sign up.
[12:25] It just lets me make these tutorials faster.
[12:27] Now that I got that out of the way,
[12:29] you can see we have the circle that doesn't really have much geometry
[12:32] even if I made a triangles.
[12:33] So I'm going to use my grid fill 2d node,
[12:36] which keeps the shape but adds resolution to it
[12:39] almost like you subdivided it nicely.
[12:41] And now the name of the game is making a height map,
[12:44] basically a certain kind of disturbance
[12:46] that happens to look like bubbles coming to the surface at various frequencies.
[12:50] And this isn't like something I need to vaguely compute with noise or whatever.
[12:55] If you know what a Voronoi texture is,
[12:57] which is a node we use all the time,
[12:59] this is in a sense adding a bunch of spheres.
[13:02] Let me explain what this node does.
[13:04] If I take a look at what it's making,
[13:06] you can tell there's like almost these like cells
[13:08] that create that classic Voronoi pattern.
[13:10] But inside every single one of these cells,
[13:12] there will be this black dot and they represent the center
[13:16] of some n dimensional sphere.
[13:19] What a mouthful.
[13:19] Let me show you.
[13:20] So if I take this down to two dimensions,
[13:22] now you can see really every single cell has a dot.
[13:25] And if I look at our like viewing options,
[13:27] I can look at the n sphere radius,
[13:29] which is saying the sphere that is contained in each chart.
[13:33] So for example, there's one here,
[13:35] just kind of the biggest sphere that you can pack in here.
[13:37] They have a certain radius and then a certain center point.
[13:41] If I treat this three dimensional texture as bubbles coming to the surface,
[13:45] then we've done it.
[13:46] I'm going to throw this through a map range that will let me take
[13:49] whatever this is mapped to and hopefully turn it into something more useful.
[13:53] Notice I can't just take one and zero and flip it and then kind of play
[13:56] with the numbers like it does give me these circles,
[13:59] but it doesn't account for how much I can pack in the way to do it properly.
[14:03] Is you take another Voronoi texture very importantly,
[14:05] you're going to keep the same settings here.
[14:07] And the only thing you're going to change is you're going to access the radius.
[14:10] We're going to go from zero all the way to the radius zero
[14:14] until you go as far out as you can and turn that into one to zero,
[14:17] which ends up looking something like this.
[14:20] They're tinier spheres, but they're perfectly packed in.
[14:22] I can bump up the resolution so I can actually see what's going on here.
[14:26] And because this Voronoi texture is 3D, I can hook up a position.
[14:30] Remember, whatever you do here, you have to do to both.
[14:32] And I'm going to offset this three dimensional texture on the Z axis,
[14:36] which you can think of as little bubbles or little spheres rising up to the surface.
[14:40] So if you check this out, it's looking like these circles are getting bigger and smaller.
[14:45] But really it's these spheres that are going through a cross section in a sense.
[14:48] I want this to be animated.
[14:50] So I'm going to combine XYZ so I can access the Z component and use a time node.
[14:56] I'll use my CG matter time node, which lets me quickly multiply it by a number.
[15:00] So if this feels like it's going too fast or too slow, you're going to change the speed.
[15:04] Bubbles in a boiling pot are quite chaotic.
[15:07] So I'm going to go 1.5.
[15:08] Then for the scale, whatever I do with this, I need to make sure I do it on both
[15:13] because they need to correspond to each other.
[15:15] And this lets you choose kind of the frequency of the bubbles in a sense.
[15:18] Here we have really big bubbles.
[15:19] If I bring this up to 10, we can have really tiny bubbles and we're going to add layers of this together.
[15:24] Really, the only things I want to control if I turn this into a node group
[15:28] is maybe the animation speed, the scale, and that's about it, really.
[15:32] So I'm going to turn this into a node group.
[15:35] I'll call it bubbles, which in Spanish is verbujas.
[15:38] So you not only learn English blender, you learn blender in Español.
[15:42] And now I'm going to make a second copy of this.
[15:44] I'm going to add or you can take the maximum depending if you want to allow bubbles to be on top of each other.
[15:50] And for this one, let's go for a lower frequency at maybe a higher speed.
[15:54] And now you can see we have the combination of big and tinier bubbles.
[15:58] And then maybe I want to make one more layer because why not?
[16:00] This one is going to be the high frequency layer.
[16:03] So all this together creates something that will look quite good at the end of the day.
[16:07] Now let's do our offsetting.
[16:09] So I'm going to use a height offset node.
[16:12] Really, all it's doing is saying move the mesh on the z-axis by some value.
[16:16] But I do this so much that I turned it into a node.
[16:18] I'm going to offset by this custom height, which you can see is showing the bubbles,
[16:22] but they're way too big.
[16:23] Take it and multiply it by like 0.1.
[16:26] When we do this, they are contained.
[16:28] But you can see the distribution of them is kind of this bell curve.
[16:31] And really what it's going to be is it's going to be something kind of linear.
[16:34] Whereas I want their profile.
[16:36] So like here, for example, I have this like sharp mountain.
[16:39] I want it to kind of end up as the cap of a sphere, kind of a hemisphere.
[16:42] You can do the math for this, which ends up being some Pythagorean theorem, blah, blah, blah.
[16:47] But because we know each of these goes to 0 to 1, I can just open up a node group and right after the map range,
[16:53] I'm just going to add a float curve, which will let me draw this out.
[16:57] So let's do something like that.
[16:58] You can see they just kind of became more spherical.
[17:00] If I do the opposite, they'll look like a pin points.
[17:03] I'm then going to bring down the overall height by a lot, run a shade smooth.
[17:08] In fact, I can take certain layers and make them stronger than others.
[17:11] For example, if I like this low frequency layer, I can, well, I guess I can just like multiply it, right?
[17:17] Before it even goes into the chain.
[17:18] So I can like multiply by 2 or 4, depending on how crazy you want this to be.
[17:23] And actually one more thing, if you do not like this layering, which you can't tell in real time,
[17:27] but if you don't like it, change these additions into maximums so it only keeps the bigger of the entries and then they don't overlap.
[17:34] Anyways, I need to extract the border.
[17:36] So I'm going to take my border to curve node.
[17:40] What this does is it extracts the boundary, which in this case, it's very simple.
[17:43] It's the perimeter of that circle that we happen to distort.
[17:46] And I want to take this and extrude it downwards.
[17:49] This is being stored as a curve.
[17:51] So I'm going to convert it into a mesh.
[17:53] Meshes, not curves, can be extruded as edges.
[17:57] And now we, you know, have control over this dynamically.
[18:00] Specifically, I'm going to extrude it by zero, which means you can't see it anymore, but it is there.
[18:06] It's like I added geometry and then did not move it.
[18:09] I can move it in its very own step where I set position to this top selection, where I move it down the Z axis.
[18:15] The reason I'm doing this instead of like offsetting on a negative Z is I want the bottom of this to be kind of a constant height.
[18:23] The position should not only like go down by a certain amount, but it should flatten.
[18:28] A nice way to do this is by like hard coding it in.
[18:31] So I'm going to take the position I'm going to add or I guess subtract some kind of height.
[18:35] And then I want to nullify the Z component of this position before we even offset it.
[18:41] This can be done with say with me multiply with multiply.
[18:44] So I'm going to take one, one, one and then null out the Z component.
[18:48] And now, no matter what this does, it remains, you know, where it's supposed to.
[18:51] But final thing is we need to take this bottom perimeter and join it together.
[18:55] Extrude the very same selection.
[18:57] So what I'm doing right now is only affecting the bottom and I kind of wanted to pinch inwards, which it does want to do.
[19:03] But I'm going to extrude by zero just like last time.
[19:05] And then I'm going to run a scale elements on this selection by zero for the edges.
[19:11] And that will seal this up nicely kind of extruded that didn't move.
[19:15] And I said, compress it all to a central point.
[19:17] So you're going to see the shading looks super weird.
[19:19] So you can just do a set shade smooth, turn it onto flat so we can see what we're doing.
[19:24] This whole chain on this side, I can compress to its very own frame.
[19:28] I'm going frames, not node groups recently.
[19:30] I think it's better for reading it the first time you look at it.
[19:33] Maybe either way, cgmatter.com get the file.
[19:35] What do we call it?
[19:36] Maybe I'll call it the boundary.
[19:38] And then I take this.
[19:39] I take that.
[19:40] I join it together.
[19:41] And now we have this like three dimensional thing that we put the pot over.
[19:46] I do want to make sure that the top is shade smooth.
[19:49] So I can shade smooth the top branch and not the bottom branch.
[19:53] And then we get the best of both worlds before we like apply a material and render this.
[19:58] I got to make sure it's a single water type mesh.
[20:00] So it kind of works as a volume.
[20:01] A good way to check that is you want to look at the face orientation.
[20:05] And oh, no, our faces are flipped.
[20:07] Good for us.
[20:08] There is a node that fixes it.
[20:09] So do a flip faces.
[20:11] And then we want to make sure that this boundary where we're joining them is all merged together.
[20:16] So finally run a merge by distance.
[20:19] And then let's make a super basic material for this, which is going to be the same as before.
[20:23] As we already know, that should be fully transmissive, lower roughness and already look at how much faster it's computing.
[20:29] Make sure index of refraction is 1.33.
[20:32] It's looking a bit weird right now because there's nothing to contain it.
[20:36] So make a cylinder and just kind of model it to be what it needs to be.
[20:39] Metallic material of some kind.
[20:41] And there you go.
[20:42] You have your pot of boiling water.
[20:44] One thing I would recommend though is if you're getting any stretching for the height offset, the map that we're using,
[20:49] just throw in a blur attribute at the very end here.
[20:52] And you could see we soften this up super nicely.
[20:54] Final thing that'll put this all together.
[20:56] I'm going to bring down the resolution just so I can experiment quickly is there are bubbles on the surface of the water,
[21:01] but the water itself should be perturbed almost like there's miniature waves like a tiny chaotic ocean.
[21:06] Damn, I spit bars.
[21:07] Okay, all I would have to do for that is I would add a contribution that is some noise texture.
[21:13] So something like this very importantly, I turn off normalize so it starts at zero and you can either go up or down instead of averaging upwards.
[21:21] This is going to have some contribution I can control lower scale, higher distortion.
[21:26] I think distortion is everything really.
[21:27] And then for the coordinate system, because this needs to evolve over time,
[21:31] we're going to use the same trick where I take a position and all noise textures by default are three dimensional.
[21:36] And I can use that to kind of add this like simmering.
[21:39] I'm going to use my combined XYZ and use the time node just like we did before in the Z component.
[21:44] Definitely need to bring down the overall strength of this effect.
[21:47] And that is everything I use to get the final effect really.
[21:50] When you render this, it looks something like this once you add some ground and basic lighting.
[21:54] In a way, this looks more like boiling water than the simulation, which looks far cooler.
[21:59] Just so you know, there is a real time option.
[22:01] Okay, very long tutorial.
[22:02] I just want to say again, again, again, go to my website CDMatter.com.
[22:06] Fucking do it.
[22:07] Project files.
[22:08] Other reasons.
[22:09] Okay, hopefully you learned everything there's to know about boiling water.



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
