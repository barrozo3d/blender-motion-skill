---
title: Making a new Logo Animation - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=7MIePxGcze0
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/making-a-new-logo-animation---blender-secrets/
frame_count: 0
frame_status: pending-selection
---

# Making a new Logo Animation - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=7MIePxGcze0)
**Author:** Blender Secrets
**Duration:** 11m49s | 3 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py making-a-new-logo-animation---blender-secrets <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] In this video I'll walk you through how I created this logo animation.
[0:07] Along the way I'll share some modeling tips, physics and animation tricks.
[0:12] A few handy add-ons I used how I added sound effects to get the timing just right.
[0:17] And then we'll render it and polish it up in DaVinci Resolve.
[0:20] A quick heads up, this isn't a full step by step tutorial.
[0:24] It's more of a quick overview with some useful tips sprinkled in.
[0:28] I think in this case that's the best way to highlight what really matters.
[0:31] Alright, let's dive in and make some logo animation.


### Modeling [0:34]
**Transcript (timestamped):**
[0:34] I didn't start with a specific idea for this animation, I just wanted to experiment.
[0:39] So I began by recreating the logo in 3D, just to see where it might take me.
[0:44] First I modeled the keyhole and used it as a boolean cutter on the box.
[0:49] Even though it wasn't necessary I kept the cutter all quads.
[0:52] I've been doing a lot of subdivision modeling lately and this was just a good opportunity
[0:56] to practice clean topology.
[0:58] To shape the lid of the box I added a loop cut, beveled it and removed the geometry in between.
[1:04] Then I filled the holes on both objects.
[1:07] I enabled random colors in the viewport overlays to help distinguish objects more clearly.
[1:12] It's a simple trick but really useful when modeling.
[1:15] After using the keyhole as a boolean cutter I applied the boolean modifier and turned on cavity and shadows in the viewport overlays
[1:22] or even more visual clarity in the viewport.
[1:25] Still without a clear animation idea I decided to refine the geometry and I cleaned up the endgones, turned everything into quads
[1:32] and prepared it for subdivision.
[1:35] Here I used an outset, that's just an inset, press I followed by O for outset, to add a protective loop around the keyhole.
[1:44] I creased all the edges that I wanted to stay sharp and then tested them with the subdivision modifier.
[1:50] In order to be able to triple edge everything I converted those creased edges to have a bevel weight of 1 and a remove to decreasing
[1:58] and then I added a bevel modifier.
[2:00] I set that to two segments that gives you three edges and then I used the limit method weight so that it only affects those edges marked with a bevel weight of 1.
[2:09] So that gives me those three holding edges with a bevel amount of 0.002 or 2 mm.
[2:17] Eventually though I decided to soften the look and I bumped that up to 0.02 which is 2 cm.
[2:25] I duplicated the object and put it in a backup collection.
[2:28] That's always a smart move before you apply modifiers.
[2:32] Then I applied the bevel modifier to finalize the geometry.
[2:36] Next I added a camera.
[2:39] I recommend doing that early on.
[2:41] It really helps you plan the shots and the timing better as you build up the animation.
[2:45] I then explored the simple deform modifier to get some quick ideas.
[2:49] Thanks to the clean quad topology I was able to get some interesting deformations as you can see.
[2:54] But I wasn't super inspired by this so I thought let's try rigid body simulations instead.
[3:00] And I rebuilt the top part of the box quickly to be one single object just to simplify things.
[3:07] Still lacking a final concept I decided to switch focus to the text for a while.
[3:12] You can use any font installed in your computer in Blender
[3:15] but I wanted to have something fresh, something playful and I found a nice one on Google Fonts
[3:20] where I downloaded it and then I installed it in my system.
[3:23] So then after refreshing the font list I was able to use that in Blender.
[3:27] I tweaked the thickness and bevel settings of the text and then I just converted it to a mesh.
[3:33] I could have just used this terrible geometry by the way.
[3:37] It wouldn't have made a difference but I tried using quad remesher which is a commercial add-on.
[3:41] And I wanted to see how well it handled the remeshing of the text and it actually did a great job.
[3:46] There's just one issue, the front and back faces weren't connected to the middle
[3:49] so I just deleted everything with the front and then extruded it again manually.
[3:54] To sharpen the edges I selected them and creased them.
[3:57] And then after a bit of tweaking I added a bevel modifier and switched the creased edges to edges with bevel weights
[4:04] for cleaner control of the bevel modifier.
[4:07] Here's a useful trick, if you run into overhang issues like this with subdivision modeling
[4:12] set the outer miter in the bevel modifier to arc
[4:16] and then connect the converging verges with an edge.
[4:19] Selecting it I'm pressing J to form two triangles.
[4:22] And then when you have two segments, Blender automatically turns those triangles into quads
[4:27] and your overhang is gone. So that's a really cool trick.
[4:30] To be clear I did not need this level of topology for the text.
[4:33] I just kind of enjoyed the process.
[4:35] I just wanted to make the text a little bit more precise, warm up for my brain
[4:39] and I might need to deform the text later anyway.
[4:42] Plus the smooth bevel gives it a nice visual polish and makes it match the box also a little bit better.
[4:48] I then separated each text object into individual letters and added a ground plane.
[4:54] For rigid body simulations, origin placement is really crucial.
[4:58] I set the 3D cursor to the bottom of each object and then set the origin to the 3D cursor.
[5:04] And then I immediately fall over.
[5:06] After converting the text to active rigid bodies, I ran a quick simulation
[5:10] and it looked fine, so I baked the results to keyframes.
[5:13] Same for the 3D characters, although the 3D took a bit more effort to balance properly.
[5:18] Next I parented these text objects to empties so that I could control their skill and where to place them.
[5:25] Then I animated their skill from 0 to 1 over a few frames, so they just pop into existence and fall down naturally.
[5:32] Something interesting I discovered is if you type scale in the Timelines search bar,
[5:36] you can isolate all the scale keyframes.
[5:38] So that's very convenient if you just want to fine tune the placement of those scale keyframes.
[5:43] So next I tried animating the cube to be sort of tossed into the scene, but I could never really get it quite right.
[5:49] And then when trying to adjust the camera placement, Blender gave me a cryptic message,
[5:54] no suitable context info for active keying set.
[5:58] And I couldn't really find any way to solve this and I just didn't feel like wasting a lot of time on it,
[6:03] so I just opened a new blend file and appended everything from the previous file into it.
[6:08] And of course that fixed it. Sometimes the simplest workaround is the best one.
[6:12] Still not satisfied with the cube animation, I just deleted its animation and tried something completely new.
[6:18] I created a stunt cube to handle the physics part and that I can later parent the actual logo cube too.
[6:24] The logo stays oriented properly no matter how the stunt cube ends up.
[6:28] Next I made a hole in the floor with a cutter cube and then I applied the Boolean modifier there.
[6:34] And then I animated the stunt cube to fly up by setting two z-axis keyframes
[6:39] and talking the animated property from onto off in a single frame.
[6:43] That gives it some upward velocity before then the rigid body simulation takes over.
[6:48] And to make the animation a bit more dynamic I modeled hatch doors that open
[6:52] just in time for the cube to launch through and then quickly close again.
[6:55] That was pretty easy to animate just a few keyframes.
[6:58] And then of course the doors were set as passive rigid bodies and marked as animated.
[7:03] I wanted the cube to bounce more convincingly, so I experimented with the bounceiness value and added a slight initial rotation.
[7:11] And these two tweaks made a big difference.
[7:13] Once I was happy with the result I baked the stunt cube's motion to keyframes
[7:17] and then I parented the hero cube to it and disabled the visibility of the stunt cube.
[7:22] Physics simulations can be unpredictable in blender, so be prepared for lots of trial and error.
[7:28] I actually tried to scale the keyframe influence proportionally, but I couldn't yet find a way to do it.
[7:33] So if you know how, please let me know in the comments, but I just moved on.
[7:37] I also decided to redo the 3D text animation because I wasn't super happy with it
[7:41] and origin placement and bounce values made all the difference.
[7:45] Eventually I was happy with how it looked and I baked it to keyframes.
[7:48] At this point everything started to come together, but the timing still felt off.
[7:52] There are just too many things happening, all at once.
[7:54] And that's an important thing to think about.
[7:56] Your viewer can only focus on one thing at a time, so pacing and animation is really critical.
[8:02] And to fix this I added sound effects directly in blender.
[8:05] And for that I used soundly.
[8:07] That's a sound browser that pulls from both free and paid libraries.
[8:11] I have the paid version, but I think the free one lets you index your own sounds,
[8:15] or at least those from freesound.org.
[8:18] You can preview a clip, select just the part that you want, and then drag it right into blender sequencer.
[8:23] Really cool, really fast, really easy to use.
[8:26] From there it's easy to sync the audio to the visuals and adjust the volume.
[8:30] Unfortunately I didn't record the system audio for this tutorial,
[8:34] but here is what the final animation sounds like with all the sound effects in place.
[8:42] So that's the result so far.
[8:44] This project started with no clear idea at all, just some modeling practice,
[8:47] but it evolved into something much more interesting.
[8:50] So you probably want to know how did I go from this to this.


