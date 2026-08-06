---
title: Image to 3D model workflow in Blender
source: YouTube
url: https://www.youtube.com/watch?v=DBuKtyPaIbw
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 4.3.2 (explicitly named — trace-to-mesh conversion improved significantly since 4.0.2, also explicitly demoed)"
tags: [modelling, organic, procedural, displacement, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/image-to-3d-model-workflow-in-blender/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Image to 3D model workflow in Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=DBuKtyPaIbw)
**Author:** Blender Secrets
**Duration:** 39m50s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this video we'll have a look at creating a 3D model from a black and white image.
[0:04] This is meant to be a beginner-friendly workflow and we'll go over it step by step
[0:08] so that you can definitely repeat it yourself.
[0:10] After that we'll briefly look at using the result in a sculpting workflow
[0:15] to create an interesting 3D concept.
[0:17] I wanted to revisit this topic in a little bit more detail
[0:20] because I keep getting questions about it and some things have changed also in Blender
[0:24] with how trace image degree spasal works. It's actually improved.
[0:28] And what this topic was about, if you didn't watch this video,
[0:31] it's about making little thumbnails, black and white thumbnails, in this case of robots,
[0:35] and just dropping them into Blender and then turning that into a mesh
[0:38] through the convert to grease pencil tool.
[0:41] But let me show you how that has changed and at the end of the video
[0:44] I also want to show you a slightly different workflow that I think is maybe a bit more evergreen
[0:50] and that is perhaps also easier and even more creative.
[0:54] I just want to give you both workflows so you can choose for yourself.
[0:57] So let's go into Blender and I have here Blender 4.3.2.
[1:01] So the way this works is first of all I would go to the front orthographic view
[1:04] and then drop in this concept art and press Alt G to center it.
[1:08] So this is just a little black and white sketch that I made in Krita just now.
[1:12] As you can see everything is separated into this distinct islands
[1:17] and just turn off the grid so you can see better.
[1:20] So there's white lines between everything and that just makes it easier for Blender
[1:24] to separate it into mesh islands as well.
[1:26] And so let me just turn that back on.
[1:28] So let me just select this and then go to objects convert and then trace image to grease pencil
[1:35] and just use the default options.
[1:37] And so now we can turn this empty which was the concept art that I dragged in.
[1:41] I can turn it off and then we have this grease pencil object.
[1:45] And as you can see it's created in edit mode all these vertices.
[1:48] And now let me just go again to convert and then choose mesh.
[1:52] And this is already where it's a little bit different than the older versions of Blender
[1:55] because before you had to first go to path and then you could convert that path to mesh.
[1:59] Now you can go straight from grease pencil to mesh which is great.
[2:02] And it's still called grease pencil in the Outliner but this is now just our normal mesh.
[2:06] And if I go to edit mode you can see it has a ton of vertices way too many vertices in fact.
[2:12] But it has separated everything into individual islands.
[2:15] So I can just hover over this and press L to select these individual islands as you can see.
[2:21] And I could already select everything and press F and that would fill all of these
[2:26] and turn these into mesh planes and I could just extrude them and everything.
[2:30] And this is already quite different from the old version of Blender.
[2:33] So just to show you how different it is this is Blender 4.0.2.
[2:38] So a few versions will go and if I go to object convert trace image to grease pencil
[2:43] and then click on OK and turn off the empty and then object convert.
[2:48] Then I have to go to path first and then it's already a bit confusing in the Outliner.
[2:53] Which one is the mesh? So if I turn off the grease pencil one,
[2:56] okay then the trace is the mesh and then I can look at this in edit mode and it looks like it's
[3:02] a mesh but it's not. So I have to convert it now to a mesh and now it has just changed the icon
[3:08] here. It's still called trace but now this is a mesh and it has significantly more vertices
[3:13] if you look at this compared to the 4.3.21. So this one seems to be a bit more efficient.
[3:19] So in Blender 4.3.2 you can see there are less vertices than in Blender 4.0.2.
[3:25] And if I now select everything with A and then press F to fill them,
[3:29] at first nothing is happening and then it's only filled this.
[3:32] So with the exact same drawing it actually doesn't work in Blender 4.0.2 and it worked
[3:38] right over the bed in Blender 4.3.2. So they have definitely improved something behind the scenes
[3:45] here and so if you're going to use this kind of workflow I recommend that you use the latest
[3:48] version of Blender. So now to clean this up because we want this to be kind of mechanical and machine
[3:54] looking and now this is a bit too organic because there are just too many vertices and what we can
[3:59] do is we can just press A to select all and then go to mesh clean up and then limited dissolve.
[4:06] And as you can see that already took a lot of the vertices away so it's set to 5 degrees and
[4:11] that's a good default value. And then one more thing you can do is you can press M and then merge
[4:16] by distance and then you can try increasing this value and seeing what you get. However I would
[4:22] advise to first press P and separate by loose parts and so now we can still select everything in
[4:28] object mode and then tap to go to edit mode. So we still have everything selected in edit mode
[4:34] but it is now being considered different object. So when we do the merge by distance it's never
[4:39] going to merge things from different mesh islands. Now we can try to increase the mesh distance
[4:44] and we will get a more simple topology like this. I think this is already probably good enough so
[4:49] 0.0201 meters. Here and there there are some loose vertices like this or like here there are a whole
[4:55] bunch of loose vertices and what you can do is just again press A and then go to mesh clean up
[5:00] and delete loose. That's already deleted all of those and so this is starting to look more and
[5:06] more clean and then another thing I would do is just press K for the knife tool and then just go
[5:11] all the way down here and if you press A it constrains it to an angle and then press here and
[5:15] press enter. So now we have split this in the middle and then in face selection mode we just
[5:20] select all of these, delete them and then we can add a mirror modifier to this like that and
[5:27] press ctrl i to invert shift to select this one. So we have everything selected and then as the last
[5:32] thing we have the one with the mirror modifier and then press ctrl l and copy modifiers. Now they all
[5:38] have a mirror modifier and that just makes it easier for us. We just have to do half the work
[5:42] and so what we're going to do now is we're going to improve this geometry. So let me just select
[5:47] everything in object mode. So object mode A to select everything and then tab to go to edit mode.
[5:52] The way you can work on all the objects in edit mode you don't have to keep going in and out of
[5:56] edit mode and one thing I want to do is I want to select all of these vertices in the middle and
[6:00] then just scale them on the x axis to zero. So sx zero and then enter and what that is is they are
[6:08] all scaled to zero on the x axis but it looks like they are not really in the middle. So what we have
[6:14] is we have the 3d cursor in the center of the world and if you don't have it there press shift s
[6:19] and choose cursor to world origin and then we set here the transform pivot point to 3d cursor and
[6:25] now again if we press sx and zero and enter then you can see that it really snapped to that zero
[6:30] position and then don't forget to turn this back to median point. So now we have these
[6:34] vertices really in the middle and it looks like here we still have one vertex that we don't need
[6:39] maybe just press ctrl x. So ctrl x dissolves vertices and let's see if there are any others
[6:45] that we need to get rid of. It's just good to have clean topology that will avoid issues in the
[6:51] future. We see it looks like there are two vertices here as well so ctrl x. You can always just do a
[6:57] wiggle test where you select the vertex and wiggle it around a bit to see if there's any doubles there.
[7:01] So another thing you can do is select all press m merge by distance and then make sure this is set
[7:07] back to 0.0001 meters that's the default otherwise it will start to merge too many things and if
[7:14] it's not set to that what you can do is right click and click on reset to default value. Otherwise
[7:19] it's going to start merging things that you don't want to merge but now there are definitely no
[7:22] double vertices anymore. And now before we add thickness to this I just want to make sure this
[7:27] is all quartz because now these are all just giant n-gones and that's not going to subdivide very
[7:32] well at all. Actually just let me show you what's going to happen if we use this now. So if we add
[7:37] a solidify modifier to this and increase the thickness and then we add a subdivide modifier to
[7:43] this with two levels for example. Then you get this kind of blob and we don't want to have a blob
[7:48] for our Mac. We want to have something that looks like a hard service model and for that we need to
[7:53] have quartz topology. Hey before we continue to the tutorial just a quick plug for the seal that
[7:59] I'm running. So I have a 30% discount of everything so everything is my book the hard service sculpting
[8:05] course in blender drag-and-drop materials and my new hard service modeling course and you can get a
[8:11] 30% discount with the coupon code Bday because it was because of my birthday. It's extended until
[8:17] Saturday. However if you're too late for that and you still want to get a big discount there's a
[8:22] very big discount if you buy my bundle and the bundle the hard service bundle is with my book
[8:28] hard service course modeling course and the materials course and assets and you get 60
[8:33] dollars off if you buy that so you can buy that at any time. Now if you want to turn this into quartz
[8:37] what you can do is you can use the knife tool so press K for the knife tool and then left click
[8:42] and left click and then right click so you can move the cursor and then left click again
[8:48] to cut and right click to reduce it and then left click again to cut and then press enter and as
[8:53] you can see now I have a bunch of quads. So let me repeat to you how this works so K for the knife
[8:58] tool or if you don't want to remember the K keep your shortcut just here in the tool panel the tool
[9:02] panel by the way you can open it with T here you have the knife tool and as you can see it turns
[9:07] the cursor into it and then you just click on a vertex and you left click on another vertex
[9:12] and then to make sure you can continue summary just right click and then freeze it up and then
[9:16] you left click again to continue right click left click left click right click left click and so on
[9:23] and then when you're finished just press enter so that's also turned into quads this is already a
[9:27] quad and yeah you just continue like that and it may seem like a lot of work but it just really
[9:34] takes a couple of minutes and that's all. So I'm just quickly going to do this so that you don't
[9:39] have to sit through the whole process of me doing this and if you have something like here this
[9:43] triangle what you can always do is just cut to that triangle from there and then just go back
[9:49] to select tool and then select this one and double G and slide it and now this is also a quad
[9:56] and back to vertex selection mode and then here we have a vertex which is not really contributing
[10:01] anything so we can just select and control X and dissolve it and I'll just continue cutting with
[10:07] the knife tool. I will say one thing that's very important to pay attention to is that you don't
[10:13] get too much geometry so you don't want to get too much detail at this stage you just want to have
[10:19] really as simple quad topology as possible and sometimes you can even simplify the geometry
[10:24] like here this edge we can just alternate to the connet and then just control X to solve it and like
[10:29] this one we cannot dissolve because it's important for this corner here with this one not really doing
[10:35] anything so control X get rid of it arguably this we can get rid of as well let's see maybe this one
[10:41] well this one is kind of important this one is not so we can get rid of it and you really want to
[10:46] have as little geometry as possible in the beginning if you can get rid of some vertices then just
[10:51] dissolve them I think this is a good result and sometimes you have to check it might look like
[10:56] you have all quads but if you select one where you're certain that it's quads and then you press
[11:00] shift G and then you choose polygon sides and it's set to compare equal then you can see that
[11:06] there are some faces that are not selected and these are apparently not quads so for example this
[11:10] one is not a quad let me just go into vertex selection mode and it's because there's this
[11:15] vertex here and let's see I'll have to go back and try it one more time so G polygon sides so this
[11:21] one is also not a quad and that's because of this vertex here let's try that again shift G polygon
[11:27] sides and so there's this one as well and we can still that with the knife tool here and so let me
[11:34] try that one more time shift G polygon sides and there's also this one and that's because apparently
[11:40] there are these little vertex here so it was quite well hidden if you look at it like this so I can
[11:45] dissolve that and so I think now we have everything so they are all quads now so sometimes it's important
[11:51] to do a quick check like that with the shift G select similar manual you can also find that by
[11:57] going to select here and select similar and then just choose polygon sides because it's just not
[12:03] possible to visually inspect it because sometimes those vertices are so close together or something
[12:09] can just be an end gone and you just think it's a quad because it just looks like a quad and so
[12:13] now we have this which is all quads and I'm just quickly save that and so now we can start adding
[12:18] some thickness to this so go to search and solidify and then just increase the thickness and instead of
[12:24] it going forward like this we can set the offset to zero then I just make these thickness from out
[12:29] of the center of the object let me just quickly turn a matcap on so that looks more interesting
[12:36] and I'll also turn on cavity and shadow and set this to both that just looks better maybe let's
[12:42] use a different matcap and I'll press control I to invert the selection again shift and select
[12:48] this object then again press control L and copy modifiers so now they all have these mirror and
[12:54] solidify modifiers and so you can see now it's starting to get a bit more three-dimensional
[12:58] if you want you can also set this color to a random then everything has different colors
[13:02] maybe that's easier for you to see what you're doing but I'm just gonna leave it like this
[13:06] and you can now just start increasing the thickness of individual objects so you can start
[13:12] playing around with that and so yeah you can start to increase and decrease the thickness of things
[13:17] as you see fit and this is already where it starts to get a bit more creative so now we have this
[13:23] fairly simple blockouts and I'm going to add a couple of modifiers to it to make it a bit more
[13:28] interesting but first of all we have to apply the solidify modifier and now you might be wondering
[13:33] how do I just apply the solidify modifier for all of these objects at once because if I press
[13:38] control A and choose visual geometry to mesh it will just apply the mirror as well and we want to
[13:43] keep the mirror modifier so to apply the solidify modifier for everything and only the solidify
[13:47] modifier we select everything and then we hold alt and with alt we click on this and choose apply
[13:53] and now all of these solidify modifiers are applied but we have kept the mirror modifier for all of
[13:58] the objects I will say this doesn't work on everybody's configuration because let me just
[14:03] show you in preferences here in input I have disabled emulate three button mouse that's just
[14:09] the default but that's how I like to work but some people coming from for example 3ds max they
[14:13] like to enable that because it's a bit more similar to how they used to work and if you have this
[14:17] enabled then you cannot hold alt and apply all of these modifiers at once so if you can't use
[14:23] that trick of holding alt to apply all the modifiers then just select this and press control A and
[14:29] choose visual geometry to mesh and then you just have to add the mirror modifier again that's all
[14:34] so now we have applied this solidify modifier and what we can do is just connect some object and add
[14:40] two subdivision surface modifiers and we will set this first one to simple that's very important
[14:45] and the second one to get more clerk so to show you what's happening I'm just going to turn off
[14:49] optimal display and turn on the wireframe that way you can see exactly what these modifiers are
[14:54] doing and let me set them both to zero so this is the mesh the way we have it now let me just
[15:00] get an annotation here so what the simple algorithm does is it doesn't do anything with the shape it
[15:06] just looks at everywhere where there are two edges and it adds another edge in between so it's just
[15:12] going to add loops like this and it's going to do that for everywhere where there are two loops
[15:18] and I'm just showing you if I set this to one that's exactly what it has done and I can just erase
[15:23] these real quick but what the catmalk clerk algorithm does is it also adds those loops but
[15:28] it also smooths everything and it will smooth it even more if I add more levels and by combining
[15:35] these I will kind of protect the shape and also add some smoothness I'm kind of reducing how much
[15:41] it smooths the shape let me show you if I both set these to one and let me just turn off the wireframe
[15:46] now and you can kind of control with this first modifier how smooth you want the shape to be
[15:51] so with zero levels then it's as smooth as it would normally be with this second one
[15:56] let me just increase the levels here but if I add another level it will become more blocky and if
[16:02] I add another level here it will come even more blocky so you can kind of control the shapes
[16:06] with this first modifier and of course we can set these to shade smooth and yeah that's how we can
[16:12] control the shapes for all of these objects and so what I want to do now is just control i to invert
[16:17] hold shift and select this one and then control l to copy the modifiers and then I'm going to right
[16:23] click and shade smooth so if you get something like this with this ugly crease in the middle
[16:28] that's just because there are actually faces here and you can easily solve that if we just go to front
[16:33] orthographic view select everything enable x-ray view and edit mode and then we can just select
[16:39] these faces so make sure you have face selection mode enabled and hold shift and just select all
[16:45] of these and be careful that you don't select too much that's everything and then press x and choose
[16:52] faces and so now those inner faces are deleted and we have no creases anymore and so now I can
[16:58] start to decide for all of these objects like how sharp do I want them to be for example this I can
[17:03] add some more sharpness maybe one level is enough I wouldn't add too many levels to this so don't go
[17:09] too far like this because that will just add a lot of edges that you don't want maybe something
[17:13] like that and we can still change the thickness of everything later if we want and because this is
[17:18] all very simple we can very easily change the shape so let me just go to face selection mode and
[17:23] select this face and hold control and select this one and that selects everything in between as well
[17:28] and let's say I want to scale this on the y-axis so I press s and y and then move this if you want
[17:34] you can also enable a gizmo by clicking on this drop down and then you can click on scale for example
[17:40] and then you can just drag on this green handle and so that's adjusted that shape slightly so that
[17:46] has made this a bit more round and there's also a gizmo for moving so if I select for example
[17:52] these edges here and then we can move these or we can select these two and move them forward
[17:59] so that's a very easy way to change the shape and so because the geometry is so simple just these
[18:06] small changes make a big difference so if I want I can also rotate this object however all of the
[18:12] objects have their origin here in the middle now and if you want to be able to rotate this easily
[18:18] then the origin should be in the middle of this object so if I select all by pressing a and I go
[18:23] to object set origin to geometry then we have this problem that now the mirroring doesn't work anymore
[18:30] and to solve that I can press shift a and add an empty and any kind of shape will do let me just
[18:38] put that over here so you can see it better so for example a sphere and this is a sphere empty and
[18:43] if I go to the empty menu here I can kind of decrease the size don't decrease it by pressing s
[18:50] for scale just do that here and so now when I select any of these objects and go to the mirror
[18:54] modifier then I can use this picker icon to select this empty and so now it's mirroring along that
[19:01] empty again and now if I press control i to invert the selection hold shift and select this
[19:07] shoulder piece and then I can do that trick again of holding alt and then just click here and choose
[19:14] that empty again and now I've added it to all of these objects so all their mirror modifier have
[19:20] this empty object now as the mirror object and this kind of controls where it mirrors from so
[19:26] it's best to just leave that in the right location if you accidentally move it and you don't know how
[19:31] to put it back here in the center just select it and press alt g and so now I have the origin here
[19:37] in the middle and let me just turn on the rotate gizmo as well and so now I can use these circles
[19:43] to rotate this and as you can see I also still have the scale gizmo and the move gizmo so I can
[19:49] use that to adjust this now let's say I want to scale this up I want to scale it in this direction
[19:55] then the problem is that you can see the gizmo is not pointing in that direction it's just pointing
[19:59] in the coordinates of the world so what we want to do is go over here to transform orientations
[20:05] and then set this to local and so then you can see it's pointing in the right direction so we
[20:09] just use this we drag on it and then we can just move it where we want and scale it perhaps some
[20:16] more like this and then it's best to turn this back to global and then I can just quickly erase
[20:23] this annotation and maybe we can move this a bit closer here so it becomes kind of an antenna or
[20:30] something and if you just want to be able to freely rotate something you can just press r twice then
[20:34] you can just kind of rotate it like this and by the way you can also find those rotation values
[20:39] if you press n here then you will get the option panel and then as you can see here there's also
[20:44] these rotation values and I would recommend holding shift otherwise it will go very fast
[20:49] so with holding shift you kind of have more subtle control over those values and also the
[20:55] scale and location values are here I'm just creating going to go through all of these objects
[21:00] and in edit mode adjust the shape to make it more interesting so another thing if you think it's
[21:06] annoying that you have such a big difference between this cage which is just the object the way it
[21:11] looks without modifiers and the blobby shape of the subdivided mesh you can always enable here
[21:18] this button this is the on cage button and I'm just showing you this one as well and so now you can
[21:23] see exactly what the modifiers are doing even in edit mode so that can be more convenient and again
[21:29] if you want to enable that for everything just go to object mode stacked everything and then just alt
[21:35] and click on this you might have to click on it twice and then you can see in edit mode that they
[21:40] all now have this that can make it a bit more easy to see what you're doing and yeah I'm just sort of
[21:47] pulling on edges and just trying to make these shapes a bit more complicated and of course all
[21:53] of these shapes are kind of separated from each other because that's the way it worked with the
[21:58] thumbnail but you can also just move them and overlap them now which in some cases just makes
[22:04] more sense and just kind of place them the way that you want so for example this one we want
[22:09] is to intersect with that other object if I wanted this arm shape to be a bit more tapered so for
[22:15] example I wanted to have kind of like this kind of tapered shape one thing I can do is I can select
[22:21] this bottom face here and we can just make sure we are looking at it from the side and then enable
[22:27] proportional editing here and for example set it to linear and then just scale it with s and make
[22:35] sure that the falloff is around the whole object so increase the radius of the falloff with the
[22:40] middle mouse button and then just yeah move left or right to scale so in this case move to the left
[22:47] and it looks something like this and we can adjust the shape here by selecting this face and then
[22:53] maybe scaling it up from there and I will just decrease the radius suddenly and so that's another
[22:58] way to control the shapes as well and you can also set proportional editing to smooth and it can be
[23:04] very helpful to quickly adjust some shapes so just adjust the falloff by scrolling the mouse
[23:09] up and down that way you can really control how you're affecting the shape and if I select one
[23:14] of these faces which are in the middle so if I move it then I'm breaking the mirroring what you
[23:20] can do is you can lock a specific axis so in this case I don't want to move it on the x axis what I
[23:26] can do is I can press shift and x and now I can only move it on the y and the z axis so shift and
[23:34] then the axis that you don't want to affect this case the x axis and also here with the feet I also
[23:40] want to taper it slightly so like this and increase the thickness and for example here I want to have
[23:47] a little bit more control over this shape but there's not enough geometry so I can always just press
[23:51] control r add a loop if you don't want to remember the keyboard shortcut control r let me just do that
[23:57] one you can use the loop cut tool here so just left click and then enter to confirm and then
[24:04] go back to the select box tool and so yeah now I have a bit more control over the shapes and of
[24:10] course now it's from the side not very interesting because it's a very stiff pose and it's interesting
[24:17] if we can pose it and to do that what we can do is we can set here the transform pivot point to
[24:24] 3d cursor so it's set to 3d cursor and then just select the things that we want to pose
[24:30] and then shift and right click to place the 3d cursor so now I've placed the 3d cursor there
[24:36] and I would do all these objects selected I can just rotate it along that position of that 3d cursor
[24:42] and I can do that again here so I place the 3d cursor here with shift and right click so now
[24:46] it's there and so now I can move this like this and I can just repeat that so shift and right
[24:53] click and put the 3d cursor there and then I can rotate this and maybe just adjust this one more time
[25:00] so that's already a slightly more interesting pose and when doing stuff like that it's best to always
[25:06] set the transform pivot point back to median point which is the default otherwise you might get
[25:11] confused later about why things aren't rotating the way you expect and also I would recommend to
[25:17] reset the position of the 3d cursor with shift s and cursor to world origin that way when you create
[25:24] a new object it will be in the center of the world so one more thing that we can do with this setup
[25:29] with these two modifiers is we can start extruding some stuff and so again you need to be in edit mode
[25:36] and it's best to be with face selection modes and then what we can do is for example we can
[25:41] select one or two edges and then just press E to extrude and then you can extrude it like this
[25:48] or if you don't want to remember the E keyboard shortcut although it's a very common one
[25:53] you can click here on extrude and then just use this gizmo but for that you have to have the gizmo
[25:59] enabled and of course we can scale down extrusion tool kinds of stuff with it personally I like to
[26:05] just use the keyboard shortcut E it's not all that difficult to remember so just E and extrude
[26:12] and I think I will scale this shape up slightly and I'm just going to turn off proportional
[26:18] editing because I don't want to use it for this so selecting these edges and just moving them
[26:23] slightly just to adjust the shape and again because the geometry is still so simple and it's all
[26:29] quad based it's very easy to adjust the shape and it stays nice and smooth or maybe something like this
[26:37] now let's say I'm not happy with this extrusion I can just select it and press control plus to
[26:42] increase the selection and then just X to delete so delete faces and then we're going to alt and
[26:49] left click in edge selection mode on this and press control f and g to fill it so let me show
[26:58] you how you can do that if you don't want to remember all those keyboard shortcuts so just
[27:01] select these two faces go to select and then more and then go to mesh delete faces and then in edge
[27:10] selection mode alt and left click on this loop and then go to face and grid fill and instead of
[27:18] an extrusion what you can also do is select some faces and press i to inset and then just press
[27:24] e to extrude inwards so you can also create this kind of hole if you want and guys please
[27:29] don't forget to save sometimes because I get messages sometimes on youtube where people
[27:34] say that they lost three hours of work because something crashed but things will crash sometimes
[27:40] and if you don't save for three hours that's really irresponsible so definitely save every
[27:45] half hour or something and set the auto save up for every 10 minutes and here I just want to create
[27:52] some extrusion and I'm going to press control i to inset I don't want it to inset like this
[27:58] and so what I'm going to do is press B and that will respect the boundary of the mirror modifier
[28:03] so again B to turn on boundary and if you forget that keyboard shortcut just look at the bottom row
[28:09] of the screen and you will see some helpful tips there and I'm going to press G and Y to move this
[28:15] like that and I'm just going to adjust this shape slightly
[28:22] and to minimize these gaps between all these objects I'm just going to select them all in
[28:26] object modes and then go to edit mode and just alt a to deselect anything and then I'll turn on
[28:32] x-ray mode so I can see and select through all of these objects and then I'm just going to move
[28:37] them with proportional editing enabled but to make sure that they are not all affected by the
[28:42] proportional editing I'm just going to go into this menu and choose connected only and select that
[28:48] and that way I can just move the vertices on the individual objects and I'm just sort of overlapping
[28:54] them all and sometimes you do have to make sure that you only have one object selected
[28:59] so that you can just move only one vertex otherwise sometimes you will select everything
[29:04] and so instead of just clicking on a vertex I'm just dragging a box and that way I am selecting
[29:09] all the way to the other side of the object as well so I'm selecting the vertices on the other
[29:14] side as well and here I'm just pressing G and Z to move this down on the z-axis only and G and Z
[29:21] to move it up and then I'll just move these and in some cases like for example here there's just a
[29:28] big gap between these arms and that's just because I didn't draw anything there in the design and one
[29:33] thing you can do to solve that real quick is just select one of these objects and then just shift
[29:38] D to duplicate them and then you can just kind of try to rearrange them maybe make them fit like
[29:44] this for example and let's see from the side and just press R twice if you want to have free rotation
[29:52] and then of course we can still adjust this object so with proportional editing enabled we can still
[29:58] untune the shape so we can make it fit better in this location and let's see we can also just
[30:03] select these two faces and press Ctrl and plus and then just delete them so X and faces and then in
[30:11] edge selection mode just Alt and left click on this and press Ctrl F and then choose grid fill
[30:18] or alternatively go to face and grid fill just so that that is filled again and in this case I want
[30:24] this shape to be a bit rounder and what I'm going to do is just add a loop here so Ctrl and R and
[30:30] with this loop still selected the way we can scale that up is either by pressing S and then you
[30:36] will get something like this or if I undo that real quick you can do Alt S and Alt S generally
[30:42] is better in this kind of case because it scales along the normal direction and then I'm going to
[30:48] go to vertex selection mode and then press Ctrl and I to invert the selection so now I have these
[30:54] selected and then I'm going to right click and choose smooth vertices and I'm pressing shift R
[31:00] which just repeats the last action and then you get this kind of thing so now I've made this shape
[31:06] a bit rounder and in fact if I press A to select everything and then right click and choose smooth
[31:11] vertices then it becomes even smoother and then I can press Alt S and inflate it again like this
[31:19] and it gives us this kind of shape and I would like to have some kind of spherical socket here so
[31:23] what we can do is shift and right click to place the 3D cursor there and then we can go to add mesh
[31:29] and cube and let's create an enormous cube so let's scale that down and then with this cube
[31:35] selected we'll hold shift and select any other object and then Ctrl L and copy modifiers so that
[31:42] this has all those modifiers now as well and just set it to shade smooth and maybe let's scale this
[31:49] and put over here and now we've created this kind of ball joint which is the simplest kind
[31:54] of joint for a Mac object and let's change the shape of this thing let's add a loop so that we can
[32:02] use these vertices here to just the shape I guess
[32:09] and I will put the cursor back at the world origin. Once you have a nice simple base mesh
[32:15] you can start to invent more detail there are a few directions that you can go in either
[32:20] polygonal modeling or using booleans or sculpting in this case I decided to practice my sculpting
[32:26] techniques but then to keep things simple when sculpting I mainly use the grab brush,
[32:31] scrape brush and the smooth brush using the grab brush you can quickly adjust the shape
[32:38] and clay strips helps to refine the shape. I have the brushes that I use most in my quick favorites
[32:45] menu that way I can work in full screen or on a tablet screen. The draw brush is also useful
[32:51] for quickly drawing where you may want to separate an object or to add a rough panel cut. By holding
[32:57] Ctrl you can invert the brush so the clay strips brush then removes volume for example. Often you
[33:03] can get really far with just the grab brush. These objects all have a multi-res modifier on them
[33:11] and you can change their shape quite a lot even though the underlying base remains unchanged.
[33:16] It's fun to use the scrape brush to flatten areas like this. If you get this kind of glitch
[33:23] that's because for whatever reason the auto masking option is enabled that can be quite
[33:27] frustrating if you don't know what's causing it.
[33:33] Another useful brush is the inflate brush to quickly add some volume which you can then
[33:37] refine with the scrape brush. Sometimes it's good to inflate the volume of a mesh so that you have
[33:42] something to remove in order to create more interesting shapes. So inflating things and
[33:48] then using the scrape brush can work really well. If you're not happy with the results you can always
[33:53] use the smooth brush to smooth it out and then try again. Every now and then I practice modeling
[33:58] some greeble objects. I mark them as assets so that later I can always drag and drop them on the model.
[34:07] You can also use alpha brushes to add detail or to integrate the greeble objects better.
[34:17] It can be challenging to integrate those greebles sometimes so it can be easier to just
[34:22] redepologize a sculpted part with some normal polygonal modeling. That way you have more precise
[34:26] control over the shape. With the polyline face set tool you can draw a face set in shapes like this
[34:35] and then you can use that face set to create a mask and use the mask to separate the area into a new mesh.
[34:41] Here you can see the big difference between the base mesh and what I sculpted which is stored in
[34:46] the multires modifier. By clicking on apply base the base mesh shape is adjusted to more closely
[34:52] resemble what you've sculpted. The technique that I like a lot and that I developed for my
[34:56] hard service sculpting course is using tiling displacement maps to quickly experiment with
[35:01] adding hard service details. It's really fun and creative technique and it honestly feels a bit
[35:05] like cheating. Once you've set up the modifiers with the displacement for one object you can
[35:10] just copy the modifiers stack to other objects. Here you again see how different the base mesh
[35:17] and the multires result can be. I applied the multires modifier with a lower solution so that
[35:22] I have a good base mesh for the tiling displacement to do its thing on. Of course this all explained
[35:28] in much more detail in my video course and the files for that are included there as well.
[35:32] Here I'm using a different tiling displacement map this one with cables. By controlling the
[35:37] displacement with empties you can quickly experiment. I wasn't happy with the shoulders so I remeshed
[35:43] them with the blenders built in quad remesh option to get a simple quad base mesh. I then tried some
[35:47] more tiling displacement on it until I found something that I liked and suddenly it reminds me
[35:52] of the metroid games. After adding the tiling displacement I used some alpha brushes for smaller
[35:58] details. Finally I add some materials for my drag and drop mech materials course to create a quick
[36:04] render. The good thing about these materials is you don't need UV maps so you can just drag and
[36:08] drop them on this kind of messy geometry and they'll just work. That's really fun when you've
[36:12] worked on sculpting something and you just want to create some quick renders. So at the beginning
[36:17] I promised to show you an alternative workflow to the trace image to grease pencil workflow and
[36:22] for that I'm just going to use this default cube. This is a cube effect and it has the symbol and
[36:28] the catmoclark modifier so it's the double subdiff modifier technique and yeah but the first one
[36:34] you can control how square it is and the second one it doesn't really need two levels but you can
[36:39] control the smoothness and basically just what you can do is just shift D and duplicate it and
[36:45] let's go to x-ray mode either by clicking on this or with alt Z you can toggle x-ray mode on then
[36:51] of course you see the original mesh but if we click on the on cage button here it will follow the
[36:55] subdivided mesh and then yeah we can just start adjusting the shape and this is basically what
[37:01] is called box modeling and let me just turn this up one level and we can maybe adjust it a bit more
[37:08] so by using x-ray mode we can select everything all the way to the other side and sometimes you
[37:13] just have to press ctrl r and then just add another loop and I seem to have turned off optimal
[37:20] display if you enable optimal display then you just see less geometry which it can be confusing if
[37:26] you see all those additional subdefirer loops so just enable this and then yeah we can just adjust
[37:32] the shape and let's add another loop and the more loops you have the more you can of course adjust
[37:37] the shape but of course the more loops you have also the more difficult it will be to adjust the
[37:42] shape so so it's best to only add the loops that you really need now I can adjust these like here
[37:49] yeah by adding another level here I can make it even more precise and it's just a matter of
[37:54] just dragging things to match the shape and that gives us this nice quad topology and of course
[38:00] we can add loops to that we can start adding detail to it and so on so yeah as you can see it's also
[38:07] very easy and very quick to work this way you can have very nice quad topology very quickly
[38:13] and it's up to you to decide which technique is better for you or which is faster the biggest
[38:22] factor in deciding which of these two techniques you will use is the underlying sketch so let's
[38:27] say I created a really messy quick sketch with a pencil on a napkin or whatever and it's just going
[38:34] to be too rough for trace image to grace pencil to turn it into a nice clean mesh and in that case
[38:41] I would recommend using this technique with just this cube with these two modifiers and just
[38:46] duplicating it and then adjusting it in x-ray mode just box modeling in other words and if you are
[38:52] creating a sketch in advance with the express purpose of using trace image to grace pencil
[38:57] then you know that you can create these white lines between everything and then it will work
[39:01] very easily and in the end I think both techniques will take about the same amount of time so it's
[39:06] really up to you which technique you prefer personally I probably would go for this technique
[39:13] instead because I like to just draw on paper I actually prefer to draw on paper than on the
[39:19] computer so in my case it's much more likely that I just have some sketches that I did with pencil on
[39:24] paper and in that case this technique will be better this was just a quick overview of a possible
[39:30] hard service concept in workflow if you're interested in this kind of thing you should know
[39:34] that there is a 60 dollar discount on all my hard service courses and book if you buy them all
[39:38] together in a big bundle you can find the link to that in the description of this video thanks for
[39:43] watching all the way to the end



