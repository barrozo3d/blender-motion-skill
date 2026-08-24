---
title: NS Brick Wall Builder v4 0 Guide
source: YouTube
url: https://www.youtube.com/watch?v=VZ7MObyyCJk
author: Nick Sayce
ingested: 2026-08-17
blender_version: "5.1.x (approximate, viewport title bar in captured frames; not stated verbally)"
tags: [procedural, geometry-nodes, displacement, organic, product-viz, intermediate, blender-5x]
extraction_status: complete
frames_dir: tutorials/frames/ns-brick-wall-builder-v4-0-guide/
frame_count: 9
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# NS Brick Wall Builder v4 0 Guide

**Source:** [YouTube](https://www.youtube.com/watch?v=VZ7MObyyCJk)
**Author:** Nick Sayce
**Duration:** 21m40s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Adding A curve [0:00]
**Transcript (timestamped):**
[0:00] Hello, welcome to this guide video for the latest NSBrick wall builder. It's going to be version 4. I've made a considerable amount of changes and I think it might be useful to have another guide video.
[0:17] I'm going to do all this in order as quickly as possible and separate it with time codes so you can quickly skip to whichever bit you need to know.
[0:27] But I'm going to do it in order and title it so make it as quick and easy as possible.
[0:32] So first step is getting the right curve for the add-on.
[0:37] And the way I built it was I started with a plane. I pressed M to merge at center.
[0:49] And then I take that one vertex in top mode with 7, I'll go EX2, EXY, 4. And then I get this shape.
[1:02] Now that's not going to work because it's still, as you see that icon, it's still a mesh. So you need to object, convert, curve.
[1:09] And the icon changes and that is ready for a wall. So if I just drop that straight into there, a wall will general aid.
[1:19] That's one. You could also do, I'll explain the actual, I'll talk about it now.
[1:25] The reason I went 2 and 4 is because this add-on really wants nice rounded even numbers.
[1:32] Getting it to work with corners was a nightmare. So I settled with pretty much 2 meters as the minimum you need for a wall to generate.
[1:40] If it's less, it'll give you an error in angle generating.
[1:43] So make sure you're always in even numbers. So 2, 4, 6, 7, 9, 12, whatever.
[1:53] Just they need to be no decimal places. Otherwise, it'll completely screw it up.
[1:58] Also, I was useful to tell you this now, this button here, wall flip.
[2:03] I only put that in case you decide to make a curve that starts going on the negative X axis.
[2:11] I build everything going on positive. If you go negative, this wall flip will flip the wall.
[2:18] If I show you and build wall, if I click wall flip, it's going to put them on the back of the wall.
[2:24] And that's purely there because if you decided to not recommend it, if you decided to make your first wall starting going negative X,
[2:35] you have to click wall flip, but the corner behavior won't work properly.
[2:39] So in short, don't go negative. Always build your curves positive, start positive, plus Y, plus X, whatever.
[2:49] Do that. Makes it easy.
[2:51] Okay, that's that.
[2:53] Now, where's my...
[2:57] So the other curve, because you've got straight mode and curved mode, the other curve wants a Bezier or a NURBS.
[3:05] Bezier for now will do.
[3:08] And then if you go between straight and curved, just click that. Otherwise, it will try and generate a curve, a straight wall on a curve.
[3:16] There are two different scripts and the behaviors are attic if it's on the wrong one.
[3:19] So make sure once you switch it over to curve, there's nothing in this. That's the box for the curve.
[3:26] So once I drag this in her, I'll get a curve wall.
[3:31] There we go.
[3:33] And that's...
[3:36] Edit the curve, do what you want with it. It will just follow it, but you have to, as I said, regenerate.
[3:43] So build wall.
[3:45] That's everything you need to know about the curves.
[3:48] Now, the next one I'm going to move on to is...
[3:54] We'll do the presets first. All right, the next one is going to be presets.


### Presets [3:56]
**Transcript (timestamped):**
[4:01] So presets.
[4:04] I'm going to keep this... I'm going to use this curve first. I'm going to get rid of that so nothing generates.
[4:11] And then if you click this button, you've got 11 straight and 11 curved.
[4:16] And they're separated. This is the best way I could separate them in the window.
[4:19] Blender is difficult when you're trying to put thumbnails in an add-on.
[4:22] So straight, curved. They don't work.
[4:25] Straight aren't going to work on a Bezier. They're just going to look messy.
[4:29] And the curves on a normal plane will probably look messy too.
[4:32] So stick to what they need to be on.
[4:35] So if I click broken standard, and then I have to click...
[4:40] Oh, nearly straight. Click build wall.
[4:44] Hello. I've got the wrong plane in the window.
[4:48] The curve.
[4:50] So and then you can just flick through, pick.
[4:53] Every time though, you've got to click build wall.
[4:55] I found it. I don't know why it keeps doing that.
[4:58] I found it annoying.
[5:00] Whenever I change preset, it immediately loaded the wall.
[5:04] That's something I need to look at why I need to keep changing that.
[5:07] But every time you should need to click build wall, that's something to do with a blender history.
[5:12] Nothing to do with the add-on, I don't think.
[5:14] But there's probably a guard for that. All right.
[5:16] So that's it. And then as I say, if you want to go over to curve mode,
[5:21] make sure there's nothing in your wall curve, then drop a Bezier or a NURBS.
[5:26] And then you get you all.
[5:28] And then if you change between these, so tidy common, again, you got to press build wall.
[5:33] And then you get that pattern.
[5:36] So you've got 11 of each to play with.
[5:41] And they can be a base that you can just use and then edit further or just use it.
[5:47] But that is presets.
[5:49] Next, we'll move on to these three buttons.


### Using the Buttons [5:54]
**Transcript (timestamped):**
[5:57] Okay. So that one we pretty much covered.
[6:01] You need that to generate a wall.
[6:02] We'll talk about reset to defaults.
[6:05] And I'm going to go back into straight just because I don't know why I prefer to work with a straight wall.
[6:11] Probably because I like the corners.
[6:14] Okay. So right there. Yeah, there's variation here.
[6:19] Let me just reset my variation.
[6:21] I don't want any variation.
[6:22] We'll get to these controls.
[6:24] That's a hang on from the last time I recorded this.
[6:27] Oh, pick the plane.
[6:29] Pick a plane.
[6:31] Don't. Okay.
[6:33] Okay. So now if I edited this, let's just say I did put some variation in again, we're going to get to this when we get there.
[6:46] So I've just varied the y-axis of these bricks, randomized them a bit.
[6:51] If I'm happy with that, but I want to build a new wall.
[6:55] I don't want to lose this.
[6:56] So if I click make single that effectively disconnects it completely from the add on.
[7:02] So the materials it uses become their own so you can edit them afterwards.
[7:07] The modifiers will remain.
[7:09] What you can't do is change the shape because that's only in the add on.
[7:12] So once you click make single, you've set the shape, then it's just visually and you can change it with those.
[7:18] So once I click make single, I can now add a new wall.
[7:23] Let's do a like drywall.
[7:27] And anything I do to this won't change the first wall.
[7:33] As you see, I can just, this is all independent.
[7:35] I can change everything about it.
[7:38] But because I click make single, this is now time thing and this one is brand new.
[7:43] And this button reset to defaults if like when this loaded, it's still got all the same variation.
[7:52] Everything was the same.
[7:53] The color was the same, the variation.
[7:55] Everything was the same.
[7:56] If you hit reset to defaults, it goes back to, it doesn't change the pattern, but it goes back to that strange.
[8:03] I need to look at that.
[8:04] It doesn't go back to, so it goes back to the pattern that you're working on, but just everything has gone back to default.
[8:11] So you can effectively start again.
[8:14] That's it.
[8:15] That's those three buttons done.
[8:16] We'll move on to this bit next.


### Base Shape [8:18]
**Transcript (timestamped):**
[8:19] All right.
[8:20] I'm just going to get rid of my, I just want to clean to me a segment.
[8:26] It's just quicker and I don't need a wall.
[8:28] So let's just do drywall, billboard.
[8:31] All right.
[8:32] So these here, let's talk about these.
[8:35] And there's another control which appears, which I'll go through in a second.
[8:39] So rows is just how high the wall is going to be.
[8:42] That's obviously double.
[8:44] I'm just keeping it at 12 brick gap.
[8:47] Again, that's fairly self-explanatory.
[8:50] If you go to 0.01, it's going to be tiny in it.
[8:55] If you go to 0.05, it's going to be massive.
[8:58] Some patterns have tiny bricks, so bricks will just disappear.
[9:01] If you go, if you brick gaps too high, I tend to, I like it around 0.02.
[9:07] Brick depth, just make the bricks thicker.
[9:11] It's useful if you want lots of brick variation without displaying the mortar underneath.
[9:16] You can just set the brick depth quite high.
[9:19] I mean, I would consider 0.2.
[9:21] I barely change that at all.
[9:23] Brick height doesn't work with every pattern.
[9:26] And there were reasons for that.
[9:28] I'm still working on it, but things like standard, if I do, because I couldn't change the width.
[9:34] I couldn't have people change in the width because it just messes up.
[9:38] In order for the corners to work and function properly, it was a nightmare,
[9:43] but it meant that I needed a standard width of bricks.
[9:47] So to kind of work around that, you've got a brick height.
[9:51] So if I wanted to stretch the bricks, I'd just drop that to 0.5
[9:55] and then just bring up the rows back to make it about the same height.
[9:59] It works for most patterns, but I don't want to do that.
[10:03] It works for most patterns, but some it's, I'm assuming herringbone probably doesn't.
[10:10] I'll be surprised if it does.
[10:12] No, it doesn't.
[10:14] But then, yeah, there's a couple that just I'll be working on.
[10:18] But that's how you would stretch bricks on the X axis by squashing them on the Y.
[10:28] All right.
[10:29] That's brick height.
[10:31] I'm going to go back to one, one being full height.
[10:34] Seed, this mostly just changes the colors.
[10:38] There are some patterns, I believe, regular should change.
[10:44] Yeah.
[10:45] So it just reshuffles it just for a bit of random variation.
[10:50] We've discussed wall flip.
[10:51] That is these bits done.
[10:53] Let's move on a brick color, shall we?


### Brick Colour [10:55]
**Transcript (timestamped):**
[10:55] Again, brick color.
[11:00] Drop that down and change your brick color, can't you?
[11:03] There you go.
[11:05] It's just slight random variations there.
[11:08] You've also got brick color variation, which just darkens the shades on some of the bricks.
[11:14] So again, more natural variation.
[11:17] Brightness and contrast I just put in because once I start adding dirt and brick color variation,
[11:22] you can see it darkens the bricks and I wanted to bring the brightness back.
[11:26] So I might put that up to 0.1 and then I would bring up the contrast by 0.5.
[11:38] No, that's fine.
[11:40] Brimstone 0.1, 0.2.
[11:44] Just to get that sharpness and the saturation back.
[11:48] So those colors, those controls are there if you'd like them.
[11:51] It darkens the edges of the bricks depending on your shape and if you can see the edges,
[11:55] there's no variation so we can't.
[11:57] And that's your brick roughness.
[11:59] If you want shiny bricks, do that.
[12:04] Coin color, just specifically for the coin pattern, you've got two controls there as well,
[12:11] which will change the color of the coin pattern independently to apparently pearlescent coin.
[12:18] That's color.
[12:20] Now let's move on.


### Mortar [12:21]
**Transcript (timestamped):**
[12:26] Mortar is one of the ones you're going to use a lot, this particular mortar depth.
[12:32] I'll show you why.
[12:34] Mortar color, we can't see it.
[12:36] So what I'm going to do is I usually do it this way, shift, left click and assuming I've got too many sub-dibs,
[12:41] it should update nicely.
[12:44] So they're just almost touching the front and you've got mortar cut one.
[12:49] Mortar color too.
[12:51] And again, these are just, it's a filter, a bit of variation.
[12:56] That's nice.
[12:58] Ambient occlusion, darkens around the bricks, not too visible because the bricks aren't sticking out too much.
[13:03] And again, mortar roughness, make it lighter, rough or not.
[13:08] So yeah, the mortar depth, that's the one you're going to use quite a lot
[13:12] because that's in conjunction with displacement and everything.
[13:15] That becomes very important as you will see shortly.
[13:19] Next up, jitter and variation.


### Jitter & Variation [13:21]
**Transcript (timestamped):**
[13:25] This is the fun one, jitter and variation, because this is where you can add some real natural variation.
[13:32] I normally start with the Y and depending on how old the wall is or what your requirements are,
[13:39] you can mess around with all of it.
[13:41] So you know, high Z rotation, these are in degrees as it says.
[13:46] You can really start to mess up the wall using X, Y and Z.
[13:51] And then depth variation, we're not going to see too much because the mortar's right there.
[13:55] So I'm going to bring the mortar back so we can see more brick.
[13:59] And then depth variation, 0.04.
[14:03] I'm going to just reduce the mortar again.
[14:06] So I mean, you just be going back and forth all the time.
[14:10] I might actually increase the brick depth to 0.2 just so we can really see that depth variation.
[14:19] There you go. Beautiful, beautiful.
[14:21] So again, more natural variation, scale variation, smaller man to 0.05.
[14:27] It just slightly scales each individual brick.
[14:31] Yeah, a bit smaller.
[14:33] So again, even more natural variation.
[14:36] I'm all about the natural variation.
[14:39] Okay, general variation, bush, done.


### Displacement [14:42]
**Transcript (timestamped):**
[14:46] Displacements.
[14:48] All right, you've got a few choices.
[14:50] Displacement modifier, which is what it says.
[14:54] It adds a displacement modifier and it uses like the cloud noise pattern, jubby.
[14:59] So you've got all its controls there.
[15:03] And this is where you set your brick subdivision server on one so it not a lot's happening.
[15:08] If I take that up to three, we'll see a bit more detail.
[15:13] And in this instance, I would like the noise scale to be higher than that.
[15:17] That's too much wobbly, wobbly as be it up.
[15:20] And I say, once you start adding displacement, the bricks start to get a little bit fatter.
[15:25] So I would now go back to brick gap and just decrease that to 0.01.
[15:32] And no, increase that to 0.04.
[15:37] Just to get that gap back a bit, get that gap back.
[15:41] And the material displacement is too.
[15:44] There's this one I'm actually still working on because that does very little.
[15:50] And I think it's something to do with the color ramp.
[15:53] Material displacement one, don't worry about this.
[15:55] I'll show you.
[15:57] Yeah, there's something going on with that.
[15:58] So I'll work it out.
[15:59] Don't worry.
[16:00] But I do know that material placement two, which is this slider here is it's kind of a crack type affair.
[16:09] Don't worry about the jiggy jaggy because when we get to color ramps, we'll we'll talk about that.
[16:14] But for now, we'll leave that.
[16:16] And then you've got your mid level and how much power.
[16:20] And even adding that has added a bit more fatness.
[16:24] So I'm going to put that brick gap now up to 0.06.
[16:28] And this is very soft at the edges.
[16:30] When we get to bevel, we'll see how to fix that.
[16:32] All right, displacement done.


### Filters [16:34]
**Transcript (timestamped):**
[16:38] Filters.
[16:39] This one's really useful.
[16:42] I won't go through all of them, but all the ones you need to hear.
[16:46] So the dust filter, if I just crank that up, it adds that dust and colors.
[16:53] It's based on screen.
[16:55] So light colors will do something if you lower to darker colors, they're just going to vanish.
[17:01] So that the whole point being called dust and then there's one underneath called dust.
[17:05] And it's a noise filter.
[17:06] So you've got all your usual scale jobbies distortions.
[17:10] That's just to stretch it on an axis.
[17:12] Ladettes either or or ladettes.
[17:17] And yeah, you would play with that.
[17:20] Now there's more control with the color ramps.
[17:23] We'll get to that.
[17:25] And yeah, add some, add some variation.
[17:28] Again, this is a multiply.
[17:29] So the darker the color, the more it's going to be visible.
[17:33] We need to see that more.
[17:35] So I'm going to get to the color ramps and we'll deal with that.
[17:38] But you've got all these filters for everything you need, basically.
[17:43] Filters done.


### Colour Ramps [17:45]
**Transcript (timestamped):**
[17:49] Color ramps.
[17:51] These are really useful.
[17:52] The easiest one to show you how they work.
[17:55] I mean, if you know how color ramp works, you know, this works.
[17:58] So I've just re cranked up the dust and now I've picked the dust color ramp.
[18:04] And if I add or take away the black, I'm going to get more of that filter so you can fine tune how this filter appears.
[18:14] You could have little bitty, bitty, bitty or more of it, whichever, whatever takes your fancy.
[18:21] And there's one for, in the color ramps, there's one for dirt, which I'm going to change that color.
[18:29] And I'm going to have more dark and a bunch of new select so we can really see that thing.
[18:38] It's just a bitty dirt, bitty dirt.
[18:42] And again, you've got color ramps for all of them.
[18:46] So if we went to material displacement two, which is this one, I can edit that as well.
[18:54] So you're just rounding out those cracky bits or whatever, or you can make it more obvious that it's messing up the bricks.
[19:02] Dada, it's all going to depend this as well.
[19:05] The smoothness on your displacement levels on at three, go into four that probably sort it right at.
[19:11] Yeah, that'll do it.
[19:13] So that's how you would muck around with color ramps to edit the actual filters that are being used.
[19:21] That's color ramps. We're getting there. Bevel next.


### Bevel & Bump [19:24]
**Transcript (timestamped):**
[19:27] So bevel, is either enabled or it's not.
[19:31] Because we've had a lot of displacement, it's rounded off the edges.
[19:35] You can't completely get rid of it.
[19:37] But what I would do in this instance, if I still wanted them very square, is bevel width at the most, 0.01, I would go 0.001.
[19:46] And that, as I say, you can't completely flatten them off again when you've got displacement, but that's closer to what I want.
[19:54] Not much else to talk about with bevel.
[19:56] So I'm just going to do bevel and bump in the same one.
[19:59] Yeah, you know, bevel works, works, works.
[20:02] So let's do bump as well.
[20:05] Three different types.
[20:08] You crank up pattern bump.
[20:10] This is just the bump that goes across all the bricks.
[20:13] And there's two. There's this, which is just the standard bump.
[20:17] And if you go all the way to one, you've got the cracks bump, which are these little ee-ee-ee.
[20:22] And again, the text is cool because all the bricks have their own UV space all over the place.
[20:26] So you don't see a continuation of a crack from one brick to another. It's bare natural, bruv.
[20:33] Some tricks I like to do is if I want to darken up these even more, I could, if I go over one and put 1.2, see, it blackens up those areas.
[20:46] If I went all the way left, I would be getting these.
[20:49] And if I wanted to, with the bump I've selected, which is, excuse me, standard bump one, if I wanted more roughness all over the bricks,
[20:56] I'm going to go to standard bump A and then I'm going to allow it to spread out more, you see.
[21:04] And now that really looks like a proper messed up, burnt up wall, 100% procedural.
[21:12] And there's a coin bump just for the coin bricks themselves and mortar bump, which you can't really see in this.
[21:20] But yeah, that's literally everything.
[21:24] I know it took a little bit of time, but that's why it's time stamped.
[21:27] Okay, sweet. I hope that's everything you need to know to get going with this.
[21:31] I really enjoy working with this and playing with it. It's awesome.
[21:35] All right, sweet ass. I'll see you in a bit. Bye.



---

## Captured Frames

- [0:37] tutorials/frames/ns-brick-wall-builder-v4-0-guide/frame_000.jpg
- [1:09] tutorials/frames/ns-brick-wall-builder-v4-0-guide/frame_001.jpg
- [4:11] tutorials/frames/ns-brick-wall-builder-v4-0-guide/frame_002.jpg
- [6:56] tutorials/frames/ns-brick-wall-builder-v4-0-guide/frame_003.jpg
- [8:39] tutorials/frames/ns-brick-wall-builder-v4-0-guide/frame_004.jpg
- [12:26] tutorials/frames/ns-brick-wall-builder-v4-0-guide/frame_005.jpg
- [14:46] tutorials/frames/ns-brick-wall-builder-v4-0-guide/frame_006.jpg
- [17:49] tutorials/frames/ns-brick-wall-builder-v4-0-guide/frame_007.jpg
- [20:05] tutorials/frames/ns-brick-wall-builder-v4-0-guide/frame_008.jpg

---

> **Third-party add-on note:** This is the full guide to **NS Brick Wall Builder v4.0**, a paid third-party Blender add-on by Nick Sayce (NS) — a curve-driven procedural brick wall generator, conceptually the same author/family as NS Rock Sculptor and NS Infinite Rock Builder but for masonry. Every control named here (Build Wall, Make Single, Rows/Brick Gap/Brick Depth/Brick Height, Filters, Colour Ramps, Bump types) is the add-on's own UI, not stock Blender geometry nodes.

## Structured Notes

### Core Technique
A curve object (built from a specific merged/extruded plane shape, or a Bezier/NURBS for curved walls) drives the add-on's wall generator: dropping the curve into the add-on's curve slot and clicking "Build Wall" procedurally tiles a chosen brick pattern along it, with dozens of downstream controls for scale, color, mortar, jitter, displacement, filters, bevel and bump layered on top.

### Summary
The most complete guide in the add-on's series — a full tour of v4.0's panel, top to bottom. **Curve setup:** the wall-generator curve must start as a Plane merged to a single vertex (M → Merge at Center) then extruded in round-number increments (the presenter uses E, X, 2, then E, X, Y, 4) before being converted (Object → Convert → Curve) — the add-on requires whole-number, even-numbered curve segment lengths (minimum ~2m) or corner-angle generation breaks; curves must be built running in the positive X/Y direction only (a "Wall Flip" button exists as a fallback for negative-direction curves, but corner behavior isn't reliable in that case). A separate "Straight ↔ Curved" mode toggle switches the underlying generator script between a straight-brick pattern (works on the merged-vertex curve type) and a true curved-wall pattern (needs an empty Bezier/NURBS curve instead) — mixing the wrong curve type with the wrong mode produces broken results. **Presets:** 11 straight + 11 curved preset patterns, each restricted to its matching curve mode; selecting one still requires clicking "Build Wall" to regenerate. **Buttons:** "Build Wall" (regenerate), "Reset to Defaults" (reverts all sliders to default while keeping the current pattern), and critically "Make Single" — detaches the wall from further add-on-driven edits, giving it independent materials so a new wall can be built without altering the first; shape becomes fixed at that point (only material/visual edits remain possible). **Base Shape:** Rows (wall height), Brick Gap (mortar-line width, ~0.02 sweet spot), Brick Depth (brick thickness, useful to hide mortar detail underneath at high variation), Brick Height (squash/stretch on the Y axis to fake width changes since brick width itself is locked per-pattern for corner math to work; doesn't work with every pattern, e.g. Herringbone), Seed (reshuffles color/pattern variation), Wall Flip. **Brick Colour:** base color, brick color variation (per-brick darkening), Brightness/Contrast (compensates the darkening from dirt/variation filters), Brick Roughness, and pattern-specific Coin Colour controls. **Mortar:** Mortar Depth (used constantly, works together with Displacement), Mortar Colour + Colour 2 (filtered variation), Ambient Occlusion, Mortar Roughness. **Jitter & Variation:** per-axis (X/Y/Z) rotation jitter in degrees, Depth Variation, Scale Variation — the "natural imperfection" layer. **Displacement:** a real Displacement modifier using cloud noise (controlled via Subdivision level + noise scale) plus two "Material Displacement" filter-driven slots (crack-type patterns, tuned via their own Colour Ramps) — adding displacement visibly fattens brick silhouettes, requiring Brick Gap re-tuning afterward. **Filters:** Dust (Screen blend — light colors show, dark colors vanish) and Dirt (Multiply blend — opposite), each with their own noise controls (scale/distortion). **Colour Ramps:** the fine-tuning layer for every filter above (Dust Colour Ramp, Dirt, Material Displacement 2, etc.) — dragging ramp stops changes how bitty/subtle vs. bold each filter reads. **Bevel & Bump:** Bevel (on/off + width, needed to re-sharpen edges that displacement has rounded off — can't be fully restored but gets close) and three independent Bump layers (Pattern Bump/standard bump, a "cracks" bump variant with per-brick randomized UV space so cracks don't visibly continue brick-to-brick, plus dedicated Coin Bump and Mortar Bump for pattern-specific detail).

### Key Steps
1. Build the generator curve: Add a Plane → Tab to Edit Mode → M (Merge at Center) → collapse to one vertex → Numpad 7 (top view) → E, X, [even number] to extrude along X, then E, Y, [even number] along Y to form an L/corner shape → exit Edit Mode → Object → Convert → Curve. Keep all segment lengths whole, even numbers (2, 4, 6...), minimum ~2m, or the add-on throws an angle-generation error.
2. Keep the curve building in the positive X/Y direction; only use "Wall Flip" as a fallback for a curve that had to start in the negative direction (corner math is unreliable there).
3. For curved (non-straight) walls: toggle the mode switch to "Curved," and use an empty Bezier or NURBS curve instead of the merged-vertex-plane curve — the two modes run different generator scripts and are not interchangeable.
4. Drop the curve into the add-on's curve slot, pick a pattern (11 straight or 11 curved presets, or build one manually), and click "Build Wall" to generate — every settings change (including switching presets) requires clicking Build Wall again to take effect.
5. Tune Base Shape: Rows for height, Brick Gap (~0.02 typical) for mortar-line thickness, Brick Depth for brick thickness, Brick Height to squash/stretch bricks (works on most but not all patterns — e.g. not Herringbone), Seed to reshuffle color variation.
6. Tune Brick Colour, then Mortar (Depth/Colour/AO/Roughness) — Mortar Depth interacts directly with Displacement, so revisit it after adding displacement.
7. Add Jitter & Variation (per-axis rotation in degrees, Depth Variation, Scale Variation) for natural, non-uniform brick placement.
8. Add Displacement: enable the Displacement modifier (cloud-noise driven, tune via Subdivision level + noise scale), optionally layer in the two Material Displacement slots for crack-like detail (fine-tuned via their own Colour Ramps) — expect brick silhouettes to fatten, so re-tune Brick Gap afterward.
9. Use Filters (Dust = Screen blend, favors light colors; Dirt = Multiply blend, favors dark colors) for grime/weathering, each with noise scale/distortion controls.
10. Use Colour Ramps to fine-tune exactly how any filter above reads (bitty vs. broad, subtle vs. bold) — this is the shared fine-control layer for Dust, Dirt, and both Material Displacement slots.
11. Enable Bevel (with a small width, e.g. 0.001-0.01) to re-sharpen edges softened by displacement, then dial in the three Bump layers (Pattern/standard Bump, a randomized-per-brick "cracks" Bump variant, plus dedicated Coin Bump and Mortar Bump) for final surface micro-detail.
12. To branch into a second, independently-editable wall without disturbing the first: click "Make Single" on the first wall (detaches its material from the add-on's live generator — shape becomes fixed, only visual/material edits remain possible), then build a new curve/wall from scratch. Use "Reset to Defaults" to revert all sliders on the current pattern back to their starting values.

### Nodes / Settings
- Add-on panel "NS Wall Builder": curve/pattern setup, Presets (11 straight + 11 curved), Build Wall / Reset to Defaults / Make Single buttons
- Base Shape: Rows, Brick Gap, Brick Depth, Brick Height, Seed, Wall Flip
- Brick Colour: base color, brick color variation, Brightness, Contrast, Brick Roughness, Coin Colour (pattern-specific)
- Mortar: Mortar Depth, Mortar Colour 1/2, Ambient Occlusion, Mortar Roughness
- Jitter & Variation: X/Y/Z rotation jitter (degrees), Depth Variation, Scale Variation
- Displacement: Displacement modifier (cloud noise, Subdivision level, noise scale), Material Displacement 1/2 (filter-driven, each with own Colour Ramp)
- Filters: Dust (Screen blend) + noise controls, Dirt (Multiply blend) + noise controls
- Colour Ramps: per-filter fine-tuning (Dust, Dirt, Material Displacement 2, etc.)
- Bevel: on/off + width; Bump: Pattern/standard Bump, Cracks Bump (randomized per-brick UV), Coin Bump, Mortar Bump

### Difficulty
Intermediate to Advanced (curve construction rules are unforgiving — even-number/whole-number segments, positive-direction-only — and the interaction between Displacement, Brick Gap, Mortar Depth and Bevel requires iterative back-and-forth tuning)

### Blender Version
5.1.x (approximate, viewport title bar in captured frames; not stated verbally) — consistent with the NS Rock Sculptor Guide series from around the same period.

### Tags
procedural, geometry-nodes, displacement, organic, product-viz, intermediate, blender-5x

---

## Related Tutorials
Part of the **NS Brick Wall Builder** guide set (Nick Sayce / NS add-on). This is the current/most complete guide (v4.0); an earlier, differently-versioned full guide also exists, plus two short "Mimicking a Real Wall" tip videos.
- [NS Brick Wall Builder Guide](ns-brick-wall-builder-guide.md) — earlier full guide for a previous add-on version; note the version difference when comparing panel layouts.
- [NS Brick Wall Builder - Mimicking a Real Wall](ns-brick-wall-builder-mimicking-a-real-wall.md) — short real-world-reference technique tip, builds on this guide's base controls.
- [NS Brick Wall Builder - Mimicking a Real Wall 2](ns-brick-wall-builder-mimicking-a-real-wall-2.md) — part 2 of the above tip.
- [NS Rock Sculptor Guide - Sculpt Settings](ns-rock-sculptor-guide-sculpt-settings.md) — conceptual sibling: same author's other add-on family, also uses a "Make Single" detach mechanism and Colour Ramp-driven filters.
- [NS Infinite Rock Builder Guide - Main Controls](ns-infinite-rock-builder-guide---main-controls.md) — conceptual sibling: same author, same "Make Single" pattern for branching independent copies.
