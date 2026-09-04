---
title: [Tut] How to use Vertex Group and Named Attribute? - P3 Geometry Nodes Beginners 5.0+
source: YouTube
url: https://www.youtube.com/watch?v=wgAF2lUSu70
author: Bradley Animation
ingested: 2026-09-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/tut-how-to-use-vertex-group-and-named-attribute---p3-geometry-nodes-beginners-50/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: []
---

# [Tut] How to use Vertex Group and Named Attribute? - P3 Geometry Nodes Beginners 5.0+

**Source:** [YouTube](https://www.youtube.com/watch?v=wgAF2lUSu70)
**Author:** Bradley Animation
**Duration:** 18m38s | 7 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py tut-how-to-use-vertex-group-and-named-attribute---p3-geometry-nodes-beginners-50 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro of Named Attribute [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, this is Bradley. Welcome to the third episode of this beginner series on geometry nodes.
[0:07] Here we start with a very basic setup for today's demonstration.
[0:11] You can take this as a small test and try to recreate the entire file.
[0:17] I explained the workspace layout and how to create sockets on the Group Input node in the first episode.
[0:25] I also explained how to create reroutes and labeling in the second episode.
[0:31] This file before and after the tutorial is also available to download for free,
[0:37] in case you want to follow along or check the diagram created at the end of the tutorial.
[0:43] In the last episode, we discussed important shortcuts.
[0:47] If you are not yet familiar with all of them,
[0:50] you can always check the screencast keys in the bottom left corner, showing my clicks and shortcuts.
[0:58] Today's topic is attributes and fields.
[1:01] In geometry nodes, these refer to properties of our geometry.
[1:06] For example, vertex group, weight painting, UV maps, and so on.
[1:12] Often, people use the terms attributes in the field interchangeably to refer to these kinds of properties in general.
[1:21] But of course, they can be broken down into something more specific.
[1:26] There are two kinds of attributes.
[1:28] One is called a named attribute.
[1:31] The other is called anonymous attribute.
[1:34] If you search named attribute, you will find as these are two nodes with relevant names.
[1:40] We have named attribute and the store named attribute.
[1:46] You can usually see named attributes at the top of the spreadsheet, where we have position, sharp face, and UV map.
[1:57] If you click the text box of the store named attribute node, you will find the node results.
[2:04] But as soon as you insert it into the link, you will see the relevant attributes we discussed earlier.
[2:12] Alternatively, the named attribute node doesn't require insertion to access these attributes,
[2:20] because it reads directly from the group inputs.
[2:23] If you remove the geometry from our group inputs, you will find no results.
[2:29] The reasons behind this phenomenon will be elaborated on in the next episode.


### How to use Vertex Group in GN [2:30]
**Transcript (timestamped):**
[2:35] As mentioned, vertex groups are also named attributes, because you are literally giving a name to a vertex group,
[2:42] and you can rename it however you want.
[2:45] Here, I will select some vertices on my subdivided cube to assign the group.
[2:51] Then you can find this group in the drop-down list on both named attribute nodes.
[2:57] You can use Vue to confirm the selection we did.
[3:01] Named attribute node is one way to use vertex group in geometry nodes.
[3:07] Alternatively, if you have values exposed on the group inputs reviewed in the modifier,
[3:14] you can use the plus icon in the modifier panel, which turns the value into a text box
[3:22] and allows you to use it in the same way as the named attribute node.
[3:27] Note that right now my viewer is showing black values only,
[3:33] and the search has no results found for some reason,
[3:37] but if you type AAA manually and hit enter, the viewer will review the correct vertex group selection.


### Implicit Attribute in Sockets [3:40]
**Transcript (timestamped):**
[3:46] On the other hand, since many attributes are widely used,
[3:51] the developers created dedicated nodes for them.
[3:55] For example, we have position, normal, index, ID, and curve tangent.
[4:04] Some of them may not strictly be named attributes,
[4:08] since they may not be directly available through the named attribute nodes,
[4:13] but these are very specific names for properties used somewhere in the system.
[4:19] For example, a mesh must contain normals to determine the surface angle for light reflection.
[4:27] In addition, there is one small but important concept related to the attributes
[4:33] that you may notice when using certain nodes.
[4:37] In this example, we have a set position node.
[4:41] The set position node literally sets the position of each point in our cube.
[4:48] Right now, it's not influencing the final result whether you mute it or not.
[4:54] If you check the tooltip of the position socket,
[4:58] you will see that its input is a field based on the position attribute.
[5:05] This means the node is already using the position attribute internally by default.
[5:12] If I output the position node into the socket, the result in the viewport does not change.
[5:20] However, if I plug a different attribute like normal into the socket,
[5:25] you will see it becomes immediately different.
[5:29] If I instead use a combined xyz node, the cube completely disappears.
[5:35] Because all points collapse into a single point at this location of 000,
[5:42] as you will see from the spreadsheet, all positions are outputting zeros.
[5:48] We can also visualize this by using a mesh to points node.
[5:52] You will see all points setting at the word origin.
[5:56] If I raise the z value in the combined xyz node,
[6:00] the points move upwards, making it more obvious.
[6:04] So I hope this proves that the socket was already filled with the position attribute,
[6:11] even though we did not explicitly connect a position node.
[6:16] We usually call this an implicit attribute,
[6:19] meaning the socket is automatically prefilled with an attribute by the system.
[6:26] Before Belander 5.0, this socket had a slightly different visual indicator.
[6:33] You could see a small hole in the diamond socket in the offset input,
[6:39] whereas the position socket did not have this hole because an attribute was already filling it.
[6:47] A fully filled diamond indicated that the attribute was implicit.
[6:52] However, due to technical and design changes in Belander 5.0, this visual distinction has been removed.
[7:02] Now most filled sockets appear as a filled diamond,
[7:07] so we can no longer rely on socket appearance alone.
[7:11] We have to rely on node names, experience, and tooltips
[7:16] to determine whether a socket is implicitly using an attribute or not.
[7:22] In fact, you may notice that mesh to points nodes also uses the position attribute internally.
[7:29] Other nodes, such as the random value node,
[7:33] have IDs that obviously corresponds to the ID node.
[7:38] However, socket names can sometimes be misleading.
[7:43] For example, the noise texture node has a vector input,
[7:47] but internally it also uses the position attribute by default, as you see.
[7:53] So, occasionally, when you encounter sockets that do not expose their values by default,
[8:00] you may want to check the tooltip to understand what's really happening under the hood.
[8:06] As these dedicated nodes and implicit attributes are commonly used,


### Downsides of using Named Attributes [8:10]
**Transcript (timestamped):**
[8:12] we don't always need to use store name and attribute and the name attribute.
[8:16] Working with them can also be a bit convoluted,
[8:20] because their workflow mostly appears in pairs.
[8:24] In this example, using the nodes we are already familiar with,
[8:28] I start with a UB-Sepir node,
[8:32] store a random value attribute using the random value nodes,
[8:37] and then use the name attribute node to pull this value,
[8:41] and output it to the offset of set position.
[8:46] As a result, you will find each point has been offset or displaced randomly from our original sphere.
[8:56] It works.
[8:58] But imagine you have a very large node tree with complex operations,
[9:03] and every time you have to duplicate many of these pairs just to use some parameters.
[9:09] It sounds very inefficient.
[9:12] I even have a setup that mimics this situation,
[9:15] with many store named attributes and named attribute nodes in a single node tree.
[9:21] There are lots of names,
[9:23] and it's not immediately obvious the relationship between the storage and usage.
[9:28] We have AAA here, FFF here, CCC there.
[9:34] Reading the node tree becomes very difficult.
[9:38] Another issue with this workflow is that these named attributes stay with the geometry.
[9:44] If you check the spreadsheet, you can see the data expands significantly.
[9:50] Once you subdivide the geometry, there will be even more data.
[9:56] There will be even more data in the rows.
[9:59] They actively take up disk space because the file has to store all these values,
[10:06] writing them down.
[10:08] Your file can grow from kilobytes to gigabytes because of them,
[10:13] and they do not function like a cache because you have to store them,
[10:18] and process them during subdivision or other operations.
[10:22] At some point, you may want to remove them.
[10:26] If you are familiar with the node names, you may know there is a node called the removed named attribute.
[10:32] Of course, we are not going to do that here because it will only add more chaos to this already complex setup.
[10:39] Going back to our original example, is there a better workflow that avoids all these duplications?


### a preferred Field Workflow [10:40]
**Transcript (timestamped):**
[10:47] You may already recall the examples when I showed the implicit attributes,
[10:53] where I directly connect a position node to the position socket.
[10:58] Why don't we do the same here?
[11:01] Instead of using a pair of named attribute nodes,
[11:04] we can directly connect the random value node to the offset socket.
[11:09] You will find that the result is comparable.
[11:12] So it works even if we do not have the named attribute pair.
[11:18] In this process, there is no named attribute involved.
[11:23] We call these anonymous attributes because we don't have a name, and they are used right away.
[11:30] Personally, I often use attributes to refer to the named attributes,
[11:35] and the field to refer to these anonymous attributes passed around in the node tree.
[11:41] In summary, named attributes are like weights on your body.
[11:46] They take up a memory and file size and can slow things down.
[11:51] Anonymous attributes are like tools in your hands.
[11:56] You use them when you need it, then put them down when you are finished.
[12:01] Once we finish using the random value in set position nodes, the system discards it,
[12:07] and you won't find any trace of it because there is no name attached.
[12:13] This means it won't affect any geometry modification process later on.
[12:19] Therefore, fields are more commonly used in geometry nodes.
[12:24] They are simple, clean, and often more hardware-friendly.
[12:29] However, there are cases where named attributes is the better, or even the only option.


### Pass Attribute from GN to Shader [12:30]
**Transcript (timestamped):**
[12:37] For example, as mentioned earlier, vertex groups are already named attributes from the beginning.
[12:44] If you set up a vertex group and want to use it, named attributes are the only way to do it,
[12:51] you can use the rule nodes over the modifier panel.
[12:55] Another common case is when you want to pass information to shaders.
[12:59] In that situation, you must store a named attribute for the render engine to read.
[13:05] Here I start with a grid, store a named attribute for the color of a noise texture,
[13:11] and assign material.
[13:14] An alternative method is to output the values to the group outputs,
[13:19] where you can assign a name in the modifier panel under the output attributes.
[13:24] However, store-named attributes workflow is generally preferred.
[13:29] In the Shader Editor for material, I can use the Shader version of the attribute node.
[13:37] This one is quite old and lacks many advanced features nowadays,
[13:43] so you have to manually type the name you stored.
[13:47] And I will pass color to color.
[13:50] Now we have the noise texture color passing from geometry nodes to the shader.
[13:57] Please be aware that ideally you can name these color attributes however you want,
[14:02] as long as they are matching and recognizable to you.
[14:06] However, due to certain limitations, color is not working in cycle.
[14:12] I won't go into detail here, but it's something to keep in mind that certain names are not available in cycle,
[14:20] especially this color, because I think it will be common.
[14:25] Personally, instead of full descriptive names, I usually use single letters like C for color,
[14:33] especially without search, you don't want to spend too much time typing names.
[14:39] Although this is just an example, you may still want to ask why do we do this instead of using the noise texture node directly in Shader?
[14:48] It's important to note that shaders are always calculated after geometry nodes.
[14:55] You can pass information from geometry nodes to shader, but not the other way around.
[15:00] So if you are using a noise texture to drive animations or instancing,
[15:05] then you want to use the same result in the render.
[15:08] You may need to pass that information to the shader.
[15:11] And in motion graphics, obviously this is very common.
[15:16] There are more situations where storm attributes is preferred or required.
[15:22] We will discuss them accordingly when the situation counts.
[15:26] In real life, it's used a lot.
[15:29] Nevertheless, I want to emphasize that you are discouraged from using it for simple tasks given all downsides it can have,


### Ctrl+F to Search Attribute & Group Input Sockets [15:40]
**Transcript (timestamped):**
[15:40] unless you have your personal preferences.
[15:43] At the end, I want to discuss a shortcut that may help in extreme cases where many pairs become confusing.
[15:53] If you want to find out where an attribute is stored or used, you can press Ctrl F.
[15:59] Unlike the regular Shader A search, Ctrl F search was originally used to search nodes in a large node tree.
[16:08] For example, you can search for a store name attribute, and you will see many results.
[16:14] Clicking an item will highlight and select it.
[16:17] If it's not in your view, it will lead you to it.
[16:22] With recent updates in Blender 5.0, Ctrl F also supports searching textboxes.
[16:29] So I can search AAA to find where it's stored and used.
[16:35] I can search GGG and find it's stored, but not really used anywhere.
[16:42] Furthermore, it can help you search group input sockets,
[16:47] especially if you have many group nodes scattered in the node tree for control and organization.
[16:55] Here, if I try to search this boolean socket, it seems not working,
[17:01] because none of these inputs are actually used by the node tree.
[17:05] So the search disregards them.
[17:08] If I connect it to somewhere and then search it again, you will be able to find it.
[17:16] If I add another linkage, then the search will review both of them.
[17:21] So you will know clearly where the input is used and how many time it is used.
[17:28] So that's it for now about named attributes and anonymous attributes.
[17:34] Keep in mind that the existing items you find in the named attributes, along with the dedicated nodes,
[17:42] may still not cover the full list of geometry properties in Blender.
[17:48] Nevertheless, for beginners, knowing these few attributes should be enough for now.
[17:55] In the next episodes, we will dive deeper into fields and talk about capture attribute nodes.
[18:03] Meanwhile, I hope you are still following the homework of remembering node names,
[18:09] just like memorizing vocabulary while learning a new language.
[18:14] Again, you only need to skim through the names.



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
