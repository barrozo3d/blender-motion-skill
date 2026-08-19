---
title: Blender Tutorial: Connect The Dots with Geometry Nodes, The "Plexus" Effect
source: YouTube
url: https://youtu.be/tj6ZZYO5qPY
author: Entagma
ingested: 2026-05-13
blender_version: "3.4"
tags: [geometry-nodes, procedural, particles, animation, motion-design, abstract, blender-3x, advanced]
---

# Blender Tutorial: Connect The Dots with Geometry Nodes, The "Plexus" Effect

**Source:** [YouTube](https://youtu.be/tj6ZZYO5qPY)
**Author:** Entagma
**Ingested:** 2026-05-13

---

## Description

Support us on Patreon: https://www.patreon.com/entagma

This time we'll create the "plexus" effect with Geometry Nodes inside of Blender. Manuel shows you how to abuse geometry to fake a loop, that tests all connections between the points of an incoming point cloud and compares their lengths. Then, only the ones are drawn, that are shorter than a certain threshold, creating an intricate geometric pattern. 

Download Scene File: https://www.entagma.com/downloads/GN_ConnectTheDots01.zip

00:00 Int

---

## Raw Content (for analysis)

Kind: captions Language: en hello this is Manuel with intagma and I'm here with the new blender tutorial today I want to connect the dots I want to create an effect that is known as the plexus effect I think because of an After Effects plugin that is called plexus that creates this effect inside of After Effects I want to take a point cloud and then I want to examine the distances between the points and if these distances fall below the threshold I want to connect the dots with a line and by the way this is the very first effect that I created as an Houdini tutorial on this channel I think four years ago and today it's time to create the same thing inside of blender using geometry notes so let's start by selecting everything and get rid of everything instead I want to create a mesh monkey let's subdivide this monkey like so and then apply the modifier and that will be the volume that I want to use to distribute some points in to make this invisible now let's create a new plane that's just a placeholder object and let's call it GN for geometry nodes and then connect the dots like so let's create a geometry nodes viewport and let's get rid of the side panel and create a new tree and call it TN underscore connect the dots like so let's cut this connection and let's bring in our Suzanne whenever you bring in another object you have to decide if you want to use original or relative I want to use relative because I want to use the global coordinates of the Susan points inside of the coordinate space of my object here now let's connect this and this creates our original geometry now in this coordinate space now I want to distribute some points but not on the surface but inside of a volume and to do this I think you have to use the blender 3.4 version that I'm using here currently so if you don't find some of the nodes please update to the very latest beta version so I want to first turn our Suzanne into a volume using the mesh to volume node this gives a volumetric representation of Suzanne and now with this volume in place I can use distribute points in volume and that creates some points inside of the volume I can up the density and that creates more and more points filling the volume with points to develop the effect let's go down to 10 with the density or even lower say five because as long as we have only few points it's easier to understand what we will be doing now this is our Point cloud and now comes the algorithm to make this visually clear I want to create a reroute here and now let's invoke the end panel for a second select the reroute and call it in there is a point where the point Cloud enters my setup great let's cut this connection and let's put the re-routine before we start let's think about what we are about to create so if I have some points that are scattered in space I want to start with the very first point let me create a new layer with a different color so this point here should be the first point and that has an index of zero and and now I want to examine all the distances to all the other points so I can calculate the distance to this point and the distance to this point and the distance to this point and so on and so forth or the distances and as soon as I have the distance as I can decide if the distance is short enough to be drawn as a line now once I have this I have to do the same thing for the next Point Let's create different colors so this say here is one now I have to do the same thing and have to examine this connection and this connection and this connection and so on this connection and then the same thing for the next Point dark blue say that is 0.2 and we want to examine the connection to this point and to this point and to this point and to this point and to this point and so on and so forth so as you can see to find all the connections between the points we first have to run over all the points so we want to examine point zero and then 0.1 and then 0.2 and then 0.3 and so on and 4.0 we want to look at all the other points so 4.0 we want to look at the connection between 0 and 1 and 0 and 2 and 0 and 3 and so on and 4.1 we want to look at the connection between 1 and 0 1 and 1 1 and 2 1 and 3 and so on and for two the same and for three the same so we have a lot of examination to do and if you look at this closely we want to look at all the points for every Point how can we do this without Loops inside of geometry nodes well actually we do have loops inside of geometry nodes but these Loops are not directly usable instead we can Loop over geometry only so we have to create geometry to create this Loop and unfortunately we cannot do nested Loops that is what I intended to do I want first to Loop over all these points and then for every point I want to Loop over all the points that is not possible either so what could we do well we can come up with a serialization we could think about how to turn this into a linear Loop and if you think about it we could do the following we could look at point zero and then we could pair it with point zero and then we can look at point zero again and examine the connection to point one and then 0 again connection to two and zero again connection to three and so on and so forth let's assume that we only have four point at the moment now after we did this We examined all the connections of point zero now it's time to check the connections of point one so now we could look at point one ones to examine the connection to point zero then at point one again to examine the connection with point one and then again connection to two and again connection to three and after that we can start with two so let's look at point two once to examine connection to point zero and then with one and you get the idea so if we do this we look at every Point not once but as often as necessary to go over all the points and interesting pattern is emerging here if you look at this this is an indices of the currently processed point and this is this i

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/blender-tutorial-connect-the-dots-with-geometry-nodes-the-pl.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Recreating the "Plexus" effect in Geometry Nodes by distributing a point cloud inside a mesh volume, then using a serialized loop (abusing geometry to fake nested loops) to test all pairwise point distances and draw connecting lines only for pairs below a threshold distance.

### Key Steps
1. Add a Suzanne mesh, subdivide it, and apply the subdivision modifier as the point cloud source volume.
2. Create a new plane object named "GN" as the geometry nodes host; create a new node tree named "TN_connect_the_dots".
3. Bring in the Suzanne object node (use Relative coordinates) and convert it to a volume using the Mesh to Volume node.
4. Use Distribute Points in Volume node on the volume; start with low density (e.g., 5) to prototype.
5. Design the serialized loop: to test all N×N point pairs without nested loops, create a geometry with N copies of each point paired with every other point index — representing all combinations as a linear sequence.
6. For each pair, compute the vector from point A to point B and measure its length using Vector Math (Length).
7. Compare the distance against a threshold; use a Compare node (less than) to create a boolean selection mask.
8. Use the selected pairs to create edges or lines between points using the Edges of Corner or Mesh Line approaches.
9. Delete pairs that exceed the threshold distance, leaving only the connected short-distance lines.
10. Adjust the density (Distribute Points in Volume) and threshold distance to control the visual density of the plexus network.

### Blender Nodes / Settings
- Object node (relative coordinate space)
- Mesh to Volume node
- Distribute Points in Volume node (Density: 5–10)
- Vector Math nodes: Subtract, Length
- Compare node (Less Than threshold)
- Reroute nodes (for labeling/organization)
- Index node (point indices for pairing logic)
- Delete Geometry node (filter by threshold)
- Blender 3.4 (required for Distribute Points in Volume)

### Difficulty
Advanced

### Blender Version
3.4

### Tags
#geometry-nodes #procedural #particles #animation #motion-design #abstract #blender-3x #advanced

---

## Related Tutorials
- [Create Plexus FX In Blender ( Geometry Node )](create-plexus-fx-in-blender-geometry-node.md) — directly relevant: a different route to the same "Plexus" glowing line-network look, via displaced-terrain-to-edge-network + Emission/Glare instead of this tutorial's Distribute Points in Volume + pairwise-distance serialized loop.
