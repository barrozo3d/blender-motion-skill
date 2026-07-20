---
title: the New Blender Fluid Simulator is AWESOME - MantaFlow Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=JYc_6fXEjw4
author: CG Geek
ingested: 2026-07-19
blender_version: "Blender 2.83 Alpha"
tags: [fluid, simulation, particles, materials, shaders, glass, rendering, cycles, hdri, compositing, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/the-new-blender-fluid-simulator-is-awesome---mantaflow-tutorial/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# the New Blender Fluid Simulator is AWESOME - MantaFlow Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=JYc_6fXEjw4)
**Author:** CG Geek
**Duration:** 19m12s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] So with the release of Blender 2.82, we now have a new fluid simulator and smoke simulator in Blender.
[0:05] And it's pretty awesome!
[0:16] And thanks to Squarespace for sponsoring this video, the easiest way to build an online website.
[0:21] So Mantaflow is what has replaced the old fluid and smoke simulator inside of Blender.
[0:26] It's been around for a little while now, it's kind of been an extended branch, but it's finally, finally been merged inside of Blender and is now the default fluid and smoke simulator.
[0:35] And that's really good news!
[0:36] I've been playing around with Mantaflow for the past few weeks now, and I've been really enjoying getting the amazing fluid simulations and results and having the extra control.
[0:45] I've also discovered that there's still some bugs that will need to be worked out in the future versions of Blender.
[0:50] I'm sure that's gonna happen though, and I've learned some workarounds to kind of smooth over these bugs.
[0:54] So that's what I'm gonna be sharing with you guys today, as we take a look at how to get some realistic fluid slash water simulations.
[1:01] So without further ado, let's get into that Mantaflow, bro!
[1:04] That Mantaflow, bro!
[1:05] That Mantaflow, bro!
[1:07] Oh, oh, get that Mantaflow, bro!
[1:09] What'd you say?
[1:10] Mantaflow!
[1:11] Woo, woo!
[1:11] And if you'd like to download my finished project file here for my Mantaflow simulation, you can do so over on my Patreon page for just $3 a month.
[1:19] You get access to this file and all of the other blend files available on the channel.
[1:23] Also for the $8 perks, you can get access to the asset pack downloads.
[1:26] So check it out, you can get some cool perks and support the channel in the process.


### Blender [1:30]
**Transcript (timestamped):**
[1:30] So over now in Blender, I'm actually using Blender 2.83 Alpha just because it's the newest and latest release,
[1:36] and I like to run the newest releases because it's always bug fixes coming into Blender.
[1:40] So you might as well, in my opinion, run the latest versions of Blender.
[1:42] I'll put the link into the description where you can download it.
[1:45] So I'm just gonna go ahead and scale this cube up a little bit by going S and 3, and then scale it down along the Z axis a little bit,
[1:50] and this will be a nice shape for our domain.
[1:52] Next up, just as before, we need to add an object to add fluid into our scene.
[1:56] So I'm just gonna drop in a UV sphere by going Shift A and adding in a UV sphere.
[2:00] If I hit Z and switch to wireframe, we can see that there.
[2:03] I'm just gonna scale it down to something much smaller and then hit G and Z to pull it up along the Z axis,
[2:08] just so we're sitting at the top of our cube there, but still inside of it.
[2:11] Here, I'm just adding a few cubes to the bottom of the domain so you guys can see how to add some fluid obstacles as well.
[2:17] So now we can head over to the physics tab here and start setting up some fluid settings.
[2:22] So for starters, let's grab those obstacles that we just added, choose fluid, and here we're gonna choose a type of a factor.
[2:28] This is just like the collision as it used to be in the old simulator.
[2:31] And here it's already set to collision.
[2:33] We don't have to change anything.
[2:35] Just go ahead and set that up as a fluid effector on all of your cubes.
[2:39] Next up, we need to tell Blender what we'll be adding the fluid into the scene, and that's gonna be a UV sphere.
[2:43] So here we're just gonna add fluid, choose a type of flow.
[2:46] Here we need to change the flow type from smoke over to liquid,
[2:49] and then choose the flow behavior to be in flow.
[2:52] As you can see, it says here it will add fluid to the simulation,
[2:55] and this is going to constantly add fluid to our scene for the whole duration of our timeline.
[3:00] Now, if you don't want it to be adding fluid the entire time,
[3:03] what you can do is like what I did, and jump to something like frame 40 here,
[3:07] hit a keyframe on the use in flow.
[3:09] So hovering your mouse over and hitting I will add a keyframe,
[3:12] then you can just jump to the next frame and hit I again to add a new keyframe,
[3:15] but this time uncheck it when you hit I.
[3:18] So it is now turning off the inflow at frame 40,
[3:21] and then we don't have any more fluid being added to our scene after that point.
[3:24] So now it's time for our fluid domain settings.


