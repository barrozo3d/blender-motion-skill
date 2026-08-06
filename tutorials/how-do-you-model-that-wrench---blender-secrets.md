---
title: How do you model that? Wrench - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=S9WVxHp1Sc0
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — on-cage Subdivision editing, LoopTools, F2, Round Cube (Extra Objects) and Extra Objects add-ons, consistent with Blender 3.x-5.x"
tags: [modelling, procedural, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/how-do-you-model-that-wrench---blender-secrets/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How do you model that? Wrench - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=S9WVxHp1Sc0)
**Author:** Blender Secrets
**Duration:** 28m54s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Alright, so this person asked me how to model these pliers, and that's an interesting shape
[0:05] because it goes from kind of a sharp angled metal tool to this kind of smooth round shape,
[0:12] and there's also a nice kind of boolean cut on this side. So let's see if we can figure out
[0:16] how to make that. And apologies for the blatant self-advertisement there, but I have to pay the
[0:20] bills. So I'm just dragging and dropping some reference image here and just repositioning it,
[0:26] and then we can lower the opacity a bit just to make it easier to see the mesh later,
[0:31] and then we can turn off the selectability of that reference image. And so now we can add a plane,
[0:36] so Shift A, Mesh Plane, and then in Edit Mode, let's turn on X-Ray, then we can
[0:42] skid it down and start to adjust the shape. So fortunately the reference image is almost an
[0:48] orthographic view. Of course ideally you would search a real top or a side view, but in this case
[0:54] this is the only image ahead of this, and the point is more to show how to model the shapes,
[0:59] not to make an exact replica. So I'm just extruding and adjusting vertices, and the lower
[1:05] the vertex count, you know, the faster it goes, and the easier it is to adjust everything. So I
[1:11] always recommend just working from simple shapes to more advanced. Don't start with too much geometry,
[1:17] and we can just extrude this all the way over here, and then Ctrl R and scroll the mouse whole up
[1:23] to add some more loops. So that's the basic shape, and then we can add a Subdiv modifier. So press
[1:28] Ctrl 2 to add two levels of subdivision, and let's Ctrl R and add a few more loops in these places
[1:34] where we need to have sharper corners. By disabling the modifier in Edit Mode, it's easier to add
[1:42] loops and then check in Object Mode what we get. And here I'm just adjusting these corners here.
[1:47] And of course with subdivision modeling, the closer the vertices or edges are together,
[1:53] the sharper those places will be. I was actually following the photograph here, but later I will
[1:59] redo this handle part. And here with on cage enabled, we can fine tune the shape just by
[2:06] pulling some vertices from the top orthographic view. As you can see, we're getting to the shape
[2:11] of the photograph really quick. And here I'm just adding another loop with Ctrl R, and that loop
[2:16] is going to keep the corners sharp once it has some thickness. And you can press E for even,
[2:23] and then you can slide it to match the curvature of the other edge. That way the distance of that
[2:30] support loop to the corner is more even. And here I'm just really fine tuning the closeness of
[2:38] those vertices to make it even sharper. And I'm adding another loop to support those support
[2:43] loops. So sometimes if you add, uh, yeah, a vertices really close to other vertices, and then
[2:48] there's just nothing next to it that can cause some topology stretching. So sometimes it's good to
[2:54] add a bit more geometry next to it. And here I'm also just adding a bit more geometry. And I'm adding
[2:59] a loop in the middle here to make the distribution of the geometry a bit more even. And here I'm just
[3:04] sort of fine tuning. You can slide for just with double G, so press G twice, then you can
[3:09] slide vertices along the edges that are there, and just making some small adjustments. I think
[3:14] there's probably not enough geometry here, so we can select this loop, Ctrl B to bevel, and then we
[3:21] can set it to percent to get a more organic distribution of those new edges. And then we can
[3:27] just select vertices and fine tune them. And it's important to check the subdivision result in
[3:32] object mode so that you can see if you need to tweak it some more. So I'm just making a lot of
[3:37] fine adjustments. So this is the shape so far. And we're just going to add a solidify modifier,
[3:43] although I could have also just extruded that. And then just, yeah, we can just apply that solidify
[3:48] modifier with Ctrl A. And as you can see, we need to add a little bit more geometry, otherwise it
[3:52] will come very smooth. So you can just add a loop in the middle with Ctrl R and then Ctrl B to bevel
[3:57] it and scroll the mouse wheel up if you want to add another loop in the middle. And you can
[4:01] shade it smooth. So that's the basic shape. And just having a quick look at the reference image.
[4:07] So as you can see, there's kind of a crease also in the middle of the thick part. So there's this
[4:11] edge loop in the middle. So let me just remove those support loops and select this one and Alt S
[4:17] to scale it up. That gives it a bit more thickness in the middle. So it has thickness in the middle
[4:22] and it also has a sharper ridge. So it has a few supporting edge loops in the middle as well. So
[4:29] let me just undo that and just deselect a few of these loops here. So I'm just holding Shift
[4:36] and clicking them so to deselect them, then we can scale it up again. We also need to deselect some
[4:41] stuff at the end there and then Alt S to scale it up. That creates some thickness and we can try
[4:48] using proportional editing for that, but it's probably not a good idea. So best to turn it off
[4:54] and so Alt S to scale it up. Alt S scales along normal. So it's a little bit different than
[4:59] just scaling with S and then just manually scaling up these final vertices there. So that kind of
[5:06] tapers off that middle thickness there and even a little bit of thickness there at the end maybe.
[5:11] So very subtle and then we need to have a look and see what the shape is so far. And let's check
[5:16] the reference one more time and yeah it has this nice tapering from sharp edges to like really round.
[5:23] So the handle where you're holding it with your hand really needs to be perfectly round. So let me
[5:27] just go to X-ray view and just delete those vertices and then just redo this part because
[5:34] I already added that kind of curvature but that's not really ideal. And yeah let's see what happens
[5:40] if we use grid fill and grid fill sometimes immediately gives a good result but if it doesn't
[5:46] you can always just select the opposite edges and then do it again and then it will fill it more
[5:51] perfectly. And with loop tools flatten we can make it flat and then rotate it a bit and let's
[5:57] move that a bit and add some loops again to it with control and R. So now as you can see that
[6:02] handle is just kind of square all the way until the end there and if we select that middle edge
[6:08] loop we can add some more loops that control the sharpness of the corners, control B and then move
[6:15] the mouse and that's a good look. So it really has this sharp crease in the middle as well where it
[6:20] kind of tapers. So let's just manually with control R add those loops over the corners there. So
[6:26] control R and move it and then we can select that middle loop here with alt left click and just
[6:32] bevel that with control B and then we can get this nice crease that you also see in the reference
[6:37] image. And yeah from the top actually here this part doesn't look very good so we just need to go
[6:41] into X-ray view and Y-frame and just select some vertices and just visually adjust it until it looks
[6:48] good. And so yeah that already starts to look a bit better and also here we need to adjust it a
[6:53] bit so that looks a lot better. Okay so this is what it looks like now in solid view and maybe a
[6:58] little bit more fine tuning and that part still bothers me a little bit. Okay now it's good enough.
[7:03] So let's have a look at how we can get that part where it goes from sharp to round and smooth. So
[7:10] let's have a look. So it's a smooth transition there and that's actually very easy we can just use
[7:15] the loop tools extension. So you need to enable the loop tools extension in preferences and let's
[7:20] actually move this reference image up so we can see it better while we also work on the geometry
[7:26] and in fact we can increase the opacity a bit. So here we can also fine tune it in X-ray view
[7:31] just to make that part a bit thicker because it was already very thin there. I'm just gonna select
[7:36] this and then just delete those vertices. That way it's easier to manipulate this final part here.
[7:43] Just double G sliding it and pressing C so I can slide it where there are no edges just to extend
[7:48] the length of the handle a bit and then grid filling it again and adding any support loop there
[7:53] to make it sharp. And so you can see the kind of geometric shape that it has now but it needs to be
[7:59] perfectly circular. Actually I want to just delete that cap and let's see what happens if we use a
[8:05] loop tools circle and we need to set it to 100%. As you can see now it's made that part perfectly
[8:11] circular and then we can grid fill it again and let's press I to inset and then just scale down
[8:16] the inset. And we just continue using the loop tools extension with the circle tool and let's
[8:21] add a loop there to make that corner sharp and then we just go down the handle and do all the
[8:28] parts that need to become circular. I'm just pressing shift R here to repeat the last command
[8:33] all the way until there where it needs to transition from round to sharp and there we can
[8:40] start to fine tune it. So just alt and left click on a loop and use the loop tools command
[8:46] and then just reduce the amount of circular influence and this might take a little bit
[8:52] of experimentation. You might need to go back and undo a few times and yeah until it looks good.
[8:58] One thing you can do is you can open another window and turn off overlays and then it looks
[9:02] like you're in object mode even when you're in edit mode and then if we use a math cap we can
[9:06] have a look at what it looks like with some shading especially if we turn on on cage on the
[9:11] sub-diff modifier and then we can really start fine-tuning this transition from sharp to circular.
[9:18] So as you can see that works quite well but we might have to redo it and spread out the transition
[9:24] a bit more because now it's quite sudden I think. So I'm just going to undo that a few times and
[9:29] let's try again. So let's start with 80% something like that and actually let me just undo that a
[9:36] few more times and let's split it up into five different sections. So it starts with 100% and
[9:44] then 80% and then 60% 40 and so on. So here this one is 80% ish doesn't have to be perfectly 80
[9:52] and we just reduce it by 20% each time so this one will be 60 so 60% and then this one loop
[10:00] till circle we set it to 40% so something like this and then this one we can set it to 20%
[10:07] something like that and then we get a very nice transition from sharp to circular as you can see.
[10:13] So that might seem like the difficult part of this model but actually I would say that's the easy
[10:17] part. So we can close that window again and continue working on this. Let's actually add the
[10:23] math cap here as well and let's quickly erase that annotation. So before we add those bits at the end
[10:29] let's duplicate this and hide the original and then we can flip this one around to its r180 and
[10:36] enter so r180 on the numpad and enter and just move it a bit on the y-axis and I'm just going to add
[10:42] a cube that we can use as a cutter object and I'm just holding shift and selecting the original
[10:48] and then control and minus on the numpad and then we can use this cube as a cutter object. So I'm
[10:53] just rotating it on the local y-axis and then moving it up on the z-axis adding a loop so I
[10:59] can create a kind of a curve shape. Let's add a couple more loops and move those down and
[11:04] slowly create this kind of curve shape on the cutter object and you can see I'm only worrying
[11:09] about this part where you have this final part of the cutter not all the way to the front of the
[11:16] the tool because we can do that manually later and I just need to fine tune until where the cutter
[11:22] is so let's try to align them up a bit here with the reference and you can see that actually we
[11:27] need to move the cutter back quite a bit on the x-axis and actually that makes it look nicer as
[11:32] well makes it look more circular there. The only problem is here these loops yeah they are kind of
[11:39] at an angle and I want them to be more in line with the cylinder shape of the handle so I'm just
[11:46] going to rotate them from the top view a little bit and by using the even command so e for even we
[11:53] can kind of easily tweak the other loops as well without having to rotate them so only rotated one
[11:58] and then the other ones I'm adjusting by pressing e and if they are not conforming to the right side
[12:03] just press f for flip this one also e to get even and this one also and you will see that that makes
[12:09] the boolean cleanup a lot easier. This one I'm just rotating suddenly so yeah that's the correct
[12:16] sort of boolean cut there and some small tweaks to rotate it a bit and we can also kind of adjust
[12:23] the cutter position if we want so I think it can be a bit more circular here so let's maybe adjust
[12:30] that a bit we can still use the loop tools command and make some parts a bit more circular if we want
[12:36] I can also adjust the position of the cutter and let's have a look so what if we use loop tools here
[12:41] and adjust how circular this part is and also this part make it a bit more circular that as you can
[12:48] see that kind of influences how the boolean cut looks as well so these are things that you can
[12:53] keep adjusting and fine tuning but I think this is a pretty good result for this cutter object we
[12:59] just need to apply the boolean modifier and by the way if your boolean doesn't work you can just try
[13:04] the exact solver and let's turn off the so the vision modifier before applying that otherwise
[13:10] we get a mess and then we can delete the cutter and this is the result of the cut so that's a good
[13:16] start I think and then we just need to delete manually some geometry here as well so we can
[13:21] use circle select to press c for circle select and then we can just select these really quickly
[13:26] and also select on this side and we can just delete this geometry so press x and delete faces
[13:33] in fact I can select even more for a deletion here so I can just select these faces and delete them
[13:38] as well and of course select and delete that one and then we can start cleaning things up so if we
[13:43] just enable auto merge then we can start double g sliding things and just merging them just to
[13:50] clean up this boolean mess and to simplify things so this one we can slide toward that loop here we
[13:55] can also slide that towards that one and you can see they get merged automatically so this geometry
[14:00] is not bad for a boolean cut I think it's very easy to quickly clean it up so just double g and
[14:05] slide and merge and yeah we're getting some triangles but that's easy enough to solve later
[14:11] and this one we can slide over there and then we can just go to edge selection mode and press f a
[14:16] few times with the f2 extension enabled of course which is really essential you should definitely
[14:22] have that one enabled and then we can add a loop and let's select these loops and to keep that corner
[14:29] sharp we have to bevel it so let's press ctrl b and scroll up so we can get three loops you need
[14:36] three loops to get a sharp corner you don't really need more but you definitely don't want to have
[14:40] less and that's shaded smooth because sometimes when you use a boolean cut the cutter object itself
[14:45] was said to shade flat and so we need to make everything smooth and let's merge these to simplify
[14:51] things and this is pretty good geometry so far we just need to slide some things and clean up some
[14:56] things and just make sure the edge flow is pretty organic here this is kind of a mess here and this
[15:04] kind of piece can be kind of a struggle so we need to probably actually just delete some geometry
[15:10] here and let's delete these parts as well if you don't really know what to do with this kind of area
[15:15] it's always a good place to start is just start deleting or simplifying things start merging things
[15:21] so we'll figure this area out later we just have to do the things that we know we should do and one
[15:29] of those things is we have to add a loop in the middle here for sure so ctrl r and select these
[15:34] two vertices and j to join them so that's so far so good and then we can start selecting things that
[15:39] we know we need to fill like these faces here and then we still have this kind of puzzle here
[15:44] and it is kind of a puzzle I mean you need to really think of it that way don't think of it is
[15:49] like this is a difficult like chore you have to do or this is not like suffering this is just like
[15:55] just playing with blender almost like this is just a puzzle think of it like that I don't know
[16:00] it can actually be kind of fun to model something just for the sake of kind of just modeling and
[16:05] here we definitely do need to keep that loop but here where it terminates it is too much so we need
[16:12] to find a solution for that let's see let's cut k with a knife tool cut until there right click to
[16:18] release the knife tool so you can move around and let's merge these so this is one way to do it not
[16:24] a very good way and I will end up probably redoing this but sometimes you have to do it in a kind of
[16:30] crappy way first and then suddenly you can see the correct solution that was there all along
[16:36] but you need to start somewhere and it really is a puzzle so let's merge these to make things a bit
[16:41] more simple always a good idea when you're doing a kind of geometry puzzle like this is to simplify
[16:46] things sometimes you need to even select faces and press f to turn them into one big angon and
[16:52] you can use the knife tool to start cutting and figuring things out so here I'm just trying to
[16:56] fill things up and at least now I have some geometry in place there it's not good but it's a start
[17:02] and let's have a look at that with a subdev modifier so you can see it is kind of ugly area there
[17:08] we definitely need to do something and one thing we can do is just select it and delete it so I'm
[17:13] just holding shift control and selecting things that we need to delete and let's turn off the
[17:19] subdev modifier in fact let's select all this stuff and delete it also and this one as well
[17:26] and let's delete this one as well and let's select these because we definitely need to make a face
[17:31] there and we definitely need to have a loop in the middle we definitely need to fill these so we
[17:37] know that for sure actually let's undo that and add a couple loops there so we can control the
[17:43] corners and then fill it with f and so we're almost there the only thing we need to do is we need to
[17:48] reduce some of the corners there so we have too many edges and I'm trying to figure out where to
[17:54] put them but first let's make sure we have the right shape for this so if you press g and then
[18:00] shift and z you can move something on only the x and y axis so we're pressing shift and z you
[18:08] actually exclude the z axis so select vertices g shift z and then you only move it on the y and x
[18:16] axis yeah all right and so now we can start to fill the things that we know that we need to fill
[18:22] after some small adjustments of these vertices here let's turn it off and we know we need to
[18:28] connect these at least so press f and press f again and now we can fine tune these vertices a bit
[18:35] so just a lot of double g action and there's still this corner which is kind of a puzzle
[18:40] and one thing we can do is we can select these faces and just press f to fill them and let's
[18:45] see if we can do something similar on this side or we can just merge this by double g signing it
[18:50] and then we can merge these two faces with f to one face and then we just have a hole with four
[18:54] vertices which is a lot easier to solve it just means that we have to terminate that edge somehow
[19:00] so here also let's double g slide this and then fill this hole with f okay so now on both sides
[19:05] we have a loop which terminates in an endgone but it looks a lot better so what we can do to solve
[19:12] that and let's add another loop by the way to make this a bit sharper and that looks much nicer
[19:17] so let's find a solution for this edge and what we can do now is we definitely need it in this part
[19:24] here so we just need to select a part of it and by the way here there's some weird stuff going on
[19:28] so I'm just gonna see if I can solve that let's see if we can delete some faces or something
[19:34] and then there's also a weird face there I don't know what happened there maybe there was just some
[19:39] edge or maybe there was just some double vertices or something and here's another strange face so
[19:44] let's just delete it and then we can fill it again so let's just select this and press f a couple
[19:50] times and f then we have a triangle there but that's okay so let's select this edge loop but not all
[19:57] the way around just until like here where there is this triangle and then we're gonna double g and
[20:03] slide it so that we merge it that way we simplify things so let's make sure auto merge is enabled
[20:09] and then here we can start to merge some faces together so select them and press f and then we
[20:15] can select these two vertices and press j to join them and then here we get a quad actually so we've
[20:20] reduced the amount of edges and we've also gotten rid of that triangle there so let's do the same
[20:26] thing on this side so first we select the edge that we don't want so just hold shift and select
[20:33] all the parts that you don't want and we can double g and slide it until it merges and then here we
[20:38] can select these faces and press f to fill them and then we can select these vertices and press j
[20:43] and then we get a quad and reduced amount of edges and that's looking pretty good already so let's
[20:50] quickly save it so yeah maybe here in the corner we can fine tune this a bit and it's looking a
[20:55] bit gnarly so let's go to xreview and then just move some vertices from the top water graphic
[21:01] view and let's also select these and move them as well and that's already a lot better so let's
[21:07] have a look at the reference image and we need to create this kind of knob at the end of one handle
[21:11] and this kind of you know strange tool I don't know what it is at the end of the other one and so
[21:16] let's shift D and duplicate this and move it up on the z-axis rotate it on the x-axis and then move
[21:21] it on the y-axis and then we can just move this down so this is already starting to look quite nice
[21:26] I think and the rest of it is pretty easy just making those end bits so let's select everything
[21:32] of that end here and just we need to rotate these a bit and I think we just need to delete that cap
[21:37] so let's have a look at the reference image so it's this kind of spherical object here and so
[21:41] what we can do is we can enable statistics and with statistics enabled we can see how many
[21:47] vertices that loop has so 20 vertices and let's set the 3d cursor to this cap and then we can add
[21:54] a round cube that is also an extension extra objects it's called that you have to enable
[21:59] and let's scale that down and let's see how many vertices this round cube has and we can change that
[22:04] by right clicking and choosing change route cube and then we can change the amount of arcs it's
[22:10] called until we get 20 vertices so now we have 20 vertices and so now what we can do is we can
[22:16] select one loop here press V to rip it and then hover over this part and press L to select it
[22:21] and delete it so now we have this knob geometry and let's select this cap and delete it and then
[22:27] we need to select both parts and press ctrl j to join them and then we can make a bridge and
[22:32] let's shade that smooth that's already quite close to the reference image we just maybe have to
[22:36] select some vertices here and just stretch them out with proportional editing so g and then x for
[22:42] the local x axis then you can scroll the mouse wheel up or down if you need to adjust the shape so
[22:47] that is that knob part and next let's do this kind of crap and part here and let's also select
[22:55] these vertices and set the 3d cursor there and then delete the cap and let's add a cylinder
[23:00] we don't need any caps so just set it to nothing and we can set it to maybe just 8 or 12 vertices
[23:06] scale it down and rotate it and just rotate it on the x axis by 90 degrees and then for
[23:12] no top articraf cube we might have to adjust things a little bit so I'm just quickly going to
[23:17] grab some vertices and model this pacman shape and to fill this we can select some edges and just
[23:23] press F to fill ctrl r to add some loops where needed and we can slide this vertex and then
[23:30] we can just geometry bit and fill this and here we can merge these vertices and fill this with a
[23:36] triangle that's fine and same here we're actually going to increase the resolution with one level
[23:42] of subdivision here so it doesn't really matter if there are triangles or angles and I was trying
[23:46] to symmetrize it here but apparently the rotation was not applied so I couldn't really figure out
[23:53] which direction to use for the symmetrize function so in the entire just ended up using a mirror
[23:58] modifier instead so I'm just adding a loop here and then just ripping it so I can select this other
[24:03] half and delete it and then adding a mirror modifier and setting it to the right axis and
[24:09] this is when I figured out that I had the rotation not applied so this symmetrized it and then I can
[24:14] apply the mirror modifier and let's have a look at it from the top articraf cube so let's rotate it
[24:20] and then there's also this kind of taper to the shape but first let's rotate it a bit so let's
[24:25] select this and then set the cursor to the selection and then set transform pivot point to
[24:32] 3d cursor and then we can rotate it from that point and then we can symmetrize this and let's
[24:37] rotate it to align it to the handle part and we might have to scale it up a bit so now how do we
[24:43] merge these parts together first of all let's add a level of subdivision and then let's select the
[24:48] sharp edges so these parts and just hold shift and alt and left click on them so everything
[24:53] that you want to keep sharp and then press shift E and one on the numpad and then we can apply the
[24:58] modifier and we get this shaded smooth and that's isolated by pressing forward slash and then we can
[25:04] select some of these faces here and we can make this part circular with loop to the circle and just
[25:09] make sure to set it to 100% but as you can see it's not really circular and that's because the
[25:14] scale is not uniform so control A apply scale and let's try that again loop to the circle and then
[25:21] delete those faces and let's move this loop back and just make some space so that we can bridge the
[25:27] area between those two different parts and in fact we can probably just dissolve that edge loop to
[25:33] make it a bit more simple so just control and x to dissolve it and we can move this part and actually
[25:39] let's set the transform pivot point back to median to make rotating a bit more easy and just move it
[25:45] back with double G and let's see we don't have enough geometry to really merge them so if you do
[25:51] a loop to the bridge now you get this kind of result with a lot of triangles and it's not too bad
[25:56] but let's see if we can do better than this so undo and let's see if we can add a bit more geometry
[26:02] so with the knife tool just press k for the knife tool and then just start cutting and this way you
[26:07] can create a bit more geometry and right click to release the knife tool and then you can left
[26:12] click again to create more cuts on the other side like that and then press enter and let's see
[26:16] loop to the circle to make it circular again and now we still don't have enough geometry so we need
[26:22] to cut a bit more with the knife tool so just create this kind of shape and right click and then do
[26:27] the same thing on the other side so left click with the knife tool to create this kind of redirected
[26:33] shape and now we should have 20 vertices so just like there and then we can bridge it but for some
[26:39] reason the bridge result is not good i'm not really sure why so i'm just going to have to maybe do it
[26:44] manually so let's make sure this is a circular and let's make sure the things align up correctly so
[26:51] you can see it doesn't really line up very good let's hover over this part and press l to select
[26:55] all and then just kind of adjust its position carefully and let's just try the bridge tool
[27:01] one more time but it really doesn't work very well for some reason so let's just select edges
[27:05] press f and then we can press f a few more times to fill all those other faces and one more thing
[27:11] i would like to do is just select everything in xreview just select that whole end part there
[27:18] and then press i for inset and then press o for outset and you have to move the mouse a bit but
[27:23] after a while you get this nice protective loop cut around that part and in fact we can reduce some
[27:28] of that geometry and that looks a lot better already and we can slide this to make it a bit
[27:33] nicer sharp and finally we can tweak some individual vertices because those were kind of pointing out
[27:38] in a weird way and same at the bottom here yeah and that looks pretty nice and we can add a not
[27:44] a round cube here for that yeah that bolt part and shade it smooth and then just scale it down
[27:50] and i'm not really sure how to place this part looks a bit illogical but let's just place it here
[27:56] again this video was not really about making the perfect recreation of this tool if i wanted to do
[28:01] that i would search for a bit more reference it's more to show you how to do those transitions from
[28:08] sharp to smooth and to have that kind of boolean cut so let's select this part in xre mode and
[28:14] just move it with proportional editing enabled so yeah something like this maybe and i think that's
[28:21] more or less correct and i think that's pretty much done so yeah i hope you enjoyed watching this
[28:27] and if you want me to model something please leave a comment i can't promise that i'll model it i
[28:32] will just choose the thing that i find most interesting but if you're going to leave a comment
[28:36] maybe don't use a link because youtube tends to hide comments with links so i won't see it so just
[28:43] describe in detail where i can find the picture of that thing just describe it yeah that's all
[28:49] i hope you like this video and thank you for watching and see you in the next one



