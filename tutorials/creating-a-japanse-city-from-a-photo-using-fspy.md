---
title: Creating a Japanse city from a photo using fSpy
source: YouTube
url: https://www.youtube.com/watch?v=GzHvD9RFrT8
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified (Cycles/AGX/fSpy/Gaffer workflow, likely 4.0+ given AGX)"
tags: [materials, shaders, volume, lighting, hdri, rendering, cycles, camera, animation, advanced]
extraction_status: complete
frames_dir: tutorials/frames/creating-a-japanse-city-from-a-photo-using-fspy/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Creating a Japanse city from a photo using fSpy

**Source:** [YouTube](https://www.youtube.com/watch?v=GzHvD9RFrT8)
**Author:** Blender Secrets
**Duration:** 16m56s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] This is the view from the Tokyo Metropolitan building, which you can visit for free to get
[0:12] a view of Shinjuku.
[0:13] It's not the highest place that you can find in Tokyo, but it offers a look down on some
[0:18] neighboring buildings.
[0:19] So I took the opportunity to take some photographs there for this tutorial.
[0:24] You can download these photos along with the written version of this tutorial in my ebook.
[0:28] The link for that is in the description.
[0:31] I also want to mention that you can get a 20 euro discount if you get both my book and
[0:35] my video course as a bundle.
[0:37] Let's turn this photo into a mysterious post-apocalyptic world.
[0:42] For this we'll use Fspy, which is both a standalone free app and a free Blender add-on.
[0:48] You'll need the app to create the Fspy files and the add-on to import them in Blender.
[0:53] I have noticed from the comments on older tutorials about this topic that a lot of people
[0:58] download the wrong version of Fspy and therefore think that it no longer works.
[1:03] So make sure you use the links in the description of this video for the correct versions.
[1:08] To get started, download the Fspy setup file.
[1:13] Click on it to install it.
[1:16] This is the standalone Fspy app.
[1:19] You'll also need to download the Blender Fspy add-on, version 1.0.3.
[1:26] From Blender go to Preferences and install the add-on.
[1:30] Click on Install and select the downloaded zip file.
[1:35] And then enable it.
[1:38] Drag and drop a photograph into the standalone Fspy app.
[1:42] We can enable a 3D guide in the shape of a cube.
[1:46] You can move this cube around to check if the perspective lines up with the photo.
[1:50] In the beginning it doesn't, so we'll have to adjust the finishing points.
[1:55] I would like to have the axis in Fspy point in the same direction as the do in Blender.
[2:00] That way we won't end up with some weirdly oriented upside-down scene.
[2:05] You can see the axis for reference in the navigation Gizmo in Blender.
[2:10] I'll quickly draw some annotations to show you the positive and negative axes.
[2:16] To make the axes in Fspy correspond to those in Blender, we'll need to change the finishing
[2:20] point axes.
[2:22] Like this.
[2:26] As you can see, now they match those in Blender.
[2:31] Now we can start aligning the finishing points by dragging their endpoints.
[2:36] By holding Shift you can zoom in to more precisely place them.
[2:48] In this case I'm using this building as reference.
[2:51] We can test if the perspective of the 3D guide cube matches the buildings.
[2:55] It seems to be almost there.
[2:59] I think we can improve it by using a building that is further away as the reference for this
[3:02] vanishing point.
[3:05] Now it seems to align even better.
[3:08] The next step is to save this file.
[3:11] This file can then be imported in Blender.
[3:14] Let me just remove this annotation.
[3:19] Because we installed the Fspy addon, we now have an Fspy import option.
[3:24] I'll choose the file I just saved from the standalone app.
[3:29] This file contains the photograph as well as a camera.
[3:34] And as you can see from the camera view, the cube aligns to the perspective of the photo.
[3:40] It's a good idea to save the Blender file at this point.
[3:45] We still have the original camera from the default Blender scene, which we don't need.
[3:51] So select that one and just delete it.
[3:53] As you can see, the imported camera has the name of the Fspy project.
[3:59] I'll turn on X-ray mode so I can see the buildings in the photograph through the mesh.
[4:04] In edit mode I'll delete this bottom face as it won't be visible anyway.
[4:08] Now it's just a matter of moving vertices to match the buildings in the photo.
[4:12] To move things along just one axis, press for example G and Z to move it along the Z-axis,
[4:18] G and Y to move it along the Y-axis, or G and X to move it along the X-axis.
[4:25] By holding Alt and clicking, we can select all these bottom edges and move them down.
[4:29] This is the very basic shape of this building and from here it's just a matter of adding
[4:33] more detail.
[4:36] But first let's select all and duplicate with Shift D for the next building.
[4:41] By pressing G to move and then Shift Z, we exclude the Z-axis so we can move it easily
[4:46] without accidentally moving up or down.
[4:50] And then it's just a matter of adjusting the shape for that particular building.
[4:58] Press R and Z to rotate along the Z-axis like for this building here.
[5:04] If you press G twice, select an edge to slide along, it will turn yellow, and then press
[5:09] C, you can slide outwards along that edge.
[5:14] This can be convenient if you've rotated something and need to move along its local orientation.
[5:20] So just press G twice, choose the edge to slide along so it turns yellow, then press
[5:25] C to be able to slide away from the geometry.
[5:29] To create these gaps in the side of the building, I'll select and duplicate this face, then
[5:34] scale it along the X-axis and move it over here.
[5:40] Then extrude along the Y-axis with E and Y.
[5:44] I just move it slightly so there are no faces overlapping in the exact same location.
[5:49] Let me just check the face orientation.
[5:51] Yep, they are flipped.
[5:53] Pressing Shift N recalculates the normals so that they are no longer flipped.
[5:57] I'm planning to use this to do a boolean cut and flipped faces can cause trouble with boolean
[6:01] cutting.
[6:03] Now with this extruded face selected, go to Face, Intersect boolean.
[6:07] This cuts a nice chunk out of the building.
[6:14] We can repeat the same steps on this side.
[6:17] The benefit of duplicating a face for this purpose is that the face is already perfectly
[6:21] aligned with the side that we want to cut out of.
[6:28] In this case it seems that the boolean cut didn't work.
[6:32] If that happens you can try a different solver method or checking these boxes.
[6:36] Checking Self-Intersection solves the problem in this case.
[6:41] Some minor adjustments are necessary.
[6:46] Next let's do the corners of this building.
[6:49] Hold Shift and select them all.
[6:52] Press Ctrl B to bevel and then scroll the mouse go up to add one segment.
[6:57] Changing the shape to zero gives us the shape we need.
[7:02] We can fine tune it if necessary.
[7:06] I want to explain the rest of the modeling step by step as it's mostly very basic and
[7:10] repetitive stuff.
[7:12] Just lots of extruding, adding more loops where needed, moving faces and beveling here
[7:18] and there to add some rounded parts.
[7:23] Honestly a lot of these things are just simple cubes.
[7:27] You can get away with a lot when using production mapping like this because the texture has
[7:32] so much information.
[7:35] After some more basic modeling we have a bunch of simple buildings.
[7:39] Next we need to add a material.
[7:41] I'll open a shader editor for that.
[7:44] Select the principle BSDF and press Ctrl T to add the necessary nodes.
[7:48] The photo is already loaded with the Fspire file so we can choose it as the texture.
[7:57] Select all in edit mode, press U and choose project from view.
[8:02] Then switch to material preview to see the result.
[8:06] It kind of worked but as you can see it's all wobbly and distorted.
[8:10] We can make this better by simplifying a bunch of times although in this case that adds a
[8:14] lot of unnecessary geometry.
[8:17] So let's not do that.
[8:20] I'll just move everything to the center of the world.
[8:23] This is not strictly necessary but I just feel weird having everything in a strange location.
[8:30] Let's add a grid.
[8:34] And increase its resolution to 100 by 100.
[8:38] Rotate and scale it so that it encompasses the buildings.
[8:43] And move it so it's not overlapping or inside of them.
[8:46] Go to front orthographic view.
[8:49] In edit mode press A to select all and press X then choose only faces.
[8:55] Now we just have a grid of edges.
[8:58] I'll just quickly rename this to buildings to keep things organized.
[9:04] Now with the buildings selected go to edit mode.
[9:07] Hold Ctrl and in the outliner select the grid.
[9:10] Go to mesh knife project.
[9:13] And then make sure cut through is enabled.
[9:18] Now the buildings are sliced giving them all enough geometry so that the texture is not
[9:22] distorted.
[9:25] We can hide or just delete the grid.
[9:28] Now if we carefully move the camera you'll see that we get this solo camera move.
[9:34] If you want you can increase the pass part 2 value so you don't see what's outside
[9:38] of the camera frame.
[9:41] And we can add an empty to use as the depth of field target.
[9:46] To get some unrealistic but nice looking shadow depth of field.
[9:52] What we can do is add a plane and add the background texture to it.
[9:56] To make sure it's always facing the camera add a track 2 constraint to it.
[10:01] Then choose the camera as the target.
[10:05] Move the plane behind the buildings and scale it up as necessary to fill the frame.
[10:09] Add some edge loops so that the texture won't be distorted.
[10:12] And just like with the buildings in the foreground select all, press U and choose project from
[10:17] view.
[10:18] You can use the same material as for the buildings.
[10:21] We can disable the background image now as we no longer need it for reference.
[10:26] Now the far background is also affected by the camera's depth of field.
[10:31] And we can move the empty to change the focus point.
[10:36] Now I'd like to add some volumetric haze to make it look more interesting.
[10:41] To do that I just add a cube around the scene.
[10:46] And for ease of use I'll set it to Bounce in the viewport display.
[10:51] Give it a material with an appropriate name.
[10:54] Remove the principle base diff and add a volume scatter node instead.
[10:59] Connect it to the volume input of the material.
[11:03] The density value controls how thick the haze is.
[11:06] I'll add an HDRI using the Gaffer add-on.
[11:11] Of course all this will look much better in cycles.
[11:14] And it will be faster if I use my GPU and enable D Noise.
[11:20] Using the Gaffer add-on it's easy to test different HDRIs to find a good look.
[11:26] If necessary we can always adjust the position of the buildings.
[11:33] To control the look of the haze we can use the NSotrp value as well.
[11:37] However you can also just move the volume cube.
[11:42] If you place the cube just before the camera like this the buildings nearest to the camera
[11:46] will have a bit more contrast.
[11:51] Let's add a timeline so we can animate in the camera.
[11:55] Select the camera and add a keyframe at frame 1.
[11:59] Set the key to linear interpolation so the movement is linear instead of easing in.
[12:07] I'll change the resolution to a more standard 4k format.
[12:13] And then we can go to a later frame and move the camera to a new position.
[12:17] By holding shift it's easier to make a subtle change in the location of the camera.
[12:22] I'll also move it down a bit.
[12:24] And then I'll set a keyframe.
[12:27] So now we have this small movement.
[12:31] And I'll set that second key to linear as well.
[12:35] If this was shot from a helicopter for example the movement would be linear in real life
[12:39] as well.
[12:41] Let's calculate how many frames we need.
[12:43] I want 5 seconds of animation with 24 frames per second so that's 120 frames.
[12:50] I'll move this key to frame 120 and set the end to 120 as well.
[12:56] To do a test render I'll limit the render time to 1 second per frame and set the resolution
[13:01] to 25%.
[13:06] As this will render pretty fast I'll choose an H264 video for the test.
[13:13] Then press Ctrl F12 or choose render animation.
[13:16] As you can see at this low res and with only 1 second as the render limit it goes pretty
[13:21] fast.
[13:23] And this is the result of the low quality test render.
[13:28] I recommend always rendering a low quality quick render before you commit to rendering
[13:32] slow high quality frames.
[13:35] I'm actually not really happy with this animation as it's not really showing off the 3D nature
[13:39] of the scene.
[13:40] So I'll adjust this second keyframe to make it a bit more interesting.
[13:45] This camera move is better.
[13:48] Ok, let's set the resolution back to 4K and open EXR for the file format.
[13:55] Now we'll render an image sequence.
[13:58] 16 bit or half float is enough.
[14:01] I just check that it's set to AGX which will give us a nice linear image for later color
[14:06] grading.
[14:07] And I'll also increase the render time of course.
[14:11] Let's calculate how long it'll take or less.
[14:14] 120 frames times 10 seconds divided by 60 seconds gives us 20 minutes of render time.
[14:21] 30 seconds per frame will take an hour.
[14:24] That seems fine to me.
[14:26] Before rendering let's save just in case.
[14:29] And to make it easier for the computer I'll set the viewport to solid mode.
[14:35] Actually before I render I want to make the scene a bit more mysterious.
[14:39] I think it could be interesting if one of these windows had a light inside as if that's
[14:43] like the last person in the whole world living there.
[14:47] I'll need to add a couple more edge loops.
[14:50] If you press G twice you can slide edges without distorting the texture.
[14:55] I'll add a second material to the window.
[15:00] Assign it to the selected face and give it a name.
[15:04] Remove the principaled BSDF and put an emission shader in its place.
[15:08] We can manually give it a color.
[15:11] But to be more realistic we can add a blackbody node to use a real-life color temperature
[15:17] value.
[15:18] Something like 2200 calvin gives us a nice warm artificial light color.
[15:22] You can just google these more commonly used blackbody values.
[15:26] It looks like 3400 calvin would be more appropriate.
[15:34] I'd like the light to stand out more and we can try to increase the strength.
[15:39] However we can experiment with the lighting so the window is in the shaded side of the
[15:43] building which makes it stand out more.
[15:45] The gather app lets you rotate the HDRI easily.
[15:50] This HDRI is from Polyhaven by the way.
[15:55] We can make it even darker and more dramatic by increasing the density of the volume.
[16:02] I wouldn't want to live in this post-apocalyptic city.
[16:05] In reality this part of Tokyo is a lot of fun and not post-apocalyptic at all.
[16:10] We can also reduce the brightness of the HDRI.
[16:16] This looks quite interesting and mysterious.
[16:18] Let's save it and render it in 4K.
[16:22] And here is the result of the render.
[16:28] And here it is after color grading it in DaVinci Resolve.
[16:32] Thank you very much for watching patiently all the way to the end and I hope it was an
[16:35] interesting video for you.
[16:37] See you next time.



