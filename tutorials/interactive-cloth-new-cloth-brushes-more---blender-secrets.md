---
title: Interactive Cloth + new Cloth Brushes & more - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=bHmZfA07F0Y
author: Blender Secrets
ingested: 2026-08-04
blender_version: "4.3+ (the cloth sculpt brush was split into several dedicated brushes starting in this release)"
tags: [cloth, simulation, rigging, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/interactive-cloth-new-cloth-brushes-more---blender-secrets/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Interactive Cloth + new Cloth Brushes & more - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=bHmZfA07F0Y)
**Author:** Blender Secrets
**Duration:** 12m49s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this video we'll look at how to place a cloud object interactively
[0:03] and how to squeeze the most quality out of the simulation even if your computer is very old or very cheap
[0:09] as well as some other tips for how to get the best results with the cloud simulation in Blender
[0:15] and you can find the files for this as well as some visual examples of some tests I did with
[0:19] different values for the cloud simulation options in my Blender Secrets ebook.
[0:24] First of all, create a collision object. So I'm going to use a cube, scale it down on the z-axis
[0:32] and then I'm going to shift and right click on top of it so that I can place the 3D cursor there
[0:37] and add a grid or a plane. I'm going to use a grid because it's basically a plane that is already
[0:43] subdivided and then we're going to subdivide it maybe two more times. So we have quite a lot of
[0:48] subdivisions and that's always important when you have cloth so that it has another geometry
[0:54] to move and I'm just going to select one of these vertices. It doesn't really matter but maybe it's
[1:00] easier to select one in the middle and then I'm going to go here to the vertex groups and click
[1:05] on the plus icon to add a vertex group and then click on assign and that's basically assigned
[1:11] this one vertex to this vertex group. So if I deselect everything now at alt-a and click on
[1:16] select and it will select that one vertex and if you look at weight paint mode you'll see that it
[1:22] has weight painted that one vertex and then with this vertex still selected I'm going to press
[1:29] control H and then hook to new object and this is created an empty. Let me just show you in
[1:35] wireframe mode and x-ray mode so you can see it. It's basically an empty but it is in this case a
[1:41] hook and what a hook does is it allows you to grab a vertex and move it around in object mode
[1:49] instead of in edit mode. So let's go to object mode and so I've moved this
[1:54] grid slightly above this cube and to make it a bit more easy to see I'm just going to turn this
[1:58] to a matte cap. I'm just going to use any one of these is fine maybe this one and then we're going
[2:04] to set the colors to random. You could also choose objects and then just set a color per object so
[2:11] go to this tab here and then viewport display and then here on the color you can just choose
[2:17] any color you want so I can give this one another color. So now it's more clear what we're doing
[2:23] and so now what I'm going to do is I'm going to select this green box and I'm going to here
[2:29] in this tab here and I'm going to click on collision and that just turns this into a collision
[2:34] object and what that means is that colloid sims and other kinds of simulations can now collide
[2:39] with this object and this one is also going to be some kind of physics object but in this case
[2:44] we'll click on cloth so we turn this into a cloth object and now to use the vertex group that we
[2:50] made before we're going to go here under shape and then when it says pin group you're going to click
[2:56] on that empty field and choose a group and that is the vertex group that we made before so that's
[3:01] that one vertex and a pin group is basically a vertex group where the vertices are pinned so they're
[3:09] stuck in space and they cannot move with the colloid simulation but we can move it by using the
[3:15] hook that we added and then moving that vertex around and one more thing we need to enable here
[3:20] is self-collisions otherwise the colloid will kind of self-intersect and that will look unrealistic
[3:26] of course and for the rest I'm just going to leave these settings as is and so now you can see in
[3:32] the modifiers we have the hook modifier and we have the cloth modifier and so now all we need to
[3:39] have is a timeline and by default you will have a timeline but I removed it from my default blender
[3:45] setup so I have to add it again and I'm going to make this slightly longer like 10,000 frames
[3:51] otherwise the simulation will keep looping back after a few seconds and I want to be able to
[3:57] experiment with it and so now what we can do is we can press the play button here and that starts
[4:02] the simulation and then I can grab this empty this hook empty by clicking on it and then with g
[4:09] I can move it around and to make this look a little bit better we can select the cloth
[4:15] and use shade smooth so right click and choose shade smooth and then I'm going to add a sub-div
[4:21] modifier I can either do that by pressing ctrl 1 or by just clicking on add modifier search and
[4:26] then searching for the subdivision surface modifier and it's here at the bottom so it's
[4:31] doing its thing after all of the other modifiers and so let me just go back to the beginning by
[4:36] clicking on this back button here and let me just move the hook around so as you can see now I can
[4:42] move this and place this cloth anywhere I want and for me to be able to not intersect with this let me
[4:49] just click on the pause button and go back one more time so one very useful keyboard shortcut
[4:54] is when you're moving something you can press shift and z and what that does is so g to move and
[5:00] shift and z and now I have locked the z axis so shift z locks the z axis so now I'm just moving it
[5:07] on the x and y planes and the reason it stopped after 250 frames you can see there's this kind of
[5:14] blue bar and this blue bar here is the cache for the simulation and so even though we have a long
[5:20] timeline we have to extend the cache so with the plane selected I go here to this simulation tab
[5:27] and then the collot settings under cache we can also set this to as long as our timeline
[5:34] and so now when we go back to the beginning and press the play button then we can play with this
[5:40] for 10 000 frames and I'm going to press shift z again so that it's constrained on the z axis
[5:47] let me just do that one more time and first I'll move this back to where it was so I press play
[5:54] g shift c and now I can move this around all the way I want and this is useful for when you're
[6:01] doing an architectural visualization for example you need to place some towel in a tasteful position
[6:07] on a sofa for example or on the edge of a bed then you can do that like this so again I can move it
[6:13] if I want to have it over here instead so g and shift and z and then when I'm happy with that I can
[6:20] press the pause button and let's stop it playing and now if I want to apply this so if I don't want
[6:26] this to be a simulation anymore I can just select the object knowledge mode press control a and choose
[6:33] visual geometry to mesh and that will just turn it into geometry as you can see to make this look
[6:40] better we can use some sculpting so we already had the cloth brush for a while but since blender
[6:45] 4.3 I think what they've done is they've taken the kind of obscure options that most people didn't
[6:50] know about and have split the one cloth brush up into several different ones with those different
[6:56] options enabled and where you find it is in sculpt mode you click here and then you go to simulation
[7:01] and now we have all of these different options to choose from one thing that we should pay attention
[7:07] to is for example if I click on drag cloth and I drag this as you can see we don't really have
[7:14] enough resolution in our mesh yet so let me just undo that a few times if you add a multi-res modifier
[7:20] and you simplify this a couple times I find that the result is not really very good let's go down one
[7:27] level and let's try a different brush I find that with multi-res it is quite difficult to do the
[7:33] collaud sculpting so let me just remove that one and in fact what I prefer to do is in object mode
[7:39] add one level of subdivision and then just apply that modifier now we have this amount of subdivision
[7:45] so 25600 faces and let's try some sculpting again and you can change the radius by pressing f
[7:52] and now it's way too strong so let me just undo that and reduce the strength to about 0.1 and now
[7:58] I have a lot more control now I can start adding some finer folds like this by just
[8:06] bunching folds together so let's try the expand contract cloth brush and let's see what that does
[8:15] so that just adds some general wrinkles here and there and you can always press shift and then
[8:21] just blur things out again another really fun brush to use is the grab planar cloth brush
[8:28] so if we select that and let's also set the strength fairly low then we can just kind of move
[8:34] these together so again you get this kind of bunched up effect and by pushing this up we can
[8:40] also get some more folds there push this in this direction and again if we think that's too much
[8:46] then we can always smooth it out and this brush is really fun for just sort of pushing things in a
[8:52] certain direction and seeing those folds be created and yeah if it's too much just undo or
[8:58] hold shift to smooth it out so now we have quite a bunch more folds and maybe I'll push this over
[9:04] here now with the default quality settings it's pretty easy to move this around on my computer
[9:12] but if I set this to the maximum so the maximum is 80 and in the collisions it's 20 then if I try to
[9:21] simulate this it will go very very very slowly and my computer cannot handle it so what do you do
[9:28] if you do want to have high quality and you want to be able to also control it well first of all
[9:33] let's set this back to the default values and what I'm going to do is I'm actually going to turn off
[9:39] the collage modifier for a moment so I'm just going to click on this icon so we don't see it
[9:44] and then I'm going to enable auto keying here and I'll select my empty and press play and then I can
[9:49] just move the empty to wherever I want and press the pause key and then disable auto keying very
[9:55] important and so you see now we have these keyframes for my empty and so now what I can do is I can
[10:01] turn the collage modifier back on and go to the collage panel and I can increase the quality
[10:07] as high as I want and increase the collision quality as well and then I simply click on bake
[10:12] and then I wait for a moment and as you can see it's very slowly calculating this and so now when
[10:18] you see this blue line in the timeline it means that the cache here is baked and so now we can just
[10:24] scrub through and it's not actually simulating anything it's just showing what's cached and I
[10:29] like to work this way with a recorded empty and then just baking everything because that way you
[10:34] can test out different settings and let me just delete all bakes that freeze up the bake and then
[10:40] we can go back to the first frame and now I can start experimenting like for example what will
[10:45] happen if I add one kilo of vertex mass and then I will bake again and now it's finished baking so
[10:51] we can check what the result is and we can find a good frame like this for example and it does look
[10:58] quite different than when we had our vertex mass as 0.3 which is the default I find that vertex
[11:04] mass is the setting that has the most influence on how the result looks and also the air viscosity
[11:10] so these two physical properties here are very important I have experimented with all of these
[11:15] other values however I generally only see very very subtle differences so it's not really worth
[11:22] experimenting with in my opinion those are the values that I would experiment with for the cloth
[11:26] object but for the collision object you can also try experimenting with the friction value so let's
[11:31] say we set this to 50 for example and we try to bake that again so let's play the result and you
[11:38] can see that the cloth object really has a lot of friction so it cannot slide so easily along
[11:45] this collision object and so that's controlled with this friction value another thing you want to
[11:50] keep in mind with cloth simulations is the size of the cloth object as well as the amount of
[11:56] geometry it has so in this case if we go to edit mode we can see that it has 1600 faces and I think
[12:02] this is a very reasonable amount it's not too little but it's also not too much and if it was
[12:08] double this I think the simulation would have problems and the way it looks when it has problems
[12:13] in blender is it will kind of crunch up it will shrivel up and that happens also if the object
[12:19] has a small size so if the object the cloth object has a small size it can also tend to like shrivel
[12:25] up and the way to solve that is simply by scaling it up in object mode and conversely if you scale
[12:31] it up too much it will also react differently so you really need to work with something that is not
[12:37] too big and not too small those are the tips I have today about the colt modifier but if you
[12:42] have some suggestion or some questions about it please feel free to leave a comment and thanks
[12:46] for watching all the way until the end



