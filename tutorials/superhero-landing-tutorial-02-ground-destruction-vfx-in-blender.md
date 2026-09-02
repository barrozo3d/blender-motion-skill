---
title: Superhero Landing Tutorial 02 | Ground Destruction VFX in Blender
source: YouTube
url: https://www.youtube.com/watch?v=4ULxB4PzbAc
author: Graphical Ninja
ingested: 2026-06-25
blender_version: "Blender 3.3.1 -- observed in frame_000 through frame_004"
tags: [vfx, rigid-body, particles, fluid-sim, destruction, compositing, nuke, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/superhero-landing-tutorial-02-ground-destruction-vfx-in-blender/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
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
**Transcript:** First I'm going to add another plane and scale it up.  Then I'm going to move it up about 5 or 6 inches and this will be our road surface.  I'm going to cut out a smaller chunk in the middle for the part of the ground that's going to break.  If we tab it in edit mode, do a couple cuts here and then make that about so.  Just make sure that he's centered in there.  Now we're just going to select this center face, hit P and separate by selection.  This will be the part that breaks.  Let's move it into a new collection called ground brake.  Then we need to add some more geometry to this.  Let's tab it to edit mode, control R, and then we'll cut it into smaller chunks.  Somewhere around here looks good and then we'll cut it the other way to get some square chunks.  Then I just want to grab random faces and move them around.  These aren't all even.  Just don't move the edge faces.  Now that we've somewhat randomized this, let's select the whole thing and then extrude it downwards to the actual ground plane.  Now we have some geometry to work with.  I want to hide everything except this for now.  We'll call this fracture and then we're going to start fracturing this.  Search fracture and you'll find a cell fracture.  Then we're going to use the point source, we'll be ownverts.  We'll add a recursive fracture of two, cursor close.  We should be good to go.  Now let's just watch this fracture and watch it recursively fracture the center ones.  Let's just drop these into our ground brake collection and our first fracture object we can delete.


### Rigid Body Sim [3:08]
**Transcript:** Next let's do a rigid body simulation to make these chunks fly upward and outward as he lands.  We want to speed ramp it so it ends up being slow mo in the end.  So let's add a force field, force and move it a bit below the ground.  Now select one of these chunks, turn it into a rigid body, it'll be active, dynamic and then we'll select all of our ground brake objects.  Go to object, rigid body, copy from active and now they will all have the same settings.  Now let's go to the scene properties tab, rigid body world and set this up.  First we need more steps per frame for higher quality so we'll do 20 and 20.  Then we're going to go into cache and our simulation start should be 50 and the end should be 100.  Now we want to speed ramp the speed of the simulation.  So if we go to frame 53 hit I on speed and then go three frames forward and set speed to 0.25 hit I again.  Now for the rest of the sim it'll be quarter speed.  Now our chunks are all just falling through the ground right now.  So if we grab our original ground mesh, let's make that a rigid body passive object.  Now we need the force to be a little bit stronger.  Well, a lot stronger.  So let's find the frame on which he lands which is frame 50 and on this frame we want the strength to be way higher.  So let's try like 100,000 set of key frame on there and then we'll see what that does.  Whoa, that did a lot.  And we want this force to only happen for like two frames.  So on frame 52 let's make the strength is zero.  And then we'll see how that works too much.  Let's make the strength 10,000.  That's better.  And we want some fall off so the outer pieces don't get thrown as far.  We can do that with this fall off option.  If we turn the power to one, that'll give us a lot more fall off around the edges.  And that's starting to look a lot cooler.  We've got this one chunk that's flying right up in front of the camera.  And we can just go ahead and delete some of these.  So let's delete any chunks that might fly in front of the camera.  Next, let's do the particle system to add a bunch of little rocks or dirt to trail behind these chunks.


### Particle System (Dirt) [6:33]
**Transcript:** So select one of your chunks, go to the particle settings and make a new particle system.  We will call it dirt.  Dirt chunks.  Make the number 2,000 frame start will be 50 frame end will be 200 lifetime will be 50.  And then let's go to rotation.  We want to turn on rotation so it'll randomly rotate and then turn angular velocity to random and make the amount 5.  We'll make the phase 1 on all of these so it'll randomly rotate them at the start and then randomize phase.  Just turn that up and then turn randomize up as well.  Alright, let's set up our physics settings.  We want to have a little bit of random motion which would be brownie in.  So let's turn that to 0.1 and we'll turn damping to 0.05.  We don't want the force to affect it so let's turn all on force to 0.  Let's turn gravity to 0.05 so they sort of just hang in the air.  Now let's see what this is going to do.  As you can see there's a bunch of particles coming off.  Make a new collection, call it rocks.  Make sure that's active.  And then in bridge I'm just going to grab this small stones pack.  I'm going to get exports and it should put it into that collection.  Now let's go to these rocks.  They're a little higher poly than I would want.  So let's select them all.  Go to the modifiers to have an add a decimate modifier.  Race you to 0.1 and then we'll just copy to selected.  And then we will apply this modifier.  Let's go into our particle system settings and where it says render.  Instead of halo make it collection and select your rocks collection.  Pick random.  And as you can see it's also scattering a bunch of random empties  because they're all parented to this empty empty.  So just select your rocks, alt p, clear parent, keep transformation  and then delete this empty.  Let's make them a little bit bigger.  Scale 0.05 maybe 0.1 and then scale randomness like 0.8.  Maybe they can be like 0.2.  One thing I want to turn off is the normal velocity.  So if we go up to velocity, turn normal to 0 because it's spraying the rocks out.  And then we want our object velocity.  We want to inherit the object's motion.  So turn the object velocity to 0.5.  And then randomize it by 0.25.  Now we should get something where the rocks follow along.  Now we need to instance these particles to every object here.  And it's going to get a little heavy.  So save your file.  And all we want to do is go to our ground break collection.  Select all the objects.  Go to the modifier tab.  And then on the drop down, copy 2 selected in the particle system modifier.  And all we need to do is bake this out.  And we should get rocks trailing from every chunk.  Go to cache and then bake all dynamics.  It's a bit heavy to display.  So you can go to viewport display and turn the amount down to like 5%.  Next, let's add some dust trailing behind all these chunks to really fill it in and give it that last bit of realism.


### Smoke Sim (Dust) [11:01]
**Transcript:** Make a cube and then we'll go to physics properties, fluid, and make it a domain.  Now let's make it encompass the entire area tab into edit mode and scale it up.  To look covers that whole area.  Move it up.  And then we'll grab the top.  Move that down.  Let's set up our settings for this.  Let's do a resolution divisions of 128.  Time scale of .25.  So it's slow-mo.  Let's turn our CFL number to 10.  This will speed up the simulation.  And then we're going to use adaptive time steps maximum of three.  For my final resolution, I'm going to go to 256 divisions.  Let's turn on adaptive domain.  And then we're going to go to dissolve, turn that on.  And set it to 25.  Type should be modular so you can resume it.  And then let's go to field weights.  And we'll turn all to zero because once again we don't want the force affecting the smoke.  Then we'll just set the start and end of our cache which will be 50 and 100.  Now let's set up our chunks to emits smoke.  So grab one of the chunks.  Add a fluid to it.  Set it to flow.  The type will be in flow.  And then sampling subsets will be one.  Then we'll go into flow source.  Set the surface emission to .2.  And then we want to turn on initial velocity, make that value .25.  Then we'll do the same thing we did for our particle systems.  So select all the ground break objects.  D select the domain because it ended up in there.  Make that object active.  And then go into the modifier panel.  In the fluid modifier, copy to selected.  Now all these objects should have the same settings.  Now if we go back to our domain, go to this and save and then bake data.  Next, let's tweak the material for our dust.  So go to the shading tab, go into rendered mode.  And let's make a new material on our domain.  Instead of principled BSDF, it should be principled volume.  Plug that into the volume input.  And now we should see our dust.  That's not too bad.  If you want a little more density, just turn that up to 2.  Remember you can turn up the resolution of your simulation to 256  for some more detail.  Instead of gray, let's make this just a little bit brownish.  And then turn the brightness down to about halfway.  Now it's time to do the material for our chunks.


### Chunk materials and Displacement [14:43]
**Transcript:** So let's hide our domain.  And then zoom in on one of these larger chunks.  I'm just going to reuse the dry cracked material that we used for the ground.  I'm going to select all my objects, link materials.  Now we've got some texture, but these edges are really sharp and straight.  And one way to fix that is to add a displacement modifier.  So in Modifiers tab, add a displacement.  And then we will add a new texture.  Toggle over there, we'll make it a Voronoi texture.  Default settings are good.  We go back to Modifiers.  We can adjust the strength to something like .25.  And then we want it to go in the X direction.  So it's just pushing it left and right.  Let's turn that on and off and see how that's working.  And that just breaks up the straight edges.  To give it a little more detail, we can add a subdivision surface modifier.  Move that above the displacement modifier and then make it simple.  So it doesn't round things off.  Now let's copy, let's duplicate our displacement modifier and set it to  Displace in the Y direction.  We'll click, I'm going to move our smoke domain into a new collection.  So that's not in there.  And then let's select all our objects.  Select the one that we added the modifier to.  And then we'll copy our subdivision modifier.  First, let's turn render resolution to one.  Copy our subdivision modifier to selected.  And then copy our displacement textures to select it as well.  We can add even more detail to these with actual render time displacement.  So let's select one of our chunks again.  Add another subdivision surface modifier at the very end.  Turn on simple, adaptive subdivision.  You should see that we have some displacement.  And then let's select all of our ground break objects and then copy to selected with that modifier as well.  Lastly, I want to add a material to this plane, find road, export that.  And then we will apply that to our road.  Let's make the usual tweaks.  Let's just turn our mid-level displacement to 0.5 so it doesn't push it upwards.  And then we want to adjust our scale to something smaller.  And then let's turn our clear coat off and plug the roughness texture into the roughness map.  Because it goes the wrong one.  Let's tweak our lighting on this.  These chunks got really dark and I think I just darken this texture a little too much.  So let's brighten that texture up.  Now let's darken the road to match.  RGB curves.  Drop them into the diffuse color and just pull the brightness of the road a little bit down.  And we can also tweak the specular.  Now the brightness of those things matches.  Let's go into camera view.  And I think what we want to do is just crank up the value of some of our lights.  So let's go to our first area light.  Make that twice as bright.  And then the opposite light is kind of missing too.  So let's grab that.  Turn it up to twice as bright as well.  And then let's just go ahead and turn up our sky texture to twice as bright as well.  Now we go more fill light.  One more final thing I want to do is fix the edge here where you can just see a plane that's above the rest of it.  And we can do that by just making some of these objects inactive around the edges.  So let's just select the edge objects.  And then go into physics settings down to the rigid body settings.  And turn this from active to passive.  And then go into object, rigid body, copy from active.  Now these should act as colliders, but not move.  And then you should have a nice broken up edge around your cracked ground area.  The final thing we need to do is add our plate as a cutout for all this effect stuff.  So if you go to your plate collection, turn that on.  And then right click, view layer, set hold out.  And then you may have to update some of these view layer settings.  For instance, this is the plate render pass.  So we don't want any of these other things in it.  And then if we go to the did you render pass, we also don't want any ground break, rocks, or smoke in it.  But we do want the ground as indirect.  All right, with all that updated, all you need to do is hit render animation and let that go.  My pass just finished rendering and I'm back in nuke.


### Final Comp [20:56]
**Transcript:** Let's play that back.  Obviously there's a few changes I could do.  Somehow he's all the way in shadow probably because these chunks are blocking the light.  So I'd want to adjust the light or move the chunks so he still gets lit.  And then I noticed that there's a bunch of chunks, a bunch of rocks that fall through the ground at the beginning of the shot.  You can fix that just by starting your particle system a couple frames later.  So they only start getting emitted from these chunks once they've started moving.  Adding this into your comp should be as easy as swapping it out with your ground render.  If you hit control shift as you drag it over, it should swap the plates.  And then just shift X to switch, meaning you're putting the ground on top now.  Because you've got the cut out.  Try switching this to a disjoint over.  And that should get some of the rid of some of those bright edges.  Finally, I'd like to add some grain.  And then let's turn the size down a little bit on all three of these.  Just leave the blue bigger though.  And then we'll turn the intensity down as well.  And then I don't like how much grain is in the highlights. That's not natural.  So make a chemix node.  A will be grain, B will be no grain, make a cure.  And then switch the chemix.  So that way the darker areas of the image will be grained and the brighter areas will not.  I think I can turn my grain amount back up a little bit.  And then you can play with the slider to reduce the amount of grain in the highlights.  That's it for this tutorial series.  I hope you enjoyed it and learned a few things.  And let me know what kind of tutorials you'd like to see in the future.



---

## Captured Frames

- [1:30] tutorials/frames/superhero-landing-tutorial-02-ground-destruction-vfx-in-blender/frame_000.jpg
- [4:30] tutorials/frames/superhero-landing-tutorial-02-ground-destruction-vfx-in-blender/frame_001.jpg
- [8:00] tutorials/frames/superhero-landing-tutorial-02-ground-destruction-vfx-in-blender/frame_002.jpg
- [12:30] tutorials/frames/superhero-landing-tutorial-02-ground-destruction-vfx-in-blender/frame_003.jpg
- [16:30] tutorials/frames/superhero-landing-tutorial-02-ground-destruction-vfx-in-blender/frame_004.jpg
- [21:30] tutorials/frames/superhero-landing-tutorial-02-ground-destruction-vfx-in-blender/frame_005.jpg

---

## Structured Notes

### Core Technique
Full superhero ground-break VFX pipeline: Cell Fracture add-on to shatter road surface → Rigid Body simulation with Force Field (speed ramp to slow-mo) → particle system dirt/rock chunks (collection render, Brownian motion, inherited velocity) → Mantaflow smoke sim for dust trails → Voronoi displacement on chunk materials → Nuke comp with Holdout render pass and grain.

### Summary
Graphical Ninja builds a ground destruction VFX effect for a superhero landing. Road plane is cut via Loop Cuts → separated center face → Cell Fracture (ownverts point source, recursive 2) to shatter into chunks. Rigid Body sim: force field (strength 100,000 for 2 frames at landing, falloff power 1 for edge distance) with speed ramp (frame 53 = speed 1, frame 56 = speed 0.25 = slow-mo). Passive rigid body edges prevent floating chunks. Particle system (2,000 particles per chunk, lifetime 50, Brownian 0.1, inherited velocity 0.5, rock collection from Bridge asset library, decimate 0.1) baked and copied to all chunks. Mantaflow smoke domain (128→256 resolution, time scale 0.25, CFL 10, adaptive domain, dissolve 25 modular) emitting from all chunk surfaces (flow type Inflow, surface emission 0.2, initial velocity 0.25). Chunk material: dry cracked texture + Voronoi displacement modifier (strength 0.25, X and Y) + Subdivision Surface (Simple) before displacement + adaptive subdivision at render time. Road: BlenderKit material with clearcoat OFF + roughness plugged correctly. Nuke comp: Holdout render pass for character cutout; swap plate with Ctrl+Shift drag; Disjoint Over for edge cleanup; grain node with Chemix mask (dark areas grain only).

### Key Steps
1. **Ground setup:** Add plane, scale up, raise 5-6 units. Loop cuts to isolate center section. Select center face → P → Separate by Selection → move to "ground brake" collection.
2. **Cell Fracture:** Tab into ground piece, more loop cuts to subdivide. Select outer faces, move for variety. Extrude piece downward. Select all → Cell Fracture (search): Point Source = OwnVerts; Recursive 2; Cursor Close. Apply. Delete original unshattered object.
3. **Rigid Body sim:** Select one chunk → Object Properties → Rigid Body (Active, Dynamic). Select all → Object → Rigid Body → Copy from Active. Scene Properties → Rigid Body World [frame_001]: `Collection` **RigidBodyWorld**, `Substeps Per Frame` **20**, `Solver Iterations` **20**, Cache `Simulation Start` **50** / `End` **100** — all confirmed.
    ⚠️ **"Split Impulse = 20" was a misreading.** `Split Impulse` is a **checkbox**, and it is **unticked**; the second 20 belongs to `Solver Iterations`, the field beneath it.
4. **Speed ramp:** Frame 53 → RB World Speed = 1 → I. Frame 56 → Speed = 0.25 → I.
5. **Force field:** Shift+A → Force Field → Force. Move below ground. A `Force` object does appear in the outliner from 8:00 onward [frame_002, frame_003], so the step happened — but **no force-field properties panel is captured in this set**, so its strength is unverified.
    ⚠️ **The entry disagrees with itself about that strength**: the Summary says **100,000** and this Key Step says **10,000**. Nothing in the frames settles it, so both readings are left standing and flagged rather than one being silently chosen. Fall Off Power = 1 (distance-based dropoff) is likewise narrated only.
6. **Ground plane passive RB:** Select original road plane → Rigid Body → Passive. Prevents chunks falling through.
7. **Particle system (rocks):** Select one chunk → Particle Properties → New ("dirt chunks"). Number 2000; Start 50, End 200; Lifetime 50. Rotation ON; Angular Velocity = Random, Amount 5; Phase 1 all; randomize phase+amount. Physics: Brownian 0.1; Damping 0.05; Force Fields → All = 0; Gravity = 0.05. Render: Collection → rocks collection; Pick Random; Scale 0.2 (or 0.1); Scale Randomness 0.8. Velocity: Normal = 0; Object = 0.5; Randomize 0.25.
8. **Copy particles:** Select all ground brake objects → modifier tab → particle system modifier drop-down → Copy to Selected. Bake All Dynamics.
9. **Smoke domain:** Add cube → Physics → Fluid → Domain. Edit mode: scale up to cover scene, move up, lower top. Settings: Resolution 128 (→256 final); Time Scale 0.25; CFL 10; Adaptive Time Steps max 3; Adaptive Domain ON; `Dissolve` **✓** with `Time` **25** and **`Slow` ✓** (a checkbox the entry omitted) [frame_003].
    ⚠️ **Two errors here.** "Modular" is not part of Dissolve — it is the **Cache `Type`**, further down the panel. And the smoke cache does **not** run 50–100: it reads `Frame Start` **1**, `End` **250**, `Offset` 0, `Is Resumable` ✓, `Format Volumes` **OpenVDB**, in a directory named `cache_fluid_4b85f272_v02`. ⚠️ **`Field Weights` are not all 0** either — Gravity, Force, Vortex, Magnetic and Harmonic all read **1.000** [frame_003]. Also visible: `Heat` 1.00000, `Vorticity` 0.000. Bake Data.
10. **Smoke flow (chunks):** Select one chunk → Fluid → Flow. Type = Inflow. Sampling Subsets = 1. Flow Source: Surface Emission = 0.2; Initial Velocity ON, Value 0.25. Copy Fluid modifier to all ground brake objects.
11. **Smoke material:** Select domain → Shading → New material. Replace Principled BSDF with Principled Volume → plug into Volume input. Density ~2. Color: brownish. Brightness ~50%.
12. **Chunk materials:** Link the `Dry_Cracked_…` material to all chunks. The modifier stack is captured in full on `Fracture_cell.006` [frame_004], top to bottom: **`Dirt chunks`** (the particle system, named exactly as Key Step 7 says), **`Fluid`**, **`Subdivision`**, **`Displace`** — confirming Subdivision sits *before* Displace as the step requires.
    - `Subdivision`: **Simple** ✓, `Levels Viewport` **1**, `Render` **2** (the Nodes/Settings list below said Render 1), `Optimal Display` ✓.
    - `Displace`: `Coordinates` **Local**, `Direction` **X** ✓, `Space` Local, `Strength` **0.250** ✓, on a texture shared by 2 users.
    Duplicate Displacement → set Direction Y. Copy all modifiers to all chunks.
13. **Render/Comp:** Set up render passes with Holdout for character plate. **The comp application is NukeX**, not plain Nuke [frame_005] — script `SuperheroLandingTutorial_v003.nkx`. The `Read13` node reads `SuperheroLandingTutorial_v006_Ground_%04d.exr` at `Format` **HD_1080 1920x1080**, `Frame Range` **25–100** (`hold` at both ends), `Original Range` 25–100, `Input Transform` default (linear) — a **19-channel** EXR. That 25–100 is the same range Blender's timeline carries [frame_000], which is a useful cross-check that the plate and the sim line up. Ctrl+Shift drag to swap plates; Disjoint Over to fix edges; Grain node + Chemix. *(The swap, Disjoint Over and grain operations themselves are narrated — the captured node graph is zoomed out past readability.)*

### Nodes / Settings
- Cell Fracture: OwnVerts; Recursive 2; Cursor Close
- RB World: `Substeps Per Frame` **20**, `Solver Iterations` **20**, `Split Impulse` **unticked** (not "20"), Cache 50–100 [frame_001]
- Speed ramp confirmed on both ends: **1.000** at frame 53 [frame_001] and **0.250** at frame 70 [frame_002], the field keyframe-highlighted in both
- Force: strength **unverified** — the entry says 10,000 here and **100,000** in its Summary, and no force-field panel appears in any frame. A `Force` object is present in the outliner from 8:00 [frame_002]
- Particle: 2,000 count; Brownian 0.1; Object velocity 0.5; Normal 0; Scale 0.2; Randomness 0.8
- Smoke Domain: Resolution 128/256; Time Scale 0.25; CFL 10; Dissolve 25 Modular
- Flow: Surface Emission 0.2; Initial Velocity 0.25
- Displace: `Coordinates` **Local**, `Direction` **X**, `Space` Local, `Strength` **0.250** ✓ [frame_004]; X then Y as separate modifiers
- Modifier order on a chunk: `Dirt chunks` → `Fluid` → `Subdivision` → `Displace` [frame_004]
- Smoke cache: `Frame Start` **1**, `End` **250**, Type **Modular**, Is Resumable ✓, **OpenVDB** [frame_003] — not the 50–100 recorded
- Field Weights: Gravity / Force / Vortex / Magnetic / Harmonic all **1.000**, not 0 [frame_003]
- Rocks collection: six Quixel/Bridge assets, `Asset_nature_rock_S_vdkja3tw_00_LOD0` … `_05_LOD0` [frame_003]
- Comp: **NukeX**, HD_1080, frame range 25–100, 19-channel EXR [frame_005]
- Subdivision Surface: **Simple** ✓; `Levels Viewport` 1, **`Render` 2**, Optimal Display ✓ [frame_004]

### Difficulty
Intermediate — multi-system VFX pipeline; requires Cell Fracture add-on + Mantaflow; good real-world production workflow

### Blender Version
**Blender 3.3.1** — status bar, five frames [frame_000 … frame_004]. The recorded `3.x/4.x` can be narrowed further than the frames alone would allow: the Windows taskbar clock in the same captures reads **2/4/2023** and **2/5/2023** [frame_000, frame_005], which places the session in the 3.3 LTS period and rules out 4.x entirely — 4.0 did not ship until November 2023.

### Tags
#vfx #rigid-body #particles #fluid-sim #destruction #compositing #nuke #intermediate

---

## Frame verification (2026-09-02)

| | |
|---|---|
| **Corrected** | `blender_version` `3.x/4.x` → **3.3.1**. `Split Impulse` is an unticked **checkbox**, not a value of 20 — the second 20 is `Solver Iterations` [frame_001]. The smoke cache runs **1–250**, not 50–100, and **"Modular" is the cache `Type`**, not part of Dissolve [frame_003]. `Field Weights` are all **1.000**, not 0 [frame_003]. Subdivision `Render` is **2**, not 1 [frame_004]. The texture node is **Voronoi** — "Voronoid" again, the same transcription artifact corrected in `real-time-caustics-in-blender-51.md`. The comp is **NukeX** [frame_005]. |
| **Confirmed** | the speed ramp, on both ends — **1.000** at frame 53 and **0.250** at frame 70, keyframe-highlighted [frame_001, frame_002]. Substeps 20, Solver 20, RB cache 50–100. Displace `Strength` **0.250** and `Direction X`, Subdivision **Simple** sitting before it, and the particle system named `Dirt chunks` [frame_004]. `Dissolve` `Time` 25. The Cell Fracture recursion is legible straight off the outliner: `Fracture_cell.016` spawns `Fracture_cell.016.cell`, `.cell.001 … .007` — which is what Recursive 2 produces [frame_001]. |
| **Added** | the scene's frame range (**Start 25 / End 100**) which the entry never carried [frame_000]; `Slow` ✓ on Dissolve, `Heat` 1.0, `Vorticity` 0.0, `Is Resumable`, OpenVDB and the cache directory name [frame_003]; the six Bridge rock assets by name [frame_003]; the full modifier order on a chunk; and the NukeX read — HD_1080, 19 channels, `Frame Range` 25–100 matching Blender's [frame_005]. |
| **Flagged as unverified** | the **force-field strength**, deliberately (see below); Cell Fracture's OwnVerts/Recursive 2 dialogue; every particle-system numeric (2,000 count, Brownian 0.1, velocities, scale); the smoke flow settings (Inflow, surface emission 0.2, initial velocity 0.25); the Principled Volume smoke material; and the Nuke operations themselves — the captured node graph is zoomed out past readability. |

⚠️ **An internal contradiction the frames could not settle.** The Summary says
the force field runs at **100,000** for two frames; Key Step 5 says **10,000**.
A `Force` object is in the outliner from 8:00, so the step is real, but no
force-field properties panel appears in any of the six frames. **Both numbers
are left in place and labelled**, rather than one being quietly picked — a
10× difference in the value that drives the entire destruction sim is exactly
the kind of thing a reader needs told, not guessed at.

ℹ️ **The desktop dated the build.** These captures include the Windows taskbar,
whose clock reads 2/4/2023 and 2/5/2023. That independently corroborates 3.3.1
and rules out the `4.x` half of the old version field, since 4.0 shipped nine
months later. **Where a capture includes OS chrome, the clock is a second,
independent witness to the version** — worth remembering for entries whose
status bar is cropped or obscured.

---

## Related Tutorials
- `using-geometry-nodes-for-vfx-in-blender.md` — GeoNodes VFX approach comparison
- `realistic-cloth-physics-in-blender-full-tutorial.md` — physics simulation workflow (cloth)
- `mastering-blenders-graph-editor.md` — speed ramp / F-curve techniques