### Rendering [8:54]
**Transcript (timestamped):**
[8:56] First of all I used cycles for rendering to get a softer, a little bit more subtle look.
[9:01] And I enabled GPU rendering and used the Turbo Tools add-on to speed things up significantly.
[9:08] For the materials I used the Sanctus Material Library, which is a paid pack,
[9:13] and it comes with an asset browser collection, so you can simply drag and drop the materials on your objects.
[9:19] I quickly UV-enwrapped the objects by selecting everything in Edmode, hitting U and choosing Smart UV Project.
[9:26] It actually took me a while to decide on the materials, not because they weren't good,
[9:30] but because there were so many beautiful ones to choose from.
[9:33] I kept experimenting with different looks, which was both fun and time-consuming.
[9:39] Next I set up some lighting.
[9:40] I only used Area Light, which I controlled using the Gaffer Add-ons UI.
[9:45] I tweaked the camera movement a bit after switching to a longer focal length,
[9:49] that helped to bring all the elements visually closer together for a more cohesive composition.
[9:55] For the cube that shoots up through the hole, I thought it would be fun to have a light shining up from underneath.
[10:00] So I used an Area Light pointing up and a cube with a low-density volume material.
[10:05] At this point I just got rid of the HDRI lighting.
[10:08] I wanted more precise control, and I think that Area Lights let you really sculpt the look of the light that you want.
[10:14] To get that soft, colorful gradient look in the background, I placed another cube with a principle volume material behind all the objects.
[10:22] Then I added colored Area Lights to shine into it, and this creates those dreamy gradients behind the text,
[10:28] and makes the ground plane disappear into the fog, which adds a nice touch.
[10:32] Just be careful with the volume density, less is more.
[10:36] One small but important detail, I rotated the individual text elements slightly in Edit Mode,
[10:42] just to give them a bit more depth and make them face the camera better.
[10:45] Honestly, the hardest part of this whole project for me was choosing the right colors and materials for the text objects.
[10:52] Eventually I found a combination that I was happy with.
[10:55] I also added an empty to use as the camera target for a shallow depth of field.
[11:00] It's very easy to go overboard with that effect, but this time I managed to hold back.
[11:04] I did a quick low-rest test render just to make sure everything looked good.
[11:08] Always a good idea before you commit to hours and hours of rendering.
[11:12] After a few more tweaks, I rendered the final image sequence and moved on to grading in DaVinci Resolve.
[11:19] Nothing too fancy, I just played with some sliders until it looked better.
[11:23] I also used some of the built-in effects, like vignette and film emulation.
[11:28] And you can see that that nice bit of color grading really makes a big difference.
[11:32] And that's how I made this logo animation.
[11:34] I hope you found it interesting, and thank you so much for watching all the way to the end.
[11:42] Thanks for watching!



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
