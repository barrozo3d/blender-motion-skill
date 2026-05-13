---
title: Add VFX to Cinematic RAW and LOG Footage (the right way) | ACES Part 2
source: YouTube
url: https://youtu.be/LssHxDCM7H4?si=WAKlvRJI_VfoW2rY
author: InLightVFX
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# Add VFX to Cinematic RAW and LOG Footage (the right way) | ACES Part 2

**Source:** [YouTube](https://youtu.be/LssHxDCM7H4?si=WAKlvRJI_VfoW2rY)
**Author:** InLightVFX
**Ingested:** 2026-05-13

---

## Description

ACES Kickstart Kit (now FREE): https://gum.co/HQdcC
To support more tutorials like this: https://patreon.com/inlightvfx

In this video, we dive into Davinci Resolve and Blender to see how to utilize ACES to easily add VFX to RAW and LOG footage. We’ll be building on the concepts of color gamut and gamma that were covered in Part 1. So if you haven't watched the first part yet, go check it out! 

Mario Cazares’ tutorials:
ACES Setup in Blender: https://www.youtube.com/watch?v=B7FWNNDXBl0
Image Co

---

## Raw Content (for analysis)

Kind: captions Language: en aces is a powerful free color management pipeline that makes adding vfx to raw and log footage super easy for artists like you and me in the previous video we learned about color gamut and gamma we'll be applying these concepts in this video as we dive into the aces workflow in davinci resolve and blender so join me and let's continue [Music] so you can follow along i've put together an asus kickstart kit on gumroad it includes this clip of raw footage this 360 degree hdri of our scene and the blender file for this shot the kit starts at two dollars but you can pay more if you're feeling generous your purchase goes a long way in supporting the careful planning and quality that i try to bring to every tutorial your support is needed and of course very appreciated okay first off we'll get all the software set up properly davinci resolve is free so download it next you'll need to set up aces in blender for that i'm going to direct you to my friend mario casares as he has a great video explaining how to do this it's pretty simple and with that we're ready to roll inside resolve we'll create a new project we'll head over to the media tab and import our raw footage let's go to the edit tab and drag this clip into the timeline to get rid of these small black bars we'll go into the project settings image scaling and click scale full frame with crop we'll quickly switch to our master settings and make sure our resolution is set to 4k if you'd like to work in 4k then we'll head to the color management tab here we'll change our project color workspace to ace's cc once we hit save we'll see that our footage looks different this is because we've entered the asus workspace don't worry about the picture looking bad the first step in the aces workflow is to transform the color gamut of our footage into the aces 2065 color gamut we also have to transform the gamma of our footage into the aces 2065 linear gamma asus makes this conversion simple with what is called an input device transform we'll call it an idt for short as part of aces there are tons of different idt's to select from most of these idt's are made for a specific camera and color profile for scene referred footage that is raw and log footage there's often a custom idt you can pick but with display referred footage there are fewer custom idt's and rather some general ones that are less accurate this is because display referred formats get rid of a lot of light information from the original scene making the conversion into aces less viable with most raw footage aces automatically converts the raw data into the asus 2065 1 color gamut and linear gamma for log footage we need to manually select an idt with this log clip here i can either assign an idt for the whole project in the color management tab or i can right-click each clip and select the idt this way the idt is converting the color space of our log footage adobe rgb to the aces 2065 1 color space and the idt is also converting the log gamma of our footage to be linear the idt is kind of like the great neutralizer of all different footage types in theory if we shoot footage of a scene on multiple different cameras with different color profiles raw log and otherwise the idt should make these all look exactly the same this is assuming that we have the same white balance and exposure for all cameras pretty cool huh okay back to resolve right now everything still looks bad so let's go into the color management again and we'll see this setting called output device transform let's choose srgb for now and we'll hit save now our footage looks good or normal essentially the output device transform or odt provides a way to convert from the huge color gamut and gamma of asus to the color gamut and gamma of whatever display device we want to show or preview our work on we're choosing srgb since most computer screens use the srgb color space and associated display gamma to summarize the aces idt and odt help us easily enter and exit the asus workflow now we can head to the color tab and at this point we can do any needed color correction but be very careful most color operations will destroy our linear light information at this stage we just want the white balance and exposure to look correct so changes to the color temperature this exposure slider the offset wheel and the gain wheel are all safe avoid any other changes i left the color for this clip untouched and with that we're ready to export our footage but before we do so we need to disable the odt this will ensure that we're exporting our footage in the asus 2065 color space and not srgb again don't worry about the footage looking bad we'll go into resolve's export tab and make sure that the in and out points are set to our desired clip then we'll select exr for the format in rgb half for the codec we use exrs while working in aces since this is the only file type that can store all the information for the ace's color space this does result in larger file sizes one downside of this workflow so let's hit add to render queue and start render if you want you can set the odt to srgb and create an h.264 clip that you can use for camera tracking for this shot since it's not moving i just used the free program f-spy to line up my camera's perspective and then i brought that camera into blender now we're ready to jump into blender if you set up your workspace correctly following mario's tutorial you should see aces listed as the display device in the color management tab make sure your view transform is set to srgb in your sequencer to asus cg asuscg is a linear color space with a slightly smaller gamut than aces 2065 and it's used for cg rendering we have our camera lined up here and in the camera tab we'll import the exr sequence we exported from resolve this color space setting we can think of as the idt and we'll set it to asus 2065.1 since this is the color space we exported from resolve now the footage in blender should

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
[To be extracted]

### Key Steps
[To be extracted]

### Blender Nodes / Settings
[To be extracted]

### Difficulty
[Beginner / Intermediate / Advanced]

### Tags
[To be added]
