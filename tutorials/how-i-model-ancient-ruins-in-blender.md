---
title: How I Model Ancient Ruins in Blender
source: YouTube
url: https://www.youtube.com/watch?v=lT1UBQwtZ1g
author: hbitproject
ingested: 2026-08-17
blender_version: "5.2 (visible in viewport title bar in captured frames)"
tags: [geometry-nodes, procedural, displacement, materials, shaders, procedural, compositing, rendering, lighting, hdri, product-viz, advanced, blender-5x]
extraction_status: complete
frames_dir: tutorials/frames/how-i-model-ancient-ruins-in-blender/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How I Model Ancient Ruins in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=lT1UBQwtZ1g)
**Author:** hbitproject
**Duration:** 10m25s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] A few days ago I was scrolling through some images in Pinterest when I came across this picture here.
[0:06] I got completely hooked and I decided on the spot that I wanted to do something like that in Blender.
[0:12] I already attempted similar stuff in the past which gave me good insights on procedural workflows,
[0:17] but it was now time for something a bit more mature and in line with my current skills.
[0:23] A bit of context. The picture is from a quite big oil painting from the Austrian painter Karl Maul,
[0:29] and dates back to 1891 depicting crumbling ruins located at the Schonbrunn Palace in Vienna, Austria.
[0:37] The complex is called Ruin of Cartage and it is actually fake,
[0:41] since it was engineered on purpose in 1778, simply as a garden folly.


### Procedural damage system [0:48]
**Transcript (timestamped):**
[0:49] Now ruins require damage. As a 3D artist there are a few add-ons out there that get the job done pretty decently,
[0:56] but I decided to have my own simple setup which works like this.
[1:00] Take whatever mesh you are targeting, turn it into a volume and then back into a mesh.
[1:05] This will loosen it up a bit. We can displace its vertices along their normals by multiplying the normal themselves
[1:12] by the output coming from a noise texture and feeding the result into the offset socket of a set position node.
[1:20] To control the intensity we can plug a map range node right after the noise texture
[1:25] and to get the final result we can use a mesh boolean node set to intersect
[1:29] and feed it with both the original geometry and the displaced one.
[1:33] And that's it basically. I worked just a bit more on this setup,
[1:37] exposed a few parameters and I turned it into an asset so that I could easily reuse it whenever I needed.
[1:43] Here is the full setup in case you want to copy it.


### Modelling techniques [1:47]
**Transcript (timestamped):**
[1:47] With my damage setup ready I could move on with the actual modeling.
[1:51] I started from the columns, capitals and the technique I used is the following.
[1:56] Of course the damage setup alone cannot do much,
[1:59] so I prepared in advance some variants of the different meshes forming the capital,
[2:04] like the acanthus leaves where I would deliberately cut out some of the extremities.
[2:08] Only then I would apply my procedural damage system.
[2:12] With a few variants ready and placed into a collection,
[2:15] I could use this as an input for the Geonode system used for the capital itself,
[2:20] enabling the pick instance option in the instance on points node
[2:24] and the separate children option in the collection to make the different variants display at the same time.
[2:30] I repeated the same process for all of the different items of the capital,
[2:34] like the leaves and volumes and this was the final result.
[2:37] Similarly I created the pilasters and the shafts.
[2:41] It is worth mentioning that for the damage setup to work properly,
[2:44] each individual element needs to be a separate mesh.
[2:48] If you take the shafts for instance each drum is a separate piece,
[2:51] so it is essential to have everything cleanly lined up in the outliner.
[2:56] With the first few meshes ready I started assembling the scene with the different columns and pilasters,
[3:01] a placeholder for the entablature and the main arch on top.
[3:05] For the corbels I used again pre-prepared variants placed within a collection
[3:10] to be used as an input in a simple Geonode system in a similar way to what was done for the Capitals.
[3:17] At this point I started recreating the entablature but this time separating the different parts of the mesh
[3:23] to make the damage system as already stated more effective.
[3:26] One simple way to apply the same modifiers to multiple meshes at the same time
[3:31] is to select all the target meshes, then the one containing the modifiers we wish to copy
[3:37] and press Ctrl L and select Copy Modifiers.
[3:40] By having each piece being an individual mesh I could still use different parameters setups
[3:46] to control each time the exact amount of damage decide and its specific pattern.
[3:51] I proceeded to add the dentils, deleting and resizing some of them
[3:55] to get a more consistent look with the mood of the scene
[3:58] and I then completed the modeling part of the entablature
[4:01] adding the different pieces for the frizz and the archy-trav.
[4:05] For the arch I started manually deleting pieces of it to achieve the crumble look in the picture
[4:10] making sure to allow for some missing rosettes as well from the overall structure.
[4:16] With the same techniques I completed the scene by adding all the missing elements such as walls, stones,
[4:22] the briefs and making little touches here and there to emphasize the ruinous state of the complex.
[4:28] The last bits were to recreate the composition of rocks emerging from the water
[4:33] serving as the base for the statues.
[4:36] Talking about textures I highly leverage on procedural materials in particular from my own marble pack


