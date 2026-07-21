---
title: BLENDER - Full animated character course for Free : THE GAMEBOY PROJECT PART 01
source: YouTube
url: https://www.youtube.com/watch?v=mapuLpQNSAw
author: Pierrick Picaut
ingested: 2026-07-21
blender_version: "Not specified (~2020-era Blender 2.8x based on UI)"
tags: [modelling, hard-surface, procedural, beginner]
extraction_status: complete
frames_dir: tutorials/frames/blender---full-animated-character-course-for-free-the-gameboy-project-part-01/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# BLENDER - Full animated character course for Free : THE GAMEBOY PROJECT PART 01

**Source:** [YouTube](https://www.youtube.com/watch?v=mapuLpQNSAw)
**Author:** Pierrick Picaut
**Duration:** 15m49s | 17 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone, this is Péric from P2Design. In this mini tutorial series, I will show you how to create this whole animation from scratch in Blender.
[0:12] A lot of people in the world will be stuck home for a while because of the COVID-19. This is why I've decided to provide this tutorial for free.
[0:22] But if you want to support me, you can set whatever price you want when you are accessing the files for the first time. Just enter a price of 0 if you want it for free or whatever more if you want to help me on this one.
[0:37] First of all, take good care of you and I hope you will enjoy this tutorial. All the source files are already available on Gumroad and a different video will be available on Download as soon as they are published on YouTube.
[0:52] I originally made this project during a training week with my students. The idea was to teach them the fundamentals of 3D modeling, shading and a bit of animation.
[1:05] Right at the beginning of this week, I've decided to work on a Game Boy and I was planning to create some artwork that was close to what Jonathan Ball from Pocket Studio generally does.
[1:18] He generally creates vibrant and very complex artwork based on very simple characters. And this is a very good way to create appealing artwork and to work with the basis of 3D modeling.
[1:33] This is a beginner-friendly tutorial where I will show all the steps to create the final render from scratch. All the different blender files for each step are provided and also the different textures are provided too.


### create the final render from scratch [1:37]
**Transcript (timestamped):**
[1:48] The provided file may vary a bit compared to the final results because they were done during the training week, but I've also included the final file I've been doing while recording this tutorial.
[2:01] We will be following a pretty classical pipeline. We will first model, then we will go into shading, lightening, rigging our character, making its work animation, and then creating a rapid composition with the different elements animated to create the final render.


### creating a rapid composition with the different elements [2:14]
**Transcript (timestamped):**
[2:22] Let's get started. As usual, I will start by removing everything, then adding an empty image, go to the empty option, and node the reference image provided with the files.
[2:36] Then I want to properly scale this image, so I will add a simple cube and I will enter the different values that I can read on the blueprint.
[2:46] Beware as blender units are set to meters by default since our units are in millimeters, make sure that it's 0.09 for 19 millimeters, etc.
[2:58] Then I will go into the reference picture option of the empty and I will scale it so that it fits the box I created that has the correct size.
[3:08] I will often switch between the solid view mode and the X-ray mode that you can activate by pressing Alt plus Z.
[3:16] I am positioning the reference image and scaling it using its option so that then I can move it as an object without destroying its scaling.
[3:27] If I press then Alt G, Alt R, or Alt S, it will return to this space position with the correct scaling and the correct proportion compared to the real size box.
[3:41] Once I figure the correct value to get the correct proportion, I will just duplicate it and rotate it on the Y axis by 90 degrees and place it on the side so that I will be able to have this blueprint whether I'm in top view or inside view.


### rotate it on the y axis by 90 degree [3:47]
**Transcript (timestamped):**
[4:00] Once I'm done with this, then I was willing to separate my mesh into two pieces so I've entered edit mode.
[4:08] Then I've pressed Ctrl R to activate the loop cut tool and cut it into half. Selected the top point and pressed P to separate the selection.


### activate the loop cut tool [4:09]
**Transcript (timestamped):**
[4:18] But it's not useful since we will be using only the top face. So what you can do is simply enter edit mode and select the top face, duplicate it and press P to separate.
[4:31] This will create a new object, cube.001, that will be editing in a few seconds.
[4:37] So as told before, I will get rid of the unwanted vertices and I will only keep the top ones.
[4:43] This will leave me with a simple plane and I will use the shortcut Ctrl Shift to B that will allow me to create a vertex bevel.


### create a vertex bevel [4:50]
**Transcript (timestamped):**
[4:52] So we will select only those three vertices, press Ctrl Shift to B and scale up.
[4:59] Then I will increase the number of cuts to four segments and scale so that it fits the corners.
[5:06] I always, I generally use a pair number of segments so that I make sure that I get a vertex aligned with the original one.
[5:16] A common mistake that beginners do because a lot of tutorials show you this way of modeling by using box modeling and then using a ton of loop cuts to increase the geometry is that they destroy their shapes.
[5:30] Because when you are box modeling this way, you're not planning what you're doing and then you may have curvature that is not good at all.
[5:38] The technique I always teach to my students is to isolate their main shape, their proper shape using facelips.
[5:46] I've been modeling for industrial design for more than two years quite intensively so I've developed a lot of technique that allow me to model quite efficiently with nice topology.
[5:59] So it might be frightening here when you see this but you will see that we are going to get to this result very fast.
[6:07] My first tip is to use the inset face as often as possible.
[6:12] Here we have the end guns we have generated by beveling the vertices.
[6:16] Now what I want is to isolate this nice shape by creating a face loop around the border.


### creating a face loop around the border [6:20]
**Transcript (timestamped):**
[6:23] If I simply press I to activate the inset face tool, then there will create this face loop for me and then I just have to press X to get rid of the inner face.
[6:36] I will select this loop and duplicate it and move it on the z axis until I'm aligned with the next odd edge on our model.
[6:45] Now I want to connect those loops to create the side of our case.
[6:51] To do it quickly I will use the F2 addon by going into the preferences addon, search for F2 and activate it.
[6:59] This is a must use whenever you're modeling.
[7:02] Just select two vertices, place your 3D cursor in the direction you want to feel and press F and then repeat pressing F as many times as needed.
[7:13] Whenever you're completing like this a big chunk of geometry by feeling it or extruding it, select every face, press Shift N to recalculate the normals.
[7:25] In most cases every 3D software needs to know whether a face is pointing inside or outside of a mesh.
[7:33] Pressing Shift N in edit mode will recalculate this orientation and you can see this orientation in object mode by using the option in the overlay menu.
[7:44] Now that we know how to create simple volume with beveled corner properly, we will create the screen cover.


### create the screen cover as usual [7:50]
**Transcript (timestamped):**
[7:52] As usual we will start with a plane but if I don't care where my 3D cursor is, this plane will be generated in the wrong place.
[8:01] So I will first select the top edge loop by double clicking it and then I will press Shift S cursor to select.
[8:10] Now my 3D cursor is in the right position. I can add a plane and scale it down and then make it fit the blueprint for the screen.
[8:20] The process is then exactly the same as before.


### press ctrl shift b to below the free corner using 4 cuts [8:24]
**Transcript (timestamped):**
[8:24] I will press Ctrl Shift B to bevel the 3D corner using 4 cuts. Then press Ctrl Shift B and bevel the 4th corner.
[8:34] I will inset the face. Then I will get rid of the inner face and here I am with my face loop.
[8:43] The issue here is that I'd like to extend this border. The problem is that I can't use the scaling tool because the shape is not square based.
[8:53] So it won't be scaled homogeneously. What I can do instead is press G twice and hold Alt and confirm with Enter.
[9:03] This will allow me to extend the loop slide tool and create a border outside of the boundaries.


### extend the loop slide tool [9:04]

### use the loop cut tool to align [9:10]
**Transcript (timestamped):**
[9:10] Then we can use the loop cut tool to align our cut with the blueprint and get rid of this face loop.
[9:18] Just a note, you should keep this gap a little tighter because I've made it quite a little too large.
[9:26] I've corrected it in the very end of the modelling stage but if you do it right now, it will be easier than in the end.
[9:33] I will repeat the process for the screen and the screen glass and also for the LED recess.
[9:40] Once we'll be done with this, this will be the time to add our subdivision modifier that will allow us to increase the resolution of our mesh procedurally.


### add our subdivision modifier [9:42]
**Transcript (timestamped):**
[9:52] Meaning that we will be able to smooth the surface and the corner keeping the resolution and the topology we've just created.
[10:03] So it will still be very easy to edit our mesh.
[10:07] In the meantime, you can see that I haven't placed the recess for the LED properly.


### placed the recess for the led [10:09]
**Transcript (timestamped):**
[10:13] What I can do is use the snapping tool, the magnet icon here, set to vertex, press G and Z and snap it onto one of the vertices of the outer edges of the screen.


### snap it onto one of the vertices of the outer edges [10:21]
**Transcript (timestamped):**
[10:28] I will then proceed with a few extrusion and loop cuts to create the inside extrude here and I will switch to matcap with the metallic look here.
[10:40] This will allow us to check the reflection on our model.
[10:45] This is a good way to double check if the surface is looking good.
[10:50] I will add the subdivision modifier, set it to 2 in the viewport.
[10:55] The subdivision modifier is increasing the geometry of my surfaces, making them smoother.
[11:02] The way it smooths the surfaces is by creating additional geometry and interpolating the position between two points.


### creating additional geometry and interpolating the position between two points [11:05]
**Transcript (timestamped):**
[11:12] This results in smoother surfaces, but it can also curve surfaces and here you can see that our case is not straight anymore.
[11:22] This is because the subdivision modifier behaves a bit like a NURBS curve or a BASIC curve.
[11:30] So it will create an interpolation of the geometry between two points.
[11:36] One is the target, the two others are the direction, a bit like a vector.
[11:42] If we create a NURBS curve here, we can see that we get this curvy shape based on different points in space.
[11:52] But if we align multiple points consecutively, the curve will become a straight line.
[11:59] So this is exactly what we have to do on our 3D model by using supporting edge loop or supporting loop cuts.
[12:09] What I like to do to create them is to use the CTRL R shortcut, which is the loop cut shortcut.
[12:15] But then instead of multiplying it, I use the bevel by pressing CTRL B and make sure that I extend it near the corners of the different parts of my mesh.


### support the rounded edges of the rounded corner of our case [12:28]
**Transcript (timestamped):**
[12:28] So that it will support the rounded edges or the rounded corners of our case.
[12:35] The benefit of the bevel modifier is that it will automatically evenly distribute the edge loop for me.
[12:43] The idea is to get supporting loop near the different corners of the mesh so that it will protect each corner and will keep each side perfectly straight.
[12:54] You can finally give depth to the different parts of the screens that are separated, the different panel, and bevel those edges to harden them.
[13:04] I will greatly increase the video speed while I am just adding those supporting edge loop on the different parts of the screen elements.
[13:14] And then we will be able to fill the different gaps.
[13:17] The fact that we have been working with those separated face loops allows us to get rid of any problem of running edge loop across your model.
[13:28] I always model this way and I always teach base modeling this way.
[13:33] Now I just need to connect the different parts of my mesh by pressing F and following the top of G flow.
[13:41] I can finally connect the LED recess so you don't need to add those two loop cuts, don't add them.
[13:49] Because we will use the existing loop cut just beneath to connect the middle of the LED to this part.


### create a loop cut on the top part [13:55]
**Transcript (timestamped):**
[13:56] Just create a loop cut on the top part, it will go all around the frame.
[14:01] And we can already foresee our final topology.
[14:05] So I will be messing around a bit because I've added those two loop cuts for nothing and I will have a hard time getting rid of them because I wasn't using the right shortcut.
[14:16] If you've done so just double click to create those edge loop, press X and select edge loop, not edges.
[14:24] You will see that you will get a nice and smooth result then you can extrude the LED recess inward and add a bevel so that you will get an hardened edge.
[14:36] Once I'm done with this I will fill the front face of the screen.
[14:41] So instead of extruding the screen, scaling it down and then trying to peel it manually, you can select the wall edge loop and press Ctrl F and select grid fill.
[14:53] If you have a pair number of vertices around your edge loop, it will automatically create a faces patch.
[15:02] This is a super useful tool.
[15:04] Then you have the pan and offset options that allow you to modify the pattern of this face patch.
[15:12] But in this case, it was already set properly.
[15:16] This is the end of part one for modeling.
[15:19] In the next video, we will see how to create the button a smart way and how to finish the whole model.
[15:27] In the meantime, if you want to support me, don't forget to like this video and subscribe.
[15:33] And if you want, go to my Gumroad page and check out my full courses.



---

## Captured Frames

- [2:22] tutorials/frames/blender---full-animated-character-course-for-free-the-gameboy-project-part-01/frame_000.jpg
- [4:08] tutorials/frames/blender---full-animated-character-course-for-free-the-gameboy-project-part-01/frame_001.jpg
- [6:23] tutorials/frames/blender---full-animated-character-course-for-free-the-gameboy-project-part-01/frame_002.jpg
- [8:24] tutorials/frames/blender---full-animated-character-course-for-free-the-gameboy-project-part-01/frame_003.jpg
- [10:50] tutorials/frames/blender---full-animated-character-course-for-free-the-gameboy-project-part-01/frame_004.jpg
- [12:15] tutorials/frames/blender---full-animated-character-course-for-free-the-gameboy-project-part-01/frame_005.jpg
- [14:24] tutorials/frames/blender---full-animated-character-course-for-free-the-gameboy-project-part-01/frame_006.jpg

---

## Structured Notes

### Core Technique
Face-loop-driven hard-surface box modeling (inset face + vertex bevel + F2 addon + subdivision modifier with supporting edge loops) applied to a stylized Game Boy handheld case — Part 1 of a free 16-part full character course (modeling → shading → rigging → animation → environment → compositing).

### Summary
Pierrick Picaut (P2Design) opens his free "Gameboy Project" course (released during COVID-19 lockdown, pay-what-you-want on Gumroad) by modeling the handheld's case body from a blueprint reference image. Sets up the reference: add an Empty (Image type), load the blueprint PNG, and — since Blender units default to meters while the blueprint is in millimeters — scale precisely (e.g. 0.019 for 19mm) using the Empty's own reference-image scale option so the object itself stays undistorted when moved (Alt+G/R/S resets to the correct proportioned transform). Duplicates and rotates the reference 90° on Y for a second orthographic view. Splits the mesh into working pieces (edit mode, Ctrl+R loop cut, P to separate by selection), then teaches his core hard-surface philosophy: don't box-model with excess loop cuts (destroys curvature control) — instead isolate each panel/shape with **face loops** built via **Inset Face (I)** + deleting the inner face, then **vertex bevel (Ctrl+Shift+B)** at the corners to create rounded corner geometry with an even, controllable segment count. The **F2 addon** (enabled via Preferences) fills selected-edge gaps in one keypress, and **Shift+N** recalculates face normals after heavy extrude/fill work. Once the paneled shape is blocked out, adds a **Subdivision Surface modifier** to smooth it — but explains subdivision surfaces behave like a NURBS/Bézier interpolation between control points, so straight edges need **supporting loop cuts** (via Ctrl+R, then converted to a tight bevel with Ctrl+B) placed near corners to keep faces flat and prevent unwanted curvature/warping. Uses matcap shading (metallic preview) to visually check surface quality. Closes by fitting the recessed LED screen area with the **Snap tool** (vertex snapping, G+Z) and filling the front screen face with **Grid Fill** (Ctrl+F) instead of manual extrude/scale/peel, provided the edge loop has an even vertex count.

### Key Steps
1. **Reference setup**: Add → Empty → Image, load the blueprint PNG; since default Blender units (meters) don't match a millimeter blueprint, manually scale to match real-world dimensions (e.g. 0.019 = 19mm) using the Empty's own Image/Reference scale field so the transform stays clean; duplicate + rotate 90° on Y for a second reference view; toggle Solid/X-Ray with Alt+Z to see through the model while aligning it to blueprints.
2. **Splitting the mesh** [frame_001 4:08 blueprint-view scene] — Edit Mode → Ctrl+R (loop cut) to bisect, select the half to keep, P (Separate → Selection) to split into independent working objects per body panel.
3. **Face-loop hard-surface technique** [frame_002 6:23; frame_003 8:24] — the core philosophy: avoid uncontrolled box-modeling with excess loop cuts; instead select the shape's border, press **I** (Inset Face) to create an isolating face loop, **X** to delete the now-redundant inner face, then **Ctrl+Shift+B** (vertex bevel) at corners with an even segment count (e.g. 4) to build rounded corners with predictable topology.
4. **Fast geometry connection**: enable the **F2 addon** (Preferences → Add-ons) — select two vertices, position the 3D cursor, press **F** repeatedly to fill/connect geometry quickly; after heavy extrude/fill passes, select all and press **Shift+N** to recalculate normals (check orientation via the Face Orientation overlay).
5. **Subdivision + supporting loops** [frame_004 10:50 metallic matcap check; frame_005 12:15 supporting loop cuts] — add a **Subdivision Surface modifier** (viewport level 2) to smooth the blocky mesh; because subdivision interpolates like a NURBS curve between edge-loop "control points," straight panel edges will bow/curve unless protected — add a **supporting loop cut (Ctrl+R)** near each corner, then tighten it into a bevel with **Ctrl+B** so consecutive points stay aligned and the surface reads as flat/straight rather than curved. Use a metallic matcap preview to visually verify surface quality/reflections.
6. **LED recess placement** — enable **Snapping** (magnet icon, Vertex mode), press G+Z and snap the recess geometry onto an existing screen-edge vertex for exact alignment; extrude/loop-cut the inside of the recess, switch to matcap to verify, then bevel the resulting hard edges.
7. **Front screen fill** [frame_006 14:24 near-final topology] — instead of manually extrude-scale-peel to cap the screen face, select the (even-vertex-count) boundary edge loop and use **Ctrl+F → Grid Fill** to auto-generate a clean face patch in one step (Pan/Offset options available if the pattern needs adjustment).

### Nodes / Settings
- **Modifiers:** Subdivision Surface (viewport level 2; behaves like NURBS/Bézier interpolation between edge points — needs supporting loop cuts to preserve straight edges).
- **Add-ons:** F2 (Preferences → Add-ons) — fast face-fill from 2 selected vertices via repeated F presses.
- **Key shortcuts used:** Ctrl+R (loop cut), P (Separate), I (Inset Face), X (Delete → Face), Ctrl+Shift+B (vertex bevel), Ctrl+B (edge bevel), Shift+N (recalculate normals), Alt+Z (X-Ray toggle), Shift+S → Cursor to Selected, G/Z + Snapping (vertex snap), Ctrl+F → Grid Fill, Alt+G/R/S (reset transform to origin/rotation/scale while keeping visual position via a parent Empty's own scale).
- **Reference-image workflow:** Empty (Image type) with its own independent Image/Reference scale field, kept separate from the object transform to avoid distorting geometry moved relative to it.

### Difficulty
Beginner (explicitly pitched as beginner-friendly; assumes only basic Blender navigation)

### Blender Version
Not specified on screen (2020-era tutorial; UI matches Blender 2.8x)

### Tags
modelling, hard-surface, procedural, beginner

---

## Related Tutorials
- Part 2-16 of the same "Gameboy Project" series (not yet ingested in this library beyond Part 1 and Part 5 — see `blender-easy-led-screen-shader-the-gameboy-project-part-05.md`) cover: further hard-surface modeling (Parts 2-3), shading (Part 4), decal shaders (Part 6), rigging (Parts 7-9), walk-cycle animation (Parts 10-12), environment (Parts 13-14), compositing (Final Part), plus a bonus animation-polish video.
- [Create a Walk Cycle animation in Blender](create-a-walk-cycle-animation-in-blender.md) — same instructor (Pierrick Picaut), a *different* standalone walk-cycle tutorial using his P2M Library rig rather than this Gameboy character; complementary rigging/animation philosophy from the same teacher.
