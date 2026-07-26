---
title: Create an Audio Visualizer with Geometry Nodes in Blender 5.2
source: YouTube
url: https://www.youtube.com/watch?v=h_Q91x_8dd4
author: Ryan King Art
ingested: 2026-07-26
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/create-an-audio-visualizer-with-geometry-nodes-in-blender-52/
frame_count: 0
frame_status: pending-selection
---

# Create an Audio Visualizer with Geometry Nodes in Blender 5.2

**Source:** [YouTube](https://www.youtube.com/watch?v=h_Q91x_8dd4)
**Author:** Ryan King Art
**Duration:** 20m39s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py create-an-audio-visualizer-with-geometry-nodes-in-blender-52 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] In this Blender tutorial, I'll show you how to create an audio visualizer with geometry nodes in Blender version 5.2.
[0:21] So in Blender version 5.2, there was a new node that was added in the geometry nodes called Sample Sound Frequencies.
[0:27] And we're going to use this to create the audio visualizer.
[0:30] So for this tutorial, the follow along, you are going to need to use Blender version 5.2 or a later version.
[0:35] If you'd like to purchase the tutorial project files, you can also get those with the links in the description on my Gumroad store and Patreon page.


### 3d Modeling [0:42]
**Transcript (timestamped):**
[0:42] So in a new scene in Blender, I'm just going to delete everything and we're going to go to the AdMunue and I'm just going to add a plane.
[0:48] And we're going to use this to create the bars for the audio visualizer.
[0:51] So I'm going to go into Edit Mode and I'm going to hit 7 on the numpad to go to Top View.
[0:55] So I'm now going to select everything and I'll hit Shift D to duplicate and then I'll click and drag with my middle mouse wheel to move everything over on the X axis.
[1:02] And then I'm going to hold down the Ctrl key so it moved by increments.
[1:05] And I'm going to move it over so it's two of these Blender mini-grids over by the other one.
[1:10] So now if I zoom in here, you can see it's moved two grids over.
[1:13] Now before I do anything else, I'm going to hit Shift R.
[1:16] So Shift R is going to repeat the last action, so it's going to duplicate it and move it over.
[1:21] And if we zoom out until we can see these larger Blender grids, I'm going to continue to hit Shift R and just keep on pressing Shift R until we get about halfway.
[1:29] So I'm just going to go a little bit farther about like that.
[1:32] So now we're about halfway.
[1:34] But you can of course make this whatever size you want, but these are going to be the bars for my audio visualizer.
[1:39] Now what I'm going to do is hit 7 to go to Top View and I'll hit A to select everything.
[1:43] And I'll hit U to unwrap because we do want to unwrap this.
[1:46] And I'm going to unwrap it, Project from View.
[1:49] And this is flattened from our view.
[1:50] So if I go over to the UV Editor right here and zoom in, you can see I was just flattened right down there from our view.
[1:56] And this is important because we're going to use the frequency value and the geometry nodes and we're going to map it to the UV unwrapping.
[2:02] And I also want to make sure that this isn't rotated up like this.
[2:05] So if it is, you can rotate it by 90 degrees.
[2:07] I want to make sure that it's going back and forth like this and the length of it is going along the X-axis.