### Texturing [4:37]
**Transcript (timestamped):**
[4:43] to get at least a solid foundation.
[4:45] On top of this base I would plug the same combinations of nodes I use almost every time
[4:50] and that can be used really with any material setup.
[4:53] The random output of the object info node overlaid on top of the albedo to add color variation at mesh level
[5:00] the dot product of the normarts coming from the bevel and geometry nodes
[5:05] to expose the contours of the meshes, the ambient occlusion output to multiply it on top
[5:10] again to sell a sense of separation among the different pieces of geometry.
[5:15] In between lots of grunge maps to enhance muddiness and dirtiness in the final look of the material.
[5:22] One nice addition is to be able to setup different materials based on whether a specific portion of a mesh is damaged or not
[5:30] and to do that procedurally.
[5:32] So back in the Geono tree I stored whatever belongs to the original geometry before any deformation
[5:38] with a capture attribute node set to face and placed before the boolean operation.
[5:44] To target the faces created by the boolean which would represent indeed the damaged part of the mesh
[5:49] I took the selection output of the attribute node which will be true for every original face
[5:55] I inverted it with a boolean node set to not and I used this as the selection input of a set material node.
[6:02] For the remaining geometry I inverted again the selection with another boolean node again set to not
[6:08] and I used this along with another set material node.
[6:11] This solution is pretty easy and effective.
[6:13] Now suppose I want to add an additional material this time to a custom selection of faces.
[6:18] I can do that by tapping into edit mode, selecting the faces I desire and in the object data properties tab of the mesh
[6:26] under attributes click the plus icon and add a new attribute set to face and boolean.
[6:32] I would give it a name and with the face or faces still selected under mesh I would select set attribute and tick the newly created one.
[6:40] In the notary I can evoke this with the named attribute node where I would select the attribute just created
[6:46] and use its output in yet another set material node.
[6:50] This comes pretty handy when adding additional details like in this case where I'm using some displacement maps
[6:56] to display ornaments in a way that is coherent with the damaged pattern and that updates dynamically.
[7:02] This is essentially the technique I used for the frizz of the entablator and for some other little details.
[7:08] With models and textures ready I could move on to add the different layers of foliage, grass and trees.


### Foliage [7:10]
**Transcript (timestamped):**
[7:15] To do that I used the Geoscatter addon which is really awesome since it gives a lot of options on how to distribute assets on a surface.
[7:23] Of course the same with a little bit more of a hassle can be done natively with geonodes as well.
[7:29] In this way I populated the scene with some grass and flowers in the foreground,
[7:33] dillipads on the pond's water and grass, bushes and trees for the background.
[7:39] It was now time to think about rendering and compositing.