---

## Captured Frames

- [0:32] tutorials/frames/interactive-cloth-new-cloth-brushes-more---blender-secrets/frame_000.jpg
- [2:29] tutorials/frames/interactive-cloth-new-cloth-brushes-more---blender-secrets/frame_001.jpg
- [3:56] tutorials/frames/interactive-cloth-new-cloth-brushes-more---blender-secrets/frame_002.jpg
- [6:33] tutorials/frames/interactive-cloth-new-cloth-brushes-more---blender-secrets/frame_003.jpg
- [7:14] tutorials/frames/interactive-cloth-new-cloth-brushes-more---blender-secrets/frame_004.jpg
- [8:06] tutorials/frames/interactive-cloth-new-cloth-brushes-more---blender-secrets/frame_005.jpg
- [8:28] tutorials/frames/interactive-cloth-new-cloth-brushes-more---blender-secrets/frame_006.jpg
- [10:07] tutorials/frames/interactive-cloth-new-cloth-brushes-more---blender-secrets/frame_007.jpg

---

## Structured Notes

### Core Technique
Placing and posing a cloth simulation interactively via a Hook + Pin Group (grabbing and dragging one pinned vertex in Object Mode while the sim plays), then refining the result with Blender 4.3's split-out Cloth sculpt brushes, and finally baking high-quality settings efficiently by first recording a low-quality "rehearsal" via keyframed Auto Keying before baking the real simulation at full quality.

