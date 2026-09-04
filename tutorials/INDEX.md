# Tutorial Library Index

This is the skill's growing knowledge base. Every ingested tutorial is listed here with tags for searchability.

**To add a tutorial:** say "ingest this tutorial: [URL]" and the skill will fetch, structure, and add it here automatically.

**To search:** look for tags matching the technique you need.

---

## How to Read This Index

Each entry format:
```

### 3 Easy Lighting Setups | Blender Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=FYJb10NIMH8
- **Author:** Max Hay
- **Blender Version:** Blender 4.x
- **Tags:** lighting, volume, rendering, cycles, eevee, hdri, materials, shaders
- **Summary:** Three reusable lighting recipes: a dramatic spotlight rig (main spot + dim area fill + Light Falloff/Color Ramp/Map Range rim-highlight trick) in volume scatter fog; a natural outdoor HDRI setup decoupled from a separate emissive sky-image background plane (with an optional lens-flare-on-alpha trick for visible suns); and a dark futuristic/neon setup using reflective surfaces, thick volume scatter, an emissive sign mesh, and a Compositor Glare/Bloom node.
- **File:** tutorials/3-easy-lighting-setups-blender-tutorial.md



### 3D Smoke (Blender Geometry Nodes)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Vqe4jBf3wx4
- **Author:** Seanterelle
- **Blender Version:** Blender 5.0
- **Tags:** geometry-nodes, simulation, smoke-fire, volume, blender-5x, advanced
- **Summary:** Physically-based 3D smoke simulation in Blender 5.0 using Geometry Nodes volume grid nodes. Implements velocity, divergence, pressure, and density fields in a simulation zone with variable solver/smoke resolution for interactive preview vs. final bake quality.
- **File:** tutorials/3d-smoke-blender-geometry-nodes.md



### A FULL Blender Compositor Course!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=_7N7emOvDko
- **Author:** SharpWind
- **Blender Version:** Blender 4.5
- **Tags:** compositing, rendering, materials, shaders, lighting, beginner, intermediate, advanced
- **Summary:** Full Compositor walkthrough: practical FX (Glare/Bloom, Mist-Pass fake fog, color grading, Ellipse Mask grading/vignettes, fake Defocus-based DOF via the Z-Pass, Cycles compositor-side denoising), then Render Layers with manual secondary-bounce visibility, and full Render Pass reconstruction (diffuse/glossy/transmission/volume × direct/indirect/color) with Cryptomatte for post-render per-object recoloring.
- **File:** tutorials/a-full-blender-compositor-course.md



### A New Way To Loop Animations in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9Fvw8HlWHpo
- **Author:** Ducky 3D
- **Blender Version:** Blender 4.x
- **Tags:** geometry-nodes, animation, motion-design, abstract, glass, procedural, intermediate
- **Summary:** Teaches a mathematically precise seamless loop technique using the Mesh Line node: add the Z Offset value to the Start Location keyframe to guarantee a perfect loop regardless of spacing. Builds a stacked glass cube array with spherical gradient scaling and noise displacement.
- **File:** tutorials/a-new-way-to-loop-animations-in-blender.md



### ALL 300+ Geometry Nodes in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Y0zAZnbBcQU
- **Author:** RADIUM
- **Blender Version:** Blender 4.5
- **Tags:** geometry-nodes, procedural, blender-4x, beginner, intermediate, advanced
- **Summary:** One-hour reference video covering all 275+ Geometry Nodes in Blender 4.3 — each node's purpose, socket types, and use cases. Deep dives into Fields vs. single values, field context (domain adaptation), and attributes in the Spreadsheet Editor.
- **File:** tutorials/all-300-geometry-nodes-in-blender.md



### Another Blender String Tutorial....But even Better This Time!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=0lBaaCMpZGs
- **Author:** Ducky 3D
- **Blender Version:** Blender 3.x/4.x
- **Tags:** geometry-nodes, simulation, animation, motion-design, procedural, intermediate
- **Summary:** Uses Simulation Zones to generate an array of Quadratic Bezier curves (strings), then displaces them with per-string randomized W values in a 4D Noise Texture for organic movement. Covers two animation modes: center swell and string reveal.
- **File:** tutorials/another-blender-string-tutorialbut-even-better-this-time.md



### Art Stream #27: Nodes, nodes, nodes! [Blender / Geometry Nodes]
- **Source:** YouTube
- **URL:** https://www.youtube.com/live/7FdfSKOkzXg
- **Author:** Midge "Mantissa" Sinnaeve
- **Blender Version:** Blender 3.x/4.x
- **Tags:** geometry-nodes, particles, volume, procedural, abstract, intermediate, advanced
- **Summary:** Live stream exploring procedural nebula creation using Volume Cube + Distribute Points with iterated Noise Texture offsets through a Repeat Zone for organic space nebula shapes. Also explores converting points to volume and using Blur Attribute for smooth mesh nebulas.
- **File:** tutorials/art-stream-27-nodes-nodes-nodes-blender-geometry-nodes.md



### Blender 5 Beginner Tutorial - Part 2 - Materials and rendering
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RQvTplfsz8k
- **Author:** Rob Tuytel
- **Blender Version:** 5.0
- **Tags:** materials, rendering, cycles, eevee, lighting, hdri, beginner, blender-5x
- **Summary:** Beginner introduction to Blender 5 render engines (Eevee vs Cycles), adding PBR materials with UV maps, and lighting a scene with a Sun Light at intensity 10. Covers Eevee Ray Tracing, Cycles denoising, and material preview modes.
- **File:** tutorials/blender-5-beginner-tutorial-part-2-materials-and-rendering.md



### Blender 5.0 particle attraction and follow surface motion
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QHJXi25OczQ
- **Author:** Zack (3D animation)
- **Blender Version:** 5.0
- **Tags:** geometry-nodes, simulation, particles, animation, procedural, intermediate, blender-5x
- **Summary:** Creates a particle system in Blender 5.0 Geometry Nodes where particles attract to a surface using two vector forces: a normalized attraction vector toward the nearest surface point and a cross-product force for surface-following flow, with added Noise Texture for organic curved paths.
- **File:** tutorials/blender-50-particle-attraction-and-follow-surface-motion.md



### Blender 5.0's NEW Audio Visualisation is INSANE!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=YOx9me2MnGA
- **Author:** MTR Animation
- **Blender Version:** 5.0
- **Tags:** geometry-nodes, simulation, animation, smoke-fire, volume, motion-design, blender-5x, intermediate
- **Summary:** Builds a music-reactive smoke simulation in Blender 5.0 using the Graph Editor's Sound to Samples feature to drive an Empty's Z location from audio, then using the Empty as a force controller for a Geometry Nodes Grid Node volumetric simulation. Covers converting audio graphs to keyframes and scaling amplitude.
- **File:** tutorials/blender-50s-new-audio-visualisation-is-insane.md



### Blender 5.1's NEW Rigging Tool is INSANE!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=NwYZ1QKQhx0
- **Author:** MTR Animation
- **Blender Version:** 5.1
- **Tags:** rigging, geometry-nodes, animation, particles, procedural, blender-5x, intermediate, advanced
- **Summary:** Uses Blender 5.1's new Bone Info Node to bridge Geometry Nodes and armature rigging, replacing bones with procedurally scattered geometry (rocks, spikes, leaves) on a Rigify-rigged golem character. Demonstrates Mesh Lines driven by bone head/tail positions, converted to curves for scattering.
- **File:** tutorials/blender-51s-new-rigging-tool-is-insane.md



### Blender Geometry Nodes – Sci-Fi Cube Creation (Step-by-Step Tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ZmoL0Wa5n0Y
- **Author:** NextFrameSaga
- **Blender Version:** 4.x
- **Tags:** geometry-nodes, procedural, materials, shaders, rendering, cycles, eevee, motion-design, blender-4x, beginner
- **Summary:** Fully procedural sci-fi glowing cube grid in Blender 4.x using Geometry Nodes to distribute and instance cubes with procedural scale variation, combined with emission and metallic materials for a futuristic look. No manual modeling required.
- **File:** tutorials/blender-geometry-nodes-sci-fi-cube-creation-step-by-step-tut.md



### Blender Tutorial: Connect The Dots with Geometry Nodes, The "Plexus" Effect
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=tj6ZZYO5qPY
- **Author:** Entagma
- **Blender Version:** 3.4
- **Tags:** geometry-nodes, procedural, particles, animation, motion-design, abstract, blender-3x, advanced
- **Summary:** Recreates the "Plexus" effect by distributing points inside a Suzanne volume using Distribute Points in Volume, then using a serialized loop approach to test all pairwise point distances and connect only those below a threshold with lines. Demonstrates how to fake nested loops in Geometry Nodes using geometry serialization.
- **File:** tutorials/blender-tutorial-connect-the-dots-with-geometry-nodes-the-pl.md



### Blender Tutorial - Control Physics Sims with Geometry Nodes (Beginner Friendly)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Fec4BhDFBUo
- **Author:** Skramble
- **Blender Version:** 4.5
- **Tags:** geometry-nodes, rigid-body, simulation, animation, procedural, blender-4x, intermediate
- **Summary:** Builds a non-destructive Geometry Nodes system in Blender 4.5 for flexible non-linear playback control of baked rigid body simulations — control start frame, end frame, speed, direction, and spatial proximity triggering without rebaking. Uses Cell Fracture, two identical collections (static/physics), and a Map Range node.
- **File:** tutorials/blender-tutorial-control-physics-sims-with-geometry-nodes-be.md



### Blender Tutorial - Create a Beautiful River Landscape in Blender | Free Addon
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=csvduOcQpIw
- **Author:** Fattu Tutorials
- **Blender Version:** Blender 3.x/4.x
- **Tags:** materials, displacement, rendering, cycles, lighting, hdri, organic, beginner
- **Summary:** Creates a river landscape in Blender using the free Biome Reader add-on for vegetation and environment scattering. Covers terrain shaping, water/river materials, and outdoor lighting with HDRI.
- **File:** tutorials/blender-tutorial-create-a-beautiful-river-landscape-in-blend.md



### Blender Tutorial - Procedural Rope in Geometry Nodes
- **Source:** YouTube
- **URL:** https://www.youtube.com/live/z-fKQtlQPw0
- **Author:** CG Cookie – Learn Blender
- **Blender Version:** 5.0
- **Tags:** geometry-nodes, procedural, organic, animation, blender-5x, intermediate, advanced
- **Summary:** Builds a fully procedural, customizable rope generator in Blender 5.0 Geometry Nodes using a hierarchy of instanced Curve Circles to create interlocking spiral strands along a Bezier curve path, with fine surface hairs. Also covers maze generation and organic leaf scattering.
- **File:** tutorials/blender-tutorial-procedural-rope-in-geometry-nodes.md



### Create Text in Geometry Nodes! (Blender Tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qrYmDg0HpYI
- **Author:** Ryan King Art
- **Blender Version:** Blender 4.x
- **Tags:** geometry-nodes, typography, animation, procedural, particles-reveal, beginner, intermediate
- **Summary:** Creates and animates text entirely in Geometry Nodes using String to Curves, covering font selection, alignment, extrusion, wireframe effects, per-letter random transforms, particle reveal animations, and bubbly animated text with index-based random seeds.
- **File:** tutorials/create-text-in-geometry-nodes-blender-tutorial.md



### Creating an Underground Scene in Blender (Step by Step)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=-QbetK8c1As
- **Author:** Max Hay
- **Blender Version:** Blender 3.x/4.x
- **Tags:** materials, rendering, lighting, compositing, intermediate
- **Summary:** Full scene-building walkthrough for an industrial underground silo environment: modeling custom factory stairs using the Spin tool, Mirror modifier, and bevel; constructing platforms and structural elements; then developing the complete scene with concrete textures and dramatic spotlight lighting.
- **File:** tutorials/creating-an-underground-scene-in-blender-step-by-step.md



### Credit Card Texture and Animation SaaS FinTech [ PART – 1 ]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=DvMyxyMG0Mk
- **Author:** The Visual Vibe
- **Blender Version:** Blender 3.x/4.x
- **Tags:** materials, shaders, animation, product-viz, brand-video, beginner
- **Summary:** Designs a credit card texture in Figma (860Ã—540px with safe areas, typography, chip, Visa logo) then imports it into Blender for a SaaS/FinTech product animation with gradient and metallic material transitions. Covers Figma layout grids, pen tool chip creation, and PNG export for use as Image Texture nodes in Blender.
- **File:** tutorials/credit-card-texture-and-animation-saas-fintech-part-1-blende.md



### Demystifying Geometry Nodes: The Ultimate Guide to Mastering Blender's Procedural Power
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=WbrjlYM0Qno
- **Author:** Deayan Studios
- **Blender Version:** Blender 4.x
- **Tags:** geometry-nodes, procedural, beginner, intermediate
- **Summary:** Comprehensive conceptual guide to Geometry Nodes covering all data types (integer, float, vector, boolean, geometry), socket color-coding, node categories, data flow, Fields vs single values, and field context. Teaches how to use the Spreadsheet Editor to inspect attribute values across geometry domains.
- **File:** tutorials/demystifying-geometry-nodes-the-ultimate-guide-to-mastering.md



### Fundamentals of Lighting in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ENnEYoUpFfU
- **Author:** Blender Guru
- **Blender Version:** Blender 4.x
- **Tags:** lighting, rendering, cycles, eevee, materials, beginner
- **Summary:** Teaches the four lighting fundamentals — Position, Falloff (inverse-square law, used to direct attention), Size (Radius/Area lamp controls shadow softness and detail-vs-form emphasis), and Color (Kelvin temperature for natural light vs. Color for stylized) — on a sci-fi crate. Also covers camera-lock-to-view staging, ground-plane bounce light, an RGB-Curves silhouette-readability trick, and final polish via Spot lamp vignetting and isolated single-light judging.
- **File:** tutorials/fundamentals-of-lighting-in-blender.md



### Geode Nodes (i am so clever) // Blender Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=1hKAkCP-tFQ
- **Author:** CGMatter
- **Blender Version:** Blender 4.5
- **Tags:** geometry-nodes, procedural, displacement, materials, shaders, organic, abstract, blender-4x, advanced
- **Summary:** Procedurally generates an amethyst geode in Blender 4.5 Geometry Nodes: noise-distorted Icosphere exterior, Boolean cut (new Manifold mode), boundary isolation via Geometry Proximity, variable-height crystal extrusion via Noise→Map Range, and instanced spike geometry. Full amethyst and rock material setup.
- **File:** tutorials/geode-nodes-i-am-so-clever-blender-tutorial.md



### Glass Cell Division Effect in Blender 5.0 (tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=XOLuYDLYEgI
- **Author:** Ducky 3D
- **Blender Version:** Blender 5.0
- **Tags:** geometry-nodes, simulation, glass, materials, shaders, animation, motion-design, abstract, blender-5x, intermediate
- **Summary:** Creates a metaball-style cell division animation in Blender 5.0 using the new Points to SDF Grid and Grid to Mesh nodes for efficient organic blob geometry from animated point clouds — far more efficient than the old instances→volume method. Topped with an RGB glass dispersion material in Cycles.
- **File:** tutorials/glass-cell-division-effect-in-blender-50-tutorial.md



### How Apple Makes 3D Wallpapers (Blender Tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=KhBaHDvIamw
- **Author:** Ducky 3D
- **Blender Version:** Blender 4.x
- **Tags:** materials, glass, animation, rendering, cycles, motion-design, abstract, beginner, intermediate
- **Summary:** Recreates the Apple MacBook Air 3D wallpaper using a tall teardrop cylinder (Z:47, X/Y:2) with a circular Array modifier (14 cylinders, Align Rotation Y), a glass transmission material in Cycles, and an emissive highlight plane for the signature glowing band. Covers exact camera positioning for the spiral composition.
- **File:** tutorials/how-apple-makes-3d-wallpapers-blender-tutorial.md



### How I Built This Gate Animation in Blender | Scene Breakdown
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=upUPrc35DYw
- **Author:** Max Hay
- **Blender Version:** Blender 4.x
- **Tags:** animation, motion-design, camera, compositing, rendering, materials, shaders, intermediate
- **Summary:** Breakdown of a sci-fi gate opening animation using simple location keyframes staged with the Graph Editor, Mirror modifier for symmetrical animation, and staggered timing for sequential choreography. Complex visual look is achieved by layering emissive wireframe textures and particles on top of the basic keyframed motion.
- **File:** tutorials/how-i-built-this-gate-animation-in-blender-scene-breakdown.md



### How I Made Realistic Storm Clouds in Blender!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Kep7URnyXgU
- **Author:** c g s l a v
- **Blender Version:** Blender 4.x
- **Tags:** geometry-nodes, volume, rendering, cycles, lighting, hdri, organic, intermediate, advanced
- **Summary:** Creates realistic storm clouds using a multi-pass Geometry Nodes pipeline: mesh→volume→distribute points→set position with Noise Texture→points to volume→mesh→volume. The cycling between representations adds fine organic detail. Also covers god rays using a Volume Scatter cube with an interior Spotlight.
- **File:** tutorials/how-i-made-realistic-storm-clouds-in-blender.md



### How to Make Cyberpunk Scenes in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=SybPYdsd_DI
- **Author:** Max Hay
- **Blender Version:** Blender 4.x
- **Tags:** materials, shaders, lighting, rendering, compositing, procedural, displacement, intermediate
- **Summary:** Intermediate guide to building a cyberpunk alleyway in Blender: wet concrete with noise-driven roughness and normal strength for puddle effects (no roughness map), building modeling from photo reference using Ian Hubert's technique, neon emissive signs, and Volume Scatter atmosphere. Uses Polyhaven add-on for free PBR textures.
- **File:** tutorials/how-to-make-cyberpunk-scenes-in-blender.md



### How To Make This Style in Blender 5.0
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rbPOL9ibooY
- **Author:** Ducky 3D
- **Blender Version:** Blender 5.0
- **Tags:** geometry-nodes, animation, motion-design, materials, shaders, eevee, compositing, abstract, blender-5x, beginner, intermediate
- **Summary:** Creates a stacked-curve motion graphics animation using 120 Curve Circles on a Mesh Line, animated by Wave and Noise Textures through stored Spline Parameter and Random Value attributes. Uses an 8mm ultra-wide camera for the distinctive zoomed-through-ring effect; rendered in Eevee with Emission shaders and compositing glow.
- **File:** tutorials/how-to-make-this-style-in-blender-50.md



### I Recreated movie scene in Blender & Nuke | Complete Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=iW6WF8guDMY
- **Author:** MISSING PIXEL VFX
- **Blender Version:** Blender 5.0
- **Tags:** rendering, compositing, animation, camera, lighting, materials, intermediate, advanced
- **Summary:** Full VFX pipeline recreating a Kong: Skull Island shot using free Sketchfab assets, Mixamo animation retargeting (Kong at 80m scale), a 700m camera distance with telephoto compression, atmospheric volume lighting, and multi-pass Blender rendering composited in Nuke. Covers asset fixing, helicopter blade rig with Empty parent, and Nuke compositing.
- **File:** tutorials/i-recreated-movie-scene-in-blender-nuke-complete-tutorial.md



### I'll teach you Geometry Nodes
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=JU70u6cJZqI
- **Author:** Default Cube
- **Blender Version:** Blender 4.5
- **Tags:** geometry-nodes, procedural, blender-4x, beginner, intermediate
- **Summary:** 5.5-hour comprehensive Geometry Nodes course in Blender 4.5 starting from zero: workspace navigation, Node Editor left-to-right flow, Spreadsheet Editor for live attribute inspection. First project is a 3D Menger Sponge fractal demonstrating the power of procedural iteration and instancing.
- **File:** tutorials/ill-teach-you-geometry-nodes.md



### Introduction to Geometry Nodes - Ø§ØªØ¹Ù„Ù… Ø§Ù‚ÙˆÙŠ Ø§Ø¯Ø§Ø© Ø¹Ù„ÙŠ Ø¨Ù„Ù†Ø¯Ø±
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RU3VO-qb91o
- **Author:** Tabasheer
- **Blender Version:** Not specified
- **Tags:** geometry-nodes, procedural, animation, particles, displacement, materials, beginner, intermediate
- **Summary:** Arabic-language 3.5+ hour beginner course covering Geometry Nodes from scratch: objects, joining, basic shapes, object info, scaling, extruding, insetting, displacement, particles, curves, geometry proximity, drawing curves, and materials. Comprehensive foundation for Arabic-speaking Blender learners.
- **File:** tutorials/introduction-to-geometry-nodes-اتعلم-اقوي-اداة-علي-بلندر.md



### Mastering Blender's Graph Editor
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=MS1z9diLUOI
- **Author:** elijah sheffield
- **Blender Version:** Blender 4.x
- **Tags:** animation, rigging, camera, beginner, intermediate
- **Summary:** Demystifies the Graph Editor for animation: covers F-curves, interpolation modes (Linear vs Bezier), Bezier handle types, Auto Keying, and Animation Modifiers (Cycles, Noise, Envelope). Practical demonstration animates a pan flip with proper anticipation, weight, and easing using only three keyframes refined in the graph.
- **File:** tutorials/mastering-blenders-graph-editor.md



### Math x Blender 5.0 = UNLIMITED POWER!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=EvWAcSA86fw
- **Author:** MTR Animation
- **Blender Version:** Blender 5.0
- **Tags:** geometry-nodes, procedural, abstract, animation, blender-5x, expert, advanced
- **Summary:** Builds an Apollonian Gasket fractal (infinite tangent circles) in Blender 5.0 Geometry Nodes by implementing Descartes' Circle Theorem with Math nodes, Repeat Zones, and For Each Element Zones. Pre-built curvature formula node groups handle the complex mathematics; the result is a fully procedural iterative fractal pattern.
- **File:** tutorials/math-x-blender-50-unlimited-power.md



### Organic Liquid Metal effect in blender 5.0 (tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=2MKKuHcni1U
- **Author:** Ducky 3D
- **Blender Version:** Blender 5.0
- **Tags:** geometry-nodes, simulation, metal, materials, shaders, animation, abstract, organic, blender-5x, intermediate
- **Summary:** Creates an organic liquid metal effect in Blender 5.0 using SDF Grid Boolean (Union) to merge multiple sphere instances into a unified organic mesh with liquid connective tissue. Animated via 4D Noise Texture W value; includes metallic and subsurface fleshy material variants with Smooth Geometry node for artifact removal.
- **File:** tutorials/organic-liquid-metal-effect-in-blender-50-tutorial.md



### Powerful Light Trails in Blender 4.5 (tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=965bgIUHoxA
- **Author:** Ducky 3D
- **Blender Version:** Blender 4.5
- **Tags:** geometry-nodes, simulation, animation, motion-design, materials, shaders, camera, abstract, blender-4x, intermediate
- **Summary:** Topographic map-inspired light trail animation using Simulation Zone to array 77 Quadratic Bezier curves, Noise Texture displacement shaped by RGB Curves for flat ground areas, and a camera-parented gradient transparency that reveals curves as the camera moves. Uses Wave Texture for center focal highlighting and metallic floor material.
- **File:** tutorials/powerful-light-trails-in-blender-45-tutorial.md



### Powerful Logo Particle Flow Effect in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=TTGcr-45jCE
- **Author:** Ducky 3D
- **Blender Version:** Blender 4.x
- **Tags:** geometry-nodes, particles, particles-reveal, animation, logo-animation, typography, materials, shaders, motion-design, intermediate
- **Summary:** Converts text or logos into a dusty particle flow effect using Distribute Points on Faces (density 10,000+, tiny radius) with selective displacement via two Noise Textures and a Mix Vector node — some areas stay readable while others disperse. Particles are colored procedurally with Noise Texture + Color Ramp in an Emission shader.
- **File:** tutorials/powerful-logo-particle-flow-effect-in-blender.md



### Procedural Grass in Blender Geometry Nodes | Fast Viewport Setup & Optimization Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8wFnzrRz0Xg
- **Author:** RTF Dimensions
- **Blender Version:** Blender 4.x
- **Tags:** geometry-nodes, procedural, particles, organic, rendering, beginner, intermediate
- **Summary:** Builds a viewport-optimized procedural grass system using Geometry Nodes with Instance on Points and random rotation/scale variation, then optimizes by culling instances outside camera bounds. Explains how instances reference the original object for memory efficiency and how to link camera visibility properties to the node setup.
- **File:** tutorials/procedural-grass-in-blender-geometry-nodes-fast-viewport-se.md



### Realistic Cloth Physics in Blender – Full Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=KnYGp58REUk
- **Author:** Ahad Animates
- **Blender Version:** Blender 4.x
- **Tags:** cloth, simulation, animation, rendering, beginner, intermediate
- **Summary:** Step-by-step cloth simulation setup in Blender covering Cloth modifier settings (quality, mass, stiffness, damping), collision objects, pin vertex groups, self-collision, baking, and fabric material. Aimed at beginners and intermediate users wanting natural fabric movement in their animations.
- **File:** tutorials/realistic-cloth-physics-in-blender-full-tutorial.md



### Remake this in Blender in 20 mins
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=erICwexR7Iw
- **Author:** Bad Normals
- **Blender Version:** Blender 4.x
- **Tags:** materials, glass, shaders, rendering, cycles, organic, abstract, geometry-nodes, intermediate
- **Summary:** Recreates an AI-generated glass flower in 20 minutes: organic sculpting from a remeshed cylinder base, distance-based center glow emission using Texture Coordinate + Vector Length + Color Ramp in the glass shader, and multi-color luminescence matching the AI reference. Glass at Roughness 0.1 with slight blue tint.
- **File:** tutorials/remake-this-in-blender-in-20-mins.md





### Using Geometry Nodes for VFX in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=PgRax5MeZgY
- **Author:** Jacob Zirkle
- **Blender Version:** Blender 4.5
- **Tags:** geometry-nodes, compositing, rendering, lighting, hdri, camera, blender-4x, intermediate, advanced
- **Summary:** Full VFX pipeline integrating a 3D asset into live-action footage in Blender 4.5 using camera tracking, shadow catcher, ACES color workflow, and HDRI calibrated to footage brightness with a Multiply Mix Color node. Geometry Nodes drives the procedural VFX element; final composite assembled in the Blender compositor.
- **File:** tutorials/using-geometry-nodes-for-vfx-in-blender.md



### You Should Make Glass Animations in Blender 5.1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=vemW4ceygRg
- **Author:** Ducky 3D
- **Blender Version:** Blender 5.1
- **Tags:** glass, animation, materials, shaders, motion-design, abstract, rendering, cycles, blender-5x, intermediate
- **Summary:** Six glass animation design patterns using transparent glass objects as magnifying lenses over animated emissive texture planes — with no scene lights. Covers interlocking sphere arrays, ribbed glass panels, and proper emissive plane distance for optimal refraction spots. Key insight: Wave Texture at scale ~0.7 with animated Distortion looks best.
- **File:** tutorials/you-should-make-glass-animations-in-blender-51.md



### You Should Try this Blender Color Hack
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=U5y1Krd-ykk
- **Author:** Ducky 3D
- **Blender Version:** Blender 4.x/5.x
- **Tags:** materials, shaders, glass, animation, motion-design, procedural, geometry-nodes, eevee, intermediate
- **Summary:** Teaches a color distribution technique where a first Noise Texture drives highlight/dark patterns and a second Noise Texture provides color — connected via Mix Color with the first texture as Factor, so color distributes naturally within the pattern's highlights rather than being limited to center-to-edge gradients. Demonstrated with glass brick wall geometry nodes setup.
- **File:** tutorials/you-should-try-this-blender-color-hack.md



### The Key to Realism in Blender (or 3D)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=0OVEJVbklV0?si=9fHvKcSM0pjBBy2G
- **Author:** Kaizen
- **Blender Version:** Blender 3.x/4.x
- **Tags:** realism, photorealism, 3dscanning, lighting, camera, workflow, beginner
- **Summary:** Introduces the "Triforce of 3D Realism" — Subject, Lighting, Camera — as the three pillars that together produce convincing photorealism. Covers using KIRI Engine for free mobile 3D scanning to generate realistic subjects without years of modeling skill, optimal scanning conditions (overcast outdoor vs. controlled indoor lighting), and how all three forces compound.
- **File:** tutorials/the-key-to-realism-in-blender-or-3d.md



### Tutorial: How to make a volumetric projector in Blender 4.5
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=F8pqNeVam54
- **Author:** Polyfjord
- **Blender Version:** Blender 4.5
- **Tags:** lighting, volume, animation, rendering, cycles, intermediate, god-rays, projector, video-texture
- **Summary:** Creates a volumetric projector effect by setting the World Shader to Volume Scatter (density ~0.1) as scene fog, then assigning a video image texture to a Spotlight via Use Nodes + Node Wrangler (Ctrl+T). Animated video travels through the fog as god rays. Key trick: set image color space to AGX Base sRGB for correct vibrant color.
- **File:** tutorials/tutorial-how-to-make-a-volumetric-projector-in-blender-45.md






### Photorealistic Renders In Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=J_mweAPcO4M?si=_bc3120mdobqksIE
- **Author:** Extra 3d
- **Blender Version:** Blender 4.x
- **Tags:** realism, photorealism, materials, textures, lighting, workflow, intermediate, 3dscanning, imperfections
- **Summary:** Comprehensive photorealism pipeline: reference gathering in PureRef → camera focal length/height decision early → high-res stacked textures with imperfections (Polyhaven, Ambient CG, Megascans) → photoscanned or AI-generated assets (Tripo3D: 1-4 photo input → 4K PBR output) → bevel all edges → scale verification with Rigify rig.
- **File:** tutorials/photorealistic-renders-in-blender.md



### Frozen Motion Blur Bridge — Geo Nodes Breakdown (Albin Merle)
- **Source:** Direct file analysis
- **URL:** https://www.youtube.com/watch?v=675BOBWbTt4
- **Author:** Albin Merle
- **Blender Version:** 4.x / 5.x
- **Tags:** geometry-nodes, motion-blur, procedural, animation, scene-time, glass, displacement, intermediate, advanced, albin-merle
- **Summary:** Full breakdown of the `Frozen_MotionBlur` node group from file `061_AM_Frozen_motion_Blur_Bridge`. Two Scene Time nodes oscillate X/Z displacement vectors at different speeds (÷24 and ÷45), masked by Z height via Map Range. Geometry source is a Collection (not the modifier input). Includes Python snippet to add a Strength input for animating the effect on/off.
- **File:** tutorials/frozen-motion-blur-bridge-geo-nodes-breakdown.md




### Photorealistic Eevee Renders In Blender 5.1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=AoGPxjgqVYE&t=76s
- **Author:** Extra 3d
- **Blender Version:** Blender 5.1
- **Tags:** eevee, rendering, photorealism, ray-tracing, lighting, light-probes, materials, glass, hdri, vulkan, blender-5x, beginner, intermediate
- **Summary:** Full workflow for photorealistic Eevee renders in Blender 5.1: switch backend to Vulkan, enable ray tracing, then combine irradiance volume + reflection cubemap light probes (baked) to fix Eevee's screen-space limitations. Covers 5 chapters: theory, basic scene, light probes, glass/translucent materials, and relighting complete scenes.
- **File:** tutorials/photorealistic-eevee-renders-in-blender-51.md



### Realistic Product Lighting In Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=WreZ_VKDn4M
- **Author:** Extra 3d
- **Blender Version:** Blender 4.x
- **Tags:** lighting, product-viz, materials, rendering, glass, brand-video, beginner, intermediate
- **Summary:** Three-point product lighting system covering non-glossy products (Area Lights with Image Texture nodes to fix reflections) and glass products (Emission planes with Gradient Texture + Color Ramp for smooth falloff). Includes the 3D Cursor pivot trick for rotating lights around a product, hiding emission planes from camera via Visibility settings, and using Light Linking to prevent lights from contaminating ground reflections.
- **File:** tutorials/realistic-product-lighting-in-blender.md


### Replacing Adobe After Effects with Blender (tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ZK92Uuhiesg
- **Author:** Ducky 3D
- **Blender Version:** Blender 4.x/5.0
- **Tags:** materials, shaders, animation, motion-design, abstract, procedural, beginner, intermediate
- **Summary:** Creates a looping animated texture on a flat canvas plane using Shader Editor nodes: Voronoi Texture twisted into circular patterns by a Wave Texture (Rings), plus three stacked radial masks (outer edge, inner core, lighting variation). All motion driven by keyframed node values — no geometry animation. Part of Ducky 3D's "Blender as After Effects" series.
- **File:** tutorials/replacing-adobe-after-effects-with-blender-tutorial.md


### A Powerful Lighting Node in Blender 5.0
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=BoCCxy9ec0g
- **Author:** Ducky 3D
- **Blender Version:** Blender 5.0
- **Tags:** materials, shaders, compositing, motion-design, animation, procedural, lighting, intermediate
- **Summary:** The key lesson: a Sun Beams Glare node alone looks weak — stack it on top of two Bloom Glare nodes (one tight/strong, one large/atmospheric) to give the brightness visual context. Demonstrated on a procedural animated dot-grid (Voronoi/Noise-masked Emission shader) with a seamless loop via mirrored keyframes on a 4D Noise Texture's W value, parallax via a duplicated/instanced grid layer, and Blender 5.0's Sensor Noise compositor node for grain.
- **File:** tutorials/a-powerful-lighting-node-in-blender-50.md


### Real time Caustics In Blender 5.1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=wOyk5V7PyfA
- **Author:** Extra 3d
- **Blender Version:** Blender 5.1
- **Tags:** shaders, caustics, glass, cycles, voronoi, transparent-shader, light-path, procedural, extra-3d, intermediate
- **Summary:** Fake real-time caustics via shadow manipulation — Cycles only. Mix Shader + Transparent Shader + Light Path (Is Shadow Ray) makes the shadow controllable. Voronoi 4D Smooth F1 (two with different smoothness subtracted via Difference node) creates caustic pattern fed into shadow. Water variant animates via W value. Final complex variant adds Gradient + Noise distortion + Color Ramp fringes.
- **File:** tutorials/real-time-caustics-in-blender-51.md


### Remove Noise from Volumetrics in Blender 5.0+
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=wWv0E94XE4M
- **Author:** Extra 3d
- **Blender Version:** Blender 5.0
- **Tags:** volumetrics, noise, rendering, cycles, bug-fix, ray-marching, extra-3d, beginner
- **Summary:** Blender 5.0 volumetrics noise fix — new default rendering algorithm causes noise that increasing samples cannot fix. Fix: Render Properties → Volume → enable Legacy Ray Marching. The legacy method is faster AND noise-free for typical fog/smoke use cases.
- **File:** tutorials/remove-noise-from-volumetrics-in-blender-50.md


### My Circle Problem in Blender (tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=89ZPdMI_nE8
- **Author:** Ducky 3D
- **Blender Version:** Blender 4.x
- **Tags:** wave-texture, curves, seam-fix, animation, motion-graphics, procedural, shader-animation, ducky-3d, intermediate
- **Summary:** Fixing wave texture seam on closed curves — standard Texture Coordinate (Generated/Object) creates a visible break at the seam on looping curves. Fix: UV unwrap the curve as a strip (convert to mesh) or use Geometry Nodes Spline Parameter Factor (0→1 seamless around loop). Animating Phase drives smooth flow. Enables clean looping wave animations on circle/ring shapes.
- **File:** tutorials/my-circle-problem-in-blender-tutorial.md


### How To Render Faster In Blender Cycles
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=gmGMsKJ6xd8
- **Author:** Extra 3d
- **Blender Version:** 4.x
- **Tags:** rendering, cycles, compositing, camera, intermediate
- **Summary:** Three-chapter Cycles optimization guide: GPU selection (OptiX/HIP/Metal/oneAPI + Vulkan backend), adaptive noise-threshold sampling, memory reduction (disable off-camera collections, mute unused textures, Alt+D instancing, Purge Unused Data), and render stitching in the VSE for still-camera animations — claimed up to 4000% speedup without hardware upgrades.
- **File:** tutorials/how-to-render-faster-in-blender-cycles.md


### My New Favorite Lighting Trick in Blender!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=1-Cj4mtdCMc
- **Author:** Curtis Holt
- **Blender Version:** Blender 4.x
- **Tags:** lighting, animation, materials, shaders, cycles, abstract, laser, vfx, intermediate, curtis-holt
- **Summary:** Curtis Holt (Project Fold) demonstrates a physical laser-style lighting method that avoids area lights or shader raycasting.
- **File:** tutorials/my-new-favorite-lighting-trick-in-blender.md


### Blender NEW Cloth Simulator changes EVERYTHING!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ih100VB7BUI
- **Author:** SouthernShotty
- **Blender Version:** Blender 5.2 (experimental)
- **Tags:** cloth, simulation, geometry-nodes, animation, organic, blender-5x, intermediate, advanced
- **Summary:** Full breakdown of Blender 5.2's Cloth Dynamics Experimental GN node — covers all parameters (Pin Group, Stretchiness, Bendiness, Sub Steps, Tearing, Geometry Collider, Custom Force, Bake node) then builds a "peeling skin" effect where an offset outer shell tears away from a skull mesh. The GN modifier is portable to any object. Requires Blender 5.2 experimental build.
- **File:** tutorials/blender-new-cloth-simulator-changes-everything.md



### THIN WALL, the incredible new Principled BSDF feature in Blender 5.2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=eQLCfPwEcrI
- **Author:** Christopher 3D
- **Blender Version:** Blender 5.2
- **Tags:** materials, shaders, rendering, cycles, eevee, organic, blender-5x, beginner
- **Summary:** The new Thin Wall checkbox in Blender 5.2's Principled BSDF simulates correct light transport through zero-thickness geometry (leaves, curtains, lampshades, glass panes, soap bubbles) without needing a Solidify modifier. Two sub-parameters — Weight (0.5 typical) and Anisotropy (−0.25 for fabric, 0.0 for foliage) — fine-tune the effect. Part of the OpenPBR specification integration.
- **File:** tutorials/thin-wall-the-incredible-new-principled-bsdf-feature-in-blender-52.md


### Procedural Desert Buildings in Blender | Geo Nodes Blender Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=HMxZTPjFoc0
- **Author:** Cinematic Cookie
- **Blender Version:** Blender 4.x
- **Tags:** geometry-nodes, procedural, modelling, instancing, materials, organic, intermediate, advanced
- **Summary:** Builds procedural desert/Middle-Eastern-style buildings in GN using Normal Z component + Compare node for automatic top-face selection, fed into a free custom Inset node for architectural recessing. Covers procedural scattering of multiple building instances and ends with a complete sandy building complex with carved windows and rooftop detail.
- **File:** tutorials/procedural-desert-buildings-in-blender-geo-nodes-blender-tutorial.md


### NeXus for Blender Official Training - Follow Curve
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=na6NGPw4XWM
- **Author:** INSYDIUM LTD
- **Blender Version:** Blender 4.x
- **Tags:** particles, simulation, fluid, meshing, motion-blur, addon, intermediate
- **Summary:** Using the NeXus particle plugin (Insydium) to emit a liquid particle stream from a sphere emitter, make it follow a scene curve's path, mesh the stream into a continuous surface, and apply render-time motion blur for a dynamic fluid-trail effect.
- **File:** tutorials/nexus-for-blender-official-training---follow-curve.md


### Curves Just Got Easier in Blender 5.0
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=NzZTrDln6Ko
- **Author:** Ducky 3D
- **Blender Version:** Blender 5.0
- **Tags:** geometry-nodes, materials, shaders, motion-design, animation, procedural, abstract, intermediate
- **Summary:** Uses the UV Map attribute auto-generated by Curve to Tube (with a flat Path as Custom Profile for ribbon geometry) to map a Wave Texture per-strand across an evenly-spaced curve array (constant ring spacing via Radius = iteration × constant inside a Repeat Zone). A per-spline Random attribute desyncs each strand's wave phase and drives per-strand coloring, finished with Sensor Noise + Bloom compositing for an After-Effects-style animated background.
- **File:** tutorials/curves-just-got-easier-in-blender-50.md


### Blender's NEW Transparency Material is CRAZY!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=U2I8YDrO5Jc
- **Author:** SouthernShotty
- **Blender Version:** Blender 5.2
- **Tags:** materials, shaders, rendering, lighting, glass, organic, intermediate, blender-5x
- **Summary:** Blender 5.2's Thin Wall option on the Principled BSDF correctly renders one-sided transmissive/subsurface surfaces without a Solidify modifier — demonstrated on bubble/thin-film glass, faster and more natural foliage backlighting, fixing the classic dark-glass light-loss bug, and a frosted-glass creative effect.
- **File:** tutorials/blenders-new-transparency-material-is-crazy.md


### How to Create Abstract Crystal Renders in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RKz3DdbybVk
- **Author:** Extra 3d
- **Blender Version:** Blender 3.x/4.x
- **Tags:** geometry-nodes, materials, shaders, procedural, glass, lighting, volume, compositing, abstract, intermediate
- **Summary:** Scatters a free crystal GLB model across a UV sphere using Geometry Nodes (Distribute Points on Faces → Instance on Points → Join Geometry), then builds a transmissive purple crystal shader and a bump/displacement rock material. Finished with high-focal-length DoF camera, point lights, cube volumetrics, and Cinematic Compositor+ grading.
- **File:** tutorials/how-to-create-abstract-crystal-renders-in-blender.md


### Add VFX into Cinematic RAW+LOG Footage (the right way) | ACES Part 1 (full re-extraction)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=aJF2sAjRsy0
- **Author:** InLightVFX
- **Blender Version:** Any (theory only)
- **Tags:** compositing, rendering, intermediate
- **Summary:** Color theory primer (not hands-on Blender): color gamut via the CIE diagram (ACES2065-1's gamut covers the full visible spectrum), gamma/transfer functions (linear vs. non-linear luminance math, why human vision is non-linear), and display-referred vs. scene-referred camera storage (RAW/Log) — explains why RAW/Log footage looks flat and how ACES's linear working space lets VFX artists ignore source footage gamma. Note: a near-duplicate entry for this video exists at the 80-char-truncated slug `tutorials/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-par.md` — left as-is per the known slugify duplicate-entry issue, not merged.
- **File:** tutorials/add-vfx-into-cinematic-rawlog-footage-the-right-way-aces-part-1.md


### Add VFX to Cinematic RAW and LOG Footage (the right way) | ACES Part 2 (full re-extraction)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=LssHxDCM7H4
- **Author:** InLightVFX
- **Blender Version:** Any (with ACES config installed)
- **Tags:** compositing, rendering, lighting, hdri, intermediate, advanced
- **Summary:** Full hands-on ACES pipeline: DaVinci Resolve (Color Workspace ACES CC, IDT per clip, ODT sRGB for preview, disable ODT before EXR/RGB-Half export) → Blender (Display Device ACES, View Transform sRGB, render in ACES CG, per-image IDT via node Color Space, Shadow Catcher + split Main-Objects/Shadows render layers) → Compositor (Alpha Over chain, EEVEE 1-sample render-trigger workaround) → re-import final EXR to Resolve (IDT: ACES CG) for color grading and final ODT-based delivery export. EXR throughout preserves full dynamic range (demonstrated recovering blown highlights via the Gain slider). Note: a near-duplicate entry for this video exists at `tutorials/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces.md` — left as-is per the known slugify duplicate-entry issue, not merged.
- **File:** tutorials/add-vfx-to-cinematic-raw-and-log-footage-the-right-way-aces-part-2.md


### Blender Tutorial - Eternals Gold Wireframe Animation (full re-extraction)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=WmldjCv9P84
- **Author:** Blender Made Easy
- **Blender Version:** Blender 4.x
- **Tags:** materials, shaders, animation, motion-design, logo-animation, procedural, metal, intermediate
- **Summary:** Curve-based "build-on" logo animation (Bevel Depth + Start/End mapping in Spline mode) with a Taper-curve thickness falloff and a Fresnel-masked, driver-animated Noise Texture for a traveling molten-gold emission edge. Note: a near-duplicate legacy-format entry for this same video exists at `tutorials/blender-tutorial-eternals-gold-wireframe-animation.md` (single-dash slug, captions-based, missing the taper/material/render sections covered here) — left as-is per the known slugify duplicate-entry issue, not merged.
- **File:** tutorials/blender-tutorial---eternals-gold-wireframe-animation.md


### Fractals in Blender - Geometry Nodes Extrude Node (full re-extraction)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=bHWvVtuLJkM
- **Author:** CrossMind Studio
- **Blender Version:** Blender 3.1
- **Tags:** geometry-nodes, procedural, materials, shaders, glass, abstract, beginner, intermediate
- **Summary:** Chains 4-5 duplicated copies of a grouped [Extrude Mesh (Offset ~0.01) + Scale Elements (Top selection)] node pair — all sharing the same group data, so editing one updates all — to build a self-similar fractal pattern on a cube. An optional extra layer uses Face Area + Compare (>0.4) so only larger faces get additional recursive detail, for organic size variation. Rendered in Cycles with Glass BSDF + colored point lights inside hollow cubes. Note: a near-duplicate entry for this video exists at the single-dash slug `tutorials/fractals-in-blender-geometry-nodes-extrude-node.md` — left as-is per the known slugify duplicate-entry issue, not merged.
- **File:** tutorials/fractals-in-blender---geometry-nodes-extrude-node.md


### How to create a Cinematic Landscape inside Blender | Full tutorial with Project file
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QJhiYYf6qJI
- **Author:** vfx world
- **Blender Version:** Blender 3.x/4.x
- **Tags:** landscape, terrain, foliage, camera-animation, cycles, hdri, biome-reader, blenderkit, sketchfab, intermediate
- **Summary:** Full cinematic landscape pipeline — A.N.T. Landscape (Lake 1 preset, scaled 50x), weight-painted foliage zones, Biome Reader grass+background trees, Blenderkit ground material (displacement+bump), animated procedural water, Follow Path + Track To camera constraints on Bezier curve, Easy HDRI with two mixed HDRIs for cloudy sky. Intermediate multi-add-on workflow; transcript is Hinglish.
- **File:** tutorials/how-to-create-a-cinematic-landscape-inside-blender-full-tutorial-with-project-fi.md


### Sci-Fi Grid Pattern Animation Loop - Blender Motion Graphics Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=IzSRBH8CDTo
- **Author:** Ryan King Art
- **Blender Version:** Blender 5.x
- **Tags:** motion-graphics, eevee, geometry-nodes, looping, honeycomb, displacement, compositing, beginner
- **Summary:** Seamless looping sci-fi glowing dot grid — Extra Mesh Honeycomb (50x50, Edge Width 1 to triangle) + Instance on Elements (Realize Instances) placing Icospheres. Two-noise 4D crossfade loop: noise1 W 40-80, noise2 W 0-40, Mix factor 0-1 over 251 frames with linear F-curves. Glare Bloom compositor; Displacement node makes glowing dots physically pop out. EEVEE, Filmic Very High Contrast.
- **File:** tutorials/sci-fi-grid-pattern-animation-loop---blender-motion-graphics-tutorial.md


### Superhero Landing Tutorial 02 | Ground Destruction VFX in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=4ULxB4PzbAc
- **Author:** Graphical Ninja
- **Blender Version:** Blender 3.x/4.x
- **Tags:** vfx, rigid-body, particles, fluid-sim, destruction, compositing, nuke, intermediate
- **Summary:** Ground destruction VFX pipeline (Part 2 of superhero landing series) — Cell Fracture (OwnVerts, recursive 2) + Rigid Body sim with Force Field (10,000 strength, 2 frames, falloff 1) + speed ramp to 0.25x. Rock particles (2,000 per chunk, Brownian 0.1, inherited velocity, Bridge rock collection) baked and copied to all chunks. Mantaflow smoke domain (128-256 res, timescale 0.25) from chunk surfaces. Voronoid displacement + SubSurf on chunks. Nuke comp with Holdout pass + Disjoint Over + Chemix grain mask.
- **File:** tutorials/superhero-landing-tutorial-02-ground-destruction-vfx-in-blender.md
- **Related:** How I made this bridge destruction scene in blender (`how-i-made-this-bridge-destruction-scene-in-blender.md`) — shares vfx, rigid-body, particles, destruction; custom Simulation-Nodes-driven fracture/emission tooling vs. this tutorial's Cell Fracture + Mantaflow approach to the same problems.


### The COMPLETE BLENDER 3D Animation COURSE (5+ HOURS) #blender #b3d #animation
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=IgpUXXg2Vbs
- **Author:** JB 3D Studio
- **Blender Version:** Blender 4.4
- **Tags:** animation, rigging, beginner, modeling, rendering, 12-principles, robot, course
- **Summary:** 5-hour beginner animation course by JB 3D Studio covering the full pipeline: Blender interface, 12 principles of animation, basketball bounce, robot character modeling, armature rigging, IK constraints, NLA editor, Cycles rendering. 11+ modules, soup-to-nuts production walkthrough.
- **File:** tutorials/the-complete-blender-3d-animation-course-5-hours-blender-b3d-animation.md


### Track Objects Using Align Rotation To Vector In Geometry Nodes – Blender Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ZBZ26xQ9Pnk
- **Author:** Photini By Design
- **Blender Version:** Blender 4.x
- **Tags:** geometry-nodes, tracking, align-rotation, instances, procedural, animation, intermediate
- **Summary:** Reusable GeoNodes tracking modifier — Align Rotation to Vector node with direction vector (target Location minus point Position via Vector Math Subtract) drives Rotate Instances. Scale-by-distance: Vector Math Distance + Multiply Add + Combine XYZ into Scale. Exposed Group Inputs for Track Target, Scale Target, min/max scale per modifier. F-Curve Noise on master empty for automated random movement. Works on any mesh surface.
- **File:** tutorials/track-objects-using-align-rotation-to-vector-in-geometry-nodes-blender-tutorial.md


### Your Guide to Mechanical Rigging in Blender (Robot Arm Tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=SCz1tmOVmFw
- **Author:** DemNikoArt
- **Blender Version:** Blender 4.x
- **Tags:** rigging, ik, mechanical, armature, constraints, robot, intermediate
- **Summary:** Mechanical robot arm IK rigging — single-bone chain with Shift+I IK constraint, per-bone axis locks (only Y rotates), stiffness bias. Pistons via Damp Track constraint to empties parented to geometry. Clamp range via Transformation constraint (Location range to Rotation range, local space). Bone Widget add-on for custom gizmo shapes; Parent to Nearest Bone add-on for geometry assignment.
- **File:** tutorials/your-guide-to-mechanical-rigging-in-blender-robot-arm-tutorial.md


### ZoZos Contact Solver - The ultimate Blender cloth simulator
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=D0k6evTvJDg
- **Author:** CGMatter
- **Blender Version:** Blender 5.0+
- **Tags:** cloth, simulation, physics, add-on, third-party, contact-solver, self-intersection, pinning, vertex-groups, toml, pc2-cache, intermediate
- **Summary:** Setup guide for ZoZo's PPF Contact Solver (free open-source third-party engine) integrated into Blender — eliminates cloth self-intersection. Covers installation, Windows Native connection, Dynamic Groups (Shell/Solid/Rod/Static), vertex group pinning animated in Edit Mode, material TOML presets (denim/cotton/silk/rubber), invisible wall colliders, and multi-layer cloth stacking. Output bakes to per-frame shape keys.
- **File:** tutorials/zozos-contact-solver---the-ultimate-blender-cloth-simulator.md


### The FUTURE of Blender Cloth Simulation (with Tearing!)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=6hn12BWufTs
- **Author:** CGDive (Blender Rigging Tuts)
- **Blender Version:** Blender 5.2 (experimental)
- **Tags:** cloth, simulation, geometry-nodes, physics, tearing, blender-5x, experimental, pinning, wind-force, stability, beginner, intermediate
- **Summary:** First-look at Blender 5.2 Alpha's experimental Cloth Dynamics GN node. Full setup: Collection → Geometry Collider → Combine Bundle → Effectors chain for collisions; vertex group pinning via Pin Group Input node; Simulation Force node for wind; dynamic tearing via Tearing toggle + Threshold (no pre-cutting). "Deforming Setting" option fixes the old system's collapse with animated collision objects. Covers Bendiness, Stretchiness, Damping, Collision Radius, Sub Steps, Constraint Steps.
- **File:** tutorials/the-future-of-blender-cloth-simulation-with-tearing.md


### INFINITE WOOD! Don't Fear the Shader: EP01
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=gpC7s-tGpc4
- **Author:** Clipping Issues
- **Blender Version:** not stated (Shader Editor node groups, Blender 4.x/5.x compatible)
- **Tags:** materials, shaders, procedural-texture, wood, node-groups, map-range, vector-math, mixed-node, bump, hsv, beginner
- **Summary:** 10m27s procedural wood-shader build by Clipping Issues (Episode 1 of a "Don't Fear the Shader" series). Sets up an HDRI in viewport shading first so material judgments aren't made against Blender's default gray void...
- **File:** tutorials/infinite-wood-dont-fear-the-shader-ep01.md


### Como hacer Agua Realista en Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fB_F8x_59LA
- **Author:** MinerDesign
- **Blender Version:** not stated (Adaptive Subdivision + 4D Noise Texture, Blender 3.x/4.x/5.x compatible)
- **Tags:** materials, shaders, water, ocean, procedural-texture, displacement, noise-texture, driver, adaptive-subdivision, hdri, eevee, spanish, beginner
- **Summary:** 8m32s Spanish-language ("Como hacer Agua Realista en Blender") tutorial by MinerDesign, a follow-up to viewer requests after an animation he posted. Base setup: new file, add a Plane, apply a Subdivision Surface modifier set to **Adaptive** with subdivision type **Simple** (not Catmull-Clark, to avoid corner/edge deformation), switch to Render view...
- **File:** tutorials/como-hacer-agua-realista-en-blender.md


### Blender 5.2: Printing Muscles
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ByWrhGggWm8
- **Author:** Cartesian Caramel
- **Blender Version:** Blender 5.2
- **Tags:** geometry-nodes, procedural, simulation, uv-mapping, materials, shaders, cycles, eevee, advanced, intermediate, blender-5x, attributes, organic, sci-fi, anatomy, livestream
- **Summary:** Unedited ~2hr livestream (no chapter markers) building a procedural "3D printer" Geometry Nodes rig: a spline traces across a mesh's per-UV-island map and progressively deforms/reveals the surface along it, faking a live tissue-printing/growth process, applied to hand tendons/muscles over a skeleton reference. Covers the tracer/deform/muscle-fiber node-group architecture, an ad-hoc auto-square-UV trick (shortest-edge-path gradients, no add-on), a progress auto-stop via Attribute Statistic, a minimum-stretch UV-unwrap trick for circular fiber UVs, and a genuinely useful Cycles-only gotcha: naming a Store Named Attribute output `UV` silently collides with Blender's reserved active-UV-map attribute and gets ignored in Cycles (EEVEE unaffected).
- **File:** tutorials/blender-52-printing-muscles.md



### Easy Geometry Nodes - Low-poly Rocks Blender 5.1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=n1_NMIV7A5U
- **Author:** ALL THE WORKS
- **Blender Version:** Blender 5.1
- **Tags:** geometry-nodes, procedural, instancing, organic, curves, beginner, intermediate, blender-5x
- **Summary:** Scatters a Collection of hand-modeled low-poly rock variants across a mesh or curve using Distribute Points on Faces (Poisson Disk) + Instance on Points (Pick Instance), with Align Rotation to Vector for surface-normal alignment, layered Random Value nodes for scale/rotation variety, and an optional Normal/Compare face-selection mask. Covers merging overlapping instances via Realize Instances + Remesh + Decimate, and a curve-based scattering variant.
- **File:** tutorials/easy-geometry-nodes---low-poly-rocks-blender-51.md


### How to fix SHADING ERRORS in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=EdEIUkWzYY0
- **Author:** Josh - Blender Bros
- **Blender Version:** Blender 5.1
- **Tags:** shading, normals, weighted-normal, boolean, bevel, topology, hard-surface, intermediate, advanced, blender-5x
- **Summary:** Diagnostic (not build) tutorial covering three distinct causes of hard-surface shading distortion after Booleans/Bevels: inherited Sharp edge-marks on bevel holding edges (fix: clear the mark, avoid it pre-bevel, or Hard Ops Recalculate), non-90° holding-edge angles on flat surfaces (fix: Weighted Normal modifier), and bent n-gon polygons from Booleans on curved surfaces (Weighted Normal does NOT fix this — needs clean quad topology or added geometry density instead).
- **File:** tutorials/how-to-fix-shading-errors-in-blender.md


### I Tested 5 Different Ways to Simulate Water
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QF-gxJLVNOw
- **Author:** Nils Gallist
- **Blender Version:** Not specified (Mantaflow works on any recent Blender 3.x/4.x/5.x)
- **Tags:** simulation, fluid, particles, review, workflow, intermediate, advanced
- **Summary:** Comparative benchmark (not a build tutorial) of five water-simulation tools on an identical splash scene: Blender-internal Mantaflow (free but slow, 19-115GB caches, crash-prone), Flip Fluids add-on (best realism/detail, CPU-bound), NeXus Particles (fast/GPU but no whitewater and broken caching), LiquiGen (external, real-time GPU, fastest iteration, exports via Alembic), and HydroFX (external, GPU, most fun to iterate with). Ranks tools by bake time, cache size, viewport performance, and final quality; honorable mention to an untested AI water LoRA.
- **File:** tutorials/i-tested-5-different-ways-to-simulate-water.md


### How to make this style in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=oAKrQboXo78
- **Author:** Bad Normals
- **Blender Version:** 5.x (viewport/UI style, exact point release not stated)
- **Tags:** shaders, materials, gradients, color-ramp, node-groups, evaluate-closure, generated-coordinates, glass, emission, light-path, capsule-shader, intermediate
- **Summary:** A style-replication tutorial (Bad Normals recreating art by Taiwanese artist Damon Zhang/Damong) that turns a flat piece of 2D concept art into a procedural Blender material technique. It covers building rounded "capsule" primitives cheaply (Bevel modifier instead of a Metaball or heavily-subdivided mesh), placing many of them precisely using snapping/x-ray/box-select instead of manual duplicate-and-nudge,...
- **File:** tutorials/how-to-make-this-style-in-blender.md


### Realistic Ocean in Blender From Scratch (No Plugins)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=1eQp-H73zeI
- **Author:** Vlabs
- **Blender Version:** not stated on screen (Gabor Texture + Principled Volume node — Blender 4.x/5.x compatible)
- **Tags:** materials, shaders, ocean, water, procedural-texture, gabor-texture, displacement, volume-scattering, light-path, eevee-cycles, beginner
- **Summary:** A fast (under 6 minutes), plugin-free walkthrough for building a stylized/cinematic ocean using only built-in Blender nodes and modifiers — no Ocean modifier, no Flip Fluids, no third-party add-ons. It layers four independent techniques: (1) a Displacement modifier over a subdivided plane, driven by a Voronoi texture, to sculpt rocky terrain without manual sculpting; (2) a Gabor Texture → Bump node combo for a...
- **File:** tutorials/realistic-ocean-in-blender-from-scratch-no-plugins.md


### Doing Surface Imperfections Right | Vray, Cycles, Arnold..
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=OW4L0vdo_e4
- **Author:** Lucas
- **Blender Version:** N/A — cross-renderer conceptual video (Vray/Cycles/Arnold)
- **Tags:** shading-theory, material-layering, roughness, surface-imperfections, blend-shader, cross-renderer, principled-bsdf, dirt-and-grime, intermediate
- **Summary:** This is not a Blender screen-recording — it is a cross-renderer shading-theory video (demoed live in 3ds Max with Chaos Corona / V-Ray-style material editor UI, with Cycles and Arnold discussed conceptually) about how to correctly author "surface imperfections" like fingerprints, dust, dirt, stains, and grease. The core argument: roughness-map-driv...
- **File:** tutorials/doing-surface-imperfections-right-vray-cycles-arnold.md


### Everything New in Blender 5.2 LTS 🍪
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=FlKu6e_VrDc
- **Author:** CG Cookie – Learn Blender
- **Blender Version:** 5.2 LTS
- **Tags:** blender-5x, release-notes, geometry-nodes, grease-pencil, rigging, animation, rendering, eevee, cycles, compositing, feature-survey
- **Summary:** A comprehensive "what's new" survey for the Blender 5.2 LTS (Long Term Support) release, structured as a multi-presenter compilation (each department narrated by a different community member/CG Cookie contributor) rather than a single workflow tutorial. It functions as an index of new features and quality-of-life changes rather than a deep dive int...
- **File:** tutorials/everything-new-in-blender-52-lts.md


### Blender 5.2 Health Potion Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=NrK9FjcNBJA
- **Author:** Polygon Runway
- **Blender Version:** Blender 5.2
- **Tags:** materials, shaders, procedural, glass, product-viz, lighting, hdri, compositing, rendering, cycles, blender-5x, intermediate
- **Summary:** Full "health potion" prop build: models bottle/liquid/cork/label from one duplicated cylinder (Shift+D + P separate workflow), shades glass and red liquid with noise-driven roughness variation, and uses Blender 5.2's new Thin Wall Principled BSDF option for translucent paper label and backlit liquid glow from an interior point light. Finishes with Essentials/Polyhaven HDRI + ground texture and a compositor pass (Bloom, DOF, color curves).
- **File:** tutorials/blender-52-health-potion-tutorial.md



### Perfect Textures in Blender - Works Every Time
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=s-kGlEsXTQw
- **Author:** Nico Linde
- **Blender Version:** Not specified (modern 4.x/5.x UI; version-agnostic)
- **Tags:** materials, shaders, procedural, rendering, cycles, intermediate
- **Summary:** Nico Linde's four-step recipe for believable materials without UV unwrapping: (1) box-project 2–3+ image textures at the shader level (Generated + Box projection) and blend them with image masks / Multiply-Screen-Overlay modes instead of plain opacity; (2) make the shader geometry-aware with Ambient Occlusion nodes — Inside+small Distance for edge wear (grunge texture into AO Distance, Math-Divide for thickness), normal AO multiplied in for cavity grime; (3) drive Roughness via Color Ramp and Normal via Bump with Distance ≈0.01–0.02 (never the 1m default); (4) integrate into the environment by mixing in Alt-click-averaged sampled surround colors, or blending the ground's shader via Mix Shader + Gradient Texture driven by an Empty.
- **File:** tutorials/perfect-textures-in-blender---works-every-time.md


### Quick & Easy Megastructures in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=DX36hit2g0s
- **Author:** Nico Linde
- **Blender Version:** Not specified (modern 4.x/5.x; version-agnostic)
- **Tags:** materials, shaders, displacement, modeling, sci-fi, intermediate
- **Summary:** Build detailed sci-fi megastructures fast using two methods: kitbashing greeble packs, and displacement detailing — subdivide + Simple subdivision modifier + Displace modifier (UV coords, Edit-Mode visibility on) driven by JSplacement-generated panel/circuit maps (~1M face budget, Decimate afterwards). Red paint panels are masked by the displacement map itself through a Color Ramp + Multiply Mix so paint follows panels; windows mix Emission/Transparent shaders with a JSplacement window mask. Space-station demo: cylinder → inset/bridge/loops/bevels, P-separate the section to displace, duplicate the ring, then selective greebles (antennas/railings) to break the silhouette.
- **File:** tutorials/quick-easy-megastructures-in-blender.md


### Photoreal Volumetrics in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=0xZby2ObL6o
- **Author:** Nico Linde
- **Blender Version:** Not specified (modern 4.x/5.x; version-agnostic)
- **Tags:** volume, materials, shaders, lighting, hdri, rendering, cycles, intermediate
- **Summary:** Three-layer photoreal volumetrics on an A.N.T.-Landscape mountain scene (photo-projected textures, HDRI, silhouette for scale): (1) haze cubes with Principled Volume at tiny densities (~0.001) rigged as Value → Math-Multiply → both Density and Emission Strength, sky-sampled RGB into Color + Emission Color — one slider controls everything; use one overall + one distance cube; (2) ground fog via Gradient Texture + Mapping + Color Ramp (duplicate rotated over peaks to sell height); (3) free JangaFX VDB clouds — Attribute(density) into Emission Color, and uncheck Custom Range in render settings so distant volumes render; VDBs double as fog to break gradient smoothness, animate Mapping location mixed with noise for movement.
- **File:** tutorials/photoreal-volumetrics-in-blender.md


### Photoreal Skies In Blender 5.0
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=nXubB9krxVI
- **Author:** Extra 3d
- **Blender Version:** Blender 5.0
- **Tags:** lighting, hdri, volume, materials, shaders, rendering, blender-5x, beginner, intermediate
- **Summary:** Animation-safe cinematic skies without volumetric cost: use pure-sky HDRIs (Polyhaven >8K HDR or free collections) for the backdrop; for daytime keep Sky Texture as the light source (match Sun Rotation to the HDRI; demo 0.545°/36°/185°, strength 0.1) and mix the two World Background nodes with Light Path → Is Camera Ray so the camera sees the HDRI while the Sky Texture lights the scene. Depth tricks: scene-covering cube with near-zero-density Principled Volume at anisotropy 0.7; dark max-roughness light-blocking plane behind camera (camera visibility off, bounds display); cloud-shadow plane (Noise Texture → Color Ramp → Alpha) between sun and scene; fake fog = bluish low-strength Emission in the Volume socket.
- **File:** tutorials/photoreal-skies-in-blender-50.md


### The Easiest Way to Texture in Blender (Adaptive, No UV Unwrapping)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=AMnMbxEwa7Q
- **Author:** Grant Abbitt (Gabbitt)
- **Blender Version:** Blender 5.0
- **Tags:** materials, shaders, modeling, beginner, blender-5x
- **Summary:** Texture complex hard-surface objects with zero UV unwrapping: Node Wrangler Ctrl+Shift+T auto-wires a freepbr.com PBR set, then switch texture coordinates from UV to Object and every Image Texture's projection from Flat to Box (Alt-click edits all selected nodes), raising Blend (~0.2) to dissolve projection seams — the material then adapts live to any mesh edit (loop cuts, insets, extrudes). Also covers the classic gotcha: Ctrl+A Apply Scale before beveling (non-uniform scale skews Ctrl+B), and the limitation that game-engine export still requires unwrap + bake at the end (model with live textures first, bake onto the final unwrap).
- **File:** tutorials/the-easiest-way-to-texture-in-blender-adaptive-no-uv-unwrapping.md


### 3 Easy steps to make Realistic Materials
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=hAWLqRpzK6I
- **Author:** Jamie Dunbar
- **Blender Version:** Not specified (Cycles for Bevel/Pointiness; AO or baking for EEVEE)
- **Tags:** materials, shaders, procedural, rendering, cycles, intermediate
- **Summary:** Fully procedural paint-over-metal wear shader on a shader ball: edge wear from the difference of two Bevel nodes (0 vs 0.002) through a Constant ramp (~0.01) roughened with multiplied noise; scratches from Voronoi Distance-to-Edge masked by a same-scale Voronoi F1 (shared Value ≈10) randomized by Musgrave into the mapping; random noise damage; all Add-combined into a Mix Shader factor plus an inverted Bump (~0.2). Dirt layer: object-space Gradient Texture (rot Y −90, apply transforms first) with noise added into its mapping vector, tinting the paint brown with its own bump. Method guide: Bevel = hard surface, AO = curved/EEVEE-safe, Pointiness = organic sculpts; bake masks to textures for EEVEE.
- **File:** tutorials/3-easy-steps-to-make-realistic-materials.md


### Everything New in Blender 5.2 Geometry Nodes
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=3B9_kJEjsqc
- **Author:** Cartesian Caramel
- **Blender Version:** Blender 5.2
- **Tags:** geometry-nodes, procedural, simulation, release-notes, blender-5x, feature-survey, intermediate
- **Summary:** Complete survey of Geometry Nodes changes in Blender 5.2: experimental XPBD Solver node powering new Cloth/Hair Dynamics modifiers with custom forces; Bundles attachable to geometry (Set/Get Geometry Bundle) crossing modifier/object boundaries; Lists as a core data type (Field to List, Closure to List, List Length, Get/Filter/Sort List, Collection Children); Sound socket + Sample Sound Frequencies for audio-reactive setups; GN on Empties (and thus collection instances); Merge-by-Distance decomposed into Merge Points / Cluster by Distance / Cluster by Connected; Mesh Bevel node with per-edge offsets and selection outputs; new attribute nodes (Rename, Get Names, Transfer, Capture with Selection, 4D storage), NURBS Order/Weight, string nodes, six screen-space/PCA assets, recursive closures, and field-dedup performance gains.
- **File:** tutorials/everything-new-in-blender-52-geometry-nodes.md


### 30 little-known Blender tricks
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=5_Jy97TzZuM
- **Author:** Robin Squares
- **Blender Version:** Not specified (thin film + shader repeat zone imply 4.5+; modern 4.x/5.x UI)
- **Tags:** materials, shaders, procedural, compositing, rendering, cycles, eevee, geometry-nodes, cloth, intermediate
- **Summary:** Rapid-fire collection of 30 short tips: texture bombing (Voronoi per-cell offset), Substance-style histogram-range roughness group, baked-emission instant renders, hybrid Cycles+Eevee fog compositing, shader AOV render passes, Filmic Log grading sandwich, clone-stamp texture tiling on a 3×3 array, thin-film boosting via repeat zone, Dual Mesh instant hexagons, plus workflow one-liners (Ctrl+F2 batch rename, Ctrl+F node search, GPU driver restart, EXR/DWAB output, realistic albedo 0.2–0.9, shot numbering by tens).
- **File:** tutorials/30-little-known-blender-tricks.md


### Blender 5.0: How to UV Unwrap Anything
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=dm3bBpZVmnE
- **Author:** On Mars 3D
- **Blender Version:** Blender 5.0
- **Tags:** materials, modeling, beginner, intermediate, blender-5x
- **Summary:** Universal 5-step UV workflow (apply scale, project from view, mark seams, unwrap, pack islands) applied to hard-surface, sub-D, triangulated and organic models, with seam-placement logic, checker-map + UV Stretch verification, and Blender 5.0 updates: UV sync on by default, mark seam inside the UV editor, pack to custom region, arrange islands. Ends with hiding seams via tri-planar projection and 3D painting in Substance Painter.
- **File:** tutorials/blender-50-how-to-uv-unwrap-anything.md


### Brand New Material Assets in Blender 5.2 LTS
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QkIr1-lDPW0
- **Author:** Blender Studio
- **Blender Version:** 5.2 LTS
- **Tags:** materials, shaders, procedural, displacement, beginner, blender-5x
- **Summary:** Overview of Blender 5.2's first bundled procedural material assets (Essentials library, online assets): downloading, drag-to-assign, the packed-data model (click packed indicator to make local and unlock parameters), 1 UV unit ≈ 1 m² mapping convention, non-tiling procedural coverage, per-material parameter exploration (Fabric–Linen, Wooden Boards–Herringbone), and enabling displacement with Subdivision Surface or Cycles Adaptive Subdivision.
- **File:** tutorials/brand-new-material-assets-in-blender-52-lts.md


### How to texture REALISTIC buildings in Blender #b3d
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ilaD-V8R1gI
- **Author:** CG Boost
- **Blender Version:** Not specified (modern 4.x/5.x UI)
- **Tags:** materials, shaders, procedural, displacement, intermediate
- **Summary:** All-in-one building texturing pipeline: box-mapped PolyHaven PBR bases (Object coords, Box projection blend 0.3, bump-only displacement), material blending via Mix Shader + Mix pairs with grunge→ColorRamp masks, stacked color variations, hand-painted wall paint and damage masks (custom rake/view-plane brushes), stencil-painted decals on an alpha-0 4K image (drips, dirt, graffiti), and procedural finishing: Bevel+Geometry dot-product edge wear and AO-node dirt with Less Than grunge breakup.
- **File:** tutorials/how-to-texture-realistic-buildings-in-blender-b3d.md


### 4 new retopology tips to discover! - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=24EtrCpg4Iw
- **Author:** Blender Secrets
- **Blender Version:** Not specified (modern 4.x/5.x UI)
- **Tags:** modeling, organic, beginner, intermediate
- **Summary:** Four retopology workflow upgrades: the Retopology overlay with tunable depth offset (replaces In Front + backface culling), Ctrl+RMB extrude that orients geometry while extruding, the Relax Slide sculpt brush for redistributing vertices without volume loss, and Face Nearest snapping (vs Face Project) for extruding around limb-like forms; cleanup via LoopTools Space and Ctrl+R.
- **File:** tutorials/4-new-retopology-tips-to-discover---blender-secrets.md


### This Blender Shader is the Secret to Magical 3D Art
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mQPFjzAgGQo
- **Author:** Levi Magony
- **Blender Version:** Not specified (EEVEE + real-time compositing, 4.x/5.x era)
- **Tags:** shaders, materials, procedural, eevee, compositing, motion-design, abstract, intermediate
- **Summary:** 9-step lightless procedural "magical crystal" shader in EEVEE: generated-coord Z gradient, Layer Weight (Facing) fake lighting with remapped normals, object-space Voronoi + noise frosted color variations, camera-space dual-Voronoi subtract cracks, reflection-space ambient color and diagonal highlight lines, emission+transparent mix driven by shading (Blended render method), plus a Grease Pencil line art rig (Tint gradient from empty, Simplify Sample → Dot Dash → Noise → Envelope) and real-time compositor Bloom + masked Sun Beams. Hex colors captured in frames.
- **File:** tutorials/this-blender-shader-is-the-secret-to-magical-3d-art.md


### 5 Lighting SECRETS in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qQgK7gYbvco
- **Author:** Max Hay
- **Blender Version:** Not specified (modern 4.x UI)
- **Tags:** lighting, volume, cycles, rendering, shaders, intermediate, advanced
- **Summary:** Five advanced lighting tricks from client work: image textures inside light sources via Use Nodes (phone photos of refracted light, fake water caustics; radius blurs the pattern), gobo planes with noise/image alpha masks parented to lights, reliable god rays (small-radius hard light + complex shadow caster + volume scatter cube at density 0.02–0.3), fake bounce lights (large radius, ~100W, color-matched, placed where bounce already exists, Ray Visibility volume scatter off), and Light Falloff → Color Ramp for distance-based color gradients (red near → blue far).
- **File:** tutorials/5-lighting-secrets-in-blender.md


### Create a Walk Cycle animation in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=SLh3hUIxv1s
- **Author:** Pierrick Picaut
- **Blender Version:** Blender 5.x
- **Tags:** animation, rigging, organic, beginner, intermediate, blender-5x
- **Summary:** Classic 4-key-pose walk cycle (Contact 1/13/25, Down 4/16, Passing 7/19, Up 10/22 at 24 fps) blocked pose-to-pose on the free P2M mannequin rig with no graph editor: asset-library linking + library override, Action Editor with Only Insert Available, constant interpolation, Ctrl+Shift+V mirrored paste, Breakdowner (Shift+E) for linear grounded-foot placement, contrapposto hips/chest, arm drag, heel-controller-only foot rotation, and airborne-foot swing/twist finishing touches.
- **File:** tutorials/create-a-walk-cycle-animation-in-blender.md


### Hair Grooming in Blender ft. New Hair System (Hair Curves)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=pQcYoH4H1MM
- **Author:** adiidiin
- **Blender Version:** Not specified (hair-curves system, 3.5+ node-group assets)
- **Tags:** organic, geometry-nodes, materials, shaders, animation, beginner, intermediate
- **Summary:** Full hair/eyebrow/eyelash workflow with the hair-curves system: inward-scaled UV'd scalp mesh + Empty Hair, sculpt-mode grooming with all Interpolate options on, stacked node-group modifiers (Set Hair Curve Profile → Duplicate → Clump → Curl → Trim → Interpolate Hair Curves), weight-painted vertex groups pasted into Density Mask per region, Principled Hair BSDF with Curves Info intercept/random color ramps, shrinkwrapped mirrored brows, and Attach Hair Curves to Surface lashes.
- **File:** tutorials/hair-grooming-in-blender-ft-new-hair-system-hair-curves.md


### the New Blender Fluid Simulator is AWESOME - MantaFlow Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=JYc_6fXEjw4
- **Author:** CG Geek
- **Blender Version:** Blender 2.83 Alpha
- **Tags:** fluid, simulation, particles, materials, shaders, glass, rendering, cycles, hdri, compositing, intermediate
- **Summary:** Full built-in MantaFlow liquid pipeline: Domain (Liquid, Resolution 64→128+, FLIP, FLIP Ratio 0.970)/Inflow-sphere/Effector-cube setup, live Replay-cache preview, and three-stage baking (Fluid → Mesh with Speed Vectors → Particles with Spray/Foam/Bubbles). Finishes with a Cycles Glass BSDF fluid material under an HDRI, Transparent Glass film settings, icosphere-instanced foam/bubble particles (randomized "Splash" collection to hide MantaFlow's grid-pattern bug, per-particle opacity via Object Info Random), camera DOF, and a Vector Blur compositing node for fluid motion blur.
- **File:** tutorials/the-new-blender-fluid-simulator-is-awesome---mantaflow-tutorial.md


### Fluid Simulations for Beginners Blender Tutorial ( FLIP Fluids)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=PcYQtV1_nRg
- **Author:** Fattu Tutorials
- **Blender Version:** Blender 4.3.2
- **Tags:** fluid, simulation, materials, rendering, cycles, hdri, lighting, beginner, blender-4x
- **Summary:** Fast settings-focused FLIP Fluids (paid add-on) workflow: a scaled cube becomes the Domain and a UV sphere becomes the Fluid object, with a ground-plane Obstacle and framed camera. Domain settings cover Resolution 75, World (Surface Tension + Sheeting Effect), Materials (FF Water Ocean Volumetric with Foam/Bubbles/Spray), and Advanced FLIP Whitewater, baked over 300 frames and rendered in Cycles (GPU, 128 samples) under HDRI lighting.
- **File:** tutorials/fluid-simulations-for-beginners-blender-tutorial-flip-fluids.md


### How this 2D/3D animation was made - Introduction to Blender greasepencil and tips for beginners
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=saIFT8_j0LQ
- **Author:** Dédouze
- **Blender Version:** Not specified (Blender 3.x-era 2D Animation workspace)
- **Tags:** animation, motion-design, materials, shaders, rigging, compositing, beginner, intermediate
- **Summary:** Technique breakdown (not a build tutorial) of a YouTube Premiere countdown scene made entirely with Grease Pencil: flat hand-drawn "canvas" objects floating in 3D space (frame-by-frame + onion skinning + sculpt-tool in-betweens + auto-interpolation), looped via Time Offset, warped by a Lattice driven by a parented Armature, or projected onto 3D surfaces via Surface draw-mode placement. 3D objects use a custom hard-stepped toon shader plus a duplicated-and-inverted Solidify outline. Closes with tips: one-face-per-object canvases, canvas-local double-tap axis moves (G, X, X), and Auto-Keying caution.
- **File:** tutorials/how-this-2d3d-animation-was-made---introduction-to-blender-greasepencil-and-tips.md


### Product Animation in Blender: Phone
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=lZPedlX6CMw
- **Author:** Derek Elliott
- **Blender Version:** Blender 2.8
- **Tags:** materials, shaders, glass, metal, eevee, lighting, animation, camera, product-viz, brand-video, intermediate
- **Summary:** Full 75-minute EEVEE product-commercial pipeline: Boolean-based hard-surface phone modeling (Bevel + Solidify + cutout Booleans), metallic/glass/emission materials (including a live video texture on the screen), manual studio lighting (Point Light + Area Lights, no HDRI), and beat-synced keyframe animation across 7 scenes — a basic pan, a shape-key button press, an exploded camera-cluster reveal, a two-color reveal, a black-background float, a double-float, and an audio-waveform-synced multicolor finale.
- **File:** tutorials/product-animation-in-blender-phone.md


### Master Blender Sculpting: Every Brush Explained
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=5-mNgCpEkCI
- **Author:** Grant Abbitt (Gabbitt)
- **Blender Version:** Blender 4.3.1
- **Tags:** organic, displacement, cloth, intermediate, blender-4x
- **Summary:** Full brush-by-brush survey of Blender 4.3's Sculpt Mode: add/subtract brushes (Draw, Clay, Clay Strips, Crease Polish/Sharp, Inflate, Layer, Flatten, Scrape, Trim), push/pull brushes (Grab, Snake Hook, Grab Silhouette, Pose, Boundary), and the full cloth-simulation brush family (Drag/Expand/Bend/Twist Cloth, Grab Planar, Pinch Folds), plus Mask and Face Sets. Anchored on the Voxel Remesh (R gizmo + Ctrl+R) and Dyntopo workflows needed to keep enough topology under each brush, and notes which brushes require a non-manifold mesh with real boundary edges.
- **File:** tutorials/master-blender-sculpting-every-brush-explained.md


### Easy Rigging Using RIGIFY in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RdTuAY23vzk
- **Author:** Grant Abbitt (Gabbitt)
- **Blender Version:** Blender 4.3
- **Tags:** rigging, animation, beginner, intermediate, blender-4x
- **Summary:** Rigs a low-poly character with the Rigify add-on: adds and scales the Human meta-rig, matches bones to the mesh in Edit Mode (X-Mirror, Snap-to-Volume, deleting unused finger/face bones), applies scale, Generates Rig, parents the mesh with Automatic Weights, then walks through the color-coded control bones (IK/FK, tweak, foot roll). Finishes by fixing cross-object weight-paint bleed using Alt+Click bone preview and Auto Normalize.
- **File:** tutorials/easy-rigging-using-rigify-in-blender.md


### Camera Tracking in Blender for Beginners | Motion Tracking Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=IvyfdxkABKU
- **Author:** 3Dnot2D
- **Blender Version:** Blender 4.x (AgX default, switched to Standard; Cycles GPU)
- **Tags:** camera, compositing, rendering, cycles, hdri, lighting, product-viz, intermediate, blender-4x
- **Summary:** Full camera match-move pipeline: tracks handheld footage of a plaza (manual + automatic marker detection, Detect Features, Track Forward/Backward), solves the camera (Solve Error tuning via Clean Up/Filter Tracks down to ~0.25px), sets Floor/Origin/Axis/Scale from tracked markers, then composites a 3D car into the shot with a Poly Haven HDRI matched to the footage lighting (Node Wrangler Mapping rotation), a matte ground shadow-catcher, and a transparent-film Cycles render assembled back over the plate in an NLE.
- **File:** tutorials/camera-tracking-in-blender-for-beginners-motion-tracking-tutorial.md


### Blender 2D Animation Tutorial for Beginners (Grease Pencil Tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=5epzCprCdGc
- **Author:** Jesse J. Jones
- **Blender Version:** Blender 3.6
- **Tags:** animation, camera, motion-design, beginner, blender-3x
- **Summary:** End-to-end beginner Grease Pencil 2D animation workflow: drawing tools and Draw/Object/Edit/Sculpt modes, a bouncing-ball exercise using Auto Keying with keyframe duplicate/reverse/retime tricks (Shift+D, S -1, S 2 for ones-vs-twos), Fill tool coloring (Multi Frame + Inverted Fill, Holdout materials), masked-layer cel shading, background image planes with camera parallax animation, and audio-driven lip sync with a mouth-shape reference chart.
- **File:** tutorials/blender-2d-animation-tutorial-for-beginners-grease-pencil-tutorial.md


### Blender Sound Reactive Geometry Nodes | Tutorial How-To Audio Music Simulation Mograph
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=XOsXZ1qDfSk
- **Author:** Chris P
- **Blender Version:** Blender 3.6.1
- **Tags:** geometry-nodes, simulation, particles, procedural, animation, materials, shaders, motion-design, abstract, advanced, blender-3x
- **Summary:** Pure-Blender audio-reactive motion graphics with no add-ons: bakes 3 frequency bands (bass/mid/high) of a music track to F-Curves via the Graph Editor, then drives three Geometry Nodes systems from the baked values — bass-triggered bubbles that spawn and shrink inside a Simulation Zone, mid-range particles emitted along surface normals whose velocity scales with volume, and random high-frequency "laser" line bursts gated by a threshold. Includes cartoon-cloud bubble shading (Layer Weight + Color Ramp) and age-based particle emission color.
- **File:** tutorials/blender-sound-reactive-geometry-nodes-tutorial-how-to-audio-music-simulation-mog.md


### How to Quickly Create Clothing using Blender and Marvelous Designer
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Rp1G9mIBskI
- **Author:** Martin Klekner
- **Blender Version:** Blender 2.8 RC (+ Marvelous Designer)
- **Tags:** cloth, organic, animation, intermediate
- **Summary:** Blender <-> Marvelous Designer round-trip pipeline for simulated character garments: pose the character to a clean T-pose at frame 1, bake and export FBX, then in Marvelous Designer pattern flat fabric rectangles (Edit Pattern, Add Point, Edit Curvature), mirror them, Segment-Sew the seams, simulate the drape, gather the waist with an elastic Internal Line, Pin fabric to fixed spots for a cloak, change Fabric Type presets (linen/wool/silk), remesh to clean topology, and reimport the OBJ into Blender for scale/normal cleanup.
- **File:** tutorials/how-to-quickly-create-clothing-using-blender-and-marvelous-designer.md


### New Compositing Effects in Blender 5.2!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=UhlIT_-3xQM
- **Author:** Ryan King Art
- **Blender Version:** 5.2
- **Tags:** compositing, procedural, rendering, cycles, beginner, intermediate, blender-5x
- **Summary:** Tour of new Blender 5.2 Compositor nodes: String to Image (text-in-compositor, composited via Alpha Over Fac), GPU-default compositing, and new stylized asset-shelf effects — Film Grain (stock presets), Night Vision (depth-darken, distortion, glare), Depth Atmosphere (Depth-pass or Mist-pass driven fog with Min/Max Distance and tint), Dithering (Bayer pixel-art), Paint Filter (Watercolor/Oil Paint/Custom stroke texture), and Rim 2D (transparent-background edge outline/rim light). Flags Normal Mask, Position Mask, and Exposure Visualization as undocumented new nodes.
- **File:** tutorials/new-compositing-effects-in-blender-52.md


### Forgotten Metal Knowledge | Vray, Cycles, Arnold..
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=uz8PIi3ELJg
- **Author:** Lucas
- **Blender Version:** Not specified (3.x/4.x-era Cycles)
- **Tags:** materials, shaders, metal, procedural, cycles, product-viz, advanced
- **Summary:** PBR shading theory (hands-on in Cycles) on recreating the "reflection tail-off" of real polished/scratched metal by layering multiple BSDFs (duplicated Principled BSDF or mixed Glossy BSDF nodes via Mix Shader) of increasing roughness/decreasing presence, instead of one Roughness value. Compares against Clearcoat/Coat Weight (distorts base color, not properly metallic) and a GGX Tailoff exponent control (cheap but limited/not exposed in Cycles), validated with ground-truth turntable comparisons and a 52-artist survey.
- **File:** tutorials/forgotten-metal-knowledge-vray-cycles-arnold.md


### BLENDER - Full animated character course for Free : THE GAMEBOY PROJECT PART 01
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mapuLpQNSAw
- **Author:** Pierrick Picaut
- **Blender Version:** Not specified (~2020-era Blender 2.8x based on UI)
- **Tags:** modelling, hard-surface, procedural, beginner
- **Summary:** Part 1 of a free 16-part Game Boy character course (Pierrick Picaut/P2Design, released free during COVID-19 lockdown). Hard-surface box modeling of the handheld's case from a blueprint reference: Inset Face + vertex bevel technique for controlled rounded-corner topology, the F2 addon for fast face-fill, and Subdivision Surface + supporting edge loops to keep panel edges straight rather than curving. Closes with vertex-snapped LED recess placement and Grid Fill for the screen face.
- **File:** tutorials/blender---full-animated-character-course-for-free-the-gameboy-project-part-01.md


### BLENDER Easy LED screen shader - THE GAMEBOY PROJECT PART 05
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=BhJfdQn5Sf4
- **Author:** Pierrick Picaut
- **Blender Version:** Not specified (~2020-era Blender 2.8x based on UI)
- **Tags:** shaders, materials, procedural, geometry-nodes, beginner, intermediate
- **Summary:** Part 5 of the free "Gameboy Project" course. Fully procedural, deliberately non-physical shader-editor recipe for a plastic LED indicator (Layer Weight Facing output → Color Ramp gradient, Add Shader for independent emission strength) and a pixelated backlit LCD screen (Gradient Texture vignette + Brick Texture pixel grid multiplied together to drive Emission strength, re-projected UVs via Project From View).
- **File:** tutorials/blender-easy-led-screen-shader---the-gameboy-project-part-05.md


### MetaHumans in Blender: Using OpenRigLogic to Customize DNA's Behavior | Inside Unreal
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=WZhDr5Ktf9c
- **Author:** Unreal Engine
- **Blender Version:** 5.2 LTS (add-on supports 4.5–5.2)
- **Tags:** metahuman, riglogic, dna, facial-rig, rigging, shape-keys, animation, mocap, add-on, unreal-engine, blender-5x, advanced
- **Summary:** Inside Unreal stream with Polyhammer's James Baeber: free Character DNA add-on runs Epic's RigLogic runtime natively in Blender — drag-drop head/body DNA import for a 1:1 MetaHuman rig (face board, poses/visemes, wrinkle-map debugging, RBF-corrected body, RigLogic LODs where editing LOD 0 auto-fixes lower LODs, Texture Logic shader node, MetaHuman Animator mocap import, full DNA round-trip export). Pro editors replace the Maya Expression Editor: Raw Editor with PyTorch hyperopt bone matching (192 bones in 3.7s), Shape Key Editor (zero-delta ghosts, freeze), Behavior Viewer graphing PSD corrective trees, layer-by-layer (L1→L6, MH12/MH50) calibration, Backup Manager with pre/post-commit backups — demonstrated by converting human DNA onto a wrapped ape and fixing its facial rig.
- **File:** tutorials/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea.md


### Perfect Procedural Clouds in Blender | Geometry Nodes Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=6_vwVjODhog
- **Author:** adrien_ltn
- **Blender Version:** Blender 4.x
- **Tags:** geometry-nodes, volume, procedural, cycles, rendering, materials, lighting, hdri, compositing, organic, intermediate, blender-4x
- **Summary:** Fully procedural photoreal clouds without VDBs using the creator's "Cloud Creator" geometry-nodes tool (free Converter / paid Pro), modeled on Houdini's cloud pipeline: a Generator scatters and displaces spheres into cloud silhouettes (Humilis/Mediocris/Congestus/Fractus presets, curve-drawn shapes), a Converter turns any geometry into a particle-scattered volume (Resolution = voxel size, Noise/Flatten/Wind/Vortex tabs, camera-culling optimization, bake to still/animation), and volume shaders add billowy noise, Z-gradient colors, and edge halation. Rendering half: Cycles Volumes Max Steps 10–25 for sane render times, HDRI-first lighting ("90% lighting, 10% shader"), Volume Direct/Indirect passes for comp, and rendering clouds on separate layers every 2–10 frames interpolated with Flowframes.
- **File:** tutorials/perfect-procedural-clouds-in-blender-geometry-nodes-tutorial.md


### Create an Audio Visualizer with Geometry Nodes in Blender 5.2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=h_Q91x_8dd4
- **Author:** Ryan King Art
- **Blender Version:** 5.2
- **Tags:** geometry-nodes, animation, motion-design, procedural, materials, metal, lighting, compositing, cycles, rendering, abstract, intermediate, blender-5x
- **Summary:** Bar-style audio visualizer built on the new Sample Sound Frequencies node (5.2): a UV-unwrapped row of planes maps UV X into the Low/High frequency inputs via Map Range nodes, and Amplitude drives Extrude Mesh along normals (Offset Scale 40, To Min 250/600 for variation/strength). Finished with Mesh Bevel, grungy metal material, red/blue area lighting, Bloom + chromatic aberration compositing, and a frames-to-Video-Editor pipeline synced to the audio.
- **File:** tutorials/create-an-audio-visualizer-with-geometry-nodes-in-blender-52.md


### I Fixed a Difficult Animation Issue! (Kind Of)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ZqON1ms8VOM
- **Author:** Curtis Holt
- **Blender Version:** Not specified
- **Tags:** animation, rigging, advanced, curtis-holt, vlog
- **Summary:** Talking-head R&D vlog (not a tutorial): Curtis Holt's automated mocap foot-sliding cleanup — classifies support feet via heel/spin control-bone rotation+location thresholds with pre/post keyframe context, then magnetizes the residual offset to the flat grounded pose ("grav boots" snap; kills sliding, needs animator polish). Proposes a body-wide semantic event-labeling pass (queryable markers: fingers open/close, foot plants) to replace per-script context detection; also covers markerless mocap's missing hand capture, Rokoko Smart Gloves vs a DIY ESP32 glove idea.
- **File:** tutorials/i-fixed-a-difficult-animation-issue-kind-of.md


### How to Create Stylized Feathers and Fur in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=yR8FatqgTDQ
- **Author:** SouthernShotty
- **Blender Version:** Not specified (4.2+ UI)
- **Tags:** geometry-nodes, procedural, materials, shaders, eevee, animation, organic, particles, intermediate
- **Summary:** Stylized EEVEE-friendly feathers/fur: the bundled Scatter on Surface preset (density 150, Y-aligned, randomized rot/scale) is unpacked and extended with the key trick — Set Mesh Normal (Free) fed by Sample Nearest Surface from a hidden smooth proxy sphere so all instances shade as one smooth surface — plus a Scene Time/Noise → Rotate Instances idle-motion rig and an instance-domain "ran_color" Random Value attribute. Feather shader layers UV gradient, stretched noise lines (Scale 2, Distortion 1.1, UV X×5), random color mix (0.25), and a Layer Weight → HSV (Value 5) fake rim light; EEVEE looks best with ray tracing off or Fast GI tamed (1 ray/4 steps, thickness 0.1, bias 0.25).
- **File:** tutorials/how-to-create-stylized-feathers-and-fur-in-blender.md


### How to Create a Time Shift Blur in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=TYo0Vpf13E0
- **Author:** Kai🔸
- **Blender Version:** 5.x (5.2+ for footage modifier)
- **Tags:** compositing, motion-design, camera, animation, procedural, advanced, blender-5x
- **Summary:** Builds the film "time shift" shutter-desync streak (Project Hail Mary aspect-ratio blends) as a reusable compositor group asset: highlights isolated via Map Range 0.5 + threshold mix, smeared with Directional Blur (64 samples, −π/2 angle offset), and edge-wrapped through a hand-built 32-tap Translate-node accumulator (Repeat sampling, taps at index/31, 5-stage halving cascade with 0.001008 shift) run twice (Repeat − Clip) so only the wrapped tail is added back at 0.72. Exposes Highlight Threshold, Streak Length, Angle, Wrap/Symmetric toggles, Intensity/Tint panel, Scene Time 1D-noise animated jitter, Mask input, and a streaks-only output; usable in 5.2+ as a non-destructive modifier on video footage.
- **File:** tutorials/how-to-create-a-time-shift-blur-in-blender.md


### How to Blend Separate Objects in Blender. Easy Method!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=KGf58mE5fZI
- **Author:** Kenan Proffitt
- **Blender Version:** 5.1
- **Tags:** geometry-nodes, procedural, materials, shaders, displacement, organic, intermediate, blender-5x
- **Summary:** Boolean-free blending of a rock into terrain with Geometry Nodes: ground-object Geometry Proximity (via Relative Object Info) drives Map Range + reversed Color Ramp displacement at the contact (strength ~0.1, optionally mirrored onto the ground at the cost of a Join Geometry), Sample Nearest Surface (Vector, Normal→Value) mixed with the mesh's own normal by proximity distance feeds Set Mesh Normal (Free) so both surfaces shade as one, and the ramp color is stored as a "blend" attribute driving a Mix Shader between the two materials (each Ctrl+G-grouped into a clean master material). Fully dynamic — move/sink the rock and the blend follows.
- **File:** tutorials/how-to-blend-separate-objects-in-blender-easy-method.md


### [Tut] How Pick Instance is used for Instance Variations - P10 Geometry Nodes Beginners
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=fgPiXjKkRdI
- **Author:** Bradley Animation
- **Blender Version:** Not specified
- **Tags:** geometry-nodes, procedural, instancing, beginner
- **Summary:** Beginner-series episode on faking instance variation in Geometry Nodes: recaps Object Info (Original/Relative transforms, the self-reference "geometry cannot be retrieved" error, and the As Instance toggle for perf + instancing lights/cameras), then covers the core recipe — Collection Info + Separate Children + Pick Instance on Instance on Points — to pick a different pre-made variant per point, with Instance Index + a Random Value node to randomize which variant lands where. Also covers Geometry to Instance for procedurally-generated variants.
- **File:** tutorials/tut-how-pick-instance-is-used-for-instance-variations---p10-geometry-nodes-begin.md
- **Related:** [Tut] Different Instance Color and Materials - P13 Geometry Nodes Beginners (`tut-different-instance-color-and-materials---p13-geometry-nodes-beginners.md`) — direct successor in the same series; this episode's geometry variation vs. P13's color/shader variation.
- **Related:** Easy Geometry Nodes - Low-poly Rocks Blender 5.1 (`easy-geometry-nodes---low-poly-rocks-blender-51.md`) — shares geometry-nodes/procedural/instancing/beginner tags, also uses Distribute Points + Instance on Points (Pick Instance) for per-point variety.
- **Related:** [Tut] Everything about For Each Element Zone in Variations - P14 Geometry Nodes Beginners 5.0+ (`tut-everything-about-for-each-element-zone-in-variations---p14-geometry-nodes-be.md`) — later episode that explicitly contrasts this episode's "fake variation" (Pick Instance) with FEEZ's "real variation" approach.


### Blender Finally Did It!!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=KNqV2wJgxVM
- **Author:** Ducky 3D
- **Blender Version:** 5.2
- **Tags:** geometry-nodes, procedural, displacement, animation, lighting, rendering, cycles, motion-design, abstract, volume, intermediate, blender-5x
- **Summary:** Showcases Blender 5.2's new native Mesh Bevel node in Geometry Nodes (no more external-model-then-instance workaround). Builds a volume-distributed grid of beveled cube instances whose scale is driven by an animated, looping Noise Texture → Color Ramp, plus a culled cylinder "rain line" accent layer, finished with a white emission-plane rim light and an orange disc Area Light in Cycles.
- **Related:** A New Way To Loop Animations in Blender (`a-new-way-to-loop-animations-in-blender.md`) — the exact loop-keyframe trick referenced directly in this video's transcript. Also shares tags with Blender 5.0's NEW Audio Visualisation is INSANE! (volume, blender-5x), Glass Cell Division Effect in Blender 5.0 (abstract, blender-5x), and You Should Make Glass Animations in Blender 5.1 (motion-design, cycles, blender-5x) — all Ducky 3D "new 5.x feature" showcases.
- **File:** tutorials/blender-finally-did-it.md


### Photoreal Metahumans In Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=kaDtwG3JimM
- **Author:** Extra 3d
- **Blender Version:** Not specified (viewport UI consistent with Blender 4.x — modern tab layout, Cycles GPU compute)
- **Tags:** materials, shaders, rigging, animation, cycles, organic, advanced
- **Summary:** Full photo-to-MetaHuman pipeline: generates a likeness head mesh from one photo in Meshy AI, uses it to facial-track and conform a MetaHuman preset in Unreal Engine 5 (Identity + Character tools), then exports the DNA rig and grooms and reassembles the fully textured, groomed character in Blender via the free Polyhammer add-on, including a from-scratch hair/beard shader (Image Texture -> Separate Color -> Principled BSDF) bound to the face with Surface Deform.
- **Related:** MetaHumans in Blender: Using OpenRigLogic to Customize DNA's Behavior | Inside Unreal (`metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea.md`) — shares the MetaHuman DNA / Unreal Engine -> Blender rigging pipeline.
- **File:** tutorials/photoreal-metahumans-in-blender.md


### Beginner Geometry Nodes - Helix Twist [Blender Tutorial]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Y4qk49lryRk
- **Author:** Seanterelle
- **Blender Version:** Not specified (node editor styling consistent with Blender 3.x/early 4.x)
- **Tags:** geometry-nodes, procedural, animation, materials, shaders, rendering, cycles, motion-design, abstract, organic, beginner
- **Summary:** Builds a multi-strand helix that twists together into a rope/candy shape and unwinds apart, animated by frame: strand curves driven by Curve Tilt + Curve Scale off Spline Parameter, resampled onto an evenly-spaced guide curve via Sample Curve for constant strand length, meshed with Curve to Mesh, eased with a Mix+Power node combo, and finished with a glossy subsurface "candy" shader plus a Bake-node trick to keep procedural surface textures from swimming as the geometry animates.
- **Related:** Blender Tutorial - Procedural Rope in Geometry Nodes (`blender-tutorial-procedural-rope-in-geometry-nodes.md`) — same interlocking spiral-strand domain. Curves Just Got Easier in Blender 5.0 (`curves-just-got-easier-in-blender-50.md`) — shares the per-strand attribute-driven shading approach.
- **File:** tutorials/beginner-geometry-nodes---helix-twist-blender-tutorial.md


### The End of Expensive Motion Capture?
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=PUjZECgANYU
- **Author:** Curtis Holt
- **Blender Version:** Not specified
- **Tags:** motion-capture, facial-animation, pipeline, mocap-tools, opinion
- **Summary:** Opinion/R&D-log video (not a build tutorial): argues AI-assisted scripting now gets solo creators ~90% of the way to commercial mocap suite quality using free tools (MetaHuman live-link facial capture + custom Blender Python smoothing/retargeting scripts) instead of paying thousands for hardware/subscriptions. Covers the "90/10 principle" for evaluating tools, remaining pain points (finger capture, body sampling smoothness), and a hard requirement for local/offline operation with no usage limits.
- **File:** tutorials/the-end-of-expensive-motion-capture.md


### Blender PROCEDURAL BUILDING! | Geometry Nodes
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VdxTlfLLe_s
- **Author:** SharpWind
- **Blender Version:** Not specified (recent, modifier UI matches 4.x/5.x)
- **Tags:** geometry-nodes, procedural-generation, architecture, modifier-stack, asset-showcase
- **Summary:** Feature walkthrough (not a build-from-scratch tutorial) of a paid procedural-building geometry-nodes asset: one `Building_Generator` modifier with six grouped panels (General Shape, Colors, Floor Distribution, Details, Roof Elements, Manage) driving brick facade, window/awning distribution, fire escapes, and roof clutter from sliders and seeds. Demonstrates organizing a complex node asset into readable modifier-panel sections rather than the node graph itself.
- **File:** tutorials/blender-procedural-building-geometry-nodes.md


### The Sample Sound Node is So Powerful (Blender 5.2 tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=B0KwaI0Eqqk
- **Author:** Ducky 3D
- **Blender Version:** 5.2
- **Tags:** geometry-nodes, audio-visualization, shading, procedural-generation, motion-graphics
- **Summary:** Intro tutorial to Blender 5.2's new `Sample Sound Frequencies` geometry-nodes node: samples audio amplitude via Scene Time, remaps it with Map Range, and uses it to drive Extrude Mesh offset for both flat and circular (Index-mapped) waveform bar visualizers, plus pushes the same value into the Shader Editor via Store Named Attribute to drive an Emission color.
- **File:** tutorials/the-sample-sound-node-is-so-powerful-blender-52-tutorial.md


### Easy Railing Generator with Geometry Nodes | Blender 5.2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=deAw5dU5Wfs
- **Author:** Max Hay
- **Blender Version:** 5.2
- **Tags:** geometry-nodes, procedural-generation, architecture, modifier-stack, beginner
- **Summary:** Beginner geometry-nodes tutorial building a railing/fence generator from scratch: Mesh to Curve → Resample Curve → Instance on Points, with Curve Tangent + Align Rotation to Vector for orientation and Split Edges + Endpoint Selection to fix corner instancing. Covers exposing node inputs to the modifier for per-object control, Realize Instances for applying, and a looser show-and-tell of an advanced platform/stairs generator plus a Fillet Curve + Curve to Mesh solid-pipe railing variant.
- **File:** tutorials/easy-railing-generator-with-geometry-nodes-blender-52.md


### How to make Godrays in Blender ( NO PLUGINS )
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=alDV81qXQtA
- **Author:** Vlabs
- **Blender Version:** Not specified
- **Tags:** volume, lighting, cycles, rendering, beginner
- **Summary:** No-plugin Cycles god-rays/haze recipe: add a large cube encompassing the scene, delete its Principled BSDF, wire a Volume Scatter node into the material's Volume input, and tune Density (0.01-0.05 for subtle haze, higher for heavy fog) and Anisotropy (0.3-0.6 for stronger god-ray scattering); optionally layer a second lower-density volume cube for extra atmospheric depth.
- **File:** tutorials/how-to-make-godrays-in-blender-no-plugins.md


### Я сделал инструмент, которого мне не хватало в Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=r1SNvD73Qvo
- **Author:** Batyr K.
- **Blender Version:** 4.x/5.x (Simulation Nodes zones, not exactly specified)
- **Tags:** geometry-nodes, simulation, particles, procedural, product-viz, motion-design, abstract, glass, intermediate, blender-4x, blender-5x
- **Summary:** Demonstrates a custom packaged GeoNodes asset (Surface Flow / free Surface Flow Light) that distributes flowing, noise-driven particle instances across any watertight proxy surface — shown on a cream tube product shot, bubbles rising inside a liquid-filled glass, and an abstract vortex hugging a drinking glass. Exposes particle size/density/distribution and Flow Speed/Scale/Type controls without manual node editing; full version adds Stick to Surface, Particle Relaxation, and Self Collision.
- **File:** tutorials/я-сделал-инструмент-которого-мне-не-хватало-в-blender.md


### Sand Simulation - Blender Tutorial (Nexus)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8Swzwo83OP0
- **Author:** CGMatter
- **Blender Version:** Not specified (3.x-4.x era workflow)
- **Tags:** simulation, fluid, particles, geometry-nodes, procedural, typography, materials, abstract, advanced
- **Summary:** Uses the third-party Nexus add-on's granular SPH fluid solver to make a text mesh assemble out of clumping sand particles, driven by an "infection" growth mask (red/blue color-coded) that freezes particles outside the spreading region via a speed clamp. Covers baking to a real Point Cloud object, a Point-Info-driven sandy material, and a cache-retiming trick to make the sand settle and stop instead of jittering forever.
- **File:** tutorials/sand-simulation---blender-tutorial-nexus.md


### Abstract Wave Lines | Looping Curves | Geometry Nodes Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=CztCgbqaiZk
- **Author:** Artemiy Galutskiy
- **Blender Version:** Not specified (silent video, no version indicator visible in captured frames)
- **Tags:** geometry-nodes, procedural, abstract, typography, motion-design
- **Summary:** Music-only video (no narration — extracted from visuals only). Builds a Geometry Nodes setup producing dense, evenly-offset "looping" contour/wave lines that trace the silhouette of input geometry — shown on a flat plane (radiating swirl pattern) and on 3D text (concentric contours around the letter "A"), with a Color Ramp driving line color. Exact node names/values unverified due to lack of audio — re-watch directly for precise parameters.
- **File:** tutorials/abstract-wave-lines-looping-curves-geometry-nodes-tutorial.md


### How to Build After Effects-Style Motion Graphics in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=-cscjxxxebk
- **Author:** Bring Your Own Laptop
- **Blender Version:** Not specified (recent 4.x-era Geometry Nodes UI)
- **Tags:** geometry-nodes, procedural, motion-design, typography, materials, animation, camera, rendering, intermediate
- **Summary:** A Geometry Nodes dot-grid whose per-point scale is driven by proximity (Geometry Proximity → Map Range) to an animated text object, revealing/hiding the text as it slides through — a procedural, After Effects-style kinetic-typography effect. Also covers instance coloring via Object Info Random + Color Ramp sampled from a flat palette image, and the AGX→Standard color-management fix for true graphic-design colors.
- **File:** tutorials/how-to-build-after-effects-style-motion-graphics-in-blender.md


### Fluid sim testing in Blender 5.3! (Rasterize Points Node)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qcOMsFVMMQA
- **Author:** Cartesian Caramel
- **Blender Version:** 5.3
- **Tags:** geometry-nodes, simulation, particles, fluid, volume, procedural, materials, rendering, advanced, blender-5x
- **Summary:** Livestream exploring Blender 5.3's new Rasterize Points and Geometry Materials nodes, building a from-scratch grid-based pseudo-fluid particle sim inside a Simulation Zone: velocity/density rasterized to a voxel grid each step, a Volume Gradient of density drives repulsion, custom SDF node groups handle collision, gravity is delta-time scaled, and at high point counts the sim visibly explodes and resettles fluid-like. Finishes with curve trails colored by velocity length for a colorful energy-trail render.
- **File:** tutorials/fluid-sim-testing-in-blender-53-rasterize-points-node.md


### Easily Add Details to a Surface without Connecting them or using Booleans - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=juXPyDLTJTE
- **Author:** Blender Secrets
- **Blender Version:** Not specified
- **Tags:** materials, procedural, beginner, intermediate
- **Summary:** Snaps a detail mesh onto a host surface using Face Project snapping, then blends the seam with a weight-painted Shrinkwrap modifier (weight 1 at the base fading to 0) and a Data Transfer modifier (custom normals, nearest-face-interpolated) so the two objects shade as one continuous surface — no booleans or geometry merge required.
- **File:** tutorials/easily-add-details-to-a-surface-without-connecting-them-or-using-booleans---blen.md


### Cloth Tearing with Geometry Nodes in Blender 5.2 - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=nhhv9lw152A
- **Author:** Blender Secrets
- **Blender Version:** 5.2
- **Tags:** geometry-nodes, simulation, cloth, procedural, animation, intermediate, blender-5x
- **Summary:** Blender 5.2's experimental Cloth Dynamics geometry node replaces the old Cloth+Hook modifier workflow: empties pin the cloth via Typed Bundle (Pin Position) + Named Attribute nodes into the node's Effectors input, and a native Tearing option with a custom edge-group threshold lets the cloth rip exactly where you choose instead of always at the highest-stress hook point.
- **File:** tutorials/cloth-tearing-with-geometry-nodes-in-blender-52---blender-secrets.md


### 6 Panel Cut Tips - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=IZFniY_vyGo
- **Author:** Blender Secrets
- **Blender Version:** 5.0+ (Instances on Elements modifier is explicitly new in 5.0)
- **Tags:** procedural, materials, displacement, cycles, intermediate, advanced
- **Summary:** Six hard-surface panel-cut methods, most ending in a bake to a normal map: (1) sharp-marked edges + Bevel(Miter Outer=Arc)/Subdivision modifier stack for straight/diagonal cuts, (2) ripped edges (V) for naturally rounded panel corners, (3) Sculpt-mode Mask brush + Curve Stroke + Inflate mesh filter, (4) Sculpt-mode Layer brush with Persistent Base + Line stroke for straight sculpted cuts, (5) direct normal-map painting via the free Youku Paint extension, and (6) the Blender 5.0 Instances on Elements modifier for vertex-group-masked scattered surface details (rivets/bolts) with Realized Instances for baking.
- **File:** tutorials/6-panel-cut-tips---blender-secrets.md


### This technique lets you make Hard Surface models easily
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=_6uBdIsvm7c
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Extra Objects add-on, Multires workflow; 3.x-5.x)
- **Tags:** displacement, procedural, materials, organic, advanced
- **Summary:** Builds a custom tiling hard-surface displacement map from scratch: alpha-brush sculpting with View-Plane texture mapping for seamless tiling, hand-modeled pipe details via a ±tile-size Array modifier for guaranteed edge match, tiling-mismatch troubleshooting, and pre-bake flat-shading checks.
- **File:** tutorials/this-technique-lets-you-make-hard-surface-models-easily.md


### How to model ornamental iron railings in Blender using Curves - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=_1OLudY5qQY
- **Author:** Blender Secrets
- **Blender Version:** Blender 5 (explicitly named for the new curve-mode Array modifier)
- **Tags:** procedural, modelling, organic, intermediate, advanced
- **Summary:** Full cast-iron railing built from Curves: a custom mesh-to-curve Bevel Object for bar thickness, Blender 5's curve-mode Array modifier for rigid spokes, a separate Array+Curve-modifier combo for deforming swirl decorations, and the Curve Pen tool for hand-drawn scrollwork.
- **File:** tutorials/how-to-model-ornamental-iron-railings-in-blender-using-curves---blender-secrets.md


### Easy Ear Sculpting Tip - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=-ij6rXb15yA
- **Author:** Blender Secrets
- **Blender Version:** Not specified
- **Tags:** organic, beginner, intermediate
- **Summary:** Blocks out an ear's cartilage folds as bevel-thickness curves traced over reference photos, converts curves + a separate flat shell plane to mesh, joins and Voxel-Remeshes them into one manifold, then finishes with standard sculpt brushes (Draw, Grab, Clay Strips, Smooth).
- **File:** tutorials/easy-ear-sculpting-tip---blender-secrets.md


### Blender Origin / Pivot Point Tips - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=t_r8qT_4oGM
- **Author:** Blender Secrets
- **Blender Version:** Not specified
- **Tags:** beginner
- **Summary:** Every way to move or set an object's origin independently of its geometry: the on-screen gizmo, Object Mode's "Affect Only → Origins" toggle, Edit Mode Select-All-then-move, a Maya-style D-key origin drag, and Object → Set Origin → Origin to Geometry / Origin to 3D Cursor.
- **File:** tutorials/blender-origin-pivot-point-tips---blender-secrets.md


### How do you model that? Kingdom Hearts Keyblade - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QV2Av9dSDbc
- **Author:** Blender Secrets
- **Blender Version:** Not specified
- **Tags:** procedural, organic, advanced
- **Summary:** Builds an ornate swirl-shaped weapon (for 3D printing, not subdivision topology) as dozens of individually hand-shaped bevel curves and box-modeled mesh pieces traced over a reference image, unified at the end via Convert-to-Mesh → Join → voxel Remesh → Sculpt-smooth → repeated 50% Decimate (30M → ~300-400k triangles). Covers curve bevel-objects for non-round ridges, Mirror modifier merge pitfalls, the Extra Objects add-on's Simple Star primitive with per-face inset/extrude, and Symmetrize as the reliable fix for messy merged regions.
- **File:** tutorials/how-do-you-model-that-kingdom-hearts-keyblade---blender-secrets.md


### How do you model that? Wrench - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=S9WVxHp1Sc0
- **Author:** Blender Secrets
- **Blender Version:** Not specified (On Cage editing, LoopTools, F2, Extra Objects; 3.x-5.x)
- **Tags:** modelling, procedural, intermediate, advanced
- **Summary:** Reference-to-model workflow (title says Wrench, content is actually pliers) covering box-modeling over a photo reference, graduated LoopTools Circle percentages for sharp-to-round transitions, a boolean jaw cut, freeform post-boolean topology cleanup, and Round Cube end-cap details.
- **File:** tutorials/how-do-you-model-that-wrench---blender-secrets.md


### Easy hole modeling for beginners - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=jrR1T-dIA8c
- **Author:** Blender Secrets
- **Blender Version:** Blender 5 (explicitly named)
- **Tags:** modelling, procedural, beginner, intermediate
- **Summary:** Two hole-modeling approaches: a fast vertex-bevel/LoopTools-Circle method that leaves n-gons, and an all-quad subdivision-ready method using three intersecting edge loops plus edge-creasing to keep corners sharp under a Subdivision modifier.
- **File:** tutorials/easy-hole-modeling-for-beginners---blender-secrets.md


### Grease Pencil in Blender 5 - New Pen tool and Sharp Corners (and some common Grease Pencil issues)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=tyPirJ_qWKs
- **Author:** Blender Secrets
- **Blender Version:** Blender 5 — Pen tool and Sharp corner point type are explicitly new features in this release
- **Tags:** grease-pencil, workflow, intermediate
- **Summary:** Full inking workflow using Blender 5's new Pen tool (click for straight points, click-drag for Bezier handles) and true Sharp corner points, plus common fixes: Dissolve to smooth strokes, Cyclic for closed loops, Fill Opacity=1, and Layers/Separate for stacking-order issues.
- **File:** tutorials/grease-pencil-in-blender-5---new-pen-tool-and-sharp-corners-and-some-common-grea.md


### For Beginners: Easiest Modeling Technique (long version)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=YCd_tS_3BTU
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Multires + On Cage editing + Gaffer add-on; 3.x-5.x)
- **Tags:** modelling, procedural, organic, beginner, intermediate
- **Summary:** Full 37-minute walkthrough of the "double-subdivision-modifier" (Simple + Catmull-Clark, edited On Cage) fast blockout technique, tools primer plus a complete sci-fi robot build through symmetry, panel cuts, hard-surface alpha-brush sculpting, and UV-less drag-and-drop materials.
- **File:** tutorials/for-beginners-easiest-modeling-technique-long-version.md


### Anime Girl character course overview - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=M-zUIL-DnRA
- **Author:** Blender Secrets
- **Blender Version:** 4.5 LTS (author notes no features newer than Blender 4.x are used)
- **Tags:** course-overview, not-a-tutorial, character, stylized
- **Summary:** **COURSE OVERVIEW — NOT A WALKTHROUGH (4m41s).** Promotional overview (not a step-by-step tutorial) of the author's paid stylized-anime-character course, naming its full pipeline: box-modeling shoes/socks/limbs/body over reference, joining and adding hands, clothing built on clean geometry with sculpted folds/pockets, head done last via 2D-topology-projected retopology (block-out then deformation topology) plus mouth geometry and Shape Keys for expressions, and hair via a hybrid mesh-clumps + thickened-curves + sculpting workflow. Useful as a reference checklist for a full stylized-character pipeline even without the paid lesson detail.
- **File:** tutorials/anime-girl-character-course-overview---blender-secrets.md


### Grid Fill update in Blender 4.5 LTS - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=gS8MHAXKFQE
- **Author:** Blender Secrets
- **Blender Version:** Blender 4.5 LTS (explicitly named)
- **Tags:** modelling, procedural, intermediate
- **Summary:** Grid Fill turns a boundary loop into a curvature-aware quad patch (with a "select two rails instead of the full boundary" trick); Blender 4.5 LTS adds running it on existing face selections to retopologize n-gons/triangles into quads.
- **File:** tutorials/grid-fill-update-in-blender-45-lts---blender-secrets.md


### Making a new Logo Animation - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7MIePxGcze0
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Cycles + GPU, Gaffer/Turbo Tools/Soundly add-ons; recent 4.x)
- **Tags:** rigid-body, animation, materials, lighting, rendering, compositing, brand-video, intermediate
- **Summary:** Production-diary walkthrough (not a step-by-step lesson) of a logo animation: weighted-bevel hard-surface modeling, Rigid Body physics for a "stunt cube" launched through animated hatch doors, Cycles rendering with volume-lit gradient backdrops, Sequencer sound design via Soundly, and DaVinci Resolve grading.
- **File:** tutorials/making-a-new-logo-animation---blender-secrets.md


### How to Texture Paint in Blender -- Using XPPen Artist Pro 22 (Gen 2) + Ucupaint, Auto Reload & Krita
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=96ppCrgb2JI
- **Author:** Blender Secrets
- **Blender Version:** 4.2+ (for Extensions-tab install of Ucupaint/Auto Reload)
- **Tags:** organic, materials, procedural, intermediate
- **Summary:** Dyntopo-sculpts a stump prop, retopologizes it, then paints layered textures via the free Ucupaint extension (Principled or flat-Emission mode) and round-trips painting through Krita via the free Auto Reload extension for near-live PSD updates. Contains a sponsored XP-Pen tablet segment, flagged in the notes.
- **File:** tutorials/how-to-texture-paint-in-blender----using-xppen-artist-pro-22-gen-2-ucupaint-auto.md


### Easy PBR Textures - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qxxoDYGrvtw
- **Author:** Blender Secrets
- **Blender Version:** Blender 4.2 (explicitly named for EEVEE displacement support)
- **Tags:** materials, shaders, displacement, cycles, eevee, intermediate
- **Summary:** Full PBR pipeline: sourcing free textures from Polyhaven, Node Wrangler's Principled Texture Setup, real geometric displacement with adaptive subdivision, baking displacement into real geometry, and triplanar/box mapping for objects without UVs — for both Cycles and EEVEE.
- **File:** tutorials/easy-pbr-textures---blender-secrets.md


### Interactive Cloth + new Cloth Brushes & more - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=bHmZfA07F0Y
- **Author:** Blender Secrets
- **Blender Version:** 4.3+ (Cloth sculpt brush split into several dedicated brushes)
- **Tags:** cloth, simulation, rigging, intermediate
- **Summary:** Poses cloth interactively via a Hook+Pin-Group rig (drag a pinned vertex in Object Mode while the sim plays), refines with Blender 4.3's split-out Cloth sculpt brushes, and bakes efficiently by rehearsing motion via Auto-Keying before a full-quality bake.
- **File:** tutorials/interactive-cloth-new-cloth-brushes-more---blender-secrets.md


### What if you Alpha Brush texture is square? Or the resolution is too low? Blender Sculpting tips
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rtnsLjP1ebo
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Area Plane/Stencil mapping, Multires; 3.x-5.x)
- **Tags:** displacement, procedural, organic, intermediate
- **Summary:** Fixes for two alpha-brush problems: square textures getting corner-clipped by the brush's circular sample radius (fix: Size X/Y ≈1.1, or use Stencil mapping), and blurry alphas (caused by inactive-object Multires resolution saving, insufficient geometry, or missing Shade Smooth).
- **File:** tutorials/what-if-you-alpha-brush-texture-is-square-or-the-resolution-is-too-low-blender-s.md


### Image to 3D model workflow in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=DBuKtyPaIbw
- **Author:** Blender Secrets
- **Blender Version:** Blender 4.3.2 (explicitly named, compared against 4.0.2)
- **Tags:** modelling, organic, procedural, displacement, intermediate, advanced
- **Summary:** Two paths from a B&W concept sketch to a mech blockout — Trace Image to Grease Pencil → Mesh with quad-topology cleanup and mirrored Solidify+double-Subdivision, or classic box-modeling from a cube — followed by a full hard-surface detailing pass (sculpting, multires, tiling displacement maps, greebles).
- **File:** tutorials/image-to-3d-model-workflow-in-blender.md


### Vertex Groups, Modifiers and Tissue Add-on - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=75inBBl39es
- **Author:** Blender Secrets
- **Blender Version:** Blender 4.3.2 (explicitly named)
- **Tags:** organic, procedural, abstract, intermediate
- **Summary:** A painted Vertex Group drives both a Decimate modifier's density and the free Tissue add-on's "Convert to Dual Mesh" honeycomb generation plus a Wireframe modifier's line thickness, on a free Blender Studio human base mesh — vertex groups as general-purpose modifier masks, not just deformation.
- **File:** tutorials/vertex-groups-modifiers-and-tissue-add-on---blender-secrets.md


### Offset Edge Slide - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=y7EuYx9CaTU
- **Author:** Blender Secrets
- **Blender Version:** Not specified (long-standing core shortcut)
- **Tags:** modelling, procedural, beginner
- **Summary:** Compares three ways to add symmetric loops around a middle edge loop — manual Ctrl+R (imprecise), Bevel + Profile correction, and the recommended Shift+Ctrl+R Offset Edge Slide shortcut, which adds both loops precisely with no shape distortion.
- **File:** tutorials/offset-edge-slide---blender-secrets.md


### How to make awesome Topology Animation | Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=m7dccc-J9aQ
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Camera Shakify add-on, Skinify extension; recent 4.x/5.x)
- **Tags:** animation, rigging, camera, procedural, intermediate
- **Summary:** A "topology reveal" animation made from a chain of objects (one Shape Key each) with synchronized visibility keyframes swapping between them to fake one continuously-evolving mesh, finished with a hand-animated camera and the Camera Shakify add-on.
- **File:** tutorials/how-to-make-awesome-topology-animation-blender-secrets.md


### In-depth look at my new Hard Surface course - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=K6IEt4T91Jw
- **Author:** Blender Secrets
- **Blender Version:** Blender 4.3 (explicitly named)
- **Tags:** course-overview, not-a-tutorial, hard-surface, modelling
- **Summary:** **COURSE OVERVIEW — NOT A WALKTHROUGH (4m27s).** Promotional overview (not a walkthrough) of the author's paid "Beginner Hard Surface Modeling" (Spiderbot) course — reference-image-faithful modeling in Chapter 1, retopology/animation/export prep in Chapter 2.
- **File:** tutorials/in-depth-look-at-my-new-hard-surface-course---blender-secrets.md


### Modeling a Devil Fruit from One Piece - Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=_-a8k2LaZbA
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Surface Deform + Shrinkwrap workflow; 3.x-5.x)
- **Tags:** organic, procedural, modelling, intermediate
- **Summary:** Builds swirl motifs via vertex-to-curve extrusion + mirroring, then uses a Surface Deform + Shrinkwrap combo (swirl bound to a wireframe plane, plane shrinkwrapped onto the base sphere) to conform each swirl to the sphere's curvature and tile a full "Devil Fruit."
- **File:** tutorials/modeling-a-devil-fruit-from-one-piece---blender-secrets.md


### First look at the new "Master Characters in Blender" course from CG Boost
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QNckGYykCNc
- **Author:** Blender Secrets
- **Blender Version:** Not specified (b-roll consistent with Blender 4.x/5.x)
- **Tags:** course-overview, not-a-tutorial, affiliate-review, character
- **Summary:** **AFFILIATE REVIEW OF A THIRD-PARTY COURSE — NOT A WALKTHROUGH (2m55s).** Affiliate review/first-look at Jim Moran's third-party "Master 3D Characters" course on CG Boost — not a walkthrough, but b-roll shows Geometry-Nodes-driven zippers and hardware-bolt scattering plus cloth-brush sculpting for clothing folds.
- **File:** tutorials/first-look-at-the-new-master-characters-in-blender-course-from-cg-boost.md


### 3D Sculpting on the go with XPPen Magic Drawing Tablet and visiting Ghibli museum (Nomad Sculpt)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=WKaQ_V-FHGA
- **Author:** Blender Secrets
- **Blender Version:** Not applicable (Nomad Sculpt app content, not Blender)
- **Tags:** organic, beginner
- **Summary:** Not a Blender tutorial — hardware review/vlog testing an XPPen Android tablet by sculpting a Totoro-like creature in Nomad Sculpt on a train to Tokyo's Ghibli Museum (Blender doesn't run on Android). Covers Nomad Sculpt's Blender-parallel workflow: base sphere, Symmetry/Mirror, Multires/VoxRemesh/Dyntopo-style modes, standard brush set (Drag, Move, Smooth, Flatten, Inflate, Mask), Add-primitive + Gizmo + Validate flow, and its Scene outliner. Exporting for use in Blender requires the paid version.
- **File:** tutorials/3d-sculpting-on-the-go-with-xppen-magic-drawing-tablet-and-visiting-ghibli-museu.md


### Creating a Japanse city from a photo using fSpy
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=GzHvD9RFrT8
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Cycles/AGX/fSpy/Gaffer workflow, likely 4.0+ given AGX)
- **Tags:** materials, shaders, volume, lighting, hdri, rendering, cycles, camera, animation, advanced
- **Summary:** Full photo-to-3D city pipeline from a real Tokyo/Shinjuku photograph: fSpy camera-matching (standalone app + Blender add-on, vanishing-point alignment, axis-matching), vertex-level building blockout matched to the photo, Boolean facade cuts, photo-projected texturing fixed for distortion via a dense Knife-Project reference grid, a Track-To background plane, volumetric haze (Volume Scatter cube), Gaffer HDRI lighting, a Linear-interpolated camera move sized to a target duration, low-res test renders before a full 4K EXR/AGX render, and a story-detail emissive window (Blackbody-driven color temperature) for a moody post-apocalyptic look — finished with external color grading in DaVinci Resolve.
- **File:** tutorials/creating-a-japanse-city-from-a-photo-using-fspy.md


### Remeshing Tips for Beginners | Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=3VNiWcO1QN8
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Voxel/Quadriflow/Remesh modifier; 3.x-5.x)
- **Tags:** organic, procedural, modelling, beginner, intermediate
- **Summary:** Three escalating remesh methods (plain Voxel, Voxel+Fix-Poles+Preserve-Volume, Quadriflow) with cleanup via Mirror+Shrinkwrap, troubleshooting Voxel-Remesh holes via a Remesh modifier fallback, avoiding finger-spiral topology with the paid Quad Remesher add-on, and the conceptual distinction between remeshing and retopology.
- **File:** tutorials/remeshing-tips-for-beginners-blender-secrets.md


### Perfect Holes with Quad Topology in Curved Surfaces - Step by step Blender beginner version
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=bfdI_-ymkas
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Shrinkwrap + vertex-group workflow; 2.8+)
- **Tags:** modelling, procedural, beginner, intermediate
- **Summary:** Cuts a circular hole into a curved surface with boundary-protection inset/extrude loops, then fixes the "lumpy" Subdivision distortion around the hole via a Shrinkwrap modifier (targeting an undisplaced duplicate) restricted by a vertex group, baked via Visual Geometry to Mesh, and optionally Decimated back down.
- **File:** tutorials/perfect-holes-with-quad-topology-in-curved-surfaces---step-by-step-blender-begin.md


### Step by Step: Boolean Holes to Quad Topology | Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=pe-8GiRCLmM
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Weld/Shrinkwrap/Decimate workflow; 2.8+)
- **Tags:** modelling, procedural, intermediate, advanced
- **Summary:** Cuts a complex (heart-shaped) boolean hole then retopologizes it into clean quads: Weld modifier cleanup, Bridge Edge Loops + Bevel (2 segments, Profile 1) for proper boundary loops, Grid Fill caps, and a Shrinkwrap modifier (vertex-group-limited, targeting a smooth duplicate) to restore true surface curvature.
- **File:** tutorials/step-by-step-boolean-holes-to-quad-topology-blender-secrets.md


### Step by Step: Image File to 3D Geometry | Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=HUL9o27m11M
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Grease Pencil trace + Knife Project; 3.x-4.x)
- **Tags:** modelling, procedural, intermediate
- **Summary:** Engraves a 2D logo image onto a curved surface via Knife Project: image traced to Grease Pencil then mesh, cleaned up with Merge by Distance/Checker Deselect/LoopTools Space, projected into a sphere from the current view, cleaned up via non-manifold Merge by Distance, and given depth with Extrude+Alt+S.
- **File:** tutorials/step-by-step-image-file-to-3d-geometry-blender-secrets.md


### Review and Tips for using the XPPen Artist Pro 16 Gen 2 in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=HV4pRb6XKAI
- **Author:** Blender Secrets
- **Blender Version:** Not specified (OS/driver-level configuration, version-agnostic)
- **Tags:** organic, beginner
- **Summary:** Hardware review (not a modeling tutorial) of the XP-Pen Artist Pro 16 Gen 2 drawing display, with actionable Blender-specific tips: mapping pen buttons to left/middle/right-click for viewport navigation, and using Windows' "Extend" display mode for a tablet-as-second-monitor setup.
- **File:** tutorials/review-and-tips-for-using-the-xppen-artist-pro-16-gen-2-in-blender.md


### Making an Ocean with Foam and a Boat | Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qjJ3kSCis4k
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Ocean modifier, EEVEE/Cycles compatible; 3.x-5.x)
- **Tags:** displacement, shaders, materials, rigging, procedural, intermediate
- **Summary:** Modifier-only ocean (no fluid sim): the Ocean modifier drives wave displacement, a height-based ColorRamp fakes peak/valley coloring, Generate Foam + an Attribute/Power node mixes in white foam, and a Shrinkwrap-plane + Copy Transforms rig floats a boat naturally on the waves.
- **File:** tutorials/making-an-ocean-with-foam-and-a-boat-blender-secrets.md


### Combining Ragdoll physics with Motion Capture animation | Rokoko Smartsuit 2 | Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=d16IOajUwIc
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Rigidbody/NLA/Rokoko/Mixamo workflow, 2.9x-4.x)
- **Tags:** rigid-body, simulation, animation, rigging, expert
- **Summary:** Blends Rigidbody ragdoll physics (constrained-joint ragdoll, deactivated-until-hit hitboxes, bone-parented trigger cube, baked to keyframes) with Rokoko-retargeted motion capture (Mixamo T-pose auto-rig, Rokoko Retargeting add-on) across three separate animation-layer/NLA-blended phases: mocap walk-in → hand-posed "Stunt" layer bridging to the physics sim → baked ragdoll impact → NLA-blended "Getting Up" mocap. Includes an improvised root-bone fix for root-less Mixamo rigs (extrude from hips) to reconcile the ragdoll's end position with the mocap clip's own starting location.
- **File:** tutorials/combining-ragdoll-physics-with-motion-capture-animation-rokoko-smartsuit-2-blend.md


### Blender Secrets - In Depth Cloth Sculpting tricks with Pose Brush
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=dtFFc6f2rK8
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Pose brush Cloth Simulation target, 3.x-5.x)
- **Tags:** cloth, simulation, organic, rigging, advanced
- **Summary:** Poses a clothed character's limb with the Sculpt Mode Pose brush using two Face Sets (built via X-Ray+Lasso Select → Face Set from Edit Mode Selection) and Deformation Target = Cloth Simulation instead of Geometry — producing real, physically-simulated fabric folds while bending, especially strong with the Squash & Stretch deformation type. Recommends pre-stretching with Geometry mode first to offset the length-shortening from squashing. Cleanup via Smooth brush for minor intersections, Alt+Q + Grab brush for larger ones.
- **File:** tutorials/blender-secrets---in-depth-cloth-sculpting-tricks-with-pose-brush.md


### Monster Sculpting | Full Process | Blender Secrets | Stranger Things Vecna
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=s6GQv6eZVms
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Human Base Meshes add-on, Voxel/Multires workflow; 3.x-5.x)
- **Tags:** organic, procedural, materials, advanced
- **Summary:** Full Vecna-inspired monster bust process: Boolean+Voxel-Remesh blockout from a base mesh, Clay Strips sculpting, a curve-based (non-sculpting) technique for tapered tendrils/veins, and purchased ArtStation alpha-texture stamping for skin detail.
- **File:** tutorials/monster-sculpting-full-process-blender-secrets-stranger-things-vecna.md


### Create a Photoreal Moon in minutes | 3D Tutorial | #blender secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=iNL98QwGEmQ
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Cycles displacement workflow, 2.9x-5.x)
- **Tags:** materials, shaders, displacement, rendering, cycles, intermediate
- **Summary:** Builds a photoreal Moon from free NASA color/height textures on a UV Sphere (Subdivision+Displace modifier, UV coordinates, Non-Color height map), then fixes the classic equirectangular-on-UV-sphere pole-pinching artifact by switching to Generated+Sphere-projected texture coordinates (Smart Interpolation) and moving displacement from the mesh modifier into a shader-graph Displacement node (Material Settings = Displacement Only/Displacement and Bump) so color and height stay aligned under the new projection.
- **File:** tutorials/create-a-photoreal-moon-in-minutes-3d-tutorial-blender-secrets.md


### Export VDM maps from Zbrush to Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=KACmuXsoc30
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Vector Displacement brush, standard since 2.8+)
- **Tags:** displacement, organic, advanced
- **Summary:** Converts a ZBrush Vector Displacement Map (VDM) brush into a Blender-compatible sculpt stamp — export as OpenEXR, mirror the axis to fix the background color, swap/boost the Green and Blue channels in Photoshop, then load it as a Draw brush with Vector Displacement enabled.
- **File:** tutorials/export-vdm-maps-from-zbrush-to-blender.md


### Ruffled Skirts | Virtual Fashion | Blender Tutorial | Blender Secrets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=hJ5zUTp9zCc
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Cloth Sewing Springs + Presets; 2.8+)
- **Tags:** cloth, simulation, materials, organic, intermediate
- **Summary:** Ruffled fabric via Cloth Sewing Springs: an oversized flat extension is deleted down to just boundary edges, pinned/sewn to a smaller opening so it puckers into ruffles, tuned with material Presets (Denim/Rubber/Silk) and repeated in layers via Pin/Effects vertex groups for a multi-tier skirt.
- **File:** tutorials/ruffled-skirts-virtual-fashion-blender-tutorial-blender-secrets.md


### Blender Secrets - (Long Version) Marvelous Designer-like Cloth Grabbing
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=1YqtY02n8iU
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Cloth/Hook/Multires workflow, 2.9x-5.x)
- **Tags:** cloth, simulation, rigging, organic, advanced
- **Summary:** Makes a garment interactively grabbable like Marvelous Designer: model a simple shirt from a base mesh (Circle Select, mirror, duplicate+offset, Separate), scale the whole rig 10x for cloth-solver stability, rig Hook modifiers to individual vertices with a Pin Group excluding them from the sim, then grab hooks in Object Mode to pose realistic folds live. Bakes via Ctrl+A Visual Geometry to Mesh, then refines with Multires + Draw brush hand-sculpting. Includes a downloadable GitHub Python script that automates the repetitive hook rigging/teardown into "Add Hooks"/"Remove Hooks" N-panel buttons.
- **File:** tutorials/blender-secrets---long-version-marvelous-designer-like-cloth-grabbing.md


### Blender Secrets - Auto Masking Cavities in Sculpt Mode
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RbqpANWvTWY
- **Author:** Blender Secrets
- **Blender Version:** 3.4+ (Auto Masking Cavity feature is explicitly new in 3.4)
- **Tags:** organic, procedural, beginner, intermediate
- **Summary:** Blender 3.4+'s Sculpt Mode Cavity Auto Masking (dropdown or Alt+A pie menu, plus per-brush Advanced overrides): constrains brush strokes to surface recesses (or raised areas via Cavity Inverted), tuned with Factor/Blur; "Create Mask" bakes a standalone Mask From Cavity that can be refined further with Smooth/Sharpen Mask filters. Demoed on a detailed T-Rex sculpt; noted use case is bringing out extra detail on 3D scans.
- **File:** tutorials/blender-secrets---auto-masking-cavities-in-sculpt-mode.md


### Better Billboards using Normal Maps (Low Poly Trees)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Ix-KT9a4PSo
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Cycles + modern Color Management, Blender 3.x-5.x compatible)
- **Tags:** materials, shaders, procedural, rendering, cycles, lighting, organic, intermediate
- **Summary:** Bakes a 2D billboard tree impostor with dynamic lighting response: light a real 3D tree with a scaled-up Area Light, render a transparent-background PNG (F12) for the color/alpha texture, then switch to Matcap shading (Color=Object, "normal" matcap, Color Management View Transform=Standard) and use View→Viewport Render Image to capture a second bake as the normal map. Loading both textures on a flat billboard plane makes it shade and cast shadows correctly as scene/HDRI lighting rotates, instead of looking flat.
- **File:** tutorials/better-billboards-using-normal-maps-low-poly-trees.md


### Creating a Realistic Forest in Blender using Billboards (low poly Planes with tree images)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mSdzwRcFJM0
- **Author:** Blender Secrets
- **Blender Version:** Not specified (EEVEE referenced generically; UI matches Blender 3.x/4.x)
- **Tags:** particles, camera, organic, beginner
- **Summary:** Uses camera-facing billboard planes (Images as Planes + Track To constraint targeting the camera) instanced across a terrain via a Hair particle system to fake a dense background forest cheaply.
- **File:** tutorials/creating-a-realistic-forest-in-blender-using-billboards-low-poly-planes-with-tre.md


### Blender Secrets - Create Towers with Ivy
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=3cllYcT-MRg
- **Author:** Blender Secrets
- **Blender Version:** Not specified (built-in add-ons/modifiers, 2.8x-5.x)
- **Tags:** procedural, organic, modelling, intermediate
- **Summary:** Builds a stone tower entirely from built-in Blender add-ons: Extra Objects' Wall Factory generator (stones scaled to overlap via Alt+S) bent into a cylinder with Simple Deform (Bend 360°, Z-axis), heightened via an Array modifier, varied with a second hidden top section, softened with a Voxel-mode Remesh (transcript mis-heard as "Foxhole"), and finally covered in procedurally-grown ivy via the built-in Add Curve: IvyGen add-on (Max Ivy Length, Gravity, Randomness, separate Leaves/Stem materials).
- **File:** tutorials/blender-secrets---create-towers-with-ivy.md


### Blender Secrets - 4 tips for Cinematic Lighting
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=lXvmt0QxAFY
- **Author:** Blender Secrets
- **Blender Version:** Not specified (EEVEE + Cycles compatible, modern 3.x-4.x UI)
- **Tags:** lighting, hdri, materials, shaders, volume, cycles, eevee, intermediate
- **Summary:** Four cinematic lighting tips: aim a Spot light precisely by making it the Local Camera (N-panel View tab, Lock Camera to View, Numpad0); build a leaf/gobo light-shaper from an Images-as-Planes video texture (Color→Alpha, MapRange) in front of a spot, extended with a Volume Scatter-filled cube for visible light shafts; browse/swap HDRIs live via the Gaffer add-on (auto-transcribed as "Kevver"/"Gether," confirmed from on-screen UI); and drive an Emission shader's Strength with an expression/driver for a pulsating light (exact expression syntax not verifiable from the source video).
- **File:** tutorials/blender-secrets---4-tips-for-cinematic-lighting.md


### Blender Secrets - How to merge 3D Scans and bake the Texture as Color Attributes
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=AxDXWgFDwLA
- **Author:** Blender Secrets
- **Blender Version:** 3.2+ (Color Attributes bake workflow)
- **Tags:** materials, procedural, organic, cycles, advanced
- **Summary:** Merges two textured 3D scans (deer head + cow body example) without losing either texture: boolean-trim + Proportional-Editing overlap blend + matched UV map names + BoolTool join, then Dyntopo-sculpt the seam on a texture-free duplicate (Dyntopo strips texture, hence the duplicate), and finally Cycles-bake the original's texture (Emit or Diffuse channel, Selected to Active, Extrusion ~0.2) onto the sculpted duplicate as a Color Attribute (vertex colors) — viewable via Color Attribute viewport shading and touch-up-paintable with the Sculpt Paint tool.
- **File:** tutorials/blender-secrets---how-to-merge-3d-scans-and-bake-the-texture-as-color-attributes.md


### Blender Secrets - 4 tips for Photoreal Lighting
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=do_S94ZXLSc
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Cycles required, modern 3.x-4.x UI)
- **Tags:** lighting, hdri, cycles, materials, shaders, rendering, intermediate
- **Summary:** Four photoreal lighting techniques: real-world IES light profiles (Cycles-only) driving a Point light's Emission Strength via an IES Texture node (Radius 0.02-0.03 for a sharp, artifact-free distribution pattern); a textured/video Spot light built with Ctrl+T auto-texture-node-wiring (Match Movie Length + Auto Refresh for video); the procedural Nishita Sky Texture with Sun Disc as a physically-based sun (Elevation/Rotation/Size/Air-Dust-Ozone controls, Solidify modifier to stop light leaks, Linear-keyframed Elevation for sunset timelapses); and manual HDRI world lighting via Poly Haven with a Transparent-Film + PNG/EXR RGBA trick to keep the lighting but hide the HDRI background.
- **File:** tutorials/blender-secrets---4-tips-for-photoreal-lighting.md


### 12 Tips for Creating Epic Trees in Blender Without Paid Add-Ons
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=6wHgqPPQ3WI
- **Author:** Blender Secrets
- **Blender Version:** 2.8x-2.9x (M3 add-on step specifically: 2.83.2)
- **Tags:** procedural, organic, particles, animation, rigging, materials, intermediate
- **Summary:** Twelve free tree-building techniques: the M3 node-based tree generator (Trunk/Branch/Tree Parameters nodes) with armature-rig "Fast Wind" animation, the built-in Sapling add-on, fully hand-modeled Skin-modifier trunks with weight-painted twig/leaf Hair particle systems, photogrammetry-scanned bark texture baked and blended onto a procedural trunk (Mix Shader + Gradient), Grease Pencil-sculpted stylized branches, and Hair-particle forest scattering across an A.N.T. Landscape terrain.
- **File:** tutorials/12-tips-for-creating-epic-trees-in-blender-without-paid-add-ons.md


### Blender Secrets - Draw Grease Pencil On Surfaces (without offset distance issue)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=xLAlFoRPTPM
- **Author:** Blender Secrets
- **Blender Version:** Not specified (core Grease Pencil/Curve workflow, 2.9x-5.x)
- **Tags:** modelling, procedural, materials, beginner, intermediate
- **Summary:** Draws ornamental surface patterns directly on a 3D object via Grease Pencil's Stroke Placement = Surface, avoiding zoom-dependent offset drift by working in Orthographic view (Numpad5). Strokes are smoothed (right-click Smooth, Shift+R), converted to a Bezier curve ("GP_Layer"), Decimate-Curve-simplified (~10%), and given physical thickness via Bevel Depth/Resolution — turning a hand-drawn pattern into a raised-relief engraved curve mesh (demoed as goblet filigree).
- **File:** tutorials/blender-secrets---draw-grease-pencil-on-surfaces-without-offset-distance-issue.md


### Blender Secrets - Car Modeling Tips
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=jcSDF917dBo
- **Author:** Blender Secrets
- **Blender Version:** Not specified (core modifier/Quad-View workflow, 2.8x-5.x)
- **Tags:** modelling, procedural, intermediate, advanced
- **Summary:** Full hard-surface car-body pipeline: aligned multi-view blueprint reference setup (Collections for selectability toggling, opacity/perspective-display tuning); box-modeling from a single vertex under a Mirror(Bisect,On Cage)+Subdivision modifier stack in 4-way Quad View (Alt+Ctrl+Q); black-and-white matcap smoothness checking; and a Shrink Wrap technique (holed duplicate conforming to a hidden, extra-smooth original) for cutting clean windows/grilles without pinching geometry.
- **File:** tutorials/blender-secrets---car-modeling-tips.md


### Blender Secrets -  How to make a Base Mesh for Sculpting (three methods)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=UojINqTfZsM
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Skinify Rig/Rigify/Metaball/GP-trace workflow, 3.x-5.x)
- **Tags:** organic, procedural, rigging, modelling, intermediate, advanced
- **Summary:** Three base-mesh workflows: (1) Skinify Rig + Rigify — pose a rig, Add Shape to generate skin/subdivision geometry from bones, Visual Geometry to Mesh, Inflate-brush + Separate/Join cleanup (dragon/wyvern example); (2) Metaball blockout over a photo reference, Convert to Mesh, Symmetrize + Merge by Distance (horse example); (3) Grease Pencil trace of a 2D silhouette → Path → Mesh, fill+cleanup, Mirror+Solidify+Voxel-Remesh, with primitive meshes addable in Edit Mode for the remesh to auto-merge (mech/robot example).
- **File:** tutorials/blender-secrets---how-to-make-a-base-mesh-for-sculpting-three-methods.md


### Blender Secrets -  Scaling Tips for Better 3D Modeling
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=jlh275ZKsLw
- **Author:** Blender Secrets
- **Blender Version:** Not specified (core transform-tool workflow, 2.9x-5.x)
- **Tags:** modelling, procedural, beginner, intermediate
- **Summary:** Three scaling techniques: G,G shape-conforming scale for insets that should follow non-uniform surrounding edges; S+Shift+[axis] to exclude one axis when scaling an Alt+E-extruded face; the Scale Cage tool (Toolbar) for interactive multi-object/edit-mode scaling with opposite-handle pivot and numeric input; and Shrink/Fatten (Alt+S) with Proportional Editing's "Connected" option for thickness-only adjustments (e.g. fattening a cylinder without lengthening it) that don't drag along nearby-but-disconnected geometry.
- **File:** tutorials/blender-secrets---scaling-tips-for-better-3d-modeling.md


### Blender Secrets - Every Circular Array or Radial Array method
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Q6nq1HEA5Y8
- **Author:** Blender Secrets
- **Blender Version:** Not specified (core operators/modifiers, 2.8x-5.x)
- **Tags:** procedural, modelling, animation, intermediate, advanced
- **Summary:** Six circular/radial array methods with different tradeoffs: Spin operator (Alt+E, edit-mode, fast); manual Duplicate+Rotate+Shift-R-repeat (precise angle=360/count control); Vertex-Parented Instancing on a Mesh Circle (non-destructive, animatable, Align to Vertex Normal); Screw modifier driven by a single displaced vertex (fully procedural); Curve modifier + stacked Array modifiers around a Bezier Circle (best for tapering/twisting tower-like structures, Ctrl+T twist, Constant Offset brick-coursing); and Array modifier with Object Offset driven by an interactively-rotated Empty (fully non-destructive).
- **File:** tutorials/blender-secrets---every-circular-array-or-radial-array-method.md


### Blender Secrets - Making Holes in Cylinders with decent Quad Topology
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=JvJ_Hoj82us
- **Author:** Blender Secrets
- **Blender Version:** Not specified (core mesh/modifier + Loop Tools workflow, 2.9x-5.x)
- **Tags:** modelling, procedural, intermediate, advanced
- **Summary:** Four all-quad hole-cutting methods for cylinders: (1) snap a separate low-poly Circle onto the surface (Face snap + Project Individual Elements), join, remove+Grid-Fill, Inset+Extrude; (2) circularize duplicated cylinder faces via Loop Tools Circle, snap, Bridge Edge Loops; (3) snap in reusable Asset-Browser detail geometry, Merge by Distance + recalc normals; (4) build the hole pattern flat on a Plane with a 2D Array grid of circular cutouts, then wrap it into a cylinder via a Simple Deform Bend 360° modifier (+Weld/Solidify/Subdivision).
- **File:** tutorials/blender-secrets---making-holes-in-cylinders-with-decent-quad-topology.md


### Blender Secrets - 5 mins of ArchViz Tips (Diamond Tufting, Pillow Edges, Pillows, Interactive Cloth)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=hpFaDiTDZgc
- **Author:** Blender Secrets
- **Blender Version:** Not specified (version-agnostic core workflow, 3.x-5.x)
- **Tags:** cloth, simulation, materials, procedural, intermediate
- **Summary:** Four ArchViz soft-furnishing techniques: a gravity-free, pressure-inflated Cloth-sim pillow finished with Cloth Brush sculpt wrinkles; curve-based decorative piping/edges built from a duplicated edge selection (or, for scanned geometry, vertex-by-vertex with face snapping) converted to a beveled Curve; diamond-tufted button upholstery via Poke Faces → Tris to Quads → Select Similar (connecting edges) → Bevel Vertices → dual Extrude Along Face Normals with Individual-Origins scaling; and a draped Cloth sim pinned to a Vertex Group and reshaped live via a Hook modifier.
- **File:** tutorials/blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in.md


### Blender Secrets - 5 minutes of Topology Tips
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=V7Y-Il-7JFE
- **Author:** Blender Secrets
- **Blender Version:** Not specified (core mesh-editing workflow, 3.x-5.x)
- **Tags:** modelling, procedural, intermediate
- **Summary:** Five manual topology-cleanup techniques: Rotate Edge (Ctrl+E) to fix bad triangle shading; systematic extrude/merge/fill patterns to reduce N quads down to fewer quads (4→2, 5→3, 3→1); adding an edge loop across triangulated geometry where Ctrl+R fails (Alt-select loop → Ctrl+I invert → Subdivide → slide new loop); conforming/straightening a wavy edge loop (G,G,E or LoopTools Flatten); and three ways to flatten (Select Similar Coplanar+Flatten, scale-to-zero, delete+Grid Fill) or smooth (Smooth Vertices, Sculpt Mode, Vertex-Group-masked Smooth modifier) a patch of geometry.
- **File:** tutorials/blender-secrets---5-minutes-of-topology-tips.md


### Blender Secrets - 5 minutes of Beveling knowledge (17 tips!)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rzZFIpqc98M
- **Author:** Blender Secrets
- **Blender Version:** Not specified (modern 3.x-5.x Bevel modifier/shader Bevel node)
- **Tags:** procedural, materials, shaders, cycles, intermediate, advanced
- **Summary:** Dense bevel-technique reel: Ctrl+B vs. Bevel modifier vs. per-edge Bevel Weight (Limit Method=Weight) for varying bevels from one modifier, Data Transfer/Weighted Normal for smoothing simple 2-edge bevels, the Cycles-only shader Bevel node for fake render-time rounding, Inner/Outer Miter (Sharp/Patch/Arc) for meeting-corner resolution, Custom Bevel Profiles for stairs/hard-surface detail, and fixes for common bevel failures (N-gons via J, double geometry via Merge By Distance, tight geometry via Edge Slide, unapplied Scale).
- **File:** tutorials/blender-secrets---5-minutes-of-beveling-knowledge-17-tips.md


### Blender Secrets - 5 minutes of N-Gons to Quads tips
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=DwpajQ0oQPI
- **Author:** Blender Secrets
- **Blender Version:** Not specified (core mesh-editing/modifier workflow, 3.x-5.x)
- **Tags:** modelling, procedural, intermediate
- **Summary:** Five n-gon/triangle-to-quad cleanup techniques: Knife Project a subdivided helper plane onto a traced organic outline for a clean bendable quad grid; Solidify (thin) + Remesh (Smooth, Octree Depth) + Convert to Mesh + Merge by Distance for flat n-gon shapes; Triangulate (Ctrl+T) then Tris to Quads (Alt+J) for boolean-created n-gon patches; Crease (Shift+E, 1) + apply Subdivision Surface to protect and quad-ify Knife-tool cuts; and a plain Alt+J pass for models that were originally quad-based before being triangulated (e.g. internet downloads).
- **File:** tutorials/blender-secrets---5-minutes-of-n-gons-to-quads-tips.md


### Blender Secrets - 6 Minutes of Boolean Basics
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=_S3D8djM5bE
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Boolean Fast/Exact solver + BoolTool add-on, 2.9x-5.x)
- **Tags:** procedural, modelling, materials, intermediate
- **Summary:** Full non-destructive Boolean hard-surface workflow: modifier-based Boolean Difference with cutter objects hidden via Wire display or render-visibility toggle; the BoolTool add-on's Ctrl+Numpad− fast live/destructive cutting (cutter stays editable as a bounding box); layered Solidify+Bevel cutter objects for rounded slice cuts (stack multiple Solidify modifiers above the Bevel for multi-slice variation); Quick-Favorites/Modifier-Tools workflow speedups (Apply All); and cleanup for boolean-leftover geometry via manual merge, Auto-Merge+Edge-Slide, inset support loops, or the Weld modifier (On Cage, Vertex-Group-limited).
- **File:** tutorials/blender-secrets---6-minutes-of-boolean-basics.md


### Blender Secrets - Hard Surface Sculpting Tips Part 2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=f8xoUkPY4e8
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Dyntopo/Multires/Mask Extract workflow, 3.x-5.x)
- **Tags:** organic, procedural, materials, advanced
- **Summary:** Part 2 of a hard-surface sculpting series (helmet/creature-head example): Dyntopo base-mesh blocking (Grab/Snake Hook/Clay Strip/Crease/Scrape/Smooth); panel cuts via Mask+Mesh-Filter-Inflate+Remesh; Mask Extract to split a design into separately-sculptable sub-objects (auto Solidify thickness, Paint-Mask-preserving Remesh beforehand, Separate by Loose Parts, Alt+Q to pick the active sculpt target); Multires+alpha detailing; and the Line Project tool for fast flat faceting on a Round-Cube Quadsphere (Ctrl-constrain angle, Limit to Segment, remesh afterward since it doesn't boolean-cut).
- **File:** tutorials/blender-secrets---hard-surface-sculpting-tips-part-2.md


### Blender Secrets - Hard Surface Sculpting Tips
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=3Ty0dNNO4bE
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Multires/Dyntopo sculpt workflow, 3.x-5.x)
- **Tags:** organic, procedural, materials, advanced
- **Summary:** Part 1 of a hard-surface sculpting series (Part 2 continues it): panel cuts via Crease brush (accumulates depth at overlaps — a problem) vs. the Layer brush with Persistent+Set Persistent Base (the fix, clean non-accumulating cuts); geometric Mask workflow (Curve/Line/Lasso stroke, Strength>1 for crisp edges, Shrink Mask+Paint-Mask-preserving Remesh+Smooth-filter for clean inflated-panel sides); and alpha-texture stamping (free JRO Tools/Bergman 3D packs, Area Plane mapping, Ctrl+F to rotate) including a Radial-value Drag-Dot mode for perfect circular bolt/rivet arrays.
- **File:** tutorials/blender-secrets---hard-surface-sculpting-tips.md


### Blender Secrets - Modeling Circular Hard Surface Details
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=tHnKR8DB1gg
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Curve modifier + Knife Project, version-agnostic)
- **Tags:** modelling, procedural, intermediate
- **Summary:** Bends a flat sci-fi panel (Boolean slice-cuts + Solidify, hand-detailed) into a circular band via a Curve modifier — fixing the initial faceted bend by transferring the pattern onto a denser plane first with Knife Project.
- **File:** tutorials/blender-secrets---modeling-circular-hard-surface-details.md


### Blender Secrets - Modeling Sci-Fi Greebles on a Sphere (using Annotate Tool)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=IeLNfxeEqz0
- **Author:** Blender Secrets
- **Blender Version:** Not specified (core Annotate/Snapping/Shrinkwrap/Solidify workflow, 2.9x-5.x)
- **Tags:** modelling, procedural, sci-fi, intermediate
- **Summary:** Sketches a sci-fi panel-line/greeble design directly onto a curved surface (dome/sphere) using the Annotate tool (Placement=Surface), then manually traces real edge geometry over the sketch (single-vertex merge + extrude, Face-snap + Project Individual Elements, "In Front" viewport display to see through the sphere), and finally conforms + thickens it with a Shrinkwrap modifier (target=sphere) followed by a Solidify modifier.
- **File:** tutorials/blender-secrets---modeling-sci-fi-greebles-on-a-sphere-using-annotate-tool.md


### Blender Secrets - Decorative Edges for Sofas and Cushions
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8D8F0BpeZvQ
- **Author:** Blender Secrets
- **Blender Version:** Not specified (core mesh/curve workflow, 3.x-5.x)
- **Tags:** modelling, materials, procedural, intermediate
- **Summary:** Short standalone tip (same technique as this channel's fuller "5 mins of ArchViz Tips" video): curve-based decorative piping for upholstery — duplicate+separate an edge selection, Convert to Curve, add Bevel Depth + Shade Smooth; for complex/scanned geometry without a clean edge loop, use Snap-to-Face + Project Individual Elements to build the seam path vertex by vertex instead, then convert/bevel the same way. Subdivide+smooth extra vertices at corners for rounder turns.
- **File:** tutorials/blender-secrets---decorative-edges-for-sofas-and-cushions.md


### Blender Secrets - Modeling from Photos with the Knife Tool (part 1: basics)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VzsxFT3-Kmk
- **Author:** Blender Secrets
- **Blender Version:** Not specified (core Knife tool/Images-as-Planes/UV workflow, 2.9x-5.x)
- **Tags:** modelling, materials, procedural, beginner, intermediate
- **Summary:** Uses the Knife tool (K) directly on an Images-as-Planes photo (Material Preview, Front Orthographic) to trace and cut a textured 3D shape from a building facade photo, deleting unneeded faces, extruding sub-selections for real depth, and fixing UV stretching on extruded faces via U → Project From View.
- **File:** tutorials/blender-secrets---modeling-from-photos-with-the-knife-tool-part-1-basics.md


### Blender Secrets - Reconstruct a Face / Head from just a few photos with Keen Tools Face Builder
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rUh2cEWAIgk
- **Author:** Blender Secrets
- **Blender Version:** Not specified (KeenTools FaceBuilder 2021.2.0; 2.9x-3.x era)
- **Tags:** organic, modelling, materials, intermediate
- **Summary:** Reconstructs a photorealistic 3D head from a handful of photos using the paid KeenTools FaceBuilder add-on: auto-align a generic head mesh per photo, refine with manually-dragged Pins on facial landmarks, then bake a texture from the aligned photo set.
- **File:** tutorials/blender-secrets---reconstruct-a-face-head-from-just-a-few-photos-with-keen-tools.md


### Blender Secrets - Blender GIS (Extra Bonus Tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=IcL7N335oCk
- **Author:** Blender Secrets
- **Blender Version:** Not specified (BlenderGIS + Gaffer add-on workflow, 2.8x-4.x)
- **Tags:** procedural, materials, lighting, hdri, rendering, cycles, advanced
- **Summary:** Real-world terrain render using the BlenderGIS add-on: load/lock/zoom a real satellite basemap (e.g. the Matterhorn) and download its height map for accurate displaced terrain, subdivide for detail, fix the shiny default material (lower Specular, raise Roughness), light with Gaffer HDRIs, and handle the resulting massive real-world-scale mesh (increased Camera Clip End, Simple viewport display, DOF Empty target, 30mm lens). Includes a render-crash fix: scale up the camera, delete everything outside its frustum to cut memory usage before rendering.
- **File:** tutorials/blender-secrets---blender-gis-extra-bonus-tutorial.md


### Daily Blender Secrets - 10 ways to make Holes in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=oFg367w5Cpo
- **Author:** Blender Secrets
- **Blender Version:** Not specified (BoolTool + Carver + Box Cutter add-ons, native LoopTools; 2.9x-5.x)
- **Tags:** modelling, procedural, intermediate
- **Summary:** Rapid-fire survey of 10 distinct ways to cut a hole into a mesh — Knife Project, BoolTool boolean, beveled vertex, LoopTools Circle/Bridge, curve-to-mesh, snap-and-project, Face-menu Intersect, Carver, and Box Cutter — each labeled on-screen as it's demonstrated.
- **File:** tutorials/daily-blender-secrets---10-ways-to-make-holes-in-blender.md


### Daily Blender Secrets - 15 Tips Compilation (part 3)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=xLAakVcA1hc
- **Author:** Blender Secrets
- **Blender Version:** 2.8+ (Scatter Objects described as a new default 2.8 add-on)
- **Tags:** rigging, animation, cloth, simulation, rendering, particles
- **Summary:** Continues Part 2's ragdoll build (Rigid Body Constraint limits, then Armature parented to the ragdoll via Child Of bone constraints), then covers 13 more tips: slow-motion cloth, inverted-hull outlines, baked normal maps, vacuum-pack cloth pressure, Scatter Objects, 3D-Print-Toolbox particle cleanup, Blue Noise Particles, OpenVDB volumetrics, self-repulsing particles, wireframe thickness, inset/outset, and view-isolation shortcuts.
- **File:** tutorials/daily-blender-secrets---15-tips-compilation-part-3.md


### Daily Blender Secrets - 15 Tips Compilation (Part 2)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=4AttSorvirM
- **Author:** Blender Secrets
- **Blender Version:** 2.82+ (Custom Bevel Profile stairs preset explicitly requires 2.82 or later)
- **Tags:** materials, modelling, procedural, simulation, cloth, rigid-body
- **Summary:** 13-tip grab-bag: box/triplanar texture mapping, Auto Smooth, BoolTool cutting, LoopTools bridging/twisting and circular holes, bevel-profile stairs, vertex sliding, Cloth Pressure inflation, Subdivision shortcuts, PolyBuild retopology, and three bouncy-ball/ragdoll physics methods (keyframes, Rigid Body, Soft Body).
- **File:** tutorials/daily-blender-secrets---15-tips-compilation-part-2.md


### 15 Blender Secrets (Compilation of 15 Blender Tutorials in 11 minutes)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=hZ2iWrbRNd0
- **Author:** Blender Secrets
- **Blender Version:** 2.8x (references Blender 2.8 + a Blender 2.83 alpha experimental build)
- **Tags:** materials, shaders, procedural, animation, rigging, cloth, simulation, beginner, intermediate
- **Summary:** Grab-bag of 13 unrelated quick tips: cross-build smoke sim via Alembic, select-linked (L/Ctrl+L), Noise/ColorRamp/Bump procedural shading, Shift+RMB reroute-node insertion, tris-to-quads (Alt+J), custom transform orientations for sliding along a face, Copy Attributes rotation copying, linked/unlinked animation data, a cloth-sim curtain baked to a static mesh via shape keys, Holdout collections for render masking, support loops for non-destructive sharp edges, and the experimental Blender 2.83 alpha Cloth Sculpt Brush (mask, pinch, expand) for sculpting fabric.
- **File:** tutorials/15-blender-secrets-compilation-of-15-blender-tutorials-in-11-minutes.md


### Not a tutorial: Modeling a chair with wireframe backrest
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=IgZqPjHr0eI
- **Author:** Blender Secrets
- **Blender Version:** Not specified — silent screen recording, no version indicator visible
- **Tags:** modelling, procedural, intermediate
- **Summary:** A silent (non-narrated) ~8.5min speed-modeling timelapse of a chair: bent-tube legs, a rounded seat, and a dome-shaped backrest whose surface is refined via a dense quad wireframe grid before final smoothing. Explicitly flagged "not a tutorial" by its own title — no voiceover to transcribe.
- **File:** tutorials/not-a-tutorial-modeling-a-chair-with-wireframe-backrest.md


### Daily Blender Tip 224 - Growing Plant animation (part 2) (Blender 2.7 & 2.8)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qJgbhKcHKsY
- **Author:** Blender Secrets
- **Blender Version:** Blender 2.7 and 2.8 (explicitly named)
- **Tags:** animation, organic, beginner
- **Summary:** Animates a growing vine by keyframing a Bezier curve's Bevel Start value (with Taper/Bevel objects for thickness) from 1.0 to 0.0, while individual leaves along the path pop into view via Scale keyframes timed to the growing tip's position.
- **File:** tutorials/daily-blender-tip-224---growing-plant-animation-part-2-blender-27-28.md


### Daily Blender Tip 186 - Make a rope
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=v6WFoVV3IhY
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Screw + Curve + Array modifiers, version-agnostic)
- **Tags:** modelling, procedural, intermediate
- **Summary:** Procedural rope: a merged cloverleaf profile is twisted into a helical strand via the Screw modifier, bent along a target path with a Curve modifier, and extended/looped with an Array modifier for a longer coiled rope.
- **File:** tutorials/daily-blender-tip-186---make-a-rope.md


### Daily Blender Tip 146 - Microdisplacement in one minute!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=i0c4uCa-WRQ
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Cycles Experimental Adaptive Subdivision; 2.9x-5.x)
- **Tags:** displacement, shaders, cycles, materials, intermediate
- **Summary:** True Cycles microdisplacement: Noise Texture Fac → Displacement socket, Experimental feature set + Adaptive Subdivision modifier, Material Displacement set to real (not Bump), a Multiply node for strength control, and Dicing Scale for render detail.
- **File:** tutorials/daily-blender-tip-146---microdisplacement-in-one-minute.md


### Daily Blender Tip 141 - Fracture Modifier: Helper Add-on
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Tc3Q_OzR628
- **Author:** Blender Secrets
- **Blender Version:** Custom "Fracture Modifier" build (third-party fork)
- **Tags:** rigid-body, simulation, intermediate
- **Summary:** A third-party helper add-on adds one-click Add Fracture/Add RigidBody buttons plus Debris/Dust scattering tools on top of the Fracture Modifier build; also covers Start Deactivated so a fractured object stays visually intact until disturbed.
- **File:** tutorials/daily-blender-tip-141---fracture-modifier-helper-add-on.md


### Daily Blender Tip 140 - Fracture Modifier: Use Constraints
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Lh1wtY2uRPE
- **Author:** Blender Secrets
- **Blender Version:** Custom "Fracture Modifier" build (third-party fork)
- **Tags:** rigid-body, simulation, intermediate
- **Summary:** Fracture Constraint Settings keep pre-shattered shards glued together until stress exceeds a threshold; the key Angle value controls how much bending a joint tolerates before breaking — demoed with a cube crushed under a rolling cylinder at 4° vs 7°.
- **File:** tutorials/daily-blender-tip-140---fracture-modifier-use-constraints.md


### Daily Blender Tip 139 - Blender Fracture Modifier Build - Quick Start
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=6Tk22EdbbLc
- **Author:** Blender Secrets
- **Blender Version:** Custom "Fracture Modifier" build (third-party fork, not stock Blender)
- **Tags:** rigid-body, simulation, beginner
- **Summary:** Quick start for the third-party Fracture Modifier Blender build: passive Rigid Body ground, a Fracture system (Voronoi + Boolean, 1000 shards) pre-shatters an object via Execute Fracture, then Alt+A plays the rigid body sim as it breaks apart realistically.
- **File:** tutorials/daily-blender-tip-139---blender-fracture-modifier-build---quick-start.md


### Daily Blender Tip 138 - How To Make A Curtain In One Minute
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=lYoeTliKX_4
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Cloth Pinning + animated Collision; 2.8+)
- **Tags:** cloth, simulation, animation, beginner
- **Summary:** A pre-wrinkled plane with Cloth Pinning (Silk preset, top-edge Vertex Group) drapes as a curtain; an animated, scaling Torus with Collision cinches the fabric into a tied-back drape as it shrinks from frame 1 to 50.
- **File:** tutorials/daily-blender-tip-138---how-to-make-a-curtain-in-one-minute.md


### Daily Blender Tip 137 - Tissue Add-on: Experiment 3
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8wimWMzVA9M
- **Author:** Blender Secrets
- **Blender Version:** Not specified (earlier-era Tissue add-on Tesselate operator)
- **Tags:** organic, procedural, abstract, intermediate
- **Summary:** Final Tissue experiment: a branching "unit" object grows itself fractally via Tissue's Tesselate + repeated Refresh, then a Remesh modifier set to Metaball fuses the resulting branch network into one smooth organic tree/coral surface.
- **File:** tutorials/daily-blender-tip-137---tissue-add-on-experiment-3.md


### Daily Blender Tip 136 - Tissue Add-on: Experiment 2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=HabMke3KDFc
- **Author:** Blender Secrets
- **Blender Version:** Not specified (earlier-era Tissue add-on workflow)
- **Tags:** organic, procedural, displacement, abstract, intermediate
- **Summary:** Sequel to Experiment 1: a painted Weight Map restricts the Displace modifier to specific regions, and the same weight map continues masking later Decimate/Dual-Mesh/Wireframe steps — showing vertex-group masking survives topology-changing operations.
- **File:** tutorials/daily-blender-tip-136---tissue-add-on-experiment-2.md


### Daily Blender Tip 135 - Tissue Add-on: Experiment 1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=aoZD_EwpWmo
- **Author:** Blender Secrets
- **Blender Version:** Not specified (earlier-era Tissue add-on workflow)
- **Tags:** organic, procedural, displacement, abstract, intermediate
- **Summary:** Early exploratory pass: procedural Displace (Marble/Magic textures) bakes organic bumps into a sphere, Decimate simplifies it into low-poly facets, then Tissue's Dual Mesh operator + a Wireframe modifier transform it into a tangled cage-like structure. First of a 3-part experiment series.
- **File:** tutorials/daily-blender-tip-135---tissue-add-on-experiment-1.md


### Daily Blender Tip 133 - Cast Modifier (Or How To Make Another Weird Sphere...)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=yEDi5SIqXxs
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Cast + Solidify + Subdivision, version-agnostic)
- **Tags:** modelling, procedural, intermediate
- **Summary:** Companion "weird sphere" trick: select a deliberate maze/pattern of faces on a subdivided cube, delete the rest, then use a Cast modifier (Sphere, Factor 1) to bend the resulting lattice into a ball, finished with Solidify + Subdivision for a dimensional ornamental sphere.
- **File:** tutorials/daily-blender-tip-133---cast-modifier-or-how-to-make-another-weird-sphere.md


### Daily Blender Tip 131 - How To Make A Pillow In One Minute
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=EAKd0g65fo8
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Cloth Sewing Springs + Force Field; 2.8+)
- **Tags:** cloth, simulation, beginner
- **Summary:** Puffs a flattened cube into a pillow: Cloth Sewing Springs + zero Gravity hold two near-overlapping "fabric" faces together at the edges, while a high-Strength Force Field blows them apart from the inside for natural creases.
- **File:** tutorials/daily-blender-tip-131---how-to-make-a-pillow-in-one-minute.md


### Daily Blender Tip 132 - Limited Dissolve (Or How To Make An Awewsome Scifi Sphere...)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=HnbVAwIk0lk
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Limited Dissolve + Solidify + Bevel, version-agnostic)
- **Tags:** modelling, procedural, intermediate
- **Summary:** "Death Star" panel-sphere trick: Limited Dissolve randomly merges a dense sphere's faces into jigsaw n-gon panels, invert-selection + a Solidify-style offset modifier stagger alternating panel heights, finished with a Bevel modifier for defined edges.
- **File:** tutorials/daily-blender-tip-132---limited-dissolve-or-how-to-make-an-awewsome-scifi-sphere.md


### Daily Blender Tip 128 - Material Basics: Dust/Snow
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=1F-wFa-oExw
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Geometry Normal node shading, version-agnostic)
- **Tags:** shaders, materials, procedural, beginner
- **Summary:** Fakes dust/snow on upward-facing surfaces: Geometry Normal → Separate RGB isolates the "faces up" channel, used as a Mix Shader Fac to blend a dust/snow material with a base material, shaped further with a ColorRamp for coverage/sharpness control.
- **File:** tutorials/daily-blender-tip-128---material-basics-dustsnow.md


### Daily Blender Tip 120 - NEW Curve Tool in Grease Pencil Blender 2.8
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7SXqr_HlYEg
- **Author:** Blender Secrets
- **Blender Version:** Blender 2.8 Beta (explicitly noted as beta, not for production)
- **Tags:** animation, beginner
- **Summary:** First look at Grease Pencil's then-new Curve tool: editable Bezier-like control points, E to extrude/continue a curve, a configurable Thickness Profile, and Shift for perfectly straight segments.
- **File:** tutorials/daily-blender-tip-120---new-curve-tool-in-grease-pencil-blender-28.md


### Daily Blender Tip 119 - Super Easy PBR Textures With Node Wrangler
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=t1v7lPbCipo
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Node Wrangler, version-agnostic)
- **Tags:** materials, shaders, cycles, beginner
- **Summary:** Quick Node Wrangler PBR workflow: subdivide a test UV sphere (Ctrl+4), create a material, then Ctrl+Shift+T with the Principled BSDF selected to select a whole folder of PBR maps and auto-wire them all in one step.
- **File:** tutorials/daily-blender-tip-119---super-easy-pbr-textures-with-node-wrangler.md


### Daily Blender Tip 114 - Easily Add Camera Movement To A 2D Painting
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=KMcdkXGBTo8
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Images as Planes + Shape Keys, version-agnostic)
- **Tags:** animation, camera, materials, motion-design, beginner
- **Summary:** Fakes camera-move parallax on a still 2D painting by splitting it into depth-offset image planes (Images as Planes add-on, foreground PNG with alpha) each skewed via an animated Shape Key.
- **File:** tutorials/daily-blender-tip-114---easily-add-camera-movement-to-a-2d-painting.md


### Daily Blender Tip 113 - From Sketch To Clean Lines in Grease Pencil
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QO5a2rKhMtQ
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Grease Pencil layers, matured in 2.8x)
- **Tags:** animation, beginner
- **Summary:** Photoshop-style sketch-to-lineart workflow: rough sketch on a low-opacity Grease Pencil layer, clean strokes traced on a layer above, Sculpt Mode to smooth lines, Edit Mode to select/duplicate stroke parts, then hide the sketch layer for the finished line art.
- **File:** tutorials/daily-blender-tip-113---from-sketch-to-clean-lines-in-grease-pencil.md


### Daily Blender Tip 102 - Random Object Colors in Blender 2.8
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=3G0OxL2lfLs
- **Author:** Blender Secrets
- **Blender Version:** Blender 2.8 (explicitly named)
- **Tags:** beginner
- **Summary:** Viewport Shading > Color = Random gives every object a distinct color automatically; combined with the Cavity and viewport-only Shadow overlays for much more readable modeling than the flat default gray shading.
- **File:** tutorials/daily-blender-tip-102---random-object-colors-in-blender-28.md


### Daily Blender Tip 101 - Cycles Bevel Shader in Blender 2.8
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=OIXSc-DM4Pk
- **Author:** Blender Secrets
- **Blender Version:** Blender 2.8 (Cycles Bevel shader, not EEVEE)
- **Tags:** shaders, cycles, materials, beginner
- **Summary:** Fakes a rounded-edge look on sharp hard-surface geometry using Cycles' Bevel shader node (no real geometry change); joining two objects with Ctrl+J is required for the fake bevel to read continuously across their shared seam.
- **File:** tutorials/daily-blender-tip-101---cycles-bevel-shader-in-blender-28.md


### Daily Blender Tip 99 - Drawing In 3D With Grease Pencil And Converting To Mesh
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Fl8PXZWnxr4
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Grease Pencil 3D drawing, Curve conversion, and Mesh from Curve are version-agnostic core Blender features
- **Tags:** grease-pencil, modelling, procedural, intermediate
- **Summary:** Sketches freeform tube-like shapes in 3D space with Grease Pencil, converts the stroke to a Curve (adding Bevel Depth/Resolution for thickness), then F3 > Convert To > Mesh from Curve to bake it into real editable mesh geometry — Decimate afterward to reduce density.
- **File:** tutorials/daily-blender-tip-99---drawing-in-3d-with-grease-pencil-and-converting-to-mesh.md


### Daily Blender Tip 97 - Exploring Grease Pencil - Different Brushes
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=j3M8DFFcysM
- **Author:** Blender Secrets
- **Blender Version:** Blender 2.8 (explicitly referenced in the on-screen caption)
- **Tags:** grease-pencil, workflow, beginner
- **Summary:** Quick survey of the built-in Grease Pencil brush presets in the 2D Animation workspace (Pencil, Noise, Marker, Ink, Block), comparing each preset's default stroke character without manual settings adjustment.
- **File:** tutorials/daily-blender-tip-97---exploring-grease-pencil---different-brushes.md


### Daily Blender Tip 96 - 2D Animation From 3D Animation (Blender 2.8)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QI5rEvu7r4I
- **Author:** Blender Secrets
- **Blender Version:** Blender 2.8 (title explicitly references "Blender 2.8")
- **Tags:** grease-pencil, animation, workflow, intermediate
- **Summary:** Rotoscoping workflow: drags a rendered 3D character walk-cycle into the 2D Animation (Grease Pencil) workspace as a background reference, then hand-draws a rough sketch over it frame-by-frame with the Draw Pencil tool, drastically speeding up hand-drawn animation.
- **File:** tutorials/daily-blender-tip-96---2d-animation-from-3d-animation-blender-28.md


### Daily Blender Tip 95 - Using Empty To Animate Displacement Modifier In A Loop
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=FIYZk64PsWY
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Displacement modifier with Empty texture coordinates, Follow Path constraint, and Linear key interpolation are version-agnostic core Blender features
- **Tags:** procedural, animation, materials, intermediate
- **Summary:** Assigns an Empty as a Displacement modifier's texture coordinate source, then animates the Empty along a circular Follow Path curve so the sampled Clouds-texture region shifts continuously; Linear key interpolation in the Dope Sheet keeps the loop at constant speed.
- **File:** tutorials/daily-blender-tip-95---using-empty-to-animate-displacement-modifier-in-a-loop.md


### Daily Blender Tip 90 - How To Have Characters Interact With Physics Simulations
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RXTJshRSyjk
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Rigid Body physics (Active/Passive/Animated) and bone-parenting are version-agnostic core Blender features
- **Tags:** rigging, character, simulation, rigid-body, advanced
- **Summary:** Since bones can't directly drive Rigid Body physics, parents icosphere proxies to key bones and sets them as Active Rigid Body objects with the Animated flag enabled, letting the keyframed character physically knock through a Rigid Body wall simulation.
- **File:** tutorials/daily-blender-tip-90---how-to-have-characters-interact-with-physics-simulations.md


### Daily Blender Tip 89 - Riggin With Seperate Objects Or Not?
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9takya3FrtI
- **Author:** Blender Secrets
- **Blender Version:** Not specified — this is a modeling/rigging strategy discussion, not tied to specific Blender version features
- **Tags:** rigging, character, modelling, intermediate
- **Summary:** Conceptual comparison under a shared armature: a single connected mesh (skin+clothes fused) deforms without clipping during extreme poses, while separate clothing objects are more modular but risk visible overlap/clipping; references Junya Motomura's Guilty Gear -X- rigging talk (~400 bones).
- **File:** tutorials/daily-blender-tip-89---riggin-with-seperate-objects-or-not.md


### Daily Blender Tip 88 - How To Make A Character Follow A Path
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=k19Gg094jOA
- **Author:** Blender Secrets
- **Blender Version:** Not specified — NLA Editor Action strips and the Follow Path constraint are version-agnostic core Blender animation tools
- **Tags:** rigging, character, animation, intermediate
- **Summary:** Converts the walk-cycle keyframes into an NLA Action strip, then adds a Follow Path constraint (Ctrl+P > Path Constraint, Follow Curve + Animate Path) so the character walks in place while physically traveling along a drawn curve, with Frames controlling travel speed.
- **File:** tutorials/daily-blender-tip-88---how-to-make-a-character-follow-a-path.md


### Daily Blender Tip 87 - Adding Props To Your Character (like a stylish hat)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=eQTkprbLxfA
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Ctrl+P > Bone (Parent to Bone) is a version-agnostic core Blender rigging/parenting tool
- **Tags:** rigging, character, animation, intermediate
- **Summary:** Parents a prop (a top hat) directly to the rig's head bone via Ctrl+P > Bone (select prop, then Shift+select the bone), instead of parenting to the whole armature, so the prop follows head rotation correctly during animation.
- **File:** tutorials/daily-blender-tip-87---adding-props-to-your-character-like-a-stylish-hat.md


### Daily Blender Tip 86 - Simple Character Walk Cycle
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=-QCqVZVwwvM
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Paste Pose Flipped (Ctrl+Shift+V) and standard Pose Mode keyframing are version-agnostic core Blender animation tools
- **Tags:** rigging, character, animation, intermediate
- **Summary:** Part 3: builds a basic walk cycle from 4 key poses (Contact, Down, Up, mirrored Contact), using Ctrl+C / Ctrl+Shift+V (Paste Pose Flipped) to mirror each pose onto the opposite leg instead of hand-posing both sides.
- **File:** tutorials/daily-blender-tip-86---simple-character-walk-cycle.md


### Daily Blender Tip 85 - Rigging A Simple Character Part 2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=I-OSWKJg0ss
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Rigify-generated control rig, Armature Layers, and Pose Mode hide/unhide are version-agnostic core/built-in Blender rigging tools
- **Tags:** rigging, character, animation, intermediate
- **Summary:** Part 2: cleans up the Rigify-generated control rig by hiding raw deform bones (A, H) and isolating the animator-facing control-shape layer (Armature Layers Shift+click, Alt+H to unhide), leaving a clean rig ready for Pose Mode animation.
- **File:** tutorials/daily-blender-tip-85---rigging-a-simple-character-part-2.md


### Daily Blender Tip 84 - Rigging A Simple Character Part 1
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=_OZVTOF1U_U
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Rigify Basic Human Meta-Rig and Armature Symmetrize are version-agnostic core/built-in Blender rigging tools
- **Tags:** rigging, character, animation, intermediate
- **Summary:** Part 1 of a 7-part rigging series: adds a Rigify Basic Human meta-rig, fits bones to one side of the character (using Shift+S Cursor to Selected for pivot placement), then mirrors them with Armature > Symmetrize instead of positioning both sides manually.
- **File:** tutorials/daily-blender-tip-84---rigging-a-simple-character-part-1.md


### Daily Blender Tip 82 - Using Empties For Transformations And Mirroring
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=tUU0zFfMaEE
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Empty objects, Mirror modifier's Mirror Object field, and Make Links (Ctrl+L) are version-agnostic core Blender features
- **Tags:** modelling, workflow, beginner
- **Summary:** Uses an Empty as the Mirror modifier's Mirror Object so the mirror axis can be freely repositioned by moving the empty, then propagates that modifier setup to multiple objects at once via Ctrl+L > Modifiers (Make Links).
- **File:** tutorials/daily-blender-tip-82---using-empties-for-transformations-and-mirroring.md


### Daily Blender Tip 80 - My Painting Workflow In Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Z7JCMVygWoA
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Texture Paint mode, Sample Color (S), brush radius resize (F), and Save As Image are version-agnostic core Blender features
- **Tags:** texture-painting, materials, workflow, beginner
- **Summary:** A practical landscape-painting workflow in Texture Paint mode using Tip 79's custom sharp brush, with S to sample colors directly from the painting, F to resize the brush radius, and F3/Save As Image to export the finished texture.
- **File:** tutorials/daily-blender-tip-80---my-painting-workflow-in-blender.md


### Daily Blender Tip 79 - Texture Painting and Custom Brushes
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=u1h3_0aOBe4
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Texture Paint mode and Brush Curve falloff editing are version-agnostic core Blender features
- **Tags:** texture-painting, materials, workflow, beginner
- **Summary:** Paints directly on a UV-unwrapped object in Texture Paint mode (via the 3D view or the UV/Image Editor's Paint mode), and builds custom sharp/soft brush presets by editing the brush's Curve falloff (Line type + Vector Handle for hard edges).
- **File:** tutorials/daily-blender-tip-79---texture-painting-and-custom-brushes.md


### Daily Blender Tip 78 - Export UV Layout
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=w-GVrw0FBXs
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Export UV Layout and Open Image workflow are version-agnostic core Blender UV/texturing tools
- **Tags:** uv, workflow, materials, beginner
- **Summary:** Exports the cup model's UV Layout (UVs > Export UV Layout, View mode) as a template image, paints the texture externally in Krita on a layer above it, then reloads the finished PNG in Blender's UV/Image Editor and switches to Texture shading to preview it.
- **File:** tutorials/daily-blender-tip-78---export-uv-layout.md


### Daily Blender Tip 77 - Unwrap a Cup - Follow Active Quads
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ScRIlkmNTfw
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Mark Seam, Align Auto, and Follow Active Quads are version-agnostic core Blender UV tools
- **Tags:** uv, modelling, workflow, intermediate
- **Summary:** Manually marks UV seams on a cylindrical cup (thinking of it as unfolded paper), then uses W > Align Auto on a reference face followed by UV > Follow Active Quads to force an even, undistorted grid unwrap across the whole side-wall quad strip.
- **File:** tutorials/daily-blender-tip-77---unwrap-a-cup---follow-active-quads.md


### Daily Blender Tip 75 - More Fracture Stuff!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ZDq2WOrqpRM
- **Author:** Blender Secrets
- **Blender Version:** Not specified — built-in Cell Fracture add-on + Rigid Body physics workflow is version-agnostic
- **Tags:** simulation, rigid-body, procedural, beginner
- **Summary:** Uses the built-in Cell Fracture add-on (distinct from the third-party Fracture Modifier build in Tips 139-141) to shatter a subdivided cube, then applies Rigid Body physics so the fragments explode/collapse realistically when played (Alt+A).
- **File:** tutorials/daily-blender-tip-75---more-fracture-stuff.md


### Daily Blender Tip 72 - Wave Modifier And Blender 2.8!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=gHx-hH5rrD8
- **Author:** Blender Secrets
- **Blender Version:** Blender 2.8 (title explicitly references "Blender 2.8 Stuff")
- **Tags:** modelling, animation, organic, beginner
- **Summary:** Models symmetrical creature legs with a Mirror modifier and Proportional Editing (a jelly-like blob character), then applies a Wave modifier for a continuous jiggly ripple animation across the mesh.
- **File:** tutorials/daily-blender-tip-72---wave-modifier-and-blender-28.md


### Daily Blender Tip 69 - Add Leaves To Our Plant (Make a Plant Part 3)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=DOfWm3GIh-k
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Import Images as Planes, Decimate modifier, and Hair Particle System are version-agnostic core Blender features
- **Tags:** particles, procedural, organic, intermediate
- **Summary:** Part 3 of the plant series: applies Part 2's twig particles to real geometry, Decimates the twig mesh, then adds a second Hair Particle System (Advanced, Number 50) scattering a leaf-texture plane across the twigs, tuned via Rotation/Size Randomness.
- **File:** tutorials/daily-blender-tip-69---add-leaves-to-our-plant-make-a-plant-part-3.md


### Daily Blender Tip 68 - Plant Part 2: Adding Twigs With Particles
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=HqwpZutERRU
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Hair Particle System with Group render mode is a version-agnostic core Blender feature
- **Tags:** particles, procedural, organic, intermediate
- **Summary:** Scatters twig objects (built with Tip 66's Skin-modifier technique) across a tree trunk using a Hair Particle System set to Group render mode, Rotation = Normal for surface-aligned twigs, and tuned Amount/Size/Randomness for natural variation.
- **File:** tutorials/daily-blender-tip-68---plant-part-2-adding-twigs-with-particles.md


### Daily Blender Tip 66 - Quick Tree Trunk With Skin Modifier
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=nfuk9ywJc44
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Skin modifier, Merge at Center, and Proportional Editing are version-agnostic core Blender modeling tools
- **Tags:** modelling, procedural, organic, beginner
- **Summary:** Collapses a mesh to one vertex (Alt+M > Merge at Center), extrudes a branching vertex skeleton, then applies a Skin modifier to instantly generate tapered tube geometry — a fast way to block out tree trunks/branches, refined with per-vertex Ctrl+A scaling and Proportional Editing.
- **File:** tutorials/daily-blender-tip-66---quick-tree-trunk-with-skin-modifier.md


### Daily Blender Tip 65 - Properly Use Poliigon Textures And Add-On
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mOwgdioU1Pw
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Poliigon add-on + Material Settings Displacement dropdown is consistent with Cycles-based displacement across modern Blender versions
- **Tags:** materials, workflow, add-on, beginner
- **Summary:** Getting real geometric displacement working with Poliigon PBR materials: UV Unwrap the object, switch Material Settings > Displacement to True, Tab in/out of Edit Mode to refresh the mesh, and add a Subdivision Surface modifier for enough resolution to actually displace.
- **File:** tutorials/daily-blender-tip-65---properly-use-poliigon-textures-and-add-on.md


### Daily Blender Tip 64 - Faster Render Speeds By Rendering Seperate Layers (Re-Upload)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=WqxHOro0dV8
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Film Transparent, Denoising, and Alpha Over compositor node are version-agnostic core Blender features
- **Tags:** rendering, compositing, workflow, intermediate
- **Summary:** Renders static elements as a single frame and moving elements separately with Film > Transparent + Denoising, then recombines both in the Compositor via two Image nodes → Alpha Over → Composite, avoiding wasted re-renders of unchanging geometry.
- **File:** tutorials/daily-blender-tip-64---faster-render-speeds-by-rendering-seperate-layers-re-uplo.md


### Daily Blender Tip 63 - Using SkinWrap To Project A Sticker To A Surface
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ZtrD7vxi6ik
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Shrinkwrap modifier + Cycles ray-visibility toggles are consistent across modern Blender versions
- **Tags:** modelling, materials, workflow, beginner
- **Summary:** Projects a logo/sticker image plane onto a curved surface using the Shrinkwrap modifier (Target = the object, Keep Above Surface + small Offset), with Cycles Shadow/Glossy ray visibility disabled on the sticker plane; adds Subdivision Surface to the target if the wrap looks distorted.
- **File:** tutorials/daily-blender-tip-63---using-skinwrap-to-project-a-sticker-to-a-surface.md


### Daily Blender Tip 62 - Duplicate Linked
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=W3EtoiG99mo
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Alt+D (Duplicate Linked) and U (Make Single User) are version-agnostic core Blender shortcuts
- **Tags:** workflow, modelling, beginner
- **Summary:** Uses Alt+D (Duplicate Linked) instead of Shift+D so copies share mesh data and update together when any one is edited; breaks a specific copy free with U > Object & Data (Make Single User) when it needs unique geometry.
- **File:** tutorials/daily-blender-tip-62---duplicate-linked.md


### Daily Blender Tip 59 - Crease Edges
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=4YF1p_odCwk
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Edge Crease (Shift+E) is a version-agnostic core Blender modeling tool
- **Tags:** modelling, subdivision-surface, beginner
- **Summary:** Uses Edge Crease (Shift+E, or Shift+E then 1/-1 for max/reset) to non-destructively sharpen selected edges on a Subdivision-Surface-smoothed mesh without adding support-loop geometry.
- **File:** tutorials/daily-blender-tip-59---crease-edges.md


### Daily Blender Tip 56 - How To Use the BoolTool Add-on
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=5_Xa3HwVLRA
- **Author:** Blender Secrets
- **Blender Version:** Not specified — BoolTool has shipped as a built-in opt-in add-on since Blender 2.8x
- **Tags:** modelling, boolean, add-on, beginner
- **Summary:** Enables the built-in BoolTool add-on to turn an object into a movable, non-destructive boolean Brush; cleans up the cut with a Bevel modifier placed below the Boolean modifier, Auto Smooth at 30°, and Bevel Limit Method set to Angle if flat-shading artifacts persist.
- **File:** tutorials/daily-blender-tip-56---how-to-use-the-booltool-add-on.md


### Daily Blender Tip 54 - 2 Viewport Tips
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qj2yDtU2M_I
- **Author:** Blender Secrets
- **Blender Version:** Blender 2.8+ (Viewport Display material color + Matcap/Cavity Viewport Shading popover)
- **Tags:** workflow, viewport, materials, beginner
- **Summary:** Two viewport-clarity tricks: per-material Viewport Display Color (independent of render color) to distinguish mechanical parts, and Matcap + Cavity/Ambient Occlusion (with tuned Strength/Samples) in the Viewport Shading popover for easier-to-read solid shading while modeling.
- **File:** tutorials/daily-blender-tip-54---2-viewport-tips.md


### Daily Blender Tip 51 - Layer Management
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qZTR0HWZ1UE
- **Author:** Blender Secrets
- **Blender Version:** Blender 2.7x (legacy 20-slot Layers system, pre-2.8 Collections)
- **Tags:** add-on, workflow, organization, beginner
- **Summary:** Enables the third-party "3D View: Layer Management" add-on for a readable, renamable list panel over Blender's legacy 20-slot layer system — replacing the tiny grid picker so layers can be named (e.g. "jaw," "shoulder," "Camera") for organizing a rigged character's parts; M+number still moves objects to layers.
- **File:** tutorials/daily-blender-tip-51---layer-management.md


### Daily Blender Tip 48 - Installing Custom Fonts From Google Fonts
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=V1C0TxBfuw0
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Text object Font panel workflow is version-agnostic
- **Tags:** text, workflow, beginner
- **Summary:** Downloads free fonts from fonts.google.com, installs the .ttf files at the OS level, then selects the newly-installed font in a Blender Text object's Font panel (calendar icon shows recently-added fonts first) — with Extrude/Bevel for 3D styling and Alt+C to convert to mesh.
- **File:** tutorials/daily-blender-tip-48---installing-custom-fonts-from-google-fonts.md


### Daily Blender Tip 47 - Custom Transform Orientation
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=dQZ2RwpvFtM
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Ctrl+Alt+Space, version-agnostic)
- **Tags:** modelling, beginner
- **Summary:** Ctrl+Alt+Space creates a Custom Transform Orientation from a selected face, letting Move/Rotate/Scale be constrained to that face's own local axes; saved orientations remain reusable afterward in the Transform Orientation dropdown.
- **File:** tutorials/daily-blender-tip-47---custom-transform-orientation.md


### Daily Blender Tip 46 - 2 Types Of Quick Fluids
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=eElKEBoKUG8
- **Author:** Blender Secrets
- **Blender Version:** Legacy Quick Fluid operator (2.8x-era)
- **Tags:** fluid, simulation, beginner
- **Summary:** The Quick Fluid search operator sets up a full fluid rig instantly in two flavors: the object itself becomes a one-time falling/settling fluid mass, or (by switching its Fluid Type to Inflow) it becomes a continuous fluid source for an ongoing stream/pour effect.
- **File:** tutorials/daily-blender-tip-46---2-types-of-quick-fluids.md


### Daily Blender Tip Number 45 - Quick Hair / Fur and How to Comb and Weight Paint
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cZlzzIBqYbY
- **Author:** Blender Secrets
- **Blender Version:** Not specified — Hair Particle System with Vertex Group density masking and Particle Edit combing are version-agnostic core Blender features
- **Tags:** particles, hair, weight-paint, intermediate
- **Summary:** Paints a Weight Paint vertex group to mask where a Hair Particle System should emit (e.g. only a chin beard), assigns it to the particle system's Density field, then styles the fur directly with Particle Edit mode's Comb brush plus Length/Smooth adjustments.
- **File:** tutorials/daily-blender-tip-number-45---quick-hair-fur-and-how-to-comb-and-weight-paint.md


### Daily Blender Tip #44 - Non-Destructive Boolean Workflow, Round Edges, Bevels,
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=JBJ5dYjPieI
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Boolean + Wireframe draw type, version-agnostic)
- **Tags:** modelling, procedural, intermediate
- **Summary:** Models a rounded L-bracket, then cuts non-destructive Boolean mounting holes using cutter cylinders with Maximum Draw Type set to Wire for real-time-visible positioning, finished with a Bevel modifier for realistic edge highlights.
- **File:** tutorials/daily-blender-tip-44---non-destructive-boolean-workflow-round-edges-bevels.md


### Daily Blender Tip #43 - Import Images As Planes Add-On
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=d028uL7ZRXE
- **Author:** Blender Secrets
- **Blender Version:** Not specified (bundled add-on, disabled by default)
- **Tags:** materials, beginner
- **Summary:** Enables the bundled-but-inactive Import Images as Planes add-on (Preferences search + Save User Settings); once active, Shift+A imports any image as a textured plane with shader nodes (including PNG alpha) auto-wired, demoed by compositing smoke into a photoreal interior render.
- **File:** tutorials/daily-blender-tip-43---import-images-as-planes-add-on.md


### Daily Blender Tip #40 - How To Make Pipes
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=v6mJ6XJatUI
- **Author:** Blender Secrets
- **Blender Version:** Not specified (Curve conversion + Bevel Object, version-agnostic)
- **Tags:** modelling, procedural, beginner
- **Summary:** Turns any object's edges into a pipe: merge all vertices to a skeleton path, bevel corners for rounded bends, convert to Curve, assign a Circle as Bevel Object for thickness, then edit/duplicate that circle profile for ridge/band detail along the pipe.
- **File:** tutorials/daily-blender-tip-40---how-to-make-pipes.md


### Extra Nodes v4.0 | Powerful New Tools for Blender Geometry Nodes - Full Demo
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mS27dSXDSuc
- **Author:** 3D Singh VFX
- **Blender Version:** Not specified (EEVEE + simulation zones; Blender 4.x)
- **Tags:** geometry-nodes, procedural, simulation, animation, motion-design, abstract, advanced
- **Summary:** Feature tour of the paid "Extra Nodes" v4.0 add-on: Curve Roller (physically-accurate curve rolling), Recursive Topology, Mesh Cutter (simulated CNC-style cutting), Geometry Roller, Step Force, Plexus, Inflate Solver with Tear, Edge Tracer, and Animated Follow.
- **File:** tutorials/extra-nodes-v40-powerful-new-tools-for-blender-geometry-nodes---full-demo.md


### My Stylized Blender NPR Pipeline - NOXIOUS Shot Breakdown
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=51aK8POWKQA
- **Author:** Kay Hilman
- **Blender Version:** Blender 4.1
- **Tags:** grease-pencil, geometry-nodes, npr, non-photorealistic, line-art, uv-projection, texture-paint, shading, cycles, eevee, aov, compositing, render-passes, pipeline, advanced
- **Summary:** Full 2D-illustration-to-3D-render NPR pipeline from the short film Noxious: hybrid 2D/3D layout, a custom Geometry Nodes group that offsets hand-drawn Grease Pencil surface curves to kill camera-motion flicker, texel-density-aware UV projection + Clone Brush texture-paint cleanup, a dual EEVEE/Cycles toon shader (Diffuse-BSDF-to-RGB trick for EEVEE, built-in Toon BSDF for Cycles) with starved render settings for crisp cheap shadows, AOV-driven custom render passes with Holdout-masked Line Art view layers, and a full compositing breakdown (After Effects, mirrored in Blender 5.2) combining color/shadow/AO/depth/line passes with mist and a dilated-mask Defocus for depth of field.
- **File:** tutorials/my-stylized-blender-npr-pipeline---noxious-shot-breakdown.md


### Blender 5.2 Just Made Bevels Better
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=PICzZINI0VM
- **Author:** SouthernShotty
- **Blender Version:** 5.2
- **Tags:** geometry-nodes, mesh-bevel-node, bevel, hard-surface, procedural-modeling, panel-cut, sharp-edges, for-each-element, sci-fi
- **Summary:** Tours Blender 5.2's new Mesh Bevel node in Geometry Nodes (Selection, offsets, Miter, Segments, Shape, Profile, and new output-selection mask sockets), then rebuilds a classic hard-surface "panel cut" modifier stack (Edge Split + Solidify + Bevel) as one portable node group: Named Attribute reads `sharp_edge` into Split to Instances, a For Each Element zone solidifies each panel piece independently, Merge By Distance welds seams so the bevel reads continuous edges, and an Edge Angle → Greater Than comparison drives angle-limited beveling (with the angle-subtype gotcha for degrees vs. radians).
- **File:** tutorials/blender-52-just-made-bevels-better.md


### Awesome Wire Generator with Geo Nodes | Blender Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=SvOBxvRjQ8Q
- **Author:** Max Hay
- **Blender Version:** not specified on screen
- **Tags:** geometry-nodes, procedural-modeling, instancing, curves, hard-surface, wires, cables, split-edges, align-rotation-to-vector, endpoint-selection, group-input, menu-switch
- **Summary:** A reusable Geometry Nodes modifier that instances pre-made wire meshes along a hand-drawn chain of extruded edges: Split Edges + Mesh to Curve turn each edge into its own spline, Instance on Points (via Collection Info/Pick Instance for variety) places the wires, an Endpoint Selection node (Start Size 1/End Size 0) fixes a double-instance-per-segment artifact, Spline Length through a Combine XYZ node auto-scales each instance's X to fit its segment, and Curve Tangent through two chained Align Rotation to Vector nodes (second one on Z axis/Pivot X — an empirically-found fix for random upside-down flips) keeps wires hanging naturally regardless of extrude direction. Z-scale and a random seed are exposed as Group Inputs so duplicated wire clusters can be varied independently; a fuller variant adds a Menu Switch to toggle between single-object and full-collection instancing.
- **File:** tutorials/awesome-wire-generator-with-geo-nodes-blender-tutorial.md


### How To Make Better Materials In Blender 5.2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=DhSJ8gD7iyo
- **Author:** BlankFaceStudios
- **Blender Version:** 5.2
- **Tags:** shading, procedural-materials, shader-editor, masking, color-ramp, noise-texture, voronoi-texture, wave-texture, bump-mapping, metal-shader, node-wrangler, node-groups, texture-layering
- **Summary:** Procedural-shading primer built on one core insight — a color is just a 3-value vector, so any single number (a Math node, a noise texture) can drive any color input, and crucially can be used as a black/white mask in a Mix Color node's Factor to blend two colors/values in a patchy pattern instead of a flat average. Covers the four core texture nodes (Noise, Voronoi, Wave, Gradient) plus Color Ramp, then applies masking to Roughness (wet/worn variation) and to a Bump node (fake surface detail without geometry). Builds a full scratched-metal shader from a reference photo: layered noise for a mottled base color, a clamped noise mask multiplied in for dark speckles, Metallic slider, scratches via two rotated Wave Textures (Ctrl+T to expose rotation) or an alternate Voronoi (F1 Distance to Edge) method for longer marks, each broken into discrete clumps by a noise mask, then applied as both a color overlay and an inverted Bump layer. Finishes with a Displacement modifier (Clouds) and node Frame/Group organization tips.
- **File:** tutorials/how-to-make-better-materials-in-blender-52.md


### (Spoilers) Spiderman Tornado Webs Test (Blender 5.3)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ufaZPxkiwtM
- **Author:** Cartesian Caramel
- **Blender Version:** 5.3
- **Tags:** geometry-nodes, simulation-zone, particles, procedural-modeling, curves, vfx, web-effect, sdf-collision, tension-force, blur-attribute, eevee-next, shading, alpha-blend, tri-planar, livestream, advanced
- **Summary:** 113-minute live build recreating the *Spider-Man: Brand New Day* "web tornado" VFX purely in Geometry Nodes (no cloth/physics sim). A Simulation Zone fires particles from a spinning empty into a room collider; on hit, only "end"-marked particles freeze while "start" stays pinned to the spinner, producing taut strands. Each strand instances a separately-built procedural web-patch mesh (grid → random deletion → blurred position → frayed extrude/scale) converted to Cylinder curves for rendering. A tension force built from blurred rest-position offset (captured post-hit, not pre-hit — a real gotcha) makes unattached sections droop realistically. Covers real debugging dead-ends (recursive-subdivision web-shape attempts abandoned, direct constraint-baking broken, velocity blur silently breaking after freeze), a 180°-duplicated "double helix" density trick, Tri-Planar brick/plaster set dressing, a Copy Location constraint gag shot, and a closing lighting/compositing pass. Good case study in GN Simulation Zone debugging methodology.
- **File:** tutorials/spoilers-spiderman-tornado-webs-test-blender-53.md


### Ucupaint Quick Start Guide for Beginners 🖌️ (Blender Tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=KaB8FkBb5rQ
- **Author:** Ryan King Art
- **Blender Version:** 5.2
- **Tags:** ucupaint, texture-painting, layers, blender-addon, roughness, normal-map, bump-map, metallic, baking, shading, beginner
- **Summary:** Quick-start walkthrough of the free Ucupaint extension, which wraps texture painting in a Photoshop-style layer stack over an auto-generated shader network. Quick Ucupaint Node Setup creates a Principled material with toggleable channels (Color/Metallic/Roughness/Normal/Alpha/AO); each paint layer (+ → New Image) is assigned to one channel and resolution, with Preview Mode (paired with the matching Channel button) isolating any single map. Covers Roughness (black=shiny/white=rough), Normal/Bump layers (32-bit float, white=raised/black=recessed), and Metallic (white=metal) painting, then Bake All Channels flattens everything to standard texture maps (auto-baking a bonus Displacement map), a node-icon button auto-wires the baked maps into the real shader graph, and Save All exports them to disk.
- **File:** tutorials/ucupaint-quick-start-guide-for-beginners-blender-tutorial.md


### How to get good lighting in blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=c3FnWQTMo9s
- **Author:** Max Hay
- **Blender Version:** not specified on screen
- **Tags:** lighting, environment-lighting, hdri, sun-light, spot-light, area-light, volume-scatter, golden-hour, overcast, world-shader, composition, beginner, intermediate
- **Summary:** General environment-lighting methodology (not one fixed node setup): always start pitch black, add exactly one light at a time, and position each so it casts visible directional shadows rather than lighting from the camera's own direction. Demonstrated by relighting one static rock/tree/pagoda scene four ways: sunny day (rotated HDRI + low-density Volume Scatter), golden hour (angled warm Sun lamp + Anisotropy-biased volume + a background sky-photo plane, with a callout that the photo's light direction must match the scene's or it instantly reads as fake 3D), a dramatic/moody Spot+Area fill light setup (Radius softens Spot shadow edges from a literal zero-radius hard-shadow default), and an overcast look (denser volume + minimal Area fill). Also covers a controlled-ambient trick: a large fully-black-material cube placed outside camera view blocks/absorbs ambient light from that direction, turning a flat all-directional HDRI setup into something with more directional shadow control.
- **File:** tutorials/how-to-get-good-lighting-in-blender.md


### How I Made This Awesome MRI Effect In Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=4cy1i9THUQg
- **Author:** Nick Impson
- **Blender Version:** 5.1
- **Tags:** mri-effect, x-ray, cross-section-reveal, ray-visibility, light-linking, wave-texture, gradient-texture, subsurface-scattering, compositor, color-correction, film-grain, product-visualization, cad, grabcad, blender-5.1
- **Summary:** Studio-style MRI/X-ray cross-section reveal built with zero volumetrics: an animated slicer plane is hidden from camera-shadow interactions via per-object Ray Visibility toggles (object: Camera+Shadow off; plane: everything off except Camera), lit by an Area light Light-Linked exclusively to the sliced object so the plane only shows bounce light. Plane shader combines a Wave Texture (scan-line look) with a Gradient Texture-driven alpha falloff; object gets a black metal material plus optional Subsurface Scattering for colorful cross-section glow. Finishes with a Compositor pass (Color Correction via Waveform scope, film grain, Tune Image, Posterize, optional Glare/Bloom). Source geometry from grabcad.com.
- **File:** tutorials/how-i-made-this-awesome-mri-effect-in-blender.md


### Volume Editing - Blender Geometry Nodes Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VU_FhO4Jlpg
- **Author:** CGMatter
- **Blender Version:** 5.3
- **Tags:** geometry-nodes, simulation, smoke-fire, volume, procedural, displacement, cycles, advanced, blender-5x
- **Summary:** Deforms an already-baked OpenVDB smoke+fire simulation (bend, twist, split, noise-distort) without re-simulating, by converting volume grids to points with Grid to Points, transforming point positions with ordinary node math, and rebuilding the volume with Blender 5.3's new Rasterize Points node. Covers a divide-by-1 trick to recover lost density weighting and a Principled Volume fire material from the recombined density/flame grids.
- **File:** tutorials/volume-editing---blender-geometry-nodes-tutorial.md
- **Related:** Fluid sim testing in Blender 5.3! (Rasterize Points Node) (`fluid-sim-testing-in-blender-53-rasterize-points-node.md`) — same Rasterize Points node and Blender 5.3. Also shares tags with 3D Smoke (Blender Geometry Nodes) (geometry-nodes, simulation, smoke-fire, volume, blender-5x, advanced) and Blender 5.0's NEW Audio Visualisation is INSANE! (smoke-fire, volume, blender-5x).


### Is This the Most Photorealistic Glass in Blender?
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=c95-5gg3kOs
- **Author:** Blender Wizard
- **Blender Version:** Not specified (4.x-era UI)
- **Tags:** materials, shaders, procedural, glass, cycles, advanced
- **Summary:** Four-node-group photorealistic glass shader with no HDRI (two spotlights only): a Refraction group breaks up perfect refraction with layered/mesh-following Noise Textures into a Bump node; a Caustics group uses Light Path's Shadow Ray output through a Mix Shader plus Geometry Pointiness-driven Color Ramps to fake light bleeding through edges; a Scratches group blends UV-mapped scratched-metal image textures with pointiness edge masks (Overlay) into a Translucent+Metallic Add Shader; and a final fingerprint pass pipes a Fingerprints texture into Roughness/Metallic, with the key realism trick being Anisotropy 1 + a UV Map-driven Tangent node so smudges streak light directionally instead of reading as flat roughness.
- **File:** tutorials/is-this-the-most-photorealistic-glass-in-blender.md
- **Related:** Real time Caustics In Blender 5.1 (`real-time-caustics-in-blender-51.md`) — same Light Path/Shadow Ray caustics-faking trick. Also shares tags with You Should Make Glass Animations in Blender 5.1 (glass, materials, shaders, cycles).


### How to Use Blender Emission Shaders Correctly
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=x1IpbtQ_jO8
- **Author:** Blender Wizard
- **Blender Version:** Blender 5.1.2
- **Tags:** materials, shaders, lighting, procedural, product-viz, blender-5x, intermediate
- **Summary:** Turns a flat uniform Emission shader into a believable glowing-lampshade look: an Image Texture drives Emission Color, while a Gradient Texture (Quadratic Sphere) through a Color Ramp and Math Multiply drives Emission Strength for a fake internal-hotspot falloff. A Blackbody node warms the color (~3000K), kept warmer than any separate light-bulb object's own cooler temperature. For fabric shades, adds Translucency BSDF on modeled fold/wire-armature geometry plus a Layer Weight/Fresnel-driven rim-brightness Color Ramp so edges glow more than flat faces. Final version swaps Multiply for Multiply Add to decouple hotspot strength from rim contribution, finished with Brightness/Contrast.
- **File:** tutorials/how-to-use-blender-emission-shaders-correctly.md
- **Related:** Realistic Product Lighting In Blender (`realistic-product-lighting-in-blender.md`) — same Gradient Texture + Color Ramp emission-falloff technique. Shares tags: lighting, materials, product-viz.


### [CROSS-REFERENCE ONLY] Fire FX in Houdini, Blender and Nuke
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=NRM-e4ECT7c
- **Author:** Anton Dann
- **Blender Version:** Not specified
- **Tags:** camera-tracking, cross-platform-reference
- **Summary:** Cross-platform VFX breakdown (Blender camera tracking → Houdini fire sim/render → Nuke comp). The Blender-side technique is just plate tracking in the Movie Clip Editor (auto Detect Features + manual markers, ~1.58px error, no lens/camera data). The bulk of the technical content is Houdini simulation/rendering, so the full extraction lives in the **houdini-wand** skill, not here.
- **Full extraction:** `houdini-wand/tutorials/fire-fx-in-houdini-blender-and-nuke.md` (https://github.com/barrozo3d/houdini-wand/blob/master/tutorials/fire-fx-in-houdini-blender-and-nuke.md)
- **⚠ Do not re-ingest this URL in blender-motion** — this stub exists only so this index surfaces the tutorial by search; ingesting it here would fork the content. If new Blender-specific detail is found, add it to the canonical file in houdini-wand instead.


### Photorealistic Texturing In Blender 5.0
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8HfKtaDx6tM
- **Author:** Extra 3d
- **Blender Version:** Blender 5.0
- **Tags:** materials, shaders, texturing, pbr, procedural-texture, texture-painting, node-wrangler, uv, displacement, bump-map, normal-map, color-ramp, product-viz, intermediate
- **Summary:** Layered photoreal texturing workflow on a wood side-table and a Hitem3D-generated statue: Node Wrangler PBR auto-setup, grunge-texture-masked color variation via Mix Color, a dirt layer via Mix Shader, edge wear from Bevel·Geometry dot product, per-layer displacement/bump/normal mixing (Add vs. Overlay), and hand-painted wood-chip detail via Texture Paint with an image stencil. Closes with a bonus fingerprint/scratch-driven glass roughness trick.
- **File:** tutorials/photorealistic-texturing-in-blender-50.md
- **Related:** Easy PBR Textures - Blender Secrets (`easy-pbr-textures---blender-secrets.md`) — shares Node Wrangler PBR setup + box mapping fundamentals. Also shares tags with Daily Blender Tip 119 - Super Easy PBR Textures With Node Wrangler (node-wrangler) and Daily Blender Tip 79 - Texture Painting and Custom Brushes (texture-painting).


### Top Tip Tuesday - Liquid Fill
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=vglrHSL-uc4
- **Author:** INSYDIUM LTD
- **Blender Version:** Not specified (NeXus for Blender plugin by Insydium)
- **Tags:** simulation, fluid-sim, flip, particles, foam, whitewater, third-party-plugin, nexus, motion-blur, procedural, intermediate
- **Summary:** Insydium's one-click nxLiquid Fill sets up a full FLIP/APIC liquid rig (emitter, solver, mesher, foam) automatically; covers emitting into a custom object with an nxCollider, the auto-managed resolution/particle-count relationship, mesher Scale/Smoothing tuning to avoid holes vs. lost droplet detail, nxFoam whitewater with a separate dedicated foam emitter for clean output control, and render prep (Create Point Cloud, Transfer Velocity for motion blur).
- **File:** tutorials/top-tip-tuesday---liquid-fill.md
- **Related:** NeXus for Blender Official Training - Follow Curve (`nexus-for-blender-official-training---follow-curve.md`) — same NeXus plugin and emitter/mesher/motion-blur workflow. Also shares tags with Sand Simulation - Blender Tutorial (Nexus) (nexus, particles, third-party-plugin).


### Improve your Motion Blur in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VeW-3BWUtlM
- **Author:** Dantti
- **Blender Version:** Not specified
- **Tags:** compositing, motion-blur, view-layers, holdout, render-layers, grease-pencil, workflow, intermediate
- **Summary:** Fakes per-part motion blur in the Compositor with a Directional Blur node (independent Iterations/Distance/Angle/Spin/Zoom) applied to Holdout-masked, separately-rendered View Layers, then recombined with Add nodes — works even on object types like Grease Pencil that don't get good native render-time motion blur. Note: source video's ASR transcript is badly corrupted past ~1:24; extraction relies mainly on the captured frames' node graphs.
- **File:** tutorials/improve-your-motion-blur-in-blender.md
- **Related:** My Stylized Blender NPR Pipeline - NOXIOUS Shot Breakdown (`my-stylized-blender-npr-pipeline---noxious-shot-breakdown.md`) — shares grease-pencil, compositing, render-passes; same Holdout-masked View Layer → Compositor pattern.


### [Tut] Different Instance Color and Materials - P13 Geometry Nodes Beginners
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=812uN8EFWVs
- **Author:** Bradley Animation
- **Blender Version:** Blender 5.3+ referenced on-screen (Switch node in shader editor); techniques otherwise version-general
- **Tags:** geometry-nodes, instancing, materials, shaders, procedural, attributes, eevee, cycles, motion-graphics, intermediate
- **Summary:** Per-instance shading in Geometry Nodes without realizing instances: Store Named Attribute on the Instance domain + the shader Attribute node's Instancer domain toggle for per-instance color; Set Position's before/after-instancing behavior difference; UV vs. raw-position texture mapping surviving realize-instances; a dual-domain (per-polygon + per-instance) Mix-node color recipe; Cycles' inability to displace instances differently; EEVEE's 14-attribute-per-material cap; and a White Noise Texture ID/seed trick to fake shader-side randomness (with a Round-node fix for float-precision flicker).
- **File:** tutorials/tut-different-instance-color-and-materials---p13-geometry-nodes-beginners.md
- **Related:** [Tut] How Pick Instance is used for Instance Variations - P10 Geometry Nodes Beginners (`tut-how-pick-instance-is-used-for-instance-variations---p10-geometry-nodes-begin.md`) — direct predecessor in the same series, explicitly referenced; geometry variation (P10) vs. color/shader variation (P13).
- **Related:** [Tut] Everything about For Each Element Zone in Variations - P14 Geometry Nodes Beginners 5.0+ (`tut-everything-about-for-each-element-zone-in-variations---p14-geometry-nodes-be.md`) — direct successor in the same series; its Hash Value "index seed" fix parallels this episode's White Noise Texture ID/seed trick for the same correlated-randomness problem.


### How I made this bridge destruction scene in blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=yV4zUZiDZW4
- **Author:** FxForge
- **Blender Version:** ~Blender 5.1 (visible in-frame title bar; uses the newer Array modifier and Simulation Nodes)
- **Tags:** geometry-nodes, simulation-nodes, rigid-body, destruction, fracture, procedural, particles, smoke-fire, soft-body, lattice, dynamic-paint, vfx, advanced
- **Summary:** High-level breakdown (not step-by-step) of a from-scratch, no-paid-add-ons Blender destruction pipeline: a custom dual-mesh Geometry Nodes fracture cutter (straight sim-proxy + noisy render mesh), a custom "Destruction Tools" panel for large-scale auto-constraint placement, Simulation-Nodes wire continuity (closest-vertex tracking + break threshold) and a 7-iteration procedural rebar system, Simulation-Nodes seam-only smoke/particle emission, a lattice+soft-body-plastic-deformation car-crush cheat, Dynamic Paint water fake, and a low-poly-viewport-proxy scattering tip.
- **File:** tutorials/how-i-made-this-bridge-destruction-scene-in-blender.md
- **Related:** Faster Alembic Playback in Blender (MDD Workflow) (`faster-alembic-playback-in-blender-mdd-workflow.md`) — contrasting approach: simulating destruction natively in Blender (this tutorial) vs. simulating elsewhere (Houdini RBD) and importing fast via Alembic+MDD (that tutorial).
- **Related:** Superhero Landing Tutorial 02 | Ground Destruction VFX in Blender (`superhero-landing-tutorial-02-ground-destruction-vfx-in-blender.md`) — shares vfx, rigid-body, particles, destruction; traditional Cell Fracture + Mantaflow approach to contrast against this video's custom Simulation Nodes tooling.


### NS Infinite Rock Builder Guide - Main Controls
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VkYNlPxOsUk
- **Author:** Nick Sayce
- **Blender Version:** 4.x (title-bar visible in frames but exact point release not legible)
- **Tags:** geometry-nodes, procedural, displacement, organic, intermediate, blender-4x
- **Summary:** Foundation/overview video of the third-party "Infinite Rock Builder" add-on (Nick Sayce/NS): install the add-on, apply it to a subdivided plane, add 1 of 25 preset procedural "formations," and stack more on top via Mix Strength or a Blend Mode (Add/Exclusion/Subtract/Divide), noting formations chain in numeric order and can be transferred from the default plane onto a custom hand-sculpted shape (Object mapping requires re-scaling Overall Scale/Strength). "Make Single" detaches a rock's node group so duplicates stop sharing edits.
- **File:** tutorials/ns-infinite-rock-builder-guide---main-controls.md


### NS Infinite Rock Builder Guide - Colours
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=1ezIk-0qoDg
- **Author:** Nick Sayce
- **Blender Version:** 4.x (see Main Controls video for title-bar reading; not independently confirmed here)
- **Tags:** materials, shaders, procedural, organic, beginner, blender-4x
- **Summary:** Third-party NS Infinite Rock Builder add-on (Nick Sayce): coloring a rock via the add-on's pre-wired Shader Editor node group — Main Colour 1/2 (each with a Color Ramp + noise Filter) combined with a Screen-mode Colour 1-2 Mix, plus a Disp Colour that follows displacement for a built-in AO/weathering effect; Node Wrangler Ctrl+Shift-click used throughout to preview individual nodes.
- **File:** tutorials/ns-infinite-rock-builder-guide---colours.md


### NS Rock Sculptor Guide - Geometry & Scatter
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=BePg_iEbaM4
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, partially legible in frames)
- **Tags:** procedural, displacement, particles, organic, product-viz, beginner
- **Summary:** Third-party NS Rock Sculptor add-on (Nick Sayce): decimating a sculpted rock (~0.1-0.2 ratio, repeatable) into a low-poly pebble for scattering, a warning that Edge Wear must be applied before decimating (it turns white/blotchy on mangled decimated topology), and the Scatter tab workflow — plane target, rock presets, vertex-group-painted density, Number/Scale/Length tuning to build a layered rock pile.
- **File:** tutorials/ns-rock-sculptor-guide---geometry-scatter.md


### NS Infinite Rock Builder Guide - Filters
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=yLhymD__KvI
- **Author:** Nick Sayce
- **Blender Version:** 4.x (see Main Controls video for title-bar reading; not independently confirmed here)
- **Tags:** geometry-nodes, procedural, displacement, organic, intermediate, blender-4x
- **Summary:** Third-party NS Infinite Rock Builder add-on (Nick Sayce): each active formation auto-populates its own Filters entry (Displacement Control, Shape Ramp, Shape Filter) controlling that formation's displacement shape, distinct from the color filters; demonstrated on Formation 1 and 24, stressing that filter selection must be deliberate (Shift-click) and adjustments should stay subtle to avoid a messy result.
- **File:** tutorials/ns-infinite-rock-builder-guide---filters.md


### NS Infinite Rock Builder Guide - Moss / Fresnel / Dust
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=thzYTUEyrKI
- **Author:** Nick Sayce
- **Blender Version:** 4.x (see Main Controls video for title-bar reading; not independently confirmed here)
- **Tags:** materials, shaders, organic, procedural, beginner, blender-4x
- **Summary:** Third-party NS Infinite Rock Builder add-on (Nick Sayce): three quick finishing sliders — Ambient Dust (AO-style crevice darkening), Fresnel (~0.6 for glancing-angle shine), and Moss (Z-axis/height-masked green tint that favors upper surfaces, formation-dependent).
- **File:** tutorials/ns-infinite-rock-builder-guide---moss-fresnel-dust.md


### NS Infinite Rock Builder Guide - Cliff-top Flatten / Bump
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VwaeyQtmgw8
- **Author:** Nick Sayce
- **Blender Version:** 4.x (see Main Controls video for title-bar reading; not independently confirmed here)
- **Tags:** geometry-nodes, procedural, displacement, organic, intermediate, blender-4x
- **Summary:** Third-party NS Infinite Rock Builder add-on (Nick Sayce), series finale: Cliff Top Flatten levels the rock's upper surface for set-dressing (Shift-click to raise/lower height, plus a rounding slider); Bump 1/2/3 layer independent fine-detail passes (verified via Node Wrangler on "Bump Out"); closes with build-order advice — dial in everything on the flat plane first, then re-lower Scale/Strength when transferring to a custom Object-mapped shape.
- **File:** tutorials/ns-infinite-rock-builder-guide---cliff-top-flatten-bump.md


### NS Rock Sculptor Guide - Bump
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=E9J_1VH2aPM
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, partially legible in frames)
- **Tags:** procedural, displacement, organic, product-viz, beginner
- **Summary:** Third-party NS Rock Sculptor add-on (Nick Sayce): layering four bump-detail channels (standard bump, cracks bump, cracks bump 2, dusty bump) each with their own strength/distance and mask, plus dusty bump's dedicated Colour Ramp; cracks bump overrides standard bump at full strength; a strength ~1.5-2 tip for extra weathered detail.
- **File:** tutorials/ns-rock-sculptor-guide-bump.md


### NS Infinite Rock Builder Guide - Water Level Roughness
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8ZX5DsV7eBc
- **Author:** Nick Sayce
- **Blender Version:** 4.x (see Main Controls video for title-bar reading; not independently confirmed here)
- **Tags:** materials, shaders, procedural, organic, beginner, blender-4x
- **Summary:** Third-party NS Infinite Rock Builder add-on (Nick Sayce): "Water Level / Roughness" section sets a height (UV-space or 3D-space, with an Object/UV toggle) below which the rock is tinted by two color swatches (Water Level, Coral Ring), and a roughness/softness value controls how hard vs. blended the waterline transition reads. Thin transcript (flagged needs-review by ingest safeguard) — extraction leans on captured frames.
- **File:** tutorials/ns-infinite-rock-builder-guide---water-level-roughness.md


### NS Rock Sculptor Guide - Displacement
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=l174YngAFs8
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, viewport title bar in captured frames; not stated verbally)
- **Tags:** procedural, displacement, organic, product-viz, intermediate
- **Summary:** Third-party NS Rock Sculptor add-on (Nick Sayce): two complementary displacement paths — material/shader displacement gated by a noise-driven Displacement Mask Colour Ramp, and a genuine Blender Displace modifier ("Rock Displace", Clouds texture) with a hand-paintable Vertex Group mask; warns that stacking too much of both mangles geometry, and shows Weight-Paint mask editing to localize/blur where displacement reads.
- **File:** tutorials/ns-rock-sculptor-guide---displacement.md


### NS Rock Sculptor Guide - Colour Ramps
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=vm4QsOascts
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, viewport title bar in captured frames; not stated verbally)
- **Tags:** materials, procedural, organic, product-viz, beginner
- **Summary:** Third-party NS Rock Sculptor add-on (Nick Sayce): fine-tuning the Dust and Main Colour Ramps in the sidebar's Colour Ramps tab — dragging stops closer/further apart resizes dust patch density, and extra ramp stops can be added via the color picker for multi-color variation; this ramp is reused as the Displacement Mask in the next tab.
- **File:** tutorials/ns-rock-sculptor-guide---colour-ramps.md


### NS Rock Sculptor Guide - Filters
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=9jrj0IG7Xe8
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, viewport title bar in captured frames; not stated verbally)
- **Tags:** procedural, displacement, organic, product-viz, beginner
- **Summary:** Third-party NS Rock Sculptor add-on (Nick Sayce): a centralized "Choose a Filter to Edit" dropdown exposes parameters for every effect layer (Roll, Main Colour, Grain/Cracks/Cracks 2/Dusty Bump, Displacement, Displacement Mask) instead of hunting across separate panels; demoed on Dusty Bump Filter (Scale/Seed/Weight/Distortion) plus adjacent Displacement group fields.
- **File:** tutorials/ns-rock-sculptor-guide---filters.md


### NS Rock Sculptor Guide - Moss
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Acp5-LuffVA
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, viewport title bar in captured frames; not stated verbally)
- **Tags:** materials, procedural, organic, product-viz, beginner
- **Summary:** Third-party NS Rock Sculptor add-on (Nick Sayce): two-color Moss layer gated by Moss Height (world-space "up" threshold) with Distortion/Thickness edge-shaping controls; flags a gotcha where a randomly-rotated rock needs Ctrl+A Apply Rotation before the moss mask aligns with its visual top.
- **File:** tutorials/ns-rock-sculptor-guide---moss.md


### NS Rock Sculptor Guide - Colour
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=NaimTlxwn2Q
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, viewport title bar in captured frames; not stated verbally)
- **Tags:** materials, procedural, organic, product-viz, intermediate
- **Summary:** Third-party NS Rock Sculptor add-on (Nick Sayce): base Colour 1/2 plus Dirt (Multiply blend) and Dust (Screen blend) color passes routed through the Filters tab, and two independent Edge Wear swatches (bottom vs. top of the color-blend stack) that read differently depending on whether a later Dirt multiply breaks up the wear pattern beneath them.
- **File:** tutorials/ns-rock-sculptor-guide---colour.md


### NS Rock Sculptor Guide - Edge Crease
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=YEtwMhsKh1A
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, viewport title bar in captured frames; not stated verbally)
- **Tags:** procedural, geometry-nodes, organic, product-viz, intermediate
- **Summary:** Third-party NS Rock Sculptor add-on (Nick Sayce): a weighted Edge Crease panel (weight ~0.3 + Apply Crease button) plus a fully manual G-G vertex-nudge fallback for corners the remesh/crease combo can't reach cleanly, so selected edges stay sharp/faceted under the Subdivision Surface modifier instead of the whole rock rounding into a uniform blob. Also references the add-on's separate Edge Wear feature for previewing crease results.
- **File:** tutorials/ns-rock-sculptor-guide---edge-crease.md


### NS Rock Sculptor Guide   Sculpt Settings
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ErHZ6gbPl6g
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, viewport title bar in captured frames; not stated verbally)
- **Tags:** procedural, geometry-nodes, displacement, organic, product-viz, intermediate
- **Summary:** Third-party NS Rock Sculptor add-on (Nick Sayce), core-algorithm episode: knife-bisects a base cube Number-of-Cuts times with each cut's center-distance constrained by Min/Max Offset to carve a boulder silhouette; covers Make Single (detaches shared material) with a critical warning to add any Displace modifier before clicking it, plus a paintable white mask to protect areas from cutting.
- **File:** tutorials/ns-rock-sculptor-guide-sculpt-settings.md


### NS Rock Sculptor Guide - Presets
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=XbdMfva0fPA
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, viewport title bar in captured frames; not stated verbally)
- **Tags:** procedural, displacement, organic, product-viz, beginner
- **Summary:** Third-party NS Rock Sculptor add-on (Nick Sayce), series intro/Presets tab: 32-thumbnail preset grid + "Load Selected Preset" one-click starting point (bundles mesh, material, and any Displace modifier); demos active-material isolation — separately loaded presets keep fully independent material data, so edits to one never affect the other.
- **File:** tutorials/ns-rock-sculptor-guide---presets.md


### NS Brick Wall Builder v4 0 Guide
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VZ7MObyyCJk
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, viewport title bar in captured frames; not stated verbally)
- **Tags:** procedural, geometry-nodes, displacement, organic, product-viz, intermediate, blender-5x
- **Summary:** Third-party NS Brick Wall Builder v4.0 add-on (Nick Sayce), full guide: curve-driven wall generator (strict even-number/positive-direction curve rules), 11+11 presets, Make Single for branching independent walls, and the full Base Shape/Colour/Mortar/Jitter/Displacement/Filters/Colour Ramps/Bevel/Bump control stack.
- **File:** tutorials/ns-brick-wall-builder-v4-0-guide.md


### NS Brick Wall Builder Guide
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=zcuefJcZdUY
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, viewport title bar in captured frames; not stated verbally)
- **Tags:** procedural, geometry-nodes, displacement, organic, product-viz, intermediate
- **Summary:** Third-party NS Brick Wall Builder add-on (Nick Sayce), earlier full guide (predates v4.0): requires 3 specific materials appended into the scene, same curve-driven generator concept, Cracked/Damage Bricks Amount sliders (no separate Colour Ramps tab yet), Make Single to branch independent walls.
- **File:** tutorials/ns-brick-wall-builder-guide.md


### NS Brick Wall Builder   Mimicking a Real Wall
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=jl2Q-86o0JE
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, viewport title bar in captured frames; not stated verbally)
- **Tags:** procedural, geometry-nodes, organic, product-viz, beginner
- **Summary:** Third-party NS Brick Wall Builder add-on (Nick Sayce), silent tip video: side-by-side visual matching against a real brick-wall reference photo, tuning Rotation Variation/Distorted Bricks/Damaged Bricks Amount by eye until the procedural wall's irregularity matches the reference.
- **File:** tutorials/ns-brick-wall-builder-mimicking-a-real-wall.md


### NS Brick Wall Builder   Mimicking a Real Wall 2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=v3rbV49UVwo
- **Author:** Nick Sayce
- **Blender Version:** 5.1.x (approximate, viewport title bar in captured frames; not stated verbally)
- **Tags:** procedural, geometry-nodes, materials, organic, product-viz, beginner
- **Summary:** Third-party NS Brick Wall Builder add-on (Nick Sayce), Part 2 of the silent real-wall-matching tip: continues into color (Brick/Mortar Colour via HSV picker, Colour Variation, Dirt Colour) and Bump strength (Pattern/Coin/Mortar) matching against the reference photo.
- **File:** tutorials/ns-brick-wall-builder-mimicking-a-real-wall-2.md


### Abstract Animated Geometric Pattern | Squares | Geometry Nodes Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7I4k8iaF7D8
- **Author:** Artemiy Galutskiy
- **Blender Version:** 4.x (Repeat Zone node present, feature introduced in Blender 4.0; exact point release not stated)
- **Tags:** geometry-nodes, procedural, abstract, motion-design, animation, intermediate, blender-4x
- **Summary:** Recursive quad-subdivision "fractal squares" pattern using a Repeat Zone: each pass tests a per-cell Noise Texture value against a threshold to decide subdivide-vs-keep, then a second noise+Color Ramp pass selects a scattered highlight-color subset over the resulting grid, finished with an animated wipe/reveal.
- **File:** tutorials/abstract-animated-geometric-pattern-squares-geometry-nodes-tutorial.md


### Create Plexus FX In Blender ( Geometry Node )
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ZUiCC5iTUWs
- **Author:** Manbo Studio
- **Blender Version:** 4.x (Geometry Nodes UI matches 4.x-era layout; exact point release not stated or clearly legible)
- **Tags:** geometry-nodes, procedural, abstract, motion-design, compositing, animation, intermediate, blender-4x
- **Summary:** Animated glowing "Plexus" line network: Scene Time + Noise Texture-driven Set Position displaces a Grid into a faceted, flat-shaded terrain, its edges isolated into a line network, lit with strong Emission and finished with Compositor Glare/bloom for the neon look.
- **File:** tutorials/create-plexus-fx-in-blender-geometry-node.md


### Blender 3.0 Tutorial - Creating a Glowing River
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=YwDj4bs4bSY
- **Author:** Blender Made Easy
- **Blender Version:** 3.0 (stated in title; Mantaflow fluid domain UI confirmed in frames)
- **Tags:** simulation, fluid, particles, materials, shaders, compositing, cycles, volume, glass, emission, motion-design, intermediate, blender-3x
- **Summary:** Mantaflow liquid domain flowing through an A.N.T. Landscape "River" preset mesh, foam particles instanced onto low-poly cones with an Emission shader for the glow, a Glass+Volume water material, and compositor Vector Blur (fed by Z/Vector passes) for motion blur on the particles.
- **File:** tutorials/blender-30-tutorial---creating-a-glowing-river.md


### Creating Realistic 3D Water in Blender : The Ultimate Guide
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=vr7mkSiKRLM
- **Author:** stache
- **Blender Version:** 3.6 (stated in transcript: "the advent of simulation nodes now in Blender 3.6")
- **Tags:** materials, shaders, procedural, simulation, fluid, particles, animation, compositing, rendering, product-viz, motion-design, intermediate, advanced, blender-3x
- **Summary:** Broad reference survey of every water technique in Blender: shader-only murky/pool water (volume nodes, caustics via Voronoi), Ocean modifier foam/spray, Dynamic Paint waves, underwater volumetrics + bubbles, rain add-ons, fake/cheat simulations (displaced cylinder tap water, video-texture streams/beach), and a critical take on native Mantaflow fluid sim reliability.
- **File:** tutorials/creating-realistic-3d-water-in-blender-the-ultimate-guide.md


### Blender Tutorial - Creating a Crown Splash Simulation
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=KbAUrN0ExjM
- **Author:** Blender Made Easy
- **Blender Version:** 3.x (Mantaflow domain/Modular cache UI matches 3.x era; exact point release not stated)
- **Tags:** simulation, fluid, materials, shaders, camera, lighting, rendering, cycles, glass, product-viz, intermediate, blender-3x
- **Summary:** Mantaflow liquid domain with a keyframed Ico Sphere effector crashing through a flow layer for a "crown splash," deliberately simulated at low resolution/large scale then sold as macro water via a ~200mm focal length, Glass BSDF (IOR 1.333) in Cycles, and a 3-light glass product-photography rig with DoF.
- **File:** tutorials/blender-tutorial---creating-a-crown-splash-simulation.md


### [Tut] Align Rotation to Vector & Axes to Rotation - P11 Geometry Nodes Beginners 5.0+
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=bZXZNEiKlNg
- **Author:** Bradley Animation
- **Blender Version:** 5.0+ (stated in title; UV Tangent node specifically called out as new in 5.1)
- **Tags:** geometry-nodes, procedural, animation, motion-design, intermediate, advanced, blender-5x
- **Summary:** Deep dive on instance/point rotation: Align Rotation to Vector's single-axis limitation vs. the modern two-axis Axis to Rotation node, building target-tracking direction vectors via subtraction, UV Tangent/Curve Tangent/Normal as direction sources, and Rotate Rotation + Axis Angle to Rotation + Cross Product for bending curves (gravity/tree-branch effect) rather than constructing rotation from scratch.
- **File:** tutorials/tut-align-rotation-to-vector-axes-to-rotation---p11-geometry-nodes-beginners-50.md
- **Related:** [Tut] Everything about For Each Element Zone in Variations - P14 Geometry Nodes Beginners 5.0+ (`tut-everything-about-for-each-element-zone-in-variations---p14-geometry-nodes-be.md`) — same series/author/version target, complementary instance-modification deep dive.


### How I Model Ancient Ruins in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=lT1UBQwtZ1g
- **Author:** hbitproject
- **Blender Version:** 5.2 (visible in viewport title bar in captured frames)
- **Tags:** geometry-nodes, procedural, displacement, materials, shaders, compositing, rendering, lighting, hdri, product-viz, advanced, blender-5x
- **Summary:** Full ruined-architecture production breakdown: a reusable asset-ized procedural damage system (Mesh to Volume/back, noise-driven normal displacement, Boolean Intersect), Pick Instance for hand-cut mesh variants, damage-aware material masking via Capture Attribute + boolean NOT, Geoscatter foliage, and HDRI+Sun light-group/mist-pass compositing.
- **File:** tutorials/how-i-model-ancient-ruins-in-blender.md


### Mastering Complex Textures in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=GejnTuB2GNQ
- **Author:** rileyb3d
- **Blender Version:** 4.x (viewport title bar visible in captured frames, exact point release not fully legible)
- **Tags:** materials, shaders, procedural, rendering, product-viz, motion-design, intermediate, advanced, blender-4x
- **Summary:** Full low-poly game-asset pipeline (notebook prop): real-world-scale modeling with snapping/grid-fill, UV cleanup, deeply layered procedural+photo-reference shader work (Map Range as the workhorse node, physical-prop-photography texturing trick), then a high-to-low-poly PBR bake via the SimpleBake add-on into a clean Base Color/Roughness/Normal set.
- **File:** tutorials/mastering-complex-textures-in-blender.md


### NPR Light Accumulation (Blender 5.3 Branch Testing)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=GFGIjeI539k
- **Author:** Cartesian Caramel
- **Blender Version:** 5.3 experimental/unmerged branch build (self-compiled by presenter from a pull request, not a public release; not in main 5.2/5.3 as of recording)
- **Tags:** shaders, materials, lighting, rendering, eevee, compositing, motion-design, abstract, advanced, expert, blender-5x
- **Summary:** EXPERIMENTAL/UNRELEASED feature exploration: three new EEVEE-only shader nodes (Light Info, Shadow Raycast, Light Accumulation) expose per-light data for hand-built lighting, plus a "clip fix" (Vector Math Project+Subtract) technique for freely offsetting the shadow ray's sampling position — enabling stylized fractured-glass, pixel-aligned "Minecraft," and pseudo-SSS shadow looks.
- **File:** tutorials/npr-light-accumulation-blender-53-branch-testing.md


### [Tut] Everything about For Each Element Zone in Variations - P14 Geometry Nodes Beginners 5.0+
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Mm1Oxz6sGAg
- **Author:** Bradley Animation
- **Blender Version:** 5.0+ (stated in title)
- **Tags:** geometry-nodes, procedural, instancing, animation, motion-design, intermediate, advanced, blender-5x
- **Summary:** Deep dive on the For Each Element zone (FEEZ) as a real alternative to Realize Instances: zone input/output structure and the Inspection Index, using loop Index/ID to seed per-element Random Value, modifying existing instances individually on the Instance domain (Extrude Mesh per-instance), correcting the rotation/scale "relative influence" pitfall, and using FEEZ for procedural generation (per-element primitive parameters like Cube vertex count) impossible after instancing. Extensive benchmarking shows FEEZ is 2x-10x slower than Realize Instances for simple/high-count elements but ~2x faster once element complexity crosses a threshold. Closes with the same-ID/seed correlated-randomness bug fixed via per-node seeds or a Hash Value "index seed" node group, plus a hybrid FEEZ+Pick Instance pattern for performance.
- **File:** tutorials/tut-everything-about-for-each-element-zone-in-variations---p14-geometry-nodes-be.md
- **Related:** [Tut] How Pick Instance is used for Instance Variations - P10 Geometry Nodes Beginners (`tut-how-pick-instance-is-used-for-instance-variations---p10-geometry-nodes-begin.md`) — earlier "fake variation" (Pick Instance) approach this episode explicitly contrasts against FEEZ's "real variation".
- **Related:** [Tut] Different Instance Color and Materials - P13 Geometry Nodes Beginners (`tut-different-instance-color-and-materials---p13-geometry-nodes-beginners.md`) — immediately preceding episode; its White Noise Texture ID/seed trick parallels this episode's Hash Value "index seed" fix for correlated randomness.
- **Related:** [Tut] Align Rotation to Vector - Axis to Rotation - P11 Geometry Nodes Beginners 5.0+ (`tut-align-rotation-to-vector-axes-to-rotation---p11-geometry-nodes-beginners-50.md`) — same series/author/version target, complementary instance-rotation deep dive.


### Faster Alembic Playback in Blender (MDD Workflow)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=H0_hfNoEv_I
- **Author:** DAMIDIGITAL
- **Blender Version:** Not specified
- **Tags:** alembic, rigid-body, destruction, animation, rendering, cycles, intermediate, houdini-crossover
- **Summary:** Workflow tip for viewport-fast playback of external point-count-stable simulations (example: a Houdini RBD/Bullet destruction sim): export both a standard Alembic sequence and an MDD point cache from the source DCC, import the Alembic once (static, first frame only) for topology, then drive it in Blender with a Mesh Cache modifier pointed at the .mdd file (with corrected axis mapping). Side-by-side comparison shows Alembic-sequence playback at ~10-13 fps vs. a smooth, consistent 25 fps via the MDD/Mesh Cache route. Roughly two-thirds of the video is Houdini-side scene/sim/export setup rather than Blender; only works for sims with a constant point count (not applicable to fluids that add/remove points).
- **File:** tutorials/faster-alembic-playback-in-blender-mdd-workflow.md
- **Related:** How I made this bridge destruction scene in blender (`how-i-made-this-bridge-destruction-scene-in-blender.md`) — Blender-native destruction/fracture tooling, contrasted with this tutorial's import-a-Houdini-sim workflow.
- **Note:** A significant portion of this video (Houdini RBD sim build + MDD export setup) is Houdini-specific; a lightweight cross-reference stub pointing back to this canonical entry was added to `houdini-wand/tutorials/INDEX.md`.


### Grease Pencil Fundamentals: 2D Animation
- **Source:** Blender Studio
- **URL:** https://studio.blender.org/training/grease-pencil-fundamentals/5c40c0d679f30a0147c0c194/
- **Author:** Matias Mendiola (Blender Studio)
- **Blender Version:** 2.80 (status bar reads v2.80.37 / v2.80.39) — see the version caveat: Grease Pencil was rewritten as GPv3 in 4.3
- **Tags:** animation, grease-pencil, 2d-animation, onion-skinning, beginner
- **Summary:** Onion skinning, multiframe editing, and duplicating keyframes instead of redrawing them: the lesson builds a bouncing ball animation on the 2D Animation template and then generalises the same workflow to character animation. It starts by shortening the playback range and adding a dedicated layer for a **reference motion path** — the pink arc visible across [frame_001] and [frame_002] — drawn in **Camera...
- **File:** tutorials/grease-pencil-fundamentals-2d-animation.md


### Grease Pencil Fundamentals: Drawing Brushes and Materials
- **Source:** Blender Studio
- **URL:** https://studio.blender.org/training/grease-pencil-fundamentals/5c40c1d379f30a0147c0c19a/
- **Author:** Matias Mendiola (Blender Studio)
- **Blender Version:** 2.80 (status bar reads v2.80.39) — see the version caveat: Grease Pencil was rewritten as GPv3 in 4.3
- **Tags:** grease-pencil, materials, brushes, texturing, beginner
- **Summary:** Brush versus material: stroke colour, fill style, the stabilizer, jitter and the texture brush. Each Grease Pencil tool has its own brush family — the freehand draw tool and the primitives use **draw** brushes, the fill tool uses **fill** brushes, the eraser uses **eraser** brushes. Brush settings live in the Active Tool panel or the top bar, which in [frame_001] reads `Draw Pencil | Radius 221px | Strength 0.936 |...
- **File:** tutorials/grease-pencil-fundamentals-drawing-brushes-and-materials.md


