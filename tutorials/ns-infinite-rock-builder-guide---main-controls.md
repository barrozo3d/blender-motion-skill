---
title: NS Infinite Rock Builder Guide - Main Controls
source: YouTube
url: https://www.youtube.com/watch?v=VkYNlPxOsUk
author: Nick Sayce
ingested: 2026-08-12
blender_version: "Blender 5.1.2 -- observed in frame_000"
tags: [geometry-nodes, procedural, displacement, organic, intermediate, blender-4x]
extraction_status: complete
frames_dir: tutorials/frames/ns-infinite-rock-builder-guide---main-controls/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Infinite Rock Builder Guide - Main Controls

**Source:** [YouTube](https://www.youtube.com/watch?v=VkYNlPxOsUk)
**Author:** Nick Sayce
**Duration:** 12m43s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello, hello. Welcome to the first video for the guide to the NS Infinite Rock Builder.
[0:10] The thing that does this. I'm going to do similar to the RockSculptor, I'm going to do a video
[0:16] for each dropdown, because as you can see there's quite a lot. It's very simple, it's
[0:20] just sliders really, but you've got a lot of them. So you can do a lot with this and
[0:27] you'll never have the same rock formation. And then you would turn something like that
[0:31] into a rock face for your scene or sign. Depending on the formation that you created and that
[0:38] you are happy with. It's very simple to do very quick, very fast, and I'm going to show
[0:43] you a quick. So for this one, I'm going to go just discuss all of this. Sorry, it's mostly
[0:49] self-explanatory, but there's a couple of bits. So the first thing I would want to do
[0:54] is I make everything on a plane first, because I just find it's what it's been built on a
[1:00] single plane, scaled for a single plane, so that it's just quick and easy to get something
[1:08] you're happy with. And I'm just going to subdivide that five times. And oh, the add-on, yeah,
[1:13] that'll help. I mean, it's same as any add-on. Go to preferences, add-ons, install from disk,
[1:20] to the zip file that's in the downloads. Incidentally, to uninstall them now, you can't do it in the
[1:27] add-ons. You've got to go into get extensions and then find it, which is there, and then drop that
[1:33] down and you get uninstall. Just slightly different now. So once that's installed, it'll be here in
[1:41] your tabs and select the plane. This will always apply to what's selected. And literally click
[1:48] add formation one, which is the base, as it says there, because all of these 25 formations are all
[1:56] in a chain. So two is above one, three is above two, da-dee-da-dee-da. I don't need to explain that to
[2:02] you, but it does become important. So it's useful to explain that. And once you get it, of course,
[2:08] this has got jaggy-jaggy edges. So there's this here, the subdivision. It applies one automatically
[2:16] when you add a formation. And then I would normally work at three and I render in five. So just to
[2:21] keep it a bit smooth. Now, if I wanted to get to making a cool new rock formation, I can simply do
[2:31] it by clicking here, having a butcher's seeing which one you like the look of and add it. I'm
[2:37] going to go formation 16 and you get an add formation 16 baton. Press that and it swaps.
[2:44] A point of note is that some of these formations are intended to be mixed. They're unlikely to be used
[2:51] as a standard formation. Like I wouldn't use this in a scene. You could do, that's fine,
[3:00] you know. But I use this realistically as a mixing formation. And what I mean by that is when you
[3:07] add a formation, it adds here. Formation one is always there because it is at the bottom,
[3:11] but you can edit the strength. So formation 16 is added. It's got a drop down and you've got the
[3:18] blend mode and mix and strength. So when you add multiple formations, you can individually, if they're
[3:24] all mixed individually, add more strength. Say one formation is more interesting to you than another,
[3:29] you would add more strength. But let's start with this. I'm going to actually going to knock
[3:34] the sub-div down to two. I should have done that there. Just so you can see the rapid update.
[3:40] So the mix slider, it could just be simply 0.5 of each, which is fine. I'll put that to three at least.
[3:50] That's fine. You know, it's different. And you can add as much or as little as you want.
[3:55] You know, and as you can see, it just slowly, well, depending on how slow you're going with that,
[4:00] adds each formation together. But there's another way, which is the way I tend to use more, which is
[4:05] the blend mode. And the ones I usually use often are add different, exclusive, subtract, divide.
[4:12] For some reason, it goes crazy. Watch. I don't know why it does that. I'm sure there's a mathematical
[4:19] reason, but I would normally try something like add first. So as you can see, it's now added
[4:24] formation 16 on top of formation one. Let's add another sub-div. So it's a bit smoother.
[4:30] So now you've got the best of both worlds. And you can still edit how much you're adding
[4:35] using the slider. Add none. You've got formation one. Add 100%. You've got 100% of both. So as you
[4:43] can see, very quickly, you've got a completely different look. And we can go even further
[4:49] but in another formation. Each time you add formations, you are adding calculations on top
[4:55] of calculations. So it will start to take longer to render the more formations you add, but that
[5:00] makes sense, doesn't it? And Evie hates it. Don't put it. Don't do it, Evie. If you switch to Evie
[5:06] or Material Preview, Blender's probably going to, you could wait, but it'll probably crash. It hates
[5:13] my shaders. And as you can see, because this is the main group, I've left this here for a reason.
[5:19] So this is the main group as of version seven and all the controls are here. So the functionality is
[5:27] all there, but it just took longer. And then each formation requires you to go within the main
[5:33] control group. And then you've got the 25 formations there to edit, but now it's all over here. So it's
[5:39] much quicker, much, much quicker indeed. Right, so we're a formation 16. So I'm going to put
[5:44] something else. Now, when I mentioned the chain and the order of the chain, if I was to add formation,
[5:54] let's say eight, it's going to add it between formation one and formation 16.
[6:03] Dink, you see. So now formation 16 is, I don't know what Blend Mode set to this. Oh, so that's
[6:11] unmixed. It should have been unmixed. So now that's formation 16 adding to formation eight,
[6:18] because eight is just unmixed. So it's completely replaced one. So now 16 is only
[6:25] adding to formation eight, because it's covered formation one, because it's higher in the chain
[6:31] than formation one. I hope that makes sense. It still looks pretty cool. I like that. I like that.
[6:36] But I would probably still, again, maybe change the Mix Mode to Exclusion.
[6:44] Okay. So now I've got the best of both worlds. As you can see, it gets crazy detailed.
[6:50] There's, you know, I like the bitty-bit-iness of this, but I like the big chunky, angular shapes.
[6:56] It looks very natural and very rockish. All right. So that's how you add the formations.
[7:03] And just remember, there is an a chain. So anything that's above one that's set 100% to Mix,
[7:10] that's just replaced. You might as well think of Mix as Replace. And then you just edit the
[7:15] Blend Mode or the Strength. Again, if you wanted more Strength, if you wanted more formation one
[7:20] to be showing through this, because it's not gone, but I might want more. So I might put that up to
[7:26] 1.5. And then it's just pushing out formation one, as you see. So it's just kind of making these more
[7:33] bolder-esque, I guess, jutting out from the wall. Okay. So that's the formations,
[7:40] your subdivisions, we know all about that up here. So I'm going to put this back to 2, just for speed.
[7:47] And there we are. Overall scale probably doesn't need much explanation. But the reason,
[7:54] I mean, there's a very good new purpose for this, because if I was happy with this,
[7:59] and I wanted to make another one of these shapes, it might actually have updated to that
[8:04] formation. It hasn't, because I made it single. The scale would be way off. Because when I make,
[8:13] if you make a new shape to add your thing on, the rock builder, I tend to go to Object UV,
[8:21] and I'll show you exactly why. So let me hide that again, get out of here. And so
[8:30] there's tons of ways to do it. It's just, it's object mapping, which means it's based on the
[8:34] object, not UVs, not nothing. So what I normally do, which I find the easiest way to get it,
[8:41] to get the shape is add a plane, tab into edit mode, press M, merge at center, you've got a vertex,
[8:47] and then just press E and create your rocky shape, I guess. And then I just tend to round it off at
[8:57] the end, so I've got that. And then I'm going to go into right view with three and just start
[9:05] rotating upwards, just going down a bit, keeping it tidy, keeping it tidy.
[9:10] And now I've got, you know, a shape. So because I made this on a single plane,
[9:21] if I now link these materials, Q, link, sorry, not Q, that's not a thing,
[9:27] select, select, linked material. I've done that wrong, right, Q, select, link materials,
[9:35] where is that? I'm going the wrong way, link materials. Where's link materials, select,
[9:42] it's in here somewhere, select linked material, that's it. All right, so I've now copied that over
[9:49] to my shape and it looks weird. So we're just going to add some subdivision surfaces to this,
[9:55] generate subdivision surface. And I normally, for a new shape, because I want the roundness,
[10:00] I'll make do twice and then apply it and then just check another one on and put that to four.
[10:10] Right now it's in UV mapping mode. And when we go, when I go to objects,
[10:15] well, you'll see it'll appear on there. So now if I slide to this, it's going to crazy. So like I
[10:21] said, the scales way off. So it's good on the plane, and that's all good on the shape. So it's
[10:27] just a case of lowering that scale significantly, maybe not that far, maybe 0.5. And then I might
[10:35] lower the strength to 0.5. That looks about right. Okay, so then that's how you get your,
[10:46] that's how you build your rock face, my even less strength 0.3. Obviously, the lighting is
[10:52] terrible. I've got nothing in way of lighting. So it looks kind of flat. Unless let me just turn
[10:57] off the background. We can see a bit of shape now from that angle.
[11:04] Yeah, so I've taken that pattern, put it over there. And then we've got my rock face,
[11:11] as I say, sort out your lights. That's terrible. That's a better angle. I would think that looks a
[11:18] bit. I'm going to lower the strength of formation one, which is the base and put that back to one,
[11:25] and then up the strength of all of it. Two, well, I got 0.3, 0.8. Oh, no, wrong one, 0.6.
[11:38] Yeah, that looks all right. Cool. Okay. So yeah, that's how you'd make your rock face. Now, what I
[11:48] mentioned about this makes single. If you've selected your object, you click make single. With
[11:53] your notes here, this will become a 0.001. So click make single. And then everything that's on here,
[11:59] including any modifiers, becomes single. So now if I added another plane, and just I'm not going to
[12:07] bother subdividing it, and then just add a formation one to this, don't think any changes I make to
[12:14] this won't affect the other one. And so you can change everything about it, because that one has
[12:21] been made single. I believe that is everything in this section. There's all the formations.
[12:26] My favorites are 16, 24, 1, and 9, and 8. I like 25 too. I like them all. All right, so I'll do colors next.



---

## Captured Frames

- [0:10] tutorials/frames/ns-infinite-rock-builder-guide---main-controls/frame_000.jpg
- [1:41] tutorials/frames/ns-infinite-rock-builder-guide---main-controls/frame_001.jpg
- [2:44] tutorials/frames/ns-infinite-rock-builder-guide---main-controls/frame_002.jpg
- [3:18] tutorials/frames/ns-infinite-rock-builder-guide---main-controls/frame_003.jpg
- [6:03] tutorials/frames/ns-infinite-rock-builder-guide---main-controls/frame_004.jpg
- [8:41] tutorials/frames/ns-infinite-rock-builder-guide---main-controls/frame_005.jpg
- [10:00] tutorials/frames/ns-infinite-rock-builder-guide---main-controls/frame_006.jpg
- [11:04] tutorials/frames/ns-infinite-rock-builder-guide---main-controls/frame_007.jpg

---

## Structured Notes

### Core Technique
Building procedural rock faces with the **Infinite Rock Builder** — a third-party Geometry Nodes add-on by Nick Sayce (NS) — by stacking numbered "formations" on a subdivided plane and blending them with Mix/Strength and Blend Mode controls.

**Add-on disclosure:** This entire tutorial (and the rest of this series) documents a paid third-party add-on's custom node-group UI, not stock Blender geometry nodes. Panel names like "Add Formation", "Make Single", the 25 numbered formation thumbnails, and the Mix/Blend/Strength rows are add-on-specific — they will not exist in a vanilla Blender install and should not be confused with core GeoNodes primitives when giving general Blender advice.

### Summary
Part of the NS Infinite Rock Builder Guide series — this is the overview/foundation video covering Main Controls; see also Colours, Filters, Moss/Fresnel/Dust, Water Level Roughness, Cliff-top Flatten/Bump. The viewer learns the base workflow: install the add-on, apply it to a subdivided plane, add one of 25 preset "formations" from the sidebar panel, and stack additional formations on top using Mix Strength or a Blend Mode (Add, Difference, Exclusion, Subtract, Divide) to combine their displacement patterns. Formations are chained in numeric order (formation 2 sits above 1, 3 above 2, etc.), and adjusting a formation's Strength pushes more or less of the formation below it through. The end result is a unique, non-repeating rock-face shape that can then be mapped onto a custom hand-sculpted mesh (instead of the default flat plane) via Object-based mapping, and made independent of other rock instances with "Make Single" so each rock can be edited separately.

### Key Steps
1. Install the add-on: Edit → Preferences → Add-ons → Install from Disk → select the add-on zip (to uninstall on newer Blender, use Get Extensions instead of the Add-ons list).
2. Create a base mesh: Add a Plane, Subdivide it ~5 times (transcript uses 2-3 while working for speed, renders at 5 for smoothness).
3. With the plane selected, open the N-panel "NS Infinite Rock Builder" tab and click "Add Formation 1" — this is always the base/first layer in the chain.
4. Browse the 25 preset formation thumbnails in the panel; click any thumbnail (e.g. Formation 16) and press "Add Formation X" to stack it on top of the chain.
5. For each added formation, expand its row to reveal Blend Mode, Mix, and Strength — use Mix for a simple 0–1 blend, or a Blend Mode (Add, Exclusion, Subtract, Divide) for more dramatic non-linear combinations; Strength scales how much of that formation shows through.
6. Note the chain order matters: a formation added between two others (e.g. adding Formation 8 after 1 and 16) inserts itself into the stack and can visually replace whichever formation is beneath it if its Mix is at 100% ("Mix" effectively behaves like "Replace" at full strength).
7. Adjust "Subdivisions" (viewport-friendly value while iterating, e.g. 2-3; higher, e.g. 5, for final render) and "Overall Scale" on the modifier.
8. To use a custom (non-plane) base shape: Add a Plane → Tab into Edit Mode → M (Merge at Center) to collapse to one vertex → E (Extrude) repeatedly to sculpt a rough rock silhouette → exit Edit Mode.
9. Copy the rock-builder material/node-group across via Select → Select Linked → Linked Material, then add a Subdivision Surface modifier (2 levels, applied, plus one more unapplied ring set to 4) to smooth the custom shape.
10. Because the custom shape uses Object-based mapping (not UV), the formation Scale will look "way off" versus the flat plane — reduce Overall Scale (e.g. to ~0.5) and Strength (e.g. ~0.3–0.6) to compensate and dial in a natural look.
11. Click "Make Single" on an object to detach its rock-builder node group into its own independent copy (data becomes a `.001` instance) so edits to one rock no longer propagate to duplicates from the same source.
12. Favorite formations mentioned by the presenter: 16, 24, 1, 9, 8, and 25.

### Nodes / Settings
- Add-on panel: "NS Infinite Rock Builder" (N-panel sidebar tab)
- Panel controls seen: Toggle Material, Make Single, formation thumbnail grid, "Add Formation X" button, per-formation Blend Mode / Mix / Strength rows, Subdivisions slider, Overall Scale field
- Panel section headers visible below the formation list (covered in the other videos of this series): Filters, Water Level Roughness, Moss / Fresnel / Dust, Cliff Top Flatten, Bump
- 25 numbered preset "formations" (procedural displacement patterns), chained/stacked in numeric order
- Blend Modes referenced: Mix (Replace-like at 100%), Add, Exclusion, Subtract, Divide
- Standard Blender ops used alongside the add-on: Subdivide, Merge at Center (M), Extrude (E), Select Linked → Linked Material, Subdivision Surface modifier

### Difficulty
Intermediate (no geometry-nodes authoring required, but understanding the formation chain/blend-mode interaction takes a bit of experimentation)

### Blender Version
Not stated explicitly by the narrator. The captured frames' title bar reads "Blender 4.x" but the exact point release is not legible at the video's source resolution — do not assume a specific 4.x/5.x minor version from this video alone.

### Tags
geometry-nodes, procedural, displacement, organic, intermediate, blender-4x

---

## Related Tutorials
Part of the **NS Infinite Rock Builder Guide** series (Nick Sayce / NS add-on) — all 6 parts cross-link regardless of tag overlap since they form one continuous guide:
- [Colours](ns-infinite-rock-builder-guide---colours.md)
- [Filters](ns-infinite-rock-builder-guide---filters.md)
- [Moss / Fresnel / Dust](ns-infinite-rock-builder-guide---moss-fresnel-dust.md)
- [Water Level Roughness](ns-infinite-rock-builder-guide---water-level-roughness.md)
- [Cliff-top Flatten / Bump](ns-infinite-rock-builder-guide---cliff-top-flatten-bump.md)
