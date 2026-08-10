---
title: Volume Editing - Blender Geometry Nodes Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=VU_FhO4Jlpg
author: CGMatter
ingested: 2026-08-10
blender_version: "5.3"
tags: [geometry-nodes, simulation, smoke-fire, volume, procedural, displacement, cycles, advanced, blender-5x]
extraction_status: complete
frames_dir: tutorials/frames/volume-editing---blender-geometry-nodes-tutorial/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Volume Editing - Blender Geometry Nodes Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=VU_FhO4Jlpg)
**Author:** CGMatter
**Duration:** 8m18s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] How cool would it be to take a volumetric simulation?
[0:02] And without re-simulating it, bend it, or you can twist it, or deform it in many different ways again without re-caching it.
[0:08] There are two problems with... two problems with this.
[0:10] It's not possible in Blender, it just isn't.
[0:12] Even if we did, volumetrics especially deformed ones take forever to render.
[0:16] I'm gonna solve the first problem just with a good ol' brain.
[0:19] As for rendering, I'm gonna use Drop and Render, which is a render farm.
[0:22] The Rasterize Point node only exists in 5.3.
[0:25] When you download it, just make sure in geometry nodes you have this bad boy.
[0:28] First thing we need is some volumetrics simulation.
[0:30] I'm gonna use Blender's Cursed Volumes.
[0:32] Take an object, run it through a quick smoke.
[0:34] Then, in the physics settings, I want it to emit smoke and fire.
[0:37] In the domain, which you can see is super low resolution, bring up the divisions.
[0:41] And to add some interest in vorticity, I'm gonna do .3.
[0:43] In order you can see it's kinda getting more definition.
[0:45] Bring it way up.
[0:46] We're gonna cache, let's say, 100 frames.
[0:49] In the type of caching, I'm gonna create a All Cache, which lets me save this as an open VDB.
[0:54] Again, the first 100 frames.
[0:55] Make a folder.
[0:56] Hit Bake.
[0:56] And, honestly, just walk away for 5 years.
[0:58] It'll probably be close to done at that point.
[1:00] We did it!
[1:01] And the proof is in the folder, specifically in data.
[1:04] You're gonna see all of these VDBs.
[1:06] And here's the core idea.
[1:07] If I take a volume grid, turn it into a bunch of points.
[1:09] Well, we know how to distort points in an arbitrary way.
[1:12] And if we can get that back into a volume, then that's it.
[1:15] That's how you bend, split, whatever a volume.
[1:17] To import a VDB sequence, as in, it's animated,
[1:19] I'm gonna use my import VDB node.
[1:21] Any purple node is for free on my website.
[1:24] It will tell you how to download those.
[1:25] The way this works is you just need to say what folder and what is the file name.
[1:28] This is the folder.
[1:29] Paste that in there and add a trailing slash file is called Fluid Data with a underscore.
[1:34] And if I look at this, you can see we're getting our volumetric transform it.
[1:37] So it's centered for whatever reason.
[1:39] Usually you have to like subtract by 0.2.
[1:41] I want you to notice we have all of these different grids that I can look at.
[1:44] I can get something like the density grid or maybe the flames grid,
[1:47] because I'm gonna want to transform all of these.
[1:49] Take the density grid.
[1:50] We're gonna turn it into points.
[1:52] The way you should think about this is these points carry the grid information.
[1:55] I'm then gonna turn this back into a volume using this rasterized points node.
[1:59] First of all, what is the voxel size, the resolution?
[2:01] For now, I'm just gonna do 0.1.
[2:02] Second of all, we have the sampling or averaging method.
[2:05] And then we say where do we want to sample and what field are we using?
[2:08] This is gonna be our field.
[2:09] You can see it's kind of like a low resolution version of what we had before.
[2:13] So we're gonna want to recover that,
[2:14] which can be done by lowering the voxel size over and over.
[2:16] Once you start seeing this kind of, I don't know if it's coming through on YouTube compression,
[2:19] but this kind of banding.
[2:20] This is where you want to take the kernel type and bring it up to something higher quality.
[2:24] Now, something you're gonna notice when I go between these is kind of like the density is greatly reduced.
[2:28] That's because rasterized points, it in a sense doesn't account for density.
[2:32] So if I'm evaluating some field that's based on a grid,
[2:35] we want to kind of get rid of this density term by multiplying.
[2:38] Kinda, sorta, not really.
[2:39] Long story short, you add a value of 1, so it's gonna sum everything in the area.
[2:44] Take the thing we care about and we're gonna divide by this value.
[2:46] Boom, we get back our strength.
[2:48] Here comes the crux of this tutorial.
[2:49] Rasterized points can be done on any arbitrary position.
[2:52] By default, that's just gonna be the position,
[2:54] but if I do some kind of addition, I can transform this to the side.
[2:58] You probably see where I'm going with this.
[2:59] We can do really complicated transformations.
[3:01] Let's start by taking this and bending it.
[3:04] Some kind of root point and as you go up the volume, you're gonna pivot.
[3:07] Vector rotate, where the center is gonna be somewhere low.
[3:09] The axis I want to rotate by, in this case, is either the x or the y.
[3:13] I'm gonna use the x-axis.
[3:15] If I plug this in directly, it lets me do this kind of rotation.
[3:17] But if I do this as the position goes upwards, separate x, y, z, and use this as the z component,
[3:22] all of a sudden, we get this spinny boy.
[3:24] I'm gonna add a multiplication factor.
[3:26] Now I can bend like this.
[3:28] I want you to notice I didn't need to re-simulate anything.
[3:30] We have our volumetric and now it is curving.
[3:32] If I also want to render the fire,
[3:34] Fetch a named grid called flame,
[3:36] grid two points rasterized,
[3:37] where this time this is the field we're evaluating,
[3:39] again doing that like division by one trick.
[3:41] And now we have our flames that I want to use this transformation on.
[3:44] And now this is bent as well.
[3:46] Recombine them into a single volume.
[3:48] Store this one, density, chain it, and store this other one, flame.
[3:51] Even though only the flame grid is visible,
[3:53] you can see we do actually have two grids.
[3:55] Let's do the kind of classic fire material.
[3:57] This can be our smoke and fire.
[3:59] Because this is a volumetric, we use the principled volume.
[4:02] Kinda hard to tell, but it is already here.
[4:04] You want the density to be the density for the temperature, saying,
[4:07] Where is it hot?
[4:07] I'm just gonna use flames.
[4:09] As I increase the black body intensity, you're seeing it's kinda starting to get red.
[4:12] Make it brighter by taking the temperature and making it something bigger than a thousand.
[4:16] Hey, nobody told me I inverted these.
[4:17] Whoops.
[4:18] Anyways, we're not seeing the density.
[4:19] Take it and bring it up, maybe add a basic light source.
[4:22] And just like that, we've created a custom transform that moves the flame and the fire.
[4:26] What I want to show you now is some different transforms you can do,
[4:28] where all of this can be a node group, volume,
[4:31] and then I can just make a new transform and plug it in here.
[4:34] Let's do some twisting.
[4:35] Take the axis, we're gonna make it into the z-axis.
[4:37] Increase our rotation factor.
[4:39] So here we're getting this kind of tornado.
[4:41] It's rotating about the origin, even though it's supposed to be kinda off to the side.
[4:44] So just kinda shift it to where it needs to be.
[4:46] Boom, we can twist a volume.
[4:47] What about taking a volume and splitting it in half?
[4:49] Just add to the position.
[4:50] Make two different versions of these.
[4:52] One goes to one side, one goes to the other.
[4:54] We're gonna choose which goes where, based on some factor,
[4:57] which is gonna depend on the z-position, and specifically, am I above a certain height threshold?
[5:01] So check where z is greater than, I don't know, 0.3.
[5:04] Connect that here.
[5:05] And now we've split the volume.
[5:06] It does preserve the motion that it had before.
[5:08] Kind of a weird use case, but it does exist.
[5:10] What about a basic distortion?
[5:11] Add a random noise texture where I'm gonna turn off Normalize.
[5:15] I wanna control kind of the strength of this.
[5:17] And we have a nice blurring, just like that.
[5:19] Let's bring down the scale a little.
[5:20] Bring up the detail.
[5:21] Now we've just added a bit of kind of free visual interest or detail to our simulation.
[5:25] If I add a normalization, this is gonna take our volume and kinda project it onto a sphere,
[5:30] because all the vectors are of the same length.
[5:32] So I'm gonna put a project file on my website, along with some cache simulation, maybe this one.
[5:36] And I'll make a couple preset transforms that you can just use, twist, bend, whatever.
[5:39] Now that we're on the topic of rendering big beefy volumetric scenes,
[5:43] I made this monstrosity.
[5:44] And I've maxed all of this out.
[5:46] This rotating explosion volume is based on this VDB file, pretty much half a gigabyte.
[5:50] I need my 1080p 1000 sample worst of all motion blur enabled render.
[5:54] I'm gonna hit render and render this locally.
[5:56] And while this churns going 2, 3, can we get 3 samples?
[6:00] I'm gonna tell you about Drop and Render, which is a render farm sponsoring this video,
[6:03] and can hopefully save the render time for a shot like this, where there are 100 frames.
[6:07] And since I've been talking, again, only 24 samples.
[6:09] I'm gonna open another instance of Blender, but in this case, I have my Drop and Render add on already set up.
[6:14] You can kind of do everything from inside of Blender without leaving it.
[6:16] So if you want to get technical, you can start this cloud manager thing, all of this stuff.
[6:20] You don't even want to deal with this.
[6:21] I'm just gonna hide that.
[6:22] And for any scene, regardless if you've done Link, path relative absolute,
[6:26] it will just check your blend, make sure it's good to go, render it, and bring the files to your computer.
[6:30] So from your point of view, you've never left Blender.
[6:32] So I'm gonna call this explosion.
[6:34] Even though this is local, it's going to render, then download back.
[6:37] And how are we doing with our render?
[6:39] 175 samples.
[6:40] So once you have everything set up, just gonna check your scene,
[6:43] saying we're using cycles, 120 frames.
[6:45] I was actually recommended to render 60 frames for this segment, but you can't stop me.
[6:49] You can pick your, like, level of priority.
[6:51] I'm gonna keep it on Emerald, and all you have to do is hit Submit Project.
[6:54] It's gonna pack anything that you broke with your blend file.
[6:56] It's gonna fix.
[6:57] And then you're just gonna see Job is successfully submitted.
[6:59] You could just, like, sit here and wait for the images to populate, and that's perfectly fine.
[7:03] But if you do want to see what's going on, you can instead just go to the website.
[7:06] So I'm gonna open up this explosion project, which it's already uploaded.
[7:10] I think you already know the essence of a render farm.
[7:11] Instead of rendering on one computer, and mine's a very good one,
[7:14] you take the task and you divide it amongst, in this case, 24 computers,
[7:18] each one taking a few frames at the same time.
[7:20] While this is all churning, let's do a calculation.
[7:22] We've done 542 samples, and we're already 10 and a half minutes into the render.
[7:27] 1000 divided by, let's see, 572.
[7:29] We need to render 1.7 times longer than we currently have.
[7:33] Multiplied by roughly 11 minutes.
[7:35] Oh, by the way, our files are starting to come in over here.
[7:37] Multiplied by that, meaning one frame is going to take 19 minutes,
[7:40] times a 120 frames, divided by 60, 38 hours.
[7:45] If I was to leave it to my 5090, it's gonna take 1.6 days.
[7:49] I'm just gonna let this run and tell you the total runtime of all this,
[7:52] and I guess I can do a time lapse.
[7:53] And just like that, the avatar has returned.
[7:55] I submitted this at basically 730, and my time, it is 7.59, so a little under half an hour.
[8:00] Part of that was the upload process of half a gigabyte of a VDB.
[8:04] From 1.6 days to half an hour.
[8:07] I guess it's a little faster.
[8:08] If you wanna check out Drop-In Render, Render Farm, there's information, a link below.
[8:12] And the cool thing is, you get render credits when you sign up.
[8:15] You don't need to use a credit card, so you can render a thing for free.



