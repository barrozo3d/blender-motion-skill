---
title: Easy PBR Textures - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=qxxoDYGrvtw
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/easy-pbr-textures---blender-secrets/
frame_count: 0
frame_status: pending-selection
---

# Easy PBR Textures - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=qxxoDYGrvtw)
**Author:** Blender Secrets
**Duration:** 10m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py easy-pbr-textures---blender-secrets <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] To use physically based textures or PBR textures, first of all, make sure that you have Node Wrangler enabled.
[0:06] To do so, go to Add-ons, type node, and then check the Node Wrangler box.
[0:11] Next, you'll need some PBR textures.
[0:13] Polyhaven.com is a great source for free textures.
[0:16] Go to Assets, and then click on Textures, and then search for some texture that you like.
[0:21] I like this Castle Brick 02 Red texture, so I'll click on that.
[0:25] You can choose a texture resolution, I think 4K is enough in this case.
[0:30] Then here, if you click on ZIP, you can choose all of the files that you want.
[0:35] For example, you can choose to download a blend file, which already has the assembled material in it,
[0:39] and you can uncheck the things that you don't need.
[0:41] For example, I don't want a glTF file, and then you can choose which files you want,
[0:45] as well as which file type.
[0:46] So for example, for Diffuse, which is just color, the JPEG is more than enough.
[0:51] But for the displacement, I would prefer to have an EXR file, because it's smaller than a PNG file,
[0:56] and it contains all the information that we need.
[0:58] For the normal maps, you have the choice between DirectX or OpenGL.
[1:02] I'll just uncheck the option of DirectX, because Blender uses OpenGL.
[1:07] And then I will click on Download.
[1:08] Once I've downloaded and unzipped the downloaded file, we have the blend file,
[1:13] which actually already contains the assembled material,
[1:16] as well as a folder with all of the different textures.
[1:19] And you can see that the type of texture is identified in the file name,
[1:22] for example, NOR for normal map.
[1:24] Now in Blender, let's open a window for the shader editor, and choose Shader Editor here.
[1:29] And then let's add an object to test the texture.
[1:32] So I'll choose a UV sphere.
[1:34] Let's scroll the mouse wheel to get a bit closer, and I will set it to Shade Smooth.
[1:38] And I'll add some subdivisions by increasing these two levels.
[1:42] Now I can add a new material here, or by clicking on New here.
[1:45] And since we already have the shader editor open, I'll just click on New here.
[1:49] Next, to add our downloaded PBR textures to this material,
[1:53] I simply click and select this principal PSDF node.
[1:56] And then I'll press Shift, Control and T, and then it will open this dialog.
[2:01] Then I can select all of these textures and click on principal texture setup.
[2:06] And as you can see, it has created all of the nodes that we need.
[2:09] So it has the mapping nodes here, and all of the textures.
[2:13] The only thing it has not connected is the ambient occlusion node,
[2:16] and in a moment we will look at how to connect that.
[2:18] First of all, let's have a look at how we can see our texture.
[2:21] Now we are in solid mode, but if we click here, then we are in textured preview.
[2:25] And I'm also going to select cycles for the render engine,
[2:29] and I'm going to choose my GPU and turn on the noise to make it all a bit faster.
[2:34] If you don't have GPU, go to System in preferences,
[2:37] and make sure that the GPU is enabled here.
[2:40] Now it's a bit dark, so I will go to the World tab,
[2:43] and I can either increase the strength of the world.
[2:46] And I have this HDRI checkbox, and if I check this, it will add an HDRI.
[2:50] And I have this option because I have the add-on gather installed.
[2:53] And that's also free, and it's also from the makers of Polyheaven.
[2:57] So as you can see, we have the texture, however, we don't have any displacement.
[3:01] It's still a perfectly smooth sphere.
[3:03] And now to get the displacement, make sure that you have your object selected,
[3:06] so you can go into the material tab.
[3:08] And then you might think it's somewhere here in displacement,
[3:11] but it's not, that would make way too much sense.
[3:13] So go to settings, and then set displacement here to displacement only.
[3:18] And you can see that we need to change the scale.
[3:21] So here in the displacement node, zoom in on it by scrolling the mouse wheel up,
[3:25] you can set the scale to something like 0.1.
[3:28] And as you can see, now we do have some real displacement.
[3:31] If you're wondering if you should use displacement only or displacement and bump,
[3:35] displacement and bump gets a little bit more detail out of the texture
[3:39] at a lower subdivision level.
[3:41] However, it takes a little bit longer to render.
[3:44] So that's up to you.
[3:45] And I will just choose an interesting HDRI to get a good look at the texture.
[3:50] And if you don't want to have the background of the HDRI,
[3:52] you can go to the render tab and then render film,
[3:55] you can check the transparent box.
[3:57] Now, if you want to mix in this ambient occlusion node, which looks like this,
[4:01] you can preview nodes by shift and control left clicking on it.
[4:05] So we can shift, control, left click on each of these textures to see what they look like.
[4:10] And the image occlusion node just adds some kind of shadow in the texture as well.
[4:14] So I'll shift, control and left click on the principle.
[4:17] We used to have node again, so we can see its output.
[4:19] And so what we can do is we can add a mix node.
[4:21] So either shift A and then search or mix or click here and go to add over their mix.
[4:28] And then set this to color and set this to multiply because we're going to multiply
[4:33] these two textures and then drag the color here to start A and the AO to start B.
[4:39] And then the results can go back into the base color.
[4:42] And so now when I drag this factor to zero, we are just seeing the texture the way it was before.
[4:47] So I can show you the difference.
[4:49] So if I just drag the base color directly into here, we see the same result as if we
[4:54] have the factor of zero with this mix.
[4:57] And when I drag the factor to one, then we mix in this AO.
[5:01] So you can see the difference when I add it and when I remove it.
[5:05] So the AO or ambient occlusion just adds a bit more shadow to it.
[5:08] They don't have to keep this at one.
[5:09] It can also just be a more subtle effect.
[5:11] And so that's how we set up the PBR textures.
[5:14] Now, if you want to have a little bit more detail out of this, I can add a camera.
[5:18] So shift A and choose camera.
[5:20] And then to make the camera look at this, I'll press control alt and zero.
[5:25] And that just gives the camera the view that we have in the viewport.
[5:28] And then in the option panel here, if I go to view, I can choose to lock camera to view.
[5:33] So enable this and press N again to close that.
[5:36] And now we can rotate the view in the camera view and zoom in and out.
[5:40] Just like we would with the 3D viewport.
[5:42] And when you're happy with that, you can unlock it.
[5:45] So we can just zoom in and out on that camera view.
[5:48] Now let's have a look at how we can squeeze a bit more detail out of that texture.
[5:52] So instead of a shader editor, I'm going to add a image editor
[5:55] and scroll up to zoom in a bit.
[5:57] And let's render this.
[5:58] So go to render, render image or press F12.
[6:02] And the reason it's showing the render outputs in my image editor window here
[6:06] and not in some popup window is because in preferences,
[6:09] under interface, I've set temporary editors render into image editor.
[6:15] So you can choose here if you want to open that in a new window or in the image editor.
[6:19] And I just prefer to keep it in the interface of Blender rather than constantly having popup windows.
[6:24] So this is the result of the render with just two levels of subdivisions.
[6:29] And if I increase the subdivisions here, then we will get more detail out of our texture.
[6:34] But another thing I can do because I'm using a camera, I can go here
[6:37] and I can choose the experimental feature set.
[6:40] And then in the subdef modifier, I can check adaptive subdivision.
[6:44] And what that does is it will add more resolution to where the camera is close to the object.
[6:51] And it will use less resolution for where it is far away.
[6:54] And so you can see the result when I render this.
[6:57] And so this is the result with a dicing scale of one.
[7:00] And let me just open another slot for another render.
[7:03] And we can compare them more easily.
[7:05] And so the dicing scale, I will set it to five, for example, and render again.
[7:10] So this is the result of a dicing scale of five.
[7:13] And you can see when I compared to the previous render,
[7:15] that it is much lower resolution.
[7:18] So when you increase this number, you reduce the resolution.
[7:21] So the lower this number, the higher the resolution and the higher the detail on your object will be.
[7:26] But of course, at the cost of longer render time.
[7:29] And in some cases, if you set it to two, though, then it might run out of memory as well.
[7:33] So what if you want to use EV instead of cycles?
[7:36] Well, good news.
[7:37] It's very easy as a Blender 4.2.
[7:40] You just have to switch to EV.
[7:42] And that's all.
[7:43] As you can see, you now have displacement in EV as well.
[7:47] Now, if you want this material to look smaller or bigger,
[7:49] you can go to the mapping node and then click and drag down on these scale values.
[7:54] So you select all of them.
[7:56] And then you can just add a higher value like three, for example,
[7:59] and that scales the texture down.
[8:01] And now it's very obvious that we need to increase the levels of the resolution a bit.
[8:06] Just make sure that the levels of the render are also set higher.
[8:09] Otherwise, your render will turn out lower resolution than your viewport.
[8:13] One more thing you might be wondering is what if you want to make this real geometry?
[8:18] Now, you can see that this mesh is still very simple.
[8:21] And what if I want to have all this real displacement as geometry?
[8:25] Well, it's not enough to just apply the sub-diff modifier,
[8:28] because as you can see, it's still perfectly smooth and round.
[8:32] Let's undo that.
[8:33] Well, the way you can do that is to select the displacement texture and the displacement node
[8:37] and either mute them by pressing M or just delete them by pressing X.
[8:41] And then you can add a displacement modifier and then click on new.
[8:45] And then click on this icon to go to the texture tab
[8:47] and then select the displacement texture from your download at PBR set.
[8:51] And it usually has this in the file name.
[8:54] And of course, now it looks very strange.
[8:55] So as the coordinates, use UV and choose the UV map.
[8:59] And then reduce the strength to something like 0.1 again.
[9:03] And as you can see, now we have the displacement back.
[9:06] Now you might notice that it doesn't really look right.
[9:08] And that's because we had the scale of the material set to three.
[9:11] But the displacement still has the scale of one.
[9:14] So here in the displacement texture, click on this icon.
[9:17] And then in the texture tab under mapping,
[9:19] set this to the same value that you have here.
[9:21] So in this case, three.
[9:23] And as you can see, now it looks more like the way it should.
[9:26] And then select your object by clicking on it,
[9:28] Ctrl A and choose visual geometry to mesh.
[9:32] And that just applies all the modifiers.
[9:34] And as you can see, now we have all of this as geometry.
[9:38] Now, what if your object simply doesn't have a UV map?
[9:41] So this is a UV sphere, which comes with UV map by default.
[9:44] But let's just delete it.
[9:46] And in that case, it doesn't know how to map the textures.
[9:49] But what we can do is we can just use generated texture coordinates.
[9:53] So drag the generated into the vector here.
[9:55] And then in the textures, instead of flat, use box.
[9:59] So set it to box for all of these textures.
[10:02] And then we can use a blend value of something like 0.2.
[10:05] And that just blends the projection in every way.
[10:08] So it doesn't work perfectly with this kind of brick texture,
[10:11] but it's better than nothing.
[10:12] And this is called triplanar or box mapping.
[10:15] And it just kind of projects the texture from three axes.
[10:18] But as you can see, that also makes it kind of blend here and there,
[10:21] which is not ideal.
[10:22] But if you have no UVs, then it's better than nothing.
[10:25] But of course, a better solution if you don't have a UV map,
[10:28] is just to UV unwrap it so you do have a UV map.
[10:31] So I hope that answered all of your questions
[10:33] about setting up VBR textures in Blender for Cycles and EV.
[10:38] If you still have some questions about this, please leave a comment.
[10:41] And thanks for watching all the way to the end.



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
