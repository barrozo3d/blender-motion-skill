---
title: Awesome Wire Generator with Geo Nodes | Blender Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=SvOBxvRjQ8Q
author: Max Hay
ingested: 2026-08-09
blender_version: "not specified on screen"
tags: [geometry-nodes, procedural-modeling, instancing, curves, hard-surface, wires, cables, split-edges, align-rotation-to-vector, endpoint-selection, group-input, menu-switch]
extraction_status: complete
frames_dir: tutorials/frames/awesome-wire-generator-with-geo-nodes-blender-tutorial/
frame_count: 11
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Awesome Wire Generator with Geo Nodes | Blender Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=SvOBxvRjQ8Q)
**Author:** Max Hay
**Duration:** 12m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this video, I'm going to show you how to make a wire generator in Blender's geometry nodes.
[0:04] So we're going to take some wire models and then set up a geometry node system so that you can just move these points around,
[0:10] extrude new points and move them wherever you want.
[0:12] And then it'll just auto fill in random new wires and you can adjust the scale, randomness, variations, seed, all that within the modifier.
[0:20] So it's really useful so you can just take a cluster of these, duplicate it, change some settings, get a whole bunch of new wires,
[0:27] adjust the points super easily.
[0:29] I love this thing.
[0:30] It makes it so easy to just get wires exactly where you want and control the endpoints really easily.
[0:35] And you can do some crazy stuff like putting them all in a circle and then getting random variations around really easily and then you can see how crazy this gets if you want it to be.
[0:43] But it's also good for like really simple stuff like you can even just add a couple of them in a scene,
[0:47] you know, even take some edge loops off an existing model, separate them out, throw that modifier on and just have wires wherever you want.
[0:53] So it's pretty easy to set up.
[0:55] There's also a free download.
[0:56] I'll link below on the one I've already made.
[0:57] If you want to just use that, you can also just make your own or at least follow along with this video so you know how it's made.
[1:02] And yeah, we'll just get into it.
[1:04] OK, so we need a collection of these wires.
[1:07] You probably know how to make this already.
[1:09] It's just a regular model.
[1:11] If you don't really, really quickly, I'll show you the basic idea here.
[1:14] We want to just take a Bezier curve.
[1:17] Let's bring it over here.
[1:18] You want to scale it down on the y-axis.
[1:21] So s, y, zero.
[1:22] So it's flattened out that way.
[1:24] Let's go to front view and we can just shape this into a little hanging wire shape like this.
[1:29] You can probably do this in geometry if you wanted, but I'll just come down to the curve settings, increase the bevel amount a little bit.
[1:35] And then you can just basically take this duplicate and subdivide it into whatever hanging wire kind of shape that you want.
[1:43] So I'll just do something like that.
[1:46] Let's make this a little bit thinner and you get the idea.
[1:49] You can just recursively kind of like go in, duplicate, subdivide, add points and just kind of make any kind of like thing like this.
[1:57] Right.
[1:59] OK, not going to get into that too much because I'm assuming you probably know how to make something like that already.
[2:03] All you need to know is once you're happy with your wire, which this looks terrible, but you can put more effort into it than I just did right there.
[2:10] Just like those curves, right click, convert to mesh and then control J to join it all together.
[2:16] The only other thing you need to know is make a bunch of variations of these like before we do that, I can probably, you know, copy this down here and make some changes to it.
[2:26] Once you have your wires, convert to mesh, join.
[2:30] The only thing you need to know is you need to have the origin point on the far in this case, I'm going to do far left side.
[2:36] So I'll just take these two models, go to edit mode and just align it so that the origin point is right on that left side.
[2:44] So that when you rotate and scale it, it's from that side there.
[2:46] This looks so stupid.
[2:47] I'm sorry, but that's that's the technique.
[2:49] It's literally just the exact same thing I showed with just a little bit more effort and you just make some hanging wires like this.
[2:55] You can even change in the curve settings over there, the profile shape to make it like four circles of a curve circle so that it has like something like that.
[3:02] But not that important.
[3:05] Just get some wires or even just one singular wire model works.
[3:08] And then if you're going to use a collection, just take all these and move to collection, call it whatever you want, put them all into a single collection, have them all the same length and have all the origin points on the left side.
[3:21] Okay, once we have that, I'll show you the setup here.
[3:24] So I'll just take the start from scratch.
[3:27] I'll add a cube and we're going to do geometry on this.
[3:31] I'm going to just take all these vertices in edit mode and merge at center.
[3:36] Okay, so we have, I go to vertex select mode, we have a single vertex here.
[3:40] And if I extrude that, you can see I can just extrude the single point into like whatever shape I want these wires to follow.
[3:48] So we'll make a new system on this and I'm going to do first of all a split edges.
[3:54] I want kind of every chunk of this to be its own kind of like curve segment that it's going to use.
[4:00] So that's what I'm going to do is split edges so that each edge is split apart.
[4:04] Let's do a mesh to curve and then I'm going to do an instance on points.
[4:11] Okay, for the instance, let's just pin this thing here.
[4:15] We can either just take one and drag that in and you can use that as our instance.
[4:20] That works.
[4:21] If you want to have a collection, you would just take, if you want to do a single object, that's all you need to know.
[4:26] Just that.
[4:27] If you want to do a collection info, you can have that here, plug that in, choose our wires.
[4:34] Collection here and then just choose separate children, reset children and pick instance.
[4:40] And now it'll do a random wire every time.
[4:43] If you want to change the seed, we can run that out to a random value here and just adjust the seed right there.
[4:48] And that's something you can run out to the modifier as well.
[4:50] We could do that later.
[4:51] So I'll leave that out for now just to keep this simple.
[4:54] Okay, so it is kind of working if we come here and look at this.
[4:57] Let's just go to edit mode and let's just go in here.
[4:59] So every every point on this thing I, you know, add, it's going to add new curves, new wire.
[5:05] So that's kind of doing what we want a little bit.
[5:08] Okay, so right now you can see if I just take this point and I extrude it, we're actually getting an extra one.
[5:14] So it's doing like one at the start of this curve and then one at the end as well.
[5:19] If I extrude it, it's another one at the start, one at the end kind of thing.
[5:22] I want to use actually an end point selection here.
[5:26] I'm just testing something.
[5:27] I'm just going to switch it back to collection.
[5:30] So that's how it was before.
[5:32] So I'm going to use an end point selection, plug that into the selection input here and then let's go start size one end size zero.
[5:41] And that way, anytime I extrude one more point, it'll kind of be doing what you would expect where it's like kind of following the end of that thing there.
[5:50] Okay, the reason I converted this to a curve as well is we can actually use the spline length to drive the X scale.
[6:01] So I want to plug this into the scale and only have it affect the X this way, right?
[6:07] That's the one I want to affect, not the Y or the Z.
[6:11] I want it to be stretching it this way.
[6:13] The thing is I can't plug this in directly to the X unless I use a combined XYZ node.
[6:19] I have that going in here.
[6:21] You can see this actually splits it up.
[6:22] So now I have independent control over X, Y and Z as an input.
[6:28] We can run the spline length into the X input there and it's actually working.
[6:32] It's just way too big.
[6:34] So we can actually just use like a multiplied, you know, math node here and just drive that down and probably just guess what the correct length should be.
[6:43] I'm sure you could do a calculation based off how big you made your model.
[6:46] But something like that is probably fine.
[6:47] Let's just do two, one, five.
[6:49] That'll depend on how big the wires you made are.
[6:54] That's why I'm saying just make them all the same scale so that this value works the same for all of them.
[6:59] And then you can see now when I move these points around, it's going to actually scale based on each spline.
[7:05] Since I did the split edges, each one of these edges turns into its own spline.
[7:09] Each spline length is going to determine the X scale, which is great.
[7:12] Okay, let's fix the rotation because right now it's doing it, but it's not following where I want it to go.
[7:18] So another thing that we get from this curve is actually a curve tangent.
[7:24] Curve tangent we can use to get information about how this curve is rotated.
[7:30] We can use that to drive the rotation of our instances here.
[7:33] So we can plug this into an aligned rotation to vector and we can plug that into the rotation.
[7:40] I'm actually going to run this into the vector input here and just click around until you find the one that works.
[7:48] This is good, but it actually doesn't always follow it as you can see.
[7:53] Like sometimes we're getting it upside down.
[7:56] It's just not really doing what you would expect sometimes.
[7:58] Like if I move it up, it just is doing that.
[8:01] So after some experimenting and just kind of trying out a bunch of different values and inputs here,
[8:07] what I found work best is actually duplicate this align rotation to vector node.
[8:12] And then the first one we're going to keep X and auto.
[8:17] The second one I'm going to put to Z and actually I'm going to pivot on X.
[8:24] So that I actually don't.
[8:27] I can't explain exactly what that works, but it just it does.
[8:29] So just do that.
[8:30] And now if you just move this around, you can see no matter which way I extrude it,
[8:35] it's always going to kind of do what you would expect where it's kind of just trying to go towards like hanging downwards.
[8:41] And that's great.
[8:41] So we can just take this and kind of like literally just spam it around as much as possible.
[8:46] And you can see it's always going to be aligned to up and down, which is great.
[8:51] So exactly what we want.
[8:53] Okay, the other thing is it might be nice to have control over, for example, the scale on the Z axis, right?
[8:59] This right here might be nice to put that into the modifier.
[9:02] So that if I duplicate this, I can control like this one might I want to have it hang down more, right?
[9:09] We can do something like let's just take the Z scale and run that into right.
[9:13] So this one here, the Z scale can run into the modifier and you can name that.
[9:19] If I just come to the group, name this height or whatever, right?
[9:23] Call whatever you want.
[9:25] And now I have control over that.
[9:27] I can duplicate this and this one I can make lower.
[9:31] This one I can make like this.
[9:33] And that's really nice to just have customized ability over that.
[9:37] Remember, they're all the same shared system.
[9:38] So if I make a change, it's going to affect all of them.
[9:44] But since this height controls now in the modifier, that is independent of each like you can you can change it for each duplicate basically.
[9:53] So that's great.
[9:55] In my other one, I've added more variations or more controls rather like random scale.
[10:00] Seed values, all that stuff.
[10:02] You just you can run literally anything out any parameter out into the modifier and then you can customize as much as you want and make it exactly how you want.
[10:11] But that's the basic idea right there.
[10:13] So if you wanted to have this so that you had a seed control here so that every time you duplicate it, you can change the seed.
[10:18] What you could do is just take a random value.
[10:20] I'll actually just go to the instance index, drag that out and then search for random value.
[10:27] And then that'll give us this here.
[10:28] So you can adjust the seed right here.
[10:31] What you could do is just take that seed, just run that out into the group input and then that puts it over in the modifier.
[10:39] So I have one seed here.
[10:41] I can duplicate this, change the seed, duplicate, change the seed again.
[10:46] And that's how you do that.
[10:48] So here's the setup, which you can screenshot if you want.
[10:51] Okay, so that's the wire generator.
[10:53] I'll show you really quick on my other one.
[10:56] I had a few more controls here.
[10:59] You can see it's the same setup, split edges, mesh to curve, endpoint selection.
[11:03] The rotation is the same.
[11:06] The only thing different, I've added a menu switch to switch between a single object for one simple wire and then a collection, which is a bit more crazy.
[11:15] And then that menu switch gives you an output if option two is selected.
[11:19] So if the menu is set to collection, when that option is activated, that is actually going to turn on pick instance and it's going to turn off if object is selected.
[11:32] So that's cool thing about the menu switch.
[11:34] You can also just run this option.
[11:37] That's another thing you can just drive out from the group input.
[11:40] So you have that menu control right here so that if it's like, oh, I want just one simple wire, boom, I can just do that.
[11:47] If I want a collection of them, I can do that there.
[11:51] Okay, so that's the wire generator.
[11:52] Thank you for watching.
[11:53] I hope this was useful.
[11:55] Again, I'll just link mine below if you don't want to set it up yourself.
[11:57] You can download mine if you want, but I do recommend actually going through and trying it yourself at least because that'll give you a better understanding of geometry nodes and you can use this type of system for so many different things.
[12:06] So it's pretty useful to know.
[12:08] Thanks for watching and I'll see you in the next video.



