---
title: I'll teach you Geometry Nodes
source: YouTube
url: https://youtu.be/JU70u6cJZqI
author: Default Cube
ingested: 2026-05-13
blender_version: "4.5"
tags: [geometry-nodes, procedural, blender-4x, beginner, intermediate]
---

# I'll teach you Geometry Nodes

**Source:** [YouTube](https://youtu.be/JU70u6cJZqI)
**Author:** Default Cube
**Ingested:** 2026-05-13

---

## Description

🧮 ➠ https://superhivemarket.com/products/geometrynodes

---

## Raw Content (for analysis)

Kind: captions Language: en How do you learn geometry nodes? First of all, by playing with them and second of all, by watching tutorials. I made a 5 and 1/2 hour course thing. The first hour or so is going to be free to you. So, let's begin. Hello everybody and welcome to Introduction to Geometry Nodes, the course that takes you from not knowing geometry nodes to knowing it very well. I'm not going to assume you know anything from the get- go, which is probably what you want. And I'm not a fan of wasting your time. So, quick description. My name is Tom. You might know me as CG Matter or Default Cube. These are tutorial channels where I've been teaching geometry nodes for years. All the clips you're about to see, I worked at Mayor Studios doing just geometry nodes. Some effects, some snow, some particle stuff, and that is the extent of it. And every single bit of freelance I've ever gone has involved [music] geometry nodes. It is the most powerful tool in Blender, and it's only getting more powerful. So, it is essential that you know how to use it. Literally the only two prerequisites I would like you to have before starting this course is one I'm going to be using Blender 4.5. As you can see in the corner here, this is the latest version as of recording and geometry notes tends to have a kind of a history or a trend of adding features and pretty much never taking any away. So I expect this course to be valid and upto-date in a sense for a long time. If you use a older version of Blender like 4.4 or 4.3, there's a slight chance you're missing a node or a feature that I'm going to talk about. So use 4.5 if you're watching now. Use 4 whatever or 5 point whatever if you're watching in the future. It's still going to be applicable. The only other prerequisite I would like you to have is ideally you watch this course on a desktop computer. This doesn't just let you follow along, but what I really mean is it has a big screen. I want you to watch this on a big screen, not a phone, because it makes it easier to see what I'm doing cuz nodes tend to be kind of small unless we really zoom in, which sometimes will do. And I can add more and more nodes. And the more that I add, in a sense, the more I have to zoom out. So, I would highly recommend watching on a big screen. You can throw it on your living room or just follow along on your [music] computer. I guess let's just get into it with chapter 1 coming up. Okay, we've officially begun with chapter 1. This is about the very very basics. How do you even interact with geometry nodes? What are they? Why are they even called geometry nodes? And by the end of this chapter, you're not only going to know how to navigate around, which is great, but we're also going to make a project where we make a three-dimensional fractal of an arbitrary resolution. This thing you're seeing is a variant or it's called the menure sponge. And this is the kind of thing that's perfect for geometry nodes cuz it has like so much detail and it would be a pain to model by hand. So let's begin by setting up geo nodes itself. So I'm in Blender here obviously and the first thing you need to know is how do I get how do I navigate to geometry nodes? At the very top where you have all your workspaces by default you're going to have something called geometry nodes which when we click it it has all the editors that we need. If you do not have this, you can click this plus icon, which lets you add a workspace. And under general, you have geometry nodes, which I don't need a second one, so I'm just going to delete it. So, from wherever you are, no matter how lost in the woods you are, you can just go to geometry nodes. This is composed of primarily three workspaces that we really, really care about. The first one is obviously the 3D viewport. This is helpful to see what it is we're making. The second one is the one we're going to be interacting with the most and is the newest to you. This is the node editor where we do all of our geometry nodes. We basically draw out our code or blueprints or whatever you want to call it inside of here which is represented again in the 3D viewport. So you can think of this as input what we're making output in the viewer what we're seeing. And then right here we have another new editor. It's called the spreadsheet editor. You could think of this as a companion or intermediary editor. Really, it's more so of a viewer where we can see all kinds of data about what it is we're making. And this is useful cuz when we're juggling around data, adding attributes, it can be confusing and it's nice to see what's going on here. So, for example, here I have the position of, you can see it's eight vertices. Coincidentally, well, not coincidentally, the cube has eight vertices. And when I move one around, you're going to see this updates. If I scale them all up, they all update. So this is a live viewer of what is going on essentially. Alternatively, you can also make your own workspace. If I go to the editor types, you can see we have the geometry nodes editor. We also have the spreadsheet and obviously we have the viewport. So set this up however you want. I could do a geo nodes editor, which I can throw on the bottom and make this the 3D viewport. And I can also like for example replace the outliner with this spreadsheet. To start off with, I'm going to use the basic layout, but once we get a bit more comfortable and involved and whatever, I do have this custom workspace that is designed to make things more legible. We have our big node editor and our big viewport and it might just be easier for you to see what's going on. Note that geometry nodes, whatever it is we do, so I'm just going to throw some random nodes on, you're going to see it follows a left to right workflow. So, for example, I start with this node. I move to this one. I move to this one. When I move to this one, this progresses from left to right, which is unlike some other software that goes top to bo

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/ill-teach-you-geometry-nodes.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Comprehensive Geometry Nodes course (5.5 hours) in Blender 4.5, starting from absolute basics of the GN workspace, node editor, and Spreadsheet editor, and building up through a 3D fractal Menger Sponge project to demonstrate procedural power.

### Key Steps
1. Navigate to the Geometry Nodes workspace (top tab bar); understand the three editors: 3D Viewport (see output), Node Editor (draw code/blueprints left-to-right), Spreadsheet Editor (inspect live data like vertex positions).
2. Alternative workspace setup: open Geometry Node editor manually via editor type dropdown; customize layout to have a large node editor + large viewport.
3. Learn left-to-right node flow: data enters from the left (Group Input), gets processed through a chain of nodes, and exits to the right (Group Output) affecting the 3D object.
4. Understand the Spreadsheet as a live viewer: move vertices and watch positions update in real time; inspect attributes per element.
5. First project: build a Menger Sponge fractal — demonstrates procedural iteration, instancing, and scaling that would be impossible to model by hand.
6. Learn to add nodes: Shift+A in the Node Editor; search for node names; connect sockets by drag-and-drop.
7. Use Blender 4.5 specifically — prerequisite for full node access; course stays valid for 4.x and 5.x versions as GN only gains features.
8. Follow along on a large screen/desktop for best visibility of small node labels.

### Blender Nodes / Settings
- Group Input / Group Output nodes
- Node Editor (left-to-right workflow)
- Spreadsheet Editor (live vertex/attribute data)
- Shift+A (add node menu)
- Geometry Nodes workspace (top tab)
- Custom workspace: editor type dropdown
- Menger Sponge fractal (first project)

### Difficulty
Beginner

### Blender Version
4.5

### Tags
#geometry-nodes #procedural #blender-4x #beginner #intermediate
