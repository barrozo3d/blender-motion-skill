---
title: Sand Simulation - Blender Tutorial (Nexus)
source: YouTube
url: https://www.youtube.com/watch?v=8Swzwo83OP0
author: CGMatter
ingested: 2026-08-03
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/sand-simulation---blender-tutorial-nexus/
frame_count: 0
frame_status: pending-selection
---

# Sand Simulation - Blender Tutorial (Nexus)

**Source:** [YouTube](https://www.youtube.com/watch?v=8Swzwo83OP0)
**Author:** CGMatter
**Duration:** 6m40s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py sand-simulation---blender-tutorial-nexus <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] This simulation I made went super viral if a hundred views on Twitter's considered viral.
[0:04] Core ideas, we're gonna need an object, turn it into points, find a way to simulate it with sand,
[0:08] but we're gonna use an infection or a growth system to say only do the physics on those parts.
[0:13] Some materials, and that's it.
[0:14] We are gonna be using the Nexus add-on, so make sure you have it.
[0:17] First thing I need is a ground plane for this to collide on next.
[0:20] I need a object, text object, rotate it, be the letter, maybe R, to give it actual geometry, extrude that bad boy, bit of roundness,
[0:27] convert it into a mesh, and now we are ready to start.
[0:30] Hide both my text and my plane object.
[0:32] For the plane, I'm gonna add a NX, Nexus collider.
[0:35] This collider is going to inherit the plane.
[0:37] I don't want anything bouncing and nothing moving around, so a high friction.
[0:40] As for the particles, make a emitter, which we can call sand.
[0:44] This is going to be a object being that text, which by default, you know, does this.
[0:48] We wanted to in fact spawn from inside the volume all at once, which is what this shot means.
[0:53] Now we just get a initial burst.
[0:55] Change the mode to hexagonal, have no speed in the beginning.
[0:57] Just like that, we get our letter.
[0:59] There's the spacing.
[1:00] If I go to display and show these as spheres, you're gonna see this is why it's spaced so widely, because the radius is quite big.
[1:06] Teremity-dith.
[1:06] Yeah?
[1:07] The re-
[1:07] Teremity-dith.
[1:08] Fuck.
[1:09] Teremity-dith.
[1:10] Take the radius and let's divide it by two.
[1:12] We have particles, we have a thing for the particles to go on, but no gravity.
[1:15] Add a gravity.
[1:16] Now these falls, sometimes through the plane.
[1:18] Just gonna nudge the plane down a little.
[1:19] And there we go.
[1:20] Now all we need is for them to act in a way where they clump together and fall apart like sand.
[1:24] The way you do this with Nexus, weirdly enough, with a fluid, by using an advection from a fluid.
[1:29] The point is, take the solver, change it to SPH where the type is granular.
[1:33] It's falling apart in a way where it's like respecting the boundaries, respecting space is important.
[1:37] To get it to clump together, we call that friction in this case, the particles stay next to each other.
[1:42] I'm gonna have a lot of friction, a lot of friction, iterations, and now these clump more together.
[1:46] The kind of separation you might want, where there's certain clumps that stay with others, can be thought of as the stability.
[1:51] The more stable it is, the more it stays in one piece.
[1:54] Whereas if the stability is really low, it kinda all separates.
[1:56] I'm gonna go 15, I'm gonna take the radius and make it smaller.
[2:00] Eugh, no no no.
[2:01] It should be doing it, but it's passing through itself, almost like it's not doing enough calculation.
[2:05] That's the problem.
[2:05] In your fluid, take these sub steps, basically how accurate is our simulation, and turn off adaptive,
[2:10] saying it has to be this number of sub steps.
[2:12] Which, by the way, I'm gonna make bigger.
[2:14] I saw this in a tutorial for the emitter turn off subframe emit, and now we're already getting something much better.
[2:19] Take the stability, bring it down, bring down the friction a little.
[2:22] We can of course hone in these settings, but what I wanna do first is have this infection growth, and then we can fix the look.
[2:27] I'm gonna turn off gravity and fluid, so I just have my particles.
[2:31] To get this kind of like spreading behavior, in the business we call that a infection, or a infectio.
[2:36] This little gizmo over here is saying where is COVID starting from?
[2:39] I heard saying COVID demonetizes your videos.
[2:41] I don't know if that's still the case.
[2:42] If I hit play, you can see this is the infection.
[2:45] I mean, it's kinda already working by default.
[2:46] The only setting I really wanna play with is what color it turns into.
[2:49] Why is that useful?
[2:50] If I take the infected color, and with RGB I make it pure red, then for our emitter, I'm gonna make the initial color only blue.
[2:57] Then we have a really good way to say what is and isn't infected by looking at how red the particle is.
[3:03] Use this to drive different properties, like where's gravity being applied, etc.
[3:06] If I can force certain areas to not move, to have a speed of zero, then we've done it.
[3:09] I'm sure there's other ways to do it, but I'm gonna bring in a NX speed, which I don't really care about setting the speed to anything, and in fact this can be zero.
[3:15] But what I care about is doing a clamp, saying the speed cannot be higher than a certain number.
[3:20] If I set this to zero, you can see it's now frozen, and the infection takes over.
[3:23] This is basically a number I want to animate based on the infection.
[3:27] So I'm just gonna set it to like 10, and then in the mapping, I'm gonna take the red color.
[3:31] I'm gonna say I want to control the clamp max, particle speed max.
[3:35] When it's not red, it should multiply by zero, and when it is red, it should multiply by one.
[3:39] You can kinda see that does what we want. Not exactly, exactly.
[3:43] I believe the issue is kinda this like spreading in the beginning.
[3:45] Yeah, if we go to frame two, you can see it's colliding.
[3:47] Take this plane, bring it down so that there is no collision.
[3:50] Hopefully that will help, and it seems to help.
[3:52] Look at that. Now let's just hone in the look.
[3:54] I think I want to decrease the friction a little, decrease the stability a little.
[3:57] Gonna add more sub steps as basically a quality thing, and additionally, the whole simulation can have sub steps.
[4:03] So you have the overall quality and then the sub quality.
[4:05] To control that, go over to document.
[4:07] I don't know why it's called that, and bring up the sub steps to two.
[4:09] I don't know if this is cutting the recording in and out, cause it's using the GPU, but let's say I like the look of this,
[4:15] and I want to cache it. In other words, I wanna save it.
[4:17] Then maybe I wanna render it out of some GeoNote stuff.
[4:19] And by adding a NX cache, basically saying, save the thing.
[4:23] So make a directory. I'm gonna call the folder this.
[4:26] In here, I'm gonna build my cache, and I think all of these settings are fine.
[4:29] So, build cache and then wait.
[4:31] So the beauty of the cache is we calculate once, keep it forever.
[4:34] But everything you're seeing right now is just kinda like a viewport effect.
[4:37] For example, if I like go into a camera that faces this, and I hit render,
[4:41] you can see it's just kinda like a blank plane. It doesn't actually exist in our scene.
[4:44] But we can make it exist. So take the emitter in export, create a point cloud.
[4:48] If I look at our emitter, you can see in fact, there is now a point cloud object.
[4:51] I can take the display of this and turn off show particles.
[4:54] And then we just have this point cloud. That is true of geometry notes.
[4:57] In fact, if I take a look at my spreadsheet, you can see the points.
[5:00] There's 100,000 of them inherit everything that we made.
[5:02] At least everything we cared about.
[5:03] This color attributes, saying what is and isn't active, the velocity, the position, the radius.
[5:08] We could do whatever we want. For example, if the radius is a little too consistent,
[5:11] I can take it and just multiply it by a random factor.
[5:15] 0 to 1 before, after, it keeps the motion.
[5:17] But now we just added some like visual interest.
[5:19] I'm gonna set up like a super basic scene to just kinda show you how I made the material.
[5:23] By default, it is inheriting the color.
[5:25] The reason this is the case is this node.
[5:27] By default has this set material. We examine this material.
[5:30] And you can see there's already this color like put inside here.
[5:32] I could visualize the velocity if I wanted to.
[5:34] I'm gonna bring in my point info, cause these are actually points.
[5:37] Look at random, which is gonna have a 0 to 1 on all of these kind of like differentiating grains from each other.
[5:42] Throw that through a color ramp.
[5:43] Some of the colors are like a dark brown and some of them are kind of like a bright, sandy color.
[5:48] Bring this through the principal to be SDF.
[5:49] Tweak the color and the brightness and generally you get your final result.
[5:53] The only difference with mine is I simulated with more honed in settings with many more particles,
[5:58] like a few million and with more sub steps.
[6:00] And that, that's it. Now I know you. I know you.
[6:03] You might be wondering, how do I get the sand to like stop and settle?
[6:06] I'm sure there's some way to like do it in simulation, but because we already have this cache,
[6:10] I'm gonna show you a trick.
[6:11] Go to playback, which is deciding how this is playback.
[6:13] By default, it's gonna say disabled, set it to custom.
[6:16] And you're gonna take your in and out point.
[6:17] In my case, this is frame 2 to 120.
[6:19] Whatever it is, it's gonna remap it to this like linear time thing.
[6:23] We want it to like progress, you know, most of the way, then it just kind of slows down like that.
[6:26] That's what we want.
[6:27] Add a point linearly so that we get kind of like a something like that.
[6:31] So here you can see it's falling.
[6:32] Nothing has changed at all, but when we get around the end, it just kind of settles down and stops.
[6:36] Project file on my website cgmatter.com.
[6:38] See you there. Bye.



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