### Summary
Frame 000 shows the setup's collision object: a flattened, Z-scaled cube selected in Object Mode, the starting point before adding the cloth grid above it. Frame 001 shows the core rig: a blue subdivided Grid (the future cloth) hovering just above a green collision cube, an Empty's axis cross visible at the grid's center vertex — the Hook object created via Ctrl+H. Frame 002 shows the Cloth modifier's Hook settings panel open in the sidebar (Object: Empty, Vertex Group, Strength, Falloff) with the timeline scrubber near frame 0 — confirming the Hook-to-Empty setup on the pinned vertex. Frame 003 shows the simulation mid-play: the grid now draped over the collision cube's corner like real cloth, an Object menu open with "Visual Geometry to Mesh" highlighted — the step that bakes the live simulation into static geometry. Frame 004 shows the baked cloth mesh in Sculpt Mode, now shaded reddish and heavily creased/dragged into deep folds by the Drag Cloth brush, brush palette visible along the bottom. Frame 005 shows a further-refined result — finer, more numerous folds after reducing brush strength for more control, still using a drag-style cloth brush at higher mesh resolution (26,922 vertices reported top-left). Frame 006 shows the Cloth Brushes flyout menu open (Bend Planar, Bend Cloth, Drag Cloth, Expand/Contract Cloth, Grab Planar Cloth highlighted, Pinch/Perpendicular/Point/Multi Grab variants), illustrating Blender 4.3's split of the old single Cloth brush into many dedicated options. Frame 007 shows the Cloth modifier's Physical Properties/Damping panel open (Tension, Compression, Shear, Bending fields, plus a Self Collisions checkbox) on the un-deformed flat grid/collision setup — the tunable parameters used later for quality experiments.

