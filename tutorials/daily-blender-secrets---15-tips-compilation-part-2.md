---
title: Daily Blender Secrets - 15 Tips Compilation (Part 2)
source: YouTube
url: https://www.youtube.com/watch?v=4AttSorvirM
author: Blender Secrets
ingested: 2026-08-04
blender_version: "2.82+ (Custom Bevel Profile stairs preset explicitly requires 2.82 or later)"
tags: [materials, modelling, procedural, simulation, cloth, rigid-body]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-secrets---15-tips-compilation-part-2/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Secrets - 15 Tips Compilation (Part 2)

**Source:** [YouTube](https://www.youtube.com/watch?v=4AttSorvirM)
**Author:** Blender Secrets
**Duration:** 13m28s | 13 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] UV unwrapping can be a lot of work and not all objects really need it.
[0:15] You can use box mapping, sometimes called triplanar mapping, as a quick fix.
[0:19] First, create the usual mapping nodes by selecting the material and pressing Ctrl T.
[0:25] Set the texture coordinate to Generate it.
[0:28] Choose a texture.
[0:29] Choose the projection type to box.
[0:31] This projects the texture from all sides of the model.
[0:34] To avoid these sharp edges, you need to set a blend value so the different angles of the
[0:40] textured projection blend into each other a bit.
[0:43] Point 25 usually does the trick.
[0:45] With object coordinates, you can assign an object to drive the texture coordinates.
[0:50] For example, this empty.
[0:52] You can use it to control the position in 3D space of the texture as well as its rotation
[0:56] and scale.


### Auto Smooth [0:59]
**Transcript (timestamped):**
[1:08] Auto Smooth is a great feature in Blender that creates smooth surfaces without a high polygon
[1:14] count.
[1:15] To use it, first you need to turn on Shade Smooth, then turn on Auto Smooth.
[1:20] An angle of 30 degrees works well in most cases.
[1:23] This means that every angle under 30 degrees gets smoothed out.
[1:28] Every angle over 30 degrees stays sharp.
[1:31] In other words, you don't need to use a sub-diff modifier in support loops, keeping things
[1:35] very low poly.
[1:36] It's an efficient and fast modeling technique for objects that don't deform.
[1:41] Keep in mind, this only works inside of Blender, so if you need to export your model to another
[1:45] program use support loops and sub-diff modeling instead.


### Cut Tool [1:50]
**Transcript (timestamped):**
[1:59] Ghoul Tool is a really awesome cutting add-on that comes with Blender by default.
[2:04] Make sure the box is checked so that it is active in preferences.
[2:09] Create an object that you want to use to cut into another object.
[2:13] Select it, then Shift-Select the other object that you want to cut into.
[2:17] Press Ctrl-1 to cut.
[2:19] Now you can see that the cutter object has become a bounding box.
[2:23] This allows us to see through it while still giving us the ability to select it and move
[2:27] it.
[2:28] The Boolean operation updates in real time.
[2:31] The cool thing is that this is a completely non-destructive way of modeling.
[2:35] You can set the model to smooth shading with Auto Smooth, and you will need to repeat that
[2:39] last step for the cutter object as well.
[2:41] The cutter object is also called the Brush.
[2:44] If you don't want to learn the shortcuts in the Option Panel under the Edit tab, you'll
[2:48] find all the Boolean tool options.


### Loop Tools [2:51]
**Transcript (timestamped):**
[3:00] This chair has an interesting piece of wood that twists around itself.
[3:04] How do you model that?
[3:06] Let's delete that part and start from scratch.
[3:09] Select the faces at both ends and right-click.
[3:12] The Loop Tools menu gives us some extra modeling options, like Bridge.
[3:16] If you don't see these options, make sure the Loop Tools add-on is activated in Preferences.
[3:21] Now that we've selected Bridge, the faces are bridged.
[3:24] In other words, they are now connected by new faces.
[3:27] The original faces are removed.
[3:29] To create the twisting effect, we need to add more edge loops first by increasing the
[3:34] segments.
[3:35] Then create the twisting effect by increasing the Twist value to 3.
[3:39] To bring out the subtle edge reflections of the wood material, I added a Bevel modifier.
[3:45] It's set to Angle.


