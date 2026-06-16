---
title: Procedural Desert Buildings in Blender | Geo Nodes Blender Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=HMxZTPjFoc0
author: Cinematic Cookie
ingested: 2026-06-16
blender_version: "Not specified (4.x era, modern GN features)"
tags: [geometry-nodes, procedural, modelling, instancing, materials, organic, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/procedural-desert-buildings-in-blender-geo-nodes-blender-tutorial/
frame_count: 4
---

# Procedural Desert Buildings in Blender | Geo Nodes Blender Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=HMxZTPjFoc0)
**Author:** Cinematic Cookie
**Duration:** 21m40s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, so today I'm going to show you how I made these procedural buildings in Blender. I prepared this file here with these assets. These are just basic normal sets with textures and so on. So let's start making our building mesh. I'm going to add a cube that makes something like this extrude. Take this shape here. Yeah, this is going to be our base mesh for our building. Let's open up geometry nodes, new geometry nodes. The first thing we want to do is to create this insetted shape at the top. So first we want to select all of the faces at the top. Let's take the normal, separate the normal by its x, y, c components and let's preview this. Let's take the c value and I'm going to set this to face. I'm also going to turn on the viewer node color opacity and attribute text. Now you can see the c value selects all of the top faces. So we can use a compare node and compare to a value of greater than 0.5. So we'll make sure to select only the top faces. Then we can use the inset node. This inset node is not default in Blender. I created this node and made a tutorial about it. You can also get this inset node for free. The link is in the description. So we can use this as a selection and...

**Frame:** tutorials\frames\procedural-desert-buildings-in-blender-geo-nodes-blender-tutorial\frame_000.jpg


---

## Structured Notes

### Core Technique
**Normal-based face selection + custom Inset node** in Geometry Nodes to procedurally generate desert-style architecture — selecting top/side faces by their Normal Z value, insetting to create recessed window/wall detail, then scattering building instances across a scene.

### Summary
Cinematic Cookie builds procedural desert buildings entirely in Geometry Nodes starting from a hand-modeled cube base. The key insight is using the **Normal Z component + Compare node** to select top faces without manual selection, then feeding that into a free custom **Inset node** to create architectural recesses. The system is extended to scatter multiple building instances procedurally (frame_001) and ends with a complete sandy desert building complex (frame_003) featuring carved windows, wall articulation, and rooftop elements — all driven by a single GN modifier applied to the base mesh.

### Key Steps
1. Prepare a base mesh — author starts with a cube and extrudes/shapes it into a rough building footprint (hand-modeled; keep it simple)
2. Author provides a pre-built asset file (linked in video description) with textures and base meshes to start from
3. Add a **Geometry Nodes** modifier → New → open the GN editor
4. **Select top faces procedurally:**
   - Add a **Normal** node
   - **Separate XYZ** the normal vector → take the **Z** component
   - Set the domain to **Face**
   - Enable **Viewer Node** (color opacity + attribute text) to debug — confirms Z=1.0 on top faces
   - Add a **Compare** node: input = Z value, operation = **Greater Than**, threshold = **0.5** → outputs a boolean selection of only top faces
5. Feed the top-face selection into a custom **Inset** node (not a default Blender node — author created it; download free link in video description). Use the selection to inset only top faces for architectural detail
6. Build wall detail — use similar Normal-based selection for side faces; extrude/offset to create window recesses, ledges, and wall articulation visible in frame_003
7. **Scatter/instance buildings** — the node graph in frame_001 shows a scattering phase where multiple building instances are placed procedurally across a ground plane
8. Apply desert/sandy material — the final result (frame_003) uses warm sandy/beige procedural materials with carved-looking shadow detail across the building faces
9. Add rooftop detail — frame_003 shows smaller structures and decorative elements on the roof, likely instanced procedurally
10. The full GN modifier is applied to the base mesh and drives the entire building form

### Nodes / Settings
| Node / Setting | Purpose |
|---|---|
| Normal | Outputs the per-face normal vector |
| Separate XYZ | Extracts Z component from normal for top-face detection |
| Viewer Node (color opacity + attribute text) | Debug — visualize attribute values on geometry |
| Compare (Greater Than, threshold 0.5) | Converts Z normal to a boolean face selection |
| **Custom Inset node** | Non-default; author-created; free download in description; performs face inset with selection input |
| Instance on Points / Scatter | Procedural building placement (frame_001 node graph) |
| Materials | Sandy/desert procedural material; warm beige tones (frame_003) |

**Note on the Inset node:** The author explicitly states this is not a default Blender node — it's a custom node group they created and made available for free. Without it, you'd use Inset Faces in edit mode or approximate it with Extrude + Scale in GN.

### Difficulty
Intermediate / Advanced — requires understanding of Normal-based attribute selection, domain switching, custom node groups, and procedural scattering in GN. (~22 min tutorial)

### Blender Version
Not specified — uses modern GN features (Viewer Node with color opacity + attribute text, Compare node) consistent with **Blender 4.x** era.

### Tags
`#geometry-nodes` `#procedural` `#modelling` `#instancing` `#materials` `#organic` `#intermediate` `#advanced`

---

## Related Tutorials
- [[all-300-geometry-nodes-in-blender]] — Complete GN node reference; shares `#geometry-nodes #procedural`; useful for looking up any node type used here
- [[blender-geometry-nodes-sci-fi-cube-creation-step-by-step-tut]] — Another procedural box/architecture style GN build; shares `#geometry-nodes #procedural #modelling`
- [[demystifying-geometry-nodes-the-ultimate-guide-to-mastering]] — Covers domains, face vs point data, Compare node concepts; shares `#geometry-nodes #procedural`
- [[procedural-grass-in-blender-geometry-nodes-fast-viewport-se]] — Procedural instancing + scattering pattern; shares `#geometry-nodes #procedural #instancing`
