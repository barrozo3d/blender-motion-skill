---
title: Tutorial: How to make a volumetric projector in Blender 4.5
source: YouTube
url: https://www.youtube.com/watch?v=F8pqNeVam54
author: Polyfjord
ingested: 2026-06-23
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/tutorial-how-to-make-a-volumetric-projector-in-blender-45/
frame_count: 12
---

# Tutorial: How to make a volumetric projector in Blender 4.5

**Source:** [YouTube](https://www.youtube.com/watch?v=F8pqNeVam54)
**Author:** Polyfjord
**Duration:** 11m40s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction to volumetric projection in Blender [0:00]
**Transcript:** In this tutorial, I'm going to show out to make this volumetric projector effect in Blunder,  where the light from this video file travels through this volumetric shader in this scene.  And the best part about this workflow is that it works with any video file.  So I'm going to show you some really cool techniques you can use to add some unique lighting to your scene.  So here we are in Blunder version 4.5.

**Frame:** tutorials\frames\tutorial-how-to-make-a-volumetric-projector-in-blender-45\frame_000.jpg

### Setting up the render engine and viewport [0:32]
**Transcript:** And I'm going to start out by changing our render engine to cycles.  So let's go to the render properties.  And I set the render engine from EV to cycles.  And then if your GPU compute is great out there, you need to go to edit preferences.  And then let's go to system.  And here you can see you have the cycles render devices.  And then you set it to whatever GPU you have.  Because this will be a lot faster if we use our GPU.  And now in the top right corner, let's change our viewport shading to rendered.  So now we can see our render view and we can delete everything.  And we can make a plane, for example.

**Frame:** tutorials\frames\tutorial-how-to-make-a-volumetric-projector-in-blender-45\frame_001.jpg

### Adding and adjusting a spotlight [1:03]
**Transcript:** And if you go shift a light spot, now you can press G and Z.  And you can move this spot light up.  And you can see that we have a spot light that we've seen.  So now you can right click and you can go adjust light power.  And you can just move this to increase the power.  But no matter how bright you make this, you will never be able to see the cone just by the default settings.  So this entire effect is all about making a huge volumetric shader.  So we can see this light there.  And then we're going to add a video texture to this spot light.

**Frame:** tutorials\frames\tutorial-how-to-make-a-volumetric-projector-in-blender-45\frame_002.jpg

### Creating a volumetric world [1:33]
**Transcript:** So first of all, to make a huge volumetric object, we can actually just set our entire world to be volumetric.  So let's just right click and do a vertical split.  And then let's set this to be the shader editor.  And then we can change this from object to world.  And now here you can see you have the background.  So we need to set this back to render view here.  And now if you take this background, you can just press X to delete it.  And now you can see our entire world is black.  But in shader editor, if you go shift A and you search for volume scatter, you can do this one.  Now we can connect this to the volume of the world output.  But now everything is still black and that's because our fog is too thick.  So in the volume scatter node, we can lower the density.  So let's just click and drag and do maybe 0.1 here.  And now if we turn off the gizmo here and we can also turn off the overlays.  You can see that here we have a very tiny spotlight.

**Frame:** tutorials\frames\tutorial-how-to-make-a-volumetric-projector-in-blender-45\frame_003.jpg

### Enhancing the spotlight's effect [2:21]
**Transcript:** So to make this stronger, you can go right click and just light power.  And you can just bring this up and look at that.  Now we can see our code.  And this is actually really powerful.  If you change your transform pivot point to 3D cursor now, you can rotate this around.  And you can for example, go shift A and you can add a icosphere.  You can bring up this menu here and increase the subdivisions.  And you can move it on the z axis by pressing G and Z.  And look at this.  This is already a pretty cool effect.  We have this really interesting volumetric effect which creates these god rays like this.  But we can make it look even better by adding a video texture to this spotlight here.  So let me just press Ctrl Z a bunch of times.

**Frame:** tutorials\frames\tutorial-how-to-make-a-volumetric-projector-in-blender-45\frame_004.jpg

### Adding a video texture to the spotlight [3:02]
**Transcript:** Yeah, there we go.  So to add a texture to this spotlight, we're going to use the shader nodes.  So let's change this back from world shader to object shader.  And now with this spotlight selected, at the top here you can click use nodes.  So now this spotlight will effectively have a material that we can control using this node here.  So if you take this emission shader for example, you can change the color of it and it will update in real time.  So now that we have this emission node, we can add an image texture to it.  So let's go to edit preferences.  And under add-ons, you can search for node Wrangler.  So you want to enable this one.  So now when you have this emission node, you can press Ctrl T to do this automated texture setup.  So now we have the texture coordinate node, the mapping node and the image texture node.  So let's take this image texture node and let's click open.  And I'm just going to go to my desktop and I'm going to take this glass knot video file and click open image.  And look at that.  Now we have an image texture that is being projected by this spotlight here.  And we can increase the strength for example.  That is such a cool effect already.  You can really see these patterns in the gold race here.  Look at that.  But this doesn't move.  It's not animated.  If we move in our timeline, nothing happens.

**Frame:** tutorials\frames\tutorial-how-to-make-a-volumetric-projector-in-blender-45\frame_005.jpg

### Animating the video texture [4:12]
**Transcript:** So to fix this, you can select this texture here, press N to bring up this side panel.  And let's go to the options.  Nope, let's go to the node.  Yeah, this is the one.  And here you can see you have this refresh icon there next to the frames.  If you click this, it will update to say the number of frames.  And then you can enable auto refresh.  And now if you move in your timeline, you can see that the video file is moving.  Look at that.  Just in the preview, it looks, you can see that something is happening.  Something is like traveling across.  Very, very cool.  Okay, but now we can see that the colors here aren't really popping.  They are technically incorrect because our view transform is set to AGS by default.

**Frame:** tutorials\frames\tutorial-how-to-make-a-volumetric-projector-in-blender-45\frame_006.jpg

### Correcting the color space for better visuals [4:50]
**Transcript:** So a super simple fix is to select this node here.  And you can change the color space from sRGB to AGS base sRGB.  And look at that.  Now we have a much more vibrant looking color here.  Look at these beautiful lines here.  That is so amazing.  And the best part is this is even animated.  Can't really see it now, but in the final render it will look really cool.

**Frame:** tutorials\frames\tutorial-how-to-make-a-volumetric-projector-in-blender-45\frame_007.jpg

### Fixing the aspect ratio of the video texture [5:15]
**Transcript:** Okay, but one problem here, our video file is a circle.  And if you go right click and you adjust the spotlight size,  it just changes the size of the circle.  We want this to be like a 16 by 9 video file.  And also, if you look at the original video file here,  you can see that it's actually not that squished.  It should have this aspect ratio.  Look at that.  This is super squished.  So to fix this, it's actually super simple.  We can use the mapping node that we already have set up with the node Wranglondon.  First of all, I want to lower the scale.  So you can click and you can hold down and drag down here.  And you want to set the scale to two like this.  And now you can see our video texture is repeating four times.  But we only want one texture.  So in the video texture here, let's change the extension from repeat to clip.  So now we only have one texture.  But it's just offset in the corner there.  So to fix this, we can use the mapping node to bring it back.  And you can simply just click and pull down and type minus 0.5.  And it will be in the center.  Look at that.  And now for a very nice trick.  This is really cool actually.  If you want to fix the aspect ratio of this, you have two options.  You can either mess around with this, which is a nightmare.  Trust me, it's really difficult to get this right.  Because then you need to change the location and stuff like that.  But a super simple fix I've found, which is actually really cool,  is that if you select your light and you go to the object properties,  not the object data properties, but the object properties.  And if you go over to the scale here, you can see you have the x-axis scale  and you have the y-axis scale.  Now, our video file has an aspect ratio of 1920 by 1080.  So that means we can do something very simple.  On the x-axis scale, if you click it, you can just simply type 1920,  divided by 1080 and press enter.  And you will get the correct aspect ratio.  Really cool.  So, let me just full screen this.  Now we have a video texture that is being projected onto a surface.  Really, really cool effect.

**Frame:** tutorials\frames\tutorial-how-to-make-a-volumetric-projector-in-blender-45\frame_008.jpg

### Adding the projector screen [7:09]
**Transcript:** So, now we can start having some fun.  Let's make some room here.  I want to rotate this.  So let's set the period point to 3D cursor.  And I want to rotate it on the x-axis.  Yeah, let's do 90 degrees actually.  And then we can move it up on the x-axis.  And then I want to go shift A and let's add a plane.  And I want to rotate it like that.  Oh, by the way, you just got a sneak peak of my upcoming blender album,  which will be free.  So stay tuned for that.  If we move this plane up like this, yeah, I think this is a good...  It's like a movie screen projector.  Look at that. That's such a cool effect already.  You can create this really volumetric vibe with just a few textures that is being projected.  It's not even a few textures. It's just one texture.  Really, really cool.  You can see you get this beautiful, bound slide hair.  And if you want to, you can take this light and you can make it even more powerful.  So maybe 15.  And now you can see you have this really weird pattern hair.  Let's just wait and let this load for a second.  Look at these patterns here.  This is because our D-noiser has some noise threshold cutoff,  which is making some issues.  So, what I like to do is you simply go to the render properties.  And under D-noiser, here you can just disable the noise threshold.  If you do it for the viewport and the noise threshold for the render as well,  you can see now you have this much smoother ground hair.  And what's so cool is that this just looks even better when it's animated.  But we can't really preview that because I mean, I'm live previewing this on an RTX 4090,  which is super fast and it's still really slow.  So, yeah, this takes a while to render.  But, yeah.  There's no but it takes a while to render.  That's just, it sucks a little bit.

**Frame:** tutorials\frames\tutorial-how-to-make-a-volumetric-projector-in-blender-45\frame_009.jpg

### Final result! [8:47]
**Transcript:** So, hair's water animated video texture looks like as a rendered animation,  where the colors from the video creates this beautiful dynamic gold race floating in the air.  But look at this beautiful lighting.  It almost feels like we're wasting this amazing light stores by just pointing it at the wall.  What if instead of projecting this light race onto a flat two-dimensional plane,  we'll use this projector technique to light up a scene with an object in it.  So, to have something that will catch this beautiful light,  we can use a free 3D model of this marble bust,  and with a subsurface scattering shader, we'll get some really soft and interesting details  in the surface of the model.  Then we can add a ground plane and give it a texture as well,  and now we have a scene that we can start lighting.  But this is where things start to get interesting.  Even though we only have one spotlight object,  it turns out our marble bust is being lit from every direction,  because the volumetric shader creates this cage of light that is based on the video file,  which got me thinking what happens if we change the video file.  So, to quickly make new video files, I made this web app where you can tweak basic geometric shapes  to create seamless looping animations and download them as animated textures.  And when we import this to Blunder and give it a vibrant color,  it creates how much the vibe of the scene instantly changes.  And if you want a new texture, just select the different preset,  download the animation and replace the file in Blunder.  Honestly, it's a really cool workflow, actually. You should try this.  The animated pattern generator is free and live on my website.  Just pick a preset, play around with the sliders,  download in whatever format you want.  And then you can add some tint with a colorful gradient texture, for example.  And it's a surprisingly powerful and fun way to light your scene.  And I know what you're thinking. Could we just do this procedurally with nodes inside the spotlight?  Yes, that is absolutely correct. I have a tutorial on that already.  But for me, after playing around with this for a while now, it just feels so valuable  to be able to see the animated texture play in real time and then tweak it in real time as well.  So, I made a free public post on my Patreon,  where you can download this glass-knought video texture,  as well as the final project file from this tutorial if you want to check that out.  And speaking of Patreon, if you subscribe to the advanced project file tier,  you'll also get access to these scenes and all their settings if you want to use them  and just pick them apart and see how they work.  So that's it. I wish you and your GPU the best of luck with these projects.  Thanks for watching.  Thanks for watching.

**Frame:** tutorials\frames\tutorial-how-to-make-a-volumetric-projector-in-blender-45\frame_010.jpg

### Thanks for watching! [11:30]
**Transcript:** you

**Frame:** tutorials\frames\tutorial-how-to-make-a-volumetric-projector-in-blender-45\frame_011.jpg


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
