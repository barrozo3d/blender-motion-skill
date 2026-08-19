---
title: [Tut] Everything about For Each Element Zone in Variations - P14 Geometry Nodes Beginners 5.0+
source: YouTube
url: https://www.youtube.com/watch?v=Mm1Oxz6sGAg
author: Bradley Animation
ingested: 2026-08-19
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/tut-everything-about-for-each-element-zone-in-variations---p14-geometry-nodes-be/
frame_count: 0
frame_status: pending-selection
---

# [Tut] Everything about For Each Element Zone in Variations - P14 Geometry Nodes Beginners 5.0+

**Source:** [YouTube](https://www.youtube.com/watch?v=Mm1Oxz6sGAg)
**Author:** Bradley Animation
**Duration:** 30m15s | 21 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py tut-everything-about-for-each-element-zone-in-variations---p14-geometry-nodes-be <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Recap & Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, this is Bradley. Welcome to the 14th episode of the beginner series on geometry nodes.
[0:06] I hope you've watched the previous episodes because they will make today's topic much easier to follow.
[0:12] In the last several episodes, I explained the nature of instances, their linked geometry,
[0:19] and to break that linkage, you need to realize the instances, which can have a negative impact on performance.
[0:27] So in the last several tutorials, I taught you ways to fake instance variations using peak instance,
[0:34] rotation, scale, and instance attributes in textures.
[0:39] But I also emphasized that you should have realistic expectations.
[0:44] There are cases where you have to realize instances, especially when working with motion graphics,
[0:51] where you frequently modify the geometry or sampling their attributes.
[0:56] Today, we will talk about a different method for creating real instance variation using for each element zone.
[1:05] Nevertheless, be aware that this is not an omniscient method, as you might expect. We will see.
[1:14] So here I have an example of a grid with 2 times 2 vertices.


### Inspection Index for Viewer [1:15]
**Transcript (timestamped):**
[1:20] And I pass this into the zone. The zone will separate each relevant element within the zone.
[1:26] If I use the viewer to check the input elements, you will only see a single vertex.
[1:32] To make it more obvious, we can use smashed points to convert the vertices into something with a larger radius.
[1:40] This zone will run through all of its elements and apply the operation within the zone.
[1:46] If you want to visualize the next few points in the viewer, make sure you are selecting the zone inputs and going to the M panel.
[1:55] I will need to go to the node settings where you will see the inspection index.
[2:01] The index always starts from 0 for our first element.
[2:05] Then you go to the second point, third point, and so on until it disappears.
[2:11] Because we only have 4 points in total, you won't find anything for an index beyond the 3.
[2:17] You can also find the inspection index using the output.


### Regarding Zone Output [2:20]
**Transcript (timestamped):**
[2:21] It's just that the output contains 2 sections, representing the upper panel and the lower panel.
[2:28] The inspection index can only be found in the lower panel.
[2:32] The upper panel is for the original geometry from what you input.
[2:36] It's hard coded and you cannot change it.
[2:39] The rest of the sockets are parameters you can set.
[2:43] They function exactly like a capture attribute.
[2:46] I personally have never used these parameters.
[2:50] The bottom line is very important for what we need.
[2:53] It will join all the elements together for the final output.
[2:58] If we output the points to it and look at the final output in this case,
[3:03] you don't see the original geometry, but 4 points joined together instead.
[3:09] If you disable match to points, then you have 4 vertices remaining.
[3:14] Now let's unmute the conversion and add a random value node to the radius.


### Field to Single Constant through Zone [3:15]
**Transcript (timestamped):**
[3:20] Now you will see that there's no variations.
[3:24] All the points are the same size even after changing the seed.
[3:29] This is because within the zone, your input geometry is always a single element.
[3:36] If you check the ID with the viewport overlay text,
[3:40] you will find that it only contains a single zero and stays the same from element to element.
[3:46] Our seed is also a constant, therefore, you must end up with the same random result across all elements.
[3:56] This is the moment when you need some uniqueness in either the ID or the seed.
[4:01] Traditionally, we can use the input ID for uniqueness.
[4:06] Directly plugging it in obviously won't make any difference, but we can utilize the zone input.
[4:13] You input an ID and you can see it converts the diamond socket into a rectangular socket,
[4:21] meaning it converts a field into a single value,
[4:26] because each element contains only a single value of that field.
[4:31] We can also confirm with the viewer that this is a single constant for our single points every time
[4:37] until the inspection index is out of range.
[4:41] Moreover, here you can see the link has been transformed from a dashed link into a solid line
[4:48] to tell their critical differences.
[4:51] Now, we output this new ID to the ID input.
[4:54] We are overriding the original ID field.
[4:57] As a result, each point has a random radius.
[5:01] If it's not obvious, you can change the seed to really confirm it.
[5:07] While this works, in practice, I will use the index from the zone to replace the ID.


### Element Index/Loop Index [5:10]
**Transcript (timestamped):**
[5:13] The result is the same.
[5:15] The index here is the index of each element, which is equivalent to passing an index into the zone.
[5:23] You can call it the element index.
[5:26] I personally often call it the loop index for technical reasons.
[5:30] But anyway, you can call it whatever you want.
[5:33] I discussed the similarities and the differences between ID and the index in episode 10.
[5:39] So I'm not going to repeat that here.


### unnoticed "For Each Element" in Daily Life [5:40]
**Transcript (timestamped):**
[5:42] At least they are the same here in this example.
[5:46] Right now, this setup is not anything special,
[5:50] because I can totally duplicate these nodes and move them outside the zone.
[5:55] I will use setPosition to offset it so you can compare two results side by side.
[6:01] And you can see that they are totally the same.
[6:04] So, for each element, it is not really a new concept.
[6:09] It has been with us all along.
[6:11] And most of the time, some kind of equivalent function is already implemented within each node.
[6:19] So you don't need an extra step to perform these functions.
[6:23] Nevertheless, we discussed the relationship between instance attribute and the attribute of continuous geometries.


### FEEZ for Instance Modification [6:25]
**Transcript (timestamped):**
[6:31] Here we come to this example about extrudeMesh that we keep talking about.
[6:36] Normally, if you extrude a mesh with a random value, the node can perform the function,
[6:42] but instances are linked without showing any variation.
[6:46] The result is equivalent to doing it before instancing.
[6:51] And you can compare the build results in the build port to see how identical they are.
[6:57] Here, if we try for each element on the point of domain, it won't work.
[7:03] And it will show a warning that there are no points in the point of domain.
[7:08] Of course, because these are instances, so we can use the instance domain and trigger the build again.
[7:17] And then we can apply the extrude function within the zone.
[7:22] Nevertheless, instead of plugging the loop index into the ID, I will plug it into the seed instead,
[7:30] so that the ID can keep working as the attribute of continuous geometry.
[7:36] Now, you will notice that each cube instance has a different pattern of extrusion on each face,
[7:43] while the final outputs remain instances.
[7:48] The reason it works is that as you separate each instance into an individual element within the zone,
[7:55] you are temporarily breaking the linkage between them.
[7:59] So this is basically the idea.


### When FEEZ is Slower than Realize Instance [8:00]
**Transcript (timestamped):**
[8:01] While this works, and many people may start cheering for it as an alternative to realize instances,
[8:08] I have to mention some important and serious aspects regarding performance.
[8:14] Here, I'm instancing a bunch of planes and extruding them using two different approaches.
[8:21] Using the zone and the realized instances respectively.
[8:25] I prepared them so we can compare them side by side, and ensure that they are the same.
[8:32] The time show and the button left of the frame indicates how much time it takes to perform the function, including within it.
[8:41] You can see that the time cost for the zone on the top is about two times longer than the one using realizing instances on the bottom.
[8:51] If I increase the instance count control from 5 to 125, you will notice that the time cost for the zone is about 10 times longer now.
[9:02] This is very, very bad.
[9:05] The shading differences are not important here.
[9:08] They are caused by overlapping instances.
[9:11] Once you realize the instances, this will be resolved in the viewport.
[9:17] Although it takes another 100 milliseconds to calculate the whole thing.
[9:22] If you compare two geometry in the viewport, you can find some signatures telling two functions are still outputting exactly the same result.
[9:32] I will keep realized instance disabled, just to keep in mind that the shading is not important at all.
[9:39] This example is here to show that the zone is not the universal solution to everything.
[9:45] And the realized instances is really not that bad if you want to achieve certain functions.
[9:51] Please keep this in mind carefully.
[9:54] When you need it, you really need it.
[9:57] On the other hand, let's reset the instance count control to 5 and play with the subdivision control instead.


### When FEEZ is Faster than Realize Instance [10:00]
**Transcript (timestamped):**
[10:05] As I increase it to 125, you will find that the time cost is flipped.
[10:12] The zone is now becoming more than two times faster than the realized instance approach.
[10:18] Now, if I increase the count control from 5 to 15, the ratio between them remains as about two times.
[10:28] The time shown here may not be exactly accurate, because when you join the geometry from two calculations,
[10:35] and the calculations become heavier and heavier, they are competing for CPU resources.
[10:42] Nevertheless, the overall relationship is still trustworthy.
[10:47] So the differences come from the complexity of your geometry.
[10:52] The more complex your geometry is, the more optimized for each element becomes for handling instances.


### Why FEEZ may not be recommended for Curves [11:00]
**Transcript (timestamped):**
[11:00] You have to seriously keep this in mind, because if you blindly use the zone for a huge amount of low subdivision instances, your computer will freeze.
[11:11] This is especially common when you are dealing with curves, like a curve circle that only contains 32 points.
[11:18] Plus, curves don't contain all these edges or faces.
[11:24] In this specific test, our grid takes 225 vertices plus other information to make two approaches cost a similar time.
[11:35] Nevertheless, the curve may require a much higher threshold to reach this state.
[11:40] Or not.
[11:42] Plus, you likely want a much higher instance count for curves, like when you want trillions of hairs or knitting strands.
[11:51] So overall, if you are uncertain about what you are doing, realize instances is the safest approach.


### Instance Transform in FEEZ [12:00]
**Transcript (timestamped):**
[12:00] Now, I want to demonstrate another problem with our zone.
[12:04] Let's go to a similar example where I start with an instance plane, and extrude these instances within the zone.
[12:12] I have a combined XYZ set to 001, meaning a vector pointing upwards, and I use it to replace the offset.
[12:22] Now, if I rotate my instance, you'll notice that it's not extruding upwards, it's going upside down.
[12:31] If I realize the instance, then it will extrude upwards as expected.
[12:37] A similar issue can happen with scale.
[12:40] If I only extrude one meter now, but if I scale the instance up, it will extrude much farther.
[12:48] So you may want to remove these relative influences.
[12:51] The way to do this is simply to perform the opposite operations.
[12:56] And fortunately, here we have a vector control in the extrude mesh node.
[13:01] I first need both the instance rotation and the instance scale.
[13:05] I will output both of them to the zone input.
[13:09] To perform the opposite operation, I will rotate the vector with invert rotation.
[13:15] Scaling is multiplication, so the opposite operation is division.
[13:21] Once you finish these two steps, no matter how you change the rotation and the scale, they will remain consistent.
[13:29] And the only two parameters influencing the extrusion will be the vector offsets or the float offsets directly influencing our extrude mesh node.
[13:40] Of course, this is a very specific and fortunate example.
[13:46] This is just one of a million possible examples.
[13:51] Relative influence may not always be a bad thing.
[13:54] In this mesh variable example, firstly, rotation doesn't matter.
[13:59] Secondly, we don't have a vector solution for it.
[14:03] Thirdly, absolute influence is not always a good idea.
[14:09] If I decrease the scale of the instances, then our absolute value will be able to match.
[14:16] So I'd rather disable it so that it remains relative all the time.
[14:23] But the headache still exists if you are scaling it unequally.
[14:28] And these are always things you have to keep in mind.
[14:31] It's not solvable with division in this case, as I explained in episode 7.
[14:37] Purple to gray conversion is not ideal and is strongly discouraged.
[14:43] I don't think it's common for instances to have an equal scaling, but to conclude,
[14:49] you will have to think about the influence of instance rotation scale on top of each of these modifications.
[14:57] There's no universal answer for how to solve these issues,
[15:01] and these are not avoidable even if you do the scaling afterwards.
[15:06] The issue will just occur.
[15:09] In contrast, realized instance is always simple, clean, organized, and consistent with your expectations.


### Realize & Geometry to Instance workflow [15:15]
**Transcript (timestamped):**
[15:17] Sometimes, for simplicity, you might think about realizing instance first
[15:22] and converting the geometry back to instance later.
[15:25] Note that you won't benefit from this in terms of performance.
[15:29] In fact, it can even be slower.
[15:32] Another issue is that geometry to instance always works based on the model regime.
[15:38] Here I have an example of instances in cubes on grids.
[15:42] I turn the instances into points, and they are nicely scattered,
[15:47] but if I do the same thing after realizing the instances and converting the geometry back to instances,
[15:53] you will find that all the points appear at the model regime.
[15:58] Earlier, rotate instance rotates each instance locally,
[16:02] but later, all the instances are rotated around the model regime as a whole group.
[16:09] In practice, this workflow can actually happen due to some design issues,
[16:14] but setting it up properly is not easy or straightforward.
[16:19] At last, about this modification workflow, I want to discuss set position.
[16:24] As said in the last episode, set position is almost the only exception


### Set Position for Instance Modification [16:25]
**Transcript (timestamped):**
[16:30] that normally works on the points, but will work on the instance domain for instances.
[16:35] So if you use a noise texture to directly perform a normal displacement,
[16:40] it doesn't work because instances don't have normals.
[16:44] You will have to do it manually using the stonemd attribute approach.
[16:48] Normally, they will be identical, and to create variation,
[16:53] you will need to use position and loop index together as a kind of a seed.
[16:58] In reality, this should be done more sophisticatedly.
[17:02] Due to time constraints, I want to discuss this too much here.
[17:06] Up to now, we have all been talking about smootification.
[17:10] It works very well for us to generate instance variation using for each element.
[17:15] Nevertheless, it's not used that commonly.
[17:19] Yes, I've spent a long time talking about something I haven't really used so far.
[17:25] Realized instances is so useful in daily work,
[17:28] and the real strength for each element is actually not modification,
[17:33] but the generation as hinted at by what's written on the panel.
[17:38] As we know, this zone can convert a field value into a single constant within the zone.


### FEEZ for Geometry Generation [17:40]
**Transcript (timestamped):**
[17:44] You may notice that it can be used with a random value node
[17:48] to influence the rectangular sockets on these primitive nodes, such as a cube.
[17:54] Normally, you are not able to do that as indicated by the warning,
[18:00] and you must not do it.
[18:02] I explained this in episode 4.
[18:05] If you cannot explain the reason, please go back to earlier episodes.
[18:09] This is a very fundamental and important concept.
[18:13] So here I have a grid, and my zone is on the point of domain.
[18:17] I have a random value node, and I will use the loop index
[18:21] to overwrite the implicit id attribute.
[18:25] I will link it to the vertices x inputs.
[18:28] For simplicity, I will directly instance the cube on points within the zone
[18:33] to place our cubes onto each vertex.
[18:37] Now you can see that we have nine cubes,
[18:40] each with a different number of subdivisions on the x-axis.
[18:46] This example is only practically possible with the zones.
[18:50] And it's not possible to do it after instancing.
[18:55] Since no matter how you modify the geometry using either for each element
[18:59] or realize instances, you cannot go back and change the certain parameters
[19:04] that were set at the very beginning.
[19:08] Nevertheless, please be aware that this method is not really efficient
[19:13] when out-putting instances, because the performance cost of generating cubes is real.
[19:20] Here I have a similar setup where I increased the instance count to 400 in total
[19:26] and set the subdivision amount equally on all three axes.
[19:31] The cube itself may not take too much time to generate,
[19:35] but because this zone has to run hundreds of times,
[19:39] the overall zone calculation accumulates and turns out to be quite heavy,
[19:44] even though we are out-putting instances at the end.
[19:48] In terms of performance, technically speaking,
[19:52] just like our last example about modification,
[19:56] the more complex the geometry generation process inside the zone,
[20:00] the more optimized and suitable the entire zone becomes for this function.
[20:05] I don't have any comparison provided,
[20:08] but this is a function that is generally not otherwise possible,
[20:13] so you have to accept the cost if you have to do it.
[20:18] In real life, I often use a hybrid method where I use for each element


### Hybrid Method of FEEZ & Pick Instance [20:20]
**Transcript (timestamped):**
[20:23] to generate different procedural models,
[20:26] but I don't generate one for each vertex.
[20:29] Instead, I use a point node to set a small cut, such as 5,
[20:34] to generate five different cubes.
[20:37] Then I run each of them through geometry to instance inside the zone.
[20:43] The end result is five instances,
[20:46] which we can then use with picking instance methods.
[20:50] This minimizes the cost of for each element
[20:53] while utilizing the benefits of instancing.
[20:56] On top of that, we could use all the knowledge we gained
[21:00] from the previous episodes to create random picking index,
[21:04] random rotations, random scales, random colors, and so on and so forth.
[21:09] Overall, it's about making things less boring to look at,
[21:13] and I believe no one will find out whether there are trillions of variations
[21:18] or just a repetition of a field.


### Flower Scattering File Free to Download [21:20]
**Transcript (timestamped):**
[21:22] Here I want to discuss this flower scattering animation.
[21:26] It was originally made with procedural flowers randomized using for each element.
[21:33] The flowers are picked and colored differently using the techniques we taught.
[21:38] The file is available for sale along with its included procedural flower generator.
[21:44] On the other hand, there is a free version provided as a supplement to this course.
[21:51] The free file only picks the existing flowers from a collection
[21:57] without the procedural flower generator, which is why there is a price difference.
[22:02] Nevertheless, the animation is still classical enough
[22:06] to cover many techniques we discussed in this course.
[22:10] So it would be great if you check it out.
[22:14] Note that the blue frame indicates that the functions are taught in the relevant episodes.
[22:20] Here I'm only teaching the basics in this course.
[22:24] It's time-consuming and not realistic to teach how to make flowers
[22:29] or trees in this beginner series.
[22:33] But in fact, most of the techniques that lead to them have already been taught.
[22:39] As I said, these are ultimately just the simple techniques performed step by step.
[22:45] It's something you will need to figure out and explore yourself after this course.


### Issues of Same ID & Seed in Node Tree [22:50]
**Transcript (timestamped):**
[22:51] Now, I want to show you an important note about seeds for random values.
[22:56] Right now, we are only using a single random value for demonstration.
[23:01] But in reality, you will likely need lots of random values.
[23:05] Here I have an example of instance in cones.
[23:09] I use random values for their brightness, scale, and rotation.
[23:14] You can notice an obvious pattern.
[23:17] The darker cones are always small and pointing to the right,
[23:22] while the white cones are larger and pointing to the left.
[23:27] This is simply because they are all using the same ID and seed.
[23:32] Developers have been planning for a long time to add an internal dynamic seed for every node.
[23:39] But it has been several years and it still hasn't happened.
[23:44] For the moment, solving the issue is very simple.
[23:48] Just change the seed for each individual node and you now have the black cones going left and right.
[23:56] I also made a comparable example extruding the plain instances.
[24:01] You can see that the dark extrusion are always short and the white extrusion are tall.
[24:09] The reason is the same that we are using the same ID and seed for both random values.
[24:14] To make them different, you just need to add a new value to it.
[24:18] Then the problem seems to be solved immediately.
[24:22] Now in practice, you will probably want a seed for global control.
[24:27] Then we expose the addition value to the grouping part and rename it to seed.
[24:32] We add the seed to both data flow and I will keep an extra addition to make sure the top and the bottom seeds are not the same.
[24:42] Now we are having a global seed exposed in the modifier panel or whatever place.
[24:48] This is very simple and it really happened in a demo file provided by Blender Foundation a long time ago.
[24:57] Nevertheless, this specific setup is highly discouraged.


### Hash Seed & Index Seed [25:00]
**Transcript (timestamped):**
[25:02] Because as I change the seed, you can see that we are really just shifting the sequence older
[25:09] and most of the results are still identical.
[25:13] Therefore, this brings us to a node called the hash value node where you can generate completely unique numbers based on your input.
[25:22] Either of the inputs can be considered seed regardless of their name.
[25:27] And we use two hash value nodes to replace the addition we have and make sure one value must be different from the others.
[25:36] Now as we change the seed, you won't see shifting orders behaviors again.
[25:42] I call this concept an index seed since we try to randomize the seed from a known sequence of index.
[25:50] I even have a node group for it where you plug in index and can get four random seeds coming out of it.
[25:58] You also have two seed controls either way can work.
[26:03] If four seeds are not enough, you just duplicate it and remember to change the idle of the parameters.
[26:11] Using these presets really helps the workflow a lot and saves you from having to set up all these additions manually.
[26:21] Finishing up these important aspects of seeds, I want to talk about the two real life examples to give you an idea of how these things are constructed.


### Design of Node Group for Procedural Model [26:30]
**Transcript (timestamped):**
[26:32] Here I have a group node for a stylized explosion effect that I shared for free.
[26:37] You can download it from the link in the description.
[26:41] If you want to know how it is built, I've also made an advanced tutorial in the past.
[26:47] The tutorial uses presets and is not really for beginners, but we are not far from finishing this course.
[26:55] If you're interested, you can take a look after completing this entire course.
[27:00] This node group exposes three parameters.
[27:04] The top two parameters are for the loop index and the seeds that we just discussed.
[27:10] Either of them can make the explosion looking totally different.
[27:15] And the third one is an animation factor used to control the animation as you slide it from 0 to 1.
[27:23] For the moment, you can imagine this as a static flower generator since I'm not going to provide the actual one for free.
[27:31] I've already prepared the hybrid method setup I mentioned.
[27:36] If I add this explosion unit inside and link the index to it, the effect is immediately done.


### Static FEEZ Example [27:40]
**Transcript (timestamped):**
[27:44] You can instance it however you want, such as instancing flowers on a plane with distributed points on face, or whatever.
[27:55] I just want you to understand that why I needed these seed controls for my procedural model,
[28:02] and how we utilize the peak instance to save the performance in real life, or static procedural models instancing.


### Animated FEEZ Example [28:10]
**Transcript (timestamped):**
[28:10] Next, we will talk about the animated zone generation, because I have this animation factor.
[28:17] Here I've prepared a similar setup, but I didn't use the hybrid method because I want each individual explosion to be completely different from the others.
[28:29] So I prepared a mesh line at the beginning.
[28:32] Previously, in the node tree 0.6, I was instancing directly inside the zone.
[28:40] But here, I'm instancing it outside with peak instance.
[28:44] This way, if you want random rotation and random scale, it will be more convenient without using the loop index.
[28:53] Now, first, let's finish the setup.
[28:58] Outside the zone, I've prepared the delay fault we discussed at the end of episode 12.
[29:05] I really don't have time to explain this again, so you will need to check the older video and think about it yourself.
[29:13] Now, I will play the animation.
[29:16] You may be able to roughly see the explosions happening one by one.
[29:21] It's not easy to render in the viewports, so we can switch to solid mode to visualize it more clearly.
[29:29] And this is why I cannot use the hybrid methods, because I need to ensure that each of them is actually animated at a different time.
[29:40] If you are animating them randomly, or applying some variations from outside, such as controlling their scales,
[29:49] then you can keep using the hybrid method.
[29:52] Overall, this is just an example.
[29:55] And the same principle can be used for growing flowers, trees, or whatever else you may think of.
[30:02] I hope you enjoyed this tutorial, and I will probably see you next time. Bye-bye.
[30:08] And I will see you next episode. Bye-bye.



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
