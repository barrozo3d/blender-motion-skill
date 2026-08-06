---
title: Extra Nodes v4.0 | Powerful New Tools for Blender Geometry Nodes - Full Demo
source: YouTube
url: https://www.youtube.com/watch?v=mS27dSXDSuc
author: 3D Singh VFX
ingested: 2026-08-06
blender_version: "Not specified — Extra Nodes v4.0 add-on demo, uses standard EEVEE viewport rendering, consistent with Blender 4.x"
tags: [geometry-nodes, procedural, simulation, animation, motion-design, abstract, advanced]
extraction_status: complete
frames_dir: tutorials/frames/extra-nodes-v40-powerful-new-tools-for-blender-geometry-nodes---full-demo/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Extra Nodes v4.0 | Powerful New Tools for Blender Geometry Nodes - Full Demo

**Source:** [YouTube](https://www.youtube.com/watch?v=mS27dSXDSuc)
**Author:** 3D Singh VFX
**Duration:** 28m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] NVG Analog
[0:06] どう Truly
[0:43] Hello everyone, the extra nodes version 4.0 is released with many new features and updates.
[0:56] This new update is really important if you want to create a really cool motion graphics
[1:00] with the extra nodes.
[1:02] So let's start with the new curve roller node.
[1:04] So you can add that from this asset browser or you can also add that from this admin.
[1:10] So we have this curve roller node and if we add that here, it's going to roll this curve
[1:16] and the rolling of this curve is going to be very physically accurate.
[1:19] Like it is not going to stretch or scale down the individual segments of the curve.
[1:23] It's going to basically roll the curve based on the angle.
[1:27] So let me lower the count here, maybe around 15.
[1:32] Then let me do something like this.
[1:36] And you will see that if I change this factor, see the inner radius of this role is not changing.
[1:48] So that is really important.
[1:51] And you can see that how the overall scale of this rolled curve is increasing.
[1:56] This is what we need to roll any like curve or sheet or paper physically.
[2:02] So that is the major feature of this node.
[2:06] So let's talk about the settings of this.
[2:08] So first you have the settings for the curve.
[2:11] So here you can define the sampling of this curve based on the count or length.
[2:17] Then you have the tilt.
[2:18] So you can define the tilt or you want to roll this curve relative to it is normal.
[2:25] And then you have the reverse option.
[2:26] So you can reverse the curve.
[2:29] In the role setting, first we have the role control option.
[2:32] So here we can roll this curve based on the factor that is 0 to 1 or we can use the length
[2:38] option.
[2:39] So here we can define the length to roll this curve.
[2:42] And then you have the option for the size, the role size.
[2:45] So you can define the radius or you can define the angle.
[2:48] So let me change this to length so that you can see this properly.
[2:53] So here we can define the radius, the initial radius.
[3:00] So it will be more clear if I make this angle 0 for the spiral.
[3:04] So now you can see the overall radius if I type 0.5.
[3:07] So we have the circle that is 1 meter and then we have the angle.
[3:13] So let me change this to count and let's unroll this.
[3:18] So basically you're going to define this angle like this angle from its original segment.
[3:25] So if I type here, let's say 90 degree, it will roll up to 90 and then it will move to
[3:31] the next segment.
[3:32] So you have something like this.
[3:35] Okay, or you can define 45.
[3:40] So it will roll something like this.
[3:44] And for this, you can also combine this option for the spiral and now it will be a spiral.
[3:53] Okay, and after that you have the option for the circular.
[3:58] So let me make this 0.
[4:00] So if you enable this option, it's going to roll this curve into a complete circle.
[4:05] If the spiral option is 0, the spiral factor is 0.
[4:09] So sometime you want to roll this into a complete circle so you can do that.
[4:13] So then you have the option for the spiral.
[4:16] To define the spiral, you have two options, angle and scale.
[4:19] Angle is very physically accurate.
[4:21] So it's going to only affect the angle of the segments.
[4:24] Okay, something like this.
[4:26] And if we roll this, see we have this spiral.
[4:31] But if we use the scale, it's going to scale the segment down to create this spiral.
[4:37] So in some case, probably you need that.
[4:40] So you can use this option.
[4:42] But it's going to have this kind of stretch effect.
[4:45] Okay, so that may be useful for some cases.
[4:49] And then you have the depth.
[4:51] Depth option allow you to offset this rolled curve along the rolling axis, something like
[4:57] this decrease the radius, probably 0.25 and also make this more spiral.
[5:06] You have this.
[5:09] So this also work with the curve that is circular.
[5:14] So we have something like this.
[5:16] And if I add that, so you have something like this.
[5:23] After this, you have the clip option.
[5:25] So that is really nice feature.
[5:27] With this option, basically you can clip the rolled curve into a certain angle.
[5:32] So if I enable this option.
[5:37] Let me also make the spiral zero.
[5:40] So then it will be more clear.
[5:42] See now we are clipping this to a 180 angle.
[5:46] If I make this 90, then we have something like this.
[5:52] So that is really nice.
[5:54] Like we can make this 180 and we can easily combine these two together to create a nice
[6:00] effect.
[6:01] So for this, I think we need to make this tilt 180 to decrease this roll factor, something
[6:11] like that.
[6:13] And now we have something like this effect.
[6:18] You can also affect this factor or you can also animate this one.
[6:23] These options are field based.
[6:25] So for example, we can use these curves, the multiple curves as input.
[6:31] So we have something like this.
[6:34] And here we can like input the noise texture.
[6:37] Okay, or you can also use the fall offs.
[6:41] So let's use that probably object sphere fall off.
[6:45] Let me connect this to this and also add the empty here.
[6:53] And then probably we can make something like this.
[6:58] So now with this empty, you can basically create this interactive rolling effect.
[7:07] Or you can also use the noise as well.
[7:14] So this is how you can use the curve roller.
[7:16] So next we have the recursive node or the recursive topology effect.
[7:20] So here we have this grid.
[7:23] Okay, and then we're going to add the recursive effect node.
[7:28] So let's add that here.
[7:30] It's going to basically recursively subbed by this topology of the discrete.
[7:38] So with this vector, we can basically animate this.
[7:41] And here you can define the number of iterations or the subdivisions.
[7:47] And this is really important settings.
[7:50] This is the alternate mode.
[7:52] Basically it's going to sequentially divide the each face.
[7:56] But if you use random, then it's going to randomly divide the individual faces to create
[8:02] this nice pattern.
[8:03] So here you can change the seed.
[8:06] So then you have the scale.
[8:08] So scale allow you to scale down these elements based on the relative scale or you can use
[8:14] the width.
[8:15] So with this, you can basically specify a fixed width for each segment.
[8:21] See all these have a same width.
[8:24] And then you have the advanced option that is allow you to basically remove the faces
[8:28] that have area less than this threshold.
[8:32] So next I'll show you it is important attributes.
[8:36] So let me enable this options.
[8:37] It comes with the seven attributes.
[8:39] So the first one is the random.
[8:42] So that is really important.
[8:43] With this, you can basically randomly assign the color variation or material to these faces.
[8:49] And after that, you have the face scale and then the local axis of the face and also the
[8:55] face orientation.
[8:56] So let's use these two.
[9:00] So what we can do, we can easily convert this to a points, mesh to points, change this to
[9:05] face.
[9:06] And here you can instance any geometry on these faces.
[9:10] Okay.
[9:11] And maybe grid.
[9:14] And first we need to plug this into this.
[9:16] It will align this grid properly.
[9:18] And then we need to plug this into this.
[9:20] So now we have this more resolution grid for each face.
[9:27] Or you can also use the icospere or other geometry.
[9:31] Let me make this point five because we need a one scale object here.
[9:37] So you have something like this.
[9:41] Or you can even use a complexity like if you want to create some kind of building, you
[9:47] can add these windows into these faces and create amazing motion graphics.
[9:53] And another thing is that this vector is a field based.
[9:57] So we can control that with the fault nodes and other custom fields.
[10:01] So let's try with the object follow up notes.
[10:04] So let me plug that here.
[10:06] And here I'm going to select this empty.
[10:09] So we have this probably one.
[10:13] Let me increase the base resolution maybe around five by five.
[10:18] This should be around four.
[10:22] Now we can move this empty.
[10:26] Now they are interacting with this.
[10:29] So that is really important if you want to create interactive motion graphics.
[10:33] So now you can do that.
[10:35] So next we have the cutters.
[10:38] If you want to create the effects of cutting metals like with the CNC machine, it's creating
[10:43] some kind of pattern with this node, you can do that.
[10:46] So let me add that.
[10:47] We're going to add the cutters mesh cutter node here.
[10:50] Here we have this cube that is rotating around this.
[10:54] And we're going to cut this big cube with the smaller one.
[10:59] Here we have this node.
[11:00] So here you can define the simulation parameters like start and end frame and also sub step
[11:05] if the cutter objects is moving fast.
[11:08] So you can add that.
[11:10] And here you can input your cutter geometry.
[11:13] If we plug this and run the simulation, see we have this effect that is cutting this
[11:20] geometry.
[11:21] So here you have a lot of option like you can basically stop this cutting enable this
[11:27] and then you can even stop that further.
[11:31] Then you have the different mode for that cutting like a manifold or exact mode.
[11:35] Exact mode is really computationally heavy.
[11:37] So I recommend you use some manifold option when you're this base mesh and also this cutting
[11:43] mesh is closed.
[11:45] Then you have the multi mesh option.
[11:47] So that is really important if you have this cutter object contain multiple meshed matrix.
[11:52] So you can enable that option to remove any artifacts.
[11:56] And after that you have this option like triangulate cuts.
[12:00] Basically you can triangulate this symmetry.
[12:02] So that is also really important to remove any artifacts during the rendering.
[12:07] And you can also add the UV map from this cube, the this cutter cube to the base geometry.
[12:12] So you can add that to add a material variation or if you want to add some kind of texture.
[12:17] These are the masks.
[12:18] So you have the cutter mask basically where this cutter object is.
[12:22] This is the total mask like this cutout mask.
[12:26] This is also really important in the cutter frame.
[12:29] With this you can create an animated mask for this region.
[12:32] So now you have this kind of mask.
[12:37] So next we have the geometry roller.
[12:40] So here we have these instances and we want to roll them.
[12:44] So you can do that with the geometry roller.
[12:47] So we can add that note from the effects and then you have the metroid roller.
[12:52] Just add that here.
[12:54] So here you have two options.
[12:56] You can roll the instances or you can also roll the geometry.
[13:00] So in the instances you need to define the group ID.
[13:03] So by default it's going to use the individual index of the instance as group ID.
[13:10] But sometime if you want to combine some of the instance as a single instance.
[13:14] So you need to define this group ID for that.
[13:17] And for the geometry same you have to input this group ID per per geometry because this
[13:23] input contains multiple geometries like we have multiple mesh islands.
[13:28] So you need to input that here so that it properly roll individual geometries.
[13:33] And in this case you have to also input it is world location.
[13:36] So you can use this option average.
[13:38] It will basically calculate the average location using the position field of the geometry or
[13:43] you can input the exact location.
[13:46] So that is the basic difference.
[13:48] So let's use the instances and then you have the translation options.
[13:52] So first you have the location option.
[13:54] So if we run the simulation we can roll this along the x axis, y axis something like this.
[14:04] Nice thing about this node is that it keeps the original offset of the input instances
[14:09] or geometry.
[14:10] So we can also roll these together using the empty location.
[14:14] So let me bring that empty here.
[14:16] So plug this into this.
[14:17] So we have this empty.
[14:19] So now if I go to the full screen and run the simulation, we can roll this something
[14:25] like this.
[14:30] And here you can define the basically normal or the upward direction for the rolling.
[14:36] And this is the offset basically offset from this XYZ plane, the world plane.
[14:42] And then you have really advanced option that is the curve.
[14:45] So you can roll all these instances along the path of the curve.
[14:50] So we have this curve and if we plug this curve here, it's going to roll all these instances
[14:57] along the curve.
[14:59] And this option also supports some multiple curves like you can define individual path
[15:03] for each instance.
[15:04] So you can input multiple curves here and it's going to map that according to their this
[15:09] ID, the group ID.
[15:11] Now if we basically animate this factor, it's going to roll these objects along the
[15:17] curve based on it is normal.
[15:19] See, it is rolling something like this.
[15:24] So right now we need to make this normal of this curve upward.
[15:28] So go to the normal and either you can basically make this a negative 90 degree or you can
[15:35] use this dropdown to specify the normal direction.
[15:39] So let's use this field and go to the first frame something like this and run the simulation.
[15:44] Now they are rolling along the this guy.
[15:50] You can also use this length parameter.
[15:53] You can roll these instances along the curve based on it is a length.
[15:57] And then you have the loop option.
[15:59] So loop option allow you to basically loop this animation.
[16:03] Let me put the first frame and then you have this offset option.
[16:13] So it will offset these instances or the geometry along the specified normal.
[16:21] So this is how you can use this geometry roller.
[16:24] So next we have the step force.
[16:26] So we have these particles.
[16:28] So we have these points and then I have added this XPB resolver node.
[16:33] So next we're going to add the step force node.
[16:38] This one go to the dynamics and add that here.
[16:41] Now if you run this, see these points are moving and for this effect, we need to decrease
[16:47] this velocity factor basically the velocity from the previous frame.
[16:52] And let me increase this maybe around 150.
[16:57] See we have this step motion and will be more clear if I basically trace these particles
[17:03] using this node.
[17:04] Okay, go to the first frame.
[17:06] So now we have this kind of path based on their motion of these particles.
[17:15] So in this node, you can use the axis like the world axis or you can use the basically
[17:20] the random axis.
[17:23] So you have something like this and then you can define the strength seed and the increment.
[17:30] So this is really important settings if I make this less say 15, it will take a big
[17:34] steps before any turn or we can do something like this.
[17:40] So we can make this around three at the start something like this and then we can make this
[17:47] around 20.
[17:52] So this is really a nice effect.
[17:54] You want to create some kind of electronics effect with this and an amazing thing about
[18:00] this force node is that we can also combine other forces to this like we can add the gravity
[18:05] here.
[18:06] Let's plug that here.
[18:08] Now if we run this, let me increase this maybe around 10.
[18:16] See we have this kind of effect.
[18:22] So this is the step force node.
[18:25] Nice thing about these forces nodes is that you can easily use them with the new solver
[18:30] like the XPV solver, the clock dynamics and the here dynamic like I have made this video.
[18:36] Probably you have seen that here I'm using this vertex turbulence force to create this
[18:41] kind of pattern from this cloth.
[18:44] So with this custom force node, you can easily use these nodes.
[18:49] So next we have the plexus.
[18:52] So let me add the plexus effect node.
[18:55] Just plug that here.
[18:57] It will engineer the plexus.
[19:01] So you have two options.
[19:03] You can use the surface and then you can distribute the points or you can use the direct points
[19:09] and then it will basically add the plexus.
[19:12] So here you have the animation option.
[19:15] So you can define the offset, the speed and then you have the noise texture types and
[19:21] you can define their scale and also the X by Z scale create a different motion for these
[19:26] particles.
[19:27] And then we have the points option.
[19:29] Basically you can join the original points with these lines, the plexus lines.
[19:35] See we have these hypospheres.
[19:37] You can also add the cube or you can also use the custom.
[19:41] And here you can basically define their radius, subdivision and the material.
[19:46] And after that you have the settings for the plexus.
[19:50] So first you have the general settings like the number of connections per point.
[19:55] So you can find that here.
[19:58] Option like the minimum and maximum distance.
[20:01] So if I make this five here and increase the minimum distance, maybe around point two.
[20:07] When these particles really close, we don't have any plexus line.
[20:11] Okay, so this is kind of minimum distance and this is for the maximum.
[20:15] So if the points are really far away, we can also break the lines or the lines will not
[20:20] form.
[20:21] So this is the radius for these plexus lines.
[20:23] If I add the profile, so this you can define the radius for these lines.
[20:29] Then we have the trim option.
[20:31] So we can trim these cars from the start side and also from the end side.
[20:36] Then you have the collision option.
[20:37] So that is really nice.
[20:39] So you can define the collision based on the selection or you can define the collision
[20:43] based on the geometry.
[20:45] So we have this cube.
[20:47] Let me add that here.
[20:49] So right now the setting is like that.
[20:51] The points only going to form the connection that are inside this cube.
[20:56] Okay.
[20:57] Or we can reverse that.
[21:00] See the connections only form the outside of this cube.
[21:06] It is 3D.
[21:07] That's why probably not clear.
[21:09] Let me make the scale.
[21:11] Is that scale zero?
[21:13] No.
[21:14] See.
[21:15] How we can also slightly increase the proximity distance.
[21:21] So that is really important settings.
[21:24] Like you can easily create or define the pattern within the plexus to reveal something.
[21:29] So here are the profile settings.
[21:31] You can use a circle or the custom curve to define the profile and other settings like
[21:35] resolution fill cap and the material.
[21:38] So this is how you can use the plexus node.
[21:40] So next we have the inflate solver.
[21:43] So in this node I have added the tier and the stiffness option.
[21:46] So let me add that here.
[21:49] So in the inflate now you have these panels and in the stiffness you have these two settings
[21:55] the shear and the compression.
[21:57] So let me run this.
[22:00] See it is inflating this.
[22:02] So you have two options.
[22:03] So these are kind of the limits for the shear and compression.
[22:06] Is how much shear is possible with this geometry during the inflation.
[22:11] If I make this 0.25 it going to inflate up to certain region and after that it going
[22:15] to like stop.
[22:19] It is no longer inflating and then you have the compression.
[22:22] So this is really important and it going to basically affect the faces that are really
[22:27] compressed.
[22:28] So let me disable this and let's make this 0.2.
[22:33] See the geometry is not inflating because this compression is really low.
[22:38] So we are not allowing the simulations to inflate the geometry.
[22:43] So let's make this 0.35.
[22:50] See it is slowing down the inflation for these faces.
[22:56] So these parameters are really useful when we use the tier option.
[22:59] So let me enable this option.
[23:01] So you have two mode either you can split the edges to add the tier or you can delete
[23:07] the points to add the tier.
[23:10] Then you have the threshold option.
[23:11] It can be static or dynamic and this is the threshold basically between the rest length
[23:17] and the current length of the edges.
[23:20] Let me decrease this around 0.15 and run this.
[23:25] Here start tearing from this side and as it reach this point so this region of the mesh
[23:36] basically reach this threshold and start.
[23:41] Cheer up.
[23:42] You can easily define this threshold based on the noise.
[23:47] See here we have a really small value for the noise that you start from there.
[23:58] Now we can also use the delete option.
[24:01] It gives you a different result.
[24:06] Let me add the shear as well.
[24:11] I mean this 0.5 and also 0.35 and make this split.
[24:22] And but if I disable this compression, see how the motion is changing.
[24:32] See their motion really fast.
[24:36] If I enable this option, it is going to slow this part down.
[24:42] So next we have the edge tracer.
[24:45] So here we have the mesh circle.
[24:48] So I'm basically animating it is position something like this and there is another copy
[24:53] of that where I'm animating it is scale based on this sound.
[24:58] So we have something like this.
[25:00] So we can trace this using this edge tracer node and if I delete this, so we have something
[25:07] like this.
[25:08] So here you can basically define the start and frame, the step and then the flip faces
[25:18] like you can flip that or these are the basic steps on what frame you want to trace.
[25:24] See we have something like this.
[25:27] With this node, you can trace any message or curve and this is really nice if you want
[25:32] to create some kind of trail effect behind any vector.
[25:35] So you can basically attach a curve or specify the edge.
[25:38] And with this, you can basically even easily generate the geometry.
[25:41] Here you can define that trail material.
[25:44] And the last we have the animated follow.
[25:46] So we have a lot of follow of nodes.
[25:49] Basically you can animate this follow based on the same object.
[25:54] But if you want to animate this field, the follow field, so I have added this node, the
[26:00] animated follow of node, you plug that here.
[26:03] So here you can define the start and frame for the animation.
[26:07] Let me make this around maybe 96 here and also 96 here.
[26:12] Then here you have to input the follow.
[26:16] Let me move that here.
[26:18] And with this, you can define the width or let me decrease the range and also make the
[26:23] noise zero so that you can see that with this, you can define this.
[26:28] Where you can also invert this.
[26:31] And this is basically the range.
[26:33] Let's make this around point 25 something like that.
[26:38] And then you have the smooth option.
[26:40] You can basically smooth this.
[26:42] And then you have a really important feature that is the noise.
[26:45] You can add the noise to this region.
[26:47] Okay, the width region, something like that.
[26:51] So now you have this kind of effect.
[26:56] We can also make this 40.
[26:58] Okay, add some speed to this noise.
[27:11] With this node, you can easily create the generative effect.
[27:16] So we have something like that.
[27:27] And because it is derived by the follow, okay, this follow field, so we can use any follow
[27:33] here.
[27:34] You can use any follow here for the animation like we can use follow from this curve.
[27:40] So we have this curve.
[27:41] Let me hide the empty object.
[27:45] You can even input our curve text object to create a.
[27:52] We have this kind of effect.
[27:59] Apart from these updates, there are also other important changes and fixes in the nodes that
[28:05] you can check from the log.
[28:07] Another thing is that all the intro project files are also available with this preset.
[28:11] So you can study them and create amazing effects with the extra nodes.
[28:15] All these project files and the presets are also available on my patron page.
[28:19] I hope you like this update.
[28:21] So thank you for watching.
[28:22] See you in the next video.
[28:23] Happy noting.
[28:24] Bye.



