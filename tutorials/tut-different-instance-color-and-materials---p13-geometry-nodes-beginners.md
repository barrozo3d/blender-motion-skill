---
title: [Tut] Different Instance Color and Materials - P13 Geometry Nodes Beginners
source: YouTube
url: https://www.youtube.com/watch?v=812uN8EFWVs
author: Bradley Animation
ingested: 2026-08-11
blender_version: "Blender 5.3+ referenced on-screen (Switch node in shader editor); techniques otherwise version-general"
tags: [geometry-nodes, instancing, materials, shaders, procedural, attributes, eevee, cycles, motion-graphics, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/tut-different-instance-color-and-materials---p13-geometry-nodes-beginners/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# [Tut] Different Instance Color and Materials - P13 Geometry Nodes Beginners

**Source:** [YouTube](https://www.youtube.com/watch?v=812uN8EFWVs)
**Author:** Bradley Animation
**Duration:** 30m3s | 18 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Random Rotation of Instances [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, this is Bradley. Welcome to the 13th episode of the beginner series on geometry nodes.
[0:06] I hope you have watched the previous episodes because they will make today's topic much easier to follow.
[0:12] In the last two episodes, we respectively talked about rotation scales for instances.
[0:19] We mainly focused on features related to those topics, such as online rotation to vector, access to rotation,
[0:27] and the demographic aspects of creating forks.
[0:32] Instead of giving a full recap, I just want to emphasize what to do if you want randomness for these two parameters.
[0:41] Here I have a simple setup instance in a single flower on grid points.
[0:46] It looks very boring because everything is so organized, so I want to add some rotation variation.
[0:54] We have the random rotation assets shaped with Blender. By default, it rotates on all axes.
[1:01] If you want to rotate only on the z-axis, you can decrease the maximum value.
[1:07] And you will find that the flower becomes less tilted while keeping their random rotation around the z-axis as you change the seed.
[1:16] If it's not easy to see, you can switch to Suzanne to see the effect more clearly.
[1:22] By design, it assumes you want 360-degree random rotation on the z-axis.
[1:28] This can be a bit surprising because people may not immediately realize that decreasing the maximum value still allows rotation to happen somewhere within an internally defined range.
[1:41] If you want to construct your own methods, you can use a random rotation or the set to vector to construct an Euler rotation.
[1:50] If you prefer a quaternion rotation, you can use axis angle to rotation with a random value node set to float. All these methods can work.
[2:01] If you already have an existing rotation, such as from the distributed points node, you can use the exact same process with the rotate-rotation nodes in local mode.


### Random Scales of Instances [2:15]
**Transcript (timestamped):**
[2:15] For random scale, you can use either random value set to float or vector depending on your needs.
[2:22] Float gives a unified scale across all three axes and is easier to control.
[2:28] And the vector gives independent values for each axis. Sometimes it creates weird results, but anyway, I think float scale is the most common approach in real projects.
[2:40] So these are some reminders about the random rotation scale. They may not have been directly mentioned before, but you should be able to figure them out yourself after watching the previous episodes.
[2:53] I really cannot cover every possible combination of the techniques we have taught, so you have to use your own logic and experiments.


### Instance Attributes Vs. Attributes of Contained Geometry [3:00]
**Transcript (timestamped):**
[3:03] Today's topic is to discuss instance attributes. At the very beginning of episode 9, when we discussed the instance, I reminded you about the relationship between different data structures.
[3:15] An object is like a container holding the mesh data. And in object properties, we can move, rotate and scale it.
[3:26] We can also swap the mesh data. For example, we can replace the default cube mesh with a Suzanne mesh.
[3:33] This relationship is somewhat comparable to the relationship between an instance and its internal content.
[3:39] Although we cannot easily swap the internal geometry of an instance in geometry nodes at the moment, what I want to mention here is the separation of data.
[3:50] For example, even if my mesh becomes Suzanne, it does not change the name of the object. It does not change the object transform, including location, rotation and scale, or any other object properties.
[4:06] This separation also applies to geometry nodes. Instance attributes are completely separate from the attributes of their internal content.
[4:18] Here, I have a simple example where UV spheres are instance on a cube.


### Random Color per Instance [4:22]
**Transcript (timestamped):**
[4:24] My current goal is to create different instance colors in the material. To export the color from geometry nodes to the shader, we need to use the store name attribute.
[4:36] Since this is color information for instances, it makes sense to work on the instance domain.
[4:42] For the name, I will simply call it C. For random colors, I will use a random value node.
[4:50] It does not have a color mode, but as we discussed before, color can be converted from a vector within the range of 0 to 1.
[4:59] I have already prepared the material, so let's go to the shader editor. I will use the attributes node and input C.
[5:06] However, you will find that it's not working. This is because shader attributes also have a concept similar to domains, as shown in this menu.
[5:16] It's slightly different from the domain system in geometry nodes because shader can receive more types of information from the entire blender system.
[5:25] However, you do not need to worry about those details. Here, you can simply see that there is an Instancer option.
[5:33] Once you select it, it immediately works. This is the standard method to make it work.
[5:41] One thing I want to mention is attribute interpolation. Here, if we look at the domain side nodes for each geometry type,


### Instance Attribute Interpolation [5:50]
**Transcript (timestamped):**
[5:50] you will find that instances are unique because they do not contain a point domain, while meshes, point clouds, and curves
[5:59] can share their point domains through conversions such as meshed points, point curve, and so on.
[6:07] However, there are several exceptions regarding instances. Since we are distributing instances onto individual points, each point corresponds to one instance.
[6:21] Therefore, the instance on point nodes will actually pass point attributes to each instance.
[6:29] This means I can store the named attributes earlier in the data flow on the point domain, and the results will remain the same.
[6:39] Personally, I prefer this method because it avoids one extra step of dealing with the domain menu.
[6:47] This is the most common way to allow variations between different instance geometries.
[6:54] However, once you do that, our shader setup stops working. The attribute is still on our geometry.
[7:02] If you check the named attribute nodes, you may be able to find our attribute C, and it's likely on the point domain.
[7:11] We can also confirm it with the viewer. Basically, when you realize the instance, the instance attributes will be transferred to every point of that specific geometry.
[7:24] It does not work with our current material because there are no longer instances. Therefore, for the shader material, you need to change the data type from instance to geometry.
[7:36] Personally, in real projects, I usually just realize instances without thinking too much about it. I know many people dislike this node, but in motion graphics workflow, it's not always a harmful operation.
[7:51] My personal preference is to realize instances earlier and work with attributes directly on geometry instead.
[7:59] This avoids switching back and forth between instance and geometry domain because of the later changes in the node tree.
[8:08] Only when I find that realized instance is truly becoming a performance bottleneck, I will start to optimize the setup such as trying to remove unnecessary realized instance nodes.
[8:23] Of course, this is just my personal workflow preference, and you may prefer a different approach.
[8:30] Now we have finished creating random colors for each instance. Let's move on to a similar example we discussed in episode 9.
[8:39] In this example, we are instancing tube on a grid. We first set the instance with a red material, and then we try to select an index to set a green material.


### Modifying Instanced Geometry [8:40]
**Transcript (timestamped):**
[8:53] Surprisingly, instead of setting the material on the fifth instance, it assigns the material to a polygon inside each cube instance.
[9:04] This entire setup is equivalent to setting the material step by step before instance on points, and then instancing this specific result onto each point of the grid.
[9:17] If we switch the viewer between the two setups, you won't find any difference.
[9:24] Similarly, I've shown the case where we extrude a mesh with a random value, each instance outputs exactly the same result.
[9:34] This process is the same as directly extruding it before instance, and therefore the deformation will be identical across all instances.
[9:44] Generally, the modifications available before instance on points are still available after instance on points.
[9:53] There is one well-known exception regarding the set position node. Here, before instance on points, I use set position with a noise texture.


### Set Position to modify Point/Instance Domain [10:00]
**Transcript (timestamped):**
[10:05] As I scale up the displacement, you can see that each point on the original cube has been displaced. The result is then passed equally to all instances.
[10:18] However, if I perform the same process after instance on points, each cube instance is moved as a whole.
[10:28] Basically, set position in this case is equivalent to the translated instance node without the local space option.
[10:37] Please don't ask me why we have this exception. I really do not know.
[10:43] However, we can cheat with a different method. Set position is a node created for our convenience.
[10:51] Essentially, it works by storing and updating the existing position attribute.
[10:57] The offset input is simply an additional value added to the existing position.
[11:04] So we can do exactly the same with the store name attribute. We store the position after adding the noise displacement.
[11:12] And yes, congratulations, you've achieved the equivalent of set position on the point domain while the geometry is still inside an instance.
[11:23] Of course, there is no variation between instances, but it works.
[11:29] To summarize what we have discussed so far, we have two levels of data structures, instance attributes and the attributes of the geometry inside the instance.


### Attributes of Contained Geometry [11:30]
**Transcript (timestamped):**
[11:40] They are separated, and each one is controlled by a different data flow into instance on points.
[11:47] The point domain from the top flow is directly responsible for the instance attributes.
[11:53] The bottom flow is responsible for all domains inside the instance geometry.
[12:00] Both domains exist and are accessible while working with instances.
[12:06] This means you can directly visualize the UV map from our instance cube.
[12:12] You can see that we have a proper UV map with its UV same on our cube.
[12:19] This can become important after a realized instance.
[12:23] For example, here we are instance in plane on a random rotation only on the z-axis.
[12:30] If I visualize the checker texture, it works based on the position attributes of the geometry as a whole.
[12:38] It looks straight and ugly, but still acceptable.
[12:42] However, if I tilt the plane into different orientations, you can see that the result becomes more disorganized, because mapping in 3D space is in nightmare.
[12:54] So we have two ways to solve this problem.
[12:58] One way is to use the UV map, which is a known 2D coordinate system.
[13:04] It works.
[13:06] The other way is to capture the position attribute.
[13:10] This way, you know your original plane has a good texture mapping, and you can capture the position and pass it through after realizing instances.
[13:21] The result will be preserved correctly.
[13:24] These examples are actually quite common when creating stable and organized coordinates or lost controls.
[13:32] Because it's possible that you are animating the rotation of these instances, and you don't want your effect to change all the time, like this checker texture.
[13:44] And remember, realizing instances is a well-known way to allow variations between instances' geometry.
[13:53] Right now, the textures are all the same across instances, but you can add a random value node based on the Mesh Island Inbacks to make them look different.
[14:05] Up to this point, I want to mention a critical confusion that people commonly have.


### Auto mode of the Viewer on Instances Uses the Point Domain [14:10]
**Transcript (timestamped):**
[14:11] At this moment, we are visualizing the result after realizing instances.
[14:17] But what happens if we do not realize them and keep the geometry as instances?
[14:23] Then it behaves the same way as we discussed earlier with setMaterial and extrudeMesh.
[14:29] The auto mode of the viewer on instances visualizes the results from the point of domain.
[14:35] Switching it manually to point of domain will not make any difference.
[14:40] And sometimes, you want to give each instance a different color.
[14:44] We can use the previous methods with random value on vector, but you will find that the result is miserable on the point of domain.
[14:52] The exact same result happened in auto mode.
[14:55] To visualize the instance's random color, you need to manually switch the viewer to the instance's domain, just like we did when setting random colors at the beginning.
[15:06] Many people dislike the auto mode behavior because it shows the point of domain for instances and it can be confusing.
[15:14] Some community members have suggested changing this behavior.
[15:19] I'm not sure whether it will happen, so depending on when you watch this tutorial, you may see the same or different behavior in this simple setup.
[15:30] Regardless, both behaviors can make sense and can be important in different situations.
[15:37] Now, we have finished discussing attribute interpolation between the two data flows, top and bottom, regarding the instance on point node.
[15:48] Let's move on to a more complex problem and see how we can solve it using attributes on two different levels.


### A Challenging Question [15:50]
**Transcript (timestamped):**
[15:56] So here, I'm instancing cube on a grid again.
[16:00] Within each cube, I want to color only specific polygon, and for a specific instance, I want the polygon to show a different color.
[16:10] At the bottom, I can store a face-doming mask called Geo, using the index comparison method we showed earlier.
[16:19] As I confirm the target polygon, I will plug it into the boolean socket.
[16:26] Now on the top, I will store a point-doming mask called inns, using the same method.
[16:33] It's better to confirm it towards the viewer before proceeding.
[16:38] Finally, I've already prepared an empty shader.
[16:42] Now inside the shader, the geo attribute is on the geometry domain.
[16:47] We don't have a boolean socket output, nor do we have a switch node.
[16:52] But we can use a factor and a mix node instead.
[16:56] Make sure it's connected to the factor input and set the mixed data type to color.
[17:02] As we discussed the last episode, factor 0 goes to A, which I will set to black,
[17:09] and factor 1 goes to B, which I will set to blue.
[17:13] Then we move on to the inns attribute, which is on the instance domain, since we haven't realized the instances.
[17:22] We do the same thing with the mix node.
[17:25] I will drag and drop the previous color into A, and set up another color in B.
[17:31] Finally, I output it to replace the polygon color we set earlier.
[17:38] At the end, we accomplish the goal.
[17:41] I'm not sure if I would call this an advanced technique, but anyway,
[17:46] this is an example demonstrating how to use attributes from different domains at the same time to accomplish color variations between instances.
[17:57] Here, I hope you realize that in geometry nodes, instead of working with multiple materials,


### Geometry Nodes prefers a "Single Material" workflow [18:00]
**Transcript (timestamped):**
[18:05] we can work with a single material and use attributes and mix nodes to control different parts of the geometry.
[18:12] This way, it's also much easier to use the fall off techniques we discussed last episode for motion graphics purposes,
[18:21] such as color and the material transitions.
[18:25] Moreover, in previous episodes, I discussed that picking instances can have unique use cases for different geometries.
[18:35] Here, I have three geometries, each with its own unique material for coloring.
[18:41] This method definitely has its downsides.
[18:44] No matter how you change the picking index, the cone will always be blue.
[18:50] Therefore, for different colors, you can use this instance attribute method instead.
[18:57] This approach is much more flexible that your instance will never be limited to a specific color anymore.
[19:04] And this applies not only to color, but to shaders in general.
[19:09] You can also decide whether they share the same roughness, metallic values, or even mix different image textures.
[19:17] Basically, everything remains editable.
[19:21] Up to this point, we have been setting up colors directly in geometry nodes.


### Random UV offset in Shader [19:23]
**Transcript (timestamped):**
[19:26] Now, let's move on to a different case.
[19:30] Sometimes we don't just need different colors.
[19:33] We may need all kinds of random parameters, such as different UV offsets.
[19:39] Here we have a similar but different example.
[19:42] On the bottom floor, we store a UV map on the face corner domain.
[19:48] On the top floor, we store a random vector called w on the point domain.
[19:54] UV maps normally range from 0 to 1.
[19:57] For UV offsets, you could keep everything within the same range as we did for colors,
[20:04] or use a larger range depending on your needs.
[20:07] In the shader, I use this UV map to drive the checker texture, which looks identical across all instances.
[20:15] But when I add our random vector w from the instance domain, you can see that the textures are no longer identical.
[20:24] This UV offset technique can be used in many situations.
[20:28] I also want to remind you that it's common to see a mapping node in shaders,
[20:34] which is mainly provided for convenience.
[20:37] In reality, location is simply addition, rotation is a vector rotation, and the scale is multiplication.
[20:47] So regardless of how the node tree presents it, the underlying operations are essentially the same.
[20:54] I may use either method randomly throughout the tutorial, or game-like visual effects.
[21:00] Also, I often increase the random value much higher for a larger offset.
[21:06] But anyway, now I want to remind you of some issues.
[21:12] Here, you can see the texture is different across instances because of the shifted UVs.


### Cycles can't displace Instances differently [21:15]
**Transcript (timestamped):**
[21:19] We can plug this checker texture into bump to influence the normal.
[21:24] It's not very beautiful, but you can see that the fake shadow corresponds to the texture we have.
[21:31] Now, we do the same for displacement.
[21:35] Make sure to go to the mPanel option and switch to bump and displacement.
[21:41] Immediately, in EV, you can see that the white regions are elevated by our displacement node,
[21:48] and they correspond to our texture.
[21:51] However, if I switch the render engine to cycles, you will find that it doesn't work.
[21:59] Cycle displacement does not show the same result as the color.
[22:04] This problem in cycles is a non-limitation.
[22:07] Displacement is essentially a kind of geometry modification,
[22:12] and to save performance, or whatever the reason may be, geometry is linked.
[22:19] Therefore, this kind of differential displacement between instances is not allowed.
[22:24] I don't know why EV allows it, but anyway.
[22:27] To solve these in cycles, the only solution is to realize instances,
[22:32] and to make the same setup work, do not forget to change the instance or attributes into a geometry attribute.
[22:41] So, displacement not working in cycle is one issue.
[22:46] The second issue is about limitation on the number of attributes.


### Each Eevee material can only use up to 14 attributes in total [22:50]
**Transcript (timestamped):**
[22:51] Here, I have a setup where I store eight groups of two attributes, making 16 attributes in total.
[22:59] In the shader, I simply add them all together.
[23:03] If I output the result using up to the 14th attribute, the cube is still white.
[23:11] But here by adds attribute 15 and 16, the shader starts to show in the pink arrow result.
[23:18] If you stop using attributes beyond the limits, it will recover.
[23:23] Likewise, if you remove the previous attribute usage and decrease the total number of active attributes,
[23:31] it will also return to the normal result.
[23:34] And if I switch to cycles, it shows the normal result.
[23:40] Basically, each individual EV material can only use a maximum of 14 attributes at the same time,
[23:49] while cycles can use an unlimited amount.
[23:53] Personally, I've never reached this limit.
[23:57] I don't think it's very common, but ultimately it depends on your setup.
[24:01] The third issue is related to a possible solution for this kind of problem.
[24:08] Previously, we were storing random colors and offsets directly within geometry nodes.


### White Noise for Random Value Function in the Shader [24:10]
**Transcript (timestamped):**
[24:15] You may think about storing an ID or index attribute in geometry nodes
[24:20] and generating random values in the shader instead,
[24:23] so that we can minimize the number of attributes used in the shader.
[24:28] And this is what I'm doing right now.
[24:31] As before, I've already prepared the material.
[24:36] Now, let's go to the shader.
[24:40] We don't directly have a random value node in the shader.
[24:43] What you are seeing here is an asset I created for myself for convenience.
[24:50] This asset uses the white noise texture to reproduce the random value function.
[24:56] For a 3D vector, each channel can be used as a seed.
[25:01] So we have one channel for ID, a second channel for seed,
[25:06] and a third channel for anything else.
[25:09] Now I plug the ID attribute into one of the channels
[25:13] and visualize the white noise texture.
[25:16] We immediately get a random value from 0 to 1 for each instance.
[25:21] By manipulating the other seed channels, I'm changing the random seed.
[25:26] You can also use the color outputs for random colors.
[25:30] Now, as you know, these values and colors are in the range from 0 to 1.
[25:36] This means they can be coupled with mixed nodes for float and vector to create other ranges.
[25:42] These functions together are basically the equivalents of the random value function in the shader.
[25:49] Right now, this works well in both EV and cycles.
[25:54] If I realize the instance, we lose the randomness because we need to switch the attribute from instance to geometry.


### Shader Inaccuracy from Geometry Nodes to Render Engines [26:00]
**Transcript (timestamped):**
[26:02] Then you will immediately find another problem about these flickering artifacts,
[26:08] where some parts appear darker than others.
[26:11] This happens in cycles, and if I switch to EV, it does not look any better.
[26:19] This is because for some technical reasons, the render engine cannot preserve precise values.
[26:27] In geometry nodes, these indices may look like 0, 1, 2, 3, and so on.
[26:34] But in the shader, they may become values like 1.0001 or something similar.
[26:42] White noise is very sensitive to these small differences,
[26:46] so it generates different values for each pixel causing these artifacts.
[26:51] This is more than simply the fact that we do not have an integer socket from the attribute node.
[26:57] The developers have been very clear that it's impossible to fix this issue.
[27:02] Recently, I discovered that you can use a round-mass node to remove this inaccuracy and make the result look correct.
[27:12] I have tested this method to some extent, and personally, I haven't found any real issues so far.
[27:19] However, I also cannot be 100% confident because I haven't tested every possible cases.
[27:28] Float point precision issues are notorious in Blender, so you never know when this problem may appear.
[27:35] So I want you to keep this issue and its possible solution in mind.
[27:40] At the end, I want to discuss some ways of generating random colors.
[27:46] Previously, I already discussed using the vector-to-RTB method.


### Ways to generate Random Colors [27:50]
**Transcript (timestamped):**
[27:52] You can also create a random value node set to float to generate a gradient from 0 to 1,
[27:59] and combine it with a color ramp so you have more controls.


### A summary of Fake Instance Variations without realize Instance [28:00]
**Transcript (timestamped):**
[28:04] You can change the interpolation type and even distribute the stops so that you have an equal chance of selecting each color.
[28:13] For the other workflow, I already sawed an index attribute and prepared the white noise texture setup we just discussed.
[28:22] Since the value is also from 0 to 1, we can use exactly the same color ramp method and change the seed or whichever parameter you want.
[28:32] Now, by finishing this episode, we have basically covered all the common cheating methods
[28:39] for creating fake instance variations without realizing instances.
[28:45] In episode 10, we talked about pick instance, which is a very common method in real projects to fake complete geometry variations.
[28:57] Then we discussed the transform aspects of instances, including earlier today,
[29:03] where we discussed random rotation and random scale to make similarities less noticeable when using the same geometry.
[29:13] And today, we discussed the different colors and the texturing methods.
[29:19] Next episode will be our last episode about instances, where we are going to talk about the for each element as well.
[29:28] It will lead us towards the true variations we eventually want or fully proceed workflows and potentially provide a replacement for the realized instance method.
[29:41] Or not.
[29:43] I hope you enjoyed this tutorial and I will probably see you next time. Bye bye.



---

## Captured Frames

- [5:10] tutorials/frames/tut-different-instance-color-and-materials---p13-geometry-nodes-beginners/frame_000.jpg
- [7:05] tutorials/frames/tut-different-instance-color-and-materials---p13-geometry-nodes-beginners/frame_001.jpg
- [10:20] tutorials/frames/tut-different-instance-color-and-materials---p13-geometry-nodes-beginners/frame_002.jpg
- [12:45] tutorials/frames/tut-different-instance-color-and-materials---p13-geometry-nodes-beginners/frame_003.jpg
- [17:00] tutorials/frames/tut-different-instance-color-and-materials---p13-geometry-nodes-beginners/frame_004.jpg
- [21:55] tutorials/frames/tut-different-instance-color-and-materials---p13-geometry-nodes-beginners/frame_005.jpg
- [23:10] tutorials/frames/tut-different-instance-color-and-materials---p13-geometry-nodes-beginners/frame_006.jpg
- [25:10] tutorials/frames/tut-different-instance-color-and-materials---p13-geometry-nodes-beginners/frame_007.jpg

---

## Structured Notes

### Core Technique
Giving each Geometry Nodes instance a unique color/material/shader parameter without realizing instances (which is expensive and collapses per-instance geometry variation) — by exporting instance-domain attributes into the Shader Editor via Store Named Attribute + the Attribute node's Instancer domain setting, plus generating extra per-instance randomness directly inside the shader with a White Noise Texture instead of storing more geometry-node attributes.

### Summary
Bradley Animation's Geometry Nodes beginner series episode 13 covers instance-level shading. After quick reminders on randomizing instance rotation/scale, the core lesson is the separation between **instance attributes** and **attributes of the geometry contained inside an instance** — two independent data flows into Instance on Points. To get a per-instance color into the shader, store a named Color attribute on the **Instance** domain, then in the Shader Editor's Attribute node switch its type from the default to **Instancer** (not Object/Geometry) — this is the standard trick that's easy to miss. Realizing instances collapses this: the instance attribute transfers down onto every point of the realized geometry, so the shader's Attribute node type must be switched from Instance to Geometry to keep working. The episode covers several gotchas: Set Position behaves differently before vs. after Instance on Points (point-level displacement vs. moving the whole instance) with a Store Named Attribute workaround to fake point-level displacement after instancing; UV maps and captured Position attributes survive realize-instances correctly while 3D-position-based texture mapping (e.g. a Checker Texture) becomes visually disorganized once instances are rotated into different orientations; the Spreadsheet/viewer's "Auto" domain-display mode is a common confusion point (it shows the Point domain for instances, not the Instance domain, so per-instance random colors look wrong until you manually switch the viewer domain); a worked example mixes attributes from *two* different domains (a per-polygon mask + a per-instance mask) inside the same shader via chained Mix (Color) nodes to control which polygon on which instance gets a highlight color — demonstrating Geometry Nodes' general preference for a **single shared material controlled by attributes**, over Blender's traditional multi-material-slot workflow. The back half covers renderer-specific limitations: Cycles cannot displace instances differently (a known Cycles limitation, since instance geometry is linked/shared — realizing instances is the only fix), EEVEE materials cap out at **14 simultaneous attributes** (Cycles has no such limit), and using a White Noise Texture fed an ID/index attribute as a fake "random value in the shader" function to reduce attribute count — with a caveat about float-precision-driven flickering artifacts (integer-looking indices become slightly-off floats like 1.0001 by the time they reach the shader) fixable with a Round node. Closes with two random-color-gradient recipes using a Color Ramp.

### Key Steps
1. **Per-instance color, the standard way:** on the Instance domain, use **Store Named Attribute** (type Color, name e.g. `C`) fed by a **Random Value** node (color = a Vector in range 0–1, since Random Value has no native color mode). In the Shader Editor, add an **Attribute** node with the name `C` — by default it won't work; open its domain dropdown and select **Instancer** to read instance-domain data instead of geometry-domain data.
2. **Instance Attribute Interpolation:** instances have no Point domain of their own, but since **Instance on Points** assigns one instance per point, storing the attribute earlier on the **Point** domain (before Instance on Points) produces an identical result and skips the extra Instancer-domain menu step — this is the author's preferred shortcut. However, once you **Realize Instances**, the instance attribute is transferred onto every point of the now-realized geometry, so the shader's Attribute node domain must be switched from **Instance** to **Geometry** or it breaks.
3. **Modifications before vs. after Instance on Points are generally equivalent** (setting a material on a face, extruding with randomness before instancing produces the same per-instance result as instancing first) — **except Set Position**, which is the one well-known exception: before Instance on Points, Set Position displaces individual points of the *source* geometry (affecting all instances identically); after Instance on Points, Set Position moves each *whole instance* as a rigid body (equivalent to Translate Instances without Local Space). To fake point-level displacement while still working on already-instanced geometry, use **Store Named Attribute** on `position`, adding the noise offset onto the existing position value — replicating what Set Position does internally, since Set Position is just a convenience wrapper around storing/updating the position attribute.
4. **UV/Position attributes survive realize-instances correctly**; raw 3D-position-based texture mapping (e.g. a Checker Texture with no UV map) does not — once instances are tilted into different orientations, position-based mapping becomes visually disorganized per-instance. Fix: either give the source geometry a proper **UV Map** before instancing, or **Capture Attribute** the position before realizing instances and pass that captured value through to preserve consistent per-instance coordinates (important for animated rotation, so a texture effect doesn't visibly swim as instances rotate).
5. **Spreadsheet/Viewer "Auto" domain gotcha:** the Viewer node's Auto mode displays the **Point** domain for un-realized instance geometry, not the Instance domain — so per-instance random colors will look wrong/uniform in the viewer until you manually switch its domain dropdown to **Instance**.
6. **Multi-domain shader mixing (dual-mask coloring):** store a per-polygon boolean mask (`geo`, Face domain, via index comparison) and a per-instance boolean mask (`inns`, Point/Instance domain, same method) separately. In the shader, since there's no boolean socket/Switch node pre-5.3, use two chained **Mix (Color)** nodes instead: plug each mask into a Mix node's Factor (0 → input A, 1 → input B), assign different colors to A/B on each Mix, and chain the second Mix's output to replace the first's result — letting a single material show different colors on different polygons *and* different instances simultaneously. An on-screen caption notes the **Switch node** (mentioned in the previous episode) became available in the Shader Editor starting **Blender 5.3**, which can replace this Mix-node workaround going forward.
7. **Random per-instance shader parameters beyond color** (e.g. UV offset): store a random Vector (`w`) on the instance/point domain and add it directly to a UV map's coordinates in the shader (or via a Mapping node — functionally identical to raw add/rotate/multiply math) before a Checker Texture, to get different texture offsets per instance without geometry-side variation.
8. **Cycles cannot displace instances differently** — EEVEE will show per-instance bump/displacement correctly (Material Properties → Settings → Displacement mode = Bump and Displacement), but Cycles treats instance geometry as linked for performance, so all instances show identical displacement regardless of per-instance attribute data. **Fix:** Realize Instances (and switch the shader's attribute domain from Instance to Geometry accordingly).
9. **EEVEE's 14-attribute-per-material limit:** EEVEE materials can read a maximum of **14 simultaneous named attributes**; a 15th/16th attribute in the same material causes visibly wrong (e.g. pink error-tinted) shading. Cycles has no such limit. Rare in practice, but worth knowing when debugging unexplained shading errors in complex attribute-driven materials.
10. **White Noise Texture as a fake "random value" function in the shader:** store just an ID/index attribute in Geometry Nodes (minimizing attribute count for the EEVEE-14 limit) and generate randomness in the shader instead — feed the ID into one channel of a **Combine XYZ** driving a **White Noise Texture**'s Vector input (other channels act as additional seed/variation controls), producing a 0–1 random value or color per unique ID, in both EEVEE and Cycles. Couple the 0–1 output with Mix nodes to remap into other ranges, replicating Random Value's behavior shader-side.
11. **Float-precision flickering artifact:** clean integer-looking indices from Geometry Nodes (0, 1, 2...) can arrive in the shader as slightly-off floats (e.g. `1.0001`), and White Noise Texture is sensitive enough to those tiny differences to produce per-pixel flicker/noise instead of a flat per-instance value. A **Round** node on the ID before it reaches White Noise Texture removes this inaccuracy — tested by the author with no issues found so far, though not exhaustively verified (float-precision bugs in Blender are described as "notorious").
12. **Random color recipes:** (a) Vector→RGB conversion from a Random Value vector node (covered in an earlier episode); (b) a Random Value (Float) node feeding a **Color Ramp** for more visual control over the gradient, adjustable interpolation type and stop distribution for even color-selection odds — reusable with either the geometry-node-side random value or the shader-side White Noise ID method from step 10.

### Nodes / Settings
- **Geometry Nodes:** Store Named Attribute (Color/Vector/Float on Instance or Point domain), Random Value (Float/Vector), Instance on Points, Realize Instances, Capture Attribute, index-comparison boolean masks, Translate Instances (implicit equivalence with post-instance Set Position)
- **Shader Editor:** Attribute node (domain dropdown: Instancer vs. Geometry — the key toggle), Mix (Color) node (Factor-driven A/B branching, used to fake Switch-node behavior pre-5.3), **Switch node** (native boolean branching in shader, Blender 5.3+), Combine XYZ, White Noise Texture (ID/seed channels), Round node (precision fix), Color Ramp, Bump/Displacement (Material Settings → Displacement mode)
- **Renderer differences:** EEVEE = max 14 simultaneous shader attributes per material, supports per-instance Cycles-incompatible displacement; Cycles = unlimited attributes, cannot displace instances differently (must realize instances)
- **UI gotcha:** Spreadsheet/Viewer node "Auto" domain mode shows Point domain for instances, not Instance domain — must manually switch to see per-instance attribute values correctly

### Difficulty
Intermediate — assumes the viewer has followed the earlier episodes in this series (instance rotation/scale randomization, Pick Instance, Object Info); the attribute-domain concepts (instance vs. point vs. geometry, and their interpolation across Instance on Points / Realize Instances) are the crux and take real practice to internalize, even though no single node used is advanced on its own.

### Blender Version
Not explicitly stated as a single version, but an on-screen caption notes the Shader Editor's **Switch node** — used as an alternative to the Mix-node dual-mask workaround in step 6 — is available starting **Blender 5.3**. Core techniques are otherwise version-general across recent Blender releases.

### Tags
geometry-nodes, instancing, materials, shaders, procedural, attributes, eevee, cycles, motion-graphics, intermediate

---

## Related Tutorials
- [[Tut] How Pick Instance is used for Instance Variations - P10 Geometry Nodes Beginners](tut-how-pick-instance-is-used-for-instance-variations---p10-geometry-nodes-begin.md) — direct predecessor in the same series (explicitly referenced in this episode's closing summary); covers faking *geometry* variation between instances via Pick Instance, complementing this episode's *color/shader* variation techniques.
