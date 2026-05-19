---
title: Track Objects Using Align Rotation To Vector In Geometry Nodes – Blender Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=ZBZ26xQ9Pnk
author: Photini By Design
ingested: 2026-05-19
blender_version: "4.x"
tags: [geometry-nodes, animation, instancing, intermediate, attributes]
extraction_status: complete
frames_dir: tutorials/frames/track-objects-using-align-rotation-to-vector-in-geometry-nodes-blender-tutorial/
frame_count: 0
---

# Track Objects Using Align Rotation To Vector In Geometry Nodes – Blender Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=ZBZ26xQ9Pnk)
**Author:** Photini By Design
**Duration:** 22m22s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro / Brief [0:00]
**Transcript:** Hey folks, in this episode I'm going to show you how to track any object in  geometry nodes using the Align Rotation to Victor node. This technique is useful  for various different applications so it's worth taking the time to learn this  method so without further ado let's get to it. So open up Lender we're going to go


### Initial Setup / Concept Overview [0:15]
**Transcript:** to Edit Preferences and Under Add-ons we're going to search for node and then  enable the node Wrangler here. Once you've enabled that we're going to click this  button and click Save Preferences and that will ensure the node Wrangler loads  every time we load Blender we'll then close this window here. In my 3D view  port with the default cube selected I'm going to hit numpad one to go into  Front View, I then tab into Edit Mode, I'm going to hit G, Z, I'm going to hold down  Control to snap it to the grid and I'm going to bring it up to right about  there. Just over base is in line with the origin of N hit S, Shift Z and that will  scale it on all axes excluding these Z axes of N hit 0.1, I hit Enter. I'll now  toggle into X-ray view, I'm going to box select these top vertices here, I'm going to  hit G, Z and I'm going to snap them down to five units, I'll then hit E to  extrude, S to scale and I'll scale it by two, I hit Enter, I'll then hit E, Z, I'm  going to hold down Control to snap it to the grid and I'm going to bring it up  to a random out there, I'll then hit S.1 Enter, tab out of Edit Mode, I'll just  toggle off X-ray view in my Outliner, I'm going to rename this object ...


### Geometry Nodes Tracking Sub System [2:20]
**Transcript:** cursor to the bottom left of the 3D viewport until I see a crosshair, I'll left  click and drag up and open up a new window, I'll then change this window from the  3D viewport to Jomitronode Editor, in the Jomitronode Editor, I'm going to click  New and I'll rename this to Follow Target, I'm going to hit End, Tardin  panel, the first thing we need to do is distribute points on this Icosphere  and then we can create instances on those points, so I'll take this group  input, I'll just drag this over to here for now, I hit Shift-A and I'm going to  search for Distribute and I'll select Distribute points on faces and I'll pop  that there, I'm going to change it from random to Poison Disk, I want to CD  Original Jomitry, so I'm going to hit Shift-A and search for Join and we'll  choose Join Jomitry and I'll pop that there, I'll then connect the original  Jomitry from the group input into the Join Jomitry, so now on each of these  points we want to create an instance of this arrow, so I hit Shift-A and I'll  search for Instance and we'll choose Instance on points and I'll pop that in  between there and the object we want to instance will be the arrow, so I'm  going to go to my Outliner a...


### Geo Nodes Scale By Distance System [5:00]
**Transcript:** going to take this step further, I'll just box select these nodes here, I'm going to  hit G, I'll bring these across over to here, I'll then grab this one and bring  this over to here, in fact I'll just bring this down here, for this next part  I want to be able to scale these arrows based on the distance of the target  object, so I'm going to take these three nodes here, I'm going to hit Shift-D to  duplicate and I'll pop these there, and on the Vector Math node I'm going to  change it from Subtract to Distance, I'll then hit Shift-A and I'm going to  search for Maths and I'll pop that there, I'm going to change it from Add to  Multiply Add, I'll then connect the Value Socket from the Vector Math node  into the Value Socket of the Multiply Add node, I'll hit Shift-A and I'll  search for Combine and I'll choose Combine XYZ, and I'll pop that there, I'll  then connect this Value Socket into the X Socket, the Y Socket and the Z Socket,  I'll then connect the Vector Socket from the Combine XYZ into the Scale Socket of  the Instance on Points, I'll set the Multiply on the Multiply Add node to a  negative number, so I'll probably set this to negative one, and this will serve as  the min...