### Fluid Domain [3:25]
**Transcript (timestamped):**
[3:26] Grab the cube and under the fluid physics, choose fluid and choose a type of domain.
[3:31] And as you can see by default is set to gas, which is going to technically be smoke.
[3:36] We don't want that. We want to change that over to liquid for this tutorial.
[3:39] So before we get into the domain settings,
[3:41] I want to tell you about some of the really cool features that Maniflow offers.
[3:44] One of them being that you can resume bakes after you've already baked it.
[3:48] This is really cool because if you baked your simulation, you really like it,
[3:52] but you wish it was just a little longer.
[3:53] You don't have to rebake everything again like you would in the previous versions of Blender with Maniflow.
[3:58] You can just resume your bake and continue from that point.
[4:01] Really cool. Also, you can bake the fluid, the mesh and the particles all in different sections.
[4:09] This also allows for a little bit quicker baking and more control.
[4:12] If you want to tweak the particles without tweaking your fluid mesh,
[4:16] you can go ahead and just rebake the particles.
[4:18] And another thing that I was really excited to find is that Maniflow is seemingly multi-threaded.
[4:22] And I believe this is a pretty new feature,
[4:24] but that means that it will take advantage of multiple CPU cores to speed up your baking process,
[4:29] which I was really excited to find.
[4:31] As a lot of you guys know, the previous fluid simulator was not multi-threaded at all.
[4:35] With Maniflow, I can even use all 64 cores on the 3990X threadripper processor back there to accelerate my bakes.
[4:43] Now, it's still not crazy fast and it only seemed to utilize the cores to about 20 to 30%.
[4:48] But the fact that it's using all of the cores means that higher core processors are going to process your simulations faster.
[4:54] I don't know if this might even get faster with the future builds,
[4:57] but it's really good news to see that it's multi-threaded and that a higher core processor will make your bakes happen faster.
[5:03] So, let's get into some of these cool settings inside of the domain.
[5:06] Starting off with the fluid resolution.
[5:08] We'll leave this at 64 for now, but once we want to do our final bake,
[5:11] we'll crank the resolution up a little bit higher.
[5:13] Then we have the time scale.
[5:14] Now, I found that the time scale was a bit fast for my liking, at least at 24 FPS.
[5:19] It seemed like the fluid was just moving ridiculously fast.
[5:23] Now, maybe that's realistic because fluid is pretty fast, I guess.
[5:26] But I found it looked better to my eye, changing this down to about a 0.5.
[5:29] And I recommend you do it too because you can always speed up your footage later on,
[5:33] but you can't slow down a fluid simulation.
[5:35] So, go ahead and change it to 0.5 and you might like it better and you can always speed it up later.
[5:39] And then with the time steps here, you might want to increase the minimum amount
[5:43] because I found I got a little bit better results when I cranked this up to at least a 2
[5:47] as it gave it a little bit more information to calculate between frames
[5:50] and fix some of the issues I was getting with some faster moving fluid.
[5:53] So, I'm going to go ahead and set that to 2.
[5:55] Down here, you can see we have border collisions now.
[5:57] This will allow the fluid to collide or not collide with parts of the domain,
[6:01] which could be kind of cool for some uses.
[6:02] Then in the liquid settings here, we have some options for fine tuning your simulation.
[6:06] I actually didn't really change much of these because I found the defaults here to be pretty good.
[6:09] But you can add like more or less particles by increasing the particle maximum
[6:13] and there's also some other fine tuning tweaking that you guys might want to get into,
[6:16] but don't really have to touch for some basic fluid simulations.
[6:19] And now what we can do before we go into the particles or the mesh
[6:23] is we can see what our fluid simulation is looking like if we scroll all the way down.
[6:27] So, under the cache setting here, we can get a real-time playback
[6:29] of what the fluid simulation is looking like in our viewport
[6:32] if we change it from module to replay.
[6:35] Here, we can go ahead and play it right inside of our viewport then
[6:38] and get a live playback of what the fluid simulation is going to look like.
[6:41] As you can see, it's happening kind of slow,
[6:43] but it's cool to kind of see how the fluid will be interacting with our scene.
[6:46] You can see that the collisions are of course working here.
[6:49] Great to just save you a little bit of time and see if the simulation is going to look the way you want.
[6:53] And actually, by doing this, I can see that there's not quite as much fluid in the scene as I might like.
[6:57] So, what I can do here is just grab our fluid emitter here and scale it up a bit larger.
[7:02] This will of course add more fluid to our scene now
[7:04] and to get it to update, I might have to hit one of these settings real quick
[7:07] and just make sure that it updates the cache here.
[7:10] This is one of the areas where the fluid simulator was acting a little bit weird with the playback.
[7:15] A little bit not the way you might expect it,
[7:18] but as you can see, scaling that up a little bit and giving a few more keyframes
[7:21] gave me a lot more fluid into my scene, which you may or may not want.
[7:26] This looks pretty crazy at this point, but hey, it's kind of cool.
[7:29] But using these fluid particles in the viewport,
[7:31] you can kind of get an idea of how much fluid you might be adding to your scene
[7:35] and kind of tweak your settings respectfully.
[7:36] So, when I'm happy now with the amount of fluid in the scene,
[7:39] I'm going to go ahead and change that back from replay over to module
[7:43] where I can start baking some of the different stages here.
[7:45] You also want to change the end frame of the cache here
[7:47] as it's only going to bake 50 frames right now.
[7:50] If you wanted more than that, you'd want to increase this right here.
[7:52] I'm going to leave it at 50 because I'm not doing a big simulation for this tutorial.
[7:56] So, here you can see I just click the bake button, let it go for a while, then hit escape.
[8:00] And the cool thing is that you can click resume and continue your bake
[8:03] or you can free your bake.
[8:04] This is something you could never do before.
[8:06] And it's really cool.
[8:07] You just click resume and it picks up from where it left off.
[8:10] I think this is looking pretty cool.
[8:11] So, we can move on to the next baking stage now, which is the meshing stage.
[8:15] So, scrolling down here, you can see we have mesh.
[8:17] You don't want to go ahead and check that.
[8:19] You have the up res factor, which kind of adds another layer of divisions over the fluid
[8:23] to make it a bit of a higher quality fluid.
[8:26] So, even at 64 divisions, if you have it set to an up res factor of two,
[8:30] it's going to be a higher quality than 64 divisions of our old fluid simulator inside of blender.
[8:35] What you also want to do is enable use speed vectors.
[8:37] This is a way of adding some motion blur to your fluid
[8:40] because it really helps the realism of fluid to add a bit of blur.
[8:44] And it doesn't really work with the cycles blur
[8:46] because it takes insanely long right now to render.
[8:48] Might be a bug, but if you choose use speed vectors,
[8:51] there is a way that we can add some motion blur to it using compositing.
[8:54] So, go ahead and choose use speed vectors.
[8:56] So, that's really the only setting you need to change.
[8:58] You can play around with some of the smoothing options here,
[9:00] but I found the default to look just good enough for what I need.
[9:03] So, I'm going to leave it at that and choose bake mesh.


