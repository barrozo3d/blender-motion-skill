---
title: INFINITE WOOD! Don't Fear the Shader: EP01
source: YouTube
url: https://www.youtube.com/watch?v=gpC7s-tGpc4
author: Clipping Issues
ingested: 2026-07-08
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/infinite-wood-dont-fear-the-shader-ep01/
frame_count: 12
---

# INFINITE WOOD! Don't Fear the Shader: EP01

**Source:** [YouTube](https://www.youtube.com/watch?v=gpC7s-tGpc4)
**Author:** Clipping Issues
**Duration:** 10m27s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** We're building procedural wooden floorboards.  First go to viewport shading, uncheck scene world and choose a nice HDRI.  If you try to build the material using Blender's default gray void in a single point light,  you're just lying yourself about what the texture actually looks like.  Much like ogres, materials also have layers.  Somewhere out there someone taught me that every single material on earth can be broken down into  three layers. Micro details, medium details, and macro details.  For if you can't branch. Once you figure out how to break them down and recombine them digitally,  you'll be able to create any material in the world.  So let's break it down. We start small. Add a noise texture in a mapping node set the object.

**Frame:** tutorials\frames\infinite-wood-dont-fear-the-shader-ep01\frame_000.jpg

### Small details [0:35]
**Transcript:** What grain is literally just noise that got squashed on one axis. Drop the X scale down.  Now we're gonna build a custom controller using Combine XYZ and some value nodes. Why?  Because two months from now when you need to make the grain 10% smaller,  you shouldn't have to dig through the 50 nodes spaghetti monster.  Why XYZ into one value node? But run the X through a standard math node set to multiply and  multiply it by a really small number. This gives you a master switch for the stretch and a master  switch for the scale. Frame the important values with F so that we can remember them forever.  Slide them around until it actually looks like wood grain to you.  Trust your judgment. Don't just blindly copy my numbers. I believe in you.  Now select all of it and press F to frame it all nice and pretty.

**Frame:** tutorials\frames\infinite-wood-dont-fear-the-shader-ep01\frame_001.jpg

### Medium details [1:17]
**Transcript:** Add a wave texture. Set it to rings. Set it to saw.  Don't forget to plug it into the object coordinates.  Boom, we already have some wood. Very nice.  But perfect rings don't exist in nature. We need to distort them using our noise.

**Frame:** tutorials\frames\infinite-wood-dont-fear-the-shader-ep01\frame_002.jpg

### Distorting the wood [1:29]
**Transcript:** We're not gonna use a regular math node for this. Use a vector math node set to add.  A regular math node only calculates one single grain number at a time.  Vector math does the exact same calculation but it processes XY and Z all at the same time  so you aren't doing math like a caveman. That's because we're gonna take advantage of the  fact that the noise generates three different values in its color socket. Plug your noises  color into the vector. Whoa, trippy. That's a bit too much so let's add a mixed vector node and  plug the noise into the second socket and the object in the first socket.  A mixed node does exactly what you think it does. It makes us stuff.  The factor value controls how much of one thing is mixed.  Now we have a way to control the drugs to wave texture's taking.  But look what happens. As we add the noise, the entire texture shifts off center.  Why? Because the noise texture outputs a value from 0 to 1.  If you add that to your coordinates, your 0 point literally walks away.  To fix this, we use a map range node.  This is one of the most important tools in the editor.  It takes any set of numbers and forces them into a new box. Drop it in the noise and add node.  Switch it to vector because we're dealing with 3D. That's 3 digits.  Tell us to take that 0 to 1 noise and force it to be negative 1 to 1.  The math is now balanced perfectly around 0.  Your center stays locked and the rings are beautifully distorted.  Copy our stretching setup to this noise.  To make the noise scale in detail until it looks right for you.  Once again, let's frame the important values so that we know where they are.  It's a surprise to little help us later.  Look at the side of the cube.  The rings are bunching up and glitching.  Unless this is a terribly made wood veneer,  or some tree infected with an outerge sickness,  wood grain doesn't warp across the rings.  We need to tell the distortion to leave the side face alone.

**Frame:** tutorials\frames\infinite-wood-dont-fear-the-shader-ep01\frame_003.jpg

### Masking ends [2:57]
**Transcript:** We do this using normals.  A normal just tells blender which way of face is pointing.  It gives a value of 1 if it's facing completely in a set direction,  and a value of negative 1 if it's completely backwards.  Add a separate xyz node connected to your normal coordinates.  Run the x-axis to an absolute math node,  which, if you remember math from your school,  just turns negative numbers into positive numbers.  This generates a black and white mask that isolates faces facing the x-axis.  Use a color ramp to crush the contrast so you dictate where exactly the mask ends.  A color ramp is another one of the most useful tool in your noding arsenal.  Plug it into the factor of another mixed node set to vector.  We aren't mixing colors.  We're mixing 3D coordinates.  We're essentially telling blender.  If it faces this way, use the clean coordinates.  If it points sideways, warp it to oblivion.  But we don't want exactly zero distortion.  So let's lower the white value of the color ramp.  Alternatively, you can use a map range node after the ramp and tweak the two max value.  Now we have a solid block of hyper realistic wood.  Now we chop it up.

**Frame:** tutorials\frames\infinite-wood-dont-fear-the-shader-ep01\frame_004.jpg

### Large details [3:53]
**Transcript:** Add a brick texture.  Turn the mortar size to zero.  We don't want the visual lines yet.  We want the random grayscale data it assigns to each brick.  Set color 1 to pure white and color 2 to pure black.  We're going to use these random colors as a mathematical crowbar to prior wood apart.  Tweak the setting so it looks like hardwood flooring.  Don't forget that, the texture coordinate nodes.  And run the brick color into a map range with the two values set to something absurdly large.  We really want those coordinates to run away from each other.  Now violently add this offset into every single object coordinate at the start of your tree.  Instantly the infinite wood fractures into unique floorboards.  Tweak the scales so you can see them better.  Don't mind these front faces.  We'll pretend they don't exist for now.  Change these minimum and maximum values from our brick texture until you like the spread.  The main mass is done, but don't think you're safe.  You aren't out of the woods just yet.  We now have our micro, medium and macro details.  Now we combine and route the data into the principal BSDF to light to the light engine.

**Frame:** tutorials\frames\infinite-wood-dont-fear-the-shader-ep01\frame_005.jpg

### Putting it together: color [4:46]
**Transcript:** Add a mixed color node and plug your grain into the factor.  Set your colors to some light and dark brown.  Use another mixed color node to combine your grain and your bands.  Using the bands as the mask,  tweak the colors until it looks like whatever species of wood you're trying to fake.  And that's basic color.

**Frame:** tutorials\frames\infinite-wood-dont-fear-the-shader-ep01\frame_006.jpg

### Putting it together: roughness [5:00]
**Transcript:** For the micro roughness, we go back to standard math nodes.  By the way, I just turned the cube into shiny metal to better see what we're doing for this part.  Run your grain to an add and multiply node.  The add node controls the general overall roughness,  and the multiply node controls exactly which parts are rough.  Slide the values until the reflection looks right.  Do the same for the bands and mix them together.  Finally, the physical bump.  Run your fine grain into a bump node.

**Frame:** tutorials\frames\infinite-wood-dont-fear-the-shader-ep01\frame_007.jpg

### Putting it together: bump [5:22]
**Transcript:** Now you need to add the bands.  You can add the height data together or you can daisy chain them.  Plug the normal output of the first bump node into the normal input of the second bump node.  They stack perfectly.  Remember the brick texture?  Duplicate it and give it a small mortar size and max smoothness.  Then daisy chain the factor into a third bump node.  Now just tweak the bump settings more until the seams are visible.  Then set the bump to invert.  This... well,  inverts the bump direction.  Turning that frown upside down.  Or in this case, a smile into a frown.  Perfectly recessing the gaps between your floorboards without adding a single piece of geometry.  Now we have infinite floorboards.  As far as 3 I can see.  But what if you don't want floorboards?  What if you just want a solid sheet of wood for a table?  What we need is a bypass switch.

**Frame:** tutorials\frames\infinite-wood-dont-fear-the-shader-ep01\frame_008.jpg

### The bypass [6:08]
**Transcript:** Go to where your brick texture is violently offsetting your coordinates.  Add a mixed node and set 8 to 0 and plug your brick into B.  Do the exact same thing for your mortar.  Now as we slide this factor,  you can see the wood coalesced into a single block like a locker robo.  Trull both of these at the same time.  Add a menu switch node set to Boolean and plug it into both factors.  Now you might be familiar with Booleans in modeling.  Technically speaking, a Boolean is a strict mathematical toggle.  It is only ever a 1 or a 0.  True or false?  Check or uncheck?  Leave A unchecked and B check.  You just built a master switch that toggles the floorboards on and off without destroying the underlying wood grain.  Open the side panel with N and let's give it proper names so that we look professional.  Infinite floorboards look fake if every single plank is that same shade of brown.  We need variation.

**Frame:** tutorials\frames\infinite-wood-dont-fear-the-shader-ep01\frame_009.jpg

### Color Variation [6:51]
**Transcript:** Add a hue saturation value node before your principal BSDF.  We're going to use a random grayscale data from our brick texture to drive the colors.  Plug the brick color directly into the hue saturation and value socket.  Congratulations, you made a disco floor.  This happens because the brick texture outputs values from 0 to 1,  which aggressively swings the color wheel.  We need to clamp it.  Add a map range node for each input.  God I love the map range so much.  Few defaults exactly 0.5.  We only wanted to deviate a tiny fraction from 0.5.  Use the map range to crush the brick texture random data so it only shifts the hue by a teeny tiny amount.  Do the exact same thing for a saturation and value.  But these have a default of 1 instead so adjust your values accordingly.  Now every single plank has a mathematically generated highly controlled solo color variation.  For even more randomness you can add another map range node before the map range  and tweak the two values so that they're slightly offset from each other.  Tweak the values until they look perfect to you.  No need to copy my values, just eyeball it.  I still believe in you.  Now plug the factor of the HSV node into our toggle.  The math is complete.  Look at our wood.  But look at your shader editor.  It's a cluster of spaghetti that will give you a panic attack if you look at it two months from now.  We're gonna hide the evidence so like absolutely everything except the material output

**Frame:** tutorials\frames\infinite-wood-dont-fear-the-shader-ep01\frame_010.jpg

### Cleaning it up and packaging it [7:59]
**Transcript:** and press Ctrl G.  You just collapse your entire psychopath wiring diagram into one single clean node.  Press tap to go inside and out.  Use the node triangular add on to drop rear out points and organize your noodles.  Make it look like a professional built this not a lunatic.  Don't forget to name it something nice.  Right now you still have to go inside the node group to change anything.  We fix this by dragging our master values into the group input node.  Whatever you plug into this node becomes a slider on the outside of your group.  Plug in your colors.  Plug in your grain scale.  Plug in your band distortion.  Plug in your floorboard toggle.  See if this is why we labeled them earlier.  Make sure to plug the brick texture values into the same socket so that they don't deviate from each other.  But only plug in the mortar values for the second one.  If your group input nodes get too long,  you can press Ctrl H to only show sockets that are being used.  You can do this for any node by the way.  Open the side panel with N again.  Rename your input so they actually make sense.  Group them into panels.  Wood grain, bands, wallboards,  and most importantly set minimum and maximum limits on your slider so you don't accidentally drag a value into the negatives and break the universe.  Press tap to exit the group and admire your creation.  Wow!  It's something looks wrong.  You might have forgotten to set a value somewhere.  You now have a single clean node.  A custom UI with sliders for grain scale, band distortion and flank count.  We have depth, reflections, and zero resolution limits.  You can scale it across an entire warehouse floor and will never pixelate.  And you didn't even have to download a single texture map.  You built this by staring at the microsurface,  warping the structure, and slicing the macro shape.  Like I said, it's just a calculator.  Now if you were too lazy to follow along,  you can get the project file on my gumroad.  Leave a tip if you're nice.  Or if you're a paid-of-wind player,  I took this wood, added a bunch more settings,  some fun stuff you can tweak,  and some preset materials.  And put it on my gumroad for a few bucks so you can support the channel.  Buy it or don't.  I don't care.  I thought you the process.  It's your turn to apply it.  Now go forth my children and spread your newtly wings,  and I'll see you in the next episode.  If you made it this far,  comment something random about this image  to confuse everybody in the comment section.  You are the 1% and you deserve an inside joke.  Like, subscribe, support, coffee, gumroad, blah blah blah.  Okay, bye.  Okay.

**Frame:** tutorials\frames\infinite-wood-dont-fear-the-shader-ep01\frame_011.jpg


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