### Automate Target Location Using F-Curve Modifiers [6:33]
**Transcript:** I'm just going to add another empty object in my 3D viewport, I'll hit Shift-A, I'll  go empty, and I'll choose Sphere, I'm going to hit numpad 7 to go into top view, I'll  then go to my empty data tab over here, and I'm going to increase the size to, let's  say, 4 meters, I'll then select the Senti Object, which is our Target Object, I'm  going to hold down Shift and left click select the other empty object, I'll then hit  Control-P, and I'll choose Set Parent to Object, keep transform, for this  empty object in my Outliner, I'm going to rename this to empty master, I'm going to go  to the top left of my 3D viewport until I see a cross here, or left click and drag  across and open up a new window, I'll then change this window from the 3D viewport  to the graph editor, and with your empty master object selected, I'm going to go to my  Object Data tab over here, and with my timeline set to 1, I'm going to add a keyframe  on the X rotation, Y rotation and Z rotation, I'll then navigate to the graph editor, click  this Modifiers tab over here, I'll expand the empty master action, I'll expand the  Object Transform, I'll then select the X oil up rotation, I'll then click Add Modifier  a...


### Bonus Free Procedural Eye [9:25]
**Transcript:** this a bit more interesting, so just as a bonus, I've uploaded this procedural eye onto my Patreon,  where you can download it for free, I'll leave a link to it in the description, so download  the file, we'll then hit F4, and we'll choose Append, locate the file procedural eye,  FOTINY BY DESIGN, double click the blender file, locate and double click the object file,  and then select Eye Procedural, we'll then click Append, I'll just grab that eye, I'm going to hit G,  X, I'm going to hold down Ctrl, snap it to the grid, and I'll just bring it over to here,  I'm going to go to my Render's tab, over here, I'm going to change it from EV to Cycles,  I'm going to change my device type from CPU to GPU, and just so we can see it, I'm going to take  the default light, I'm going to hit Delete, I'll then hit Shift A, I'll go Light, and we'll choose  Sun, I'll then navigate to my Light Data tab, over here, and I'm going to change the Strength to  10, I'll just toggle on to Rendered View, just to make sure it's working, excellent, I'll take the  cursor to the top right of the Jomitru No Data tab, until I see a crosshair, I'll left click and  drag across and open up a new window, I'll then ch...


### System Management [11:22]
**Transcript:** period, I'll take my cursor to the top right of the Jomitru No to Window, until I see a crosshair,  I'll left click and drag across, and we'll just collapse that window there, so now all we have to do  is locate the arrow instance object, and we'll click in here, and we'll change it from arrow to  eye procedural, obviously these eyes are way too big at the moment, and to reduce the scale on  this Multiplow node, I'm going to take the Add-In to let's say 0.5, maybe I'll take it up to 0.7,  I'll just orbit round, okay, so now if I hit play, you should see that the eyeballs are following  the object, excellent, so with the ICO sphere selected, navigate to your Material tab, over here,  we'll click new, and we'll rename this material to base, I'm just going to change the base color to  black, and I'll increase the roughness to 1, I'll just increase my Jomitru node window,  let's just get a bit more organized, I'll then box-select these nodes here, I'm going to hit F to  add a frame, and I'll rename the frame to track target, and I'll just drag this down to here,  I'll then box-select these nodes here, I'm going to hit G, bring these down a bit, I'll then hit F to  add a frame, and I'll...


