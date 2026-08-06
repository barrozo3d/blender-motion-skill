---
title: Easy PBR Textures - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=qxxoDYGrvtw
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 4.2 (explicitly named for EEVEE displacement support)"
tags: [materials, shaders, displacement, cycles, eevee, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/easy-pbr-textures---blender-secrets/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Easy PBR Textures - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=qxxoDYGrvtw)
**Author:** Blender Secrets
**Duration:** 10m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


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

## Captured Frames

- [0:21] tutorials/frames/easy-pbr-textures---blender-secrets/frame_000.jpg
- [1:56] tutorials/frames/easy-pbr-textures---blender-secrets/frame_001.jpg
- [2:09] tutorials/frames/easy-pbr-textures---blender-secrets/frame_002.jpg
- [3:13] tutorials/frames/easy-pbr-textures---blender-secrets/frame_003.jpg
- [4:21] tutorials/frames/easy-pbr-textures---blender-secrets/frame_004.jpg
- [6:40] tutorials/frames/easy-pbr-textures---blender-secrets/frame_005.jpg
- [7:37] tutorials/frames/easy-pbr-textures---blender-secrets/frame_006.jpg
- [8:47] tutorials/frames/easy-pbr-textures---blender-secrets/frame_007.jpg

---

## Structured Notes

### Core Technique
A complete PBR-texturing pipeline: sourcing free physically-based textures from Polyhaven, auto-wiring them with Node Wrangler's Principled Texture Setup, driving true geometric displacement (with adaptive subdivision for render efficiency), converting that displacement into real baked geometry, and handling edge cases like non-UV'd objects via triplanar/box mapping — covering both Cycles and EEVEE (4.2+).

### Summary
Frame 000 shows the sourcing step: Polyhaven's Textures > Brick browser with a red brick sphere thumbnail selected mid-hover, illustrating the free-texture search that starts the workflow. Frame 001 shows a bare UV sphere with a Principled BSDF material freshly created but no textures wired in yet — the state right before running Node Wrangler. Frame 002 shows the payoff of Shift+Ctrl+T (Principled Texture Setup): a full chain of Mapping/Image Texture nodes auto-connected into the Principled BSDF's Base Color, Roughness, Normal and other sockets. Frame 003 shows the shader graph fully wired with an interior-room HDRI background rendering behind a smooth (not-yet-displaced) brick sphere in Cycles Texture Preview. Frame 004 shows the Displacement node in the graph with the ambient-occlusion node chain visible alongside it, mid-render with the brick sphere now showing real surface relief. Frame 005 shows a side-by-side comparison render setup: a wireframe sphere silhouette next to a fully rendered, deeply-displaced brick sphere — illustrating the adaptive-subdivision dicing-scale comparison technique. Frame 006 shows the same brick sphere at a different dicing-scale render, filling the frame at high resolution to compare detail levels. Frame 007 shows the later "convert displacement to real geometry" step: the shader graph with a Displacement Texture node selected and its Texture Properties tab open (Mapping section), matching the material's mapping scale to the modifier's before running Convert to Mesh.

