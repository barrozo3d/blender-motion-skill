---
title: This technique lets you make Hard Surface models easily
source: YouTube
url: https://www.youtube.com/watch?v=_6uBdIsvm7c
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Extra Objects add-on, Multires sculpt workflow, consistent with Blender 3.x-5.x"
tags: [displacement, procedural, materials, organic, advanced]
extraction_status: complete
frames_dir: tutorials/frames/this-technique-lets-you-make-hard-surface-models-easily/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# This technique lets you make Hard Surface models easily

**Source:** [YouTube](https://www.youtube.com/watch?v=_6uBdIsvm7c)
**Author:** Blender Secrets
**Duration:** 9m21s | 21 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Hard Surface Course update [0:00]
**Transcript (timestamped):**
[0:00] I recently added a new lesson to my hard surface sculpting course and I want to share
[0:05] it here as a preview for anyone curious in that course.
[0:08] The alpha brushes that you see used in the video are included with the course as well
[0:12] as the blend file.
[0:13] One thing you'll notice is that there's not a lot of sculpting in this video.


### What are we making? [0:17]
**Transcript (timestamped):**
[0:17] This video is more about making a sculpting tool.
[0:19] Specifically, we're making a tiling displacement map, which can be a really fun tool to use
[0:23] to quickly generate some concepts in 3D.
[0:26] It's not the only method for making this kind of tiling map and the course explores
[0:29] another technique as well, but this one is pretty easy.
[0:32] For the occasion of this small update, I'm running a short discount just for the weekend,


### Paying the bills [0:33]
**Transcript (timestamped):**
[0:37] so if you're curious about this course and you want to get it, now is a good time.
[0:40] So go to 3dcquests.com if you want to learn more.
[0:43] So here I'm in a fresh scene and I'm just going to switch to the top orthographic view


### Start of the tutorial [0:45]
**Transcript (timestamped):**
[0:48] and I'm going to add a grid.
[0:50] A grid is basically the same as a plane except it already has some subdivisions and I'm going
[0:54] to set it a couple more times.
[0:56] Just so that we have enough geometry.
[0:58] I just want to make sure that the unit scale is 1 and that the scale of the grid is 1 so
[1:03] that there are no surprises later with the scale or anything like that.
[1:07] So let's add a camera and we're going to set this camera to orthographic.


### Setting up the Camera [1:08]
**Transcript (timestamped):**
[1:11] But first let's move it up on the z-axis.
[1:13] It doesn't really matter how high with an orthographic camera, but just set it to orthographic
[1:18] and then set the orthographic scale to 1.5 and I'll explain in a minute why that is.
[1:23] Now let's set the resolution to a square format.
[1:25] So 1080 by 1080 for example.
[1:28] As long as it's square it's all fine.
[1:30] And let's switch by pressing 0 to the camera view and I'm just going to choose a matte
[1:34] cap real quick and turn on the cavity and it's a bit easier to see the depth.
[1:39] Now in sculpt mode I've got my brushes here and these are the brushes from the course


### Using Alpha brushes to add detail [1:44]
**Transcript (timestamped):**
[1:44] and now I can just start dragging them on the surface but as you can see the resolution
[1:48] is much too low.
[1:50] So I'm going to add a militarized modifier.
[1:52] Now it's good that we already have some geometry subdivisions and now if I certified it linearly
[1:58] a few times then it's just easier for the computer to handle all those subdivisions.
[2:03] If we just added a sub-diff modifier to a plane with no geometry subdivisions then it
[2:08] would take a lot more subdivisions and would be heavier for the computer.


### How many Faces do you need? [2:12]
**Transcript (timestamped):**
[2:12] So I have it up to about a million and a half faces, a little bit more, five subdivisions
[2:18] and as you can see now the alphas look nice and crisp.
[2:22] So if they're blurry you basically just don't have enough resolution.


### Tiling Symmetry [2:25]
**Transcript (timestamped):**
[2:25] I want to have tiling symmetry so X and Y tiling that's what we have to turn on and
[2:30] then we're going to set the tile offset X and Y to the same value as the scale of the
[2:35] orthographic camera and that way it's tiling exactly along the borders of the camera but
[2:40] as you can see the alpha doesn't look particularly good.


### Fixing Potential Brush issue [2:43]
**Transcript (timestamped):**
[2:44] It has a radial shape so how do we solve this problem?
[2:48] So let's go to the brush because that's actually a brush setting.
[2:51] We just have to set it to view plane as you can see now it looks fine and so it's really
[2:57] important that the tile offsets and the orthographic camera scale are the same value that way it
[3:02] maps perfectly as you can see.
[3:04] So everywhere we drag the alpha it shows up on the other side as well and unfortunately
[3:09] we have to change for every brush that we use we have to change it to view plane the
[3:14] first time we use it.


### Adding details [3:15]
**Transcript (timestamped):**
[3:15] So now I can just start really quickly adding some detail just have to remember to keep setting
[3:21] it to view plane and no matter where we drag it it will arrive on the other side and it
[3:27] will tile perfectly once we bake it to a displacement map.
[3:31] So I'm just having some fun adding some detail and this one is a negative brush so I have
[3:35] to hold control and so I'm quickly going to add some more detail this way.
[3:39] And of course with control F we can rotate the brush with F we change the radius and
[3:44] with shift F we change the strength but I recommend with alpha brushes that you set
[3:49] the strength always to one to have the correct shape of the alpha.
[3:53] And of course you don't have to stick just to alpha brushes you can also just model geometry


### Where did my details go? [3:58]
**Transcript (timestamped):**
[3:58] and now when we switch to object mode we can't see the detail and that's because we have
[4:02] to increase the viewport levels on the motorized modifier.
[4:05] Now I'm just going to add a single third from the extra objects addon that you have to install


### Adding a Single Vertex and Extruding [4:07]
**Transcript (timestamped):**
[4:11] in extensions and I'm just extruding that vertex and I'm just creating some shapes real
[4:17] quick by just extruding that and it is perfectly on the surface of the grid.
[4:22] It's important that there is no undercut on the curves that I'm going to create from


### Adding Array modifiers for X,Y tiling [4:26]
**Transcript (timestamped):**
[4:27] this and I'm just going to add an array to this extruded vertex and let's set it to constant
[4:32] offset and then again use that value of one and a half on the x axis and then we duplicate
[4:38] it and then we set the negative version of the x value and then we duplicate it again
[4:43] and we repeat that for the y axis.
[4:46] So set y to 1.5 and then another one minus 1.5 on the y axis.
[4:56] So now we have a tiling extruded vertex and we can extrude it and it will appear on the
[5:02] other side as well.
[5:03] And let's quickly set this grid to be non-selectable otherwise we keep accidentally selecting it.
[5:11] And let's turn on on cage so that we can select it everywhere in all the arrays and we can


### Turn on On Cage to edit the Array anywhere [5:12]
**Transcript (timestamped):**
[5:17] just take one vertex and shift t and duplicate it and we just have to make sure that when
[5:22] we exit on one side of the axis we appear on the other side that we just continue it
[5:27] until it goes inside of some extruded alpha shape or something else.
[5:33] So now that I've finished doing that I will convert it to a curve and then we can easily
[5:37] give them all some thickness.
[5:40] So now we can start the shape and then we just undo that and let's select some of these


### Beveling Vertices for nice round corners [5:42]
**Transcript (timestamped):**
[5:44] corner vertices and then we can just bevel them to make them all a bit smoother.
[5:49] So shift control B to bevel these vertices.
[5:52] Then when we convert it to a curve it will have a nice round shape.
[5:56] So when you press shift control and B to bevel these vertices you will be able to scroll
[6:00] the mouse wheel up or down to increase or decrease the amount of vertices.
[6:06] And if you want you can also change the profile but in this case the default is fine.
[6:11] So that looks a bit smoother so let's convert it again to a curve and then again give it


### Convert to Curves, add thickness [6:13]
**Transcript (timestamped):**
[6:16] some depth in the bevel settings here.
[6:19] So then I converted this all to mesh and then I selected everything in edit mode and merged
[6:25] by distance and as you can see that removed a lot of vertices and then I was able to edit
[6:29] the shape with proportional editing.
[6:32] I just wanted to make sure that these pipes don't really overlap each other and just adjust
[6:37] their thickness a bit as well with alt S.
[6:40] So you can select one particular piece with L in edit mode and then alt S to scale it
[6:45] up or down.
[6:46] You just have to make sure that you also do that on the other side.
[6:51] So if it shows up somewhere else in the map then you need to make sure that it's scaled
[6:55] equally.
[6:56] So here I have a test file for detailing displacement and as you can see it tiles very


### Testing the baked displacement map [6:57]
**Transcript (timestamped):**
[7:01] nicely but there is one little problem and that is here things don't match up and that
[7:06] is simply because I was messing up those pipes with proportional editing and let me just show
[7:13] you how you can fix that.
[7:14] You can see it here this is the same problem that is repeated and let me just quickly show
[7:19] you how to solve that.


### How to fix inconsistencies [7:21]
**Transcript (timestamped):**
[7:21] So here we are back in the file and yeah it is basically just this area here that doesn't
[7:28] match up.
[7:29] Here you can see it doesn't even go all the way to the edge.
[7:31] It's pretty easy to solve that.
[7:32] First of all I am just going to take this and I just go to wireframe mode and I am just
[7:39] going to add in x-ray mode.
[7:40] I am just going to make sure this goes all the way till there and then I am just going
[7:44] to take these, select these and just delete them.
[7:49] So I am just going to select these.
[7:50] These are the ones that I edited with proportional editing and I am just going to duplicate them
[7:55] with shift D and just right click to cancel and then transformation.
[8:00] And change it to shift C and Y to move them minus to move them down in the minus y direction.
[8:06] And can you think of the value that I should type on an iPad to move them?
[8:10] Is it one unit, two units?
[8:14] It's one and a half.
[8:15] It's the same value as the camera scale and everything else 1.5.
[8:20] And then it should match up perfectly now so let me just quickly go ahead and bake that


### Result of the bake [8:25]
**Transcript (timestamped):**
[8:25] and I will show you the results.
[8:27] Well, you can see the problem is now completely solved by replacing that texture.
[8:31] And so now we can just tile this as many times as we want.
[8:35] And one more thing before you bake is these things that are looking quite segmented, they


### Use Flat Shading, not Smooth shading (before you bake) [8:36]
**Transcript (timestamped):**
[8:41] will also render that way in the displacement map, even if you set it to shade smooth.
[8:47] So it's important to check.
[8:50] And if necessary, just add a sub-diff modifier.
[8:52] So I'm just pressing Ctrl 2 in this case to add two levels.
[8:56] And then when I bake this, the map will look nice, otherwise you will see those flat faces
[9:02] in the bake.
[9:03] So this concludes making the geometry for the displacement map.


### Conclusion [9:05]
**Transcript (timestamped):**
[9:06] And next we'll bake it with a simple gradient material, and then we can actually use it
[9:10] like in this example here.
[9:12] So if you're curious to learn more about this course and its unique workflow, now is a good
[9:16] time with this discount.
[9:17] So check that out on 3dsecrets.com.



---

## Captured Frames

- [0:56] tutorials/frames/this-technique-lets-you-make-hard-surface-models-easily/frame_000.jpg
- [1:34] tutorials/frames/this-technique-lets-you-make-hard-surface-models-easily/frame_001.jpg
- [2:18] tutorials/frames/this-technique-lets-you-make-hard-surface-models-easily/frame_002.jpg
- [2:51] tutorials/frames/this-technique-lets-you-make-hard-surface-models-easily/frame_003.jpg
- [4:32] tutorials/frames/this-technique-lets-you-make-hard-surface-models-easily/frame_004.jpg
- [5:52] tutorials/frames/this-technique-lets-you-make-hard-surface-models-easily/frame_005.jpg
- [7:06] tutorials/frames/this-technique-lets-you-make-hard-surface-models-easily/frame_006.jpg
- [8:52] tutorials/frames/this-technique-lets-you-make-hard-surface-models-easily/frame_007.jpg

---

## Structured Notes

### Core Technique
Building a custom **tiling hard-surface displacement map** from scratch: a subdivided grid is detailed with alpha brushes (using a Multiresolution modifier and the sculpt brush's "View Plane" mapping mode so strokes tile seamlessly across the camera's exact orthographic frame) combined with hand-modeled extruded/curve-based pipe details built with an X/Y Array modifier for guaranteed edge-to-edge tiling, then flat-shaded and baked into a real, tileable displacement texture usable on any hard-surface model. Framed as a preview lesson from the author's paid Hard Surface Sculpting course.

### Summary
Frame 000 shows the base geometry setup: a Top Orthographic view of a subdivided square Grid with all vertices selected and a right-click Vertex context menu open (LoopTools, Extrude Vertices, Bevel Vertices, Merge Vertices, etc.) — the starting canvas before any detail work. Frame 001 shows the camera framing step: an orthographic camera view of the same square grid from directly above, matched exactly to its boundary, with render Output settings (File Format, Color Depth, resolution fields) visible in the sidebar — confirming the "bake target" framing setup. Frame 002 shows Sculpt Mode active on the now heavily-subdivided plane (Multires modifier, Levels Viewport/Render, Sculpt Base Mesh) with an alpha-brush thumbnail strip along the bottom — a plain pink/red canvas ready for stamping. Frame 003 shows the "View Plane" brush-texture-mapping fix being applied: the Texture Mapping panel (Offset, Size, Angle, Include/Vector Displacement fields) open with a faint square-tile boundary visible on the still-blank canvas. Frame 004 shows the payoff: a fully alpha-stamped tile densely packed with varied mechanical shapes (bolts, hex sockets, rounded plugs, angular brackets) symmetrically arranged and clearly tiling right up to all four edges, an Array modifier's Relative/Constant Offset (Constant X: 1.5) visible in the sidebar. Frame 005 shows the hand-modeled pipe network layer added on top: dark reddish tube/conduit shapes winding between the alpha-stamped bumps, a Bevel operator's Segments/Profile Shape/Miter settings visible (Shift+Ctrl+B shortcut badge shown) — the curve-based detail pass. Frame 006 shows the final baked displacement map result: a grayscale tiling normal/height map preview (top-left) next to the Shader Editor graph (Texture Coordinate → Mapping "Tiling Displaceme..." node, Vector output) — confirming the geometry successfully baked into a reusable tiling texture map. Frame 007 shows the finished panel applied at an angled close-up in Rendered view: crisp orange-lit pipes and bumps with sharp, well-defined edges (a "Blade Fill"/"Keep Sharp Edges" toggle visible bottom-left) — the payoff render demonstrating the baked map's quality.

### Key Steps
1. **Base grid setup:** add a Grid (pre-subdivided plane) sized so its Unit Scale and object Scale are both exactly 1 — avoids scale-related surprises later; subdivide it a few more times for enough starting geometry.
2. **Camera framing for the bake:** add a Camera, set it to Orthographic, position it above the grid (exact height doesn't matter for an orthographic camera) and set its Orthographic Scale to a specific value (1.5 in this example) — this value becomes the reference "tile size" used throughout the rest of the workflow; set render resolution to a square format (e.g. 1080×1080); press Numpad 0 to view through the camera.
3. **Sculpt setup:** apply a Matcap with Cavity enabled for easier depth perception while sculpting; add a Multiresolution modifier and Subdivide it several times (leveraging the grid's existing base subdivisions makes this far less heavy on the computer than subdividing a bare, ungeometried plane from scratch) — around 5 levels / ~1.5 million faces was needed here for the alpha stamps to read crisp rather than blurry; more geometry resolution is always the fix for blurry alpha results.
4. **Enable seamless tiling for alpha brushes:** in the sculpt brush Texture settings, turn on X and Y **Tiling**, and set the Tile Offset X and Y to the *same value* as the camera's Orthographic Scale (1.5 in this example) — this makes the alpha tile exactly at the camera frame's borders. A radial-looking alpha may initially look wrong when tiling is enabled; the fix is a **brush setting**, not a texture setting: set the brush's texture Mapping to **View Plane** (must be re-set for every new brush the first time it's used) — after that, strokes dragged near one edge correctly reappear tiling on the opposite edge.
5. **Adding alpha detail:** drag alpha brushes across the surface; hold Ctrl for a negative/subtractive brush where needed; Ctrl+F rotates the brush, F changes radius, Shift+F changes strength — but for alpha brushes specifically, keep Strength at 1 so the alpha's shape reads at its correct/undistorted form. After returning to Object Mode, sculpted detail may appear to vanish — this just means the Multiresolution modifier's **Viewport** level needs raising to preview the detail outside Sculpt Mode.
6. **Hand-modeled geometry detail (pipes/conduits), built for guaranteed tiling:** install the free Extra Objects add-on (Preferences > Extensions) for its Single Vert primitive; add a single vertex exactly on the grid's surface and extrude repeatedly to trace a pipe/conduit path — ensure there's no undercut in the resulting curve shape. Add an Array modifier to the extruded vertex-chain, set to **Constant Offset**, and enter the same tile-size value (1.5) on the X axis; duplicate the modifier setup with a *negative* X offset (−1.5), then repeat both a positive and negative version on the Y axis — this produces a chain that automatically tiles across all four camera-frame edges, since any point continued past one edge reappears in the correct place on the opposite edge.
7. **Editing a tiled chain across all its array copies at once:** set the base grid to Non-Selectable (to avoid accidentally selecting it) and enable **On Cage** on the Array-modified vertex chain, so any vertex can be selected/edited from any of its repeated instances; extend the pattern by Shift+D duplicating a vertex and continuing the path, making sure to continue it correctly across tile edges until it terminates inside another shape (e.g. an alpha-stamped bump) for a clean visual connection.
8. **Give the pipe network thickness:** select corner vertices and Shift+Ctrl+B to bevel them for smoother, rounder corners (scroll the mouse wheel to add more bevel segments; the default Profile is usually fine) before converting to a curve — beveled corners read much better once curved. Convert the vertex chain to a Curve and set its Bevel Depth in the Curve Geometry settings for pipe-like thickness.
9. **Post-conversion cleanup:** convert the curve to mesh, select all in Edit Mode, Merge by Distance to remove a large number of redundant overlapping vertices generated by the array+bevel+curve pipeline; use Proportional Editing afterward to adjust the shape further — but watch out, since Proportional Editing's soft falloff can unintentionally desync matching geometry on opposite tile edges (see the troubleshooting step below). To resize one specific pipe segment without proportional editing's side effects, hover and press **L** to select just that connected piece in Edit Mode, then **Alt+S** to scale it along its normals — critically, remember to apply the same scale change to its mirrored/tiled counterpart on the opposite edge, or the tiling will visibly break.
10. **Test-bake and catch tiling mismatches:** bake a test displacement map and tile it repeated across a test surface — any place where the seam doesn't line up (a repeating visible seam artifact, or geometry that doesn't reach all the way to the tile edge) traces back to an asymmetric edit (usually from Proportional Editing) that wasn't mirrored to the opposite side.
11. **Fixing a tiling mismatch:** switch to Wireframe + X-Ray, verify the correct/undamaged side of the tile reaches all the way to its edge, delete the mismatched geometry on the broken side, then select the correct (undamaged) geometry, Shift+D to duplicate, right-click to cancel the move (keeping it in place), and move the duplicate by exactly the tile-size value in the correct direction (Shift+C then the axis, or a numeric G-axis move — 1.5 in this example, the same Orthographic Scale value used throughout) so it lands exactly where the broken geometry used to be, restoring perfect tiling.
12. **Pre-bake shading check (important, easy to miss):** before baking, check whether any part of the model still reads as faceted/segmented even under Shade Smooth — a displacement bake captures the *actual* underlying facets regardless of shading mode, so flat-looking segments will bake as visibly flat in the final map unless real smoothing geometry is added. Fix by adding a Subdivision Surface modifier (Ctrl+2 for two levels, in this case) to genuinely round out the geometry before baking, rather than relying on Shade Smooth alone.
13. **Next steps (outside this video's scope):** baking the finished geometry using a simple gradient material, then applying the resulting tiling displacement map to other hard-surface models — covered in the full paid course.

### Nodes / Settings
- **Base setup:** Grid primitive, Camera (Orthographic, Orthographic Scale value used as the universal tile-size reference), square render resolution.
- **Sculpt Mode:** Multiresolution modifier (Levels Viewport/Render, Subdivide), Matcap + Cavity overlay, brush Texture settings (Tiling X/Y, Tile Offset X/Y matching camera Orthographic Scale, Mapping: **View Plane**), Ctrl+F (rotate), F (radius), Shift+F (strength, keep at 1 for alpha brushes), Ctrl-hold (negative brush).
- **Add-on:** Extra Objects (Single Vert primitive).
- **Tiling geometry:** Array modifier (Constant Offset, ± tile-size value on X and Y, stacked/duplicated per axis/direction), On Cage (edit an array from any repeated instance).
- **Curve pipeline:** Shift+Ctrl+B (bevel vertices, corner rounding pre-curve-conversion), Convert to Curve, Curve Geometry > Bevel Depth (thickness), Convert to Mesh, Merge by Distance, Proportional Editing (with tiling-desync caveat), L (select linked piece) + Alt+S (scale along normals, must mirror to the opposite tile edge).
- **Finishing:** Subdivision Surface modifier (Ctrl+2) before baking, to avoid flat-faceted results in the bake regardless of Shade Smooth.
- **Downstream (course-only):** baking with a gradient material into a usable tiling displacement texture map.

### Difficulty
Advanced (this is explicitly a paid-course preview lesson focused on building a reusable production tool, not a beginner walkthrough)

### Blender Version
Not specified — relies on the Extra Objects add-on and a standard Multiresolution sculpt workflow, consistent with Blender 3.x through 5.x.

### Tags
displacement, procedural, materials, organic, advanced

---

## Related Tutorials
- [6 Panel Cut Tips - Blender Secrets](6-panel-cut-tips---blender-secrets.md) — shares procedural, materials, advanced; that tutorial's normal-map-baking methods are downstream siblings of this video's tiling-displacement-map creation process.
- [Image to 3D model workflow in Blender](image-to-3d-model-workflow-in-blender.md) — shares procedural, displacement, advanced; that flagship video's hard-surface detailing pass explicitly uses "tiling displacement maps" — this is the dedicated tutorial on how to build one from scratch.
