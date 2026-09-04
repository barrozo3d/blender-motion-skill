---
title: "Frozen Motion Blur Bridge — Geo Nodes Breakdown"
blender_version: "4.x / 5.x"
tags: [geometry-nodes, motion-blur, procedural, animation, scene-time, glass, displacement, intermediate, advanced, albin-merle]
source: direct-file-analysis
url: https://www.youtube.com/watch?v=675BOBWbTt4
author: Albin Merle
extraction_status: complete
---

# Frozen Motion Blur Bridge — Geo Nodes Breakdown

## Raw Data

*Source: direct-file-analysis — no YouTube transcript.*

## Overview

Procedural frozen motion blur effect applied to a bridge mesh using Geometry Nodes. The effect creates an oscillating displacement that simulates frozen/smeared motion blur — a signature Albin Merle technique. Fully automatic: no keyframes needed on the effect; driven entirely by Scene Time nodes reading the current frame.

**File:** `061_AM_Frozen_motion_Blur_Bridge`  
**Node group:** `Frozen_MotionBlur`  
**Applied to:** `P010_Geo_Bridge` (a 4-vertex plane as modifier input)  
**Total nodes:** 50

---

## Core Technique

Two Scene Time nodes read the current frame and drive two Mix nodes that blend between X-axis and Z-axis displacement vectors. The blended vector is scaled by a height-based Map Range mask and stored as a Named Attribute, which the Glass material reads to produce the smeared blur look.

---

## Animation Chain (Scene Time → Motion Vectors)

```
Scene Time.004.Frame  ÷ 45  →  Group.006  →  Mix.005.Factor
Scene Time.005.Frame  ÷ 24  →  Group.007  →  Mix.004.Factor
```

- **Group.006 / Group.007** — sub-node-groups that take float `W` (normalized time) and output a 0–1 oscillating factor
- **Mix.004** blends between:
  - A = `Combine XYZ.006` = `(0, 0, 10)` — Z-axis displacement
  - B = `Combine XYZ.005` = `(10, 0, 0)` — X-axis displacement
  - Factor driven by `frame ÷ 24`
- **Mix.005** further blends Mix.004's result
  - Factor driven by `frame ÷ 45`

Two different oscillation speeds (÷24 and ÷45) layer to create a complex, non-repeating motion feel.

---

## Displacement Output Chain

```
Mix.005.Result
  → Vector Math.008 (SCALE operation)
      Vector:  Mix.005.Result
      Scale:   Map Range.001.Result  [× Strength if modified]
  → Store Named Attribute  (×2, for viewport and render)
```

### Height Mask — Map Range.001

Reads Z position of each vertex relative to the ground reference object and fades the blur in only above ground level:

```
Position.001 → Vector Math.005 (subtract Object Info.001.Location)
  → Separate XYZ.001 → Z
  → Map Range.001
      From Min: 0.1 | From Max: 0.2
      To Min:   0.0 | To Max:   1.0
  → Vector Math.008.Scale
```

Effect: blur is zero below Z=0.1, fully active above Z=0.2 world units. Adjust these values if using a mesh with different proportions.

---

## Subdivision Control

```
Is Viewport → Switch → Clamp (Min=0, Max=11) → Subdivide Mesh.Level
```

Subdivision capped at 11. Viewport/render mode toggles via Is Viewport for performance.

---

## Key Dependencies

### 1. Collection Info → `Old_Bridge` collection
The actual 3D bridge geometry does NOT come from the modifier's Geometry input (which is just a quad plane). It comes from:
```
Collection Info ("Old_Bridge") → Realize Instances → [mesh processing chain]
```
**To swap the mesh:** place the new mesh inside the `Old_Bridge` collection and remove the old one. Hiding the old mesh from viewport/render is NOT enough — Collection Info ignores visibility flags.

### 2. Object Info → `P010_Geo_Ground`
Used for the height-based masking. References the ground plane object to compute relative Z height.
```
Object Info.001 (P010_Geo_Ground) → Location → Vector Math.005
```
**To use in a different scene:** update this reference and adjust Map Range.001's From Min/Max to match the new mesh's height scale.

### 3. Material — `Glass`
Both `Set Material` nodes inside the node group hard-assign the `Glass` material, overriding any source geometry materials. The Glass material reads the Named Attribute to produce the blur shading.

---

## Scene Animation (camera, not geo nodes)

