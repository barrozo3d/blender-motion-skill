---
title: How I Made This Awesome MRI Effect In Blender
source: YouTube
url: https://www.youtube.com/watch?v=4cy1i9THUQg
author: Nick Impson
ingested: 2026-08-09
blender_version: "5.1"
tags: [mri-effect, x-ray, cross-section-reveal, ray-visibility, light-linking, wave-texture, gradient-texture, subsurface-scattering, compositor, color-correction, film-grain, product-visualization, cad, grabcad, blender-5.1]
extraction_status: complete
frames_dir: tutorials/frames/how-i-made-this-awesome-mri-effect-in-blender/
frame_count: 9
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How I Made This Awesome MRI Effect In Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=4cy1i9THUQg)
**Author:** Nick Impson
**Duration:** 18m20s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Okay, welcome back to the channel. In this video, we're going to go over how I make this
[0:20] super cool MRI effect inside of Blender. I love adding this to a lot of client projects.
[0:25] Most recently, I did it for a Kawasaki KPM project where we made this really cool environment
[0:29] that's kind of Studio Tendril inspired. And then basically a pump gets selected. And then
[0:32] on the background of that, there's a screen that's got like a wireframe effect, then it
[0:35] also has this MRI effect. And it's super good. It kind of showing all the complexity that
[0:39] goes inside of these objects. I work with a lot of CAD, and actually have a video coming
[0:43] out next week about that. But in this video, I just want to show you how you make this
[0:45] MRI effect in Blender. So let's go ahead and jump over into Blender. And then I'm going
[0:48] to also show you where you can get some really good assets to add this MRI effect to. Okay,
[0:52] here we are inside of my default Blender 5.1 scene. The first thing that we're going to
[0:55] need to do is add some geometry to this scene. I'm going to talk about this in my video next
[0:59] week about CAD and my CAD to render workflow. But I'm just going to show you a good resource
[1:03] that we can use to kind of find some models that have really good complexity and then
[1:06] bring that into Blender. Okay, the website I'm going to recommend to you is grabcad.com.
[1:10] You can see it here on my screen. Basically, people upload tons of really awesome files
[1:13] that they've made, you can download them and use them in different types of projects. I
[1:16] typically don't stick with these for a commercial project, just because I'm not entirely sure
[1:20] whether or not the licensing would work. So make sure you do your research on that. But
[1:23] basically, I just wanted to create an effect similar to the one that I did on my client
[1:26] work, but not really show the client work. So I just wanted to find some type of engine
[1:30] or 3d model that I was going to use. I just searched for a v16 engine. This one popped
[1:34] up by Sanny Patel. And what's cool about this model is it's already an OBJ file, which
[1:38] means you don't have to do any like CAD conversion and like a different program. So I'm just
[1:41] going to go ahead and download this file, you can download it from this link here. You may
[1:44] have to create an account to do that. But once you've downloaded this file, you just
[1:47] bring it into Blender. You can also use any other 3d object that you have, you know, available.
[1:51] I just want to show you this resource because it's really good. So let's go ahead and download
[1:53] this and bring it into Blender. Okay, back inside of Blender, I'm going to press F4 and
[1:57] do import and then look for a way front because I know this is going to be an OBJ file. Once
[2:00] you click that, you can just navigate to whatever file you've got downloaded as long as in the
[2:04] dot OBJ format and then bring that into your scene. Okay, I went ahead and imported that
[2:07] and not seeing anything in my screen. And I know that if I go to the item here and I
[2:10] look at the dimensions, it's basically enormous. So I'm going to head and scale this down.
[2:13] Typically, it's going to be by a factor of 10. So I'm just going to guess to be 1000 because
[2:17] of how big this is. I'm going to press S and then do 0.001. And then when I do that, you
[2:21] can see it kind of comes in here to a scale that we expect. I'm going to do Ctrl A and
[2:24] just apply the scale here. And then I just want to rotate this around a little bit. So
[2:27] I'm going to rotate it here. Just kind of want to put this in the center of the world
[2:30] origin and then maybe do the same here on the front, something like that. I'm going to
[2:33] right click and then do set origin to the 30 cursor. And now if I am on that individual
[2:38] origins for the pivot point, which I also can change up here, I can just trackball rotate
[2:42] this and go crazy with it. Okay, so yeah, this is basically what I want. So now we basically
[2:46] have our model here. And what we want to do is basically create an effect where we slice
[2:50] through this. Now there's a couple different ways we can do it. The way the first way that
[2:53] I think works really well is you basically have a plane, and you're not using any thickness
[2:57] in the plane, you're basically kind of slicing with that, which you're also getting some
[3:00] internal like bounce lighting and stuff, which looks really good. And then there's also another
[3:04] method that's really common that I think folks that are in cinema 4D do where you have a
[3:07] really thin cube that has some subsurface scattering on it. So I'm just going to show
[3:10] you how we set that up. The first thing I want to do is set up a little bit of a camera
[3:13] view here. I'm going to make this a vertical render because it's a little bit easier to
[3:15] show for a tutorial. I'm just going to drag a new window out. And then over here, I'm
[3:19] going to turn my camera collection on. I'm just going to do Alt G and R to reset the
[3:23] location rotation of this. I'm going to rotate it up here. I'm going to rotate it to this
[3:26] side. I kind of want to look at this along the longest axis just because that's going
[3:29] to give me the most kind of depth here. And then I want to make this a vertical render.
[3:33] So over here in the output settings, I've made a little add on that gives me these little
[3:36] presets. If you want that, just comment to me and I'll either put it on Patreon, or I
[3:40] can either send it directly to you. So I'm going to make this vertical and then over
[3:43] here, I'm going to go into camera mode, just kind of set that up by pressing zero on my
[3:47] Numbaki. Sorry, I'm stumbling over my words. I'm going to press G X and just kind of move
[3:51] this back. So now we basically have our object here, but we want to start to add this little
[3:54] bit of a slicer. So I'm going to put this object here in the product collection, and
[3:57] we're going to do a little bit of light linking. So it's kind of important to stay somewhat
[4:01] organized here. So I'm just going to grab this environment and do shift a add in a mesh
[4:04] plane. I'm just going to rotate this along this axis. And then I'm not going to use this
[4:08] right at the very beginning, but I'm going to go ahead and make this have a little bit
[4:11] of depth. So let's have an edit mode on this object. And with this face selected, just press
[4:15] E and just move this back here. And then basically, we're going to animate this to kind of cut
[4:18] through this object. So let's go ahead and add our keyframe animations. I'm going to
[4:21] make this go from one to 150. I have mine set to 30 frames per second by default. I'm just
[4:26] going to press G X and go all the way over here. We can't see anything. And then on frame
[4:29] one, I'm going to press K and then insert a location keyframe, go to the very end G X
[4:34] to bring it all the way to the other side. EJ from my school motion hates that I've
[4:38] pressed G X. He wants to use the gizmos, but sorry, EJ, this is just how I do it. K to
[4:42] insert another location here. So now if we scrub our timeline, you see we get this kind
[4:45] of effect. And over on the right hand side, you can already see this is already just a
[4:48] cool effect. We're just getting that really nice kind of reveal of this product. This
[4:52] looks like a little robot character to me. It's like, do do do do do. But anyway, it's
[4:56] definitely not a character. So now what we want to do is start to set up a little bit
[4:59] of the lighting for the scene. And I want to kind of think about it a little bit procedurally
[5:03] before we kind of get into how to do it just because I kind of want to explain to you why
[5:06] what we're doing as opposed to just showing you the steps to do it. So basically what
[5:10] we want is we want to be looking at this and we want to see some type of interaction with
[5:13] this geometry with this plane, but we really don't want to see this geometry. So like I've
[5:17] seen people try to create a shader where they make it transparent or opaque or you know,
[5:21] fully alpha removed as you move across and that way just doesn't give you as good of
[5:25] a interaction with this cube. So a really good trick that we can do to do this is we
[5:29] can change the ray visibility. So I'm going to go over here and just in this area, I'm
[5:33] going to make this a little bit cleaner. And then with this object selected, I'm going to
[5:36] scroll down here to these ray visibilities and we're going to deselect some of these that
[5:39] we don't want to use for this render for this object specifically, I definitely don't want
[5:42] it to be in the camera. So I'm going to go ahead and turn that off. And that means that
[5:45] when I go here into render mode, you basically see that we're not going to see anything related
[5:48] to this object. And it's a little bit dark because I have a low HDR. Let me just crank
[5:52] that up a little bit so you can see. So basically, we don't see that we're only seeing how it's
[5:56] basically intersecting with this plane. And that's kind of the approach that we want to
[5:59] go for this. So with this one, we're just going to make sure that we have over here in the
[6:02] shading. So with this object selected, go back to our object, go down to the ray visibility.
[6:07] We don't want camera and I also typically turn off the rest of these, I just have found that it
[6:10] works a little better. And the biggest one that the most important is this volume scatter, or
[6:15] no, I think it's shadow. Yeah, basically, if we turn off shadow from this, that's going to really
[6:18] help us get this really nice transparent effect where light kind of bleeds through it in a very
[6:22] convincing way. And that is just one of the main things of this effect. So I'm gonna go ahead and
[6:26] do that. And then we need to start to set up a shader for this object and then also for this
[6:30] plane. Before we do that, I want to just change this material. I think to them that works really
[6:34] well is to give it a black metal material. This object came with these default materials from the
[6:40] grab cad website. So I'm just gonna go ahead and remove all those by just pressing minus, click
[6:44] all the way through them till we get to the very bottom. And then now I can add a new material
[6:48] with this selected, I'm just gonna make this a totally black metal. So crank them attack all
[6:52] the way up and the reference all the way down. I just found that it makes a really nice effect.
[6:55] And again, when we set this up, you can then take this effect and you can tweak any of your
[6:59] materials or lighting setups or anything that you want to do to make a little bit of a different
[7:02] effect. But okay, now we basically have this setup here. The only thing that I also want to do is I
[7:06] don't want to use an HDI I want to basically control this lighting. So I'm going to do here is just
[7:10] turn off this HDI. So in my world strength, I'm going to set this to zero. And then in my lighting
[7:14] collection, let's go ahead and create a new light. So I'm going to shift a and just add in a light
[7:17] area. I'm going to go into front end mode here and then just kind of rotate this around and rotate it
[7:22] this way. And I'm just going to bring this over here to this side. And so then what I want to do is I
[7:27] want this light to be relative to this plane, I want to kind of move and be animated. So I'm going to
[7:30] grab this light and then shift select this and then the control P object key transform. Okay, and now
[7:36] we basically lost you can kind of see it there. It's very faint, but we've kind of lost the effect that
[7:40] we wanted to create. And the way that we fix this and this is what changed the making it in blender
[7:44] for me was really cool. If we think about it again procedurally, I don't want there to be a lot of
[7:48] light on this object. I really want that to be only influenced by the bounce light and the things
[7:52] happening with this object. So what I'm going to do is I'm going to grab this. And we've already put
[7:56] this plane in this environment collection, we need to do a little bit of light linking. So let's grab
[7:59] our light here, let's go to the shading for it, go down to light linking and then press new, I'm going
[8:04] to drag in this environment. And then that's basically going to be basically the same because this light
[8:08] really isn't affecting this object that much. But if we flip it, now we're going to start to get this
[8:12] effect that we are looking for where we're basically having some bounce lighting some things that are
[8:15] happening with the geometry in this plane, but it's only be infected, you know, basically, the light
[8:20] is hitting this object, it's influencing and then that is being cast on this plane as opposed to this
[8:24] light, you know, doing anything with that. That's basically the base effect for this. So I'm going
[8:28] to go ahead and crank this up to 500. And already this is looks so so cool. This is such a good effect
[8:33] for kind of revealing all the different, you know, complex geometry, like look at this area right
[8:37] here with these like kind of screw I'm not sure what these are, but they're like probably the intake.
[8:42] I'm not actually sure what that is. It looks like there's like ball bearings there. So this might be
[8:45] like where these are spinning inside of this or something. Anyway, just so cool. This effect is
[8:49] already super, super sweet. But now we can start to change a little bit of the other things related to
[8:54] this shader on the slicer that's going to be cool. I'm going to show you how to also do the kind of
[8:58] like where we take a specific slice of this as opposed to looking basically at what this is touching.
[9:03] Because if I move this back here, you can see that what is on this is basically the exact front of
[9:07] this. So like this is that point right here, we press GX, you can see those three things coming in.
[9:11] So we're not really doing a thing where we're highlighting this area inside of this, we're only
[9:15] really looking at this front edge. So if you want to do the more the other way, we can set up this
[9:18] new material for this X-ray. Now for this one, we also want to go over here and scroll down to it.
[9:22] And I want to do the exact opposite or basically, you know, do what we did for the other one, but
[9:26] a different way. We only want this plane to be visible to the camera. So I'm going to turn off
[9:30] all these other things here, except for camera. I'm just going to make sure that the bounce lighting
[9:33] is a little bit less and directly changing this here. And then we can create a new material for
[9:38] this. I'm just going to drag this down. Let's make a new material. So for this plane, I'm going to
[9:41] press S and then go into the object set here. So we're looking at the object material, press new.
[9:46] And then for this one, I'm going to do a little bit different than we did previously for the plane.
[9:49] What I want to do is first of all, I want to make a wave texture that's going to basically give it
[9:53] those little at the MRI looking effects. I may put it back on screen here so you can kind of see
[9:57] those individual lines. I'm going to also show you how you could basically create a little bit of a
[10:01] mass to kind of help this effect grayed out if you want to. So the first thing we're going to do is
[10:05] add in a wave texture. So there's just a search for wave texture here. I'm going to press control
[10:10] T with node regular enable. That's going to make sure that we get these coordinates. I want to use
[10:14] the object coordinates here. And then I want to preview this. I'm going to control shift and click
[10:18] basically getting this nice little setup here. I think I changed this on mine to be the saw instead.
[10:23] And I changed it to Z, which I don't know if that actually changes anything, but I'm going to leave
[10:27] this already know that the X was looking basically how I want. I'm going to crank this scale up to
[10:31] like 300. And then if you zoom in, you're basically getting these small little lines here. You can
[10:35] change this as needed. But then what's going to happen is I can basically put this into the color
[10:39] and this into here. And then you see that we get this super, super, super nice effect. That was
[10:43] like a bunch of supers. But this gives you this like, okay, this is being read on like an old TV
[10:48] or you know, something where you're getting these little bit of lines. Again, you could do this
[10:52] with any different texture here, you could use like a noise grain texture. But I really love the
[10:56] way that these lines are looking here. That's going to be the first thing that we do for that.
[10:59] But then the other thing that I might want to do is if I go into camera mode here, this light and
[11:03] white is kind of bleeding off into a bunch of different areas. So what I want to do is kind
[11:06] of affect the the alpha and make this where it basically fades out into black. So what I'm going
[11:10] to do is do shift a and search for gradient texture. And then again, we're going to do control T,
[11:14] make sure that we're using the object coordinate instead of the generated ones. We're going to
[11:18] hear a quadratic sphere. And then if I do control shift and click and preview that, that's exactly
[11:21] what we're expecting. And then now I can just kind of do is influence these values here. I'm just
[11:26] going to bring this down a little bit something like that and then squish it perfect. And then
[11:30] now I just basically want to use this factor to control the alpha. And then when we plug that in
[11:34] here, oh, that's a little bit strong, you may need to take a color ramp and then kind of tweak the way
[11:38] this works. Let's just bring this back and bring this back. And then let's make this a bit bigger.
[11:44] So we might set this back to like one, one. Obviously, this is strong. Oh, the other reason
[11:49] why this is doing that is because I have it set to transparent. So if you go over here to this
[11:53] tab here, we scroll down the film, we turn off transparent, it's going to go off to black. Okay,
[11:57] yeah, that's more what I was expecting. So now I'm going to read delete this here. I'm just going to
[12:01] look at it with this gradient texture. I'm going to do exactly what I did before kind of bring this
[12:06] in and around something like that. You can shape this to whatever size object that you're doing.
[12:10] And so now just plug this back in. That's going to make sure this doesn't get too bright in different
[12:14] areas. Cool. Okay, so now we basically have a little bit of this texture set up here. I'm going
[12:18] to make this just a little bit less obvious. So in this color ramp, I'm just going to drag this up
[12:22] just a touch to where it's not quite as strong a fall off. Okay, cool. Yeah, I'm happy with that.
[12:25] Okay, now I want to show you what we can do where we basically create a little bit of a section view
[12:29] instead of looking at only what's happening on this front. And the way that we do that is with
[12:32] the subsurface scattering. So we go here to subsurface and then we crank this up. Basically,
[12:36] it's going to start to take in these other colors. And what's really cool about this is this is
[12:40] actually doing some neat little things with the different rays of light and the colors. I'm going
[12:44] to go ahead and set these all to one so that it's not doing anything that we wouldn't expect. And the
[12:47] other thing that I need to do is I just noticed that my focus object is not attached to this.
[12:51] So again, another add on that I've made, I made an add on that works like the place tool in cinema
[12:56] 4d where I just press shift and all and then I can get a place these things or my this cursor on
[13:00] object. If you also want that, let me know. Drop a comment because I really have a bunch of these
[13:04] little add ons that I've made that I want to share. But it's a bunch of work to get them out there.
[13:08] People want to use them. So I'm going to do one thing here where we just control P and then object
[13:11] keep transform. And now we notice is this has gotten a little bit blurrier. And a good way that we
[13:16] can kind of fix that is sort of tweak this scale value. So I'm going to crank this up here to I
[13:20] had one where I said it like all the way to 10. And then now basically what we could do is we
[13:24] could adjust the thickness of this little slice that we're doing, you can make it very, very thin,
[13:28] or you can make it a lot thicker. When we do that, we're going to introduce some more light
[13:32] probably. So I would go to light here. Let's crank this up to maybe 1500, for example. It gives a
[13:36] little bit of a different effect. And I actually don't personally like this one quite as much.
[13:40] So in mine, for the final minute that I did actually her turn this completely off. This is
[13:44] the point where you could start to really affect the different things related to this look with
[13:48] this shader. So like you could change the metallic shader a little bit, you could change the overall
[13:53] alpha, you can adjust the roughness actually had the roughness turned down online all the way. And
[13:56] I think I had this fully on metallic here. Okay, now we're starting to get this effect. And now I
[14:00] just want to show you some of the post processing things that we can do with this. But I just want
[14:03] to quickly play through this. This just looks so cool. You can obviously adjust the way that you
[14:08] want this to look. But this is the basic effect. And then it's basically just art directing how
[14:12] you want to look kind of from there, choosing these different light angles changes a good bit.
[14:16] So like we could bring this back, I definitely recommend doing something off to a side as opposed
[14:20] to front lit if we kind of bring this around the 30 cursor, we kind of get I mean, look how cool is
[14:26] you can do so many things you even like render out multiple versions of this and kind of do
[14:29] little cross cuts in between it looks it looks so good. Okay, now for me just for fun, let's make
[14:34] this light a little bit blue because this is the kind of like that look that I made in one of those.
[14:38] I'm going to also grab this and then just G X and really bring this in. Okay, sweet. And then again,
[14:43] you can art direct and kind of tweak the way that you want this to look but for some post
[14:46] processing, let's go into our compositor by pressing C in this area and bring it up to
[14:50] composite window, I'm going to make a new window here. And then I want to see it in the viewport.
[14:54] So I'm going to go over here and just turn composite on always. For mine, I had a color
[14:58] correction note on one thing that I've also been doing is looking at the scopes of this image.
[15:02] This is somebody that was from Blender developers that kind of told me how to do this. So really
[15:06] quickly, I just want to do one frame render. So I'm going to press F 12 and write this out at 500
[15:10] samples. For me, I have a 5080 and a rising. I can't remember which one I have. This is what it
[15:17] looks like here. I'm just going to go ahead and hide this. So we're going to start to add in some
[15:21] different layers to this render. So in this area here, let's press I make an image editor and look
[15:25] at the render result. And so now it's basically going to pop in here. So the other thing that I
[15:29] would do is go over to my scopes and just turn them on where I want to see how this image looks.
[15:33] If I look at the parade form in here, I don't really have anything that's pushing all the way
[15:36] up to the full dynamic range of this image. So the first thing that I did was I added a color
[15:40] correction node. And I plopped that in and the master settings, I think I just tweaked the gain
[15:44] until it kind of got all the way up there toward the top. And this is already looking a lot better.
[15:47] You could just do that however much you desire. And then the next thing that I add to give it
[15:51] that effect with some sensor noise, I dropped that in here. This is a huge for this because if you
[15:55] have it to details, definitely not going to look as good as you want. I had this crank all the way
[15:59] up to point six to really make this grainy and you can see it kind of gives us effect. And then I
[16:02] also added I think around point one of chroma noise, which looks really good. And then after that,
[16:07] if you want to tweak the overall image, I love this tune image notes. I'll search for tune image
[16:12] would drop this in here. I think for mine, I boosted a little bit of the colors to point one
[16:15] to kind of give a little bit of that color back to it. And I think that's basically all I did there.
[16:19] Then I just added this you could do whatever creative effects you want. One other thing that I
[16:22] think is cool is the posterize effect. So we do shift day and search for posterize and drop this
[16:27] in here. I actually don't know specifically what this does. But it looks really cool. And you can
[16:31] kind of affect the amount that you want to do making it higher makes the effect less. But you
[16:36] can obviously do kind of whatever you want here. And then the only thing that you might do after
[16:39] that is over here in the final settings, you could do like some glare, if you want to add this in
[16:44] and then maybe set this to like bloom. But you know, obviously, the bloom only affects once
[16:48] there's something kind of reaching the highest point of this unless you adjust your highlights.
[16:51] I'm going to go ahead and mute this post rather don't really want to have that right now. I definitely
[16:54] see how it like bans everything. But because of the way this colors are doesn't really change that
[16:58] much. So I'm just going to mute this. And then I'm going to go back to my color correction,
[17:02] and just boost that game all the way until we're getting some of that blue getting here
[17:06] toward the top. Let's just crank it all the way to four. And again, we can also just address the
[17:10] lightness or the brightness of that light in our scene. And then make you just kind of see what
[17:14] this is doing is basically giving a little bit of bloom here, which I think was cool. Yeah,
[17:18] so this is basically the way that I did some post processing for this. And this effect is
[17:22] basically the entirety of the way that you would do it. And then my final render that I did, I just
[17:26] adjusted the light tweaking. One thing that also looks really good is if you rotate and animate
[17:30] your light. But this is like I said, this is the basic effect, I tweaked lots of little individual
[17:35] things with the materials, there wasn't anything like, you know, groundbreaking, or otherwise that
[17:38] I changed to make that effect. But play with the subsurface scattering play with mixing different
[17:44] layers of this to kind of create whatever level of opacity and kind of softness that you want.
[17:49] You can tweak the materials of the colors and of the light overall make this final render
[17:52] look have you want to look okay so hopefully you like this effect I think it looks super super good
[17:56] and next week like I mentioned I have a video coming out for my CAD to render workflow. We'll
[18:00] go over kind of the whole process of getting a CAD model from clients bringing it in,
[18:04] doing some retopology, I'm converting it from a CAD model into actual mesh model.
[18:08] We'll do the texturing, the lighting, all that good stuff. So if you're interested in that,
[18:11] make sure to subscribe and follow. You can also reach out to me on Instagram or LinkedIn. If you
[18:15] have any other questions or want to chat about anything, so hopefully you enjoyed this video
[18:18] and with that, we'll see you in the next one.



