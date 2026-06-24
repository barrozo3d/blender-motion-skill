---
title: Fractals in Blender - Geometry Nodes Extrude Node
source: YouTube
url: https://www.youtube.com/watch?v=bHWvVtuLJkM
author: CrossMind Studio
ingested: 2026-06-23
blender_version: "3.1"
tags: [geometry-nodes, procedural, materials, shaders, glass, abstract, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/fractals-in-blender---geometry-nodes-extrude-node/
frame_count: 4
---

# Fractals in Blender - Geometry Nodes Extrude Node

**Source:** [YouTube](https://www.youtube.com/watch?v=bHWvVtuLJkM)
**Author:** CrossMind Studio
**Duration:** 8m1s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** While our main geometry node series is still going on, let's try and keep up with the new exciting nodes being released every now and then inside blender. So with the new release of blender 3.1 comes a list of new nodes. I would say these are more beneficial for procedural system and marketing part. But for now, let's look at these two nodes, extrusion and scale instances. These are one of the most simple to use which doesn't need any explanation. But I will give you an interesting example anyway, just in case if you are new to geometry node and find it intimidating. So to extrude a geometry, just bring in, so let's start with a default cube and I'm going to click on a new network inside the geometry node editor. From here in the add menu, let's go to the mesh and over here you can see there are plenty of new things, new nodes. The list is bigger than the last time we saw the geometry nodes. I'll just click on the extrude mesh and plug it right here. So just as expected, all the four phases are being extruded in their own direction. So you have plenty of things to tweak from here, maybe vertices, edges, what do you want to extrude. But for now, I'll choose the phases and keep it like this. And the other node I'm going to bring in here is going to be the scale element node, which is also new to the geometry node inside 3.1. So the scale element is going to scale any element inside the geometry. As of now, this entire thing is stitched as one. This is geometry. It's actually going to scale everything. In case if I split all these edges, then the scale element is going to scale all these phases separately. So since all the edges are now broken. So let's get rid of this. Instead of that, we are going to scale elements, which are being extruded here. So the top side from the extrude mesh, you have these two outputs. The top side, which are these and the side areas, which are these the length area. So the top side, we are going to plug that into the selection of the scale element. As soon as we do that, you'll see now we are only scaling the top side of the extruded mesh. So to keep this effect subtle and for today's example that we are going to discuss something like fractals, I'm going to keep it very minimal like 0.1 and it doesn't matter what you put here, we can always change this later. So I have this. Now let's start layering things up and make it more exciting. So I'll press Ctrl G on these two nodes and that makes it a group. Now press tab to exit the group and you have this group. Let's call it extrude and insert. So as of now, we don't have any loop node, which can actually loop this for the number of iterations. So we are going to do some manual work. All you have to do is just plug this right here again, multiple copies, you can do that with a shift D. Just be careful that the heavier the geometry gets, the slower your computer is going to get. So I think the four iterations work fine. So I'm just going to try my luck and see if the fifth iteration works. So yeah, this works and now it looks all messed up. But let's go inside the geometry node, the group that we have made. So all of these are copy of the same group. So it doesn't matter which group I select, it's going to show me the same thing and all of these have the sharing properties. So from the scale element, if I scale these now, you'll see something going on, which looks like kind of fractal. But it doesn't look really clean. So I'm going to change the offset inside the extrude to 0.01. And that's it. You have something which looks like a pattern repeating on every phase. And now if you change the scale, you have the new patterns and the shapes emerging inside this cube's faces. Now I'll go out and press, press, dab and move out of the group and delete one of these. So that's because I'm going to experiment with this up little more. Let's extrude again. And this is going to get heavier. But this time, I'm going to bring in one new node and that would be phase area. Let's plug that into the selection. And now I want to extrude only the area which gets bigger than any number. Let's say compare. If I bring compare here and type 0.4. So now any phase which gets bigger than this number 0.4 gets extruded again. And then scale element and top side. So if I deselect this, if I disconnect this, you have this quite grainy thing going on. If we don't want that, we don't want all the faces to have this extrusion, we only want some faces which are maybe larger than 0.4 to break the pattern. That's all. You can actually leave it. You can just make the fractal with these two nodes that's totally up to you. But for my example, I'm going to just try a bit hard. So you have this extra layer of detail going on for any phase which grows bigger than this number. And then let's go out of the group and plug this number here. So now you have this variation like the bigger shape in the center and smaller shape on the side. Now if you try to drag and change this number, what will happen is as soon as this center area grows and becomes bigger than this number, this threshold, the new shapes will emerge in from here. And that will be sent to the new extrude node that we have added here. So just a very basic use of the few nodes which are added here. And there are plenty more things we are going to do with this. So don't worry about that. Just take it lightly and just be careful and try not to stack too many of these groups. It could get heavy. And yeah, that's about it. To render all I'm going to do is go to the shader editor and make sure that I have a cycle render. You can try eb if you prefer. Delete this one, bring a class PSDF, connect this here with the surface and I bring in few lights, maybe a point light. And I'll make a multiple copies of this and try to make a nicely out for myself. And to make the scene a little more exciting, I'm going to add some lights inside these cubes. Just make sure you don't have any HDR in the background. And then we have these three lights for the different colors. And that's about it. It's going to shine through those transparent glass surfaces and will help bring out those shape of the crystals and the patterns which are forming on the surface. And once you have everything set up, just try and place a camera and animate these values and take some good close-ups, maybe try a different material for yourself to make anything you want. So I hope you guys are enjoying this series. If you are new to Blender's Geometry node, try out this playlist which is covering everything you need to know for the beginners, keeping it all simple and clean and not really getting into two complex examples. So I'm sure you're going to enjoy this series if you're new to Geometry node. And let's talk about a few more things in the next video about how you can use the materials with the Extrude node. So I'll see you guys in the next video. Bye.

**Frame:** tutorials\frames\fractals-in-blender---geometry-nodes-extrude-node\frame_000.jpg


---

## Structured Notes

### Core Technique
Manually chaining an "Extrude Mesh → Scale Element (top faces only)" node group multiple times (Blender 3.1's then-new Extrude Mesh and Scale Elements nodes) to build a recursive, fractal-like crystalline pattern across a cube's faces — with an optional Face Area + Compare threshold to selectively break the pattern only on faces above a certain size.

### Summary
Introduces two nodes new in Blender 3.1: **Extrude Mesh** (extrudes selected faces/edges/vertices along their own direction, exposing Top and Side output selections) and **Scale Elements** (scales mesh elements — uniformly as one shape unless edges are first split, in which case each face scales independently around its own center). Plugging Extrude Mesh's Top output into Scale Elements' Selection makes only the newly extruded top faces scale inward, creating a stepped "inset" look; grouping these two nodes (Ctrl+G, named e.g. "Extrude and Inset") creates a reusable unit. Since Geometry Nodes (at the time) had no native loop node, the group is manually duplicated and chained in series (Shift+D, 4–5 copies found to be a practical limit before performance degrades) — because all duplicated group instances share the same underlying node group data, editing the Scale factor or Extrude Offset inside ONE instance updates all copies simultaneously, letting you tune the whole recursive pattern from a single edit. A small Extrude Offset (~0.01) combined with the scale produces a repeating fractal-like pattern across every face; changing the Scale value live-updates new emergent shapes across all chained iterations. For selective/non-uniform fractal detail, add a **Face Area** node → **Compare** node (e.g. threshold 0.4) into a NEW extra Extrude+Scale group's Selection, so only faces larger than the threshold receive an additional recursive extrusion layer — as the pattern grows and a face's area crosses that threshold, new geometry spontaneously emerges from it, creating organic big-shape/small-shape size variation rather than uniform repetition everywhere. Finished with a simple crystal-style render setup: Cycles, a Glass BSDF, multiple colored point lights placed inside hollow cube shapes (no HDRI background) so colored light shines through the transparent glass and highlights the fractal surface detail.

### Key Steps
1. Default Cube → new Geometry Nodes network.
2. Add → Mesh → Extrude Mesh; select Faces mode; plug Mesh in.
3. Add → Mesh (or relevant category) → Scale Elements; plug Extrude Mesh's **Top** output into Scale Elements' Selection so only the newly extruded top faces scale (rather than the whole shape, which only works correctly if edges are split — otherwise it scales as one connected piece).
4. Set a small initial Scale value (e.g. 0.1) — exact value doesn't matter yet, tune later.
5. Select both nodes, Ctrl+G to group them; name the group (e.g. "Extrude and Inset"); Tab to exit the group.
6. Duplicate the group node in series with Shift+D, chaining each copy's output into the next copy's input — 4–5 iterations is a practical performance ceiling; all duplicated instances share the same underlying node group, so editing one instance's internal Scale/Offset values updates every chained copy at once.
7. Lower the Extrude Mesh's Offset inside the group (e.g. to 0.01) for a cleaner, more pattern-like repeating result; adjust Scale Elements' factor to reveal new emergent shapes.
8. For selective/area-based variation: outside the simple chain, add another Extrude+Scale step fed by a **Face Area** node → **Compare** node (threshold e.g. 0.4) into its Selection, so only faces exceeding that area get the extra extrusion layer — creates organically varied (not uniform) fractal detail as the recursive pattern's face sizes change.
9. Shading/render: Shader Editor, swap to a Glass BSDF, set render engine to Cycles (EEVEE usable too); place several point lights of different colors inside hollow cube shapes, no HDRI background, so colored light refracts/shines through the glass surfaces and highlights the fractal pattern; animate parameters and frame close-up shots with a camera for final renders.

### Nodes / Settings
Geometry Nodes: Extrude Mesh (mode: Faces, Offset, Top/Side selection outputs), Scale Elements (Selection input, Scale factor; requires split edges for independent per-face scaling), Face Area, Compare (threshold), node Group (Ctrl+G) with shared-instance editing via Shift+D duplication. Shading: Glass BSDF, Cycles render engine, colored Point lights, no HDRI/world lighting.

### Difficulty
Beginner to Intermediate — explicitly aimed at Geometry Nodes beginners; the manual loop-via-duplicated-groups workaround and Face Area/Compare threshold trick are the more advanced ideas.

### Blender Version
3.1 (Extrude Mesh and Scale Elements are explicitly introduced as new in this release).

### Tags
#geometry-nodes #procedural #materials #shaders #glass #abstract #beginner #intermediate

---

## Related Tutorials
- `all-300-geometry-nodes-in-blender.md` — covers Extrude Mesh and Scale Elements (under different terminology, e.g. Scale Element) as part of its full node reference
- `geode-nodes-i-am-so-clever-blender-tutorial.md` — likely shares crystal/geode procedural geometry territory