### Camera / Lights [12:37]
**Transcript:** I'm going to skip back to frame 1, and with the ICO sphere selected, I'm going to hit numpad 1,  numpad period, I'll then hit control, out numpad 0, that will align the camera to the 3D viewport,  I'll then select my camera, I'm going to go to my object data tab, over here, I'm going to change  the x location to 0, and the z location to 0, and maybe I can drag it back on the y axis until  everything is encompassed in the frame, in the outliner, I'm going to hide the arrow from the 3D viewport,  and from render, and I'll also do the same for the eye, I'll then toggle on solid view, I'm going to  select my tracking object, I'm going to hit shift S, and I'll choose cursor to selected, I'll then  hit shift A, I'm going to go light and add a point, and with the point light selected, I'm going to  hold down shift, and left click select the target empty object, I hit control P, and I'll select  object key transform, so now if I hit G and grab the empty object, you can see that the light is  parented to that target object, and that will make it look like the eyes are tracking to the light  source, I'll just hit numpad 0, in my outliner, I'm going to select my sun lamp, I'm going to hit  de...


### Use Case Example [14:05]
**Transcript:** this geometry node tracking system isn't just restricted to an icosphere, it can work with a plane  or any other object, so I'll just give you an example quick, so in my 3d viewport, I'm going to hit  shift C, and that will recenter the cursor to the world, I'll then hit shift A, I'm going to go  mesh, and I'll choose plane, I'll tab into edit mode, I'm going to hit R, X, 90, I'll then hit S  4 to scale up by 4, and I'll tab out of edit mode, I'm going to go to my modifiers tab over here,  I'm going to click add modifier, and I'll go to geometry nodes, I'll then click this button here,  and I'll select the follow target, I'll then navigate to the outliner, and I'm going to hide the  icosphere object, I'll then select my target empty object, I hit G, Y, I'll bring this forward,  I'll then hit numpad 1 to go into front view, I'll then hit G, and I'll drag this around, and as  you can see all of the eyes are tracking the target object, I'll just re-enable the icosphere,  I'm going to go back to frame 1, I'll then hit numpad 3 to go inside view, I'll then hit G,  I'm going to hold down control, snap it to the grid, and I'm going to bring this target object  right back to the master emp...


### Additional Dynamic Features [15:12]
**Transcript:** more feature to this system just to make it a bit more dynamic and easier to use, so if your icosphere  is selected, I'm going to increase my geometry and open window up here, I'll then take this group  input, I'm going to hit shift D, and I'm going to bring it down to here, and under this scale target  subsystem, I'm going to take this socket from the object info, and plug it into the bottom socket  of the group input, I'll just hit end to open up the m panel, navigate to the group tab up here,  and then select the object group socket, I'm going to double click here, and I'm going to rename this to  scale target, and now as you can see we can change the target on the fly, I'll then go to this  track target subsystem, and I'll connect the top socket from this object info into the bottom  socket of the group input, I'll then navigate to the group tab on my end panel, I'll then navigate  and select the object socket on the group sockets, and I'm going to rename this to  track target, I'll just hit end, I'll expand my 3d viewport, maybe I'll select this plane,  I'm going to tab into edit mode, I'm going to hit S, I'm going to hold down control, snap it to the  grid, and I'm going to b...


### Exposing Extra Controls [18:17]
**Transcript:** if you're experiencing this problem here where your target object has gone too far,  and your instances are pointing in the wrong direction, we can find tune up, that's an easy enough  fix, so we just select the geometry node system, we're going to zoom in to this scale target element,  and on your multiply ad node we can just reduce the multiplier, so for example we can set this to  minus 0.05, and that should cure the problem, obviously this is affecting both of the objects,  so it's affecting the plane and the icosphere, so maybe we could actually expose these values here,  so I'm just going to set this back to minus 0.1, I'll just expand the geometry node window,  this was a bit of an oversight by me, so I'll connect this multiplier into the bottom  socket of the group input, and I'll also connect the add-in socket into the bottom socket of the  group input, in hindsight a matte range node would have probably been better in this multiply ad node,  I'm going to select the group input, I'm going to hit end, and with your group tab selected,  we'll navigate to the group sockets, and I'll double click the multiplier, and I'll rename this to  minimum scale, I'm going to scroll down,...


