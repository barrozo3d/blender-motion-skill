---
title: ALL 300+ Geometry Nodes in Blender
source: YouTube
url: https://www.youtube.com/watch?v=Y0zAZnbBcQU
author: RADIUM
ingested: 2026-05-18
blender_version: "4.3"
tags: ["geometry-nodes", "procedural", "blender-4x", "beginner", "intermediate", "advanced"]
extraction_status: complete
frames_dir: tutorials/frames/all-300-geometry-nodes-in-blender/
frame_count: 0
---

# ALL 300+ Geometry Nodes in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=Y0zAZnbBcQU)
**Author:** RADIUM
**Duration:** 83m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** There's a wide wide world of geometry nodes. Shut the fuck up. You can only know what you can make. If you know what tools you have in your workshop and what they're capable of. Similarly, you can only know what you can do with geometry nodes. If you know what each node does, unfortunately there are about two 75 nodes in blender 4.3. Not so unfortunately this video is about an hour long. This is... The first nodes we're going to look at are called the input and output nodes. The first section in this is the constant nodes. Constant nodes are input nodes that provide fixed values such as numbers, colors, strings, or other data types to be used across a node dream. These are small tiny nodes so I'm just going to quickly roll over them. The first node is the Boolean node. This node gives a single Boolean value either false or true. Next node in the list is the color node. This node basically allows you to choose a color. Moving on, we got the image node. This node lets you load an image file into the geometry node editor. Next up, we got the integer node. Like the name such as this node provides an integer value. Next is the material input node. This node gives you access to materials...



---

## Structured Notes

### Core Technique
Complete reference covering all ~275 Geometry Nodes in Blender 4.3 — every node's purpose, input/output socket types and colors, and use cases. Deep dives into Fields vs single values, field context (domain adaptation), and the Spreadsheet Editor for attribute inspection.

### Summary
RADIUM's 1-hour reference video is a comprehensive catalog of all Geometry Nodes available in Blender 4.3. Covers Input/Output, Geometry, Curve, Mesh, Point, Instance, Volume, Material, Texture, Utilities, and Vector node categories. The most valuable sections explain Fields vs single values (why some nodes work differently depending on context), how domain adaptation works, and using the Spreadsheet Editor to inspect attribute values live.

### Key Steps
1. **Constant input nodes**: Boolean, Color, Image, Integer, Material, String, Value, Vector — provide fixed values to the network
2. **Field input nodes**: ID, Index, Named Attribute, Position, Radius — evaluate differently per-element (per point, per face, etc.)
3. **Fields vs values**: a Field node evaluates lazily at each element; a Value node is a single constant. Mixing them requires understanding domain context
4. **Domain adaptation**: when connecting a field from one domain to another (e.g. point→face) Blender automatically adapts — use Spreadsheet to verify
5. **Spreadsheet Editor**: pin it to see attribute values live; switch domain (Point/Face/Edge/Vertex) to inspect what's stored where
6. **Geometry nodes** (core): Join Geometry, Transform Geometry, Bounding Box, Convex Hull, Delete Geometry, Duplicate Elements, Merge by Distance, Separate Geometry
7. **Mesh nodes**: Subdivide Mesh, Extrude Mesh, Flip Faces, Mesh Boolean, Mesh to Curve, Edge Paths to Curves, Dual Mesh
8. **Instance nodes**: Instance on Points, Realize Instances, Rotate Instances, Scale Instances, Translate Instances
9. **Utility nodes**: Math, Vector Math, Map Range, Float Curve, Color Ramp, Switch, Compare — the building blocks of all logic

### Nodes / Settings
- Boolean / Integer / Float / Vector / Color input nodes — constant single values
- Index node — per-element integer 0,1,2… used to drive variation
- Named Attribute — reads any custom attribute by string name
- Position node — per-point position as a field
- Spreadsheet Editor — Domain selector: Point/Edge/Face/Corner/Spline; live attribute inspection
- Join Geometry — merges multiple geometry streams
- Instance on Points — instancing with per-point Scale/Rotation
- Realize Instances — converts instances to real geometry for further modification
- Map Range — remaps value from one range to another; Clamp option
- Color Ramp — maps 0–1 float to color gradient; Constant/Linear/Ease interpolation
- Merge by Distance — removes duplicate vertices within threshold
- Extrude Mesh — extrudes faces/edges/vertices; Offset and Scale parameters

### Difficulty
Beginner / Intermediate / Advanced

### Blender Version
4.3

### Tags
#geometry-nodes #procedural #blender-4x #beginner #intermediate #advanced

---

## Related Tutorials
[PENDING EXTRACTION]