### Add Music [2:12]
**Transcript (timestamped):**
[2:12] So now what I want to do is add in the audio.
[2:14] So what we're going to do is actually jump over to Geometry Nodes.
[2:17] Let's click on New to add a new Geometry Nodes setup.
[2:20] Now I do want to open up the video sequencer down here so I can add the audio.
[2:24] So I'm going to click down here when the crosshair appears and click and drag up to split the window.
[2:28] And then I'll click, drag over and let go just to split this window.
[2:32] Now this window here, if I click right above me, I'm going to change this to the video sequencer.
[2:37] So let me just make this bigger so you can see it.
[2:39] So here it is, change it to video sequencer.
[2:41] Now if I click on New, what it's going to do is create a new Blender scene.
[2:45] But I don't want to create a new scene.
[2:46] So I'm instead just going to click on the dropdown and add our existing scene.
[2:50] Now you can of course use whatever music you want, but what I'm going to be doing is using this Wake Up song from Sasha Enda on enda.app.
[2:57] So I'll have the link in the video description and it's royalty free music that you can use in YouTube videos.
[3:02] So I'm just going to drag and drop the music from my file browser into the Blender video editor.
[3:08] And then I'm just going to drag it here and I'm going to make sure it's at frame one.
[3:11] Make sure it's exactly at frame one.
[3:13] So now when I play this, I can hear the music.
[3:15] So we're now going to add it into geometry nodes.
[3:18] So I'll hit Shift-A for the Add menu.
[3:20] I'm going to search for sound and I'm going to add the sample sound frequencies.
[3:24] And again, this is a new node in Blender version 5.2.
[3:27] So make sure you're using 5.2 or a newer version.
[3:30] And then we don't need to open it because if I just click on the dropdown, you can see there's the music.
[3:34] So I'll just add it in.