---

## Captured Frames

- [3:31] tutorials/frames/awesome-wire-generator-with-geo-nodes-blender-tutorial/frame_000.jpg
- [3:48] tutorials/frames/awesome-wire-generator-with-geo-nodes-blender-tutorial/frame_001.jpg
- [4:04] tutorials/frames/awesome-wire-generator-with-geo-nodes-blender-tutorial/frame_002.jpg
- [4:34] tutorials/frames/awesome-wire-generator-with-geo-nodes-blender-tutorial/frame_003.jpg
- [5:32] tutorials/frames/awesome-wire-generator-with-geo-nodes-blender-tutorial/frame_004.jpg
- [6:19] tutorials/frames/awesome-wire-generator-with-geo-nodes-blender-tutorial/frame_005.jpg
- [7:33] tutorials/frames/awesome-wire-generator-with-geo-nodes-blender-tutorial/frame_006.jpg
- [8:17] tutorials/frames/awesome-wire-generator-with-geo-nodes-blender-tutorial/frame_007.jpg
- [9:13] tutorials/frames/awesome-wire-generator-with-geo-nodes-blender-tutorial/frame_008.jpg
- [10:20] tutorials/frames/awesome-wire-generator-with-geo-nodes-blender-tutorial/frame_009.jpg
- [11:15] tutorials/frames/awesome-wire-generator-with-geo-nodes-blender-tutorial/frame_010.jpg