### Particles [9:05]
**Transcript (timestamped):**
[9:05] So, here I have a fluid simulation that I think looks pretty cool
[9:08] and I'm ready to move on to the particles and then the rendering.
[9:11] So, there's one more stage of baking as I've been saying.
[9:13] It's the particles and here we're going to want to enable spray, foam and bubbles.
[9:19] You can see we have a lot of settings for fine-tuning the particle simulations here.
[9:23] I didn't really find that I needed to change any of these.
[9:25] A lot of these settings change things very subtly,
[9:28] so it's not going to be a big obvious change.
[9:30] The biggest one is going to be the up res factor.
[9:33] This is going to take a lot more time to bake if you increase it,
[9:35] but it's going to give you a lot more particles and a lot higher resolution particles, I guess.
[9:39] I found that you really don't need to use the up res factor
[9:42] if you have about 128 divisions or more on your fluid simulation,
[9:45] but you could do like your low quality bake on your fluid here
[9:49] and then the higher quality version of the particles by upresing it here,
[9:53] changing it to 2 and getting more quality.
[9:55] But with those selected, all we need to do is choose bake particles.
[9:58] This again will happen quite fast at only 64 divisions.
[10:01] And there you can see we just got a little bit of extra particles added to our scene.
[10:05] And if we go ahead over to the particle simulations here,
[10:08] you can see we have all of those particles as particle simulations now in Blender.
[10:12] So, I can turn off the view on some of these and you can see that the spray
[10:15] is the particles on the edge of your wave there, kind of creating that spray.
[10:20] That's something that's really cool and manifold to kind of be able to add that spray
[10:24] with something that's really hard to achieve before.
[10:27] Now it's going to be a lot easier.
[10:28] Now, before I get into rendering our finished fluid,
[10:30] I'm going to go ahead and bake this at a higher resolution that I want for our scene.
[10:33] I can see the simulation is working and now I want my higher resolution.
[10:37] So for my final bake in this tutorial, I'm going to go for 128 divisions.
[10:42] I recommend going even higher if you can, but it's going to be hardware limited
[10:46] if you don't have the hardware going up to 200 looks pretty nice.
[10:49] All way up to 256 looks really cool.
[10:52] If you can go that high and what's cool is that the fluid particles are going to
[10:56] automatically increase with the resolution of your stimulation.
[10:59] So you really don't have to change the particle settings as there's just going to be
[11:02] more particles with more resolution.
[11:04] So while we're doing all this baking, I got something I want to quick tell you about.