### Geo-Nodes [3:35]
**Transcript (timestamped):**
[3:36] Now we want to make sure to sync up the node sound with the actual music here.
[3:40] So to sync this up, we're going to search for a scene time.
[3:43] Let's add the scene time node and we're going to put the seconds here into the time.
[3:48] So now when I play this, it'll be synced up with the scene time.
[3:51] So now what I want to do is put the frequencies along the UV map.
[3:55] So we need to actually add the UV map data.
[3:57] So what I'm going to do is search for a named attribute.
[4:00] Let's drop the named attribute right here and we want to add in the UV mapping data.
[4:05] Well, if I select the object and go down here to the object data properties,
[4:08] I'm going to open up the UV maps and you can see this is called UV map.
[4:12] So if it is click on it and hit control, say to copy, I'm going to click here on the name and hit paste.
[4:17] So UV map and hit enter.
[4:19] So this way we have this exact UV map data inside geometry.
[4:23] And it's important that the name is exactly the same.
[4:25] Now what I want to do is just use the X value of the UV mapping.
[4:29] So not the X, Y and Z, but just the X.
[4:31] So what I'm going to do is search for separate XYZ and I'm going to put that attribute into the vector.
[4:36] And then we're going to take the X value and we're going to put this into the low frequencies and the high frequencies.
[4:43] Now if I go back over here to the UV editing workspace, because this is going along the X axis, if I hit G to grab and then hit X,
[4:50] you can see it's going along the X axis.
[4:52] That way it's going to put the frequencies along the UV mapping.
[4:55] So we'll go back here to geometry nodes.
[4:57] We should also save the project.
[4:59] So I'm just going to save this project.
[5:01] Now later on when we can actually see the effect, I'm going to want to control the strength of the audio visualizer.
[5:06] So what I'm going to do is search for a map range node and drop it here between the separate XYZ and the high value.
[5:13] Then I'm going to drag it down and it'll hit Shift to duplicate and drop it here above here on the low values.
[5:19] So this way the UV mapping data is going through a map range and with the map range we can basically tell the values to be larger or smaller.
[5:26] So you can sort of think of like a map range being sort of like a color ramp where you can control the black and white values,
[5:31] but the map range is more customizable.
[5:33] So again we're just going to use these to control the low and high frequencies.
[5:37] Now what I want to do is actually make it affect the geometry.
[5:40] So to do this we're going to search for the extrude mesh.
[5:43] So we're going to put the sample sound frequencies into the extrude mesh so that when there's more music it's going to extrude up higher.
[5:49] So what we're going to do is we're going to take the group input here and we're going to put this into the mesh.
[5:54] And then let's just preview the extrude mesh.
[5:57] So we're just going to Shift Alt select the extrude mesh to preview.
[6:00] And then what we're going to do is take the amplitude and we're going to put this into the offset so that purple offset value.
[6:06] But now what we need to do is we need to mix it with the normal data so the normal is the direction of the faces.
[6:11] So let's search for a normal and we're going to add the geometry read normal and stick this here.
[6:16] Then what we're going to do is search for scale and we're going to add a vector math scale and stick this here.
[6:21] Now the normal is going to go into the vector and the amplitude is going to go into the scale.
[6:26] And then make sure the vector math scale is going into the extrude mesh offset.
[6:30] Now this offset scale right here if I just make this bigger you can see it says offset scale.
[6:34] This is going to be like a strength value so I'm going to turn this up to like a 40 so it's stronger.
[6:39] But when I play this you still can't really see anything.
[6:42] So what we want to do is make it a lot stronger so I can actually see it.
[6:45] So we're going to go back over here to the map range.
[6:48] So on the first map range what I'm going to do is go down here to the two min and I'm going to turn this up to 250.
[6:55] So it's quite a bit stronger.
[6:56] Then I'm going to go down here to the second map range and this two min I'm going to turn to 600 again so it's a lot stronger.
[7:03] And now when I actually look at this on side view you can see it's popping up and when I play this you can see it's actually affecting things.
[7:09] And then here on the two max I'll turn this to a 50.
[7:12] So these are the values that I find work pretty well but you can of course customize this and change it how you want.
[7:17] So now I can play this so we can take a look at it and you can see that is looking really cool.
[7:22] So a very cool audio visualizer.
[7:24] Now I find that this 250 value on the two min is actually really important because if I turn this down you can see that it kind of loses like a lot of the variation.
[7:32] Whereas instead now with the two min turned to zero it just kind of slowly goes up.
[7:36] But if I turn this to a pretty high value like maybe 250 or 300 or something now you can see there's a lot more variation in the sound frequencies.
[7:44] And then also this two min is kind of just changing like the overall strength.
[7:47] And then also this two max which kind of affect the side of it.
[7:50] So you can play around with all these values the two max and also that two min.
[7:55] You can also play around with like this value here the from min.
[7:58] But I found that the most useful values to play around with is the two min on the top one and then the bottom one the two min and two max.
[8:04] Now what you can also do is play around with the UV map.
[8:07] So if I select the object we're going to go over here to the UV editing.
[8:10] Now what you can do is you can scale it and you can see if I make it really big you can see the ones over here on this side they're going to be all the same.
[8:16] And then the ones over here are going to be all the same.
[8:19] But the ones in the middle those are the ones which are going to have the variation.
[8:22] And that's because here in the UV island you can see here's this side of the UVs and then this side of the UVs and we only have these three in the center.
[8:28] Or if I like scale it way down but it is going to be a little bit smoother now because it's only one small area.
[8:34] So I find out the best thing to do is to just scale it up so that this side is on this side of the UV grid and then this side again is on the other side of the UV grid.
[8:42] And that way you will get like a lot of variation.
[8:44] Now also what we can do is go back here to geometry nodes and let me open up this here the sequencer and we just need to take the end frame we just need to drag the end frame up.
[8:54] So it goes all the way to the end of the song.
[8:56] And now we can play this and jump through other parts of the song and just check out our animation.
[9:01] So that is very cool.
[9:04] Now there's a few more things that I want to do to make this look pretty nice.
[9:14] So here in the geometry nodes I'm going to go to the very end of the geometry node setup and I'm going to search for the bevel, the mesh bevel.
[9:20] This is also a new node that was recently added to geometry nodes.
[9:24] So I'm going to add the mesh bevel and if I zoom in you can see we have a really nice bevel there in our cubes.
[9:28] And I'm going to turn the segments up maybe to like a three or a four and then it will just shade the object smooth.
[9:33] And then I can also add a material to this.
[9:35] So I'm going to search for the set material node and put here after the mesh bevel and on the set material I just need to choose a material.


