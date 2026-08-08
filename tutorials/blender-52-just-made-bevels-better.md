---
title: Blender 5.2 Just Made Bevels Better
source: YouTube
url: https://www.youtube.com/watch?v=PICzZINI0VM
author: SouthernShotty
ingested: 2026-08-08
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-52-just-made-bevels-better/
frame_count: 0
frame_status: pending-selection
---

# Blender 5.2 Just Made Bevels Better

**Source:** [YouTube](https://www.youtube.com/watch?v=PICzZINI0VM)
**Author:** SouthernShotty
**Duration:** 13m56s | 6 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-52-just-made-bevels-better <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### New Geometry Nodes Feature [0:00]
**Transcript (timestamped):**
[0:00] Blender 5.2 added a whole host of new features to geometry nodes, including sound support,
[0:05] string detects, experimental cloth physics, which we've actually covered in a previous
[0:08] tutorial on this channel, and many more features. So you might have missed the fact that they added
[0:13] a bevel mesh node right in geometry nodes. So in this video, we're going to dive in how to apply
[0:18] this node and how to utilize it. Then we're going to show how to create this cool Inset Panel Setup
[0:23] all on one Blender geometry node, something you previously had to do a large modifier stack to
[0:27] achieve. So let's dive in and get started. So applying the mesh bevel node is pretty simple.


### Mesh Bevel Basics [0:30]
**Transcript (timestamped):**
[0:32] Alls you need to have is a geometry node system, and you can search for the mesh bevel node. We'll
[0:38] take a look at some of the settings that we have here, and then we'll dive into creating that panel
[0:42] setup that I showed. So up top here, we have the selection. This enables you to determine where you
[0:46] want to bevel. So for example, if I drag this onto our output here, turn this into a selection,
[0:52] I can select one of my vertex groups here, which is called bevel. And you'll see that it's only
[0:57] beveling the selected vertex points. Below that, we have the option to start the offset per direction.
[1:03] For example, we can start from the left or the right there. Now, in most cases, you're going to
[1:09] want to keep these all to be the same number. So one thing you can do is drag these all into the
[1:14] same socket here. And then that'll give you one output that'll control them all at once,
[1:19] similar to the bevel modifier node. Below that, we have the miter option to change how it handles
[1:23] corners. And we can change the spread size there as well. Beneath that, we have the option for
[1:29] segments to introduce additional edge loops to round out the corners more. And here we can change
[1:33] the shape, whether we want it to be inset or outset from the object. I'm going to leave that at point
[1:39] five to give us a neutral result. Down here, we have the option for a profile. This is so that you
[1:44] can input curved inputs here. And then you can use that to drive the shape of your bevel edge.
[1:50] You need to make sure that you introduce some additional segments there so that you have
[1:54] actual geometry to work with. Now, a cool feature is that you can now output your selections here.
[1:59] As far as I'm aware, this is not possible within the modifier. And if I click here, you can actually
[2:04] snap through and see that we can see on our object where things are being beveled. And we can output
[2:09] these masks to utilize in other nodes and shaders. Now, of course, the biggest advantage of having
[2:14] access to mesh bevel within geometry nodes is that we can set it up in systems like this. If we take


### Building the System [2:20]
**Transcript (timestamped):**
[2:20] look here at this mesh box, you can see that anything that has a sharp edge is actually being
[2:25] cut and beveled to create a hard surface panel cut. Over here, you can see that it's just one
[2:30] simple panel that gives us all of these controls. And it's actually not that complicated of a geometry
[2:35] node setup. So now we're going to dive in how to create this simple system. But before we start
[2:40] building nodes here, I want you to understand what we're actually creating this panel cut system is
[2:44] something that's been utilized and blended for a while. But as you can see on this example here,
[2:48] it typically involves a pretty large modifier stack that you can see over here on the right.
[2:54] So we're essentially going to be creating a stripped down simplified version of this in
[2:58] geometry nodes so that we can access all this information from one panel and easily copy it to
[3:02] any object. So I'm going to break down how it works here in the modifier stack. And then we're
[3:06] going to recreate that in a simpler way within our geometry nodes. Now, a really cool thing about
[3:10] this effect is that if I tab here into the geometry mode, you can see that this is actually a very
[3:15] simple box. So our geometry node setup is actually doing a lot of heavy lifting to kind of create
[3:20] those cool sci fi panels and beveled edges to take it from a simple low poly object to a detailed
[3:26] asset. So the way this effect works is that we are feeding in sharp edges to tell it where we want
[3:31] to cut panels. And in the traditional way, we would use an edge split modifier here with the
[3:36] edge angle turned off and the sharp edges turned on. And if I were to take this and apply it here,
[3:41] what that's actually done is it's actually split our object into various pieces, wherever it has
[3:47] been cut by those sharp edges. Now the next step in that process is a solidify modifier. And what
[3:53] this is going to do is add a little bit of extrusion to the geometry set inwards. And if I
[4:00] apply all these effects, you can see that now what it has done is given us a couple objects here,
[4:05] where I move out here, and you can see now we have a few objects that have been completed with
[4:10] their own edge sets. So that means that when we turn on the last modifier here, the bevel,
[4:16] it is beveling all those individual objects, and it creates the scene for us giving us that nice
[4:21] hard surface panel cut. So let's look at how we can recreate this effect all in one geometry
[4:26] node. So to start, I'm going to use my box object here. I will be putting the final project files
[4:32] on Patreon if you'd like to take a look at those. But if I tab into edit mode here, you can see that
[4:36] it's a very simple geometry setup. And the only unique thing here is that there are these sharp
[4:42] edges. If you don't know how to add a sharp edge, all you need to do is be an edge select mode,
[4:46] and you can just right click and come down here to mark sharp or clear sharp if you'd like to get
[4:52] rid of it. I like to set mine to the quick favorite menu so that I can quickly do it by pressing Q.
[4:56] I'm going to drag this over here to give us some space. The first thing we're going to do is recreate
[5:01] that edge split modifier and geometry nodes. So here I have my geometry nodes window open with


### Creating Panel Cuts [5:05]
**Transcript (timestamped):**
[5:07] my object selected, I'm going to click new, and I'm going to call this hard surface panels. So on
[5:13] this geometry line, I'm going to add a split to instances node, and you're not going to see anything
[5:19] happen here. But we're going to choose what we want to split by. So I'm going to split by face.
[5:24] And now what it's doing is splitting all these faces into their own instances. And now we want
[5:29] to give it some direction about where to split. So we're going to feed the sharp edges into here.
[5:34] And luckily for us, that's actually just a base attribute within blender. So if we search for
[5:39] named attribute here, we're going to switch this to a Boolean mode so that it is on or off, and we
[5:44] can type in sharp underscore edge, and then we can take this attribute here and drag it into our
[5:51] group ID. Now I'm also going to add a edges to face groups, because we're going to end up using a
[5:56] face group here later. I'm just going to drag that in between there. And now what we've done is
[6:01] create some face groups based off of our sharp edges. Now you might be wondering why we're doing it
[6:06] this way, instead of just utilizing a split edges node. And that's because if you recall before,
[6:11] when I applied the solidify modifier and the edge split modifier, it actually put it into
[6:16] its own objects, where it was solidifying each object individually. And so we want to make
[6:21] sure that we're recreating that if we use a split edges node, it won't do that. Now let's do
[6:26] a quick viewport shading trick to make this a little bit more visible. So if I come up here,
[6:31] click here, I can switch to mat cap, turn on cavity and outline. And now I can see that when I tab
[6:36] in edit mode here, wherever I have a sharp edge in its creating an object intersection, we can now
[6:41] see that outline of the object. So essentially what we're telling geometry nodes is this one
[6:46] object is now split into all these objects based on where we put the sharp edges. So the next thing
[6:51] we need to do in the process is we want to solidify the geometry. Now this is pretty simple to do
[6:57] with an extrude mesh node, but we're going to do it slightly differently because we want to extrude
[7:02] every one of these objects individually so that it gets its own edge geometry. And we can utilize
[7:07] the bevel node to take advantage of that and create our panel cuts. So for this effect to work,
[7:11] we first want to realize our instances. So we're going to search for a realize instances, put that
[7:16] there and just leave it at the default settings. Now we're going to do the solidify effect. This
[7:21] is very simple to do. You just need to use an extrude mesh. And we can put that there right
[7:26] after the realize instances. And I'm going to split our window here so that you can see a wireframe
[7:32] on the right here and our final result on the left. So to do that, we're going to use a for each
[7:37] element. So I'm going to search for for each element. And we're going to put this here after our split
[7:41] instances. And we're going to get this little zone right here. And what this is going to do
[7:46] is go through every object and repeat the action we have in here. So we're going to create a solidify
[7:52] modifier. It will look at every instance that's been input into it and repeat the action, meaning
[7:58] we will do a solidify every independent object, which is what we want to get the effect I showed
[8:03] earlier so that we can bevel the edges and get the seams. Now you'll notice here that we don't see
[8:08] any visual difference. And that's because right now our for loop here is looking for points. And
[8:13] we've input instances, where we're going to switch this to instance, you'll see nothing is still
[8:17] happening. And that's because we have a different input geometry and output. So we just need to
[8:21] take this little output over here and plug it in. And you can see now that it is exploding with the
[8:27] extrude mesh. So let's do a few things here. First, we're going to turn off individual faces. We want
[8:31] this to do per object. And then let's actually plug our offset value into our group input here.
[8:36] So this way we can control the number over here. Now I'm going to do a really small value here
[8:41] like point zero zero nine. And then I want this to be going inward, not outward, you can see right
[8:47] now it's extruding outward. So we're going to add a multiply node. So we'll just do a math multiply,
[8:54] click that there, make sure this is plugged into the top. And then I'm going to do a negative one
[8:59] value here at the bottom. And now you can see how it is in setting inwards. Now we have a couple more
[9:04] notes to do here, we need to flip the faces as well. By turn on face orientation here, you can see
[9:11] how we're seeing a lot of red bleeding through there. So we're going to grab the join geometry
[9:17] node, like this here. And then we're going to grab a flip faces node. And we're going to take the
[9:23] original geometry here, plug it into here, and then plug that up into our join geometry. Now we're
[9:29] going to end up flipping this again at the end here. So now we've created the entire solidify effect.
[9:36] So next what we want to do is create the bevel modifier effect. So we're going to do that over
[9:41] here. And the first thing we're going to do is that we have all of our faces here facing the same
[9:44] direction like we wanted. And we are going to flip faces one more time. And now things will return to
[9:50] normal. And we're ready to begin setting up our bevel modifier. So now we're ready to add our


### Finishing the Setup [9:54]
**Transcript (timestamped):**
[9:55] bevel node. So let's add our mesh bevel node right here. And we're going to expose some controls
[10:01] so that we can easily work with this over here in our panel. Now you can drag all these back to
[10:07] the group input, but you can actually just duplicate the group input and bring it up here. And then
[10:11] we can keep our graph a little more organized. So the first thing we want to add is a thickness
[10:17] option for the bevel. And so we're just going to grab all of these and plug them into the same
[10:22] socket here. Now, if you don't know, you can actually rename these over here. So this would be
[10:26] our solidify thickness. And then this would be our bevel amount. You can see now those are organized
[10:32] over here. And I'm going to set this bevel to something really small. So it quits breaking
[10:36] like that. So I'm going to do 0.01. And we can see that now if I turn off the face orientation here
[10:43] that we're starting to get our effect there. Now if I zoom in here, you can see even with a small
[10:48] bevel, we're still getting a lot of breakage and how these things are almost poking out and creating
[10:53] some awkward geometry. Now this has to do with the fact that we did that instancing and created all
[10:59] these separate objects and then solidified them, but we didn't join them back. So as far as blender
[11:04] geometry nodes is concerned, those edges that are sitting along here aren't really all part of one
[11:09] object. Again, if we go back to the example I showed when it was split apart into various objects,
[11:14] that's what we're trying to create here. So what we just need to do is ensure that when we send this
[11:18] over to our bevel, each one of these panel cuts is seen as its own object with its own
[11:23] individual edge data. That's pretty simple. Alls we need to do is add a merge by distance here.
[11:29] We can set this to a really small number. So I'm just going to add an extra two zeros here.
[11:33] And you can see it's already starting to clean itself up. So let's look at what else we can do
[11:37] to improve this here. One thing I want to do is expose the segments here. So I'm going to expose
[11:41] the segments there and I'm going to bump this up to three. You can see that's already starting to
[11:45] fix the effect. And the other thing I want to do is have an angle limit. So we're actually going to
[11:51] make our selection here work off an angle limit. And it'll look at the angle of the edges and
[11:57] determine whether it bevels that or not. This is pretty simple. Alls we have to do is input an
[12:02] edge angle node. And for this one, we want to take the unassigned angle here. And we're going to
[12:07] drag this off and search for a greater than. Make sure this is set to float. This is set to greater
[12:13] than. And we're going to plug the result here into the selection. You'll see here that a lot of our
[12:17] options here disappear. And then we're going to drag the B option here. We're going to put this down
[12:22] here. And I'm going to rename this bevel angle. And now whatever value I enter here will be
[12:28] accounted as the angle. So I'm going to do 30. And you can see how it quit angling all of our
[12:34] edge loops. Whereas before you can see here, it was beveling every single edge loop that we had on
[12:40] our object. So here, if I hit 30, that can help clean it up. Now you'll notice here that once we
[12:45] implemented this greater than it completely deleted our bevel on everything. And over here,
[12:50] that's because it's actually looking for an angle value. So what you want to do is grab your bevel
[12:55] angle over here on your group node, come down here to the subtype, and we're going to set this to
[13:00] angle. And when we do that, it's going to turn our value into an angle. Here you can see it's
[13:05] incredibly large at 1700 degrees. So if we bump this back down to 30, now you can see we have
[13:10] our final effect. And then the last thing you can do is right click, shade auto smooth, I'm going to


### Final Result [13:12]
**Transcript (timestamped):**
[13:16] set mine to something like 60 degrees here. And you can choose to ignore sharpness. And now you
[13:21] can see we have a super simple, easy to do panel cut system. If I wanted to add more in here, I
[13:27] could grab this edge loop, mark as sharp and come out and you can see how it's already gone through
[13:32] and added that panel cut effect. If you found this tutorial helpful and you'd like to support the
[13:36] channel, you can check out my Patreon where I provide project files such as this and other
[13:41] goodies. I also have a variety of in depth courses on Skillshare and several products on SuperHive,
[13:48] which are all linked below.



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