### Bevel Holes [3:48]
**Transcript (timestamped):**
[3:56] One easy way to create holes in a flat surface is to bevel the vertices.
[4:01] Just create some edge loops with Ctrl R and increase their amount if needed with the mouse
[4:06] scroll wheel.
[4:08] Then select the vertices where you want to create holes and press Shift Ctrl B to bevel
[4:13] them.
[4:14] In the Bevel menu, increase the number of segments and set the Profile to 0.1.
[4:20] This creates a circular profile.
[4:23] Make sure the pivot point is set to Individual Origins.
[4:27] Now you can add some depth to these bevels by extruding them.
[4:31] Extrude by pressing E and then scale them down by pressing S and moving the mouse.
[4:36] Press G and C and move the selection down along the Z axis.
[4:41] This creates a nice beveled edge.
[4:44] Make sure that Auto Smooth is turned on and that the model is smooth shaded.
[4:49] Then extrude down again to create the depth of the hole.
[5:03] This hole is the result of a Boolean operation.
[5:06] As you can see, some unnecessary vertices are left over.
[5:10] We can fix this in a couple of ways.
[5:13] First we can select them and then merge them one by one.
[5:16] Before we can turn on Auto Merge Vertices.
[5:20] Then just slide the vertices to their neighbors by pressing G twice.
[5:24] The vertices are then merged automatically.
[5:27] Now we just have to repeat this step.
[5:32] To create some support loops around this hole, the easiest way is to select the interfaces
[5:37] and press I to inset but don't move the mouse.
[5:41] Then press Alt S and scale the selection inwards.
[5:44] Now add an edge loop on the inside with Ctrl R.
[5:47] Subdivide it, it looks perfect.
[5:49] No Boolean issues left.


### Round Holes [5:52]
**Transcript (timestamped):**
[6:02] If you want to avoid N-Guns and Boolean artifacts, modeling with Quads is the way to go.
[6:07] For a round hole, you don't actually need that many loops.
[6:10] Three edge loops per side of this cube will do.
[6:13] Press Ctrl R and press 3 and on a pad to add three edge loops.
[6:18] Now select four faces in the middle and inset them by pressing I and moving the mouse.
[6:23] Right click and from the Loop Tools menu choose Circle.
[6:26] The Loop Tools addon needs to be activated in preferences.
[6:30] Inset the selection again slightly and extrude down a little bit by pressing E and Z to create
[6:34] some support loops.
[6:36] Extrude further down and create some support loops there as well, if you like.
[6:40] Now we've got a hole with Perfect Quad Topology.


### Stairs [6:46]
**Transcript (timestamped):**
[6:56] Making stairs is easy now with custom Bevel Profiles.
[7:01] Start by beveling an edge using the Ctrl B shortcut.
[7:04] Then open the Bevel menu.
[7:07] Increase the segments and profile as needed.
[7:10] Turn on Custom Profile.
[7:12] You can now choose several presets.
[7:14] Stairs and Molding presets will come in handy for architectural visualization.
[7:19] There is also a Support Loops option.
[7:21] You can even create your own custom profile.
[7:24] Note that this does not work in Blender builds before 2.82.


### Vertex Sliding [7:31]
**Transcript (timestamped):**
[7:41] Sliding a vertex along an edge is easy.
[7:43] Just press G twice and move the mouse.
[7:46] But what if you want to move it along the same angle but in the other direction where
[7:49] there is no edge?
[7:52] Start the same way by pressing G twice and sliding the vertex in one direction of the
[7:56] edge.
[7:57] Then press C and move it in the direction you want.


### Pressure [8:02]
**Transcript (timestamped):**
[8:12] I was curious how the talented at ZUGA Masta on Twitter made this animation.
[8:17] Fortunately, he shares the file on the Blender website.
[8:21] First of all, it uses the new Cloth Physics, which includes something called Pressure.
[8:26] Pressure is a key frameable value which deflates or inflates objects.
[8:31] When we fill in a positive value and press the spacebar, the simulation starts and the
[8:35] model gets inflated and starts to float a bit.
[8:39] The amount of pressure you need depends on your object.
[8:43] In the beginning, this object has a pressure of minus 2, so it gets kind of sucked into
[8:47] itself.
[8:49] Then these collision objects squash it.
[8:51] They are not visible in the render.
[8:53] Next they move away from one frame to the next.
[8:56] And at the same time, the pressure is increased from minus 2 to 70.
[9:01] This causes the object to inflate and then unsquash itself.


### Subdivision Modifier [9:05]
**Transcript (timestamped):**
[9:15] To quickly add a subdivision modifier, instead of adding it in the modifier stack, press
[9:20] Ctrl and a number from 1 to 5.
[9:22] You can then use this keyboard shortcut to toggle between the subdivision levels and
[9:26] Ctrl 0 turns the modifier off.
[9:29] It does not work with the numpad keys, only the top row of numbers from 0 to 5.
[9:34] Bonus tip, if your goal is to make a perfectly round sphere, a subdivided cube is not the
[9:39] way to go, unless you add a cast modifier and set it to Sphere Vector 1.
[9:44] Alternatively, you can activate the Extra Objects add-on, which adds the round cube to the primitives.