---

## Captured Frames

- [2:07] tutorials/frames/how-i-made-this-awesome-mri-effect-in-blender/frame_000.jpg
- [3:00] tutorials/frames/how-i-made-this-awesome-mri-effect-in-blender/frame_001.jpg
- [6:15] tutorials/frames/how-i-made-this-awesome-mri-effect-in-blender/frame_002.jpg
- [8:20] tutorials/frames/how-i-made-this-awesome-mri-effect-in-blender/frame_003.jpg
- [10:10] tutorials/frames/how-i-made-this-awesome-mri-effect-in-blender/frame_004.jpg
- [11:30] tutorials/frames/how-i-made-this-awesome-mri-effect-in-blender/frame_005.jpg
- [12:33] tutorials/frames/how-i-made-this-awesome-mri-effect-in-blender/frame_006.jpg
- [14:38] tutorials/frames/how-i-made-this-awesome-mri-effect-in-blender/frame_007.jpg
- [15:45] tutorials/frames/how-i-made-this-awesome-mri-effect-in-blender/frame_008.jpg

---

## Structured Notes

### Core Technique
A studio-style "MRI/X-ray slice reveal" effect (used on real client work, e.g. a Kawasaki KPM project) built entirely from ray-visibility tricks and light linking on a slicing plane — no volumetrics, no simulation. A moving plane intersects a black-metal object; the plane itself is invisible to camera but shows only the bounce light being cast onto it by an animated light that is light-linked exclusively to the object. A wave-texture-driven emission shader on the plane produces the fine scan-line/MRI look, and subsurface scattering on the object adds colorful internal "cross-section" glow.

