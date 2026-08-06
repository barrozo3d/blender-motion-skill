---
title: How do you model that? Kingdom Hearts Keyblade - Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=QV2Av9dSDbc
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified"
tags: [procedural, organic, advanced]
extraction_status: complete
frames_dir: tutorials/frames/how-do-you-model-that-kingdom-hearts-keyblade---blender-secrets/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# How do you model that? Kingdom Hearts Keyblade - Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=QV2Av9dSDbc)
**Author:** Blender Secrets
**Duration:** 35m31s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] For this video, somebody asked me to model a Keyblade from Kingdom Hearts,
[0:04] and so I went looking for some designs, and I found a lot of really interesting ones,
[0:09] and eventually I settled on one of them. It has a kind of interesting swirling shape,
[0:16] and they specifically asked me for modeling something for 3D printing.
[0:21] So we're not going to be dealing with quad topology or subdivision ready topology,
[0:25] we're just going to model it for 3D printing. So step one would be always to look for as much
[0:31] references you can find, and they were all a bit different, but this one had a nice side view.
[0:36] So just drag and drop that reference in Blender, and I'm adding a cube here so I can get an idea
[0:42] of the size. I decided it's probably about a meter and a half. So with the cube as reference,
[0:47] we can scale down the reference image to about a meter and a half in size, and let's turn off the
[0:53] selectability of that reference image so we cannot accidentally select it while we're modeling.
[0:57] So let's start by adding a plane, and why do I need a plane? It's because I need an edge,
[1:03] so I'm just going to delete two vertices, and then we're left with two vertices making one edge,
[1:08] and we can select it in edit mode and then subdivide it a couple of times, so subdivide it once and
[1:14] then twice, and so now we have these five vertices, and I'm going to convert that to a curve, and yes,
[1:20] I know I could have just chosen a path instead, but if you start with a mesh and then transform it
[1:26] to a cube and set the resolution to one, you have more control over the shape of the curve.
[1:34] So here I'm giving it some depth, and then we can scale down the vertices by scaling on the radius
[1:39] in this panel, or with Alt S. So let's add a nice math cap that's always more fun. I wouldn't
[1:45] recommend using zero as the radius just because it might cause some issues when you're remeshing it,
[1:51] and that very infinitely small point might cause some problems. So just leave it at a very small
[1:58] value instead, something like this, and then you have to make sure the caps are closed,
[2:03] so you can see now the cap there is closed, and so we can start scaling these down with the
[2:07] radius value, or just by pressing Alt S. So not S like you would be used to for scaling,
[2:13] but Alt S. So that's one of the strange things about curves, and if we add some subdivision to
[2:18] it, you can see it becomes nice and smooth. So now we have this kind of long teardrop shape,
[2:23] and we can very easily manipulate it because it only has five control points. Of course,
[2:28] now it's way too big, so let's scale it down a bit, and let's move it over here, and of course,
[2:32] we need to be in wireframe mode, otherwise we cannot see the reference image. So I would recommend to
[2:38] apply the scale just in case, so we can predict what's going to happen, and then just start lining up
[2:45] the curve with the drawing, and you can subdivide between two vertices, and you add another vertex
[2:50] in between, then you get a bit more control if you don't have enough vertices. So here,
[2:54] just right click, subdivide, and then you can move another point, and then we just have to scale them
[2:59] up or down and move them according to the reference underneath. So very easy technique, and yeah,
[3:05] just try not to add too many control points from the beginning, that way you can have a bit more
[3:10] control over the shape, and the roundness, the curves stay more perfect than if you have to
[3:16] control a lot of vertices. So just try to get away with as few vertices as you think you need.
[3:22] Like here, I need one more maybe to get this little upward shape in the curve at the end there,
[3:28] and then it looks like this in a solid view. And so this one, it also has this kind of nice
[3:33] ridge at the end, so the curves are not supposed to be completely round. So the way we can do that
[3:38] is we can create another curve, and let's just rotate that and scale it down. So now we have a
[3:44] circle curve, and we can scale it down and move it out of the way. It doesn't really matter where it
[3:48] is. And then we just scale two of these vertices down, so the ones at the side are scaled down,
[3:54] and that is with S instead of Alt F. And here we just pick that curve as the bevel object,
[4:00] and as you can see now it has that nice ridge at the side. And that's really all we need to do
[4:04] for this curve. Now we just have to place it everywhere. And we do have to scale it up a bit,
[4:09] because by using that bevel object, we adjusted the shape a bit, and we can also just scale up the
[4:15] bevel object itself and just move that over to the side so you cannot accidentally manipulate it.
[4:22] So let's do some final tweaking for this shape. So that looks really nice. And now we can actually
[4:27] add a mirror modifier to it, because the one on the other side is exactly the same. We just have
[4:31] to set it to the Z axis. And we should add an empty that is in the world origin. And let's scale
[4:38] that empty down a bit. We can do that in this panel. Don't do that by pressing S, because that
[4:43] affects how it works. So pick the empty as the mirror object in the mirror modifier, and then
[4:49] you get this result. Yeah, and then we can just start adding the other curves as well. So just
[4:54] shift D to duplicate this one. And we can reduce the amount of subdivisions a bit if needed,
[4:59] just to keep the scene more lightweight. And now let's shift D and duplicate it. And then we can
[5:04] rotate this and we can start adjusting this curve as well. So switch back to wireframe mode, and then
[5:10] we can start adjusting all the vertices as we can see it should be in the reference image. So you
[5:16] can also select multiple vertices and then just rotate and transform them. So it goes a bit faster.
[5:21] It looks like here we probably don't have enough vertices in this duplicated curve.
[5:25] And here we need to scale this up. And when they touch, you can see something weird happens. And
[5:29] that's just because the merge option is enabled on the mirror modifier. So some small tweaks. And
[5:35] you can see we very quickly get the shape that we need. So something like this. So I'm just going
[5:40] to turn off that merge option in the mirror modifier. Then I can move those curves a bit closer
[5:46] together without it acting strange. So you can see the difference if I turn on merge and have I
[5:50] turn it off. So those are mirrored. And for the most part, they don't need a mirror modifier.
[5:55] So for the most part, every curve that you see is unique. So just duplicate one and remove the
[6:00] mirror modifier and then just start adjusting it. And if you want, you can try to use the
[6:06] proportional editing option, but it might not always really be beneficial in this case. It's
[6:11] really just a matter of moving each vertex individually. But as long as you don't have
[6:15] too many of them, it shouldn't really take that long. And it's pretty easy to do. So you can
[6:20] just listen to a podcast or listen to some music or something. It's not something that requires a
[6:24] ton of concentration. So this is a pretty easy technique to use, actually. It's just kind of a
[6:30] lot of work if you have a lot of these curve shapes. Like in this keyplate, there are quite a lot of
[6:35] them. So it takes a minute, but yeah, it's a relaxing kind of work. So as you can see, I need to
[6:40] subdivide this curve quite a lot to get enough control points or vertices. But it's always good
[6:46] to start with a smaller curve and then add points. Although you can always delete them, of course,
[6:51] if you have too many. So here I'm just adjusting the bevel shape a bit. I'm just lowering the
[6:56] resolution to a few less vertices. But if there are too few, then you also don't get that rich
[7:02] at the side. So you have to be kind of careful and find the balance. So you can see what it looks
[7:06] like in solid view. So I have to add at least a few of these vertices in the resolution there.
[7:12] Just enough to get that rich at the side of the shape. The reason I'm doing that is just
[7:18] I'm trying to make it as low a poly or as low resolution as possible, because it's just a
[7:25] bit more lightweight for my computer and a bit easier to manipulate. And here I'm just scaling
[7:29] everything to zero on the y-axis, because some of those curves were not in the right location.
[7:34] And this way they are all just on a flat plane. So if the resolution of these curves is not that
[7:40] high, then I can later convert them to meshes and just add a sub-diff modifier. And then the
[7:47] distribution of the geometry will be more even than if the resolution of the bevel object is higher
[7:54] than that of the curves themselves. This is for a 3D printing result. So what I'm doing is I am
[8:01] going to, after creating all these curves, convert this to mesh, and then I'm going to join it all
[8:06] and then I'm going to remesh it so that I can merge everything together. And then in sculpt mode,
[8:10] I'm going to make sure that everything is nicely merged together where it needs to be by smoothing
[8:15] parts where they merge together. And that gives a very beautiful result. And then I can just
[8:21] decimate it to be not too high resolution, but still look good. And then that will be useful
[8:28] for 3D printing. So a very different workflow than you would do when you would be making a
[8:33] subdivision ready model. Although if I were making this for perfect subdivision ready topology,
[8:39] I would do everything the same up until the end. And then I would just continue after where here I
[8:46] stop with the 3D printing workflow. I would actually continue and just read, apologize that result.
[8:51] So the beginning stages would all be the same. It would just be creating these curves, turning it
[8:55] into mesh, converting everything and joining everything together as a mesh topology, converting
[9:00] everything to meshes and joining it together and then in sculpt mode, merging everything together
[9:05] and remeshing it and stuff. But I would just use that as the base for read apology. So some parts
[9:11] are sort of partially mirrored. So here I can actually duplicate this part and flip it around
[9:16] and then at least use half of it. So I'm just adjusting this half at the back. And for the rest,
[9:22] I'm just selecting and deleting these vertices because I don't need those. So you can just use
[9:26] one part of the curve if it suits you. So here we are continuing to duplicate and adjust some curves.
[9:34] And I would recommend maybe putting all the curves roughly in place and then fine tuning them later.
[9:41] So maybe don't spend too much time in one area, just so you can get a bit of an overview early on
[9:49] and almost kind of blocking it out rather than going for perfect from the start. But it's just
[9:55] up to your personal preference. I mean, I like to block out shapes to get to the overall result
[10:00] as quickly as possible and then kind of make it better because then I have a better idea of how
[10:05] much time I have left and how much time I can spend on perfecting all the shapes. And if I run out
[10:11] of time at that point, then at least I've already blocked everything out and I have at least some
[10:15] kind of result. So here I am creating the circle by extruding the circular shape and then I'm
[10:20] selecting two vertices at the end and then pressing F to close that gap. And so rather than
[10:25] adjusting every vertex manually to get a more circular shape, we can smooth the vertices
[10:31] and then press Shift R a few times to repeat the smoothing. And as you can see it shrinks,
[10:35] so we have to scale it back up. But now as you can see it's more perfectly circular. And then
[10:40] maybe we can add a bit more volume by pressing Alt S. Instead of duplicating a whole curve,
[10:44] you can also just take some vertices from another one and press Shift D to duplicate
[10:48] and then press B to separate it to a new object. And I'm just scaling everything to zero on the
[10:53] y-axis just to make sure that it's still all on the same plane. And let's set the grid to a smaller
[10:59] size like 0.01. That is a bit more convenient if you're working at this small scale. So we are
[11:06] actually working with centimeters. Let me just change that here. So set it to centimeters and
[11:11] then we can just type the centimeters in the scale value or the dimension values there. So
[11:17] let's create the shaft by just adding any kind of mesh primitive so we can collapse that to one
[11:23] vertex and then we can start extruding that vertex in vertex selection mode and edit mode. So just
[11:29] extruding with E and then converting it to a curve and giving it some thickness there. And then
[11:34] just like with the other curves, we can start to adjust the individual vertices by pressing Alt S
[11:39] and by changing their location. And we can extrude some more here where needed. And for this grip,
[11:44] I'm just adding a cylinder with eight sides and no caps and just scaling that down. And then we can
[11:51] move this part at the end here to the end of the grip. And we can start adding some loops with
[11:56] Ctrl R and adjusting the shape as we see fit from the reference image, of course. So yeah,
[12:02] every time you add loops with Ctrl R, you can scale them down and get a bit closer to the shape.
[12:07] And after adding a sub-diff modifier, you might have to adjust the scaling of those loops a bit
[12:13] more because when you add a sub-diff modifier, it always shrinks the volume of the object a little
[12:18] bit. And then we need to just close this by selecting it and pressing Ctrl F and then G for
[12:23] grid fill. And we can move that curve back and add another loop around it. And that's the grip done.
[12:29] And now let's add another cylinder here to fill that circle there. And we can rotate it and then
[12:35] select this boundary loop and grid fill it to close that cap. And then we can do symmetries,
[12:41] which didn't work in this case because I had to apply the rotation first. So now it's symmetrized
[12:47] and I can scale it down on the y-axis. So scale it down on the y-axis so that it's just thick enough
[12:52] to fill that gap there. It shouldn't be completely thin because then it will cause some issues when
[12:57] you're remashing it. And so that's that gap filled. And then we can also create this. And this we can
[13:02] do with some box modeling. So I'm just adding a box and an extruding vertices and scaling them
[13:07] up or down. And yeah, just creating that shape real quick like that. And just adding loops with
[13:13] Ctrl R to be able to get closer to the shape. And I'm just adding a sub-diff modifier and
[13:19] adjusting the shape some more. So this is box modeling. This is just one of the most ancient
[13:23] 3D modeling techniques. But as you can see, we can very quickly get to the results that we want.
[13:28] And we can maybe scale some of these vertices up a bit to make it a bit thicker at the side there.
[13:33] And I'm just scaling that top vertices up a bit there. So you need to sometimes enable x-ray mode
[13:39] to be able to tweak vertices that are beneath something else. And we still need to add a few
[13:44] more curves. So I'm just shift D into getting some other curves and just adjusting them as needed.
[13:50] Now this shape is a bit unusual. So I just have to convert it to a mesh to get it to the way I want.
[13:56] And to do that, I'm temporarily lowering the resolution of the bevel object and then converting
[14:00] this to mesh. And I'll turn the resolution back up for the bevel object. But that way I get a very
[14:05] low res mesh here. And this part we need to merge some vertices because that cap is loose for some
[14:11] reason. And then we can move those vertices out a bit. And then we can select loops by alt and
[14:17] left clicking on them and then scaling them up or down. And it helps to have proportional editing
[14:21] on for this to more organically adjust the shape. And the reason I'm converting this to mesh is just
[14:28] have a bit more control over the shape over each individual vertex. That is something that is not
[14:33] so easy with a curve. So then we get something like this. And as you can see, it's not really
[14:36] symmetrical. So we will need to do something about that. So after scaling this in a bit, we have to
[14:42] symmetrize it. And so I have that in my quick favorites, but I will have to quickly set the
[14:47] origin to the very center to make sure we can really symmetrize it. Correct. Sometimes it can
[14:51] be useful to convert something to a mesh. So for example, I'm going to convert this piece to a mesh
[14:57] and it gives me a lot of vertices that I can work with. So I can use proportional editing and pull
[15:02] this down, for example, and we can do the same for this piece. And then we can pull on these
[15:06] vertices in order to close this gap. We can also convert this staff piece to a mesh. And then we
[15:12] have a bit more control over these vertices. And we can pull them in on the y axis to make that part
[15:18] thinner than the rest of it. That way it doesn't obscure those curved parts. But since we're only
[15:23] doing that on one side, actually, we should symmetrize this mesh. So I just select everything in edit
[15:28] mode and then symmetrize and make sure you symmetrize it on the right axis. I've got symmetrize on my
[15:33] quick favorite menu because I use it a lot. Otherwise you can find it in the mesh menu. So next
[15:38] we need to make these pieces in between the curves. And for that, I'm just using a plain,
[15:42] very simple piece of geometry with four vertices. And then we can adjust the vertices. And when we
[15:48] adjust it each time, we can add a bit more geometry to it. So we have more vertices to work with.
[15:53] And eventually we will get to the shape that way. And this is a fairly simple two dimensional shape.
[15:58] We just need to add some thickness to it afterwards. So we control R. I'm adding some loops and then
[16:03] adjusting the new vertices and adding some loops in between here as well. So we've got our two
[16:08] dimensional shape. And then we need to add a sub-diff modifier to it to get more to work with.
[16:13] And we can apply that sub-diff modifier. And then we have a bit more of the shape to work with.
[16:17] But I will add another sub-diff modifier to it right after. And I'm not going to apply that one.
[16:21] I'm just going to use it to fine tune the shape. So as you can see, now we already have the two
[16:26] dimensional version of that shape. And we just need to add a bit of thickness to it. And we can use
[16:30] a sub-diff modifier to add thickness to it. So just search for the sub-diff modifier and maybe drag
[16:35] it up to be the first one on the modifier stack. And you can set the offset to zero so that it's
[16:40] nice and centered and then adjust the thickness. And here we've got this floating piece of geometry,
[16:46] which happens when you convert a curve to a mesh. I noticed, but we can just delete it.
[16:51] And it's always a good idea to merge by distance. And with the same workflow, we can create this
[16:55] piece at the end here, just another plane. Then we just add more and more edge loops to
[17:00] with Ctrl R in order to get to the shape. And then in this case, we need to mirror it as well.
[17:05] However, in this case, the mirror modifier didn't work because I did not apply the rotation. I
[17:10] rotated the plane after I added it. And then I forgot to rotate it. That's why the mirror doesn't
[17:15] work in this case. So I'm applying the rotation and then setting the mirror to Z. And I increased
[17:19] the merge value so that the vertices at the center gets merged. And I'm going to apply that
[17:24] mirror modifier. So now we have that two dimensional piece. And now we can add a solidify modifier
[17:28] to this, but we can also just copy it from the previous piece by selecting both and I'm pressing
[17:33] Ctrl L and copy modifiers. So you can see now it has the thickness, but it does seem to be a bit
[17:38] off center. So we have to move this on the y-axis. Next, let's work on this star object. So I actually
[17:44] have the extra objects extension enabled. And that gives me the primitive simple star. So we
[17:50] just add a simple star and then we just need to tweak the settings a bit. So as you can see,
[17:54] we can get the exact shape that we want pretty easily. And it's really worth exploring the
[17:59] primitives that you get with the extra objects extension. Now I only need the front face of
[18:04] this. So we can actually just select that and then delete all the other stuff. And then let's
[18:09] select these faces and press F to join them into one quad. And let's do that for all of them.
[18:15] This way we can inset them more easily. So let's select them all now and press I to inset. And
[18:20] when you press I twice or you check the individual box, then you get this individual inset. And that
[18:26] is what we want in this case. And let's select these faces and then we can inset these. And in
[18:32] this case, you'll have to press I twice again just to toggle that individual option off. And
[18:36] let's repeat that. We can just select faces and then press shift R because the shift R command,
[18:41] which is the repeat last command remembers that we wanted to inset. And that way you get the
[18:46] exact same inset each time. So let's select all of these loops and then extrude them. Now let's
[18:51] scale these down, but not to the median point, but to the individual origins. And this is the shape
[18:56] we have so far. Let's select the outer loop and then set the 3D cursor to it. So shift S
[19:02] cursor to select it. And then we can set the origin to the 3D cursor. Now the origin is right
[19:06] where it needs to be in the middle of this star. And now we can add a mirror modifier to it. But
[19:10] since I rotated the primitive shape, we need to apply the rotation before it works correct. So
[19:16] Ctrl A, apply rotation, and then it's mirrored along the y-axis. But I think we can add a bit
[19:20] more thickness to it by selecting everything in edit mode and then moving it a bit away from the
[19:25] center in the y-axis. So that creates a bit of a gap and let's apply the mirror modifier. And now
[19:30] that we've applied the mirror modifier, we can add faces in between these gaps. And now let's add a
[19:35] battle modifier to make the edges seem a bit more interesting. This way the corners catch some light,
[19:40] which is more like what a real object would be like. Then let's add another plane and let's add
[19:45] those little details at the corners of the star. And again, we are just starting with the very basic
[19:51] shape and then just adding more loops to it. Just remember to set the transform pivot point back to
[19:56] median point. Then after this shape is finished modeling, we can select the star and set the
[20:02] cursor to it. And then we can set the transform pivot point to 3D cursor and then we can easily
[20:07] duplicate and rotate this shape. So shift D and msr and rotate it. And you can see in the top of the
[20:13] 3D viewport the rotation angle. So you can just use that and round it up to say in this case 72
[20:19] degrees and just repeat it a few times. Next I will drag in an image that I found which has the star
[20:24] in a bit more detail because it was quite difficult to see those details. So now we can see exactly
[20:29] what that shape is supposed to be like. And again, I just model this by starting with a simple plane
[20:34] and then extruding vertices and adding some loops and then extruding some more until I just get the
[20:40] two dimensional version of this shape. And so let's move that to the star and then let's hide it
[20:45] and rotate that so that we can really place it correctly and let's scale it up a bit. And then
[20:50] we can extrude everything and we need to flip the faces if we extrude in the wrong direction.
[20:55] And we're just going to select these sharp corners and then bevel it, but I will have to turn off
[20:59] auto merge for that. As you can see, auto merge needs to be disabled and then I can control B
[21:03] and bevel this. And with three edges you get very sharp corners. We just need to add a few more edge
[21:08] loops so that there are no ugly overhangs. So here for example, you can see the overhang that is
[21:13] created by the subdivision and what to do to solve it. Anyhow you can solve it by adding more
[21:18] control loops. Now this is just a really rough and dirty way to add those sharp corners. I probably
[21:23] would spend a little bit more time on this if this was for a sub-tiv modeling, but since it's
[21:28] gonna be 3D printed, all I need to worry about really is that this water tight and let's move it
[21:33] to where exactly it needs to be. And then finally this other sharp object, we also just do it in
[21:39] exactly the same way, just starting with a plane and then just adjusting the shape and just extruding
[21:44] and adjusting some vertices and extruding it to add some thickness to it. And very quickly,
[21:49] you already get the right shape. And of course, this one, I'm also gonna bevel the edges and add
[21:54] some more loops to counter these overhangs. And with that, the shape is pretty much done. And then
[21:59] we just need to put it in the correct location. And with that, we have the finished star object.
[22:05] So now we can select that and we can move it to where it needs to be, which is here in this
[22:09] circular part. And it would have been smart of me to add the star to its own collection,
[22:15] because not doing so will create some trouble for me later, which I will show you. Now that I have
[22:20] blocked everything out, I will do some perfecting of the curves. However, one of the parts of that
[22:26] is that I have to fix this asymmetry issue, as you can see. So I'm just gonna set the transform
[22:31] to 3D cursor and then set the cursor to the world origin, select everything in edit mode,
[22:38] and then scale everything to zero on the y-axis. That way, at least it is all definitely on the
[22:44] center of the world plane. And as you can see, that helped a little bit, but it's still not perfect.
[22:49] And it's probably because this object is not symmetrical. So let's apply the solidify modifier
[22:54] first, and then let's symmetrize it. And here too, we need to apply the rotation first. This is
[23:00] very often a problem. So Ctrl A, apply rotation, and then symmetrize it on the y-axis. And so now
[23:06] this is definitely symmetrical, but it still doesn't look symmetrical. And that's because it is not
[23:11] aligned correctly on the y-axis. So these are all really things you need to take into account.
[23:15] And so now it is symmetrical. And I'm just gonna quickly check which other objects I need to align
[23:21] on the y-axis, or which I need to symmetrize. So for example, this I need to move a bit to the
[23:28] center of the world, and this one as well. And this, for example, I need to symmetrize also,
[23:32] and move it a bit. And this also needs to be symmetrized. And if you've got a little issue
[23:36] like this, then you can just select those vertices and merge them to center. So after a while,
[23:40] everything is properly symmetrized. And now we can start to really perfect the curves. And let's
[23:46] quickly rename this collection. It's always good to keep a backup, like I have these curves, which
[23:51] are non-destructive. And so it's good to have that as a backup before we convert everything to a mesh,
[23:56] just in case we need one of those curves later. And you'll see later that we do indeed need one.
[24:01] And so here, to make these curves look a bit prettier, I'm just deleting some of the vertices
[24:06] so that I can scale them down better. And I'm doing the same to all three of these. So just
[24:11] delete the vertices that I don't need, and scaling down the one at the top. And as you can see, now
[24:15] it looks nice and symmetrical. So basically, I'm just moving these curves on the x and z-axis.
[24:20] I'm being very careful not to move them on the y-axis. And here, there, I'm scaling some
[24:25] vertices up or down with all this. And I'm mainly taking care to remove any of these gaps
[24:30] between these curves, because it just doesn't look as nice. And here, for example, to remove that
[24:34] gap, we just scale this up and move it a bit on the z-axis. And here, we've got some more floating
[24:39] geometry as well. And we can just delete that and then fill this gap with a grid fill.
[24:44] Ultimately, we're going to remesh everything. So it is important that those meshes are watertight,
[24:49] so that there are no open caps. Here, I'm just moving this geometry a bit in edit mode and with
[24:55] x-ray mode enabled, just to make it a bit more aesthetically pleasing. And for this piece,
[24:59] sometimes in edit mode, it's a bit difficult to symmetrically adjust things. So in sculpt mode,
[25:04] it can be easier just by using the grid brush or just using something like the clay strips brush,
[25:09] for example, just to push the geometry in. And of course, by having y symmetry enabled,
[25:13] you can nicely symmetrize everything. So I'm quite happy with the curves now. So what I'm going to do
[25:19] is I'm going to create a duplicate of this collection. So I'm just going to rename this to
[25:23] mesh, because this is what will be all the meshes. And I'm going to turn off the curve collection,
[25:27] select everything and then hold shift and make sure you click on one more thing so that it has
[25:31] the yellow outline like this, and then right click and convert to mesh. And that does two things.
[25:36] First, obviously, it converts everything to a mesh, but also it applies any modifier that was
[25:41] still on that object. And so in edit mode, let's see how the geometry looks. So the easiest way
[25:47] to do this is by turning on the wireframe option. And we can see, for example, this does not have
[25:52] as dense geometry. So I'm just going to add a subdef modifier and apply it. And I'm going to do the
[25:57] same for this. So control one and then control eight to apply it. And same for this handle here,
[26:02] control one and then control a. And by doing that, I'm just making the topology a bit more equal
[26:08] everywhere. So when I subdivide it all together, it doesn't need as many subdivisions to get a smooth
[26:14] result. And I don't get ultra dense parts somewhere. And I'm just going to select everything and press
[26:19] control J now to join everything to one object. And I'm going to set the origin to the 3d cursor.
[26:24] Now we do need to apply the rotation and the scale just in case. And just a quick check to see if
[26:29] everything is really symmetrical. And one more thing before I remesh everything is I'm just going
[26:33] to close some of these little gaps that you see here and there. And to do that, I'm going to go
[26:38] to X-ray mode and wireframe mode and just selecting and dragging some vertices with proportional
[26:43] editing enabled, just until those gaps are closed. So here's another one. For example, we just need
[26:47] to drag this up a bit and then it's closed. And that prevents the remeshing from running into trouble.
[26:53] And I'm going to add a subdef modifier and that reveals more little gaps between those objects.
[26:58] And it's important to shade it flat because when you're going to be 3d printing something,
[27:02] what you see flat shaded is what will come out of the printer more or less. And so I'm going to
[27:07] just quickly close a few more of these gaps that are revealed by adding the subdef modifier. The
[27:12] reason we see more gaps is because the subdef modifier kind of shrinks the volume of the topology
[27:18] and it will make it more obvious to see some more gaps that we couldn't see without the subdef
[27:23] modifier. And so here I think this is a bit ugly. So I'm just quickly move some of these
[27:27] vertices to close that gap between those two curves. And I think with that, that looks a little
[27:33] better already. So we definitely need enough subdef division levels to make it look nice and
[27:38] smooth without smooth shading. So it's flat shaded, but it still looks smooth simply because it has
[27:44] so many subdivisions. And at this point, we have quite a dense mesh with millions and millions of
[27:49] triangles. So this might become a bit sluggish on your computer if it's an old computer. So I really
[27:54] recommend that you save iterations of your file when you're working in this workflow. Because the
[27:59] higher the density of your geometry, the more likely blender is to crash. So now I'm going to apply
[28:04] the subdef modifier and I'm going to add a remesh modifier. And at this point, I really hope you
[28:09] listened to me when I said you had to save backups because remeshing an object this big can take a
[28:14] long time and maybe your computer will crash. So I'm doing a voxel remesh and I'm experimenting
[28:19] with the voxel size. And please be careful not to enter too small a voxel size right from the bed.
[28:24] So I'm just trying to find the right voxel size to have a lot of detail. And it seems that 0.03 in
[28:31] this case is what I need. And so now as you can see, everything is kind of merged together. So now
[28:36] we really have one watertight object. However, one big mistake I made is that I also remeshed the
[28:42] star object, which will cause some issues later. But that's good. Then I can show you how to solve
[28:47] that. So now I've applied the remesh modifier. So now we really have millions and millions of
[28:52] triangles. But it means that in Skulled mode, we can make it nice and smooth where we want. So I'm
[28:57] just going to select the smooth brush. So this is the smooth brush. And just by using my mouse,
[29:02] I'm not going to use a graphic tablet or anything because I'm not going to do that much sculpting.
[29:06] I'm just going to smooth out some parts, especially the parts where the geometry merged into other
[29:12] geometry. And as you can see, the smooth brush does a really nice job of that. So where you smooth
[29:17] these things is really up to your own artistic interpretation, I guess. I'm just trying to
[29:23] keep the peaks of the curves really sharp. So wherever possible, I'm not touching those. I'm
[29:27] just touching the areas in between. And for example, here where some curves come together,
[29:31] I think it looks nice when they kind of get smoothed out like that. It just makes it look kind
[29:36] of like it's all kind of cast from metal in one big mold or something. And here also, I'm going to
[29:41] make these transitions smooth between this flat area and these curves. I think that looks nice.
[29:47] And also the part where one curve enters another curve, I think that looks nice when it's smoothed
[29:51] out as well. Just remember, of course, to make sure that the symmetry is enabled for that brush,
[29:56] otherwise you're only doing it on one side. And if you accidentally smooth a part that you don't
[30:00] want to smooth, just press Ctrl Z to undo. And if you want to make the brush smaller, you can press
[30:06] F and then just change the radius like that. So as you can see, this area looks a bit wonky,
[30:10] and we will use a curve from the curves collection later to fix that. Now, I just want to have this
[30:15] flat circle. I don't want to have that star object as part of the mesh. So that was a mistake I made
[30:20] earlier. So I'm going to have to remove that star from it. And here this part, I want to replace that
[30:26] by a curve. Fortunately, I saved the curves collection so I can easily just grab a curve
[30:31] from there. So let me just enable that curve collection again, take this curve and shift
[30:35] the interpolated and press M and move it to the mesh collection. And let's turn the mesh collection
[30:40] back on. So now we have that curve in the mesh collection. And we can kind of adjust it to make
[30:45] a nicer transition between the staff and that curve that comes out of it. So I'm just scaling up with
[30:50] Alt S just like we did before and just kind of adjusting that shape. And then we can create a
[30:55] nicer transition between those two parts. And we don't need all of these vertices. So we can
[31:00] actually just delete part of it. We can delete all of these. And then we just have the vertices that
[31:06] we need. So we can scale this down as well. And we can convert this piece to a mesh by pressing
[31:13] Ctrl A and choosing visual geometry to mesh. And before we merge them together, let's use the
[31:18] Grab Brush and just adjust this shape a little bit more. And I think the Grab Brush is really great
[31:23] for adjusting shapes like this. And let's just quickly check that it's symmetrical as well.
[31:28] And so now let's select both of these pieces and press Ctrl J to join them. Now there are a couple
[31:32] of ways we can remove this star object before we remesh everything. So one is we can add a
[31:37] cutter object to create a boolean. The problem is that when you have millions and millions of
[31:42] vertices, doing a boolean like this is a bit difficult and doesn't always work. And it takes a
[31:48] very long every time you change an option. And in fact, in this case, when I tried the
[31:52] self-intersection option, blender just crashed. So another way to try it is by using a mask.
[31:58] So I just masked out the star object. And then once you have masked something, you can use the
[32:04] Fair Positions tool in Skulled Mode. And Fair Positions, it flattens everything that is affected
[32:12] by it. So in this case, anyway, I should have inverted the section, but it didn't work anyway,
[32:16] just crashed blender again. And so the third solution, and that's the one that is more reliable
[32:21] when you have a lot of geometry, is to use this kind of box selection, select the whole part,
[32:26] and make sure you select it in X-ray mode, and then symmetries it. And of course, make sure you
[32:30] have the right axis. So in this case, I needed to symmetries it from plus Y to minus Y. And let's
[32:36] go back to object mode and solid view. And then you can see actually that it worked very well.
[32:41] It just created this little issue, but we were going to remesh it anyway. So let's do that real
[32:46] quick. And let's go and pick the resolution from the object in Skulled Mode, and then just click on
[32:51] remesh. And that might take a little while. But as you can see, it has remeshed nicely. And then we
[32:56] can just smooth this area out. And now the problem is invisible. So now the star is removed, as you
[33:02] can see. And let's go and go back to that Curves collection where the original star object was.
[33:07] And let's finally put it in its own collection. So select all press M, new collection, and call
[33:12] it star. And let's turn the mesh collection back on. And so now we have that as a separate object.
[33:17] And we can add a mirror modifier to the star as well. And let's use the empty as the mirror object.
[33:22] Then to copy the mirror modifier only to all of these other objects, just select them and select
[33:27] the one with the mirror modifier last, press Ctrl C, and then copy selected modifiers. And then just
[33:32] choose the mirror modifier. I have that option because I have the Copy Attributes extension
[33:38] enabled. Let me show you. So Copy Attributes, that way you can copy specific attributes like a specific
[33:44] modifier. And then we need to just quickly fix this area, of course, because it's been remeshed,
[33:49] we can now smooth this out and make a nice transition. And of course, make sure that the
[33:54] Y Symmetry is enabled. I'm just adjusting the shape a little bit with the Grab Brush,
[33:58] and then smoothing out the transition. So now I'm smoothing out this sharp part to the rounded
[34:03] part. And as you can see, that creates a nice transition. And if necessary, we can use the
[34:07] Grab Brush to do some final tweaks. And then finally, to bring the file size down a bit,
[34:11] and to make sure that the file can be 3D printed, we're just going to add a Decimate modifier to
[34:17] it. Now, of course, in real life, you would have to check what kind of size you can print on your
[34:22] 3D printer. And you would have to split the object into chunks accordingly, and create a way to connect
[34:27] them as well. But that is a bit outside of the scope of this video. So instead of trying to find
[34:32] the exact value in one Decimate modifier, I'm just halving each time by 50% and applying the
[34:37] Decimate modifier and adding another one at 50% until I get to the right amount of decimation.
[34:43] That way it's a bit faster in Blender, otherwise you have to wait a long time. Even so, with the
[34:48] first decimation, I had to wait quite long, to be honest. So we went from something like 30 million
[34:53] triangles to something like 300 or 400,000 triangles. Still very dense mesh, but at least it's more
[35:00] manageable. And of course, don't forget to save. So yeah, thanks a lot for watching all the way to
[35:05] the end. I hope you find it interesting. If you have something that you want me to model, please
[35:09] send it to me either by email on my website, 3dsecrets.com, or just comment. But on YouTube,
[35:15] if you comment with a link, then it might get hidden automatically. So probably either on Twitter
[35:21] or some other social media, it is more easy to ask me that kind of thing. And with that,
[35:26] thank you for watching and see you in the next one.



