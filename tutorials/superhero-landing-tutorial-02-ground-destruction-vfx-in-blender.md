---
title: Superhero Landing Tutorial 02 | Ground Destruction VFX in Blender
source: YouTube
url: https://www.youtube.com/watch?v=4ULxB4PzbAc
author: Graphical Ninja
ingested: 2026-05-18
blender_version: "Not specified"
tags: ["rigid-body", "simulation", "particles", "smoke-fire", "animation", "rendering", "compositing", "advanced"]
extraction_status: complete
frames_dir: tutorials/frames/superhero-landing-tutorial-02-ground-destruction-vfx-in-blender/
frame_count: 0
---

# Superhero Landing Tutorial 02 | Ground Destruction VFX in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=4ULxB4PzbAc)
**Author:** Graphical Ninja
**Duration:** 23m13s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Welcome to part 2 of my super hero landing tutorial.  In this part I'll show you how to do the ground brake effects with a rigid body simulation.  Add some extra rock chunks with particle system and add a smoke sim for dust trails.


### Ground Fracture [0:34]
**Transcript:** First I'm going to add another plane and scale it up.  Then I'm going to move it up about 5 or 6 inches and this will be our road surface.  I'm going to cut out a smaller chunk in the middle for the part of the ground that's going to break.  If we tab it in edit mode, do a couple cuts here and then make that about so.  Just make sure that he's centered in there.  Now we're just going to select this center face, hit P and separate by selection.  This will be the part that breaks.  Let's move it into a new collection called ground brake.  Then we need to add some more geometry to this.  Let's tab it to edit mode, control R, and then we'll cut it into smaller chunks.  Somewhere around here looks good and then we'll cut it the other way to get some square chunks.  Then I just want to grab random faces and move them around.  These aren't all even.  Just don't move the edge faces.  Now that we've somewhat randomized this, let's select the whole thing and then extrude it downwards to the actual ground plane.  Now we have some geometry to work with.  I want to hide everything except this for now.  We'll call this fracture and then we're going to start fracturing this.  Search fracture and ...


### Rigid Body Sim [3:08]
**Transcript:** Next let's do a rigid body simulation to make these chunks fly upward and outward as he lands.  We want to speed ramp it so it ends up being slow mo in the end.  So let's add a force field, force and move it a bit below the ground.  So let's add a force field, force and move it a bit below the ground.  Now select one of these chunks, turn it into a rigid body, it'll be active, dynamic and then we'll select all of our ground brake objects.  Go to object, rigid body, copy from active and now they will all have the same settings.  Now let's go to the scene properties tab, rigid body world and set this up.  First we need more steps per frame for higher quality so we'll do 20 and 20.  Then we're going to go into cache and our simulation start should be 50 and the end should be 100.  Now we want to speed ramp the speed of the simulation.  So if we go to frame 53 hit I on speed and then go three frames forward and set speed to 0.25 hit I again.  Now for the rest of the sim it'll be quarter speed.  Now our chunks are all just falling through the ground right now.  So if we grab our original ground mesh, let's make that a rigid body passive object.  Now we need the force to be a little bit stronger.  Well, a lot stronger.  So let's find the frame on which he l...


### Particle System (Dirt) [6:33]
**Transcript:** So select one of your chunks, go to the particle settings and make a new particle system.  We will call it dirt.  Dirt chunks.  Make the number 2,000 frame start will be 50 frame end will be 200 lifetime will be 50.  And then let's go to rotation.  We want to turn on rotation so it'll randomly rotate and then turn angular velocity to random and make the amount 5.  We'll make the phase 1 on all of these so it'll randomly rotate them at the start and then randomize phase.  Just turn that up and then turn randomize up as well.  Alright, let's set up our physics settings.  We want to have a little bit of random motion which would be brownie in.  So let's turn that to 0.1 and we'll turn damping to 0.05.  We don't want the force to affect it so let's turn all on force to 0.  Let's turn gravity to 0.05 so they sort of just hang in the air.  Now let's see what this is going to do.  As you can see there's a bunch of particles coming off.  Make a new collection, call it rocks.  Make sure that's active.  And then in bridge I'm just going to grab this small stones pack.  I'm going to get exports and it should put it into that collection.  Now let's go to these rocks.  They're a little higher p...


