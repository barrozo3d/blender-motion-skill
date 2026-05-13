# Blender Version Reference

When recommending workflows, always identify which version introduced each feature. Suggest the newest LTS unless the user specifies otherwise.

---

## Current Recommended Versions

| Version | Status | Recommendation |
|---|---|---|
| **4.5 LTS** | Current LTS (Jul 2025) | **Default recommendation** — stable, 2yr support |
| 4.4 | Stable | Good if user already on it |
| 4.2 LTS | Previous LTS | Many tutorials still reference this |
| 3.6 LTS | Legacy | Older tutorials, some addons still target this |
| 3.x general | Legacy | Missing Simulation Zone and many GeoNodes features |

---

## Feature Availability by Version

### Geometry Nodes

| Feature | Introduced | Notes |
|---|---|---|
| Geometry Nodes (basic) | 2.92 | Instance on Points, basic modifiers |
| Fields system | 3.0 | Complete redesign — most modern tutorials assume 3.0+ |
| Realize Instances | 3.0 | Essential for converting instances to real geometry |
| Simulation Zone | 4.0 | **Critical** — enables frame-by-frame GeoNodes simulation |
| Repeat Zone | 4.1 | Loop within GeoNodes; recursive operations |
| Bake GeoNodes | 4.1 | Cache simulation results for performance |
| Set Mesh Normal | 4.5 | Custom normals in GeoNodes; intersecting objects blend |
| File Import Nodes | 4.5 | OBJ/CSV/VDB/STL import via nodes |
| Grease Pencil in GeoNodes | 4.3+ | GP stroke creation and editing via nodes |

### Rendering

| Feature | Introduced | Notes |
|---|---|---|
| Cycles X (rewrite) | 3.0 | Massive speed improvement over old Cycles |
| EEVEE Next | 4.2 | Complete rewrite; global illumination, reflections |
| AgX color transform | 3.5 | Better highlight rolloff than Filmic |
| Point cloud rendering | 3.5 | Render GeoNodes point output natively |
| Adaptive subdivision motion blur | 4.5 | Fixes artifacts on animated subdivision surfaces |
| Vulkan backend | 4.5 | Production-ready, better viewport performance |
| GPU denoising (OIDN) compositor | 4.5 | Faster denoising in compositor |

### Animation

| Feature | Introduced | Notes |
|---|---|---|
| NLA editor improvements | 3.x+ | Ongoing |
| Bone collections | 4.0 | Replaces bone layers |
| Timeline snap to any element | 4.5 | Snap playhead to any visible marker |

### Materials & Shading

| Feature | Introduced | Notes |
|---|---|---|
| Principled BSDF v2 | 4.0 | New coat and sheen parameters |
| Principled Hair | 3.5 | Replaces old hair BSDF |
| Light Temperature (Kelvin) | 4.5 | Set light color via Kelvin directly |
| Light Normalize | 4.5 | Prevents intensity change during scaling |
| Light Exposure parameter | 4.5 | Scene-wide simultaneous exposure adjust |

### Import/Export

| Feature | Introduced | Notes |
|---|---|---|
| FBX C++ importer | 4.5 | 3–15× faster than previous Python importer |
| glTF improvements | ongoing | Better material support each version |
| USD improvements | 4.x+ | Growing USD pipeline support |

---

## Version Migration Notes

### If a tutorial says "3.6"
- Most Modifier and GeoNodes setups still work in 4.x
- Exception: if it uses "Attribute" nodes (old system) — needs remapping to Fields
- If it uses Simulation Zone: requires 4.0+

### If a tutorial says "4.2"
- Fully compatible with 4.5
- EEVEE settings may look different (EEVEE Next redesign)
- GeoNodes setups work identically

### If a tutorial says "4.0–4.4"
- Fully compatible with 4.5
- Can benefit from 4.5 additions (Set Mesh Normal, file nodes, etc.)

### Common Breaking Changes
- **3.x → 4.0**: Principled BSDF changed (Coat/Sheen params new), some deprecated nodes
- **3.x → 4.0**: Simulation Zone introduced — older particle-only workflows may be richer now
- **3.x → 4.2**: EEVEE rewritten (EEVEE Next) — material settings differ slightly
- **Attribute system (2.x) → Fields (3.0+)**: Old "Attribute" node replaced by named attribute access

---

## Recommended Stack for Ad/Motion Design (2025–2026)

```
Blender 4.5 LTS
├── Renderer: Cycles X
├── Denoiser: Open Image Denoise (OIDN) — GPU accelerated in compositor (4.5)
├── Color: AgX view transform
├── GeoNodes: Simulation Zone + Repeat Zone
├── Physics: Mantaflow (fluid/smoke), Bullet (rigid body), built-in cloth
├── Compositing: Blender compositor → export EXR → After Effects
└── Hardware: RTX 4090 / RTX 5070 (CUDA for Cycles GPU)
```

---

## Key Addons Referenced by Albin Merle

| Addon | What it does | Where to get |
|---|---|---|
| A.lbos 2D Pyro Solver | High-quality 2D smoke/fire simulation | Paid, Blender Market |
| Havard Dalen Lens Sim | Physically-based lens simulation for renders | Paid |
| Caramel Cartesian | Parallax mapping tools | Community |
| Poly Haven asset browser | Free HDRI, textures, models | polyhaven.com / built into Blender |

---

## Useful Blender Resources

| Resource | What it covers |
|---|---|
| blender.org/download | Official downloads, release notes |
| docs.blender.org | Official manual (most up to date) |
| polyhaven.com | Free HDRI, textures, models |
| blendermarket.com | Paid addons |
| blenderartists.org | Community forum, WIP threads |
| Entagma (YouTube) | Advanced GeoNodes, procedural techniques |
| Default Cube (YouTube) | GeoNodes tutorials, creative experiments |
| Grant Abbitt (YouTube) | Modeling, beginner-friendly |
| Blender Secrets (YouTube) | Quick tips, shortcuts |
