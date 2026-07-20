---
title: Camera Tracking in Blender for Beginners | Motion Tracking Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=IvyfdxkABKU
author: 3Dnot2D
ingested: 2026-07-20
blender_version: "4.x (AgX default color management, Cycles GPU)"
tags: [camera, compositing, rendering, cycles, hdri, lighting, product-viz, intermediate, blender-4x]
extraction_status: complete
frames_dir: tutorials/frames/camera-tracking-in-blender-for-beginners-motion-tracking-tutorial/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Camera Tracking in Blender for Beginners | Motion Tracking Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=IvyfdxkABKU)
**Author:** 3Dnot2D
**Duration:** 19m50s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this video, we will learn the basics of motion tracking or how to 3D track your camera inside the Blender and how to add additional 3D elements in your scene to make them appear like they're belonging there.
[0:10] So let's do it.
[0:11] Let's press A to select everything, X and delete everything from the scene because we don't need that at all.
[0:16] And let's switch a layout.
[0:17] Let's go to the plus VFX and motion tracking because we will track the motion of our camera.
[0:22] This is how the layout looks.
[0:23] And now we need to open our footage.
[0:25] By the way, you have the links down the description so you can download both the footage and the 3D file that I
[0:29] will use here for this example so you can follow along.
[0:32] All right, now that we covered that, you can either just directly drag and drop our footage or the scene or click open and find it.
[0:38] Or what I prefer what I found that Blender works a little bit better with an image sequence.
[0:43] So instead of dragging your video file, which is perfectly okay, you can just render your video file as an image sequence in any of 3D, any of video editing
[0:51] software like Premiere Pro, the Winters, all Final Cut, it doesn't matter.
[0:55] And now I will select everything here, just drag and drop it.
[0:58] And here we have it.
[0:59] First thing that you will probably notice or maybe not is that the footage is a little bit washed out.
[1:04] The colors are a little bit different.
[1:06] The contrast is different.
[1:07] And that's because the color management in Blender by default is AGX.
[1:11] It's not standard.
[1:12] So we need to change that.
[1:14] Go here to the render tab, go all the way down to the color management and switch from AGX to the standard.
[1:20] And you will see before and after.
[1:22] This is much better.
[1:23] We need the standard one.
[1:24] And now that we are here in render tab, switch from EV to Cycles and from CPU to GPU because we will use
[1:29] Cycles for these type of jobs for VFX because Cycles give you a photo realistic result.
[1:35] You want that.
[1:36] All right.
[1:37] Now that we covered that, we need to tell the Blender how many frames we will work with.
[1:41] And we can just click on set scene frames and Blender will automatically set the amount of frames that we have here.
[1:50] The footage is 239.
[1:54] Perfect.
[1:54] And you can see this purple line.
[1:56] It's a jagged a little bit.
[1:57] So it's not completely purple.
[2:00] And that's because we didn't load everything into the cache from the footage.
[2:04] So let's do that.
[2:05] Let's prefetch it.
[2:07] Now everything is full and you can easily scrub back and forth without any hiccups.
[2:13] Perfect.
[2:14] Now what we need to do is to track the scene.
[2:16] There are two ways how you can track the scene.
[2:17] You can track it manually.
[2:18] You can track it automatically.
[2:20] I almost always use automatic method, but it's important to know how to do it manually because
[2:26] sometimes you will be in need to manually add some trackers to the scene.
[2:29] So let me show you how to do it manually and then let's do it automatically.
[2:32] So let's zoom it right to this portion of the scene.
[2:36] And here you have the markers.
[2:38] We need to add markers.
[2:39] Blender need at least eight markers per frame in order to be able to perform proper 3D tracking.
[2:45] So we can click add and just click somewhere in the scene and we are adding our marker.
[2:51] Marker has two segments.
[2:53] It has the pattern size and in this rectangle here you can see everything that is inside
[3:02] it will be treated like a pattern and Blender will try to match that pattern in every single frame.
[3:08] And if you press Alt and S you will see the search region, the search size.
[3:13] And this is the size, the region where Blender will try to find this pattern.
[3:18] So the smaller the search size is, the more precise tracking will be and the smaller the pattern is,
[3:24] again, the more precise as tracking will be.
[3:27] But you don't need to think too much about that.
[3:30] The default value work most of the time.
[3:33] Let's press Alt S again to delete it to hide the search size.
[3:37] And here you can see there is a pattern size and the search size.
[3:41] So you can add another marker.
[3:43] Here you can see this is much higher the pattern size than this and the search size also much bigger than this.
[3:53] So let's press Alt S.
[3:55] I will delete both of these markers and this is how you manually add the markers.
[4:00] Remember you need to have at least eight per frame in order for Blender to properly track it.
[4:06] And here you have some presets.
[4:08] So blurry footage will have certain pattern and search size.
[4:12] Then fast motion against certain and so on and so forth.
[4:15] So I will use default, which works perfectly fine for this scene.
[4:19] And we will use automatic method and how to do it.
[4:22] Just go to the first frame.
[4:24] Okay, right there.
[4:25] Click the text features and Blender will automatically detect the best tracking markers that will be good for our tracking.
[4:33] And now we need a few more things.
[4:37] We need to change the motion model.
[4:39] We have location, location, rotation, location, scale, location, rotation, scale, a fine and perspective.
[4:44] So a fine will work in most of the cases.
[4:47] If you're not sure what you can you're doing, a fine will cover you.
[4:51] But here if we go, we can see we have location changing.
[4:55] So we have motion and we have rotation.
[4:58] So we can go with location rotation.
[4:59] We can add the scale.
[5:00] So also it's not the wrong.
[5:02] So let's go with this.
[5:03] And also we want to check normalize.
[5:07] Here in this footage, the normalize is not that important, but normalize will normalize the lights
[5:14] while tracking the intensity of the light.
[5:16] And this will be a little bit slower, but it will be more precise.
[5:20] So I always like to check normalize.
[5:22] And one more thing, the tracking, this tracking setting extra.
[5:27] I want to correlation to set 0.9.
[5:31] And that basically means that Blender needs to be 90% sure that track is correct in order to continue tracking.
[5:37] Now all we need to do is to press either Ctrl T or click on this icon that means track forward.
[5:41] So let's track forward.
[5:43] This is how it looks.
[5:44] Now I want also to detect features right here at the end of the footage.
[5:49] So detect more features.
[5:50] By the way, if you want to detect even more features, you can open this menu right there.
[5:55] And for example, lower the distance a little bit, it will add more and more features and play with
[5:59] these threshold and margin.
[6:01] But for me, this is okay.
[6:03] So now let's track backwards.
[6:05] Perfect.
[6:05] We have more tracking markers.
[6:06] Now I want to go somewhere in the middle, somewhere here, for example, detect features,
[6:12] track forward and come back to the same keyframe and track backwards.
[6:18] Perfect.
[6:19] And maybe somewhere here to detect even more features.
[6:22] Perfect.
[6:22] Track forward and come back here and track backwards.
[6:26] Perfect.
[6:26] Now we have plenty of tracking markers.
[6:28] Some of them are perfectly fine.
[6:30] Some of them are really bad.
[6:32] We will delete bad ones.
[6:34] And now you can see here there are a lot of spikes.
[6:37] These spikes means that the tracking has a high error.
[6:40] So these markers are not good.
[6:42] You can either click on these spikes and just delete them manually.
[6:46] Or you can let Blender do it for you.
[6:49] I will show you both ways.
[6:50] So this is how you do it manually.
[6:53] But automatically is just by going from the track to the solve tab because now we need to solve the camera.
[7:01] First in the solve tab I like to set keyframes.
[7:05] So basically these keyframes A and B is the keyframes between those keyframes.
[7:11] Blending are detecting the parallax motion and everything.
[7:14] And if you set a keyframes like that, check the keyframes option here.
[7:19] Blender will do it for you automatically.
[7:21] For this case, let's do it manually.
[7:22] Let's press keyframe one.
[7:24] So from this to keyframe, I know 200.
[7:27] Let's detect the motion between these two.
[7:29] I think it's okay.
[7:30] And also I want to refine the focal length, optical center and radial distortion.
[7:34] So Blender will do everything for you automatically.
[7:37] Let's click the solve camera motion and depends on the complexity of the scene,
[7:41] of the amount of tracking markers, speed of your computer.
[7:43] It will be more or less time to do it.
[7:46] But the solve is done.
[7:48] The solve error is 2.38 pixels.
[7:50] This is pretty high solve error.
[7:53] The idea is to lower this error below one pixel.
[7:57] Ideally below 0.5, below half pixel.
[8:01] So how to do it?
[8:02] Well, we need to go to clean up here.
[8:05] And with a clean up, let's go here to filter tracks.
[8:08] I like to set this first at 10 and delete these.
[8:12] You can see I had identified 24 problematic tracks.
[8:15] Press X and just delete it.
[8:17] Solve the camera again.
[8:20] It will wait for a few seconds.
[8:22] Perfect.
[8:23] 0.47.
[8:25] This is amazing.
[8:26] We can do it even better, I think.
[8:28] We can change maybe here to, I don't know, 150.
[8:32] Let's see.
[8:33] Solve motion.
[8:34] Okay, 0.47.
[8:36] And now let's go to clean tracks.
[8:39] And we can move the reproduction error to something around maybe one.
[8:47] And let's clean all of this and see.
[8:49] Solve motion, 0.26.
[8:52] And you can play with these settings.
[8:55] Maybe seven.
[8:57] Let's delete that and solve camera motion.
[9:00] See if you can lower it more and more.
[9:02] The idea is to make it as close to zero as you can.
[9:06] But of course, 0.25 pixels, the quarter of the pixel is more than enough.
[9:11] And we will be there.
[9:13] And also, I didn't show you, but at the beginning, let's undo a few times.
[9:18] Let me show you that this is something that you want to see.
[9:20] So this is, I think this is our begin.
[9:25] Let's solve it again.
[9:29] We have 2.38.
[9:30] And if I deselect all the pixels, click somewhere out of the, these tracking markers,
[9:36] not pixels.
[9:37] If I click on this icon right there, I will see this blue line.
[9:41] And the goal is to make this blue line as straight as it can.
[9:45] Now you can see there are a lot of these spikes.
[9:48] We don't want that.
[9:49] Okay, so let's do what I did before.
[9:52] So, okay, 0.25 is perfectly okay for this.
[10:00] And the next step is to go all the way down, set the background, set up tracking scene.
[10:06] And you will see here we have things that looks crazy.
[10:11] We have the plane, we have the cube.
[10:13] And the orientation is not good.
[10:15] So we now need to set what is the floor, what is the origin, x,
[10:18] and y axis and the scale.
[10:20] So how to do it?
[10:21] First, let's set the floor.
[10:23] For the floor, we need at least, at least in some software at least in this software,
[10:27] three points, so three markers.
[10:29] I will go with this, this and this, for example, and let's press floor and you will see
[10:35] something crazy happen.
[10:36] Don't worry.
[10:37] Now let's find the origin point.
[10:39] I want to use this as an origin, okay, set origin.
[10:45] Perfect.
[10:45] And now we need to set the x.
[10:48] So this, compared to the origin point, will be x.
[10:53] So this will be x axis.
[10:54] And also let's set the scale.
[10:56] So for the scale, I don't know how long is between these two markers.
[11:04] For the scale, we need to select two markers.
[11:06] And let's approximate that this distance is, I don't know, around maybe two meters.
[11:14] So say two and set scale.
[11:16] And this is how it looks.
[11:18] If I grab the cube and move it one unit up and see maybe this is like two meters high.
[11:27] If we scale it, like imagine that this is person two meter high,
[11:34] something like that, or maybe, maybe we need to set this distance a little bit better.
[11:39] But the idea is when you're having your own footage and when you're
[11:44] making your own VFX and camera tracking, you always want to have something on the scene to
[11:49] know the real measurements so you can have the proper values here and see.
[11:54] So some reference that you know the distance between things in the scene and then just
[11:59] put it right here in Blender and you will have the proper values.
[12:03] Okay, now that we are finished with that, let's go to the layout here.
[12:07] Press zero to go to the camera view and also I will check the camera here
[12:11] and go to the camera options and go to the background images and move this opacity all the
[12:17] way up. So I want to see everything here.
[12:20] Also, I want to delete the foreground, the background
[12:24] collection. So I want all of this and I don't need this light.
[12:28] And also here, I want to go to foreground and background.
[12:32] I want to delete the background, set the background, press X and delete the background
[12:37] and leave only the foreground. Blender automatically set our tracking scene like that
[12:43] because it will render the foreground separately than the background separately
[12:48] and you will have something like that. I don't like that. I like to have my own control but
[12:53] this is how it looks. And now let's load our Volvo car 3D model in the scene.
[12:59] You can either open this scene and copy Volvo and paste it here or just append it here file
[13:05] and append to the scene however you want. I don't need this cube anymore.
[13:09] So let's paste our Volvo here and now I want to press M, new collection name it Volvo.
[13:17] Okay, like that and here we have a car. So I can press R and Z and rotate it on Z axis,
[13:23] something like that. And if I hide the ground for a moment, we will see how this looks. I can
[13:30] move the car G and shift Z somewhere here for example. Okay, and let's see. The track is amazing.
[13:42] We can zoom here to see how the wheel is fitting to the scene. Really nice. It's sticking really
[13:48] nice. If you press 1 to go to the front view, you can see the car is levitating a little bit about
[13:56] the X axis. So let's right click, select objects and G and Z and move it down like that, zero. And
[14:03] now it's a little bit better but this is perfectly fine. I really like it now. This is the end of
[14:09] the tracking tutorial. This is the point of 3D camera track. You can now add more elements here
[14:15] to the scene and it will perfectly stick with that like it's belonging there. But let's go a little bit
[14:22] forward. Let me show you how to add the lights and everything so this looks really nice. So if I go here
[14:29] to the rendering viewport, so basically rendering preview to see how this looks, this looks really
[14:36] cool but we don't see anything except the car and car is in the dark. So in order to see the car,
[14:42] you need to go to the render tab, not the car but the background. You need to go to the render tab
[14:46] and go to the film and set the transparent here. Perfect. And also if you want to see
[14:52] through the car window, you need to go transparent glass. Perfect. Now we need to match our light.
[14:59] So for that, you can go to polyheaven.com, go to HDRIs and find any of the HDRIs that you like.
[15:07] So we need outdoor, we need overcast. So let's see, overcast and find something that you think
[15:15] it suits best for that. I like this one, urban courtyard and you can download this one. The
[15:20] point is that has some building around and it's overcast and let's load this in the blender. I
[15:25] have already downloaded that. So in order to load it, go to here to the world, color, environment
[15:31] texture and now just open your EXR file that you downloaded. So is this one? Let's press open.
[15:39] And this is how it looks. If I go here, you can see also the reflection from the buildings, etc.
[15:44] You can also rotate it but here if you load the ground, you will see the shadows and everything.
[15:49] Okay, now what I like to do, let's go right here in the corner where the plus icon appear,
[15:57] the cross, just move it a little bit up and I want to switch to shader editor, objects world.
[16:05] And let's zoom this in, click on the image node, control T to load these two additional nodes.
[16:13] But for that, you need to go to edit preferences, add ons and you need to have node wrangler,
[16:19] node wrangler enabled. It's there in blender but it's not enabled by default. In case you don't
[16:25] have it enabled, just enable it, click save preferences and you're ready to go. Now with
[16:30] these nodes, you can go to rotation and Z and you can rotate this. And now if I go to this
[16:36] scene right there, let's see, I want to move this building somewhere here for fun. Why not?
[16:43] This looks cool, this looks cool. And also the ground, make sure that the ground is big enough.
[16:48] So something like that. Perfect. And there we have it. We can also change the color of the car.
[16:54] So click on the car right there and go to the materials and car paint, I want a little bit
[17:00] more metallic. So maybe maybe maybe a little bit more bluish, something like that. Maybe brighter,
[17:08] darker, whatever you want, play with that. And here we have it, we can render this out. So in
[17:13] order to render this out without a background, everything we need to do a few tweaking, let
[17:19] me show you how this looks currently. So I want this preview to be 128 and also the render 128.
[17:25] And the noise, I want to use the GPU. And also what I like to use here, I like to go to performance,
[17:31] just use persistent data and it will render a little bit faster for me. So now if I render this
[17:40] frame, press F12 and render this, you will see in a moment, it will render the car and the background,
[17:47] but I don't want the background to be loaded. I just want the car. So how to do it? Well, we need
[17:52] to go to compositing tab and there is a lot of there are a lot of nodes here. So we don't need
[17:57] any of this, we don't need this, I will delete it, I don't need this, I just need the car. So let's go
[18:04] with this. This is, oops, image, go to the image of compositor. And also if you want to see what
[18:12] is going on, we have only the car. And also you can see here the, yeah, this is perfectly okay,
[18:18] this is the end of our frame. This is the end of our frame. So this is why it looks like that.
[18:24] Let's go back to layout. And one thing that we forgot to do is to go to the plane here, go to
[18:31] the materials, add a new material to the plane. And I want to sample the color from the ground
[18:37] right there. So I want that. And also if you press, if you go with the roughness all the way back,
[18:43] you will see some reflections, we don't want that we want roughness all the way up because this is,
[18:48] this is not reflective material. And this is perfectly fine. Now you need to go here and
[18:55] choose a folder where we want to put your render image sequence and just render it out. So I will
[19:01] find my folder. Okay, I set my sequence here PNG with alpha eight bits, it's perfectly okay.
[19:08] For this purposes, for more advanced VFX and compositing, you will separate the shadow from the
[19:14] car and so on and so forth. But for this basic, it's more than enough, I will go to render,
[19:18] render animation and come back shortly. Now that the rendering is done, let's go to video editing
[19:23] software of your choice. For me, it's the winter resolve select all the image sequence, put it
[19:29] just about and this is the final result. You can see how beautiful the track is. I really love this.
[19:35] Looks really, really cool and realistic. And now if you want to see how I use the same principles,
[19:41] same ocean tracking techniques, and a little bit of fire effect to fool everyone that my oven is
[19:46] on fire, check out this video. See you there. Bye bye.