### Smoke Sim (Dust) [11:01]
**Transcript:** Make a cube and then we'll go to physics properties, fluid, and make it a domain.  Now let's make it encompass the entire area tab into edit mode and scale it up.  To look covers that whole area.  Move it up.  And then we'll grab the top.  Move that down.  Let's set up our settings for this.  Let's do a resolution divisions of 128.  Time scale of .25.  So it's slow-mo.  Let's turn our CFL number to 10.  This will speed up the simulation.  And then we're going to use adaptive time steps maximum of three.  For my final resolution, I'm going to go to 256 divisions.  Let's turn on adaptive domain.  And then we're going to go to dissolve, turn that on.  And set it to 25.  Type should be modular so you can resume it.  And then let's go to field weights.  And we'll turn all to zero because once again we don't want the force affecting the smoke.  Then we'll just set the start and end of our cache which will be 50 and 100.  Now let's set up our chunks to emits smoke.  So grab one of the chunks.  Add a fluid to it.  Set it to flow.  The type will be in flow.  And then sampling subsets will be one.  Then we'll go into flow source.  Set the surface emission to .2.  And then we want to turn on ...


### Chunk materials and Displacement [14:43]
**Transcript:** So let's hide our domain.  And then zoom in on one of these larger chunks.  I'm just going to reuse the dry cracked material that we used for the ground.  I'm going to select all my objects, link materials.  Now we've got some texture, but these edges are really sharp and straight.  And one way to fix that is to add a displacement modifier.  So in Modifiers tab, add a displacement.  And then we will add a new texture.  Toggle over there, we'll make it a Voronoi texture.  Default settings are good.  We go back to Modifiers.  We can adjust the strength to something like .25.  And then we want it to go in the X direction.  So it's just pushing it left and right.  Let's turn that on and off and see how that's working.  And that just breaks up the straight edges.  To give it a little more detail, we can add a subdivision surface modifier.  Move that above the displacement modifier and then make it simple.  So it doesn't round things off.  Now let's copy, let's duplicate our displacement modifier and set it to  Displace in the Y direction.  We'll click, I'm going to move our smoke domain into a new collection.  So that's not in there.  And then let's select all our objects.  Select the o...


### Final Comp [20:56]
**Transcript:** Let's play that back.  Obviously there's a few changes I could do.  Somehow he's all the way in shadow probably because these chunks are blocking the light.  So I'd want to adjust the light or move the chunks so he still gets lit.  And then I noticed that there's a bunch of chunks, a bunch of rocks that fall through the ground at the beginning of the shot.  You can fix that just by starting your particle system a couple frames later.  So they only start getting emitted from these chunks once they've started moving.  Adding this into your comp should be as easy as swapping it out with your ground render.  If you hit control shift as you drag it over, it should swap the plates.  And then just shift X to switch, meaning you're putting the ground on top now.  Because you've got the cut out.  Try switching this to a disjoint over.  And that should get some of the rid of some of those bright edges.  Finally, I'd like to add some grain.  And then let's turn the size down a little bit on all three of these.  Just leave the blue bigger though.  And then we'll turn the intensity down as well.  And then I don't like how much grain is in the highlights. That's not natural.  So make a chemix no...



---

## Structured Notes

### Core Technique
Ground-destruction VFX combining manual ground fracture + Cell Fracture rigid body simulation (with a Force Field strength keyframed at the landing moment for slow-motion chunks at 0.25×), a 2000-particle dirt/rock Collection emitter, a smoke simulation for dust trails at Resolution 128–256, and final Blender compositor compositing with Disjoint Over merge and film grain.

### Summary
Graphical Ninja builds a superhero landing ground-destruction shot in three simulation layers. First, a road plane is manually cut (Ctrl+R, separate by selection), then fractured using the Cell Fracture add-on into angular chunks. A Force Field (below ground) and Rigid Body simulation blow the chunks upward/outward when the superhero lands; a Speed keyframe at frame 53 sets the sim to 0.25× (slow motion) for dramatic effect. Passive rigid body on the undamaged ground keeps chunks from falling through. A particle system (2000 dirt chunks from a rock Collection) emits from the chunks with low gravity (0.05) for hanging debris. A smoke (fluid) domain with Resolution 128–256, Time Scale 0.25, and Dissolve: 25 creates the dust cloud; each chunk is a Flow emitter with Surface Emission: 0.2. Rock chunks get a Voronoi Displacement modifier plus Subdivision Surface (Simple mode) for jagged edges. Final composite in Blender's compositor uses Disjoint Over to merge layers and a Grain node for film texture.