### Rendering/Compositing [7:40]
**Transcript (timestamped):**
[7:43] I plugged in an HDRI from polyhaven to have a diffuse neutral light in the scene
[7:49] and I then added a sunlight as well with the intent to make the shape of the structure pop out a bit more
[7:55] positioned in such a way to emphasize the different outlines.
[7:59] In the view layer tab I created two different light groups and I assigned the ambient one to the HDRI in the world settings
[8:07] under Light Group and the directional one to the sunlight in its object properties tab under Shading Light Group.
[8:14] This was done to retain the ability in post-processing to play with how both are mixed together in the final image
[8:21] and with the overall tint for each light source.
[8:24] In the render tab under Film I checked the transparent option so that I could add with an alpha over node
[8:31] whatever sky image I wanted just after the rendering.
[8:35] To enhance the sense of separation between the foreground and background
[8:39] I activated the missed pass in the Layer tab and this needs to be done before the rendering.
[8:45] I then activated the missed option in the data properties of the camera under Viewport Display
[8:51] This way by tweaking the start and depth values of the missed pass in the World tab
[8:56] I could control the starting and ending points for the pass to be evaluated.
[9:01] Ultimately I chose the quadratic falloff for a smoother fading effect in space.
[9:06] To composite this in it was enough to mix it on top of the render with the screen blending mode
[9:11] tweaking the factor to change the density of the fog.
[9:14] Something similar can be achieved with a cube and a volume shader
[9:18] For this scene the missed pass was more than enough, especially since it is a lot less burning on the hardware.
[9:25] The final step was to add the denoise node at the end of the chain and that's it.
[9:30] As a final note I do like to save my renders in the OpenEXR format
[9:35] to retain the full range of values per pixel in the final image
[9:39] and to fit this into the Vinci Resolve but this can be done in Blender as well
[9:43] Where in between the needed color space transformation nodes I would apply some farther post processing corrections
[9:50] and at the end of the day this is the final result
[9:55] I hope you found some of the techniques in this video helpful for your own renders
[10:00] Thank you for watching and see you next time



---

## Captured Frames

- [1:05] tutorials/frames/how-i-model-ancient-ruins-in-blender/frame_000.jpg
- [1:29] tutorials/frames/how-i-model-ancient-ruins-in-blender/frame_001.jpg
- [2:15] tutorials/frames/how-i-model-ancient-ruins-in-blender/frame_002.jpg
- [2:51] tutorials/frames/how-i-model-ancient-ruins-in-blender/frame_003.jpg
- [5:00] tutorials/frames/how-i-model-ancient-ruins-in-blender/frame_004.jpg
- [5:44] tutorials/frames/how-i-model-ancient-ruins-in-blender/frame_005.jpg
- [7:23] tutorials/frames/how-i-model-ancient-ruins-in-blender/frame_006.jpg
- [8:45] tutorials/frames/how-i-model-ancient-ruins-in-blender/frame_007.jpg

---

## Structured Notes

### Core Technique
A reusable, asset-ized Geometry Nodes "procedural damage" system (Mesh to Volume → Volume to Mesh to loosen topology, then noise-driven normal displacement combined with the original mesh via a Boolean Intersect) applied piece-by-piece across a full ruined-architecture production pipeline — hand-cut variant meshes, Pick Instance for capital/corbel variation, damage-aware procedural material masking, Geoscatter foliage, and light-group/mist-pass compositing.