---

## Captured Frames

- [0:40] tutorials/frames/how-do-you-model-that-wrench---blender-secrets/frame_000.jpg
- [1:28] tutorials/frames/how-do-you-model-that-wrench---blender-secrets/frame_001.jpg
- [2:05] tutorials/frames/how-do-you-model-that-wrench---blender-secrets/frame_002.jpg
- [10:00] tutorials/frames/how-do-you-model-that-wrench---blender-secrets/frame_003.jpg
- [10:36] tutorials/frames/how-do-you-model-that-wrench---blender-secrets/frame_004.jpg
- [13:16] tutorials/frames/how-do-you-model-that-wrench---blender-secrets/frame_005.jpg
- [18:35] tutorials/frames/how-do-you-model-that-wrench---blender-secrets/frame_006.jpg
- [21:47] tutorials/frames/how-do-you-model-that-wrench---blender-secrets/frame_007.jpg

---

## Structured Notes

### Core Technique
A full reference-image-to-model workflow (despite the title, the reference and result are a pair of pliers, not a wrench — flagged here for accuracy) demonstrating the double-subdivision "quad blockout" method applied to a real, messy hand tool: box-modeling over a reference image, sharp-to-round transitions via graduated LoopTools Circle percentages, a boolean cut for the tool's jaw notch, freeform topology cleanup ("the puzzle"), and small end-cap details built from a Round Cube primitive.

