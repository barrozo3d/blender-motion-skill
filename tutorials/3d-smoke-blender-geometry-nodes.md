---
title: 3D Smoke (Blender Geometry Nodes)
source: YouTube
url: https://www.youtube.com/watch?v=Vqe4jBf3wx4
author: Seanterelle
ingested: 2026-05-18
blender_version: "5.0"
tags: ["geometry-nodes", "simulation", "smoke-fire", "volume", "blender-5x", "advanced"]
extraction_status: complete
frames_dir: tutorials/frames/3d-smoke-blender-geometry-nodes/
frame_count: 0
---

# 3D Smoke (Blender Geometry Nodes)

**Source:** [YouTube](https://www.youtube.com/watch?v=Vqe4jBf3wx4)
**Author:** Seanterelle
**Duration:** 34m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hello everybody and welcome to this geometry notes tutorial in Blender 5.0 using the new volume grid nodes, new ish, it's been a while since they came out actually. But nonetheless, we're going to be making this 3D smoke with geometry nodes. So, let's get into it. The basic structure of this whole thing is that we're going to have a simulation zone here, represented by this cube, and we've got an emitter, which is going to be Suzanne. They've got their own geometry nodes networks that I'll explain. Basically, we're going to set up a domain, which is going to be this cube, just subdivided into a bunch of little voxel cubes. Then, we are going to do something really similar to the 2D fluid simulation tutorial that I had a long time ago, where we're using a couple different fields, velocity divergence, pressure, and then a density field which we're actually calling smoke. Here, that smoke field is what you actually see. Then, we're essentially creating forces, enforcing incompressibility in the fluid, and watching the density or the smoke evolve over time. So, that's our basic setup. We have our initialization here, we have our simulation here, and then a little bit of post-processing...



---

## Structured Notes

### Core Technique
Physically-based 3D smoke simulation in Blender 5.0 using Geometry Nodes volume grid nodes inside a Simulation Zone — implementing velocity, divergence, pressure, and density fields with variable solver resolution.

### Summary
Seanterelle builds a real fluid simulation from scratch using Blender 5.0's volume grid nodes in Geometry Nodes. The setup uses a Simulation Zone with a subdivided cube as the domain and Suzanne as the emitter. Implements a proper CFD-style solver: density (smoke), velocity field, divergence, and pressure fields. The simulation resolution can be lowered for interactive preview and raised for final quality bake.

### Key Steps
1. Create domain cube → subdivide → inside Geometry Nodes add **Simulation Zone** → the subdivided cube becomes the voxel grid
2. Create emitter object (Suzanne) with its own GeoNodes that output point positions as smoke source
3. Inside Simulation Zone: create **Grid** nodes for each field — density (smoke), velocity (vector), divergence (float), pressure (float)
4. Initialize velocity from emitter: sample emitter position → drive velocity field outward
5. Enforce incompressibility: compute divergence of velocity → solve pressure (Jacobi iterations) → subtract pressure gradient from velocity
6. Advect density: move density values along velocity field using trilinear interpolation
7. Expose **solver resolution** as a Group Input — low value (e.g. 32³) for viewport preview, high (e.g. 128³) for final bake
8. Post-process: clamp density, apply volume material with absorption and scatter
9. Bake simulation using Geometry Nodes bake operator; output as VDB for rendering

### Nodes / Settings
- Simulation Zone — core node group; state persists across frames
- Grid nodes (Blender 5.0) — store float/vector values per voxel; new in 5.0
- Sample Grid — read grid value at world position
- Store Named Attribute — write computed field values back to grid
- Group Input — expose Resolution parameter (default 32, final 128+)
- Volume Scatter + Volume Absorption — smoke material; Density: linked to smoke grid
- Object Info → Position — get emitter position for velocity sourcing

### Difficulty
Advanced

### Blender Version
5.0

### Tags
#geometry-nodes #simulation #smoke-fire #volume #blender-5x #advanced

---

## Related Tutorials
[PENDING EXTRACTION]
