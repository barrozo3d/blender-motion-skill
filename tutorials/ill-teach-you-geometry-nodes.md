---
title: I'll teach you Geometry Nodes
source: YouTube
url: https://www.youtube.com/watch?v=JU70u6cJZqI
author: Default Cube
ingested: 2026-05-18
blender_version: "4.5"
tags: ["geometry-nodes", "procedural", "blender-4x", "beginner", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/ill-teach-you-geometry-nodes/
frame_count: 0
---

# I'll teach you Geometry Nodes

**Source:** [YouTube](https://www.youtube.com/watch?v=JU70u6cJZqI)
**Author:** Default Cube
**Duration:** 50m36s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** How do you learn geometry notes? First of all, by playing with them and second of all, by watching tutorials. I made a five and a half hour course thing. The first hour or so is gonna be free to you. So let's begin. Hello everybody and welcome to introduction to geometry notes. The course that takes you from not knowing geometry notes to knowing it very well. I'm not gonna assume you know anything from the get-go, which is probably what you want. And I'm not a fan of wasting your time. So quick description. My name is Tom. You might know me as CG matter or default cube. These are tutorial channels where I've been teaching geometry notes for years. All the clips you're about to see, I worked at Nayer Studios doing just geometry notes. Some effects, some snow, some particle stuff, and that is the extent of it. And every single bit of freelance I've ever gone has involved geometry notes. It is the most powerful tool in Blender and it's only getting more powerful. So it is essential that you know how to use it. Literally the only two prerequisites I would like you to have before starting this course is one. I'm gonna be using Blender 4.5 as you can see in the corner here. This is the l...



---

## Structured Notes

### Core Technique
A 5.5-hour comprehensive Geometry Nodes course in Blender 4.5 that teaches from zero — workspace navigation, the Node Editor left-to-right data flow, Spreadsheet Editor for live attribute inspection — with the first practical project being a 3D Menger Sponge fractal demonstrating procedural iteration and instancing.

### Summary
Default Cube (Tom, also known as CGMatter) delivers a professional Geometry Nodes course aimed at complete beginners. The free first hour covers the conceptual foundation: what Geometry Nodes is, how data flows left to right through the node tree, the difference between single values and Fields, and how the Spreadsheet Editor reveals what attributes exist at each point, edge, face, or instance domain. The first major project is a Menger Sponge fractal — cubes with holes cut in them recursively — which teaches instancing, boolean-style operations, and iterative procedures in GN. The course was created by someone with professional studio experience (Nayer Studios), focusing on skills that apply directly to real-world VFX and motion design work. Blender 4.5 is used throughout.

### Key Steps
1. Open Blender 4.5 → select the default cube → go to **Properties > Modifier > Add Geometry Nodes Modifier** → click New
2. In the Geometry Nodes editor: understand left = input geometry, right = output geometry; data flows strictly left to right
3. Open the **Spreadsheet Editor** (split a viewport → change to Spreadsheet) → click on any node to inspect the attribute values at that point in the tree
4. Learn the difference between **Fields** (per-element values like Index, Position) and **single values** (constants like a number you type)
5. First project — Menger Sponge: add **Mesh to Points** → **Instance on Points** (smaller cubes) → use **Boolean** operations or **Delete Geometry** with face domain conditions to remove the center face of each face group
6. Understand **Domain adaptation**: a value in the Point domain automatically adapts when used in a Face domain operation via interpolation
7. Use the **Repeat Zone** (Blender 4.0+) to iterate fractal subdivisions procedurally without manual copy-paste of node groups
8. Use **Node Groups** (Ctrl+G) to encapsulate repeated logic into reusable nodes with clean inputs/outputs

### Nodes / Settings
- Geometry Nodes modifier — add to any object; Input: Group Input (geometry); Output: Group Output
- Spreadsheet Editor — Domain selector (Point / Edge / Face / Corner / Instance); shows all attributes and their values live
- Index node — outputs per-element integer (0, 1, 2…); essential for per-element logic
- Position node — outputs XYZ vector per point; used for spatial operations
- Instance on Points — places any object at each input point; Scale and Rotation can be driven by attributes
- Repeat Zone (Blender 4.0+) — iterates a sub-graph N times for fractal and simulation-like patterns
- Node Groups (Ctrl+G) — encapsulates nodes; Inputs/Outputs become sockets on the group node
- Boolean Math node — And/Or/Not operations on boolean attributes for conditional logic

### Difficulty
Beginner

### Blender Version
4.5

### Tags
#geometry-nodes #procedural #blender-4x #beginner #intermediate

---

## Related Tutorials
- [ALL 300+ Geometry Nodes in Blender](./all-300-geometry-nodes-in-blender.md)
- [Demystifying Geometry Nodes: The Ultimate Guide to Mastering Blender's Procedural Power](./demystifying-geometry-nodes-the-ultimate-guide-to-mastering.md)
- [Geode Nodes (i am so clever) // Blender Tutorial](./geode-nodes-i-am-so-clever-blender-tutorial.md)
- [Math x Blender 5.0 = UNLIMITED POWER!](./math-x-blender-50-unlimited-power.md)