### Making my lens in Blender (Bokeh, glare, chromatic aberrations)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=nru_2wdBqsY
- **Author:** Robin Squares
- **Blender Version:** Blender 5.2
- **Tags:** compositing, camera, rendering, cycles, lighting, materials, shaders, blender-5x, expert
- **Summary:** Rebuilds one specific real lens (17.5mm prime, MFT) inside Blender so CG matches footage shot on it: three compared bokeh methods (camera DoF, a physical bokeh-image plane giving cat's eyes, and nine screen-segmented Bokeh Blur nodes), a custom glare kernel generated in RealBloom and loaded via the Glare node in Kernel mode, lens breathing driven by a focus-to-focal-length driver curve calibrated from a filmed focus rack, and depth-varying chromatic aberration built per-channel with Vector Curves. Centres on a 15-step order of operations where every effect removed from the plate is re-added after compositing.
- **File:** tutorials/making-my-lens-in-blender-bokeh-glare-chromatic-aberrations.md


### Blender 5.3 gets dispersion!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Q9irGPAcUDE
- **Author:** Christopher 3D
- **Blender Version:** Blender 5.3
- **Tags:** materials, shaders, glass, rendering, cycles, blender-5x, intermediate
- **Summary:** Blender 5.3 adds native dispersion to the Principled BSDF transmission channel via Dispersion Scale and Dispersion Abbe Number, replacing the legacy trick of splitting RGB into three hard IOR offsets with a quasi-spectral approximation converted back through a CIE colour matching function. Covers the inverse Abbe scale, an IOR/Abbe table for 16 real materials, and the critical fix: Cycles default indirect clamp of 10 truncates the red and blue spectral spikes and leaves a green cast, so raise it to 50+ — with a worked counter-example where disabling clamping entirely reintroduces denoiser-breaking fireflies.
- **File:** tutorials/blender-53-gets-dispersion.md


### I made the VFX tool Blender was missing... (Full Workflow)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=TWYYOKlwgds
- **Author:** InLightVFX
- **Blender Version:** Blender 5.2
- **Tags:** compositing, camera, rendering, blender-5x, advanced
- **Summary:** Full undistort/VFX/redistort pipeline using a free Blender 5.2+ add-on ("Undistort") that calibrates lens distortion from a checkerboard or Charuco board and exports the solve as ST maps. Compares five lens models by solve error, builds the compositor Map UV setup automatically, and generates a matched camera carrying solved focal length, sensor width and optical-center shift. Key lesson: single-image calibration removes distortion well but yields an untrustworthy focal length, which multi-image Charuco calibration fixes — and the final composite never undistorts the plate, only redistorts the CG, with overscan preventing transparent edges.
- **File:** tutorials/i-made-the-vfx-tool-blender-was-missing-full-workflow.md


### [Tut] What makes Spline/Curves more complicated - P16 Geometry Nodes Beginners 5.0+
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=YLJjEYd47JQ
- **Author:** Bradley Animation
- **Blender Version:** Blender 5.2
- **Tags:** geometry-nodes, procedural, rendering, eevee, cycles, blender-5x, intermediate
- **Summary:** Episode 16 maps Blender's two coexisting curve systems: the legacy Curve object (invisible until converted via Curve to Mesh, whose Scale socket replaced the old Set Curve Radius auto-behaviour) and the new Hair Curve object (natively renderable, added only as a child of a selected mesh, bound to the surface by data settings rather than parenting). New-curve rendering works only on that object type and only on realized geometry — instancing breaks it. Decodes curve_type in the spreadsheet (Poly 1, Bezier 2, NURBS 3, plus Catmull Rom for sculpted hair), shows that "resolution" only fabricates virtual render points (a Bezier Segment at Resolution 256 still has 2 real points), flags Quadratic Bezier as actually a polyline, and contrasts Resample Curve (converts to polylines; Evaluated/Count/Length modes) with Subdivide Curve (preserves type). Also untangles the spline vs curve vs hair nomenclature split.
- **File:** tutorials/tut-what-makes-splinecurves-more-complicated---p16-geometry-nodes-beginners-50.md


### I Combined 5 HDRIs in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=MvJEnsMX4DU
- **Author:** roe.num77
- **Blender Version:** Blender 4.5
- **Tags:** lighting, hdri, materials, shaders, rendering, blender-4x, intermediate
- **Summary:** Layers five HDRIs in the World shader by chaining Mix (Color) nodes on Lighten/Screen at Factor 0.3, each map getting its own Texture Coordinate/Mapping/Environment Texture chain in a labelled frame plus independent grading via Hue-Saturation-Value and a Separate Color to Math(Multiply) to Combine Color triplet (dropping a channel entirely is used to kill unwanted red). Closes with a Light Path node feeding Is Camera Ray into a Mix Shader Fac, so one Background node controls how much light the HDRI emits while a second controls how bright it appears, independently — and a Sky Texture can be swapped into either side. Camera is Panoramic / Fisheye Equisolid at 360 degrees.
- **File:** tutorials/i-combined-5-hdris-in-blender.md


### Can Blender Still Compete (Motion Graphics)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=bDHdUT2oiZE
- **Author:** Ducky 3D
- **Blender Version:** Blender 5.2
- **Tags:** geometry-nodes, motion-design, materials, shaders, lighting, cycles, glass, blender-5x, intermediate
- **Summary:** Rebuilds a Tendril Studio Cinema 4D render in Blender 5.2 to argue the MoGraph case. The core move is an SDF round trip: scattered, randomly stretched cubes are forced to intersect, then Realize Instances into Mesh to SDF Grid into Grid to Mesh fuses every intersection into one continuous surface with a natural bevel (watch the voxel size — it is effectively subdivision). Material is a Mix Shader of Glass and Principled BSDF driven by a Noise Texture and Color Ramp; the backdrop is a spherical Gradient Texture sharpened by a Math Power node at exponent 5.8 rather than a Color Ramp, lit so the key light falls into the dark side of the gradient. Loops by keyframing two Mapping nodes Z from -25 to 25 with linear default interpolation.
- **File:** tutorials/can-blender-still-compete-motion-graphics.md


### Kinetic Typography in Blender | 09 | Geometry Nodes Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=D3t_ysgEqxQ
- **Author:** Artemiy Galutskiy
- **Blender Version:** Blender 5.2
- **Tags:** geometry-nodes, typography, motion-design, animation, procedural, eevee, blender-5x, advanced
- **Summary:** NO NARRATION — silent screencast; the ingest transcript floor flagged it CRITICAL (136 chars against a 500-char minimum), so this entry is extracted from frames alone with evenly-spaced sampling. Recreates the Studio Dumbar kinetic-typography look ("DUMBAR STYLE") entirely in Geometry Nodes: a String node into String to Curves generates the letterforms procedurally, a low-resolution Grid (12.3m x 1m, 3x3 verts) slices them into horizontal bands, and a Repeat zone with Sample Index on the Instance domain plus Set Instance Transform drives per-band motion, controlled by an Empty read through Object Info. A Bake node freezes the instance evaluation, Color Ramps drive material colour and alpha, and the whole animation is keyed from one Value socket exposed on the modifier. Captures the node vocabulary and technique shape, not the intermediate wiring.
- **File:** tutorials/kinetic-typography-in-blender-09-geometry-nodes-tutorial.md


### Don't Make Boring Audio Visualizers (Blender Tutorial)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=2xGchC_1Mi8
- **Author:** Ducky 3D
- **Blender Version:** Blender 5.2
- **Tags:** geometry-nodes, motion-design, animation, procedural, compositing, eevee, blender-5x, intermediate
- **Summary:** Breaks the left-to-right waveform bias of the Sample Sound Frequencies node by driving the frequency lookup from a shuffled Index (Index into Random Value in Integer mode) instead of position, so audio-reactive values scatter across faces rather than marching along one axis. Frequency window is a Map Range to 20-15000 Hz into Low with an Add of 100 into High, fed by Scene Time seconds; the result is stored as a named attribute and read into an Emission shader. Design pass adds Split Edges, Scale Elements, Extrude Mesh and Mesh Bevel, a Layer Weight facing mix, and a Bloom plus Film Grain composite (Blender 5.2 required). Note: the author explicitly doubts on camera whether his Index-into-ID link does anything, so that connection is recorded as unverified.
- **File:** tutorials/dont-make-boring-audio-visualizers-blender-tutorial.md


### Optimize Heavy Blender Scenes
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=SLVbMEF5LVU
- **Author:** roe.num77
- **Blender Version:** Blender 5.0
- **Tags:** rendering, materials, intermediate, blender-5x
- **Summary:** Non-destructive optimisation of a 10 GB scene with the free memsaver add-on (N-panel tab "polygoniq"). Resize Images and Decimate Meshes apply across all scene objects in one click and are fully reversible from a per-scene cache. The workflow that matters is the ordering: crush everything first, then Revert Images/Meshes to Originals on only the objects inside the camera frustum, so the viewport stays navigable while the render keeps its detail. Depth of field is exploited deliberately — out-of-focus characters go to 64 or 32 px textures. Measured on a test plane: 5,222,912 triangles down to 522,290 at Decimation Ratio 0.10. Texture resizing propagates through scatters (GeoScatter, geometry nodes or particles). Panel also exposes Adaptive Optimize, Check & Regenerate Images and Memory Estimation with HTML reports, none of which the video covers.
- **File:** tutorials/optimize-heavy-blender-scenes.md


### Boiling Water - Blender Fluid Simulation + Geometry Nodes Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=MRGgqR1N_b8
- **Author:** CGMatter
- **Blender Version:** Blender 5.2
- **Tags:** simulation, fluid, geometry-nodes, procedural, materials, shaders, blender-5x, advanced
- **Summary:** Two routes to boiling water. The simulation route drives a FLIP sim with geometry-node bubbles: points rising on a looping Fraction of time, instanced icospheres, Realize Instances, then registered as a Fluid Effector with Sampling Substeps 2 so they physically displace liquid; spray/foam/bubble/liquid particle systems are pulled out through Particle Instance modifiers on single-vertex proxy objects for separate shading (bubble IOR 1.05 vs water 1.33). The real-time route is the better idea: two Voronoi Textures with identical Scale 5.0 and Randomness 1.0, one in F1 distance mode and one in N-Sphere Radius mode, mapped against each other (Map Range inverted To Min 1.0 / To Max 0.0) to build a correctly-packed height field of hemispheres rising through a cross-section, rounded by a Float Curve and layered at several scales. Needs the free CGMatter node pack (Grid Fill 2D). Closes with Border to Curve walls, Flip Faces and Merge by Distance to make a valid watertight volume.
- **File:** tutorials/boiling-water---blender-fluid-simulation-geometry-nodes-tutorial.md


### The 6 Levels of Blender Materials
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=RfPro3hlOMg
- **Author:** Kaizen
- **Blender Version:** Blender 5.2
- **Tags:** materials, shaders, procedural, geometry-nodes, cycles, metal, blender-5x, intermediate
- **Summary:** Six-stage progression from a bare Principled BSDF to a reusable smart material. Levels 1-3 cover the BSDF, layering texture nodes (Voronoi at Scale 1000 through a Normal Map at Strength 0.1 for metallic flake), and tuning 0-1 texture output into sensible ranges with Color Ramp or Map Range. Level 4 is the architectural turn: a material can hold multiple shader nodes, so a second Principled BSDF becomes a dirt shader combined via Mix Shader (not Add Shader) with a texture mask, and scratches go into Coat Roughness rather than Roughness. Level 5 makes it smart — Edge Angle stored as a named attribute in Geometry Nodes masks scratches onto convex edges, and an Ambient Occlusion node masks dirt into crevices, so the material adapts to any mesh. Level 6 exposes the controls on the Geometry Nodes modifier as Base Color, Speckle Scale, Speckle Strength and Dirt Level.
- **File:** tutorials/the-6-levels-of-blender-materials.md


### [Tut] Sample UV Surface for UV Deformer - P15 Geometry Nodes Beginners 5.0+
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=XmSjMms8KoA
- **Author:** Bradley Animation
- **Blender Version:** Blender 5.2
- **Tags:** geometry-nodes, procedural, displacement, blender-5x, advanced
- **Summary:** Episode 15 builds a UV deformer with Sample UV Surface: remap source geometry into 0-1 space via a Bounding Box, sample the target through its UV map to reposition it, then recover the lost height with a second sample of the surface Normal driving an offset. Resolves the node's confusing pair of UV sockets (UV Map takes the sampled geometry's UV; Sample UV takes the field from your own geometry) and gives a diagnostic: mix the result against original position, and collapse to world origin means a failed sample. Covers Bounding Box Min/Max/Use Radius, the instance case where Min and Max output zero entirely, the Is Valid socket for dropping unsampled points, and overlapping-UV breakage fixed with Pack UV Islands. Two blunt performance warnings: UV operations in geometry nodes are very slow (0.40 ms to 124 ms on a 55-cubed cube once Pack UV Islands is inserted), and Split to Instances is slow and origins every instance at the world origin — use an island-index average position with Vector Rotate instead.
- **File:** tutorials/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50.md


