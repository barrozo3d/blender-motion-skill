---
title: This Blender Shader is the Secret to Magical 3D Art
source: YouTube
url: https://www.youtube.com/watch?v=mQPFjzAgGQo
author: Levi Magony
ingested: 2026-07-19
blender_version: "Not specified (EEVEE Next-era 4.x/5.x; real-time compositing required)"
tags: [shaders, materials, procedural, eevee, compositing, motion-design, abstract, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/this-blender-shader-is-the-secret-to-magical-3d-art/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# This Blender Shader is the Secret to Magical 3D Art

**Source:** [YouTube](https://www.youtube.com/watch?v=mQPFjzAgGQo)
**Author:** Levi Magony
**Duration:** 24m9s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Overview [0:00]
**Transcript (timestamped):**
[0:00] This shader feels like cheating, because it makes anything look magical, and it's procedural.
[0:06] So, if you wanna understand how shader nodes work or create complex line art, then watch this video,
[0:11] because it's filled with valuable information, or don't, and you won't improve, it's your choice.
[0:17] The shader is created in 9 steps. Here's a quick overview.
[0:20] We're gonna add the gradient, then shadows and highlights, color variations, an outline using grease pencil,
[0:27] then cracks, ambient color, reflections, transparency, and finally compositing to make the whole thing shine.
[0:34] There's a lot to cover, so let's jump right in.


### Setup [0:37]
**Transcript (timestamped):**
[0:37] A quick setup before we start. The render engine is EEVEE, and in color management, the view transform is set to standard.
[0:46] This shader looks best on objects with sharp edges, so keep that in mind.
[0:50] Alright, go to the shading tab and let's make the gradient.


### Gradient [0:52]
**Transcript (timestamped):**
[0:54] Add a new material, delete this, hit Shift A, and start typing coordinates, and select texture coordinates.
[1:01] Use generated, and search for separate XYZ node.
[1:05] This node makes gradients on the axis. You can view it by Ctrl Shift clicking on the node.
[1:10] You can see it's on the X now, but you need to apply rotation, so it appears on the right axis.
[1:16] Ctrl Shift click again, this is the Y, but we need the Z axis for a top-bottom gradient.
[1:23] Let's add the color ramp to change the colors.
[1:25] I'll set the bottom color to dark blue, and the top to turquoise.
[1:30] We can make this look better by changing this to B spline, and dragging the sliders closer to each other, so the colors are more obvious.
[1:38] The cool thing about generated coordinates is that when you move a vertex, the texture adjusts to fit the new shape.
[1:46] It's perfect for gradients, and it's a bummer I hadn't heard about this until a few weeks ago.
[1:50] Anyway, let's put these in a frame with Ctrl J, and name it with F2 gradient.


### Shadows & Highlights [1:56]
**Transcript (timestamped):**
[1:56] The next step is to make shadows and highlights with a cool reflective effect.
[2:01] So, add the layer rate node and change it to Facing. This gives us this cool effect.
[2:07] But I want some shadows here, so to customize it, drag out the normal input and search for mapping node,
[2:13] and plug a texture coordinate node's normal output here.
[2:17] You can change the rotation till you have a nice shading with shadows and highlights.
[2:22] Normal coordinates are powerful, because you don't have to use actual lights to light the scene.
[2:27] Now it looks better, and we still have this reflective effect.
[2:31] You can fine tune it with the blend slider.
[2:34] Let's add colors using a color ramp.
[2:37] You can pick the exact colors from this video, and move these sliders to add some contrast.
[2:43] If your object looks too bright, lower the intensity till it looks right.
[2:48] Set the word to black so it looks cooler. Wow.
[2:51] Alright, to make this crystal more interesting, we need color variations.


### Color Variations [2:52]
**Transcript (timestamped):**
[2:56] So, add the texture coordinate node, drag out the object output, and type Voronoi texture.
[3:03] The color output gives us this shattered look.
[3:06] We're using the object output this time, because it doesn't distort the texture compared to generated coordinates.
[3:12] It was fine with gradients, but please don't distort my Voronoi texture. Thanks!
[3:17] We'll change this texture in a bit. Let's add colors first.
[3:21] Drag out the color output, and add the color ramp.
[3:24] I use a different shade of blue and turquoise to have some variations.
[3:28] Let's adjust the scale to have bigger shapes. This depends on your object size.
[3:33] The edges look too sharp. I want to have a frosted glass effect, so I change this to smooth F1.
[3:39] And now it's too blurred. You can change the smoothness here, but I want to make it less uniform.
[3:44] So I'm gonna show you a really cool technique that does exactly that. Check this out.
[3:48] Drag this out, and add the noise texture.
[3:51] Something's changed already, but it looks weird, so duplicate the coordinates node, and plug the object output here.
[3:58] If you don't do that, the noise will use generated coordinates by default, which is not ideal.
[4:03] Now we have this interesting water color effect.
[4:07] What I'm gonna do is set the detail to 0, and add the color ramp here.
[4:12] Adjusting the black color, clamps the effect, so the noise doesn't appear everywhere.
[4:17] I lower the scale so we have a cleaner look.
[4:20] As you can see, the contrast is too big. This part is too sharp, and this is too blurred.
[4:25] To fix this, you gotta lower the contrast in the color ramp.
[4:29] But how? When you change the black color to dark gray, it makes the sharp edges blurred.
[4:34] I just need a slight blur. Change the white color to light gray, and the blurred parts are not that crazy anymore.
[4:40] Now we have this broken texture with a frosted glass finish.
[4:44] I don't know why, but I just wanna lick that texture so bad.
[4:48] It's time to mix this with this node setup.
[4:51] To do that, either you can be really slow, and drag out this, and search for mix, and plug this in,
[4:58] or be fast, and enable Node Wrangler in the preferences, and hold down Ctrl plus Shift right click drag from this node to this node,
[5:05] and mix them automatically.
[5:07] You can see they are mixed, but they are just slapped onto each other.
[5:11] To make them blend nicely, change the blending mode to soft light.
[5:15] Make sure the Voronoi setup is at the bottom socket. If not, the result is different.
[5:21] You can experiment with different modes.
[5:23] Holding down Ctrl while scrolling on the drop-down helps you switch modes quickly.
[5:28] Alright, let's set the factor to 1, and this is how it looks.
[5:32] Hey, wanna take your Blender's Kiss to the next level?
[5:36] Watch exclusive tutorials, and get my project files by joining my Patreon.
[5:41] Thank you, and I'm really grateful to you guys who are already supporting me.
[5:45] Let's bring the gradient to the equation.
[5:48] Mix it with the Mix node, and set it to Overlay this time, cause it looks punchier than Softlight.
[5:54] Stick with Softlight if you are going for a more subtle look. Set the factor to 1.
[5:59] If both Mix nodes were set to Overlay, it would look too much.
[6:02] Now we've got something, and it's only going to get better.
[6:06] Let's put this in a frame, and rename it to Color Variations.
[6:10] Here's the setup if you need the whole picture.


### Lineart [6:13]
**Transcript (timestamped):**
[6:13] Let's continue with the lineart to get the feel early on, then continue with the shader.
[6:18] This shader is nothing without a lineart.
[6:21] I'm not talking about slapping a boring-ass lineart through it and call it a day.
[6:25] I'm talking about a lineart that has a soul, and is specifically crafted for this shader to bring out its full potential.
[6:33] They live in a symbiosis, and one does not exist without the other, and the...
[6:37] So let's make that outline.
[6:39] Select your object, Shift-A, grease pencil, object lineart, and you have an outline.
[6:45] You need a camera, because the outline is calculated from the camera view.
[6:50] Select the outline, and go to Modifiers.
[6:53] I increase the thickness a bit.
[6:55] I need lineart on these edges as well, so in Edge Types, increase the crease.
[7:00] The larger the angle, the more line is displayed.
[7:04] Let's add colors.
[7:05] You can do it here and choose a simple color, but I want a gradient.
[7:10] So I add a thin modifier and choose gradient.
[7:13] Let's add turquoise for the highlights and the saturated blue for the shadows, but nothing seems to happen.
[7:20] This red icon indicates we are missing something.
[7:23] That something is an object, because right now the modifier has no clue where to start the gradient from.
[7:30] Let's provide something to it.
[7:32] This is when an empty becomes really handy.
[7:35] Put it here, select the lineart, and pick the empty.
[7:39] So now go to Render View, and we have a really ugly gradient, and it reacts to the empty.
[7:45] Whoa, whoa, whoa!
[7:47] Place it so the colors align with the shading, with turquoise at the top and dark blue at the bottom.
[7:53] Make sure the empty is close to your object.
[7:56] If it's not, the gradient isn't visible.
[7:59] To adjust the gradient, select the lineart, and with the radius you can change how far the effect goes, or scale the empty.
[8:06] Alright, let's make this ugly lineart look pretty.
[8:09] First, change the factor to 1 to use these colors at full intensity.
[8:14] If the factor is less than 1, the original lineart color will become visible, and we don't want that.
[8:20] It's still not too convincing, so in lineart data set the blend mode to divide, and now they elevate it to the full.
[8:28] Now they elevate each other.
[8:30] This is some mutualistic symbiosis type shit.
[8:33] Let's increase the radius to make the bottom part more visible.
[8:37] I changed the world to a dark blue, now everything looks better.
[8:41] It's time to make this lineart look hand drawn.
[8:44] So add the dot dash modifier, but it looks weird.
[8:47] It's supposed to make cracks in the lineart.
[8:50] But that ain't no crack, that's a canyon.
[8:52] To tell you why that happens and how to fix it, you gotta understand how lineart is generated.
[8:58] Lineart has a resolution just like objects do.
[9:01] This resolution depends on how many vertices your object has.
[9:05] Basic outlines look the same no matter what the resolution is, but if you want to create a lineart with gaps, the resolution makes a huge difference.
[9:14] The lower the resolution, the bigger the gaps.
[9:18] This is because the dot dash modifier removes points to make gaps, and without enough points, the gaps will end up too large.
[9:27] To change the lineart resolution, without changing the object subdivision, use the simplified modifier.
[9:34] So this is what happened.
[9:36] The object doesn't have enough vertices, so it can only generate a lineart with a few points, and fewer points result in larger gaps.
[9:45] So add the simplified modifier.
[9:47] Add it before the dot dash and choose sample mode.
[9:50] This regenerates the lineart geometry with evenly distributed points.
[9:55] The length slider changes the distance between each point.
[9:58] I set it to 0.C.
[10:00] What? I set it to 0.03.
[10:02] Now we can play with the dot dash and have small cuts in the lineart.
[10:07] The dash value is the number of points that makes up a segment.
[10:11] And the gap value is the number of points removed between segments.
[10:15] Play around with them, and you can also offset the dashes.
[10:19] The line is too straight. Let's give some character to it with a noise modifier.
[10:23] The noise scale adjusts the level of detail, but this also depends on the line's resolution.
[10:30] I lower the scale and the position so it's a bit more subtle.
[10:34] It might be too subtle, but the fact that it's there makes me feel better, you know?
[10:38] Now comes the last thing, the secret sauce for a hand drawn outline.
[10:43] The Invalop modifier... Hell yeah!
[10:46] It makes the corners round.
[10:48] I set it to D4 mode now, but segments mode might look cleaner in other cases.
[10:53] Change the roundness with the spread length, but this also depends on the line's resolution.
[10:58] I set it to 2 to keep it subtle.
[11:01] I forgot to mention that if you find the color too intense, you can decrease the alpha,
[11:06] but it doesn't update automatically. I don't know why.
[11:09] So hit play and pause or go to edit mode and back to refresh it, and you can see it's less intense.
[11:15] Okay, after this I tweak the outline a bit.
[11:19] I make it thinner, make the gap smaller, and play with the offset.
[11:23] And look at that outline, it looks beautiful. I love it!
[11:27] The fact that you are still watching shows that you are serious about improving your 3D skills.
[11:33] If you wanna get even better, join my free newsletter,
[11:36] and I'll send you 8 wallpapers instantly as a welcome gift.
[11:40] My newsletter is about Blender tips, the latest 3D news, inspiration, special discounts, and updates on my projects.
[11:48] Let's continue with the shader. I'll show you two ways to make cracks.


### Cracks [11:49]
**Transcript (timestamped):**
[11:53] You can create them in a simple way or in a slightly more advanced way, but the result looks much better.
[11:58] To make the simple one, select the object and go back to the shading tab.
[12:03] Let's tidy up the space.
[12:05] To add the texture coordinate node, we're gonna use the camera output and add the Voronoi texture.
[12:10] The camera output uses the camera space, so when you rotate the scene, the texture rotates with it.
[12:17] When you move the scene, the texture moves with it.
[12:20] Basically, you are the center of attention.
[12:22] Change the texture type to distance to edge.
[12:25] To fine-tune the look, add the color ramp, change it to constant, drag the slider, and we get cracks.
[12:31] You can change the scale here.
[12:33] What I don't like about this is how sharp the corners are. It doesn't look hand-drawn, so I'll show you the better looking option.
[12:41] Let's switch back to F1 and delete the color ramp.
[12:45] Duplicate this with Shift-Ctrl-D to keep the node connection.
[12:49] Switch this to smooth F1 to get round corners, but we also need the sharp edges from the other texture.
[12:56] So drag out distance and add the math node.
[13:00] Plug the other texture here and choose Subtract.
[13:03] Now we have sharp lines, but also smooth corners.
[13:07] To make it less blurry, add the color ramp and choose Constant.
[13:11] When you drag the white color stop, you see this alien texture.
[13:15] It doesn't look like cracks because the corners are too round.
[13:19] So decrease the smoothness and adjust this again.
[13:23] Now it's better.
[13:24] Let's keep lowering the smoothness, but it's getting harder to adjust the color ramp.
[13:29] So I'm gonna duplicate this and change it to Divide.
[13:32] And now, when I adjust the value by holding down Shift, I can set it more precisely.
[13:38] I set the smoothness to 0.11 and tweak the Divide till the cracks become visible.
[13:44] You can still adjust the color ramp, but use the position slider because it's more precise.
[13:49] You can see the corners are still round.
[13:52] But the cracks are too small, so let's change the scale.
[13:55] Whoa, what is going on?
[13:57] Remember, we are using two textures, so we should scale both at the same time.
[14:02] But how?
[14:03] Drag out the scale, type value, and with this we can output numbers.
[14:08] Plug this scale into it, and now both scale values can be changed at the same time.
[14:14] Let's make it smaller so we have less cracks, but now they are too thick, so decrease this value.
[14:21] What if you don't like the position of them?
[14:23] There's a note for that.
[14:24] First, reroute these connections which shift right-click and add the Mapping note here.
[14:30] With this, you can adjust the location of the texture on every axis.
[14:34] If you don't like how this texture moves, switch to Object coordinates to make it static.
[14:39] But it will look good, trust me.
[14:41] Okay, let's add colors.
[14:43] Change the white color to turquoise and leave the black as it is.
[14:47] By the way, if you are having a hard time selecting color stops because they are too close to each other,
[14:52] just select them with this.
[14:54] The cracks are done, it's time to add them to the shader.
[14:58] Mix it with this mix node using Ctrl Shift right-click drag and switch the blending mode to Color Dodge.
[15:05] This blending mode removes the black color and blends the light color nicely with the shader.
[15:10] Setting it to 1 makes it too intense, so I decrease it to around 0.75.
[15:16] Now we have nice cracks.
[15:18] Frame this and rename it to cracks.
[15:20] Look at them, do you think they are cracking jokes?


### Ambient Color [15:25]
**Transcript (timestamped):**
[15:25] The next step is to add ambient color in the darker areas to make the shader more interesting.
[15:31] So, add the mix node and choose a color.
[15:35] Lilac works well with the scene.
[15:38] I don't want this color everywhere, so I need a mask that keeps the top part as it is and thins the dark areas.
[15:45] In my case, the bottom part.
[15:47] So let's make that.
[15:48] Add the Texture Coordinate node and use the Reflection output to make the ambient color look like a reflection.
[15:55] To limit the reflection to the bottom half, add the Separate XYZ node and view the Z output.
[16:01] We need the white part at the bottom.
[16:03] To do that, add the Mapping node, place it here and rotate it on the Y-axis till it's at the bottom part.
[16:11] Let's check how it looks when the object is rotated.
[16:14] There's too much white showing that we'll become the ambient color which we don't want.
[16:19] So, I'll move it down along the Z-axis until only a small part remains white.
[16:25] Perfect!
[16:26] Let's add the Math node and set it to Multiply to change the intensity.
[16:31] Plug this into the factor and voila, we made ambient color.
[16:35] Not so fast, because when you've rotated, you can see it's too intense,
[16:40] so set the Blending mode to Color and change the intensity with the Multiply.
[16:44] And now when you've rotated, it looks nice.
[16:47] Let's put it in a frame and rename it to Ambient Color.
[16:51] This color adds a nice touch to the shader.
[16:54] I know the shader looks a bit intense, but the transparency will fix it.
[16:58] Before making that, let's add reflections.


### Reflections [16:59]
**Transcript (timestamped):**
[17:01] This small yet crucial detail tricks your mind into thinking it's a shiny object.
[17:06] So let's make two diagonal lines.
[17:09] Add the Texture Coordinate node, use the Reflection output and add the Separate XYZ node.
[17:16] Use the Z output and we can turn this gradient into lines with a color ramp.
[17:21] Switch to Constant mode and drag the Y stop somewhere, it doesn't matter for now.
[17:26] Add the new black color stop with the plus button and drag it to this side.
[17:30] And this is the line, but you don't see the line on the object, so add the Mapping node and scale up the thing.
[17:36] Now we can see the line.
[17:38] Let's adjust this quickly and make the second line by adding a color stop using a shortcut.
[17:43] Click here while holding Ctrl.
[17:45] Ta-da! Make this white.
[17:47] Add another stop and make it black.
[17:50] Adjust them till the second line is thinner. It looks better that way.
[17:54] Visually more balanced to sound smarter.
[17:57] To make it diagonal, change the rotation on the Y axis.
[18:01] I set it to minus 20.
[18:03] Let's make the lines bigger with the scale so it looks more realistic.
[18:06] And now when you rotate the object, the reflection is reflection-ing.
[18:10] The settings depend on your object's shape and size, so you gotta figure out what looks best for you.
[18:16] Let's use a color ramp to make the white part turquoise.
[18:19] Alright, it's time to add it to the setup with the Mixed node.
[18:23] Set the blending mode to Add and the factor to 0.8. It looks nice.
[18:28] Frame it and rename it to Reflections.


### Transparency [18:32]
**Transcript (timestamped):**
[18:32] The last ingredient for this shader before I show you some compositing tricks is liking this video.
[18:38] Haha, I'm making it transparent.
[18:41] The first thing is to convert this setup to a shader.
[18:44] So add an Emission shader.
[18:46] It looks the same, but you can change the strength now, but don't.
[18:50] The reason I did this, cause now I can mix it with a transparent shader, not with translucent, transparent.
[18:57] So mix it with Ctrl Shift right-click drag.
[19:00] Now we gotta mix shader.
[19:02] Make sure the transparent is at the top socket and the Emission at the bottom.
[19:07] Adjusting the factor lets you make the shader either more transparent or more emissive, but it looks noisy.
[19:13] To fix it, go to Material Settings and switch the render method to Blend-It.
[19:18] Now it's clean.
[19:20] Make sure transparency overlap is enabled.
[19:23] If not, you won't see the inside faces.
[19:26] The transparency is too uniform, so I'll need a factor to spice it up.
[19:30] The factor is gonna be the reflective effect in the color variations.
[19:35] The light parts will be less transparent, while the darker parts will be more transparent.
[19:40] So instead of grabbing this and taking a journey across Middle Earth through each Mordor,
[19:45] just simply put this in a group with Ctrl G.
[19:48] You can go back from Group View, either pressing this button or hitting Tab.
[19:53] Now we have this group. Rename it to Shadows and Highlights.
[19:57] Go back to the transparency, hit Shift A, type Shadows and Highlights,
[20:02] and you can find the node group we just created, so now you can plug this into the factor easily.
[20:07] However, it looks too dark, because darker values fit into the factor makes the object more transparent.
[20:14] And this is quite dark.
[20:16] So to make it brighter, add the color ramp and increase the value of the black color to 0.6.
[20:22] This is better. Drag this stop closer to add contrast, but white makes it opaque.
[20:27] So lower the value to around 0.77 to add a little bit of transparency.
[20:33] Alright, let me tell you one thing about groups. Click here to go into it.
[20:38] They are useful, because when you change something inside them, it will change everywhere you use that group.
[20:43] Like here, so they are linked.
[20:46] Okay, we have a transparency that makes the crystal look fragile.
[20:51] This shader needs one more thing, adding a texture to the transparency, which will add more detail to it.
[20:58] This is gonna be quick. Add the texture coordinate node, use the camera output, add the Voronoi texture,
[21:05] add the color ramp, make the colors really saturated, increase the contrast and set this to ease.
[21:12] Switch the texture to Smooth F1 and to make random smoothness,
[21:17] and then, we will build a setup we made at the beginning and put it in a group with Ctrl G.
[21:22] Tab out, rename it to Random Smoothness, go back to here, search for Random Smoothness and plug it in here.
[21:31] Adjust the scale to get bigger cracks and plug this into the transparency color.
[21:36] This is how it looks like. It might take some time for Blender to calculate it.
[21:41] This is without it. This is with it.
[21:44] When you rotate it, you can see the texture moving.
[21:47] Put this in a frame and rename it to Transparency Color.
[21:51] The shader is done, but to make it truly shine, we gotta make it literally shine in compositing


### Compositing [21:52]
**Transcript (timestamped):**
[21:57] and add the cool effect that you might not heard about.
[22:00] So go to Compositing, make a new window here, change it to 3D viewport and enable Real Time Compositing.
[22:09] Make sure Use Nodes is enabled. Add the glare node.
[22:13] Ooooo, switch it to Bloom. Ooooo, with the mix, adjust the intensity to your liking.
[22:20] Increase the threshold a bit so the glare only applies to the bright parts.
[22:24] Change the quality to High and decrease the size, but this is just a guide so you can do whatever you want.
[22:30] The other effect is made with the Sunbeams node. This adds light rays.
[22:35] Make them shorter. Let's position the Source point till it's in the middle of the object.
[22:41] This effect is too much. I only want to apply it to the brightest parts.
[22:45] So duplicate the Bloom and put it before the Sunbeams.
[22:48] Let's view this node so we can see what we are doing.
[22:51] Set the mix to 1 so only the brightest parts are visible.
[22:55] Increase the threshold to remove the reflections.
[22:59] The size changes the intensity. I set it to 1.
[23:02] So now the Sunbeams node will use this image as a source, making the light rays less intense.
[23:08] By the way, I love real-time compositing. Look at this.
[23:11] Ok, it's time to apply it to our image.
[23:14] To do that, let's mix them and set the blending mode to Lighten.
[23:18] Or choose from these four, cause these are the ones that remove the black background.
[23:23] I lower the intensity cause this is just a small detail. And this is how it looks.
[23:28] Something to keep in mind when you render the image, the effects get a bit more intense, because of the higher resolution I think.
[23:35] Oh, we have a warning here. To render grease pencil, enable combined and Z passes.
[23:41] Let's do that. Go to View Layer and enable the Z pass.
[23:45] You can make the scene look more magical by adding tiny spheres.
[23:49] I'm using the Stardust tool from my asset library called Celeste Tools,
[23:53] which speeds up the process of adding details. Get it on Gumroad.
[23:57] Congrats, you completed the shader!
[24:00] Drop a diamond emoji in the comments so I know who put in the work to level up their knowledge.
[24:05] Watch this video next to take your skills even further.



---

## Captured Frames

- [1:30] tutorials/frames/this-blender-shader-is-the-secret-to-magical-3d-art/frame_000.jpg
- [2:40] tutorials/frames/this-blender-shader-is-the-secret-to-magical-3d-art/frame_001.jpg
- [4:40] tutorials/frames/this-blender-shader-is-the-secret-to-magical-3d-art/frame_002.jpg
- [8:28] tutorials/frames/this-blender-shader-is-the-secret-to-magical-3d-art/frame_003.jpg
- [13:44] tutorials/frames/this-blender-shader-is-the-secret-to-magical-3d-art/frame_004.jpg
- [17:54] tutorials/frames/this-blender-shader-is-the-secret-to-magical-3d-art/frame_005.jpg
- [19:07] tutorials/frames/this-blender-shader-is-the-secret-to-magical-3d-art/frame_006.jpg
- [22:41] tutorials/frames/this-blender-shader-is-the-secret-to-magical-3d-art/frame_007.jpg

---

## Structured Notes

### Core Technique
A 9-step procedural stylized "magical crystal" shader in EEVEE (lightless, emission-based) paired with a hand-drawn-style Grease Pencil line art rig and real-time compositing bloom/sunbeams.

### Summary
Levi Magony builds a fully procedural crystal shader with no scene lights: a generated-coordinate Z gradient, Layer Weight (Facing) fake lighting with a remapped normal, Voronoi color variations softened by object-space noise, camera-space Voronoi cracks (dual-texture subtract trick for sharp lines with round corners), reflection-space ambient color and diagonal highlight lines, and transparency mixed by shading (dark = more transparent). The line art half uses a Grease Pencil Object Line Art with tint-gradient-from-empty, Simplify (Sample) to control resolution, Dot Dash for gaps, Noise, and Envelope for rounded corners. Finishing happens in the real-time compositor with Bloom and a bloom-masked Sun Beams node. Setup: EEVEE, view transform Standard, world black→dark blue; works best on sharp-edged objects.

### Key Steps
1. **Gradient** [frame_000, 1:30] — Texture Coordinate (Generated) → Separate XYZ (Z; apply rotation first) → Color Ramp (B-Spline) dark blue #4586E2 → light turquoise #B5FFFE. Generated coords re-fit the gradient when the mesh deforms.
2. **Shadows & highlights (lightless)** [frame_001, 2:40] — Layer Weight set to **Facing**; feed its Normal input from Texture Coordinate Normal → Mapping, rotating until shadows sit right; Color Ramp with #347CD8 / #CBFFFB; blend slider fine-tunes; no lights needed.
3. **Color variations** [frame_002, 4:40] — Texture Coordinate (**Object**, to avoid generated-space distortion) → Voronoi (Smooth F1) → Color Ramp (alternate blues); plug an Object-space **Noise Texture (Detail 0)** into the Voronoi vector and clamp with a Color Ramp (black→dark gray blurs sharp parts, white→light gray reins in blur) for a frosted watercolor look. Mix: Voronoi setup Soft Light (bottom socket), then gradient via second Mix set to Overlay, both factor 1 (Node Wrangler Ctrl+Shift+RMB drag to mix).
4. **Line art** [frame_003, 8:28] — Shift+A → Grease Pencil → Object Line Art (needs a camera). Modifiers: thickness up, Edge Types → Crease angle; **Tint modifier (Gradient)** with an Empty as the gradient object (place near object, radius/scale to fit), factor 1; layer blend mode **Divide**. Hand-drawn feel: **Simplify (Sample mode, length 0.03)** first — line art resolution controls gap size — then **Dot Dash** (dash = points per segment, gap = removed points), subtle **Noise**, and **Envelope** (spread length 2) to round corners. Alpha changes need a refresh (play/pause or edit-mode toggle).
5. **Cracks** [frame_004, 13:44] — Texture Coordinate (**Camera**) → two linked Voronoi Distance-to-Edge textures (one F1, one Smooth F1 smoothness 0.11) → Math **Subtract** → Math **Divide** (Shift-drag for precision) → Color Ramp (Constant): sharp lines with rounded corners. One Value node drives both scales. Optional Mapping node (rerouted) repositions; Object coords make cracks static. Color white→turquoise; mix into shader with **Color Dodge** at ~0.75.
6. **Ambient color** — Mix (blend mode **Color**) with lilac; mask = Texture Coordinate **Reflection** → Separate XYZ (Z) → Mapping (rotate on Y to put white at bottom, slide down Z until only a sliver remains) → Math Multiply for intensity → factor.
7. **Reflections** [frame_005, 17:54] — Reflection coords → Separate XYZ (Z) → Color Ramp **Constant** with 4 stops making two diagonal white lines (second thinner; Ctrl+click on ramp adds stops), Mapping scale up + rotate Y −20°; tint turquoise; Mix set to **Add**, factor 0.8.
8. **Transparency** [frame_006, 19:07] — feed everything into an **Emission** shader, mix with **Transparent BSDF** (transparent top socket) via Mix Shader; Material Settings → render method **Blended**, transparency overlap on. Factor = the "Shadows and Highlights" setup grouped (Ctrl+G) and reused: dark = transparent, bright = opaque, remapped by Color Ramp (black value 0.6, white 0.77). Extra: camera-space Voronoi "Random Smoothness" group into the Transparent BSDF color for internal facets.
9. **Compositing** [frame_007, 22:41] — enable real-time compositing in a 3D viewport; **Glare → Bloom** (High quality, raise threshold, smaller size); **Sun Beams** node (source point centered, short rays, Ray Length ≈ 0.33) fed by a duplicated Bloom (mix 1, high threshold, size 1) as its mask; combine with Mix **Lighten**, low factor. Enable View Layer **Z pass** (+Combined) so Grease Pencil renders.

### Nodes / Settings
- EEVEE; Color Management → View Transform: **Standard**; world dark blue/black
- Gradient: Generated → Separate XYZ Z → ColorRamp B-Spline (#4586E2 → #B5FFFE)
- Fake light: Layer Weight (Facing) with Mapping-rotated Normal input; ColorRamp #347CD8/#CBFFFB
- Variations: Object coords → Voronoi Smooth F1 + Noise (Detail 0) into vector; ramps as clamps; Mix Soft Light + Overlay, factors 1
- Cracks: Camera coords → Voronoi Distance-to-Edge ×2 (F1 & Smooth F1 0.11) → Subtract → Divide → ColorRamp Constant; shared Value scale; Color Dodge 0.75
- Line art: GP Object Line Art; Tint (Gradient, empty object, factor 1); layer blend Divide; Simplify Sample 0.03 → Dot Dash → Noise → Envelope (spread 2)
- Transparency: Emission + Transparent BSDF via Mix Shader; render method Blended, transparency overlap ✓; factor from Shadows-and-Highlights group through ColorRamp (0.6/0.77)
- Compositor: Glare Bloom (High, mix/threshold/size tuned) + Sun Beams (masked by second Bloom), Mix Lighten; View Layer Z pass on
- Node Wrangler: Ctrl+Shift+click preview, Ctrl+Shift+RMB drag auto-mix

### Difficulty
Intermediate

### Blender Version
Not specified (EEVEE with real-time compositing — 4.x/5.x era)

### Tags
shaders, materials, procedural, eevee, compositing, motion-design, abstract, intermediate

---

## Related Tutorials
- [How to make this style in Blender](how-to-make-this-style-in-blender.md) — sibling stylized-look breakdown
- [How Apple Makes 3D Wallpapers (Blender Tutorial)](how-apple-makes-3d-wallpapers-blender-tutorial.md) — glossy abstract aesthetic with related fake-lighting tricks
- [Glass Cell Division Effect in Blender 5.0 (tutorial)](glass-cell-division-effect-in-blender-50-tutorial.md) — Voronoi-driven crystal/glass looks
- [30 little-known Blender tricks](30-little-known-blender-tricks.md) — the noise→vector warping and color-variation micro-techniques used here
