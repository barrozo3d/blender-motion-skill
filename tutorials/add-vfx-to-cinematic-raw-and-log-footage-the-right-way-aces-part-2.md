---
title: Add VFX to Cinematic RAW and LOG Footage (the right way) | ACES Part 2
source: YouTube
url: https://www.youtube.com/watch?v=LssHxDCM7H4
author: InLightVFX
ingested: 2026-05-19
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2/
frame_count: 0
---

# Add VFX to Cinematic RAW and LOG Footage (the right way) | ACES Part 2

**Source:** [YouTube](https://www.youtube.com/watch?v=LssHxDCM7H4)
**Author:** InLightVFX
**Duration:** 12m17s | 4 section(s)

---

## Raw Data (for Claude Code extraction)


### <Untitled Chapter 1> [0:00]
**Transcript:** Aces is a powerful free color management pipeline that makes adding VFX to raw and log footage  super easy for artists like you and me.  In the previous video we learned about color gamut and gamma.  We'll be applying these concepts in this video as we dive into the Aces workflow in  DaVinci Resolve and Blender.  So join me and let's continue.  So you can follow along, I've put together an Aces Kickstart Kit on Gumroad.  This includes this clip of raw footage, this 360 degree HDRI of our scene, and the Blender  file for this shot.  The kit starts at $2, but you can pay more if you're feeling generous.  Your purchase goes a long way in supporting the careful planning and quality that I try  to bring to every tutorial.  Your support is needed and of course very appreciated.  Okay, first off we'll get all the software setup properly.


### SOFTWARE SETUP [0:49]
**Transcript:** DaVinci Resolve is free, so download it.  Next you'll need to setup Aces in Blender.  For that I'm going to direct you to my friend Mario Costa Deis as he has a great video explaining  how to do this.  It's pretty simple and with that we're ready to roll.  Inside Resolve we'll create a new project, we'll head over to the Media tab and import  our raw footage.  Let's go to the Edit tab and drag this clip into the timeline.  To get rid of these small black bars we'll go into the project settings, image scaling  and click Scale Full Frame with Crop.  We'll quickly switch to our master settings and make sure our resolution is set to 4K  if you'd like to work in 4K.  Then we'll head to the Color Management tab.  Here we'll change our project Color Workspace to Aces CC.  Once we hit Save we'll see that our footage looks different.  This is because we've entered the Aces workspace.  Don't worry about the picture looking bad.  The first step in the Aces workflow is to transform the color gamut of our footage into  the Aces 2065 color gamut.  We also have to transform the gamma of our footage into the Aces 2065 linear gamma.  Aces makes this conversion simple with what is called an input de...


### RENDER SETUP [8:06]
**Transcript:** Now let's create some different collections to organize the objects in our scene.  We'll have a collection for our camera, another collection for our floor, and one for  any added objects.  Finally for our floor we'll go into the object tab and set it to be a shadow catcher.  We'll now set up some render layers so we can render the objects separately from their  shadows.  We'll name this current layer main objects.  Let's set the floor collection to indirect only.  You can see this makes it so that our floor shows only indirectly in the main objects.  Then we'll create another render layer naming it shadows.  We'll set the main objects collection to indirect only so we only see the shadows.  Once we have our render layer set up we'll make sure our background is set to transparent  and set the output type to open EXR multi-layer and we'll hit render animation.  For compositing we'll create a separate scene and go into the compositing tab make sure  use nodes and backdrop are enabled and make sure you have a viewer node and composite  node to start out.  Next we'll bring in our background footage which is the EXR sequence from resolve.  Remember to set the color space to ACES 20651. ...


### Proverbs 16:18 [12:15]


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
