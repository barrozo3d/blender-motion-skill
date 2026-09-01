---
title: Monster Sculpting | Full Process | Blender Secrets | Stranger Things Vecna
source: YouTube
url: https://www.youtube.com/watch?v=s6GQv6eZVms
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Blender 3.5.0 Beta -- observed in frame_000"
tags: [organic, procedural, materials, advanced]
extraction_status: complete
frames_dir: tutorials/frames/monster-sculpting-full-process-blender-secrets-stranger-things-vecna/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Monster Sculpting | Full Process | Blender Secrets | Stranger Things Vecna

**Source:** [YouTube](https://www.youtube.com/watch?v=s6GQv6eZVms)
**Author:** Blender Secrets
**Duration:** 21m48s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] OK, so I have this reference image from Titan Troll Miniatures from CGTrader
[0:09] and this is just to give me some reference of the Verna monster from Stranger Things
[0:15] I'm not going to recreate it, just use it as an inspiration base
[0:20] So let me get a base mesh
[0:30] and let me join these
[0:43] set the origin to the 3D cursor
[0:47] and I just want to have the bust part so I will remove the rest
[0:52] I think I can just use a boolean
[1:00] and maybe also the arms
[1:30] and I will just symmetrize this real quick
[1:42] OK, now we can go to Scott Mode and just remesh this
[1:48] I don't need those facets
[1:53] and do a focus on remesh
[1:56] preview R and then Ctrl R
[2:00] that's pretty low, let's try that again
[2:06] you hold down shift you can change values in smaller increments
[2:14] that didn't work, so let's use a remesh modifier instead
[2:21] let's undo
[2:24] it's not undoing for some reason
[2:37] so let's use a remesh modifier then
[2:43] and apply it
[3:14] OK, now in Scott Mode I can
[3:21] use some brushes
[3:44] these areas that are problematic
[3:48] I will just smooth them out and then remesh
[3:53] because otherwise we can never get it right there
[4:02] so remeshing is taking care of those issues
[4:13] now we can just use the claystitch brush
[4:17] to add some volume, let's use symmetry for that
[4:35] this seems he doesn't really have ears
[4:39] let me just remove those I guess
[4:51] and just do a quick remesh
[5:01] it looks like when I do this it's destroying the back of the mesh
[5:06] so I will need to check
[5:12] front faces only, then that doesn't happen
[5:25] let me add a bit of volume back here
[5:37] OK, let me just file
[5:42] smooth out this seam a bit
[5:54] now to add these veins I could use a draw brush
[5:57] but instead I'm going to use another technique which is not sculpting
[6:05] I'm going to use some curves, so I'll add a curve
[6:09] a Bezier curve
[6:12] and in edit mode select all and then just delete the vertices
[6:18] so now I still have my curve selected but it doesn't have any vertices
[6:25] and as you can see in the tool panel in edit mode I have the draw tool here
[6:31] and up here you have some options
[6:35] you have cursor and surface
[6:38] so I can use that to draw on top of the surface
[6:43] it's very close to the surface so sometimes it's clipping so that's why you cannot see it very well
[6:49] but if I draw it and I add some thickness by increasing the depth value
[7:01] then I get this kind of stuff
[7:06] if we open the tool panel we get the draw tool options here
[7:11] and we can set the taper, start and values to 1
[7:16] and then when we draw a curve
[7:19] and we need to increase that
[7:23] we need to increase the depth a little bit more than
[7:28] then we get this kind of sausage with tapered ends
[7:34] like what you see in the reference image as well
[7:38] so now I can just draw those all over the place
[7:43] so let's do that
[7:53] I guess I'm making them a little bit too wavy so they should be a little bit more simple like this
[8:02] we can still adjust these later because they are curves
[8:05] so we can select these points and scale them up or move them around
[8:12] let's see what's that
[8:14] just like this
[8:17] they do overlap each other which is nice
[8:23] this is much faster than if you were to scope this
[8:45] and if you don't like something you can just press Ctrl Z and undo
[8:50] and just draw it again
[8:56] okay I think that's an evanes
[9:06] now we can adjust these a bit but actually
[9:11] they're fine, they're not perfect but it's supposed to be something organic so
[9:16] I'm not going to bother with changing it too much but if you want you can select these
[9:22] and you can rotate them
[9:28] rotate, move them
[9:32] you can scale them up
[9:35] like maybe some of these we can make them a bit fatter
[9:39] just thinner
[9:44] and the short key for that is Alt S, confusingly
[9:53] they shouldn't all be the same
[9:55] we can also just select randomly
[10:01] maybe a little bit less than this and just scale some of these down randomly
[10:07] let me invert that selection
[10:10] and reduce it and then scale some of them up
[10:14] to give it a bit more of an organic random feeling
[10:22] and now let me just select them all
[10:26] and then we can go back to the previous selection
[10:32] okay so I've joined them
[10:35] and now I can convert them all to mesh
[10:38] I hope, yep
[10:40] so now this is all one mesh
[10:44] and I can just join these two together
[10:47] and then in sculpt mode
[10:50] we can do a voxel remesh again
[10:53] and then do a voxel remesh
[10:58] and now it's a part of that mesh
[11:01] so of course now I can clean it up a bit
[11:07] and make sure it's a bit more integrated in the rest of the model
[11:16] and of course we can also add to that with the place strips brush
[11:23] looks like I still had symmetry on that's not good
[11:25] because it's a very asymmetrical model
[11:42] okay it's starting to look good
[11:45] alright
[11:49] how does that look with a mad cap?
[11:53] I guess he doesn't have a mouth anymore
[11:56] so let me add his mouth back
[11:59] let me see
[12:01] can you crease?
[12:04] I guess and
[12:06] use some smaller clay strips
[12:10] to build that up again
[12:17] and now I can add some more
[12:19] to the base
[12:28] I guess I should turn symmetry back on
[12:31] it's one of those things that's easy to forget
[12:34] for the rest I'm going to use some
[12:37] alpha textures to do the details
[12:58] and these are some
[13:01] alpha textures that I purchased
[13:04] from ArtStation
[13:09] actually let me just open a tool panel that's easier
[13:13] so what I'm doing is I just make a copy of this
[13:16] and then I click on new texture
[13:20] I have folder with all kinds of alpha textures
[13:24] and I just bought these
[13:26] these are from Nicholas Swangudow on ArtStation
[13:29] he makes really nice alpha textures
[13:35] I use the TIFF versions
[13:38] he sells both video brushes
[13:41] and also in this case the alpha textures
[13:44] which are just images black and white hide maps
[13:47] and I chose the TIFF files because it's easy to preview them
[13:50] in the browser
[13:53] so let's just start with the first one
[13:59] and we want this to be
[14:02] area plane
[14:04] mapping
[14:06] front faces only
[14:10] and I want to drag dot for the stroke
[14:13] so that we can drag it to where we want
[14:16] the falloff with a alpha texture should just be constant
[14:19] because you want to use the whole image
[14:22] we can set it up so that the rotation is random
[14:25] but let me see
[14:28] if you want to rotate something
[14:31] an alpha texture like if you don't want it to be like this
[14:34] you can always press CTRL F
[14:37] and then you can change the angle
[14:40] so for example I can
[14:43] put it above his brow or something
[14:46] and I notice that I don't have enough resolution by far
[14:49] so I am just going to add a
[14:52] multi-res modifier
[14:55] and simplify that one time
[14:58] which already gives us
[15:01] 5 million vertices so
[15:04] that's okay
[15:07] let me just quickly
[15:10] set it to shade smooth because I think that was
[15:13] not the case
[15:16] mmhmm that looks alright
[15:19] and we can change the size of the alpha
[15:22] with F radius
[15:25] that's a bit too much
[15:28] okay cool
[15:31] so now we are just going to place some
[15:34] alpha textures
[15:37] and I think I will use the random
[15:46] profile
[15:49] you can just adjust
[15:51] the intensity
[15:54] even alpha is too strong
[15:56] you can also press Shift F and just reduce
[15:59] the intensity
[16:02] like this is just a complete one
[16:05] this is just a strength of one that's obviously too much
[16:08] so you can reduce it to say 0.3ish
[16:11] and
[16:14] Of course you don't want to use the same alpha too many times because it will be very obvious.
[16:29] So let's load another texture.
[16:31] I guess you can create another alpha by clicking here and then you have all those alphas but
[16:37] in this case I'm just going to change the texture.
[16:58] I'm just going to use them all until I have something cool.
[17:02] So save sometimes, very very important.
[17:21] So these appear to all be like cut since stuff and I want to have some little bit more
[17:26] monstery alpha. So like this one. This looks like some kind of mutated monster texture.
[17:41] I don't want it to randomly rotate in this case.
[17:43] Let me reduce the strength and increase the size. That's interesting.
[18:13] I wonder if we can use this for his eyes.
[18:35] When you press ctrl z in blender sometimes it will undo the settings in the interface
[18:41] oddly enough. So we have to re-enable symmetry.
[18:47] And what's creepier if the eyes are close together.
[18:51] I guess we can always stretch them out a bit like this.
[18:58] Make him look a bit more angry.
[19:04] It looks a bit silly. I don't know. I'm not too happy with that.
[19:08] Let me see if I can find a better texture for that.
[19:24] I don't know. The eyes are not a big success I guess.
[19:31] Let's see. I think we've already got quite a lot of detail now.
[19:46] I think what we need is more veins in those creepy.
[19:53] I think we need more veiny stuff. So let me see if I can find another good
[20:00] of a texture.
[20:04] I think this one was really good. We can get a bit more mileage out of this.
[20:16] Not too strong.
[20:22] I'm just going to place lots of veins everywhere.
[20:25] Like this. Just as long as I rotate the alpha you won't really notice.
[20:33] It's the same one over and over again.
[20:37] I hope.
[20:46] He uses really good skincare products on his back but not in front.
[20:56] Maybe add a little bit more stuff in his face I guess.
[21:02] Let me have something good for this. What is this?
[21:18] If you're placing an alpha texture with drag dot like this
[21:24] and you don't like it then you want to undo it.
[21:26] Instead of pressing undo just press escape.
[21:31] That's faster because if you have to wait for undo it takes a couple of seconds.
[21:40] That's good. This is good enough.