---

## Captured Frames

- [1:04] tutorials/frames/volume-editing---blender-geometry-nodes-tutorial/frame_000.jpg
- [1:34] tutorials/frames/volume-editing---blender-geometry-nodes-tutorial/frame_001.jpg
- [2:47] tutorials/frames/volume-editing---blender-geometry-nodes-tutorial/frame_002.jpg
- [3:16] tutorials/frames/volume-editing---blender-geometry-nodes-tutorial/frame_003.jpg
- [3:27] tutorials/frames/volume-editing---blender-geometry-nodes-tutorial/frame_004.jpg
- [4:21] tutorials/frames/volume-editing---blender-geometry-nodes-tutorial/frame_005.jpg
- [4:45] tutorials/frames/volume-editing---blender-geometry-nodes-tutorial/frame_006.jpg
- [5:05] tutorials/frames/volume-editing---blender-geometry-nodes-tutorial/frame_007.jpg

---

## Structured Notes

### Core Technique
Deform an already-baked volumetric simulation (bend, twist, split, distort) without re-simulating, by round-tripping the volume through a point cloud: **Grid to Points → transform point positions → Rasterize Points** (Blender 5.3's new volume-reconstruction node) back into a volume.

### Summary
CGMatter takes a cached OpenVDB smoke+fire simulation and shows how to bend, twist, split, and add noise distortion to it entirely in Geometry Nodes, with zero re-caching. The core trick: convert a volume grid (density or flame) to points with `Grid to Points` (each point carries the grid's value), transform the point *positions* with ordinary node math (Vector Rotate, Add, Noise Texture), then rebuild the volume with the new `Rasterize Points` node — exclusive to Blender 5.3. Because `Rasterize Points` doesn't account for density weighting, a "divide by 1" trick (rasterize a constant 1 alongside the real value, then divide) recovers the correct density strength. The same transform is applied to both the density and flame grids so smoke and fire deform together, then they're recombined via `Store Named Grid` for a Principled Volume fire material. The video closes on a sponsored segment using the Drop and Render farm to render a heavy 0.5GB VDB explosion (1.6 days locally → ~30 min on the farm).

### Key Steps
1. Bake a Quick Smoke simulation: bring up domain resolution, set vorticity ~0.3, cache ~100 frames as an "All" cache (OpenVDB sequence) to a folder.
2. Import the VDB sequence with an `Import VDB [CGM]` node (free custom node from the author's site): set Folder, File Name prefix (e.g. `fluid_data_`), 4-digit numbering, Offset.
3. Pick a grid (Density or Flame) and feed it into `Grid to Points` — this bakes the grid's scalar value onto each generated point.
4. Transform the *positions* of those points with normal node math — this is the whole trick, since the points still carry the original grid value.
5. Rebuild the volume with `Rasterize Points` (Blender 5.3 only): set Voxel Size (start coarse ~0.1, refine to ~0.025 for detail), pick a higher-quality kernel/sampling method (e.g. Quadratic B-Spline) to remove banding, and wire in the transformed Position and the grid Value.
6. Recover lost density: run a second `Rasterize Points` on a constant value of `1` (same positions), then `Divide` the real-value rasterize by that count-rasterize to get back correct density strength.
7. **Bend:** `Vector Rotate` (Axis Angle), Center placed below the volume, Axis = X; drive the angle from `Position` → `Separate XYZ` → Z-component × a Multiply factor, so curvature increases with height.
8. **Twist:** same Vector Rotate setup but Axis = Z and a larger multiply factor on the height-driven angle → tornado-like twist; recenter the rotate Center to the volume's actual XY origin.
9. **Split:** `Separate XYZ` on Position → `Greater Than` on Z (threshold e.g. 0.5) → two different `Add` position offsets → `Mix` between them using the boolean/factor, splitting the volume into two chunks by height while preserving prior motion.
10. **Noise distortion:** `Noise Texture` (Normalize OFF) added into the position for subtle blur/detail; turning Normalize ON instead projects all points onto a sphere.
11. Apply the same transform node group to both the density and flame grids, then `Store Named Grid` both back into one volume.
12. Fire material: `Principled Volume` — Density input = density grid; feed the flame grid into Blackbody/Temperature (temperature > 1000 for a hot look) for the fire color.
13. For a heavy final render, offload to a render farm (Drop and Render, sponsor) instead of rendering 1000-sample motion-blurred volumetrics locally.

### Nodes / Settings
- **Import VDB [CGM]** — custom/free node (author's site): Folder, File Name, Time → 4 Digits, Offset; outputs VDB / Density / Velocity.
- **Grid to Points** — Grid → Points (+ per-point Value carrying the grid's scalar).
- **Rasterize Points** — Blender 5.3-exclusive. Voxel Size (0.025–0.1 m range shown) or Matrix mode; kernel/sampling type (raise to Quadratic B-Spline to remove banding); Position and Value inputs.
- **Divide** — recovers true density: (value-rasterize) ÷ (ones-rasterize).
- **Vector Rotate** — Type: Axis Angle; Center + Axis vary per effect (bend: Axis X, Center below volume; twist: Axis Z, Center at volume origin).
- **Separate XYZ + Multiply** — derives a height-driven rotation angle from Position.Z.
- **Greater Than + 2× Add + Mix** — splits the volume into two halves by a Z threshold.
- **Noise Texture** (Normalize off for distortion; on for spherize).
- **Principled Volume** — Density = density grid; Blackbody Intensity/Temperature (>1000) = flame grid, for the fire look.
- **Store Named Grid** — recombines density + flame grids into a single output volume.

### Difficulty
Advanced — depends on a Blender-5.3-exclusive node (`Rasterize Points`) and a non-obvious point-cloud round-trip technique; not beginner-friendly, though each individual transform (Vector Rotate, Add, Mix) is simple once the core idea clicks.

### Blender Version
Blender 5.3 — required. The video states explicitly: "The Rasterize Point node only exists in 5.3."

### Tags
`#geometry-nodes` `#simulation` `#smoke-fire` `#volume` `#procedural` `#displacement` `#cycles` `#advanced` `#blender-5x`

---

## Related Tutorials
- **Fluid sim testing in Blender 5.3! (Rasterize Points Node)** (`tutorials/fluid-sim-testing-in-blender-53-rasterize-points-node.md`) — closest match: same `Rasterize Points` node, same Blender 5.3, also builds density/velocity grids from a point-cloud round-trip, just for a from-scratch pseudo-fluid sim instead of post-processing a cached one.
- **3D Smoke (Blender Geometry Nodes)** (`tutorials/3d-smoke-blender-geometry-nodes.md`) — shares geometry-nodes/simulation/smoke-fire/volume/blender-5x/advanced; builds the underlying volumetric smoke sim from scratch with velocity/pressure/density fields, complementary to this video's "deform an existing bake" angle.
- **Blender 5.0's NEW Audio Visualisation is INSANE!** (`tutorials/blender-50s-new-audio-visualisation-is-insane.md`) — shares smoke-fire/volume/blender-5x; another Geometry Nodes volumetric grid workflow, driven by audio instead of manual transforms.