---

## Captured Frames

- [3:00] tutorials/frames/extra-nodes-v40-powerful-new-tools-for-blender-geometry-nodes---full-demo/frame_000.jpg
- [8:03] tutorials/frames/extra-nodes-v40-powerful-new-tools-for-blender-geometry-nodes---full-demo/frame_001.jpg
- [9:53] tutorials/frames/extra-nodes-v40-powerful-new-tools-for-blender-geometry-nodes---full-demo/frame_002.jpg
- [11:20] tutorials/frames/extra-nodes-v40-powerful-new-tools-for-blender-geometry-nodes---full-demo/frame_003.jpg
- [14:57] tutorials/frames/extra-nodes-v40-powerful-new-tools-for-blender-geometry-nodes---full-demo/frame_004.jpg
- [17:03] tutorials/frames/extra-nodes-v40-powerful-new-tools-for-blender-geometry-nodes---full-demo/frame_005.jpg
- [19:37] tutorials/frames/extra-nodes-v40-powerful-new-tools-for-blender-geometry-nodes---full-demo/frame_006.jpg
- [23:25] tutorials/frames/extra-nodes-v40-powerful-new-tools-for-blender-geometry-nodes---full-demo/frame_007.jpg

---

## Structured Notes

### Core Technique
A feature-tour demo of "Extra Nodes" v4.0, a paid third-party Geometry Nodes node-pack add-on, covering nine new custom nodes for motion graphics: Curve Roller (physically-accurate curve/paper rolling), Recursive Topology (recursive face subdivision patterns), Mesh Cutter (simulated CNC-style progressive cutting), Geometry Roller (rolling instances/geometry along an axis or curve), Step Force (a particle-dynamics force for stepped/electric-looking motion), Plexus (point-network line generator with collision masking), Inflate Solver with Tear (cloth-like inflation simulation with tearable seams), Edge Tracer (mesh/curve motion-trail generator), and Animated Follow (keyframed follow-field driver).

