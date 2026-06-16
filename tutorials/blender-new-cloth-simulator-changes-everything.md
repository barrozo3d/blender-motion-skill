---
title: Blender NEW Cloth Simulator changes EVERYTHING!
source: YouTube
url: https://www.youtube.com/watch?v=ih100VB7BUI
author: SouthernShotty
ingested: 2026-06-16
blender_version: "5.2 (experimental)"
tags: [cloth, simulation, geometry-nodes, animation, organic, blender-5x, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/blender-new-cloth-simulator-changes-everything/
frame_count: 9
---

# Blender NEW Cloth Simulator changes EVERYTHING!

**Source:** [YouTube](https://www.youtube.com/watch?v=ih100VB7BUI)
**Author:** SouthernShotty
**Duration:** 18m24s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### A New Simulation System [0:00]
**Transcript:** Today we're going to be taking a look at Blinter 5.2's amazing new experimental cloth simulator.  This works right out of geometry nodes giving us access to all areas of the simulator,  similar to like you might see in software such as Houdini.  Now in this video we're going to go through the new nodes and their settings,  and then we're going to create this peeling off effect together,  made possible by the new cloth sims tearing function.  The cool thing about this effect is that it's all one geometry node setup,  meaning you can apply that geometry node modifier to any object,  and it'll create this peeling away effect.  Now before we dive in, I want to say thank you to this video sponsor,  Skillshare, and let's get started.  So first up, I want to say that this is a 5.2 exclusive feature,

**Frame:** tutorials\frames\blender-new-cloth-simulator-changes-everything\frame_000.jpg

### Getting Started [0:35]
**Transcript:** which is not officially released at the time of recording this video.  So you may need to download an experimental build.  In my experience, they are at a very stable phase though.  So I haven't had any issues with crashing.  After that, you need to go to edit preferences,  and you need to go to the experimental tab,  and you just need to click and drag to turn on the experimental features.  Also notice here that they have here dynamics,  and they are enabling hairs and geometry nodes as well.  So maybe that's something we'll cover in a future video.  Next up, all you need to do is have geometry nodes setup,  and you can grab an object, and I'm going to create one there  and call this cloth sim.  And now you should have access to all the clots and nodes.  So if I go ahead and search for cloth dynamics experimental here,  I can just click and drag this on our geometry output here.  And if I hit play, we can see that it's already starting to work.  Now remember, we are going to be making this cool effect here,  but before I go through how to set up all these nodes,  I'd like to first dive into what each of these settings do  so that you actually know what you're clicking.

**Frame:** tutorials\frames\blender-new-cloth-simulator-changes-everything\frame_001.jpg

### Core Controls [1:35]
**Transcript:** If you're impatient, you can't just skip ahead in the video though.  So first thing, I'm going to twirl down all these  so that we can expose all of our settings here.  First up, we have the pin group, which allows us to pin portions of our object.  And to utilize this, you need to drag the pin group here  to expose it on the group input.  Then you need to have a pin set on your object.  So I've created a vertex group here on my sphere  with a simple selection there.  And now if I come over to the Modifiers tab,  you'll see that we have the pin group exposed there.  And we just need to select the vertex group that you've created.  And if I hit play, you'll see that that remains pinned there.  The need that we have the invert pin group,  which will invert that option and make it so that just the pin selection  is what is affected by the cloth sim.  So right here, we have two of our most important settings,  which are stretchiness and bendiness.  Now, stretchiness to my understanding  means that it will determine how much your edges  construct in terms of links.  And bendiness will determine how much those can rotate in sway.  But it's a little easier if I just show you.  With stretc...

**Frame:** tutorials\frames\blender-new-cloth-simulator-changes-everything\frame_002.jpg

### Simulation Quality [4:15]
**Transcript:** Now beneath that, we had the solver with sub steps  and constraint steps.  Substeps will determine how many steps  between every frame it calculates for the simulation,  giving you more accurate results.  And constraint steps will help with constraints  such as pins, edge length, and more  to give you more accurate results there.  Now keep in mind when you tweak these settings,  it will greatly increase the time you have to render.  So I recommend bumping them up little by little  until you get a result that you like.  I found that 20 and 5 generally gives me pretty good results  while still being able to render quickly.  If I set these values to something really low,  like one in one and click play here  and then go back to something like 20 and 5 and restart,  you can see the vast difference in the simulation quality.  Here we have a simulation to world.  There's nothing we can change here,  but you can input fields and objects into here  to alter how the system views the world space.  Autoresc shape is pretty much always going to be left on.  It allows you to reference the original objects proportions  and shape for the simulation.  And then beneath there we have things like mas...

**Frame:** tutorials\frames\blender-new-cloth-simulator-changes-everything\frame_003.jpg

### A Powerful New Feature [5:50]
**Transcript:** One of the most exciting new features  is the ability to tear.  So we can just check that on.  And if we hit play here, you'll see that nothing tears  and that's because of the threshold being set relatively high.  So if I set this to something really low,  like one and hit play again,  we'll see here that it just tears right off.  But as I set this to an in between value,  for example, 1.05 and hit play again,  you'll see how it holds its form again.  So I've noticed that this threshold's pretty finicky.  The numbers you input to change it  are going to be pretty small.  Up here you have the options to set tearing zones by groups  or verony noise patterns.  So if I turn this on here in tear,  you can see how instead of just tearing  where it pulls off the edges,  it actually kind of tries to create a noise pattern  across the tear to give you a more realistic tear.  Also notice that these have sockets  so you can actually plug in your own noise patterns  or make it so that you tear specific edges.  Now I actually saw this used in really cool effect.  Here on Bradley Animation,  who used that input there to draw curves  and cut the cloth where ever he drew a curve to intersect it. ...

**Frame:** tutorials\frames\blender-new-cloth-simulator-changes-everything\frame_004.jpg

### Forces & Collisions [7:00]
**Transcript:** which we're going to look at how to use next.  Now there are a couple fields here  where you can input things.  But in my experience,  I've pretty much done everything  just plugged into the effector node down here.  So that's what we're going to focus on.  Now we have two nodes to interact with the effectors over here.  We have the custom force node  and the geometry collider node.  Now the cool thing about geometry nodes  is you can build anything  and turn it into a force  or into a collider.  So you're no longer limited  to the simple options they had before,  such as wind.  Now up here we have the option between a field  which will work off the options we have here.  Or if you want,  you do complex setups  and build a closure and blender  and feed all that information into here.  This is where you get into some of the crazy setups  like I said,  similar to Houdini rigs.  We're going to keep it simple  and focus on the field here.  Now with the selection here,  you can actually feed in specific selection  so that you only  affect certain parts of the mesh.  We've already seen how to do this on a pin group,  so I'm not going to redo that process.  Now beneath that,  we have the ...

**Frame:** tutorials\frames\blender-new-cloth-simulator-changes-everything\frame_005.jpg

### Building the Effect [10:36]
**Transcript:** which you can apply to any object.  These files will be on my Patreon  if you just want to skip and download them.  So let's break down how I made this note setup.  First of all, I want to show that also  having my scene is an object.  Now you're going to want some simple density here,  but you don't want it to be too dense  or it'll lag out your computer.  So here we can see that I have about 50,000 faces  and I found that that gave me a pretty decent result.  And after you have your object,  you're going to want to add a geometry note here  and then a subdivision after.  Now I recommend turning off this subdivision  while you're working or it will lag your scene.  Let's get started on this.  First, you're going to take the geometry note output  and we're going to plug it into a shrink setup here.  So when you scale your object,  it just scales the object in and out as a whole.  But what I want to do is scale along the normal.  So you can see what that looks like here.  And the reason I want to do that is because we're actually  going to duplicate the object on top of itself  and use itself as a fabric and a collision object.  The setup's pretty simple.  Grab a set position node a...

**Frame:** tutorials\frames\blender-new-cloth-simulator-changes-everything\frame_006.jpg

### Bringing It Together [14:00]
**Transcript:** So let's create that object underneath.  Also, we need to do is grab the group output here.  We're going to drag this down into a geometry collider.  Now, this is another one of those  really important settings here.  On the collider, adjusting the friction  can determine whether your effect will work or not.  I know that depending on the object I used  or the size of the scale,  I had to adjust the friction here  in order to get it to actually peel off correctly.  You're also going to want to check on this deforming option.  Since we are scaling the animation up here,  this deforming option will make sure that it works.  Then after that, scroll down to the object space here  and select whatever object you have this effect applied on.  So in my case, that's the skull low poly.  Now, we need to plug this all into a cloth sim.  So we're going to do that right after our shrink simulation.  So add a cloth sim here  and plug the shrink simulation result into the geometry.  And this is going to take the outer shell  that we've created and turn it into a cloth.  Now, I don't need to pin anything  and I can do really low values for the stretchiness  and bendiness.  I found things from 0.5 ...

**Frame:** tutorials\frames\blender-new-cloth-simulator-changes-everything\frame_007.jpg

### Final Tips [18:05]
**Transcript:** Now lastly here, I added a bake node at the end.  I've noticed that not a lot of people  in the Blender beginner community  seem to know about this node,  but you can actually put it right at the end of your geometry  nodes and click bake and just pre-bake your animation.  And then when you're done, you can trash it  if you need to rebake it.  I hope you found this tutorial helpful.  Let me know what you think in the comments below.

**Frame:** tutorials\frames\blender-new-cloth-simulator-changes-everything\frame_008.jpg


---

## Structured Notes

### Core Technique
**Cloth Dynamics Experimental** node in Blender 5.2 Geometry Nodes — a Houdini-style GN-based cloth simulator with tearing support, used here to build a "peeling skin" effect where an object's outer mesh tears and falls away from its surface.

### Summary
SouthernShotty covers every parameter of Blender 5.2's new **Cloth Dynamics Experimental** GN node (Pin Group, Stretchiness, Bendiness, Sub Steps, Constraint Steps, Tearing, Geometry Collider, Custom Force), then builds a complete "peeling skin" effect applied to a skull mesh. The trick is duplicating the object onto itself — the offset outer shell becomes the cloth that tears while the inner geometry acts as the collision object. The entire setup is a single GN modifier, portable to any mesh. A **Bake** node pre-bakes the simulation to disk for playback.

### Key Steps
1. Download Blender 5.2 experimental build (or official 5.2+ when released)
2. Enable experimental features: **Edit → Preferences → Experimental** tab → enable (drag slider)
3. Select your mesh; add a **Geometry Nodes** modifier. Object needs ~50,000 faces for good detail — not too dense or it lags
4. Add a **Subdivision** modifier after GN (but **disable it while working** to avoid viewport lag)
5. In the GN editor, search `cloth dynamics experimental` → add the node → plug geometry output into it → hit play to confirm it works
6. **Study the core parameters before building** (frames 002–005):
   - **Pin Group** → expose as group input → assign a Vertex Group in the modifier tab to pin portions of the mesh
   - **Invert Pin Group** → reverses which part is pinned
   - **Stretchiness** → controls edge elasticity (lower = cloth keeps its shape; frame_005 shows ~0.500)
   - **Bendiness** → controls angular swing of cloth
   - **Solver Sub Steps** → simulation accuracy per frame (recommended: **20**); **Constraint Steps** → pin/edge accuracy (recommended: **5**); low values (1/1) give visible jitter
   - **Tearing** checkbox → enables mesh tearing; **Tear Threshold** → values around **1.05** for controlled partial tearing; very low (1.0) = immediate total tear
   - Tearing by Voronoi noise pattern for organic tear lines; socket accepts custom noise inputs
   - **Geometry Collider** node → makes any geometry a collision surface; key params: **Friction** (critical for peel behavior), **Deforming** (enable when collision mesh is animated), **Object Space** selector
   - **Custom Force** node → plug in force fields or custom vector force geometry
7. **Build the peeling effect:**
   - From the GN group input, add a **Set Position** node and offset the mesh slightly **along its normals** (this creates the outer shell floating just above the surface)
   - The offset shell = the cloth fabric that peels; the original mesh = the collision object underneath
   - Drag the **Group Output** down → connect it into a **Geometry Collider** node
   - Set **Friction** on the collider (tune per object scale), enable **Deforming**, set **Object Space** to the base mesh object
   - Add the **Cloth Dynamics Experimental** node after the Set Position; plug the offset geometry → Cloth Sim → Group Output
   - Cloth settings: **Stretchiness ~0.5**, **Bendiness** low; no pin group needed for the peel
   - Stretchiness / Bendiness together produce the peeling fall (frame_006 / frame_007)
8. Animate a scale driver on the outer shell to initiate the peel timing
9. Place a **Bake** node at the very end of the GN chain (after all simulation nodes) → click **Bake** to pre-bake the simulation to disk for smooth playback (frame_008)

### Nodes / Settings
| Node / Setting | Value | Notes |
|---|---|---|
| Cloth Dynamics Experimental | — | Main simulation node; search by name in GN editor |
| → Pin Group | Vertex Group | Expose to Group Input; assign via Modifier tab |
| → Invert Pin Group | toggle | Reverses pinned region |
| → Stretchiness | ~0.5 | Controls edge length elasticity |
| → Bendiness | low | Controls angular flexibility |
| → Solver Sub Steps | **20** (recommended) | More = better quality but slower |
| → Constraint Steps | **5** (recommended) | Helps pins/edge constraints converge |
| → Tearing | ON | Enables mesh tearing |
| → Tear Threshold | ~1.05 | Finicky — small adjustments; 1.0 = instant total tear |
| → Tearing Noise | Voronoi | Enable for organic noise-patterned tear lines |
| Geometry Collider | — | Makes geometry a collision object for the cloth |
| → Friction | tune per-object | Critical; may need adjustment per object scale |
| → Deforming | ON | Required when the collision mesh is being animated |
| → Object Space | Base mesh | Set to the object the modifier is applied to |
| Custom Force | — | Input force fields or built custom vector force geometry |
| Set Position | along normals | Offsets the outer shell above the surface for the peel |
| Subdivision | OFF while working | Add after GN; disable during simulation iteration |
| Bake | end of chain | Pre-bakes GN simulation to disk; shown at chain end (frame_008) |
| Target mesh density | ~50,000 faces | Sweet spot: enough detail without viewport lag |

### Difficulty
Intermediate / Advanced — multiple GN nodes, simulation parameter tuning, Blender 5.2 experimental build required

### Blender Version
**5.2 (experimental)** — the "Cloth Dynamics Experimental" GN node is a 5.2-exclusive feature, not available in 5.1 or earlier. Author recommends downloading the experimental build; describes it as "very stable phase" at recording time.

### Tags
`#cloth` `#simulation` `#geometry-nodes` `#animation` `#organic` `#blender-5x` `#intermediate` `#advanced`

---

## Related Tutorials
- [[realistic-cloth-physics-in-blender-full-tutorial]] — Traditional Cloth modifier workflow (pre-5.2); shares `#cloth #simulation #animation`; useful comparison for understanding what the new GN approach replaces
- [[blender-50-particle-attraction-and-follow-surface-motion]] — GN Simulation Zones for forces; shares `#geometry-nodes #simulation #blender-5x`
- [[another-blender-string-tutorialbut-even-better-this-time]] — GN Simulation Zones for animated curves; shares `#geometry-nodes #simulation #animation`
- [[blender-51s-new-rigging-tool-is-insane]] — Blender 5.x GN + simulation bridge; shares `#geometry-nodes #simulation #blender-5x`