### Key Steps
1. Add a ground Plane → in Edit Mode: **Ctrl+R** to cut the center section → **P → Separate by Selection** to isolate the breakable chunk
2. Add the **Cell Fracture** add-on (built-in, enable in Preferences) → select the breakable chunk → **Object → Quick Effects → Cell Fracture** → Source: Volume, Source Limit: 50–100 shards
3. Move all fracture pieces to a "ground brake" collection → select one chunk → **Physics → Rigid Body → Active, Dynamic** → Object → Rigid Body → **Copy from Active** to all chunks
4. Add **Force Field** (Wind or Turbulence type) below ground → set Strength: 0 → go to frame 53 (landing frame) → **I on Strength** → go to frame 56 → **Strength: 5000–10000** → **I** → back to 0 at frame 60 for the burst
5. **Rigid Body World** → Steps Per Second: 20; Solver Iterations: 20; Cache Start: 50; End: 100
6. Speed ramp: frame 53 → **I on Scene Speed (1.0)** → frame 56 → Speed: 0.25 → **I** (quarter speed for rest of sim)
7. Select original ground mesh → **Rigid Body → Passive** for collision boundary
8. Add particle system to one chunk: Number: 2000; Frame Start: 52; End: 200; Lifetime: 50; Rotation: on; Brownian: 0.1; Damping: 0.05; Gravity: 0.05; Force: 0 → Render as: **Collection** (rocks collection)
9. For dust: add **Cube** → **Physics → Fluid → Domain**; Type: Gas (Smoke); Resolution: 128 (256 final); Time Scale: 0.25; CFL: 10; Adaptive Time Steps Max: 3; Dissolve: 25, Modular cache
10. Select each chunk → **Physics → Fluid → Flow** → Type: Inflow; Surface Emission: 0.2; Smoke Flow: on
11. Add **Displacement modifier** to chunks: Texture: Voronoi, Strength: 0.25, X direction; add **Subdivision Surface** (Simple) above displacement for jagged cracked edges
12. In Compositor: Render Layers → use **Disjoint Over** (not regular Over) to merge simulation layers with hero plate; add **Grain** node, reduce intensity in highlights

### Nodes / Settings
- Cell Fracture add-on — Source: Volume; Source Limit: 50–100; Noise: 0.1 for irregular shapes
- Rigid Body (chunks) — Active, Dynamic; Steps Per Second: 20; Solver Iterations: 20
- Force Field — type: Force; Strength keyframed: 0 (frame 50), peak value (frame 53–56), 0 (frame 60)
- Speed keyframe — Scene Properties → Rigid Body World → Cache → Speed; 1.0 → 0.25 at frame 56
- Particle system (dirt) — Number: 2000; Lifetime: 50; Brownian: 0.1; Damping: 0.05; Gravity: 0.05; Force: 0; Collection render
- Smoke Domain — Resolution: 128 (viewport) / 256 (final); Time Scale: 0.25; CFL: 10; Dissolve: 25, Modular; Field Weights All: 0
- Smoke Flow — Type: Inflow; Surface Emission: 0.2; Temperature Diff: 1.0
- Displacement modifier — Texture: Voronoi; Strength: 0.25; Direction: X (then Y duplicate)
- Subdivision Surface (Simple) — above Displacement; Levels: 2; Simple mode (no smoothing)
- Compositor — Disjoint Over for layer merge; Grain node: Size 0.5 (RGB separate, Blue larger); Intensity: 0.02–0.05

### Difficulty
Advanced

### Blender Version
Not specified

### Tags
#rigid-body #simulation #particles #smoke-fire #animation #rendering #compositing #advanced

---

## Related Tutorials
- [Blender Tutorial - Control Physics Sims with Geometry Nodes (Beginner Friendly)](./blender-tutorial-control-physics-sims-with-geometry-nodes-be.md)
- [I Recreated movie scene in Blender & Nuke | Complete Tutorial](./i-recreated-movie-scene-in-blender-nuke-complete-tutorial.md)
- [Using Geometry Nodes for VFX in Blender](./using-geometry-nodes-for-vfx-in-blender.md)
- [A FULL Blender Compositor Course!](./a-full-blender-compositor-course.md)
