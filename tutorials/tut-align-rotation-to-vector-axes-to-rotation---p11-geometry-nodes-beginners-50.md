---
title: [Tut] Align Rotation to Vector & Axes to Rotation - P11 Geometry Nodes Beginners 5.0+
source: YouTube
url: https://www.youtube.com/watch?v=bZXZNEiKlNg
author: Bradley Animation
ingested: 2026-08-17
blender_version: "5.0+ (stated in title; UV Tangent node specifically called out as new in 5.1)"
tags: [geometry-nodes, procedural, animation, motion-design, intermediate, advanced, blender-5x]
extraction_status: complete
frames_dir: tutorials/frames/tut-align-rotation-to-vector-axes-to-rotation---p11-geometry-nodes-beginners-50/
frame_count: 9
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# [Tut] Align Rotation to Vector & Axes to Rotation - P11 Geometry Nodes Beginners 5.0+

**Source:** [YouTube](https://www.youtube.com/watch?v=bZXZNEiKlNg)
**Author:** Bradley Animation
**Duration:** 28m9s | 17 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Recap of Pick Instance [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, this is Bradley. Welcome to the 11th episode of the beginner series on geometry nodes.
[0:06] I hope you have watched the previous episodes because they will make today's topic much easier to follow.
[0:12] Last episode we talked about picking instances, which is one kind of basic but useful way to fake instance variations.
[0:21] On this grid, imagine these different geometries as different shapes of flowers.
[0:26] Then we could have different variants instanced in different places, which seems like we are having different flowers generated.
[0:34] We also discussed the instance index in resolving certain issues about some obvious patterns.
[0:42] In this episode and the next episode, we are going to talk about transform aspects of instances,
[0:49] which are basically rotation scales. Therefore, today we will specifically focus on the rotation aspects of it.
[0:58] Here we have a basic example where I start with a UV sphere and instance cones onto our sphere.


### Align Rotation to Vector [1:00]
**Transcript (timestamped):**
[1:06] The result looks very ugly with the default rotation, and my goal is to make these cones pointing outwards from our UV sphere.
[1:16] This is the moment when we need to use a line rotation to vector. The idea of this node is very simple.
[1:23] We need a directional vector, which I explained in episode 6. It's a vector relative to the word origin used to draw an arrow.
[1:34] So here, 0, 0, 1 in the default setting simply means it asks the rotation of every instance to face upwards.
[1:42] Then we set up an axis to decide which axis of these instances should point towards the assigned direction.
[1:51] In this case, I will keep using the default Z axis, which I also think is the most common one.
[1:58] As we output it to the rotation socket, it does not change anything because our instances were already using their Z axis, with the tip facing upwards by default.
[2:10] Here, I change the direction to 1, 0, 0 instead. You find that all cones are facing towards the positive region of our axis axis.
[2:20] And so on. So how can we make them face outwards? We use normal direction, which is supposed to be perpendicular to the surface,
[2:30] and therefore determines how light is reflected over the surface.
[2:35] We have two types of normals, which I will explain later. For the moment, using either one will be fine.


### Instance on Face Center with Aligned Rotation [2:40]
**Transcript (timestamped):**
[2:43] Now, our cones are facing outwards correctly. Here, let's go to another example.
[2:51] I start with a cube to do basically the same operation with a line rotation to vector using the normal. It's working as expected.
[3:01] These point normals on the corners are pointing outwards from these sharp corners.
[3:08] Nevertheless, I want to instance my cone on the face center instead of on points.
[3:14] So I prepare mesh two points in face mode to create points on the face centers.
[3:20] However, once we do that, you find our rotation is not working.
[3:25] The reason is simple. The mesh contains normals to reflect the light. Points do not naturally contain these normals, as we discussed in episode 4.
[3:36] So we could use capture attribute to preserve the normal while it is still a mesh.
[3:43] And these normal will be available after it's converted into points.
[3:48] Right now, it seems to work correctly with capture on points domain.
[3:54] But if you increase the subdivision, then you can see how the point normal influences these corners and makes them tilted.
[4:03] Capture on face domain will make everything better.
[4:06] Besides capture attribute, I have also discussed other methods, such as sample index by index and so on.
[4:14] You can choose whatever methods you like. We never have only one method to achieve a result.
[4:20] Your brain is more important than the software.
[4:24] So far, it seems a line rotation to vector with normal can solve tons of problems.
[4:30] Nevertheless, this is not the end of the story.
[4:34] So far, we have always been using cones.


### Axes to Rotation [4:35]
**Transcript (timestamped):**
[4:38] Going back to our initial example on the sphere, if you replace the cone with a special Susan head, whose face is facing upwards,
[4:48] you will find our Susan on the sphere is somehow tilted. I believe this is not what you would expect most of time.
[4:57] So what's the problem here?
[5:00] There is actually a conceptual limitation within a line rotation to vector.
[5:05] Here I have an empty with three axis shown.
[5:09] As I mentioned before, a line rotation to vector aligns a single axis to a specific direction, like asking the empty to look upwards.
[5:21] But now I duplicate my empty and rotate it on the z axis.
[5:26] While keeping the z axis intact, which is always looking upwards, the x and y axis are facing different directions compared to before.
[5:36] There are limited options where the x and y axis should face.
[5:41] And this is why we have issues in this case with our Susan head.
[5:46] Blender fulfills our requirement by using the z axis to face the normal and cause it a day.
[5:53] The other axis are usually chosen based on some hidden logic written in Blender's code.
[6:01] You should not expect them to be extremely reliable because they are not.
[6:07] So, a line rotation to vector is usually sufficient if you only care about one axis, such as cones, eyeballs, and so on.
[6:17] But if you are looking for specifically designated rotations, such as Susan heads or flower petals, then you need a more reliable method.
[6:29] The solution is very simple. You just need another line rotation to vector to choose another axis, whether it's x or y.
[6:39] So we input the previous rotation and output it. You can see some immediate changes, which are actually disrupting our previous rotation.
[6:49] Susan is now facing more horizontally instead of the previous tilted direction going outwards.
[6:56] So to keep the previous z axis rotation intact, it should be the pivot of our rotation, just like how we rotated our empty.
[7:06] The previous axis should become our current pivot.
[7:10] Now, you can see our Susan head is aligned in a more formal way.
[7:15] If you don't like it, I guess changing it to y is what you really expect.
[7:21] So here I have finished explaining the entire line rotation to vector node.
[7:27] The factor is just a mixed factor for the rotation. You can find it in the mixed rotation node.
[7:34] I don't think I've used it much in practice. Nowadays, these two aligned rotation setups have been combined into a new node called axis to rotation.
[7:46] Now I believe I don't need to specifically explain how to use it.
[7:51] You just set the first axis and the second axis along with their vectors and you're good to go.
[7:58] The results are basically the same and you don't need to specifically set up a pivot anymore.


### How about always using Axes to Rotation? [8:00]
**Transcript (timestamped):**
[8:04] At this point, while making this tutorial, I came up with a question.
[8:10] If axis to rotation is more accurate, why don't we always use it?
[8:15] To be honest, I don't have a definitive answer to this. I guess you can always use axis to rotation.
[8:22] I just don't do that myself because of historical reason and using aligned rotation for some simple cases is sufficient, such as for a comb.
[8:33] Or another use case I can think of is that aligned rotation can modify an existing rotation.
[8:40] For example, from the object info node, you only get a rotation and nothing else.
[8:47] So, aligned rotation to vector is one of the possible ways to modify the rotation compared to axis to rotation.
[8:54] It's just a thought. It doesn't necessarily have to be true.
[8:59] But anyway, I will move on to the next topic.


### Track to Constraint for Instances [9:00]
**Transcript (timestamped):**
[9:03] Here we have lots of Suzanne Heads instances are in grid and I have an empty object called the target.
[9:10] My goal is to make these Suzanne Heads face towards this empty object.
[9:16] Similar to what happens with the track 2 constraint.
[9:20] Since we are only dealing with a single axis, I will use aligned rotation to vector for the moment.
[9:27] Of course, you can always use axis to rotation by setting up the primary axis, whichever way you prefer.
[9:35] But for the directional vector, we need to deal with the location of our target and the position of our instances.
[9:43] How can we do that?
[9:45] The principle here is very simple. Here I have a graphical representation.
[9:50] We have the word origin at 0, 0.
[9:53] And imagine that our instance position is at 3, 0.
[9:57] While our target location is at 5, 0.
[10:01] My goal is to generate an arrow starting from the instance position and pointing towards the target location.
[10:09] So, it should be drawn like this small arrow.
[10:13] Now imagine our target location and instance position as arrows drawn relative to the word origin.
[10:21] You will have a large target arrow and a smaller instance arrow.
[10:26] Their lengths will be about 5 and 3 respectively.
[10:30] Here you will find that the instance arrow plus our goal equals the target arrow.
[10:37] It's like 3 plus something equals to 5.
[10:41] So, the target arrow subtracting our instance arrow equals our goal, like 5 minus 3 equals to 2.
[10:51] Simple math, even elementary students can do it.
[10:55] So, what should we do exactly?
[10:57] We just use the target location to subtract the instance position.
[11:03] We can do it directly in nodes.
[11:05] Here it's not necessary, but I prefer to enable relative.
[11:09] And I will disable the instance in plane, so you can see clearly that the instances are looking towards my target object,
[11:18] where my empty moves to the other side.
[11:21] You will find that our Suzanne is flipped upside down.
[11:24] This is the moment where you can use axis to rotation instead to force an axis to look upwards.
[11:32] And now it's fixed.
[11:35] If you want instances to look away from the object, you just reverse this subtraction.
[11:42] There is nothing special about vector math.
[11:45] The principle is as simple as what's taught in elementary school.
[11:49] These arrows may seem fascinating or terrifying,
[11:53] but they are really just the graphical obstructions of very simple numerical math.
[11:59] And this math of drawing arrows is not only for directional vectors,


### Principles of Attraction & Repulsion, & Billboarding. [12:00]
**Transcript (timestamped):**
[12:04] it can also be used for actual position vectors,
[12:08] so that we can create attraction or repulsion animation, whichever way you like.
[12:14] I teach this section because it's a pretty common function that people need,
[12:20] such as billboarding in stylized art.
[12:23] Although in my real life practice, billboarding may not use exactly the same method for rotation,
[12:30] it follows a similar principle of subtracting values.
[12:34] The second reason I teach this section is because I want to give you an alternative example,
[12:41] where you use your own logic and methods to build a vector other than normal for rotation alignment.
[12:48] Here I'm only teaching tools,
[12:51] but in the end, it's human creativity and responsibility that decides what they are going to do with them.
[12:59] And here, we again go back to our initial case on the UBSphere.


### vector Tangent [13:00]
**Transcript (timestamped):**
[13:05] While our rotation works in this case,
[13:08] if you put 010 on the secondary axis in axis to rotation,
[13:14] the result will again become undesired.
[13:18] So it really depends on the rule we set for the second axis.
[13:22] Simple values are often too simple to accomplish complex tasks.
[13:27] And just like we have normal for the primary axis,
[13:31] we often need another complex factor for the secondary axis.
[13:36] We call it a tangent.
[13:38] If you search for a tangent, you will find the mass operations for tangents,
[13:43] but you will also find a node called UVTangent.
[13:47] And we also have a curved tangent node.
[13:50] These are what we are looking for.
[13:53] UVTangent is for meshes.
[13:55] Since only meshes can have UV maps,
[13:58] curved tangent is obviously for curves,
[14:01] which we will discuss later.


### Importance of using Node Assets [14:03]
**Transcript (timestamped):**
[14:03] The UVTangent node was only added in 5.1.
[14:07] Before that, you would need a very complex method to get similar results.
[14:13] I provided the file and assets, but no one was using them.
[14:17] Users wanted to construct the node trees after learning,
[14:21] and you don't need to learn those complex methods anymore,
[14:25] because finally, something that was simply provided in other software
[14:30] is not becoming available in geometry nodes.
[14:33] This node is quite simple to use.


### UV tangent [14:35]
**Transcript (timestamped):**
[14:36] It asks for a UV map, which is directly available in procedural geometry.
[14:42] So we just connect UV to UV.
[14:45] In other cases, such as when you are using geometry from object info,
[14:51] you may need the named attribute to access the UV map.
[14:55] Now, as I output these tangents to the secondary axis,
[15:00] we immediately get an expected result.
[15:03] If you are not satisfied with it, you can change the secondary axis.
[15:08] So this is the beauty of using a more accurate method.
[15:12] It's not only working in this simple case,
[15:15] but it's also expected to work in much more complex cases.
[15:19] Here, the UVTangent node contains two modes.
[15:23] The first mode uses a sophisticated algorithm.
[15:27] It has a specific name called MIGT space calculation.
[15:31] You don't need to know about it,
[15:33] but seeing it makes me sound more professional.
[15:36] So yes, I feel it's cool.
[15:39] Developers don't want you to be bothered by the name,
[15:42] so they simply call it exact.
[15:45] This method is a gold standard and accurate method,
[15:49] which is also used in other software.
[15:52] The other method is four times faster,
[15:55] but it can be slightly inaccurate.
[15:58] Here, let's zoom into the instances.
[16:01] And as I scroll through the menu,
[16:04] please pay attention to the viewport.
[16:07] You may see that Suzanne is slightly shaking
[16:10] because there are tiny differences between these two methods.
[16:14] The exact mode is the default,
[16:16] so developers probably want to promote the standard method,
[16:20] even if it may sound slower compared to the other one.
[16:24] But anyway, for CurbTangent, it's much more straightforward to use.
[16:30] You simply output CurbTangent and it's done.
[16:34] The example will be shown later,
[16:36] but for now, I want to discuss a little more about normal,


### Custom Normal & True Normal [16:40]
**Transcript (timestamped):**
[16:41] because we have two outputs.
[16:44] As we said, normal is used to determine how light is reflected from the surface.
[16:51] Sometimes, however, you don't want the light to behave exactly like in real life,
[16:57] such as when shading stylizes the characters.
[17:01] In this scenario, we need a custom normal,
[17:05] which is different from the true normal based on the mesh shape.
[17:09] It can also be used to fix our modeling perspective,
[17:13] such as making Suzanne appear to blend with the ground when it actually does not.
[17:19] Therefore, we have a custom normal that you can edit with the setMeshNormal node.
[17:26] The sharpness mode may not be obvious, but if you change it to free,
[17:31] you can see how you can intentionally set up a vector for a custom normal.
[17:37] True normal would be the real geometry normal.
[17:41] Therefore, unless you specifically set a custom normal, it will be the same.
[17:48] Also, CurbNormal shares the same node as the one for mesh normal.
[17:53] However, Curves do not have custom normal, so these two sockets will always be the same.
[17:59] As I said, CurbNormal is a different and unrelated story.
[18:04] Now, let's move on to discuss more about tangent and normal on Curves.


### Curve Tangent & Curve Normal [18:05]
**Transcript (timestamped):**
[18:10] Here I have a bezier circle, which has four points in total,
[18:15] and it's flowing in a clockwise direction.
[18:18] CurveTangent basically represents the direction of the curve flow, which we have previously seen.
[18:25] So they should appear like this from the four points to construct a clockwise flow.
[18:31] CurveNormal is not really used to reflect light.
[18:35] It's just an arbitrary direction perpendicular to the curve tangent while pointing somewhere.
[18:41] It can face left or right, up or down, depending on the algorithm defined in Blender,
[18:47] but it's meant to be mostly continuous and consistent along the curve.
[18:52] So if the normal of our first point is facing outwards,
[18:56] then the second point is unlikely facing inward and so forth.
[19:01] Now, as we finish discussing these two parameters, let's go to our example of instancing on a spiral curve.
[19:09] In practice, I think it's more common on curves to use tangent as the primary axis and normal as the secondary axis,
[19:19] but you can definitely do whatever you want.
[19:22] Regardless, now you can see that our Suzen has been oriented in a well-organized way.


### Rotate Rotation to modify existing rotations [19:30]
**Transcript (timestamped):**
[19:30] So far, we have discussed ways to generate accurate rotations.
[19:36] If the rotation is already set, how do we modify it?
[19:40] For example, in this case, the Suzen is upside down, which looks extremely ugly.
[19:47] Besides align rotation to vector, which we discussed previously, it's more commonly done with the rotate rotation node.
[19:55] We have a global option based on the word axis and a local option based on your specific rotation.
[20:02] Basically, I always use the local option.
[20:06] In this case, as we are using the z-axis to align with the curve tangent,
[20:12] rotating locally around the z-axis means rotating around the curve tangent.
[20:17] It's like rotating the stick of your barbecue on your curve.
[20:21] This way, we can make Suzen face more downwards.
[20:24] Of course, it's just rotating the existing rotation instead of asking Suzen to face somewhere.


### vector math: Cross Product [20:30]
**Transcript (timestamped):**
[20:32] But you probably get an idea of how it works and how to use it.
[20:36] For our last topic, I want to start with a concept of a vector mass operation called cross product.
[20:44] So far, when we construct rotations, we only need two axes at the maximum, like defining x and y.
[20:52] The z-axis of the object will automatically position itself.
[20:57] It's something we ignored in axis to rotation, but it does exist.
[21:03] Cross product uses these two vectors to construct a plane and generates a new vector a bandicular to both of them.
[21:12] For example, if you import x and y, the cross product will give you the z-axis.
[21:19] Likewise, if you know the z-axis and x-axis, it will give you the y-axis.
[21:25] Here, we have a con with its z-axis facing upwards using aligned rotation to a vector.
[21:32] I will replace it with the cross product method.
[21:36] As I input the x-axis at the top and the z-axis at the bottom, you will find that the cross product is making a cone aligned to the y-axis on the negative region.
[21:49] The order matters here.


### Right Hand Rule in Cross Product [21:50]
**Transcript (timestamped):**
[21:51] If I flip the top and bottom inputs, you will find that it's pointing to the positive region of the y-axis instead.
[22:01] The cross product here follows the right-hand rule.
[22:05] Here, I have a right-hand model for demonstration.
[22:09] You use your index finger as the primary axis and your middle finger as the secondary axis.
[22:15] Then your thumb will show the cross product direction.
[22:20] You can see that if I match the index finger to 1 0 0 and the middle finger to 0 0 1, the thumb is facing the direction where the cone is pointing.
[22:30] This is just a fun fact about how the direction is determined.
[22:35] In practice, if the direction is not what you want, you simply flip the math.


### Bend Curves like gravity on tree branches [22:40]
**Transcript (timestamped):**
[22:41] So, why do we need to know this cross product if we do not need it for ordinary rotations?
[22:49] Here, we have an example.
[22:51] I have a curve growing diagonally and you can imagine it as a tree branch.
[22:57] I would like to bend this branch downward to simulate gravity.
[23:02] To do this, we use set position together with rotate vector.
[23:07] At this point, however, we are dealing with a completely different kind of rotation.
[23:13] Previously, we were constructing rotations from scratch.
[23:17] The objects themselves had no existing rotation.
[23:21] In this case, however, we want to rotate these points relative to their existing orientation to create the bending effect.
[23:30] This is why our previous methods based on aligning axes are not directly useful.
[23:37] We do not want to tell the branches where to face.
[23:40] So, the common and simple method is to use axis angle to rotation, where you can define a local pivot on this axis
[23:49] and increase the angle from zero to rotate it.
[23:53] Here, for the angle, I am using index with a mass multiply node.
[23:59] So, later points with higher index value will have a greater rotation angle than the earlier points.
[24:07] Once we connected to the rotation, you can see our curve has been bent to generate this spiral shape.
[24:15] The axis here is a directional vector.
[24:18] In this case, 001 means the z axis, and the entire extension of this line into infinity will be the pivot of rotation.
[24:30] This is why we have this spiral shape created.
[24:33] Here, I will decrease the multiplier to a smaller value.
[24:38] As we complete the angle, the remaining task is to find the correct axis.
[24:44] It may not be obvious how to think about this diagonal case,
[24:49] but if we start with a simple case of a straight line along the x axis and consider the parameters we have so far,
[24:58] my curve tangent is pointing along x, gravity is pointing downwards along the z axis,
[25:05] and my desired pivot axis will be the y axis.
[25:09] Here, you may be able to figure out the relationship between them.
[25:13] If I know the x and z axis, it's actually the cross product of these two values.
[25:20] So, if I generate a cross product using 100 and 00-1, you can see that it bends in the way we are looking for.
[25:28] To make it more accurate, we should use curve tangent, which still works correctly when I plug it in.
[25:36] Now, we can duplicate the exact same function and apply it to our diagonal case,
[25:42] and you can see how the tree branch bends.
[25:45] You can increase the multiplier to see how the axis is perfectly defined using our method.
[25:52] So, this is a real-world case where you may want to bend the curves of trees, flowers, or similar effects.


### Rotate Vector Vs. Vector Rotate [26:00]
**Transcript (timestamped):**
[26:00] Another benefit of this axis angle-to-rotation method is that controlling one value is much easier than controlling three values in a typical rotation.
[26:12] This is extremely helpful in motion graphics, which we will discuss in the next episode.
[26:19] In this example, I'm using the rotate vector node and axis angle-to-rotation.
[26:26] If you remember what we discussed in episode 7, I mentioned its similarity with the vector-rotate node,
[26:33] which should be outdated but has not been deprecated yet as the align-oiler to vector.
[26:40] I use the new method because I don't want to distract you from the differences between the paint rotation and the older purple rotation.
[26:49] Nevertheless, vector-rotate should be used more in practice because it supports the center function.
[26:57] In this example, it does not matter because our curve starts at the word origin at 000.
[27:05] In practice, obviously, this may not be the case, and you would have to add this function yourself using rotate vector.
[27:14] While it could be done, it's not worth learning because users did not need to learn it in the past.
[27:23] It's purely the developer's responsibility to handle this, although they did not do it for whatever reasons.
[27:30] You can take this as a brainstorming homework task, how to achieve the center functions using rotate vector.
[27:37] It's quite simple although a bit tedious.
[27:41] But in real life usage, I would simply recommend using the older vector-rotate node wherever possible.
[27:49] So, this is all for today's discussion about rotations.
[27:54] I hope you enjoyed this tutorial, and I will probably see you next episode where we talk about the scale and motion graphic aspects of instances.
[28:04] Bye-bye.



---

## Captured Frames

- [1:16] tutorials/frames/tut-align-rotation-to-vector-axes-to-rotation---p11-geometry-nodes-beginners-50/frame_000.jpg
- [3:14] tutorials/frames/tut-align-rotation-to-vector-axes-to-rotation---p11-geometry-nodes-beginners-50/frame_001.jpg
- [4:48] tutorials/frames/tut-align-rotation-to-vector-axes-to-rotation---p11-geometry-nodes-beginners-50/frame_002.jpg
- [7:10] tutorials/frames/tut-align-rotation-to-vector-axes-to-rotation---p11-geometry-nodes-beginners-50/frame_003.jpg
- [10:57] tutorials/frames/tut-align-rotation-to-vector-axes-to-rotation---p11-geometry-nodes-beginners-50/frame_004.jpg
- [14:36] tutorials/frames/tut-align-rotation-to-vector-axes-to-rotation---p11-geometry-nodes-beginners-50/frame_005.jpg
- [18:10] tutorials/frames/tut-align-rotation-to-vector-axes-to-rotation---p11-geometry-nodes-beginners-50/frame_006.jpg
- [21:03] tutorials/frames/tut-align-rotation-to-vector-axes-to-rotation---p11-geometry-nodes-beginners-50/frame_007.jpg
- [24:07] tutorials/frames/tut-align-rotation-to-vector-axes-to-rotation---p11-geometry-nodes-beginners-50/frame_008.jpg

---

## Structured Notes

### Core Technique
A deep theory pass on orienting instances/points in Geometry Nodes: **Align Rotation to Vector** (single-axis alignment, with a conceptual limitation on the other two axes), the newer **Axis to Rotation** node (accurate two-axis alignment replacing the old "second Align Rotation to Vector with a pivot" workaround), building custom direction vectors via simple subtraction (target-tracking/billboarding), Normal/Tangent as ready-made direction sources (mesh UV Tangent, curve Tangent/Normal), and **Rotate Rotation** / **Axis Angle to Rotation** + **Cross Product** for modifying an existing orientation (e.g. gravity-bent tree branches) rather than constructing one from scratch.

### Summary
Part 11 of a structured Geometry Nodes beginner series (follows on directly from Episode 10's Pick Instance topic). Starts with cones instanced on a UV Sphere via Instance on Points, fed through **Align Rotation to Vector**: its Direction input is a directional vector relative to the world origin (as taught in Episode 6), and its Axis input picks which local axis of the instance gets pointed at that direction — with the default 0,0,1 direction and Z axis, nothing visibly changes since cones already point up. Feeding it the Normal of the surface (mesh point Normal, or captured via Capture Attribute when instancing on Mesh to Points face centers, since raw Points have no normal) makes cones correctly point outward from any surface — but Capture Attribute must be captured on the **Face** domain, not Points domain, or subdivision increases will visibly tilt corner instances. Swapping the cone for a Suzanne head (which has a strong "forward-facing" identity, unlike a cone) exposes Align Rotation to Vector's core limitation: it only constrains ONE axis (the one you specify); the remaining two axes are resolved by Blender's internal logic and are "not extremely reliable." Demonstrated with an Empty's 3-axis gizmo: rotating the empty around Z while keeping Z pointing up still leaves X/Y facing arbitrary directions — exactly Suzanne's problem. **Fix option A:** chain a second Align Rotation to Vector (feeding the first's output Rotation back in as input Rotation) to also constrain a second axis (X or Y) — but the previously-fixed Z axis must be set as the new node's **Pivot** input, or the second alignment disrupts the first. **Fix option B (preferred/modern):** the single **Axis to Rotation** node, which takes a Primary Axis+Vector and Secondary Axis+Vector directly (no manual pivot chaining needed) and produces the same accurate two-axis-constrained result. The presenter's own practical take: Axis to Rotation is more accurate, but Align Rotation to Vector remains useful for simple single-axis cases (cones, eyeballs, a "comb" example) and specifically for *modifying* an already-existing rotation (e.g. from an Object Info node, which only outputs one rotation value) rather than building one from nothing. **Building a custom direction vector (target-tracking):** the core insight is that positions/locations ARE vectors relative to world origin, so "point instance A toward point B" reduces to elementary subtraction: `target_location − instance_position` gives the arrow from instance to target (demonstrated with a simple 1D number-line proof: instance at 3, target at 5, gap = 5−3 = 2). Feeding that difference vector into Align Rotation to Vector's Direction (with the target axis, e.g. Z or X) makes every instance track an Empty target object as it moves — same principle used for attraction/repulsion effects and billboarding in stylized art, though the presenter notes real billboarding setups don't use exactly this same node chain despite sharing the same subtraction principle. Reversing the subtraction order flips instances to face away from the target instead of toward it; if simple axis alignment causes an upside-down flip when the target crosses over, Axis to Rotation (forcing a second axis, e.g. Z, to stay "up") fixes it where a single Align Rotation to Vector can't. **Better direction sources than raw normals for the secondary axis:** a flat vector like 0,1,0 is often "too simple" for complex secondary-axis alignment. For meshes, the **UV Tangent** node (new in Blender 5.1 — previously required a much more complex manual node setup that the presenter says nobody actually used from his provided assets) reads directly from a mesh's UV map (`UV` input socket; use Named Attribute to fetch UVs from an Object Info-sourced mesh) and outputs a tangent vector well-suited as the secondary axis. It has two Mode options: **Exact** (the accurate/"gold standard" method, matching other DCC software, called MikkTSpace under the hood but exposed simply as "Exact") and a ~4x faster but slightly less accurate alternative — switching between them is visibly detectable as a tiny jitter/shake on the instances. For curves, the **Curve Tangent** node gives the direction of curve flow (simpler to use — just plug it straight in) and **Curve Normal** gives an arbitrary-but-continuous perpendicular direction (not related to lighting, unlike mesh Normal) that stays roughly consistent point-to-point rather than flipping randomly. In practice, curve instancing commonly uses Tangent as the primary axis and Normal as the secondary. **Normal nuance:** mesh geometry has both **True Normal** (the real geometric normal) and **Custom Normal** (editable via Set Mesh Normal with Sharpness Mode set to "Free," used to fake different light behavior for stylized shading, or to visually blend an object with the ground without changing its actual geometry) — Curve Normal is a completely separate, unrelated concept from mesh Normal despite the shared node name in some contexts, and curves have no custom-normal equivalent (both curve normal sockets are always identical). **Modifying an already-existing rotation** (rather than building one from scratch) is done with **Rotate Rotation**, offering Global (world-axis) or Local (relative to the current rotation) modes — the presenter defaults to Local, e.g. rotating locally around Z when Z is already aligned to a curve tangent effectively "spins the object around the pivot line itself" (compared to rotating a barbecue skewer). **Cross Product** (vector math) takes two axis vectors and returns a third perpendicular to both, following the **right-hand rule** (index finger = first input, middle finger = second input, thumb = result direction; swapping input order flips the result). Though Axis to Rotation only exposes two axis inputs, the implicit third axis is exactly this cross product, and it becomes essential for a different rotation problem: **bending a curve like gravity** (e.g. a tree branch) using **Set Position** + **Rotate Vector**, where **Axis Angle to Rotation** (Axis = a directional pivot vector, Angle = increasing per point, e.g. via point Index × a Math Multiply node) rotates each point progressively around a chosen pivot line to create a bending/spiral effect. Finding the correct pivot Axis for a diagonal branch is worked out by reasoning about a simpler straight-along-X case: if the branch runs along X and gravity pulls along -Z, the correct bend pivot is the Cross Product of those two vectors (X × -Z = Y), and using the branch's own Curve Tangent as one cross-product input generalizes this correctly to any branch direction. Axis Angle to Rotation's single-scalar-angle control is highlighted as much easier to drive with motion graphics logic than manipulating a full 3-value rotation directly — flagged as the subject of the next episode. Finally, **Rotate Vector** (a lower-level vector rotation used with Axis Angle to Rotation in this episode) is compared to the older, technically-not-yet-deprecated **Vector Rotate** node (referenced from Episode 7): Vector Rotate is recommended for real-world use because it has a built-in Center input (a pivot point offset from world origin), which Rotate Vector lacks and would require manually reimplementing — left as a "homework" exercise for viewers rather than demonstrated.

### Key Steps
1. Instance geometry (e.g. cones) onto points/faces via Instance on Points.
2. Feed a directional Vector (e.g. the surface Normal) and an Axis choice (e.g. Z) into **Align Rotation to Vector**, and plug its output into the Instance on Points' Rotation socket, to point one axis of every instance toward that direction.
3. When instancing on face centers instead of raw points (via Mesh to Points, Face mode), the mesh's Normal attribute is lost on plain Points — use **Capture Attribute** on the original mesh (captured on the **Face** domain, not Points, to avoid corner-tilting artifacts at higher subdivisions) to carry the Normal through to the point cloud.
4. To recognize when Align Rotation to Vector is insufficient: swap in an asymmetric object (e.g. Suzanne) — if it looks randomly tilted despite one axis being correctly aligned, the other two axes are being resolved unreliably by Blender's internal logic.
5. Fix by either (a) chaining a second Align Rotation to Vector on a different axis, feeding the first Rotation output back in as the second's input Rotation, AND setting the first-fixed axis as the second node's **Pivot** — or (b) replacing both with a single **Axis to Rotation** node (Primary Axis+Vector, Secondary Axis+Vector) for the same result without manual pivot chaining.
6. To make instances track a moving target object: subtract the instance's own position from the target object's world-space Location (`target_location - instance_position`) to build a direction vector; feed that into Align Rotation to Vector's Direction. Reverse the subtraction to face away from the target instead. If flipping occurs as the target crosses over, use Axis to Rotation with a second axis forced "up" instead of a single-axis alignment.
7. For a UV-mapped mesh's secondary axis (e.g. matching Suzanne's "forward" orientation precisely), use the **UV Tangent** node (`UV` input connected to the mesh's UV map, or via Named Attribute when the geometry comes through Object Info) instead of a flat constant vector — choose Mode "Exact" (accurate, default) or the faster/less-precise alternative depending on whether performance or precision matters more.
8. For curve instancing, use **Curve Tangent** as the primary axis (direction of curve flow) and **Curve Normal** as the secondary axis (arbitrary but continuous perpendicular direction) — commonly Tangent-primary/Normal-secondary in practice.
9. For stylized shading or fixing visual ground-contact issues without altering real geometry, edit **Custom Normal** via the **Set Mesh Normal** node with Sharpness Mode "Free" — leave alone to default to True Normal otherwise; note curves have no custom-normal equivalent.
10. To rotate an object that already has a rotation (rather than building one from scratch), use **Rotate Rotation** with Local mode (rotate relative to the object's current orientation, e.g. spinning around an axis already aligned to a curve tangent) rather than Global (world-axis) mode.
11. For gravity-bend/spiral effects on a curve: use **Set Position** combined with **Rotate Vector**, driven by **Axis Angle to Rotation** — set Angle from the point Index multiplied by a scalar (Math Multiply) so later points rotate further, and set Axis to the correct pivot direction.
12. Determine the correct pivot Axis for Axis Angle to Rotation by reasoning through a simplified straight-line case first (e.g. branch along X, gravity along -Z ⇒ pivot = Cross Product of X and -Z), then generalize using the branch's own **Curve Tangent** as one Cross Product input so the technique works for any branch direction, not just axis-aligned ones.
13. Recall Cross Product follows the right-hand rule (index = first input, middle = second input, thumb = output direction) — swap input order to flip the result if it comes out backwards.
14. For real production use requiring a rotation pivot offset from world origin, prefer the older **Vector Rotate** node (has a built-in Center input) over the newer **Rotate Vector** node (lacks Center, would need to be manually reimplemented).

### Nodes / Settings
- Align Rotation to Vector: Rotation (input, for chaining/pivoting), Vector (Direction), Axis, Pivot Axis, Factor (blend amount, rarely used per the presenter)
- Axis to Rotation: Primary Axis + Vector, Secondary Axis + Vector — modern replacement for chained Align Rotation to Vector setups
- Instance on Points (Rotation socket), Mesh to Points (Face mode), Capture Attribute (domain: Face vs. Points — Face avoids corner-tilt artifacts)
- UV Tangent (mesh, Blender 5.1+): UV input, Mode (Exact / faster-approximate), used as secondary axis
- Curve Tangent, Curve Normal: direction-of-flow and continuous-perpendicular vectors for curve instancing
- Set Mesh Normal: True Normal vs. Custom Normal, Sharpness Mode "Free" for manual custom-normal authoring
- Rotate Rotation: Global vs. Local mode (Local = relative to existing/current rotation)
- Axis Angle to Rotation: Axis (pivot direction vector), Angle (often driven by point Index × Math Multiply)
- Cross Product (Vector Math): two axis vectors in, perpendicular vector out, right-hand rule, input order matters
- Set Position + Rotate Vector (older/lower-level) vs. Vector Rotate (has Center/pivot-offset input, recommended for production over Rotate Vector)
- Object Info node (source of a single existing rotation value, relevant to when Align Rotation to Vector is preferred over Axis to Rotation)

### Difficulty
Advanced (this is explicitly theory-dense — vector math, right-hand-rule cross products, and the conceptual distinction between "constructing" vs. "modifying" a rotation — aimed at viewers who've followed the full beginner series through Episode 10, not a standalone quick-tip)

### Blender Version
5.0+, stated in the title; the UV Tangent node is specifically called out as new in Blender 5.1, giving a firmer lower bound for that portion of the tutorial.

### Tags
geometry-nodes, procedural, animation, motion-design, intermediate, advanced, blender-5x

---

## Related Tutorials
No directly related tutorials yet in the library for this Geometry Nodes Beginners series (episodes 1-10 not yet ingested) or for rotation/vector-math-focused GN content specifically — flag for cross-linking if earlier/later episodes of this same "Bradley Animation" beginner series are ingested.