---

## Captured Frames

- [0:22] tutorials/frames/camera-tracking-in-blender-for-beginners-motion-tracking-tutorial/frame_000.jpg
- [2:45] tutorials/frames/camera-tracking-in-blender-for-beginners-motion-tracking-tutorial/frame_001.jpg
- [4:24] tutorials/frames/camera-tracking-in-blender-for-beginners-motion-tracking-tutorial/frame_002.jpg
- [7:48] tutorials/frames/camera-tracking-in-blender-for-beginners-motion-tracking-tutorial/frame_003.jpg
- [9:36] tutorials/frames/camera-tracking-in-blender-for-beginners-motion-tracking-tutorial/frame_004.jpg
- [10:35] tutorials/frames/camera-tracking-in-blender-for-beginners-motion-tracking-tutorial/frame_005.jpg
- [13:42] tutorials/frames/camera-tracking-in-blender-for-beginners-motion-tracking-tutorial/frame_006.jpg
- [16:05] tutorials/frames/camera-tracking-in-blender-for-beginners-motion-tracking-tutorial/frame_007.jpg

---

## Structured Notes

### Core Technique
Full 2D-to-3D camera match-move pipeline in Blender's Motion Tracking workspace: solving a real camera's motion from footage, establishing scene scale/orientation from tracked markers, then compositing a 3D CG object (a car) into the live-action plate with HDRI lighting matched to the shot.

