---
title: Superhero Landing Tutorial 02 | Ground Destruction VFX in Blender
source: YouTube
url: https://www.youtube.com/watch?v=4ULxB4PzbAc
author: Graphical Ninja
ingested: 2026-05-18
blender_version: "[PENDING]"
tags: []
extraction_status: pending
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
**Transcript:** Next let's do a rigid body simulation to make these chunks fly upward and outward as he lands.  We want to speed ramp it so it ends up being slow mo in the end.  So let's add a force field, force and move it a bit below the ground.  Now select one of these chunks, turn it into a rigid body, it'll be active, dynamic and then we'll select all of our ground brake objects.  Go to object, rigid body, copy from active and now they will all have the same settings.  Now let's go to the scene properties tab, rigid body world and set this up.  First we need more steps per frame for higher quality so we'll do 20 and 20.  Then we're going to go into cache and our simulation start should be 50 and the end should be 100.  Now we want to speed ramp the speed of the simulation.  So if we go to frame 53 hit I on speed and then go three frames forward and set speed to 0.25 hit I again.  Now for the rest of the sim it'll be quarter speed.  Now our chunks are all just falling through the ground right now.  So if we grab our original ground mesh, let's make that a rigid body passive object.  Now we need the force to be a little bit stronger.  Well, a lot stronger.  So let's find the frame on which he l...


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
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Blender Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
