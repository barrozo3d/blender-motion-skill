---
title: Easy Ear Sculpting Tip - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=-ij6rXb15yA
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified"
tags: [organic, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/easy-ear-sculpting-tip---blender-secrets/
frame_count: 4
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Easy Ear Sculpting Tip - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=-ij6rXb15yA)
**Author:** Blender Secrets
**Duration:** 1m39s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this video, let's look at a fun and easy way of sculpting ears in Blender.
[0:05] First, find some good reference images.
[0:07] Next, let's create a curve with thickness.
[0:09] Personally, I like to start with a edge and subdivide it a couple of times and then convert that to a curve.
[0:15] Give it some depth and set the resolution to 1 to keep the vertex counted down, then add a subdivide modifier to make it smooth.
[0:22] And yes, I know you can just use a path instead of converting a mesh to a curve, but in my experience, this just works better.
[0:29] Next, start adjusting the curve based on the reference image.
[0:33] So move vertices with G and scale them up or down with Alt S and extrude by pressing E.
[0:39] Then to make the ear a bit more three-dimensional, move some vertices on the Y-axis.
[0:43] Once you need another curve, just select a couple of vertices and press Shift D to duplicate.
[0:48] On this particular reference, you can't really see that typical Y shape that the ear has, so make sure that you have enough reference images.
[0:55] Now once you have all the main shapes, convert it all to a mesh.
[0:58] Then add a plane and add some more loops to it to create the two-dimensional shape of the ear.
[1:03] And then make it a bit more three-dimensional using the Grab Brush in Sculpt Mode.
[1:07] After giving that some thickness, you can select everything and join it with Ctrl J.
[1:12] Then in Sculpt Mode, use a foxhole remesh to merge everything together.
[1:16] Now use all your favorite brushes to do the rest of the work.
[1:20] For me personally, that's the Draw Brush, the Grab Brush, Clay Strips and the Smooth Brush.
[1:25] And since all the basic shapes are already there, it's pretty easy to get to the final stage.
[1:30] If you liked this video, check out my sculpting playlist here on YouTube.



---

## Captured Frames

- [0:32] tutorials/frames/easy-ear-sculpting-tip---blender-secrets/frame_000.jpg
- [1:00] tutorials/frames/easy-ear-sculpting-tip---blender-secrets/frame_001.jpg
- [1:14] tutorials/frames/easy-ear-sculpting-tip---blender-secrets/frame_002.jpg
- [1:22] tutorials/frames/easy-ear-sculpting-tip---blender-secrets/frame_003.jpg

---

## Structured Notes

### Core Technique
Block out an ear's cartilage folds as bevel-thickness curves traced directly over a reference photo, convert the curve blockout plus a separate flat "shell" plane to mesh, join and remesh (Dyntopo/Remesh) to fuse them into one manifold, then finish by hand-sculpting with standard brushes.

### Summary
Rather than sculpting an ear from a sphere or freehand, trace its cartilage ridges as curves with bevel depth/thickness directly over reference images (curve created from a subdivided edge converted to a curve, not a native Bezier path — the author found this works better in practice; resolution set to 1 to keep vertex count low, plus a Subdivision modifier for smoothness). Adjust each curve to match the reference with G/Alt+S/E, duplicating strands with Shift+D as needed, and nudge some vertices along Y for volume. Separately, a plane with extra loops forms the ear's flat outer shell, pushed into shape with the Grab brush in Sculpt Mode and given thickness. Convert everything to mesh, join with Ctrl+J, then use a Voxel/"foxhole" Remesh in Sculpt Mode to fuse the curve-tubes and shell plane into one continuous sculptable surface — after which it's finished with ordinary brushes (Draw, Grab, Clay Strips, Smooth).

### Key Steps
1. Gather multiple reference photos of an ear (the author notes a single reference may not show the characteristic Y-shaped cartilage ridge clearly, so cross-check with more than one image).
2. Build the curve tool: start with a single edge, subdivide it a few times, then Convert To → Curve (preferred over starting from a native curve/path). Give it bevel Depth for thickness and set Resolution to 1 to minimize vertex count, then add a Subdivision Surface modifier for smoothing.
3. Trace the ear's ridges directly over the reference image: move points with G, scale with Alt+S, extend the strand with E; nudge some points along Y to add dimensionality (not perfectly flat); duplicate additional cartilage strands from existing points with Shift+D.
4. Separately build the flat outer ear shape from a Plane with extra loop cuts, then push it into rough 3D shape using the **Grab** brush in Sculpt Mode, and give it thickness (e.g. Solidify or manual extrude).
5. Convert the curve network to mesh, select everything (curves + shell), and Ctrl+J to join into a single object.
6. In Sculpt Mode, apply a **Remesh** (voxel-based, referred to loosely as "foxhole remesh" in the transcript) to fuse the separate tube-like curve geometry and the shell plane into one continuous, sculptable manifold surface.
7. Finish the form using standard sculpt brushes: **Draw**, **Grab**, **Clay Strips**, and **Smooth** — since the underlying volumes are already blocked out correctly, this final pass is comparatively quick.

### Nodes / Settings
- Curve setup: Edge → Convert to Curve, Bevel Depth > 0, Resolution = 1, + Subdivision Surface modifier
- Sculpt Mode brushes: Grab (shell shaping), Draw, Clay Strips, Smooth (final detailing)
- Remesh: Voxel Remesh in Sculpt Mode to merge curve-mesh + shell-mesh into one manifold after Ctrl+J join

### Difficulty
Beginner–Intermediate

### Blender Version
Not specified.

### Tags
organic, beginner, intermediate

---

## Related Tutorials
No other ingested tutorials share 2+ tags with this one yet.
