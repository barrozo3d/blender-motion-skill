---
title: Fractals in Blender - Geometry Nodes Extrude Node
source: YouTube
url: https://www.youtube.com/watch?v=bHWvVtuLJkM
author: CrossMind Studio
ingested: 2026-05-19
blender_version: "3.1"
tags: [geometry-nodes, procedural, fractal, beginner]
extraction_status: complete
frames_dir: tutorials/frames/fractals-in-blender---geometry-nodes-extrude-node/
frame_count: 0
---

# Fractals in Blender - Geometry Nodes Extrude Node

**Source:** [YouTube](https://www.youtube.com/watch?v=bHWvVtuLJkM)
**Author:** CrossMind Studio
**Duration:** 8m1s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** While our main geometry node series is still going on, let's try and keep up with the new exciting nodes being released every now and then inside blender. So with the new release of blender 3.1 comes a list of new nodes. I would say these are more beneficial for procedural system and marketing part. But for now, let's look at these two nodes, extrusion and scale instances. These are one of the most simple to use which doesn't need any explanation. But I will give you an interesting example anyway, just in case if you are new to geometry node and find it intimidating. So to extrude a geometry, just bring in, so let's start with a default cube and I'm going to click on a new network inside the geometry node editor. From here in the add menu, let's go to the mesh and over here you can see there are plenty of new things, new nodes. The list is bigger than the last time we saw the geometry nodes. I'll just click on the extrude mesh and plug it right here. So just as expected, all the four phases are being extruded in their own direction. So you have plenty of things to tweak from here, maybe vertices, edges, what do you want to extrude. But for now, I'll choose the phases and keep it li...



---

## Structured Notes

### Core Technique
Fractal-like recursive geometry using Blender 3.1's new `Extrude Mesh` and `Scale Elements` GeoNodes: extrude faces, scale them down, repeat iteratively to create branching fractal structures directly in Geometry Nodes without any scripting.

### Summary
8-minute quick tutorial from CrossMind Studio introducing the new Extrude Mesh and Scale Elements nodes added in Blender 3.1. Creates a fractal-like branching structure by repeatedly extruding and scaling faces in a Repeat Zone (or manual chain before Repeat Zones existed). Simple to understand, but produces visually complex results — great entry point for procedural fractals in GeoNodes.

### Key Steps
1. **Setup** — default cube; add Geometry Nodes modifier, click New network
2. **Extrude Mesh** — Add → Mesh → `Extrude Mesh`; connect Group Input → Extrude Mesh → Group Output; Mode: Faces; all faces extrude in their normal direction
3. **Scale Elements** — Add → Mesh → `Scale Elements`; connect after Extrude Mesh; Mode: Faces; Scale value < 1 (e.g. 0.8) shrinks extruded faces for fractal taper
4. **Chain for iteration** — duplicate the Extrude+Scale pair, connect outputs to inputs of next pair; each iteration adds another fractal level
5. **Vary offset** — reduce Extrude Offset (use Math node: Multiply by 0.5 per iteration) so branches get shorter each generation
6. **Randomize** — add Random Value to Extrude Offset input for organic irregular branching
7. **Repeat Zone (Blender 4.0+)** — use Repeat Input/Output nodes to replace manual chains; set iterations = fractal depth

### Nodes / Settings
- `Extrude Mesh` — Mode: Faces; Offset Factor controls extrude distance
- `Scale Elements` — Mode: Faces; Scale < 1 for tapering (0.5–0.8 typical)
- Chain: Extrude → Scale → Extrude → Scale … (manual in 3.1; Repeat Zone in 4.0+)
- `Math: Multiply` — reduce offset per iteration for realistic fractal proportion
- `Random Value` — add variation to offset/scale for organic look
- Introduced in Blender **3.1** — these are the first appearance of Extrude Mesh in GeoNodes

### Difficulty
Beginner

### Blender Version
3.1 (nodes introduced in this version; Repeat Zone available from 4.0+)

### Tags
geometry-nodes, procedural, fractal, beginner

---

## Related Tutorials
- [[math-x-blender-50-unlimited-power]] — another fractal approach (Apollonian Gasket) with complex math
- [[all-300-geometry-nodes-in-blender]] — reference for Extrude Mesh and Scale Elements nodes
- [[geode-nodes-i-am-so-clever-blender-tutorial]] — advanced GeoNodes procedural structures
