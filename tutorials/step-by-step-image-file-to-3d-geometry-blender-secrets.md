---
title: Step by Step: Image File to 3D Geometry | Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=HUL9o27m11M
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/step-by-step-image-file-to-3d-geometry-blender-secrets/
frame_count: 0
frame_status: pending-selection
---

# Step by Step: Image File to 3D Geometry | Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=HUL9o27m11M)
**Author:** Blender Secrets
**Duration:** 7m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py step-by-step-image-file-to-3d-geometry-blender-secrets <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Knife Project is another interesting tool for making holes.
[0:08] To demonstrate it, I'll use a round cube.
[0:13] This is the Quadsphere preset.
[0:17] I'll just hide that for now.
[0:21] You can just drag and drop images from a File Explorer window.
[0:27] This image is imported as an empty object.
[0:34] Convert it to a grease pencil object by going to this menu.
[0:40] I recommend the default resolution, which is 5.
[0:50] This creates a new grease pencil object.
[0:52] We can hide the original image empty.
[0:54] It's a bit difficult to see, but it also kept the keyhole of the logo.
[0:59] But we actually still need to convert it to a path.
[1:05] If we disable the grease pencil object, we can see the path.
[1:09] Finally, we convert it to a mesh.
[1:12] I hope that in the future we can convert directly from grease pencil to mesh.
[1:18] I'll just rename this mesh to logo in the Outliner.
[1:27] Now as you can see, this has a lot of vertices.
[1:31] That will make it difficult later to get a nice smooth result when we cut into the Quadsphere.
[1:36] What we can do is select all the vertices and then press M for the Merge menu.
[1:40] Then Merge by Distance and experiment with the Distance value.
[1:55] To further get rid of vertices, we can use Checker Deselect.
[2:00] Unfortunately, we need to do it per individual mesh island.
[2:08] So select one mesh island by hoovering the cursor over it and pressing L.
[2:12] Then go to Checker Deselect.
[2:15] This selects every other vertex.
[2:19] Then you can press Ctrl X to dissolve these selected vertices.
[2:24] Repeat these steps for each mesh island.
[2:27] I do recommend deselecting the corner vertices as these are important for the shape.
[2:34] We can manually slide or remove some vertices to repair these corners where the shape got
[2:45] destroyed a bit.
[2:50] For the next step, first select all the corner vertices and then invert the selection.
[3:10] Then you can use the Loop Tools space tool to evenly space out those vertices.
[3:20] I'm just manually sliding and moving some vertices for some final improvements.
[3:31] Unhide the Quadsphere.
[3:37] Move the logo along the Y-axis.
[3:39] And distance doesn't matter as long as it's not inside of the sphere.
[3:44] If we select both objects and go to Edit Mode, we can inspect and compare the vertex distribution.
[3:50] Usually it's a good idea to have the resolution of both objects fairly similar to make things
[3:54] easier later on.
[3:56] In this case, the sphere is a much lower resolution than the logo, so I'll add some
[4:00] subdivisions to it.
[4:02] After applying that Subdiff modifier, we can see that the objects now match better in terms
[4:05] of their resolution.
[4:09] Now we're ready to use Knife Project.
[4:11] Select only this sphere in Object Mode.
[4:13] I will enable Shade Autos Mode.
[4:19] Go to Edit Mode.
[4:20] It doesn't matter if you're in Vertex Edge or Face Mode or if anything or nothing is
[4:25] selected.
[4:26] Then hold Ctrl and in the Outliner, select the logo.
[4:31] Go to Mesh Knife Project.
[4:38] As you can see, this has cut the logo shape into the sphere.
[4:42] We can enable Cut Through in the last operator panel to cut all the way to the other side
[4:46] of the sphere.
[4:48] One thing that's important to know is that the viewing angle determines how you cut.
[4:53] So for example, if we cut from this view, we only cut the overlapping part of the logo.
[5:01] While the last operator panel is active, we can still cut from different angles.
[5:05] In this case, we're going to cut from the front and without cutting through the sphere.
[5:12] Since these faces are all selected after the cut, we can easily delete them.
[5:18] As you can see, the Knife Project operation has left us all these unwanted vertices.
[5:23] You could enable Auto Merge Vertices and then slide them, we're pressing G twice to clean
[5:28] up this mess manually.
[5:30] However, that's quite time consuming.
[5:34] We can take advantage of some nice time saving steps.
[5:38] First select the non-manifold geometry, which is just the verges around the hole.
[5:43] Then merge by distance.
[5:48] Experiment with the value until you get a good result.
[5:52] As you can see, this took care of a lot of vertices.
[5:57] We can still manually clean the leftover ones by sliding them and merging them.
[6:04] Here there is a hole and we can fill it by selecting the vertices and pressing F.
[6:14] I want to keep this vertex and connect it to another one by pressing J, as I think that
[6:18] vertex is important for the overall shape.
[6:27] This is also an opportunity to fix the shape of the hole where necessary.
[6:35] Select the non-manifold vertices again.
[6:38] Let's switch to edge mode so we can deselect these edges.
[6:45] Now if we extrude with E and then scale with S, we get a not so great result.
[6:55] Let's scale with Alt S, which scales in the direction of the normals.
[7:03] This gives a pretty clean and smooth result.
[7:11] Let's add another quad sphere.
[7:14] Subdivide and shade it smooth, then scale it down.
[7:18] This gives us an easy and non-destructive way to control the depth of the logo.
[7:29] If necessary, you can still adjust some edges to improve the shape.



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