---

## Captured Frames

- [0:47] tutorials/frames/monster-sculpting-full-process-blender-secrets-stranger-things-vecna/frame_000.jpg
- [3:44] tutorials/frames/monster-sculpting-full-process-blender-secrets-stranger-things-vecna/frame_001.jpg
- [6:49] tutorials/frames/monster-sculpting-full-process-blender-secrets-stranger-things-vecna/frame_002.jpg
- [7:34] tutorials/frames/monster-sculpting-full-process-blender-secrets-stranger-things-vecna/frame_003.jpg
- [10:44] tutorials/frames/monster-sculpting-full-process-blender-secrets-stranger-things-vecna/frame_004.jpg
- [14:04] tutorials/frames/monster-sculpting-full-process-blender-secrets-stranger-things-vecna/frame_005.jpg
- [17:26] tutorials/frames/monster-sculpting-full-process-blender-secrets-stranger-things-vecna/frame_006.jpg
- [20:22] tutorials/frames/monster-sculpting-full-process-blender-secrets-stranger-things-vecna/frame_007.jpg

---

## Structured Notes

### Core Technique
A full creature-sculpt process (a Stranger Things "Vecna"-inspired monster bust, used as loose inspiration rather than an exact recreation) combining a Human Base Meshes starter, Boolean + Voxel Remesh blockout, Clay Strips sculpting, a non-sculpting technique for tendrils/veins (Bezier curves with a Draw tool, tapered bevel depth, converted to mesh and merged into the sculpt), and purchased ArtStation alpha-texture stamps for skin detail — all narrated informally as a live, iterative process including several real mistakes and fixes.