---

## Captured Frames

- [2:00] tutorials/frames/creating-a-japanse-city-from-a-photo-using-fspy/frame_000.jpg
- [3:40] tutorials/frames/creating-a-japanse-city-from-a-photo-using-fspy/frame_001.jpg
- [6:05] tutorials/frames/creating-a-japanse-city-from-a-photo-using-fspy/frame_002.jpg
- [7:55] tutorials/frames/creating-a-japanse-city-from-a-photo-using-fspy/frame_003.jpg
- [9:15] tutorials/frames/creating-a-japanse-city-from-a-photo-using-fspy/frame_004.jpg
- [10:45] tutorials/frames/creating-a-japanse-city-from-a-photo-using-fspy/frame_005.jpg
- [12:15] tutorials/frames/creating-a-japanse-city-from-a-photo-using-fspy/frame_006.jpg
- [16:25] tutorials/frames/creating-a-japanse-city-from-a-photo-using-fspy/frame_007.jpg

---

## Structured Notes

### Core Technique
A complete photo-to-3D city pipeline: match a real photograph's camera with the free fSpy app + Blender add-on, block out buildings by moving vertices to match the photo (boolean cuts, bevels), project-texture the buildings directly from the photo (fixing UV distortion via a Knife-Project grid), add a matching background plane + volumetric haze + HDRI for atmosphere, animate a subtle camera move, and finish with an emissive "lit window" story detail and EXR rendering for color grading.

