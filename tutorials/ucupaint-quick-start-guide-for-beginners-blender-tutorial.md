---
title: Ucupaint Quick Start Guide for Beginners 🖌️ (Blender Tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=KaB8FkBb5rQ
author: Ryan King Art
ingested: 2026-08-09
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/ucupaint-quick-start-guide-for-beginners-blender-tutorial/
frame_count: 0
frame_status: pending-selection
---

# Ucupaint Quick Start Guide for Beginners 🖌️ (Blender Tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=KaB8FkBb5rQ)
**Author:** Ryan King Art
**Duration:** 8m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py ucupaint-quick-start-guide-for-beginners-blender-tutorial <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this Blender Quick Start Guide video, I'll teach you the very basics of how to use the Uchu Paint Blender Extension for texture painting.
[0:07] Now if you do want to watch a longer video where I go into more depth, then you can check out my Uchu Paint for Beginners tutorial,
[0:12] but this is just a quick start guide video if you want to learn the very basics and just the main things which you'll need to use to get started with Uchu Paint.
[0:19] So there's two ways to install Uchu Paint. One way is to go to the Blender Extensions page, which I'll have linked in the video description.
[0:25] You're going to click on Get Add On, and then you're going to click and drag and drop this into Blender.
[0:29] So just drag and drop it from your internet browser, it'll check for updates. Now I have already installed it, so let's just close this.
[0:36] The other way is to click on Edit, go to the User Preferences, you can go to Get Extensions, and you can search for Uchu Paint and you can just install it.
[0:45] Then you can click on the Save Preferences button so it's always saved in your future Blender projects.
[0:49] Now if you hit the N key to open up the side panel, you can click here on Uchu Paint, and here is your Uchu Paint Tools.
[0:55] Now before you actually paint, you will need to UV unwrap your object, and I do have a UV unwrapping for a beginner's tutorial if you want to learn the basics of UV unwrapping.
[1:02] I'm just going to be painting on this cube, and if I go over here to the UV editing workspace, you can see the cube is already unwrapped.
[1:08] So now I'm going to go to the Texture painting workspace, but you could also do this in the layout, whatever you want to do.
[1:12] I'll hit N to open up the side panel, I'll go to Uchu Paint, and I'll click on Quick Uchu Paint Nodes setup.
[1:17] So you don't have to add any material or anything, it'll actually add a material for you.
[1:21] Then you can create a name here, you can also choose the type, I'm just going to leave it as principle, and then here's all the different channels which you'll need to add.
[1:28] So if you want the cube to be metallic, you'd want to leave this on, and then of course Roughness, Normal, and Color, those are the main ones which you should turn on.
[1:34] You could also turn on these other ones if you want to, I'm just going to click on OK to add new Uchu Paint.
[1:39] Now there's two main parts of the add-on. The top part here is the different channels.
[1:43] So the channels are the Color, Metallic, Roughness, and Normal, and then down here there's the Layers, so you can add different layers,
[1:49] and you can paint like Color Maps, Roughness Map, Bump Maps, whatever you want to do.
[1:53] And so now I'll be using my drawing tablet for the texture painting, and I'm just using this small Walk-on-Pad tablet.
[1:58] Now I'm going to make this side panel really small because I don't actually want to paint on a texture, I'm going to paint on the model.
[2:04] So I can now click on the plus here, and there's a bunch of things here, but most of these I never used, you just want to click on New Image,
[2:10] and then you can create a name. So I could call this for example Color.
[2:14] Now this is the name, but down here you need to choose what channel you want this layer to affect.
[2:19] So if you want to paint a metallic map to make something more metallic or less metallic, you'd choose Metallic.
[2:24] If you want to paint Roughness so that more parts are rough and other parts are shiny, you can do that.
[2:28] Or you can paint Unnormal to paint like a bump map. I'm just going to leave it as Color, and then here on the resolution you can make 4K or 1K.
[2:35] I'm just going to go with 2K, and then I'll click on OK.
[2:38] So you can obviously have a layer down here, and you can double-click on it to rename it.
[2:41] You can also click on the I here to hide it or unhide it, and you can also click on this number here and drag it, and that's going to change the Opacity.
[2:48] So I can change my brush color right here, and now I can just start to paint. I'll just use like a soft brush.
[2:54] And then you can see if I drag this, that's going to make the layer more visible or less visible.
[2:58] And then of course I can disable the layer, and then let me just save my project.
[3:02] So I'll just click on File and Save.
[3:04] And in Blender 5.2, it's asking me if I want to save this image, and of course I do want to save that. I don't want to lose it.
[3:09] So I'll just click on Save.
[3:11] So I can just save my Blender file and click on Save Blender File.
[3:14] So now when I paint here, you can see when I paint, there's this little pack icon.
[3:18] So the pack icon is telling us that UchuPaint has saved it into the Blender file.
[3:23] So it's not an external image, it's actually packed into the Blender file.
[3:26] Now you can also see that there's this little asterisk here, or this star.
[3:30] And so when I hit Ctrl-S to save, I can just click on Save, and now you can see that little asterisk goes away.
[3:36] And so that's telling us that UchuPaint has actually saved this into the Blender file.
[3:40] And so what's so useful about the layering system is I can now click on the plus.
[3:43] I can add a new image. I can just choose color.
[3:46] And for example, I can just type in like red, and then click on OK.
[3:49] And I can use these arrows to move it up and down.
[3:51] So if I want the red to be underneath, now what I could do is just choose a color, so I could just choose red.
[3:56] And I can paint here, but clearly you can see the red layers underneath the black layer.
[4:00] And so this is so useful, and it makes texture painting so much easier.
[4:03] As soon as I started using UchuPaint, I realized how amazing it was.
[4:07] And so now every time I do texture painting, I always use UchuPaint,
[4:10] because the layering system just makes it so much easier to do texture painting.
[4:13] And I do have a texture painting playlist where I have some fall along videos
[4:17] where I create like hand painted rocks, some wood, some different weapons, and also some mushrooms.
[4:22] So you can definitely check out my texture painting playlist after this video if you'd like to.
[4:27] Now you can also click on the toggle eraser button.
[4:29] So now I can just erase and that's just going to jump to my eraser brush
[4:32] or I can just click on it right down here.
[4:34] Now another really great feature of UchuPaint is this preview mode.
[4:38] So if I click on preview mode, that's just going to preview that layer.
[4:41] Now you can see it looks really pink and weird and it's not actually previewing your layer.
[4:45] That's because here up on the channels, we need to click on the color channel.
[4:48] So now we're just previewing those colors.
[4:50] So if you select a layer and then click on preview mode, I can just preview the black layer
[4:55] or I can just preview the red layer.
[4:57] So very useful.
[4:59] Now if you just want to preview a certain channel, you can also do that.
[5:02] So I can just preview the roughness and you can see there's also a roughness slider
[5:06] to make it more rough or more shiny.
[5:08] So if it's white, it's going to be more rough.
[5:09] If it's black, it's going to be more shiny.
[5:11] So I can just preview the roughness and if I were to paint a roughness map,
[5:14] then I could just preview the roughness or I can click on the color here and preview the color
[5:18] or the metallic or the normal.
[5:19] Now let's try also painting with roughness and normal.
[5:22] So I'm going to click on the plus here.
[5:24] We're going to click on a new image.
[5:26] We're going to call this one roughness on the channel type.
[5:28] I'm going to have it affect the roughness and then I'll leave it at 2K resolution and click on.
[5:33] Okay.
[5:34] So now if I make my brush black and I paint, you can see it's going to look very shiny.
[5:39] So if I paint, it's shiny.
[5:41] If I make it a white color, then wherever I paint, it's going to be very rough.
[5:45] And if I click on the roughness channel and then preview that, you can see it's white here and black here.
[5:49] We can also paint a bump map by clicking on the plus.
[5:52] We're going to click on new image.
[5:54] This one I'm going to just call bumps so we can remember what it is.
[5:57] And then here on the channel, I'm going to have it affect the normal.
[6:00] Then here in the type here, I'll just leave it as a bump map and then to make bump maps and normal maps look higher quality
[6:06] because they're affecting the normal, I want to turn on 32 bit float and then we'll click on.
[6:10] Okay.
[6:10] So I'm just going to click on the base color here and real quick, I'll click on the color and make this darker just to make the entire base color darker.
[6:17] And so I now have a white brush.
[6:19] So if I paint on the bump layer because this layer is affecting the bump, it actually looks like there's a bump popping out of the mesh.
[6:25] If I paint with a black brush paint black, you can see it looks like it's pushing into the mesh.
[6:31] So very useful for quickly painting a bump map.
[6:33] And then of course, you could also do the same thing with the metallic.
[6:36] So plus new image.
[6:38] Let's call this metal here on the channel type.
[6:40] We want it to affect the metallic and I'll turn off the 32 bit flow.
[6:44] I don't need that 2k resolution and I'll click on.
[6:47] Okay.
[6:47] So now if I make it black, you can see if I paint here, it's not metallic.
[6:50] But if I make the color white and then paint, now you can see it looks like it's metal.
[6:54] So for it to paint all around here.
[6:56] Now this part here, it looks like the cube is made out of metal.
[7:00] So then once you're done painting, if you want to bake this to texture maps, you can click on the little gear icon and you can click on bake all channels.
[7:08] I'm going to bake it as a 2k resolution because that's what I painted and I am going to turn on the use 32 bit float for the normal because that's going to make the normal higher quality.
[7:17] And then I'm also going to use my GPU because I do have a GPU.
[7:20] You can also use any of these other settings if you want to and I'll click on.
[7:23] Okay.
[7:23] And it's going to bake it.
[7:25] So it appears as though blender is crashed, but it actually hasn't crashed.
[7:28] We're just waiting for it to finish baking.
[7:30] And now it's finished baking.
[7:32] So now what I can do is click on this little node icon, click on that.
[7:35] And that's actually going to plug up all of our baked maps.
[7:39] So now if I click here to go to the shading workspace, look over here, I'm just going to go into the rendered mode or the material preview.
[7:45] You can see it baked our color map, our metallic map, our roughness map and our normal map.
[7:50] And it also did to bake a displacement map.
[7:52] So if you want to use the displacement, you can.
[7:54] And if I go back over to texture painting, if I scroll down, you can see there is this save as all.
[7:59] So I'll just click on that button and I can just save all the texture maps to my folder and I'll just click on saved baked images.
[8:05] And it'll just save all of those images to the folder on my computer.
[8:09] So that's the basics of how to use Uchupaint for beginners.
[8:11] So I hope you found this helpful and thank you for watching.
[8:14] And if you'd like to learn more about Uchupaint, then you can check out my longer video with the link in the description.
[8:18] And you can also check out my texture painting playlist to watch more of my texture painting videos.
[8:23] So I have this help and thanks for watching.



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