### Summary
Frame 000 shows the Curve Roller node (KS_Curve_Roller) wired between a Curve Circle/Curve Line + Set Curve Radius chain and the Group Output, its parameters visible (Selection: Curve/Roll, Factor 1.700, Radius 0.43m, Circular, Spiral, Angle 0.17, Scale 0.000, Depth, Clip) — with a spiral curve shape shown top-left, demonstrating the node's physically-accurate rolling (no segment stretching). Frame 001 shows the Recursive Topology node (KS_Recursive_Topology) fed by a Grid, with Iterations, Seed, and Factor (0.494) fields, producing a rectangular recursive-subdivision pattern on a flat grid viewed from Top Orthographic. Frame 002 shows the same Recursive Topology node applied to a circular grid/disc shape, Iterations/Seed/Factor visible again (Factor 0.398), demonstrating the effect works on non-rectangular base topology too. Frame 003 shows the Mesh Cutter node (KS_Mesh_Cutter) — a Cube's Mesh and UV Map feeding into Cutter Frame/Cutter Mask/Cut Mask outputs, a rotating smaller cutter cube (Transform Geometry, Rotation/Scale 0.250) driving progressive simulated cutting into the larger cube's corner, joined via a Join Geometry node before Group Output. Frame 004 shows the Geometry Roller node (KS_Geometry_Roller) taking Instances from a Collection Info node and a Curve from an Object Info node (Bezier Curve, As Instance), with Group ID, Translation, Curve (Animate, Normal, Offset) inputs — rolling small cylinder instances along a curved path in the viewport. Frame 005 shows the Step Force node (KS_Step_Force) feeding into an XPBD Solver node (KS_XPBD_Solver) alongside a Distribute Points on Mesh Surface node — Force/Selection/Axis/Strength/Seed/Increment fields visible, driving jagged, stepped particle-trail motion from a scattered point cloud on a plane. Frame 006 shows the Plexus node (KS_Plexus) with Mesh/Surface/Distribution/Animation/Points inputs, Join Points enabled, Ico Sphere point-markers (Radius 0.01m, Subdivisions) — generating a sparse network of connecting lines between scattered points on two separate point clusters. Frame 007 shows the Inflate Solver node (KS_Inflate_Geometry) with Simulation/Inflate/Weight/Dynamic/Stiffness sections — Enable Shear, Enable Compression (0.350), Enable Tear (Split mode, Threshold 0.002, Static) all checked — inflating a flat subdivided plane (80×80 vertices) into a pillow-like puffed shape.

