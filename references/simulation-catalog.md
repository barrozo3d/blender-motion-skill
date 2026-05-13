# Simulation Catalog

Recipes for every major simulation type in Blender, focused on motion design output.

---

## Smoke / Pyro (Mantaflow)

### Basic Smoke Setup
```
1. Object (emitter) → Physics → Fluid → Flow Type: Smoke
2. Domain object (cube around scene) → Physics → Fluid → Type: Domain → Smoke
3. Domain: Resolution Divisions 64–256 (higher = more detail, slower)
4. Bake: Physics → Fluid → Bake Data
5. Material on domain: Principled Volume shader
   Density: driven by "density" attribute
   Color: driven by "flame" attribute for fire
```

### 2D Pyro (Albin's technique)
- A.lbos 2D Pyro Solver addon creates high-quality 2D smoke in a plane
- Sample velocity attribute from baked domain to drive GeoNodes deformation
- Result: geometry that moves like smoke — fluid advection

### Smoke Render Settings
```
Cycles: 256–512 samples minimum for clean volume
Volume Sampling: Step Rate 0.1 (lower = slower but better)
Volume Bounces: 2–4
```

---

## Fluid (Liquid) — Mantaflow

### Liquid Splash/Pour
```
1. Emitter: Flow Type → Liquid, Flow Source → Mesh
2. Domain: Type → Domain, Domain Type → Liquid
3. Mesh: enable "Mesh" in Liquid settings for smooth surface
4. Resolution: 64–128 (liquid needs high res for detail)
5. Bake Mesh separately after Baking Data
6. Material: Principled BSDF, Transmission 1.0, IOR 1.33 (water)
```

### Liquid in Container (Filling)
```
- Emitter inside container, set as Inflow type
- Container as collision object (Physics → Fluid → Effector)
- Animate emitter strength from 1→0 to stop flow
- Bake at resolution 128+ for clean meniscus
```

---

## Rigid Body

### Falling/Shattering Objects
```
1. Select objects → Physics → Rigid Body → Active
2. Ground/surfaces: Rigid Body → Passive
3. Cell Fracture addon (built-in): Object → Quick Fracture → pre-shatters mesh
4. Animate: set Animated=True for frames before impact, False after
5. Bake: Scene → Rigid Body World → Bake
```

### Marble/Ball Simulation
```
- Sphere: Rigid Body → Active → Shape: Sphere (most accurate)
- Friction, Damping: tune for material feel
  Chrome/metal: Friction 0.1, Damping 0.1 (bouncy)
  Rubber: Friction 0.8, Damping 0.5 (sticky, less bounce)
- Reference: Albin's Chrome Ball simulation
```

---

## Cloth

### Fabric Drape
```
1. Plane mesh (subdivided) → Physics → Cloth
2. Subdivide: 50×50 minimum for smooth drape
3. Quality: 10–15 steps for accurate result
4. Collision object: Physics → Collision
5. Bake: Object → Apply → Visual Geometry (to freeze)
6. Shape key workflow: bake multiple drape positions as shape keys
```

### Knitted Fabric (Albin's polo shirt technique)
```
1. Low-res cloth sim for overall drape shape
2. GeoNodes on deformed mesh:
   - Distribute points on faces
   - At each point: create curve segment aligned to UV
   - Curve to Mesh with circle profile (tiny radius)
   - Principled Hair BSDF on curves
3. The cloth sim drives shape; GeoNodes adds fiber detail
```

---

## Particles

### Particle System (legacy, still useful)
```
Object → Particles → Add
Types:
- Emitter: burst or continuous emission from surface
- Hair: static strands growing from surface

Key settings:
- Number: 1000–100000 depending on density needed
- Lifetime: frames each particle lives
- Emit From: Face (surface scatter) vs Volume (internal)
- Physics: Newtonian (gravity, wind) vs Keyed (path-following)
```

### Particles + GeoNodes (modern approach)
```
Particle system → GeoNodes modifier reads particle positions
OR: replace entirely with GeoNodes Simulation Zone
Advantage: full procedural control, no baking needed
Disadvantage: no collision physics (must fake with GeoNodes)
```

### Gold Dust Effect (Albin's particle vortex, file 049)
```
1. GeoNodes Simulation Zone
2. Start: distribute points on surface of logo mesh
3. Per frame: 
   - Rotate points around center (Z axis, speed: 0.02 rad/frame)
   - Add slight upward drift (Z velocity += 0.001)
   - Add noise displacement (scale 0.5, strength 0.002)
4. Instance: tiny UV sphere (radius 0.001m) on each point
5. Material: Principled BSDF, Metallic=1, Roughness=0.05, Base Color: gold
6. Render: Cycles, point cloud mode for performance with 100k+ particles
```

---

## Soft Body

### Jelly/Elastic Object
```
Object → Physics → Soft Body
Goal: 0 (fully elastic) to 1 (rigid)
Edges: Stiffness controls resistance to stretching
Bending: Stiffness for bending resistance
Collision: enable for interaction with other objects
Use case: bouncing logos, jelly reveals, elastic deformation
```

---

## Force Fields

### Wind
```
Add → Empty → Physics → Force Field → Wind
Strength: how much force
Noise: adds turbulence to wind
Direction: follows Empty rotation
Apply to: particles, cloth, soft body
```

### Vortex (Spiral motion)
```
Force Field → Vortex
Creates spiral pull toward the field center
Great for: particles spiraling into a logo reveal
Strength: positive = inward spiral, negative = outward explosion
```

### Turbulence
```
Force Field → Turbulence
Adds random chaotic force to particles/cloth
Use with particles for organic cloud-like behavior
Combine with Wind for directional turbulence
```

---

## Simulation Performance Tips

| Goal | Approach |
|---|---|
| Fast iteration | Low resolution domain (32–64), bake, preview |
| Final quality | High resolution (128–256+), re-bake |
| Very slow sim | Split into passes: bake sim first, then render |
| Cache size too large | Use OpenVDB format (compressed) |
| GeoNodes sim too slow | Bake in GeoNodes (4.1+ Bake node) |
| Render farm | Bake locally, render on farm (farm doesn't need to simulate) |