### Summary
Source geometry: complex mechanical models (engine block) downloaded from **grabcad.com** as OBJ — a good source of free, highly detailed CAD-derived meshes for this kind of reveal effect (author flags to check licensing before commercial use). Import via File > Import > Wavefront (.obj); these CAD exports come in enormous, so scale down (author guesses/tests factors like 0.001), Ctrl+A Apply Scale, recenter via right-click Set Origin to 3D Cursor, and use Individual Origins pivot point to freely rotate into place.

**The slicer plane:** add a mesh Plane, rotate to face the intended camera axis, optionally extrude the single face back (E) to give it a bit of thickness (a thin-cube variant of this effect, common in Cinema 4D, uses subsurface scattering on that thickness). Animate the plane moving through the object on the X axis with two Location keyframes (I/K to insert) across the timeline (e.g. frame 1 to 150 at 30fps) — this alone already produces a rough "reveal" as it scrubs through the mesh.

**Hiding the slicer plane from camera while keeping its lighting interaction (the core trick):** rather than faking transparency with a shader (author notes this looks worse), use the Object Properties > **Visibility > Ray Visibility** toggles per-object. On the object being sliced: turn off **Camera** ray visibility (frame_003) and also turn off **Shadow** ray visibility — shadow-off is called out as the single most important toggle, since it's what lets light convincingly bleed/pass through the object onto the plane behind it. On the slicer plane: the opposite — turn off everything except Camera, so the plane is camera-visible but doesn't cast/receive shadows or get lit directly by the scene light, and set its Diffuse/etc. bounce contribution low.

