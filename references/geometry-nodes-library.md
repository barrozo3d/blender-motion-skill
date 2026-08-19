---
class: topic-reference
verified: no
sources: []
last_verified: never
version_basis: "unknown"
# WARNING: written from model memory, not ingested from a source.
# Do not cite as authority. If a tutorial disagrees, the tutorial wins.
---
# Geometry Nodes Library

Core GeoNodes techniques for motion design. Each entry includes: what it produces, key nodes used, and a recipe.

---

## Foundational Patterns

### 1. Instance on Points
**What it makes:** Copies of any object placed at each point of a mesh.
**Use for:** Particle fields, forests, crowds, gold dust, chrome balls.
```
Mesh → Distribute Points on Faces → Instance on Points → [geometry to instance]
Key parameters: Density (points/m²), Seed (randomize placement)
Add: Rotate Instances + Random Value for variation
Add: Scale Instances + Random Value for size variation
```

### 2. Curve to Mesh (Tube / Ribbon)
**What it makes:** Geometry following a curve path — tubes, ribbons, cables, veins.
**Use for:** Network connections, DNA, cables, hair strands, fabric.
```
Curve → Curve to Mesh (Profile: Circle curve)
Profile radius controls tube thickness
Resample Curve before for smooth result
Add: Set Curve Radius with noise for organic variation
```

### 3. Mesh to Volume → Volume to Mesh
**What it makes:** Converts geometry to a blobby/volumetric form.
**Use for:** Metaball-like effects, organic growth, liquid reveal.
```
Mesh → Mesh to Volume (Voxel Size: 0.01–0.05) → Volume to Mesh
Lower voxel size = more detail but slower
Add noise to volume for organic irregularity
```

### 4. Geometry Nodes Simulation Zone (Blender 4.0+)
**What it makes:** Frame-by-frame simulation entirely in GeoNodes.
**Use for:** Particle systems, fluid-like motion, growing networks, physics-lite.
```
Simulation Input → [per-frame logic] → Simulation Output
Inside: Translate Instances (by velocity), Set Position + noise
Use: Accumulate Field for memory across frames
Warning: requires Blender 4.0+ — check version
```