### Poly Builds [9:53]
**Transcript (timestamped):**
[10:03] First turn on the PolyBuild tool.
[10:05] In Edit mode, when you mouse over an edge, it will become highlighted.
[10:09] Drag it to extrude a new face, or Ctrl-Drag to extrude a triangle.
[10:14] Repeat that on an edge of the triangle to turn it into a face.
[10:18] Hold Shift and click on a face to delete it.
[10:22] Ctrl-click to create new vertices.
[10:24] Select all with A and press F to fill.
[10:28] Ctrl-Drag a corner vertex to create a face from that location.
[10:32] Together with the shrink-wrap modifier, or with snapping turned on, you can use this
[10:37] tool for manual retopology.


### Bouncy Ball [10:39]
**Transcript (timestamped):**
[10:49] Here's three ways to do a bouncy ball.
[10:51] Method 1.
[10:52] First, set some keyframes for the location by pressing I and moving the ball with G.
[10:57] Then in the Graph Editor, select the keyframes, press T and choose Bounce.
[11:03] Method 2.
[11:04] Set the ground plane to Rigid Body and make it passive.
[11:07] Reduce the Friction and increase Bounceiness to 1.
[11:10] Set the ball to Rigid Body and keep it as active.
[11:13] Reduce the Friction and increase Bounceiness to 0.5.
[11:18] Method 3.
[11:19] Enable Collision for the ground plane.
[11:21] Enable Softbody Physics for the ball.
[11:24] Turn off Softbody Goal and set Bending to 10.
[11:27] Turn on Stiffness.


### Flag [11:30]
**Transcript (timestamped):**
[11:40] Make a flag-shaped plane with enough subdivisions.
[11:44] Add the vertices on one end to a vertex group.
[11:47] Add a Cloth modifier and add the vertex group to the Pinning group.
[11:51] Start playing the simulation by pressing the spacebar.
[11:54] Add a Force, Force or Wind to the scene either will work.
[11:58] And add some more Force to the Wind.
[12:00] A value of 5000 for example.
[12:04] Experiment with the vertex mass.
[12:05] This value depends on your object.
[12:07] You can experiment with the different Cloth presets.
[12:11] Turn on Self-Collisions so the flag doesn't intersect with itself.
[12:26] Create a floor plane when set it to Rigid Body, passive.
[12:30] Create a ragdoll from a bunch of cubes.
[12:33] Set all the cubes to Rigid Body, active.
[12:36] If we play the simulation now by pressing the spacebar, they all fall down, so far so good.
[12:41] Now to connect all the body parts, select two at a time and go to the Object menu, Rigid
[12:46] Body, Connect.
[12:47] In the Connect menu, set it to Point.
[12:50] Select the connection and set Disable Collision to Off.
[12:54] Repeat this for all the parts that should be connected.
[12:57] Parent everything except the floor.
[12:58] Do a new empty so you can easily move it around.
[13:01] Hide the relationship lines in the Overlay options.
[13:04] Play the simulation and check that everything works.
[13:07] For a bit of fun, create a new object and set it to Rigid Body, passive and check animated.
[13:12] This way you can play with the ragdoll in real time.



---

## Captured Frames

- [0:29] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-2/frame_000.jpg
- [2:19] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-2/frame_001.jpg
- [3:35] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-2/frame_002.jpg
- [4:20] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-2/frame_003.jpg
- [6:23] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-2/frame_004.jpg
- [7:12] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-2/frame_005.jpg
- [8:35] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-2/frame_006.jpg
- [12:41] tutorials/frames/daily-blender-secrets---15-tips-compilation-part-2/frame_007.jpg

---

## Structured Notes

### Core Technique
A 13-tip grab-bag spanning triplanar/box texture mapping, non-destructive modeling (Auto Smooth, BoolTool cutting, LoopTools bridging/circles, bevel-based holes and stairs, PolyBuild retopology) and three physics categories (Cloth Pressure inflation, Rigid Body bouncing/ragdolls, Soft Body bouncing).

