---
title: Top Tip Tuesday - Liquid Fill
source: YouTube
url: https://www.youtube.com/watch?v=vglrHSL-uc4
author: INSYDIUM LTD
ingested: 2026-08-11
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/top-tip-tuesday---liquid-fill/
frame_count: 0
frame_status: pending-selection
---

# Top Tip Tuesday - Liquid Fill

**Source:** [YouTube](https://www.youtube.com/watch?v=vglrHSL-uc4)
**Author:** INSYDIUM LTD
**Duration:** 19m57s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py top-tip-tuesday---liquid-fill <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi, Bob from Insidium here. In today's top tip, I'm going to show you how we can use the liquid fill tools in Nexus for Blender to quickly set up these fluid simulations.
[0:11] We can add foam to these simulations to get this type of look set up really quickly and easily.
[0:18] You can go one step further and here is an example of a render where we have made this quite abstract look using a fluid sim, using some foam which has filled this Suzan model.
[0:30] We'll leave the scene file for this render in the description of the video as well.
[0:35] So let's start a new scene in Blender and we'll begin.
[0:39] Okay, let's go to our Nexus tools then and look, we have our Nexus liquid fill which offers you basically a shortcut to bring in all of the tools that are required to do a liquid fill simulation.
[0:53] So look, in our viewport, we've got our liquid domain here. Let's just switch off that floor.
[0:59] And in our end panel, it has brought in the Nexus Gravity and we have this liquid fill folder.
[1:06] Inside that, we have got an emitter, we've got a fluid solver, we've got a measure which is deactivated by default.
[1:13] We've got a particle group which is called foam and we have a foam solver here which is also switched off.
[1:20] So this is designed to give you, if we hit play, without doing anything, we've got a fluid tank.
[1:26] Okay, and that's looking good. Let's just bring in a, what could we do?
[1:31] Let's bring in a wind modifier. There we go.
[1:35] And we'll put this in Von Karman mode just to get a bit of movement in our scene, maybe 2.5.
[1:40] But let's put loads of variation.
[1:43] And then what I'm going to do is just increase this friction velocity under the turbulent settings,
[1:47] which will just mean that that turbulent force will be quite strong.
[1:52] Hit play and now we have got this wind affecting our particles.
[1:57] So there we've got our fluid sim.
[1:59] Cool. So let's have a look at how this is set up.
[2:03] You can do all of this manually.
[2:05] This is nothing that you can't do by bringing in these various different objects individually,
[2:11] which is kind of the way I work just because I'm used to doing it that way.
[2:14] But the Nexus Liquid Fill gives you this shortcut.
[2:17] What elements are there?
[2:18] Well, obviously there is an emitter which is giving us the particles.
[2:21] Let's have a look at those settings.
[2:24] So the emitter is automatically in object shape mode,
[2:27] and it's using the Nexus Fluid domain that was brought in as the object in which it's emitting the particles.
[2:35] It's set to volume, obviously.
[2:37] And you can see that the emission type is set to Liquid Fill.
[2:41] It needs a fluid solver to reference.
[2:46] So look, our NX Fluids, that's our fluid solver here.
[2:49] And I'll show you why that's important in a minute.
[2:52] Then we have a resolution setting, and we have a fill level setting.
[2:57] So let's just go back to the first frame.
[2:59] Let's put show fill level, and this shows you how far up on the volume it's going to fill with our fluid particles.
[3:08] So if we hit play, you'll see that's where it's filled from.
[3:12] All right, let's just make that wind invisible, and we'll make the gravity invisible as well.
[3:18] All right, so it is linked to our emitter to our fluid solver here.
[3:24] So look, let's go to our Nexus Fluids, and we're going to go to display,
[3:31] and I'm going to show you the back drawing of the voxel grid.
[3:36] Let's put it on back only.
[3:38] So there is our 2D representation of our 3D voxel grid,
[3:42] and this is showing you the resolution of the simulation.
[3:45] The smaller these voxels are, the higher detail, higher realism,
[3:50] but the more VRAM and the longer it'll take to simulate, and that's the resolution of the sim.
[3:55] Let's just go back to our emitter.
[3:57] So look, if I change my resolution in the emitter to say 70,
[4:02] you can see, look, the voxel size is hugely reduced, which means it's more accurate,
[4:08] but it's going to take longer to simulate.
[4:10] But it's not just changed the resolution of our grid.
[4:14] When you have these voxel-based liquid solvers,
[4:18] it's very important to have an appropriate number of particles per voxel
[4:23] for the fluid calculation to be accurate.
[4:27] And so now that we have got far more voxels,
[4:31] with this amount of voxel detail, we need more particles,
[4:36] and this all happens automatically when we have our emitter in liquid fill mode.
[4:42] When we adjust the resolution, it changes the resolution of the voxel grid,
[4:46] but it also changes how many particles are within that particle cloud,
[4:51] so we have got the appropriate amount per voxel.
[4:54] So now we have got resolution of 70, much more high detailed sim.
[4:59] Obviously it's taken longer to simulate because it is way more voxels and way more particles.
[5:05] But it's all done automatically for you.
[5:08] So you've always got the perfect number of particles for the resolution of your grid.
[5:13] Cool.
[5:14] And I would say that's probably the most important reason for using this feature,
[5:21] is that it does that automatically for you,
[5:23] so you've always got that appropriate particle count.
[5:25] If the particle count isn't an appropriate number, your fluids will collapse,
[5:30] and it won't look very good.
[5:31] Let's put that back down to 50 and hit play.
[5:36] Okay, so that is the basics.
[5:38] But we don't have to just emit particles from within this domain.
[5:44] Let's say we wanted to emit them from a different object.
[5:47] Well, we can do that.
[5:48] Let's go and bring in, let's just bring in a UV sphere,
[5:53] and let's say we want to contain and have a fluid simulation within our sphere.
[5:58] How might we do that?
[6:00] Well, we'll just make that sphere invisible.
[6:03] Let's go back to our emitter.
[6:06] So we can leave all of these settings as they are.
[6:09] We're referencing this fluid solver.
[6:11] We've got it in flip mode.
[6:13] We're doing a resolution of 50, full of 30%.
[6:16] That's fine. We'll leave that as is.
[6:17] But we don't want to emit the particles within this domain.
[6:22] We want to do it inside the sphere.
[6:23] All we need to do, look, is just get rid of that, put in our sphere,
[6:28] and now those particles.
[6:30] Let's just go forward one frame, and now the sphere has been filled up by 30%.
[6:36] Now, the issue here is that there's no collisions going on,
[6:40] so those fluid particles are just going to drop to the floor and splash,
[6:43] which looks cool, but it might not be what you want.
[6:45] You may want to contain them within the sphere.
[6:48] So how we do that is we need to set up a collision.
[6:52] So let's bring in a Nexus Collider.
[6:57] There we go.
[6:58] And in this, we're going to select the sphere.
[7:01] We want it to use the inside normals,
[7:04] because we want to trap the fluid inside the sphere.
[7:06] Let's take off the bounce and the friction,
[7:09] and now you'll see, yes, now we have got our fluid fill filling that sphere
[7:15] and splashing around.
[7:17] Perfect. That's what we want.
[7:19] Let's go back to our emitter.
[7:22] So one other thing that I can show you,
[7:24] we are referencing our Nexus fluids,
[7:26] and we have the solver set to flip mode.
[7:29] Because it's referencing this, if we change this to A-pick and hit play,
[7:34] now it's using the A-pick solver,
[7:36] and we can confirm that if we go back to our Nexus fluids,
[7:40] it has automatically been set to A-pick,
[7:44] because we made that change. Fantastic.
[7:47] All right.
[7:49] So now that we are in this emitter,
[7:51] we are filling it by 30%.
[7:54] Let's put our resolution up to maybe 75.
[7:59] We've got something like this. Cool.
[8:03] So, a couple more things to show you.
[8:06] By default, we have our mesher switched off,
[8:10] and that's because it's a good idea to leave the mesher switched off,
[8:13] so you're not having to calculate that mesh
[8:16] whilst you're setting up your particle sim.
[8:18] But at some point, you're going to want to mesh these particles to render the fluid.
[8:22] So, let's make our emitter invisible,
[8:25] so we don't see those fluid particles anymore.
[8:28] And let's activate our mesh.
[8:31] Now, this, if we go to our mesher,
[8:33] this, because we used the Nexus liquid fill,
[8:36] which brings all this in automatically, is already all linked up.
[8:39] Look, the mesher has an emitter layer.
[8:42] It's referencing our liquid emitter,
[8:44] and we're getting this mesh in the scene.
[8:47] But actually, what we need to do is,
[8:50] it's automatically judged that the polygon size of 0.027
[8:54] is required to get a detailed enough mesh.
[8:57] But if we come in a bit, you'll see that there's too many kind of holes in our liquid.
[9:03] So, what we need to do is increase this scale up to say,
[9:07] let's start at 300.
[9:09] Yes, and now we have managed to kind of wrap each particle within that mesh,
[9:14] and that is looking better.
[9:16] And then we can add some smoothing to this.
[9:19] So, let's add a smoothing layer.
[9:22] We'll take it off, Gorgian.
[9:24] Let's put it on mean curvature as my go-to for most liquids, full.
[9:29] And then you can adjust the iterations to get more or less detail.
[9:33] Now, you see, when I put that on 10,
[9:35] we lost the meshing of those droplets in the middle of this liquid bit,
[9:41] because that's too much smoothing.
[9:43] At this polygon size and this scale,
[9:46] we've smoothed so much that we've lost that detail.
[9:49] Let's just go to the fluids, make that invisible.
[9:53] So, let's go back to our mesh and we'll reduce that to 5.
[9:56] Yep, and you can see, look, we've got that fine detail of those droplets back in.
[10:00] Now, we've put that on 5.
[10:01] Cool.
[10:02] So, now if we hit play, now we have got our liquid meshed.
[10:08] Brilliant.
[10:09] That's looking really good.
[10:11] Okay.
[10:12] So, whilst we are working, let's just switch off the mesh.
[10:17] The final thing we're going to look at is our Nexus Foam,
[10:20] which again was brought in by default.
[10:23] So, I'm going to click on this foam.
[10:25] We're going to activate it.
[10:27] So, now this is activated.
[10:29] What I'm going to do is a couple of things to set things up.
[10:32] First of all, we need to tell the foam what type of fluid solver is going on.
[10:38] So, it's going to know how to interpret the liquid fluid data that's happening under the hood.
[10:44] So, we need to put this on A-pick.
[10:46] We chose an A-pick solve.
[10:48] So, that needs to match.
[10:50] And then, before we hit play, because we are not using just the simulation bounds,
[10:56] the cube that is our fluid domain, because we're using that sphere as our bounds.
[11:04] We're keeping the fluid in here.
[11:05] What we want to do is the simulation bounds for our foam,
[11:08] we want to select that sphere as well.
[11:11] So, it's going to kind of contain it within there.
[11:13] So, let's just deselect that.
[11:16] All right.
[11:17] So, now let's go to our liquid particles emitter and make that visible again.
[11:23] And if we start playing this, you're going to see our liquid sim.
[11:27] And this is now actually generating foam.
[11:30] But it's difficult to see that foam because they're all being drawn in the same way.
[11:37] By default, our emitter, which is generating now the liquid and the foam particles,
[11:42] in the display options, it's set to screen space fluid,
[11:46] which gives us this nice almost meshed look.
[11:48] But this isn't good for viewing our foam particles.
[11:52] So, let's change it.
[11:53] We'll put this now on points.
[11:56] So, all of the liquid particles are just going to be this stock blue color.
[12:01] Let's put the points down to one.
[12:03] But we are going to be able to see our foam particles.
[12:05] Let's have a look.
[12:06] After a few frames, we get these white and light blue particles appearing.
[12:11] Cool.
[12:12] So, let's have a look at what's happening and why this is happening.
[12:14] We'll go to our Nexus foam solver.
[12:17] So, what this does, as I said, it analyzes the fluid data.
[12:22] Those liquid particles analyzes the fluid density, their movement, the vorticity.
[12:28] All kinds of clever stuff is happening to calculate how this white water is generated
[12:34] and then how it's moved around by the fluid.
[12:37] And there are three different types of white water particles that are generated.
[12:42] There are foam particles, spray particles and bubble particles.
[12:47] And all of these have their own settings.
[12:49] So, in this tutorial, we're not going to go into a real in-depth NX foam tutorial
[12:56] because we need a full dedicated long tutorial to do that, which we will do in the future.
[13:01] So, with that in mind, what we're going to do is only concentrate in simulating one of these white water types.
[13:10] We're just going to do the surface foam and then it's easier to manage.
[13:14] So, if we come down this surface foam layer with all of the various different settings,
[13:19] we can come down to the appearance and by default, custom display is active
[13:25] and it's giving the foam particles this white color.
[13:29] So, if we hit play, you'll see that after a few frames, we start getting those white foam particles.
[13:36] All right, that's cool.
[13:38] Now, why are they only generating after a few frames?
[13:42] Look at the beginning, there's none.
[13:44] And that's because by default, we have spawn after age set to 30.
[13:49] So, that's saying that the liquid particles are not allowed to spawn foam particles
[13:55] until they are at least 30 frames old.
[13:58] And this is just to prevent, if you've got kind of a big drop tank scene,
[14:01] it's to prevent billions of particles being generated on the first frame.
[14:05] So, you can kind of delay it to the point in which you want.
[14:08] But we want them almost straight away.
[14:10] I'm going to put this down to say after four frames old,
[14:12] these liquid particles can start generating foam.
[14:15] Yeah, and then we're getting our foam particles and that's looking cool.
[14:18] All right.
[14:20] So, that is our foam particles.
[14:24] And what is happening under the hood is this.
[14:28] All of these particles, liquid and foam, are being generated by our one scene emitter.
[14:36] But can you see, remember we said that when we set up our liquid fill,
[14:41] we got this group foam set up automatically as well.
[14:45] And if we come to our foam layer here and come to the bottom,
[14:49] you'll see, look, output, output group, group foam.
[14:55] So, what that is saying is, is it's separating these particles out.
[14:59] All of the particles are coming from this same emitter,
[15:02] but the foam ones are being separated and put into group foam.
[15:06] And this means we could access this group at render time
[15:10] to render the foam particles in a different way
[15:13] than how we're going to render the liquid particles.
[15:17] But, what I'm going to do is show you a workflow
[15:21] which is going to help you separate them out a little bit more easily.
[15:26] And this is the way I choose to do it.
[15:28] I mean, both ways work, but I prefer this way.
[15:31] So, instead of using this group, in fact, look, let's just delete that group out.
[15:35] We're not going to use a group.
[15:36] Instead, we're going to use a completely separate emitter
[15:41] that we're just going to use for the foam particles.
[15:44] So, let's bring in a new emitter.
[15:46] And we'll just move that up to the original one.
[15:49] And this one, we're going to change it and call it foam.
[15:54] All right.
[15:56] And then let's go back to our Nexus Foam Solver.
[15:58] So, in our foam layer, where we came to the bottom here,
[16:03] we did have that output group being used.
[16:06] Instead, look, we can use an output emitter,
[16:09] which means it's going to use all of...
[16:12] It's going to use this new emitter to generate our foam particles.
[16:16] And we can have a separate emitter if we were simulating
[16:20] all of these three different types.
[16:22] We could have a separate emitter for each type,
[16:25] which means that we can completely...
[16:27] We can generate a different point cloud for each different foam type
[16:31] and render them totally differently.
[16:32] It means that on the bubbles, you can instance some actual bubble geometry, for example.
[16:37] So, now that we have got that, we have got our foam particles
[16:41] being generated by our foam emitter.
[16:45] So, let's just make sure that that's working.
[16:48] Let's make our liquid emitter invisible.
[16:52] So, now we can't see our liquid emitter,
[16:54] and we're now getting our foam particles.
[16:56] But, look, the foam emitter is actually emitting particles
[16:59] on top of the ones it's generating, and we don't want that.
[17:02] So, let's go to our emitter foam.
[17:03] That's because, look, by default, the birth rate is set to 1,000.
[17:06] So, it's being used to generate foam,
[17:09] but it's also generating its own particles, which we don't want.
[17:11] So, let's just put that on zero.
[17:13] And in the display, let's put that size down to 1,
[17:18] and then hit play, and now we should just get yes.
[17:21] So, now we've just got our foam particles from our independent emitter.
[17:27] Cool.
[17:29] So, the reason we've done that is, now we can generate a point cloud,
[17:34] which is just the foam particles,
[17:36] and it can ignore all of these fluid particles,
[17:39] because we're only really using them so we can mesh them.
[17:42] So, let's activate our mesher again.
[17:45] There's our mesh, and the mesh is simulating,
[17:50] and now we're getting the white water moving around on that mesh,
[17:54] and that's looking excellent.
[17:57] So, when it comes to render time, a couple of things that we need to do.
[18:01] We need to go to the emitter foam.
[18:03] Now, this is just a viewport display.
[18:05] We need to generate a point cloud to be able to render.
[18:07] So, we go to the export tab, we create point cloud.
[18:11] We can now make, look, if we twirl this down,
[18:14] we now have this point cloud,
[18:16] which is actual geometry node geometry,
[18:18] so we can make the particles invisible.
[18:21] So, now we have a point cloud being generated,
[18:24] which is geometry that can be rendered,
[18:26] and we have a mesh that's being generated, which can be rendered.
[18:31] So, if we hit play, now we have got that working.
[18:36] Cool.
[18:38] A couple of considerations.
[18:39] This point cloud, you don't need to do anything with it.
[18:42] It will render with motion blur at work
[18:44] if you're rendering with motion blur.
[18:46] If you want motion blur to work with this mesh,
[18:49] which is a dynamic point changing mesh,
[18:51] all you need to do is go to the measure.
[18:54] You need to go to the export tags,
[18:56] and you need to transfer velocity.
[18:58] That's it, and then that will render correctly with motion blur as well.
[19:03] So, there we have got our liquid surface mesh,
[19:08] and simulating, this is all still happening live.
[19:11] This isn't even cached yet, so we can make adjustments, should we wish.
[19:14] We are generating our point cloud from our foam emitter,
[19:18] and that is the basics of how you use the Nexus Liquid Field
[19:23] to set up these pretty simple fluid scenes,
[19:27] and how you generate that white water
[19:29] and get that ready for render time.
[19:32] I'll leave you an example of the more complex rendered scene
[19:37] in the description of this video,
[19:39] so you can download that and have a dig around
[19:41] to see how we rendered that shot.
[19:43] But this is that basic scene.



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
