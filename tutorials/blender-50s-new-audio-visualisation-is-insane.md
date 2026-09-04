---
title: Blender 5.0's NEW Audio Visualisation is INSANE!
source: YouTube
url: https://youtu.be/YOx9me2MnGA
author: MTR Animation
ingested: 2026-05-13
blender_version: "5.0"
tags: [geometry-nodes, simulation, animation, smoke-fire, volume, motion-design, blender-5x, intermediate]
extraction_status: complete
---

# Blender 5.0's NEW Audio Visualisation is INSANE!

**Source:** [YouTube](https://youtu.be/YOx9me2MnGA)
**Author:** MTR Animation
**Ingested:** 2026-05-13

---

## Description

📖 Use the code "AUDIO" to get 25% off The Big Nodebook!!!
https://mtranimationgumroad.gumroad.com/l/thebignodebook/MATH

Use this link if you want to become an affiliate:
https://mtranimationgumroad.gumroad.com/affiliates

Audio visualisation has become insanely cool in Blender 5.0! In this video, we will create an audio visualiser by using smoke simulation and Blender 5.0's new Grid Nodes to simulate particles in a beautiful way! Enjoy the video! 

Subscribe if you want to see more: 
 @mtranima

---

## Raw Content (for analysis)

Kind: captions Language: en Audio visualization is everywhere like festivals or games and of course in 3D and Blender 5.0 just changed this forever because Blender's new geometry nodes gives us amazing control over simulated volumetrics. And this allows us to combine audio and physics like never before. So before we jump into Blender and create an audio visualizer, we actually need some audio. And in my opinion, the best place to get royalty-free audio is from Epidemic Sound. I'm not sponsored or anything like that, but I would still recommend it a lot. But of course, you can do this tutorial with any song that you like. What we are going to do first is we're going to search for a nice genre that we want to use. So, if you go into music, we have all these genres over here, but I want to have more genres. So, I want to view all the genres that Epidemic Sound has. And while working on this tutorial, I figured that it would not be a good idea to choose my personal favorite genre because that genre sounds a little bit like this. And I don't think the majority of my viewer will appreciate that kind of sound. So I figured we would go for a genre that is a little bit more accessible for everyone. And I found that genre in Electro House. So if you click on that, then we have this song skip. If we play this, it sounds like this. It has a really nice beat to it. So it's really easy to make an audio visualizer out of this. However, the whole song is 5 minutes and 10 seconds long, and that's a little bit too long for this tutorial, of course. So, I want to have a shorter version. So, if we go over here into create versions, and you can choose for a 15 seconds version, and let's see what it will create. Okay, it created uh this version. Let's see. I think that's perfect. If you take this one and we download it, then we can jump into Blender and start visualizing this music with physics. Okay, the first thing that we're going to do inside of Blender is, of course, as always, removing the default cube. We don't really need it. And to be honest, let's also remove this light. Okay, of course later we want to create a smoke simulation which reacts to the music. But before we do that, I want to create one controller which is later going to control everything that should be dependent on the audio. And that controller is going to be an empty. So if you press shift A, you can go into empty and do plane axis. And we want that the Z location of the empty reacts to the music. And to do this, we first need to create a key frame for the Z location. So if you click on the empty and press K, you can do an location key frame. And you see we've created a key frame right over there. And now to make it follow the beat of the music, we want to go into the graph editor. So let's split our screen in half like this. And let's go into the graph editor. Then you will see that we have over here the X, Y, and Z location of this empty. To be honest, we don't need the X and Y location. So let's just remove those by clicking on them and press X. And then you see we only have the Z location here, which is perfect. And now to make this Z location line follow the beat of the music, you want to select the Z location and go into channel and then go to sound to samples. Click on that and then select your song and do sound to samples. Then you see, okay, it is working, but it starts a little bit too late, right? We want it to start at frame one, but it's now starting at frame 7 because our cursor was at frame 7. So let's do that again. So, let's go to frame one and do channel sound to samples and do the song again. And then you see it starts at the beginning, which is perfect. You see it follows the song, the beats of the song. But at the moment, it's just silent, right? Then we're not really hearing the song. And I think it would be better if we can actually hear the song. So, let's import the audio into Blender by splitting our screen in half again. And let's go into the video sequencer. And at the moment we cannot really add anything in this because we haven't assigned this sequencer to our scene because over here we have scene as you can see. And if you go over here you can assign the video sequencer to scene and then you can press shift A and do sound and select the sound and make sure that it starts on frame one. And then if you press play you will start hearing the song in Blender. However, for the sake of the tutorial, so that I don't have to worry about that the song is interrupting my voice, I'm going to remove this. But you can keep it like that, of course. Now that you've done that, we can merge these two screens again. Basically, what you see happening is that the Z location over here is always above zero. So, it's always floating. That's not really what I want. I want to make it that the empty is going to be like jumping from zero and then above. And at the moment, it's not really doing that. So what I want to do is I want to take this graph and scale it on the y-axis and then move it down so that it will make big jumps on the beat. Don't worry, it will make sense in a moment. But first I want to make sure that we can manually change the key frames of this graph. And for that we have to convert this graph into key frames. And actually before we do that you see that the graph is going further than the end frame that we set our animation on. So it now goes like this. Yeah, that's not really what we want. So let's set the end frame on like 350 so that it is for sure within the range of our animation. Now to convert this graph into individual key frames, we can select the Z location again and go into channel again and then do samples to keys. Then we see we have it like this. And now if you press A to select all the key frames, you can press S and Y and scale it up like so. Let's make it very big. And then let's make sure that the top part over here is kind of like this like around five by pressing G and Y of course. But now yo

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/blender-50s-new-audio-visualisation-is-insane.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Building a music-reactive smoke simulation in Blender 5.0 by using the Graph Editor's Sound to Samples feature to drive an Empty's Z location from an audio file, then using that Empty as a force controller for a Geometry Nodes volume/smoke simulation.

### Key Steps
1. Import royalty-free audio (e.g., 15-second Electro House track from Epidemic Sound) for use in the visualizer.
2. Add an Empty (Shift+A > Empty > Plane Axis); insert a Location keyframe (K) on its Z axis.
3. Split the screen to show the Graph Editor; remove X and Y location curves, keeping only Z.
4. In the Graph Editor: select Z Location > Channel > Sound to Samples; choose the audio file; make sure timeline cursor is at frame 1 before running.
5. Extend the End Frame (e.g., 350) to cover the full audio length.
6. Convert the audio-driven graph to individual keyframes: Channel > Samples to Keys.
7. Select all keyframes (A), scale on Y axis (S + Y) to exaggerate amplitude, then move down (G + Y) so beats jump from zero upward (peaks at ~5).
8. Import audio into Blender's Video Sequencer: Shift+A > Sound; set start frame to 1; assign sequencer to scene.
9. Use the Empty's Z value to drive the smoke simulation parameters in Geometry Nodes using the new Grid Nodes for volumetric simulation.
10. Set up lighting and rendering for the final audio-reactive smoke visualization.

### Blender Nodes / Settings
- Empty (Plane Axis type) — Z Location as controller
- Graph Editor: Sound to Samples (Channel menu)
- Graph Editor: Samples to Keys (Channel menu)
- Keyframe scaling: S + Y (amplitude), G + Y (offset)
- Video Sequencer: Sound import, assign to scene
- Geometry Nodes Grid Nodes (Blender 5.0 volume grid)
- Simulation Zone with volumetric smoke
- End Frame: 350

### Difficulty
Intermediate

### Blender Version
5.0

### Tags
#geometry-nodes #simulation #animation #smoke-fire #volume #motion-design #blender-5x #intermediate

---

## Related Tutorials
- `volume-editing---blender-geometry-nodes-tutorial.md` — shares smoke-fire/volume/blender-5x/geometry-nodes; deforms an already-cached volumetric sim (bend/twist/split via Rasterize Points) rather than driving a live Grid Nodes smoke sim from audio.
