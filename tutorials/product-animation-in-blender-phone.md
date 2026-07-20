---
title: Product Animation in Blender: Phone
source: YouTube
url: https://www.youtube.com/watch?v=lZPedlX6CMw
author: Derek Elliott
ingested: 2026-07-19
blender_version: "Blender 2.8"
tags: [materials, shaders, glass, metal, eevee, lighting, animation, camera, product-viz, brand-video, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/product-animation-in-blender-phone/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Product Animation in Blender: Phone

**Source:** [YouTube](https://www.youtube.com/watch?v=lZPedlX6CMw)
**Author:** Derek Elliott
**Duration:** 75m15s | 19 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Ladies and gentlemen, I'm Derek Elliott from Dirk.com and today we are going to be making this.
[0:05] So yeah, a whole lot going on there. All the clips are of course rendered straight from EEVEE at


### Tutorial Overview [0:25]
**Transcript (timestamped):**
[2:00] the end of this video. So let me know if these hour long ones are just a little too overwhelming for you. I just want to show you guys cool stuff and sometimes takes time to make cool stuff. First, what we're going to do is create the phone model as a modeling exercise. And then I encourage you to put your own spin on it, of course, come up with something unique, or maybe if you're already familiar with modeling, you don't want to show some product besides a foam, you're welcome to do that. What I'm going to teach you today definitely applies to other stuff. So after all that, we're going to do a quick little detour. I'll show you how I made that little background animation. Since I know a few of you were interested in doing that, I'm going to show you how to do that. So I'm going to show you how to do that. So I'm going to show you how to do that. So I'm going to show you how to do that. So I'm going to show you how to do
[2:30] that. And once we've got our phone model already for action, we'll get it into a basic scene,
[2:35] do some lighting, set up our first animation, kind of lay down the ground rules for how
[2:39] this is all going to come together. We will also touch on how to work with an audio tracking
[2:43] blender, how to find some unique places in the track to help inspire and kind of drive
[2:48] your animation. I'm not going to create every animation since it can be a very time consuming
[2:52] process of kind of fine tweaking curves and camera angles. But what I will do instead
[2:57] is show you each scene that you saw in the intro and do a quick breakdown, kind of covering
[3:01] the unique elements in each one. So let's go ahead and get started with the modeling.


### Modeling the Basic Phone Shape [3:06]
**Transcript (timestamped):**
[3:07] All right, so let's go ahead and get started modeling that phone can't have a phone commercial
[3:11] without a phone can't have a blender file without the default cube. Let's actually use
[3:16] that default cube. I'm going to scale it down to zero merge vertices by distance. So we basically
[3:21] just have a plane here. And while that plane is pretty, we're going to make it into more
[3:25] of a phone shape. Some may call that a rectangle called what you will, we're going to add a
[3:29] bevel modifier and check this only vertices options. And this will allow us to make a
[3:34] just kind of a nice rounded rounded edge there. That looks pretty good. We're going to be
[3:40] getting in pretty close with some of our renders. So we'll do 10 segments. Maybe we go wild.
[3:46] Let's do 11. Don't get too crazy, Derek. Toriel just started. Anyways, let's add in a solidify
[3:53] modifier to give this some thickness, bump that up something like this. And if you're losing your
[3:58] mind already, or maybe you just need a simplified phone, then you can leave it at this. We basically
[4:03] got our modern phone just like a rounded rectangle here. So leave it at that if you like. But what
[4:07] I'm going to do is add another another bevel modifier. And if you've seen my tutorials before,
[4:13] you know, we need to turn on a limit method. So that just gets those edges we want it to get. And
[4:17] now we can adjust this bevel to whatever we like. And this is all stylistic at this point. But
[4:23] this is actually this is a history lesson here. So once upon a time, Steve Jobs went to Johnny
[4:28] Ivan said Johnny, the iPhone has been a wild success. How do we make it better? And what Johnny
[4:33] did was he launched blender, he upped the segments on his bevel modifier. And then he just made it
[4:39] a little bit thinner, maybe this bevel a little bigger. And the new iPhone was born. Just kidding.
[4:46] I have a lot of respect for product designers. But there's no getting around the fact that
[4:50] phones are like rounded rectangles nowadays. So anyways, that looks pretty good. What I need to
[4:56] do to make it look a little more detailed, a little better. And again, you can skip this part,


### Creating Ports / Cutouts [5:00]
**Transcript (timestamped):**
[5:00] if you like, is add in some buttons, some ports, some things of that nature, just to give this
[5:05] again, a little more spice. So I'm going to press shift D to duplicate this, bring it up a little
[5:11] bit just so I can see what I'm doing for a second here. I'm going to remove this bottom bevel
[5:15] modifier. And then we can shape this flat for now. And what I'm going to do is actually use this
[5:20] plain object with all the modifiers enabled, you just have this nice little kind of object here
[5:27] with these modifiers that we can use to start making some of those ports. So I'm going to go
[5:31] into edit mode here. Let's just bring this down a little bit, rotate this on the y axis. And if you
[5:39] pay very close attention, you'll see what I'm doing here. You don't have to pay that close
[5:43] attention. I'm just going to kind of make, yeah, I'm going to use this object with those modifiers
[5:49] applied or not applied, but with those modifiers active to just start kind of cutting into this
[5:55] object a little bit. And we do want that to cut in. So let's, let's bring that in a little bit,
[5:59] something like that. You can see in wireframe view how that's going into the object. That's
[6:04] looking pretty good. And now we did actually use this. Since we duplicate the object, this 11
[6:12] segment bevel modifier was this edge, but for these pieces, we don't need quite so much detail. So
[6:17] let's, let's maybe crank that down to like a, like a five or something. I think it's going to look
[6:21] fine. So with that together like that, let's add a few more little parts where that is going to be
[6:26] cut up. And we will do maybe over here, we'll do kind of like a volume rocker thing. Let's just
[6:31] kind of move that in there somewhere about there, duplicate that volume up volume down, maybe over
[6:38] here, we've got something like a, like a hold button or, you know, just, it's just another
[6:44] detail. You don't need to know what it does. It just looks good. Okay. Maybe we scale it down a
[6:49] little bit on the x axis. That's looking fancy. That's looking snazzy. Maybe over here, we'll add
[6:55] in some, you know, that could be like a little speaker port or something. Let's duplicate this,
[6:59] bring it down, and then maybe like scale this on the y axis a little bit. You know, again,
[7:07] add as much detail as you want. Don't drive yourself crazy, but I'm just going to do that.
[7:12] Maybe duplicate this and then let's maybe like duplicate again, something like that. We're not
[7:19] being super accurate here. We're just trying to quickly add some detail so that when we make this
[7:24] little phone commercial we end up with, we'll have some nice details to work with. So let's just get
[7:31] that place to, you know, somewhere nice and, somewhere nice and even. Again, we're not using a
[7:37] mirror modifier here or anything. So this isn't completely accurate, but I think that's going to
[7:41] look pretty good. Now, so people don't go crazy. We better add a phone jack. I'm going to add that
[7:48] right over here. Not a phone jack, a headphone jack. That's what they call it. And now since
[7:53] we're rounding these with the bevel modifier, this isn't going to be quite perfect, but let's just
[7:58] get that to sort of a circle shape. I think that's going to look fine like that. You just got to
[8:05] have it in there. Otherwise, people will be mad. She'll be like, why didn't you glue the headphone
[8:08] jack? Anyways, that looks good like that. It doesn't need to be super duper perfect. Maybe we'll move
[8:13] it over here. That's where I want my headphone jack. Okay, so with that all together, looking pretty
[8:19] good. Now what we need to do is use this object to cut into the phone object. But for us to be able
[8:25] to do that, we will need to apply these modifiers. And since applying those modifiers is going to be a
[8:30] destructive process, I'm actually going to press shift D and duplicate those and then M to move them
[8:35] to a new collection, which I will call the trash collection. You can call that whatever you want.
[8:39] I think Andrew Price did a tutorial where he did a similar thing and called it the archive
[8:43] collection, which maybe makes a little more sense. But I don't know, I like to call it trash. Call it
[8:47] what you will. What we can do now is go into these modifiers and just start applying them. So now
[8:53] if we tab into Ed mode, we can see we have full access to all that geometry. So that's looking
[8:58] pretty good. Now maybe what I want to do while I'm in here is let's just inset this face a little
[9:03] bit. And we're just going to create a nice little lip here that we can have as kind of the edge of
[9:08] our screen. So let's just extrude that down a little bit. And then over here, we'll turn on this
[9:13] auto smooth option, normal auto smooth, and that will just tell Blender to keep a certain area sharp.
[9:19] So that's looking pretty good. Now what we can do is go into this object and apply the modifiers. So
[9:25] let's apply each one of them. And then now in edit mode, before I actually do the Boolean
[9:31] operation, the Boolean operation, what I'm going to do is right click and merge vertices by distance.
[9:37] And that's going to remove quite a bit of vertices there. And sometimes that's because, you know,
[9:44] when the bevel is kind of intersecting itself and create duplicate vertices, don't want those.
[9:48] So that's why we did that. Now what we can do is go into this object again, and add a Boolean
[9:55] modifier. Use this little eye dropper to pick it. And yeah, it's working properly. We do have some
[10:01] kind of weird shading here. And that's just because the Boolean will kind of mess up the things. You
[10:06] can kind of move this around a little bit, try to get it to look a little nicer. You can see if
[10:10] we've got on that flat surface, it's going to work a little bit better. But you know, the Boolean is
[10:16] kind of a sometimes it works really well, sometimes it doesn't. And it is kind of hard to see what
[10:20] it's doing. So it's working properly. But just so you can see a little better, I'm going to go down
[10:24] here and change this to the bounds method of viewport display. So now you can see that this is,
[10:30] this is working properly. So this is actually what the Boolean is doing. It's just basically cutting
[10:35] into that object. So I'm going to leave it right where it is. So I'm going to go in now and just
[10:40] apply that Boolean modifier. And then I can delete this again, if we need to go back and find it
[10:45] again, it would be in this trash collection, which I suppose at that point, you could call the
[10:49] pet yourself on the back for making duplicates collection instead of trash, because yeah,
[10:55] I don't think that would fit here though, patch yourself on that. No. Anyways, we need to actually
[11:01] put some buttons in those holes that we created. So we're going to do that by you could do it a
[11:05] number of ways like anything in London. But I'm going to go in here and tab into edit mode,
[11:10] and then just select these faces here and watch what I'm going to do. I'm going to press I to
[11:15] inset this face just a little bit. And then E to extrude out. That is the sound buttons made
[11:22] when they are born. Just kidding. Let's let's bellow that just to make it nice and nice and
[11:28] smooth. We're going to use some shiny materials here and you know, having those little edges will
[11:32] make this make this catch some light very nicely. Sometimes when you're doing those operations,
[11:36] you need to reshade smooth. So yeah, those are some pretty sexy buttons. If you ask me,
[11:41] maybe down here, I don't think you're going to see it. But just in case you did little tiny
[11:46] details, add kind of a little port right there. That looks good. Now over here, let's make this
[11:51] like I said kind of like a hold button. Let's do the same process I to inset. And then maybe with
[11:56] this one, let's actually like, let's say, let's say this is one that can kind of travel back and
[12:02] forth this switch here. So let's grab that. Let's just bring it down here. And then let's do the
[12:09] same process just extrude that out a little bit. Maybe just a little past the edge, control B, give
[12:15] it that same bevel. We're not working with a modifier here. So this isn't necessarily exactly
[12:18] the same as it is on the other side. But we don't need to be perfectly accurate. I think that looks
[12:23] pretty good. So yeah, so now this, you know, this is just like a button that would have, you know,
[12:27] little bit travel is the traveling button. Actually, it's not going very many places. It's
[12:32] going to go like right there. So not exactly the most exciting trip that that bevel or that button's
[12:39] going to go on. But enough about that. This is looking really nice. Again, well, I'm so vain. I
[12:44] think it looks pretty good. And if you've been following along, I'm telling you right now, your
[12:48] phone is beautiful. Congratulations to you. Let's do a couple more things. I'm going to flip this bad
[12:54] boy over. Yes, this bad boy. And and I'm going to add in now kind of like a little camera cluster


### Adding the Camera to the Back [13:00]
**Transcript (timestamped):**
[13:02] up here. And the way I'm going to do that is by pressing shift s with that face selected, and snap
[13:08] my cursor there. So it's sitting right on top. And now what I'll do is go in and add a circle. And
[13:12] this will just kind of be the, this will be the start of my little, my little camera cluster
[13:18] here. So move this to where you think it goes for me. I think that's going to look pretty good
[13:24] right about there. And now what I'll do is just extrude it inwards, something like that. And then
[13:32] extrude up something like that. And yeah, that's looking decent, except that little flickering
[13:39] is driving me freaking crazy as it always does. I'm just going to bevel this. So we've got kind of a
[13:45] nice smooth transition here, something like that. I think it looks good. Let's shake it smooth. And
[13:51] maybe this outside edge, let's just bring this down ever so slightly so that we don't have those
[13:57] duplicate faces there. And yeah, blend seamlessly, just kidding. No, doesn't. There's this little
[14:04] option called outline, which will show you the outlines of separate objects, really handy. But
[14:09] in this case, I want to see that that is indeed nice and smooth, not completely perfect. If you
[14:13] did want it perfect, you probably have to actually go into your geometry and make it all proper. But
[14:21] we don't, we're not worried about that today. So don't worry about it today. So now what I want to
[14:26] do, you could just do one camera if you were playing, but we're living in the future here.
[14:32] We got some kind of weird stuff. Let's just delete this face. Yeah. Okay. So let's, I want to live
[14:39] in the future, as I was saying, and we're going to have a bunch of cameras in here. If we just tried
[14:43] to pull this out, though, we're getting some weird stuff going on there. We need to have kind of
[14:47] another straight face. I'm just going to add those right here, just adding edge loops so that now,
[14:52] when I pull all these faces out on the y axis and drag this over, it'll be nice and nice and straight.
[15:01] Oops. It's not. I think I still had some stuff selected. So let's, uh, there we go. Now we're
[15:08] looking good. Straight, straight. Maybe move this up just a little more and give ourselves some space.
[15:14] And, you know, do whatever you want here. You can make this like ridiculous shaped. You could
[15:18] like put it right there. That's kind of cool. No, don't like it. Let's, uh, let's, let's just leave
[15:23] it at that. Now what I'll do is just a couple more things here. Let's select this outer ring here.
[15:30] No, not extruded. Let's press F to fill it in. I had to inset it and just give ourselves a nice
[15:35] little lip there and then maybe E to extrude it down just so it's sitting right on top of where
[15:41] our phone was, something like that. That looks pretty good. Let's go ahead and turn on our lovely
[15:45] little auto smooth option there. And yeah, now we kind of have the basis for our camera cluster.
[15:52] And that is looking good to me. So let's, uh, let's actually go ahead and add some materials. I


### Starting to add Materials [15:55]
**Transcript (timestamped):**
[15:56] think that'll be fun. So I'm popping over here into my look dev mode and that's just going to set us
[16:00] up with kind of an automatic HDRI setup. This is not our actual scene lighting. We're going to do
[16:05] that in a little bit, but, um, yeah, this is going to help us see those materials. So about those
[16:10] materials, let's go ahead and go in here. Let's rename this default material to, um, phone body
[16:16] or something like that. Name it whatever you want. You can name it Dingledore. I don't care.
[16:20] Let's change the color to, um, yeah, whatever you like. I really do not care, but I'm going to make
[16:26] mine. I care about what color mine is. I don't care about what color yours is. I'm going to make
[16:32] mine a nice blue color. Maybe you bring it down a little bit, bring the saturation down a little
[16:36] bit. I want mine to be metallic actually, just because, you know, I like it. That looks good.
[16:41] Make it rough, make it shiny. Do whatever you want. It looks, wow, look at that shiny. See
[16:46] those automatic HDRs really help you see that, see that glimmer and shine. So I'm going to leave mine.
[16:51] Yeah, something like that. I think it's going to look fine. Mine is fine all the time.
[16:59] Derek Rymaster. Okay, back to the tutorial. Let's, um, let's make the inside of this
[17:05] camera like a black material. So I'm going to add a new material and I'm going to call it black. And
[17:11] of course we will change the color of it to yellow. Just kidding. That's green and also just be
[17:17] kidding. This is going to be, oh God, what am I doing here? Come on, click, black, got it, good.
[17:24] And I want that to be right here, assign. So now the inside of that is nice and black,
[17:30] where we will go and put our roughness to one. And yeah, we're going to put our like lenses
[17:36] and stuff in there. So let's go ahead and do that. So I'm going to shift S, now my cursor
[17:41] just selected, which will move it to this little center point where we started that object. And
[17:45] I'm going to add in a UV sphere. It's going to start off freaking huge. Let's scale it down in edit mode.
[17:53] And, um, yeah, let's just kind of get it to a nice size, something like that. I think looks
[18:00] pretty good. Let's shade it smooth and let's set up the material for that one. So let's just do
[18:04] new material. Let's call that one lens and change the color of it to a sort of a blue color. I think
[18:11] usually looks pretty good for this. And don't want it to be too rough on it to be nice and shiny.
[18:15] And we do want it to be transparent. So let's turn the transmission value all the way up.
[18:19] And then since we're working in EV here, we need to change a couple of settings down here in the
[18:24] settings section. These are like all settings. And for some reason, this section is called settings,
[18:29] which I like. So we're going to turn off the shadow. And then for the blend mode, let's turn that to
[18:35] alpha blend. Usually looks pretty good. So now what we can do is go into this alpha value right
[18:41] here on our principal shader and just bring that down a little bit. So it's kind of transparent.
[18:45] That looks pretty good to me. And now what I'll do is in edit mode, I'm going to duplicate this,
[18:50] scale it inwards. And this will just give me kind of like a nice two layer like lens effect. I don't
[18:58] know. I looked at some reference images. They looked kind of cool when they had that. So, uh,
[19:02] so we're doing it. Uh, camera people leave your nasty comments somewhere else. I'm selecting an
[19:08] outside ring there. And I'm just going to extrude it out. Oh, I can't see what I'm doing.
[19:13] I'll Z. Let's bring that up. And, uh, okay, definitely don't want that crazy material. So
[19:20] let's add in our black material using that once again, let's assign it. And then we can,
[19:25] uh, we got weird normals. Let's press shift and to recalculate those. And, uh, yeah, that's looking
[19:31] cool. So now you just want to go in and kind of add some more details as you please, just to make
[19:37] this look, make it look like you worked a little harder on it. Um, yeah. So, so work hard on it.
[19:47] Let's, uh, let's turn on our once again, lovely auto smooth feature. And I want this to be
[19:53] sharp too. That looks good. Something like that. And then now back in edit mode, I think what I'll
[19:57] do is just actually duplicate this whole thing again. And we'll make another camera because
[20:03] that's almost 2020 or I don't know, maybe you'll be watching this tutorial in 2020. Comment below
[20:08] 2020 fam. And then actually every year on January 1st, someone please comment with the new year so
[20:14] that people can like your color or something. I don't know. Never mind. So, uh, I'm going to
[20:19] make this camera, maybe a little bit bigger. This can be the hyperduper camera, you know,
[20:24] because it's freaking 2020. Okay, that is, that's maybe a little too ridiculous, even for me. Let's,
[20:31] let's maybe make that, uh, which one would be a little different so that it looks like we, uh,
[20:36] so it looks like we thought about it, I guess. Anyways, that's fine. Let's, uh, let's just add
[20:40] some more detail, maybe like put it a little ring there, a hyperduper ring, because this is the
[20:46] hyperduper camera. Maybe this comes in a little bit. Nice, sharp hyperduper camera. And you know,
[20:55] let's just go crazy. Let's, uh, let's, um, let's select, let's select this whole thing here
[21:01] and then duplicate it, maybe scale it down. This is the, uh, the hyperduper small edition.
[21:10] And what this one does is, um, it, uh, it's just hyperduper. Okay. Don't worry about it.
[21:20] Let's, um, let's try to select another camera here, maybe this one, except, uh, uh, we're getting
[21:26] some extra faces there. Let's, uh, let's select that and then let's select that. I'm pressing L
[21:33] to select these islands here. And then let's duplicate this one, maybe put that right there.
[21:39] Hyperduper 2.0. This is like, you know, what it does actually in scientific terms, this
[21:46] advanced camera allows you to, if you can't tell I'm making this up as I go, but it's like,
[21:52] you know, maybe, maybe you can like scan real world objects and it turns them into blender files.
[21:56] Wouldn't that be nice? We wouldn't have to model this darn phone. Just kidding. I'm having a good
[22:02] time modeling the phone. Are you leave a comment below. Um, yeah, I think we're gonna, we're gonna
[22:08] leave it at that. We got our ridiculous, uh, camera cluster there looking very fancy, looking
[22:12] very cool. Maybe we want to make it even cooler. Look at that. You can just add details endlessly
[22:19] and people will think you worked on it for hours. Um, maybe we have been working on it for hours.
[22:24] I should probably wrap this tutorial up. Uh, yeah, that's looking pretty good. So let's leave it
[22:28] that. Now, last thing I'm gonna do is add the glass that goes on top of this. So I'm gonna select
[22:33] that object and then I'm gonna select this ring, shift D to duplicate it, P to separate it by selection.
[22:39] Select it, make it a face and then, um, for that material, let's, uh, we don't want either one of
[22:46] these. Let's remove those. Let's start with the lens material just because it already has some of the
[22:50] EV things set up. I'm gonna add a new one and we'll just call this class because we're gonna use it
[22:55] in a couple other places. Um, well, yeah, other places where there's glass, if that makes any sense.
[23:01] So don't want it to be blue. Let's turn the saturation down value all the way up nice and bright,
[23:06] white. Uh, let's leave it nice and shiny. Maybe we can turn the alpha down a little bit so we can
[23:12] see all our hard work on the camera in there and wow, this look demo is really pretty, really pretty.
[23:18] If you don't like the, uh, HDI you got, there's a couple other options there. Oh, that's a nice one.
[23:24] And again, this is not our scene lighting. Uh, you wish it was, but it's not. Um, looks good though.
[23:30] So to add a little more realism, let's extrude this down a little bit just so we have some
[23:35] actual thickness there. Careful not to intersect our extremely expensive cameras. Uh, we do have some
[23:42] double geometry going there. So I'm just going to scale that in a little bit so we don't get that
[23:46] flicker. We can shade that smooth and yeah, should have this auto smooth already enabled
[23:50] since we duplicated it from an object that had auto smooth enabled. Anyways, that looks good.
[23:55] Now last thing maybe I'll do is another just little detail I saw in some of my reference
[24:00] photography. Let's inset that face and then, um, what we can do now is just select this ring here
[24:06] and then let's add in our black material again, assign it and yeah, now we got this kind of little
[24:15] black ring there and we got the thickness, the shininess there. This is looking very dynamic,
[24:20] very cool. Last thing I want to do, at least for now is flip this thing over and let's take a little
[24:25] bit of a look at the screen. So if you want to rotate this whole thing around, nothing's going
[24:30] to come with it. So let's, um, let's just select everything here and then parent it to the phone
[24:37] object. Object, keep transform. Oops, not those. We need to delete that for now. So yeah, we got
[24:46] all that in there looking good. So now if we spin it over and our phone object, by the way, is still
[24:52] named cube because if you forgot, we made this from the default cube. Default cube, oh, how you've
[24:58] grown. Let's name this phone because that really tripped me up. Of course we're naming it phone.
[25:09] Is anyone unclear on why we would name this phone? Okay, let's move on. Let's select this top face here
[25:17] and we want that to have the glass material and I also want this face to have that. So let's add
[25:22] a new material. Let's have the glass and let's assign it and now that is working properly. We've
[25:28] got a nice glass there, but of course we can see indoor phone and this tutorial, like I said,
[25:32] probably long enough, don't need to model the entire interior. So let's add in a screen to cover up
[25:38] that interior. And so the way I'm going to do that is just by getting that bottom edge there
[25:43] and pressing F to fill it in and then let's add a new material. Of course we'll call that screen.
[25:51] And for that material, let's make it an emission shader, I think. I know. And let's assign it.
[25:58] So now that emission shader is on that bottom part. And now for this, you could load in a picture,
[26:04] picture your mom, picture your cat or like a video or something. I of course made a nice little video,
[26:10] so I'm going to load that in. I think I'll show you in this tutorial how I made that,
[26:13] just a real quick overview. So stay tuned for that part. But let's add in an image texture.
[26:20] And then what I'll do is open it up. I've got it saved right here as background two.
[26:27] And yes, it is working properly. First thing I need to do though is in edit mode with that screen
[26:32] selected, press U and smart UV project. Now that is on there. And like I said, this is actually a
[26:39] video. So if I press spacebar, though, it's not going to play. So let's first tell it that it has
[26:44] some frames. Let's just put that like 100. And for the time being, we can leave that at 102.
[26:49] And then let's turn on auto refresh. And now when we press spacebar, that video will actually play.
[26:54] And it is upside down a little funky. So let's, let's drag out a new window here.
[27:02] If you can click that corner, it's always a little tricky. And make that a UV image editor,
[27:07] load in our background image. Guys, this is crazy. This is like the video is playing in both places.
[27:13] Our phone is rendering in beautiful detail, real time. And, and yeah, we can even like edit the
[27:20] UVs while this is playing. If that's not crazy, I don't know what is, I hate to say it, but can
[27:27] your software do that? This is insane. Blender 2.8. Oh my gosh. Okay. So anyways, that looks good.
[27:35] I think we're going to leave it there. I might go in and add maybe like a flash back here.
[27:40] And maybe a speaker, like a microphone. And then, of course, it wouldn't be a Dirk tutorial if I
[27:45] didn't slap a big Dirk logo on here. So I'll do that now and then catch it in the next part. If
[27:51] you're liking the tutorial so far, please feel free to give me a thumbs up, subscribe, like,
[27:56] leave comments, stuff like that. Yeah, enjoy your phone model if you want to leave it here.
[28:01] Otherwise, I'll catch you in the next part where we are going to tie this all together and kind of
[28:05] make a little advertisement for your freshly created phone model. Thanks so much for watching.
[28:11] I'll see you in the next part. All right. So just want to take a quick little sidetrack here, show


### How I made the Background Abstract Animation [28:12]
**Transcript (timestamped):**
[28:15] you that background scene file, how I set that up. It's basically all happening in the material here.
[28:20] We've just got a noise texture feeding into displacement. And that's going into this
[28:25] displacement input here. And to get this to work and show up, you need to go into your material
[28:30] settings here and then turn this to displacement and bump. And then that will work. You won't see
[28:34] it in the viewport, but as you can see in a render view, it's working. And to get that nice squished
[28:39] look you're kind of seeing here in the middle, I used a simple D4 modifier just kind of,
[28:44] just kind of squish it together. Give me a cool look. You know, you can do all sorts of stuff here,
[28:48] but just play around with it, come up with something cool. The way I got it to move the way it does is
[28:53] just by animating the location of the noise texture. And that just kind of gives you a nice
[28:59] flowing motion there. That's pretty much it. If you follow me on Instagram, you see that I,
[29:04] initially I was kind of working with some kind of different colors there, but I ended up not
[29:08] using that. This could just as easily be black and white, but really do whatever you want. I mean,
[29:12] this is just kind of an extra element for your animation. You can just use a photo, but that's
[29:17] what I did. Just wanted to show you how I did it. Let's move into the next part. Alrighty, so here


### Overview of Small Additions/Changes [29:22]
**Transcript (timestamped):**
[29:23] we are back in the phone file. As you can see, I've done a couple things just to spice it up a
[29:28] little bit. Hope you did the same. Get your phone, look at how you like it. Let me just walk you
[29:32] through some of those changes that I did. So first of all, you'll see that obviously I did,
[29:36] had to put the Dirk logo on there. And that's just a really simple material.
[29:40] Following pretty much the same process we did in the box tutorial. If you haven't seen that,
[29:44] I'd almost call it like a prerequisite for this tutorial, but we really covered some working
[29:49] with the shader here to create some cool effects with the glossiness happening in different places.
[29:56] Let me just show you that. So yeah, we just got an image texture feeding into here. And that's
[30:00] adjusting the roughness value so that we have that nice little spot gloss. And maybe you didn't
[30:05] catch it in the video, but I did hide a little dirk.com right there on the camera or something too.
[30:10] So think about that, add whatever you like, make it look cool. Beyond that, I did add this little
[30:15] flash object here and the microphone, those are just, you know, they're just circles and then
[30:21] kind of following the same process we did when we made the cameras. Now the material for that
[30:26] just a magic texture here is kind of controlling the, we've got a little bump going on there and
[30:30] then also some color to give it kind of an iridescent look and microphone. Same thing,
[30:36] pretty much the same exact texture just with a different scale value there. And then we've got
[30:41] that one black. And then beyond that, I went in and you can see I added this little bumper material.
[30:47] So just selecting that edge loop, assigning a new material to it, which for that material,
[30:51] same as the phone body, I just turned off the metallic value so that it had a kind of got a
[30:57] rubbery look to it. Also, I added the black material to the inside of these buttons just to
[31:03] give them a little more contrast. And then beyond that, I played with the shape of this kind of
[31:08] bump out for the camera cluster a little bit just to get it how I liked it a little bit more smooth.
[31:13] And yeah, that's pretty much it. So anyways, let's go ahead now and move into kind of setting up our
[31:19] first scene, laying down some ground rules for how we're going to light all these scenes. And
[31:24] there's actually one other thing I did here. So if you look, we've got some kind of unrealistic
[31:28] shading here with those lenses poking through. And what we did to fix that was go down here into the
[31:33] cycles or size that EV settings, and then I changed it from alpha blend to alpha hashed.
[31:39] And that ends up looking a little bit more proper. So like in the way that is, let's go ahead now


### Setting up the Backdrop/Lighting [31:42]
**Transcript (timestamped):**
[31:44] and like I said, set up the scene just a little bit. So I'm going to push shift A, add a plane,
[31:48] and let's just scale that up a little bit. And what I want to do now is just kind of create
[31:53] a nice little seamless backdrop that can serve as sort of a background for our phone.
[31:59] Something like that looks pretty good. Now I'll shade that smooth. And then
[32:02] let's actually drag out a new window here. This is how I always like to set up my viewport,
[32:06] my viewport. And this is going to be a 3d viewport as well. And we will look through the camera down
[32:12] here in this view. So I'm going to push shift A and add a camera. And then pressing zero on my
[32:18] number pad, I'm going to go into that view, shift tilde and just kind of fly out to around where
[32:24] I want that camera to be. And then what I'll do is up here in my transforms, I'll just adjust these,
[32:31] I'm holding control and just snapping these to some nice even values. So everything's nice and
[32:37] lined up. And so for this view, let's just leave that as a regular 3d view. And then down here,
[32:42] we'll actually go into the render view. So no longer are we in the look dev mode. And as you
[32:47] can see, it is not nearly as exciting. If you wanted to, you could actually use an HDR, I like
[32:52] your scene, but I like having a lot of control over that. And to get that control, basically want
[32:57] to set up all the lights myself. And it's not too difficult for process. And you do get some really
[33:02] nice results once you adjusted how you like. So let's go through some of those adjustments.
[33:06] What I'll do is so that I have complete control, I'll turn the world strength down to zero.
[33:11] And we can actually turn off the overlays here. And let's go into the camera view here, not really
[33:15] gonna see what's going on. But what I'll do first is add a point light. And I like to almost always
[33:23] start with a point light. I kind of put that right up on the edge of the seamless backdrop there.
[33:27] And then I like to crank the strength up quite a bit. And you can see this is doing a couple
[33:32] things for us. So first of all, it's just lighting the scenes, we can actually see what's going on.
[33:36] But for one, it's giving us this nice background, we've got kind of a gradient going on there.
[33:41] And then it's also acting as kind of a rim light. So when we are kind of rotating this phone around,
[33:45] you can see we catch some nice little highlights on these edges here like that. So that's what
[33:49] that point light is doing. Let's also so we're not getting there, the reflection we're seeing here.
[33:54] Let's add a material to this floor. And I'm just going to press new, let's go ahead and call that
[33:58] floor, call it whatever you like. And I like to try to speculate down a roughness up, we can leave
[34:04] it at this, it starts at like a point nine oh six for some reasons, like the default. Someone
[34:09] please tell me where that comes from. But being the perfectionist I am, I like to set that to point
[34:13] nine. Don't want it a total white so that we do, you know, we can kind of increase that value a
[34:18] little bit by using this point light. But um, yeah, something that's just like kind of an almost
[34:22] white looks pretty good. So with that there, what I want to do next is just kind of start setting up
[34:28] the rest of the lighting. But before I do that, so that I'm a little more accurate with where this
[34:32] is going to end up, I'm just going to rotate this a little bit so that I can really see, you know,
[34:37] that's kind of an angle, we're going to be creating the first animation that you see in the video,
[34:42] just that one where it's kind of moving from left to right, really simple animation that looks nice,
[34:47] but a good place to start when we're talking about how these scenes are set up and how we light them.
[34:52] So first thing I'm noticing here is I'm getting a little bit more perspective than I want,
[34:56] just kind of a little distortion there. So I'm going to crank this focal length up to, um, you
[35:01] know, maybe like 82 80 something like that looks pretty good. And that's just going to give us a
[35:06] little bit more of a, um, it's just going to remove some of that perspective distortion. And
[35:10] maybe we can move this out a little bit. So with that set up looking sort of how it may end up
[35:15] looking once we do the animation, I'm going to go ahead and start adding in some area lamps.
[35:19] And I just like to use area lamps because, um, yeah, they work pretty well. And I'm going to use a
[35:24] disc just because I think that ends up looking a little bit more attractive, but use a use whatever
[35:28] you want. And then let's just start cranking this power up. So now we're just basically going to go
[35:33] through a process of adding lights to the scene and slowly lighting this phone so that we have
[35:39] basically what we want to be doing here is, you know, you want to obviously be able to see the
[35:43] object as best you can. So we need plenty of light in the scene, but we don't want anywhere to be too
[35:48] bright and we don't want anywhere to be too dark. So it's a little dark on this back edge. So let's
[35:52] press shift D to duplicate this lamp. And then I'm just pressing R twice to kind of enter a free
[35:58] rotation mode. And you know, these don't all have to have the same values. Maybe you want,
[36:03] maybe you want this to be a little smaller, so we've got a little sharper reflection there.
[36:06] And like you can, you can kind of zoom in here and see that we're just getting now a nice highlight
[36:10] over here. Whereas before when that was turned off, it's just a little dark. You want to avoid
[36:14] things like that. So that's looking nice right there. Basically, you know, a phone is a really
[36:18] good example of an object to try to light because if you're working with something like a character
[36:23] or maybe a more complex model, there's a little bit of interest in the model itself. But in the
[36:27] case of a phone, it's so like we talked about in the modeling section, it's so plain, it's just
[36:32] like a rectangle that you really have to use the lighting to make it a little more exciting.
[36:38] I've used that rhyme a few times before, I think it's going to appear in pretty much every tutorial.
[36:43] So everything's looking pretty good there. I want just a little bit more light up here.
[36:47] This lamp that I just added is giving us a nice highlight on this on this camera cluster. Maybe
[36:52] I want that to be a little bit bigger though, and then maybe not quite so strong, just I just want
[36:57] to give myself a little bit of a soft light kind of on the front. So something like that, I think
[37:01] is looking pretty good. And all in all, I mean, I think this is going to work pretty good for us.
[37:05] We may have to adjust the lighting a little bit more. But before we do that, let's go ahead and


### Creating the First Animation [37:09]
**Transcript (timestamped):**
[37:09] get the animation set up. So now is when you need to decide kind of how long you need this
[37:15] particular animation to be. For me, I know that between the beats, Andrew actually told me that
[37:21] the BPM for this song that we're working with, and you may be working with something else,
[37:26] but I know that between each beat that I want to kind of change scenes, I need about 68 frames,
[37:32] and that's done with just a little bit of math, depending on your frame rate, which I'm going
[37:36] to go in here and make sure it is set to 30. But yeah, if you need to just kind of look at the
[37:40] peaks in your in your audio track, decide kind of where you want the scene to change, do a little
[37:46] math with your frame rate and decide how much you need to render. But really, the more easy way to
[37:50] render it would be to just render more than you need. And that's actually what I did at first,
[37:54] I just rendered like a lot of frames, I might have done 100 or maybe even more,
[37:58] because you render so fast that you can just kind of render more than you need. And then when you're
[38:03] editing it all together in your video editor, you can just kind of cut out what you don't need and
[38:09] don't worry about having a little too much extra. But in my case, I know I need exactly 68. So I'm
[38:13] going to set that to 68. And then what I'll do is again, start inserting some keyframes. So I want
[38:19] the phone to start out kind of, we're going to try to mimic kind of what I had in the intro. So
[38:24] I'm just rotating this a little bit. Maybe it'll kind of start down here. And we don't even need
[38:28] to worry that this is intersecting the floor because you're not going to see it. You know,
[38:32] if you're going to be zooming out, obviously, you wouldn't want that. But for me, I think having it
[38:36] start kind of looking down like that is going to look pretty good. So let's insert keyframes here
[38:40] and here, just right clicking to do that. And normally, if I was going to be having to play
[38:44] with the curves a lot, I would not want to insert all those keyframes, because it's just, you know,
[38:49] we're not really going to be moving that much on some of these axes. But for what I'm going to
[38:54] do, it's just going to be a steady move from one side to the other. It's just going to be a linear
[38:58] animation. So I'm not really worried about having extra keyframes. So with all with those all set,
[39:05] I'm going to go to the end of the animation here frame 68. And then I'm just going to move this over,
[39:10] have it rotate, and have it kind of start looking into that light a little bit. And this is, you
[39:15] know, kind of up to your artistic expression here. This is something that takes a little bit of practice,
[39:19] kind of how you want to frame these shots. But adjust it as much as you like, I'm going to go
[39:23] ahead and insert the keyframes there. And let's see kind of how that looks. Let's press space bar
[39:26] to play it. So that's nice, it kind of it's kind of looking down and then it goes kind of into the
[39:31] light, if you will. That's nice. So one thing I'm noticing, though, is we've got a little bit easing,
[39:36] it starts off slow, speeds up and then slows back down. Like I said, I want that to be linear. So
[39:42] I'm just going to press T down here, and set that to linear. So now it's just a nice steady move from
[39:47] one side to the other kind of looks like it's been kind of just floating through space, a nice
[39:52] effect, if you ask me. So now what I want to do is just go back into my lighting, make any adjustments
[39:57] I need to, I'm just kind of looking here. So maybe, you know, right here, I want this to, I want this
[40:02] to catch a little bit of a reflection. So maybe we can move this down here, something like that.
[40:07] So it starts off with a little bit of reflection there. And then when it kind of comes across,
[40:13] you can see we're catching the reflection from this light out here. You know, if you need to
[40:17] move that around, you could move it in, move it out. But I think it looks nice. Maybe I actually
[40:23] do want to bump that size up just a little bit. Move it down, increase the power a little bit.
[40:28] Something like that, I think looks good. And then, and then it's coming around and looking up into
[40:34] that other light, maybe don't want it to quite catch quite so much of that light. Let's kind of
[40:39] move that over and maybe give that some extra power. So it's really getting really getting
[40:44] blasted there. I said it in the blasted tour, I think sometimes you guys, when you're lighting
[40:49] your scenes, you leave these values way too low, like you're trying to save power, but
[40:53] crank it to whatever value you want. It's not going to cost you anymore. So press and space
[40:59] by here previewing that. Honestly, I think that's looking pretty good. The next thing you might want
[41:02] to do is add a little bit of depth of field. I'm going to do that by adding an empty, and that's


### Adding Depth of Field [41:04]
**Transcript (timestamped):**
[41:07] going to be object that I can focus on. Use any empty you like, but of course, since I love circles
[41:12] so much, we're going to use this sphere. So there actually is a circle empty, but I don't like that.
[41:18] I like the sphere one. So what I'm going to do is just for one, let's take this camera object,
[41:24] we can turn on depth of field here. And then so that we can see that it's working, let's just turn
[41:29] our f stop all the way down. So yeah, nice and blurry. But for the focus, let's have it set to
[41:35] that object right there. And we can actually go in. And if we needed to call this or we need to
[41:41] select this later, it'd be easier if we named it. So let's name it focus. And now, when we move this,
[41:47] so if that is set properly, as it is, then we can move this and that's going to adjust, you know,
[41:53] where that focus is. So I want to just kind of stay focused on the camera here. So I'm going to move it
[41:58] to right about there, I think looks pretty good. Insert keyframes on the location and the dev rotation
[42:03] here is not going to matter. But let's go to the end of the animation, and then just move that
[42:07] right to its new spot there, just kind of nudge it till it's in the, in the right location,
[42:12] insert keyframes there. And then this is going to have that same easing. So we can just press
[42:17] T and set that to linear as well. So it moves nicely with it. Now I don't want nearly that much
[42:22] depth of field, I would highly advise you don't use that much, it looks kind of cool for some shots,
[42:26] but a little bit overkill here. So I'm going to bring this back up to a more reasonable,
[42:31] reasonable value, maybe like four or so will look pretty good. And let's press spacebar play that.
[42:36] And yeah, honestly, that is looking pretty good. Next thing you might want to do is just go into


### Setting up the Render [42:39]
**Transcript (timestamped):**
[42:40] your EV settings here, we can turn on some bloom. Everybody loves that. Don't go too wild with it
[42:44] adjusted as much as you need, maybe turn the threshold up a little bit so you're not getting
[42:48] it everywhere. And then we can also turn on screen space reflections. And then soft shadows would
[42:53] be a good idea. Play with the settings you like. But I think that those look pretty good. I didn't
[42:59] even end up adding the light boxes and stuff to get accurate reflections in that animation. And
[43:04] it still turned out looking really good if you ask me. So don't worry about doing too much there,
[43:08] just those basic settings usually have you covered. So the next thing you want to do is just go in and
[43:13] make sure your resolution is right. Frame rate is extremely important if you're going to be syncing
[43:18] this with audio, make sure you're using your consistent frame rate. And then I, you know,
[43:23] if I was going to be running this in cycles, I would render it to individual images and then
[43:26] sync those together in a video editor. But in this case, what I did was just use the FFMPEG
[43:31] video and then changed it to a quick time. And then for quality, do whatever you like.
[43:37] But I found that the perceptually lossless looked pretty good. That gave me a good balance between
[43:43] quality of the video that was output and file size. It was pretty manageable, honestly. And yeah,
[43:48] so I have a 1080 Ti, which is kind of an upper mid range graphics card these days. Nothing too fancy,
[43:54] but this whole thing for me is rendering in like less than a minute. It's super quick. So don't
[44:00] put too much pressure on yourself to get this right before you render it. If you need to,
[44:03] sometimes it's nice to just kind of render it once, take a look at it. And then if you need to,
[44:08] go back and re-render it because EV is just so quick that it's easy to do that. So anyways,
[44:13] that's looking pretty good. What we're going to do next is just move into looking at some of these
[44:17] other scenes, covering some of the unique elements in each one. And of course, I'll show you the
[44:21] lighting setups for all those so that we don't leave anything off the table. But yeah, looking
[44:27] pretty good. Let's carry on. Thanks for watching. Alrighty, well congratulations on falling along
[44:33] so far. What we're going to do now is just walk through all the separate shots that I put together
[44:39] for my animation and talk through kind of what's happening in each of those, go through some of
[44:43] the unique elements, show you the lighting, and yeah, just give you the full picture on kind of
[44:48] what went into each of these and how it all came together. So now would be the time for you to maybe
[44:53] bust out the sketchbook, think about what you want to do, maybe do your own little research
[44:57] check out some other product, the animations, other phone commercials, and yeah, just start kind
[45:02] of thinking about what you might want to do to make this your own. Of course, you're welcome to
[45:05] copy exactly what I'm doing and try to mimic those shots. But yeah, you know, this is an opportunity
[45:11] to kind of do whatever you want. And yeah, make it make it your own. So anyways, let's go ahead and
[45:18] walk through these. What we have here is the full file that I actually used to render the animation
[45:25] you saw on Instagram or Twitter, wherever you saw it. Thank you for all the love by the way.
[45:29] Glad you guys liked that one. And and yeah, so this is we're actually going to put this file up on
[45:34] the Patreon for you to check out if you want to download the entire file and you could basically
[45:39] render exactly what I did from that file, or just use it to check out the lighting setups and a
[45:44] little more detail, whatever you want to do. But let's let's start walking through this. So what we
[45:48] have here is basically the the scene that we just created, you know, just that kind of basic
[45:54] floating scene. And it turned out looking pretty similar to I think what we just created. But
[45:59] um, yeah, if there's any discrepancy there, then feel free to check that out. But looking pretty
[46:04] good. Let's take a look at the next one, which was the it was the pan one collection there. So I do


### Animation 2 (Button Slide w/ Shape Keys) [46:05]
**Transcript (timestamped):**
[46:14] have these all as separate collections. So with that, there's its own camera. So I need to press
[46:19] control and uphead zero, so that I can be looking into the proper camera for that scene. Now not a
[46:26] whole lot happening here. Basically, the camera is just kind of moving up a little bit, while this
[46:30] phone rotates, you can see it's just moving on the z axis. Now there's a little bit of rotation or a
[46:35] little bit of other keyframes here besides just that z location. And I think what that was was me
[46:40] just trying to keep it nicely kind of aligned centered here in the frame. And you can see I
[46:46] do have a composition guide on here, these thirds kind of overlay. If you want to turn on something
[46:51] like that, there's actually a bunch of them you can use, you know, all these different options. But
[46:56] just in your camera settings here, go in and you can turn on composition guides in the viewport
[47:00] display section. To see those, you will need to have overlays on. And you can you basically need
[47:06] to uncheck everything, but then still have this overlays checked. And that composition guide will
[47:11] appear over here in your rendered view. So that's how you get that going. But the animation here
[47:16] is super simple. Lighting setup, as you can see is basically the same. But the one thing that is
[47:21] happening here, it's a little more unique is that this kind of hold button is kind of snaps up there
[47:27] right on the beat. And let me show you how to do that. We actually did that with a shape key.
[47:32] Really simple. If you use shape keys before us, there's probably going to be nothing new. But
[47:36] if you haven't, let's let's take a look at that. So I'm going to remove it just so I can show you
[47:41] how it works. Basically, with a shape key, you are setting kind of different versions of the mesh
[47:48] as it appears in edit mode, sort of. So to add a shape key, you're just going to go over here and
[47:52] press this whole plus button. And that will create what's called the basis. And this is just, you
[47:58] know, your mesh kind of as it is. But to set up a shape key, you want to press this one more time.
[48:03] And now we kind of have a second version of edit mode, if you will, where we can go in and make
[48:08] some adjustments. So those adjustments we're going to make, just select that face. And then I'm going
[48:12] to press control plus to grow my selection. And then I'm just going to press G and Z. And then
[48:19] just bring that up to about there right where I want it. And now when we tab back out of edit mode,
[48:24] you'll see our changes have gone away. But what we have now is this little slider over here
[48:30] for the value. And we can just adjust that. And that basically becomes our animation there. So we
[48:36] can, you know, go to wherever you want in the animation. If you want that to happen on a beat
[48:40] or something, you know, whenever you want to happen, just go in and insert a single keyframe.
[48:45] And then you know, you can move forward a few frames, and then set that to one insert another
[48:50] keyframe. And then you can see that little button animation. And you can do all sorts of stuff with
[48:55] shape keys. This is really a very basic example, but didn't want to show you how we set that up.
[49:01] So that's pretty much it for this scene. Let's take the next one, take a look at the next one,


### Animation 3 (Exploded Camera w/ Basic Transforms) [49:05]
**Transcript (timestamped):**
[49:07] which was the camera scene, the hyperduper cameras. Hope you guys are putting hyperduper
[49:12] cameras in your phone. I definitely want to see what you come up with there. So let's, let's snap
[49:17] our camera view there so we can see how we're looking. So yeah, this is kind of just a really
[49:22] cool effect. I feel like I see this in a lot of commercials. I don't know, I wish I could
[49:26] give credit to whoever came up with this first, but you see it in like everything nowadays. A lot
[49:31] of times with cameras, something just like this, but also just in general, you see a lot of kind
[49:35] of exploded view animations, really cool effect. And yeah, it's cool. So we put it in here, maybe
[49:42] you want to do the same. For this one, it's pretty simple. What's going on again, but let me walk
[49:48] you through it. And then again, let's just take a look at the lighting here. We can see I've added
[49:51] a little bit more, like I added another lamp in here so that you could just get a little more
[49:56] reflection. I think that was to get this guy right here. Yes, that way that nice bright there. And
[50:01] then it kind of kind of fades out there. So that looks really nice. And again, same process we did
[50:07] when we did that full walkthrough on the first scene. You know, you're just going to kind of set
[50:11] up your animation, adjust those lights as you need to and get it looking right. So to do this,
[50:17] I'm actually going to let's, let's get rid of this actually. Let's just delete the whole darn thing
[50:24] and recreate it so I can show you how that worked. So I'm going to go over here into my trash collection
[50:29] where I have just a regular phone set up, shift D to duplicate it. Let's move it to that camera
[50:34] collection. And then let's hide our trash collection again. So now I just have kind of a duplicate
[50:40] of the phone. So had you not joined all your pieces, you might be able to skip this step. But in my
[50:46] case, I had joined everything together. So what I need to go do now is go in and separate some of
[50:52] those parts so that we can animate them individually. So the way I'm going to do that is just press
[50:56] tab to go in edit mode, alt A to make sure everything's deselected. And then I'm just going to press L
[51:01] and that'll select this kind of island here. It's just an individual kind of floating piece of the
[51:05] mash. There's no shared vertices. I'm going to press P and separate it by selection. And then
[51:10] likewise, I'm going to go in here and I'm going to need to go into my x-ray so I can select those
[51:14] inner lenses. I'm just pressing L and just grabbing those. So just once you've got them all there,
[51:21] just press P and separate by selection. And now there is a reason why I left this one separate.
[51:26] So let's uh, let's tab into edit mode and oops, we're on multiple objects there. So I want to
[51:32] tab in on the phone object. L, L, make sure I got that all together. Okay, and then P separate by
[51:38] selection. So I have all those separate pieces. And if I were to rotate this, yeah, it would not
[51:43] come with it. So let's go ahead and parent these. I'm going to alt Z, go into my x-ray mode. Make
[51:49] sure that get all these selected, select that and select that, control P, parent them all to the
[51:56] phone object. And then now when we rotate this back to kind of the angle we had seen in the animation,
[52:03] something sort of like that. Since we, since these are all parented the phone object, we don't have
[52:10] any weird orientations, these are all just zeroed out. So now all we need to do is just animate it
[52:14] on the, I think it's the, yeah, the y location. So it would be a good idea since we want these to
[52:20] settle back into right where they are, to go to our end frame here, and then maybe a insert keyframe
[52:26] what was it? Yeah, the y location, insert keyframe there. Let's select that object,
[52:31] insert a single keyframe there. And then this object actually poked through a little bit,
[52:35] which is why I left it separate. So I actually gave that a little bit of a Z location animation too.
[52:40] So let's insert keyframe for both those in this case. So then maybe at the start of the animation,
[52:47] you have them all just kind of in that exploded view. So let's just give that a little bit of
[52:51] y location there, insert a single keyframe, maybe have this one start around there, insert a single
[52:58] keyframe, and then we can have this one start around here, and then you can see how it kind of
[53:04] passes through. So we want to pull this out to maybe somewhere right there, and then also have it
[53:09] kind of up a little bit. So that when it goes in, it kind of, it kind of settles in nicely.
[53:14] And maybe we need to give that just a little more, or actually, I think when we adjust these curves,
[53:18] we won't have the intersection. So about those curves, the basic automatic setup is
[53:24] that just bezier option where it does the speed up slow down thing that I'm always talking about.
[53:28] But we want this kind of settle into place nicely. So I'm going to change this.
[53:32] Let's actually let's make sure we've got all these selected. And then over here, press a to select
[53:37] everything. And then I'm going to press T and change this to quadratic. And that's going to,
[53:42] so this is actually the opposite of what I do. It's going to start off slow.
[53:46] And then it's going to snap into place. But I want the other way around. So I'm going to
[53:49] press Ctrl E and have that ease out instead of ease in. And that's looking pretty good. So,
[53:55] you know, maybe on this one, we would have to go in and just adjust that a little more. You could
[53:59] also, I think when we actually modeled it, I didn't have this, but you could go in there and just
[54:03] also just kind of scale that down. Help yourself out a little bit. And it looks like it didn't
[54:08] out me quite enough. But yeah, you would just want to adjust that curve there on the on the
[54:12] Y location, I think, so that you could get that to, you know, if you need to adjust it individually.
[54:18] So yeah, it was the Z location, you just go in here, maybe change that back to bezier. And then
[54:24] right there where it actually that got rid of it. So yeah, you could just leave it at bezier. And
[54:29] that might be actually what I did end up doing. So now it just kind of settles in there. And you
[54:33] know, I think it adds kind of a nice another little detail where this is just separate, you
[54:36] could even go in and separate the lenses, more different pieces, more action, always going to
[54:42] be a little more exciting. So yeah, that's pretty much how we set that up again, lighting,
[54:46] pretty basic here. Now this one, since we were kind of zoomed in, I probably gave this a little
[54:50] extra depth of field. Yeah, stop there is a little bit lower than the other scenes. But yeah,
[54:55] that's that's how we set that one up. Pretty basic. Besides that, yeah, let's move on to the next one.
[55:01] So let's get rid of that collection. We'll take a look now at the next one, which I believe was the


### Animation 4 (Double Reveal w/ Multiple Colors) [55:04]
**Transcript (timestamped):**
[55:08] double reveal. And so now this is where we get into talking, you've probably been looking at this
[55:13] thinking Derek, when are you going to tell me how to add that. So this one, we got into a little
[55:17] more syncing with the audio. Let's press Ctrl zero to take a look at this. Now for this one,
[55:23] instead of just doing it from frame one to 68, and then just stacking those clips on top of
[55:28] each other. Since this had a little part that was kind of more synced up with the audio, I wanted
[55:32] to actually animate this at the proper point in the animation. So so for this one, I had these
[55:38] frames out here. So this one actually kind of pops out. So this one, this one would have ended,
[55:44] I think, yeah, right around frame 271. So 271. And then this one started, I think we probably
[55:52] started with some camera movement. So then, yeah, that would have been back here at about 205.
[55:58] So for this one, we've got the camera just kind of moving in. And then there's that little part
[56:04] of the song where it goes like, let's take a look at that. So let me show you to how to add in this
[56:10] so that you can actually work with these with this waveform while you're doing your animation. So let
[56:15] me let's just press X to delete that strip. And then you know, this would be kind of what you would
[56:20] start with is not having an extra window. So you would just, you know, drag out a new window here,
[56:26] give yourself some space. And then we would change that top window here to a video sequencer.
[56:33] And then you just go in and press add. And then you would add a sound. And what you want to do is
[56:38] maybe move your cursor or the current frame that you're on to frame zero. So when you add it in,
[56:44] it'll add it there. Let's do add and add a sound. And then you just need to go in and add your audio
[56:50] file. And again, if you want to use the actual audio file, I'm going to put that on my Patreon so
[56:54] that you can check it out. And that's actually going to be free for everybody. You don't have to
[56:58] be a patron. But if you do want the full file, that is going to be just for the patrons. So thank
[57:03] you patrons for your support. So yeah, we've got the audio file in there. Now to get the waveform
[57:08] displaying, you need to go into view and then for let's see waveform displaying, turn it on pretty
[57:15] straightforward. And now you can see it. If you want to make it zoomed in a little more,
[57:19] you can kind of adjust this bar over here. And then yeah, that'll just give you a little more
[57:24] little more view of it. So back over here, let's, I think when I added this in, it should be
[57:29] unmuted. Now let's press spacebar to play this. Yes, so there was this little part here. So the
[57:35] reason I had the waveform in here and why I did this on this actual part was that I so that I
[57:39] could go in here and see exactly where that happens. You can see that's where that little peak is
[57:43] is where it makes that kind of nice sound. And that's where one of those phones to kind of split
[57:49] apart. So set the keyframes right there. And, and yeah, the rest of this animation is pretty basic.
[57:54] You know, the, the camera is just moving in. And then the phones just, I'm giving them a little
[58:00] bit of X location animation and then also some rotation. So that kind of, you know, get that
[58:05] nice little spread apart there. And yeah, same thing with the easing here. So I've got them,
[58:11] if we look at the graph here, this is just going to be that same quadratic easing. So you just press
[58:17] T, you know, you would start off with a, with a bezier, bezier, however you say it. And see how
[58:23] that doesn't look as good when it's like, when you've got that easing there. Don't want to do that.
[58:29] So, so we changed that to the quadratic. So we press control E, and we're sorry, we press T and
[58:35] change it to quadratic. And then, and then it's much nicer kind of snap. And again, this is just
[58:40] a stylistic thing, but you may want to use some of these same techniques in your own animation
[58:44] to help really sync up with the audio. I think it looks, it looks really good. So lighting here,
[58:50] also very similar, maybe added in a couple more. Since this scene is a little more dynamic, where
[58:55] we've got kind of things facing one way and then facing another, maybe had to add in a
[59:00] couple of extra lamps for that reason. But besides that, we just cut a little box in here.
[59:06] This is actually the same box I had in the NC. And I just wanted to make sure they matched
[59:10] but yeah, not gonna really, I'll talk a little bit about how that's modeled. But
[59:14] it's just kind of a nice element to have in the background there, give us a little bit more
[59:18] interest in the composition. Now, in terms of creating a second color phone, that's pretty
[59:23] straightforward. You're basically just going to take your phone model, shift D to duplicate it.
[59:29] And then what you can do is just go into the materials here. And then, you know,
[59:32] if you want to make a new material, just do that. And then you can call that, you know,
[59:37] maybe like phone body, pink or something, whatever color you want to do. You got the girls edition
[59:43] because girls like pink, right? Just kidding. So you could go in here then and just adjust the color
[59:49] to something different. And then you would have basically a new version of your phone.
[59:54] And that snapped back because it got the same keyframes. But that's all you need to do. You
[59:59] could do the same thing for the bumper to give that, you know, a different color so that matched up.
[60:04] And you could do the same process to give these all, you know, their own unique screens or something
[60:08] like that. But really simple way to make different colors there. So let's just delete that.
[60:13] And now what we'll do is check out the next scene. And if you guys, I know I'm kind of
[60:19] blasting through these, but really we covered the basics of what's going on when we did that first
[60:24] setup where you're basically just, you know, getting the animation, how you like it, adjusting
[60:28] the lighting, adjusting the animation, adjusting the lighting, just kind of back and forth until it
[60:32] looks nice. So let's, let's get rid of that one. The next scene we took a look at was the dark single,


### Animation 5 (Float Across Screen in Black Environment) [60:36]
**Transcript (timestamped):**
[60:40] I believe. And this is where we have the dark phone. Let's, uh, the dark dirt phone. Let's move
[60:48] into our camera view here, control zero, and take a look at what that's doing. So this one again is
[60:53] back on, back on that basic where we're just going from frame one to frame 68. And I'm going to mute
[61:03] the audio here. So that one's just, yeah, it's just kind of fading in there, going from left or sorry,
[61:11] right to left. And, uh, and yeah, this is another just thing to think about, you know, maybe you
[61:15] do want to end up adding some text in there. Like I, I didn't even know what I was going to add,
[61:19] but I just knew I wanted some text. So just consider, um, you know, maybe some animations
[61:23] being a little lopsided and having everything in the center so that you can have some space to put
[61:27] text. And of course the background here was black. So, um, if I actually look in my floor material
[61:33] here, so I've just got two RGB nodes. So to add that, you just do shift A, input RGB, and I just
[61:40] switched between these. So I just got the two colors there. And that was an easy way for me to kind
[61:44] of alternate between those two. So with that in there, um, that's basically all that's happening
[61:49] here. Uh, all I did was animate the, the Z rotation and the X rotation. And then the X location,
[61:56] obviously is wrote, is, um, changing as well. And then once again, same thing here, just easing
[62:02] into it with that same quadratic. So, you know, T to change that to a quadratic, and you could try
[62:07] some of these other ones if you wanted. You can see exponential moves a little faster,
[62:12] nice quick flip. But I end up usually just using that quadratic because it's a,
[62:16] it's a little more steady. I like it a little more. Um, so yeah, that's pretty much it for this.
[62:21] You know, I could have added, added in all the keyframes here, but sometimes it does look a
[62:26] little smoother if you're only animating on a couple of those values. So, so that's what I'm
[62:30] doing there. Um, so yeah, lighting once again, very similar, just making some adjustments. Anytime
[62:36] you've got the object moving a lot, you might have to do more with the lighting to make sure
[62:41] it's getting everything. You can of course animate the lamps as well, but I tend to try to avoid
[62:47] doing that just because, you know, a lot of times I'm trying to mimic a real studio setup and, uh,
[62:52] and there would not be that much movement in the actual lights. Those would usually be more static.
[62:56] Of course, you also don't usually have flown phones floating in midair. So, um, maybe that
[63:02] realism is a little pointless, but that's my theory there. Maybe I'm just trying to save myself some
[63:06] time. Anyways, let's take a look at the next scene, which was the float double and a pretty basic


### Animation 6 (Double Floating) [63:07]
**Transcript (timestamped):**
[63:13] scene here as well as you can imagine. Um, there is one thing I would say I would have done differently
[63:19] here though. And, um, so these were just into individually animated. So I inserted all the
[63:25] keyframes for each of these on, um, and the start and then again on the end, um, just add it in all
[63:32] the keyframes there. Um, I think an easier way, you can see these are kind of like, it's almost
[63:38] intersecting a little bit and they're not like nice and straight. I think what I would have
[63:43] rather done is maybe while they were, um, you know, while the rotation was all even and for
[63:48] example, all are by the way, that's kind of a cool shot. I should have done that. Somebody do that
[63:53] that's cool. Um, I would have maybe parent this all to an empty and then rotate the empty. So then
[63:58] to have these kind of slide against each other, I would only have to animate like a couple values,
[64:04] but, um, didn't do that way. Learn from my mistake. Maybe think about using an empty when
[64:09] you've got two phones at kind of a weird angle can make the animation a little bit easier.
[64:13] Lighting here, basically the same thing. And with the lighting, I'll just talk really briefly.
[64:19] It is, you know, I like to use again as little lights as possible. And then also in most scenes,
[64:24] try to use pretty much the same lights because then you start to really develop an understanding for
[64:29] what each light is doing. And it becomes a little easier to make, uh, the adjustments from one scene
[64:33] to an X when you really, um, you kind of do that. It's that repetition that just kind of helps you,
[64:38] um, understand what each light is doing and gives you a little more control. And, um, and yeah,
[64:43] okay. So this one, so there's a light down here. So this is same thing I was talking about earlier.
[64:48] Let's see if we can find that light. So yeah, I noticed that in some of the other scenes,
[64:53] I didn't need this, but in this particular scene with this lamp, um, so with that not there, it
[65:00] was just, I noticed, you know, it's kind of breaking my own rules where this was just a little too dark.
[65:05] And, um, this was the only scene I think where we actually even saw the bottom. So I wanted to make
[65:09] sure we could show it. Um, but just adding a lamp there. So we have a nice highlight on the bottom.
[65:14] And there's no completely, uh, lost detail on any part of the phone. You can see it's a little dark
[65:19] down here, but we've just gotten some barely nice highlights there. And, and that helps just kind
[65:24] of show off the entire object. And then same things we did earlier where we just got the, uh,
[65:29] reflections kind of moving nicely across where that logo gets illuminated. You see the reflection
[65:35] in the lens. And, uh, yeah, it just looks, uh, looks nice. So that's it for that one. Let's take


### Animation 7 (Multicolor/ColorSwap + Basic Box Model) [65:40]
**Transcript (timestamped):**
[65:40] a look at that last scene, which is probably the most, uh, most dynamic, most interesting thing
[65:45] happening. Um, and that is this scene I called color swaps. So let's just take a look at that
[65:50] real quick. This one all happened also on the, um, actually on the frames because there was obviously
[65:56] a lot of audio syncing there. Um, so this one started, uh, somewhere over here. I think it would
[66:02] have ended at, so the whole animation was 20 seconds and 30 frames per second. So yeah, it ended at
[66:06] frame 600 and this would have started at wherever I first animated that camera. So that would have
[66:16] been right there around frame 409 where this started. Um, so on this one, let's find that place in the
[66:23] audio track and let's unmute that audio. Let's actually, but before we do that, let's just play
[66:28] it so you can see what's happening in the scene. So we've got the camera kind of panning in and
[66:34] out with the beat and then the phone is also, uh, rotating and then it all kind of snaps down
[66:40] together at the end. So let's watch it this way. Oh, and we need to actually set the camera here,
[66:47] control number, head zero. So you can see again, just pop, pop, pop, and then kind of that final
[66:54] zoom in when that slams down. So let's listen to it with the audio. So let's unmute that.
[67:07] So just a couple of things happening there. There's this really interesting kind of part at the end
[67:14] Yeah. Andrew put a really nice little kind of ending part there where it's a little different
[67:18] than the rest of the song. And I just thought that would be a good opportunity to maybe kind of tell
[67:23] this story of, you know, different color options. You know, you see that a lot in commercials where
[67:27] they're kind of showing the, the variations that are available and kind of the way you can personalize
[67:31] the product. And, uh, and yeah, so I thought that was a good way to do that. And I, uh, you got to
[67:42] watch this stuff like hundreds and hundreds of times, maybe not hundreds, but, uh, you definitely
[67:47] like just, you'll kind of drive yourself mad listening to, especially if you're singing with audio
[67:52] as beautiful as the little song Andrew put together is you just watch it over and over and over until
[67:58] until you've got your curves all right and make your joints looking good. But
[68:02] as for those curves, same thing happening as with the other ones here. Just got that same
[68:07] quadratic animation where it's just kind of snapping back and forth. So let's, uh, and yet the way I
[68:14] would have set that up is just again moving in here, looking at these little, um, these peaks
[68:20] and stuff to know when that stuff happens and then animating according to that. So same thing
[68:25] here where this slams down is I think probably right there. So yeah, there's kind of like a
[68:30] little pop right there. So just a little stuff like that ends up, um, when you can, when you can
[68:39] sync a lot of stuff to the audio, it ends up really kind of, I feel like connecting with the
[68:43] viewer. That's something that's really important to getting a really nice looking kind of final product
[68:49] with something like this. Um, so let me talk to you just a little bit how we did the color switch.
[68:54] That is happening in the materials here. So yeah, we've got a, I have a floor changer material,
[69:02] which is pretty simple. Just we've got that same RGB value and you can actually keyframe the color.
[69:08] So this is starting off on this orange material. We can see right here, I've got a keyframe. So
[69:14] you can see this outlined yellow. We've got a keyframe there and then one frame forward. So
[69:18] that happens instantly. It changes to this darker color. And then over here, we've got another
[69:22] keyframe indicating that it's this dark color and then one forward changes to the white. So
[69:28] that's how the floor is changing colors. And I think this box, okay, so I had a, I used the same
[69:36] material on the box as I did on the floor and the logo. So there was a little bit of a logo
[69:42] there. It's kind of hard to see what the, with the white, but I did actually end up adding a
[69:47] little bit of detail to that box. You can see we've got the Dirk.com down there. Same techniques we
[69:52] did in the box tutorial. I'm not really going to talk too much about how that set up, but
[69:57] so that that changed as well. I had to make another material there, but for the phone
[70:02] changing, basically I could have just animated the color, but with this orange one, I wanted it to
[70:09] be more like a plastic material. So what I did is I got that set up and I could have just animated
[70:14] this metallic value as well, but I got the orange material set up the way I liked it.
[70:19] And then what I did is added a mixed shader and that was mixed with basically the metal material.
[70:26] And since the black metal and the lighter color metal, all the settings were the same other than
[70:31] the color. All I did was just keyframe that, but to get the orange, so it started with the orange
[70:37] and I did that with a mixed shader. So it's all the way to one. So it's just getting that orange
[70:41] material and then it snaps to zero. And then that's when we're feeding in from this metallic
[70:47] material, metallic material. And then it's just keyframed to pop to white right there.
[70:55] And then, and then yeah, that's pretty much it. And then it settles into this object,
[70:59] which I added this little detail here, like that's a little packet that like chords would come in or
[71:05] something. Didn't even really end up seeing it. What a bummer. But this is basically just, yeah,
[71:11] it's like a simple box material. It's like just, yeah, it's just, there's not a whole lot of detail
[71:18] going on there. And to add in all those nice bevels and stuff, basically what I did is just in my
[71:23] bevel modifier set the limit method to weight. And the first thing I would have set up was this,
[71:28] this largest bevel size to control those outer edges there. Just kind of line up with the phone so
[71:34] that it kind of seats in there really nicely. And then I would have just gone in and adjusted the
[71:39] weights on these other edges, you can see this edge is a, it's like a point, yeah, point two bevel
[71:45] weight, just to keep that nice and sharp. And yeah, I just adjusted these in different places so that
[71:50] I really had a simple geometry to work with and all the magic's happening over there in
[71:54] my favorite modifier, the bevel modifier. So that's pretty much it.
[72:01] Up and back and forth. And then, yeah, this is up here the whole time, just out of view,
[72:05] you can't see it. And then it slams down there right at the end. The Dirk logo here could have
[72:11] been done as a texture, but I actually just kind of cheated, used it or used it. I used the images
[72:18] as planes import feature. So shift a image images as planes, you just import your logo, slap it on
[72:25] there, do whatever you want. Pretty simple. That's an add on you do have to enable it comes with
[72:30] Blender though, so just search for it and pop it in there. But that about wraps it up folks. I hope


### Wrapup + THANKS [72:35]
**Transcript (timestamped):**
[72:37] you enjoyed this walkthrough. This isn't the same type of tutorial, I normally do where I kind of do
[72:45] everything ahead of time and then kind of walk you through it after the fact. Let me know what you
[72:49] thought about that. I thought this was going to be like a short quick tutorial, but of course,
[72:55] it turned into an extremely long one. But let me know if you don't mind that it was long or
[73:02] if you want to leave nasty comments, tell me about how the next one better be shorter. I really do
[73:07] want to eventually put some like 20 minute tutorials again together. But I really like these
[73:14] more polished ones. I think it's really easy to get carried away with just quick little easy stuff.
[73:19] I like that. But sometimes for your own sake, it is good to take a little more time looking at the
[73:26] different parts of a project and really putting in the time to get a nice polished piece. That's
[73:31] something you can put in your portfolio and use to get some freelance work. A lot of people ask me
[73:36] like, do you do Blender for a living? The answer is yes. One of the reasons it took me so long to
[73:42] get this tutorials out was because I had a big freelance project. I'm doing work completely in
[73:48] Blender and making a living using Blender. So hopefully from this tutorial and some of my other
[73:54] tutorials, you guys can get some knowledge. And of course, there's a lot of other good tutorials
[73:59] out there. So just keep practicing. Don't get too frustrated. Blender is a really amazing
[74:03] style for you. Definitely can make a living doing it. As you can see, you can make some really cool,
[74:10] really cool stuff with it. So thank you guys for watching. If you want this full tutorial file or
[74:15] sorry, the full file here, I'll have it on my Patreon and you can check that out. And then the
[74:20] audio file we're also going to have available even if you're not a patron, but you'll be able to
[74:25] download it on the Patreon so that you can use that in your own projects. But thanks for watching.
[74:31] Please feel free to give me a thumbs up if you liked the video. Leave a comment. Let me know what
[74:35] you thought. Again, this is kind of a different format for me. But if you liked it, let me know.
[74:41] I would love to hear from you. And please be sure to tag me on Instagram with whatever you come up
[74:47] with. I'd love to see it. I'd love to see all your hyper duper cameras. So anyways, thanks for
[74:53] watching. I'll see you next time.



---

## Captured Frames

- [3:40] tutorials/frames/product-animation-in-blender-phone/frame_000.jpg
- [9:00] tutorials/frames/product-animation-in-blender-phone/frame_001.jpg
- [13:20] tutorials/frames/product-animation-in-blender-phone/frame_002.jpg
- [16:20] tutorials/frames/product-animation-in-blender-phone/frame_003.jpg
- [18:10] tutorials/frames/product-animation-in-blender-phone/frame_004.jpg
- [26:10] tutorials/frames/product-animation-in-blender-phone/frame_005.jpg
- [32:20] tutorials/frames/product-animation-in-blender-phone/frame_006.jpg
- [48:15] tutorials/frames/product-animation-in-blender-phone/frame_007.jpg

---

## Structured Notes

### Core Technique
Full EEVEE product-commercial pipeline for a phone: Boolean-based hard-surface modeling, PBR/glass/emission materials, manual studio-style lighting (no HDRI), and beat-synced keyframe animation across seven short looping scenes.

### Summary
A long-form, full-pipeline product-animation walkthrough: models a stylized phone from the default cube using Bevel + Solidify + Boolean cutouts (frame_000–frame_003 confirm the bevel-modifier rounded shape, port cutouts, and headphone jack), materials it with a metallic body, glass camera lenses, and an emission screen playing a live video texture, lights it manually with one Point Light plus several Area Lights against a seamless backdrop instead of an HDRI, then builds and breaks down seven short beat-driven scenes — a basic pan, a shape-key button press, an exploded camera-cluster reveal, a two-color reveal, a black-background float, a double-floating shot, and a multicolor color-swap finale — all rendered in EEVEE and synced to an audio track's waveform in the Video Sequencer.

### Key Steps
1. Model the phone body from the default cube: scale it to 0 and Merge by Distance to get a flat plane, add a Bevel modifier (Only Vertices, ~10–11 segments) for rounded corners, a Solidify modifier for thickness, and a second Bevel modifier (Limit Method) for the outer edge chamfer (frame_000 shows this exact rounded-rectangle result with the Bevel modifier panel open).
2. Cut ports, buttons, and a headphone jack into the body: duplicate the beveled plane (modifiers still active, not applied) into rough port/button shapes, move a copy set into a "trash" collection, apply the modifiers on those cutter copies, Merge by Distance to clean up bevel-intersection duplicate vertices, then add a Boolean modifier (Difference, eyedropper-picked target object, Bounds viewport display for clarity) on the phone body to carve the shapes in (frame_001 and frame_003 show the resulting port cutouts and headphone-jack slot on the beveled body).
3. Detail the cut holes with Inset (I) + Extrude (E) + a small Bevel to make raised or recessed buttons, and enable Shade Auto Smooth to keep edges crisp without adding geometry.
4. Build the camera cluster on the back: snap the 3D cursor to a face (Shift+S), add a circle, extrude inward then up and bevel for each lens housing, add edge loops so pulling the lens rings out stays straight, then Fill (F) + Inset + Extrude to seat each lens flush; duplicate an outer ring and Separate (P) it to become the cluster's cover glass.
5. Material pass in Look Dev / automatic-HDRI mode: rename the default material (e.g. "PhoneBody"), give it a metallic base color; add a black material for interior camera housings (Roughness 1); add a glass "Lens" material (low roughness, Transmission = 1, Blend Mode = Alpha Blend/Alpha Hashed, Settings > Shadow off in EEVEE — frame_004 shows this glossy blue lens material with its color/roughness panel); add a "Glass" material for the cluster cover lens; add a "Screen" material using an Emission shader fed by a movie-clip Image Texture (UV-unwrap the screen face with Smart UV Project, set the clip's frame count, enable Auto Refresh so it plays back live in the viewport — noted as Blender 2.8-era functionality).
6. Set up manual studio lighting instead of an HDRI: zero out World strength, add a seamless backdrop plane (shaded smooth, near-white ~0.9 roughness material), place one Point Light near its edge for both key illumination and a rim-light edge highlight, then add several Area Lights (Disc shape) around the object — duplicating/rotating per shot — tuning size/power per light until every face reads without pure-black or blown-out spots; adjust the camera's Focal Length (~80mm) to flatten perspective distortion (frame_005 shows the shiny phone front with composition-guide grid overlay under this lighting setup; frame_006 shows the camera object and its Focal Length/Depth of Field properties panel).
7. Animate a beat-synced loop: derive frames-per-beat from the track's BPM at a fixed frame rate (30 fps → 68 frames/beat for most scenes), key start/end rotation/location, then set interpolation to Linear for steady pans or Bezier→Quadratic + Ctrl+E Ease Out for a fast "snap-into-place" beat hit — reused across all seven scene variants.
8. Add camera Depth of Field: enable DOF on the camera, create and name an Empty ("focus") as the Focus Object, animate the Empty's location with Linear interpolation alongside the camera move, and dial the f-stop back from an extreme test value to a subtler one (~4).
9. Shape-key micro-animation (Animation 2): add a Shape Key (Basis), add a second key, in that key select the button face (Ctrl+Numpad+ to grow the selection) and move it (G, Z), then key the shape key's Value slider (0 → 1) on the beat for a snappy button-press pop (frame_007 shows this exact Shape Keys panel — Basis/Key 1, Range, Interpolation, Vertex Group — alongside the Video Sequencer's audio waveform used to time the beat).
10. Exploded camera-cluster shot (Animation 3): separate the joined mesh into individual island pieces (Edit Mode, L to select linked, P to separate by selection), parent all pieces to the main phone object (Ctrl+P, Keep Transform) so rotation stays correct, then animate each piece's local Y/Z location from an exploded start position back to a Quadratic-eased settled end position. For beat-exact syncing on later scenes, add the audio file in the Video Sequencer (Add > Sound), enable View > Waveform, and place keyframes directly on the waveform peaks. For the finale color-swap scene, keyframe material values directly — two switched RGB input nodes for the floor color, and a Mix Shader blended between two metallic color variants for the phone body — so everything snaps to a new color on the beat.

### Nodes / Settings
- Modeling: Bevel (Only Vertices; separate Bevel w/ Limit Method + bevel weight for hard-surface edges), Solidify, Boolean (Difference, Bounds display mode), Shade Auto Smooth
- Materials: Principled BSDF variants — "PhoneBody" (metallic), black interior (Roughness 1), "Lens" (low roughness, Transmission 1, Blend Mode Alpha Hashed/Blend), "Glass" (cluster cover), "Screen" (Emission + Image Texture / movie clip with Auto Refresh, UV via Smart UV Project)
- Color-swap finale: two RGB input nodes switched (floor), Mix Shader between metallic color variants (phone body), both driven by keyframed node values
- Lighting: World strength = 0; 1 Point Light (key + rim); several Area Lights (Disc shape, size/power tuned per shot); backdrop plane ~0.9 roughness
- Camera: Focal Length ~80mm to flatten perspective; Depth of Field with a named Empty ("focus") as Focus Object; f-stop dialed to ~4
- Animation: 30 fps, ~68 frames per beat-driven scene; interpolation Linear (steady pans) or Quadratic + Ease Out (snap beats); Shape Keys (Basis + posed key, keyed Value) for the button press; Ctrl+P Keep Transform parenting for exploded-view pieces
- Audio sync: Video Sequencer, Add > Sound, View > Waveform enabled to read peaks for keyframe placement
- Render: EEVEE with Bloom, Screen Space Reflections, and Soft Shadows enabled; output via FFmpeg/QuickTime at Perceptually Lossless quality

### Difficulty
Intermediate/Advanced (assumes comfort with modeling, materials, and keyframe animation; covers a full 75-minute production pipeline with many EEVEE-specific settings)

### Blender Version
Blender 2.8 (creator explicitly names it while demoing live video-texture playback in the viewport)

### Tags
materials, shaders, glass, metal, eevee, lighting, animation, camera, product-viz, brand-video, intermediate

---

## Related Tutorials
- [Realistic Product Lighting In Blender](realistic-product-lighting-in-blender.md) — shares lighting, product-viz, materials, glass, brand-video, intermediate
- [Credit Card Texture and Animation SaaS FinTech [PART-1]](credit-card-texture-and-animation-saas-fintech-part-1-blende.md) — shares materials, shaders, animation, product-viz, brand-video