### Key Steps
1. **Curve Roller (KS_Curve_Roller):** feed a Curve into the node; it rolls the curve physically accurately — individual segments don't stretch or scale, only the overall roll angle/scale changes. Curve settings: sample by Count or Length, Tilt (roll relative to the curve's normal), Reverse. Roll settings: Roll Control via Factor (0-1) or Length; Size via Radius or Angle; a Circular toggle rolls the curve into a complete circle (when Spiral factor is 0); Spiral mode via Angle (physically accurate, affects only segment angle) or Scale (visually stretches segments, sometimes desirable for a different look); Depth offsets the rolled curve along its rolling axis (also works on circular curves); Clip trims the rolled result to a specific angle range, combinable with Tilt for creative partial-roll effects. All roll inputs are field-based, so they can be driven by multiple curves, Noise Textures, or Falloff nodes (e.g. an Object/Sphere falloff linked to an Empty) for interactive or procedural rolling animation.
2. **Recursive Topology (KS_Recursive_Topology):** recursively subdivides a mesh's existing face topology (works on a Grid or other base mesh). Mode: Alternate (sequential per-face division) or Random (randomized per-face division with a Seed) for more organic patterns. Scale controls per-element shrink (Relative Scale or a fixed Width per segment). An Advanced option removes faces below an Area threshold. Ships with 7 useful output attributes including Random (per-face color/material variation), Face Scale, Local Axis, and Face Orientation — the latter two enable instancing new geometry onto each generated face (e.g. Mesh to Points → Instance on Points, aligned via the Local Axis/rotation outputs) to build things like architectural window grids or complex generative motion graphics; the driving Vector input is field-based and can be controlled by an Object Follow-Up node linked to an Empty for interactive control.
3. **Mesh Cutter (KS_Mesh_Cutter):** simulates progressive CNC-style cutting of one mesh by another moving cutter object over a frame range. Simulation parameters include Start/End Frame and Sub Steps (raise for a fast-moving cutter). Cutting Mode: Manifold (fast, requires closed/manifold base and cutter meshes) or Exact (much more computationally expensive, more robust for non-manifold geometry). A Multi Mesh option removes artifacts when the cutter input contains multiple separate mesh islands. Triangulate Cuts reduces rendering artifacts at cut boundaries. The node can transfer the cutter's UV map onto the base geometry for material/texture variation at cut regions. Outputs include a Cutter Mask (where the cutter currently is), a Cutout Mask (the accumulated cut region), and a Cutter Frame output for building an animated mask of the cut area over time.
4. **Geometry Roller (KS_Geometry_Roller):** rolls either Instances or raw Geometry along a translation axis, an Empty's location, or a Curve. For Instances, a Group ID (defaults to per-instance index) lets multiple instances be rolled together as one logical group; for raw Geometry (which may contain multiple mesh islands), a Group ID must be supplied per-island, along with a World Location method (Average, computed from the geometry's position field, or an exact location). The node preserves each input's original relative offset while rolling. Curve-based rolling supports multiple curves mapped per Group ID (individual paths per rolled group), rolling based on curve Length, with a Normal direction control (numeric angle or dropdown preset) to orient "upward," a Loop option for seamless looping animation, and an Offset for positioning instances along the specified normal.
5. **Step Force (KS_Step_Force, under Dynamics):** a custom force node for particle/XPBD simulations that produces sharp, stepped, "electric"-looking motion rather than smooth motion — tune by lowering the Velocity Factor (how much previous-frame velocity carries over) and raising Strength; Axis can be World or Random per particle; Seed and Increment control the step pattern's variation and step-size progression over time (e.g. small steps early, larger steps later). Combinable with other forces on the same particle system (e.g. stacking a Gravity node) since it's built to compose with the newer solvers (XPBD Solver, Cloth dynamics, Hair dynamics) — the author notes using a similar Vertex Turbulence force node on cloth for a separate video's effect.
6. **Plexus (KS_Plexus):** generates a network of connecting lines between a point cloud, either distributed procedurally from a Surface or fed Direct Points. Animation options: Offset, Speed, and configurable Noise Texture Type with independent X/Y/Z scale for varied per-particle motion. A Join Points option merges the original points into the plexus lines output. Point markers can be Ico Sphere, Cube, or a Custom mesh, with adjustable Radius/Subdivisions/Material. Plexus-specific settings: Connections per point (min/max), Minimum/Maximum Distance thresholds (points too close get no line; points too far apart also don't connect), line Radius/Profile (curve-based radius definition), Trim (shorten lines from the start and/or end), and a Collision option that restricts line formation to inside or outside a target collision object/selection — useful for revealing a hidden shape within the plexus pattern. Profile settings support a Circle or a Custom curve cross-section, plus Resolution, Fill Cap, and Material.
7. **Inflate Solver (KS_Inflate_Geometry):** a cloth-like simulation node that inflates a mesh, with Shear and Compression stiffness limits — Compression specifically affects how much heavily-compressed faces resist further inflation (a low Compression value can effectively halt inflation in already-compressed regions, while a higher value allows it to continue, just more slowly). An Enable Tear option adds tearing: Mode is either Split (splits edges to introduce a tear) or Delete (removes points instead, giving a different visual result); a Threshold (Static or Dynamic, comparing rest length vs. current edge length) controls when tearing triggers — a low threshold tears early, and the threshold itself can be driven by a Noise texture for organic, non-uniform tear patterns/timing. Disabling Compression while Shear/Tear remain active visibly speeds up and changes the resulting motion.
8. **Edge Tracer:** traces the motion of a mesh's edges or a curve across a frame range into new trailing geometry — define Start Frame, Step, and Flip Faces; useful for building motion trails behind any moving object, and the output can be assigned its own Trail material.
9. **Animated Follow:** drives a Follow field (as used by many of the pack's other Follow-based nodes) via explicit keyframed Start/End frame animation rather than tying it to a moving object directly. Feed it any Follow source (an Empty-based Follow, a curve-based Follow, even a text object's Follow) and control Width/Range, Invert, Smooth, and an animatable Noise (with adjustable speed) added specifically within the follow's width region — useful for building generative reveal/wipe effects driven by any follow field.

### Nodes / Settings
- **KS_Curve_Roller:** Selection (Curve/Roll), Factor, Radius, Circular, Spiral (Angle/Scale sub-modes), Depth, Clip, Tilt, Reverse — all field-based inputs.
- **KS_Recursive_Topology:** Iterations, Seed, Mode (Alternate/Random), Scale (Relative/Width), Advanced (Area threshold), output attributes (Random, Face Scale, Local Axis, Face Orientation).
- **KS_Mesh_Cutter:** Simulation (Start/End Frame, Sub Steps), Cutting Mode (Manifold/Exact), Multi Mesh, Triangulate Cuts, UV transfer, outputs (Cutter Mask, Cutout Mask, Cutter Frame).
- **KS_Geometry_Roller:** Instances vs. Geometry mode, Group ID, World Location (Average/Exact), Translation, Curve (Animate/Normal/Offset, multi-curve-per-group support), Loop.
- **KS_Step_Force:** Force, Selection, Axis (World/Random), Velocity Factor, Strength, Seed, Increment — composes with XPBD Solver, Cloth, Hair dynamics, and other force nodes (e.g. Gravity).
- **KS_Plexus:** Mesh/Surface/Distribution/Animation (Offset, Speed, Noise Texture Type + XYZ scale)/Points (Join Points, marker geometry, Radius, Subdivisions), Connections per point (min/max), Min/Max Distance, Radius/Profile, Trim, Collision (selection or geometry-based, invertible).
- **KS_Inflate_Geometry:** Simulation/Inflate/Weight/Dynamic/Stiffness, Enable Shear, Enable Compression, Enable Tear (Split/Delete, Threshold Static/Dynamic, noise-drivable), Self Collision, Collision.
- **Edge Tracer:** Start Frame, Step, Flip Faces, Trail material.
- **Animated Follow:** Start/End Frame, Follow input, Width/Range, Invert, Smooth, Noise (speed-animatable).
- **Complementary stock nodes used throughout:** Set Curve Radius, Object Info (As Instance), Collection Info, Distribute Points on Faces/Mesh Surface, Mesh to Points, Instance on Points, Transform Geometry, Join Geometry, Object Follow-Up node, Falloff nodes (e.g. Object/Sphere Falloff).

### Difficulty
Advanced (assumes solid familiarity with the Geometry Nodes editor and simulation zones; this is an add-on feature tour, not a from-scratch beginner lesson)

### Blender Version
Not specified — the Extra Nodes v4.0 add-on demo uses standard EEVEE viewport rendering and simulation-zone-based nodes (XPBD Solver, Cloth/Hair dynamics references), consistent with Blender 4.x.

### Tags
geometry-nodes, procedural, simulation, animation, motion-design, abstract, advanced

---

## Related Tutorials
- [Another Blender String Tutorial....But even Better This Time!](another-blender-string-tutorialbut-even-better-this-time.md) — shares geometry-nodes, simulation, animation, motion-design, procedural; builds a comparable string/curve-array effect from scratch with stock Simulation Zone + Noise Texture nodes, versus this add-on's KS_Geometry_Roller/Plexus shortcuts.
