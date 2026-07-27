---
title: [Tut] How Pick Instance is used for Instance Variations - P10 Geometry Nodes Beginners
source: YouTube
url: https://www.youtube.com/watch?v=fgPiXjKkRdI
author: Bradley Animation
ingested: 2026-07-27
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/tut-how-pick-instance-is-used-for-instance-variations---p10-geometry-nodes-begin/
frame_count: 0
frame_status: pending-selection
---

# [Tut] How Pick Instance is used for Instance Variations - P10 Geometry Nodes Beginners

**Source:** [YouTube](https://www.youtube.com/watch?v=fgPiXjKkRdI)
**Author:** Bradley Animation
**Duration:** 18m7s | 16 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py tut-how-pick-instance-is-used-for-instance-variations---p10-geometry-nodes-begin <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Recap about Instance & Realize Instance [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, this is Bradley. Welcome to the tenth episode of the beginner series on geometry nodes.
[0:06] I hope you've watched the previous episodes because they will make today's topic much easier to follow.
[0:12] Last time we talked about the essence of instancing. Instances must share the same geometry data.
[0:19] So editing one will affect them all, and the DC effect includes the material.
[0:27] Because of this true instance variation is technically impossible, instead we use practical methods to make them look different using various tricks.
[0:38] And today we are digging deep into instancing and reviewing some of the tricks for variations in the later half of today's tutorial.
[0:48] Last time, we covered the basic usage of instance on points.


### Instance on Points Basics [0:50]
**Transcript (timestamped):**
[0:53] This node will conveniently take the points from that geometry right away.
[0:58] Then you just input another geometry as your instance, and you have basic instancing data, like in this example where we instance cone on each point of a cube.
[1:11] Similarly, we could use the geometry from the group input.
[1:16] My original geometry from the group input is a torus, so I'm instancing torus on a cube, or instancing cone on torus now.
[1:27] Or I have a Suzanne object, we can pull an object from the outline for an object info node to instance our Suzanne object.
[1:36] In episode 5, I already talked about the settings, original and relative.


### Object Info: Original & Relative [1:38]
**Transcript (timestamped):**
[1:42] Relative will keep the transformed data.
[1:45] For example, if I move Suzanne upwards, my instances will also move upwards relative to the designated points.
[1:53] This is often not desired in instancing, because as I rotate my instance, you will find it's rotating around the designated point instead of the object's center.
[2:05] So when you are using instancing, you probably want to use original to clear all transforms.
[2:11] Of course, original only clears the object transform.
[2:16] If your geometry has been elevated in edit mode, you are going to have the same problem.
[2:22] Also, this object info is evaluated, meaning if your object has a modifier on it, like a subdivision surface modifier, then this object info will output the modified result as well.


### Object Info Error: Geometry cannot be retrieved from the modifier object [2:26]
**Transcript (timestamped):**
[2:38] Another important aspect of the object info node is that its geometry output cannot be used on the object that holds this geometry node's modifier.
[2:49] Like here, our torus object has a node tree with an object info node trying to access the object info of the torus.
[2:57] And you end up with an arrow saying geometry cannot be retrieved from the modifier object.
[3:04] The arrow is literally what it says, you cannot view or use the geometry from the object itself, and therefore our viewport is completely empty.
[3:15] Because this geometry is meant to be evaluated after all the modifiers, so this object info is like taking geometry after the group output.
[3:27] If you are using the same object holding this node tree, you are putting information from your current group output.
[3:34] The computer cannot decide if you want egg first or chicken first, and therefore the arrow warning.
[3:41] Most of the time, please pay attention to these arrow messages, whether on the nodes or on the modifier panel.
[3:49] Not only are they straightforward, but it's also impossible for me to explain every warning myself.
[3:57] Note we have a self-object node to more easily trigger this arrow in object info. Please always be aware of what you are doing in the node tree.
[4:08] When you are using the self-object in object info, you can read only the transformed data while the geometry is not supported.
[4:18] And if you need the input geometry, currently geometry input is the only way.
[4:25] Finally for object info, I want to discuss this toggle called as instance.


### Object Info: As Instance [4:26]
**Transcript (timestamped):**
[4:31] Here I have a cube with 600 vertices on each axis. I apply the modifier, and let's go to a node tree with a moving point.
[4:43] I'm pulling the cube to instance yet on this moving point.
[4:48] You will find that the node tree is lagging a lot because of this heavy geometry.
[4:54] If I turn on as instance, it immediately becomes much faster.
[4:59] This is not exactly due to instance in itself, because if we disable the toggle and put a geometry to instance,
[5:07] then the animation won't actually give you the same performance benefits.
[5:11] This performance boost is a tricky part of Blender's cache and the evaluation system.
[5:17] Also if you remove this same time node, you won't really have any performance issues.
[5:23] Even more tricky, as long as you have a same time node, even if you are not actually using it, it will still negatively impact your performance.
[5:33] It's really a very weird topic. I mention it because it's true, but I don't want you to worry too much about this setting.
[5:41] Although the performance looks very frightening in our example, remember this is a cube that has been subdivided much more than normal.
[5:49] In real life, it's quite rare that you would instance in a single object this heavy and worry too much about this toggle.
[5:58] The setting is not on by default because a common use case is to evaluate the actual geometry.
[6:05] For example, I discussed morphing with mixed position in episode 5, and similarly, the shape key animation worked around using geometry nodes.
[6:15] In order to access mesh position information for this geometry, they must not be used as instance.
[6:24] You turn it on and it will not work. If you don't keep the toggle off, you would have to manually realize the instance for it, whichever way the result is the same.
[6:36] As I said in the last episode, making something into an instance doesn't necessarily improve the performance, and having realized the data doesn't always mean it's a fatal thing.
[6:47] It's kept off with a reason.
[6:50] Besides this specific use case for performance, the instance option can be useful when working with special object types.
[6:59] Currently, geometry nodes do not fully support lights and cameras because they are not represented as regular geometry like meshes or other geometry types.


### Object Info: to instance light and camera [7:00]
**Transcript (timestamped):**
[7:10] Here I have a point-slite object elevated above the ground, and I reference it using the object info node with as instance turned off.
[7:21] As you can see, nothing appears in the viewport. The tooltip also indicates that there is no geometry to output.
[7:30] Nevertheless, if I enable as instance, you can see the light appear in the viewport, especially if I toggle as instance on and off.
[7:40] Furthermore, our cube can be illuminated by these light instances.
[7:46] Basically, instancing is like pushing a present box around the data.
[7:51] Although the internal data is not supported or editable, geometry nodes will recognize the present box and show it with internal content.
[8:01] Although you cannot edit the internal parameters, maybe you may need to instance lighting in EV, and it can be helpful.
[8:09] In Cycles DC is not suggested because you can just take objects with the emission shader.
[8:17] Now we've covered a single object, so we are moving on to collection info and pick instance.


### How Pick Instance is useful in Instance Variation [8:21]
**Transcript (timestamped):**
[8:24] Pick instance is one of the first features that lets you fake instance variation.
[8:31] In Blender, we cannot so easily generate instance variation, but assuming you have already prepared variants of a flower,
[8:40] then you will be able to instance different flowers that makes it look like you have instance variations.
[8:48] Like in this case, as I drop my flower variants to a collection, then different variants of flowers are picked and instanced.
[8:57] Likewise, in Blender, we cannot offset keyframes in geometry nodes, but you can duplicate the animation with different delays and instance them.
[9:08] Then it will look like we have instances with different animation delays.
[9:13] Therefore, it's a hack, but it works.
[9:17] And it's used quite commonly in many real life projects, since you may not always be productive to create everything procedurally due to skill and technical issues.
[9:29] Collection instance is simple. Just like we can pull in an object to create an object info, we can pull in a collection to create a collection info.


### Collection Info: Basics [9:30]
**Transcript (timestamped):**
[9:40] Nevertheless, unlike the object info node which outputs realized data by default,
[9:46] collection info outputs a single instance containing all of its internal content by default.
[9:53] Therefore, for our Snowman collection, this use case is the same as the regular object info, and it happens when the geometry is built by multiple objects that you don't want to join otherwise.
[10:09] Now, I have another collection of different objects like a cube, Cylinder, Sophia, and a Taurus.


### Collection Info: Separate Children & Instance Depth [10:10]
**Transcript (timestamped):**
[10:16] And I want to instance one of them on each point of my grid, pretending that I have instance variation with different geometry.
[10:25] So, in a different node tree, I pull in the collection as before.
[10:30] The collection is showing a single instance containing four different objects, and I need to enable separate children.
[10:39] It removes the outer instance container, and it reveals the insider content as separate instances.
[10:48] So, I end up four instances for four different objects respectively.
[10:54] This is a bit like a realized instance, but instead of realizing all instances, I disable all options and use the depths.
[11:04] Depths zero means nothing is removed, depths one meaning we will remove the outer most layer and reveal one layer inside.
[11:14] And of course, in this case, using the toggle is much more convenient.


### Collection Info: Reset Children [11:20]
**Transcript (timestamped):**
[11:20] I will also turn on reset children so that all transforms of inner objects are cleared to the world of origin.
[11:28] Previously, this function was handled by the original and relative settings on the object info node.
[11:35] But here it's managed by this reset children toggle in practice.
[11:39] It may be confusing to think about, but I'm not going to elaborate on the differences here.
[11:46] This is simply a toggle you click that solves many problems.
[11:50] Right now, if you output this instance to instance on point, we're still instancing the input as a whole.
[11:59] So now it's time for us to turn on picking instance, and we've completed our goal right away.


### Pick Instance Error about realized geometry [12:00]
**Transcript (timestamped):**
[12:06] It's important to note that picking instance is literally picking instances.
[12:11] Your input geometry must be real instances.
[12:15] This means if you import anything like a match or realize the data, you will have a warning to notify you that it doesn't work.
[12:25] And you can use geometry to instance or whatever method to solve it.
[12:33] Anyway, we completed our goal.


### Pick Instance: Instance Index [12:34]
**Transcript (timestamped):**
[12:35] However, right now you may notice they are being picked in a somewhat visible order.
[12:41] If you want to pick them completely randomly, you will want to work with the instance index setting.
[12:48] By reading the tooltip, it says it uses ID or index.
[12:53] This is actually the same concept as the ID you see on the random value node.
[12:59] Most of the time in practice, ID is the same as index.
[13:04] If you add a set ID node and read its tooltip, it's using the index to set the ID.
[13:10] Therefore, whether you input ID or index into this field, the result won't change here in this case.
[13:17] There is only one common exception.


### Distribute Points on Face sets ID [13:18]
**Transcript (timestamped):**
[13:19] The distribute points on faces node actively sets ID.
[13:24] As you can see in the spreadsheet, we have a column of ID.
[13:28] These are large unique numbers assigned to each point.
[13:33] And here we have an example using it to instance objects on a plane.
[13:38] You can see that index and ID is not having the same result.
[13:44] And the disabling ID will not change the result, but the disabling the index will change it.
[13:51] This is because by default, instance index is using ID, but most of the time, ID is determined by the index.
[14:00] Therefore, this is the situation.
[14:02] Moreover, this distribute points node is used in the scatter on surface, which is a group node asset shipped with blender.
[14:13] As you see the menu about random and Poisson disk that also present on the distribute points node.
[14:21] Therefore, this node will also generate IDs.
[14:25] These are just some extra stories about ID and index.
[14:30] As I said in real life, there differences aren't very important for beginners because it's automatically set within the instance index without users awareness.
[14:43] So going back to our previous problem, we have this regular pattern because the index follows a fixed sequence like 0, 1, 2, 3.


### Randomize Instance Index [14:45]
**Transcript (timestamped):**
[14:52] And here the next index should be 4.
[14:55] But since we only have 4 objects in total, index 4 is equivalent to 0, followed by 1, 2, 3 and so on.
[15:04] Now, a simple way to solve this pattern is to use a random value node.
[15:09] We set it to integer and connect it to instance index.
[15:13] Immediately the problem is solved.
[15:16] We don't need to worry about the integer range here because the values will automatically wrap around.
[15:22] Just like the cases of 4 and 0.
[15:26] Of course, ideally, you may want the numbers to be more accurate because the instance index can also be used to control the ratio of fixed instances.
[15:36] I'm not going to elaborate on the detailed methods here, but let's say you want certain objects to be instanced more often than the others.
[15:45] A simple cheating method is to duplicate the same object multiple times.
[15:51] Like the cylinder and the sphere here.
[15:54] So they have a higher chance of being picked.
[15:58] As you can see, even if you change the seed or not.


### Instancing Collection within Collection [16:00]
**Transcript (timestamped):**
[16:04] Now we finish the collection with objects.
[16:08] What if we have a collection containing two different versions of a snowman collection?
[16:13] Here I have a collection of snowman with Susan Hat and a regular snowman we saw earlier.
[16:20] And I have a note tree doing the operation we did earlier.
[16:24] By default it's instanced in everything as a whole, so we need to separate the children.
[16:29] Then each collection will be revealed as its own instance, so they could be picked respectively.
[16:37] Recent children won't be very useful here because these are collections and they don't have object transforms.
[16:45] But anyway, often please just make sure your stuff is centered around the world origin.
[16:52] Finally, so far we've discussed a lot about this external geometry.
[16:58] What if we are generating procedural variations inside the geometry nodes?


### Geometry to Instance [17:00]
**Transcript (timestamped):**
[17:03] I have hinted the idea before that we have geometry to instanced.
[17:09] And it has this elongated multi-input socket to receive multiple inputs.
[17:14] We should have seen it in joint geometry nodes.
[17:17] Nevertheless, in this case, it's not simply joining, but also converting each linkage into their own instances.
[17:24] So you can pick instance with what we taught earlier.
[17:28] I think this is one of the most common use case of it.
[17:32] Now, basically these are all cases about instance on points and pick instance.
[17:38] We've covered many related topics, but in daily life,
[17:42] you are basically just pulling objects or collections from Outliner
[17:47] and deciding whether to use pick instance or not.
[17:50] And although this sounds very much like a cheat or a many trick,
[17:54] it's something we really do a lot in daily life for cheap instance variation.
[18:00] I hope you enjoyed this video and I'll probably see you next time. Bye-bye.



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