### Summary
Frame 000 shows the setup: a reference photo of pliers dragged into the viewport behind a plane, in Top Orthographic view, ready for box-modeling on top of it. Frame 001 shows the payoff of that box-modeling pass — an orange-outlined mesh silhouette tracing the pliers' jaw and handle shape directly over the reference photo, viewed in Object Mode with 27 modifier-stack vertices reported top-left. Frame 002 is the same shape in Edit Mode, showing the raw low-poly cage (vertex dots, edge lines) tracing the reference's jaw curve, with the Subdivision modifier's Ctrl+2 shortcut noted in the corner. Frame 003 shows a right-click Vertex context menu open (Merge Vertices, Split, Separate, etc.) over a partially-cleaned handle/jaw junction — the "topology puzzle" cleanup phase after the boolean cut. Frame 004 shows the near-final shape rendered solid next to the reference photo split-screen for comparison — jaw, boolean-cut notch, and both handles present and closely matching the photo. Frame 005 shows a close, shaded 3D view of the handle-to-jaw transition, revealing the underlying quad topology and edge flow that creates the smooth curved surface. Frame 006 shows an extreme close-up of one such transition corner with a Vertex Slide operator panel open (Factor, Even, Flipped, Clamp, Correct UVs), matching the transcript's "double-G slide, press E for even" technique for keeping support loops evenly spaced. Frame 007 shows the far end of one handle — a perfectly round tube segment being edited, "Image ID: A3MB6R" watermark from the reference visible, illustrating the round-cube-based end-cap detail work.