### Lights-Materials [9:41]
**Transcript (timestamped):**
[9:41] So I'm going to go to the materials.
[9:43] Let's click on new and then here on the set material I can just add that material.
[9:47] So you can end the tutorial here if you want to but now I'm going to go through and create a really cool setup where we have like some cool grungy metal and some cool like colored lights.
[9:55] So I'm going to go back here to the layout.
[9:57] So I'll hit shift a for the admin you and I'm going to add a camera and then I'll move my view to right about here.
[10:02] And I'll hit control and then pad zero which is going to bring the camera to my view and then I'll hit G to grab also hit G and then click with my middle mouse wheel to move the camera back like that.
[10:13] And I'll also go into the rendered viewport mode and I'll hit control B and drag a box around the camera to add a camera boundary.
[10:20] Now you could definitely do this in the EV rendering engine because EV will render faster.
[10:24] I think cycles looks a bit nicer though so I'm going to use cycles but if it's taking too long to render you could definitely use EV.
[10:30] I'm also going to go to the admin you and add a plane and I'll just scale up the plane.
[10:34] So it should make the plane really big something like that stick it there.
[10:38] And then also if I go back to solid view I just want to move the plane down so the plane is slightly below all of the cubes there.
[10:45] So if I go back to the starting now you can just see the cubes and they look like they're sitting on the top of the plane.
[10:50] Now also if I go into edit mode I think I need to hit shift and to recalculate the normals because it looks like the normals got flipped.
[10:56] I think that's because I scaled up the plane in the wrong direction.
[10:59] But now what I want to do is make a basic backdrop.
[11:02] So I'm going to select these two vertices and I'll extrude them up on the Z axis.
[11:06] And then if I select these two vertices again I'll hit control B to add a bevel and I'll scroll my mouse wheel a bunch of times.
[11:13] Click right there and then I'll go back to object mode and just shade it smooth.
[11:16] So let's go into the rendered view and go into the camera view and let's go to the world properties and I'm going to delete the world.
[11:22] So it's fully black and then I'll hit shift A for the add menu and I'm going to add some lights.
[11:27] So let's go here and add an area light.
[11:30] Let's move the area light over and I can scale it up.
[11:33] And if I go here to the object data properties let's turn the power up to maybe like a thousand so it's brighter.
[11:38] And then what I can do is just drag this exposure to make it even brighter.
[11:42] So now I can rotate this and let's just play this a little bit and find a spot where they're coming up a lot.
[11:48] So something like that where the audio visualizer is coming up a lot and now I can just kind of move this.
[11:53] Let's scale it up.
[11:54] And then what I could do is change the color.
[11:56] So maybe I'll make this like a cool like sci-fi blue color, something like that.
[12:01] And then I'll turn the exposure up again.
[12:03] And then also I don't really like this grid right down here.
[12:06] So if I just click here on the overlays, I'm just going to hide the grid and the floor and the axes just because I like to get that out of the way most of the time.
[12:13] So then what I could do is just duplicate this light by hitting shift D. I can rotate it over.
[12:18] You can also double tap R to use the track bar rotation.
[12:21] And I'm just going to put another light over here.
[12:23] And this one I could maybe make like a red color.
[12:26] So we're getting some cool like blue and red kind of like sci-fi colors like that.
[12:30] And then I could duplicate this one again, scale it down, rotate this one over and maybe have another one here on the side.
[12:36] And this one I could even make it a bit brighter and make it like a lighter blue.
[12:41] And this one here on the top could maybe be like a darker blue, something like that.
[12:45] I also want to play around with the color management.
[12:47] So if I go here to the render properties and scroll down, I'm going to set the view to filmic or you can use a GX.
[12:53] I just like filmic. I think it looks nice.
[12:55] And then at the look here, I'll change it to very high contrast.
[12:57] So this will pop out the colors and make everything more contrasted and saturated.
[13:01] And I think this light on the top will make a bit brighter.
[13:04] And then also maybe this red light, click on the red light and make this a bit brighter.
[13:08] You can of course have fun with this and make your own unique setup.
[13:12] I'm going to now select the object and I'm going to go to the shading workspace and I'll go into the render view and I'll just make a cool grungy metal.
[13:19] So I'm going to turn the roughness down so it's shiny and I'll turn the metallic up.
[13:23] So now I have a cool metal.
[13:24] And then what I could also do is search for a noise texture, drop this here and with the noise texture selected, I'll hit control T.
[13:32] That's using the feature of the no-dringler out on.
[13:34] If you have the no-dringler enabled and it's going to add the texture coordinate mapping and I can just put the object into the vector.
[13:40] So it places the texture on the object more evenly and then I can put the factor into the roughness.
[13:46] So now you can see there's a bit of roughness variation.
[13:48] And then I can change the scale to maybe like a one and I'll turn the detail up to 15 and I'll turn the roughness to maybe like a 0.9 or a 1.
[13:56] So now we get some cool roughness variation.
[13:58] But then to control the roughness, I'm going to add a color ramp and I'll put the color ramp between the noise texture and the principle shader.
[14:04] And I'll take the black tab and maybe drag it up a bit and then I'll take the white tab and maybe drag it down a little bit.
[14:10] So this is an easy way to control the roughness.
[14:12] So if it's lighter, the metal is going to be more rough.
[14:14] If it's darker, the metal is going to be more shiny.
[14:17] So just something like that and you can already see we have a really cool metal and I really like how the reflections look.
[14:22] I can even duplicate these lights, maybe rotate this and add another one.
[14:25] I really like the red and blue, maybe add like a hint of purple.
[14:28] And then I can also add the same metal to the ground.
[14:30] So if I just select the ground, we're going to click on the drop down and add that same material.
[14:35] Now that's a little bit too shiny.
[14:37] So I think I want to duplicate this material and make it a bit more rough on the ground.
[14:40] So I'm going to click on this button here, which is going to duplicate the material.
[14:43] So now it's separate and then to make it more rough, I can just search for a huge saturation value and put this in between the color ramp and the principle shader.
[14:51] And then I can just drag this value up and that's going to make it more rough.
[14:54] So it still looks like a metal material, but it's quite a bit more rough.
[14:58] And then for the final render, what I could also do is go to the render properties and turn on the motion blur because the motion blur is going to make it look a lot more interesting.


