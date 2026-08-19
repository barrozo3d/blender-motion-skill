---
class: topic-reference
verified: no
sources: []
last_verified: never
version_basis: "unknown"
# WARNING: written from model memory, not ingested from a source.
# Do not cite as authority. If a tutorial disagrees, the tutorial wins.
---
# Blender Version Reference

When recommending workflows, always identify which version introduced each feature. Suggest the newest LTS unless the user specifies otherwise.

---

## Current Recommended Versions

| Version | Status | Recommendation |
|---|---|---|
| **5.2 LTS** | Current latest, LTS (2026) | **Use for new projects** — latest features AND long-term support; XBPD cloth/hair dynamics (experimental), GN Bundles/Lists, sound sampling |
| 5.1 | Stable (Mar 2026) | Good; EEVEE planar reflections |
| 5.0 | Stable (Nov 2025) | Good; first 5.x release, volume GeoNodes, null scattering |
| **4.5 LTS** | LTS (Jul 2025) | **Use for stability** — 2yr support, safest for production |
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
| Volume Grid data type | 5.0 | OpenVDB grids in GeoNodes — native volumetric workflows |
| SDF nodes (Laplacian/Median) | 5.0 | Signed distance field processing — curvature flow, noise reduction |
| Closures & Bundles (stable) | 5.0 | No longer experimental; also available in Shader Nodes |
| UV Tangent node | 5.0 | Access tangent vectors on mesh for advanced shading |
| Essential Assets (built-in node groups) | 5.0 | Scatter on Surface, Instance on Elements, Randomize Instances, Flexible Array |
| Bone Info node | 5.1 | GeoNodes access to armature bone transforms (Pose, Rest, etc.) |
| Volume grid manipulation nodes | 5.1 | Dilate, erode, clip volume grids procedurally |
| Mesh Island & Matrix sockets | 5.1 | Advanced procedural workflows, matrix math in nodes |
| XPBD Solver node (Cloth/Hair Dynamics modifiers) | 5.2 | Experimental — generalized physics with custom forces |
| Bundles attached to geometry | 5.2 | Set/Get Geometry Bundle — arbitrary data across modifier/object boundaries |
| Lists data type | 5.2 | Field to List, Closure to List, List Length, Get/Filter/Sort List, Collection Children |
| Sound socket + Sample Sound Frequencies | 5.2 | Audio-reactive setups: amplitude/frequency-range sampling |
| GN on Empty objects | 5.2 | Enables GN on collection instances |
| Mesh Bevel node | 5.2 | Modifier-grade bevel with per-edge offsets and selection outputs |
| Merge-by-Distance building blocks | 5.2 | Merge Points, Cluster by Distance, Cluster by Connected |
| NURBS Order/Weight, string nodes, recursive closures | 5.2 | See everything-new-in-blender-52-geometry-nodes.md |

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
| Null scattering volumes (Cycles) | 5.0 | Reduces overlapping volume artifacts; simpler parameter tuning |
| Thin-film iridescence | 5.0 | Metallic BSDF shader support for iridescent surfaces |
| OptiX Denoiser improvements | 5.0 | Cleaner, more stable results on NVIDIA GPUs |
| Render Time Pass | 5.0 | Per-pixel render time data as a render pass |
| EEVEE planar reflections (glossy+refraction) | 5.1 | Accurate planar reflections with glossy and refraction support |
| EEVEE shader pre-processing | 5.1 | GPU shaders compile 25–50% faster |
| EEVEE texture pooling | 5.1 | Reduces VRAM use for large scenes |
| Cycles GPU improvement | 5.1 | ~5–10% speed gain across most scenes |
| HIP RT ray tracing (AMD) | 5.1 | Enabled by default on AMD GPUs |

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
| Metallic BSDF thin-film | 5.0 | Iridescence on metallic surfaces |
| Raycast shader node | 5.1 | Shoot a ray, get surface info back — enables toon shading, X-ray effects |

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

### If a tutorial says "5.0"
- Fully compatible with 5.1
- Volume Grid nodes, null scattering, and Closures available
- Essential Assets (built-in GeoNodes modifiers) available

### If a tutorial says "5.1"
- Fully compatible with 5.2 LTS

### If a tutorial says "4.5"
- Fully compatible with 5.0, 5.1, and 5.2
- Can benefit from 5.x additions (volume GeoNodes, iridescence, EEVEE planar reflections)

### Common Breaking Changes
- **3.x → 4.0**: Principled BSDF changed (Coat/Sheen params new), some deprecated nodes
- **3.x → 4.0**: Simulation Zone introduced — older particle-only workflows may be richer now
- **3.x → 4.2**: EEVEE rewritten (EEVEE Next) — material settings differ slightly
- **Attribute system (2.x) → Fields (3.0+)**: Old "Attribute" node replaced by named attribute access

---

## Recommended Stack for Ad/Motion Design (2026)

**For new projects (cutting-edge — 5.2 is both latest and LTS):**
```
Blender 5.2 LTS
├── Renderer: Cycles X or EEVEE Next (planar reflections, faster shaders)
├── Denoiser: OptiX (NVIDIA) — improved stability in 5.0+
├── Color: AgX view transform
├── GeoNodes: Simulation Zone + Repeat Zone + Volume Grids + Closures
├── Physics: Mantaflow (fluid/smoke), Bullet (rigid body), built-in cloth
├── Compositing: Blender compositor → export EXR → After Effects
└── Hardware: RTX 5070 (CUDA for Cycles GPU)
```

**For production stability:**
```
Blender 4.5 LTS
├── Renderer: Cycles X
├── Denoiser: Open Image Denoise (OIDN) — GPU accelerated in compositor
├── Color: AgX view transform
├── GeoNodes: Simulation Zone + Repeat Zone
├── Physics: Mantaflow (fluid/smoke), Bullet (rigid body), built-in cloth
├── Compositing: Blender compositor → export EXR → After Effects
└── Hardware: RTX 5070 (CUDA for Cycles GPU)
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
