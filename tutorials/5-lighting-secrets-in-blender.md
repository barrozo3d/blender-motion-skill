---
title: 5 Lighting SECRETS in Blender
source: YouTube
url: https://www.youtube.com/watch?v=qQgK7gYbvco
author: Max Hay
ingested: 2026-07-19
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/5-lighting-secrets-in-blender/
frame_count: 0
frame_status: pending-selection
---

# 5 Lighting SECRETS in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=qQgK7gYbvco)
**Author:** Max Hay
**Duration:** 27m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py 5-lighting-secrets-in-blender <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] And this one I'm going to show you five more advanced lighting tricks in Blender that you probably didn't know.
[0:03] The first one is using image textures inside of the actual lights to create really interesting colors and highlights.
[0:09] I just got some crazy looking results with the lighting that you just wouldn't expect.
[0:13] The second one is using fake caustics, kind of a similar technique, but a different application of it.
[0:17] The third one is using lighting go bows to kind of save an otherwise boring and flat lighting situation.
[0:23] So I'll use this one. There's like, I like the lighting, but it's just too boring. I'll use this trick.
[0:27] It's really easy. And then the fourth one is using God rays and how to get that reliably to work every single time.
[0:33] And the fifth one is using the light fall off node to get actually a gradient fall off of a different color
[0:39] so that it could like start off as red and then fall off to blue as it moves further from the light.
[0:43] And I'll show you an example of how we use that in client work and an actual render.
[0:47] And I'll also show you like combining these different techniques in multiple different ways and how I'm doing that as well.
[0:52] So let's get started with number one. Yeah.
[0:56] Okay, so let's just get started on the first one. So this setup right here is what I want to talk about, which is
[1:02] but to sort of show you what's going on here. We have this very interesting sort of setup with kind of like
[1:09] it almost looks like something is refracting through something else and that's what's creating the lighting.
[1:14] What is going on here is it's just a spotlight with an image texture actually as the source of light.
[1:22] So I'll just show you what I mean here.
[1:24] So actually I took a picture just on my phone. There was some light
[1:29] the sun like coming through the door and it was hitting the wall next to it and creating this just interesting
[1:36] pattern on the wall. So I just took a picture of that and I'm actually running that
[1:41] through this light here. So the main one is just doing this where it's just kind of a
[1:46] or actually that's not even the main one. There's kind of a bunch of them stacked on top for each other.
[1:49] One is affecting the volume and one is not but you can see this creates a really
[1:54] interesting setup and you can actually just swap the image for a bunch of different things.
[1:57] So I was trying out a bunch of weird images.
[2:00] So like this is a random download from unsplash of just like this thing and you can see this can give you some really
[2:06] just crazy lighting if you
[2:10] throw the right image in here.
[2:12] So that's a bit too much. That's too extreme for what I want here, but I'm using the same technique with just something
[2:17] a bit more simple with you know, just a kind of nice refraction that's coming from the wall.
[2:21] Okay, I'll just I'll just show you how to set this up really quick in a new file.
[2:24] So I'll just add some objects in here just for quick demo scene.
[2:28] So I'll add a spotlight for this.
[2:30] It works with an area light and a point light too, but I'll just do with a spotlight and
[2:35] for the different light sources by the way, you might have to adjust the actual
[2:38] radius of the light to get it to work.
[2:39] So just be careful with that or the with an area light you have to adjust the
[2:44] Spread just be careful if you're gonna use that, but it's all kind of the same.
[2:47] So spotlight in just go to render view here
[2:50] Take the background way down and I'll just go to the object
[2:55] In the shader editor the object settings and then just for this light here
[2:59] We're in the shader editor. You just need to click this button up here use nodes. Click that now
[3:05] This emission node will actually affect the strength, but this one will affect the strength as well
[3:10] So if you adjust it over here, so I set this to whatever number
[3:13] That's that's actually one influence on the light same with the color. So if I make it a bit blue
[3:17] That's one influence this emission node kind of acts as a second influence
[3:21] So if I adjust the strength it adjusts it there as well
[3:24] And if I make the color like a different color, it's gonna also
[3:28] interact with it and they are both kind of fighting with each other
[3:31] So if I make both of them kind of extreme colors, they'll both kind of combine into one output
[3:35] So it's a bit weird, but it works
[3:38] So anyways, what I want to do here is just I'll keep those both on white
[3:43] I'll just go and find an image to drop in here
[3:47] So again, I just took this picture on my phone
[3:49] Oh, just some cool light coming through the door and then hitting the wall
[3:52] So I'll plug that image just drop it in there plug it into the color and you can see it's straight away working
[3:59] So you just have to kind of angle this how you'd want
[4:01] I'm gonna rotate this on the local Z
[4:04] So it's just our Z and then Z one more time so that this can spin kind of on its axis like this
[4:10] I'm gonna position it like that. Let's maybe just
[4:14] Bring up that strength a bit. So I'll just set this to bit higher. I
[4:18] Can also increase the radius of the light a little bit
[4:21] So I'm kind of getting the texture of the wall coming through
[4:24] So if I want to blur that a little bit
[4:25] I can just increase the radius of the light and that's probably gonna make it feel a bit more natural as well
[4:30] If you go too high that image won't be visible anymore, but just increasing that a little bit is probably a good idea
[4:35] and
[4:36] Then I can tint this whatever color I want so I want to make it like a bit blue and do that
[4:41] Maybe let's bring the radius back down a little bit there
[4:44] And then what I might want to do also is run the color of this into the strength of this node
[4:50] What that's gonna do is it's gonna make
[4:52] The strength actually lower in the darker areas and I can actually use like a color ramp or curves or something
[4:58] Sorry color ramp clicking the wrong thing. Okay color ramp in there and then I can adjust exactly where this falls off
[5:04] I probably want to set this to like ease or be spline just to get a smoother fall off
[5:10] But that works there. I could take a math node and multiply the strength
[5:15] Up here if I want to do that
[5:17] But yeah, that's the first set up for just some really interesting kind of textures
[5:21] You can get coming through there and then I'll just increase the blend a bit and then the spot size will kind of just do this
[5:27] so one thing I didn't mind is I just added a hue saturation value node increase the saturation on that and then
[5:33] just
[5:34] kind of
[5:36] Get that in combination with a different color here and balance it out
[5:39] And then you're kind of getting the rainbow kind of splitting happening there a bit more clearly
[5:43] So it's a really fun way to do this and then you can duplicate this as many times you need
[5:47] Rotated, you know different ways
[5:49] So I'll just kind of do that and you can get some pretty
[5:53] Interesting lighting like this and this also works for area lights or point lights
[5:56] So for example, if I just take this I can just switch it over to point
[6:00] And then if I just kind of have this in here, you can see from a point light
[6:04] It's actually doing the exact same thing and that can create some really
[6:09] Interesting results as well if you kind of have this in the middle one thing I'll do sometimes is put like a water
[6:13] image into this and that'll give you some
[6:16] caustics like fake looking caustics that you can just output from there and you can animate this with like a noise texture or
[6:22] Whatever, I have a video on that. I can link below so another video. I did on water a while ago
[6:27] But yeah, you can get some really crazy
[6:30] Just lighting like this and it usually works better in combination with something else
[6:34] So you might want to have something that's more normal and then kind of have this just in combination
[6:40] Somewhere else in the scene a bit lighter
[6:42] And then that it could just be like a nice complement to the actual lighting that you have
[6:47] That's a bit more, you know of a traditional normal setup with like a spotlight or something
[6:54] Same thing with an area light if I just point this down
[6:56] You do have to decrease the spread all the way down though
[6:59] So I'll just bring that to zero increase the size and then you can get the same exact sort of pattern here
[7:04] so yeah, that's the exact setup that I used in this one here and
[7:08] I just duplicated the light a couple more times, but it's the exact same setup. I just showed
[7:12] Here's another example. I use this technique in this one. It's actually the same image
[7:16] So if I hide the main light source, you can see that it's actually
[7:20] That same image is actually running in here covering the main light back in it's kind of making that a bit more subtle
[7:26] But it's the same thing running through there and then you can see there's that same image
[7:30] Kind of just creating some interesting highlights in the scene to making it a bit more interesting overall
[7:34] okay, the next technique is using lighting gobos which basically just means a
[7:39] some sort of surface that's
[7:41] Blocking some of the light to cast interesting shadows onto the scene
[7:45] So here's an example of that in this scene if you pay attention to the beams of light at the top
[7:50] We'll get to actual god rays later on but this is sort of
[7:54] Different method this stuff at the top the so the light is here, right?
[7:59] This is the light. There's basically just one main light. It's actually going through
[8:04] These two planes right here, which are actually have an image of like paint or something on there
[8:10] You can use the noise texture. I'll show you how to set this up in a second, but basically just some sort of plane with
[8:17] Some thing running into the alpha and that will create these really interesting
[8:23] Like shadow casting things which will then kind of like cast
[8:28] More beams of light down onto the scene and that's where if we look at this from the top down
[8:33] If I just hide these two planes instead of the whole thing just being fully
[8:38] Covered in the same neutral level of light all the way through when you do this and you create some interesting shadows
[8:44] We're blocking out some of the lights and like letting it through in
[8:48] Like bright little patches and it just creates more interesting looks sometimes
[8:52] So I don't always do this, but it's just a fun technique you can do sometimes to create just more cool lighting
[8:58] Especially if the lighting just feels off or boring
[9:01] Like I'm just not I'm happy with the direction in this case
[9:04] But it's just something is missing and it's just not quite ready or there
[9:08] So doing this is I feel like just making it more finalized and just cool
[9:14] So yeah, here's how to do this. I'll just show you how to set this up right now
[9:17] Okay, so with this method I'll use the spotlight as well
[9:19] Just for an example, but this works with anything to work with a sun lamp area light doesn't matter
[9:24] So we'll add a light spotlight just to make it easy go to my review and
[9:29] Take the background way down
[9:31] Let's make this a bit brighter. I guess a lot brighter
[9:35] And just kind of move it up so it's covering this sort of general area. Let's make it even brighter. Just like
[9:41] Whatever I'll make the radius a bit bigger than zero because we don't want a radius of zero meters
[9:48] That's impossible. So we'll just increase that a bit
[9:50] Increase the blend so it's a bit smoother and we'll just start with that
[9:54] Okay, so let's actually add a plane in here
[9:57] So shift a mesh plane and I want to just kind of bring this up and cover
[10:02] Where I want to cast a shadow over basically everything so wherever there's light
[10:07] I want to fully block it out with this plane
[10:11] So kind of like that and then on this plane
[10:13] I'm just gonna go to the shader editor object on the shader editor there and then we'll make a new material
[10:19] So basically what the alpha is gonna do is an alpha of if the alpha is at one, right? It's gonna be fully opaque just regular
[10:26] Not transparent at all as you'd lower this down
[10:29] It's gonna be more and more transparent all the way to where it's fully invisible at zero
[10:34] So what I want to do is take like a noise texture or an image texture or just something with variation
[10:40] And I want to I'm gonna plug that into the alpha
[10:44] Okay, so right away. It doesn't seem like it's doing that much and that's because this noise is really low contrast
[10:49] So if I take a color ramp and I just increase the contrast of this noise, then you'll start to see
[10:55] What we're gonna get some like patches of interesting light here
[10:58] So the first thing is we have to lower this down so that this becomes
[11:03] opaque enough that it actually starts casting some shadows below and
[11:08] We have to have it like this high enough so it's not just fully dark
[11:11] So just increasing the contract increasing the contrast like that is usually what I'll start with and
[11:16] Then I'll just usually increase the detail and roughness a little bit
[11:19] So now notice I want this to be a bit more harsh, but no matter how harsh I make this
[11:26] Plane here. It's still like really soft shadows down below
[11:30] so the distance of the light from the plane as well as the
[11:34] Radius of the light are both gonna have an effect on how crisp and sharp this is
[11:39] So you probably don't want it to be really really crisp and sharp
[11:44] Like hard light coming through this. It's just gonna look weird if you have this kind of setup
[11:50] Could be interesting in like an artistic abstract way
[11:53] But most of the time you'll want to increase the radius like the actual size of the light itself
[11:59] And that's gonna help soften out the shadows
[12:01] And you don't usually want to be able to tell what this
[12:06] Blocker is so sometimes you do if you want to use like an image of leaves or something or like an actual tree in there
[12:12] That can work
[12:13] But for just a situation like this where you just want some general kind of interesting shadows
[12:17] You probably want to keep it relatively soft and that'll lead to the most pleasing kind of natural-looking results
[12:23] Sometimes what I'll do as well is just take some weird image. I downloaded so like I'll take some image of tiles or something that I got from
[12:30] I think this is from unsplash, and I'll just drop that into the shader editor and plug that in to this
[12:36] Then you can do something like let's just unwrap the plane
[12:40] So just you unwrap cube projection and then we can just let's just do that again. So it does it properly
[12:47] You can kind of scale this to whatever and then I'll adjust the radius this light so that
[12:52] You can see if it's if it's zero. That's gonna be way too harsh interesting, but too harsh
[12:56] but you can get some really
[12:58] Like unique looking lighting if you kind of just throw in some random image this I wouldn't use
[13:03] Exactly how it is
[13:04] But just could be a good starting point for like getting some ideas for some interesting lighting
[13:08] one thing I will usually do is take this plane image and then just
[13:12] Shift select the light hit control P to parent it and then just choose object to keep transform
[13:17] So control P and then k for keep transform then when you move the light around it's just gonna that plane is gonna follow it
[13:24] So this could lead to some really interesting stuff like you know if you start making this weird colors and make it really bright or whatever like
[13:31] You could do some weird stuff with this
[13:33] And it doesn't have to be this extreme to like it can be a bit more soft
[13:37] But yeah, sometimes just throwing random images in here stuff that you wouldn't expect would work
[13:43] Sometimes it looks really cool
[13:45] So I'll just try like I don't know I think I have some like
[13:49] Patterns of us and like nature kind of stuff. I'll do like an image of ice or something
[13:54] Just just weird stuff that you would not expect or be able to really make on your own
[14:00] Sometimes looks really interesting
[14:02] So I don't know I can just give you some cool results that you wouldn't expect sometimes
[14:06] You can also combine this with the first technique if you want to use like an image in the actual light source itself
[14:12] So I could just drop in like this run that into here and then we're just gonna get some like really
[14:18] Ridiculous stuff going on. I don't even know what's happening here
[14:20] But you get the point right you could just combine this together and get some really interesting results
[14:24] And then that just kind of over the entire scene sometimes is enough to just make the lighting really interesting
[14:29] Okay, let's go to the next technique
[14:32] Okay, the next technique is God raise and I'll just show you how to set this up
[14:35] We'll use the same example demo file here the way the only thing you have to do differently here is just add some volume
[14:40] So if I just add a cube in here, and I'll show you the settings to make this sure this works every time
[14:45] Because sometimes people get confused with this
[14:47] So I'll add a cube over the entire scene delete the principal shader add a volume scatter node plug that to the volume
[14:55] Lower the density since it's just a brick right now. It's way too high
[14:58] So just lower that down to like point oh two point three somewhere around there to start and we have some volume now
[15:04] Okay, so the way this works is
[15:08] The way you get God raise is if you have a really hard light I'll explain what that means in a second going through a
[15:15] some sort of pattern or
[15:17] Getting cast through like leaves or something that's creating really harsh shadows
[15:22] Going through volume. So you need something that's first of all creating shadows
[15:26] So this technique works for that. So I'll just kind of ramp up the contrast of this to make this really really clear
[15:33] So that's the first thing and then the second thing is you need hard light and by hard light. I mean a small
[15:39] Light source that is not soft
[15:41] So a light source which is soft is going to be a big radius like this
[15:45] And that's going to create really soft shadows if you look at the cube the shadows are you know
[15:50] This would be like really hard shadows where it's a really defined line coming off this cube
[15:54] Really soft shadows are going to be more of a blurred line on there
[15:58] So you need hard light
[16:00] And that's just going to be a small radius on the light source just like that
[16:04] So it doesn't need to be zero, but it needs to be relatively small and that's how you're going to get
[16:09] this sort of effect there and
[16:11] Different blockers will kind of work better here. So if I choose like something else, it's probably gonna
[16:17] Give me a different or more interesting result
[16:20] Sometimes what I'll do as well is just throw a model of like a tree in here. So if I just spawn in some random
[16:27] Tree from Botanic, I'll just do like this or whatever. Let's delete that other plane. I'll just hide that for a sec
[16:35] And I'll just kind of block this with a tree and let's make this a bit brighter as well
[16:42] And
[16:44] You can see like something like this will give you
[16:47] Kind of a god ray setup and obviously you'll have to adjust the scale based on the scene
[16:52] But you can see you can very easily get a setup like this with just like a small light and then a tree or some
[16:59] image that's casting a shadow like some plane and that's gonna give you
[17:06] Like that'll give you god rays every time if you just have a small light source and then some sort of complex shadow
[17:11] Going through volume. That's how you do that
[17:13] If you don't see it like you're just not getting what you want
[17:17] Just try and reduce the radius of the light and the small you make it the closer you're gonna get to just like this
[17:22] You probably don't want to do zero like I said, because it's just too extreme, but somewhere on there is gonna be nice
[17:28] Okay, the next trick I want to show you is fake bounce lighting when there's just not enough of that happening naturally in the scene
[17:33] so you got to be careful with this because it can really make an
[17:37] Environment look unnatural because you're you're doing something that is not how light actually behaves here, but
[17:44] Let me just show you what I mean
[17:45] So in this case, I was happy with the lighting how it was here. The problem is I'm getting this really big
[17:53] section of really dark shadow, which I just thought was
[17:57] Overkill, but I didn't want to move the light around because I was happy with the rest of the lighting all around the scene
[18:02] It was just this one area
[18:03] I didn't like so what I did was I just added the point light in there
[18:06] Seems like it doesn't make a big difference, but when you render it out and you actually add post-processing it really does
[18:13] Enhance the vibe and really make it look quite a lot different
[18:17] And it brings out details that you wouldn't see like so we there's all these pillars and stuff in here that I'm just
[18:22] Brightening up a little bit with this fake bounce lighting. So what this is it's just a point light this I
[18:27] Happen to be using the nodes in here like the first technique
[18:30] You don't have to do that if you just use a regular default point light
[18:33] And it's really just not doing much in here anyways
[18:36] The key here is you want to have a large radius
[18:39] So it's fairly soft because what you're what you're simulating here, right?
[18:43] Is light coming from the main light source. So like this spotlight coming down hitting a surface
[18:48] So like the floor down here and then bouncing back up onto some other surface
[18:54] So it's kind of like you're simulating light bouncing off of like the floor and coming up hitting
[19:01] Some surface here, right? So
[19:04] What you want to do is
[19:05] Like the floor is essentially already acting kind of as a second light source where it's it's just kind of like a big
[19:14] Like I'll show you I mean here if I add a plane in here just a white plane
[19:19] This is actually acting as the same thing where it's just a big white surface
[19:24] It's gonna be reflecting tons of light off it and you can see on this thing here if I show and hide this plane
[19:29] It's it's reflecting light almost as if it was its own light source
[19:33] So that's actually happening already in the scene. It's just that these other objects aren't full of white and they're not really
[19:40] Balancing off that much light. So one thing you can do is actually just brighten up like the floor or something and that'll have the same effect
[19:46] But if you don't want to do that and you want to just fake it
[19:49] You could just add in a point light and just put it in or ordinary light to but just put it in the rough area
[19:56] Where there's already light bouncing off and the key here to making it not look fake and making it look real is you want to do
[20:03] It in an area where there is already a bunch of bounce lighting, but it's just maybe not enough
[20:08] So there's definitely some bounce lighting happening off of this floor down here. There's lots of light hitting this area
[20:14] So if I put a point light in that rough area
[20:17] Increase the radius so it's nice in a big soft light source just like the floor down here would be
[20:23] Then start increasing this then it'll feel a lot more natural
[20:29] Where this doesn't work is if you have it in an area that just makes no sense where there would be bounce lighting
[20:35] So if there wasn't a big patch of light here, or if this was like over here or something
[20:40] That's where you get that kind of fake
[20:42] Look where there's just a random light casting light out of nowhere with no apparent source
[20:47] That's where it gets weird and just bad and fake so avoid that
[20:52] The other thing is you probably want to color match this so I noticed that the light hitting the floor here is kind of like blue
[20:57] So I'm just gonna make the light a bit more kind of a blue ish greenish kind of color
[21:01] Not overkill like not too saturated, but just a little bit and then when I put that kind of in this rough area
[21:07] That looks fairly natural, you know and it helps bring helps bring out all those details in there
[21:12] Now one thing you can do if you're getting kind of like a glow from the volume
[21:16] If you're using volume metrics and it's just kind of glowing weirdly
[21:19] First of all turn off multiple importance if you're getting like weird reflections
[21:23] So that's the first thing the second thing is go into this orange square tab
[21:26] Go down to visibility and then array visibility down here turn off volume scatter for this light
[21:32] And that will make it so that it's not like if I make the radius really small here
[21:38] You'll probably let's see this better like you can see we're just getting this weird like
[21:42] glow
[21:43] From the volume. It's just like you just don't want that
[21:45] So I'm just gonna go in here turn off the volume scatter and then you just don't get any of that at all
[21:50] Make the radius a bit bigger and that's gonna be like the most natural way to include this in here
[21:54] This is too bright at a thousand usually I'll keep us at like a hundred ish
[21:59] just really really subtle and
[22:02] Usually less is more if you go too high, it's just gonna ruin it, but that can be really nice way to just add that kind of special
[22:09] Bounce lighting look to your renders
[22:11] That's something I do a lot and as long as you don't go too far with it
[22:14] It can really make things look a lot nicer
[22:17] Okay, the next technique which is a new feature you might have seen this already
[22:20] But here I am with an example using it in actually client work. So I'll show you how I actually use this in a render
[22:26] Is the light falloff node where you can get a gradient falloff of like a different color at the start of the light
[22:33] Versus where it kind of falls off. So what I mean is like this, right?
[22:37] These lights here are
[22:39] Red at the start and as the light gets further away from the light source it actually turns into
[22:45] Like blue ish purplish light that's being emitted. So if I move this around you can see it's actually red up close
[22:51] and then like
[22:53] Blue as it gets further from the light source
[22:57] And that that'll like change over the
[23:00] Over the distance you can adjust it all here. This is a
[23:03] client work for
[23:05] res and virtual riot. So virtual riot has like a kind of blue and
[23:10] purple
[23:11] Pinkish kind of color scheme res has a very red sort of color scheme
[23:16] And I was really having a hard time like balancing all those three things together. It was really
[23:21] Uh a little bit stressful on this one, but anyways
[23:23] the point is
[23:25] Um, I was stressing and I found this was like a really good solution to get a nice balance of these two colors where it's like
[23:31] If I hide this you'll see what I mean, right? If I take this away
[23:34] this is just like
[23:36] Not nice at all this weird red emission from these three like light bars here
[23:43] But when I bring in these point lights, it's all of a sudden creating this really interesting
[23:48] Uh kind of like just nice feeling glow around this thing
[23:52] Where it's like warmth and red, but it's concentrated and very controlled
[23:56] So obviously you got to be careful with this and don't go too crazy with it. It can really make it look super unnatural
[24:03] But if you can like tweak around with it and balance it in a way that feels nice
[24:07] You can get some really
[24:09] Interesting and just cool unique lighting with this technique here. So here's how you set this up from scratch
[24:15] I'll just make a new file really quick
[24:17] Okay, so I'll just add a plane for a floor get some objects in here
[24:22] And we'll just start here. So I'm going to add a point light for this, but it works with any light source
[24:26] so point light
[24:28] And we'll just go to render view
[24:30] make this darker
[24:32] Okay, let's go to the object settings and for that point light there. I'm just going to hit use nodes in the shader editor
[24:39] So let's get the light fall off node
[24:42] And we'll just plug that into the color
[24:45] Okay, so I was using linear on that one, but you can use I think any of these
[24:50] Linear or quadratic. I don't actually know what constant does
[24:53] But we'll just start with linear because it's going to be probably the easiest
[24:56] And let's turn down the strength of that till it gets to kind of like a more normal looking strength
[25:01] Then let's take a color ramp and run that through there. So we're plugging this
[25:08] Light fall off through a color ramp into the emission color of the light
[25:12] So if I said I can actually just go in here and set these colors to whatever so if I make this like
[25:16] Blue and I make this one like red
[25:20] It is working, but the range is just not in the right spot here
[25:24] So if I just start adjusting the strength we should
[25:28] like find a
[25:30] uh section of this strength slider where it kind of like
[25:33] Transitions from one color to the other. So I'm going to just move it around until it's kind of in between there
[25:39] Let's increase the strength of this a bit and you can see now it's working. So the light up close is actually
[25:47] Like blue and then as you get further away it gets more red
[25:51] so this is a really
[25:54] interesting technique where it's like
[25:56] um
[25:57] It just it's not something that's possible in real life
[25:59] And this is where it's kind of like fun to be able to run experiments like this in blender with just crazy
[26:05] Situations like this, but you can get some really cool stuff like this
[26:08] So I might want to flip this around where it's like warm
[26:11] At the start and then kind of fades off into something cool
[26:14] Another trick you might have seen is you can switch this rgb color mode here actually to
[26:19] Like hsv or hsl and that'll actually run through
[26:22] The entire color spectrum. So it'll be like if I just crank this to like something over here and make this
[26:30] like you know
[26:32] I don't know something crazy
[26:34] so
[26:35] So what it's doing is it's kind of instead of transitioning with like a weird just going straight from one color to the other
[26:42] It's kind of running across the entire spectrum and picking up any color
[26:46] Uh that it runs into so that can be a really just weird
[26:50] Trippy result you get but I usually don't like doing that
[26:52] I usually just keep it on rgb and then yeah, you can get I kind of like having something warm at the start
[26:56] and then fading off into something cool, but you can do whatever you want here
[27:00] And you could probably actually combine this with all the other techniques
[27:03] So let me try and like bring an image texture in here and just see what that does
[27:09] Okay, so I'm just bringing in that texture of or that image of water caustics
[27:14] Using a mix rgb node set to multiply and then that's just going in here
[27:18] Um, and then you could see if you combine these things together
[27:22] You can just do some wild stuff like this is just
[27:25] super
[27:27] Weird crazy lighting, but yeah, I mean
[27:30] That's funny
[27:33] Oh my god, okay
[27:35] But yeah, you get the point and then you can combine this with lighting gobo's too
[27:37] Like you can do all you can combine all this stuff together into one technique or into like one scene if you want, right? So
[27:44] um
[27:46] That's fun
[27:47] Okay, that's it for this one. Thank you for watching
[27:49] Go and check out the new cyber environments course if you are interested in the newest course that I have for cyberpunk renders
[27:56] Other than that. Thank you for watching and I'll see you in the next one



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