**Lighting setup:** turn off the HDRI (World strength → 0) to fully author the lighting. Add an Area light, parent it to the slicer plane (Ctrl+P > Object (Keep Transform)) so it travels with the slice. Critically, use **Light Linking** (light's Object Data Properties > Light Linking > New, drag in the object's collection) so this light illuminates ONLY the sliced object, not the plane — the plane then only shows the object's bounce light hitting it, which is what produces the convincing "internal glow" look. Boost light power substantially (author used ~500W, later ~1500W with a thicker slice) since almost all direct light is being excluded from camera view.

**Object shading:** strip GrabCAD's default materials (select all, minus-remove to bottom of material slots) and replace with a simple black metal (Metallic ≈ 1, Roughness ≈ 0, i.e. "reference all the way down").

**Plane/slice shading (the MRI scan-line look):** on the slicer plane's material, add a **Wave Texture** node with Texture Coordinate set to Object (Ctrl+T generates the full coordinate node group automatically), Wave Type = Saw, Scale ≈ 300 for fine lines; plug into an Emission-style setup so the lines glow at the intersection (frame_004, frame_005). Layer in a **Gradient Texture** (Quadratic Sphere type, Object coordinates again via Ctrl+T) to control falloff — feed its Fac output through a Color Ramp into the shader's Alpha, shaping/squishing/scaling the gradient's empty texture space to control where the effect fades to black at the edges of the slice (turn off Film > Transparent in Render Properties so the background renders solid black instead of transparent, matching what "fading to black" should look like). A subtle Color Ramp position tweak softens the falloff so it isn't too harsh.