---

## Captured Frames

- [1:14] tutorials/frames/how-do-you-model-that-kingdom-hearts-keyblade---blender-secrets/frame_000.jpg
- [4:00] tutorials/frames/how-do-you-model-that-kingdom-hearts-keyblade---blender-secrets/frame_001.jpg
- [5:35] tutorials/frames/how-do-you-model-that-kingdom-hearts-keyblade---blender-secrets/frame_002.jpg
- [13:19] tutorials/frames/how-do-you-model-that-kingdom-hearts-keyblade---blender-secrets/frame_003.jpg
- [18:04] tutorials/frames/how-do-you-model-that-kingdom-hearts-keyblade---blender-secrets/frame_004.jpg
- [18:36] tutorials/frames/how-do-you-model-that-kingdom-hearts-keyblade---blender-secrets/frame_005.jpg
- [32:56] tutorials/frames/how-do-you-model-that-kingdom-hearts-keyblade---blender-secrets/frame_006.jpg
- [34:53] tutorials/frames/how-do-you-model-that-kingdom-hearts-keyblade---blender-secrets/frame_007.jpg

---

## Structured Notes

### Core Technique
Building an ornate, freeform organic/hard-surface shape (a Kingdom Hearts Keyblade) as a bundle of individually hand-shaped bevel curves and box-modeled mesh pieces traced directly over a reference image, then unifying everything at the end via Convert-to-Mesh → Join → Remesh → Sculpt-smooth → Decimate — a "model loose, unify late" workflow aimed at 3D printing (not quad/subdivision-ready topology).