### Summary
Frame 000 shows the box-mapping setup from Tip 1: a Suzanne head material with the mapping/texture-coordinate node chain open in the Shader Editor, mid-way through "Choose a texture." Frame 001 shows Tip 3 (Cut Tool/BoolTool): a cube with a cylinder cutter positioned for a Ctrl+Numpad-1 boolean cut, the "hole" already visible as a live non-destructive preview. Frame 002 shows Tip 4 (LoopTools) applied to the twisting chair-wood piece: the Bridge/Loft operator panel (Segments 16, Cubic interpolation, Remove Faces, Strength 1.00) mid-adjustment while increasing Segments for a smoother twist. Frame 003 shows Tip 5 (Bevel Holes): the Bevel operator redo panel on a cube (Width Type Offset, Width 0.175m, Segments 5, Profile 0.100, Vertex Only) producing four small circular bevel "islands" that will become holes. Frame 004 shows Tip 6 (Round Holes / Quad Topology): the right-click context menu with the LoopTools submenu open and Circle highlighted, about to snap an inset face selection into a perfect circular quad ring. Frame 005 shows Tip 7 (Stairs): the Bevel operator's Custom Profile panel on an edge-beveled cube, with a stair-step profile curve drawn and a preset dropdown ready ("You can now choose several presets"), producing physical stair-step geometry along the bevel. Frame 006 shows Tip 9 (Pressure): a Cloth modifier's Physical Properties panel on a blob-like mesh, with Pressure set to a large positive value (≈37,300) and the caption noting the simulation is about to inflate the object after Spacebar. Frame 007 shows Tip 13 (Ragdoll): a cube-built stick-figure rig mid-simulation, all parts set to active Rigid Body and just released to fall ("they all fall down, so far so good") before Rigid Body Constraints connect the limbs.

### Key Steps
1. **Box/triplanar mapping (Tip 1):** select the material, press Ctrl+T to auto-generate mapping nodes; set Texture Coordinate to Generated, choose a texture, set the projection type to Box; raise the Blend value (≈0.25) to soften the seams between the projected sides; optionally drive the mapping's position/rotation/scale from an Empty via Object coordinates.
2. **Auto Smooth (Tip 2):** enable Shade Smooth then Auto Smooth with an angle around 30° — angles under the threshold smooth, angles over stay sharp — avoiding a Subdivision modifier and support loops for low-poly, non-deforming hard-surface objects (Blender-only effect; use real subdivision + support loops if exporting elsewhere).
3. **Cut Tool / BoolTool (Tip 3):** enable the BoolTool add-on (bundled with Blender) in Preferences; select the cutter object, Shift-select the target, press Ctrl+Numpad-1 to cut; the cutter becomes a movable/selectable bounding box ("Brush") and the Boolean updates live and non-destructively; apply Shade Smooth + Auto Smooth to both the target and the cutter; all BoolTool options also live in the N-panel Edit tab.
4. **LoopTools twist (Tip 4):** select faces at both ends of a gap, right-click > LoopTools > Bridge (requires the LoopTools add-on) to connect them with new faces, removing the originals; add more edge loops via the Bridge/Loft panel's Segments field; set its Twist value (e.g. 3) for a spiral/twisted look; finish with an Angle-based Bevel modifier to catch material highlights along the twist.
5. **Bevel Holes (Tip 5):** add edge loops with Ctrl+R (scroll to add more); select the vertices where holes should go and Shift+Ctrl+B to bevel them, raising Segments and setting Profile to 0.1 for a circular profile; set the Pivot Point to Individual Origins; extrude the beveled ring (E, then S to scale down, then G,Z or G,C to slide along the normal) for depth; enable Auto Smooth + smooth shading; clean up leftover boolean vertices via manual merge or Auto Merge Vertices + G,G sliding; add support loops by insetting (I, no mouse move) then Alt+S to scale inward, plus a Ctrl+R loop cut and Subdivide.
6. **Round Holes with Quad Topology (Tip 6):** add 3 edge loops per side (Ctrl+R, type 3) to a cube; select 4 center faces and Inset (I); right-click > LoopTools > Circle to snap the inset ring into a perfect circle; inset again slightly and extrude down (E, Z) for support loops, repeating for more depth — yields a hole with clean all-quad topology and no N-gons or boolean artifacts.
7. **Stairs via Custom Bevel Profile (Tip 7):** bevel an edge (Ctrl+B), open the Bevel panel, raise Segments/Profile, enable Custom Profile — choose the built-in Stairs or Molding presets (useful for archviz) or draw a fully custom profile curve; requires Blender 2.82 or later.
8. **Vertex sliding off an edge (Tip 8):** press G,G to slide a vertex along an existing edge in one direction; to continue moving along that same angle past the edge's end, press C after G,G and move the mouse freely in that direction.
9. **Cloth Pressure (Tip 9):** on an object with Cloth Physics, the Pressure setting (under Physical Properties) is a keyframeable value that inflates (positive) or deflates (negative) the mesh on simulation playback; a large negative starting value (e.g. −2) can suck a shape into itself, and animating it up to a large positive value (e.g. 70) makes it inflate/unsquash — combine with (invisible-in-render) collision objects to squash the shape as it's evolving, as seen in the referenced ZUGA Masta reference file.
10. **Subdivision Modifier shortcut (Tip 10):** press Ctrl+0–5 (top-row number keys, not numpad) to instantly add/toggle a Subdivision Surface modifier at that level; Ctrl+0 removes it. Bonus: a subdivided cube alone won't make a perfect sphere — add a Cast modifier set to Sphere (Factor 1), or enable the Extra Objects add-on for a ready-made Round Cube primitive.
11. **PolyBuild retopology (Tip 11):** enable the PolyBuild tool; in Edit Mode, hover an edge (it highlights) and drag to extrude a new face, or Ctrl-drag to extrude a triangle; repeat on a triangle's edge to build it into a quad face; Shift+click a face to delete it; Ctrl+click to add new vertices; select all (A) and press F to fill; Ctrl-drag a corner vertex to fill a face at that location; combine with a Shrinkwrap modifier or snapping for manual retopology over a reference mesh.
12. **Bouncy Ball, 3 methods (Tip 12):** (1) Keyframe location with I/G, then in the Graph Editor select the keyframes, press T and choose the Bounce interpolation type; (2) set the ground to Rigid Body/Passive with low Friction and Bounciness 1, set the ball to Rigid Body/Active with low Friction and Bounciness 0.5; (3) enable Collision on the ground, Soft Body physics on the ball, turn off Soft Body Goal, set Bending to 10, and enable Stiffness.
13. **Flag & Ragdoll (Tip 13):** *Flag:* build a subdivided flag-shaped plane, assign one edge's vertices to a Vertex Group, add a Cloth modifier and set that group as the Pinning group, play the sim, add a Force/Wind field with high strength (e.g. 5000), tune Vertex Mass and try different Cloth presets, and enable Self Collisions to stop the flag intersecting itself. *Ragdoll:* build body parts from cubes, add a passive Rigid Body floor and set every body cube to active Rigid Body; play to confirm they fall correctly; connect adjacent parts two at a time via Object > Rigid Body > Connect, set the constraint type to Point and Disable Collision to Off; parent everything except the floor to a new Empty for easy repositioning, hide relationship lines in Overlays, then play; optionally add a passive, "Animated"-checked Rigid Body object to interactively puppet the ragdoll in real time.

