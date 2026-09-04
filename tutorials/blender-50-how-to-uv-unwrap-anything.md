---
title: Blender 5.0: How to UV Unwrap Anything
source: YouTube
url: https://www.youtube.com/watch?v=dm3bBpZVmnE
author: On Mars 3D
ingested: 2026-07-19
blender_version: "5.0"
tags: [materials, modelling, beginner, intermediate, blender-5x]
extraction_status: complete
frames_dir: tutorials/frames/blender-50-how-to-uv-unwrap-anything/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Blender 5.0: How to UV Unwrap Anything

**Source:** [YouTube](https://www.youtube.com/watch?v=dm3bBpZVmnE)
**Author:** On Mars 3D
**Duration:** 28m34s | 33 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Let's learn how to UV map anything in Blender 5.
[0:02] If you've watched my previous videos on UV mapping anything in Blender, the good news is the workflows are entirely the same.
[0:08] But thankfully, Blender has made a bunch of quality of life updates that makes UV mapping in Blender even easier.


### Preparing 3D Models [0:14]
**Transcript (timestamped):**
[0:14] You can see what I have here.
[0:15] We have three various types of models.
[0:18] One being a low poly model that includes a lot of triangles.
[0:22] Another that is a fully hard surface sub-D model.
[0:26] And third, Susanne the Monkey, which is a fully organic object.
[0:31] What I want you to understand is that these workflows apply to any type of model.
[0:35] Now, before we jump into the five core steps on how to UV map anything, it helps to understand what is UV mapping.


### Understanding UV Mapping [0:40]
**Transcript (timestamped):**
[0:42] UV mapping is the process of taking a 3D object in the XYZ coordinate system and converting it to the U and V or X and Y coordinate system.
[0:52] With that in mind, the most important skill for UV mapping is knowing where to place the seams.
[0:58] When it comes to knowing where to place the seams, you can start with simple objects that are sitting around your desk or your desk itself.
[1:05] The best and most obvious place to put your seams is when you have corners.
[1:09] That's why cubes are so easy to UV map or you can take a look at a cylindrical object like a can.
[1:14] If I were to take this, you can see we have aluminum on the tops and bottoms.
[1:18] So I would cut the caps off, then split the label right down the middle.
[1:22] And then that will allow it to UV map properly.
[1:25] But then you might be thinking, well, what about objects that don't have obvious seams like skin or your hand or a monkey?
[1:33] The key thing to understand is UV seams are unavoidable.
[1:38] You absolutely need to place them on your models to properly unfold and UV map.
[1:43] The good thing is with the advancements of texturing software and tools, UV seams aren't a big deal.
[1:49] In this video, we're going to look at tri-planar mapping, which is a great way to blend and hide seams and just painting directly on your 3D models.


### Let’s Begin! [1:58]
**Transcript (timestamped):**
[1:58] So let's start with UV mapping this object.
[2:01] We can see that it's composed of multiple objects, which will make things easier to UV map.
[2:06] This is a hard surface mesh with clean topology and edge flow.
[2:11] This is actually a red dot site that I fully modeled with my modeling and topology course.
[2:16] So if you're interested, you can check that out on my website.


### Step 1: Apply Scale [2:18]
**Transcript (timestamped):**
[2:19] So step number one, this will honestly fix probably the vast majority of your issues.
[2:25] It is applying scale.
[2:27] If we select the rounder model, you can see we have a couple of objects that have a minor scale on here.
[2:34] So you would want to select all of your assets, hit Ctrl A and then apply scale.
[2:41] So select this bracket piece, press Ctrl A and apply scale.
[2:46] And everything should be set to 111 on your XYZ.
[2:49] Next, we'll head over to the UV editing tab in Blender.
[2:53] Now we're going to look at step number two.
[2:55] I recommend this step, especially for people that are new to UV mapping, because what happens is they look at the left and they see the UV editor and you're completely intimidated, scared, and have no idea what they're looking at.
[3:09] How am I supposed to take this 3D object here on the right and lay it out properly on the left?
[3:15] So we're going to fix that.
[3:16] The easiest way that I recommend is in your 3D viewport, head to UV and do project from view.


### Step 2: Project from view [3:18]
**Transcript (timestamped):**
[3:23] You could do that or you could do a reset, which will reset each face to the one-to-one UV coordinate system.
[3:30] But I like using project from view because it keeps things very nice and clean.
[3:35] Next, I'll hit Tab and then forward, non-slash, so I can really focus in on this object, this bracket piece.
[3:42] I will turn on my wireframe and this is what we're looking at.


### Step 3: Mark Seams [3:45]
**Transcript (timestamped):**
[3:45] Now here, you should already be visualizing where you want to select your UV seams.
[3:51] The most obvious places are going to be where you have corners or large changes in surfaces.
[3:57] So with this selected, I'll hit Tab and press 2 to go into edit mode.
[4:02] With that selected, we'll now select our edge loops.
[4:06] So the way that I want to do that is hold Alt and this will select your edge loop.
[4:11] I'll press N to hide the panel and I'll select the other panel because remember, this is a fully solid object.
[4:18] So like our can, we want to just split the top and the bottom.
[4:22] That's always your go-to when it comes to UV mapping.
[4:25] Then from here, remember, we want to split it down the center.
[4:30] So I would select this edge here with control, go all the way down to the end of the edge here
[4:35] and while holding control, left click that edge and there you go.
[4:40] This should be all the seams that we need to get started for UV mapping.
[4:44] So if you right click now, you can mark seam and there it is.
[4:48] It will turn everything red.
[4:50] You could also right click and press M on your keyboard to mark seam.
[4:56] Then you press 3 to go into face mode and we can select all of our faces.
[5:00] Now one thing that's super nice now is this here at the top left.
[5:04] I brought this up in my last video, but UV sync can be enabled


### Blender 5 Update: UV Sync Enabled by Default [5:05]
**Transcript (timestamped):**
[5:08] and is enabled by default now.
[5:10] Meaning that if I just select this model, this little guy here will be selected,
[5:15] which this is super nice because now this behaves like your traditional
[5:19] or almost every other UV editing tool.


### Step 4: Unwrap [5:22]
**Transcript (timestamped):**
[5:22] So with that, press A to select all because we're about to do step number three,
[5:27] which is unwrap or unfold.
[5:29] So if I right click, you see that we have unwrap.
[5:33] So simply unwrap and there it is.
[5:36] Perfect.
[5:37] One thing to keep in mind is that in the unwrapped settings,


### Unwrap Methods [5:38]
**Transcript (timestamped):**
[5:40] we have a couple different types of methods.
[5:43] We have conformal and angle based.
[5:46] The key thing to keep in mind is angle based is really good for organic models
[5:52] like characters or monkeys or something that's not hard surface.
[5:56] Conformal is really good when it comes to more of these
[6:00] geometric or hard surface pieces of geometry.
[6:03] Don't worry so much about remembering exactly that
[6:05] because really all you need to do is if one's not giving you the results you need,
[6:09] just try another.
[6:11] Right.
[6:11] We try angle based is about the same minimum stretch.
[6:13] Okay.
[6:14] A little bit of distortion here.
[6:15] We definitely don't want that.
[6:17] So I'm completely fine with what it defaulted to, which is conformal.
[6:21] Now we go on to step number five, which is going to be packing


### Step 5: Pack Islands [6:22]
**Transcript (timestamped):**
[6:24] because what happens is the default UV unwrap is essentially overlapping
[6:30] or getting very, very close.
[6:32] Right.
[6:33] This is very bad when it comes to texturing.
[6:35] We need to have what's called padding.
[6:38] We need to have distances between our UV islands to avoid issues later when we're texturing.
[6:44] So what I can do now is with all of this selected,
[6:47] you can just select all with A and go to UV.
[6:50] Then we have pack islands.
[6:52] Here we can see these are the default settings.
[6:55] I typically bump up the margin to maybe 0.005 and hit pack.
[7:00] And there you go.
[7:01] And what this does now is it gives us a nice distance between our objects.
[7:05] Now I've assigned this to my quick favorites.
[7:08] As in if I hit Q, you'll see that I have quick favorites and pack islands.
[7:12] So I'll do pack islands again.
[7:14] You can do maybe a 0.01 and do a pack.
[7:17] And that gives us some nice padding between our islands.
[7:20] Great.
[7:20] So those are the five core steps to UV map anything.
[7:24] Apply your scale, reset or project from view to create a clean slate for your UVs.


### 5 Step Process [7:25]
**Transcript (timestamped):**
[7:30] Select your edges and mark seams, unwrap and unfold your UVs,
[7:34] and pack your UVs.
[7:36] We're going to take that core workflow and apply it to our objects over and over again.
[7:41] Now you want to get in the habit of always checking your UVs.


### Verify and review UV Unwrap with Checker Map [7:45]
**Transcript (timestamped):**
[7:45] How do we do that?
[7:46] If we have this object selected, we head over to our shading tab.
[7:50] You can see we have this nice simple texture map.
[7:54] Now this texture map can be just brought in from our UV editor.
[7:59] For example, I can head over here.
[8:01] If I give myself a little bit more,
[8:04] we do create a new image in our UV editor.
[8:07] And I'll just call this UV checker.
[8:10] I'll set this to 2048.
[8:13] We do generated type UV grid and do new image.
[8:17] And there you go.
[8:17] This will give you a default checker map that we can use on our model.
[8:22] So then here with that selected, we head over to shading and we can put that new checker map.
[8:28] You can see I have UV checker right here.
[8:30] That was the one I just generated.
[8:32] And then there it is.
[8:34] It's literally the same one that I had just generated.
[8:37] And this will now allow me to review the model.
[8:41] Now if you're not seeing it by default, it's just our render mode.
[8:44] We can see we have viewport shading set to solid.
[8:47] So you could set that to material preview or hit Z on your key bra.
[8:52] Key bra.
[8:53] Z on your keyboard and then do material preview.
[8:56] We can switch back to solid material preview.
[8:59] That's a very quick way to just jump back and forth.
[9:02] And the goal here, you guys, is we want nice clean grids, square like checkers.
[9:08] We don't want this to be, you know, if I just happen to go in here and scale this,
[9:14] if we start to get rectangular, that's going to cause an issue.
[9:17] But everything looks good.
[9:18] Let's apply this workflow to another object, something that's a bit more complex.


### OM3D Game Art Program [9:24]
**Transcript (timestamped):**
[9:26] If you want to learn game art the right way and not just follow random tutorials,
[9:30] I built a full game art program that walks you through the entire pipeline
[9:34] from an idea to a finished portfolio piece.
[9:38] It's split into two courses.
[9:39] Modeling and UV mapping foundations is the first one,
[9:42] and texturing, rendering, and presentation is the second.
[9:45] Each has over 40 modules, 15 hours of narrated content, exercises, time lapses, project files.
[9:52] And you're not doing it alone.
[9:54] You get access to a private Discord community where you can ask questions and get feedback along the way.
[9:59] If you want real world production workflows, you can use for both studio work and your personal
[10:03] projects, the program is live now.
[10:06] I'll see you there.


### Apply the 5 step workflow to objects with thickness [10:10]
**Transcript (timestamped):**
[10:10] Now, this is still a cylindrical object, but now we're dealing with thickness, all right?
[10:16] Now, if this UV checker here is bothering you and your UV editor,
[10:19] you can simply hit the X on the image settings.
[10:23] And so here we go.
[10:24] Just like I had explained previously, you get a mess of UVs and we don't want to deal with them.
[10:29] So I will actually press Z and go back to solid mode.
[10:33] Then I'll press Ctrl A and apply scale.
[10:36] Then I'll go into edit mode, select all of these with A and go to UV and do project from view.
[10:42] And that gives me a nice clean slate so I don't have to worry about that mess on the left.
[10:46] Now, press tap to enter edit mode, and we begin selecting our edges.
[10:51] Now, like I said, we want to cut off the tops to separate the thickness.
[10:56] So if I press 2 for edit mode, alt click this edge here, alt click this bottom edge here as well.
[11:03] Same thing with this edge and this edge.
[11:07] So I'm holding shift alt to add to selection, right?
[11:10] So again, it's alt click.
[11:12] And when you want to add new loops, you hold alt and shift and add to selection.
[11:16] Now, I want to show you something because we know that we need to kind of cut this in half,
[11:23] right?
[11:24] Or at least give it an edge to split, right?
[11:28] So I'll show you what happens when you don't do that.


### Example of bad UV seams [11:30]
**Transcript (timestamped):**
[11:31] So I'll add in one edge here at the bottom, but I'll leave this inside thickness piece.
[11:35] So right click, press M to mark scene, press 3 to enter face mode, select all, right click and unwrap.
[11:43] And there you go.
[11:44] We start to get a bit of a mess here now.
[11:47] And really what's happening here, regardless of whatever method you're using,
[11:52] angle based, conformal, minimum, it's going to look terrible, right?
[11:58] Because again, you have to understand what's happening here without a scene, right?
[12:03] Literally, if you were to try to take this label here as a sleeve and then try to lay it flat
[12:08] without cutting that back label portion, you're going to have a bad time.
[12:13] That's exactly what's happening here.
[12:15] And I look at this with material preview, with this material and the top side or the outside.
[12:22] It looks good, but we look on the inside and it's actually a pretty interesting effect, right?
[12:26] It looks nightmarish.
[12:28] So we already know what the VIX is.
[12:30] Now we head in here, right?
[12:32] And this is why I love the UB sync now, the new thing in Blender,
[12:35] because I can see my UBs without having to press A.
[12:37] That was always super annoying.
[12:39] But anyways, I can go in here and select these edges.
[12:46] Go all the way to the backside.
[12:49] While I'm holding control, this will specifically select a path, right?
[12:54] There's a bunch of different ways to do this, but this is exactly what I want.
[12:58] So you can select that, right click, mark seam, go into face mode, select all, unwrap.
[13:03] Boom, there you go.
[13:05] Let's look at our checkers.
[13:07] We got nice, square, square, square, square.
[13:11] Let's look at our checkers.
[13:13] We got nice squares all across.
[13:17] Looks beautiful.
[13:18] That's exactly what we want.
[13:21] Now, if we look at this, remember what I said, this is a smooth model, right?


### Unwrapping with sub-d models [13:22]
**Transcript (timestamped):**
[13:27] So if I head down to the bottom and look at this UV seam, in our subdivision,
[13:34] we have this here, which is Katmell Clark.
[13:37] It's smoothing by two subdivisions.
[13:39] And if I go to advanced, notice what's happening.
[13:42] It's preserving our borders.
[13:44] And so we get this little bit of distortion here that's happening.
[13:48] You see that?
[13:49] This bit of a distortion.
[13:51] You can also visualize distortion.
[13:54] So if I go over here to overlays, this will visualize distortion.


### Overlay: UV Stretch/Distortion [13:56]
**Transcript (timestamped):**
[13:57] The first thing I have to do is go into edit mode, and let me move this over to the side.
[14:02] And now head over to UV stretch and look at that.
[14:05] This is going to show us where we have some distortion on our model.
[14:09] So we can alleviate some of that distortion by going in here now.
[14:15] I'll show this in edit mode so we see what's happening.
[14:17] And then if I do keep boundaries and then all, you can see how that will help
[14:22] the smoothing here of the UV.
[14:25] So that's smoothing the borders of our UV.
[14:27] That's just always something I like to bring up just in case you UV mapped your object and base
[14:31] mesh form and then smooth it.
[14:33] If you get distortions around your seams, you can just smooth these seams out.
[14:38] So that's looking great.
[14:39] And I can already tell what some of you are going to say.
[14:42] There is a way to straighten these UVs out and we're going to look at that shortly.
[14:46] So let's keep moving around.
[14:47] Let's do one more object that's probably one of the most complex, which is this guy here.


### Apply the 5 step workflow to complex objects [14:48]
**Transcript (timestamped):**
[14:51] Right?
[14:51] Looking at this, you're like, oh man, this is all one fully modeled object.
[14:56] How the heck do we go about UV mapping this?
[14:58] One method that helps a lot is we already know.
[15:02] Right? Let me set this to solid most of it's easier to see.
[15:05] We already know we got to select these edges, right?
[15:07] So let me turn off smooth preview and look at this messy UVs.
[15:11] So we first select this object, we apply our scale, we hit tab, select all, and let's just
[15:18] project from view because this is a mess.
[15:20] I don't want to worry about this junk.
[15:22] I go to project from view and I got to emphasize this because you guys always bring up in this
[15:26] in the comments.
[15:27] It's not necessary.
[15:28] You can unwrap with Mark seams.
[15:30] The reason I bring this up is because it confuses people that are learning.
[15:34] Right?
[15:34] It's very, again, intimidating right out the bat, but you don't need this step to unwrap.
[15:40] It just helps clean our UV editor out.
[15:43] Next, we want to select our UV seams.
[15:45] Now, here's the thing that's super nice is I could go through and select all these edges manually
[15:51] on our mesh, right?


### Select seams with Sharp Edges [15:53]
**Transcript (timestamped):**
[15:53] Or I can use select sharp edges and I have that set to my quick favorite.
[15:59] So I'll hit Q for quick favorites and do select sharp edges and there it goes.
[16:02] Now, this is super nice because it selects the vast majority of edges that I need and
[16:07] you can see, I mean, look how nice that is, right?
[16:10] I do have to clean some stuff up here that gets a little bit more intricate.
[16:14] And remember, whenever you have these cylindrical type objects here, you need to have a seam to
[16:21] split that.
[16:22] So what I'll do is to spare you time.
[16:25] I'll run through, select the edges, get it ready for seam work here.
[16:29] So I just went through, cleaned up the edge selection and now I'm ready to move on to the
[16:40] next step.
[16:40] So which is right click, mark seam, press three, A to select all, and then all in my UV
[16:47] editor, right click and unwrap.
[16:50] And there we go.
[16:51] Now, here's the thing.


### Blender 5 Update: UV Sync and Mark Seam in UV Editor [16:53]
**Transcript (timestamped):**
[16:53] I missed a couple of edges and that's gonna happen, right?
[16:57] You're like, oh shoot, I missed some edges over here.
[17:00] No big deal.
[17:01] And this is why this is the update for Blender 5 with this fantastic UV sink on.
[17:06] So I can go in and select my edges here, right in the UV editor to finish that selection.
[17:13] It's these edges right here that I forgot.
[17:15] And then I can go to UV and then mark seam right in the editor, right?
[17:20] So then if I go in and let's say I select, I press L to select link and then unwrap,
[17:28] boom, look at that.
[17:29] I can just do that right in the UV editor.
[17:31] And this like long time professional 3D artist, I've been using Maya forever.
[17:36] I've been using UV plugins forever.
[17:39] This is super, super nice and is probably one of my favorite quality of life updates.
[17:44] So I select everything, good to go.
[17:47] And we see that overall, it's pretty good.
[17:50] It's using minimum stretch.
[17:53] I could use conformal.
[17:56] Look at that, right?
[17:57] Conformal, which is made for hard surface objects like these,
[18:00] UV maps is so much nicer.
[18:03] We double check our overlay.


### UV Stretch/Distortion [18:06]
**Transcript (timestamped):**
[18:06] We can see our overlay is on.
[18:09] We see that we don't get any or too much blue or wait, there it is actually.
[18:13] Notice you might get some extra blue or green.
[18:16] Those are areas of distortion.
[18:19] So we look at our material preview.
[18:22] We apply the UV checker material.


### Troubleshooting UV issues [18:25]
**Transcript (timestamped):**
[18:26] Let's select a link here with L. Ah, there we go.
[18:30] All right.
[18:30] So I missed a couple areas.
[18:33] And this one is just barely, right?
[18:36] I missed this one tiny edge here.
[18:38] And this is where a lot of problems happen.
[18:40] This is why we have to go through this workflow of checking our UV distortion.
[18:45] I already have this in my quick favorite.
[18:46] So if I press Q, I can just mark that edge seam.
[18:49] There it is.
[18:50] I forgot to do that here too.
[18:52] So I'll select that one, right?
[18:54] Press Q and then mark seam.
[18:57] And this is why I always love showing you guys what happens when things go wrong.
[19:00] This is how I always teach my classes, right?
[19:02] And there it is.
[19:04] Beautiful.
[19:06] Everything's fine when it works, right?
[19:08] But it's always what happens when things don't work
[19:10] and how do you troubleshoot that to figure that out?
[19:13] Awesome, right?
[19:14] And so now you get the idea.
[19:16] It's that workflow over and over and over again.
[19:20] And then we have a finished version.
[19:24] So I'll hide this.
[19:25] I have the finished version.
[19:27] We jump to layout.
[19:28] I can go into material preview and this is it, right?
[19:31] We see how good everything looks.
[19:34] And let's see what happens when something else goes wrong.
[19:37] So I have the top piece here.
[19:38] And this is what I mean.
[19:39] We'll troubleshoot a couple of things, right?
[19:41] I'll take this.
[19:42] You can see that the mess of UVs here.
[19:44] If I right click, unwrap it, still unwraps completely fine.
[19:47] Conformal looks great.
[19:49] But here's something that you have to keep a close eye on
[19:53] is that it looks okay.
[19:57] But our grids here, they're not square.
[20:01] They're more rectangular, right?
[20:03] And think to yourself, why is that happening?
[20:05] What could cause this to have nicely UV mapped UVs,
[20:10] but not be square like?
[20:11] It comes back to our first step, which is applying scale.
[20:16] If I select this and I press N, look at that.
[20:19] This has transforms on our Y and Z axes that I never applied.
[20:24] So no big deal.
[20:25] I'll hit control A, apply scale, go back to my UV editor, press A, unwrap this,
[20:32] and look at, watch what's about to happen, right?
[20:34] Look at these guys.
[20:36] They're going to go from rectangular now, boom, to square.
[20:39] That's exactly what we're talking about.
[20:41] That's exactly what we want.
[20:44] So that should give you a good idea on how I went about UV mapping this.


### Custom UV Checker [20:48]
**Transcript (timestamped):**
[20:48] Also, you'll see I have this really cool looking checker map here.
[20:52] That is from UV checker map maker.
[20:55] It's free.
[20:56] I always encourage you guys to support them.
[20:58] It's fully procedural.
[20:58] You can do all sorts of stuff and get some really unique looking maps.
[21:02] And especially like the arrows, because it lets you know
[21:04] the direction your UV islands are facing.
[21:06] So again, what I've done so far is just taken all of this,
[21:10] applied the same workflow over and over.
[21:13] Then I select everything at the very end, tab, A to select all, A,
[21:20] and then we can go through and do a UV pack islands, right?
[21:25] And it goes through in packs.
[21:27] Now this is using a different UV packer.
[21:29] I'm just showing vanilla blender here.
[21:31] So you can see the UV packer by default does need a little bit of work.
[21:35] But again, even if I look at this object here,


### Reviewing UVs on other models [21:36]
**Transcript (timestamped):**
[21:38] look at how this was UV mapped, right?
[21:40] And we can look at this in solid so we can clearly see where these UV seams are.
[21:45] All in all, it's right on the corner, right on the edges, and works very, very well.
[21:51] There were a couple other new updates in blender five.
[21:54] For example, let's say I just grab a few parts,


### Blender 5 Update: Move UVs on Axis [21:55]
**Transcript (timestamped):**
[21:58] or let's say I grab like my lens objects here,
[22:02] and I want those to be on a completely separate map, right?
[22:05] So I have these guys, should be one more in here.
[22:11] There we go.
[22:12] And let's say I want to separate these onto their own.
[22:15] So I can hit tab to enter edit mode, and then three, and then A to select all.
[22:20] So we can use our numpad to move these in what's called the UDIN, right?
[22:25] So now I've moved this completely separate, which is great.


### Blender 5 Update: Pack Islands to Custom Region [22:28]
**Transcript (timestamped):**
[22:28] Then I can say, hey, you know what?
[22:29] I want these guys instead of being sporadic and all over the place.
[22:33] Let me throw this down at this bottom quadrant here with control B.
[22:37] So I'll do control B and left marquee select.
[22:42] Boom.
[22:42] So I have now have this specific area and watch this.
[22:45] I can head over to UV pack islands.
[22:48] I have it on my quick favorite.
[22:49] So I'll do pack islands.
[22:51] We can change this to pack to custom region.
[22:56] And just like that, it'll take all those UVs all over the map,
[23:00] throw them right in this region here, which is super, super nice.
[23:04] I have instances like that where I want to take a specific part of the model,
[23:07] put them together, and move them in the quadrant.
[23:09] So awesome to see Blender stepping up its UV mapping game.


### Blender 5 Update: Arrange Islands [23:13]
**Transcript (timestamped):**
[23:13] And one of the last most impactful updates I found was arrange islands.
[23:20] So you can now do it like this.
[23:22] You go to arrange UV islands.
[23:24] By the way, if you want to get rid of this quadrant thing, you do control.
[23:27] I'll be there.
[23:29] You go.
[23:29] So again, we can arrange islands and you can do it by X, Y.
[23:36] You can change the margin, how close you want these.
[23:38] So that's also super nice.
[23:40] You can do a line by center.
[23:43] Very powerful way if you wanted to, especially if you're doing like texture sheets and whatnot.
[23:48] But okay, those are the key updates for Blender 5.
[23:52] What I'll look at now is addressing a couple of questions I get a lot.


### Apply the 5 step workflow to Game Art Assets [23:54]
**Transcript (timestamped):**
[23:56] It's always nice when I can show nice clean topology,
[23:58] but what happens when you have an object like this, which is triangulated, right?
[24:04] A bit of a mess.
[24:07] Well, the same thing still applies, right?
[24:09] Like this is a very, very unique object here, right?
[24:12] So the way that I would go about it is if I turn off everything but my seams, there we go.
[24:20] I can select this, go into tab edit mode.
[24:24] I can go into edge mode, select sharp edges, and there you go.
[24:28] Like for hard surface objects, it works perfectly fine.
[24:32] I can mark my seam and then go about my day.
[24:37] And you could literally do that for everything except the script because it's organic, right?
[24:41] So I tab all of these.
[24:44] Let's say now I'll go into edge mode and do a select sharp edges.
[24:52] I mean, there you go, right?
[24:53] It selects most of the sharp edges on my entire object.
[24:57] There are a couple of things that I need to clean up,
[24:59] but that plus UV mapping will give me exactly or give me the vast majority of my seams that I need.
[25:08] Because now with that, that's how I go through and UV map everything on this object here.
[25:13] Then one of my most common questions from teaching in my YouTube video is if I look at


### How to minimize UV distortion [25:15]
**Transcript (timestamped):**
[25:19] Suzanne here, she already has UVs.
[25:22] I go to UV editing, UVs are fine for this demonstration.
[25:26] And you might be concerned with, well, I want to minimize the amount of UVs,
[25:30] minimize the distortion.
[25:32] You cannot minimize distortion without UV seams.
[25:35] So the only way to get rid of distortion is by adding more UV seams.
[25:41] And so with this quick demonstration here, if I take this model with the UVs as is,


### Dealing with UV seams when texturing [25:45]
**Transcript (timestamped):**
[25:47] head over to Substance Painter.
[25:49] I want to show you an example, right?
[25:51] So I have Suzanne here already baked with the material, but what's happening here is look at this.
[25:59] We see this obvious seam here where we should have the marble continuous over the seam.
[26:05] That's where you can hide your UV seams by using something called tri-planar mapping.
[26:10] So you see in Substance, I have my material, my mask, and then within my mask,
[26:16] I have this marble here being applied.
[26:19] With this marble selected, I go to projection and switch this from UV projection to tri-planar
[26:26] projection.
[26:27] And there you go.
[26:28] It hides the UV seams.
[26:29] And really what it's doing, it's projecting the texture from X, Y, and Z in 3D space.
[26:35] Hence tri-planar.
[26:36] And it's blurring them.
[26:38] So it's a lot less noticeable.
[26:40] If you combine that with texture painting in 3D, I'll add a black mask here.
[26:48] I'll make this red so it's easy to see.
[26:52] And then in this, I'll paint, quickly paint.
[26:55] And we have a seam right here, right?
[26:59] We have the seam right here.
[27:00] So we want to avoid that UV seam, right?
[27:03] Well, the good thing, you guys, is we can just simply paint in 3D.
[27:09] And look at that.
[27:09] It automatically takes care of everything for us.
[27:12] So now we don't have to worry about hiding our seams through the 2D UVs.
[27:18] We can do that right through 3D texture painting.
[27:21] And now to bring this home, this is exactly the workflow that I used for the game art


### The 5 step workflow applied to Game Art Assets [27:22]
**Transcript (timestamped):**
[27:26] environment you see in front of you.
[27:28] This is what I've included in my game art course.
[27:30] And for example, I'll select my lamp, isolate.
[27:34] We can take a look at all of this here.
[27:36] And we see all the nice UVs.
[27:39] And what's even nicer is that I specifically took all of these assets here
[27:44] and packed them down to this UV using these same exact workflows,
[27:50] using some extra add-ons, free by the way, to get these beautiful UVs
[27:55] that replicates a production pipeline.
[27:58] I will plan to release more YouTube videos on some of the add-ons that I use,
[28:02] but I wanted to make this one really focused on just using Blender 5 and Vanilla Blender.
[28:07] But in the meantime, if you're interested in learning more,


### Wrap Up [28:08]
**Transcript (timestamped):**
[28:09] be sure to check out the game art course, check out the Discord community.
[28:13] We've got hundreds of people already in there helping each other every day.
[28:17] So with that, I'll see you in the next one.



---

## Captured Frames

- [4:44] tutorials/frames/blender-50-how-to-uv-unwrap-anything/frame_000.jpg
- [6:55] tutorials/frames/blender-50-how-to-uv-unwrap-anything/frame_001.jpg
- [9:02] tutorials/frames/blender-50-how-to-uv-unwrap-anything/frame_002.jpg
- [13:07] tutorials/frames/blender-50-how-to-uv-unwrap-anything/frame_003.jpg
- [14:05] tutorials/frames/blender-50-how-to-uv-unwrap-anything/frame_004.jpg
- [17:06] tutorials/frames/blender-50-how-to-uv-unwrap-anything/frame_005.jpg
- [22:51] tutorials/frames/blender-50-how-to-uv-unwrap-anything/frame_006.jpg
- [23:36] tutorials/frames/blender-50-how-to-uv-unwrap-anything/frame_007.jpg

---

## Structured Notes

### Core Technique
A universal 5-step UV unwrapping workflow (apply scale → project from view → mark seams → unwrap → pack islands) applied to hard-surface, sub-D, and organic models, plus the Blender 5.0 UV quality-of-life updates (UV sync on by default, mark seam inside the UV editor, pack to custom region, arrange islands).

### Summary
On Mars 3D demonstrates one repeatable workflow that unwraps any model type — low-poly triangulated game assets, clean sub-D hard surface, and organic meshes — with seam-placement logic explained through real-world objects (cut the caps off a can, split the label down the middle). The second half covers verifying UVs with checker maps and the UV Stretch overlay, troubleshooting non-square checkers (unapplied scale) and messy unwraps (missing seams), and hiding unavoidable seams at texture time via tri-planar projection and 3D painting in Substance Painter.

### Key Steps
1. **Apply Scale** — Ctrl+A → Apply Scale on every object (scale must read 1,1,1); unapplied scale is the #1 cause of rectangular (non-square) checker distortion [frame_006 troubleshooting moment at 20:16].
2. **Project From View (or Reset)** — UV menu → Project from View for a clean slate in the UV editor; not required for unwrapping, purely to de-clutter.
3. **Mark Seams** [frame_000, 4:44] — Tab → edge mode (2), Alt+click edge loops (Shift+Alt to add), Ctrl+click for shortest-path selection; right-click → Mark Seam (or M). Cylinder logic: cut caps off, split the sleeve once vertically. For objects with thickness, also seam the inner/outer boundary or the unwrap becomes a mess (demonstrated at 11:31).
4. **Unwrap** — right-click → Unwrap; method Conformal for hard surface, Angle Based for organic — just try the other if one distorts (Minimum Stretch also available).
5. **Pack Islands** [frame_001, 6:55] — UV → Pack Islands: Shape Method "Exact Shape (Concave)", Scale+Rotate on, Margin Method Scaled, margin bumped to 0.005–0.01 for texture padding, Pack To Closest UDIM.
6. **Verify with a checker map** [frame_002, 9:02] — New Image in UV editor, Generated Type: UV Grid, 2048px; assign in Shading tab; want square checkers everywhere. Free "UV Checker Map Maker" gives procedural checkers with direction arrows.
7. **Check distortion** [frame_004, 14:05] — Overlays → Display Stretch: Angle in the UV editor; blue = fine, green/red = distortion. On sub-D models set the Subdivision modifier's Advanced → UV Smooth to "Keep Boundaries"/"All" to fix seam-border distortion.
8. **Speed-ups** — Select Sharp Edges (via Q quick favorites) auto-selects most hard-surface seams; Blender 5.0's UV sync lets you fix missed seams directly in the UV editor [frame_005, 17:06]: select edges there → UV → Mark Seam → L to select linked → Unwrap.
9. **Blender 5.0 packing updates** — move islands between UDIMs with numpad; Ctrl+B marquee defines a custom region then Pack Islands → "Pack to Custom Region" [frame_006, 22:51]; Arrange UV Islands operator [frame_007, 23:36] with Initial Position/Axis/Align/Order (e.g. Bounding Box, Y, Min, Largest to Smallest) for texture sheets.
10. **Hide seams while texturing** — in Substance Painter switch a fill's projection from UV to Tri-planar (projects along X/Y/Z and blends), or paint directly on the 3D model across seams.

### Nodes / Settings
- Pack Islands: Shape Method Exact Shape (Concave); Scale ✓ Rotate ✓; Rotation Method Any; Margin Method Scaled; Margin 0.001 default → 0.005–0.01 recommended; Lock Method All; Pack To Closest UDIM / Custom Region
- Unwrap methods: Conformal (hard surface), Angle Based (organic), Minimum Stretch
- Subdivision Surface modifier: Catmull-Clark, Advanced → UV Smooth: Keep Boundaries → All (fixes border distortion)
- UV editor overlay: UV Stretch display set to Angle; UV Opacity slider
- Checker: 2048×2048 Generated UV Grid image
- Arrange/Align Islands: Initial Position Bounding Box, Axis Y, Align Min, Order Largest to Smallest, Margin
- Shortcuts: Ctrl+A apply scale, Alt+click edge loop, Shift+Alt add loop, Ctrl+click shortest path, M mark seam, L select linked, Q quick favorites, Z shading pie, Ctrl+B custom region marquee

### Difficulty
Beginner–Intermediate

### Blender Version
Blender 5.0 (UV sync default, mark seam in UV editor, pack to custom region, arrange islands are 5.0 updates; workflow itself is version-agnostic)

### Tags
materials, modeling, beginner, intermediate, blender-5x

---

## Related Tutorials
- [The Easiest Way to Texture in Blender (Adaptive, No UV Unwrapping)](the-easiest-way-to-texture-in-blender-adaptive-no-uv-unwrapping.md) — the counterpoint workflow: texturing without UVs; this video covers when you do need proper UVs
- [Perfect Textures in Blender - Works Every Time](perfect-textures-in-blender---works-every-time.md) — texture application that benefits from the clean UVs produced here
- [How to fix SHADING ERRORS in Blender](how-to-fix-shading-errors-in-blender.md) — companion troubleshooting mindset for mesh/shading issues
