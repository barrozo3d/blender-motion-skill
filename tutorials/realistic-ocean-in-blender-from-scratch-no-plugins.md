---
title: Realistic Ocean in Blender From Scratch (No Plugins)
source: YouTube
url: https://www.youtube.com/watch?v=1eQp-H73zeI
author: Vlabs
ingested: 2026-07-16
blender_version: "not stated on screen (Gabor Texture + Principled Volume node — Blender 4.x/5.x compatible)"
tags: [materials, shaders, ocean, water, procedural-texture, gabor-texture, displacement, volume-scattering, light-path, eevee-cycles, beginner]
extraction_status: complete
frames_dir: tutorials/frames/realistic-ocean-in-blender-from-scratch-no-plugins/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Realistic Ocean in Blender From Scratch (No Plugins)

**Source:** [YouTube](https://www.youtube.com/watch?v=1eQp-H73zeI)
**Author:** Vlabs
**Duration:** 5m55s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### What we're building [0:00]
**Transcript (timestamped):**
[0:00] What if I told you that you could create a cinematic ocean scene using nothing but free built in blender tools?
[0:05] No plugins, no paid add-ons, just blender and the right techniques?
[0:09] In this tutorial, I'm going to walk you step by step through building a fully realistic ocean scene from absolute scratch.
[0:15] To rain, water, waves, depth, reflections, all of it.
[0:19] Stay to the end because the final render trick is what takes this from good to cinematic.


### part 1 Building the Terrain [0:25]
**Transcript (timestamped):**
[0:26] Before we touch water, we need land.
[0:29] Hit Shift plus A and add a plane, now scale it up.
[0:34] This will be the base of our environment, the ground the ocean sits on, now press tab to enter edit mode.
[0:39] Right click and hit subdivide.
[0:44] Do this twice.
[0:45] Sub-vision adds more geometry to the flat plane, which gives us polygons to push and pull into actual terrain.
[0:53] Head to the modifier properties tab the wrench icon and add a displacement modifier.
[0:58] This modifier physically pushes the vertices of your mesh up and down based on a texture, creating the illusion of rugged terrain without manual sculpting.
[1:06] Now go to texture properties and add a new texture.
[1:10] Change the type to Voronoi.
[1:12] This is a cell-based noise pattern that naturally mimics rocky, irregular terrain.
[1:17] Adjust the size and intensity until your terrain feels natural to you.
[1:28] With the terrain shaped, let's give it a material that actually looks like rock or sand.


### part 2 Terrain Material [1:31]
**Transcript (timestamped):**
[1:37] In the material properties tab add a new material.
[1:40] Now open the shader editor.
[1:41] Here we're going to use a Gabor Texture node.
[1:44] Think of it as a procedural wave pattern that blender generates mathematically.
[1:49] Add a bump node.
[1:51] Connect the value output from the Gabor Texture into the height input of the bump node.
[1:55] Then connect the normal output of the bump node into the normal input of the principal BSDF.
[2:02] For a 90-degree rotation to shift the grain direction, set the rotation value accordingly.
[2:08] Keep tweaking until it looks right to your eye.
[2:11] There's no wrong answer here.
[2:13] Alright, now for the star of the show.


### part 3 Building the Water [2:19]
**Transcript (timestamped):**
[2:23] Add a cube and scale it to cover your scene.
[2:26] Imagine it as a giant block of water sitting on the terrain.
[2:31] Add a new material.
[2:35] Set the transmission weight to 1.
[2:37] This tells blender to let light pass through the object, which is essential for glass, water, and ice.
[2:43] Set the IOR to 133 because that's the real world value for water.
[2:47] Meaning our blender water bends light exactly like real water does.
[2:51] Set roughness to 0 for a perfectly smooth mirror like water surface.
[2:55] You'll immediately notice the plane below starts reflecting inside the cube.
[3:01] Now add a transparent BSDF node and a mixed shader.
[3:07] Connect the transparent BSDF to the first input of the mixed shader and the principal BSDF to the second.
[3:19] Add a light path node and plug the is camera ray output into the factor of the mixed shader.
[3:25] Is camera ray is only for rays coming directly from the camera, not from reflections or lights.
[3:30] By routing this to the mix, we make the water appear crystal clear to the viewer's eye,
[3:35] while still behaving realistically for reflections and lighting.
[3:39] Without this, water often looks murky or weirdly opaque.
[3:42] For now, set the water color to a blue tone,
[3:45] just so it's easy to see and adjust while we're still building the scene.
[3:48] We'll refine this later.


### part 4 Adding Underwater Depth [3:51]
**Transcript (timestamped):**
[3:53] Flat water looks like a swimming pool.
[3:55] Real ocean water has depth, light fades, color shifts, things get darker the deeper you go.
[4:01] Add a principled volume node and connect it to the volume input of the material output.
[4:06] Light rays interact with it as they pass through, giving you that gorgeous deep water look.
[4:11] Keep the density value very low, something like 0.01 to 0.05.
[4:16] Too high and your water looks like thick soup, too low and you lose the effect entirely.
[4:21] Think of density as how foggy the water is.
[4:25] An isotropy controls the direction that light scatters through the volume.
[4:31] A high positive value pushes light forward, like sunlight cutting down through shallow clear water.
[4:36] A low or negative value scatters light in all directions, giving you murkier, deeper ocean feel.
[4:42] Play with this to match the mood of your scene.
[4:46] Finally, change the volume color to a turquoise or aquashape.
[4:50] This gives that beautiful tropical lagoon feel.
[4:52] Water that glows with color when sunlight hits it.
[4:57] The last thing missing is surface movement, that rippled, textured top layer that makes water


### part 5 Surface Waves [5:00]
**Transcript (timestamped):**
[5:02] unmistakably look like water. We use the same trick as the terrain. Add a gabor texture.
[5:08] Connect it to a bump node and plug the bump node into the normal input of the water's principled BSDF.
[5:16] Adjust the distance, scale and frequency until your waves feel right.
[5:21] Higher frequency means more ripples pack together, rougher water.
[5:24] Lower frequency means longer, smoother swells, deeper, calmer ocean.


### outro [5:30]
**Transcript (timestamped):**
[5:35] And that is how you create a cinematic tropical ocean in blender.
[5:38] If this helped you, hit that like button. It genuinely helps this channel grow
[5:43] and tells me to make more of these deep dives.
[5:45] Subscribe and turn on notifications so you don't miss the next one.
[5:48] And drop a comment below what you want to build next in blender. See you in the next one.



---

## Captured Frames

- [0:34] tutorials/frames/realistic-ocean-in-blender-from-scratch-no-plugins/frame_000.jpg
- [0:58] tutorials/frames/realistic-ocean-in-blender-from-scratch-no-plugins/frame_001.jpg
- [1:51] tutorials/frames/realistic-ocean-in-blender-from-scratch-no-plugins/frame_002.jpg
- [2:43] tutorials/frames/realistic-ocean-in-blender-from-scratch-no-plugins/frame_003.jpg
- [3:19] tutorials/frames/realistic-ocean-in-blender-from-scratch-no-plugins/frame_004.jpg
- [4:01] tutorials/frames/realistic-ocean-in-blender-from-scratch-no-plugins/frame_005.jpg
- [5:08] tutorials/frames/realistic-ocean-in-blender-from-scratch-no-plugins/frame_006.jpg
- [5:35] tutorials/frames/realistic-ocean-in-blender-from-scratch-no-plugins/frame_007.jpg

---

## Structured Notes

### Core Technique
Builds a full ocean scene from three stock Blender ingredients only — a Displacement-modifier terrain driven by a Voronoi texture, a glass-like water volume (Transmission + IOR 1.33 + Principled Volume) whose clarity is controlled with an `Is Camera Ray` mix, and Gabor-texture-driven bump normals for both rock and water surface ripples — with no ocean-sim modifier, no add-ons, and no plugins.

### Summary
A fast (under 6 minutes), plugin-free walkthrough for building a stylized/cinematic ocean using only built-in Blender nodes and modifiers — no Ocean modifier, no Flip Fluids, no third-party add-ons. It layers four independent techniques: (1) a Displacement modifier over a subdivided plane, driven by a Voronoi texture, to sculpt rocky terrain without manual sculpting; (2) a Gabor Texture → Bump node combo for a procedural rock-grain material; (3) a "water as a solid glass block" material — a scaled-up cube with Transmission weight 1, IOR 1.33 (real-world water), Roughness 0, mixed with a Transparent BSDF via a Light Path `Is Camera Ray` factor so the water reads crystal-clear to the camera while still refracting/reflecting correctly for indirect rays; and (4) a Principled Volume node for underwater depth/color falloff (very low density, adjustable anisotropy for scattering direction, turquoise/aqua volume color). A second Gabor+Bump pass on the water's own material adds the final surface ripple detail. The result is a "recipe" video more than a deep-dive — each step names the node and rough value range without much explanation of why, so it's best used as a checklist to replicate the exact look rather than a from-first-principles lesson.

### Key Steps
1. **Terrain base:** Shift-A → Mesh → Plane, scale it up, Tab into Edit Mode, right-click → **Subdivide** (do this twice) to add pushable/pullable geometry.
2. **Terrain displacement:** Modifier Properties → add **Displacement** modifier; Texture Properties → add a new texture, set type to **Voronoi** (cell-based noise that reads as rocky/irregular terrain); adjust Size and Intensity until the terrain silhouette looks natural.
3. **Terrain material:** Material Properties → new material → Shader Editor → add a **Gabor Texture** node (procedural mathematically-generated wave pattern) → **Bump** node (Gabor's Value output → Bump's Height input) → Bump's Normal output → Principled BSDF's Normal input; rotate the Gabor pattern (e.g. 90°) to change grain direction; tweak by eye.
4. **Water volume block:** Shift-A → add a Cube scaled to cover the whole scene (a "block of water" sitting on the terrain). New material: set **Transmission Weight = 1** (lets light pass through, essential for glass/water/ice), **IOR = 1.33** (real-world water value — bends light like real water), **Roughness = 0** (perfectly smooth/mirror-like surface — the terrain below will visibly reflect inside the cube once this is set).
5. **Crystal-clear camera view fix:** add a **Transparent BSDF** and a **Mix Shader**; connect Transparent BSDF → Mix Shader input 1, Principled BSDF → Mix Shader input 2; add a **Light Path** node and plug its `Is Camera Ray` output into the Mix Shader factor. `Is Camera Ray` is true only for rays coming directly from the camera (not reflections/lighting), so this routes direct camera view to transparent/clear while keeping full reflective/refractive behavior for indirect rays — without it, water reads as murky or oddly opaque. Set a temporary blue Base Color to make the setup visible while building.
6. **Underwater depth:** add a **Principled Volume** node, connect it to the Material Output's Volume socket. Set **Density** very low (0.01–0.05 range — too high looks like thick soup, too low loses the effect). **Anisotropy**: high positive value scatters light forward (sunlight cutting through shallow clear water look), low/negative value scatters light in all directions (murkier/deeper ocean feel). Set Volume **Color** to turquoise/aqua for a tropical-lagoon look.
7. **Surface ripples (final water detail):** reuse the same Gabor Texture → Bump trick from step 3 — add a Gabor Texture, connect to a Bump node, plug the Bump's Normal output into the water material's Principled BSDF Normal input. Adjust the Gabor node's distance/scale/frequency: higher frequency = more/tighter ripples (rougher-reading water), lower frequency = longer smoother swells (calmer, deeper-reading ocean).

### Nodes / Settings
**Displacement modifier** (terrain sculpting) + **Voronoi** texture, **Gabor Texture** node (used twice — terrain grain and water ripples) → **Bump** node → **Normal** input of **Principled BSDF**, water material settings: **Transmission Weight = 1**, **IOR = 1.33**, **Roughness = 0**, **Transparent BSDF** + **Mix Shader** driven by **Light Path → Is Camera Ray**, **Principled Volume** node (Density ~0.01–0.05, Anisotropy, turquoise Color) wired into the Material Output **Volume** socket.

### Difficulty
Beginner — every step is a single stock node/modifier with a stated value, no custom node groups, drivers, or geometry-nodes logic; the only conceptual leap is understanding why `Is Camera Ray` is needed to separate direct-view transparency from physically-correct reflection/refraction.

### Blender Version
Not stated on screen. The **Gabor Texture** node requires Blender 4.3 or later, so despite no explicit version card this tutorial needs at minimum Blender 4.3 (likely presented on a current 4.x/5.x build).

### Tags
#materials #shaders #ocean #water #procedural-texture #gabor-texture #displacement #volume-scattering #light-path #beginner

---

## Related Tutorials
- [Como hacer Agua Realista en Blender](como-hacer-agua-realista-en-blender.md) — the other indexed water/ocean tutorial; uses Adaptive Subdivision + 4D Noise Texture + a driver instead of Displacement+Voronoi/Gabor, useful as an alternate no-plugin water recipe to compare against this one.
- [Blender's NEW Transparency Material is CRAZY!](blenders-new-transparency-material-is-crazy.md) — covers the newer Thin Wall transmission option on the Principled BSDF, directly relevant to refining or modernizing the plain Transmission-weight-1 water/glass material built in step 4-5 here.
- No other indexed tutorial currently covers the Gabor Texture node or Principled Volume for underwater depth directly — this is the first entry using either.