### Summary
A complex organic-swirl weapon design is built piece by piece rather than as one continuous mesh. Each curl/tendril starts as a 2-vertex edge subdivided a few times then converted to a Curve (preferred over a native Bezier path for more predictable control-point behavior), given bevel Depth for thickness, and shaped to match a reference image using Alt+S (radius scale) per control point — keeping vertex counts low keeps curves smoother and easier to control. A separate small circular curve, scaled down on two of its points, is used as a custom **Bevel Object** on the main curves to add a non-round ridge/edge detail along their length. A Mirror modifier (axis-dependent, needs an Empty as the mirror object, and its Merge option can visibly break adjacent-but-not-touching curves if left on) handles symmetric parts; most curls are unique per side and just duplicated + reshaped instead. Harder shapes (rings, box-modeled sections, the star guard) are built as ordinary meshes: primitives collapsed to a vertex and extruded, cylinders capped with Grid Fill, Ctrl+R loop cuts to approach curved forms, and a **Simple Star** primitive (from the Extra Objects add-on) with per-face Inset/Extrude to create the decorative guard. Trickier one-off shapes get converted from curve to mesh specifically to gain per-vertex control that curves don't offer, then Symmetrize is used to mirror the fix-ups. At the end, everything is Converted to Mesh, joined (Ctrl+J), and unified with a Remesh (voxel) pass; a few Sculpt-Mode techniques — Smooth (to blend seams), a Mask + Fair Positions attempt (found unreliable, crashed Blender on this model), and ultimately X-ray box-select + **Symmetrize** as the reliable way to delete/rebuild half of a messy merged region — clean up merge artifacts. A Decimate modifier is applied repeatedly at 50% (rather than solving for one target ratio directly, since large-percentage single passes are slow/unstable) to bring the mesh from ~30 million triangles down to a 3D-printable ~300–400k.

