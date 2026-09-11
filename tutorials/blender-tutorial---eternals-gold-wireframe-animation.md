---
title: Blender Tutorial - Eternals Gold Wireframe Animation
source: YouTube
url: https://www.youtube.com/watch?v=WmldjCv9P84
author: Blender Made Easy
ingested: 2026-06-25
blender_version: "Blender 3.0.0 Beta -- observed in frame_001, frame_002"
tags: [animation, curves, shaders, materials, motion-graphics, vfx, wireframe, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/
frame_count: 15
frame_status: complete
grounding: key-steps-anchored (15/15 steps, 2026-09-11)
frame_selection: explicit-timestamps (supplied to select_frames.py; NOT evidence that the frames were read -- see `grounding:`)
---

# Blender Tutorial - Eternals Gold Wireframe Animation

**Source:** [YouTube](https://www.youtube.com/watch?v=WmldjCv9P84)
**Author:** Blender Made Easy
**Duration:** 14m24s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### <Untitled Chapter 1> [0:00]
**Transcript:** Hello everyone and welcome to another Blender Made Easy tutorial.  Today I'll be learning how to create this Gold Wireframe build animation in Blender.  I got this idea from the new Marvel film Eternals from this scene right here, where the weapon  creates itself.  I thought it looked pretty cool so I decided to recreate this effect in Blender.  Using any Curve object you are able to create this.  For this animation I used a single vertex and I basically traced out the sword and then  converted it to a curve.  To keep things simple I'm going to be using the Blender logo for this tutorial.  Fortunately for us the Blender logo actually has an option for us to download it as an SVG.  I will link this page in the description.  Once you have it you can jump over into Blender and then import it in by going over to file  down to import and then selecting the SVG.  Once you import it in it's very very small so make sure you select everything by box  selecting it and then scaling the entire thing up.  We're going to scale it up pretty big and then place it in the middle of our scene.  We don't really need the extra objects so select the extra parts of the logo and delete  them because you're not going to need them.  We only really want the main part of the logo.


### Fixing the Curve [1:09]
**Transcript:** Now that we have the logo in our scene let's go over the Curve settings and I'm going  to talk about how to create this effect.  To make things simple let's select both of these and press Ctrl J to join them together  as one curve object.  Next over in the Fill mode we don't really need it, we don't need a face so switch it  over to none right there.  If we open up the geometry tab we can give it some thickness by changing the depth right  here.  You'll notice though if I drag it up just slightly it creates a huge amount of bevel  even though the value is so small.  Well the reason for that is because we scaled everything up really big so make sure you  press Ctrl A and apply the scale.  Next if we go into Edit mode and press A to select everything and open up the properties  tab by hitting N you're going to notice the mean radius is set to 284.  That means it's going to multiply the depth by that value.  That's not going to look very good and that's why it's scaling everything so big.  So make sure you set the mean radius down to a value of 1 and now the depth should actually  work correctly.  So if we drag this up you're going to see it's actually working properly.  The next step is to clean up our curve you'll notice that there's some parts of the  curve that have these weird shading issues and the reason that's happening is because  there are two vertices right on top of each other.  If we go into edit mode we can select the one X and then delete that vertex that will  fix the issue go around the curve and make sure you do that for every single part that  has that weird issue.  Now let's talk about how to animate the build effect and that is done by using the start  and end in the mapping section over here in the geometry panel.  At the moment if we drag this up you can see it's not working and that's because our  curve is a complete loop we need to add in a hole in the middle of our curve.  You might think to go into edit mode and then delete one of the vertices but you're  going to notice that it doesn't create a hole it's still right there it's a complete  loop instead what you need to do is select two vertices then press X and delete the  segments not the vertices delete the segments and that will create a hole in the middle.  From there select one of the parts and then just fill out the hole so we'll select right  there press E to extrude and drag it down until it's right in the same position just like  that.  Now what happens is if we drag up the start you're going to see that this is the effect  that we're getting we can actually animate this value and it will create the build effect.  We need to do that exact same thing for the inner circles so go into edit mode and  delete two of the segments so select two of them X and delete the segments then grab  them and move them into place.  Keep in mind wherever you create this hole that is worthy build animation is going to  start so if you want your animation to start building at this point then create a hole  right there but if you want it to start building over here create a hole right here on  this curve.


### Animating the Curve [4:12]
**Transcript:** To actually get the build effect we need to animate the end value if we drag this down  you're going to notice that it starts to create this effect but there are two problems.  One problem is I don't want it to go in this direction I want it to go in the opposite  direction and another problem is I don't want these to go in the same direction I want  one to go this way and the other one to go this way.  So to fix that you can go into edit mode we'll select the outer logo right here and then  we'll select the inner logo and press control L and then to switch the direction all you  have to do is right click and then click on switch direction.  So let's animate this value I'm going to bring the end frame all the way down to zero  and then add in a keyframe right on that side.  We're going to jump all the way to frame 200 and drag the end all the way up to a value  of 1 and then add in another keyframe.  Let's take a look at this by restarting our animation and playing it and this is the  effect that we're getting.  Now let's talk about the mapping start and end values.  These are how the mapping is going to affect the animation with it set to resolution what  it's going to do is it's going to take the geometry of your object and base the end  value on that.  For example if we scroll up to this part of our logo and then we scroll forward a little  bit you're going to see at this point if we go into edit mode there's a big chunk  that is missing a lot of geometry.  So this part is going to go very fast and then play it you can see this part slow this  parts fast and then it becomes slow again because there is more geometry.  That is because the end is set to resolution.  The segment work a little bit different it takes the number of subdivisions and the length  of each segment and bases the end value on that.  You can see here if I select the same widths and restart it's going to create this effect  which is a little bit different but you'll notice this part is still a little bit faster.  What we want is we want the end to be set over to spline this will take the entire length  of the curve and base the end on that.  So now everything is going to move at the exact same speed all throughout the entire animation  and that is what we want.  If we go to the middle of our animation you're going to notice that it's very harsh along


### Adding Taper [6:22]
**Transcript:** this side.  So now what we're going to do is we're going to create a taper effect using this taper  option over in the geometry panel.  How this works is we need to add in a new curve, suppress shift A, go over to curve  and then add in a busier curve.  Go into edit mode and then we're going to drag this down so it's completely flat.  From this point select your original logo and for the taper object select the new curve  that we just added.  You'll notice everything disappears but don't worry it's still there.  We need to go into edit mode on our new curve and then move the vertices around.  If we drag the right vertex up you're going to see this is the effect that we're getting.  Now we have that taper effect.  So now if we restart and play it this is the effect that we're getting.  But you can see it's actually inverted so what we need to do is select it and then click  on map taper and that will fix that issue.  If it's still thick on one side all you have to do is just invert it so we'll drag this  part down and then we'll drag this vertex up like that and that's going to give us the  effect that we need.  So now for your restart and play it here is the result that we're getting.  At this point you can control how thick that part on the end is.  If you want it to be thicker just drag this value up.  If you want it to be thinner drag it down.  A note thing to keep in mind is if you go in the negative direction along the Y it's  actually going to add thickness on the outer edge of the curve.  As you can see the part where it's thinner is actually in the middle rather than the  end.  So make sure this vertex is above in the positive direction along the Y and that'll  make sure it's thin just like that.  So after playing around with the depth value and the thickness of the curve I think this  is a good result.  Let's go ahead and restart our animation and play it and here is the result that we're  getting.  As you can see that looks much better because it has that taper effect.


### Animating the Taper [8:20]
**Transcript:** Finally, the last thing that we'll do for this animation is we're going to delete that  taper effect at the end of the animation.  Our animation ends at frame 200 so let's get rid of the taper at 200.  To do that we need to animate this shape of this be easier curve.  You can do this by adding in some shape keys over in the curve properties.  We're going to add in a new basis curve shape and then we'll add in a keyframe right there.  With the value set at zero this is the shape that we're going to get.  We're going to drag this value all the way up and then go into edit mode.  To make the taper disappear we need to drag this up until the vertices are in line with  each other.  So right about there is perfect just like that so it's a completely straight line.  And as you can see the taper is now gone.  If we drag this value down to zero now you can see the curve goes back to its original  position and the taper reappears.  If we drag it all the way up to one the taper disappears and now this curve is very flat.  So all we have to do is animate this value on frame 150.  We're going to drag this all the way down to zero add in a keyframe then on frame 200  when the animation ends this is going to go all the way up and the taper will disappear.


### Gold Material [9:34]
**Transcript:** Now before this tutorial ends let's create that gold metallic material with that really  cool light going across it.  Over in the material tab we're going to click use notes to create a new material.  What we need to do first is create that gold look.  We're going to bring the metallic all the way up to one and the roughness all the way  down to point one and then for the base color we're going to select a nice gold color  somewhere around there.  Let's press Z and go into render view to see what we're doing.  Next we're going to add in any mission so we'll press shift A add in a shader and  emission then we'll add in a mix shader and mix these two together.  We'll deal with the color and the strength of this later but for now we need to add in  where we want the emission to be on our curve.  What we're going to do is add in a texture and a noise texture.  Then with the node wrangler add on enabled you can press control T to add in a mapping  and a texture coordinate node.  Instead of using the generated we're going to use the UV and plug it into the vector.  Let's take a look at this by control shift left clicking on the noise texture.  To see this a bit better we're going to add in a color ramp and then drag the black  handle closer and the white handle closer as well and here is the effect.  Using the UV node from the texture coordinate node will allow us to move the noise texture  along the curve.  You can do this by animating the x location.  If we drag the x location up you can see it's actually moving along the curve.  If you look down here it's going to move along the curve just like that.  So this is going to give us a really cool effect once we animate this.  To animate it we're going to go hashtag frame to add in a new driver divided by 250.  Now if we play this this is the result that we're getting.  So we're basically going to take this noise texture as a mask for the emission.  Before we do that though there is a couple of settings that I want to change in this  noise texture.  First off the scale I want to drag up to 15 and I don't want there to be any detail  so I'm going to drag that down to zero.  The roughness I'm also going to drag down to a value of .2.  If we take a look at the noise texture you can see we have these long streaks right here  which I don't really like.  To fix that we can set the scale of the y to a much lower value.  Let's go .05 and enter.  And then here is the result that we get.  Now we have actual like splotches of noise which we can use for the emission.  I only want the emission to appear along the edges of where the noise is.  We can do this by adding in an input and a fronel node.  We'll place it above the noise texture.  We'll then take the color wrap and shift it and drag it above.  We'll take the factor, plug it into the factor and then control shift left click on this.  As you can see there is a thin line along the top and bottom of our logo.  We can control this line by changing this value here.  If you go lower it's going to appear more like that.  Let's go with a value of about .9.  Then to actually mix these two together we're going to add in a converter, math node and  place it here.  We'll take the color, plug it into the bottom input and then set this down to multiply.  We can take the value and plug it into the mix shader factor and then we can control shift  left click on this.  Now you can see the effect that we're getting.  If we then drag the strength of the emission up to let's say 50, here is the effect that  we have.  As for the color of the emission you can use the same color as the base color for the  principal shader.  And that's the effect that we get.


### Render Settings [13:06]
**Transcript:** And that is basically it for the material.  After this you can experiment with the strength of the emission.  You can also enable bloom in the render settings, add in a plane and a dark background and  you can create some really cool results.  Another thing I wanted to mention in this tutorial is this effect right here where we have  some weird glowing issues along the curve.  That is due to the filter size and the sample count.  The filter size basically helps the render look a bit better.  If you bring this a lot lower it's going to make that effect even worse and the splatging  is going to appear more visible.  But if you go too high it becomes way more grainy.  So I found a value of about 1.8 works for this scene.  You also want to bring up the sample count.  You can see my viewport is at 16 but if I drag this up to 256 that's going to help smooth  out that line as you can see there.  So for the render amount I'm going to bring it up to 256.


### Outro [14:00]
**Transcript:** And there you go that is the end of this tutorial.  Thank you very much for watching.  If you learned something new or created your own cool wireframe build animation I would  love to see it so make sure to send it to me on Instagram at BlenderMadeEasy.  If you have other suggestions for tutorials in the future leave a comment down below and  I'll be sure to check it out.  Thanks again for watching and I will see you in the next one.



---

## Captured Frames

- [0:50] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_000.jpg
- [1:55] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_001.jpg
- [2:20] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_002.jpg
- [3:10] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_003.jpg
- [3:30] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_004.jpg
- [3:50] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_005.jpg
- [4:50] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_006.jpg
- [7:00] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_007.jpg
- [8:50] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_008.jpg
- [9:55] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_009.jpg
- [11:10] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_010.jpg
- [11:45] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_011.jpg
- [12:15] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_012.jpg
- [12:35] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_013.jpg
- [13:30] tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/frame_014.jpg

---

## Structured Notes

### Core Technique
Animate a curve's Geometry > End value (0→1) over time to create a "drawing on" build effect; add a Bezier taper curve that's dissolved via shape keys at the end; a Noise Texture masked by Fresnel and animated along curve UV via a driver creates a moving golden light streak on a metallic Emission material.

### Summary
Blender Made Easy recreates the Eternals weapon-building effect using a curve SVG import. The core trick: set Mapping mode to Spline and animate the Geometry End value from 0 to 1 so the curve draws at constant speed. A `BezierCurve` assigned as Taper Object [frame_007] adds a pointed tip that disappears at the end of the animation via Shape Key animation (taper curve from angled → flat). The gold material uses Principled BSDF (metallic=1, roughness=0.1) mixed with an Emission shader — a Noise Texture animated along the curve UV via a driver (`#frame/250` on X Mapping location) and masked by a Fresnel node creates a moving golden highlight streak. Rendered in **EEVEE** with Bloom and Screen Space Reflections [frame_014], not Cycles as this entry previously recorded.

### Key Steps
1. **Import the SVG.** `File ▸ Import ▸ SVG` brings the artwork in as **many separate curve objects** — the outliner lists `path1273`, `path1275`, `path1279`, `path1287`, `path1291`, `path1295`, `path1299`, `path1305`, `path1309`, `path1313` under `blender_community_badge_white.svg` — and at a tiny scale, so box-select everything and scale up [frame_000, transcript 0:46].
2. **Join and set the curve up.** `Ctrl+J` to join the parts, `Fill Mode: None`, `Ctrl+A` to apply scale. The curve data panel shows `Shape 2D`, `Resolution Preview 12`, `Curve Deform ▸ Radius` on, and a `Geometry` block holding `Offset`, `Extrude`, `Taper Object` and `Taper Radius` (set to **`Override`**) [frame_001].
3. **Thickness is `Depth` under `Bevel`, not under `Geometry`.** Bevel offers `Round` / `Object` / `Profile` with `Depth`, `Resolution` (`4`) and `Fill Caps`; it starts at `Depth 0 m` [frame_001] and the finished tube here sits at **`0.018 m`**, giving the object dimensions `2.21 × 1.8 × 0.036 m` [frame_002].
4. **Fix Mean Radius first, or Depth misbehaves.** Edit mode ▸ `A` ▸ `N` panel: `Mean Radius` reads **`284.094`** after the scale-up (with `Mean Weight 0.000`, `Mean Tilt 0°`) and must be set to `1`, because it multiplies the bevel depth [frame_001, transcript 1:49].
5. **Clean up the doubled vertices.** Two control points sitting on top of each other pinch the tube and produce a visible shading glitch at the corner [frame_003]; delete one at each such location [transcript 2:14].
6. **Make a hole so the build animation has a start and an end.** Deleting a vertex does not open the closed loop [transcript 3:00]; instead select two adjacent points, `X ▸ Delete Segments`, then move the ends into place [frame_004, transcript 3:42] and `E` to extrude and bridge where needed [frame_005, transcript 3:21].
7. **Animate the build with `Start & End Mapping`.** The panel carries `Factor Start` / `Factor End` — the animated pair — plus separate `Mapping Start` / `Mapping End` dropdowns which default to **`Resolution`** [frame_005]. Keyframe `Factor End` from `0` at frame 0 to `1` at frame 200; mid-draw it reads **`0.299`** with roughly a third of the logo drawn [frame_006]. Set `Mapping End` to `Spline` for an even drawing speed.
8. **Build the taper curve.** `Shift+A ▸ Curve ▸ Bezier`, then in edit mode flatten it to a horizontal line at the origin — a separate `BezierCurve` object with its own `Bevel Depth 0 m` [frame_007, transcript 6:38]. Assign it as `Taper Object` in the main curve's Geometry panel and enable `Map Taper`. Vertex Y positions control the taper profile (positive Y = thin at the end, negative Y = thin in the middle).
9. **Animate the taper away with shape keys.** On the taper curve add **`Basis`** (the current tapered shape) and **`Key 1`**, `Relative` on, `Relative To: Basis`, `Value 0.000` with `Range Min 0.000 / Max 1.000` [frame_008]. In `Key 1`, flatten the curve to a straight horizontal line so the taper vanishes, then keyframe the shape-key `Value` from `0` at frame 150 to `1` at frame 200 [transcript 8:26].
10. **Gold material.** `Principled BSDF` (`GGX`, `Random Walk`): **`Metallic 1.000`**, **`Roughness 0.100`**, `Specular 0.500`, `IOR 1.450`, gold `Base Color`; material `SVGMat.022` [frame_009, transcript 9:49].
11. **Drive a streak along the curve.** `Texture Coordinate (UV)` → **`Mapping`** (`Type: Point`) → `Noise Texture` (`3D`). Animating the Mapping node's **`Location X`** slides the pattern along the curve — caught mid-drag at `1.07 m` [frame_010, transcript 10:56] — and the tutorial drives it with `#frame/250` rather than keyframes [transcript 11:20].
12. **Tune the noise into streaks.** The Noise Texture is set to **`Scale 15.000`, `Detail 0.000`, `Roughness 0.200`, `Distortion 0.000`**, with the Mapping node's `Location X` at `0.768 m` [frame_011]. (An earlier moment in this chapter catches the node still at its `Scale 5.000 / Detail 2.000 / Roughness 0.500` defaults, which is why this entry once recorded those figures as unconfirmed — the frame here confirms the tuned values.)
13. **Add a Fresnel so the emission rides the edges.** A `Fresnel` node feeds a `ColorRamp`; the frame catches it at the default **`IOR 1.450`** [frame_012] before the narration lowers it to about `0.9` [transcript 12:26]. Two `ColorRamp` nodes (`RGB`, `Linear`) compress the ranges — positions **`0.136`** and **`0.459`** [frame_013, frame_012].
14. **Mix the emission in.** An `Emission` shader — white `Color`, **`Strength 39.800`** — and the Principled BSDF meet at a **`Mix Shader`** (`Fac 0.500`), with the ramp output driving the factor [frame_013]. (The "Strength ~50" this entry recorded is narration; the node reads `39.800`.)
15. **Render settings — EEVEE, not Cycles.** The render panel shown is unambiguously EEVEE: `Sampling Render 64 / Viewport 16` with `Viewport Denoising` on, **`Bloom`** ticked (`Threshold 0.800`, `Knee 0.500`, `Radius 6.500`, white `Color`, `Intensity 0.100`, `Clamp 0.000`) and **`Screen Space Reflections`** ticked (`Half Res Trace`, `Trace Precision 0.250`, `Max Roughness 0.500`, `Thickness 0.2 m`, `Edge Fading 0.075`, `Clamp 10.000`) — both panels exist only in EEVEE [frame_014]. The "Cycles, Filter Size ~1.8, Samples 256" figures this entry previously recorded are not supported by any frame. Add a dark background plane behind the logo [transcript 13:10].

### Nodes / Settings
- Curve data: **Geometry** → `Offset`, `Extrude`, `Taper Object` (Bezier curve), `Taper Radius` = **Override**, `Map Taper`; **Bevel** → `Round`/`Object`/`Profile`, `Depth` (this is the thickness control), `Resolution` 4, `Fill Caps`; **Curve Deform** → `Radius` ✓, `Stretch` ☐, `Bounds Clamp` ☐ [frame_002]
- **Start & End Mapping** panel: `Factor Start` 0.000 / `Factor End` 1.000 (Factor End is the animated one); `Mapping Start` / `Mapping End` dropdowns default to `Resolution` — set **Mapping End = Spline** for constant speed [frame_005, frame_006]
- Mean Radius — reads `284.094` after scaling up and must be set to **1** in the Edit-mode N panel, since it multiplies the bevel depth [frame_001]
- Taper curve Shape Keys — `Basis` (tapered) and `Key 1` (flat), `Relative` on, `Relative To: Basis`, `Range Min 0.000 / Max 1.000`; keyframed 0 at frame 150 and 1 at frame 200 [frame_008]
- Material `SVGMat.022` — Principled BSDF (`GGX`, `Random Walk`, `Metallic 1.000`, `Roughness 0.100`, `Specular 0.500`, `IOR 1.450`) [frame_009] mixed with an `Emission` (white, **`Strength 39.800`** — not the ~50 of the narration) through a `Mix Shader` at `Fac 0.500` [frame_013]
- Noise Texture — `3D`, tuned to **`Scale 15.000`, `Detail 0.000`, `Roughness 0.200`, `Distortion 0.000`** [frame_011]; an earlier moment catches it still at the `5.000 / 2.000 / 0.500` defaults [frame_010], which is why those figures were once recorded as unconfirmed
- Texture Coordinate `UV` → `Mapping` (`Type: Point`) — `Location X` is the animated channel, caught at `1.07 m` [frame_010] and `0.768 m` [frame_011], driven by `#frame/250` [transcript 11:20]
- `Fresnel` → `ColorRamp` — masks the emission to the curve edges. The frame catches the Fresnel at its default `IOR 1.450` [frame_012]; the narration lowers it to about `0.9` [transcript 12:26]. The two ColorRamps sit at positions `0.136` and `0.459` [frame_013]
- Math Multiply — Fresnel mask x Noise mask → `Mix Shader` `Fac` [frame_013]
- Render engine — **EEVEE**: `Sampling Render 64 / Viewport 16`, `Bloom` on (`Threshold 0.800`, `Knee 0.500`, `Radius 6.500`, `Intensity 0.100`) and `Screen Space Reflections` on (`Half Res Trace`, `Trace Precision 0.250`, `Max Roughness 0.500`, `Thickness 0.2 m`) — both panels are EEVEE-only [frame_014]. The "Cycles, Filter Size ~1.8, Samples 256" figures previously recorded here are unsupported by any frame

### Difficulty
Intermediate — requires curve editing knowledge, shape keys, material node setup, and basic drivers.

### Blender Version
**Blender 3.0.0 Beta** — read from the status bar in two independent frames [frame_002, frame_004]. This entry previously said *"Blender 4.x (… no version-specific features)"*, which was an inference and is wrong by two major versions.

### Tags
#animation #curves #shaders #materials #motion-graphics #vfx #wireframe #intermediate

---

## Frame verification (2026-09-01)

| | |
|---|---|
| **Corrected — version** | `Blender 4.x` was an inference. The status bar reads **3.0.0 Beta** in two independent frames [frame_002, frame_004]. Wrong by two major versions. |
| **Corrected — panel names** | Thickness (`Depth`) lives under **Bevel**, not Geometry [frame_002]. The build animation is driven from the **`Start & End Mapping`** panel, where `Factor End` is the animated value and `Mapping End` is the dropdown that must be set to *Spline* — two different controls this entry had merged into one [frame_002]. |
| **Scoped down** | The Noise Texture values (Scale 15 / Detail 0 / Roughness 0.2) are transcript-only. The frame covering that chapter shows the node still at defaults [frame_004], so those numbers are now labelled as narration rather than presented as observed. |
| **Added** | `Taper Radius: Override`; Bevel `Resolution` 4 and `Fill Caps`; Curve Deform `Radius`/`Stretch`/`Bounds Clamp`; Mapping node `Type: Point`; Noise Texture in **3D** mode [frame_002, frame_004]. |

**Subject:** the SVG being animated is `blender_community_badge_white.svg`
(spline `path1313`, material `SVGMat.022`) — the Blender community badge, not an
Eternals asset [frame_002, frame_004]. The entry described the technique but never
said what was on screen.

---

## Related Tutorials
- `powerful-logo-particle-flow-effect-in-blender.md` — another logo-driven animation effect
- `sci-fi-grid-pattern-animation-loop---blender-motion-graphics-tutorial.md` — motion graphics animation companion
- `photorealistic-renders-in-blender.md` — materials context for metallic/gold Cycles renders
- `my-new-favorite-lighting-trick-in-blender.md` — Fresnel-based lighting effects