### Key Steps
1. **Setup:** enable the Node Wrangler add-on (Preferences > Add-ons, search "node," check the box).
2. **Source textures:** on polyhaven.com, go to Assets > Textures, search/pick a texture (e.g. Castle Brick 02 Red), choose a resolution (4K is usually enough), then use the ZIP download picker to select exactly what's needed — a .blend file with the material pre-assembled, JPEG for Diffuse/color, EXR (not PNG) for Displacement since it's smaller and holds full precision, and OpenGL (not DirectX) normal maps since Blender uses OpenGL.
3. **Wire the material:** open a Shader Editor, add a test object (UV sphere, Shade Smooth, a couple of subdivision levels), create a new material, select the Principled BSDF node and press Shift+Ctrl+T to open Node Wrangler's texture-setup dialog; select all the downloaded texture files and click "Principled Texture Setup" to auto-generate and wire the full node chain (mapping + all texture maps) — everything except the Ambient Occlusion node, which is wired manually later.
4. **Preview correctly:** switch the viewport to Texture/Rendered shading, set the render engine to Cycles with GPU device enabled (Preferences > System) and denoising on; raise World strength or enable an HDRI (via the free Gaffer add-on, from Polyhaven's makers) since the default world is too dark.
5. **Add real displacement:** with the object selected, go to Material Properties > Settings > Displacement and set it to "Displacement Only" (not the Displacement panel's own field, which does nothing on its own); open the Displacement node and set its Scale to roughly 0.1 to reveal real surface relief. "Displacement and Bump" pulls more apparent detail at low subdivision at the cost of longer render times — use "Displacement Only" for pure geometric height.
6. **Mix in Ambient Occlusion (optional):** Shift+Ctrl+click each texture node to preview its output; add a Mix Color node set to Multiply; feed the Base Color texture into Input A and the AO node into Input B; feed the Mix result into the Principled BSDF's Base Color; the Mix Factor blends between 0 (no AO) and 1 (full AO) — keep it subtle rather than maxed out.
7. **Frame with a camera:** Shift+A > Camera, Ctrl+Alt+Numpad0 to snap it to the current view, then enable "Lock Camera to View" in the viewport's N-panel View tab so orbiting the 3D view also moves the camera; disable the lock once framed.
8. **Render and tune resolution vs. speed:** render with F12 (routed into the Image Editor if "Render into image editor" is set under Preferences > Interface > Temporary Editors); raise Subdivision modifier levels for more displaced detail; with a camera present, enable the Experimental feature set and check "Adaptive Subdivision" on the Subdivision modifier so more geometry is generated near the camera and less far away; tune the Dicing Scale — lower values = higher resolution/detail but longer render time and higher memory use (values around 1-2 risk running out of memory; 5 is much coarser).
9. **EEVEE support (Blender 4.2+):** simply switching the render engine from Cycles to EEVEE preserves the same displacement setup with no extra steps.
10. **Rescale the material:** select all Mapping-node Scale values and drag/type a higher number (e.g. 3) to shrink the visible texture tiling; remember to raise the render's subdivision levels too, or the final render will be lower-detail than the viewport preview.
11. **Bake displacement into real geometry:** select and mute (M) or delete (X) the Displacement texture/node chain in the shader (so it stops driving shader-only displacement); add a Displacement modifier, click New, open its Texture Properties tab and pick the same displacement texture from the downloaded PBR set (usually named with a DISP suffix); set its Coordinates to UV and pick the UV map; set Strength to ≈0.1; critically, open the Displacement texture's own Mapping settings and match its scale to whatever value was set on the shader's Mapping node (e.g. 3) or the geometric and shaded displacement won't line up; finally select the object and use Ctrl+A > Visual Geometry to Mesh (applies all modifiers) to bake the displacement permanently into the mesh.
12. **Objects without a UV map:** if there's no UV map, plug Generated (not UV) into the Mapping node's Vector input, and switch every texture node's Projection from Flat to Box; add a Blend value (~0.2) to soften the seams between the three projected axes — this triplanar/box mapping doesn't look as clean as true UVs on strongly directional textures like brick, but is usable when no UV map exists; unwrapping the object properly remains the better long-term fix.

### Nodes / Settings
- **Add-ons:** Node Wrangler (Shift+Ctrl+T Principled Texture Setup), Gaffer (free, Polyhaven-made, adds one-click HDRI to World).
- **Shader nodes:** Principled BSDF, Mapping (+ Texture Coordinate: Generated for no-UV objects), Image Texture (per PBR channel: Diffuse/Color, Roughness, Normal — OpenGL variant, Displacement — EXR), Displacement node (Scale ≈0.1), Mix Color node (Multiply, for AO), Ambient Occlusion node, Normal Map node.
- **Material Settings:** Displacement dropdown set to "Displacement Only" (vs. "Displacement and Bump").
- **Modifiers:** Subdivision Surface (Levels Viewport/Render, Adaptive Subdivision under Experimental feature set, Dicing Scale), Displacement modifier (New texture, Texture Properties > Mapping scale matched to shader, Coordinates: UV, Strength ≈0.1).
- **Render:** Cycles (GPU device, denoising), EEVEE (Blender 4.2+, same setup works unmodified), F12 / render-into-Image-Editor preference, Render Film > Transparent (hide HDRI background).
- **Camera:** Ctrl+Alt+Numpad0 (snap to view), N-panel View tab "Lock Camera to View."
- **Finalizing geometry:** Ctrl+A > Visual Geometry to Mesh (bakes Displacement modifier into real mesh data).

### Difficulty
Intermediate

### Blender Version
Blender 4.2 — explicitly named for EEVEE's displacement support ("It's very easy as a Blender 4.2. You just have to switch to EEVEE").

### Tags
materials, shaders, displacement, cycles, eevee, intermediate

---

## Related Tutorials
- [6 Panel Cut Tips - Blender Secrets](6-panel-cut-tips---blender-secrets.md) — shares materials, displacement, cycles; that tutorial bakes hand-sculpted/painted hard-surface detail to a normal map, this one sources and applies photo-real PBR texture sets with real geometric displacement instead.
