---
title: Add VFX to Cinematic RAW and LOG Footage (the right way) | ACES Part 2
source: YouTube
url: https://www.youtube.com/watch?v=LssHxDCM7H4
author: InLightVFX
ingested: 2026-05-19
blender_version: "4.x"
tags: [vfx, compositing, color-grading, aces, intermediate]
extraction_status: complete
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
ACES hands-on workflow (Part 2): set DaVinci Resolve to ACEScc color workspace and apply IDT to footage, configure Blender for ACES rendering, use Shadow Catcher + render layers to separate shadows, composite in ACES color space with EXR multi-layer output.

### Summary
12-minute practical workflow tutorial. Downloads: RAW footage clip, matching HDRI, and Blender project file from an Aces Kickstart Kit. Walks through: DaVinci Resolve setup (project Color Workspace = ACEScc, IDT for RAW footage → exports ACES EXR sequence), Blender ACES configuration (via Mario Costa Deis method), scene setup with collections, Shadow Catcher for floor, render layers for object/shadow separation, EXR multi-layer render output, and Blender compositor assembly.

### Key Steps
1. **DaVinci Resolve setup** — New Project; import RAW footage; Edit tab → drag to timeline; Project Settings → Image Scaling → Scale Full Frame with Crop; Master Settings → resolution 4K; **Color Management → Color Workspace = ACESccc**
2. **Input Device Transform (IDT)** — in Color tab, apply Input Color Space (IDT) matching the camera that shot the footage (e.g. ARRI LogC → ACES, Sony S-Log3 → ACES); this converts the flat footage into linear ACES space
3. **Export from Resolve** — export ACES color space EXR sequence for use in Blender compositor
4. **Blender ACES config** — follow Mario Costa Deis tutorial: replace Blender's color management with ACES config (set OCIO_CONFIG env variable); Blender now renders in ACES linear space natively
5. **Scene organization** — create collections: Camera, Floor, Added Objects; use collection visibility for render layers
6. **Shadow Catcher** — select floor plane → Object Properties → Visibility → **Shadow Catcher ON**; floor only appears as shadows, not as solid geometry
7. **Render Layers** — Render Properties → View Layers: Layer 1 "Main Objects" (floor collection = Indirect Only); Layer 2 "Shadows" (objects collection = Indirect Only); background transparent (Film → Transparent)
8. **Output: EXR Multi-layer** — Output Properties → Output format = **OpenEXR MultiLayer**; renders all render layers in one file per frame
9. **Compositor** — new scene for compositing; Compositor workspace → Use Nodes; bring in ACES footage EXR (color space = ACES 2065-1); bring in rendered EXR (image + shadow pass); Alpha Over to blend; adjust color/levels to match plate

### Nodes / Settings
- DaVinci Resolve: Color Workspace = **ACESccc**; IDT per camera type
- Blender ACES: OCIO config replacement (external tutorial by Mario Costa Deis)
- Object → Visibility → Shadow Catcher for floor
- View Layer: Indirect Only on appropriate collections
- Output: OpenEXR MultiLayer
- Compositor: Image node (color space = ACES 2065-1); Alpha Over; Render Layers node (for shadow pass)

### Difficulty
Intermediate

### Blender Version
4.x

### Tags
vfx, compositing, color-grading, aces, intermediate

---

## Related Tutorials
- [[add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1]] — Part 1: ACES theory (color gamut, gamma, linear light)
- [[i-recreated-movie-scene-in-blender-nuke-complete-tutorial]] — professional VFX pipeline using similar compositing techniques
- [[superhero-landing-tutorial-02-ground-destruction-vfx-in-blender]] — VFX ground destruction composited onto footage