### Finishing Touches [19:51]
**Transcript:** I think for this plane object, I'm going to add the same material as the iCosephere,  I'm just going to do a quick scene setup, so with this plane selected, I'm going to hold down shift,  and left click select the target to object, I'll just hit numpad free, to go inside view,  g, y, I'm going to hold down control, snap it to the grid, and I'm going to bring this down to  random out there, I'll then select the target to object, I'm going to hit shift s, and I'll choose  cursor to selected, I'll then hit shift a, I go light, and I'll choose point, with the point  light selected, I'm going to set the power to 500 watts, I'm going to increase the radius to 0.025,  I'll then change the color to blue, in my 3D viewport, I'm going to hold down shift,  left click select the target to object, I'll then hit control p, and we'll set parent to object,  keep transform, so now this blue light is parented to this empty object, and this light here is  parented to the other empty object, in fact we can give this another color, so maybe I'll set this  orange, I'll just hit numpad zero, to go into camera view, I'm going to select the plane object,  I'll tap into edit mode, I'm just going to hit s, h...



---

## Structured Notes

### Core Technique
Object tracking in Geometry Nodes using `Align Rotation to Vector`: instances on a surface continuously face a target object by computing the direction vector from each instance to the target via `Object Info` + `Vector Math (Subtract)`, then feeding that into `Align Rotation to Vector` on the rotation socket of `Instance on Points`.

### Summary
22-minute tutorial building a reusable GeoNodes tracking system where icosphere-distributed instances (arrows, later procedural eyes) always face an animated target object. Extends to scale-by-distance (instances grow/shrink based on proximity), exposes Track Target and Scale Target as group inputs, and automates the target path with F-Curve Modifiers for a fully procedural orbiting pattern. The GeoNodes modifier is reusable on any object.

### Key Steps
1. **Setup** — Enable Node Wrangler; model a simple arrow mesh as the instanced object
2. **Distribute points** — Add GeoNodes modifier to base object; `Distribute Points on Faces` (Poisson Disk) + `Join Geometry` to keep original; `Instance on Points` with arrow as object
3. **Track target** — `Object Info` (target empty) → Position output; `Position` node (instance positions) → `Vector Math: Subtract` (target pos − instance pos) = direction vector; plug into `Align Rotation to Vector` → Rotation input of `Instance on Points`
4. **Scale by distance** — duplicate the subtract nodes; change `Vector Math` to `Distance` → `Multiply Add` (multiply=negative, controls min size) → `Combine XYZ` (same value on X/Y/Z) → Scale socket of `Instance on Points`
5. **Automate target orbit** — parent target Empty to a master Empty; in Graph Editor add F-Curve Modifier (Cycles) on X/Y/Z rotation of master → target orbits procedurally without keyframes
6. **Expose controls** — connect Target Object socket to Group Input; expose as "track target" and "scale target" GeoNodes group inputs; now reusable on any object
7. **Re-use** — apply same GeoNodes modifier to a plane, change instance object from arrow to procedural eye; all instances track the moving target

### Nodes / Settings
- `Distribute Points on Faces` — mode: Poisson Disk for even spacing
- `Object Info` — Location output gives world-space position of target
- `Position` — per-instance world position
- `Vector Math: Subtract` — target_pos − instance_pos = tracking direction
- `Align Rotation to Vector` — Vector input = direction; Axis = Z (or match arrow's forward axis)
- `Vector Math: Distance` → `Multiply Add` → `Combine XYZ` → Instance Scale (scale-by-distance)
- F-Curve Modifier: `Cycles` on rotation channels (before: Repeat, after: Repeat Offset)
- Group Inputs: expose "track target" (Object) and "scale target" (Object) for reusability
- Node Wrangler: Ctrl+T for quick texture setup

### Difficulty
Intermediate

### Blender Version
4.x

### Tags
geometry-nodes, animation, instancing, intermediate, attributes

---

## Related Tutorials
- [[all-300-geometry-nodes-in-blender]] — reference for Align Rotation to Vector and Instance on Points
- [[using-geometry-nodes-for-vfx-in-blender]] — VFX applications of GeoNodes
- [[a-new-way-to-loop-animations-in-blender]] — F-Curve modifier looping technique used here
