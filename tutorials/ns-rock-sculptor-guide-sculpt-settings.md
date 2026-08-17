---
title: NS Rock Sculptor Guide   Sculpt Settings
source: YouTube
url: https://www.youtube.com/watch?v=ErHZ6gbPl6g
author: Nick Sayce
ingested: 2026-08-17
blender_version: "5.1.x (approximate, viewport title bar in captured frames; not stated verbally)"
tags: [procedural, geometry-nodes, displacement, organic, product-viz, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/ns-rock-sculptor-guide-sculpt-settings/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Rock Sculptor Guide   Sculpt Settings

**Source:** [YouTube](https://www.youtube.com/watch?v=ErHZ6gbPl6g)
**Author:** Nick Sayce
**Duration:** 7m37s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] The sculpt settings are very simple and it's what I use to make all of these presets.
[0:10] It's pretty powerful, you'll see. You can either start with, there are some base shapes that come with the NSWrack Builder
[0:21] I use a rough sculpt blend file, but for now we can just drop in a cube and I will explain the sculpt as best I can.
[0:33] So, we'll come back to them. So, number of cuts make sense. So these are, imagine if you've got the knife and bisected and just kept slicing all over the place to make your rock shape.
[0:44] Because obviously rocks and boulders, they do have straight edges. You can't just put a displaced modifier on a cube and expect to get a rock.
[0:51] You've got to cut this and cutting it takes time. So I've automated it. So, number of cuts is three. So, three cuts.
[1:02] This is the bit that will take a little explanation. So you've got min offset and max offset.
[1:09] And what this means is, 0.5 is 0.5 of the distance between the center of the object, in this case it's a cube, and the end.
[1:20] So this, all this here is half. So if I go 0.5, I'm going half way towards half of the cube, half of the object.
[1:33] You know, I'm in the center of mass. So even if you set minimum offset to zero, that is half way. So 0.5 is literally quarter.
[1:43] So I'm allowing this to cut, the deepest cut will be a quarter. The max offset is how close to the edge will cuts be as well.
[1:55] So if they go straight through 0.5, they could go like that, I guess, which means this cut is roughly 0.9 away from the outside.
[2:07] So you can think of it as a color ramp. If you bring them closer together, the cuts are going to stay very close together.
[2:13] So as an example, if I put 0.3 and leave the max offset at 0.5 and just do one cut, if you press sculpt, this one sculpt rock, it's going to make one cut.
[2:24] Which you can't see, and it automatically applies the NS Rock sculptor, but if we go round the back, that's one cut.
[2:31] And as you see, that's a large cut because I've allowed it to go very close to the center.
[2:36] Now, if I wanted, if I like that, I don't, but if I did, I'd now want to just make smaller cuts and just maybe chip off the edges a bit and whatnot.
[2:47] So to do that, I'm going to have to up the min offset. So as I say before, it was, I've got it 0.5, which is about here.
[2:57] That's a quarter of the whole cube at 0.5 from the distance from the center. So if I jump that up to 0.7, I didn't know, 0.7.
[3:07] So now it's about here. It shouldn't cut closer to the center than about here.
[3:12] And again, because I'm leaving this at 0.95, I'm just going to put that at 0.9.
[3:17] It's that's cutting up to about here. So I've done one cut. I'm going to put in another seven cuts, little shavy, shavy shavies sculpt.
[3:29] And there you go. So now it's much closer to a boulder. We've just made a bunch of smaller shaves, little cuts like that.
[3:39] And that has given it a much better build of shape. All right, the seed is at minus one, which is random.
[3:45] So you don't really need to change that. So yeah, once you're, if you think I like it, but it's a rock, let me look at it from a different angle.
[3:54] Just press random rotation and it'll just, you know, until you get an angle you're happy with and you want to work with, you can just rotate it.
[4:02] I like that. You can rotate it around. Make single is very important if you're making your own.
[4:09] Because if you, if I was, if I'd done all my edits through here on this, and then let's say I just duplicate that.
[4:18] And I just want to sculpt that a little bit more. So I'm just going to click on that. And this, this applies to whatever is the active object.
[4:25] It will still work on this one, but the material is not connected. Well, actually it is because it's both the same one.
[4:31] But anyway, so let's just sculpt that a little bit more to make it a bit different. There we go. Just shaved off a bit more of the edges.
[4:38] So if I wanted to make changes to this one, it's going to affect both. Both will take these changes.
[4:48] There we go. Blue. That's a horrible coloured boulder. So it's green.
[4:53] So it's going to affect both. And if I was going to make a completely different rock, I don't want to affect them both.
[4:59] So all you've got to do is press make single. Like, if you see here, Nick Rocksculter, no, it has Rocksculter.
[5:08] In the material properties, they're both using the same one. If I click make single on this, that makes it its own material.
[5:17] So now I can edit this one. I'm doing the wrong one because this one, I see it confused. I've confused myself.
[5:23] This one's still connected to the Rocksculter. So if I want to edit this one, which is now .01, I'm going to go there and do that.
[5:31] And now if they change the material, it's only going to affect that one.
[5:35] Important note, we're not going to get to it when we get there. If you add a displaced modifier, you want to do that before you click make single
[5:45] because then it won't make the modifier single as well. So then you'll find that if you make another rock and start editing what you think is a brand new displaced modifier,
[5:52] it's not. It's the same one and you've just completely buggered up the first one you did. So be aware of that.
[5:58] But that is the sculpt set here. Oh, no, it isn't. Last thing. All right. This is why I'm time stamping this.
[6:06] So this here use white mask. If I like a certain area of the rock, let me just change that color. I don't know why, but that's horrible to look at.
[6:17] That's better. Yeah, so let's pretend I like this back face. I like this and this and this. So what I'm going to do is in edit mode, I'm going to go to that's my quick menu, just white paint.
[6:32] Head over to white paint and the area that I want not to be cut. I'm going to paint with full weight and I'm telling the sculptor.
[6:43] Don't cut this. Don't cut this. It's all sad. So yeah, I'm just hoping that when I'm hoping I've programmed it so wouldn't it should leave this side of the rock alone.
[6:57] So if I put seven cuts, we'll leave it at point seven. The first time it should leave this.
[7:03] And it did. So it's just made cuts to the back now.
[7:07] And it left left what we wanted. Let that alone. Once you've done once you sculpted it again, if again you want to keep different bits, you're going to have to go back in and wait paint more because it's going to lose that mask.
[7:20] Sorry, the white, the white. Yes, the white paint every time you sculpt again.
[7:25] So that is how you use the white mask. Wait for us all just how close and how contrasty. I've never touched that. I'll leave that where it is.
[7:33] That is sculpt settings done.



---

## Captured Frames

- [0:21] tutorials/frames/ns-rock-sculptor-guide-sculpt-settings/frame_000.jpg
- [1:20] tutorials/frames/ns-rock-sculptor-guide-sculpt-settings/frame_001.jpg
- [2:24] tutorials/frames/ns-rock-sculptor-guide-sculpt-settings/frame_002.jpg
- [3:17] tutorials/frames/ns-rock-sculptor-guide-sculpt-settings/frame_003.jpg
- [4:25] tutorials/frames/ns-rock-sculptor-guide-sculpt-settings/frame_004.jpg
- [5:08] tutorials/frames/ns-rock-sculptor-guide-sculpt-settings/frame_005.jpg
- [6:32] tutorials/frames/ns-rock-sculptor-guide-sculpt-settings/frame_006.jpg
- [7:03] tutorials/frames/ns-rock-sculptor-guide-sculpt-settings/frame_007.jpg

---

> **Third-party add-on note:** This is the core-algorithm episode of **NS Rock Sculptor**, a paid third-party Blender add-on by Nick Sayce (NS). "Sculpt Rock," "Number of Cuts," "Min/Max Offset," "Seed," "Randomize Rotation," and "Make Single" are the add-on's own operator/parameter set driving a knife-bisect-based procedural generator, not stock Blender geometry nodes.

## Structured Notes

### Core Technique
Starting from a plain cube (or one of the add-on's bundled base shapes), NS Rock Sculptor repeatedly knife-bisects the mesh a set number of times, with each cut's distance-from-center constrained between a Min Offset and Max Offset, to procedurally carve a cube into an irregular boulder silhouette — this is the underlying generator that produces every preset elsewhere in the series.

### Summary
The presenter explains this is literally how every other preset in the series was built. Starting from a base cube, "Number of Cuts" sets how many knife-bisect operations are automatically applied (each cut simulates manually selecting the knife tool and slicing across the mesh). The key, more subtle controls are Min Offset and Max Offset, both expressed as a fraction of the distance from the object's center to its outer edge (0.5 = halfway to the edge, i.e. the actual midpoint of that half — described in the video as effectively "a quarter" of the total width from center-to-center). Min Offset sets how close to the center a cut is allowed to reach (raising it keeps cuts away from the core, producing smaller edge-chip cuts instead of deep gouges); Max Offset sets how close to the outer surface a cut can land. A single cut with a low Min Offset (demoed at 0.3) allowed to run close to center produces one large, dramatic slice; raising Min Offset to 0.7 and Max Offset to 0.9 with several more cuts (demoed building up to 8 total) produces many small edge-chipping shaves that read as a much more convincing, natural boulder. Seed is left at -1 (random) by default and rarely needs changing. "Randomize Rotation" lets you cycle through orientations to find a pleasing angle without re-sculpting. "Make Single" detaches a duplicated rock's shared material/data so edits to one copy stop propagating to its sibling — critically, if a Displace modifier will be added later, it must be added *before* clicking Make Single, or the modifier itself stays shared/linked even though the material looks separated, silently corrupting both rocks' displacement when you think you're only editing one. Finally, a "Use Vertex Weight Mask" / paintable white mask (reached via a Weight Paint quick-menu shortcut in Edit Mode) lets you protect chosen areas from being cut at all — paint full white weight over regions you want preserved, then re-run Sculpt Rock; note the painted mask does not persist automatically and must be repainted before every subsequent sculpt pass if you keep re-rolling the shape.

### Key Steps
1. Start from a plain cube (Add → Mesh → Cube) — or one of the add-on's bundled base shapes/blend file — as the input mesh for the sculptor.
2. Set "Number of Cuts" — each unit automates one knife-bisect slice across the mesh; more cuts = more facets/detail, but every cut takes real generation time.
3. Understand Min Offset / Max Offset as positions along the distance from the object's center (0) to its outer bound (1, though frames show it clamped/behaving like a 0.5 range in practice): Min Offset sets the closest a cut is allowed to approach the center; Max Offset sets the closest a cut is allowed to approach the outer surface.
4. For one dramatic, deep single cut: set a low Min Offset (e.g. 0.3) with a wide-open Max Offset (e.g. 0.5-0.95) and a single Number of Cuts, then click "Sculpt Rock" — produces one large gouge/slice.
5. For a natural boulder look: raise Min Offset well away from center (e.g. 0.7) and tighten Max Offset closer to the surface (e.g. 0.9), then increase Number of Cuts (demoed building to 8 total) — produces many small edge-chipping shaves rather than one dramatic cut.
6. Leave "Seed" at -1 (random) unless you specifically need a reproducible result across re-sculpts.
7. Use "Randomize Rotation" to spin through orientations after sculpting, without re-running the generator, until you find an angle you like.
8. To duplicate a sculpted rock and vary it independently: duplicate the object, select the copy, and adjust its sculpt — but note both copies still share the same material/data at this point, so material edits (e.g. changing color) affect both simultaneously.
9. Click "Make Single" on the copy to detach it into its own independent material instance (becomes a `.001` data-block) — only then do further material edits stay isolated to that one object.
10. **Critical ordering rule:** if you plan to add a Displace modifier (Displacement tab, later episode), add it *before* clicking Make Single — otherwise the modifier itself remains linked/shared between the "separated" objects even though the material looks single, and editing what you think is one rock's displacement silently corrupts the other's too.
11. To protect specific areas from future cuts: enter Edit Mode, open the quick-favorites menu (right-click) and choose Weight Paint (or the add-on's "Use Vertex Weight Mask" toggle), paint full white weight over the region(s) you want preserved, then run "Sculpt Rock" again — the sculptor avoids cutting into fully-white-masked geometry.
12. Remember the mask does not persist automatically across repeated sculpt passes — repaint the white mask before every subsequent "Sculpt Rock" click if you're iterating and want to keep protecting the same area.

### Nodes / Settings
- Sidebar section "Sculpt Settings" (first section in the panel order: Sculpt Settings, Weight Paint, Edge Crease, Colour, Moss, Filters, Colour Ramps, Displacement, Bump, Geometry, Scatter)
- Operator/parameters: "Sculpt Rock" (generate button), Number of Cuts, Min Offset, Max Offset, Seed (default -1/random)
- Utility buttons: "Randomize Rotation," "Make Single" (detaches shared material/data into an independent `.001` instance)
- "Weight Paint" section: "Use Vertex Weight Mask" toggle + a Weight Paint mode shortcut (reachable via Blender's right-click quick-favorites menu) for painting a protect-from-cutting mask; does not persist across repeated Sculpt Rock runs

### Difficulty
Intermediate (the Min/Max Offset relationship and the modifier-before-Make-Single ordering trap both require real understanding, not just slider-dragging)

### Blender Version
5.1.x (approximate, viewport title bar in captured frames; not stated verbally) — consistent with other NS Rock Sculptor Guide episodes from this same upload batch (2026-07-30/31).

### Tags
procedural, geometry-nodes, displacement, organic, product-viz, intermediate

---

## Related Tutorials
Part of the **NS Rock Sculptor Guide** series (10 episodes, all uploaded 2026-07-30) covering the NS Rock Sculptor add-on tab by tab. This is the foundational/core-algorithm episode — every other tab in the series operates on rocks generated here.
- [NS Rock Sculptor Guide - Geometry & Scatter](ns-rock-sculptor-guide---geometry-scatter.md) — same add-on/series, Geometry & Scatter tabs (directly relevant — decimation and scatter both consume the sculpted mesh produced here).
- [NS Rock Sculptor Guide - Displacement](ns-rock-sculptor-guide---displacement.md) — same add-on/series, Displacement tab (directly relevant — this episode's Make-Single-ordering warning specifically concerns the Displace modifier covered there).
- [NS Rock Sculptor Guide - Edge Crease](ns-rock-sculptor-guide---edge-crease.md) — same add-on/series, Edge Crease tab (directly relevant — operates on the same base-mesh facets this episode's cuts create).
- [NS Rock Sculptor Guide - Colour](ns-rock-sculptor-guide---colour.md) — same add-on/series, Colour tab (directly relevant — the shared-material-until-Make-Single behavior demoed here with color is the same mechanism, just for shape instead).
- [NS Infinite Rock Builder Guide - Main Controls](ns-infinite-rock-builder-guide---main-controls.md) — conceptual sibling: same author's other add-on, also has its own "Make Single" detach mechanism, different tool/UI.