### Key Steps
1. **Reference setup:** drag-and-drop a reference photo into the viewport, reposition/scale it, lower its opacity for mesh visibility, and disable its selectability so it doesn't interfere with clicking; add a plane (Shift+A), enter Edit Mode with X-Ray enabled.
2. **Box-model the silhouette:** working from a mostly-orthographic reference (not a perfect ortho view — the goal is teaching shape transitions, not an exact replica), extrude and adjust vertices to trace the tool's outline, keeping vertex count low at first for speed; add Ctrl+R loop cuts for more detail as needed.
3. **Double subdivision blockout:** press Ctrl+2 to add a Subdivision modifier at 2 levels; disable it temporarily in Edit Mode while adding more Ctrl+R loops at points that need sharper corners, then re-check the smoothed result in Object Mode; enable **On Cage** to fine-tune the *smoothed* shape directly against the top-orthographic reference.
4. **Even support loops:** after adding a support loop near a corner (to control sharpness), press E (Even) while sliding it so its distance to the corner stays consistent along a curved edge, rather than drifting; add a second loop supporting the first if two very-close loops cause topology stretching; G,G (double-tap G) slides vertices along existing edges for fine adjustment.
5. **Organic edge redistribution:** select a loop and Ctrl+B (bevel) with the "Percent" width type for a more organic, non-uniform spacing of new edges when a straight bevel doesn't read naturally.
6. **Thickness:** add a Solidify modifier (or extrude manually) for material thickness, then Ctrl+A to apply it; a center support loop plus a corner bevel keeps the solidified edge from going too smooth/round.
7. **Adding a center crease/ridge:** select the center loop and Alt+S (scale along normals) to push it outward for extra mid-section thickness and a sharper visual ridge, matching a reference detail; deselect end loops with Shift+click before scaling so the taper reads correctly, since Alt+S scales differently than a plain S.
8. **Round-handle transitions (the "sharp-to-round" trick):** enable the LoopTools extension (Preferences); delete a rough end section and rebuild it via Grid Fill (select opposite edges and re-run if the first attempt isn't clean) then LoopTools Flatten to square it off; add loops with Ctrl+R; for a fully circular cross-section use LoopTools Circle set to 100% Influence; work down the handle applying Circle at decreasing influence values in graduated steps — e.g. 100% → 80% → 60% → 40% → 20% across five consecutive loops — to produce a smooth, gradual transition from sharp/angular to fully round rather than an abrupt jump; use Shift+R to repeat the last operator across further loops; open a second viewport with overlays off and a Matcap enabled (plus On Cage on the Subdivision modifier) to preview the shaded transition while tuning percentages, since it's easy to misjudge from wireframe alone.
9. **Boolean jaw-cut:** duplicate the jaw shape (Shift+D), hide the original, rotate the duplicate 180° (R,180,Enter) and offset it to form the opposing jaw; model a cube as a cutter object, shape it (rotate, add loops, curve it to match the reference's jaw notch) — align the cutter to the reference image, nudging its position along each axis until the cut silhouette looks right; use Even (E) and Flip (F) on the cutter's own loops so its edges align well with the cylindrical jaw shape before cutting, since well-aligned cutter geometry makes for a much cleaner boolean result; select cutter + target, Ctrl+Numpad− to cut; disable the Subdivision modifier before applying the Boolean (to avoid a subdivided mess), and switch the Boolean modifier's solver to Exact if the default doesn't produce a clean result; delete the cutter afterward.
10. **Post-boolean cleanup ("the puzzle"):** circle-select (C) and delete stray boolean-created faces; enable Auto Merge Vertices, then repeatedly double-G-slide loose vertices onto neighboring geometry to merge and simplify the mess (accepting some resulting triangles as fine for now); enable the F2 add-on (described as essential) so pressing F repeatedly fills faces intelligently; use the Knife tool (K, right-click to release) to manually cut a path through an awkward n-gon area when no clean automatic solution presents itself — treat messy post-boolean topology as an iterative puzzle: simplify by merging/dissolving first, then fill what's clearly needed, and only hand-solve the remaining ambiguous pocket last; a Ctrl+R loop plus J (connect two vertices) helps re-establish clean edge flow through the patched area.
11. **Small end-cap details:** enable Statistics to count a loop's vertices (e.g. 20); snap the 3D cursor to that loop; add a **Round Cube** primitive (from the free Extra Objects add-on), scale it down, and right-click > Change Round Cube to adjust its Arc/segment count until its vertex ring matches the target loop count (e.g. 20); select a loop and V (Rip) plus L (select linked) to isolate and delete unwanted cap geometry; join the pieces (Ctrl+J) and Bridge Edge Loops to connect the round-cube knob to the handle end; use proportional editing sparingly (G, scroll wheel to adjust falloff radius) to blend the transition; for a second, more cylindrical/asymmetric end detail, use a capless Cylinder (8-12 sides) instead, hand-model a "Pacman"-like notch shape into it, fill gaps with F and Ctrl+R loops, and use a Mirror modifier (after first verifying Object > Apply > Rotation, since an un-applied rotation can make Symmetrize pick the wrong axis) to build it symmetrically before merging it onto the handle with Bridge Edge Loops, extra Knife-tool cuts for missing geometry density, and Apply Scale (Ctrl+A) if Loop Tools Circle produces a non-circular result due to non-uniform object scale.

### Nodes / Settings
- **Modifiers:** Subdivision Surface (Ctrl+2 shortcut, On Cage editing), Solidify (applied via Ctrl+A), Boolean (Difference via Ctrl+Numpad−, Exact solver fallback), Mirror (axis-specific, applied after symmetry verification).
- **Add-ons/extensions:** LoopTools (Circle with adjustable Influence %, Flatten, Bridge), F2 (smart face-fill on F), Extra Objects (Round Cube primitive, adjustable Arc count via right-click > Change Round Cube).
- **Core edit tools:** Grid Fill, Knife (K), Rip (V), Select Linked (L), Circle Select (C), Merge/Auto Merge Vertices, Connect Vertex Path (J), Vertex Slide with Even (G,G then E) and Flip (F) options, Inset+Outset (I then O), Fill (F), Dissolve Edges (Ctrl+X), Statistics overlay.
- **Transform nuances:** Alt+S (scale along normals, for ridges/thickness), G then Shift+Z (move on X/Y only, excluding Z), Apply Scale/Rotation (Ctrl+A) before Mirror/Symmetrize or Loop Tools Circle.
- **Viewport workflow:** second viewport window with Overlays off + Matcap + On Cage enabled, used specifically to preview shaded results while tuning LoopTools Circle percentages.

### Difficulty
Intermediate to Advanced (assumes comfort with subdivision modeling fundamentals; the boolean-cleanup "puzzle" section is genuinely improvisational, open-ended topology problem-solving)

### Blender Version
Not specified — relies on On Cage Subdivision editing, the LoopTools/F2/Extra Objects add-ons, and the Exact boolean solver, all consistent with Blender 3.x through 5.x.

### Tags
modelling, procedural, intermediate, advanced

---

## Related Tutorials
- [For Beginners: Easiest Modeling Technique (long version)](for-beginners-easiest-modeling-technique-long-version.md) — shares modelling, procedural; both use the double-Subdivision-modifier + On Cage blockout method, this video applies it to precise reference-matching rather than freeform sci-fi design.
- [Blender Secrets - 6 Minutes of Boolean Basics](blender-secrets---6-minutes-of-boolean-basics.md) — shares modelling, procedural, intermediate; that tutorial's boolean-cleanup techniques (Weld modifier, Auto Merge, support loops) are the same category of fix applied here to the jaw's boolean cut.
- [How do you model that? Kingdom Hearts Keyblade - Blender Secrets](how-do-you-model-that-kingdom-hearts-keyblade---blender-secrets.md) — shares procedural, advanced; same "How do you model that?" reference-to-model series, applying the same box-model-over-reference approach to an organic fantasy weapon instead of a mechanical tool.
