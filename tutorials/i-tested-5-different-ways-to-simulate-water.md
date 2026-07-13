---
title: I Tested 5 Different Ways to Simulate Water
source: YouTube
url: https://www.youtube.com/watch?v=QF-gxJLVNOw
author: Nils Gallist
ingested: 2026-07-13
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/i-tested-5-different-ways-to-simulate-water/
frame_count: 0
frame_status: pending-selection
---

# I Tested 5 Different Ways to Simulate Water

**Source:** [YouTube](https://www.youtube.com/watch?v=QF-gxJLVNOw)
**Author:** Nils Gallist
**Duration:** 17m4s | 14 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py i-tested-5-different-ways-to-simulate-water <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Water is particularly famous for one thing.
[0:30] It's known for being a pain in the butt for getting right in CGI.
[0:36] Obviously for fluid simulations there is specific software such as
[0:40] putty-me, but that's a lot of work. So I want you to know how could I do this on any budget and
[0:46] in the time scale. Hey guys, unfortunately it's me again. Let's talk about water.


### Overview [0:47]
**Transcript (timestamped):**
[0:54] I tried to recreate the same scene in every scenario that I've used and I've compared
[1:00] different fluid simulations from blender and tunnel, montha flow, flip fluid which is a popular
[1:07] add-on Nexus particle which is a new plugin for particle simulation general that just released
[1:12] a thing a month ago or still in beta. I heard a lot about liquid gin from DjangoFX. I've used it
[1:18] over the past couple of years a couple of times but never really gave it a shot. So that's in the
[1:24] and last but not least HydroFX which is probably a software that you've known if you are
[1:30] in the same sort of CGI bubble that I am. Each of our test benches I ran a couple of times.
[1:36] I made sure to spend a lot of time with those plugins just to give it a fair shot. This video took
[1:42] a long time. It was in the making for a couple of weeks now. So here somewhere should be a link
[1:48] to my patreon. There's a couple of free stuff on there but if you want to leave some love,
[1:51] thank you very much if not then we'll just continue with the video but you can also support
[1:56] by leaving a like and subscribe or share your thoughts in the comments down below. But let's get
[2:01] let's get going. Let's get going. We will start out with a blender in tunnel. So blender in


### Blender Internal [2:05]
**Transcript (timestamped):**
[2:08] tunnel uses grid simulation resolution which is typically set to 256 or 512 and the higher the
[2:17] number is the final simulation is the more time it takes to bake. As I've mentioned I tried to
[2:22] keep every test scenario as close to each other as possible. I timed how long it took. I timed
[2:29] how long everything took to bake and how the viewport performance is after baking and then the final
[2:35] result. I typically tried to give 256 and 512 as these are the most common resolutions. I would
[2:45] assume for testing out this stuff. I'm a short and timed each and every one of them. So you can see
[2:50] blender based 256 took me about 20 minutes and 40 seconds to cache. So to bake and order it for
[3:00] it to be able to render. Taking a quick look around it does seem to be a bit extreme on the extreme
[3:06] side. What I do like is that you have still control over all the particles like foam, spray and
[3:12] liquid. Sometimes I ran the simulation twice. This time it I don't know it was 4 minutes quicker.
[3:20] I have no idea why. But just so you know it's had about 19 gigabytes of cache. So when you're doing
[3:28] fluid simulations make sure to reserve some of your hard drive space for cache. Here's a quick viewport
[3:36] render. However I have rendered out the final result as well but only 4512. I didn't want to
[3:42] render everything all the time. So only for the higher resolution renders I have put them through
[3:46] the paces. Speaking about blender base and 512 resolution I always baked that as well. That was
[3:52] more troublesome way more troublesome. They they're baking crashed a couple of times. So I had to bake
[3:59] it multiple times. It took significantly longer two hours and two minutes and over 115 gigabytes
[4:08] in cache size. Viewport performance on the 256 version was sluggish but okay ish in here not
[4:17] usable at all. So when you have cached out the simulation your viewport you just have to trust
[4:23] that everything is looking fine within your render. For the final result you can see that it actually


### BI Results [4:28]
**Transcript (timestamped):**
[4:33] works quite well. However the particle spray is insanely extreme. There are some there are some
[4:40] hiccups in here. You can definitely see it in here that the particles stuck around for some for
[4:48] sometimes. That is because the simulation or the render itself crashed again multiple times.
[4:56] I do have a pretty beefy computer so these are these are the stats of my computer. I don't think
[5:05] it should have crashed and I was only able to render it out using console commands and not
[5:11] the typical control f12. So hey get as you want this is the result for blender internal 512. Again
[5:20] also for the other things I only rendered out the 512 the more accurate version. For flip fluids


### Flip Fluids [5:24]
**Transcript (timestamped):**
[5:26] which is an amazing plugin I have to say what I love about flip fluids is that you can get into so
[5:31] much detail. It's not just a fluid simulation tool but also apex we can make some more viscous
[5:37] stuff and you have so so much controls over particles and the data that comes within particles.
[5:43] So if you want to do some motion graphics as well flip fluids is the way to go and their demo
[5:48] reels it's just it's just I love to work with it however it is still CPU bound we'll get to that
[5:53] in a second. The 256 version was quicker to render than the internal. My flip cache 256 flip fluids
[6:03] cache 256 is six gigabytes big. You can see that I have excluded the sides of the simulation
[6:11] which is actually nice touch. I like it I really like it. Now I said that I have rendered out the
[6:17] 512 version as well and I did. It took a long time it took about like one minute one hour and
[6:24] 10 minutes or something so it was still twice as fast as blender internal but why I'm quickly
[6:30] you know interrupting this right now is that flip fluids is CPU based but flip fluids as of last month
[6:37] has like a community update which is GPU accelerated so that is actually quite amazing somebody in
[6:42] a community took it upon itself upon himself or herself I have no idea to make a GPU version of
[6:49] flip fluids significantly speeding up the render time or like the simulation time so I tried it out
[6:57] and I have to say I did not see any big improvement at all so the simulation still took an hour
[7:05] and 10 minutes I have rendered multiple times on CPU and GPU it's I don't know it's about
[7:13] 5 minutes apart from each other so for me the GPU accelerated version did not do as much as I would
[7:21] have hoped however community feedback is quite clear apparently it is speeding up things just not
[7:28] for me maybe I did something wrong I've rendered multiple times I gave it up fair shot I have to say


### FF Results [7:34]
**Transcript (timestamped):**
[7:34] still I still like the results of flip fluids we can see it right now
[7:38] love it looks amazing I am a big fan of flip fluids always looks really really cool take a look at
[7:44] this shot that I did for a film a short film of a friend of mine a couple of months ago oh my god it's
[7:50] one and a half years ago so they are used flip fluids as well I just am a big fan of this
[7:55] moving on there's a new plugin in town called Nexus particle also particle simulations which is


### NeXus Particles [7:58]
**Transcript (timestamped):**
[8:04] well capable of doing flip fluid simulations so I put it through the ringers the process here is
[8:09] a bit more difficult because the plugin itself is a bit more convoluted I have to say it's not as
[8:13] beginner friendly as I would have hoped to but I did my best to compare 256 and 512 now you have to
[8:21] deal with voxel size but you can make some calculations and still get a comparable result from it
[8:29] the cool thing about Nexus is that it's incredibly performant and also GPU accelerated so even
[8:35] rendering out the cache of 256 took about a minute viewport performance is fine I guess
[8:43] and now we run into a beautiful problem when I was trying out this work to the cache was broken
[8:49] again I ran it multiple times it's just the cache didn't seem to work every time I hit play
[8:56] or like playback it's calculated from the from the beginning I tried it with 512 resolution as well
[9:03] the cache version the cache function just did not seem to work for me so I went into the discord
[9:11] ask hey was up with the cache and they did confirm cache at this point in time was not working however
[9:18] you don't really need cache in this case you can just render it out if you want to yeah yeah okay


### NP Results [9:23]
**Transcript (timestamped):**
[9:25] so this is the result without caching you can see that there is not really and it's not
[9:34] you can see the results are noticeably lacking and it's not because of animation or like simulation
[9:41] quality but there is no white white water at all it's just pure fluid it's a bit hard to control
[9:47] it's just not made for these kinds of animations if you look at the of the examples that they give
[9:53] you in their own youtube channel you can also see that there's no bubbles no spray no nothing
[9:57] it's just made for more you know mo graph stuff not really realistic water and fluid simulations
[10:04] so I recorded I you know I did this test two weeks later Nexus had an updated updated it's had
[10:10] the cache is working and also added foam an x foam which adds white water particles to all of
[10:16] the simulation to all of the simulations I had to try it out I tried it out again I tried it a
[10:21] couple of times sorry it just didn't work for me it just didn't work for me and at this point
[10:27] I spent well over two days just trying to get that working and it didn't so I love Nexus for all
[10:35] of their particle simulation stuff maybe it's just not meant for these kind of fluid simulations


### LiquiGen [10:42]
**Transcript (timestamped):**
[10:42] and now with this we are leaving the blender ecosystem and we are going into a program that has been
[10:48] around for quite a while liquid gin by jenga fx so they were one of the first ones to handle GPU
[10:55] accelerated particle simulation not only for water but also fire and now they have some some
[11:00] geotrain and liquid gin and it will tend to have a whole suite their claim to fame was real time
[11:07] water simulation and it is a bit more complicated because it's an external tool to work with it
[11:13] but about viewport performance you can say what you want it is real time so what you see is what
[11:20] you what you get I've only have footage here of my 512 version which is you know in all the other
[11:26] tries with the 512 resolution viewport was barely usable it was just unusable I have like straight
[11:34] up unusable here still fine still usable and you could see what's going on and direct your shot
[11:41] huge plus what I also love about liquid gin is that it's simulating while you're doing stuff
[11:47] and also at any point in time you can go in and you know fix water and the resolution of water
[11:54] and all of this that's insane that's a lot of control that you that you have so sort of pre-baking
[12:01] and caching takes about five seconds there is hundreds of millions of particles interacting in here
[12:07] it's just it's just a beast and it is really really quick there's warm caveat you can render
[12:12] in liquid gin that took ages I didn't do it you can export it to blender as abc files
[12:20] a lumbic files that is huge those files are huge but then you have to benefit that you get control
[12:26] again over everything especially the particles if you know if you add like two nodes in geometry nodes
[12:33] you can add the size of the particles and have again full control over the scene but in my version
[12:39] maybe because I was on the trial I know I know I know I could only export 256 frames so like the
[12:47] last half of the animation and that is what I brought into blender and this is what you can see
[12:54] what you can see here there are some flickerings in my in my rendering again at this point I've


### LG Results [12:55]
**Transcript (timestamped):**
[13:02] spent a lot of time learning liquid gin and getting it to work I was just happy with the render my
[13:08] final resume about this is it's amazing the tool is if you if you tool is really really good I would
[13:15] say that in terms of calculations and realism I'd still put flip fluids above but if it's if your
[13:22] workflow is just in the slightest dependent on time liquid liquid gin is just so quick and so iterative
[13:31] and that's worth a lot now the last tool we're covering is hydro fx also a standalone tool that is


### HydroFX [13:34]
**Transcript (timestamped):**
[13:39] just made for water effects and the stuff that they showcase it being used for is just amazing it's
[13:46] actually quite easy to get into even though it sort of looks a bit more complicated than it actually
[13:51] actually is but also a GPU accelerated workflow and you can really see every time you hit play it is
[13:58] playing and caching at the same time the quality and the speed of how hydro fx has worked was actually
[14:07] fun I don't know just playing around with it seeing how interactive it is how quick it is
[14:13] just was really fun to play around with even the high resolution one took like six minutes and 10
[14:18] seconds to to run through I only used their demo software so you can purchase it or subscribe to
[14:26] it and everything so in my demo version I was not able to export anything I can only look at it
[14:33] in the soft so sadly I have not rendered anything out there but I tried it out I spent a significant
[14:38] amount of time within hydro fx and I really I want to give it a shot like I want to do something big
[14:45] with it because it feels like it is capable of doing something huge something huge now that's my


### Honorable Mentions [14:51]
**Transcript (timestamped):**
[14:52] little deep dive and how you can simulate some water on your own machine honorable mentions is that
[14:58] LTX a artificial intelligence model has a water Laura which I have not tried out yet so maybe that's
[15:05] something to take consider as well depending on your stance to AI obviously so that video took a lot


### Results [15:11]
**Transcript (timestamped):**
[15:13] of time here are my findings this is this is how long it took for everything to cash out I'm not
[15:18] including render time because they you know can vary dramatically but I think for my tier list
[15:25] flip fluids was again maybe but because I'm more used to it it takes a lot of time to simulate
[15:32] because it's not yet really GPU accelerated apart from his one cool plugin this guy that just
[15:37] didn't work for me I assume but for in terms of realism and what you can do flip fluids inside blender
[15:44] is just amazing then liquid gen if it is just so quick so if you don't need perfect realism but
[15:53] something that is really good and like 15 times quicker than just simulating over and over again
[16:00] liquid gen is just a way to go liquid gen is the way to go I wouldn't view avoid mantle flow if
[16:05] possible I know it's free and within blender but I gave it a couple of shots and that what you saw
[16:11] was the best that I could manage so that could be a skill issue on my side but I just don't see
[16:18] why I would use it if you have access to any of these other other tools hydra of X is something I'm
[16:23] gonna keep my eye on and I want to try out and maybe make a dedicated video about this as well
[16:29] last but not least nexus nexus I appreciate for a lot of things but maybe it's just not meant for
[16:35] that kind of workflow thank you very much for indulging in my yapping we'll see you guys in the


### Outro [16:36]
**Transcript (timestamped):**
[16:41] next video I have a patreon so if you want to support much appreciated if you leave some love
[16:48] some some love behind thank you thank you very much and that was me thank you very much



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