### Summary
Frame 000 shows the standalone fSpy app: a real Shinjuku/Tokyo skyline photo with a 3D calibration cube and its vanishing-point guide lines overlaid, camera parameters visible in the side panel — mid-calibration. Frame 001 shows the same photo after import into Blender via the fSpy add-on: a default cube now precisely aligned to the photo's perspective from the matched camera's point of view, confirming the camera match succeeded. Frame 002 shows detailed building blockout in progress: a rooftop structure's edges (orange selection) being shaped to match the actual rooftop geometry visible in the background photo, viewed from the matched camera angle. Frame 003 shows a wider blockout stage: several gray, un-textured building volumes roughly matching the skyline's silhouette, with a Shader Editor graph (Texture Coordinate → Mapping → Image Texture → Principled BSDF) open below, about to receive the projected photo texture. Frame 004 shows the Knife-Project fix in two side-by-side views: Camera Perspective (left, buildings now textured with the photo but showing UV wobble) and Front Orthographic (right, a dense reference grid overlaid in orange ready to be knife-projected through the buildings to add clean, undistorted geometry). Frame 005 shows the background plane setup: the photo visible behind a simple box/plane shape in Camera Perspective, with a Move/Transform panel and Proportional Editing option visible, mid-alignment. Frame 006 shows the render-setup stage: Output panel (Resolution, Frame Rate, File Format, Color, Compression) open next to a Top Orthographic view showing the camera's path/track line across the scene, with the Timeline below for the camera-move animation. Frame 007 shows the atmospheric final payoff: a heavily hazy, moody rendered cityscape close-up with one small illuminated window glowing in an otherwise dark building — the deliberate "last person alive" story detail.

