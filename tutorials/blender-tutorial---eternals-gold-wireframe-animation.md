---
title: Blender Tutorial - Eternals Gold Wireframe Animation
source: YouTube
url: https://www.youtube.com/watch?v=WmldjCv9P84
author: Blender Made Easy
ingested: 2026-05-19
blender_version: "3.x-4.x"
tags: [animation, curves, materials, shaders, motion-design, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/blender-tutorial---eternals-gold-wireframe-animation/
frame_count: 0
---

# Blender Tutorial - Eternals Gold Wireframe Animation

**Source:** [YouTube](https://www.youtube.com/watch?v=WmldjCv9P84)
**Author:** Blender Made Easy
**Duration:** 14m24s | 8 section(s)

---

## Raw Data (for Claude Code extraction)


### <Untitled Chapter 1> [0:00]
**Transcript:** Hello everyone and welcome to another Blender Made Easy tutorial.  Today I'll be learning how to create this Gold Wireframe build animation in Blender.  I got this idea from the new Marvel film Eternals from this scene right here, where the weapon  creates itself.  I thought it looked pretty cool so I decided to recreate this effect in Blender.  Using any Curve object you are able to create this.  For this animation I used a single vertex and I basically traced out the sword and then  converted it to a curve.  To keep things simple I'm going to be using the Blender logo for this tutorial.  Fortunately for us the Blender logo actually has an option for us to download it as an SVG.  I will link this page in the description.  Once you have it you can jump over into Blender and then import it in by going over to file  down to import and then selecting the SVG.  Once you import it in it's very very small so make sure you select everything by box  selecting it and then scaling the entire thing up.  We're going to scale it up pretty big and then place it in the middle of our scene.  We don't really need the extra objects so select the extra parts of the logo and delete  them because you'r...


### Fixing the Curve [1:09]
**Transcript:** Now that we have the logo in our scene let's go over the Curve settings and I'm going  to talk about how to create this effect.  To make things simple let's select both of these and press Ctrl J to join them together  as one curve object.  Next over in the Fill mode we don't really need it, we don't need a face so switch it  over to none right there.  If we open up the geometry tab we can give it some thickness by changing the depth right  here.  You'll notice though if I drag it up just slightly it creates a huge amount of bevel  even though the value is so small.  Well the reason for that is because we scaled everything up really big so make sure you  press Ctrl A and apply the scale.  Next if we go into Edit mode and press A to select everything and open up the properties  tab by hitting N you're going to notice the mean radius is set to 284.  That means it's going to multiply the depth by that value.  That's not going to look very good and that's why it's scaling everything so big.  So make sure you set the mean radius down to a value of 1 and now the depth should actually  work correctly.  So if we drag this up you're going to see it's actually working properly.  The next step...


### Animating the Curve [4:12]
**Transcript:** To actually get the build effect we need to animate the end value if we drag this down  you're going to notice that it starts to create this effect but there are two problems.  One problem is I don't want it to go in this direction I want it to go in the opposite  direction and another problem is I don't want these to go in the same direction I want  one to go this way and the other one to go this way.  So to fix that you can go into edit mode we'll select the outer logo right here and then  we'll select the inner logo and press control L and then to switch the direction all you  have to do is right click and then click on switch direction.  So let's animate this value I'm going to bring the end frame all the way down to zero  and then add in a keyframe right on that side.  We're going to jump all the way to frame 200 and drag the end all the way up to a value  of 1 and then add in another keyframe.  Let's take a look at this by restarting our animation and playing it and this is the  effect that we're getting.  Now let's talk about the mapping start and end values.  These are how the mapping is going to affect the animation with it set to resolution what  it's going to do is it's ...


### Adding Taper [6:22]
**Transcript:** this side.  So now what we're going to do is we're going to create a taper effect using this taper  option over in the geometry panel.  How this works is we need to add in a new curve, suppress shift A, go over to curve  and then add in a busier curve.  Go into edit mode and then we're going to drag this down so it's completely flat.  From this point select your original logo and for the taper object select the new curve  that we just added.  You'll notice everything disappears but don't worry it's still there.  We need to go into edit mode on our new curve and then move the vertices around.  If we drag the right vertex up you're going to see this is the effect that we're getting.  Now we have that taper effect.  So now if we restart and play it this is the effect that we're getting.  But you can see it's actually inverted so what we need to do is select it and then click  on map taper and that will fix that issue.  If it's still thick on one side all you have to do is just invert it so we'll drag this  part down and then we'll drag this vertex up like that and that's going to give us the  effect that we need.  So now for your restart and play it here is the result that we're getti...


### Animating the Taper [8:20]
**Transcript:** Finally, the last thing that we'll do for this animation is we're going to delete that  taper effect at the end of the animation.  Our animation ends at frame 200 so let's get rid of the taper at 200.  To do that we need to animate this shape of this be easier curve.  You can do this by adding in some shape keys over in the curve properties.  We're going to add in a new basis curve shape and then we'll add in a keyframe right there.  With the value set at zero this is the shape that we're going to get.  We're going to drag this value all the way up and then go into edit mode.  To make the taper disappear we need to drag this up until the vertices are in line with  each other.  So right about there is perfect just like that so it's a completely straight line.  And as you can see the taper is now gone.  If we drag this value down to zero now you can see the curve goes back to its original  position and the taper reappears.  If we drag it all the way up to one the taper disappears and now this curve is very flat.  So all we have to do is animate this value on frame 150.  We're going to drag this all the way down to zero add in a keyframe then on frame 200  when the animation ends this...


### Gold Material [9:34]
**Transcript:** Now before this tutorial ends let's create that gold metallic material with that really  cool light going across it.  Over in the material tab we're going to click use notes to create a new material.  What we need to do first is create that gold look.  We're going to bring the metallic all the way up to one and the roughness all the way  down to point one and then for the base color we're going to select a nice gold color  somewhere around there.  Let's press Z and go into render view to see what we're doing.  Next we're going to add in any mission so we'll press shift A add in a shader and  emission then we'll add in a mix shader and mix these two together.  We'll deal with the color and the strength of this later but for now we need to add in  where we want the emission to be on our curve.  What we're going to do is add in a texture and a noise texture.  Then with the node wrangler add on enabled you can press control T to add in a mapping  and a texture coordinate node.  Instead of using the generated we're going to use the UV and plug it into the vector.  Let's take a look at this by control shift left clicking on the noise texture.  To see this a bit better we're going to add ...


### Render Settings [13:06]
**Transcript:** And that is basically it for the material.  After this you can experiment with the strength of the emission.  You can also enable bloom in the render settings, add in a plane and a dark background and  you can create some really cool results.  Another thing I wanted to mention in this tutorial is this effect right here where we have  some weird glowing issues along the curve.  That is due to the filter size and the sample count.  The filter size basically helps the render look a bit better.  If you bring this a lot lower it's going to make that effect even worse and the splatging  is going to appear more visible.  But if you go too high it becomes way more grainy.  So I found a value of about 1.8 works for this scene.  You also want to bring up the sample count.  You can see my viewport is at 16 but if I drag this up to 256 that's going to help smooth  out that line as you can see there.  So for the render amount I'm going to bring it up to 256.


### Outro [14:00]
**Transcript:** And there you go that is the end of this tutorial.  Thank you very much for watching.  If you learned something new or created your own cool wireframe build animation I would  love to see it so make sure to send it to me on Instagram at BlenderMadeEasy.  If you have other suggestions for tutorials in the future leave a comment down below and  I'll be sure to check it out.  Thanks again for watching and I will see you in the next one.



---

## Structured Notes

### Core Technique
Curve-based wireframe build animation: import SVG logo as curve, set bevel depth for wire thickness, animate the Curve End value from 0→1 for the draw-on effect, use a Taper Object (Bezier curve with shape keys) for the leading taper, and a gold metallic + noise-based emission material for the glowing energy trail.

### Summary
14-minute tutorial recreating the Eternals weapon materialization effect using Blender's curve system. Imports the Blender SVG logo, converts it to a single curve with bevel depth, animates the End mapping value for the draw-on effect, adds a custom Bezier taper curve that disappears at the end using shape keys, and finishes with a gold PBR material blended with a noise-driven emission shader for the glowing energy trail. Works with any curve/SVG.

### Key Steps
1. **Import SVG** — File → Import → SVG; box select all and scale up; delete unwanted parts; select both curve objects → Ctrl+J (join)
2. **Fix scale** — Curve Properties → Geometry → Depth to add thickness; Apply Scale (Ctrl+A) first or Mean Radius will multiply incorrectly; in Edit Mode select all, N-panel → set Mean Radius = 1
3. **Curve bevel depth** — Geometry tab → Bevel → Depth ~0.01 (after scale fix)
4. **Animate End value** — Curve Properties → Shape → End: keyframe at 0 on frame 1, keyframe at 1 on frame 200; this reveals the curve progressively
5. **Fix direction** — Edit Mode, select inner/outer loops → right-click → Switch Direction; so both animate inward/outward correctly
6. **Taper object** — Shift+A → Curve → Bezier; go into Edit Mode, flatten all vertices to the baseline; assign as Taper Object in original curve's Geometry settings; adjust taper vertex height for desired shape; enable Map Taper
7. **Animate taper removal** — on taper curve: Object Data → Shape Keys → Add Basis, Add Key; at frame 150: Shape Key Value=0 (taper visible); at frame 200: Shape Key Value=1 and all vertices straightened (taper disappears)
8. **Gold material** — Principled BSDF: Metallic=1, Roughness=0.1, gold Base Color; Mix Shader with Emission; Noise Texture (Node Wrangler Ctrl+T) mapped to UV; use noise to reveal where emission appears (the "energy point")
9. **Animate emission** — animate the Noise Texture Location to slide the bright spot along the curve as it animates
10. **Render** — Cycles; enable Bloom (Render Properties); dark plane background; sample count 256+; Filter Size ~1.8

### Nodes / Settings
- Curve → Shape → Start/End: animation from 0 to 1
- Curve → Geometry → Bevel Depth; Taper Object field
- Curve → Shape Keys: Basis + Key 1 (straightened)
- Principled BSDF: Metallic=1.0, Roughness=0.1, Base Color gold (~H30°, S80%, V90%)
- Mix Shader: BSDF + Emission; Emission Color = bright gold/white; Emission Strength animated
- Noise Texture → UV mapping; Color Ramp for sharp emission spot
- Render Properties → Bloom ON; Filter Size 1.8; Samples 256

### Difficulty
Intermediate

### Blender Version
3.x–4.x (SVG import and curve features consistent across these versions)

### Tags
animation, curves, materials, shaders, motion-design, intermediate

---

## Related Tutorials
- [[powerful-logo-particle-flow-effect-in-blender]] — another logo/text effect in Blender
- [[a-new-way-to-loop-animations-in-blender]] — curve animation looping technique
- [[powerful-light-trails-in-blender-45-tutorial]] — curve-based light trail animation
