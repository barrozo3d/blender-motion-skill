---
title: NS Brick Wall Builder Guide
source: YouTube
url: https://www.youtube.com/watch?v=zcuefJcZdUY
author: Nick Sayce
ingested: 2026-08-17
blender_version: "5.1.x (approximate, viewport title bar in captured frames; not stated verbally)"
tags: [procedural, geometry-nodes, displacement, organic, product-viz, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/ns-brick-wall-builder-guide/
frame_count: 9
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Brick Wall Builder Guide

**Source:** [YouTube](https://www.youtube.com/watch?v=zcuefJcZdUY)
**Author:** Nick Sayce
**Duration:** 19m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello, welcome to my new add-on, the NS Brick Wall Builder. I'm going to show you very quickly how to get started and then I'm going to go through everything.
[0:12] You can either open the blend file that you can download in the download section, which will have all three materials, or just append the materials and make sure those materials are in your scene.
[0:25] I'm just going to check my knowledge by adding a plane. So yeah, you need NS Brick Wall, NS Mortar, NS Coin. They're in a blend file. You can download or you can just append them into a new scene from that file.
[0:37] Alright, so we've got the materials because the add-on needs those materials. Make sure you've got your add-on installed in preferences. You want to install and then click point to the NS Wall Builder zip file and it will be in and then it will appear over here with the NS Wall Builder.
[0:56] So it's important first to have the materials, but it's also important to have this, which is the wall curve. And when you open the add-on, you see you've got a straight mode and a curve mode because it turns out it was incredibly difficult to put both in the same script.
[1:09] So there is a separate straight script and a separate curve script. This add-on targets both. So under wall curve, you need a wall curve.
[1:21] So the way I built it to edit is there's several ways to do this, but I just added a plane. I tabbed into edit mode, selected all, and then you've got, it's in my merge, mesh, merge at center, and we get one vertex.
[1:40] That's the way I've always done it. It's probably an easy way, but that's the way I do it. And then this will become the basis of the curve. So I'm going to just, if I was to build a wall, let's say it's four meters across on the X, which is that.
[1:55] And then let's say it turns and goes two meters on the Y and then X, let's go six meters on the X. So that's the curve that I've built for my scene.
[2:08] What's, you can do odd values like three, five, but though I've tested it on three, five, sevens, it seems to work fine. I can't guarantee because in order to get the corner behavior to work, it needed to be doubles, so multiples of two.
[2:25] So two, four, six, eight, dotted up.
[2:27] By all means go with three, but see what happens. But as I say, it's been built specifically for even length curves, only in straight mode. It doesn't matter at all in curved, but in straight mode.
[2:38] All right, so once you've got your curve ready, or at least your, the edge is ready, you want to convert this to a curve. So object, convert, mesh, curve.
[2:50] So now you'll see it's, it was assigned to change, it's image, thumbnails change. So now that is a curve. And all we need to do is put that into here. And the second we do that, we'll get a nice straight wall.
[3:04] All right. And if we go into viewport, edit, render mode, it's targeting the materials. So we've got everything set up. This is just from the last setup I had. So whilst that's in place, you can go ahead and pick any pattern.
[3:22] It'll just restart, regenerate a new wall. It'll keep the majority of your settings. And note, point of note, basket weave takes a little bit longer. I think because it's just a bit more complex to do, I guess.
[3:39] So, I mean, that's just, don't worry about it looks, it's because I've got all these settings wrong. In fact, if I delete this, it's going to delete that wall.
[3:47] All right, because I just want to get this back to a standard so I can explain everything. We don't want that. We don't want that. Again, I'm going to explain all of this in a moment.
[3:58] That'll do. All right. Yep, yep, yep. And yep, yep, yep. Okay. So I'm just going to drop that back in and generate another one.
[4:06] I'm going to drop that back in and generate another one. And we'll come back to editing the shape in a second. Just going through the patterns and then coin and this one, this was a piece to get right.
[4:19] This every end and corner, it will add these coin bricks, which have a separate material. If you see if I click on this in the material properties, you've got NSB, well, then NSCoin now, because we're going to coin.
[4:34] So let's go from the start and let's just build and then go through it bit by bit. I'm going to just put, let's just go through it and say you started like this.
[4:46] All right. Let's say I just want a nice standard wall. So the first one will go to the first drop down dimensions. So the first one is rows.
[4:54] So this will just tell us how high you want the wall. So if we put 20 in the rows, it makes it a bigger wall. But just for speed, I'm just going to put it down to 10. So we've got 10 rows.
[5:09] All right. Cell size. This was kind of, most of this was built on a grid kind of basis using two meter cells.
[5:19] So if we bring this up to point three, it's going to just make the whole thing larger. You see, and then it starts to get a bit strange.
[5:28] That would be to do with brick depth. But I honestly never mess with that. I leave it at point two. And if I want a bigger wall, I'll just scale it up, you know, or just add more bricks, whatever.
[5:41] So that's what cell size does. Brick gap. That's fairly self explanatory point zero one. Just make some more closer together.
[5:49] Don't it? Let's put that point zero to one brick at point zero two.
[5:54] So yeah, that just changes the the the access to the mortar. Brick depth point two just makes it fatter and strange thing going on there.
[6:06] I'll have to look at that. All right. So yeah, that's just changes it. And it is built to sort out the corners, depending on brick depth, the higher you go, it's supposed to and it does. Thankfully, it keeps this.
[6:22] This was very difficult to do get this corner behavior. A lot of nudging.
[6:26] But I tend to leave that at point two or point one. I don't really build too much that goes above that. And just kind of like standard and brick shaped seed.
[6:37] That's obvious. Press two, you get a different seed, a different variation. The wall flip. I've only put this in for one particular reason.
[6:46] And I'll show you that reason. So if I take this curve, I'm just going to now extrude that on negative X by four and then extrude negative Y by two and then extrude.
[7:07] So now I've built a wall. I better separate that. Otherwise, it's going to mess up. All right. So now I've built a wall in the opposite direction. And you'll see what happens when I drop this plane on there.
[7:25] As you can see, the wall is on the wrong side. So if I click wall flip, it will come to the other side. But the caveat is that the corner behavior does not work properly when you're building it negative.
[7:39] So my suggestion, don't build negative. That's the simplest way to do it. Build your builds your walls in positive directions and you'll never need to use that. And it will never be an issue.
[7:49] Bosh. All right. Better generate a wall again, hadn't I? I've put the wrong plane. Which one is this? Just plain. All right.
[8:00] So next box, drop down is bricks. That is fairly self explanatory, I think. In fact, let's just put a coin pattern in so you can see the difference with the difference with the coin color.
[8:15] So you've got brick color, blah, blah, blah. So that's coin color. There you go. That's explained. All right.
[8:22] Brick color variation. It just darkens. It just adds different shades to different bricks. So you can have a bit of a bit more color variation there.
[8:33] Mortar color at the moment is at the back. I can't really see it. So that's why do we want the dirt color. This here dirt and mounts at zero. There's no dirt.
[8:43] I've called it dirt. Could be dust. I don't know. But this you can add. Again, it adds a bit more variation.
[8:52] And there's one cool thing about the texture, actually, which I'll show you in a minute because it'll be clearer.
[8:57] I'll be in the conclusion. Put it up if you want. Just darkens around it, but it does weird things. It's back there. Maybe not.
[9:03] All right, bricks, dirt, mortar. I've just realized mortar colors in two places. I'll remove that. Displace mortar color.
[9:14] But I did add displacement. I might put that back in. It's not there now, but don't worry. All right. Mortar depth.
[9:20] So that's just, as you say, that's just going to change the depth of the mortar behind. I seem to have disconnected the wall somehow.
[9:28] So I'm just going to delete that. It'll keep all my settings. Unless there's an issue with mortar depth, which was working earlier.
[9:35] Yep, brilliant. For the moment, it will work in the add-on. Don't worry. I'll figure it out. But you can change the mortar depth.
[9:41] It's got a bevel modifier. If you wanted to bring it closer, lower the brick depth and put it back to point one.
[9:47] That will be connected when I finish this video. That's more so. Right.
[9:52] Just in variation is what I call the fun part. So this is where you can really mess around with the shape of the bricks.
[10:00] So we will need a bit more depth for depth variation, not to put walls into the wall.
[10:07] So we're going to go back to dimensions and let's give it a bit more brick depth. Let's go to point two this time.
[10:13] So that we'll see the depth variation better. And then just a variation depth variation point three.
[10:20] Too much point one.
[10:24] I mean, you see what's happening. It's randomly randomly varying the depth of the bricks. That's what that does.
[10:32] Scale variation. You'll be surprised to learn it's a variation of the scale of each brick. So you can see some have got smaller, some have got bigger.
[10:39] Again, it's all about keeping it varied and more natural.
[10:44] These are the fun values. The one I use, no, I use all of them, but probably less the X.
[10:51] So rotation Y, if we put five on that, we'll get random variation on the Y axis.
[10:58] If we put Z, you'll be surprised to learn it doesn't on the Z axis, but I found that high values for Z, if you really want variation,
[11:05] because if you look from the top, you can see another all going a bit funny.
[11:09] I mean, with coin pattern, it gets a bit weird. Maybe don't do this with coin, but you only get an adjust and damage bricks amount.
[11:18] So this, let's talk about cracked bricks amount first. So this refers to the bump and there are filters for both of these in the aptly named drop down filters.
[11:30] So if I put cracked bricks amount all the way to the top, I set this on purpose that it completely removes every other bump and just leaves you with the crack bump.
[11:41] If you lower it a little, you see you bring the rest back in, but you're still keeping the cracks.
[11:47] So if you didn't want this bump at all, you would just go to bump and then lower the strength.
[11:53] You know, if you wanted a bit cleaner bricks, but that seems to be the easiest way.
[11:57] So crack bricks amount. And this is the point I can show you the key part of my sex.
[12:02] You'll notice that the cracks, they're wave textures, obviously, but they're independent on each brick.
[12:10] It's not consistent. So you're not getting the wave crack going all the way down.
[12:16] Each brick is assigned to a different area of the texture.
[12:20] Hence how we get this individual cracked bricks rather than consistent crack up the middle and waves.
[12:28] You know what I mean? Just thought I pointed out because it's clear, but I like a little bit of bump.
[12:33] Okay. Damage bricks amount is regarding displacement.
[12:38] So if we put that up to one for now and then head into displacement.
[12:45] We now have two things, but we'll go to material to place displacement first.
[12:49] So material displacement is this stuff that the material group is using.
[12:54] So we can we, but we also want subdivisions at the moment.
[12:58] The bricks have only got one level to really see it do something and not look really strange.
[13:04] We want at least three and then that's way too much strength.
[13:08] So I can either lower the strength or lower the bricks crack damage bricks amount.
[13:12] So I'm going to put that to point five and it just messes them up a little bit.
[13:18] So that's damage bricks amount. You've got mid level. You've got strength, but I wouldn't bother messing with that.
[13:22] Just strength. So if you want it though.
[13:24] So the displaced modifier, if what we'll need because it does puff out the bricks a little is we'll want a bigger gap between the bricks.
[13:33] So brick gap. I'm going to go crazy at point zero five.
[13:38] And then when we go back to displacement, by the way, I get into the habit.
[13:42] I'm trying to teach myself to get into this habit of closing a box because if you've got all open, it gets long.
[13:48] So displacement modifier, tick that and it will add a displacement modifier.
[13:53] And you see what it's done. It's kind of puffed out the bricks.
[13:55] It's the only really white, but the only way I could really get this to look correct.
[14:01] You've got the strength here point zero three.
[14:05] Maybe I'm going to go point zero two.
[14:09] You don't really see much now, but I might.
[14:12] But then you've got the filters again, we'll get to the filters in a second.
[14:16] But I'm going to put that back to point zero three.
[14:21] Two six point. No point zero two six.
[14:27] So you can see it just wobbles the bricks a little and it makes them look incredibly damaged.
[14:32] And right. So now we can look at the filters.
[14:37] So let's leave the displacement of fire on and then go filters.
[14:42] And these are for. Yeah.
[14:45] So the dirt damage they're connected.
[14:49] So if I put dirt back into bricks, dirt amount.
[14:56] That's way too much.
[14:59] So in the filter, fortunately, so this is the scale of the dirt and the damage filter.
[15:05] So when this changes, the damage will also change.
[15:07] So if I put that up, you can see how it's all moving together.
[15:12] You've got scale width and scale height.
[15:14] You can play just play with these values.
[15:15] They just filter values, standard noise filter values you can muck around with.
[15:20] But if you didn't want that much, just lower it lower the amount.
[15:25] And if we now turn off material, let's turn off both of these so I can easily show you the cracks as well.
[15:32] And I don't want damaged bricks, which would be in just a variation.
[15:37] Damage bricks.
[15:38] No one that has cranked that up to one.
[15:40] So it's just the cracks.
[15:43] And then you see under filters, this is the cracks filter.
[15:48] So you can play around with that as well.
[15:50] And again, this is all, you know, it's probably a way filter.
[15:54] I can't remember what I did and just play with the values.
[15:58] Muck around with them.
[15:59] You know, I mean, that's the filters.
[16:02] I'm going to bring my brick, the edges for variation.
[16:09] I want my brick bump, brick, right.
[16:12] Brick bump back a little bit.
[16:16] Is that all?
[16:17] Yes.
[16:18] Done that.
[16:19] Done filters.
[16:20] Bevel.
[16:21] Does it need much?
[16:23] It's a bevel modifier.
[16:27] And that's what that does.
[16:29] It's coupled, obviously, with a subdivision surface in the modifier stack.
[16:34] If I click on the bricks, this is the stack.
[16:36] So the sub-div comes after the bevel.
[16:38] The bevel is there to keep the brick shape.
[16:40] The sub-div is to add enough resolution for, you know, material displacement, doddy-daw.
[16:46] So, yeah, that's the bevel.
[16:48] That all, obviously, is standard, as you know what a bevel is.
[16:52] And the bump, there you go.
[16:54] There you go, it's trying.
[16:55] And then the coin has a separate bump strength.
[16:57] So if you wanted really clean coin bumps, you would just turn it off and separate to the main brick bump.
[17:06] Okay.
[17:07] Now, let's say I'm happy with that wall.
[17:09] I think, yeah, that's it, bro.
[17:11] Then I want to unlink this from the UI because if I wanted to make it look like a brick,
[17:17] if I wanted to make another completely different wall in the same scene,
[17:21] unless it unlinks, it will all stay connected.
[17:24] So the wall will just snap back here, the colors, whatever.
[17:27] So what you want to do is click Make Single.
[17:30] And unlike sapling, you can click anywhere, click About.
[17:33] It doesn't disconnect.
[17:34] It's only disconnected fully when you click Make Single.
[17:38] And then if you want to move that wall, I have a rear all the time.
[17:42] Now we can do very quickly a curve.
[17:44] So delete that and change that to Curved.
[17:49] And we're just going to simply put in a Bezier, a Bezier Curve.
[17:54] And just on that, and then we'll put a course rubber.
[17:59] Actually, it's slightly different in the curve version.
[18:04] So drop that in there.
[18:07] And there we go.
[18:08] So we've got course rubber.
[18:09] It's because the dimensions, it's just keeping the ones we just set.
[18:15] Everything stayed the same.
[18:17] But again, you can see this is completely disconnected.
[18:20] Nothing I do here is going to affect the other wall we made.
[18:28] I think that's the lot.
[18:33] So Bill Wall, you know, that doesn't make single.
[18:35] When you're happy with the wall, make sure you click Make Single.
[18:39] And then it will be successfully disconnected from the wall.
[18:43] That's the lot.
[18:45] There are going to be more additions to this.
[18:48] I'm planning on updating this.
[18:50] I'm going to find more patterns to add.
[18:52] I'm going to look at adding functionality if you wanted the brick to go at an angle,
[18:57] which I did already do a while back, but I lost it through lots of edits.
[19:01] That's the lot.
[19:04] That's the important one to make single to disconnect it after you're done.
[19:08] All right, sweet.
[19:09] That's the lot.
[19:10] I hope I said that three times twice.
[19:12] I hope that's enjoyable.
[19:13] I hope you enjoy using the thing.
[19:16] Yeah, the curve has got all the same patterns.
[19:18] Don't worry about it.
[19:19] You can flick and change.
[19:21] All right, sweet.
[19:22] Enjoy.
[19:23] I've been here.
[19:24] Bye.



---

## Captured Frames

- [0:37] tutorials/frames/ns-brick-wall-builder-guide/frame_000.jpg
- [1:40] tutorials/frames/ns-brick-wall-builder-guide/frame_001.jpg
- [2:50] tutorials/frames/ns-brick-wall-builder-guide/frame_002.jpg
- [4:19] tutorials/frames/ns-brick-wall-builder-guide/frame_003.jpg
- [5:54] tutorials/frames/ns-brick-wall-builder-guide/frame_004.jpg
- [9:52] tutorials/frames/ns-brick-wall-builder-guide/frame_005.jpg
- [12:02] tutorials/frames/ns-brick-wall-builder-guide/frame_006.jpg
- [14:32] tutorials/frames/ns-brick-wall-builder-guide/frame_007.jpg
- [17:27] tutorials/frames/ns-brick-wall-builder-guide/frame_008.jpg

---

> **Third-party add-on note + version note:** This is the earlier full guide (2026-07-13) for **NS Brick Wall Builder**, by Nick Sayce (NS) — predates the v4.0 guide covered separately. Panel layout differs from v4.0: this version uses a "Cell Size" field and a flatter Dimensions/Bricks/Mortar/Jitter & Variation/Displacement/Filters/Bevel/Bump structure with no dedicated Colour Ramps section, whereas v4.0 reorganizes into Base Shape/Brick Colour/Mortar/Jitter & Variation/Displacement/Filters/Colour Ramps/Bevel/Bump and adds a Colour Ramps tab. Treat this as documenting an older add-on version — check the v4.0 guide for the current control set.

## Structured Notes

### Core Technique
Same curve-driven generator concept as v4.0: a curve object (built from a merged-vertex plane, extruded in segments, then Object → Convert → Curve) drives procedural brick tiling when dropped into the add-on's Wall Curve slot and generated, with materials (NS Brick Wall, NS Mortar, NS Coin) that must be present in the scene (via the provided .blend file or appended) before the add-on will render correctly.

### Summary
Requires three specific materials (NS Brick Wall, NS Mortar, NS Coin) to be present in the scene — either open the provided .blend file directly or append them from it — before the add-on's shading works. The wall curve is built the same way as in the newer guide (Plane → Merge at Center → extrude in segments → Convert to Curve), with the same even-number-length recommendation for reliable corner behavior in Straight mode (curved mode is unaffected by segment length). A separate Straight/Curved toggle switches between two independent generator scripts, same as v4.0. Once a curve is generated, switching between pattern presets (Standard, Basket Weave, Coin, etc.) keeps most existing settings and just regenerates the tiling — Coin pattern adds separate coin bricks at ends/corners with their own NS Coin material. **Dimensions:** Rows (height), Cell Size (overall grid scale, built around a 2m base unit — going far from default distorts brick shape), Brick Gap, Brick Depth (also affects corner behavior, kept low ~0.1-0.2), Seed, Wall Flip (only needed if the curve was built in the negative direction — corner math is unreliable then, so the presenter recommends always building positive and never needing this button). **Bricks:** brick/coin color, brick color variation (per-brick shade darkening), mortar color, and a "dirt"/dust amount slider. **Jitter & Variation:** per-brick rotation on Y (and less commonly X), high Z rotation values for strong random variation (visible from top view), plus "Cracked Bricks Amount" and "Damage Bricks Amount" — Cracked Bricks Amount at maximum isolates only the crack-bump pattern (each brick reads an independent region of the crack noise texture, so cracks don't visibly continue from brick to brick); Damage Bricks Amount feeds into Displacement. **Displacement:** Material Displacement (needs Subdivision level 3+ to read properly) plus the Damage Bricks Amount-driven displacement — both puff bricks outward, requiring Brick Gap to be widened afterward (demoed going to 0.05) to compensate. **Filters:** the dirt/dust filter and the crack-bump filter each have their own Scale Width/Height/noise controls, directly linked to how the corresponding Jitter & Variation slider reads. **Bevel & Bump:** a Bevel modifier (paired with a Subdivision Surface modifier later in the stack — bevel keeps brick shape, subdiv adds resolution for displacement) plus a brick bump slider and a separate coin bump strength (so coin bricks can have clean/no bump independent of the main bricks). Finishes with the same **Make Single** workflow as v4.0: building a second wall in the same scene without clicking Make Single on the first will keep both linked to the same live add-on state (editing one snaps the other back); Make Single fully detaches a wall so further edits are independent.

### Key Steps
1. Ensure the three required materials (NS Brick Wall, NS Mortar, NS Coin) exist in the scene — open the provided .blend file directly, or append them from it into your working scene.
2. Install the add-on via Preferences → Add-ons → Install, pointing to the NS Wall Builder zip.
3. Build the wall curve: Add a Plane → Tab into Edit Mode → select all → Merge at Center (M) → collapse to one vertex → extrude in segments (e.g. 4m on X, 2m on Y, 6m on X) → exit Edit Mode → Object → Convert → Curve. Even-numbered segment lengths are recommended for reliable corner behavior in Straight mode (irrelevant in Curved mode).
4. Drop the curve into the add-on's Wall Curve slot — a wall generates immediately using whichever pattern preset is selected.
5. Switch between pattern presets freely; most settings persist across a pattern change (Basket Weave takes noticeably longer to generate than simpler patterns).
6. Tune Dimensions: Rows for height, Cell Size for overall grid scale (built around a ~2m base unit — pushing it far from default starts distorting brick shape), Brick Gap, Brick Depth (also influences corner behavior — keep it low, ~0.1-0.2), Seed for variation reshuffling.
7. Only use Wall Flip if the curve had to be built in the negative direction (corner behavior is unreliable there regardless) — the recommended practice is to always build curves in the positive direction and never need this button.
8. Tune Bricks: brick/coin color, brick color variation, mortar color, and the dirt/dust amount.
9. Tune Jitter & Variation: Y (and lightly X) rotation jitter, high Z rotation for strong randomness, Cracked Bricks Amount (isolates/blends the crack-bump pattern — each brick samples an independent region of the noise texture so cracks don't chain between bricks), and Damage Bricks Amount (feeds Displacement).
10. Enable Displacement (Material Displacement needs Subdivision level 3+ to show properly) and dial in Damage Bricks Amount-driven strength — widen Brick Gap afterward (e.g. to ~0.05) to compensate for the puffed-out silhouette displacement causes.
11. Fine-tune the Filters section (Scale Width/Height/noise) for both the dirt/dust filter and the crack-bump filter — these are directly linked to their respective Jitter & Variation sliders.
12. Add Bevel (paired with a Subdivision Surface modifier later in the stack) to keep crisp brick edges, then dial in brick Bump strength and, separately, coin Bump strength if using the Coin pattern.
13. Click "Make Single" once satisfied with a wall before starting a second, independent wall in the same scene — without it, both walls stay linked to the same live add-on state and editing one will snap the other back to match.

### Nodes / Settings
- Add-on panel "NS Wall Builder": Straight/Curved toggle, Pattern preset dropdown, Build Wall / Make Single buttons
- Dimensions: Rows, Cell Size, Brick Gap, Brick Depth, Seed, Wall Flip
- Bricks: brick color, coin color, brick color variation, mortar color, dirt/dust amount
- Jitter & Variation: Y/X/Z rotation jitter, Cracked Bricks Amount, Damage Bricks Amount
- Displacement: Material Displacement (needs Subdivision 3+), Damage Bricks Amount-driven displacement, Mid Level, Strength
- Filters: dirt/dust filter (Scale Width/Height/noise), crack-bump filter (Scale Width/Height/noise) — linked to their Jitter & Variation sliders
- Bevel modifier + Subdivision Surface modifier (later in stack); Bump: brick bump strength, separate coin bump strength
- No dedicated Colour Ramps section in this version (added later in v4.0)

### Difficulty
Intermediate (requires understanding the material-dependency setup before anything works, plus the same curve-construction and Displacement/Brick-Gap interaction as the newer version)

### Blender Version
5.1.x (approximate, viewport title bar in captured frames; not stated verbally).

### Tags
procedural, geometry-nodes, displacement, organic, product-viz, intermediate

---

## Related Tutorials
Part of the **NS Brick Wall Builder** guide set (Nick Sayce / NS add-on). This is the earlier full guide (2026-07-13); a newer, more complete v4.0 guide supersedes it with a reorganized panel and an added Colour Ramps tab.
- [NS Brick Wall Builder v4.0 Guide](ns-brick-wall-builder-v4-0-guide.md) — current/most complete guide, same add-on, later version — compare panel layouts (Colour Ramps section, Base Shape naming) before assuming controls match exactly.
- [NS Brick Wall Builder - Mimicking a Real Wall](ns-brick-wall-builder-mimicking-a-real-wall.md) — short real-world-reference technique tip, builds on this guide's base controls.
- [NS Brick Wall Builder - Mimicking a Real Wall 2](ns-brick-wall-builder-mimicking-a-real-wall-2.md) — part 2 of the above tip.
- [NS Rock Sculptor Guide - Sculpt Settings](ns-rock-sculptor-guide-sculpt-settings.md) — conceptual sibling: same author's other add-on family, also uses a "Make Single" detach mechanism.