### Key Steps
1. **Camera-match a real photo with fSpy:** download the standalone fSpy app and the matching Blender fSpy add-on (v1.0.3 specifically noted — using a mismatched version is a common cause of it "not working"); install and enable the add-on in Preferences. Drag a photo into the standalone app, enable the 3D guide cube, and adjust the vanishing-point line endpoints (hold Shift while dragging for precision) until the cube's perspective matches real buildings in the photo — pick reference buildings that are further away for a more accurate vanishing point. Before finalizing, align fSpy's axis directions to Blender's (using the on-screen navigation gizmo as reference) to avoid an upside-down/misoriented import. Save the fSpy file.
2. **Import into Blender:** use the fSpy add-on's Import option to load the saved file — this brings in both the photo (as camera background) and a matched Camera object; delete Blender's original default camera, since the imported one (named after the fSpy project) replaces it. Save the .blend file at this point.
3. **Block out buildings to match the photo:** enable X-Ray so photo-referenced geometry is visible through the mesh; in Edit Mode delete unseen bottom faces; move vertices with axis-constrained G+X/Y/Z (or Alt-click to select whole edge loops) to match building silhouettes in the photo. Duplicate (Shift+D) a basic building shape for the next one, using G then Shift+Z to move without affecting height, R+Z to rotate to match orientation. Use G,G (edge slide) then C to slide an edge outward along local orientation after rotating something.
4. **Boolean-cut architectural details:** duplicate a face, scale/position it to define a cutout shape (e.g. a gap in a facade), extrude it through the building with E+Y, check/fix face orientation with Shift+N (flipped normals cause boolean problems), then use Face → Intersect (Boolean) to carve the cut. If a boolean cut doesn't take effect, try a different Solver method or enable Self-Intersection. Reuse the same duplicated-face trick on other sides since it's already perfectly aligned to what needs cutting.
5. **Detail corners and repeat:** select corner edges, Ctrl+B to bevel (scroll for segments), set Shape to 0 for a clean chamfer profile. The rest of the modeling is repetitive basic extrude/loop-cut/bevel work — production/photo-projected mapping carries a lot of visual weight even on very simple cube-based geometry.
6. **Project-texture from the photo:** in the Shader Editor, select the Principled BSDF and press Ctrl+T to auto-generate the necessary texture-coordinate node chain; pick the photo (already loaded via the fSpy file) as the Image Texture. Select all in Edit Mode, U → Project From View to project UVs matching the camera angle, then check the result in Material Preview.
7. **Fix UV/texture distortion with a Knife-Project grid:** the initial projected texture looks wobbly/distorted on angled faces. Fix: move everything to world origin (optional, for tidiness); add a Grid primitive, set its resolution to 100×100, rotate/scale it to encompass all buildings without overlapping them; go to Front Orthographic, select all in Edit Mode and X → Only Faces (leaving just an edge grid); rename the buildings object for organization; with the buildings selected then Ctrl-select the grid in the Outliner, use Mesh → Knife Project with Cut Through enabled — this slices extra geometry into the buildings wherever the fine grid crosses them, giving enough resolution that the projected texture no longer distorts. Delete/hide the grid afterward.
8. **Background plane:** add a plane behind the buildings, apply the same background photo texture and project-from-view UVs; add a Track To constraint targeting the camera so it always faces it; scale to fill the frame; add extra edge loops so its texture doesn't distort either; disable the camera-background reference image once it's no longer needed.
9. **Volumetric haze:** add a large cube enclosing the scene (set its Viewport Display to Bounds for performance); give it a material with the Principled BSDF removed and a Volume Scatter node wired into the Volume output instead — Density controls haze thickness. Moving the volume cube itself (e.g. placing it just in front of the camera) changes which buildings read with more contrast.
10. **HDRI lighting:** add an HDRI via the Gaffer add-on (this example uses a Poly Haven HDRI) for quick browsing/testing; render in Cycles with GPU + Denoise enabled for speed. HDRI rotation and brightness, plus haze Density, are all adjustable to dial in mood.
11. **Animate a subtle camera move:** add a keyframe at frame 1 (set to Linear interpolation for a mechanical, e.g. helicopter-shot-style, movement rather than eased motion); set render resolution (e.g. 4K); move to a later frame, nudge the camera position (hold Shift for subtle precision) and down slightly, keyframe again (also Linear). Calculate frame count from desired duration × fps (5 seconds × 24fps = 120 frames) and set the End frame accordingly.
12. **Test-render before committing:** limit render time per frame (e.g. 1 second) and drop resolution (e.g. 25%) for a fast H.264 preview via Ctrl+F12 / Render Animation — always sanity-check camera movement and framing at low quality before a slow high-quality render. Adjust keyframes if the motion doesn't sell the 3D depth of the scene well.
13. **Final render setup:** set resolution back to full (4K), switch File Format to OpenEXR (16-bit/half-float is enough) for an image sequence, use the AGX view transform for a linear-friendly result suited to later color grading, increase per-frame render time budget, and estimate total render time (frames × seconds-per-frame ÷ 60). Set viewport shading to Solid before rendering to reduce system load. Save before committing to the full render.
14. **Story detail — a lit window:** add extra edge loops (G,G to slide edges without texture distortion) around one window; assign it a second, named material with the Principled BSDF replaced by an Emission shader; drive its color via a Blackbody node using a real-world color-temperature value (~2200-3400K gives a warm artificial-light look — searchable online) rather than eyeballing a color; increase Emission Strength for prominence; placing the window on the HDRI's shaded side makes it stand out more by contrast. Increasing haze Density and lowering HDRI brightness further sells a dark, moody, "last person alive in a post-apocalyptic city" atmosphere.
15. **Finish:** render the final 4K EXR sequence, then color-grade the result externally (this example used DaVinci Resolve).