### Key Steps
1. Find multiple reference images; pick one with a clear side view. Import it into Blender, add a reference-sized cube (author estimated ~1.5m) to scale the image against, then disable the reference image's selectability so it can't be grabbed by accident.
2. For each curl: start with a Plane, delete down to 2 vertices (one edge), subdivide a few times in Edit Mode, then Convert To → Curve. Give it Bevel Depth (avoid exactly 0 — use a tiny nonzero value instead, since 0 can break remeshing later) and make sure end caps are closed. Reshape with Alt+S per point (curve radius scale, not object S) and add a Subdivision modifier for smoothness. Favor as few control points as the shape allows — fewer points keeps curves rounder and more predictable; subdivide an existing segment (right-click → Subdivide) only when a spot genuinely needs more control.
3. For a non-round ridge/edge along a curve: create a second small curve (e.g. a circle), scale down two of its points asymmetrically, and set it as the main curve's **Bevel Object** (Curve properties → Geometry → Bevel → Object) instead of using the simple round bevel depth.
4. Mirror symmetric curls with a Mirror modifier set to the correct axis, using a dedicated Empty (scaled down via the modifier's own panel, not by pressing S on the empty directly, which breaks the mirror math) as the Mirror Object. Watch for the modifier's **Merge** option silently snapping/distorting nearby-but-distinct curve endpoints — disable Merge if curves need to sit close without interacting.
5. Build rigid/mechanical sub-parts (rings, grips, box shapes) as ordinary meshes: collapse a primitive to one vertex and extrude with E to rough in a shaft; use a capless cylinder for grip shapes, Ctrl+R loop cuts to approximate curvature, and Ctrl+F → Grid Fill to close circular end caps. Classic box modeling (extrude, scale, loop cuts, then a Subdivision modifier) works fine for simpler mechanical shapes.
6. For the decorative star guard: enable the **Extra Objects** add-on, add its Simple Star mesh primitive, keep only the front face, use F to merge stray triangulated faces into clean quads, then Inset (I, pressed twice or with the "Individual" checkbox) each point face individually, extrude the resulting loops, scale to individual origins (not the median point) for a faceted look, set the origin to the star's center (Shift+S → Cursor to Selected → Origin to 3D Cursor) before mirroring, and finish with a Bevel modifier so the edges catch light like a real faceted object.
7. When a curve's control-point limitations get in the way of a specific irregular shape, Convert it to Mesh (temporarily lowering the bevel object's resolution first keeps the resulting mesh light), edit at the vertex level (Proportional Editing helps for organic pulls), then use **Symmetrize** (favorited in the Quick Favorites menu) to mirror one-off edits — set the object's origin to center first or Symmetrize won't work correctly.
8. Final unification: Convert every remaining curve/mesh piece to mesh, select all, Ctrl+J to join into one object, then Remesh (voxel, resolution picked interactively) to fuse everything into one continuous manifold suitable for sculpting and printing.
9. Clean up remesh seams/artifacts in Sculpt Mode primarily with the **Smooth** brush; a Mask-selection + **Fair Positions** approach was tried for isolating and flattening an unwanted leftover shape but proved unreliable (crashed Blender twice in this session) — the more dependable fix for large messy regions was X-ray box-select the whole half, delete it, and **Symmetrize** from the clean side instead.
10. To reduce a print-ready mesh's triangle count without long single-pass waits, apply a **Decimate** modifier repeatedly at 50% (Apply, add another Decimate at 50%, repeat) rather than solving for one large target ratio in one pass — this took the model from roughly 30 million down to ~300–400k triangles.