### Compositing [15:06]
**Transcript (timestamped):**
[15:06] And then we could also do some compositing.
[15:08] So I'm just going to hit F12 to render a single image.
[15:11] And then we're going to jump over to Blender's compositor.
[15:14] We're going to click on new to add new compositing nodes.
[15:17] And what I'm going to do is search for a glare node.
[15:20] So let's drop the glare right here and I'll change it from streaks to the bloom.
[15:26] And then in the medium quality, I'll turn it to high quality.
[15:29] You could also change a tint for the bloom.
[15:31] So you could maybe make it like red or blue or something.
[15:34] And we could also turn the strength up.
[15:36] So maybe turn the strength up to like a three.
[15:38] So it's a bit brighter.
[15:39] And then what I could also do right behind me in the very corner here, there's the chromatic aberration.
[15:44] So I'll drop this here and I'll change it from scale to a lens dispersion.
[15:48] And then I'll just turn the factor way down so it's a bit more subtle.
[15:51] But that just adds kind of a cool effect, kind of a lens dispersion to the edges of the image.
[15:56] Let's go back here to the layout now.
[15:58] And in rendered mode, if I click on the drop down arrow, I'm going to change the compositor to always.
[16:03] So I can see what it looks like with the compositing.


### Rendering [16:05]
**Transcript (timestamped):**
[16:05] So once you have something that you like, we can render the images to frames.
[16:08] And as I mentioned, Eevee will probably render a lot faster, but I think cycles looks a bit nicer.
[16:13] So I'll use cycles, but it does look pretty similar.
[16:16] So let's go here to the output properties and we'll go down here to file format.
[16:20] And instead of PNG, I'm going to change it to JPEG so that each individual image is in a super large file size.
[16:26] But then to make sure there isn't any quality lost, I'll turn the quality to 100%.
[16:30] And then we need to choose an output.
[16:32] So we're going to click on this file icon.
[16:34] Let's locate to the folder where we have our project files and I'll click on the plus to add a new folder.
[16:38] I'll call this frames and I'll go into the folder and then I'll click on the accept button.
[16:43] And you can also optimize the scene to make sure it renders the fastest.
[16:46] So of course, you could use the Eevee rendering engine if you want to.
[16:49] I'm using cycles, but what I am going to do is open up the light paths and I'm going to turn down the light paths.
[16:54] So I'll turn off the caustics, I'll turn off the glossy and the indirect light.
[16:58] And then here on the max bounces, I'll turn a lot of these to two because if I turn them to zero,
[17:02] it might just make the scene look a bit weird and a bit dark.
[17:05] And then the transmission I can turn to zero and the transparent I can turn to zero.
[17:09] So by turning down the light paths, the cycles rendering engine will render faster.
[17:13] But if you're using the Eevee rendering engine, then you're not even going to have the light paths.
[17:17] So you could just optimize the scene so it renders faster.
[17:20] You can also turn the samples down if you don't want to use too many samples.
[17:23] And then just save the project and you'll just click on render and you'll render the animation.


