---
title: Don't Make Boring Audio Visualizers (Blender Tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=2xGchC_1Mi8
author: Ducky 3D
ingested: 2026-09-04
blender_version: "Blender 5.2"
tags: [geometry-nodes, motion-design, animation, procedural, compositing, eevee, blender-5x, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/
frame_count: 15
frame_status: complete
uncertainty_frames: []
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Don't Make Boring Audio Visualizers (Blender Tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=2xGchC_1Mi8)
**Author:** Ducky 3D
**Duration:** 16m37s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Alright, today I want to do kind of a relaxed deep dive into audio visualizers in Blender,
[0:07] specifically using the new sample sound frequencies node that was pretty recently released.
[0:13] What this video is, what I'm mostly thinking about is going, how can we make really interesting
[0:18] audio visualizers that are very different than what we typically have been able to do with
[0:23] After Effects? So I want to talk about two audio visuals that I made recently, what I was thinking,
[0:29] how I got there, and then I also want to show you guys a really cool trick to help you make
[0:33] some interesting audio visualizers in Blender. So I'm really just going to walk through it,
[0:38] talk through it, not a lot of fancy editing, anything like that. So if you're into audio
[0:42] visualizers, if you're into motion graphics, I think this is going to be a really interesting
[0:46] video to watch. Now, first, I do want to shout out, I just released the third edition of my
[0:52] motion graphics course, and I'm really proud of it. It's eight hours long, and it's cut into these
[0:57] two parts. The first half is your fundamentals, learning really simple concepts that when you
[1:03] combine them all together, make really beautiful animations. And then the last half, we're going
[1:07] to apply all that information to 10 really cool animations. So you can walk away with something
[1:12] really cool. Again, it's eight and a half hours, there's a lot of really cool content in there.
[1:16] It's meant to show you how to combine things to make beautiful things in Blender. So if you
[1:20] want to check that out, it's 25% off for the first month that it's released with this code. So if
[1:24] you want to check it out, that is linked in the description and onward to learning about
[1:30] audio visualizers. So first, I want to talk about the ideation phase. If you're thinking about audio
[1:35] visualizers and making audio visualizers based on other audio visualizers that you've seen,
[1:40] take a shot every time I say that, you'll come up with cool stuff, but it won't be super original.
[1:46] Normally, we're seeing the waveform. That's what I'm talking about, about like getting away from
[1:50] after effects. Now, there's nothing wrong with making animations with the waveform. In fact,
[1:55] it makes sense contextually. And there's some cool ways to do it. What I'm really interested in is
[2:00] how to get 3D scenes to be audio reactive. And this new node in geometry nodes lets you have that.
[2:07] So first, before we get into the technical how to, I think the ideation phase is really important.
[2:14] For example, with this audio visualizer that I made, this was the reference, not this specific.
[2:20] I don't have the reference anymore, but it was essentially I was looking at these organic patterns.
[2:26] If you've used Blinder for a while, you know it's Voronoi.
[2:30] How I was like, oh, why don't I make like, is it called a Petri dish where you're looking at a
[2:34] microscope and seeing cells and stuff? So this kind of stuff is what I was like, oh, can I make
[2:39] something like this? That's audio reactive. That's to me the best way to make original looking
[2:45] audio visualizers is starting with something that's not initially reactive to audio. I highly
[2:53] recommend Pinterest. Pinterest is my like number one place. And then this other audio visualizer
[3:01] was inspired by this image here. I was like, Oh, some I can have the audio react to some of these
[3:06] circles that are on and off, and then I'll get them to connect and I'll do my own thing after that.
[3:11] But this is the best place to start and come up with find a reference or even literally even easier
[3:19] one of your old designs and use that. I mean, you can do something similar to this. This is spheres
[3:27] with like a vector transform, but make something cool first. Now jumping into Blinder, how can we
[3:35] get around the constraints of what the node is giving us? So now I want to show you a really
[3:41] cool trick and give you a cool idea that you can use in Blinder if you're aware of if you know how
[3:47] to use geometry notes. If you don't, shameless plug, but my course might help you or my whole
[3:54] YouTube channel too. You don't need to buy my course at all. Let me show you. So we're thinking
[4:02] about the constraints. So let me show you what I mean by the constraint of like the limitation of
[4:07] what this node can do. So first, I'm just going to go ahead and get a plane. I'm going to go into
[4:12] geometry nodes. I'm going to click new. And I'm just going to bring this over so we can see the
[4:18] node tree first. We're going to get a store named attribute node. I'm going to name it
[4:27] song. Also get a song, get any piece of audio. It could be a piece of audio view screaming.
[4:32] Doesn't matter. Okay. So you have a store named after a store named attribute. Go ahead,
[4:40] take a screenshot of this, take a mental note, copy these nodes and then come back to the video.
[4:47] So hopefully you've done it. What we're going to do is here on this add node, make it a value of 100
[4:53] on this two minimum of the map range, 20, two max, 15,000. That's based on research, not based on my
[5:03] own knowledge of how audio works. So this is, we have this, we're going to go ahead and now import
[5:10] our song. So go here to the video sequencer, grab the scene, add sound. I'm going to grab a song
[5:21] from epidemic sound. That's who I use to avoid copyright problems. Here on YouTube, I'm going
[5:25] to give myself 5000 frames and then look at the whole song. So this is the whole song.
[5:38] Hopefully you can hear that, but it's playing audio. So now you can hit the drop down and grab it. So
[5:42] now we're able to plug this into the value. What's great about this is we can get a set material node
[5:51] and grab that material. Now we can head into shading. We can look at this little cube and we can go
[5:59] ahead and grab an attribute node, make this emissive. We are heading a direction, I promise.
[6:09] And then the song, the name of your attribute. Okay.
[6:15] And then I can also go ahead and subdivide this guy pretty heavily. Okay.
[6:27] Now I can start talking about the constraints. So the constraints of this is that it's kind of a
[6:34] float. Is that the right term? It goes from left to right or up and down, right? It doesn't have any
[6:39] information as far as I'm aware. So this map range will move it. And then this from max.
[6:46] So now we get to appreciate the whole waveform and it's left to rightness. Your low end is here,
[6:55] your high end is there, which you can hear it. You can make some...
[7:01] So when it goes, you can really see that that high end
[7:05] is affecting. So now you get it. Hopefully you get it. Base, kick drums, subs down here,
[7:13] high end like instruments, violins, pianos, vintage synthesizers, whatever. You'll see them
[7:19] visually on this end. So you have these two things. So if you're using them creatively,
[7:24] it can feel a little bit restricting. In this animation, my whole goal was to hide the fact
[7:33] that that texture was from left to right. So I spun it in circles and then the Voronoi texture
[7:39] was using a mask to sort of animate a mask to make it look more organic and more alive.
[7:46] I was sort of working around the fact that it's this left to right image. This image, this animation,
[7:55] basically I took those points. You can see how it goes from left to right and I shuffled them
[8:00] with a displacement and geometry nodes and moved those around. I'm going to show you a trick that
[8:04] I need to go back to that animation and use because this is a much better way to take this
[8:10] information that goes from left to right and shuffle it so that it's just random bits of value
[8:17] that's just reacting to audio and it looks less obvious. How do I do that? Let's build
[8:23] something in geometry nodes. So right now my input is just this grid that I created. I'm going to
[8:28] delete the input and then in geometry nodes, I'm going to get a brand new grid and plug it into my
[8:33] attribute and I'll make it 16 by 9 and then I'm going to go here, go to a camera and just add a
[8:44] camera like that and then in the faces, I'm going to give myself 16 by 9 on the faces so it looks
[8:57] really nice like that and then the attribute, because we can now see it, but specifically
[9:03] instead of using the points, I want it to apply this to the faces. So now it's going to do that.
[9:10] Now it's still because we used a position node, it's not going to, the position node doesn't
[9:17] really know about the geometry per se. It knows about the position and then we can move it around
[9:26] like that. If we can see it, where'd it go?
[9:33] Kind of move it around and then stretch it out like that. That looks cool, but again,
[9:37] the whole goal right now is I want to shuffle it. So I want some of this white port,
[9:40] like the low end to be randomly distributed around. The way that I can do that, the way that I can do
[9:48] that is with an index. Every one of these faces has an index. I think it maybe starts here at 0,
[9:53] 1, 2, 3, 4. So if I were to apply this to the index, then it would apply that
[10:01] to it and it would be kind of obvious. So instead, I'll take indexes and then I'll
[10:05] randomize the index so it throws it all over the place. That is as technical as I can explain it,
[10:14] that I'm capable of understanding it. So instead of this, we're going to go ahead and remove
[10:20] these. I'm going to get a index node and I'm going to plug it into the value.
[10:27] And you can see it's starting to work. It's starting to map it a little bit. If I go ahead
[10:31] and bring it up like that, it's applying it starting down here and then going. So you can kind
[10:37] of see it obviously, not obviously, but you can kind of start to see it and appreciate it.
[10:45] But again, it's still kind of left to right. That's not what we want. So I'm going to get a random
[10:51] value and I'm going to set it to integer because that's what indexes are. I'm going to plug this
[11:00] here and I'm going to plug index into the ID. I actually don't know if that does anything.
[11:06] Did I just discover I don't need the index ID? And then there we go. Now technically,
[11:12] you can delete the index and it does nothing. It does nothing. So I actually don't know if it
[11:18] does anything. I might be looking like a complete fool. I'm going to leave the index there anyway,
[11:22] but that's another way to map it. It's just straight up with indexes. But in this case,
[11:31] we'll randomize the index and then bring it down. And so now, if we go back to the beginning,
[11:39] that low end is showing up here, here.
[11:50] So you'll hear this kick drum kind of kick in here.
[11:56] So you're going to hear a kick drum in a sheet right about here.
[11:59] And so these really bright parts are that kick drum, are that low end,
[12:09] and it's randomly throwing it around. That's what I'm looking for. And then we can use a,
[12:15] we can brighten it up with a multiply. Now, one thing you can do is if you bring
[12:22] the minimum down, you'll get more of that low end showing up in the faces. So you have some
[12:26] control. So I did negative 16. And if you bring this from max down, I can go, oh, I only want to see
[12:37] low end. Or if you bring that from max up, it'll start to introduce from the values perspective.
[12:44] These things. I'm kind of not over the index thing. I feel like I realize that I'm talking
[12:51] out of my butt. Just put in a random value. But you can see how reactive this is now.
[13:03] So we can design something with this. We can right after the store named attribute, I'll get a
[13:11] split edges, and we'll get a scale elements. And then we can start to scale it down. Now we have
[13:17] some really cool design. I'm gonna remember world brightness down to black. Then we can go ahead,
[13:27] extrude the mesh. That's too high. We'll get a mesh bevel. Give it like eight segments.
[13:38] Set shade smooth. Maybe we'll do like six segments. Oh yeah, that'll work better.
[13:44] Now we have this.
[13:50] And then look at your camera view. I'm hitting G. Click out here. Let's go here to the shading. And
[13:57] now we can start to make this look even more awesome. Strength, bring it up.
[14:02] Strength, bring it up. We're gonna get a mixed color node. Set A to black, B to that.
[14:14] We're gonna get a, we're gonna get a layer weight node and plug facing into B.
[14:22] And we can do something like that in the camera. I can switch here to orthographic.
[14:30] And then bring that orthographic scale out.
[14:34] Add a color ramp.
[14:38] Switch it to B spline.
[14:42] And then lastly, let's just get a little compositing going. So if you go to the compositor,
[14:46] click new, get a glare node, set it to bloom, get a film grain. You are going to need Blender 5.2
[14:55] for this. 70 millimeter camera animated. And then if we go back to shading, hit drop down for always.
[15:06] Very primitive, right? You can take this much further than I just did. This is, you know,
[15:14] there's some cool stuff you can do it. You know, look, look, it's the, the course color.
[15:20] This is a really basic version. I will probably make a more designed out version of this for a,
[15:25] like independent YouTube video. But this was a cool way of shuffling your values that the sample
[15:33] sound creates to get something cool. My advice is something else in this needs to be animated to
[15:41] make it look a little bit more complete, you know, mix it another noise texture that's animating the
[15:47] cubes through. It'll make it look better. But again, I think the biggest point I want to make
[15:53] is look at some other cool stuff or make your own cool stuff and then go, let me incorporate
[16:01] the values that are created from the sample sound node and can I apply them and make it cool?
[16:08] That will be the thought process I will be using for the rest of the audio visualizer tutorials
[16:14] that I make on YouTube and Patreon. But with that being said, that's it. Again, I don't want to forget
[16:20] to mention my course that just came out. If you want to check it out and learn motion graphics,
[16:24] it is 25% off for probably like 20 more days, if not maybe a few more. So if you want to check
[16:32] that out, it is linked in the description. Hope you guys learned something from this and I'll see
[16:36] you in the next one.



---

## Captured Frames

- [4:27] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_000.jpg
- [5:00] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_001.jpg
- [5:21] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_002.jpg
- [5:55] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_003.jpg
- [6:46] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_004.jpg
- [8:50] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_005.jpg
- [9:05] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_006.jpg
- [10:22] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_007.jpg
- [10:58] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_008.jpg
- [12:24] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_009.jpg
- [13:12] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_010.jpg
- [13:34] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_011.jpg
- [14:16] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_012.jpg
- [14:38] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_013.jpg
- [14:52] tutorials/frames/dont-make-boring-audio-visualizers-blender-tutorial/frame_014.jpg

---

## Structured Notes

### Core Technique
Breaking the left-to-right spatial bias of the `Sample Sound Frequencies` node by feeding it a **randomised index** instead of position, so audio-reactive values scatter across a mesh rather than reading as a visible waveform.

### Summary
The `Sample Sound Frequencies` node returns amplitude for a frequency band, but the usual way of driving it — from X position — bakes the waveform's left-to-right layout into the design, which is what makes most audio visualisers look alike. The fix here is small and reusable: drive the frequency lookup from an `Index` passed through a `Random Value` in Integer mode, which shuffles which face responds to which band. Low end then flashes in scattered patches rather than marching along one axis. The rest of the video is a design pass on top of that idea — Split Edges, Scale Elements, Extrude Mesh and Mesh Bevel for the geometry, a Layer Weight facing mix for the shading, and a Bloom + Film Grain compositor finish. The framing argument is that original visualisers come from starting with a non-audio reference and *then* making it reactive.

### Key Steps
1. **Store the audio as a named attribute.** `Store Named Attribute` named `song`, on the mesh `[transcript 4:18-4:32]`.
2. **Build the frequency window.** `Scene Time (Seconds)` → the `Sample Sound Frequencies` node's `Time` input. A `Map Range` (`Float`, `Linear`, `Clamp` on, `From Min 0.000`, `From Max 1.000`, **`To Min 20.000`**, **`To Max 15000.000`**) feeds `Low`, and an `Add` node at **`Value 100.000`** offsets that into `High` `[frame_001]` `[transcript 4:47-5:02]`. The 20 Hz-15 kHz span is the audible range, and the +100 is the band width.
3. **Import the song.** Video Sequencer → `Add` → `Sound`, then extend the scene to ~5000 frames to cover the track `[frame_008]` `[transcript 5:10-5:35]`.
4. **Make it visible.** `Set Material`, then in the shader an `Attribute` node reading `song` into an **Emission** surface `[frame_008]` `[transcript 5:42-6:12]`.
5. **Understand the constraint.** Driven from position, the result is literally the waveform: bass at one end, treble at the other, sweeping left to right `[transcript 6:27-7:19]`. Two of the author's own past pieces worked *around* this by spinning it in circles or displacing the points `[transcript 7:24-8:03]`.
6. **Rebuild on a grid.** Delete the input, add a `Grid` at `Size X 16 m` × `Size Y 9 m` with `Vertices X 16`, `Vertices Y 9` `[frame_008]` `[transcript 8:28-8:56]`, and switch the attribute to the **Face** domain rather than points `[transcript 8:57-9:09]`.
7. **The trick — shuffle the index.** Replace the position input with an `Index` node, then a `Random Value` set to **Integer** (`Min 0`, `Max 100`, `Seed 0`) into the Map Range value `[frame_008]` `[transcript 10:20-11:04]`. Each face now samples an unrelated frequency band, so the low end appears in scattered patches `[transcript 11:31-12:14]`.
8. **Tune the response range.** Lowering the Map Range `From Min` brings more low end into the faces; raising `From Max` introduces more of the spectrum `[transcript 12:15-12:43]`. The sampled frame shows `From Min -6.900`, `From Max 266.260` `[frame_008]`.
9. **Design the geometry.** After the Store Named Attribute: `Split Edges` → `Scale Elements` (Face domain, `Scale 0.840`) → `Extrude Mesh` (Faces, `Offset Scale 0.520`, `Individual` on) → `Mesh Bevel` (Edges, `Segments`, `Shape 0.500`) → `Set Shade Smooth` `[frame_011]` `[transcript 13:03-13:43]`. Bevel segments are called out as 8 then revised to 6 `[transcript 13:34-13:43]`.
10. **Black out the world** so only the emissive faces read `[transcript 13:17-13:22]`.
11. **Shade it.** Raise emission strength, add a `Mix Color` with `A` black and `B` the colour, and drive its factor from a `Layer Weight` node's **Facing** output `[transcript 14:02-14:20]`.
12. **Switch the camera to Orthographic** and widen the orthographic scale `[transcript 14:22-14:32]`, then add a `Color Ramp` set to **B-Spline** `[transcript 14:34-14:40]`.
13. **Composite.** Compositor → `Bloom` node (mode `Bloom`, quality `Medium`, `Strength 1.000`, `Saturation 1.000`, Glare `Size 0.500`) plus a **`Film Grain`** node group from the asset shelf `[frame_014]` `[transcript 14:42-14:55]`. **Blender 5.2 is required for this** `[transcript 14:49-14:55]`.
14. **The design advice.** Something besides the audio should be animating — mixing in a moving noise texture is suggested — or the result reads as incomplete `[transcript 15:33-15:52]`.

### Nodes / Settings
- **`Sample Sound Frequencies`** — inputs `Time`, `All Channels` (on), `Channel`, `Low`, `High`, `FFT` `[frame_001]`
- **`Scene Time`** — `Seconds` output into `Time` `[frame_001]`
- **`Map Range`** (frequency window) — `Float`, `Linear`, `Clamp` on, `From Min 0.000` / `From Max 1.000` initially; **`To Min 20.000`**, **`To Max 15000.000`** `[frame_001]`. Later retuned to `From Min -6.900`, `From Max 266.260` `[frame_008]`
- **`Add`** — `Value 100.000` into the `High` input, setting band width `[frame_001][frame_008]`
- **`Store Named Attribute`** — name `song` `[transcript 4:22-4:27]`
- **`Index`** → **`Random Value`** (`Integer`, `Min 0`, `Max 100`, `Seed 0`) — the shuffle `[frame_008]`
- **`Grid`** — `Size X 16 m`, `Size Y 9 m`, `Vertices X 16`, `Vertices Y 9` `[frame_008]`
- **Geometry pass** — `Split Edges` → `Scale Elements` (`Face`, `Scale 0.840`, `Uniform`) → `Extrude Mesh` (`Faces`, `Offset Scale 0.520`, `Individual`) → `Mesh Bevel` (`Edges`, `Shape 0.500`, offsets `0.1 m`) `[frame_011]`
- **Material** — `Emission` surface, `Color` driven by `Attribute | Factor`, `Strength 1.000` `[frame_008]`; plus `Mix Color` (A black) with `Layer Weight → Facing` as factor, and a `Color Ramp` on **B-Spline** `[transcript 14:02-14:40]`
- **Compositor** — `Render Layers` → `Bloom` (`Bloom`, `Medium`, `Strength 1.000`, `Saturation 1.000`, `Tint`, Glare `Size 0.500`) → Group Output/Viewer, plus `Film Grain` node group `[frame_014]`
- **Render** — EEVEE; Viewport `Samples 16` with `Temporal Reprojection`; Render `Samples 64`, `Shadows` on `[frame_014]`
- **Audio source** — Epidemic Sound, chosen for copyright safety `[transcript 5:21-5:25]`

> **The author flags his own uncertainty, and it is worth preserving.** At
> `[transcript 11:00-11:22]` he wires `Index` into the Random Value's `ID` input, then
> immediately says he does not know whether it does anything, tests deleting it — "you can
> delete the index and it does nothing" — and concludes "I might be looking like a complete
> fool," leaving it in regardless. He returns to it at `[transcript 12:44-12:52]`: "I feel
> like I realize that I'm talking out of my butt. Just put in a random value." **Treat the
> `Index → ID` connection as unverified.** The `Random Value` alone is what produces the
> shuffle; `[frame_008]` shows `ID` present but proves nothing about its effect.
>
> **Frame-vs-transcript:** narration says "get a glare node, set it to bloom"
> `[transcript 14:47]`; in 5.2 the node reads as a dedicated **`Bloom`** node with its own
> mode dropdown `[frame_014]`. `Film Grain` is a node group added from the asset shelf,
> which is why 5.2 is the stated minimum. Whisper writes "Blinder" for Blender throughout
> and "mixed color" for `Mix Color`.

### Difficulty
Intermediate

### Blender Version
Blender 5.2.0 LTS — read from the title bar and status bar in `[frame_001]`, `[frame_008]`, `[frame_011]` and `[frame_014]`. Narration independently states 5.2 is required for the Film Grain step `[transcript 14:49]`, so both witnesses agree.

### Tags
geometry-nodes, motion-design, animation, procedural, compositing, eevee, blender-5x, intermediate

---

## Related Tutorials
- [Create an Audio Visualizer with Geometry Nodes in Blender 5.2](create-an-audio-visualizer-with-geometry-nodes-in-blender-52.md) — same node, same Blender generation, conventional position-driven approach; the direct contrast this tutorial argues against
- [Blender 5.0's NEW Audio Visualisation is INSANE!](blender-50s-new-audio-visualisation-is-insane.md) — the feature introduction for `Sample Sound Frequencies`; shares geometry-nodes, animation, motion-design
- [Can Blender Still Compete (Motion Graphics)](can-blender-still-compete-motion-graphics.md) — same author and Blender version, same instancing-and-shading design vocabulary; shares geometry-nodes, motion-design, blender-5x