### Summary
Frame 000 shows the starting point: the free Human Base Meshes add-on's asset shelf open at the bottom (Stylized Male, Base_Mesh_Vecna, Basemesh Grip Bag, Eye, Manor Skull, Primitive Sprite, and several Realistic/Stylized part meshes), with a full humanoid base body selected in the viewport and a Vecna reference photo visible in the corner. Frame 001 shows the bust after Boolean-trimming to just the head/neck/shoulders and cleanup with the Clay Strips brush — a smooth, neutral human head/bust shape, brush palette on the left. Frame 002 shows the vein/tendril technique setup: a Bezier curve (Surface Draw mode, Curve Pen tool) already sculpted into an S-curve resting on the bust's chest, its Geometry panel (Radius, Extrude, Bevel Depth, Taper Object dropdown) open in the sidebar. Frame 003 shows the same curve mid-draw with the active Draw tool's settings open (Method: Surface, Detail/Error, Radius Taper, Fit Method, Corner Angle) — the "cursor and surface" projection mode used to trace tendrils directly onto the bust's geometry. Frame 004 shows the payoff: dozens of tapered, sausage-like curve-tendrils covering the chest and neck, converted to mesh and merged with the bust — reading convincingly as thick, organic veins/tentacles even before any further sculpting. Frame 005 shows the model reshaded in Sculpt Mode after another Voxel Remesh pass integrating the tendril mesh into the base sculpt, with the Draw brush's alpha-texture panel (a wispy tendril-shaped alpha) open on the right. Frame 006 shows the file browser open on a folder of purchased grayscale alpha textures from ArtStation (root-like veins, cracks, scars, elongated scratch shapes) being selected as a new Draw-brush stamp. Frame 007 shows the heavily-detailed final head/neck, dense alpha-stamped skin texture (bark-like ridges and vein networks) covering the face and neck, the active alpha texture's thumbnail and Mapping/Angle/Offset settings visible in the sidebar.