### Squarespace [11:07]
**Transcript (timestamped):**
[11:07] If you want to build a website hassle free to get you up and running quickly,
[11:11] check out this video sponsor Squarespace.
[11:13] Whether you want to build an awesome looking portfolio, blog or e-commerce site,
[11:17] Squarespace makes it all easy to do with their powerful tools for appointment
[11:21] scheduling, social media sharing, email campaigns and much more.
[11:24] It's so easy to use actually that I'll be building my own site in the next few weeks.
[11:28] So excited for that.
[11:30] Head over to Squarespace.com for a free trial and when you're ready to launch your website,
[11:34] I can save you some money.
[11:35] If you use my link in the video description with the coupon code CGGEEK,
[11:39] you will save 10% off your first purchase of a website or domain.


### Rendering [11:43]
**Transcript (timestamped):**
[11:43] So now we have a much nicer looking bake at 128 divisions.
[11:47] And as you can see, the quality already looks a lot better and we have a whole lot more
[11:50] particles being added into our scene, which is really cool.
[11:53] So let's go ahead and start rendering some of those.
[11:54] We'll start off by right clicking and shading smooth our fluid there.
[11:57] So now all I need is a fluid material and an environment to add light to our scene.
[12:01] So I'm going to go ahead and split up my window here so I can bring in a shader editor up
[12:05] on top here.
[12:06] I'm going to give our fluid a new material by deleting the principled shader going shift
[12:11] day and adding in a shader glass shader here.
[12:14] We're just going to change it to 1.3333 and that will work just fine for our glass shader
[12:20] connecting it up there.
[12:21] Change it from EV over to cycles just as it's a bit easier to get nicer looking results
[12:25] with cycles.
[12:26] And then I'm going to jump to the world settings here and choose an environment texture under
[12:30] the color here.
[12:31] Choose environment texture and an HDR is really important for the look of your water using
[12:35] different HDR.
[12:36] So we'll give you very different results.
[12:38] So it's going to depend a lot on what the light shining and reflecting off of that fluid
[12:42] is going to look like.
[12:43] For this one I found a colorful studio HDR from HDR Haven looked really cool.
[12:47] I'll link to it in the description where you guys can check it out.
[12:49] So go ahead and open that up.
[12:50] And if we switch to rendered view here at the bottom, you can see that we have our fluid
[12:57] being rendered in a cycles.
[12:59] Now I'm going to jump over to our render properties here and under the film I'm going to choose
[13:04] transparent and then here I'm going to choose transparent glass.
[13:07] Now this is a pretty new feature and actually might be in the 2.83 alpha only.
[13:11] So you guys might want to download the latest version to make sure you have that feature.
[13:14] But if you choose transparent glass, that's going to make it look a lot more like water.
[13:18] And I just found I like the look of transparent glass without it reflecting the environment
[13:21] so much just taking the lighting basically.
[13:24] And as you can see it looks a bit more like water in my opinion.
[13:26] Now we just need to start rendering these particles.
[13:29] So the particles can be rendered as icospheres.
[13:31] So we're going to jump back to solid view here.
[13:33] I'm going to put my cursor over the side here and go shift A and add in a mesh icosphere.
[13:37] Now I'm going to change the icosphere settings down to just one subdivision because we're
[13:41] going to have a lot of these particles in the scene and we want them to be as low res
[13:45] as we can get away with.
[13:46] And what I'm also going to do is add a material now to this icosphere.
[13:49] So we're going to click new material and up here I'm just going to delete the principle
[13:53] shader again.
[13:54] And I'm just going to add in a diffuse shader here.
[13:56] Now I'm going to add in an add shader to connect it up with another glass shader.
[14:01] So I'm going to also add in a glass shader.
[14:02] We'll change it to 1.333 again, connect the glass into the bottom socket, the diffuse
[14:07] into the top.
[14:08] And then I'm going to take the color value down a little bit by taking the value here
[14:12] down to about a point five.
[14:14] Connect it up to your surface and we have a simple little material here that will look
[14:17] like a nice little foam bubble once it's rendered on our fluid.
[14:21] And then for the bubbles you want to make a separate object.
[14:23] So I'm just going to hit shift D to duplicate my little icosphere there.
[14:26] And for this is just going to be the glass material.
[14:29] I don't need the diffuse or the add so I can delete both of those.
[14:32] And then you can make the color a little bit brighter and maybe just a tiny bit blue for
[14:36] these bubbles.
[14:37] Also, when you duplicate that material, you don't want to make sure you hit that two
[14:39] button before you change any of the materials.
[14:41] Because otherwise you'll delete your original material like a dummy dummy and have to go
[14:44] ahead and recreate it like I just had to do here.
[14:46] So then under the bubbles, we're going to choose that to be rendering as an object
[14:49] as well, except this time it's going to be icosphere one, which is going to have that
[14:52] new bubble material on it.
[14:54] And then another little bonus tip here is one of the issues I found within Maniflow is
[14:58] that sometimes you'll get a pattern like a grid on your simulation.
[15:02] This is something I saw a lot of people talking about.
[15:03] You notice that the particles look kind of like they're on a grid pattern on your fluid
[15:07] simulation.
[15:08] Now I was told this is a bug that will likely be fixed in a future version of Blender.
[15:11] But kind of a workaround to hide this pattern at the moment is to duplicate your icosphere
[15:16] or multiple times make a collection out of them and make them all a bit different in
[15:19] the rotation.
[15:20] So for example, here I'm going to go ahead and hit shift D to duplicate my icosphere
[15:24] here, scale it down a little bit.
[15:26] And then I'm going to tab into edit mode and pull it off of its orange origin point right
[15:30] there.
[15:31] And then I'm going to add some of those particles to the scale here a little bit if you want
[15:32] to make some of those particles look a little bit different in shape.
[15:35] Then you're just going to go ahead and grab all of those particles, go control G to make
[15:39] a new collection.
[15:40] We can go ahead and name the collection right here, something like splash.
[15:43] And if you jump to your particle settings here and change it over to render as collection
[15:47] and then choosing that splash collection that we just created, you can see that this helps
[15:50] break up a little bit of that grid pattern.
[15:52] It doesn't do it 100%, but it definitely makes it a little bit less noticeable.
[15:56] Also choosing pick random then in that collection will give it a little bit more random variation
[16:01] of course, we want to go ahead and do that as well for the foam particles here.
[16:04] Now adjusting the scale of these icospheres will adjust the scale of the particles in
[16:08] your simulations.
[16:09] So you're going to want to make sure you're pretty happy with the scale of these particles
[16:13] by scaling up and down your icospheres here a little bit.
[16:15] Now as you can see with all those particles, our viewport gets very sluggish.
[16:19] So what you'll want to do to be able to keep your sanity and keep moving functionally in
[16:23] blender is turn off the view of all of these particle systems by clicking the little monitor
[16:27] screen there.
[16:28] This will give you a lot more responsiveness and blender not having all of those particles
[16:32] being visible.
[16:33] And as you can see, we get our sanity back.
[16:35] And then my last little bonus tip for you guys here is you can add in a mix shader onto
[16:39] your little particle splash and then use a transparent shader in the bottom socket.
[16:44] So go ahead and add transparent connect to the bottom and then add in an input object
[16:49] info node.
[16:50] Where is it right there?
[16:51] Connect the random output to the factor and this will give your particles a bit different
[16:55] of own opacity, a little bit different transparency between every particle, making it look a little
[16:59] bit more like foam I found that look kind of cool.
[17:02] We'll also improve the look of the stimulation a little bit is adding a little depth of field
[17:05] to our camera.
[17:06] So I'm jumping into our camera settings here, enabling depth of field under viewport display,
[17:10] just choose limits so we can see where we're focused at is that little orange plus single
[17:14] there.
[17:15] And we're just going to change the distance until it's right on the center of our fluid
[17:18] there.
[17:19] I'm going to jump over to our render layers here.
[17:20] And the one thing I want to add is the vector pass for adding some of that motion blur in.
[17:24] We're going to go ahead and choose vector there.
[17:26] And we can go ahead and see what we're looking like now when we render.
[17:29] Maniflow bro, maniflow bro, don't you know about that metaphor.
[17:34] So here is what we get rendered and this is looking really cool.
[17:37] You can see all those splash particles and we can make this look a little bit better
[17:40] with some motion blur as well jumping over the compositing tab here to add some of that
[17:44] motion blur in.
[17:45] We're just going to go ahead and go shift a add in a filter vector blur, connect the
[17:50] right up there, add the image to the image sockets, the depth to the Z socket and the
[17:55] vector to the speed factor there.
[17:57] So now if we go ahead and control shift click that vector node to bring it up in the background,
[18:01] as you can see that's crazy blurred way more so than we would probably want.
[18:05] So I'm going to take the blur factor all the way down to a point one five, found this to
[18:09] look quite a bit nicer and also choose curved in the vector blur settings.
[18:13] You can see dropped all the way down to a point one.
[18:15] We have a much nicer amount of blur.
[18:17] The last thing I want to point out is the vector blur is not as good as the cycles blur,
[18:21] but it seems to really be the only option that works right now.
[18:23] And you can make this look a little bit nicer as you can see, you get some weird blur on
[18:27] the particles here.
[18:28] And what I can do to kind of fix that is by adding a maximum blur speed here.
[18:32] I'm just going to change this to about a 256.
[18:34] I found to work pretty well.
[18:35] And you can see some of these jagged blurred particles just look a little bit cleaner,
[18:39] but it still adds some of that nice fluid motion to the fast moving fluid.
[18:43] So if you want to, you can go ahead and render this out as an animation now and get some really
[18:46] cool manaflow animations.
[18:49] But I'm really excited to start seeing manaflow simulations all over the web.
[18:52] It's a ton of fun to play around with.
[18:54] Yes, there's some current bugs and issues with it, but it is way better than the previous
[18:58] fluid simulator that Blender had.
[19:00] And it's going to open up all kinds of possibilities in the future.
[19:03] So I'm really excited about it.
[19:05] Hope you guys are too.
[19:06] And I hope you liked this video.
[19:07] That's going to do it for me though.
[19:08] I'm going to see you guys all in a future video.
[19:10] Bye bye.



