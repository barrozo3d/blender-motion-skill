---
title: ALL 300+ Geometry Nodes in Blender
source: YouTube
url: https://youtu.be/Y0zAZnbBcQU
author: RADIUM
ingested: 2026-05-13
blender_version: unknown
tags: []
---

# ALL 300+ Geometry Nodes in Blender

**Source:** [YouTube](https://youtu.be/Y0zAZnbBcQU)
**Author:** RADIUM
**Ingested:** 2026-05-13

---

## Description

The project started about a year ago as simple notes to help me learn geometry nodes, but it quickly snowballed into something much bigger. I’ve now created two ebooks totaling over 240 pages:

Every Geo Node on Your Finger Tips:
https://superhivemarket.com/products/egne?ref=1589


Escape Tutorial Hell Today:
https://superhivemarket.com/products/nodel?ref=1589

*My instagram:*
(https://www.instagram.com/radium.235/)


Staple addons in my workflow:
*Check out CAM-FX:*
https://blendermarket.com/pr

---

## Raw Content (for analysis)

Kind: captions Language: en There's a wide wide world of geometry nodes. &gt;&gt; Shut the [&nbsp;__&nbsp;] up. You can only know what you can make if you know what tools you have in your workshop and what they're capable of. Similarly, you can only know what you can do with geometry nodes if you know what each node does. Unfortunately, there are about 275 nodes in Blender 4.3. Not so unfortunately. This video is about an hour long. This is The first nodes we are going to look at are called the input and output nodes. The first section in this is the constant nodes. Constant nodes are input nodes that provide fixed values such as numbers, colors, strings or other data types to be used across a node tree. These are small tiny nodes. So I'm just going to quickly roll over them. The first node is the boolean node. This node gives a single boolean value either false or true. Next node in the list is the color node. This node basically allows you to choose a color. Moving on, we got the image node. This node lets you load an image file into the geometry node editor. Next up, we got the integer node. Like the name suggests, this node provides an integer value. Next is the material input node. This node gives you access to materials in the geometry node editor. Next is the rotation input node. This node allows you to control rotations. The string node lets you output a string value. The vector node basically creates a vector. The value node outputs a single numerical value. Coming up next, we got the collection node. This node allows you to input a collection into multiple sockets throughout the node tree. Last but not the least, object node. This allows you to input a singular object throughout the node. Before we move ahead, we should tackle some important concepts that help us better understand some of these nodes. The first of this concept is the concept of fields. While there's a very technical definition of what a field is in Blender, in a practical sense, a field just means more than one value. So a node when connected to a field basically means it performs its operation on more than one value at once. How do you spot a field? If the node socket is a circle, it outputs a single value. If the node socket is a diamond, it outputs a field. If the node socket is a diamond with a circle inside, the node can output a field but is currently outputting a single value. Some nodes that output fields are the position node, index node, ID node, or the normal node. But there is a little more caveat to fields because when I said a field is more than just one value, I lied. Now hang on with me for a second. A field is more than one value. But this value is not independent. It corresponds to a particular geometry element. What I mean by geometry elements is vertices, faces, edges, etc. So basically a field are a set of values that correspond to a specific geometry element. What are the values? When I say fields give more than one value, those values are called attributes. Attributes are basically data or information that correspond to a domain. For example, the position attribute in the point domain stores the position information which is the data of all the points which is the domain in a mesh. This makes geometry nodes more about data manipulation than anything else. How to view attributes? Attributes can be viewed using the spreadsheet editor. This window shows you the attributes of different domains. One important concept we need to understand is that the same kind of attribute can exist in multiple domains. For example, the position attribute we discussed earlier not only exists for the point domain, but also for the edge, face, spline, and whatever domain you can think of. How does a node determine which attribute of which domain should the node operate on? Well, that's where the tricky part comes in. This intuition a node has on which domain it should operate on is called field context. What is field context? Most nodes have some conditions associated with them. Like for example, take the set position node. This node's condition is that it operates on point domain by default. When you connect an input node like the position node to the set position node, since the position node is connected to the node which defaults to operating in the point domain, it is giving out position values of the point domain. This is the basis of field context. Input nodes like the position nodes and more nodes we'll discuss down the road bend to the context/cond conditions of the node ahead of it. One common misconception is that the node outputs the same data all the time. This is not true. For example, take this node setup. In the top part of the node tree, the position node outputs the position data in the point domain. Whereas in the bottom part of the node tree, the position node outputs the position data in the phase domain. Notice how the same position node outputs different data depending on the context of the nodes it is plugged into. That is the working of field context. Before we go ahead, I just want to take a few moments to talk about this project. This basically started out as nodes for myself to understand geometry nodes. And well, it has turned into this full-blown project where I'm explaining geometry nodes. And what I have discovered is that geometry nodes is insanely insanely [&nbsp;__&nbsp;] detailed. The more I study it, the more I play with it, the more nuances I find with it. And hence, I cannot I definitely cannot cover everything in this video. And that's why I made all my nodes that I use to study geometry nodes into an ebook. And also u I created another ebook called Nodal. This book contains a recipe style step-by-step explanation of 20 geometry node exercises that I went through that like changed and built my understanding of geometry nodes the most. This book will actually take you from 0 hours to 200 hours of experience in geometry nodes within the course of that book. And if you want t

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/all-300-geometry-nodes-in-blender.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
[To be extracted]

### Key Steps
[To be extracted]

### Blender Nodes / Settings
[To be extracted]

### Difficulty
[Beginner / Intermediate / Advanced]

### Tags
[To be added]