- `P010_Camera`: fully keyframed (251 location keys, rotation, scale) — the fly-through
- `Empty.002`, `Empty.003`: rotation keyframes (camera rig)
- **Scene range:** frames 1–250, 25 FPS

---

## How to Animate the Effect Starting from Zero

The original node group had no exposed inputs — blur was always on. To add a Strength control:

### What to add inside Geo Nodes

1. **Add `Group Input` node**, create a new **Float socket** called `Strength` (default `1.0`, range `0–1`)
2. **Add `Math → Multiply` node** (label: "Strength Scale")
3. **Break link:** `Map Range.001.Result → Vector Math.008.Scale`
4. **New connections:**
   - `Map Range.001.Result → Multiply.Value[0]`
   - `Group Input.Strength → Multiply.Value[1]`
   - `Multiply.Value → Vector Math.008.Scale`

### Python snippet to apply this via MCP

```python
import bpy

ng = bpy.data.node_groups.get("Frozen_MotionBlur")
map_range = ng.nodes.get("Map Range.001")
vec_math_008 = ng.nodes.get("Vector Math.008")

# Add socket
s = ng.interface.new_socket("Strength", in_out='INPUT', socket_type='NodeSocketFloat')
s.default_value = 1.0; s.min_value = 0.0; s.max_value = 1.0

# Add nodes
gi = ng.nodes.new('NodeGroupInput'); gi.location = (700, 260)
mul = ng.nodes.new('ShaderNodeMath'); mul.operation = 'MULTIPLY'
mul.location = (880, 450); mul.label = "Strength Scale"

# Rewire
for lnk in ng.links:
    if lnk.from_node == map_range and lnk.to_node == vec_math_008 and lnk.to_socket.name == 'Scale':
        ng.links.remove(lnk); break

ng.links.new(map_range.outputs['Result'], mul.inputs[0])
ng.links.new(next(o for o in gi.outputs if o.name == 'Strength'), mul.inputs[1])
ng.links.new(mul.outputs['Value'], vec_math_008.inputs['Scale'])
```

### Keyframing

`Strength` appears in the **GeometryNodes modifier panel** on `P010_Geo_Bridge`. Hover → **I** to keyframe. `0` = clean mesh, `1` = full blur.

**Important:** this does NOT affect the Scene Time animation. The oscillation still runs at the same speed and phase — Strength only scales the displacement magnitude.

---

## Key Takeaways

- Effect is 100% procedural — just play the timeline, no keyframes needed on the blur itself
- Two oscillation speeds (÷24 and ÷45) create the layered, non-repeating motion feel
- Z-height mask (Map Range 0.1→0.2) fades the blur near ground level
- Geometry source is a **Collection**, not the modifier's Geometry input
- To control effect intensity: multiply Vector Math's Scale input by an exposed float

---

## Structured Notes

### Core Technique
Procedural frozen motion blur via two Scene Time-driven Mix nodes blending X/Z displacement vectors, masked by Z height, stored as Named Attribute for Glass material consumption.

### Key Steps
1. Get current frame from two Scene Time nodes
2. Divide each by a different value (24 and 45) to get two normalized time values
3. Feed through sub-node-groups (Group.006/007) to get 0–1 oscillating factors
4. Use factors to drive two Mix nodes blending between (10,0,0) and (0,0,10) vectors
5. Compute Z height of each vertex relative to ground reference (Object Info)
6. Map the Z height 0.1→0.2 to 0→1 scale factor (Map Range)
7. Scale the blended displacement vector by the height mask
8. Store result as Named Attribute (×2)
9. Glass material reads the Named Attribute to produce the blur shading

### Blender Nodes / Settings
- `Scene Time` — reads current frame as float
- `Math (DIVIDE)` — normalizes frame number (÷24 and ÷45)
- `Mix` (Vector mode) — blends between two displacement vectors
- `Vector Math (SCALE)` — scales displacement by height mask
- `Map Range` — maps Z height range to 0–1
- `Store Named Attribute` — passes displacement to shader
- `Collection Info` — source of actual 3D geometry
- `Object Info` — ground reference for height masking
- `Set Material` — hard-assigns Glass material
- `Subdivide Mesh` + `Clamp` — adaptive subdivision capped at 11
- `Is Viewport` + `Switch` — viewport/render subdivision toggle

### Difficulty
Advanced

### Blender Version
4.x / 5.x (no version-specific nodes used)

### Tags
#geometry-nodes #motion-blur #procedural #animation #scene-time #glass #displacement #intermediate #advanced #albin-merle