---

## Captured Frames

- [1:04] tutorials/frames/image-to-3d-model-workflow-in-blender/frame_000.jpg
- [2:06] tutorials/frames/image-to-3d-model-workflow-in-blender/frame_001.jpg
- [4:06] tutorials/frames/image-to-3d-model-workflow-in-blender/frame_002.jpg
- [8:53] tutorials/frames/image-to-3d-model-workflow-in-blender/frame_003.jpg
- [13:00] tutorials/frames/image-to-3d-model-workflow-in-blender/frame_004.jpg
- [24:22] tutorials/frames/image-to-3d-model-workflow-in-blender/frame_005.jpg
- [34:10] tutorials/frames/image-to-3d-model-workflow-in-blender/frame_006.jpg
- [37:10] tutorials/frames/image-to-3d-model-workflow-in-blender/frame_007.jpg

---

## Structured Notes

### Core Technique
Two competing paths from a black-and-white concept sketch to a hard-surface (mech/robot) blockout — (1) Trace Image to Grease Pencil → Mesh, converting closed line-art islands directly into flat mesh shapes, cleaned up into quad topology and thickened with mirrored Solidify + double-Subdivision modifiers; (2) classic box-modeling a cube (same double-Subdivision technique) freehand, useful when the source sketch is too messy for clean auto-tracing — followed by a full hard-surface detailing pass (sculpting, multires, tiling displacement maps, greebles, alpha brushes).