**Cross-section color (optional variant):** cranking **Subsurface Scattering** on the object's material (with subsurface Radius values set to 1,1,1 to avoid unexpected tinting) pulls in extra internal color/ray-bounce complexity at the slice boundary, visible in frame_007's cyan cross-section render — an easy way to art-direct a more "medical scan" palette (author demos this as a separate cyan-tinted pass, frame_007/frame_008).

**Art direction:** revisit slice thickness (thin vs. thick — thicker needs more light, e.g. 1500W, but author preferred the thin/no-thickness look and often switched the extra light back off entirely), reposition the light off-axis instead of straight-on for a more dramatic look, and try colored lights (e.g. blue) for a different final grade.

**Post-processing (Compositor):** enable Backdrop/"Composite" viewport display; render one still frame (F12, ~500 samples) to iterate compositing live. Chain: Color Correction node (raise Master Gain until the Waveform/Parade scope shows values reaching full dynamic range near white), Film Grain-type noise node (Sensor Noise ≈0.6, Chroma Noise ≈0.1 for a gritty scan-like texture), Tune Image node (small Saturation/Color boost, ≈0.1), optional Posterize node for a stepped/graphic look (exact internal behavior not explained by the author, used purely for the visual result), and an optional Glare (Bloom) node in the final Compositor output group (muted in this pass since it didn't suit the palette, but toggled on/off live to compare).

### Key Steps
1. Download a detailed OBJ mesh from grabcad.com (check license before commercial use).
2. Import (File > Import > Wavefront OBJ), scale down (test small factors like S, 0.001), Ctrl+A Apply Scale, recenter (right-click > Set Origin to 3D Cursor), rotate into place using Individual Origins pivot.
3. Add a mesh Plane as the slicer; optionally extrude for thickness; animate it through the object with two Location keyframes.
4. On the sliced object: Ray Visibility → turn OFF Camera and OFF Shadow.
5. On the slicer plane: Ray Visibility → turn everything OFF except Camera.
6. Turn off the HDRI (World Strength = 0); add an Area light parented (Object, Keep Transform) to the slicer plane.
7. Light-link that Area light exclusively to the sliced object's collection (Light Linking > New, drag in the object) so the light illuminates the object but not the plane directly — the plane only shows bounce light.
8. Strip the imported object's default materials; assign a black metal material (Metallic ≈1, Roughness ≈0).
9. On the slicer plane's material: Wave Texture (Object coords, Saw type, Scale ≈300) for the MRI scan-line pattern; Gradient Texture (Quadratic Sphere, Object coords) → Color Ramp → Alpha to fade the effect out at the slice edges; turn off Render > Film > Transparent so it fades to black.
10. Optionally boost Subsurface Scattering on the object's material for extra internal cross-section color complexity.
11. Art-direct: light power (~500-1500W depending on slice thickness), light angle (off-axis > front-lit), light color.
12. Compositor pass: Color Correction (raise gain per Waveform scope), Film Grain/noise node (sensor + chroma noise), Tune Image (saturation), optional Posterize, optional Glare/Bloom.

### Nodes / Settings
- **Ray Visibility** (Object Properties > Visibility): the entire trick hinges on Camera and Shadow toggles being set oppositely on the sliced object vs. the slicer plane.
- **Light Linking** (light's Object Data Properties): restricts a light to only affect a specific collection/object — used here to isolate bounce-only illumination on the slicer plane.
- Shader nodes: **Wave Texture** (Object coordinates, Saw wave, high Scale ~300), **Gradient Texture** (Quadratic Sphere, Object coordinates), **Color Ramp** (drives Alpha from the gradient), **Subsurface Scattering** (Radius 1,1,1) on the base material.
- Compositor nodes: **Color Correction** (Master Gain), a film-grain/sensor-noise node (Sensor Noise + Chroma Noise), **Tune Image** (Saturation), **Posterize**, **Glare** (Bloom).
- Parenting: Ctrl+P > Object (Keep Transform) to link the light's motion to the slicer plane.
- Render Properties > Film > Transparent: OFF, so background renders solid black to match the gradient falloff.

### Difficulty
Intermediate — no scripting or simulation, but relies on several non-obvious Blender-specific settings (per-object ray visibility, light linking) that aren't discoverable without already knowing they exist.

### Blender Version
Blender 5.1 (stated on screen at the start, default startup scene).

### Tags
mri-effect, x-ray, cross-section-reveal, ray-visibility, light-linking, wave-texture, gradient-texture, subsurface-scattering, compositor, color-correction, film-grain, product-visualization, cad, grabcad, blender-5.1

---

## Related Tutorials
None yet cross-linked — this is the library's first ray-visibility/light-linking cross-section reveal entry. Cross-link future product-visualization, light-linking, or CAD-to-render (the author's teased follow-up video) tutorials here.
