---
title: Creating Realistic 3D Water in Blender : The Ultimate Guide
source: YouTube
url: https://www.youtube.com/watch?v=vr7mkSiKRLM
author: stache
ingested: 2026-08-17
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/creating-realistic-3d-water-in-blender-the-ultimate-guide/
frame_count: 0
frame_status: pending-selection
---

# Creating Realistic 3D Water in Blender : The Ultimate Guide

**Source:** [YouTube](https://www.youtube.com/watch?v=vr7mkSiKRLM)
**Author:** stache
**Duration:** 21m5s | 16 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- WARNING: Very short transcript (45 chars) in 'Water - The Short Film'

---


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py creating-realistic-3d-water-in-blender-the-ultimate-guide <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Water - The Short Film [0:00]
**Transcript (timestamped):**
[0:00] I.E.,
[0:28] This video is sponsored by Squarespace.


### Intro/Summary of The Video [0:40]
**Transcript (timestamped):**
[0:45] Scrolling through our station, I think more often than not, I come across a lot of 3D
[0:49] renders, usually in close vicinity and on a daily basis, that contains some kind of a
[0:54] water body in them.
[0:55] So I think it's safe to assume that our 3D artists love adding water into our renders.
[0:59] I wouldn't be surprised if every single one of you watching hasn't already attempted
[1:03] such a scene before.
[1:04] So, why not dig a little deeper into the subject?
[1:07] Go through all the different ways you can create water within Blender, understand all
[1:11] the parameters that go into making water look realistic, learn how to create the perfect
[1:15] material for it with foam and bubbles and dirt and volumetric gunk and even caustics
[1:20] integrated into them.
[1:22] I will also guide you to some really useful resources if you're planning to make a water
[1:26] based scene and we can learn how to animate water too which might seem like a difficult
[1:30] thing to do if you haven't done it before but it's really not as I will show you later
[1:34] in the video.
[1:35] And we will not just be covering surface level tips, we will actually go deep into the subject
[1:40] and also cover some underwater dynamics.
[1:42] And hey, water comes in all shapes and forms so why not take a fun little detour and briefly
[1:47] cover one of its most frequent use cases.
[1:49] And then finally, we can jump in and learn some neat little tricks to cheat in fluid
[1:53] simulations, learn some simple tips and tricks you can use to create fake water simulations
[1:57] so we can avoid the pain and suffering of a real fluid simulation.
[2:01] But just in case you are one of those psychos who have the time and patience for some real
[2:05] water simulations, we will briefly go into that as well.
[2:07] And then we end the video on a hopeful note as we look into the future of water simulations
[2:11] using geometry notes and what the new simulation notes will enable us to do in the future.
[2:16] So yeah, without further ado, let's get into it.


### Making Murky Water [2:18]
**Transcript (timestamped):**
[2:19] So let's say we have this scene and we want to add some water on the shore here.
[2:24] The simplest way to do that would be to just add a plane and place it in a way that you
[2:27] don't see its edges anywhere in the frame.
[2:30] Then go into the shader editor and add a Musgriff texture into the bump node and with
[2:34] a little bit of roughness and a little bit of transmission, you've got yourself a pretty
[2:38] decent looking water system right there.
[2:40] You should also set the index of refraction to 1.33 here to make it scientifically accurate.
[2:45] It doesn't really make a big difference here visually but it can in different lighting
[2:48] scenarios so I would suggest you just do it for the peace of your mind.
[2:52] Now you don't just have to limit yourself to the Musgriff texture here, you can use
[2:56] the noise texture or even the wave texture if you want a specific directional wavy look
[3:00] but to be honest you don't even have to limit yourself to procedural blender textures.
[3:04] There are normal maps available on the internet for different kinds of water waves, I found
[3:08] some free ones here on GadHatch.com so you can even use them to displace your water.
[3:13] But for now we're going to stick with the Musgriff texture because it's a little more
[3:15] versatile and easy to understand.
[3:18] So yeah, as I said, just with this simple setup you are going to get a pretty good looking
[3:21] water system right here but there is a very obvious problem going on here too.
[3:25] We can clearly see the under parts of the photo scan right here at the edge which definitely
[3:29] does not look good.
[3:30] So let's take this material a little further, let's delete the plane and add a cube instead
[3:34] of it and do the exact same thing that we just did but this time we're going to make
[3:37] use of the volume slot in the shader editor.
[3:39] We're going to bring in a principal volume node and plug it into that slot and once we
[3:43] do we'll immediately see it makes the water look extremely dark but at a lower density
[3:47] value it gives the water a nice and murky look almost like it has some sediments underneath
[3:53] it.
[3:54] You can even try giving it different colors if you want, a dark brownish color in this
[3:56] case will work fine for me and you can stop right here if you want but water does exhibit
[4:01] some volume absorption behavior too so why not add that node as well.
[4:05] Add an add shader node and attach the volume absorption node in the bottom socket and as
[4:09] soon as you do you will immediately see the water gets even darker as it should in an
[4:14] environment like this but dial it down a little bit if you want, give it a blueish greenish
[4:18] color if you want or add directed in any way you want to and a lot of people might tell
[4:22] you to use the volume scatter node here instead of the principal volume node and they're
[4:26] right because both those nodes are basically the same but the principal volume node has
[4:30] these emission sliders that I tend to use a lot whenever I really want to force a color
[4:34] on the water so set the emission strength to something really low and give it whatever
[4:38] color you want.
[4:39] It's better than changing the color of the volume absorption or the density right here
[4:42] or even the main color on the principal bsdf node because I feel like it tends to work
[4:46] a little better if compared with the others but irrespective of what you choose to do
[4:49] here you should have a pretty good looking water body at this point but let's take it
[4:53] even further and make it even more realistic.
[4:55] If you've ever looked at drone footage flying over a huge water body you would have noticed
[4:59] water usually isn't bumpy consistently or reflecting sunlight consistently, it has certain
[5:04] regions where there's clearly more bump than usual and certain regions where the roughness
[5:08] isn't as much as some other regions and we can very easily replicate that with the blender
[5:13] too.
[5:14] All you gotta do is add a noise texture with a color ramp and plug that into the roughness
[5:17] to quickly get that effect.
[5:19] Obviously do dial the back up a little bit to the right and reduce the white color to
[5:23] something like dark gray to keep it subtle and realistic and this was just to control
[5:27] the roughness though we have to do the same thing for the bump as well and we can very
[5:30] conveniently use the same set of we've got here we just gotta make a new color ramp and
[5:34] drive that into the strength of the bump instead and that's it.
[5:37] We've got both the effects working perfectly fine now.
[5:40] But again mess with the black and white values here too to keep it subtle and realistic.
[5:44] Another extra layer of detail you can add here is by mixing a diffuse shader with the
[5:48] main principle shader and driving the factor through another noise texture but making it
[5:52] extremely big in size and then driving it almost invisible with a color ramp until only
[5:57] these small specks are left which almost looks like those bubbly foam specks you usually
[6:02] see near the shore of a pond or a dock or wherever the water is moving a lot but that's
[6:06] not the only kind of foam you see in water.
[6:08] Foam can literally occur at any point of contact it has with literally anything including
[6:12] with itself so to replicate that effect we can make use of the ambient occlusion node
[6:16] which is really good at producing a black and white mask anywhere there's a contact between
[6:20] two objects.
[6:21] So let's make another principle BSDF node and mix it with the main one and drive the
[6:25] factor using the ambient occlusion node.
[6:27] To create that foamy texture you gotta use two noise textures and mix them together using
[6:31] the linear light blend mode.
[6:32] How do I know the linear light blend mode looks the best here?
[6:35] Cause I scrolled through all the other blend modes as we all do sometimes and linear light
[6:39] came out to be the best.
[6:40] That's it.
[6:41] The trick though is to keep the scale of one of those noise textures really high like
[6:44] almost around 1000 and the other one really low maybe somewhere around 100 or 200.
[6:49] And now plugging this mixture into the emission node you will immediately see the foam pop
[6:53] up.
[6:54] You can plug it into the base color too if you want but plugging it into the emission
[6:57] slot makes it a little more prominent.
[6:59] And while you're at it we can drive the same color ramp into the alpha channel as well
[7:03] for a little more control on the transparency of the foam.
[7:06] But this is how you create the foam effect procedurally within blender but if you want
[7:09] to keep it simple and not go through all this hard work just download this foam texture
[7:13] from ammincg.com to save some time and effort and get an equal if not better foam.
[7:17] Now this was just for when two objects come in contact like here in the turtle render
[7:21] you can see this foam texture in effect at the shore a little bit but you can also create
[7:25] foam at the choppy bits of the water by using the geometry node here in the shader editor
[7:30] and driving the factor using the pointiness or the normal plug instead of the amateur
[7:33] inclusion node and that is enough to create foam in the choppy bits of the water.
[7:41] And that's it you combine all these textures together and on top of that add some surface
[7:45] details yourself spread some leaves and twigs and grass and moss and lily pads manually
[7:50] on the water to really take the water to the next level.
[7:53] But this was just for still renders to animate the water you just gotta make the main musgrave
[7:57] texture 4D and then just drive the W field with a driver write hashtag frame in it to
[8:03] turn it into a driver and start wobbling the water with every moving frame but it will
[8:07] obviously be a little too fast so we can divide that rate up by about 5000 or something like
[8:11] that to really soothe it down.
[8:13] But just doing that makes the water look a bit too procedural so to take the animation
[8:17] up a notch just add a mapping node to the texture and animate the X or Y location there
[8:22] using the same hashtag frame method to give the water a bit of directionality and hide
[8:26] that procedural nest a little bit.
[8:28] And I guess that's it that's how you really quickly animate water.
[8:31] Here's a quick tip while we're at it make sure you make everything a little wetter in
[8:34] the scene by driving the roughness up using the color ramp especially for the things near
[8:38] the shoreline to sell the effect of the water even more.
[8:41] But water won't be just murky and muddy like this in all your scenes you can also have


### Making Clear Pool Water [8:44]
**Transcript (timestamped):**
[8:45] instances where you need the water to be more clear like maybe in a pool scene so achieving
[8:49] that is also really easy.
[8:50] Firstly it can be done by just removing all the volume nodes we just set up because we
[8:54] need the water to be as clear as possible here and then we can add some caustics over
[8:57] it to really give it that pool aesthetic which is done by using the Voronite texture.
[9:02] And there are a lot of ways you can make caustics with the Voronite texture.
[9:05] For a sharper look people usually like to use the distance to edge mode in the Voronite
[9:09] texture but what I have found is subtracting an F1 node with a smooth F1 node gives a much
[9:14] more realistic look.
[9:15] And you don't have to do this next step but if you want to add an extra layer of caustics
[9:19] you just duplicate this same setup again and make sure the above set is bigger in size
[9:23] and the bottom one is smaller in size and then you mix them both together and plug it
[9:27] into the emission slot to get some nice caustics.
[9:29] Definitely dial the emission down a bit because we don't want it to be too overpowering and
[9:33] to really sell the effect of the caustics you can use a caustic gobo light to light
[9:36] the surroundings as well.
[9:37] I got this gobo setup from a polyfure tutorial which I will link in the description below
[9:42] so go grab that light and spread it around in your pool scene to really take it to the
[9:45] next level.


### Important Tips and Tricks [9:46]
**Transcript (timestamped):**
[9:46] By the way this is a pretty obvious fact that I'm stating right now but I would still like
[9:49] to state it.
[9:50] The color you give to the water surface isn't going to matter much.
[9:54] Water as in real life takes the color of its surroundings.
[9:57] See if I change the HDRi the color of the water clearly appears to be different too.
[10:01] So keep that in the back of your head even though it's such an obvious thing.


### Important Resources [10:04]
**Transcript (timestamped):**
[10:04] But anyway just in case you want to experiment with different kinds of colors I found this
[10:08] great color palette resource for various kinds of watercolors you find in nature and different
[10:12] ecosystems so you can even make use of that.
[10:14] And finally after I have overloaded you with this much information you've come to the conclusion
[10:19] that this is just too much work for you.
[10:21] I would recommend you try this real water add-on for some really good looking water materials.
[10:26] It's pretty inexpensive and will do almost all the work I just taught you for you automatically
[10:30] but it is at a paid price so it's up to you if you want to opt for it or not.
[10:34] I also think a free alternative for it would be the blender kit add-on.
[10:37] You just search for water materials there and you will seriously find some awesome
[10:40] reserves.
[10:41] There's frozen water and river water and pool water and all kinds of procedural stuff so
[10:46] go check them out as well.
[10:48] Before we move on to the next section though I would like to tell you more about today's
[10:51] sponsor Squarespace.
[10:52] Now if you've been thinking about making your own website be it for e-commerce or for
[10:56] a non-profit or like for us 3D artists for a CV or for a portfolio there's really no
[11:01] question if you should go with Squarespace or not because they literally provide you
[11:04] with the best in class and extremely customizable website templates.
[11:08] I kept scrolling through their catalog and they literally kept recommending more and
[11:11] more options for me to choose from and once I did choose one I was shocked by how easy
[11:16] it was to use and how customizable it all was and I don't know about you but if I see
[11:20] a portfolio up on a custom website like this as compared to some dude with just a social
[11:25] media handle I am for sure going to go with someone who has put the time and effort to
[11:29] make a good looking website like this.
[11:31] So head on to Squarespace.com and try it all out for free for yourself and once you are
[11:35] ready to launch your website go to Squarespace.com slash stash.
[11:40] You got that Squarespace.com slash stash to get 10% off your first purchase of a website
[11:46] or a domain so go give it a try and spread your online presence like never before with
[11:51] Squarespace.
[11:52] Alright let's move on.


### Making an Ocean in Blender [11:54]
**Transcript (timestamped):**
[11:55] Let's now look at a much simpler and much quicker method to make a water system within
[11:59] Lender which is by using the Ocean modifier.
[12:02] It literally takes a few seconds to set it all up you just add a plane and apply an ocean
[12:06] modifier on it and that's it.
[12:08] Here you've got sliders for the overall sizes of the plane, there are sliders for the resolution,
[12:13] there are sliders for the wave size and choppiness and so much more and it's pretty straight forward
[12:17] unlike most things in blender.
[12:19] Those feels really do exactly what they say but what really interests me in the ocean
[12:23] modifier though is the foam option and the spray option.
[12:26] You can enable the foam layer and the spray layer and give them an attribute name here.
[12:30] To apply the foam you just gotta bring an attribute node in the shader editor and plug
[12:34] it with a color ramp that can go directly into the emission slot to get the foam right
[12:37] there in just a few clicks.
[12:39] And you can obviously use the color ramp to dial the foam in as well.
[12:42] The spray though will require a geometry node setup which I learned from a stack exchange
[12:46] post so I will just link it in the description below for you to check out so you can see
[12:50] the node set directly there.
[12:52] The results aren't super impressive by default but if you are well versed with geometry nodes
[12:56] you can really take this spray effect anywhere you want.
[12:59] But yeah that's what the ocean modifier is good for.
[13:01] It is good for really quick results that actually look good and it has really beginner-friendly
[13:06] controls too.
[13:07] But yeah if the shader editor scares you, the ocean modifier should be your first choice.
[13:12] Just make sure you up the resolution for the final render and also don't forget to check
[13:15] out some of the presets here under the spectrum panel.


### Animating Waves in Blender [13:17]
**Transcript (timestamped):**
[13:18] But now let's talk about animating some waves in your water which I think you already guessed
[13:22] it is done very easily using the dynamic paint effect.
[13:25] All you gotta do here is go to the physics properties tab, click on dynamic paint and
[13:29] mark it as the canvas and here under the surface type just choose waves and then go select
[13:34] the object you want the water to respond to and do the same thing but choose brush instead
[13:38] of canvas.
[13:39] And now when you play the animation and dip the object in the water it should create some
[13:43] waves for you.
[13:44] Just make sure your water plane has enough subdivisions though.
[13:47] More subdivisions it has, more defined the waves will be.
[13:50] The most important fields though when messing with dynamic paint are in the canvas properties.
[13:55] You should reduce the speed field to something like 0.15 to slow down the waves a little
[13:59] bit and have it at a realistic pace.
[14:01] And another brush properties change this factor value under the waves panel to something
[14:05] like 0.5 to reduce the impact the object creates when it comes in contact with the water.
[14:09] And I guess that's it.
[14:11] Dynamic paint is a very quick way to add some super easy wave simulations into your scene.
[14:15] I mean look at this animation, in the background there are literally splashes that just got
[14:19] created automatically just because I marked the right objects as the brush and had enough
[14:23] resolution on the water surface.
[14:25] So definitely give it a try if you haven't already.


### How to Make an Underwater Scene [14:26]
**Transcript (timestamped):**
[14:28] But let's now go a little deeper into the subject and understand how to create some
[14:32] underwater scenes which also surprisingly are very easy to make.
[14:35] It's literally just a principle volume node and a volume absorption node added together
[14:39] just like we did a few moments ago for the water surface.
[14:42] Just know that you can apply this material either on a cube which is surrounding your
[14:45] subject or directly do it in the world tab here in the shader editor.
[14:49] And you can combine it with that caustic light we used in the pool scene to get some really
[14:52] nice light rays here as well.
[14:54] And to really sell the effect we can add a particle simulation to the subject of the
[14:58] scene, make it emit these simple transparent bubbles that have a very low lifetime and
[15:02] aren't affected by gravity a lot.
[15:04] Just that goes a long way to show that the subject is floating underwater.
[15:07] It's not perfect but I think it looks good enough.


### How to Make Rain [15:11]
**Transcript (timestamped):**
[15:11] And now let's take that little detour and see how we can create some rain in the render.
[15:15] And I did a lot of experiments and what I found is that we could make a simple particle
[15:19] system and emit some droplets from it to mimic rain.
[15:21] We could make a plane and add some dynamic paint on it to get some ripples too.
[15:25] But nothing I did, matched the kind of results I got from this add-on called bagger rain
[15:30] generator.
[15:31] It's a geometry note based add-on made by the creator of the bagger pie add-on which
[15:34] I'm sure you've heard of.
[15:35] So I would highly suggest you give that a try.
[15:38] It is a paid add-on but still quite affordable.
[15:40] You get automatic splashes and just the material to put on the floor to make it generate procedural
[15:44] ripples too and a lot more control through this panel right here.
[15:48] Options for the droplets, the splashes, the winds, in short just a lot of control compared
[15:52] to a simple particle system.
[15:54] So definitely give it a try for your rain driven seeds.
[15:56] And don't forget to pair it up with one of those rain droplet generators.
[15:59] There's a ton of them available online.
[16:01] I'll link the one I used in this scene in the description below.
[16:04] Combine that with the bagger rain generator to get even more realistic results.
[16:08] So try them both out together.
[16:10] But for now let's get back on track and talk about those fake water simulations I showed


### Fake Water Simulations [16:12]
**Transcript (timestamped):**
[16:14] you earlier.
[16:15] Starting with this tap of running water.
[16:17] One of the quickest cheats for replicating a stream of running tap water like this is
[16:21] to just use a displaced modifier with a cloud texture attached to it on a cylinder mesh,
[16:25] change the coordinates to object, make that object an empty and then just move that empty
[16:30] infinitely downwards to create some motion in the displaced modifier and you should get
[16:34] a pretty believable stream of running water.
[16:36] On top of that we can even add a musk-grift texture to the displacement in the shader
[16:40] editor and animate that too for even more fluid like random motion.
[16:44] And on top of that we can also rotate the cylinder every few frames to get even more
[16:48] motion.
[16:49] So this is only a particle system spitting out small droplets at a very high speed to
[16:53] top it all off.
[16:54] You can even replace the cylinder with a particle system of Metaballs because Metaballs tend
[16:57] to stick together on contact which is a lot like how water droplets behave so you can
[17:02] even take that route if you want.
[17:04] And I forgot to mention it before but the rain and this fake tap water can really benefit
[17:08] from a lot of motion blur to give it that illusion of really fast moving water droplets
[17:12] so don't forget to enable that too.
[17:14] And this was just one cheat.
[17:16] You can also simply use a video texture for some water streams, cut out the water part
[17:20] from a video clip using the knife tool and then use a color ramp to drive the alpha so
[17:24] only the water stream is visible and again a particle system of droplets is always helpful
[17:28] to sell the effect a little more and a little bit of dynamic paint driven by a secretly hidden
[17:32] cube to sell the realism even more.
[17:35] But it doesn't stop there either.


### Making a Beach in Blender [17:36]
**Transcript (timestamped):**
[17:36] You can also download a top down shot of a beach and bring that into Blender and run
[17:40] that video texture into the displacement of a well-subdivided plane and you can get some
[17:44] really believable beach waves and require no crazy fluid simulations at all.
[17:49] It is kinda crazy how much we can get away with just these simple techniques.


### Roasting the Blender Fluidsim [17:53]
**Transcript (timestamped):**
[17:53] But as I said if you are one of those psychos who still would like to delve into fluid simulations
[17:57] you can but my experience with it was just horrible and not because it's difficult to
[18:03] use.
[18:04] The fluid simulation within Blender when you initially set it up has pretty good default
[18:07] settings.
[18:08] You literally don't need to touch anything here except maybe the resolution, the higher
[18:11] you take that the more realistic results you get.
[18:14] You can also change the simulation method here.
[18:16] Epic is for more stable simulations and Flip is for more splashy simulations and also you
[18:22] can generate spray and foam from these two checkboxes which just creates two particle
[18:26] systems each for spray and foam separately.
[18:29] And that's literally it.
[18:30] As I said there's not much you need to change here to be honest.
[18:33] But the problem with this system is that it's just too finicky.
[18:37] It works for a minute and then you make the tiniest change and it absolutely loses its
[18:41] mind.
[18:42] There's no consistency in performance or even the output of the fluid sim and again it's
[18:46] not difficult it's just buggy and hard to dial in because of that.
[18:50] Maybe the experience would have been different if I had a better computer but for now I would
[18:55] not recommend the fluids into anybody.
[18:57] I haven't tried the Flip Fluid add on though.
[18:59] I have heard good things about it but it's kinda expensive for me right now so I would
[19:03] love for you to share your experience if you've tried it and how it compares to the
[19:06] default Manta flow fluid system in the comment section below and maybe then I will give it
[19:11] a try.
[19:12] So please do drop a comment down below if you can.
[19:13] I would really appreciate it.
[19:15] But yeah that was my experience with the built in fluid sim options Blender has to provide.
[19:19] What really excites me though is the advent of simulation notes now in Blender 3.6 and


### Water with Simulation Nodes [19:20]
**Transcript (timestamped):**
[19:23] what that entails for fluid simulations in the future because a few Blender community
[19:27] members have already tried that hand added and gotten some really impressive results
[19:31] already so I can't wait for this to advance and solve a lot of problems that Blender has
[19:35] had for a few years now with its simulation tools.
[19:38] And understandably the team behind Blender cannot make everything perfect just by themselves.
[19:42] That's why a community driven tool like simulation notes can help other capable members in the
[19:46] community to solve those problems for them I think.
[19:49] So I will link some of the best water simulation projects in the description below if you want
[19:53] to check them out for yourself.
[19:54] I wish I was smart enough to present something I made myself but let's not even go there
[19:59] because that would be a waste of both your time and mine.
[20:03] So just check out the links in the description if you want to delve deeper into that subject.


### Crazy Looping Animation [20:07]
**Transcript (timestamped):**
[20:07] But I guess that's it from my end.
[20:09] That's all I had planned for this video.
[20:11] I would love for you to drop your thoughts in the comment section below.
[20:13] Half these tips I showed you I learned from the comment section of other YouTube videos
[20:17] so drop a comment and teach me and everyone else hanging out there a little more if you
[20:21] can.
[20:22] That would be really helpful.
[20:23] By the way I know this video was not too beginner friendly so if you are a beginner and couldn't
[20:28] catch a particular thing or a topic just drop a comment and I'll make sure I comment back
[20:32] and help you out in any way I can or at least guide you to the right tutorial for it.
[20:37] Shout the Patreon if you would like.
[20:38] I just made this looping animation a few weeks back so if you want to see the breakdown for
[20:42] that the Patreon is the place to be.
[20:45] And there's a lot more content arriving in the coming weeks so subscribe to the Patreon
[20:49] if you would like to support the channel directly.
[20:51] Thanks to the current members of course this channel would be nothing without their support
[20:55] so a huge thank you to all the Patreon folks.


### Outro [20:57]
**Transcript (timestamped):**
[20:57] Alright that's it.
[20:58] Thanks for watching till the end.
[21:00] If you did I will hopefully see you guys in the next video.
[21:02] Bye.



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