### Key Steps
1. **Reference and base mesh:** use a purchased miniature's reference photo as loose inspiration (not an exact recreation target); add a base human mesh from the free Human Base Meshes asset add-on, join its parts, set its Origin to the 3D cursor.
2. **Blockout via Boolean + Remesh:** trim the base mesh down to just the desired bust region using Boolean operations (removing legs/lower body, optionally arms too); Symmetrize the result if needed for a clean starting symmetry.
3. **Remesh troubleshooting:** in Sculpt Mode, the Voxel Size preview shortcut is R then Ctrl+R to commit — the video shows the author's own remesh attempt initially failing (holding Shift changes the value in smaller increments for finer control) and, when the interactive remesh got stuck, falling back to adding a **Remesh modifier** instead and applying it as a more reliable alternative.
4. **General sculpt cleanup:** use Clay Strips and other brushes to smooth out problem areas before remeshing again — remeshing over unresolved messy geometry tends to bake the problem in, so smooth first, then remesh. Watch for remeshing accidentally destroying backface geometry — enabling **Front Faces Only** on the relevant brush/tool avoids this.
5. **Build up base volume and details:** Clay Strips for adding volume, with Symmetry enabled for a mostly-symmetrical creature (remember to toggle Symmetry off deliberately for one-sided asymmetric details, and back on afterward — easy to forget either way); simple sculpted marks (e.g. removing/re-adding a mouth) via Crease and small Clay Strips brushes.
6. **Non-destructive tendril/vein technique (the video's key trick — not sculpting):** add a Bezier curve; in Edit Mode select all and delete the vertices, leaving an empty curve; with the curve still selected in Edit Mode, use the **Draw tool** (Curve Pen) set to Surface projection mode ("cursor and surface") to trace new curve points directly onto the bust's mesh surface — it can visually clip into the surface since it's drawn so close. Increase the curve's Geometry > Bevel Depth for tube thickness; in the Draw tool's own options, set **Radius Taper Start/End** values to taper the ends to points, producing a tapered "sausage" shape matching the reference's tendrils. Draw many of these freely over the model — overlapping tendrils read as more organic and is fine/desirable. Individual curve points can be selected afterward and moved/rotated/scaled (Alt+S to change a point's local radius specifically) for further adjustment, including deliberately randomizing some thicker/thinner for a less uniform, more organic feel (e.g. select some at random, invert the selection, scale each group differently).
7. **Merge tendrils into the sculpt:** once enough curve-tendrils are drawn, select them all, join them (Ctrl+J) into one curve object, then Object > Convert > Mesh to turn the whole curve network into one real mesh; join that with the base bust mesh (Ctrl+J); in Sculpt Mode run a Voxel Remesh again to fuse the tendril geometry seamlessly into the bust's surface, then clean up/blend the seam with more Clay Strips as needed.
8. **Resolution for fine alpha detail:** add a Multiresolution modifier and Simplify/subdivide enough to reach a workable high vertex count (millions of vertices, e.g. ~5M in this example) — alpha-texture stamping needs real geometric resolution to read correctly, not just shading tricks; Shade Smooth if not already applied.
9. **Alpha-texture skin detailing:** load a purchased grayscale alpha texture (the author uses TIFF-format alphas/brushes purchased from an ArtStation artist, chosen as TIFF specifically for easy browser thumbnail previewing) as a new Draw-brush Texture; set Mapping to Area Plane, Angle to Front Faces Only, Stroke Method to Drag Dot (drag-and-place one stamp at a time), and Falloff to Constant so the whole alpha image is used rather than fading at the edges; optionally randomize the stamp's Angle per-placement for variety, or press **Ctrl+F** mid-stroke to manually set a specific rotation angle for one placement (e.g. aligning a stamp along an eyebrow ridge). Adjust stamp size with F (Radius) and strength with Shift+F — full Strength (1.0) is usually far too strong; around 0.3 gave more controllable, subtle results in this case. Avoid overusing the exact same alpha repeatedly in visible ways — rotate it differently each placement, or swap between several different alpha textures, to avoid an obviously-repeating pattern; swapping alphas can be done by adding a brand-new texture slot or just replacing the current texture's image.
10. **Iterative refinement and troubleshooting notes:** save frequently; Ctrl+Z can sometimes undo interface/setting changes (like Symmetry toggles) in addition to mesh edits, so re-check settings like Symmetry after undo chains; when a just-placed alpha stamp doesn't look right, press **Escape** instead of Ctrl+Z to cancel it — much faster than waiting for a full sculpt-undo to process; the author explicitly iterates through several alpha textures and placements that don't work (e.g. an early attempt at stamped eyes that wasn't successful) before settling on a final look, treating this as a normal, expected part of the process rather than a mistake to hide.

### Nodes / Settings
- **Base mesh:** Human Base Meshes add-on (free asset shelf: base bodies, eyes, skulls, hands, jaws in Realistic/Stylized variants).
- **Blockout:** Boolean (trim to bust), Symmetrize, Voxel Remesh (R for size preview, Ctrl+R to commit, Shift for fine increments) or a Remesh modifier as a fallback.
- **Sculpt brushes:** Clay Strips (primary volume-building brush), Crease, Draw (used both generally and specifically as the alpha-stamping brush), Front Faces Only toggle (prevents backface remesh corruption).
- **Curve-based tendrils:** Bezier Curve, Curve Pen / Draw tool (Method: Surface for on-mesh tracing), Geometry > Bevel Depth (thickness), Radius Taper Start/End (tapered ends), Alt+S (per-point radius scaling), Ctrl+J (join curves, then join to mesh), Object > Convert > Mesh.
- **Resolution:** Multiresolution modifier (Simplify/subdivide to millions of vertices for alpha-stamp detail), Shade Smooth.
- **Alpha texture stamping:** purchased TIFF alpha textures (ArtStation), Draw brush Texture > New Texture, Mapping: Area Plane, Angle: Front Faces Only, Stroke Method: Drag Dot, Falloff: Constant, F (Radius), Shift+F (Strength/intensity), Ctrl+F mid-stroke (manual rotation angle), Escape (fast-cancel a bad stamp vs. slow Ctrl+Z).
- **Symmetry:** per-object X-symmetry toggle (must be re-checked after undo chains and after any one-sided asymmetric edits).

### Difficulty
Advanced (assumes sculpting fundamentals; the curve-based tendril trick and alpha-stamping workflow are intermediate-to-advanced techniques used together in a full creature pipeline)

### Blender Version
Not specified — relies on the Human Base Meshes add-on and standard Voxel/Multires sculpting workflow, consistent with Blender 3.x through 5.x.

### Tags
organic, procedural, materials, advanced

---

## Related Tutorials
- [Remeshing Tips for Beginners | Blender Secrets](remeshing-tips-for-beginners-blender-secrets.md) — shares organic, procedural; goes deeper on this video's Voxel Remesh troubleshooting (banding, holes, the Remesh-modifier fallback) and adds Quadriflow/Quad Remesher alternatives.
- [What if you Alpha Brush texture is square? Or the resolution is too low? Blender Sculpting tips](what-if-you-alpha-brush-texture-is-square-or-the-resolution-is-too-low-blender-s.md) — shares organic, procedural; directly explains the resolution/shading fixes needed for the purchased-alpha skin-detailing pass used in this video.
- [Blender Secrets - Hard Surface Sculpting Tips](blender-secrets---hard-surface-sculpting-tips.md) — shares organic, procedural, materials, advanced; complementary sculpting-detail toolkit (Dyntopo/Multires/Mask Extract) applied to a hard-surface rather than organic-creature context.
- [Blender Secrets - Hard Surface Sculpting Tips Part 2](blender-secrets---hard-surface-sculpting-tips-part-2.md) — shares organic, procedural, materials, advanced; same relationship as Part 1, additional sculpting tricks from the same author.