---

## Structured Notes

### Core Technique
A reusable Geometry Nodes modifier that turns a simple edited mesh (a chain of extruded points) into a procedural cluster of hanging-wire instances: each straight-line segment (edge) becomes its own spline that instances a pre-made wire mesh, auto-scaled to fit its own length and auto-rotated to hang naturally, all controllable live by moving/extruding points in Edit Mode.

### Summary
First builds simple reference wire meshes by hand (Bezier curve → flatten on Y → shape into a hanging curve → increase bevel → duplicate/subdivide for variations → convert to mesh → join → set origin to the far-left end), grouped into a Collection with matching scale and origin placement. The real content is the Geometry Nodes setup: start from a cube, merge all vertices to one point, then in Edit Mode extrude that point freely to draw the wire path as a connected chain of edges. The modifier splits each edge into its own spline (**Split Edges → Mesh to Curve**), feeds each spline into **Instance on Points** using a **Collection Info** (Separate Children + Pick Instance, for random variety) or a single object, fixes the "extra instance at both ends of each segment" artifact with an **Endpoint Selection** node (Start Size 1 / End Size 0) wired into the Selection input, drives per-instance X-scale (stretch to fit) from **Spline Length** through a **Combine XYZ** node (so only X is affected), and drives rotation from **Curve Tangent → Align Rotation to Vector**. A single Align Rotation to Vector node flips upside-down unpredictably on some segment orientations, so the fix is to chain **two** Align Rotation to Vector nodes: the first left on default (X axis, Auto pivot), the second set to Z axis with Pivot on X — empirically found by experimentation, not derived from first principles. Finally exposes the Z-scale (named "Height") and a random-value seed as Group Inputs so each modifier instance (each duplicated wire cluster) can be independently varied without affecting the shared node group, and — in the presenter's fuller version — adds a **Menu Switch** to toggle the whole system between single-object and full-collection instancing modes, which also gates Pick Instance on/off via the switch's second output.

