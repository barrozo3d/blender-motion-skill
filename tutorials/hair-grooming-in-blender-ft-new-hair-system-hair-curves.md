---
title: Hair Grooming in Blender ft. New Hair System (Hair Curves)
source: YouTube
url: https://www.youtube.com/watch?v=pQcYoH4H1MM
author: adiidiin
ingested: 2026-07-19
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/hair-grooming-in-blender-ft-new-hair-system-hair-curves/
frame_count: 0
frame_status: pending-selection
---

# Hair Grooming in Blender ft. New Hair System (Hair Curves)

**Source:** [YouTube](https://www.youtube.com/watch?v=pQcYoH4H1MM)
**Author:** adiidiin
**Duration:** 6m10s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py hair-grooming-in-blender-ft-new-hair-system-hair-curves <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, today I'll be showing you how I made this hair in Blender using the new Hair Curve system.
[0:09] I start by creating a base mesh where I want the hair to grow, but if your character is already retapologized, you can just simply extract the mesh from there.
[0:22] Since I'll be using weight paint to control the hair density, I make sure this mesh has enough resolution that I can paint on.
[0:32] Once the mesh is ready, I scale it down a bit. This helps me hide it slightly and prevents the hair strands from floating.
[0:41] Before adding any hair, it's important to unwrap the mesh.
[0:45] Hair systems rely on UVs for things like interpolation, so I just quickly do a basic unwrap.
[0:53] Next, with the mesh selected, I shift A and add an empty hair.
[0:59] I go to sculpt mode, turn on symmetry, and start adding hair curves.
[1:05] From here, I slowly build up the modifiers.
[1:09] I begin with a set hair curve profile to adjust the radius.
[1:14] I turn on render preview to see how thick the hair looks.
[1:21] From there, I stack several modifiers. I like adding a bit of variation and character to the hair shape.
[1:29] I suggest experimenting with different modifiers that will suit your character.
[1:36] Once I'm happy with the basic shape, I start styling the hair using the comb, grow, or shrink brushes.
[1:46] I tick all the options on the interpolate so new curves use the average length, radius, shape, and point count of the nearby strands.
[1:57] This will keep everything looking consistent.
[2:01] As I add more curves, I continue styling them using the same brushes.
[2:09] To increase overall density, I add the interpolate hair curves modifier after the duplicate hair curves.
[2:17] I select the mesh as a surface, then increase the density value.
[2:22] As you can see, it starts covering the entire mesh, so now it's time for weight painting.
[2:35] First, I create a new vertex group and rename it appropriately since I'll be adding more for a different area later.
[2:44] With the weight paint of 1, I paint only the areas where I want the hair to grow.
[2:51] I just copy the vertex group name and paste it into the density mask field.
[2:58] Now I go back to more styling and disable symmetry to make it look more natural.
[3:07] To create the hair on the sides, I follow the same process.
[3:12] Add hair curves, comb and trim for styling.
[3:18] I just copy the modifiers from the top hair setup, we'll still adjust the settings later.
[3:25] Create a new vertex group, weight paint the side area, paste the new group name into the density mask.
[3:38] Add more hair curves to fill the space.
[3:46] For the material, I use the principled hair BSDF.
[3:52] I add a curves info node, then connect the intercept output to the factor input of a color ramp.
[4:00] By doing this, you can control the gradient along the curve.
[4:07] To add color variation, I connect the random output to another color ramp, then blend using a mixed node and set this to add.
[4:18] This is great if your character has random white hairs.
[4:22] In my case, the character only has dark hair so I just change the color accordingly.
[4:30] Now for the eyebrows and eyelashes, this was inspired by Nazard's videos which I'll link below.
[4:38] But this is done using the new hair system where you can play with the modifiers.
[4:44] The process is very similar to the head hair, but the eyebrow modifiers are much simpler.
[4:50] You can add more if needed, but this setup is already enough for my character.
[4:56] I'm just like before, I use weight paint for the density mask.
[5:01] This whole setup makes it super easy to reuse the eyebrows on another character and tweak things later.
[5:12] Then I duplicate the eyebrow, mirror it to the other side and use a shrink wrap to attach it to the head.
[5:21] I can also scale or reposition it as needed.
[5:28] For the eyelashes, instead of interpolate hair curbs, I just use the duplicate hair curbs since I won't be needing that much density.
[5:40] But I still have a mesh for the eyelashes.
[5:43] This helps me attach the eyelashes to the surface and not be all over the place.
[5:49] I do it by adding an attached hair curbs to surface modifier and select the mesh as the surface.
[5:59] Then I duplicate and mirror it to the other side.
[6:05] That's all, thank you for watching, happy blending!



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
