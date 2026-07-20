---
title: Master Blender Sculpting: Every Brush Explained
source: YouTube
url: https://www.youtube.com/watch?v=5-mNgCpEkCI
author: Grant Abbitt (Gabbitt)
ingested: 2026-07-20
blender_version: "4.3.1"
tags: [organic, displacement, cloth, intermediate, blender-4x]
extraction_status: complete
frames_dir: tutorials/frames/master-blender-sculpting-every-brush-explained/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Master Blender Sculpting: Every Brush Explained

**Source:** [YouTube](https://www.youtube.com/watch?v=5-mNgCpEkCI)
**Author:** Grant Abbitt (Gabbitt)
**Duration:** 43m40s | 51 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Start [0:00]
**Transcript (timestamped):**
[0:00] We'll be taking a look at all the sculpting brushes in Blender to give you an insight into how they work and what they might be used for.
[0:06] This includes all the new brushes in Blender 4.3.
[0:09] I'll also be looking at some of the difficulties you might come across when using things like the cloth brushes.
[0:14] If you like my approach, then check out the links in the description for other useful sculpting videos.


### Starting of in sculpting [0:18]
**Transcript (timestamped):**
[0:18] So I'm in Blender 4.3.1.
[0:20] I've got my default scene loaded up here with my default cube selected,
[0:24] but I can't really sculpt on the default cube because sculpting deforms the vertices and the default cube only has eight.
[0:30] So we won't see much effect with the sculpting.
[0:33] What we want to do is start with a shape that has more vertices.
[0:35] So I'll delete the default cube, Shift-A to add, or that's the add menu up here, Mesh, and the Icosphere is quite a nice one to start with.
[0:43] So I'll select that.
[0:44] I'll go to the dialog box down the bottom here and I can increase the subdivisions or the amount of faces on this object by changing this to something like six to start off with.
[0:52] So we've got a bit more detail in our sphere.
[0:55] Let's go across to the sculpting workspace now and the sculpting workspace will put whatever I had selected.
[1:00] So the sphere in this case and it puts it into sculpt mode.
[1:03] We've got our brushes down the bottom here.
[1:05] If I expand those out, you can see we've got four layers.
[1:08] I'll bring this down to two just there and I can use my wheel to scroll through them and I'll increase the icon size so it's nice and big and you can easily see what I'm doing.
[1:18] I'll also tick on the names so you can see what brush I'm choosing.
[1:21] So I've got my drawer brush selected here and the settings for that brush are up the top here and indeed down the side here as well under the tool settings.
[1:30] I can resize my brush with the F key.
[1:33] Incidentally, I've got my screencast keys just on the side here and shift F is to change the strength.
[1:39] You can also find those settings radius and strength just there.


### Draw Brush [1:42]
**Transcript (timestamped):**
[1:42] You've also got the plus and minus.
[1:44] So with the drawer brush selected, I'll just resize that so it's nice and small, draw across my shape.
[1:49] You can see that it's a positive.
[1:51] So it's kind of pulling outwards from the shape.
[1:53] If I change this to the negative, I can dig into the shape as you can see there.
[1:57] I'll undo those strokes and change that back to the positive.
[2:00] The shortcut key for that, if I zoom in a bit, there's the positive and the shortcut key for the reverse is holding down control and it will do the reverse.
[2:08] You can see my strokes are a little bit blocky so I haven't quite got enough faces on my shape.
[2:13] I'll undo those strokes.
[2:14] The way we add more detail to our shape is using the remesh option.


### Remesh - Adding detail to your mesh [2:15]
**Transcript (timestamped):**
[2:19] There is also the Dynetopo.
[2:20] It's a little bit more confusing and possibly a little bit less responsive and slightly less used these days.
[2:26] More commonly used is the remesh.
[2:28] Under the remesh, there's two important aspects, the voxel size and the remesh button itself.
[2:33] The voxel size is the size of the faces you're going to create and the remesh button will actually apply those to our mesh.
[2:40] And it remesh is our shape to keep it as close as possible to the shape it already is.
[2:45] So if I draw across here, for example, like so, and then use the remesh, you can see there, it tries to keep its shape.
[2:52] In this case, our remesh size is reducing the polygon count.
[2:56] Incidentally, you can go to the overlays here, turn on statistics to see your actual count.
[3:01] We've only got 2000 faces here at the moment.
[3:03] So I need to go to my remesh and change the voxel size.
[3:06] There's a quicker way to do this, though.
[3:08] If I press R, I can actually get a grid where I can see the size of the voxels or the faces that's going to create.
[3:15] So I can go down to something like 0.01 in this case, somewhere around there and control R to remesh.
[3:23] And you can see it kept the shape and it's added more resolution.
[3:25] If I draw on this, you can see how smooth that is now.
[3:28] We've got about half a million faces, still not particularly high for sculpting,
[3:32] but certainly enough to show off exactly what we're doing here.
[3:36] What I'm going to do is undo all these steps.
[3:38] So we go back to our original sphere, which was 20,000 faces.
[3:42] Again, press R for the voxel size, somewhere around 0.01, roughly around there, and control R to remesh.
[3:49] A little bit lower this time.
[3:51] We've got this nice smooth sphere to sculpt on.
[3:54] So that's the draw brush.


### Smooth Brush [3:55]
**Transcript (timestamped):**
[3:55] The other important shortcut to know about is jumping to the smooth brush.
[3:59] You can do that by holding down shift.
[4:01] So if I hold down shift and go over this, you can see it kind of smoothing it out.
[4:06] And that's done a reasonable job there.
[4:07] So holding down shift will take you to the smooth brush.
[4:09] And if you ever want to change the settings of the smooth brush,
[4:13] so let's say you wanted it to have more or less strength, which is also up here.
[4:17] You can change it in the brush.
[4:19] And then when we go back to using something like the draw brush,
[4:22] holding down shift will take you to the smooth brush with those new settings.
[4:27] So that's the draw brush and the smooth brush.
[4:29] The draw brush is obviously the default brush,
[4:31] and it's often the brush that you use to create new brushes.
[4:35] Let's say texture brushes where you've got a rock texture
[4:38] and you can sculpt some rocks and things.
[4:39] If you want to learn more about that, then do check out the link in the description.
[4:43] Quick intro to sculpting where I talk about creating new brushes.


### Blob Brush [4:45]
**Transcript (timestamped):**
[4:46] Let's now go to the blob brush.
[4:48] I'll change the size of my brush with F and I'll start drawing.
[4:51] And you can see it creates a sort of blob.
[4:54] I like the blob brush.
[4:55] It's good for kind of character spots and things.
[4:58] So you can resize and have a few spots there.
[5:01] Looks a bit like a smiley face at the moment now.
[5:03] And the reverse of the brush, you can hold down control
[5:06] and create these cool looking dents as well.
[5:09] You can even have dents on your blobs like so.
[5:14] Now it's worth pointing out at this point.
[5:15] Let's resize the brush, make a really big blob here.
[5:19] You can slowly start to see some stretching in our mesh,
[5:22] especially if I do a blob on a blob like this
[5:25] and then a blob on a blob on a blob.
[5:26] You can really see the stretching happen.
[5:28] Let's do a blob on a blob on a blob.
[5:30] So it's becoming a bit distorted
[5:32] because I'm stretching out these vertices too much.
[5:34] And you'll see that even more when we use things
[5:35] like the snake hook brush to pull our mesh around.
[5:38] What we do in those scenarios is we do a remesh.
[5:40] So control R to use our remesh tool
[5:43] and I can smooth this out.
[5:44] And you can see the remesh keeps its shape
[5:47] but adds those new faces evenly across
[5:50] the mesh we've created.
[5:51] So I can keep blobbing out here, control R to remesh,
[5:56] blob out a bit more, control R to remesh.
[5:59] Let's blow out this way now.
[6:00] Control R to remesh.
[6:02] So you're constantly remeshing
[6:04] when you're expanding out your shape.
[6:06] And then you get some really cool looking things like this.


### Clay Brushes [6:09]
**Transcript (timestamped):**
[6:10] Okay, so let's go to the clay brush
[6:11] and the clay strips next.
[6:13] So let's click on the clay brush first,
[6:15] come down to a clean area and use it to draw.
[6:19] And you can kind of see what that does.
[6:21] Very similar to the draw brush,
[6:22] but it's just kind of wider.
[6:24] If I go to the clay strips, slightly different than that one,
[6:27] you can see that sort of creates strips like this.
[6:30] Lots of sculptors really quite like this brush
[6:32] because it adds a bit of texture to your sculpts.
[6:35] It's a tiny bit more difficult to control.
[6:37] So if you're a beginner, I'd stick with the draw brush.
[6:39] But if you want a bit of texture on your shape,
[6:41] then certainly go across to the clay strips tool
[6:45] is my favorite really, or the clay brush to add to your shape.
[6:49] As you can see there.
[6:50] And of course, remember you can hold down control
[6:53] for digging into your shape with either of these tools
[6:57] and hold down shift to smooth out.
[7:00] You can see it's kind of added some interesting texture there.


### Clay Thumb [7:02]
**Transcript (timestamped):**
[7:02] Okay, what about the clay thumb?
[7:04] Well, this is really interesting.
[7:06] Not to be confused with the nudge,
[7:07] which I'll talk about in a second,
[7:08] but it does a similar thing.
[7:10] If I draw here, I can kind of push the clay into itself.
[7:14] It's kind of a traditional sculpting tool
[7:16] where you can squish the clay together
[7:19] into an area like this.
[7:21] And again, if you like that traditional sculpting look,
[7:24] it adds a bit of texture and variation
[7:26] whilst you're doing it and pushing the mesh around.
[7:29] But do notice how it is pulling the mesh
[7:32] and kind of creating a protrusion if you like.
[7:35] That's the difference between the clay thumb brush and the nudge.
[7:37] If I click on the nudge and push this across,
[7:40] you can see I'm just pushing the mesh around.
[7:44] In fact, I want to turn the strength up a little bit there,
[7:47] give it a bit more power, squish it around the place,
[7:49] but I'm not creating any extra topology
[7:53] or protrusions or indents.
[7:55] I'm just literally pushing it around.
[7:57] And that incidentally is the difference
[7:59] between the color of the brushes.
[8:00] Notice how these are all gray,
[8:02] these have bits of red on them,
[8:04] and these ones have bits of yellow on them.
[8:06] The bits of the yellow are kind of push, pull,
[8:09] and don't add any topology.
[8:10] The gray and the red are both add and subtract elements.
[8:14] The red ones kind of cut off things,
[8:17] which we'll talk about in a moment.


### Crease Brushes [8:18]
**Transcript (timestamped):**
[8:18] So from the clay thumb,
[8:19] we can go to the crease polish just here.
[8:22] If I draw with this,
[8:23] you can see drawing over the same patch again and again.
[8:27] It will squeeze the topology together.
[8:29] So you can see a little bit of stretching
[8:31] down the two sides here,
[8:33] and crease it into an area like so.
[8:35] So it creates a line.
[8:37] The crease polish and the crease sharp are very similar.
[8:40] Let's jump to the crease sharp just quickly
[8:42] and come down here.
[8:43] And you can see the difference there.
[8:45] If I go over again, this is just a much sharper line.
[8:48] And you can see the indent that's made there
[8:51] compared to the crease polish.
[8:52] So again, for beginners,
[8:54] I'd use the crease polish a little bit more
[8:56] than I would the crease sharp,
[8:57] because it's a little bit slower to build up.
[8:59] Crease sharp, you have to be a bit more careful
[9:02] with the lines you're creating.
[9:04] But this is a really useful brush.
[9:05] Let's go back to the blob over here,
[9:07] and let's go to the crease polish.
[9:09] If I want to kind of sharpen up areas around protrusions
[9:13] like so, the crease polish would be my brush of choice there.
[9:17] And you can see that sharpening up that area quite nicely,
[9:20] or maybe in here, for example.
[9:22] The crease sharp will do the same thing,
[9:24] but I have to be a lot more careful,
[9:25] and you can see it kind of denting into the shape.
[9:28] That can work too, but it's kind of a different style,
[9:31] and it's pushing into the shape more.
[9:33] I'll have to use the smooth brush there,
[9:35] because I messed that bit up, but you get the idea.
[9:38] So there's the crease polish and the crease sharp.
[9:40] We've talked about the draw brush,
[9:42] but we've also got next to that the draw sharp,
[9:44] kind of similar to the crease sharp,
[9:46] but it doesn't bring the mesh together.


### Draw Sharp [9:48]
**Transcript (timestamped):**
[9:48] So let's select that and zoom in on an area,
[9:51] make my brush a bit smaller, and let's draw a line.
[9:54] It's not got a lot of topology there,
[9:56] so let's zoom out a little bit more,
[9:57] and you can see that line there.
[9:59] So it creates this crease, much like the draw brush,
[10:02] except digging in, so its default is the negative,
[10:06] but it's a lot sharper and kind of stronger in the middle.
[10:09] So if we look at the draw brush and hold down control,
[10:12] you can see that's nice and smooth.
[10:13] The draw sharp is sharp.
[10:16] So the thing that makes the crease polish,
[10:17] the crease sharp and the draw sharp
[10:19] a little bit different from the other Adam Subtract brushes,
[10:23] is that they dig in rather than pull out.
[10:26] You can reverse that in fact.
[10:27] So let's use the draw sharp, hold down control,
[10:31] and then reverse, and you can see it creates this protrusion,
[10:35] a sharp protrusion in fact,
[10:37] and it could be something like gills,
[10:39] and I could come underneath the gills
[10:41] and create indents like so,
[10:44] and we've definitely got some really cool gills there.
[10:46] So use the smooth brush and smooth that out a bit.
[10:48] It's actually creating a bit of a bubbly effect there,
[10:50] and that's kind of down to the way the draw sharp
[10:52] pushes the topology in.
[10:54] Let's go back to the crease polish and hold down control,
[10:57] and you can see that's creating this very nice,
[11:00] sharp edge that's sticking out from our mesh here
[11:04] over these gills that I'm creating,
[11:06] and then let's dent them in here
[11:08] by using the brush normally without control,
[11:10] and you can see we created these nice sort of
[11:13] gill type things, and I could smooth over them a little bit
[11:16] to smooth them out just a touch by holding down shift.


### Inflate/deflate [11:19]
**Transcript (timestamped):**
[11:19] Okay, so let's move on to the inflate brush just here.
[11:22] Now this is slightly similar to the blob brush in some ways.
[11:25] Let's go to a clean area and start drawing,
[11:29] and it looks very, very similar to the blob brush,
[11:31] a little bit softer in a sense.
[11:33] However, if I go to an area such as this here,
[11:38] I'll make my brush nice and big and inflate it out.
[11:42] You can see it's kind of building that area up
[11:45] and literally inflating it,
[11:47] and you can see it's gone over itself here,
[11:49] creating quite a crease in the middle there.
[11:51] If I smooth that out, you can see even more of that crease
[11:54] and in here as well, and how it's inflated over itself.
[11:58] The inflate brush is really useful
[11:59] if you've got a very thin, long line.
[12:02] So I'll quickly show you a new brush,
[12:05] which is the grab brush just here,
[12:07] and let's bring this out quite far like so,
[12:12] and it's quite thin.
[12:13] Let's bring it down, bring it out even more like so.
[12:16] Now we're getting a lot of stretch in here,
[12:18] so obviously we need to control R for a remesh,
[12:21] and let's smooth it out a bit,
[12:22] but often smoothing it out makes it even thinner,
[12:25] and you can see this long line here,
[12:27] and each time I smooth out, it creates an even thinner line,
[12:31] and it becomes quite difficult to sculpt on.
[12:33] Well, the inflate tool is really useful for this.
[12:35] If I click on the inflate tool, go over this,
[12:38] I can expand it out again like so,
[12:40] and you can create some sort of blobby bits if you need to,
[12:44] or smooth out and create nice thin bits.
[12:46] Looks like a bird's head just there, doesn't it?
[12:48] So that's the inflate brush,
[12:49] and obviously deflate is the reverse,
[12:51] so if I hold down control,
[12:52] I can kind of deflate this for my bird's nick.


### Layer Brush [12:55]
**Transcript (timestamped):**
[12:56] The next brush is the layer brush.
[12:58] Click on that, come around to an area I've drawn on,
[13:01] and you can see it kind of creating a new layer on the icon.
[13:05] Well, the cool thing about this is,
[13:06] I can lift this layer up, but keep some of the details,
[13:09] so let's create a small brush here, draw across here,
[13:12] and interestingly, it's not worked particularly well
[13:14] over that point, but you can see the idea
[13:16] is trying to push this area out,
[13:18] and push those kind of gill bits out as well,
[13:20] but really hasn't worked there.
[13:21] Let's try it over this bit instead.
[13:23] You can sort of see it working,
[13:25] and it's creating this layer outwards,
[13:27] but trying to keep some of that detail.
[13:29] It's struggling a little bit because it's inflating it,
[13:31] can you see it sort of inflates it slightly?
[13:34] If I smooth out, you can see some of that inflation there.
[13:37] So it can be useful in some places,
[13:38] but you have to be aware of these kind of glitches
[13:41] in a way that are limitations.
[13:45] So if I draw over here, you can see it's a nice even height,
[13:48] and there it's not struggling to try and keep any detail.
[13:51] I can change that height with the height setting just here,
[13:53] so I can make it nice and big like so, draw over this bit.
[13:57] It struggled a little bit there
[13:58] because it was at a slight angle.
[14:00] Let's try and be a bit more flat on,
[14:03] and you can see it having a better effect there.
[14:06] Now it's trying to lift this area up,
[14:08] and it's struggling a bit,
[14:10] but you hopefully get the idea of this layer brush.
[14:14] Then I can change the size,
[14:15] have it increase the height slightly less,
[14:19] and it's possibly a little bit more effective in those terms.
[14:22] So that's the layer brush.
[14:25] If you like my approach and want to learn
[14:26] how to use the sculpting tools effectively
[14:29] to create characters and beasts,
[14:31] then check out the links with the discount codes
[14:33] to my courses in the description.


### Fill/Deepen [14:35]
**Transcript (timestamped):**
[14:35] Okay, so I've cleared my icosphere
[14:37] for the next group of brushes,
[14:39] and let's look at the fill deepen.
[14:40] I'll start off by using the draw brush
[14:42] to indent an area here and pull out an area here.
[14:47] Let's go across to the fill deepen.
[14:48] Now it's default is to fill.
[14:50] So if I go over this object,
[14:52] you can see that it fills in that gap.
[14:54] It can leave a little bit of distortion around the edges.
[14:57] You can smooth that out,
[14:58] and it's not done too bad a job at filling that area in.
[15:02] And then of course there's the deepen,
[15:04] which is holding down control.
[15:05] So I make my brush a little bit bigger
[15:07] so I can get the whole of the stroke that I've made in,
[15:09] hold down control,
[15:11] and then I've managed to deepen that,
[15:13] and I can smooth out the edges,
[15:15] and we've generally managed to fill
[15:16] and deepen those extrusions.
[15:18] So that's the fill and deepen brush.


### Flatten Contour [15:20]
**Transcript (timestamped):**
[15:20] Then we've got the flatten contrast.
[15:22] So on this sphere, if I make my brush a bit big,
[15:25] you can kind of see that it flattens out an area like so.
[15:30] So it's bringing some of this area up
[15:31] on the edge of the brush
[15:33] to flatten it out with the area here,
[15:35] and you can see it's brought some of that back as well.
[15:37] If I put some detail in with the draw brush
[15:40] and just squiggle across here,
[15:42] and then use the flatten brush,
[15:43] it will just scrub over that and flatten it out,
[15:46] bringing some areas of the mesh upwards
[15:49] and flattening and pushing other areas down.


### Plateau [15:51]
**Transcript (timestamped):**
[15:51] What about the plateau brush?
[15:53] So if I paint here,
[15:55] it's sort of like the flatten brush,
[15:57] just a little bit more pronounced.
[15:59] Let's say we're making a rocky plateau.
[16:02] Let's use the brush here on this area,
[16:04] and you can kind of see how it flattens it out,
[16:07] but it pushes this area out a bit as well.
[16:09] It's kind of an interesting one really,
[16:11] and you can see we've got two plateaus there.
[16:14] Just a quick remesh to smarten up,
[16:16] and you can see that working there.


### Scrape Multiplane [16:17]
**Transcript (timestamped):**
[16:18] Now the scrape multi-plane is a really interesting one.
[16:21] If I start using it on an area that has no indentation,
[16:25] like the brush shows here, it really does nothing.
[16:27] But if I use something like the crease polish, let's say,
[16:30] in fact, let's make my brush a bit smaller
[16:33] and make a line going around here like so.
[16:36] So I've drawn that in there.
[16:37] Now we know that the crease polish brush
[16:39] and the crease sharp pulls the topology in.
[16:42] So there's lots of topology in the middle here,
[16:44] lots of vertices basically, and less so on the edges.
[16:47] So if I do a quick remesh,
[16:48] you can see that tidies up a bit,
[16:50] but I lose some of my crease.
[16:51] Well, we've got the crease multi-plane here,
[16:53] and we can go along it,
[16:55] and you can see it smoothing out.
[16:57] The area's going down towards the crevice,
[17:00] and in some ways, the line in the middle.
[17:04] You might have to combine it
[17:05] if you want to keep the crease in there,
[17:08] and then back to my scraped multi-brush
[17:12] to kind of smooth out the areas going down towards that crease.
[17:17] A lot of the time with the crease brush,
[17:18] I find myself smoothing the areas
[17:21] with the actual smooth brush,
[17:22] but you can see that loses a lot of its definition.
[17:25] So this scraped multi-plane could be a really interesting one.
[17:28] Now for the scrape fill brush, let's zoom out a bit.
[17:32] I'll put some clay strips down around the place.
[17:36] We've got some variation over our shape.


### Scrape Fill [17:39]
**Transcript (timestamped):**
[17:39] The scrape fill is a really interesting brush.
[17:41] I like the icon shows,
[17:42] it kind of takes the tops off the detail.
[17:45] So if I select that, come into this area here,
[17:48] I'll do a quick remesh,
[17:49] and then go over this area here,
[17:50] you can see it's kind of scraped the top off,
[17:53] so hence scrape, and you can see it flattening out,
[17:56] but taking the edges off.
[17:58] This is really good for sort of bashed in metal.
[18:01] So if I smooth some of this out a bit,
[18:03] and then you've got these sort of bashed bits here
[18:05] where the metal, let's say, or whatever object it is,
[18:08] has bashed against something,
[18:10] and been dented and flattened out,
[18:13] and you can see kind of what that's producing just here.
[18:17] And that sort of flat area like that,
[18:20] you can imagine a piece of armor
[18:22] that's been bashed in loads of times,
[18:23] having that kind of look.
[18:25] If I come around to this area here,
[18:26] I'll make my brush a little bit smaller,
[18:28] hold down control,
[18:29] you can see it builds up the area
[18:30] a little bit like the fill brush in some ways,
[18:33] but with more of an edge to it.
[18:35] The next brush is the smooth brush,
[18:37] which of course we've talked about.


### Trim [18:38]
**Transcript (timestamped):**
[18:38] Then there's the trim brush.
[18:40] This is a really interesting one,
[18:42] and you can see it sort of cut into the shape like so.
[18:46] It's a little bit like the scrape brush,
[18:47] which used to be called the scrape peak brush,
[18:50] scraping the peaks,
[18:51] whereas the trim brush just indiscriminately
[18:54] digs into the mesh.
[18:55] It's a really good brush in combination
[18:58] with something like the scrape fill brush.
[19:01] If I go back to this now,
[19:02] I can scrape the edges of this,
[19:04] of these indentations,
[19:06] and it gives a nice sort of rocky look.
[19:08] And the trim brush is used
[19:09] to kind of dig into those areas.
[19:11] It is a tiny bit difficult to control.
[19:13] You have to really take care of the direction
[19:15] that the brush is facing,
[19:17] and it will scrape really flat,
[19:19] or trim really flat to that brush direction.
[19:22] If I hold down control,
[19:24] it comes out a little bit like the layer brush,
[19:26] but again, not quite as precise as the layer brush,
[19:29] but in combination with the scrape brush,
[19:30] this can be really nice
[19:31] when you bring it out like this,
[19:33] and then almost polish the edges and bash them in.
[19:36] And you can see there,
[19:37] we've got sort of a rocky surface,
[19:38] maybe some bashed metal,
[19:40] if we smoothed it up a bit more.
[19:41] So that's all the ones with red markings,
[19:43] and that's all the kind of add and subtract brushes.
[19:47] The next group we've got are the push and pull brushes.


### Grab Brush [19:50]
**Transcript (timestamped):**
[19:51] Now I'll start off with the grab brush in this case.
[19:54] Still a quick remesh with control R.
[19:56] I make my brush fairly big,
[19:57] and let's pull out an area like this.
[20:00] So what this is doing is moving the topology
[20:02] in the direction of my brush,
[20:03] and I can bring it in, bring it out.
[20:06] A lot of the time you need to do a remesh
[20:07] once you've used the grab brush.
[20:09] So you've got more topology to play with,
[20:11] and then you can pull it a bit further
[20:12] and do the remesh like we mentioned earlier.
[20:15] Often in combination with the smooth brush
[20:17] to smooth those areas out,
[20:18] and sometimes the inflate brush,
[20:20] if it needs some inflation.
[20:22] So that's the grab brush.
[20:24] Notice there's no plus or minus with the grab brushes.
[20:27] If I go along all of them,
[20:28] you can't see any of them.
[20:30] Apart from the pinch slash magnify,
[20:32] all the other ones won't have a negative.
[20:35] And again, that's because we are both pushing and pulling.
[20:37] If I go back to the grab brush,
[20:39] I can push inwards or outwards
[20:41] with the movement of my mouse or pen.


### Dyntopo [20:43]
**Transcript (timestamped):**
[20:43] What's also important to note is that many of these brushes,
[20:46] one distinct difference here is if we're using Dyntopo.
[20:49] I won't go into Dyntopo much, but I'll just turn it on.
[20:52] You get a warning message,
[20:52] but it's not important in this particular instance.
[20:55] I'll just put the detail size down,
[20:57] which is much like the voxel size,
[20:59] and I'll turn that down to something like three.
[21:00] Bring my brush a bit smaller.
[21:01] I'll start with the draw brush and start drawing.
[21:04] Now notice, instead of stretching the topology,
[21:06] it's creating new topology.
[21:08] And that's what's clever about the Dyntopo brush.
[21:11] And for many of these brushes,
[21:12] such as the clay strip as well,
[21:13] it will just create new topology as I draw,
[21:16] which can be really nice and a great way to build up shapes.
[21:19] However, with the grab brush,
[21:21] if I go to the grab brush and start pulling this out,
[21:23] you can see it's not using the Dyntopo.
[21:25] It's just stretching it out.
[21:27] So a lot of these movement brushes
[21:29] won't utilize the Dyntopo in the way the other ones do
[21:33] by creating new topology.


### snake Hook Brush [21:34]
**Transcript (timestamped):**
[21:34] The one difference is the snake hook tool.
[21:37] And you can use this with the Dyntopo
[21:39] and pull out topology like this.
[21:42] But you do often get this absolute mess at the end here
[21:46] if you go too thin.
[21:47] So if I undo that and make my brush a bit bigger,
[21:49] a little bit safer here, and it's coming out.
[21:52] And it's about here where I'm starting to worry
[21:54] that it's going to split.
[21:55] And you can use this in conjunction with the inflate brush
[21:58] to create extrusions like so.
[22:00] So that's using it with the Dyntopo.
[22:02] I go back to our remesh, so control R to do a remesh.
[22:06] I might just smooth this area out a bit
[22:08] and maybe inflate it so it doesn't cause us any problems.
[22:10] And let's go through the other brushes.
[22:12] I'll talk about the boundary brush in just a moment.


### Elastic Grab Brush [22:14]
**Transcript (timestamped):**
[22:14] Let's start with the elastic grab.
[22:16] Now I'll zoom out for this and let's grab this area here.
[22:19] Can you see how it's not moving as fast as the grab brush?
[22:22] Let's just go back to the grab brush
[22:23] and move that area out.
[22:25] And it's affecting a much bigger area.
[22:27] So the elastic grab is the same as the grab in some ways,
[22:30] but it's a really big area.
[22:31] So it's for big adjustments to your shape.


### Elastic Snake Hook Brush [22:35]
**Transcript (timestamped):**
[22:35] Then there's the elastic snake hook.
[22:37] So much like the snake hook,
[22:39] but this time it affects a really big area
[22:43] like the elastic grab.
[22:45] So if I go back to the snake hook quickly
[22:47] and let's talk through that,
[22:48] you can see that I can pull this out.
[22:50] I've not got Dyntopo turned on,
[22:51] so it's stretching the mesh
[22:53] and I'll have to keep remeshing like this,
[22:55] stretch it out a bit more,
[22:57] and then control R and remesh.
[22:59] If I want to keep going with this stretch like so,
[23:03] it's a really good fun brush the snake hook.
[23:06] And it kind of twists the mesh nicely as well.
[23:08] Just have to be a little bit careful
[23:09] not to affect other areas like so.
[23:12] So I'd have to bring my brush down on this case.
[23:15] And then again, control R to do a remesh,
[23:18] bit of smoothing as well,
[23:19] and maybe a bit of inflating if needed.
[23:22] And then the elastic snake hook
[23:23] has that same sort of interesting twist about it,
[23:27] but it's a much bigger area.
[23:29] So when I move my brush around,
[23:31] you can see it twisting the shape.


### Grab 2D Brush [23:32]
**Transcript (timestamped):**
[23:33] Then we got the 2D grab brush.
[23:35] This is quite an interesting one.
[23:36] It treats the shape like it's 2D.
[23:38] So if I go to front view
[23:40] and then try and get this edge here and bring it out,
[23:43] and then I move around to the side,
[23:45] you can see it's moved that whole of that edge.
[23:48] So back to front view and I try and bring this area out.
[23:51] You can see it's the whole of that section across there.
[23:54] So you're seeing right through the shape in a sense
[23:56] in 2D at this point.
[23:58] Doesn't matter what angle you're at.
[23:59] I'll just go to front view for the sake
[24:01] of showing you what it's like,
[24:02] but you can see that it's doing the same thing,
[24:04] whatever angle and it's perpendicular to the camera.
[24:08] As you can see there,
[24:09] it's bringing those areas out
[24:10] for my squid monster that I'm making here.


### Grab Silhouette [24:12]
**Transcript (timestamped):**
[24:13] Then the next brush is the grab silhouette.
[24:15] And that's trying to get the very edges of your object.
[24:19] So when you move over the edges of your object,
[24:21] it will really try and pull out that particular edge.
[24:25] So it's going for the very edge point,
[24:27] silhouette being the very outline of your shape.
[24:30] And if I'm trying to get that edge there,
[24:32] it grabs it nicely
[24:33] and brings it out perpendicular to my camera.
[24:36] You might be thinking,
[24:37] well, isn't that the same as the grab brush?
[24:38] Well, it's surprising with the grab brush.
[24:39] It's not that easy to grab.
[24:41] If I pull this out,
[24:42] it sometimes goes in a direction
[24:44] that you're not expecting more towards the camera.
[24:47] The silhouette is an attempt to really target the edges
[24:51] and pull them out.
[24:52] And you can actually see it in the details there.
[24:54] Similar to the grab,
[24:55] but only affects vertices
[24:57] with the normal facing sideways away from the view.
[24:59] Very useful for adjusting outer silhouettes.
[25:01] So the very outline of your shape.


### Nudge Brush [25:04]
**Transcript (timestamped):**
[25:04] Then there's the nudge brush.
[25:05] I mentioned this briefly earlier,
[25:07] but it's like the clay thumb brush,
[25:09] but that's actually creating topology
[25:11] as you're thumbing and pushing it around.
[25:15] The nudge brush will actually push my topology around
[25:18] without creating any new.
[25:20] Just smooth that area out.
[25:22] It's a little bit more predictable to be fair
[25:24] than the clay thumb in many ways.


### Pinch and Magnify Brush [25:25]
**Transcript (timestamped):**
[25:26] Then there's the pinch and magnify.
[25:28] For this, I'm going to do a crease polish.
[25:30] So a light line across here, let's say.
[25:33] And then the pinch magnify.
[25:35] Notice when I select this,
[25:36] again, it's got the plus and minus on this.
[25:38] And the minus,
[25:40] much like the crease sharp
[25:41] and the crease polish is the default for this brush.
[25:44] So if I start brushing down here,
[25:46] you can see how it sharpens that line up,
[25:49] but it's not deepening it.
[25:50] So the pinch brush in combination
[25:52] with something like the crease polish is really useful.
[25:56] So we're creating that depth there,
[25:58] and then the pinch is bringing it together.
[26:01] Often you have to remesh and then pinch again
[26:05] to kind of sharpen those edges up.
[26:07] So when I use something like the crease polish,
[26:09] you can see that the more I use it,
[26:12] the more it pulls the topology together
[26:14] and stretches it down here.
[26:16] Then if I do a remesh to sort of sort the topology out,
[26:20] I get this horrible blobbiness in the middle.
[26:23] Well, the pinch sorts that out,
[26:25] pinches it together and combined with a smooth brush.
[26:28] And then the pinch,
[26:29] you can get some really nice crevices,
[26:31] as you can see there.


### Pull Brush [26:32]
**Transcript (timestamped):**
[26:33] I'll leave the post brush for now.
[26:34] Let's go to the pull brush quickly.
[26:35] Make my brush big.
[26:37] It's basically, if I pull this around,
[26:39] like the snake hook,
[26:40] with its sort of ability to kind of twist the mesh like this,
[26:44] but it's a lot softer, as it says.
[26:47] So you can be a bit more precise.
[26:50] I'll just remesh this and smooth it out.
[26:52] Whereas the snake hook is quite quick and fast and loose,
[26:56] the pull brush is a little bit more precise.
[26:59] In fact, I'll just remesh and smooth that out.
[27:01] So that's the pull brush.


### Relax Pinch Brush [27:02]
**Transcript (timestamped):**
[27:02] I'll quickly go through the relax pinch and relax slide.
[27:06] You can kind of see what these are doing.
[27:08] So if I go to an area such as this,
[27:12] where we've, let's say, pinched it together a bit more,
[27:15] let's do that, because I've done a remesh in here.
[27:17] It's a good point, actually.
[27:18] If you're going to do lots of remaches,
[27:20] it kind of undoes the work you do for the pinch like this.
[27:23] Because when I press Ctrl R to remesh,
[27:25] it's obviously remeshing that area.
[27:26] And I need to pinch the topology together again.
[27:29] So we've got that nice sharp line,
[27:30] where we can relax the pinch here
[27:32] and you can see that softening that pinch.
[27:34] You might be thinking, well, doesn't the smooth brush do that?
[27:36] Well, if I hold down shift for the smooth brush,
[27:38] you'll notice nothing actually happens.
[27:39] That's because for some reason,
[27:40] I can't jump to the smooth brush with the relax pinch
[27:42] or the relax slide.
[27:43] Like I can if I jump to the draw brush, for example,
[27:46] hold down shift.
[27:47] And you can see here that it's smoothing everything out.
[27:50] Whereas the relax pinch, if I undo that,
[27:53] to where we've got the sharp pinch,
[27:54] let's relax the pinch.
[27:56] You can see it's relaxing that pinch
[27:58] without changing the shape so much.


### Relax and Slide Brush [28:00]
**Transcript (timestamped):**
[28:00] Relax and slide is more for sharp edges.
[28:03] So let's get the layer tool
[28:04] and build up a layer here a little bit.
[28:07] Remesh and then let's say I want to sharpen this up
[28:10] by using something like the crease polish.
[28:12] And I'm sharpening that edge up there,
[28:13] smooth it out a little bit,
[28:14] sharpen it up, smooth it out.
[28:16] And we've got quite a sharp edge there.
[28:18] Let's go to the pinch and try and pinch that together.
[28:21] We've got this lovely sharp line there,
[28:24] but I can relax and slide that because it's very, very sharp.
[28:27] And you can see the effects of that there.
[28:29] So we've done the snake hook.
[28:31] I've still got to come back to the pose brush,


### Thumb [28:33]
**Transcript (timestamped):**
[28:33] but let's scroll down a little bit.
[28:34] And we've got two more here.
[28:35] We've got the thumb, very similar to the nudge brush this,
[28:39] if I make this fairly big,
[28:40] and then I can sort of push this across.
[28:43] When you use it, you'll see how different it is.
[28:45] It's a bit more precise in some way than the nudge brush,
[28:49] whereas the nudge brush would take this whole area,
[28:51] as you can see it there,
[28:52] it's affecting this area in this area.
[28:54] The thumb is a bit more direct on the vertices
[28:56] that are directly under the brush.


### Twist [28:58]
**Transcript (timestamped):**
[28:58] Then there's the twist.
[28:59] It's kind of fairly obvious.
[29:00] It just rotates your topology
[29:03] in the direction that you paint.
[29:05] I'll do a remesh there.
[29:06] You can see our squid monster is in a bit of trouble, I think.


### Pose Brush [29:09]
**Transcript (timestamped):**
[29:10] Okay, so let's look at the pose brush,
[29:12] and we'll use our weird tentacle that's going down here.
[29:14] If I go to the pose brush,
[29:15] you can see when I move over, we've got this white line.
[29:19] This is supposed to be to enable us to try and pose our objects
[29:23] or for the most part, things like characters into position.
[29:27] It's a little bit tricky to work with
[29:29] just on its own like this.
[29:31] It tries to judge where you want the edit to take place.
[29:34] Just undo that last one.
[29:35] And you can have some pose segments here.
[29:38] So if I turn this up to two,
[29:40] you can see that it's trying to work out
[29:43] where these two segments are.
[29:44] It's doing a relatively good job.
[29:46] You can be more precise with something like face sets.


### Face sets [29:47]
**Transcript (timestamped):**
[29:49] So if I go across to draw a face set here,
[29:53] I can just bring my brush down, start drawing over this.
[29:56] So it's a green color like so.
[29:58] Go around to the back.
[29:59] Oh, that's handy, actually, it's gone all the way through.
[30:01] And now I can, in my pose brush,
[30:03] instead of rotation orientation on topology,
[30:07] I can change it to face sets.
[30:09] And then let's just turn the segments back down to one.
[30:11] And I know I'm going to affect just that face set.
[30:14] Can be quite useful that.
[30:15] There's probably more to say about the pose brush,
[30:17] but that's probably the best introduction.


### Boundary Brush [30:18]
**Transcript (timestamped):**
[30:18] The last tool is the boundary brush.
[30:21] Now, because our mesh is manifold,
[30:23] if I click on the boundary and try and do things,
[30:26] nothing's happening.
[30:27] I'm going to go back to layout mode
[30:28] and just hide our icosphere for a moment,
[30:31] shift A to add, and let's add something like a cylinder.
[30:34] And I'll go into edit mode and delete the top face.
[30:37] So into face mode, select top face and delete.
[30:41] In fact, let's delete the bottom face as well.
[30:43] So delete faces.
[30:44] I'll add some topology.
[30:45] So control R to do a loop cut,
[30:47] use the wheel of my mouse and create some topology there.
[30:50] And then let's go back to sculpt mode.
[30:52] So there's my cylinder.
[30:53] Now when I use the boundary brush,
[30:54] you can see that it's looking at those boundaries
[30:57] that have been created.
[30:58] So I can select this boundary here
[31:00] and move it in and out.
[31:02] And there are all sorts of interesting deformations
[31:05] you can use.
[31:06] So there's bend, there's twist.
[31:09] I can twist it around, inflate.
[31:13] Just a basic grab and much more.
[31:16] So that's the boundary brush.
[31:18] And that's for working with meshes
[31:20] that actually have a boundary like this one.
[31:22] So there we have all the push and pull brushes.
[31:26] So if I bring my brushes out for a moment,
[31:28] we've been through all the add and subtract brushes
[31:31] and the grab kind of push and pull brushes.


### density, Erase Multires and smear multires [31:34]
**Transcript (timestamped):**
[31:35] There's a couple of brushes that are specific
[31:37] to the type of sculpting that you're doing.
[31:39] The density is used with dynamic topology
[31:42] and you can paint on a certain density,
[31:44] a bit like the voxel size.
[31:45] The erase multi-res displacement is only used
[31:48] with the multi-resolution modifier.
[31:50] And you can kind of take out levels of detail
[31:52] from your multi-res.
[31:53] But again, that's with a slightly different type
[31:55] of sculpting, sculpting using a multi-resolution modifier,
[31:59] which I'll talk about in different videos.
[32:00] We've slightly touched on face sets
[32:02] and you can paint face sets with this brush.
[32:05] Again, a bit beyond the scope of this tutorial.
[32:07] I'll talk about the mask in a moment,
[32:08] but we've also got smear multi-res displacement,
[32:11] which is similar to the erase multi-res displacement.
[32:14] But instead of erasing, you're smearing
[32:16] and blurring it around.
[32:17] I won't talk about all the painting brushes.
[32:19] Again, that'll be for another episode
[32:21] where we talk about vertex painting.


### Mask Brush [32:23]
**Transcript (timestamped):**
[32:23] But I will quickly introduce you to the mask brush.
[32:25] I'll just minimize my brushes again.
[32:27] The mask brush allows me to paint on to my sphere
[32:31] with a black color.
[32:32] It's automatically set at strength one.
[32:34] And anything that I paint in black
[32:36] means I can't affect it by the other brushes.
[32:38] So let's go to the draw brush, for example.
[32:40] If I paint anywhere else, you can see it painting,
[32:43] but not on that mask area.
[32:45] It's obviously very useful
[32:46] when you don't want to affect a certain area.
[32:47] I'll undo those brush strokes and alt M
[32:50] is to remove the mask you just painted.
[32:53] Further down the menu, we have the cloth sculpt brushes.
[32:56] I'll talk about the bend bounds and twist bounds
[32:58] in a moment.
[32:59] But as you can imagine,
[33:00] they're similar to the boundary brush
[33:03] that we talked about earlier.
[33:04] And therefore don't work on a manifold object like this
[33:07] or an object that hasn't got boundaries.


### Drag Cloth [33:09]
**Transcript (timestamped):**
[33:10] I'll actually start with the drag cloth just here.
[33:12] This is a useful one to explain what's going on
[33:14] with these cloth simulation brushes.
[33:17] I'll zoom in on my sphere
[33:18] and I'll draw across the surface very slowly.
[33:21] Now, the reason I say slowly
[33:22] is because it does actually affect the brush.
[33:25] You can see it's giving this idea of cloth
[33:28] that's been pulled where my brush was.
[33:31] Now, notice if I go across the surface quickly,
[33:34] it's a very different effect.
[33:35] So with all the cloth brushes,
[33:37] I find that you do need to give the simulation some time
[33:40] to actually adjust to the stroke.
[33:42] So going across fairly slowly,
[33:44] you can give it time to simulate what's going on
[33:47] and therefore come up with some sort of cloth effect.
[33:50] And as I say, the drag cloth is kind of creating creases
[33:53] along the sides of my brush stroke.
[33:55] I'll undo a couple of those


### Expand and contract cloth Brush [33:56]
**Transcript (timestamped):**
[33:56] and let's go to the expand cloth option.
[33:59] And again, I'll just brush across the surface fairly slowly
[34:03] and you can kind of see what's going on here.
[34:05] It's a really interesting effect.
[34:07] And particularly for this one,
[34:08] I do find that you do need a bit of smoothing
[34:12] in order to make it work.
[34:13] So as I smooth out,
[34:14] you can kind of see that looks a bit more realistic
[34:17] as it were as opposed to the earlier version.
[34:19] Once again, if I move quickly,
[34:21] it really doesn't work particularly well.
[34:23] So moving slowly, you can see the effects of this
[34:27] and then smoothing out gives you a more realistic effect.
[34:30] You may find that it's smoothing out a bit too much.
[34:33] You can do one of two things,
[34:34] reduce the strength of your smooth brush
[34:37] or increase the face count by remeshing to a higher count.
[34:42] So the expand contract is kind of a scrunching cloth effect.
[34:45] And I'll undo this second one here.
[34:48] This time I'm holding down control.
[34:50] Doesn't seem to be a lot happening,
[34:52] but when I move really slowly,
[34:53] you can see there is something going on.
[34:56] It's supposed to be contracting in on itself.
[34:58] I think this is one where you may have to change
[35:00] the settings slightly, perhaps the fall off.
[35:02] You can see it's got very hard edges,
[35:05] but it could possibly give an effect that you're looking for.
[35:08] Quite an interesting effect that one.


### Grab Cloth [35:09]
**Transcript (timestamped):**
[35:10] I'll undo that brush stroke
[35:11] and go across to the grab cloth.
[35:12] Now this one pulls the cloth across slightly,
[35:15] not so much outwards from the shape, but a little bit,
[35:18] but more across the shape.
[35:19] And again, simulates the cloth around the area you pull.
[35:23] And again, as with all the cloth brushes,
[35:25] you have to be a bit careful that you pull fairly slowly.
[35:28] A quick pull doesn't seem to have as an effective result
[35:32] as if you move a bit slowly with the brush.
[35:35] I'll talk about grab planar with bend and twist in a moment.


### Grab Random Cloth Brush [35:37]
**Transcript (timestamped):**
[35:38] Grab random is an interesting one.
[35:41] It's kind of like the grab cloth
[35:45] that we've just looked at up here,
[35:46] but rather than pulling it off the surface,
[35:48] it just creates a creased area, as you can see here.
[35:52] I like this one for just adding random creases
[35:54] in certain areas.


### Inflate Cloth Brush [35:55]
**Transcript (timestamped):**
[35:55] Now I've jumped to a clean sphere
[35:57] because it was getting a bit messy.
[35:58] And the inflate cloth brush is a good one
[36:00] to talk about some of the nuances of the cloth brushes.
[36:03] Now I've got 35,000 faces.
[36:05] It's fairly low resolution as it were,
[36:07] or low face count for a sculpt.
[36:09] If I use the cloth brush on here, move that around,
[36:13] you can see it's not having a huge amount of effect.
[36:15] Let's go to another spot over here.
[36:17] It's slightly better, but not much.
[36:20] I'll undo those and let's do a remesh.
[36:22] So I'll press R, go down to 0.01, so it's fairly fine.
[36:26] Somewhere around there and control R.
[36:28] Let's try again.
[36:29] And you can see it's quite a different result really.
[36:32] It's coming out a lot further,
[36:34] and I'm having to pull it out a lot further
[36:36] to get any of the creases.
[36:37] And there's two things going on here.
[36:39] It feels like the brush isn't being very effective for one,
[36:42] but I'll talk about that in a moment.
[36:43] But there's also something to be said
[36:44] for the resolution of your mesh.
[36:47] What seems to be going on here is that the higher
[36:49] the resolution, the harder your processor has to work
[36:52] to figure out the cloth simulation.
[36:54] And therefore it actually seems to have
[36:56] a bit of a different effect going on.
[36:58] Let's go to the lower resolution of about 0.03,
[37:02] do the remesh and bring it out there.
[37:04] And you can see it's very different
[37:06] in the way it's reacting to the higher resolution.
[37:09] Let's make my brush nice and big here and pull it out.
[37:12] And strangely, that's having quite a good effect
[37:15] across my mesh.
[37:16] I'll undo all those, remesh to a higher level,
[37:19] or higher face count I should say,
[37:21] and then try and bring it out in the same way.
[37:23] My processor is obviously struggling here,
[37:26] and it's just inflating the mesh.
[37:28] So not only is it down to how quickly
[37:30] you're moving the mouse across the mesh,
[37:32] it's also down to the face count,
[37:33] how effective some of these brushes can be.
[37:35] So that's one aspect of the inflate cloth.
[37:37] I'll just undo those changes.
[37:39] What I'm going to do is pull out a bit of mesh.
[37:42] So I'll go to the snake hook
[37:44] and bring out a bit of mesh like this,
[37:46] and then do a remesh, smooth it out a bit,
[37:48] and let's take us back to the inflate cloth.
[37:50] Now if I go over this area with the inflate cloth,
[37:53] and wiggle it a bit from side to side,
[37:55] you can see really that that's kind of the intended use
[37:59] it feels like.
[38:00] It's to inflate areas, let's say along an arm
[38:03] or a leg or something like that,
[38:05] and we want to inflate this little bit here,
[38:07] then you get the creases around it.
[38:08] Whereas if I try and do it on the sphere,
[38:11] it doesn't really have the same effect,
[38:12] because again, it seems to be more for these
[38:14] sort of long, thin, protruded areas
[38:16] where you're trying to inflate an area within that.
[38:19] So just be aware of those nuances of these brushes
[38:22] and the use of these brushes.
[38:23] Okay, so now I've got this extended bit.
[38:25] I'm just going to smooth that out a bit.


### Bend and twist cloth brush [38:26]
**Transcript (timestamped):**
[38:27] I can talk a bit about the bend and twist.
[38:29] That's a lot like the pose brush,
[38:31] and let's go to my tool settings.
[38:33] Remember you've got the pose segments here,
[38:35] and I can then move this across,
[38:37] and you can kind of see,
[38:39] although it's struggling a little bit,
[38:42] but if I move that around,
[38:44] it moves it like the pose brush,
[38:45] but it adds the cloth simulation to it.
[38:48] So you can kind of see that going down
[38:51] the protrusion that I've got here.
[38:53] Notice it's got two modes,
[38:54] so we can hold down control and then twist it,
[38:57] as you can see there.
[38:58] And it looks like it needs a little bit of smoothing
[39:01] to make that work.
[39:02] So the bend and twist like the pose brush,
[39:05] but adding some cloth simulation to it.
[39:07] I'll just smooth this out a fair bit again,


### Grab Planar [39:08]
**Transcript (timestamped):**
[39:09] and let's go to the grab planer.
[39:11] Now if I grab this, you can see,
[39:13] I grab it outwards and pull it inwards,
[39:16] and that's what you tend to do with these things.
[39:17] You sort of wobble the brush around,
[39:19] and it creates this nice cloth simulation,
[39:22] again, down this protrusion.
[39:25] If I try and do it on the sphere,
[39:27] it doesn't really work.
[39:28] It has some sort of effect,
[39:29] but it's all over the place.
[39:30] So it's another brush that's built
[39:32] for these long protrusions.
[39:33] And in many ways,
[39:34] that's indicated in the icons of the bend and twist,
[39:37] the grab planer and the inflate cloth.
[39:39] They have the icons show a protrusion for it to work.
[39:43] Okay, I'll undo those changes.


### Stretch and Move Cloth Brush [39:44]
**Transcript (timestamped):**
[39:45] Let's just quickly jump to the stretch and move,
[39:47] as that's a similar one to the bend and twist.
[39:50] I'll take my extrusion, and I can stretch it out,
[39:54] making sure I go fairly slowly to do this.
[39:57] It's struggling a bit,
[39:59] and give time for the cloth simulation
[40:01] to kind of catch up with me.
[40:02] And you can see that working away there.
[40:04] So that's the stretch aspect of it,
[40:06] and it's stretched all the way down here.
[40:08] If I hold down control, we've got the move option here.
[40:13] And again, it's using that pose brush
[40:16] and adding a cloth simulation to it.
[40:18] I'd need to smooth this out a fair bit, I think,
[40:20] for that to work.
[40:21] Okay, I'll go back to my protrusion and sphere.
[40:24] I'll zoom in on this area,


### Pinch Folds Cloth Brush [40:25]
**Transcript (timestamped):**
[40:26] and let's go to the pinch folds.
[40:28] Make my brush a bit smaller.
[40:30] Come across the surface,
[40:31] and you can see this is kind of similar
[40:33] to the things like the grab brush or the drag cloth,
[40:35] but it's offering a pinch in the middle there.
[40:37] I'll just smooth that out a little bit,
[40:39] and you can see that pinch that's coming together.


### Pinch Point Cloth Brush [40:41]
**Transcript (timestamped):**
[40:42] Pinch points, it's very similar,
[40:44] but instead of a fold, it's a point.
[40:46] And again, I'll move across the surface,
[40:48] and you can see it's pulling out to a point.
[40:50] It's a little bit like the grab random in that sense,
[40:52] but it comes out to a point, and I quite like that one.


### Push Cloth [40:54]
**Transcript (timestamped):**
[40:55] Let's move around a bit and go to the push cloth.
[40:57] So if I just wobble my brush around,
[41:00] again, this slightly nuanced one,
[41:02] the more you do it,
[41:03] the more it just goes into this crevice like this.
[41:06] But if I'd done that slightly less and stopped at this point,
[41:09] then it offers that nice sort of cushioned button effect.
[41:13] If I combine this with, let's say, the blob brush,
[41:18] bring that in here and have a little blob in there,
[41:20] you can see it's got a sort of cushion look,
[41:22] which looks great fun.
[41:23] Okay, so back to the sculpt cloth brushes.
[41:25] So be a bit careful with that push cloth.
[41:27] If I draw relatively quickly,
[41:29] we can get the effect that we're expecting.
[41:32] But if I keep on going,
[41:34] it slowly softens it out and becomes this crevice.
[41:38] So watch out for that.


### Boundary Cloth Sculpt brushes [41:39]
**Transcript (timestamped):**
[41:39] For the boundary cloth sculpting brushes,
[41:42] I'll create a cylinder again
[41:43] and delete the top and bottom faces.
[41:45] So we've got a boundary to sculpt on,
[41:47] and I'll make sure it's got a bit of topology down the middle
[41:49] by doing a few loop cuts and then back into sculpt mode.
[41:52] Now, when you have holes in your mesh like this,
[41:54] you can't use the remesh.
[41:56] I'll show you what happens when I try to use it.
[41:59] It comes up with this sort of error.
[42:00] So generally we use something like the multi resolution modifier
[42:03] to add detail to objects that aren't manifold.
[42:07] So I'll quickly do that for the sake of showing the brushes,
[42:10] but you'll have to look at my multi resolution
[42:12] versus dying topo videos for more information
[42:15] on this type of sculpting method.
[42:16] So I'll go across to the modifiers, add modifier,
[42:18] type in multi res and then subdivide this maybe three times.
[42:23] Just having a look at the face count over here,
[42:25] probably a little bit more than that.
[42:27] Let's go up to 300.
[42:28] So we've got quite a lot of detail here.


### Bend Boundary cloth brush [42:30]
**Transcript (timestamped):**
[42:30] So we've got the bend bounds brush
[42:32] and I'll go back to the tool settings here.
[42:35] This is very similar to the other bend brush
[42:37] and you can see there's deformation types here,
[42:39] twist, grab, inflate and so forth,
[42:41] but the deformation target
[42:43] is using a cloth simulation this time.
[42:46] So let's just see what that does.
[42:47] As I bring this down relatively slowly,
[42:50] you can see it's adding a cloth simulation
[42:52] that kind of ripples downwards.
[42:54] It's really interesting.
[42:55] Again, it's quite difficult to control.
[42:57] The things that will make a difference
[42:58] will be your face count and how fast
[43:00] or slow you move your brush
[43:02] and it probably needs a bit of smoothing out.
[43:05] But hopefully you can see the ideas
[43:06] and experiment with this for yourself.


### Twist Boundary cloth Brush [43:07]
**Transcript (timestamped):**
[43:07] The twist bounds, if I click on that,
[43:09] you can see it's the same brush
[43:11] but with the deformation of twist
[43:13] instead of bend as it was before.
[43:16] So I can go up to my end here and just twist it around
[43:21] with a very interesting effect there.
[43:23] And again, needs a bit of smoothing out really.
[43:25] So that's an overview of all the brushes available.
[43:28] Keep an eye on the channel for more in-depth tutorials
[43:30] on each of the brushes
[43:32] and other aspects of the sculpting workspace.
[43:35] If you've got any questions or thoughts,
[43:36] then do comment below.
[43:37] Thanks for watching and I'll see you next time.



---

## Captured Frames

- [0:44] tutorials/frames/master-blender-sculpting-every-brush-explained/frame_000.jpg
- [3:15] tutorials/frames/master-blender-sculpting-every-brush-explained/frame_001.jpg
- [6:49] tutorials/frames/master-blender-sculpting-every-brush-explained/frame_002.jpg
- [13:01] tutorials/frames/master-blender-sculpting-every-brush-explained/frame_003.jpg
- [21:00] tutorials/frames/master-blender-sculpting-every-brush-explained/frame_004.jpg
- [30:52] tutorials/frames/master-blender-sculpting-every-brush-explained/frame_005.jpg
- [33:19] tutorials/frames/master-blender-sculpting-every-brush-explained/frame_006.jpg
- [42:47] tutorials/frames/master-blender-sculpting-every-brush-explained/frame_007.jpg

---

## Structured Notes

### Core Technique
A comprehensive walkthrough of every brush in Blender 4.3's Sculpt Mode, organized by brush family (add/subtract, grab/push-pull, cloth simulation, boundary), paired with the Remesh/Dyntopo workflows needed to keep enough topology under each brush.

### Summary
Grant Abbitt starts from an Icosphere (not the default cube, which has too few vertices to sculpt) and demonstrates, in order, the add/subtract brushes (Draw, Clay, Clay Strips, Clay Thumb, Crease Polish/Sharp, Draw Sharp, Inflate/Deflate, Layer, Fill/Deepen, Flatten/Contrast, Plateau, Scrape Multiplane, Scrape Fill, Trim), the push/pull brushes (Grab, Snake Hook, Elastic Grab/Snake Hook, Grab 2D, Grab Silhouette, Nudge, Pinch/Magnify, Pull, Relax Pinch/Slide, Thumb, Twist, Pose, Boundary), and the cloth-simulation brush family (Drag/Expand/Grab/Inflate/Push Cloth, Bend/Twist Cloth, Grab Planar, Pinch Folds/Point, Boundary Cloth variants), plus Mask and Face Sets. Throughout, he stresses the Voxel Remesh (R for a live voxel-size gizmo, Ctrl+R to remesh) as the core workflow for keeping topology dense enough to sculpt cleanly, contrasts it with Dyntopo (creates new topology live instead of stretching existing geometry), and explains that boundary/cloth-boundary brushes only work on non-manifold meshes with actual open edges (e.g. a cylinder with its end caps deleted), while other cloth brushes are speed-sensitive — dragging too fast breaks the simulation.

### Key Steps
1. **Setup**: delete the default cube, Shift+A > Mesh > Ico Sphere, raise Subdivisions to ~6 in the operator redo panel for enough vertex density, then switch to the Sculpting workspace (auto-enters Sculpt Mode on the selected object).
2. **Brush basics**: brush picker at the bottom of the viewport (icon size + name toggle in the dropdown), F to resize brush radius, Shift+F to change strength, Ctrl held while stroking inverts add<->subtract on most brushes.
3. **Remesh workflow**: under the Remesh panel, set Voxel Size and press the Remesh button (or press R in-viewport for a live grid-size gizmo, then Ctrl+R to apply) — remeshing preserves overall shape while redistributing topology evenly; do this constantly after heavy stretching (Grab, Snake Hook, Blob-on-blob).
4. **Draw family**: Draw (default add/subtract, Ctrl to invert), Smooth (hold Shift to jump to it from any brush), Blob (rounded bumps — stacking blobs stretches the mesh and needs a remesh), Clay/Clay Strips (wider, textured build-up — favorite for adding surface texture), Clay Thumb (pushes clay into itself, adds topology) vs. Nudge (same push feel, no new topology).
5. **Crease/sharp family**: Crease Polish (gradual, gentler) vs. Crease Sharp (stronger, harder to control) both pull topology together to form a line/indent and can be reversed (Ctrl) to create a sharp protrusion; Draw Sharp is similar but doesn't pull the mesh together, giving a sharper default indent that can also be reversed into a ridge.
6. **Volume-shaping family**: Inflate/Deflate (great for thin stretched lines from Grab/Snake Hook), Layer (builds a controlled-height plateau, driven by the Height setting; struggles on angled/curved sections), Fill/Deepen (default Fill closes gaps, Ctrl = Deepen), Flatten/Contrast and Plateau (flatten an area while pushing neighboring geometry up/out), Scrape Multiplane (levels an area down toward an existing crease/crevice) and Scrape Fill (shears the tops off high points — good for battered/bashed metal look), Trim (indiscriminately cuts flat in the brush's facing direction; pairs well with Scrape Fill).
7. **Push/pull family**: Grab (moves topology bodily, needs frequent remeshing), Snake Hook (drags out thin protrusions, best combined with Dyntopo to avoid stretching), Elastic Grab/Snake Hook (same moves but affecting a much larger falloff area), Grab 2D (moves the full silhouette edge as seen from the current view, ignoring depth), Grab Silhouette (targets only outline-facing vertices, more predictable than plain Grab for outer-edge tweaks), Twist (rotates topology under the brush), Pose (segmented bend/rotate for posing limb-like protrusions, refined with Face Sets for precision), Boundary (drags open mesh edges — bend/twist/inflate/grab deformation types — only active on non-manifold meshes with real boundary edges, e.g. a cylinder with top/bottom faces deleted).
8. **Dyntopo**: enable in the header, set Detail Size (functions like Voxel Size), and brushes such as Draw/Clay Strips generate new topology live as you paint instead of stretching the mesh; movement brushes like Grab do not use Dyntopo and still stretch. Snake Hook is the one push/pull brush that does leverage Dyntopo for live topology growth.
9. **Cloth simulation brushes**: Drag/Expand/Contract/Grab/Grab Random/Inflate/Push Cloth, plus Bend/Twist Cloth, Grab Planar, Pinch Folds/Point — all run a live cloth sim under the brush, so slow, deliberate strokes are required (fast strokes barely register); Inflate Cloth, Bend/Twist Cloth and Grab Planar are specifically designed for long thin protrusions (their brush icons show a protruding shape) and work poorly on a plain sphere; higher face count makes the sim heavier and change its response, so effect is a function of both stroke speed and mesh resolution.
10. **Cloth boundary brushes**: Bend Bounds / Twist Bounds need an open, non-manifold mesh (e.g. a cylinder with deleted end caps plus a Multiresolution modifier subdivided ~3x for detail, since Remesh cannot be used on non-manifold geometry); they combine the boundary drag with a rippling cloth simulation.
11. **Masking & Face Sets**: Mask brush paints black areas immune to all other brushes (Alt+M clears the mask); Face Sets (paint face-set colors) let you scope brushes like Pose precisely to a region instead of relying on automatic segment detection.

### Nodes / Settings
- **Sculpt Mode panel**: Remesh section — Voxel Size field + Remesh button; in-viewport live gizmo via R (drag to set size) then Ctrl+R to execute. Typical voxel sizes shown: ~0.01-0.03 depending on desired resolution/performance.
- **Dyntopo**: toggle in the header; Detail Size setting (analogous to Voxel Size) controls how fine new topology is generated while sculpting.
- **Overlays > Statistics**: enabled to show live face count (used to demonstrate topology growth from ~2,000 to ~500,000+ faces after remeshing).
- **Modifiers (for boundary/cloth-boundary brushes on open meshes)**: Multiresolution modifier added and subdivided ~3 times (~300+ faces) since Voxel Remesh doesn't work on non-manifold meshes with holes.
- **Brush color coding**: gray/red-marked brushes add and subtract topology (most have a +/- default with Ctrl to invert); yellow-marked brushes (Grab, Nudge, Pose, Boundary, etc.) push/pull existing topology without adding new geometry and generally have no invert.
- **Pose brush deformation modes**: Rotation (default, driven by pose segments count) or Face Sets (scoped to a painted face set), toggled in the tool settings.
- **Cloth brush deformation targets** (Bend/Twist Bounds): selectable target list including Twist, Grab, Inflate, etc., applied through a cloth-simulation solve instead of direct vertex movement.

### Difficulty
Intermediate

### Blender Version
Blender 4.3.1 (mentions all Blender 4.3 brushes, including newer additions)

### Tags
organic, displacement, cloth, intermediate, blender-4x

---

## Related Tutorials
- [4 NEW Retopology Tips to Discover - Blender Secrets](4-new-retopology-tips-to-discover---blender-secrets.md) — covers the same Relax Slide sculpt brush referenced here, plus organic/topology-focused workflow tips that complement this brush survey.
- [Blender's NEW Cloth Simulator Changes Everything](blender-new-cloth-simulator-changes-everything.md) — deep dive on Blender 5.2's Cloth Dynamics GN node, a procedural counterpart to the cloth sculpt brushes (Drag/Expand/Bend/Twist Cloth) demonstrated in this video.
- [Recreate this in Blender in 20 mins](remake-this-in-blender-in-20-mins.md) — applies organic sculpting from a remeshed cylinder base, directly building on the Remesh workflow taught here.