### Nodes / Settings
- **Add-ons:** fSpy (standalone camera-matching app + matching Blender import add-on, v1.0.3), Gaffer (HDRI browsing).
- **Camera matching:** fSpy vanishing-point cube guide, axis-orientation matching to Blender's gizmo.
- **Modeling:** X-Ray, axis-constrained G moves, Shift+D duplicate, G+Shift+[axis] (exclude an axis), R+[axis] rotate, G,G+C (edge slide then slide-along-edge), Boolean (Face → Intersect, Solver/Self-Intersection options), Shift+N (recalculate normals), Ctrl+B (bevel, Shape=0 for chamfer).
- **UV/Texturing:** Ctrl+T (auto-build texture node chain from a selected shader input), U → Project From View, Mesh → Knife Project (Cut Through) against a dense reference Grid for distortion-free photo projection, X → Only Faces (reduce a solid grid to just its edge lattice).
- **Constraints:** Track To (background plane always facing camera).
- **Shading:** Volume Scatter node (Density) on an enclosing cube for haze; Emission shader + Blackbody node (real color-temperature values) for the lit-window detail.
- **Render:** Cycles (GPU + Denoise), AGX view transform, OpenEXR 16-bit/half-float image sequence output, Linear keyframe interpolation for camera moves, low-res/short-time-limit test renders before full quality.
- **External:** DaVinci Resolve for final color grading.

### Difficulty
Advanced

### Blender Version
Not specified — Cycles/AGX/fSpy/Gaffer workflow, consistent with modern Blender 3.x-4.x (AGX view transform implies 4.0+).

### Tags
materials, shaders, volume, lighting, hdri, rendering, cycles, camera, animation, advanced

---

## Related Tutorials
- [Blender Secrets - Blender GIS (Extra Bonus Tutorial)](blender-secrets---blender-gis-extra-bonus-tutorial.md) — shares materials, lighting, hdri, rendering, cycles; same channel, complementary real-world-photo-to-3D-environment technique (satellite/GIS data vs. this video's single-photo fSpy camera match).
- [Blender Secrets - 4 tips for Photoreal Lighting](blender-secrets---4-tips-for-photoreal-lighting.md) — shares lighting, hdri, cycles, materials, rendering; same channel, complementary HDRI/photoreal lighting fundamentals used throughout this build.
- [Blender Secrets - 4 tips for Cinematic Lighting](blender-secrets---4-tips-for-cinematic-lighting.md) — shares lighting, hdri, materials, volume, cycles; same channel, same Gaffer add-on and volumetric-haze technique referenced in both.