### Key Steps
1. Build reference wire mesh(es): Bezier curve, `S Y 0` to flatten, shape into a hanging curve in front view, increase Bevel in curve settings for thickness, duplicate/subdivide to make variations, convert each to mesh (right-click → Convert to Mesh), `Ctrl+J` to join multi-part wires, then in Edit Mode move the mesh's origin to its far-left vertex (so scale/rotate pivots from that end). Keep all wires the same base length/scale so downstream length-driven math stays consistent. Group them into one Collection.
2. New object: add a Cube, enter Edit Mode, select all verts, **Merge → At Center** to collapse to a single point — this becomes the path-drawing seed. Extrude that point repeatedly/freely to draw the wire's path as a chain of connected edges.
3. Geometry Nodes modifier: **Split Edges** (so every edge becomes an independent segment) → **Mesh to Curve** → **Instance on Points**.
4. Instancing source: either plug a single object directly into Instance, or use **Collection Info** (with the wires Collection assigned) → check **Separate Children** and **Reset Children** → check **Pick Instance** on the Instance on Points node for randomized per-segment variety.
5. Fix duplicate-instance-per-segment-end artifact: add **Endpoint Selection**, set **Start Size = 1**, **End Size = 0**, plug into Instance on Points' Selection input — makes extruding a new point add exactly one new instance at the new segment as expected.
6. Auto-scale to segment length: with the mesh-to-curve conversion in place, take **Spline Length** → plug into a **Combine XYZ** node's X input (leave Y/Z at 0/default) → plug the Combine XYZ result into Instance on Points' Scale input, so only X (the wire's long axis) stretches. Divide/multiply the raw spline length down with a **Math (Multiply)** node by a manually-tuned constant (presenter used ~0.215) since raw length is "way too big" — the right constant depends on how large the source wire mesh was modeled, hence the earlier "keep them all the same scale" requirement.
7. Auto-rotate to follow the path: **Curve Tangent** → **Align Rotation to Vector** → Instance on Points' Rotation input. A single Align Rotation to Vector node rotates unpredictably/upside-down on some segment directions. Fix: duplicate the node so there are two in series — first instance: Vector = Curve Tangent output, axis = X, Pivot = Auto (left default); second instance: axis = Z, Pivot = X. This combination reliably keeps wires hanging downward regardless of which direction a segment was extruded.
8. Expose per-cluster controls to the modifier panel: take the Z-scale value (from step 6's Combine XYZ, or a separate scale node) and drag it out to a new Group Input socket, renamed e.g. "Height" — now each duplicated instance of the whole system (each wire cluster in the outliner) can have its own droop/height independent of the shared node group. Similarly expose a **Random Value** node (dragged out from Instance Index → search "Random Value") as a Group Input "Seed" so each duplicate can get different random instance variation without editing the shared graph.
9. (Fuller variant) Add a **Menu Switch** node exposed to the modifier with two options — single object vs. collection — wired so selecting "collection" both switches the Instance source and toggles **Pick Instance** on (and off for the single-object option).

### Nodes / Settings
Split Edges, Mesh to Curve, Instance on Points (Pick Instance, Separate Children, Reset Children), Collection Info, Endpoint Selection (Start Size / End Size), Spline Length, Combine XYZ, Math (Multiply), Curve Tangent, Align Rotation to Vector (chained ×2, second on Z axis / Pivot X), Random Value (for seed), Menu Switch (object vs. collection toggle), Group Input/Output exposure for per-instance modifier controls (Height, Seed, object/collection menu).

### Difficulty
Beginner-to-intermediate Geometry Nodes — no complex math beyond one manually-tuned scale constant; the main "gotcha" (double Align Rotation to Vector to fix upside-down flips) is presented as an empirically-found fix rather than something to derive, so it's easy to copy even without fully understanding why it works.

### Blender Version
Not stated on screen or in narration (UI matches a recent 4.x/5.x Blender Geometry Nodes editor; no explicit version callout).

### Tags
geometry-nodes, procedural-modeling, instancing, curves, hard-surface, wires, cables, split-edges, align-rotation-to-vector, endpoint-selection, group-input, menu-switch

---

## Related Tutorials
None yet — first Geometry-Nodes wire/cable-instancing entry in this library. Cross-link future procedural cable/wire or curve-instancing tutorials here.