### Nodes / Settings
- Curve setup: Edge → Convert to Curve, Bevel Depth (nonzero, small if you want a fine tip), Bevel Object (secondary curve, for non-round ridges), Resolution, + Subdivision modifier
- Mirror modifier: Axis per-part, Empty as Mirror Object (scaled via modifier panel), Merge toggle (can distort near-but-distinct geometry)
- Add-on: Extra Objects (for the Simple Star primitive)
- Mesh tools: Ctrl+R (loop cut), Ctrl+F → Grid Fill, F (merge faces to quad / close n-gon), I (inset, toggle Individual), Shift+D (duplicate), Alt+S (curve radius scale), Symmetrize (mesh menu / Quick Favorites)
- Sculpt Mode: Smooth brush, Mask + Fair Positions (unreliable on dense meshes), Remesh (voxel), Grab brush (shape adjustment)
- Finishing: Decimate modifier, applied repeatedly at 50% rather than one large-ratio pass
- Scene scale set to centimeters for small-object precision; grid scale reduced (e.g. 0.01) to match

### Difficulty
Advanced — no single step is conceptually hard, but the workflow requires judgment across dozens of individually hand-fit curve/mesh pieces and troubleshooting remesh/mirror edge cases as they come up.

### Blender Version
Not specified.

### Tags
procedural, organic, advanced

---

## Related Tutorials
- [How do you model that? Wrench - Blender Secrets](how-do-you-model-that-wrench---blender-secrets.md) — shares procedural, advanced; same "How do you model that?" reference-to-model series, applying the same box-model-over-reference approach to a mechanical tool (pliers) instead of an organic fantasy weapon.