### Video Editing [17:28]
**Transcript (timestamped):**
[17:28] So once the animation is finished, we just need to compile it together into Blender's video editor with the music.
[17:33] So I'm going to open up a completely new Blender file and click on a file, new, and just open up a new video editing.
[17:39] So here in Blender's video editor, I'll hit shift day for the add menu and I'm just going to add image sequence.
[17:44] And I'm just going to locate to the folder where I saved the images.
[17:47] So this is my other version that I rendered out and I'm going to hit the A key to select all the images and I'll click on add image strip.
[17:53] And then I want to drag this over and I want to make sure I put it right here on frame one.
[17:57] So we can align it up with the audio.
[17:59] Then I want to drag and drop the audio from my file browser into Blender and let's just drag it down here.
[18:05] And then we can just play this. Let's make the end screen a lot longer.
[18:08] And then I can just play this and take a look at it.
[18:11] And you can see it is following along with the audio. So that is very cool.
[18:17] So then what you want to do is set an end frame. So I'll just have it render 20 seconds.
[18:21] So you can see the end frame is about high 500. So I'll just set the end frame to 500 down here.
[18:26] And then to render out the animation, we want to go here to the output properties.
[18:30] Let's scroll down here. We want to click on this here to sign output.
[18:34] And I'll just save it in this folder with my project files and click on accept.
[18:38] And then here on the media type, I'm going to set it to video.
[18:40] And if I open up the end coding and scroll down, I'm going to leave everything at the default.
[18:44] And here on the audio codec, I want to make sure I have some kind of audio codec.
[18:48] So the video actually has audio and I'm just going to use AAC.
[18:51] So then you'll just need to click on render and click on render animation.


### Closing [18:55]
**Transcript (timestamped):**
[18:55] So that's how to create an audio visualizer with the new sound node in Geometry Nodes in Blender version 5.2.
[19:00] So thank you for watching and I hope you enjoyed the tutorial.
[19:03] And if you'd like to help support the channel, you can also purchase the tutorial project files on my GEMROD STORY and Patreon page.
[19:09] So the links to that are in the description.
[19:11] And if you'd like to watch more of my Geometry Nodes tutorials, then I also have a Geometry Nodes playlist with more Geometry Nodes videos.
[19:17] So you can check that out right up there on the end screen or the link in the video description.
[19:21] So I hope you enjoyed the video and thank you for watching.
[19:55] I'll see you in the next one.
[20:25] Thank you.



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
