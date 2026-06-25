---
title: Superhero Landing Tutorial 02 | Ground Destruction VFX in Blender
source: YouTube
url: https://www.youtube.com/watch?v=4ULxB4PzbAc
author: Graphical Ninja
ingested: 2026-06-25
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