### Summary
Frame 000 shows the very first step: an empty Front Orthographic viewport, about to receive the dropped-in black-and-white concept sketch. Frame 001 shows the payoff of Object > Convert > Trace Image to Grease Pencil: a symmetrical mech silhouette rendered as a dense orange Grease Pencil line-art outline, with every design island (torso, shoulders, arms) traced as closed shapes. Frame 002 shows the Mesh Cleanup submenu open (Limited Dissolve highlighted) over the same mech shape now converted to a solid tan-shaded mesh — the step that removes excess trace-generated vertices while preserving the silhouette. Frame 003 shows one shoulder/head piece isolated and selected, its Mirror modifier open in the sidebar (Axis X, Bisect, Flip, Merge, Clipping) — confirming the per-island Mirror modifier setup used throughout. Frame 004 shows the model after Solidify has been applied for thickness: a shaded, beveled-looking mech torso with the Solidify modifier's Even Thickness/Rim options visible in the sidebar, one arm piece selected and highlighted orange. Frame 005 shows the two-Subdivision-modifier stack applied to the whole model (Catmull-Clark listed twice in the modifier stack, "Optimal Display" toggled) with a dropdown menu open showing Subdivide Edges / Un-Subdivide / Adaptive options — the smoothing pass that turns the flat quad blockout into a rounded hard-surface shape. Frame 006 shows a later hard-surface-detailing stage: a smooth helmet/head shape with a Quad Remesher panel open (Quad Count, Quad Size Settings, Adapt Quad Count, Symmetrize) plus an Asset Browser strip of premade greeble objects along the bottom — the retopologize-after-sculpting and greeble-library workflow. Frame 007 shows an X-ray wireframe view of the full mech with one shoulder piece isolated and being reshaped (G to grab), the flat black silhouette pieces visible underneath — illustrating the "close remaining gaps between islands" cleanup pass late in blockout.