---

## Captured Frames

- [1:47] tutorials/frames/the-new-blender-fluid-simulator-is-awesome---mantaflow-tutorial/frame_000.jpg
- [2:45] tutorials/frames/the-new-blender-fluid-simulator-is-awesome---mantaflow-tutorial/frame_001.jpg
- [5:10] tutorials/frames/the-new-blender-fluid-simulator-is-awesome---mantaflow-tutorial/frame_002.jpg
- [6:35] tutorials/frames/the-new-blender-fluid-simulator-is-awesome---mantaflow-tutorial/frame_003.jpg
- [9:15] tutorials/frames/the-new-blender-fluid-simulator-is-awesome---mantaflow-tutorial/frame_004.jpg
- [12:10] tutorials/frames/the-new-blender-fluid-simulator-is-awesome---mantaflow-tutorial/frame_005.jpg
- [14:05] tutorials/frames/the-new-blender-fluid-simulator-is-awesome---mantaflow-tutorial/frame_006.jpg
- [17:35] tutorials/frames/the-new-blender-fluid-simulator-is-awesome---mantaflow-tutorial/frame_007.jpg

---

## Structured Notes

### Core Technique
Full MantaFlow liquid-simulation pipeline: FLIP-based Domain/Flow/Effector setup, three-stage baking (Fluid → Mesh → Particles), and a from-scratch Cycles glass shader with icosphere-instanced foam/bubble particles and Vector Blur motion blur.

