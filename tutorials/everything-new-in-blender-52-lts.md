---
title: Everything New in Blender 5.2 LTS 🍪
source: YouTube
url: https://www.youtube.com/watch?v=FlKu6e_VrDc
author: CG Cookie – Learn Blender
ingested: 2026-07-16
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/everything-new-in-blender-52-lts/
frame_count: 0
frame_status: pending-selection
---

# Everything New in Blender 5.2 LTS 🍪

**Source:** [YouTube](https://www.youtube.com/watch?v=FlKu6e_VrDc)
**Author:** CG Cookie – Learn Blender
**Duration:** 36m57s | 15 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py everything-new-in-blender-52-lts <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Blender 5.2 LTS has just been released and it includes some incredible new features
[0:05] as well as some welcome quality enhancements that are going to help you work even faster.
[0:09] I'm Jonathan Lampeau with CGCookie.com and in this video, we're going to cover everything
[0:14] that's new in Blender 5.2 LTS.


### Modeling & UVs [0:17]
**Transcript (timestamped):**
[0:17] One of the first add-ons that you might have heard about when watching modeling tutorials
[0:22] is the classic loop tools.
[0:24] They have become so ubiquitous over the years and are finally being built into Blender
[0:28] itself.
[0:29] Not only does this mean you don't have to install an extension to get them, they also
[0:32] are significantly faster now since they are rewritten in C and the UIs have been modernized.
[0:38] The ones that made it into 5.2 are circle, space evenly and flatten.
[0:43] The others will be coming later.
[0:45] In the snapping department, you can now snap to lattice objects.
[0:48] The array modifier, the newer geometry nodes one, got more user-friendly alignment options.
[0:54] Selection now respects the viewport's back face culling option, which makes it easier
[0:58] to work with interior geometry.
[1:01] 3D text objects now support complex characters that have above and below font instructions.
[1:06] In the UV editor, you can now delimit by seams, sharp edges or material boundaries when
[1:11] selecting linked.
[1:13] The copy mirror UV coordinates operator now works on any axis.
[1:17] A new select by winding operator helps to isolate flipped UVs.
[1:22] Select overlapped now works for the whole island in island selection mode.
[1:25] You can now unwrap islands to their original bounds, so they don't jump up and take the
[1:29] entire UV space every time you unwrap.
[1:32] You can now add snap points when setting the snap base in the UV editor, which snaps
[1:36] to the average between all of the points just like in the 3D view.


### Sculpting & Painting [1:40]
**Transcript (timestamped):**
[1:42] A brand new sculpting brush, scene project, allows you to shrink wrap geometry to the surface
[1:46] of other objects in the scene.
[1:48] The ad primitive tools are now available directly in sculpt mode.
[1:52] The color filter tools fill mode got an upgrade.
[1:55] You can now click to apply the current color, click drag to blend with the current color,
[2:00] hold control to swap to the secondary color, and you can use control X to perform a fill
[2:05] from any tool.
[2:06] If you enable dynamic topology and switch back and forth between sculpt mode, you no longer
[2:11] have to confirm to go back to using dynamic topology every time.
[2:14] The voxel remesher better interpolates attributes like vertex colors now.
[2:18] Vertex and weight paint modes now use a 3D brush just like sculpt mode.
[2:22] The brush advanced section is now a nicely organized panel.
[2:26] And when texture painting, the altered image is now included in Blender's auto save,
[2:30] which I think is going to save a lot of keyboards and tablets from being smashed.


### Geometry Nodes [2:35]
**Transcript (timestamped):**
[2:36] Hello everyone, this is Cartesian Caramel covering the Geometry node changes for Blender
[2:40] 5.2.
[2:41] This is a big update with many features, so let's get started.
[2:45] This release comes with a new physics system focusing on hair and cloth.
[2:49] Two new modifiers paired by the new XBPD Solver node have been added, cloth dynamics and
[2:54] hair dynamics.
[2:56] These are generalized systems that allow for custom forces.
[2:59] While they are still experimental, users are recommended to try them and give feedback
[3:03] for future releases.
[3:06] Bundles can now be attached to geometry, allowing for arbitrary data to be passed across
[3:10] modifier and object boundaries, using the new set geometry bundle and get geometry bundle
[3:15] nodes.
[3:16] And attached to geometry can be seen in the spreadsheet.
[3:20] Lists are new core data type that allows storing a sequence of arbitrary data and come with
[3:24] several new nodes.
[3:26] FilterList creates a new list by evaluating index dependent fields.
[3:30] ClosureTilist creates a new list by evaluating a closure that has an index input.
[3:35] List length outputs length of a list.
[3:37] GetListItem outputs an individual item.
[3:40] FilterList creates a new list if a bullion is true or false.
[3:43] ListSorts based on a custom weight.
[3:46] The new collection children node uses lists to output the child objects and collections
[3:51] of a given collection with an option for recursion.
[3:55] A new sound socket type has been added.
[3:57] This is used by the new sample sound frequencies node, which uses an imported sound to output
[4:02] the amplitude as a float.
[4:04] It can also sample frequency ranges, which allows for creating sound spectrum animations.
[4:10] And the objects can now have geometry nodes.
[4:12] This is useful for effects that don't require original data.
[4:16] And this also allows geometry nodes to be used on collection instances.
[4:20] The building blocks of the merge by distance node are now available individually as three
[4:25] new nodes.
[4:26] Merge points combines point or mesh vertices with the same group by D. Cluster by distance
[4:30] creates group IDs for close points.
[4:33] And cluster by connected creates group IDs for close vertices connected by edges.
[4:38] The new mesh bevel node has been added.
[4:40] It is similar to the bevel modifier and provides more detailed control.
[4:45] Attributes have three new nodes.
[4:47] Rename attribute allows renaming a single attribute or all attributes with a specific
[4:52] prefix.
[4:53] Get attribute names, outputs a list of the names of attributes in a geometry, optionally
[4:58] filtered by domain and data type.
[5:00] Transfer attribute can transfer an arbitrary number of attributes from one geometry to another.
[5:06] The capture attribute node now supports selection.
[5:09] This improves efficiency when an attribute value is only required by a subset of elements.
[5:14] Attributes can now be stored as 4D float vectors, though geometry nodes still only operates
[5:19] on 3D vectors.
[5:21] Curves have two new nodes.
[5:23] Set NURBS order controls how many curve points influence each evaluated point and set NURBS
[5:28] away controls the influence of each control point.
[5:32] Strings have four new nodes.
[5:34] Trim string removes specific characters at the star or end.
[5:37] Reverse string reverses the order of the characters.
[5:40] Split string splits text into a list based on a delimiter, and set string case turns
[5:45] strings into upper or lower case.
[5:47] The value to string and string to value nodes now have a base input which specifies the
[5:52] number system used when converting two and from integers.
[5:56] The find and string node can now find the first occurrence from the end.
[5:59] Trim fields are now supported, but keep in mind string attributes are not yet implemented.
[6:04] The default prey node group input can now be the scene frame or solve object.
[6:10] Six new bundle assets have been added.
[6:12] 3D to screen space transforms 3D coordinates from world to normalized camera space.
[6:18] Screen to 3D space is the inverse of this.
[6:21] Transform and project computes 2D coordinates in screen space.
[6:24] Connect with depth transforms coordinates from the viewport 3D space to screen space and back.
[6:30] Principal components analyzes a position vector field and geometry principal components
[6:35] analyzes on a specific input geometry.
[6:39] In miscellaneous updates, the new instance reference node outputs the internal attribute
[6:43] which shows what geometry set index each instance is referencing.
[6:47] The new get geometry component node extracts a single component of a geometry.
[6:52] The compare node now supports comparing data blocks.
[6:55] The bone info node now has an exists output and the viewer node can show data block names.
[7:01] Lastly, closures can now be called recursively up to a limit.
[7:05] A new call stack depth limit for geometry nodes can be configured in the user preferences.
[7:10] No tool inputs are remembered between operator invocations and can now be assigned in python.
[7:16] Internal fields are now de-duplicated for evaluation.
[7:19] This can speed up nodes are used multiple times like sample UV surface.
[7:24] Sampling nodes have improved performance when they can avoid conversions to the face corner
[7:28] domain.
[7:30] That was a lot of condensed information, but you should be able to learn it before the
[7:33] next release.
[7:34] I hope you all enjoyed this overview of the changes in additions to geometry nodes in Blender
[7:39] 5.2.


### Grease Pencil [7:40]
**Transcript (timestamped):**
[7:42] The improvements to grease pencil keep coming and for the long term release, some long-awaited
[7:47] features have finally made it in.
[7:49] Let's begin in draw mode where the most obvious changes are to brush and stroke handling.
[7:55] The thumbnails for brushes have been updated and when you enable online access after install,
[8:02] a text to brush pack becomes automatically available.
[8:06] Although you will have to download the brush locally before using it.
[8:10] This isn't a big issue.
[8:12] Just hover your cursor over the brush, you'll see this little download icon and by clicking
[8:17] on it, it will download and you're ready to draw.
[8:21] Before you even put stylus to tablet, you can set the stroke curve type.
[8:27] This is found under the stroke post-processing brush settings.
[8:32] The threshold sets a distance between the generated points, so this is really good for
[8:37] generating strokes with minimal information.
[8:41] The point handling becomes active once you're in edit mode.
[8:48] Improvements to alpha handling for dot and square line types mean that brushes like the
[8:53] airbrush look a lot better.
[8:57] Speaking of dot line types, a new placement feature now gives you control on how the dots
[9:03] are distributed along a stroke.
[9:07] These are editable at the material level and comprise of three ways dots can be distributed,
[9:13] count, radius and density.
[9:16] The difference is that count generates dots between points.
[9:21] Radius distributes the dots based on a percentage of the brush radius and density distributes
[9:28] the dots along the entire stroke.
[9:31] This is especially good for textured strokes.
[9:36] You can also now randomise some of the parameters such as size, strength and rotation at the
[9:42] material level.
[9:44] While base color and transparency controls for a material's stroke or fill still exist,
[9:50] these two settings can now be overridden in draw mode.
[9:54] You'll already be familiar with the color attribute setting, allowing you to choose from
[9:59] a color wheel or palette and completely override the material color.
[10:04] But you can now also switch between stroke, fill or both modes for a material on the
[10:11] go.
[10:13] This will speed up your workflow dramatically.
[10:17] The fill tool now has a new solver called Delaney, which generates geometry based on the boundaries
[10:24] it is trying to fill in.
[10:27] It can automatically detect gaps, so now you can fill those donuts with ease.
[10:33] You may have noticed that the eraser function is now gone from your brush settings.
[10:38] Now whatever your last eraser tool was set to is used.
[10:44] You can hold down control while drawing to toggle between draw and erase.
[10:51] The line art tool now supports fills.
[10:55] Now admittedly this is best for more primitive objects or plain art faces.
[11:01] Finally there are some minor but useful functions to improve your workflow.
[11:06] In edit mode, Shift L now deselect strokes that are completely selected.
[11:12] The Move to Layer function now shows any groups and sublayers.
[11:20] And vertex mode color attribute replacement now has blend modes.
[11:26] And stroke mode is also available allowing you to affect just the strokes, fills or both.


### Animation & Rigging [11:34]
**Transcript (timestamped):**
[11:35] I'm Wayne Dixon from CGCookie and the next couple of minutes I'm going to inform you about
[11:38] the rigging and the animation updates in this release.
[11:40] There's some nice quality of life improvements including some that let me sneak in there.
[11:44] Let's go.
[11:45] When spawning bones with shift A you now have more options for your new bone.
[11:49] Just open up the redo panel and you can see it's actually useful.
[11:52] Previously all you could do was set the bone name.
[11:55] Now you can disable the deform option that's perfect for control bones.
[11:59] You can also set the bones length.
[12:01] That's awesome.
[12:02] And the B bone size also scales with this length value.
[12:06] So you won't get any nasty surprises.
[12:07] We'll see that in a moment.
[12:09] Plus you also have options for the coordinate space that's going to spawn in.
[12:13] That's either going to be world space or object space.
[12:15] But most of the time they should be exactly the same.
[12:18] But here's the big awesome stuff.
[12:19] In the alignment you have some very useful settings.
[12:22] The default alignment is object up.
[12:24] Just as it's always been.
[12:26] But you can now align it to the cursor or the viewport.
[12:28] But the best addition by far is for those of you like myself who'd like to world align
[12:33] your control bones.
[12:35] Just choose object axes and boom.
[12:38] Look at that.
[12:38] World align controls in a single step.
[12:41] What are you going to do with all the time you're going to save?
[12:44] And because the spawn bone length is now linked to the B bone size,
[12:47] there's no surprises when you jump over into B bone mode.
[12:51] No more of this.
[12:52] It's now easier to copy object constraints from one object to another
[12:57] as it's been added to the control L menu.
[13:00] What do you reckon of that Suzanne?
[13:02] Is that easier?
[13:03] The Suzanne say yes.
[13:05] When parenting an object to a bone, there's now a new sliner that will let you set the position along that bone.
[13:10] It will default to the tail, which might seem like an odd choice,
[13:13] but this is for backwards compatibility and it's currently going to work exactly the same as it used to.
[13:18] But now you can position that object anywhere along the bone length.
[13:21] And before you ask, no, it doesn't include the bendy bone position.
[13:25] It's just that straight bone.
[13:27] There is a new duplicate and rename operator, which is up here in the armature menu.
[13:31] This will let you duplicate the selected bones and rename them in a single operation.
[13:36] Here I want to duplicate these bones to become control bones.
[13:39] So I can use this to find the DEF and replace it with nothing.
[13:43] Ta-da.
[13:44] This search and rename happens before the name collision is detected.
[13:48] So this is one way of avoiding the .001 in a lot of situations.
[13:53] The Auto-IK feature used to stop when it found a disconnected parent will not anymore.
[13:58] It can now follow the hierarchy, even if that parent has been emancipated.
[14:02] The old motion paths used to create a jagged line when you were adjusting that with the auto update enabled,
[14:08] which kind of made it look broken.
[14:10] This is now being cleaned up.
[14:12] It still can't fix your bad animation.
[14:14] That's on you.
[14:15] The dope sheet has a new operator called Select Keyframes by type.
[14:19] You can find it in the Select menu or by searching with the F3.
[14:22] And don't forget, you can also open up the redo panel to edit that operation.
[14:26] This will open up more workflows as you'll be able to easily select those keyframes without spam
[14:31] clicking.
[14:32] It's now possible to select all the markers to the left and the right of the playhead
[14:36] by control clicking in the marker area.
[14:38] Just control click on an empty space either side of the playhead and that's going to select all
[14:43] the markers on that side.
[14:44] You can hold Shift to extend that selection.
[14:47] Plus, you can still select the camera and the marker by control clicking on that camera marker.
[14:51] So click on the space to select all.
[14:53] Click on the markers to select the markers.
[14:56] Objects now have access to the breakdown animation tools.
[14:59] This will make some things much easier to animate.
[15:02] Objects still don't have access to all the animation tools like armatures do,
[15:05] but now they're not so much like second class citizens.
[15:08] There's a nice improvement to the parent child selection tool with this square brackets
[15:12] in the old versions of blender.
[15:13] It would only work on the active bone.
[15:16] Now in 5.2 it works on all the selected loans.
[15:19] Isn't that nice?
[15:20] There are now more options for how you want the animation to play back or loop when you start the playback.
[15:26] The default is infinite.
[15:27] That's how it's always been.
[15:29] But now you can play it once and have it returned to where it was to the end of the animation
[15:33] or to the start.
[15:34] You can even make it ping pong, which is called bounce.
[15:37] That way you can make it feel like you're undoing all those bad life choices.
[15:40] You.
[15:42] Another playback option is the allow pre-roll.
[15:46] By default when you start the animation before the start frame it will snap to the start
[15:50] and then start playing.
[15:52] When you allow pre-roll it's going to start from where the playhead is.
[15:55] But note this will not override the allow negative frames option.
[16:00] Speaking of the allow negative frames this has moved to a sub panel in the user preferences
[16:05] and it now shows a warning.
[16:06] Nothing technically has changed other than now it has a better explanation.
[16:10] I'm telling you why it isn't enabled by default.
[16:13] But I like living on the edge.
[16:15] So I'm just going to check that one.
[16:16] Yeah.
[16:17] Finally we have a way to master-lead F-curve modifiers.
[16:21] There it is right under the add F-curve modifiers.
[16:24] You can remove all, remove a specific type,
[16:27] or remove the first one on each of the selected curves.
[16:30] I know this is going to make a lot of people happy because of the many hours they've spent
[16:35] manually deleting these F-curve modifiers.
[16:38] And everyone else will be like hey wasn't that there already?
[16:41] No.
[16:42] No it wasn't.
[16:43] Now it is.
[16:44] It's now easier than ever to isolate your curves by control clicking on the iBall icon.
[16:49] This makes it much faster to show what you want to see and hide what you don't.
[16:54] But that's not all.
[16:54] The graph editor now has a local view just like the 3D viewport.
[16:58] You can press slash to jump into local view for your selected curves.
[17:02] You'll see it say local view up in the corner.
[17:04] And to jump out of local view just press slash again.
[17:08] The pose library has some added improvements.
[17:10] Previously when applying a pose that had a different rotation order,
[17:14] say it was stored in Quaternion and then applied to your current file that was set to Euler.
[17:18] This would result in missing data or the wrong orientations.
[17:21] Now blender will do some magic conversions to try and correct for that.
[17:26] When going from Quaternion or access angle to an Euler,
[17:29] blender will find the closest Euler angle that's going to match and use that.
[17:33] When going from an Euler to a Quaternion or an access angle,
[17:36] it's going to assume that the asset was saved in Euler XYZ
[17:40] because there isn't actually a way of knowing if that's true or not.
[17:43] And then if you're going from an Euler to an Euler,
[17:46] this will just assume that it was saved in the same rotation order.
[17:49] Because as I previously said, there's actually no way that blender can know.
[17:53] So that's not all of them, but that's the main ones.
[17:55] Hopefully this improves your workflow. See you.


### Rendering [17:57]
**Transcript (timestamped):**
[17:59] The principal BSDF got a new thin wall checkbox,
[18:02] which while it might be a small option is a big deal.
[18:05] It allows you to properly render thin translucency within the material
[18:08] like light shining through leaves.
[18:10] And for glass, it removes the refraction, which can significantly speed up render times
[18:14] and cut down on noise for light coming through windows.
[18:17] A scene time node was also added, matching the one in geometry nodes.
[18:21] There's also input nodes for Boolean, Integer, and Vector values.
[18:24] Color spaces are now organized into menus,
[18:27] and there are new ones for reverse transforming Apple, RE,
[18:30] Blackmagic, Canon, and Sony cameras back into linear space.
[18:34] So you can more easily import your footage into blender
[18:36] and have everything work all together.
[18:38] You can also use Adobe RGB or the various options for wide gamut textures.
[18:43] You can now uncheck the render output for cases where you want to save
[18:46] with the file output node in the compositor instead of from the output panel.
[18:51] Light and shadow linking setups can now be copied from one object to another.
[18:55] For orthographic cameras, the orthographic scale can now be adjusted directly
[18:59] in the 3D view with a widget.
[19:01] Images dragged and dropped into world shaders are now assumed to be environment textures.
[19:06] The AOV output node, which links custom shader data with the compositor,
[19:11] now shows all available AOVs so you don't have to type in the names manually.


### EEVEE [19:15]
**Transcript (timestamped):**
[19:15] Blender's real-time render engine got a handful of great updates in this release.
[19:19] The main one is that screen space ray tracing was overhauled,
[19:23] and the resulting renders are much improved in the details.
[19:25] The highlights include better contact reflections, smoother denoising,
[19:29] significantly more accurate ambient occlusion, and reduced light leaks.
[19:33] There's a new back face slider option that allows you to control whether the
[19:36] screen space global illumination is single-sided, double-sided, or anywhere in between.
[19:41] The 5.1 behavior would be turning this off completely,
[19:44] but it looks much better with it on.
[19:46] The performance section now has an anisotropic filtering option,
[19:49] which is basically a control for how good your textures look at extreme angles.
[19:53] Lights can now be seen directly in the camera if you enable camera ray visibility.
[19:57] In that same panel, you can also control which objects are visible to raycast shader nodes.
[20:02] Scenes with a lot of instancing can now render up to twice as fast.
[20:06] Let me double-check that. Yep, twice as fast.
[20:08] Shadow pools up to two gigs are now supported for scenes with lots of detailed lights.
[20:13] The limit of eight attributes per material was removed.
[20:16] Reflection planes are now compatible with refraction, blended transparent materials,
[20:20] and the shader to RGB node.
[20:22] EVs' principal BSDF shader now supports the clear-coat layer normal,
[20:26] and the normal map node base option, which was recently added to cycles for improving
[20:31] normals on top of displacement, is now available in EV as well.
[20:35] There were also tons of bug fixes in this release that removed various small artifacts from edge cases,
[20:40] and the result is just much more clean and stable renders overall.
[20:44] For cycles, the realistic path tracer, the biggest new feature is texture caching.


### Cycles [20:45]
**Transcript (timestamped):**
[20:49] Generating a texture cache, which is like a set of variable-sized textures that cycles can
[20:54] choose from, depending on how big the texture appears in that specific render,
[20:57] can allow for huge memory savings for scenes with large textures.
[21:01] In the Simplify panel, you can reduce the texture resolution in the viewport to keep it interactive,
[21:06] even if your textures are way too big.
[21:08] The Raycast node can now sample custom attributes, like those from Geometry Nodes,
[21:12] wherever the rays hit, though this is just in cycles for now.
[21:15] Sub-surface scattering scale and anacetropy have been tweaked a bit,
[21:19] so their values better match other renders, so you can share textures between them.
[21:23] And last but not least, you can now ban shadows from the world.


### Compositing [21:27]
**Transcript (timestamped):**
[21:27] Hi, this is Momo from the YouTube channel MomoPTFR, and I'm titling feature Simplify
[21:33] in the video, is that the interactive or traditional compositor now supports animation playback.
[21:40] This means we can finally play image sequences and videos in the compositor,
[21:45] and also animate nodes with keyframes while having the ability to preview the outcome.
[21:50] And also, the compositor will now use the GPU by default instead of the CPU,
[21:56] which gives a huge performance boost without having to set it up manually.
[22:01] Another advantage of the interactive compositor has always been the gizmos for certain nodes,
[22:07] like the ellipse and boxmask.
[22:09] In Blender 5.2, these aren't exclusive to the compositor's backdrop anymore,
[22:15] but can now be viewed and controlled in Blender's image editor.
[22:19] To make sure this feature works like expected,
[22:22] node gizmos will now also be affected by transform offsets.
[22:26] And on top of that, the node gizmos can now also be animated by using the auto-king feature of Blender,
[22:32] which means keyframes will be created automatically when you use the gizmos.
[22:38] But let's move on to some of the new nodes.
[22:41] For example, the new blank image node allows you to create a color solid,
[22:45] in a definable resolution. This might not sound like much at first,
[22:50] but it's actually a game-changer.
[22:51] For example, if you would just use the off-over node to add a backdrop by changing the color of the
[22:57] background input, the result would automatically be clipped to the image input you use as the foreground.
[23:04] But by using the new blank image node, you can avoid this clipping behavior and just transform
[23:10] your foreground image without having to worry about clipping.
[23:14] But there's also another pretty cool use case, which is creating a kernel for Blender's
[23:19] convolve node. For example, you can use the image coordinates of a low resolution blank image
[23:25] for procedural textures and then use that low resolution texture as a kernel to create something
[23:31] like camera landsblur. Let's move to one of the biggest changes of the compositor,
[23:38] which is the addition of multiple new input socket types you might already know from geometry nodes
[23:45] like integer vectors, matrices, transforms and much more.
[23:51] Especially useful is that you're able to add object and camera data to the compositor.
[23:56] To add them, you can also just drag and drop the objects from the outliner into the compositor.
[24:03] I want to show you a feature that has been anticipated for a long time.
[24:07] I'm talking about the ability to add text elements right within the compositor.
[24:12] Like you can just define the font, the text alignment and the wrapping, type in some text
[24:18] and you have your text element. And this is also where another of the new input
[24:23] socket comes into play, which is the string input. By using this new input type and the related
[24:30] utility nodes, you can already create a few effects like this typewriter effect I've created.
[24:37] The only thing missing currently is being able to transform individual text characters,
[24:42] but you could already work around that by just using multiple string to image nodes.
[24:48] And another exciting addition to the compositor are a few new preset assets for the compositor,
[24:54] including the long rated film grain effect. It comes with some presets you can choose from by
[25:00] using the menus to keep the inputs at a minimum. But if you want further control, you can also
[25:06] add everything to custom, which will expand several inputs for you to adjust.
[25:11] Next we have blenders new Divering node group, which will reduce the amount of different colors
[25:16] of its input and then use patterns to blend between the limited colors. So basically you can
[25:23] think of it as a pixel art filter. Again, you can use a menu to choose between different Divering
[25:29] patterns, including multiple buyer Divering patterns, which is usually the most popular pattern for
[25:36] Divering. But we also got a few more complex node groups that utilize the different render
[25:42] passes of blender to create 3D post processing effects. For example, the new depth atmosphere,
[25:49] which lets you use a Randers mist or depth pass to add fork to your scene. Just keep in mind that
[25:56] the real time compositor of blender, which works directly in the 3D viewport, only supports using
[26:02] different render passes when using EV. If you're using cycles, you'd have to render the image
[26:08] once and then use the effect in the interactive compositor. This also applies to the new paint filter.
[26:16] Well, at least when deciding to use its tracking feature, if you disable the tracking feature,
[26:22] you just have a sample to D paint effect. But when enabling the tracking and using the depth
[26:28] and position render passes, the paint effect will be applied with depth, which makes it easier
[26:34] to keep different objects in your scene apart. Again, you can choose between different presets here,
[26:40] like watercolor and oil paint, and also adjust a paper texture overlay. Another effect,
[26:46] which you can use both in a 2D and a 3D version, is the Night Vision node group. As the name suggests,
[26:53] it will add this popular green Night Vision effect to your footage. We also got a few new node
[27:00] groups that already make use of the new inputs and nodes of blender 5.2. By using these, you can
[27:08] generate texture coordinates from the camera in your 3D viewport, which means you can create a
[27:15] procedural background in the compositor and make it automatically adjust itself to the position
[27:21] and rotation of the camera. The VSE also got some pretty cool new features to strengthen
[27:27] its integration of the compositor. For starters, the VSE will now use the GPU for compositing,
[27:34] which again gives a huge performance boost. And compositing node groups and assets can now
[27:41] instantly be added as a modifier on a VSE strip. There are just two conditions the compositor
[27:48] assets have to meet. The first input of the node group has to be the image input,
[27:55] and the dot blend file of the assets has to be saved in blender 5.2. For my own compositing
[28:02] pack and become, I've made sure to update all nodes to have the image input at the top for
[28:08] this exact reason in the latest update of it. This new integration of compositing modifiers
[28:14] and the VSE also allows us to easily add transitions to clips. For example, by using one of the
[28:22] transitions from a pack, you just add the modifier to the first clip, place the clip into transition
[28:29] to be load in the timeline, and then select it as a mask in the compositor modifier.
[28:36] Apart from the new input types, you can also use a default input type now. This basically
[28:43] enables you to create a node group with an input for the animation time, which if the user doesn't
[28:50] connect anything to, will automatically use the scene time. So essentially, you can make an input
[28:58] entirely optional now. We also got the warning node in the compositor node, which you can use
[29:05] to display error messages or warnings if a certain condition is met. And to create even better
[29:12] performing node setups, you can now see the total processing time of the compositor when enabling
[29:18] the timings overlay right above the group output node. Let's get to some of the smaller but
[29:25] cool new features and changes. For example, when using the grease pencil in EV, you now get the correct
[29:32] depth of the grease pencil object in the render's depth pass. Previously, grease pencil objects
[29:38] have just been ignored by it. So again, a feature that increases the 2.5D capabilities of
[29:46] Blender and its compositor. When using the transform node in Blender's compositor to scale
[29:52] something down, you can now also set it to use the anisotropic interpolation, which gives a lot
[29:58] smoother looking result. And last but not least, the stabilized 2D node, which is used to apply
[30:06] tracked stabilization to your footage, now received a frame input. This allows you to alter
[30:14] the timing of the stabilization, which can come in handy when using fast forward or pausing effects
[30:21] for footage in the compositor. So the stabilization stays in sync. Well, these were all the new
[30:28] features of Blender 5.2 for the compositor. I sure think it's very exciting.


### Video Editing [30:34]
**Transcript (timestamped):**
[30:34] In the video sequence editor, frame pre-fetching now fetches a few frames before the playhead
[30:39] to make scrubbing backwards a little bit smoother. Footage playback is now significantly faster,
[30:43] for those who are still using OpenGL. Extra timecode files are no longer needed when building or
[30:48] using proxies, so there's now less bloat in your file browser. Text, strips, now support custom
[30:54] line spacing, and have style presets that you can customize. Solid color strips can now have
[30:59] exact pixel dimensions. And speaking of strips, the thumbnails are now shown only at the start and
[31:05] end for better performance, but you can change it to display across the whole strip if you'd like.
[31:10] You can now select specific view layers for scene strips and change the viewport shading for
[31:14] all of them at once. The color scopes now fully support HDR and wide gamut color spaces,
[31:19] which is also now true in the image editor. The preview area can now show composition guides.
[31:25] There's a new optional scrubbing region that can be added to the playback controls footer.
[31:29] Strip image origins now have more snapping options.
[31:33] Importing videos now supports an unlimited number of video and audio channels.
[31:38] In the motion tracking department, masks have a new move to layer operator that has the hotkey
[31:42] M by default, just like moving to collections in the 3D view. Plus masks are now rendered about
[31:48] 10% faster. Blender in virtual reality using the built-in VR scene inspection add-on has a new feature


### Virtual Reality [31:50]
**Transcript (timestamped):**
[31:55] location scouting, which gives you a camera with all the proper camera controls, which you can
[31:59] use to plan out angles and shots. So you can now scan a live film location and spend as much time
[32:04] as you want later planning out exactly how it should be shot without having to actually be there.
[32:09] Not quite teleportation, but the next best thing.


### Assets & Pipeline [32:12]
**Transcript (timestamped):**
[32:13] Blender now natively supports online asset libraries. If you allow online connections,
[32:18] which by the way is always disabled by default for privacy and security, you'll see that the
[32:22] essentials library that comes with Blender is much larger now. You get new base meshes,
[32:27] compositing setups, and helpful geometry node groups, as well as the high res versions of the
[32:31] viewport HDRIs. Top level categories named compositing or geometry nodes are now ignored in the
[32:36] node menus, making organization a lot easier. You can now specify a preferred import method per asset.
[32:43] Asset libraries now have their own page in the preferences editor, and the built-in essentials
[32:47] is now in that list. The time it takes Blender to write 16-bit EXR images has been cut in half.
[32:54] There's a new option in the right-click context menu for render dimensions to swap the X and Y.
[32:59] Stereoscopic and panoramic metadata is now written for movies, so you can upload these types of
[33:03] renders straight to YouTube or any other platform without having to pass them through any other
[33:08] software. For importing and exporting, the color spaces are now respected when importing USD files,
[33:13] and there's a new USD export option for how frequently to flush the data, so you can reduce memory
[33:18] usage. The GLTF file format got a huge number of improvements as usual from general fixes and
[33:23] performance enhancements to support for point clouds, iridescence and dispersion materials,
[33:28] and KHR primitives which can be used for gaujin splats.
[33:31] Alembic imports now respect animated object visibility, F curves for camera data, and subdivision
[33:37] surface data. During STL export you can now choose whether the new file follows the viewport or
[33:42] the render settings of the modifiers, similar to how you can with the other formats.


### User Interface [33:47]
**Transcript (timestamped):**
[33:47] The Outliner now automatically scrolls to the active object by default, which is amazing,
[33:52] but you can turn this off if you want to. In the reorganized drop-down menu here that no longer
[33:57] has the filter icon. Shape keys are now listed in the Outliner. Aligned editor edges no longer
[34:03] snapped together by default because they could get annoyingly stuck together, but you can still
[34:07] move them together by holding SHIFT. Nested lists like those for bone collections now have auto
[34:13] scroll for dragging and dropping. You can also reverse the sorting of these lists, invert the search
[34:17] filtering, use the arrow keys to navigate, and use the number pad period to jump to selected.
[34:22] This all also works in the asset shelf. There's a new filled filtering icon that's used wherever
[34:27] filtering is active, and there are new download icons to go with the new online assets system.
[34:32] The set parent menu control P now has icons for the parenting types. Sidebar tabs have a
[34:37] compact view option now, which supports showing an icon, though that's not used anywhere in Blender
[34:43] right now, so it's not too useful as of yet. But you can also now switch between tabs with clicking
[34:48] and dragging like other areas of Blender. There's a new text box input type that allows multi-line
[34:52] text inputs. Long menus and popovers can now be panned using the middle mouse button,
[34:57] and some popovers now have sub-panels that can be collapsed. Hexadecimal values can now be
[35:01] copy and pasted directly into color inputs. You don't even have to open it up, just control V.
[35:06] Number inputs no longer have the unit as part of the text, and instead it's just rendered as a hint,
[35:11] so it won't get in the way while you're typing. For developers with developer extras enabled,
[35:15] hovering over icons now gives you the icons ID name. For users with mice with lots of buttons,
[35:21] mouse button 4 is now zoomed to selected by default. For users with Apple's magic mouse,
[35:26] why? Over in the node editor, you can now change properties for multiple node group inputs by
[35:30] holding alt. Grouping and ungrouping in node editors now avoids creating duplicate outputs and is
[35:36] better at guessing input and output socket types. Ungrouping now adds constants as the previous inputs,
[35:41] so that all the data is saved when you ungroup. Linked groups removed to a sub menu in the add menu,
[35:46] so they don't crowd out your groups from the current file. And this menu no longer shows linked
[35:50] groups that are only used as subgroups, so it just shows the top level groups. Multiple nodes can
[35:56] now be resized at the same time. The plus button to add a new socket is now used on all nodes that
[36:02] support dynamic numbers of sockets. You can also rename group inputs by control clicking on the node
[36:07] itself. There are new type conversion nodes for forcing sockets to be a specific data type.
[36:13] Vector input nodes now support 2D and 4D vectors and menus got their own input node as well.
[36:18] Floats, integers and vectors now all support the pixel subtype. There is now a theme brightness
[36:24] slider for the 3D views access colors and the theme editor was reorganized a bit overall.
[36:29] And last but not least, Blender on Mac has a very slick new icon that I will definitely be
[36:33] ripping to use on Linux, but on Mac it also automatically supports the transparent liquid glass
[36:38] styles as well. That, along with hundreds of bug fixes, is what's new in Blender 5.2 LTS.


### Conclusion [36:40]
**Transcript (timestamped):**
[36:44] You can download it today from Blender.org and don't forget to support the development
[36:48] fund while you're there to help make future updates even better. Thank you guys so much for
[36:52] watching, have a great rest of your day and as always happy blending.



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
