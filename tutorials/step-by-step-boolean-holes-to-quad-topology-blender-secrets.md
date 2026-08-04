---
title: Step by Step: Boolean Holes to Quad Topology | Blender Secrets
source: YouTube
url: https://www.youtube.com/watch?v=pe-8GiRCLmM
author: Blender Secrets
ingested: 2026-08-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/step-by-step-boolean-holes-to-quad-topology-blender-secrets/
frame_count: 0
frame_status: pending-selection
---

# Step by Step: Boolean Holes to Quad Topology | Blender Secrets

**Source:** [YouTube](https://www.youtube.com/watch?v=pe-8GiRCLmM)
**Author:** Blender Secrets
**Duration:** 11m51s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py step-by-step-boolean-holes-to-quad-topology-blender-secrets <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Cutting geometry using booleans works well for more complex holes rather than just circular ones.
[0:06] If you want to use the result in a subdivision workflow, you'll need to read-apologize it.
[0:11] Let me show you a way to do that without too much manual effort.
[0:15] All you need is an object that functions as a cutter.
[0:18] Make sure that the object doesn't have a non-uniform scale, because it makes the boolean operation less reliable.
[0:25] If this is the case, apply the scale.
[0:28] Now you can see in the option panel that the scale is 1.
[0:32] You also want to make sure that both objects are not too dissimilar in terms of complexity.
[0:37] To be able to see the topology of both objects better, we can enable wireframe in the viewport overlays.
[0:46] If we get a boolean cut now, you will see that it looks fine at first glance.
[0:52] But once we apply the modifier, it becomes clear that we have too many vertices,
[0:56] which we cannot connect to anything if we want to read-apologize this.
[1:01] In this case, we don't have any horizontal loops on the cylinder, which also will make cleanup more difficult later.
[1:07] So I'll add some loops by pressing Ctrl-R, and then I'll increase the amount of loops by scrolling the mouse wheel up.
[1:17] And just right-click to cancel any transformation.
[1:21] I'll also make a duplicate of this cylinder while it still doesn't have any holes in it.
[1:29] This will come in handy later.
[1:31] Rename it in the Outliner so we can find it easily later.
[1:36] And disable its visibility.
[1:43] Now to do the boolean operation, we just select the cutter, then hold Shift and select the cylinder.
[1:48] Then press Ctrl and Minus on the numpad.
[1:54] If it just zooms out, you are pressing the Wrong Minus key. You really need the one on the numpad.
[2:01] If you don't have a numpad, you can enable Emulate numpad in preferences.
[2:09] Alternatively, you can use the boole-dool menu in the Option panel.
[2:13] If the boolean operation fails, you can try the Fast Solver instead.
[2:23] Or moving the cutter object slightly to a different location can also make it work.
[2:30] Apply the modifier.
[2:33] We can delete or hide this cutter object.
[2:38] Typically, there will be too many vertices after a boolean operation.
[2:43] This would cause issues when adding a Subdiv modifier.
[2:49] We can take care of most of these with a Weld modifier.
[2:53] We can see the modifier result in Edit Mode by enabling this button.
[2:58] Just increase the distance value until it looks like the extra vertices are merged together.
[3:06] And then in Object Mode, apply the modifier.
[3:10] Let's enable Symmetry and the Auto Merge Verges option.
[3:16] By pressing G twice, we can slide edges or vertices to clean up the boolean hole further.
[3:25] Just be careful that you don't go too far, you don't want to alter the shape of the hole too much.
[3:32] Another thing you can do is just delete all these interfaces.
[3:40] Select all these boundary edges, right click and choose Bridge Edge Loops.
[3:46] Make sure you really select them all, otherwise you'll get this kind of bad result.
[3:53] That's already an improvement, but if you want to use a Subdiv modifier, we need to create a face loop around the hole.
[4:01] To do that, I will first select these edges again.
[4:04] You can hold CTRL and select edges to select everything in between.
[4:10] I could mirror this particular object, but in this case I'll just manually select these edges as well.
[4:16] Then press CTRL B to bevel.
[4:21] In the last operator panel, we can increase these segments to 2 and set the shape to 1.
[4:27] This way we get edge loops on both sides of our original selection without changing the shape.
[4:33] Then we can fine tune the width value.
[4:36] We can slide these inner loops a bit further in.
[4:44] Press CTRL B and scroll the mask wheel up to add some edge loops along the bridged geometry.
[4:51] That didn't look uniform enough, so I'll undo it and add more loops this time.
[4:57] That's better.
[4:59] Of course this is still not ideal geometry, we've got some triangles and any other edges.
[5:05] these are few active icons around in a hole.
[5:09] To improve this first, I'll select the sharp edges.
[5:14] Deselect any edges that shouldn't be sharp.
[5:18] Then crease them with Shift E and one on the numpad, this keeps them sharp when the object has a Subdive modifier.
[5:27] Also let's deal with these caps by pressing I to inset them.
[5:31] here is fine because it's perfectly flat, but if we want to have quads here as well we can first
[5:36] delete these caps and then use grid fill to fill the hole with quads. The offset value rotates the
[5:42] fill geometry. Press shift E and minus 1 on an unpad to remove decreasing of the inset edges.
[5:51] This rotating isn't necessary, it's just satisfying to do for some reason.
[5:56] Makes it seem more perfect, even if nobody will ever notice.
[6:02] Now for our quads we can use a sub-diff modifier and then apply it.
[6:08] Now we have all quads but there's an issue here. This is called overhang.
[6:15] Let me just undo that sub-diff modifier.
[6:19] I'm just checking if there's any double vertices here by wiggling these
[6:23] vertices around a bit. Seems fine, so what we can do is grease this edge and that will help
[6:28] it preserve the sharpness of the corner. We can slide this vertex down to distribute the geometry
[6:38] a bit better to further get rid of any issue here. Of course you can just use the symmetry or mirror
[6:44] modifier here, there is no need to do it on both sides like what I'm doing. I will enable shade
[6:49] auto smooths. And now I'll apply the sub-diff modifier again to see if the result is better this
[6:55] time. There we go, now we have all quads topology. Of course by using this trick we have increased
[7:01] the density of the model as well. But since we started out fairly low poly the density now is
[7:06] still okay. It depends also on what the ultimate goal is of your model. Let me just turn off wireframe now.
[7:16] And I'll remove the creasing as the edge sharpness is now taken care of by the geometry.
[7:21] Now one thing that still bothers me is that the geometry around the hole is not following the cylinder
[7:29] shape perfectly. So we're going to use the shrink wrap modifier to get the perfect surface back.
[7:36] First I'll select all the geometry inside the hole.
[7:43] Add a vertex group and remove the selection from it. Then invert the selection and assign that to the
[7:49] side. It looks like I need to add this loop to it as well.
[7:58] In white paint mode you can see what the vertex group looks like.
[8:05] Now we can add a shrink wrap modifier.
[8:11] And we'll use this duplicate cylinder as its target. But first let's make sure it is smooth.
[8:19] Select and crease its sharp edges. And then add a sub-diff modifier with enough levels to make it
[8:25] really smooth. Then we can set that cylinder as the target of the shrink wrap modifier.
[8:38] And use the vertex group to limit which vertices the modifier uses.
[8:42] Can you see the difference the shrink wrap modifier makes?
[8:45] This math cap will make it more obvious. You can see the distortion of the geometry around the hole
[8:54] and the shrink wrap modifier is turned off. Now it's perfect. If you're happy with this level of
[8:59] geometric density you can just apply the shrink wrap modifier now. The only way to get a better result
[9:06] would be to manually retopo it or to use the quadrimesh or plugin by exo-side.
[9:11] If you want a lower poly result you can add a decimate modifier.
[9:18] Set it to unsubdified and use an even number.
[9:24] In this case it seems two is the highest we can go before distorting the geometry too much.
[9:31] To apply both modifiers at once, apply visual geometry to mesh. Now we have this result.
[9:37] It's no longer all quads but it'll work just fine. You can select all and press Alt J to
[9:42] convert some of them to quads if possible. So that's how you do a boolean cut and
[9:48] clean up the resulting topology without having to do a lot of manual retopology work.
[9:54] Of course you can still do some manual work to make this even better.
[9:58] I've added a mirror modifier to save some time.
[10:01] First we can start to clean up this part because there are a lot of edges that we don't really need.
[10:05] Just select them and dissolve them with Ctrl X.
[10:12] Let's also simplify the hard shape by dissolving some edge loops here.
[10:16] Using the knife tool we can add an edge here and then dissolve this edge to turn this into a quad.
[10:27] We can also mirror it on the Y axis in this case.
[10:32] In X-ray mode we can select the vertices through the entire model and improve the shape of the
[10:37] hole. We could turn these triangles into quads at this stage for example by beveling some vertices.
[10:45] And then sliding them to merge with other vertices. However although this is not a quad,
[10:50] this interrupts the vertical edge flow and in this case I think keeping the triangles is better.
[10:57] Let's use this hard cutter shape as reference to improve the hole shape.
[11:03] In X-ray mode and with the sub-diff modifier resolved visible in edit mode we can fine tune the shape.
[11:11] So there you have it, a relatively low effort and repeatable workflow for adding boolean holes
[11:16] and cleaning up the topology. In case you're wondering if it's okay to have a couple of triangles
[11:21] and ancons, yes it's fine as they will become quads anyway once they are sub-diffided.
[11:29] Because we changed the hole shape I will use the shrinkwrap method
[11:32] to make sure the geometry remains cylindrical. The important thing is that we have these nice
[11:37] loops of faces around the hole which will protect the boundary.



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