### Summary
Introduces Blender's then-new MantaFlow fluid/smoke simulator (Blender 2.82+, demoed on 2.83 Alpha): builds a Liquid Domain cube, a keyframed Inflow UV sphere, and collision Effector cubes, tunes Resolution/Time Scale/Time Steps, previews the sim live via the Replay cache mode, then bakes in three stages (Fluid → Mesh with Up Res Factor + Use Speed Vectors → Particles with Spray/Foam/Bubbles). Finishes with a Cycles glass-shader material lit by an HDRI, Transparent Glass film settings, icosphere-instanced foam/bubble particles with per-particle random-opacity variation and a randomized "Splash" collection to hide MantaFlow's particle grid-pattern bug, camera depth of field, and a Vector Blur compositing node for fluid motion blur.

### Key Steps
1. Scale up the default cube (S, 3) and flatten it slightly on Z to shape the fluid Domain; add a UV sphere, scale it down, and lift it (G, Z) so it sits at the top edge of the domain as the fluid source; add a few extra cubes near the bottom as collision obstacles (frame_000 shows this domain cube + obstacle-cube layout).
2. In the Physics tab, set the obstacle cubes' Fluid type to Effector (defaults to Collision, no changes needed); set the UV sphere's Fluid type to Flow, Flow Type = Liquid, Flow Behavior = Inflow (frame_001 confirms the Fluid Type dropdown: None / Flow / Domain / Effector).
3. To stop the inflow adding fluid for the whole timeline, hover over Use Inflow at a chosen frame (e.g. 40), press I to keyframe it on, step forward one frame, uncheck it, and press I again to keyframe it off.
4. Set the cube's Fluid type to Domain, Domain Type = Liquid (defaults to Gas/smoke — change it). Domain settings: Resolution Divisions 64 (raise for the final bake), Time Scale ≈ 0.5 (default felt too fast at 24fps), Time Steps Minimum raised to 2 for better accuracy on fast-moving fluid, Border Collisions per side, and under Liquid: Simulation Method FLIP, FLIP Ratio 0.970, Particle Radius 1.0 (frame_002 confirms these exact Domain/Liquid panel fields and values).
5. Under Cache, switch Type from Modular to Replay (frame_003 shows this Modular/Replay/Final dropdown) to scrub a live, low-res preview of the simulation directly in the viewport; tune the inflow object's scale/keyframes until the fluid volume looks right, then switch Cache Type back to Module/Final before baking. Raise the cache End frame (default only bakes 50 frames) as needed, then click Bake — MantaFlow bakes are resumable (click Resume after an interrupted bake) and multi-threaded across CPU cores.
6. Bake the Mesh stage: enable Mesh, set an Up Res Factor (e.g. 2) for a higher apparent resolution than the base division count, enable Use Speed Vectors (needed later for compositing-based motion blur, since Cycles' native motion blur is extremely slow on fluid meshes), then Bake Mesh.
7. Bake the Particles stage: enable Spray, Foam, and Bubbles (frame_004 shows this Particles panel — Spray/Foam/Bubbles tabs — on an already-baked foamy splash mesh), leave most fine-tuning fields at default, optionally raise the Up Res Factor for higher-quality particles, then Bake Particles. For the final bake, raise Domain Resolution Divisions to 128+ (200–256 for higher quality if hardware allows) — particle count/resolution scales automatically with domain resolution.
8. Shade the fluid mesh smooth, then build its material in the Shader Editor: delete the default Principled BSDF, add a Glass BSDF with IOR 1.333, and switch the render engine to Cycles (frame_005 shows the shader graph mid-setup; frame_006 confirms Cycles + GPU Compute render settings). Light the scene with a World Environment Texture HDRI (a colorful studio HDRI from HDRI Haven was used).
9. In Render Properties > Film, enable Transparent, then enable Transparent Glass (a 2.83-Alpha-era feature at the time) so the water reads as clear fluid rather than heavily reflecting the environment; confirmed field: Transparent Glass Roughness Threshold = 0.1 (frame_006).
10. Render the particles as low-poly Icospheres (1 subdivision): for foam, build a Diffuse + Glass (IOR 1.333) Add Shader mix with the diffuse color value dropped to ~0.5; for bubbles, duplicate that icosphere/material, keep only the Glass shader, and tint it slightly blue/brighter. Assign the Spray/Foam/Bubble particle systems to render as these objects. Work around MantaFlow's particle grid-pattern bug by duplicating the icosphere several times with varied rotation/scale, grouping them (Ctrl+G) into a collection (e.g. "Splash"), then setting the particle system's Render As = Collection with Pick Random enabled. Add extra per-particle opacity variation via a Mix Shader + Transparent BSDF driven by an Object Info node's Random output into the Factor. Finish with camera Depth of Field (Limits display, focus distance set to the fluid's center) and, in Compositing, a Vector Blur node (Image + Z/Depth + Speed inputs from the Vector render pass) with Blur Factor lowered to ~0.15, Curved enabled, and Max Speed ≈ 256 to control fluid motion blur (frame_007 shows the final rendered splash with the inflow sphere and obstacle cubes).