### Key Steps
1. **Build the rig:** create a collision object (e.g. a Cube, scaled down on Z); Shift+right-click to place the 3D cursor on top of it, then add a Grid (a pre-subdivided plane) there; subdivide the grid a couple more times so it has enough geometry to fold realistically.
2. **Create a pin point via a Hook:** select a single vertex on the grid (a middle one is convenient), create a Vertex Group ("+"), click Assign to add just that vertex to it (verify via Weight Paint mode); with the vertex still selected, Ctrl+H > Hook to New Object — this creates an Empty that can grab and move that vertex from Object Mode instead of requiring Edit Mode.
3. **Set up collision and cloth physics:** select the cube, enable Collision (under Physics); select the grid, enable Cloth; under the Cloth modifier's Shape section, set Pin Group to the vertex group made in step 2 — pinned vertices stay fixed relative to the simulation but can still be moved via the Hook; enable Self Collisions to prevent the cloth intersecting itself.
4. **Extend the timeline/cache:** the default timeline is short and loops; extend it (e.g. to 10,000 frames) for room to experiment, and separately extend the Cloth cache length (Physics > Cloth > Cache) to match, or the simulation stops calculating past the old cache length even with a longer timeline.
5. **Play and pose interactively:** press Play, then click the Hook Empty and press G to drag it around in real time while the cloth simulates and drapes over the collision object — Shift+Z while moving locks movement to the X/Y plane only (useful for placing cloth like a tablecloth on a surface without lifting it). Pause and rewind as needed to re-try a placement; this is especially useful for archviz work like draping a towel realistically on a sofa or bed.
6. **Bake the pose to real geometry:** once satisfied with a frame's drape, select the object in Object Mode, Ctrl+A > Visual Geometry to Mesh converts the live simulation result at that frame into static mesh geometry, ending the simulation dependency.
7. **Refine with the new Cloth sculpt brushes (Blender 4.3+):** in Sculpt Mode, open the brush picker's Simulation category to find the split-out Cloth brushes (Drag Cloth, Bend Cloth, Bend Planar, Expand/Contract Cloth, Grab Planar Cloth, Pinch/Point/Perpendicular/Multi-Grab variants, etc.) — each isolates a specific behavior that used to be a buried option on one all-purpose brush. Low mesh resolution makes cloth brushes behave poorly; a Multiresolution modifier was found unreliable for this specific use, so the author prefers adding one Subdivision level in Object Mode and applying it directly for a denser, simpler mesh (25,600 faces in this example) that sculpts more predictably. Change brush radius with F; keep Strength low (≈0.1) for controllable, gradual fold-building rather than one strong stroke; hold Shift to smooth/blur an area back down if a brush pass goes too far.
8. **Efficient high-quality baking via a "keyframed rehearsal":** very high Cloth Quality/Collision Quality settings (e.g. Quality 80, Collision Quality 20) make live playback far too slow to interactively pose. Workaround: temporarily disable the Collision modifier's viewport display, enable Auto Keying, select the Hook Empty, press Play, move the Empty to the desired path/position, Pause, then disable Auto Keying — this records the Empty's motion as keyframes at low simulation cost. Re-enable the Collision modifier, raise Cloth/Collision Quality to the real target values, and click Bake — the simulation now recalculates using the recorded Empty keyframes at full quality (slow, but only needs to run once); a blue line in the timeline indicates the cache is baked, after which scrubbing just plays back cached results instead of re-simulating. Delete existing bakes before re-baking with changed settings.
9. **Tuning physical properties for the biggest visual impact:** of all the Cloth Physical Properties, **Vertex Mass** and **Air Viscosity** have by far the most visible effect on how the drape looks — the author recommends experimenting mainly with these two, since most other Physical Property values only produce very subtle differences. For the collision object, the **Friction** value strongly affects how easily the cloth slides across its surface (high friction = cloth "grips" and barely slides).
10. **Geometry sizing gotchas:** cloth simulations need a "reasonable" polygon count for their real-world size — too few faces (or an object that's too small in world scale) causes the cloth to visibly shrivel/crunch up during simulation; too many faces (or too large a scale) causes different but also undesirable behavior. In this example, 1,600 faces was found to be a good balance; doubling that caused simulation problems. If cloth is shriveling, try scaling the object up in Object Mode as a first fix.

### Nodes / Settings
- **Rig objects:** Collision modifier (on the base object), Cloth modifier (Shape > Pin Group, Self Collisions), Hook modifier (created via Ctrl+H > Hook to New Object; Object, Vertex Group, Strength, Falloff fields).
- **Vertex Groups:** used both for the Pin Group and (implicitly) for the Hook's vertex association.
- **Cloth Physical Properties:** Vertex Mass (most impactful), Air Viscosity (most impactful), Friction (on the collision object), Tension/Compression/Shear/Bending (Damping section — subtle effects).
- **Cache:** Physics > Cloth > Cache (must be extended to match a longer timeline), Bake button, cache-baked indicator (blue timeline bar), Delete Bake.
- **Sculpt Mode Cloth brushes (4.3+):** Drag Cloth, Bend Cloth, Bend Planar, Expand/Contract Cloth, Grab Planar Cloth, Pinch/Point/Perpendicular/Multi-Grab variants; brush Radius (F), Strength, Shift-to-smooth.
- **Other:** Ctrl+A > Visual Geometry to Mesh (bake simulation frame to static geometry), Auto Keying toggle (for recording Empty motion cheaply before a full-quality bake), Shift+Z (axis-lock movement while dragging with G), Shade Smooth + Subdivision Surface modifier (Ctrl+1) for a cleaner final look, per-object random Viewport Display colors (or Matcap shading) for easier visual debugging.

### Difficulty
Intermediate

### Blender Version
Blender 4.3 or later — the video explicitly states the Cloth sculpt brush was split into several dedicated brushes with previously-obscure options exposed, starting around this release.

### Tags
cloth, simulation, rigging, intermediate

---

## Related Tutorials
- [Blender Secrets - 5 mins of ArchViz Tips (Diamond Tufting, Pillow Edges, Pillows, Interactive Cloth)](blender-secrets---5-mins-of-archviz-tips-diamond-tufting-pillow-edges-pillows-in.md) — shares cloth, simulation, intermediate; that video's brief "Interactive Cloth" pillow-placement tip is expanded into the full Hook+Pin-Group rig and Blender 4.3 Cloth sculpt brushes taught here.
- [Daily Blender Secrets - 15 Tips Compilation (Part 2)](daily-blender-secrets---15-tips-compilation-part-2.md) — shares cloth, simulation; that compilation's Tip 13 "Flag" segment covers a simpler Cloth+Pinning+Wind setup, this video goes deeper on interactive posing via Hooks and the newer sculpt brushes.
