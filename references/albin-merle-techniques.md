---
class: topic-reference
verified: partial
sources:
  - tutorials/  (corroboration audit, batch B5 -- see note)
last_verified: 2026-08-19
version_basis: "unknown"
# Origin: model memory. Audited 2026-08-19 (batch B5) -- see note below.
# Parameters/API symbols remain unverified. Tutorial beats reference.
---
> ## Audit note — batch B5, 2026-08-19
>
> UNMEASURABLE — coverage 2. This documents one artist's techniques, so thin corpus overlap is inherent, not suspicious.
>
> **Method and its ceiling.** Terms were checked against this skill's ingested
> tutorials (and its vendor release-notes references) with `audit_references.py`.
> That corpus is spoken narration, so it corroborates what presenters **say** —
> node and tool names — and structurally cannot corroborate what they only
> **show or type**: parameter names, defaults, console variables, API symbols.
> **Corroboration finds fabricated names, not wrong values.**
>
> Full detail: `houdini-wand/PROMO_ENTRY_CLEANUP_PLAN.md` (workstream B).

# Albin Merle Techniques

Quick reference for Albin Merle's specific setups. Full analysis: see memory file `albin_merle_analysis.md`.

---

## Signature Technique 1: Fluid Velocity Advection

**Videos:** "Blender Geometry Nodes Fluid advection" (2uF0-jIYtoM), "Blender Fluid Advection Macro" (uvhUuqWrOgY)
**Blend files:** 058, 059

**What it looks like:** Metal sheets or surfaces that flow and deform like smoke.

**Recipe:**
```
1. 2D Pyro simulation (A.lbos addon or built-in smoke)
   → 2D setup: domain very thin on one axis
   → Bake: Data + Noise
2. GeoNodes modifier on curve/mesh geometry:
   → Object Info (pyro domain) → Sample Volume → velocity attribute
   → Add velocity × strength to Set Position
3. Curve to Mesh → metallic material (polished gold/chrome)
4. Render: Cycles, high samples, motion blur on
Result: curves that flow like smoke but look like solid metal
```

**Key addon:** A.lbos 2D Pyro Solver (dramatically improves 2D sim quality)

---

## Signature Technique 2: Knit/Fabric from Curves

**Video:** "Eden Park Polo Shirt" (2-aptv-jblA)
**Blend file:** shared via Linktree

**What it looks like:** Dense woven fabric where each thread is visible as 3D geometry.

**Recipe:**
```
1. Low-res mesh (base shape of garment)
2. Cloth simulation on base mesh → bake drape shape
3. GeoNodes on draped mesh:
   → Distribute Points on Faces (density: 200–500/m²)
   → Align each point to UV direction
   → Create short curve at each point
   → Curve to Mesh (circle profile, radius ≈ 0.0003m)
4. Material: Principled Hair BSDF
5. No texture maps — pure geometry
```

---

## Signature Technique 3: Procedural Clock Spread

**Video:** "Blender Solar eruption" (beVe7oyosO0)
**Blend file:** 053

**What it looks like:** Points that activate and spread outward like an eruption or viral spread.

**Recipe:**
```
1. GeoNodes: point cloud on sphere or flat plane
2. Single reference point: random position switch each frame
3. Each point samples distance to reference point
4. If distance < radius: become "active" (scale, color, or position change)
5. Radius grows over time: creates expanding activation front
6. No simulation zone needed — fully procedural
```

---

## Signature Technique 4: Recursive Subdivision

**Video:** "Blender recursive subdivision" (UBxXyiwL-Xc)
**Blend file:** available

**What it looks like:** Fractal-like geometry that subdivides into smaller and smaller elements.

**Recipe:**
```
1. GeoNodes Group: "Subdivide Once"
   → Input mesh → Subdivide Mesh → select new face centers
   → Scale selected faces inward → output
2. Repeat Zone (Blender 4.1+): repeat the group N times
3. Animate N or the scale factor over time for reveal
4. Or: use instancing instead of Repeat for performance
```

---

## Signature Technique 5: AI-Aesthetic (Procedural)

**Video:** "Blender Fluid Advection Macro" (uvhUuqWrOgY)
**Blend file:** 059

**What it looks like:** Hyper-sharp, extreme contrast, surreal detail — like an AI image but fully 3D.

**Recipe:**
```
Post-processing stack:
1. Advanced denoising + sharpening in compositor
2. Surreal camera: very close, unusual angles
3. Parallax mapping (Caramel Cartesian addon)
4. Overscaled motion blur (high shutter angle)
5. Velocity tricks (Cyril Muller method)
6. Lens simulation (Havard Dalen Lens Sim addon)
7. Graded in After Effects
Key insight: the "AI look" is achievable with pure Blender
```

---

## Signature Technique 6: Point Cloud Rendering

**Video:** "Blender Chrome Ball simulation" (YbZ6JfwOb2Q)
**Blend file:** 052

**What it looks like:** Thousands of metallic spheres behaving with physics (repulsion, collision).

**Recipe:**
```
1. GeoNodes Simulation Zone
2. Each point: sphere instance, with velocity attribute
3. Per frame: calculate repulsion from neighbors (Sample Nearest)
4. Update positions by velocity + repulsion force
5. Render as Point Cloud (Cycles natively renders points)
6. Material on points: Principled BSDF, Metallic=1, Roughness=0.05
7. Note: inspired by Sean Terelle's method
```

---

## Albin's Standard Render Settings
```
Engine: Cycles X
Samples: 1024–2048
Denoiser: OIDN
Compositor: Blender compositor (initial) → After Effects (final grade)
Hardware: RTX 4090 (CUDA)
Render farm: LeTruc Studio (for heavy pieces)
Blender version: 4.2 → 4.5 (updating per project)
```

## Albin's Audio Collaboration (Liam Phan)
```
Process: visuals and sound co-developed in parallel
Not: music added after render
Liam's role: field recording → granular processing → spatial sound design
Albin's role: visual responds to audio rhythm and texture
Result: audiovisual pieces where image and sound are structural, not illustrative
Key: send WIP renders during production, not just finished piece
```

## File Numbering System
Albin shares Blend files numbered sequentially (File 041–068+).
Available via: linktr.ee/albinmerle (Dropbox folder)
When a technique references a file number: check there for the actual .blend.