### Nodes / Settings
- Domain (Liquid): Resolution Divisions 64 → 128+ for final bake; Time Scale ≈ 0.5; Time Steps Minimum = 2; Simulation Method FLIP; FLIP Ratio 0.970; Particle Radius 1.0
- Cache: Type Modular / Replay (live viewport preview) / Final; End frame raised beyond the 50-frame default as needed; resumable, multi-threaded bakes
- Mesh bake: Up Res Factor (e.g. 2), Use Speed Vectors enabled
- Particles bake: Spray, Foam, Bubbles enabled; optional higher Up Res Factor for particle quality
- Fluid material: Glass BSDF, IOR 1.333, Cycles render engine, World Environment Texture HDRI
- Render > Film: Transparent + Transparent Glass, Roughness Threshold 0.1
- Foam/bubble icospheres: 1 subdivision; foam = Diffuse + Glass Add Shader mix (diffuse value ≈ 0.5); bubbles = Glass only (blue-tinted, brighter)
- Per-particle opacity variation: Mix Shader + Transparent BSDF + Object Info (Random → Factor)
- Grid-pattern workaround: duplicated icospheres (varied rotation/scale) grouped into a "Splash" collection; particle Render As = Collection + Pick Random
- Camera: Depth of Field enabled, Limits display, focus distance at the fluid's center
- Compositing: Vector Blur node (Image/Z/Speed from the Vector render pass), Blur Factor ≈ 0.15, Curved enabled, Max Speed ≈ 256

### Difficulty
Intermediate

### Blender Version
Blender 2.83 Alpha (MantaFlow shipped in 2.82; Transparent Glass noted as possibly a 2.83-Alpha-only feature at the time)

### Tags
fluid, simulation, particles, materials, shaders, glass, rendering, cycles, hdri, compositing, intermediate

---

## Related Tutorials
- [Fluid Simulations for Beginners Blender Tutorial (FLIP Fluids)](fluid-simulations-for-beginners-blender-tutorial-flip-fluids.md) — shares fluid, simulation, materials, rendering, cycles, hdri; a direct alternative-add-on comparison to this built-in MantaFlow workflow
- [I Tested 5 Different Ways to Simulate Water](i-tested-5-different-ways-to-simulate-water.md) — shares fluid, simulation; directly benchmarks Mantaflow against FLIP Fluids and other tools
- [NeXus for Blender Official Training - Follow Curve](nexus-for-blender-official-training---follow-curve.md) — shares fluid, simulation, particles