### Summary
Inspired by an 1891 oil painting (Karl Maul) of the fake "Ruin of Carthage" garden folly at Schönbrunn Palace, Vienna (built 1778 purely as ornamental ruins). **Damage system:** any target mesh is run through Mesh to Volume then Volume to Mesh to loosen/re-tessellate its topology (visible in frames as a "Mesh Boolean" cluster with Face Group Boundary, Is Edge Boundary, Face Neighbors, Mesh Bevel, Cluster on Connected, Subdivide Mesh, Subdivision Surface operations), then vertices are displaced along their own Normal by a value pulled from a Noise Texture (routed through a Map Range node to control intensity) fed into Set Position's Offset socket; the final broken look comes from a Mesh Boolean node set to **Intersect** between the original mesh and the displaced/loosened version. This whole chain was refined, given exposed parameters (Pattern, Density, Scale, Sharpness, Sharpness Offset, Diffuse, visible in the captured node group), and saved as a reusable Blender **asset** ("HBIT_procedural_damage") for repeated use across the whole scene. **Modeling workflow:** damage alone isn't enough for convincing ruins — each element (e.g. acanthus leaves on a capital) first gets several hand-modeled variant meshes with parts manually cut away at the extremities, THEN the procedural damage system is applied on top of each variant. Variants are grouped into a Collection and fed into a small Geometry Nodes setup using **Instance on Points** with **Pick Instance** enabled and the Collection's **Separate Children** option enabled, so multiple distinct variants display simultaneously across the instanced points (repeated for capitals, corbels, and other repeating elements). A hard technical requirement: for the damage system's Boolean Intersect to read correctly, every individual architectural element must be its OWN separate mesh (e.g. each drum of a column shaft is a distinct mesh object) — this demands disciplined, cleanly-organized Outliner structure. To apply the same modifier stack to many separate meshes at once: select all target meshes, select the "source" mesh with the modifiers last (making it active), then Ctrl+L → Copy Modifiers. Because each piece stays a separate mesh/modifier stack even after copying, damage amount/pattern parameters can still be tuned per-piece. The entablature, dentils (some manually deleted/resized for a mood-consistent irregular look), frieze, and architrave were modeled the same variant+damage way; the main arch's crumbling was achieved by manually deleting geometry chunks (including some missing rosettes) rather than procedurally. **Damage-aware material masking (procedural):** inside the same Geometry Nodes tree, a **Capture Attribute** node (domain: Face) placed BEFORE the Boolean Intersect stores which faces belonged to the original, undamaged geometry. After the boolean, that captured boolean attribute is TRUE on original (undamaged) faces and FALSE on the new faces the boolean operation created (i.e. the damaged/broken surfaces) — inverting it with a Boolean **NOT** node and feeding that into a **Set Material** node's Selection targets the damaged material only to break-surface faces; inverting again (another NOT) targets the remaining (undamaged) faces with a second Set Material node. For an arbitrary custom face selection needing yet another material (e.g. matching displacement-mapped ornament detail to the damage pattern dynamically): enter Edit Mode, hand-select the target faces, in the Mesh Object Data Properties → Attributes panel add a new attribute (domain Face, type Boolean), name it, then with the same faces still selected use Mesh → Set Attribute to write true into the new attribute for that selection — back in the node tree, a **Named Attribute** node reads it back out and feeds a third Set Material node. **Texturing:** procedural marble base materials (the creator's own pack) with a consistent add-on node combo layered on top of nearly every material: the Object Info node's Random output overlaid on Albedo for per-mesh-instance color variation; the Dot Product of Normals from Bevel and Geometry nodes to expose/darken mesh contours/edges; an Ambient Occlusion output multiplied in for separation between adjacent pieces; and layered grunge maps for dirt/muddiness. **Foliage:** the paid Geoscatter add-on distributed grass/flowers (foreground), lily pads (pond surface), and grass/bushes/trees (background) — noted as achievable natively with vanilla Geometry Nodes too, just with more setup effort. **Rendering/Compositing:** a Poly Haven HDRI provides neutral diffuse ambient light, plus a directional Sun light angled to emphasize the structure's silhouette/outlines; two View Layer Light Groups separate "ambient" (assigned to the HDRI via World settings → Light Group) from "directional" (assigned to the sun via its Object Properties → Shading → Light Group) so their relative mix/tint can still be adjusted in post/compositing. Film → Transparent is enabled so a chosen sky image can be composited in later via an Alpha Over node. For foreground/background depth separation, the Mist Pass is enabled in the View Layer tab (must be set before rendering) plus Mist enabled in the camera's Data Properties → Viewport Display, then Start/Depth values in the World tab control where the pass begins/ends, using Quadratic falloff for a smoother fade; in the Compositor, the mist pass is mixed on top with **Screen** blend mode, with the mix Factor controlling fog density — noted as much cheaper on hardware than an equivalent volumetric cube+Volume Shader approach for achieving the same depth-fog look. Finished with a Denoise node at the end of the compositing chain. Final renders are saved as OpenEXR (full per-pixel value range) and finished/graded in DaVinci Resolve, though the same color-space-transform-then-grade workflow could be done inside Blender's own compositor instead.

### Key Steps
1. Build the reusable damage system: target mesh → Mesh to Volume → Volume to Mesh (loosens/re-tessellates topology).
2. Displace: Normal × (Noise Texture output routed through Map Range for intensity control) → Set Position's Offset socket, producing a chaotically-displaced duplicate of the mesh.
3. Combine original and displaced versions with a Mesh Boolean node set to **Intersect** — this is what actually produces the broken/chipped-away look.
4. Expose key parameters (pattern/density/scale/sharpness/etc.) and save the whole node group as a Blender Asset for reuse across every element in the scene.
5. For each architectural element (e.g. acanthus leaf), hand-model several variant meshes first, deliberately cutting away parts at extremities, THEN apply the procedural damage system on top of each variant — damage alone isn't convincing without pre-broken source variation.
6. Group variants into a Collection; build a small Geometry Nodes setup using Instance on Points with Pick Instance enabled and the Collection input's Separate Children option enabled, so different variants appear simultaneously across instanced points (used for capitals, corbels, etc.).
7. Keep every individual architectural piece (each column drum, each capital element) as its own separate mesh object with clean Outliner organization — required for the damage system's Boolean Intersect to work correctly per-piece.
8. To copy a modifier stack to many separate meshes at once: select all target meshes, select the source (modifier-holding) mesh last to make it active, Ctrl+L → Copy Modifiers.
9. For crumbling that doesn't fit the procedural pattern (e.g. the main arch), manually delete geometry chunks by hand, including leaving some ornamental details (rosettes) missing entirely.
10. Set up damage-aware material masking: add a Capture Attribute node (Face domain) before the Boolean Intersect to record which faces are original/undamaged; after the boolean, invert that captured selection with a Boolean NOT node and feed it into a Set Material node's Selection to target only damage-created (broken) faces; invert again for a second Set Material node targeting the remaining undamaged faces.
11. For an arbitrary custom face selection needing its own material: hand-select faces in Edit Mode, add a new Face-domain Boolean attribute via Object Data Properties → Attributes, use Mesh → Set Attribute to write true for the selected faces, then read it back with a Named Attribute node feeding a third Set Material node — useful for coupling extra detail (e.g. displacement-mapped ornament) dynamically to the damage pattern.
12. Layer the standard texture-variation node combo onto materials: Object Info Random output → Albedo color variation; Dot Product of Bevel/Geometry Normals → contour/edge darkening; Ambient Occlusion → multiplied-in separation between pieces; grunge maps for dirt.
13. Scatter foliage (grass, flowers, lily pads, bushes, trees) with the Geoscatter add-on (or an equivalent native Geometry Nodes distribution setup).
14. Light the scene with a Poly Haven HDRI (ambient) + a directional Sun (silhouette emphasis); create two View Layer Light Groups (ambient → HDRI via World settings; directional → Sun via its Shading Light Group) to retain independent post-processing control over each.
15. Enable Film → Transparent for later sky compositing via Alpha Over.
16. Enable the Mist Pass (View Layer tab, before rendering) and Mist in the camera's Viewport Display; tune Start/Depth in the World tab with Quadratic falloff; composite by mixing the mist pass over the render with Screen blend mode, tuning Factor for fog density (cheaper than a volumetric cube+Volume Shader for the same effect).
17. Finish the compositing chain with a Denoise node; export renders as OpenEXR for full dynamic range in downstream grading (DaVinci Resolve in this case, though Blender's own compositor can do the color-space-transform + grading too).

### Nodes / Settings
- Damage system (asset): Mesh to Volume → Volume to Mesh, Set Position (Offset = Normal × Noise Texture routed through Map Range), Mesh Boolean (Intersect) between original and displaced geometry; exposed params: Pattern, Density, Scale, Sharpness, Sharpness Offset, Diffuse
- Instance on Points: Pick Instance enabled, Collection input with Separate Children enabled (multi-variant display)
- Damage-aware masking: Capture Attribute (Face domain, before the boolean) → Boolean NOT (invert selection) → Set Material (×2, for damaged vs. undamaged faces)
- Custom face selection: Object Data Properties → Attributes (new Face/Boolean attribute) + Mesh → Set Attribute (Edit Mode) → Named Attribute node → Set Material
- Material node combo: Object Info (Random → Albedo variation), Dot Product (Bevel Normal, Geometry Normal → contour darkening), Ambient Occlusion (multiply, separation), layered grunge maps
- Foliage: Geoscatter add-on (or native GN distribution)
- Lighting/compositing: Poly Haven HDRI + Sun light, View Layer Light Groups (ambient/directional), Film Transparent + Alpha Over (sky comp), Mist Pass (View Layer + camera Viewport Display, World tab Start/Depth, Quadratic falloff) mixed via Screen blend mode, Denoise node, OpenEXR export

### Difficulty
Advanced (combines custom Geometry Nodes asset authoring, multi-variant instancing, procedural material masking driven by boolean-operation history, and a full lighting/compositing pipeline — a real production breakdown, not a beginner walkthrough)

### Blender Version
5.2, visible in the viewport title bar across the captured frames.

### Tags
geometry-nodes, procedural, displacement, materials, shaders, compositing, rendering, lighting, hdri, product-viz, advanced, blender-5x

---

## Related Tutorials
No directly related tutorials yet in the library for procedural-damage Geometry Nodes systems or damage-aware material masking — flag for cross-linking if another architectural-ruin, weathering, or boolean-driven procedural damage tutorial is ingested later.