### 5. Attribute Transfer / Sample Nearest Surface
**What it makes:** Reads data from one mesh onto another.
**Use for:** Color transfer, velocity-driven deformation (Albin's advection).
```
Object Info → Sample Nearest Surface → [attribute name]
Use velocity from pyro sim to drive Set Position on curves
This is the core of Albin Merle's fluid advection technique
```

---

## Growth & Reveal Patterns

### 6. Trim Curve (Drawing/Growth)
**What it makes:** Progressively reveals a curve from start to end.
**Use for:** Logo draw-on, writing animation, circuit trace, growth.
```
Curve → Trim Curve (Start: 0, End: animated 0→1) → Curve to Mesh
Animate End value with ease-in for organic growth feel
Add Set Curve Radius for tapering at tip
```

### 7. Recursive Subdivision Growth
**What it makes:** Fractal subdivision that grows outward from a center.
**Use for:** Crystalline growth, circuit board expansion, fractal reveals.
```
Mesh → Subdivide Mesh (Level: driven by time) → 
Select by proximity to center → Scale/extrude selected faces
Use GeoNodes groups recursively (reference: Albin's recursive subdivision video)
```

### 8. Point Cloud Spread (Clock-based)
**What it makes:** Points that "infect" neighbors over time — organic spread.
**Use for:** Solar eruption, network propagation, viral spread visualization.
```
Single reference point → Simulation Zone
Each frame: find nearest points → check distance → flag as "active"
Active points push neighbors using Set Position
This is Albin Merle's solar eruption technique (file 053)
```

### 9. Geometry Nodes L-System (Branching/Fern)
**What it makes:** Recursive branching structures — trees, ferns, coral.
**Use for:** Nature growth, vascular systems, data tree visualization.
```
Start: single curve segment
Group: "Branch" — takes curve, adds child curves at angle
Repeat Input → Branch Group → Repeat Output
Control: branch angle, length decay, iteration count
Reference: Albin's "Blender Fern growing" video
```

---

## Fluid & Simulation-Driven Patterns

### 10. Fluid Velocity Advection (Albin's Signature)
**What it makes:** Geometry deformed/moved by smoke/fluid velocity field.
**Use for:** Metal that flows, cloth moved by wind, particles in current.
```
Step 1: Create 2D Pyro sim (A.lbos addon recommended, or built-in smoke)
Step 2: Bake simulation
Step 3: In GeoNodes: Object Info (pyro domain) → Sample Volume
Step 4: Sample velocity attribute from volume
Step 5: Add velocity to curve control point positions
Step 6: Curve to Mesh → metallic material
Result: curves that flow like smoke but look like metal sheets
Note: A.lbos 2D Pyro Solver addon dramatically improves 2D sim quality
```

### 11. Particle Vortex / Spiral
**What it makes:** Particles spiraling toward or away from a center.
**Use for:** Gold dust gathering, particle explosions, material dissolves.
```
Distribute Points → Simulation Zone
Per frame: rotate points around Z axis (angle += speed)
Add: pull toward center (Set Position toward object origin)
Add: noise displacement for organic feel
Render as tiny sphere instances with metallic material
```

### 12. Liquid Surface (Mesh from Particles)
**What it makes:** Smooth liquid surface from particle simulation.
**Use for:** Pouring liquid, liquid splash, growing blob.
```
Particle system (Fluid domain) → 
Mesh to Volume (from particle system via GeoNodes) →
Volume to Mesh → Smooth modifier → liquid shader
OR: Use Mantaflow liquid simulation directly (simpler setup)
```

---

## Material-Driven Geometry

### 13. Displacement + Noise (Procedural Terrain)
**What it makes:** Organic bumpy surface from mathematical noise.
**Use for:** Planet surfaces, abstract terrain, skin-like surfaces.
```
Subdivision Surface (high level) → 
Displace Modifier (Texture: clouds/noise, Strength: 0.1–2.0)
In GeoNodes: Set Position += Normal × noise texture output
```

### 14. Boolean Operations (Hard Surface Cuts)
**What it makes:** Geometry subtracted or intersected with another shape.
**Use for:** Industrial cutouts, logo integration, precision holes.
```
Mesh Boolean node: Operation (Union/Difference/Intersect)
Add Mesh Boolean modifier stack for complex operations
Manifold Solver (Blender 4.5+): better results on difficult booleans
```

### 15. Knit Curves (Fabric)
**What it makes:** Woven/knitted surface from thousands of curves.
**Use for:** Fabric, textile, sweater, polo shirt (Albin's Eden Park).
```
Grid mesh → Distribute Points on Faces →
At each point: orient curve to UV direction →
Scale curve to stitch length →
Curve to Mesh (circle profile, tiny radius) →
Principled Hair shader for realism
Deform base grid with Cloth simulation → fabric drape
```

---

## Text & Logo Techniques

### 16. Text Object + Geometry Nodes
**What it makes:** 3D text treated as geometry for effects.
**Use for:** Logo reveals, title animations.
```
Add Text → Convert to Mesh (for GeoNodes) →
OR: use Text object directly with GeoNodes modifier
Separate by material to isolate individual letters
Then: apply effects per-letter (instance, scatter, animate)
```

### 17. Wireframe from Mesh
**What it makes:** Wireframe/outline version of any geometry.
**Use for:** Wireframe reveals, technical/blueprint aesthetic.
```
Mesh → Wireframe node (GeoNodes) → Curve to Mesh
OR: Wireframe modifier → adjust thickness
Control: display as curves with hair shader for fine lines
```

---

## Camera & Procedural Animation

### 18. Noise-Driven Animation
**What it makes:** Organic procedural movement without keyframes.
**Use for:** Breathing objects, subtle vibration, organic drift.
```
Object → GeoNodes modifier →
Set Position: original + (Noise Texture × scale vector)
Animate noise W input for motion over time
Scale controls amplitude of movement
```

### 19. Easing Functions in GeoNodes
**What it makes:** Smooth, eased values for driving animation.
```
Map Range node: From Min/Max [0,1] → To Min/Max [start, end]
Interpolation Type: Smoothstep or Smoother Step for ease in/out
Drive with scene time or custom float input
```

### 20. Point Cloud Rendering
**What it makes:** Renders geometry as points instead of mesh faces.
**Use for:** Particle clouds, atomic/molecular visualization, digital noise.
```
GeoNodes → output Points (not Mesh)
Viewport Overlays → Point Cloud display
Render: Cycles handles point clouds natively (Blender 3.5+)
Control size: Set Point Radius node
Shader: applied to points directly (Principled BSDF on point cloud)
Reference: Albin's Chrome Ball simulation (file 052)
```

---

## Version-Specific Features

### Simulation Zone (4.0+)
Required for any frame-by-frame GeoNodes simulation. Not available in Blender 3.x — use particle system instead.

### Repeat Zone (4.1+)
Loop a GeoNodes subgraph N times in a single frame. Used for recursive operations (L-systems, subdivisions).

### Set Mesh Normal (4.5+)
Custom normals directly in GeoNodes. Allows blending intersecting objects into one continuous surface.

### File Import Nodes (4.5+)
Import OBJ, CSV, VDB, STL directly via GeoNodes. Enables data-driven geometry from external files.
