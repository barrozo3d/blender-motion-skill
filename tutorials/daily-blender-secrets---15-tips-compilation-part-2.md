---
title: Daily Blender Secrets - 15 Tips Compilation (Part 2)
source: YouTube
url: https://www.youtube.com/watch?v=4AttSorvirM
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/daily-blender-secrets---15-tips-compilation-part-2/
frame_count: 0
frame_status: pending-selection
---

# Daily Blender Secrets - 15 Tips Compilation (Part 2)

**Source:** [YouTube](https://www.youtube.com/watch?v=4AttSorvirM)
**Author:** Blender Secrets
**Duration:** 13m28s | 13 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py daily-blender-secrets---15-tips-compilation-part-2 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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