### Nodes / Settings
- **Shading:** Mapping + Texture Coordinate nodes (Ctrl+T auto-setup), Box projection with Blend ≈0.25, Object-driven coordinates via an Empty.
- **Modifiers:** Bevel (Width Type, Segments, Profile, Vertex Only, Custom Profile with Stairs/Molding presets), Subdivision Surface (Ctrl+0–5 shortcut), Cast (Sphere Factor 1), Cloth (Pressure under Physical Properties, Pinning group, Self Collisions, presets), Rigid Body / Rigid Body Constraint (Connect > Point, Disable Collision), Soft Body (Goal off, Bending, Stiffness).
- **Add-ons:** BoolTool (Ctrl+Numpad-1 live boolean cut), LoopTools (Bridge/Loft with Segments/Twist/Strength, Circle), PolyBuild, Extra Objects (Round Cube primitive).
- **Editing:** Ctrl+R (loop cut), I (inset), Alt+S (scale along normals), G,G / G,C (vertex/edge slide), Shift+Ctrl+B (vertex bevel), Auto Merge Vertices.
- **Animation/Physics fields:** Graph Editor interpolation type "Bounce" (T menu), Rigid Body Friction/Bounciness, Force Field Wind strength, Vertex Mass.

### Difficulty
Intermediate

### Blender Version
2.82 or later — the video explicitly states the Custom Bevel Profile stairs preset "does not work in Blender builds before 2.82."

### Tags
materials, modelling, procedural, simulation, cloth, rigid-body

---

## Related Tutorials
- [Daily Blender Secrets - 10 ways to make Holes in Blender](daily-blender-secrets---10-ways-to-make-holes-in-blender.md) — shares modelling, procedural; Tips 5-6 here (Bevel Holes, Round Holes) cover the same bevel-vertex and LoopTools Circle hole-cutting methods in that dedicated video.
- [Blender Secrets - 6 Minutes of Boolean Basics](blender-secrets---6-minutes-of-boolean-basics.md) — shares modelling, procedural, materials; Tip 3 here (Cut Tool/BoolTool) and its leftover-vertex cleanup echo that tutorial's deeper BoolTool walkthrough.
