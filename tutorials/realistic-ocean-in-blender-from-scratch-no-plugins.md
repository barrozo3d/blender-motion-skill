---
title: Realistic Ocean in Blender From Scratch (No Plugins)
source: YouTube
url: https://www.youtube.com/watch?v=1eQp-H73zeI
author: Vlabs
ingested: 2026-07-16
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/realistic-ocean-in-blender-from-scratch-no-plugins/
frame_count: 0
frame_status: pending-selection
---

# Realistic Ocean in Blender From Scratch (No Plugins)

**Source:** [YouTube](https://www.youtube.com/watch?v=1eQp-H73zeI)
**Author:** Vlabs
**Duration:** 5m55s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py realistic-ocean-in-blender-from-scratch-no-plugins <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### What we're building [0:00]
**Transcript (timestamped):**
[0:00] What if I told you that you could create a cinematic ocean scene using nothing but free built in blender tools?
[0:05] No plugins, no paid add-ons, just blender and the right techniques?
[0:09] In this tutorial, I'm going to walk you step by step through building a fully realistic ocean scene from absolute scratch.
[0:15] To rain, water, waves, depth, reflections, all of it.
[0:19] Stay to the end because the final render trick is what takes this from good to cinematic.


### part 1 Building the Terrain [0:25]
**Transcript (timestamped):**
[0:26] Before we touch water, we need land.
[0:29] Hit Shift plus A and add a plane, now scale it up.
[0:34] This will be the base of our environment, the ground the ocean sits on, now press tab to enter edit mode.
[0:39] Right click and hit subdivide.
[0:44] Do this twice.
[0:45] Sub-vision adds more geometry to the flat plane, which gives us polygons to push and pull into actual terrain.
[0:53] Head to the modifier properties tab the wrench icon and add a displacement modifier.
[0:58] This modifier physically pushes the vertices of your mesh up and down based on a texture, creating the illusion of rugged terrain without manual sculpting.
[1:06] Now go to texture properties and add a new texture.
[1:10] Change the type to Voronoi.
[1:12] This is a cell-based noise pattern that naturally mimics rocky, irregular terrain.
[1:17] Adjust the size and intensity until your terrain feels natural to you.
[1:28] With the terrain shaped, let's give it a material that actually looks like rock or sand.


### part 2 Terrain Material [1:31]
**Transcript (timestamped):**
[1:37] In the material properties tab add a new material.
[1:40] Now open the shader editor.
[1:41] Here we're going to use a Gabor Texture node.
[1:44] Think of it as a procedural wave pattern that blender generates mathematically.
[1:49] Add a bump node.
[1:51] Connect the value output from the Gabor Texture into the height input of the bump node.
[1:55] Then connect the normal output of the bump node into the normal input of the principal BSDF.
[2:02] For a 90-degree rotation to shift the grain direction, set the rotation value accordingly.
[2:08] Keep tweaking until it looks right to your eye.
[2:11] There's no wrong answer here.
[2:13] Alright, now for the star of the show.


### part 3 Building the Water [2:19]
**Transcript (timestamped):**
[2:23] Add a cube and scale it to cover your scene.
[2:26] Imagine it as a giant block of water sitting on the terrain.
[2:31] Add a new material.
[2:35] Set the transmission weight to 1.
[2:37] This tells blender to let light pass through the object, which is essential for glass, water, and ice.
[2:43] Set the IOR to 133 because that's the real world value for water.
[2:47] Meaning our blender water bends light exactly like real water does.
[2:51] Set roughness to 0 for a perfectly smooth mirror like water surface.
[2:55] You'll immediately notice the plane below starts reflecting inside the cube.
[3:01] Now add a transparent BSDF node and a mixed shader.
[3:07] Connect the transparent BSDF to the first input of the mixed shader and the principal BSDF to the second.
[3:19] Add a light path node and plug the is camera ray output into the factor of the mixed shader.
[3:25] Is camera ray is only for rays coming directly from the camera, not from reflections or lights.
[3:30] By routing this to the mix, we make the water appear crystal clear to the viewer's eye,
[3:35] while still behaving realistically for reflections and lighting.
[3:39] Without this, water often looks murky or weirdly opaque.
[3:42] For now, set the water color to a blue tone,
[3:45] just so it's easy to see and adjust while we're still building the scene.
[3:48] We'll refine this later.


### part 4 Adding Underwater Depth [3:51]
**Transcript (timestamped):**
[3:53] Flat water looks like a swimming pool.
[3:55] Real ocean water has depth, light fades, color shifts, things get darker the deeper you go.
[4:01] Add a principled volume node and connect it to the volume input of the material output.
[4:06] Light rays interact with it as they pass through, giving you that gorgeous deep water look.
[4:11] Keep the density value very low, something like 0.01 to 0.05.
[4:16] Too high and your water looks like thick soup, too low and you lose the effect entirely.
[4:21] Think of density as how foggy the water is.
[4:25] An isotropy controls the direction that light scatters through the volume.
[4:31] A high positive value pushes light forward, like sunlight cutting down through shallow clear water.
[4:36] A low or negative value scatters light in all directions, giving you murkier, deeper ocean feel.
[4:42] Play with this to match the mood of your scene.
[4:46] Finally, change the volume color to a turquoise or aquashape.
[4:50] This gives that beautiful tropical lagoon feel.
[4:52] Water that glows with color when sunlight hits it.
[4:57] The last thing missing is surface movement, that rippled, textured top layer that makes water


### part 5 Surface Waves [5:00]
**Transcript (timestamped):**
[5:02] unmistakably look like water. We use the same trick as the terrain. Add a gabor texture.
[5:08] Connect it to a bump node and plug the bump node into the normal input of the water's principled BSDF.
[5:16] Adjust the distance, scale and frequency until your waves feel right.
[5:21] Higher frequency means more ripples pack together, rougher water.
[5:24] Lower frequency means longer, smoother swells, deeper, calmer ocean.


### outro [5:30]
**Transcript (timestamped):**
[5:35] And that is how you create a cinematic tropical ocean in blender.
[5:38] If this helped you, hit that like button. It genuinely helps this channel grow
[5:43] and tells me to make more of these deep dives.
[5:45] Subscribe and turn on notifications so you don't miss the next one.
[5:48] And drop a comment below what you want to build next in blender. See you in the next one.



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