### Summary
3Dnot2D tracks a handheld shot of a plaza with a fountain, solves the camera's 3D motion, defines the floor/origin/axes/scale from tracker points, and drops a Volvo 3D model into the reconstructed scene so it sticks to the ground and follows the camera perspective correctly. The second half covers making the CG object render believably: transparent film + transparent glass so only the car renders, a Poly Haven overcast HDRI loaded into the World shader (rotated via Node Wrangler's Mapping node) to match the footage's lighting and pick up building reflections, a ground-shadow-catching plane sampled to match ground color, and finally compositing the alpha-rendered car frames back over the original footage in a video editor.

### Key Steps
1. **Set up the workspace**: clear the default scene (A, X, Delete), switch to the "VFX and Motion Tracking" workspace layout, and load footage — either the video file directly or (the presenter's preference) an image sequence rendered out of any NLE, since Blender scrubs/caches image sequences more reliably.
2. **Fix color management first**: Render Properties > Color Management, switch from the default AgX to Standard so the footage isn't washed out/contrast-shifted; also switch the render engine to Cycles and the device to GPU for photorealistic VFX compositing later.
3. **Sync the timeline**: click "Set Scene Frames" in the clip editor to auto-match the scene frame range to the footage length, then "Prefetch" to cache all frames into RAM (fixes the jagged/incomplete purple cache indicator bar) for smooth scrubbing.
4. **Manual tracking markers (concept)**: Add a marker in the clip; each has a Pattern Size (the box Blender pattern-matches per frame) and a Search Size (Alt+S, the region searched for that pattern next frame) — smaller pattern/search regions give more precise (but less robust) tracking; Blender needs at least 8 markers per frame for a usable 3D solve. Tracking Settings has presets for footage types (blurry, fast motion, etc.); Default works for typical shots.
5. **Automatic tracking**: on frame 1, click "Detect Features" to auto-place trackable markers; set Motion Model (Loc / Loc+Rot / Loc+Scale / Loc+Rot+Scale / Affine / Perspective — Affine is a safe default), enable Normalize (slower but more precise, accounts for lighting change during the shot), and set Correlation to 0.9 (Blender requires 90% pattern-match confidence to keep tracking a marker).
6. **Track forward/backward**: Ctrl+T (or the track-forward icon) tracks selected markers through the footage; repeat Detect Features at the end of the clip and partway through, tracking forward then back to each keyframe, to build up a dense, well-distributed marker set across the whole shot.
7. **Solve the camera**: in the Solve tab, set two keyframes (A/B) far enough apart for Blender to read parallax (or enable the auto Keyframe checkbox to let Blender choose), enable Refine: Focal Length, Optical Center, and Radial Distortion, then click Solve Camera Motion. Target a Solve Error under 1 px (ideally ≤0.5 px / a quarter-pixel is "more than enough").
8. **Clean up bad tracks**: switch to Clean Up, use Filter Tracks with an error threshold (e.g. 10, then progressively lower — 7, etc.) to auto-select and delete (X) high-error tracks, then re-run Solve Camera Motion after each cleanup pass; watch the Average Error graph (a blue/red/green line per axis) — the goal is to flatten out the spikes.
9. **Set up scene orientation**: in Set Up Tracking Scene / Orientation panel — select 3 markers on the ground plane and click "Floor" to align the world floor to them; select one marker and click "Set Origin"; select a second marker to define "Set X Axis"; select two markers a known real-world distance apart, type that distance, and click "Set Scale" to give the scene real-world units. Then Ctrl+P / "Setup Tracking Scene" from the bottom of the panel generates camera + background/foreground plane objects automatically (delete the auto-generated background/foreground split and light if you want manual control instead).
10. **Composite the 3D asset**: append/copy the CG model (a Volvo car) into a new collection, rotate/position it to sit on the tracked ground plane, and verify it "sticks" to the footage (e.g. wheel contact point) when scrubbing — check Front/Numpad-1 view to catch any residual floating offset and nudge with G, Z.
11. **Light to match**: Render > Film > Transparent (so only the CG renders, not the background plate) plus "Transparent Glass" for see-through car windows; download a Poly Haven overcast outdoor HDRI matching the shot's lighting mood, load it via World > Color > Environment Texture; use Ctrl+T (Node Wrangler add-on, enabled in Preferences) on the Environment Texture node to add Mapping + Texture Coordinate nodes so the HDRI can be rotated (Mapping > Rotation Z) to align reflections/building placement with the plate.
12. **Ground shadow catcher + render**: give the tracked ground plane a material with color sampled (eyedropper) from the footage's actual ground, Roughness maxed out (non-reflective) so it only catches contact shadows; set Render preview/final samples (e.g. 128), enable Persistent Data for faster batch rendering, then in Compositing strip the node tree down to just the render layer's Image output (skip the auto-generated foreground/background split nodes) so the render is a car-only PNG sequence with alpha.
13. **Final assembly**: render the animation to an 8-bit PNG (with alpha) image sequence, then import that sequence over the original footage in a video editor (e.g. DaVinci Resolve) for the final composited match-move shot.

### Nodes / Settings
- **Motion Tracking workspace / Clip Editor**: Marker panel (Add/Delete), Tracking Settings (Pattern Size, Search Size, Motion Model, Normalize, Correlation threshold), Track > Detect Features, Track Forward/Backward (Ctrl+T).
- **Solve tab**: Keyframe A/B selectors, auto-Keyframe checkbox, Refine (Focal Length, Optical Center, Radial Distortion), Solve Camera Motion button, reported Solve Error (px).
- **Clean Up tab**: Filter Tracks (error threshold slider), Clean Tracks (reprojection-error threshold), Average Error graph view.
- **Orientation / Scene Setup panel**: Set Floor, Set Origin, Set X Axis, Set Scale (with a real-world distance value), and the overall "Setup Tracking Scene" action that spawns camera + background/foreground plane objects.
- **Render Properties > Color Management**: View Transform set to Standard (from default AgX) for accurate footage color; Render Engine = Cycles, Device = GPU.
- **Render Properties > Film**: Transparent enabled, plus Transparent Glass, so the render outputs a car-only alpha PNG.
- **World Shader**: Environment Texture node (loads an .exr HDRI from Poly Haven) → Mapping node (Rotation Z to align reflections) → Texture Coordinate, wired via Node Wrangler's Ctrl+T shortcut (requires the Node Wrangler add-on enabled in Preferences).
- **Ground plane material**: Base Color sampled via eyedropper from the plate's ground color, Roughness set to maximum (fully matte, non-reflective) to act as a shadow-catcher without visible highlights.
- **Compositor**: simplified node tree — Render Layers > Image output only (auto-generated foreground/background split nodes removed) for a clean car-only render pass.
- **Performance settings**: Preview/Render Samples ~128, Denoise enabled, Persistent Data enabled for faster sequential frame renders.

### Difficulty
Intermediate

### Blender Version
Blender 4.x (AgX is the default View Transform, switched to Standard; Cycles + GPU device; Node Wrangler add-on used for HDRI node setup)

### Tags
camera, compositing, rendering, cycles, hdri, lighting, product-viz, intermediate, blender-4x

---

## Related Tutorials
- [Using Geometry Nodes for VFX in Blender](using-geometry-nodes-for-vfx-in-blender.md) — near-identical VFX pipeline (camera tracking, shadow catcher, HDRI matched to footage brightness) integrating a 3D asset into live-action footage; extends this video's approach with ACES color and Geometry Nodes-driven elements.
- [I recreated a movie scene in Blender + Nuke (Complete Tutorial)](i-recreated-movie-scene-in-blender-nuke-complete-tutorial.md) — shares the camera + lighting + compositing pipeline for integrating CG assets into a shot, at a larger production scale (Kong: Skull Island recreation) with multi-pass rendering into Nuke instead of Blender's compositor.
- [How to render faster in Blender (Cycles)](how-to-render-faster-in-blender-cycles.md) — Cycles/GPU optimization techniques directly applicable to speeding up the per-frame car renders in this tutorial's image-sequence workflow.
