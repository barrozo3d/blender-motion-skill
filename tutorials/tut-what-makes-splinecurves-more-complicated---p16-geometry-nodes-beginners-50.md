---
title: [Tut] What makes Spline/Curves more complicated - P16 Geometry Nodes Beginners 5.0+
source: YouTube
url: https://www.youtube.com/watch?v=YLJjEYd47JQ
author: Bradley Animation
ingested: 2026-09-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/tut-what-makes-splinecurves-more-complicated---p16-geometry-nodes-beginners-50/
frame_count: 0
frame_status: pending-selection
uncertainty_frames: []
---

# [Tut] What makes Spline/Curves more complicated - P16 Geometry Nodes Beginners 5.0+

**Source:** [YouTube](https://www.youtube.com/watch?v=YLJjEYd47JQ)
**Author:** Bradley Animation
**Duration:** 24m5s | 18 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py tut-what-makes-splinecurves-more-complicated---p16-geometry-nodes-beginners-50 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### A big picture of today's episode [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, this is Bradley, welcome to the 16th episode of the Beginner Series on
[0:06] Geometry Nodes. I hope you've watched the previous episodes because they will make today's
[0:10] topic much easier to follow. In all previous episodes, we've discussed a lot about meshes
[0:17] and instances, and we also touched a little bit on points. Starting from this episode,
[0:23] we are going to briefly talk about Curve geometry. Just recently, there was a Twitter post on
[0:29] about its role in motion graphics. Besides the needing patterns you will commonly see
[0:35] in motion graphics, you may also need to use curves in many places that may not be directly
[0:41] obvious at first. It's a very powerful and simple technique that we will use to conclude
[0:47] this series. In today's episode, we will talk about different types of curves. There are
[0:53] many different categorizations and the nomenclatures that we need to know about. One of the first
[0:59] issues I have to clarify is the inconsistency of naming in the current Blender development.
[1:06] As you may know, Blender is developing fast, which also means Blender is constantly rewriting
[1:13] its old functions. Therefore, in fact, we are dealing with distinct old and new Curve systems.


### What are Old Curve Object [1:20]
**Transcript (timestamped):**
[1:21] In the viewport where nothing is selected, if you press Shift-A to look at the Curve
[1:27] section, you will see there are white sections and gray sections. The top white sections are
[1:35] for older curves. Whether I add a bezier circle or a path, you see they have the same object
[1:42] icon. And in the property panel, they have a large Curve data block with many options.


### How to add New Empty Hair Object [1:50]
**Transcript (timestamped):**
[1:51] The bottom gray sections are new curves with a different icon. They are gray because you
[1:56] cannot directly add them in Blender 5.2. As indicated by the warning, to add them, we
[2:03] first need to create any mesh. Like a plane, keep it selected and then we can add this
[2:11] new Curve object type. This new Curve object type will be the child of your selected mesh.
[2:19] You can see it has a different icon compared to the previous circle and the path. Also,
[2:25] it doesn't have the long panel we had previously, but it comes with its own geometry nodes modified.
[2:34] Before 5.2, it was simple, like a deformed curve on a surface. Now, in 5.2, it seems
[2:41] more complicated and frightening because it includes the latest experimental hair physics.
[2:48] You don't need to worry about that. Just know that the default animation mode is exactly
[2:53] the same as the one in the past. Only if you try experimental physics, it will have some
[3:00] physics features. Basically, the initial idea of this new Curve type is to replace the old


### Why we need to have New Hair Object? [3:05]
**Transcript (timestamped):**
[3:07] hair particle system. Yes, besides the Curve objects, we have a separate hair particle
[3:14] or particle hair system that you can see on this object. Our new hair system is still
[3:20] under development, so this old hair system is still kept for the moment. It's not accessible
[3:27] through geometry nodes, so let's forget about it. Here, it must grow out from a mesh surface.
[3:34] We can go to the sculptor mode and the Wessing T panel. You can see some basic brush of hair,
[3:41] including this head brush. We can use it to grow our hair curves and you can also increase
[3:47] the count to grow more hair. These hairs are grown from the surface. I can move and rotate
[3:54] our plane and the Curve will move with it. You may think it's because of the parent's
[4:00] relationship, but even if I clear the parent, you will find that the hair will still stick
[4:07] to the surface because the critical settings are in the green data panel as shown. The
[4:13] parenting relationship is more for better indication of their relationship. It's the
[4:20] meaning of these animation modes that hair will stay on the surface regardless of its
[4:26] movement. You can also try experimental physics and by playing the animation on the timeline,
[4:33] you can see it will start to have gravity influencing these hair strands. You can also
[4:38] move the plane to trigger these hair movements. This system is still under development and
[4:44] is missing lots of features like self collisions. So I won't elaborate yet here. Now, we know


### Difference in Rendering of two Curve Objects [4:50]
**Transcript (timestamped):**
[4:52] about the two curve objects. The major practical difference between the two curve types is
[4:58] their rendering. Both bezier circle and a path curve are showing as a kind of black lines
[5:05] in the viewport now. If I turn off the viewport overlay, you will find that they disappear
[5:11] from the viewport. This means these curves cannot be rendered directly. They have to
[5:18] go through some geometry process like bevel. As you see in the panel, I don't know why
[5:24] this is called bevel, but anyway. On the other hand, disabling the overlay doesn't remove
[5:31] my hair strands from the viewport because they are natively visible for rendering and
[5:36] they are made efficiently so that you could have trillions of hair strands. This difference


### Old Curve Rendering requires Curve to Mesh [5:40]
**Transcript (timestamped):**
[5:42] also applies to geometry nodes. Now, let's add a geometry node tree to the NURBS path.
[5:48] To convert it into a tube, the basic solution is the curve to mesh node. By default, it converts
[5:56] the curve to edges, which are still not visible in the viewport without the overlay. In this case,
[6:03] you need a profile curve. Currently, a curve circle is enough to solve it.
[6:10] To change its radius, you can use the radius of our profile circle or use this scale option.
[6:18] It's important to note that said curve radius is not supposed to influence the radius of your
[6:25] curve to mesh. You may find people doing it in older tutorials, but since radius is also influenced
[6:33] by the profile curve and it can cause confusion about the actual radius of the tube, the auto
[6:40] behavior has been dropped and it has been replaced by the scale socket on a curve to mesh node.
[6:48] Nowadays, for these functions altogether, it's recommended to use curve to tube,
[6:54] which is an asset provided by the Belander Foundation. I also have my own version,
[7:00] but ultimately, they are similar. And you can use whichever one you like. The major
[7:06] point of using a preset is to construct a UV map for these curve meshes. The process takes many
[7:14] nodes and the more you need to use curves, the more you shouldn't waste the time constructing things
[7:21] from scratch yourself. So please use the preset. This node tree is for old curve rendering. For
[7:29] our new hair curve type, I'm going to discard the traditional setup by deleting the mesh objects


### New Curve Rendering Settings with Set Curve Radius [7:30]
**Transcript (timestamped):**
[7:36] and removing the beauty modifier it provided. I will add a new node tree from scratch and use
[7:43] a curve line node to replace the group input. It's very thin, but you may still find it as a visible
[7:50] curve without the overlay. If you want to increase its thickness, this is the time to use setCurve
[7:58] radius. Nevertheless, as I increase it, it's not working because you have to go to the render
[8:04] settings. In EV, the default is set to strength. You can change it to either of the other settings,
[8:12] and you can see the viewport showing the change due to the radius. Here, no matter how I rotate my
[8:19] view, this curve is always complete. If you look at its tip, you will find that strip means a plane
[8:27] that always faces the camera. Alternatively, cylinder means a semicircle facing the camera.
[8:35] This makes the system extremely efficient because the traditional curve to tube will generate many
[8:42] more vertices and polygons than needed. Another important perspective is that geometry nodes
[8:49] is running on the CPU while the rendering happens on the GPU. The only downside of this system is that
[8:57] you will find flaws at the tip, but I don't think it's really a problem since you commonly
[9:03] generate trillions of thin hairs to look at their body instead of their tips. In the render settings,


### Cycles Render Settings for New Curve [9:10]
**Transcript (timestamped):**
[9:11] you can also increase the subdivision. I don't think it changes anything these days,
[9:16] but you may want to do it for safety. Additionally, cycles has different render settings
[9:24] compared to our viewport display with EV. Let's go to the render mode. I will disable the scene
[9:31] ward and decrease the strength of the light. Now you can see the buffer. All modes in cycle
[9:38] supports radius. Given our curve line, you will find it as a perfect capsule from all angles,
[9:46] including the tip. At the moment, the stream modes seemingly don't have any difference.
[9:54] The differences can happen when you input grouping input. If you look closely, they are still perfect
[10:00] capsule shapes, but as soon as I switch it to rounded ribbon, you will find something is different.
[10:08] If I increase the radius and look more closely at the tip, you will find it's actually flat,
[10:14] like the strip in EV. If I switch to 3D curves, it's more circular, like the cylinder in EV.
[10:23] Only the linear 3D curve is showing a capsule we saw earlier.
[10:27] Why is there such a difference between the curve line and the grouping part?


### When to use New Curves [10:30]
**Transcript (timestamped):**
[10:32] This is something that we will explain later. Up to now, in conclusion,
[10:38] for geometry nodes, the rendering will differ by object type.
[10:43] An old curve object must go through the curve-to-match process. Even if you switch to the same
[10:49] node tree as our hair curve object, you will find that it's not rendered like the new hair curve system.
[10:56] This is also true if you are generating curves in a mesh object or other object types.
[11:02] The new hair curve rendering can only happen with this new hair curve object with this icon.
[11:08] There is no exception. So if you are working with motion graphics with trillions of strands,
[11:15] you want to use this new hair curve object for faster rendering.
[11:20] Now, we've covered the basics about the old and new curve objects. We need to discuss a bit about the nomenclature.
[11:29] The old system is very chaotic. A single strand is called a spline,


### Spline vs. Curve vs. Hair makes education chaotic. [11:30]
**Transcript (timestamped):**
[11:35] and the multiple splines are called a curve. As you can see from the name of the curve object,
[11:43] I know it's confusing because you could also use plurals for these ones.
[11:48] But that's how it is. Also, remember we have a hair particle or particle hair system showed at the beginning.
[11:57] The new system has a new definition of these terms. It suggests that we only have a single curve
[12:05] and multiple curves. We shouldn't have splines, and we shouldn't have hair as a separate geometry type.
[12:14] Hair should be curved and a curve should be hair. These are the ultimate goals.
[12:20] But as you know, the new system is still under development. We've just started to have hair
[12:26] simulation as an experimental feature in geometry nodes to replace the old hair particles.
[12:37] So at the moment, we are not only having both systems existing at the same time,
[12:43] but we also have mixed nomenclatures. If you search for the word spline, you will see tons of nodes with
[12:52] splines in their names. Developers made plans to change the names as early as many years ago,
[13:00] but they didn't. If you are watching this video from 6.0 or 7.0, perhaps the change has already
[13:08] happened or not. Regardless, these are the realities we are currently facing at at the time of this
[13:17] recording. Besides the rendering and nomenclatures, both systems share exactly the same functions in


### Bezier Curve [13:20]
**Transcript (timestamped):**
[13:24] geometry nodes, including these set spline type nodes I want to discuss next. We have four curve
[13:32] types here. I will firstly discuss the bezier curve as you can find it easily using shift A.
[13:40] If you check the spreadsheet, its curve type is marked with A2 for bezier. If you count from 0,
[13:47] bezier inherits the number 2 from the list of this spline type. This type is characterized by its
[13:54] handles, so you have very few points, but you use handles to construct smooth curvatures.


### NURBS Curve [14:00]
**Transcript (timestamped):**
[14:02] Similarly, we have a nerbs type. We can choose the path and you find the object named is
[14:09] nerbs path. The spreadsheet notes this type as a number of three. It's also a unique smooth
[14:18] algorithm, but it doesn't require handles. I just drag them in edit mode. The control points are
[14:25] straight lines, and they automatically form the curvature from the resulting curve.


### Resolution for Virtual Points in Render [14:30]
**Transcript (timestamped):**
[14:32] Both of these curve types are greatly influenced by resolution. At the top of the panel,
[14:39] you will see a resolution setting. If you decrease it enough, our curvature will become really
[14:45] segmented, like a straight line. The resolution in this context means how many virtual points
[14:52] the render engine will generate for you to construct the curvature. The fewer points,
[14:59] the less accurately you can fake the curvature. Here, it's important to note that a bezier
[15:06] segment only has two points in reality, and all the curvatures you see are kind of made up by
[15:14] render engine based on the resolution. So here I add a null tree and set position with a random value,
[15:23] and you won't see a very crazy result. Similarly, if you use the bezier segment primitive from
[15:30] geometry notes, you won't see a crazy result either. You keep increasing the resolution,
[15:36] and it won't change anything for our set position result. The spreadsheet clearly tells you that
[15:45] you only have two points, and that's all. Next, the third curve type I'm going to discuss is


### Polyline Curve and Catmull Rom [15:52]
**Transcript (timestamped):**
[15:53] polyline. Here, we have this curvature from a nervous pass. If I right click and set spline type to
[16:02] poly, our curvature disappears and becomes rather straight. Basically, polyline is the simplest
[16:10] curve type that connects points from point to point. As a result, it's not really influenced by the
[16:18] resolution, because there won't be any curvature from a straight segment to another. Its curve type
[16:26] number shown in the spreadsheet is one. The last curve type is catmouron. It's the curve type for
[16:34] the new hair curve that we added using sculpting brushes at the beginning. In the spreadsheet,
[16:41] on the spline domain, you may find other attributes, but it doesn't explicitly have a curve type defined.
[16:49] On the other hand, the curve line has curve type I, meaning it's a polyline. And this causes differences
[16:58] in how the cycle engine interprets them in the shape setting. I don't really understand the design,
[17:06] but that's how it is. Polyline and probably other types are not influenced by the cycle shape render
[17:13] settings. By the way, I forgot to mention earlier that the new hair curve rendering can only be


### New Hair must not be Instances! [17:15]
**Transcript (timestamped):**
[17:21] rendered on realized geometry. If I put a geometry to instance, the rendering immediately breaks and
[17:30] the day will show as black lines in the viewport. It doesn't matter what the curve type you input,
[17:37] this means if you're instancing it, you must also couple it with realized instances.
[17:44] And there is no alternative. In terms of functionality, you can consider catmouron
[17:51] as a special type of polyline that can be influenced by the resolution. It may not be obvious, but anyway.


### Resample Curve to add points to curve [18:00]
**Transcript (timestamped):**
[18:00] So generally, polyline is the only curve type not really influenced by the resolution. Nevertheless,
[18:07] sometimes, even for a straight line, you may want to add a real point to it so that you can
[18:13] potentially displace them for various effects. There are two ways to add points. One of the most
[18:20] common ways is to resample curve. Internally, it's actually converting all curves into polylines.
[18:28] It contains three modes. The first mode is called the evaluate. It will add real points based on
[18:35] the resolution you have. For example, you start with a bezier segment that only has two points,
[18:43] but once we resample it, we have the maximum point index matching the resolution. If you increase
[18:50] the resolution, it will generate small points or decrease it to have fewer points. Or if you
[18:59] additionally set the spine resolution, it will also override the existing resolution and generate
[19:06] more points during the later resampling. Interestingly, we have a quadratic bezier curve.
[19:13] If you do the same process, you will find the resampled counts won't be changed by the set
[19:19] spine resolution. It only works with the resolution settings on the original node.
[19:26] This is because, despite the name, quadratic bezier is a polyline as stated by the tooltip.
[19:35] You can also confirm this with the spreadsheet, which shows curve type one. And although it's a
[19:42] polyline, it has a resolution setting, but it's not the same one that can be modified by the set
[19:50] spine resolution node. The resolution setting for a polyline curve is more like a count setting.
[19:57] In the spreadsheet, you can see these resolution attributes, which is created by this set spine
[20:04] resolution node. The polyline doesn't contain a resolution attribute itself, but the bezier
[20:11] segment does. The differences I'm discussing here may sound very confusing, but it's not on me.
[20:18] Plus, although this is all true information, I hope you treat it like a kind of a fun fact or a story.
[20:27] Please don't take it too seriously. Because ultimately, in real life, I just
[20:33] the brainlessly re-sample everything, which converts them into polylines without a resolution setting.
[20:42] Talking about two other modes, re-sample count is straightforward. You set the count.
[20:47] Re-sample by length is essentially trying to define the interval from point to point. Take a one
[20:54] meter long curve line as an example. A longer interval means fewer points, while a shorter
[21:01] interval means more points. Note that this interval setting is not necessarily accurate,
[21:09] because if you have a one meter curve and set the interval to 0.8, you won't have enough space to
[21:16] generate all the points, because when you cut a point at 0.8 meter, the second segment must be
[21:23] less than it, and thus this result becomes invalid. Only if you set the interval to 0.5,
[21:32] you will find that you can divide it correctly, where all points are at least 0.5 meters apart.
[21:40] This logic of re-sampling also happens in curved points or possibly other presets.
[21:48] If you find any menu with similar settings I knowed related to curve, you should recall their meanings.
[21:55] Technically speaking, re-sample curve can have lots of issues within accuracy,


### Subdivide Curve as an Alternative to add points to Curve [22:00]
**Transcript (timestamped):**
[22:01] but I don't think they are important for beginners. In case it has any problem,
[22:07] we are here to discuss the second way to increase the point count. If you are familiar with the
[22:13] known names, you may know there is a node called the subdivided curve. This method
[22:20] doesn't change the curve type, and it resolves some potential inaccuracy with re-sample curve.
[22:28] The downsides are that you cannot set a definitive count, and the points may not be distributed
[22:35] equally. But it's a quite good method for solving some unique issues presented by the re-sample curve
[22:42] node. So this is all about it today. I've made this episode very verbose, but to be honest,
[22:52] the only two important things are the new hair curve for its faster rendering, and the mixture of
[22:59] nomenclatures. It's very possible that all the spline nodes will be renamed to curve nodes,


### Take Home Message [23:00]
**Transcript (timestamped):**
[23:07] like setSplineType will likely be renamed to setCurveType. In fact, you may have already noticed
[23:16] even in the spreadsheet, we have this chaos. Why does the curve contain a spline?
[23:23] So the nomenclature is so important to clarify before we move on to the next episode,
[23:29] where we will talk about the curve attributes and the more usage and utility with the curve nodes.
[23:36] I also hope this tutorial clears up the confusion when you look back at all the tutorials in the
[23:42] future. Oh, they've been renamed to curve now. So I hope you enjoyed this tutorial,
[23:50] and I will probably see you next time. Bye bye.



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
