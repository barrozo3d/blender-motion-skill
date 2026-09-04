---
title: [Tut] Sample UV Surface for UV Deformer - P15 Geometry Nodes Beginners 5.0+
source: YouTube
url: https://www.youtube.com/watch?v=XmSjMms8KoA
author: Bradley Animation
ingested: 2026-09-04
blender_version: "Blender 5.2"
tags: [geometry-nodes, procedural, displacement, blender-5x, advanced]
extraction_status: complete
frames_dir: tutorials/frames/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50/
frame_count: 12
frame_status: complete
uncertainty_frames: []
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# [Tut] Sample UV Surface for UV Deformer - P15 Geometry Nodes Beginners 5.0+

**Source:** [YouTube](https://www.youtube.com/watch?v=XmSjMms8KoA)
**Author:** Bradley Animation
**Duration:** 26m55s | 19 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### What is Sample UV Surface about? [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, this is Bradley, welcome to the 15th episode of the Beginner Series on
[0:04] geometry nodes. I hope you've watched the previous episodes, because they will make today's
[0:09] topic much easier to follow. In previous sections, we discussed the instances, which is one of
[0:15] the most powerful features of geometry nodes at the moment. In the meantime, we actually
[0:20] have already discussed many aspects of deformation, which is the second most powerful feature
[0:27] of geometry nodes. Today, we are going to discuss Sample UV Surface nodes, which is a unique
[0:33] aspect about deformation. This is generally like a shader texture. For example, I've prepared
[0:40] a wooden texture onto Suzanne without any effort. Imagine this is a geometry instead
[0:46] of a texture onto the Suzanne, then you could have achieved tons of interesting effects.
[0:52] For example, instead of fabric texture onto a cross, you can map real geometry fabric
[0:59] onto a cross. This way, it's not just making things more realistic, but also you have more
[1:05] freedom about making up animation to construct it. It could be really cool. And that's why
[1:12] we needed this Sample UV Surface node. We talked about its brothers and sisters about
[1:17] all these sampling nodes and even more. Sample nodes are different methods to get attribute


### Recap about Components of Sample Nodes [1:20]
**Transcript (timestamped):**
[1:23] information from other geometries. They have three components. They require the geometry
[1:29] targets, the value you want, and a context. It's like a phone call requiring a phone
[1:35] number or an email requiring an email address. Sample UV Surface is not an exception. You
[1:42] need all three components. And in this case, it requires two contexts, both the senders
[1:48] and the receiver's email addresses. But I don't know which one is which. Even after
[1:54] checking the menu, I still don't know which is a sender and which should be the receiver.
[1:58] By the way, this UV socket has hidden itself, looking like an implicit attribute. But by
[2:05] reading the tooltip, you find that there is nothing. This may be improved in the future,
[2:11] but for the moment, it has nothing. So you will always have to input something. And I
[2:18] don't know which socket should receive which. So always try by yourself. Here I have two


### Study the usage of Sample UV Surface [2:20]
**Transcript (timestamped):**
[2:24] planes. One plane A has a UV map A. The other plane B has a UV map B. A is a flat and B
[2:33] has been modeled in a very weird way. Nevertheless, UV map B is still just a normal plane. And
[2:41] UV map A is even more normal. My goal is to deform A to the shape of B using the sample
[2:48] UV surface node. I started with plane A, set position with sample UV surface on B for the
[2:54] position. I've already prepared the named attributes UV map A and B. Once we output
[3:00] them one to one, I don't find anything. I've taught about using the mixed node with its
[3:06] original position to check your sample result more easily. And you find our points has been
[3:12] sampled to the word origin. It means our sample results are failing and it's likely due to
[3:20] wrong context. So we swap them and immediately we can see the results recovers and we have
[3:27] successfully mapped plane A into the shape of plane B. So these tests showed us that
[3:35] the top UV socket should be the UV map from the geometry we sampled and the bottom UV
[3:41] socket should be the field from our original geometry. I don't know how to explain it
[3:47] better. So you would have to perceive yourself. Here, I want to mention that plane A is highly


### Comparison to other Sampling Nodes in specific case. [3:50]
**Transcript (timestamped):**
[3:54] subdivided, whereas plane B only has a few vertices. So these are not the same geometry.
[4:03] If I sample index by index, it seems like I have the similar ultimate geometry. But
[4:10] if you check it with mix, you'll find it's actually not working because our point cut
[4:16] doesn't match each other. If you check wireframe, it's just a trash, even if the ultimate shape
[4:23] may look a bit similar. If you sample nearest, better results. If you sample nearest the surface,
[4:31] oh, even worse. As I said in the past, there are many sampling nodes and it's your responsibility
[4:38] to choose the most suitable ones for your needs. You should always come up with your
[4:43] own understanding and think which one is the best. Otherwise, you'll have to manually
[4:48] test all of them until you succeed. It will be very inefficient. But anyway, in this specific
[4:56] case, it would be sample UV surface, which functions like mapping a geometry onto the


### Basic Concept of UV Deformer [5:00]
**Transcript (timestamped):**
[5:01] UV map. As we learned the basics of this node right now, we can move on to the next question
[5:08] of it. Take the previous wooden Suzanne as an example. In terms of shader, what happens
[5:14] is like you have a texture going from 00 to 11. And your UV map is also within the range.
[5:22] So the texture maps onto this UV map, and these textures are ultimately showing on the
[5:27] geometry in 3D space. Therefore, instead of using the UV map to map onto another UV map,
[5:35] as we did previously, in the next step, I want to map any of our geometry into the range


### Manual Mapping and Importance of Brute Force [5:40]
**Transcript (timestamped):**
[5:41] from 00 to 11. Here, I've already prepared this simple setup for instancing cylinders.
[5:49] My goal is to fit them into the 0 to 1 range. I've realized the instances so we can set
[5:55] their positions. I started with a position and the map yet using map range set to vector.
[6:01] With the map range node, I'm setting a custom minimum and the maximum range and mapping
[6:06] it to the range from 0 to 1. If I output this map range result directly, it will clip half
[6:13] of our geometry because of the clamp option. Here, you need a more accurate range to start
[6:20] with. And I know my grid is one by one inside. So I can boot force it by setting the minimum
[6:28] to negative 0.5 and the maximum to positive 0.5. We successfully get the ideal result.
[6:37] Before I progress further, I want to mention that I don't usually work like this by manually
[6:41] inputting values. Nevertheless, it works. And you can even see this kind of thing happening
[6:47] in some Houdini tutorials. It's the same idea as hard surface modeling. Even though we are
[6:53] promoting procedural modeling in this course, plenty of professionals still use destructive
[6:58] modeling in their daily work. Please always be aware that you have the option of using
[7:04] boot force and the manual controls. Of course, the issue in this case is that if I change
[7:12] the value, everything will be screwed up and the data are outside the range again. So to


### Intro of Bounding Box for Procedural Map Range. [7:15]
**Transcript (timestamped):**
[7:17] make it procedural and elegant, I will use a concept called a bounding box. If you are
[7:24] familiar with the node names, you know we have a node for it. It has three output sockets.
[7:30] The first is a geometry socket that helps you visualize the bounding box. Here I will
[7:36] join two geometries together so you can see what a bounding box is really about. Normally,
[7:42] it's the smallest cube aligned to the word axis that contains the geometry. So if you
[7:48] transform the geometry diagonally, you will get a rather large box with lots of empty space.
[7:55] Anyway, the other two sockets output single constant for the minimum and the maximum. They
[8:01] respectively represent the bottom left front corner and the top right back corner. Together,
[8:09] these two vectors define the diagonal spanning of the entire bounding box, which gives us the range
[8:16] used for remapping. By subtracting them, you can also calculate the extent of the geometry
[8:22] along each axis. Nevertheless, the bounding box node doesn't really work with instances.


### Bounding Box for Instances / Instance Bounds [8:25]
**Transcript (timestamped):**
[8:29] If I directly input the instances without realizing the instance, the geometry output
[8:36] will show a bounding box for each instance. These bounding boxes are local to the rotation of the
[8:42] instances. So if you rotate the instances, you also rotate their bounding boxes. And the other
[8:50] two sockets fail completely. They just output zero throughout because the instance bounding box
[8:57] would need to be a field to cover the available instances, like here, here, and there, and so on.
[9:05] You could either extract the bounding box for each instance using for each element an instance,
[9:11] or use an instance bound node. This node is very tricky. Here, for demonstration, I'm
[9:18] instancing cylinders on a cube. And I really have to use my own preset to visualize the result better.
[9:25] As I'm inputting the minimum, you can see a colorful 3D marker around the word origin,
[9:31] but it seems to have nothing to do with the instances over the places. Even if I rotate
[9:37] the instances, it is not moving at all. Technically speaking, you have to manually transform the points
[9:46] with the instance transform, which includes the position rotation scale. As I replace the value,
[9:53] you can see the markers have been placed at the button left from the corner of each instance.
[9:59] And you can rotate them to see how the values are behaving locally. We can even join the geometry
[10:07] from the bounding box node to see how these values are represented correctly for the bounding box.
[10:13] I don't like this design at all. While people using it for the first time,
[10:17] they will likely be confused, including me. So, I made a preset with the same name,
[10:23] called instance box. Just to save some clicks and avoid confusion, I also have more complete versions
[10:31] where you input instances and can directly visualize the geometry and the bounding boxes.
[10:38] And coupled with the viewer, you can visualize these minimum and maximum values more clearly.
[10:44] Normally, these bounding box values are local to the instance.
[10:49] Regardless of the rotation, they stick to a specific corner, but I also prepared other modes
[10:55] like a global mode, which is aligned to the word axis, so its corner doesn't rotate towards the
[11:01] geometry. I even prepared an as a whole mode that gives you the bounding box of everything as a whole.
[11:10] Overall, I don't know why the original node has to be designed like this, but anyway.


### Radius Option of Bounding Box node. [11:15]
**Transcript (timestamped):**
[11:16] At last, we can take a look at the use radius option on the bounding box node.
[11:21] It's only useful for the geometry types containing a radius attribute,
[11:27] minlet points, curves, and the grease pencil. I've already prepared a random scattering of
[11:32] points using random value nodes. You can see that the bounding box extends beyond the positions
[11:38] of the points because it considers their radius. If I disable the option, then it will only consider
[11:45] the actual positions of these points, regardless of their sizes. It's equally true to an instance
[11:52] bounding box, either we'll check the internal geometry and consider the radius or unladed
[11:58] position accordingly. Here, we've finished covering all the sockets of the bounding box node itself.


### Finish the Procedural Mapping [12:05]
**Transcript (timestamped):**
[12:05] Let's go back to our initial question. We just want to remark the position value to a 0 to 1 range.
[12:12] In this case, it's good enough to use the realized result and use the minimum and maximum vector in
[12:18] our map range. Immediately within the viewports, you can see our result.
[12:24] Mesh has no radius, so enabling or disabling this option doesn't matter here.
[12:30] The z-axis mapping is a bit too much. I will manually fix it here.
[12:36] Now, the benefit of having a bounding box node is that it will automatically fit to the mesh
[12:43] input. No matter how I change the size of our geometry, it will always be correctly mapped
[12:49] into the region from 0 to 1. Although the geometry may be squashed in the wrong dimension,
[12:54] that's a different problem. I will keep the node made for this node tree, so I move to


### Morphing Basics of Sample UV Surface [13:00]
**Transcript (timestamped):**
[13:01] another identical but clean node tree I've prepared already. Now, let's move on to the
[13:06] last step of the application I want to show. You may think of it as a kind of iron chair in a
[13:13] park. My goal is to drill holes into this iron chair. Instead of hard surface modeling, I will do
[13:20] it more procedurally with spooling so that I can freely change the pattern parameters. Therefore,
[13:28] I can use the sample UV surface method to map our current pattern onto this chair geometry.
[13:35] I've prepared the UV map for our chair. It's just the same as a regular plane,
[13:41] so this should be a simple but also practically useful example to demonstrate this technique.
[13:48] I will import the chair objects. The sample is position values and its UV map as the context.
[13:56] For the other UV input for model pattern, as we said, I'm going to use the position we created.
[14:02] And I will use this sample to the results for a new set of position. Now, you will see this sample
[14:08] results. Sometimes, when users follow someone's suggestions, they will respond to things like
[14:15] it doesn't work. In that case, you should think yourself about whether it should work in the
[14:21] first place or why it doesn't work in this case. Many things are happening at the same time here,
[14:28] and you have to consider them separately. First of all, it's definitely working because our geometry
[14:37] has definitely been shifted from the previous flat arrangement onto our chair.
[14:44] The result seems wrong because of several separate issues that we need to solve. One issue here is


### Is Valid of "Sample UV Surface" [14:50]
**Transcript (timestamped):**
[14:52] these groups of extrusion going to the word origin. Whenever you are sampling and something is going
[14:58] to the word origin, you should immediately consider that some geometries are not getting any values.
[15:05] In this case, it's because the bounding box is too perfect. They sit right on the edges,
[15:13] which doesn't help them find a position on the UV map to be sampled. A quick solution is to manually
[15:20] shrink the bounding box. For example, for the minimum values on x and y, I can set them to 0.1
[15:28] to fix one part. And for the maximum values, I can set them to 0.9 to fix another.
[15:35] This is a very specific Boolean-forced solution. It works because our chair UV map is a plane.
[15:42] Most of other times, it won't work even for a simple cube. Here, I've map-ranged everything just
[15:48] like what I did, but the result is still ugly. This is where the validity socket is required.
[15:56] If you use viewer to check this value, the white regions are showing the UV map of a cube.
[16:03] The black regions are the empty space that doesn't get any value. In this case, what I often do is
[16:10] to separate the geometry that sees values for our assembly. And you can see we removed these
[16:18] extensions. Of course, we are having other problems with the same, but that's another story which I
[16:26] don't have time to cover in details. So, there could be many ways to solve a problem. It could be a
[16:33] dumb way, a smart way, or whatever. But anyway, if it works, it is a good way. The next issue we are
[16:42] going to solve is this flat geometry, because this used to be cylinders with height. The issue
[16:49] happens because UV coordinates don't have height, so it's not part of the sample result.


### Height Recovery using Normal Displacement [16:50]
**Transcript (timestamped):**
[16:55] We need to recover it with normal displacement separately. I do the sample process of
[17:01] sample UV surface, but at this time, instead of position, I will sample the normal result,
[17:08] and I will scale it with the z-axis from our map range and plug it into the offset.
[17:15] Now, you see we've recovered the height of cylinders
[17:19] irrelevant to our chair shape and the curvatures. Now, we can use this geometry for Boolean to
[17:27] drill the holes, but you will still find another problem that the Boolean is incomplete. If you
[17:34] join the geometries and use a viewer to check, you can see that our geometry isn't really
[17:39] penetrating the chair. So, I will decrease the z-minimum a little bit, and then the problem is solved.
[17:48] Whether you like it or not, we finished this simple but practical example. The rest are parameters
[17:54] that allow you to manually decrease the margin, like setting it to 0.05 and 0.95 instead. But anyway,
[18:04] this function is generally called UV deformer. You can even find Houdini tutorials by Antagma,
[18:10] where they spend tons of time building vex for this, and I've made a preset to make the setup
[18:16] easier with kind of a one-click setup. If you check the Boolean result, it doesn't seem to work
[18:24] because I need to tweak the margins as we just did. So, overall, you either build the entire graph


### Presets Usage in Real Life [18:30]
**Transcript (timestamped):**
[18:32] manually every time or use whichever node group people provide, whichever way you like. On the
[18:38] other hand, this workflow of positioning and recovering the geometry with normal is a very
[18:44] important concept. It's also involved in another more complex preset called the Curved Deformer.
[18:50] It's equivalent to the Curved Modifier, and internally, it's using the sample curve node.
[18:57] I won't have time to discuss it in this course, but this preset is free and is basically provided
[19:03] by other software. It is just not provided in geometry nodes by the Belander Foundation yet.
[19:09] Please bear this in mind. Also, with preset, we can start to move on to more complex setup
[19:17] more quickly. Right now, we are instancing on a straight grid, but in practice, I will do a
[19:23] hexagonal array. This is also a preset I made because it's not provided by Belander Foundation.
[19:31] I plug it in and the realized instance increased the scaling, then immediately you find this kind
[19:38] of honeycomb patterns, which is definitely more interesting than the initial straight grid.
[19:44] So anyway, another important aspect of this setup is workflow optimization. Right now,
[19:51] we start with geometry that already has a height and then recovered height afterwards.
[19:57] Another way to think about it is to start with something flat and solidify the geometry afterwards.


### Operations before/after the UV Deformer [20:00]
**Transcript (timestamped):**
[20:05] I don't have a direct proof, but I think this method could be faster. It's also a different
[20:12] perspective on what we've done so far. Similarly, you could think about whether you do animations
[20:18] before or do the animation after or curve to tube before or curve to tube after. Here,
[20:28] curve to tube represents the conversion. For example, if you start with a curve line,
[20:34] it's just a straight curve, but curve to tube converts it into a mesh geometry with potentially
[20:41] many more vertices. Ideally, in this case, it will be faster to do it afterwards.
[20:48] At last, while I'm promoting how convenient are assets, you still have to understand the
[20:54] basic approach behind them, especially the pros and cons. These principles still apply


### Caveats of the Sample UV Surface Workflow [21:00]
**Transcript (timestamped):**
[21:01] whether you use an asset or build a setup yourself. For example, you must have a UV map.
[21:08] Without a UV map, you simply cannot do this kind of mapping. Or sometimes you don't have a named
[21:15] attribute, you will still need to input attribute manually from the procedural geometry. These are
[21:21] always what we have taught along the course. But having a UV map is not the only thing you need to
[21:27] consider. Here, I have an example of a geometry where its circle and square have overlapped UV.
[21:35] If we select this geometry and use sample UV surface, you will find that the sphere and
[21:41] the part of the square will not inherit any geometry. This is because the UV map doesn't
[21:47] have height. Once they overlap, the system cannot know which point should go to which part of the
[21:53] 3D space. So the sampling result is embedded. By the way, disabling our separate geometry won't help,
[22:02] as it will only reveal these ugly long extensions. To solve it, I would recommend to do it manually
[22:09] in edit mode. Or you can use a node called yetpackUBIlet. I will set the margin to 0.1.
[22:18] If we check its validity, you can see that the square and the circle are no longer overlapping
[22:25] after using our pack function. While this works, I have to warn you that all UV operations
[22:32] within geometry nodes are quite slow. Here, I'm visualizing the UV map of a cube,


### All UV Operations in GN is slow [22:34]
**Transcript (timestamped):**
[22:40] which takes 2.1 milliseconds. If I pack the island, it takes 100 milliseconds.
[22:48] This time, it's related with the subdivision level. If I increase it further, you can see it takes even
[22:54] longer. Similarly, I've prepared a cylinder. The built-in UV map takes less than 1 millisecond.
[23:02] I used some simple logic trying to add something on the top and the bottom,
[23:08] and unwrap it. It takes 100 milliseconds. And remember, I'm not even subdividing much of it yet.
[23:17] You can try to manually play with the value to see how the performance drops miserably.
[23:22] So overall, these are expensive operations in geometry nodes. Try not to rely on them ever
[23:30] for the moment. For example, UV surface, the tutorial is basically finished here,
[23:37] but I want to spend some time briefly talking about a few aspects that I didn't have time to cover


### Combination of Techniques in Animations for this technique [23:40]
**Transcript (timestamped):**
[23:42] earlier. The first thing I want to talk about is combining different techniques. I have this
[23:48] animation here, which is a variation of the moving to tree animation. I didn't add particles because
[23:55] I don't have time to discuss simulation in this course. It's another very big and advanced topic.
[24:01] The node tree looks very frightening, but it's really just a combination of techniques we've
[24:07] discussed. For example, as noted by the blue frames, we talked about time a fourth in episode 12,
[24:16] as well as float curves and the mixed nodes, data types, capture attributes, instances,
[24:22] sampling and the more thing. There are also other better and more complete free files provided,
[24:29] if you're interested. It will also be great if you try to recreate those yourself.
[24:37] The last thing I want to discuss is why not using split to instance. Here, I have 125 default cubes.


### Why I hate "Split to Instance" node [24:45]
**Transcript (timestamped):**
[24:46] These are real mesh geometries. Sometimes people think instances are fast,
[24:52] so they try to split to instances. The way it works is that the geometry with the same group ID
[24:59] will be converted into an instance. A common and a quick way is to use smash island index.
[25:07] So every island will be an instance. We end up 125 instances. The major issue with this setup
[25:15] is that it's extremely slow. If I start to subdivide my cube, then you can see that split
[25:22] to instances becomes much slower. The second issue is that the split to instances node sets the
[25:31] instance origin at the world origin. And therefore, rotating an instance will rotate it as a whole.
[25:39] I have a preset that sets the origin for you so that each cube can rotate locally. Nevertheless,
[25:47] it's using the same node internally, so you will face the same performance issue with subdivision.
[25:54] On the other hand, if you know geometry nodes well enough, I have a few average nodes that also
[26:02] has a group ID. By inputting the mesh island index, it can calculate the average position of each
[26:10] island. Then we can use vector rotates on the position and set position. Now we can achieve
[26:18] the same effect. And it's much, much faster. In real life, I find split to instances extremely
[26:27] bad and not that useful for me. So always think about and try alternatives that could be a better
[26:34] option. So we are finishing here. The next episode will be about perks, which are the building blocks
[26:42] for these knitting units. It will also be our last section for this beginner series course.
[26:49] I hope you enjoy this video and I'll probably see you next episode. Bye bye.



---

## Captured Frames

- [2:55] tutorials/frames/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50/frame_000.jpg
- [3:27] tutorials/frames/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50/frame_001.jpg
- [4:31] tutorials/frames/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50/frame_002.jpg
- [6:28] tutorials/frames/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50/frame_003.jpg
- [7:40] tutorials/frames/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50/frame_004.jpg
- [9:53] tutorials/frames/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50/frame_005.jpg
- [12:18] tutorials/frames/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50/frame_006.jpg
- [14:52] tutorials/frames/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50/frame_007.jpg
- [16:03] tutorials/frames/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50/frame_008.jpg
- [17:08] tutorials/frames/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50/frame_009.jpg
- [22:44] tutorials/frames/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50/frame_010.jpg
- [25:25] tutorials/frames/tut-sample-uv-surface-for-uv-deformer---p15-geometry-nodes-beginners-50/frame_011.jpg

---

## Structured Notes

### Core Technique
Building a **UV deformer** with `Sample UV Surface`: remap any geometry into 0–1 space using a `Bounding Box`, sample a target mesh's surface through its UV map to reposition it, then recover the lost height by separately sampling the surface `Normal` and driving an offset with it.

### Summary
`Sample UV Surface` maps geometry onto a mesh the way a shader maps a texture — but with real geometry, which is what makes procedural panelling, perforation and knit patterns possible. The episode teaches the node from its confusing two-UV-socket interface outward: how to tell the sockets apart, how to get source geometry into 0–1 range procedurally with `Bounding Box` (including the awkward instance case), how to diagnose the two failure modes (geometry collapsing to world origin, and flattened height), and where the whole approach breaks down. It closes with two blunt performance warnings: **all UV operations in Geometry Nodes are slow**, and **`Split to Instances` is worse than the alternatives**.

### Key Steps
1. **Recall the sample-node pattern.** Every sampling node needs three things — a geometry target, the value you want, and a context. `Sample UV Surface` is unusual in needing **two** contexts `[transcript 1:23-1:48]`.
2. **Work out which UV socket is which — empirically.** The node exposes `UV Map` and `Sample UV`, and the tooltip does not explain the difference; the author says outright he cannot tell from the menu and had to test `[transcript 1:48-2:18]`. The working answer: **`UV Map` takes the UV of the geometry being sampled; `Sample UV` takes the field from your own geometry** `[frame_001]` `[transcript 3:35-3:46]`.
3. **Diagnose a wrong context instantly.** Mix the sample result against the original position — if points collapse to the world origin, the sample is failing `[frame_001]` `[transcript 3:00-3:26]`. Swapping the two inputs fixes it.
4. **Know why the other sample nodes lose here.** `Sample Index` fails when point counts differ (the wireframe is "just a trash"), `Sample Nearest` is better, `Sample Nearest Surface` worse still `[transcript 3:54-4:37]`.
5. **Understand the mapping goal.** As with a shader, a texture spans 0–1 and the UV map lives in that range; so the source geometry must be pushed into 0–1 too `[transcript 5:08-5:40]`.
6. **The brute-force version first.** `Realize Instances`, then `Map Range` set to **Vector**, with `From Min`/`From Max` hand-typed to `-0.5`/`0.5` because the grid is known to be 1×1 `[frame_004]` `[transcript 5:41-6:36]`. The author defends manual values explicitly: professionals use destructive methods daily, and brute force is a legitimate option `[transcript 6:37-7:10]`.
7. **Make it procedural with `Bounding Box`.** Three outputs: a `Bounding Box` geometry for visualisation, plus `Min` and `Max` vectors giving the bottom-left-front and top-right-back corners. Those two define the span used for remapping, and subtracting them gives the extent per axis `[frame_004]` `[transcript 7:17-8:22]`. Note it is the smallest **world-axis-aligned** cube, so diagonal geometry yields a wastefully large box `[transcript 7:42-7:54]`.
8. **Know the instance trap.** Feed instances in unrealized and the geometry output shows a box *per instance* (rotating with them), while `Min` and `Max` **output zero entirely** — they would need to be fields `[transcript 8:29-9:04]`.
9. **Two ways out**: `For Each Element` on instances, or the `Instance Bounds` node — which the author calls badly designed, since its values sit at the world origin until you manually transform the points by the instance transform (position, rotation, scale) `[transcript 9:05-10:12]`. He ships his own `instance box` preset with local, global and as-a-whole modes to avoid the confusion `[transcript 10:17-11:09]`.
10. **`Use Radius`** only matters for geometry carrying a radius attribute — points, curves, grease pencil. On such data the box expands past the point positions; disable it and only positions count. Meshes have no radius, so it is inert there `[frame_004]` `[transcript 11:16-11:58, 12:24-12:29]`.
11. **Wire the procedural version.** Bounding Box `Min`/`Max` into Map Range `From Min`/`From Max`, output 0–1 `[frame_004]` `[transcript 12:05-12:23]`. The mapping then self-adjusts to any input size `[transcript 12:36-12:53]`.
12. **Apply it.** Sample the target's `Position` with its UV map as context, feeding the 0–1 remapped position as `Sample UV`, into `Set Position` `[transcript 13:48-14:07]`.
13. **Failure mode 1 — collapse to origin.** Extrusions shooting to the world origin mean some geometry received no value. Here the bounding box fits *too* perfectly, so edge points find nothing to sample `[transcript 14:52-15:19]`.
14. **Quick fix (only for a plane-like UV):** shrink the range — `To Min` `0.100` and `To Max` `0.900` on X and Y `[frame_008]` `[transcript 15:20-15:41]`. The author flags this as a special case that will not generalise, "even for a simple cube" `[transcript 15:42-15:47]`.
15. **The general fix — `Is Valid`.** The node's second output reports which points sampled successfully. Viewed on a cube, white regions are UV-covered and black regions got nothing; use it to `Separate Geometry` and drop the failures `[frame_008]` `[transcript 15:48-16:24]`.
16. **Failure mode 2 — flattened geometry.** UV coordinates carry no height, so the sample cannot restore it `[transcript 16:42-16:54]`.
17. **Recover height via normal displacement.** Run a *second* `Sample UV Surface` sampling the **`Normal`** instead of position, scale it by the Z component from the Map Range, and feed it into the `Set Position` `Offset` `[transcript 16:55-17:18]`. Height is then independent of the target's curvature.
18. **For a Boolean, push through.** If the drilling geometry does not fully penetrate, lower the Z minimum `[transcript 17:26-17:47]`.
19. **Compose further.** Swapping a straight grid for a hexagonal array preset gives honeycomb perforation `[transcript 19:17-19:43]`.
20. **Think about operation order.** Starting flat and solidifying *after* the deform is likely faster than deforming geometry that already has height; same question applies to animating before vs after, or `Curve to Tube` before vs after — converting a curve to a mesh multiplies vertex count, so do it last `[transcript 19:44-20:47]`.
21. **Caveat — you must have a UV map**, and without a named attribute you must supply the UV field manually `[transcript 21:01-21:21]`.
22. **Caveat — overlapping UVs break it.** Where a circle and square share UV space, the sampler cannot know which 3D point to use and the result is garbage; `Separate Geometry` only exposes ugly extensions rather than fixing it `[transcript 21:22-22:08]`. Fix in Edit Mode, or use **`Pack UV Islands`** with a margin `[frame_010]` `[transcript 22:09-22:25]`.
23. **Performance warning 1 — UV ops are expensive.** On a cube at `Vertices 55³`, the base evaluation is `0.40 ms`; inserting `Pack UV Islands` takes it to **`124 ms`** `[frame_010]`. Narration cites a comparable 2.1 ms → 100 ms case, and notes cost scales with subdivision `[transcript 22:34-23:29]`. The advice is blunt: "try not to rely on them ever for the moment."
24. **Performance warning 2 — avoid `Split to Instances`.** It converts same-group-ID geometry into instances, but it is very slow under subdivision **and** it sets every instance origin at the world origin, so rotation spins the whole object `[transcript 24:46-25:45]`. The faster alternative: an average-position node grouped by `Mesh Island Index`, then `Vector Rotate` on position into `Set Position` `[transcript 25:54-26:24]`.

### Nodes / Settings
- **`Sample UV Surface`** — data type `Vector`; inputs `Mesh`, `Value`, **`UV Map`** (UV of the sampled geometry), **`Sample UV`** (field from your geometry); outputs `Value` and **`Is Valid`** `[frame_001][frame_008]`
- **`Bounding Box`** — outputs `Bounding Box`, `Min`, `Max`; input `Geometry` with a **`Use Radius`** toggle `[frame_004]`
- **`Instance Bounds`** — needs manual transform by the instance transform to be usable; author supplies an `instance box` preset instead `[transcript 9:11-11:09]`
- **`Map Range`** (Vector) — brute-force `From Min -0.500 / -0.500 / 0.000`, `From Max 0.500 / 0.500 / 1.000`, `To Min 0/0/0`, `To Max 1/1/1` `[frame_004]`; margin variant `To Min 0.100 / 0.100 / 0.000`, `To Max 0.900` `[frame_008]`
- **`Realize Instances`** — `Realize All` on, `Depth 0`, required before Bounding Box works on instanced geometry `[frame_004]`
- **`Instance on Points`** — `Pick Instance`, `Instance Index`, `Rotation`, `Scale` `[frame_004]`
- **`Named Attribute`** (Vector) — `UVMap_A`, `UVMap_B` in the study setup `[frame_001]`
- **`Object Info`** — `Original`/`Relative`, `As Instance`, used to bring Plane A / Plane B in `[frame_001]`
- **`Mix`** (Vector, Uniform, `Clamp Factor`, `Factor 1.000`) — the diagnostic trick for spotting failed samples `[frame_001]`
- **`Pack UV Islands`** — `Margin 0.001`, `Rotate` on, method `Bounding Box`, `Bottom Left 0,0`, `Top Right 1,1` `[frame_010]`
- **Measured cost** — Cube at `Vertices 55³`: `0.40 ms` base, `124 ms` with Pack UV Islands, `125 ms` total tree `[frame_010]`
- **Mentioned presets (author's own, not stock Blender)** — `instance box`, a UV-deformer one-click setup, `Curve Deformer` (wraps `Sample Curve`, equivalent to the Curve modifier), and a hexagonal array `[transcript 10:17-11:09, 18:10-19:30]`

> **Whisper unreliability is high in this episode.** "Belander Foundation" for Blender
> Foundation, "boot force" and "Boolean-forced" for *brute force*, "word origin" for world
> origin, **"yetpackUBIlet"** for **`Pack UV Islands`** `[frame_010]`, "smash island index"
> for `Mesh Island Index`, "Antagma" for Entagma, "spooling" for Boolean, "minlet points"
> for "namely points", and "perks" for the next episode's topic. The frames carry the real
> node and socket names.
>
> **An honest gap in the source, worth preserving:** the author cannot explain which UV
> socket is which — "I don't know how to explain it better. So you would have to perceive
> yourself" `[transcript 3:44-3:47]`. The socket names in `[frame_001]` are the reliable
> record, and the mix-against-original-position trick is the practical way to test.

### Difficulty
Advanced

### Blender Version
Blender 5.2.1 RC — read from the status bar in `[frame_001]`, `[frame_004]`, `[frame_008]` and `[frame_010]`. The title advertises "5.0+".

### Tags
geometry-nodes, procedural, displacement, blender-5x, advanced

---

## Related Tutorials
- [[tut-what-makes-splinecurves-more-complicated---p16-geometry-nodes-beginners-50]] — P16, the immediately following episode; its instance-vs-realized rule is the same constraint that forces `Realize Instances` before `Bounding Box` here
- [[tut-everything-about-for-each-element-zone-in-variations---p14-geometry-nodes-be]] — P14; the `For Each Element` zone this episode names as one of the two ways to get per-instance bounding boxes
- [[tut-align-rotation-to-vector-axes-to-rotation---p11-geometry-nodes-beginners-50]] — P11; same series, complementary instance-transform material underlying the `Instance Bounds` workaround
- [The 6 Levels of Blender Materials](the-6-levels-of-blender-materials.md) — its Level 5/6 use `Store Named Attribute` to carry data into shaders, the mirror of this episode's use of named attributes to carry UV data between geometries