### Key Steps
**Path A — Trace Image to Grease Pencil (best when the sketch was drawn *for* this workflow, e.g. digitally with clean white gaps between shapes):**
1. In Front Orthographic view, drop in a black-and-white concept sketch, Alt+G to center it; ensure every design region is a fully closed island separated by visible white gaps, since that's what lets Blender split it into separate mesh islands.
2. Select the image, Object > Convert > Trace Image to Grease Pencil (default settings); hide the original image empty afterward.
3. Object > Convert > Mesh — in Blender 4.3.2 this goes directly from Grease Pencil to mesh in one step (older versions required an intermediate Convert to Path first); note the object stays labeled with its Grease-Pencil-derived name in the Outliner even though it's now a real mesh.
4. **Version matters a lot here:** the same source image converted much more cleanly (fewer vertices, all faces fillable with F) in Blender 4.3.2 than in Blender 4.0.2, where filling failed on most islands — always use the latest Blender release for this technique.
5. Hover over an island and press L to select it (or A to select all islands at once), then F to fill each into a flat mesh face/plane.
6. **Topology cleanup:** select all, Mesh Cleanup > Limited Dissolve (5° default works well) to remove most of the excess trace-vertices while keeping the silhouette; P > Separate by Loose Parts to split each island into its own object (do this *before* Merge by Distance so it only merges within, never across, islands); select all objects, Tab into Edit Mode (editing across multiple objects at once is supported), M > Merge by Distance (start conservative, increase gradually to simplify — author settled around 0.02m for this sketch); Mesh Cleanup > Delete Loose to remove stray unconnected vertices.
7. **Force all-quad topology (critical before adding thickness):** use the Knife tool (K) to manually cut each remaining n-gon into quads — click vertex, right-click to reposition the knife without cutting, click again to continue, Enter to confirm; fix leftover triangles by cutting them off and double-G sliding a vertex to merge it away; dissolve (Ctrl+X) any vertex that isn't structurally needed, aiming for the simplest possible quad mesh — extra detail can always be added later, but a clean starting topology is much harder to fix after the fact. **Verify** with Select Similar (Shift+G) > Polygon Sides (Compare: Equal) on a known quad — any faces that stay unselected are hidden non-quads (often caused by an invisible extra vertex) and need further knife/dissolve work.
8. **Center-line prep for mirroring:** select the vertices along the model's symmetry line, scale them to zero on X (S, X, 0, Enter) with the 3D cursor at world origin and Transform Pivot Point set to 3D Cursor (so they snap exactly to the centerline, not just visually close) — remember to set the pivot point back to Median afterward.
9. **Thickness and mirroring at scale:** cut each island's flat mesh in half with the Knife tool and delete the unwanted half, add a Mirror modifier to one, then select all objects (Ctrl+I to invert selection after selecting the source, Shift-click to add it back) and Ctrl+L > Copy Modifiers to propagate the Mirror modifier to every object at once; add Solidify with Offset set to 0 (grows thickness from the center rather than only outward) — apply Solidify-only across all selected objects at once via Alt+click on the Apply button (or, if "Emulate 3 Button Mouse" is enabled in Preferences, use Ctrl+A > Visual Geometry to Mesh per-object and manually re-add the Mirror modifier afterward instead, since Alt+Apply won't work with that preference on).
10. **Double-Subdivision smoothing (same technique as the "double subdivision modifier" beginner method):** add two Subdivision Surface modifiers — first set to Simple (adds edge loops without smoothing, letting you dial in how "square" vs. rounded the result is), second set to Catmull-Clark (smooths); raising the Simple modifier's levels keeps more of the blocky/sharp character, while relying more on Catmull-Clark alone gives a rounder result — combine them to balance shape-preservation against smoothness; propagate this modifier stack to all objects via the same Ctrl+I / Shift-click / Ctrl+L Copy Modifiers trick, then Shade Smooth all.
11. **Fixing visible creases:** an ugly crease down the mirror seam usually means leftover interior faces are still present along the centerline — go to Front Orthographic + X-Ray, Face select mode, select and delete just those inner faces (X > Faces) to resolve it.
12. **Reshaping with the two-modifier system:** since the topology is so simple, small edits move a lot of shape — use Face select + Ctrl-click to select a face range, S,Y or S,X to reshape, or enable Gizmos for click-drag scaling/moving; enable the **On Cage** button so Edit Mode previews the smoothed result directly instead of the blocky cage, making shape edits far more predictable; use Proportional Editing (O, adjustable falloff via scroll wheel, Linear or Smooth falloff type, "Connected Only" to avoid affecting unrelated overlapping objects) for organic tapering; lock an axis during a move with Shift+<axis> (e.g. Shift+X) to preserve mirror-plane alignment.
13. **Origins and mirror pivots:** setting Object > Set Origin > Origin to Geometry breaks each object's own Mirror modifier (since Mirror uses the object's own origin by default unless a Mirror Object is set) — fix by adding an Empty at the world origin, sizing it down, and assigning it as every object's Mirror Object (again via Ctrl+L Copy Modifiers) so origins can move freely for posing/rotation without breaking symmetry; reset a moved 3D cursor with Shift+S > Cursor to World Origin; for local-axis scaling/rotation, switch Transform Orientation to Local so gizmo handles point the right way, then switch back to Global afterward.
14. **Posing:** set Transform Pivot Point to 3D Cursor, Shift+right-click to place the cursor at a joint, then rotate connected geometry around that point — repeat per joint for a full pose; reset Pivot Point back to Median when done to avoid later confusion.
15. **Adding small extra shapes:** Shift+right-click to place the cursor, add a Cube (or other primitive), scale it down, Ctrl+L > Copy Modifiers from an existing piece to inherit the Mirror/Solidify/Subdivision stack instantly (e.g. building a simple ball-joint socket this way).
16. **Filling/patching gaps between separate island objects:** select the faces bordering a gap, Ctrl+Numpad+ to grow selection, X > Faces to delete, then Alt-click an edge loop and Ctrl+F > Grid Fill (or Face > Grid Fill) to patch it cleanly; alternatively Inset (I) + Extrude (E) inward to punch a deliberate hole instead of filling solid.
17. **Rounding shapes further:** add a loop (Ctrl+R), Alt+S (scale along normal) to inflate it, invert the selection (Ctrl+I) and right-click > Smooth Vertices (Shift+R repeats the last action) for extra roundness — combine Smooth Vertices + Alt+S inflate iteratively for a more organic, less blocky result on specific parts (e.g. a rounded joint socket).

