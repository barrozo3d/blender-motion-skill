---
title: 3D Smoke (Blender Geometry Nodes)
source: YouTube
url: https://www.youtube.com/watch?v=Vqe4jBf3wx4
author: Seanterelle
ingested: 2026-05-19
blender_version: "5.0"
tags: [geometry-nodes, simulation, volumes, advanced]
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
3D fluid smoke simulation entirely in Geometry Nodes using Blender 5.0's Volume Grid nodes and Simulation Zone: a voxel-grid domain (subdivided cube) stores velocity, divergence, pressure, and density fields; each simulation step advects the smoke density by the velocity field and enforces incompressibility; the density field is rendered as a volume.

### Summary
34-minute advanced tutorial implementing a real Eulerian fluid simulation from scratch inside GeoNodes. Uses Blender 5.0's Volume Grid nodes with a Simulation Zone to build a smoke simulator: domain initialization, density emitter (Suzanne head), velocity field setup, pressure projection for incompressible flow, and density advection. The simulation is entirely procedural — no Blender physics engine involved. Advanced content requiring understanding of fluid dynamics concepts.

### Key Steps
1. **Domain setup** — create a cube, subdivide it (many voxels); add GeoNodes modifier; this becomes the simulation domain grid of voxel cells
2. **Volume Grid nodes (Blender 5.0+)** — store fields: velocity (vector), divergence (scalar), pressure (scalar), density/smoke (scalar); each is a `Store Named Attribute` on the voxel grid
3. **Simulation Zone** — use `Simulation Input` / `Simulation Output` nodes; each frame processes the previous frame's state
4. **Emitter** — Suzanne head with its own GeoNodes; use `Volume to Mesh` or point-based injection to write density values into the domain grid where the emitter overlaps
5. **Velocity initialization** — add upward bias to velocity field near emitter; add buoyancy (temperature × up_vector) to make smoke rise
6. **Advection** — sample each voxel's velocity, offset position backward by that velocity × dt, sample the density at that upstream position → new density value (semi-Lagrangian advection)
7. **Pressure projection (incompressibility)** — compute divergence of velocity field; solve pressure (iterative Jacobi iterations inside GeoNodes repeat zone); subtract pressure gradient from velocity → divergence-free velocity
8. **Density dissipation** — multiply density by 0.99 each frame for natural fade-out
9. **Rendering** — use Volume Render material on domain cube; Principled Volume shader with Density input from the smoke attribute; Cycles volume rendering

### Nodes / Settings
- `Volume Grid` nodes (Blender 5.0) — store/load per-voxel data as named attributes
- `Simulation Input` / `Simulation Output` — wraps the per-frame simulation logic
- `Sample Volume` / `Store Named Attribute` — read/write voxel fields
- `Vector Math` — velocity field operations (add, subtract, multiply, normalize)
- `Repeat Zone` — multiple Jacobi pressure solve iterations
- Principled Volume shader: Density (linked to smoke grid attribute), Scatter Color, Emission
- Blender 5.0 required for Volume Grid nodes

### Difficulty
Advanced

### Blender Version
5.0

### Tags
geometry-nodes, simulation, volumes, advanced

---

## Related Tutorials
- [[all-300-geometry-nodes-in-blender]] — reference for Volume Grid and Simulation Zone nodes
- [[organic-liquid-metal-effect-in-blender-50-tutorial]] — another Blender 5.0 volume/SDF technique
- [[using-geometry-nodes-for-vfx-in-blender]] — VFX applications of GeoNodes
