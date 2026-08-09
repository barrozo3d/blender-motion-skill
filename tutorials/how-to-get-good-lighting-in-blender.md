---
title: How to get good lighting in blender
source: YouTube
url: https://www.youtube.com/watch?v=c3FnWQTMo9s
author: Max Hay
ingested: 2026-08-09
blender_version: "not specified on screen"
tags: [lighting, environment-lighting, hdri, sun-light, spot-light, area-light, volume-scatter, golden-hour, overcast, world-shader, composition, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/how-to-get-good-lighting-in-blender/
frame_count: 13
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How to get good lighting in blender

**Source:** [YouTube](https://www.youtube.com/watch?v=c3FnWQTMo9s)
**Author:** Max Hay
**Duration:** 27m52s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Okay, so let's talk about lighting. So in this video, I'm going to show you how to get really good lighting in Blender, specifically for environments.
[0:06] One thing I'm going to be doing in this one, which I think you'll find the most useful, is taking just a basic scene and lighting that in three or four different ways.
[0:13] And each way is going to look good, but I'll just show you the kind of the exact setup that I'm using and just some different examples of lighting conditions and how that can really make it into a completely different image,
[0:23] even though the scene is the same the whole way through.
[0:25] And then also just give you some general tips that really have helped me get better lighting, all that kind of stuff, just to make it as easy as it possibly can be.
[0:32] Okay, so I think just the best thing to start with is an example. Let's just jump in here. I have this basic scene set up here.
[0:39] If I just go to rendered view, let's just take a look at what we've got here.
[0:42] So right now there's basically no lighting or just background basic lighting, just the background default thing here with the strength on one.
[0:50] So just pure white or gray all around.
[0:53] It's just I just dropped in a bunch of rocks and trees and stuff from Quixel Megascans and these trees are from Botanic.
[0:59] And then I modeled this little thing here a while ago.
[1:02] So this is horrendous right now, just terrible, terrible lighting.
[1:06] The reason this is so bad is because there's no shadows right now, right?
[1:11] So we have this white void, which is just casting equal light from every single direction.
[1:17] That means that there's almost no shadows and it just when you have almost no shadows like that, it's going to create an extremely boring image.
[1:24] So we need to fix that.
[1:26] So step one is the procedure basically that I follow.
[1:29] Any time I'm going to light a scene is first of all, turn off every single light in the entire scene.
[1:36] So I'm going to unplug the background.
[1:37] If, if, for example, there are any point lights, like random little lights in here, even if it's dim,
[1:43] I'm going to just turn those off like fully just turn everything off.
[1:46] You want pitch black to start with and that's just going to simplify it as much as possible.
[1:50] OK, so let's start with the most basic example, which is just a sunny day.
[1:54] Let's just start with that.
[1:54] So I have this HDRI here.
[1:56] Just reset the rotation and let's plug that into the surface of the world.
[2:01] So I'm just in the shader editor in the world settings and I'm just plugging in an HDRI.
[2:05] I'm going to assume you know what that is.
[2:07] If you don't just Google Blender HDRI, it's basically just an image,
[2:11] which is going to light up our scene like this, right?
[2:14] So this is we have at least some light in here now.
[2:19] So it's better than before and we have at least some shadows, but this can be a lot better.
[2:25] So first of all, I don't really like where the sun is positioned right now.
[2:27] If we kind of look at this, the sun is kind of behind or off to the side, kind of behind the camera, a weird angle right now.
[2:34] What that's doing is I mentioned before, there were no shadows when we had that just background in here.
[2:40] Now there's some shadows, but the sun is at such an angle that it's kind of hiding a lot of the shadows,
[2:46] particularly on this left side here.
[2:48] If you look over here, there's still barely any shadows in here, right?
[2:51] And you generally want to avoid that when you're lighting with a sun or anything, any kind of light,
[2:55] you want to avoid lighting it from the same perspective as the camera,
[2:59] because that's just going to mean that the shadows are falling behind all the objects to where you can't see them,
[3:05] which basically still means there's no shadows.
[3:09] What that's going to do is it's going to flatten everything out.
[3:11] It's going to make it really hard to determine the form of any of the objects in the scene,
[3:15] and it's going to kind of flatten out all the detail.
[3:18] It just doesn't make it look nice and interesting, and it doesn't bring out the best in our environment.
[3:23] So what I want to do is just adjust the rotation slider.
[3:25] Any HDRI was going to come with a rotation slider.
[3:27] If it doesn't, like if you just have a thing like this, it's going to be the environment texture.
[3:32] I think it's even called that.
[3:33] Yeah, sorry, this one.
[3:35] I'm just going to just hit Ctrl T, and that'll just bring up this thing here,
[3:38] and then you get the rotation right here.
[3:39] You just want to adjust the Zed rotation, and it'll do the same thing.
[3:43] Okay, so Zed rotation, I'm just going to adjust this, and I'm just going to start moving it along.
[3:48] I'm just going to rotate this until I like the spot that it's at.
[3:52] So you can see I'm going to move this, not worrying too much about the background image
[3:56] as so much as I am the light direction and the shadows that it's creating.
[4:00] So I'm going to keep rotating this.
[4:02] So it's starting to look a bit better, a bit better, not quite where I want it.
[4:06] I don't really like exactly where it's at right now.
[4:08] Something like this could work.
[4:10] It's a little bit too silhouette-y because right now the sun is kind of right in front of the camera,
[4:17] which could work, but it's going to create like a silhouette on our objects here.
[4:21] So I don't really want that in this scene.
[4:23] So let's keep going.
[4:24] Let's keep going.
[4:26] Like sometimes I'll spin this all the way fully around and not even be happy with it,
[4:29] and then pick a different one.
[4:30] Let's keep going here.
[4:32] I think right around here, I'm going to stop.
[4:35] So right around there, I kind of like this right here.
[4:38] So now we've got much more interesting shadows.
[4:40] And notice that the sun is coming from the side right here.
[4:43] So the camera is kind of over here by these two rocks.
[4:46] That's the thing you were just seeing.
[4:48] And then the sun is kind of positioned off to kind of the side like that.
[4:54] And what that's going to do is it's going to create very pleasing shadows on everything,
[4:58] including like the main thing here.
[4:59] We're getting a light hitting one side shadow on the opposite side.
[5:03] I've kind of rotated it to be facing that direction anyways,
[5:06] because I kind of plan this out.
[5:07] But you know, even on all the rocks and stuff, we're getting nice, pleasant shadows.
[5:12] It's bringing out lots of detail in the environment and it's just making everything look nice
[5:17] and easy to understand and nice and just good to look at.
[5:20] Right.
[5:20] So you know, even on the tree and stuff, it's just creating a nice shadow and everything.
[5:26] So that's kind of the lighting setup that I'll usually use for a sunny day.
[5:30] It's just bring the sun literally off to the side, one side or the other.
[5:33] It doesn't matter which side.
[5:35] You could go the other way if you want to from coming from the other side.
[5:37] But in this case, I felt like the left side is nicer.
[5:40] One thing I want to fix here, one problem is the foreground is now really, really bright, right?
[5:46] And that's maybe fine.
[5:47] It's not a problem, but I kind of like to minimize really bright foregrounds
[5:52] and kind of direct the light a little bit more intentionally.
[5:54] So one thing I'll do is maybe just take any random object.


### Shadows [5:55]
**Transcript (timestamped):**
[5:57] So I'll take a tree or just anything doesn't matter what it is.
[5:59] It could be just add a cube, do anything, take any object.
[6:03] I'll just duplicate this and let's just move that.
[6:06] I don't actually want to see it in the render.
[6:08] I just want to see the shadow only.
[6:10] I'm just going to position that kind of like over here somewhere and just kind of get that casting a bit more of a shadow in here.
[6:18] And I'm just going to bring that over this way and just try and minimize the really bright light in this part of the image.
[6:26] I don't really want too much attention to go towards.
[6:29] Okay, so that's kind of just darkening that there.
[6:32] If I just go and look at the before and after, you can see it's at the biggest difference ever.
[6:37] No, but it just helps kind of guide your attention to where I want it to go.
[6:39] Right.
[6:40] And I think it just makes it look better overall.
[6:42] You could do that even again with this rock here.
[6:44] This is not necessary, but you could do something like this, like take another little thing here.
[6:48] Position that right in the perfect spot to kind of darken that little rock if you want to.
[6:53] That's really not necessary.
[6:54] That's just personal choice at that point, but you can do stuff like that.
[6:58] So one thing I'll often do with really sunny renders like this is just throw objects off screen, but casting shadows onto the area you're capturing.
[7:08] And that's going to just create a lot more interesting shadows and you can reveal or show just specific parts of the image that you want to.
[7:17] And it's just going to create a much more pleasant thing to look at than just a default, you know, like weirdly rotated thing like this.
[7:23] Like it's just so much more harsh like this.
[7:25] I don't don't like this at all.
[7:26] This I'm actually quite happy with.
[7:28] One thing I would do at this point is bring in some volume metrics too.
[7:30] So anytime you see me bring in a volume thing like this, just so you know what this is is it's just a cube over the entire scene with a volume scatter node as the shader plugged into the volume output there.
[7:45] And then I've just gone into this tab right here down to viewport display and then display as bounds like that.


### Sunny day [7:51]
**Transcript (timestamped):**
[7:51] Okay, so I just have some, you know, basic minimal volume with a sunny day render like this.
[7:55] I generally keep the volume really low.
[7:59] You know, if you start cranking this up too much, it's going to look just weird and like overly foggy for no reason.
[8:04] You don't really see that on a sunny day that often.
[8:06] And this makes it look like, you know, wildfire smoke or something.
[8:08] I just don't really want that look right now.
[8:10] So minimal volume on a sunny day generally looks best.
[8:13] And then yeah, you could also at this point put a sky image plan in the background.
[8:17] If you're not happy with how the HDRI background looks, that's something I'll do a lot.
[8:21] In this case, it kind of works.
[8:23] But yeah, that's that's my setup for sunny day renders.
[8:26] Okay, and you can see here that this really doesn't have to be overly complicated with tons of different lights everywhere.
[8:30] This is literally just one HDRI and nothing else just casting some shadows and some errors I don't like.
[8:35] And that's it, right?
[8:36] Very simple setup, but very effective.
[8:38] Let's take a look at another example.
[8:39] So something you'll see often is like a, you know, golden hour shot.
[8:43] So this is like sunrise or sunset.
[8:46] So let's just try and make something like that.
[8:48] So again, step one, remove all lights.
[8:50] Anytime we're going to switch up the lighting, take off all lights first.
[8:55] In this case, there's just one HDRI.
[8:56] So that's easy.
[8:58] And what I'm going to do is add, let's just add a light in here.
[9:01] I'll add a sun lamp.
[9:04] So you could do this with an HDRI again as well.
[9:06] That's another option.
[9:07] You could do it with a sky texture or you could do it with a sun lamp like I'm showing here.
[9:11] You could even do it with like a spotlight or something like that, though you have to be careful with that because it's going to,
[9:17] it's a lot easier to make it look unrealistic and weird if you do that, but it can work and I do it sometimes.
[9:23] Let's just keep it simple here with the sun lamp though.
[9:26] I'm going to make the strength a lot higher and then I'm just going to rotate the sun sort of at a similar angle, but maybe a more extreme angle, right?
[9:32] So instead of, instead of being like at a 45 degree angle, like midday, I'm going to do almost like a sunset, fairly low angle like this, right?
[9:41] And I'm going to make the color a bit more orange like this here.
[9:46] So we'll just do that there.
[9:47] Maybe a little bit more yellowy.
[9:50] Yeah, it looks good right there.
[9:52] Let's make the strength even, well, I'll leave it at 10 for now actually.
[9:56] Okay, so that's doing that.
[9:57] Obviously way too much contrast and way too much shadow in here.
[10:00] So we got to deal with that.


### Adding volume [10:01]
**Transcript (timestamped):**
[10:01] The first thing I might do is actually add a bit of volume.
[10:03] So I'm just going to add a cube scale up this cube kind of over everything in the scene, cover up the camera, get past there.
[10:11] Let's just get that kind of a little bit bigger in here.
[10:14] Okay, and then I'm going to go to the object shader editor settings over here, hit new and then just delete.
[10:21] Sorry, delete the principle to add a volume scatter, plug that into the volume density, lower it way down and then anisotropy.
[10:28] I'm going to turn that up a little bit as well.
[10:30] Just kind of you can see what that's doing is kind of shifting it a little bit more towards where the light source is coming from.
[10:35] So I kind of like doing that.
[10:37] Getting kind of a weird line in here.
[10:39] So I'm going to make the volume a little bit taller to soften that out a little bit if I can and maybe even bring it in a little bit more like this.
[10:48] Okay, so that is definitely helped, but the background is fully just blank and that's kind of a problem.
[10:53] So to deal with that, I'm actually going to bring in a sky.
[10:58] This right here, I'll just show you what this is if I should show this here.
[11:03] I'll give it a box in a second here, but what this is, this is just a image of a sky, just a picture of a sky that I took.
[11:12] If I just go here, if you've seen my sky tutorial, this is just that right there.
[11:16] So picture of a sky that I took on my iPhone, that's going into just a principle shader on.
[11:22] This is a regular just shift a plane, just that, just put the image into the shader editor, run it into the emission color, turn off the strength like five or 10 or something.
[11:33] And then I also like running it into the alpha.
[11:35] You could also do the emission strength and then use a math node and then like do it like that, switch just to multiply.
[11:41] That's another option.
[11:43] I just like doing it into the alpha.
[11:45] So that's that.
[11:47] And then that gives you kind of like this setup right here.
[11:50] Looks really nice in combination with like volume and a sun.


### Adding a plane [11:55]
**Transcript (timestamped):**
[11:55] Okay.
[11:56] One thing also to get this box out of the way, if you just go into that again, orange square tab view viewport display and then display as bounds.
[12:03] That'll just get that out of the way there.
[12:06] Okay.
[12:06] So let's bring that in here.
[12:08] So I'm just basically when you add that plane, you just move it kind of in the background.
[12:13] You want to line it up so it's covering like you can see where the camera view is.
[12:18] You want this to extend just a little bit past the camera view.
[12:20] And then obviously you don't want it to be like cut off or anything like that.
[12:26] You don't want the top to be like you cut off in the reflection or anything like that.
[12:30] Like just use common sense with this.
[12:31] Obviously one important note here, if you're going to use an image to light the background or just have something in the background.
[12:41] You want the direction of light in the image to match the direction of light in the scene.
[12:46] So the default direction of light in this image is actually if I scale it this way is actually incorrect.
[12:52] You see that?
[12:53] So the sun is actually coming from the right side of the picture shining from the right side, right?
[12:59] And in my render, the sun is shining from the left side.
[13:02] So there's a mismatch and that is going to instantly just ruin everything.
[13:07] It just makes it look super unrealistic.
[13:08] It's a dead giveaway that it's 3D.
[13:10] Just don't do that.
[13:12] So always be mindful of the direction of light that the sun is coming from in the picture you're using if you're going to do this method and match it up accordingly.
[13:19] So I'm just going to scale this by negative one on the x axis so that the direction of light in the picture matches the direction of light in the scene.
[13:27] And then it'll look much more realistic.
[13:29] Okay.
[13:29] And then you just adjust the strength as you need to.
[13:31] You can kind of go for any look you want here.
[13:34] I think maybe a little bit lower looks kind of good on here.
[13:36] I'll make the base color of this a little bit darker as well.
[13:39] And that's that's completely another lighting setup that could work really well here.
[13:42] And then you would just adjust this sun accordingly.
[13:45] You can rotate it.
[13:46] You know, you have some freedom to rotate this back and forth a little bit.
[13:48] There's a lot of like room to customize this exactly how you'd want.
[13:54] But you can see that like pretty much anything you do here is going to look nice, you know, as long as you don't do this, or again, you're lighting it from the same direction as the camera and just flattening out the whole image, getting rid of all the shadows.
[14:05] Look, this can work, but I'm just going to tell you if you're a beginner, just try and avoid this because you'll probably just mess it up.
[14:13] If I'm being honest, and it's just a lot easier to get really nice results by having the sun off to one side or the other.
[14:19] Not to say you should never try letting it from behind.
[14:22] It can work, but it's just an exception to the rule and you just have to be careful with it.


### Different lighting setups [14:26]
**Transcript (timestamped):**
[14:26] It's all.
[14:27] Okay, so that's like golden hour setup quite similar to the other one.
[14:29] Again, you could just do it with an HGRI as well.
[14:31] And you can mix and match these different methods I'm showing here with any kind of lighting setup.
[14:36] I'm just going to show you what I think works best for me and what is easiest.
[14:39] So yeah, that's that there.
[14:40] Let's move on to the next one though.
[14:41] So again, I'm just going to disable or start turning off all lights here.
[14:44] By the way, one thing you'll one thing I'll actually do quite often in a render is when I'm when I'm stuck on a render or when I'm stuck on the lighting and I don't know if it's good or not.
[14:54] And I want to try some other options.
[14:55] I'll just select all the light sources.
[14:57] So the sun lamp and the background hit M.
[15:00] Let me turn on screen caskeys so you can see when I'm pressing hit M to move to new collection.
[15:07] Just call this like lighting or like all the whatever lighting setup you want name doesn't matter create.
[15:16] And then what I'll do is just hide or disable the collection and then it'll be pitch black because all your lights are going to be in there.
[15:22] You can try out other lighting setups like add, you know, whatever mess around completely just go crazy.
[15:27] Not worry about messing anything up.
[15:29] And then if you decide, no, I don't like this.
[15:30] I want to go back to the other one.
[15:32] You just hide that thing, go back to the golden hour or whatever collection you added and it's right back there.
[15:36] Right.
[15:36] So that system right there just adding it to a collection and hiding it and then trying other stuff in a different collection makes it super easy to just try a bunch of different lighting setups and find the one that's going to work best for the scene.
[15:45] Okay, so let's hide all the lights again.
[15:47] We want pitch black and let's do the next lighting setup.
[15:50] So I'm going to do a like really dramatic kind of a bit more artsy kind of lighting setup.
[15:55] It's not really realistic, but it looks kind of cool and it's something I do a lot.
[15:58] So okay, so for this lighting setup here, I'm just going to add a spotlight.
[16:02] So as I mentioned, this is going to be less of a realistic lighting setup and more of just a cool dramatic lighting setup.
[16:08] So that's what we're doing here.
[16:11] So I'm going to add a spotlight in here.
[16:13] Let's turn up the power.
[16:15] So just pick a bright number.
[16:17] It doesn't matter what it is.
[16:20] And then I'm going to rotate this kind of like this direction and move it off the side like this.
[16:24] I'm going to increase the radius.
[16:26] What that's going to do is that's actually the size of the actual light itself.
[16:30] So if I turn that up, it's going to make a softer light.
[16:33] And what I mean by softness, if you just look at some of the shadows here.
[16:36] So for example, the shadows on this pillar here, if I turn the radius to its default setting of zero,
[16:43] that is going to create just extremely hard shadows.
[16:46] Like even if I zoom 100% fully into the shadow here, it's a fully just super sharp line, tack sharp line.
[16:55] That's because the size of the light is literally set to zero, which is impossible.
[17:00] And it's like no light sources fully zero.
[17:03] But anyways, let's increase that a little bit.
[17:05] So you can see as I as I start increasing this radius of this light,
[17:09] it's going to soften out those shadows a little bit.
[17:11] And that's going to happen across the entire environment all at once.
[17:14] And the higher you make that, the more soft it's going to be.
[17:17] So don't don't go too extreme.
[17:18] Like this is way too much, but you know, a little bit more soft is going to be probably more desirable.
[17:24] And then I'm going to have that kind of over there.
[17:27] Let's just increase the spot size a little bit.
[17:29] It's a little too like spotlighty like that's a little too dramatic there.
[17:34] I'm going to increase that a bit.
[17:35] Let's increase the blend as well.
[17:36] That's just the gradient fall off from the edges kind of.
[17:40] So I'll just increase that maybe bring up the spot size a little bit more.
[17:43] It's probably a bit too much there.
[17:45] So I'll dial it back to like there.
[17:48] And that's kind of interesting right there.
[17:49] So I'll leave that there.
[17:52] Okay.
[17:53] One other thing I might do is add in.
[17:55] I'm kind of happy with how this lights positioned on the main thing here, but it's too dark in the shadows.
[18:01] Right.
[18:01] It's just not enough light in the rest of the scene.
[18:04] What I'll do from here is add a fill light.
[18:05] So I'll just add an area light and I'll just bring that up kind of up here.
[18:10] Bring it sort of towards the dark area and then I'll just start increasing that a little bit.
[18:15] Right.
[18:15] I don't want to go too extreme and start just lighting up everything way too much.
[18:20] It's not what I want at all.
[18:21] I want to just bring it in a little bit to slightly raise some of those really, really pitch black areas just a little bit.
[18:27] So you can see a bit of detail in there.
[18:29] Right.
[18:29] So that's really nice right there.
[18:30] And that looks so much nicer and more professional than it was two seconds ago with just overly dramatic, overly dark, you know, whatever.
[18:38] You can still have a dark and dramatic, but if you just add a little bit just and I mean a little bit of light to the shadows, like the really dark shadows.
[18:45] You can just help bring that up and not make it feel so like extreme and like way too high contrast.
[18:52] So I'm going to increase the size of this a little bit.
[18:54] Maybe move it a bit further over here.
[18:56] Just try some different positions, but kind of like where it's at right there.
[19:00] We could even make this, you know, tinted a bit like blue or something if you want to kind of represent out of the moonlight or something.
[19:06] So one thing that is helpful, by the way, is kind of thinking about anytime you're lighting a scene like this in a more abstract way.
[19:13] Think about the kind of light that you're simulating by having a spotlight in here.
[19:18] So this is obviously not realistic, you know, for an environment that would never be a spotlight like this randomly up here.
[19:24] But what we're doing is we're kind of mimicking, you know, a really dramatic moonlight or something like that, for example.
[19:33] And if you think about the thing that you're trying to mimic, the real life version of that thing that you're trying to mimic, whether it's car headlights,
[19:39] whether it's a neon sign or a sun or the moon or whatever, just thinking about the thing you're trying to mimic will really help you in the decision to make with that light
[19:48] and just the way you position it, the colors you choose, the brightness, all that kind of stuff will help just ground it and make it feel a little bit more real and like something that could actually exist.
[19:58] Even if it is kind of abstract like this.
[20:00] Okay, so that's another setup.
[20:03] And again, I'm going to bring in that image plane from before.
[20:06] So I might actually just might actually just do this spring in the sky from before.
[20:13] So this is something that can work really well as well.
[20:16] It's just this kind of setup.
[20:18] And then you just throw any sky image in the back could be something more dramatic than this.
[20:22] Like if I bring in something more overcast, that might be nicer.
[20:25] So let's just do like this one.
[20:28] You know, something like that is probably going to work better.
[20:30] If I have that kind of like more like this, you know, a more overcast, moody sky would probably work better, you know, and that can work really well in combination with a really dramatic light.
[20:47] So that's something I'll do very often actually is it's kind of set up here.
[20:50] So notice the way I added that to I added one light at a time.
[20:54] So I had one light got it to the position I was happy with then and only then brought in the next light.
[21:00] I brought that to fix the problems in the scene that the first light couldn't handle, then bring in the next light.
[21:05] Okay, in this case, the background to fill in the final problem.
[21:08] And it's like just step by step.
[21:10] If you build it that way, you're not going to run into any of these many issues.
[21:14] If you try and add like three different lights at once and you try to manage all that simultaneously, that's where it becomes just impossible and like way too much to manage.
[21:22] And then you run into like conflicts in the lights and they're just interfering with each other in weird ways.
[21:27] You just add it one at a time at one, like start with pitch black, add one, get it right.
[21:32] Once it's right, then add another light only if necessary, right?
[21:36] Just as I did here.
[21:37] Okay, so that's out there and that works really well.


### Moody lighting setup [21:38]
**Transcript (timestamped):**
[21:39] So very simple, very effective spotlight area light to bring up the shadows a little bit and then a background sky.
[21:46] That's it, you know, let's move to one more lighting setup, which is just a moody, overcast sky.
[21:55] This is actually something I don't do very often, but it can look really nice and you can do it if you want.
[22:00] And it's, you know, something you'll see in real life looks really good in photos and here's how you do it.
[22:05] So let me just take off everything.
[22:08] We'll just start from scratch.
[22:09] One way you can do it is drop in a cloudy, overcast HDRI.
[22:15] That's one way.
[22:15] I don't really like doing that.
[22:16] I kind of like bringing in a sky image first.
[22:21] So for just a moody, overcast, like overcast sky render, I would actually bring in the background of a sky like this.
[22:29] And then what I'll do also is just add some volume.
[22:31] So again, shift a cube over the whole thing, go to the object settings, just create a new shader here, delete this volume scatter,
[22:40] plug that into the volume density, want to lower that down.
[22:44] Let's we can actually use higher density on this because it's going to be like a foggy day or something.
[22:48] So I'll bring that up a little bit.
[22:50] One thing I might also do is increase the number of volume light bounces in the light paths.
[22:56] So we'll just increase that increase the anisotropy a little bit to make a little more cinematic feeling.
[23:01] Display as bounds and out of the way.
[23:05] So this is overly, overly like dark and moody.
[23:08] The only light is coming from the background sky, right?
[23:10] So I want a little bit of light coming from like an actual light source.
[23:13] So I'm going to add going to add an area light in here and let's just bring that up here.
[23:17] Let's just add something with like a basic amount of strength, not too much.
[23:21] I'll increase the size as well.
[23:23] And I'll just kind of bring that up kind of over everything.
[23:27] So in an overcast sky scene, you would actually get more of like the lighting set up at the beginning where it's just, you know, a background going in like this and light coming from every single direction.
[23:39] That's technically more realistic than what I'm doing here.
[23:43] But it's not going to look as nice as if you have a little bit more controlled like this.
[23:51] One thing you can do if if if you do want to use like an HDRI setup like this or a background setup where it is just an actual like white kind of environment around everything is you could just very intentionally control where the shadows are landing by adding like something like this, like just a cube in the scene.
[24:09] Scale that up.
[24:11] I'll just put it kind of behind the camera.
[24:13] Let's go to the object settings, make a new material and then just make the color fully black.
[24:19] So what that's going to do is it's going to absorb light from behind the camera.
[24:22] It's going to limit how much the background sky is actually emitting light from that direction.
[24:27] So if I look behind here, you can see with this giant kind of blocker thing here.
[24:33] This is all the light that would normally be coming in and we just put up a big like black wall to just not have any of that coming through there.
[24:41] And you could even do this is something that sweeper 3D will do a lot.
[24:44] You kind of delete this face and then you can just put this box even more like over the this foreground area that you're trying to capture.
[24:54] Now really make the lighting just more dramatic overall, even though it's just a basic background.
[25:00] So that can be really, really fun to do.
[25:01] Obviously, you don't have this visible in the camera.
[25:04] Don't go too extreme with it.
[25:05] It looks bad too extreme, but like a little bit of that looks really nice.
[25:08] I think so it's just about controlling where the light is going to end up and not having it show up in like every single area.
[25:16] Doing this is creating some nice kind of we're actually getting some nice shadows and like interesting, you know, just interesting details on there from that kind of big box thing that we're doing there.
[25:26] So this is a just a cool technique you can do sometimes when you're doing an overcast render or even a sunny render.
[25:35] You can do this too.
[25:35] Again, you can mix and match these techniques, but it works particularly well for here and that's just going to help control things a lot more.
[25:43] Like, you know, you could see the difference there and how much better it makes it look if you just have some something blocking the light in the immediate foreground there.
[25:51] And then you can be a little bit more controlled as well with like you can add an area light in here, make it like fairly strong, not that strong.
[26:01] Just take one digit out there, make it big and then kind of have this coming from wherever you can have like a little bit of directional lighting if you want or not.
[26:10] Really just depends on the look and mood you want to go for.
[26:14] One thing I'd recommend also is just use reference images.
[26:18] So don't just try and wing it on your memory like I'm literally doing in this video.
[26:23] Actually, don't actually don't recommend you do that.
[26:25] I recommend if you want to go for a moody overcast render, go online and look at a bunch of pictures of like moody overcast scenes, photographs, shots from movies, drawings, whatever renders doesn't matter.
[26:38] And look at the techniques that they're doing to manage the light and find some images you like and try and base it a little bit closer to that rather than just like going off memory is what I'd recommend.
[26:48] Same thing for like if you're going for a sunny day, find pictures of a sunny day and look at some of the techniques and use that for inspiration.
[26:53] And that'll really help you just to get much better lighting setups.
[26:57] Okay, so I think that's it for the examples for environments.
[26:59] There's a bunch more like there's a bunch more lighting setups we can do.
[27:03] There's interior lighting setups.
[27:04] There's like cyberpunk neon lighting setups.
[27:06] There's a whole bunch of different things you can do, but hopefully this gives you just a general, you know, introduction or just a general overview of how you can take a really basic scene and make it look nice in a bunch of different ways.
[27:19] And just, you know, some techniques to manage all that for like outdoor basic environment lighting.
[27:22] So don't feel restricted to any of the examples I showed here.
[27:25] You can do like any, any type of lighting you can do in blender.
[27:30] You just have to know how to do it.
[27:31] And yeah, so don't feel like you have to follow this very strictly or anything like that.
[27:37] This is just, I meant to show you just cool examples here of stuff you can try out if you want.
[27:41] And yeah, so I might do a part two or more like advanced section on this.
[27:46] If I should do that, maybe I don't leave a comment or something letting me know.
[27:49] But yeah, that's it for this one.
[27:50] Thanks for watching and see ya.



---

## Captured Frames

- [4:38] tutorials/frames/how-to-get-good-lighting-in-blender/frame_000.jpg
- [6:32] tutorials/frames/how-to-get-good-lighting-in-blender/frame_001.jpg
- [7:55] tutorials/frames/how-to-get-good-lighting-in-blender/frame_002.jpg
- [9:52] tutorials/frames/how-to-get-good-lighting-in-blender/frame_003.jpg
- [10:35] tutorials/frames/how-to-get-good-lighting-in-blender/frame_004.jpg
- [13:19] tutorials/frames/how-to-get-good-lighting-in-blender/frame_005.jpg
- [16:46] tutorials/frames/how-to-get-good-lighting-in-blender/frame_006.jpg
- [17:09] tutorials/frames/how-to-get-good-lighting-in-blender/frame_007.jpg
- [18:29] tutorials/frames/how-to-get-good-lighting-in-blender/frame_008.jpg
- [20:28] tutorials/frames/how-to-get-good-lighting-in-blender/frame_009.jpg
- [23:08] tutorials/frames/how-to-get-good-lighting-in-blender/frame_010.jpg
- [24:33] tutorials/frames/how-to-get-good-lighting-in-blender/frame_011.jpg
- [25:16] tutorials/frames/how-to-get-good-lighting-in-blender/frame_012.jpg

---

## Structured Notes

### Core Technique
A general-purpose environment-lighting methodology (not tied to one node setup): always start pitch black by disabling every light, then add exactly one light source at a time, positioned so it casts *visible, directional* shadows rather than lighting from the camera's own direction (which flattens form and kills shadow visibility) — demonstrated by relighting one static rock/tree/pagoda scene four different ways (sunny day, golden hour, dramatic/moody spotlight, overcast).

### Summary
Opens by showing the default "no lighting" state (flat gray World background at strength 1) as a deliberately bad example — no shadow direction, no form definition. The recurring workflow for every subsequent setup: disable/hide all existing lights first (grouped into a Collection via `M → New Collection` so whole lighting rigs can be toggled and swapped without deleting work), then build up one light at a time, checking the result before adding the next. **Sunny day:** a single HDRI plugged into the World surface, rotated (via the rotation slider, or `Ctrl+T` on an Environment Texture node for the mapping/rotation inputs) until the sun sits off to one side of the camera rather than behind or in front of it — front/behind lighting flattens shadows into invisibility or creates unwanted silhouettes. A duplicated, render-hidden copy of scene geometry can be repositioned purely to cast an extra shadow into an overly bright foreground area, directing viewer attention without a real light. A large, low-density Volume Scatter cube (added over the whole scene, "Display As" set to Bounds to hide the box outline) adds atmospheric depth; kept very low for sunny scenes to avoid an unintended "wildfire smoke" look. **Golden hour:** disable the HDRI, add a Sun lamp at a low/steep angle with a warm orange-yellow tint and boosted strength; add volume (Volume Scatter, low density, Anisotropy raised to bias scattering toward the light source) and composite a real sky photo on a background plane (image → Emission, strength ~5-10, routed into Alpha instead of multiplying emission strength) as a backdrop when the HDRI sky doesn't read well. Critical gotcha: the photo's own light direction must match the scene's key light direction (flip the plane's X scale by -1 if needed) — a mismatched sky-photo light direction is called out as an instant, unmistakable giveaway that a shot is 3D. **Dramatic/moody spotlight (stylized, not realistic):** a Spot light with Radius at its literal-zero default produces perfectly hard-edged shadows (unrealistic — real lights are never a true point source); raising Radius softens shadow edges scene-wide, and Spot Size / Blend shape the cone's falloff. Once the key spotlight is positioned, an Area light is added purely as a fill to lift (not eliminate) the darkest shadow areas — enough to reveal detail without flattening the drama — optionally tinted (e.g. blue for a moonlight feel). The presenter frames this as "think about what real light source you're mimicking" (headlights, neon, moonlight) even when the actual light rig used is not physically plausible. **Overcast/moody sky:** background sky-plane photo (overcast reference) + denser Volume Scatter (raised Volume Bounces in Light Paths, Anisotropy raised for a moodier falloff) + a single soft Area light for minimal fill, since pure ambient-only lighting (light from literally every direction, e.g. straight HDRI/white-background) is technically closer to real overcast conditions but reads as flat and boring on camera. A notable control trick for any all-directional/HDRI-style setup: place a large, fully black-material cube just outside camera view (e.g. behind the camera) to physically block/absorb ambient light from that direction, which lets an otherwise shadowless ambient setup produce controlled, directional-feeling shadows and highlights — a technique the presenter attributes to common practice in "sweeper 3D"-style production work. Closing advice: build lighting incrementally (one light, get it right, only then add the next — simultaneous multi-light setups are called out as much harder to debug/manage) and always work from real photo/film reference rather than "from memory."

### Key Steps
1. Disable/remove every existing light in the scene (HDRI, point lights, anything) — start from pitch black every time you're testing a new lighting direction.
2. **Sunny day:** plug an HDRI into the World shader's Background node → rotate it (rotation slider, or add/adjust the Mapping node feeding the Environment Texture, `Ctrl+T` shortcut to spawn one) until the sun key-lights the scene from one side, not from behind/in front of the camera.
3. Optional: duplicate scene geometry, hide it from render, reposition purely to cast a shadow into an overly bright area to redirect attention.
4. Add a large Volume Scatter cube over the whole scene (new material → delete Principled BSDF → add Volume Scatter → plug into Volume output; object's Viewport Display → "Display As: Bounds" to hide the box); keep density very low for sunny scenes.
5. **Golden hour:** disable HDRI; add a Sun lamp; raise strength; rotate to a low, steep angle; tint the color warm orange/yellow; add the same low-density Volume Scatter setup but raise Anisotropy to bias scattering toward the sun.
6. Add a background image plane: `Shift+A` plane → new Principled/Emission-based material → plug the sky photo into Emission Color, set Emission Strength low (5-10) and route the image into the Alpha socket (alternative: multiply emission strength via a Math node) → position behind/around the scene, extending slightly past the camera frustum.
7. Verify the sky photo's light direction matches the scene's sun direction; if mismatched, scale the plane by -1 on X to flip it horizontally.
8. **Dramatic/spotlight look:** disable prior lights (or move them to a hidden Collection via `M`); add a Spot light; raise Power; position/rotate off to one side; raise Radius from 0 to soften hard shadow edges; tune Spot Size and Blend for the cone falloff.
9. Add an Area light as fill only, positioned toward the darkest shadow region, raised just enough to reveal shadow detail without eliminating contrast; optionally tint for mood (e.g. blue for moonlight).
10. Optionally add the same background sky-plane technique, swapping in a moodier/more overcast reference photo.
11. **Overcast/moody:** background sky-plane (overcast photo) + denser Volume Scatter (raise Light Paths → Volume Bounces, raise Anisotropy) + one soft Area light as minimal fill.
12. Controlled-ambient trick: add a large cube just outside the camera's view, give it a fully black material, and use it to block ambient/HDRI light from that direction — turns an otherwise flat all-directional light setup into something with more controlled, directional shadows.
13. Build every setup by adding exactly one light, dialing it in, then adding the next only if the scene still has an unsolved problem — never all lights simultaneously.
14. Use real photo/film reference for the target mood (sunny, golden hour, overcast, dramatic) instead of working from memory.

### Nodes / Settings
World Background (HDRI + rotation), Environment Texture + Mapping node (`Ctrl+T`), Sun light (strength, angle, color), Spot light (Power, Radius, Spot Size, Blend), Area light (as fill), Volume Scatter shader (Density, Anisotropy) on a bounding cube (Viewport Display → Display As: Bounds), background image plane (Emission Color/Strength routed to Alpha), Light Paths → Volume Bounces, Collections (`M`) for swappable/hideable lighting rigs, fully-black-material blocker geometry for controlled ambient occlusion of a light direction.

### Difficulty
Beginner-to-intermediate — no complex node graphs beyond a basic Volume Scatter/emission-plane setup; the real content is compositional/artistic judgment (light direction vs. camera direction, incremental light-by-light building, reference-driven decision making) rather than technical complexity.

### Blender Version
Not stated on screen or in narration.

### Tags
lighting, environment-lighting, hdri, sun-light, spot-light, area-light, volume-scatter, golden-hour, overcast, world-shader, composition, beginner, intermediate

---

## Related Tutorials
None yet — first general environment-lighting-methodology entry in this library. Cross-link future lighting-fundamentals or mood-lighting tutorials here.