**Hard-surface detailing pass (both paths converge here once a clean blockout exists):**
18. From a simple base mesh, add detail via polygonal modeling, booleans, or sculpting — the author demonstrates sculpting: mainly the Grab brush (fast reshaping), Clay Strips (refine volume, Ctrl-invert to remove volume instead of add), Scrape (flatten areas — a "glitch" flattening artifact is usually caused by Auto Masking being accidentally enabled), Inflate (add volume to later carve away with Scrape), and Smooth (undo-via-smoothing when unhappy with a result) — objects carry a Multiresolution modifier so heavy shape changes stay non-destructive to the low-poly base.
19. **Greebles and alpha brushes:** practice modeling small greeble objects and mark them as Assets so they can be dragged straight from the Asset Browser onto any model; alpha brushes help both add fine detail and visually integrate greebles into the sculpt.
20. **Redoing a sculpted region as clean polygons:** the Polyline Face Set tool draws an arbitrary-shaped face set, which becomes a mask, which can separate that region into its own mesh for precise manual retopology when sculpted geometry is too imprecise to integrate cleanly.
21. **Apply Base:** clicking "Apply Base" on the Multiresolution modifier bakes the sculpted high-res shape down into the low-poly base mesh's actual vertex positions.
22. **Tiling displacement maps (the author's signature hard-surface technique from their paid course):** apply a lower-resolution Multiresolution level as a clean base, then drive additional surface detail via tiling displacement-map modifiers — once dialed in on one object, the whole modifier stack can be copied to other objects (Ctrl+L) for consistent detailing; displacement position/scale can be controlled live via Empties for fast experimentation; Blender's built-in Quad Remesh option is useful to flatten a sculpted region back into a clean quad base before applying more tiling displacement.
23. **Finishing:** apply UV-less drag-and-drop mech materials (from the author's paid materials course) directly onto the messy sculpted/displaced geometry for a fast render, since these materials don't require UV unwrapping.

**Path B — Box modeling from a cube (best for messy/napkin sketches too rough to auto-trace cleanly):**
24. Start from a default cube with the same double-Subdivision-modifier stack (Simple below, Catmull-Clark above); Shift+D duplicate for a new part, enable X-Ray (Alt+Z) and On Cage to edit the smoothed result directly; this is standard box-modeling — Ctrl+R to add loops only where truly needed (too many loops makes the shape harder, not easier, to adjust), enable Optimal Display to avoid confusing extra subdivision-generated geometry in the viewport. The author states both this and the trace-based Path A take roughly the same total time — the deciding factor is simply how clean the source sketch is, and personal preference for hand-drawn paper sketches over digital ones.

### Nodes / Settings
- **Trace pipeline:** Object > Convert > Trace Image to Grease Pencil, Object > Convert > Mesh (single-step in Blender 4.3.2+), Mesh Cleanup (Limited Dissolve, Delete Loose, Merge by Distance), P > Separate by Loose Parts, Select Similar > Polygon Sides (Shift+G, quad verification).
- **Modifiers:** Mirror (Axis, Mirror Object via Empty, Bisect/Merge/Clipping), Solidify (Offset = 0 for centered thickness), Subdivision Surface ×2 (Simple then Catmull-Clark, On Cage editing, Optimal Display), Multiresolution (sculpt-safe base), tiling-displacement modifier stack (author's signature technique), Quad Remesher (retopology after sculpting).
- **Modeling tools:** Knife (K) for manual quad conversion, Ctrl+X (dissolve), Grid Fill (Ctrl+F or Face menu), Inset (I) + Extrude (E), Ctrl+R (loop cut), Alt+S (scale along normal), Proportional Editing (O, Connected Only, Linear/Smooth falloff), Ctrl+L (Copy Modifiers across selection), Object > Set Origin > Origin to Geometry, Shift+S (Cursor to World Origin / Cursor to Selected).
- **Sculpt Mode:** Grab, Clay Strips (Ctrl to invert), Scrape, Inflate, Smooth brushes; Polyline Face Set tool; Apply Base (Multiresolution).
- **Assets:** Asset Browser for greeble objects, drag-and-drop UV-less mech materials.
- **UI/workflow:** Local Transform Orientation for correctly-aligned gizmo scaling/rotation, Transform Pivot Point (3D Cursor for posing, Median as default), regular manual saves + Auto Save configured every ~10 minutes.

### Difficulty
Intermediate to Advanced (spans beginner-friendly image tracing through advanced sculpting/tiling-displacement hard-surface detailing)

### Blender Version
Blender 4.3.2 — explicitly named; the video explicitly compares trace-to-mesh behavior against Blender 4.0.2 and recommends always using the latest release for this workflow.

### Tags
modelling, organic, procedural, displacement, intermediate, advanced

---

## Related Tutorials
- [For Beginners: Easiest Modeling Technique (long version)](for-beginners-easiest-modeling-technique-long-version.md) — shares modelling, organic, procedural, intermediate; both use the identical double-Subdivision-modifier (Simple + Catmull-Clark, On Cage editing) blockout technique as their box-modeling path.
- [6 Panel Cut Tips - Blender Secrets](6-panel-cut-tips---blender-secrets.md) — shares procedural, intermediate, advanced; that tutorial's Instances on Elements greeble-scattering and normal-map baking are close cousins of this video's greeble-library and Quad Remesh detailing steps.