### [Tut] How to use Vertex Group and Named Attribute? - P3 Geometry Nodes Beginners 5.0+
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=wgAF2lUSu70
- **Author:** Bradley Animation
- **Blender Version:** Blender 5.1
- **Tags:** geometry-nodes, procedural, materials, shaders, blender-5x, beginner
- **Summary:** Episode 3 separates named attributes (written with Store Named Attribute, read with Named Attribute, persistent on the geometry) from anonymous attributes or fields (a node output plugged straight into the socket that needs it, then discarded). Named attributes inflate the spreadsheet, multiply under subdivision and are written to disk — a file can grow from kilobytes to gigabytes — so fields are the default; the analogy is weights on your body versus tools in your hands. Two cases still require a named attribute: vertex groups, which are named attributes from the outset, and passing data to shaders, since shaders always evaluate after geometry nodes and data flows one way only (avoid the name "color", which fails in Cycles). Also corrects a common misuse: "implicit attribute" is not a type of attribute but a socket pre-filled with one, and Blender 5.0 removed the socket-appearance cue that used to reveal it. Closes with Ctrl+F, which since 5.0 searches text boxes and used group-input sockets.
- **File:** tutorials/tut-how-to-use-vertex-group-and-named-attribute---p3-geometry-nodes-beginners-50.md


### How to make Looping Polyrhythms in Blender
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=-ZUAhe-gRns
- **Author:** Polyfjord
- **Blender Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/how-to-make-looping-polyrhythms-in-blender.md

---

## Tag Reference

### By Technique
`#geometry-nodes` `#simulation` `#particles` `#fluid` `#rigid-body` `#cloth` `#smoke-fire`
`#materials` `#shaders` `#procedural` `#displacement`
`#animation` `#rigging` `#motion-blur` `#camera`
`#compositing` `#rendering` `#cycles` `#eevee`
`#lighting` `#hdri` `#volume`

### By Subject
`#product-viz` `#motion-design` `#abstract` `#logo` `#typography`
`#liquid` `#metal` `#glass` `#fabric` `#organic`
`#particles-reveal` `#logo-animation` `#brand-video`

### By Level
`#beginner` `#intermediate` `#advanced` `#expert`

### By Creator (add as you ingest)
`#entagma` `#default-cube` `#grant-abbitt` `#blender-secrets` `#albin-merle`
`#cyril-muller` `#caramel-cartesian` `#sean-terelle`

### By Blender Version
`#blender-3x` `#blender-4x` `#blender-42` `#blender-45` `#blender-5x`
