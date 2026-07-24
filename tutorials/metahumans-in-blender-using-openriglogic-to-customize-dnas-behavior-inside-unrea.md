---
title: MetaHumans in Blender: Using OpenRigLogic to Customize DNA's Behavior | Inside Unreal
source: YouTube
url: https://www.youtube.com/watch?v=WZhDr5Ktf9c
author: Unreal Engine
ingested: 2026-07-23
blender_version: "5.2 LTS (add-on supports 4.5–5.2)"
tags: [metahuman, riglogic, dna, facial-rig, rigging, shape-keys, animation, mocap, add-on, unreal-engine, blender-5x, advanced]
extraction_status: complete
frames_dir: tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/
frame_count: 15
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# MetaHumans in Blender: Using OpenRigLogic to Customize DNA's Behavior | Inside Unreal

**Source:** [YouTube](https://www.youtube.com/watch?v=WZhDr5Ktf9c)
**Author:** Unreal Engine
**Duration:** 82m50s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] and
[4:23] Hello, hello everyone and welcome back to Inside Unreal, a show where we learn, explore
[4:36] and celebrate everything Unreal.
[4:39] I am your host, Dan Hutnick, and if you haven't heard, the fab summer mega sale is currently
[4:46] live.
[4:47] Check it out to stock up on everything you need for your summer projects.
[4:51] Up to 70% off of tons of assets, templates, materials and much, much more.
[4:58] You've got until 11.59pm ET on July 29th to dive in.
[5:04] Head over to fab.com forward slash sale to snag yourself a deal.
[5:11] With that, today I am joined by James Baeber from Polyhammer who is here to talk about
[5:17] MetaHumans and Blender.
[5:19] Pretty exciting.
[5:20] Go ahead and let folks know who you are.
[5:23] Hi, I'm James.
[5:25] I'm a 3D tools engineer at Polyhammer and we specialize in integrating 3D technologies
[5:31] for artists.
[5:33] Perfect.
[5:34] Perfect.
[5:35] Well, this is a very exciting thing.
[5:37] We've already had several folks in chat going kind of crazy for it.
[5:41] I'm also one of them.
[5:42] I also use Blender quite frequently.
[5:45] Let's talk about a little bit what we're going to be exploring here today.
[5:48] Yes.
[5:49] So, following Epic's official announcement of the MetaHuman Dev Kit at Unreal Fest,
[5:55] Polyhammer has integrated open rig logic into Blender.
[5:57] I'll be showing you how you can use our free add-on to get a one-to-one MetaHuman rig
[6:03] in Blender working just like it does in Unreal Engine.
[6:07] And then furthermore, I'm going to be diving into some advanced workflows in the latter
[6:11] part of the presentation, touching on some of the pro features that we have in this add-on.
[6:18] Perfect.
[6:19] Perfect.
[6:20] Well, if anybody is watching live and has any questions for James specifically about
[6:25] using this open rig logic with MetaHuman's in Blender, please leave in the comments,
[6:31] brackets, question, followed by your question, and we will gather as many of those as we
[6:36] can and toss as many of those as we can to James here towards the end of the show.
[6:41] Please keep these questions relevant to the topic of open rig logic and MetaHuman's in
[6:47] Blender because that's what we're here to talk about today.
[6:49] If you have any other questions about general ecosystem, anything of the like, please head
[6:53] over to the EDC, our Epic Developer Community, where we have our forums, tutorials, documentation,
[6:59] and so much more as a resource for you.
[7:03] With that, are you ready to jump in?
[7:05] Yeah, let's go ahead and jump into, I have a slide deck here that I wanted to show at
[7:10] the beginning.
[7:12] This is just to give people a preview because most of this is going to be a live demo, but
[7:19] when I was preparing this, I was anticipating there being two types of viewers, maybe professionals
[7:24] that work with MetaHuman's every single day.
[7:27] Maybe you use Blender and you've never used Unreal Engine, you never use MetaHuman's.
[7:32] So I did want to take a little time to just define a few things around MetaHuman tech
[7:40] so that those people that are unfamiliar can get up to speed on that.
[7:48] And also explain what rig logic is.
[7:50] You may have seen this at Unreal Fest and never even heard of that, so I'm going to
[7:55] explain that here over the next couple of slides.
[7:58] But the presentation is going to be in two parts.
[8:00] The first part is just going to be an overview of how a logic has been integrated into Blender.
[8:06] That's the runtime that powers MetaHuman rigs and it is in a free add-on that you can get
[8:13] right now.
[8:14] The second part is going to be customizing DNA's behavior with only Blender.
[8:19] So previously, you would do this with Maya in the Maya expression editor.
[8:23] We have some pro features that allow you to do this.
[8:25] So if you're a, say you work as a professional character artist, you're a tech animator,
[8:30] this part of the presentation might be a little more interesting to you.
[8:36] But we're just going to go into part one.
[8:39] And for us to even talk about that, we need to understand what is DNA.
[8:43] So DNA is a proprietary file format invented by Epic Games.
[8:47] It contains meshes.
[8:48] It contains joints, which Blender calls bones.
[8:50] It contains blood shapes, which Blender calls shape keys.
[8:56] And probably at this point, you're thinking, okay, well, this sounds kind of like FBX or
[9:01] GLTF or some other file format.
[9:04] And that's where it gets a little more interesting.
[9:05] So there's something called GUI controls.
[9:07] These map to raw controls.
[9:09] And raw controls are ultimately what feed into the rig logic runtime and tell your
[9:15] medical character how to evaluate different expressions.
[9:19] And we get into the behavior layer of DNA.
[9:22] And this is kind of what I'm going to talk about in the later portion is how we can customize
[9:25] some of this stuff.
[9:26] So there's something called PSDs.
[9:28] These are post-based deformations.
[9:30] We're going to touch on these later on.
[9:33] There's RBFs, and these are primarily in the body, but they're also in the neck of the
[9:36] metahuman.
[9:37] These are radial basis functions.
[9:38] And these act as these advanced interpolation solvers that allow you to adjust corrective
[9:43] bones.
[9:44] And a lot of this stuff is going to make a lot more sense when you see it, an actual
[9:48] demo of it.
[9:49] But we're going to touch on those briefly.
[9:51] We do have a tutorial on how to use the RBF editor on our YouTube.
[9:55] So I'm mainly just going to focus on the face today, because that's the newer stuff.
[10:00] And there's also animated maps in DNA.
[10:03] So what these are, these are basically mask values.
[10:07] And you can hook them up to a shader.
[10:09] And the actual rig logic will compute your mask values.
[10:14] And there are different variants of blood flow maps on the colors, on your base color
[10:20] map.
[10:21] So if we take a look at this character here, you can see she does this expression at a
[10:26] certain point where there's the wrinkle in the nose.
[10:28] And you can see around the nose bridge, there's kind of those wrinkles appearing.
[10:31] That's actually happening at the material level.
[10:34] And that's by these animated maps, which allow through those extra blood flow maps on top
[10:39] of your base color.
[10:41] And then it also allows through the normal maps on top of your base normal maps.
[10:44] So then get those effects that you're seeing with the light there.
[10:48] So we're also just going to demo that here in a bit.
[10:54] But the add on itself is really geared towards supporting stuff you're exporting from a metahuman
[11:01] creator.
[11:02] So metahuman creator outputs a head DNA, outputs a body DNA.
[11:06] Here's a little breakdown of some of the contents that's in those files.
[11:10] This is by no means exhaustive.
[11:11] There's actually a lot more information that's in a DNA file.
[11:15] But I think you get the idea, this is a lot of data that makes up a metahuman.
[11:21] And when you're talking about a rig and computing or evaluating all this data, you have to do
[11:27] that really, really fast.
[11:28] And so that's why Epic invented something called RigLogic.
[11:31] And this is a portable runtime that evaluates the rigs based on the contents of your DNA
[11:38] file.
[11:39] So in the first part, I mentioned the GUI controls, those map to raw controls.
[11:44] This is what you'd animate on or import your motion capture that you've baked onto your
[11:51] control rig in Unreal Engine.
[11:54] And then you have your raw controls.
[11:56] These are ultimately what dictate what happens in the RigLogic runtime.
[11:59] So those go in, out the other side, you get your bone transformations, you get your shape key values
[12:05] updating, and you also get those animated map values, those materials that I was talking
[12:09] about earlier evaluating on the material of the metahuman.
[12:14] The thing about RigLogic is it is portable.
[12:18] They designed it in a way where it is application agnostic.
[12:22] It's just a C++ SDK.
[12:25] That's what they released at Unreal Fest.
[12:27] They have Python bindings for it.
[12:29] Our add-on utilizes it.
[12:30] This runs in Unreal Engine, it runs at Maya, it runs at Udini, and now it's running in Blender.
[12:38] So what does that do for us?
[12:40] That unlocks a lot of cool workflows.
[12:43] For people who, I mean, I'm sure most people watching this have maybe seen metahuman
[12:48] animator or played with it, but if you haven't, you should Google it, you should check it out.
[12:51] They've got a ton of really cool tools that you can use.
[12:54] You can make motion capture from your iPhone, you can do it with just an audio source.
[13:00] If you're a professional studio, you can have your own head-mounted camera setup
[13:04] and process depth data and get your animations that way.
[13:09] But you can take these animations out and you can import them onto your metahuman Rig in
[13:14] Blender since the metahuman is working just like it is in Unreal.
[13:18] And then most recently, there's the market list motion capture feature that they released in 5.8,
[13:25] which just kind of magically makes a full-body animation from a single video source,
[13:30] which is really cool.
[13:31] And so this can be the start for maybe your motion capture pipeline where you clean up
[13:37] animations or stitch together different animations.
[13:39] So I kind of let people fill in the blank exactly what this could be useful for,
[13:45] what kind of workflows you could use with having this out on, having metahumans
[13:51] integrated in Blender.
[13:52] So that's the first part we're going to just show that the actual metahuman rigs and everything
[13:57] integrated into Blender.
[14:00] And then the second part, we're going to get into some of those pro features that I was talking about.
[14:03] So like I said, pure tech animator character artist, this part of the talk might be
[14:09] a little more interesting to you.
[14:12] And we're going to kind of dive deeper into some of those things that I was mentioning on that,
[14:16] those earlier slides.
[14:17] But this might be what your current custom metahuman pipeline looks like.
[14:22] You know, you first generate it in metahuman creator, you take it out into Maya,
[14:26] you're using the Maya expression editor, maybe you don't like the sculpting tools that you have in Maya.
[14:31] So you rather prefer sculpting in a program like ZBrush,
[14:35] or some people are even sculpting in Blender because Blender's got some really great sculpting tools.
[14:40] Maybe you have a face form wrap in your workflow.
[14:42] That's a very powerful mesh wrapping software.
[14:47] And then there's Houdini, which there's also the groom tools that you have with Houdini.
[14:52] But Blender's also got some really great groom tools as well.
[14:56] So the question that I'm really asking is, could your pipeline look like this?
[15:03] I'm going to be honest, I don't think we're quite there yet, but with Unreal 5.8
[15:08] and some of the features in this add-on, I think we're getting very close.
[15:13] And so what we're going to do today is, this right here, we are going to see what we can do
[15:17] with just metahuman creator and Blender.
[15:21] And to demo this, what I decided to do is I have actually an ape character.
[15:27] And the reason I decided to do this was metahuman creator is actually really, really good at
[15:33] humanoid characters. And it's actually so good that it gets a little hard.
[15:40] I'm not a character artist. I don't have a very trained eye.
[15:42] It gets a little hard to see issues in facial anatomy if you don't do that every day.
[15:48] And so when you get a humanoid character out of metahuman creator, it actually looks pretty good.
[15:54] With the ape, I was able to clearly identify some issues.
[15:58] I think everybody on the stream is going to be able to see the issues that I'm going to fix on this.
[16:03] And we're going to see how far we can get with that in the demo today.
[16:11] With all that being said, this is not a step-by-step tutorial.
[16:15] I'm not going to show every click. I'm probably going to go through some of this stuff kind of fast.
[16:20] But I do want to kind of show you as much as I can of the workflow.
[16:25] And that's why I recommend you follow us on our socials,
[16:29] but especially out of recommend subscribing to our YouTube channel,
[16:32] because we make tutorials on all this stuff.
[16:36] And that's step-by-step. All the plugins need to install exactly how to do all those things.
[16:43] We also have discussions on our GitHub that you can ask questions on there as well.
[16:49] But with that, I think I'm just going to go ahead and jump into the first part of the presentation.
[16:55] And we'll get rolling here, because I think the best way to really understand all of this
[17:02] is just playing with the tools. So I'm sure people are aware this is metahuman creator.
[17:08] If not, this is a very powerful tool in Unreal Engine.
[17:11] You have really great looking characters out of the box.
[17:15] But there's just a section on here. There's an export tab. There's a DCC export option.
[17:20] And then there is a part where you go in here and you specify a file path.
[17:25] So I already did this. I ran the export process, and I'll show you what that looks like here.
[17:33] So that gives me, like I was saying in that earlier slide, we have our headDNA file.
[17:39] We have our bodyDNA file. And then it also puts some maps in this maps folder.
[17:44] And I think this might explain a little bit what I was talking about with the
[17:49] animated maps from RigLogic. So this is a neutral pose of the metahuman.
[17:55] This is what their texture looks like. This is a variant. And there's some special masks
[18:00] that will layer this on top of different regions of the base. And then this is the second
[18:06] wrinkle map. And then the third. And then it also works the exact same way with your normal maps.
[18:11] This is your base pose. Variant one, two, and three. So I will show you what that looks like on the
[18:19] actual rig. So you can, this works. So let's get the add on installed. You just go into your import
[18:28] and you go to metahuman.dna. You can import that way. Personally, what I like doing is I just drag
[18:33] and drop the headDNA file onto the viewport. And that'll pop up a dialog. You get this option to
[18:39] include the body by default. I'm going to import the body. So you just click import.
[18:46] We'll import here for a second. And then we should have our metahuman and blender.
[18:54] So if we have our face board here and maybe we grab the jaw control, we grab the mouth,
[19:01] we have the eyes. Everything is working exactly like it does in Unreal Engine. And that's because
[19:08] it all goes through that exact same runtime rig logic. As far as the add on UI itself,
[19:18] you have this tab characterDNA and you have a face board panel here. So you have some other
[19:24] options like maybe enabling the eye aim control instead of the actual eye controls on the board.
[19:33] You also have some poses like you have some visims for the mouth. You've got some emotions.
[19:39] And these can be good for understanding how the rig works. You can see how the different controls
[19:46] map to which parts of the face. These also can be nice if, say, you have motion capture data and
[19:51] you want to overlay some kind of emotion on top of your speech. You can use those for that.
[19:58] This is the wrinkle maps that I was talking about earlier. So these are, see this? We'll
[20:04] switch to the mask view. These are the three poses that activate those maps to their maximum value.
[20:13] So if you're trying to debug those, these can be helpful or maybe you're looking to extract
[20:19] some scan data. This is kind of how you would try to get your poses so that you could then make
[20:26] those maps that we were seeing earlier for the variants. Let me go back to the combined view.
[20:35] So here is a really good example on the forehead. You can see those wrinkles on the forehead.
[20:48] That's that first wrinkle map. And that also happens at the normals layer as well.
[20:56] So some of that stuff can be useful when you're kind of decomposing your rig.
[21:05] One thing that I wanted to touch on was the rig instances panel. So what this is, is this ties
[21:13] together all the information for metahuman rig. This is a blunder scene data block. It persists
[21:21] with your blunder file. But within a rig instance itself, it has two components. It has the head
[21:28] component, it has the body component. Both of these have their respective rig logic instances,
[21:33] and then those rig logic instances read from their own DNA file. So you have the head DNA,
[21:37] you have the body DNA file. That's how it knows how to do some of these transformations of the bones
[21:44] or of the shape key values, etc. So you can disable an entire instance, for example. So
[21:55] the rig doesn't work anymore. You can re-enable. And you can also do that at the component level.
[22:00] You can also do that at the output level. So bones, shape keys, wrinkle maps, and then rbf's,
[22:07] which I'm going to talk on briefly, because like I was saying, we're not going to spend too much
[22:14] time on the body today, but I'm going to show you the body bones. So these yellow ones here are
[22:25] the driver bones. And when you rotate these, this then feeds that rotation value into your radial
[22:34] basis function, and that function computes these corrective bones. So the best way to understand
[22:43] what I'm even talking about is if you rotate this with rbf's turned off, you can see how you have
[22:51] all this pinching going on, and you're losing volume there in the shoulder. If the rbf's are on,
[22:57] it actually looks good. And that's because these corrective joints are moved or posed at key poses
[23:05] to correct for those particular rotations. So those are done by solvers, which we were looking
[23:13] at the clavicle there. So the clavicle has just a couple key poses. So you can see here, these have
[23:20] been statically set. Like this is how the bones should correct at these different poses. And then
[23:25] there is a fall off function that basically defines interpolation on those functions. You can edit
[23:32] these, you can add more of these. We have a tutorial on our YouTube video, so I'm not going to talk
[23:38] about that today, but we're just going to focus really on the face. But yeah, that's really the
[23:45] body rig, the face rig. I am going to actually touch one more time on the, I'm going to touch one
[23:54] more time on the material side of things. So if we go back to our view options and switch to masks,
[24:05] let me grab this here. The add-on itself has this special thing called a texture logic node. And
[24:13] this is just a special node. You can actually add it in your shader graph in Blender. And then you
[24:20] would link up your material in your rig instance here. You basically just say, I'm using a, you
[24:26] know, this head shader is the one to look at. And then it'll look, it'll grab the texture logic
[24:31] node out of there. And then when you have animation, it will actually drive this. So let me pin this
[24:36] so this doesn't move. And we will import some animation. This is probably what 90% of people
[24:45] are going to want to do with this is make some motion capture, like a do a performance in
[24:52] metahuman AMA, and then pull that into Blender. So I'm going to just import this onto the face board.
[25:00] And so I'm going to play through this. So you can see those different maps evaluating on our,
[25:04] on our face. And then you can see that that's, all that really is, is these slider values going
[25:08] from one to zero on this. And this is just a special node that mixes your base with one,
[25:14] two, three variants on the color. And then your base normal with your 123 variants on the normal
[25:19] map. The actual material itself is not like, so if you're trying to render something in EV or
[25:26] cycles, you're trying to make final pixels and Blender, this is not really for that.
[25:32] You would use this node and you would shed, you would set up your graph to do that, basically.
[25:39] This is really about inspecting your, your textures and making sure that you got the right
[25:45] information on them. But like I said, if you're looking to make final pixels and Blender,
[25:51] just start out with this and you build out the rest of your, your shader graph to
[25:55] rendering whichever, or EV or cycles, whichever one you're targeting.
[26:02] With that, let's import some body animation.
[26:10] Let's go to the layout here. And I'm just going to play so you can see that we are,
[26:19] you know, we're just running in real time and you have your metahuman rig working exactly like it
[26:25] doesn't Blender. And this is that exact same animation you see in metahuman creator when you are,
[26:31] you know, doing, testing out the ROMs in metahuman creator.
[26:37] So that's pretty much it. That, I mean, that is the, the actual integration itself. This is an
[26:42] exporter as well. So you can export, you can import a DNA file and you can export a DNA file.
[26:48] So I'm just going to demonstrate that. So here I actually ran through this before and there's
[26:54] some information in that file. So I'm going to jump out here and I'm going to delete this just
[27:00] so you guys can see that I'm not cheating. This is the, so I guess the best way to illustrate
[27:12] this would just be if we modified her head. So I'm going to make sure this is active in edit mode.
[27:20] If we go in here, maybe I grab a vertices here, enable proportional editing,
[27:24] and let's just do something horrible like this. So obviously we changed the mesh. So I'm going to go
[27:33] ahead and kick off this export. And this might be a little overkill because what these metahuman
[27:41] creator export option does is it mimics the same thing that metahuman creator does if the DCC
[27:48] export. So you get your head DNA, you get your body DNA, and then you get your animated maps,
[27:53] which it pulls out of the inputs of the texture logic node. And it packages those up into that
[27:58] same folder structure with the same naming conventions. And the reason why I said it was
[28:03] overkill was because we only changed the head. But you can see here we exported our DNA. And then
[28:12] if we go to a new blender scene, and yeah, one thing, well, I'll show you here in a second,
[28:21] I'm going to re-import this. And then this time I'm going to enable all these LODs and click import.
[28:38] So we just round tripped the DNA, and you can see that our changes took as we exported it.
[28:47] The thing I was trying to point out was the update LODs option. This is the default option.
[28:52] So, yeah, so let me back up. So RigLogic actually has support for levels of detail,
[29:01] which you'll see a lot in game engines. But it handles that for you. And I don't know if people
[29:07] have seen the latest demos with metahuman crowds, and I think they had like a thousand
[29:11] metahumans on screen running at frame rate. But a lot of that works based on how optimized
[29:20] metahumans are and how they can go down to these lower levels of detail. So let me switch to wireframe.
[29:28] And I'll just kind of scroll through these so you can see the meshes themselves get
[29:35] less and less complex. And then actually at the RigLogic layer itself, it does some optimization.
[29:42] So it's not computing as much data when you're working at a certain LOD level.
[29:48] But the thing that I wanted to point out was that the R tool, basically you just do an edit on LOD
[29:54] zero, and it has an algorithm that will fix all your lower level meshes. So you don't have to
[30:01] you don't have to go in and edit those things manually, just edit LOD zero, and then it takes
[30:06] care of the rest for you. So what I'm actually going to do is we're kind of at the end of the
[30:14] first part, but I'm going to kick off this example. It's just because this takes about a minute.
[30:25] It's a little slow, but I'm going to click convert. So that is a metahuman working in
[30:34] Blender. Kind of what I was talking about before with unlocking various workflows.
[30:42] You know, you have metahuman animator, you can do it from mono video, you can do it from depth
[30:47] data, if you have a professional head-mounted camera setup, and then also the, let's see,
[30:54] where was it? On the other tab here, so we have a marker list motion capture,
[31:07] which, you know, you can see here, or here, all the things that you can do with that,
[31:22] and it's really simple to get those animations into Blender. This is, I think, almost done running,
[31:31] and I'm going to show you why I decided to do it this way. Basically, you feed it a base DNA,
[31:39] and then it has its own algorithmic runs, and it will template that DNA into the shape of your
[31:45] wrapped mesh. There's also a similar feature in metahuman creator, so we're going to take a look
[31:52] at that real quick. Open this up. So, what you would do is you go to this import option from
[32:05] template, and then you're going to get some options here for meshes. So, I'm going to feed it the
[32:14] same thing, so there is the head. I'm going to do the left eye. I'm going to do the right eye,
[32:24] teeth, and the body mesh.
[32:33] Yeah, and this could be partly due to my lack of knowledge of how to correctly use all the
[32:39] settings, but in my testing, this is the best result I was getting out of metahuman creator,
[32:46] and I will say it's called metahuman creator and not meta-8 creator, so that might be part of the
[32:51] issue, but it works really well with humanoid characters, but the issues here become a little
[32:59] more obvious with something like this. So, I'm going to create the full rig,
[33:03] and then I'm going to circle back to what I was showing there in the blender scene with converting
[33:15] the DNA, and we'll keep rolling from there. One thing I want to point out too is like,
[33:23] so see how the head actually moved up a little bit from the shoulders? So, that was also one of the
[33:28] issues I was having was I wanted to keep the exact proportions of the ape as the exact shape of the
[33:35] mesh that I wrapped, and so there's a little bit of, I think, some automatic calibration and stuff
[33:43] that's going on that works great on humans, but in this case is probably not what we want.
[33:51] Seeing some love and chat for the fact that you work on LOD zero and it auto
[34:01] does everything to all the other LODs. Awesome, yeah. No, I mean, yeah, it definitely saves
[34:08] you a lot of time if you're not having to edit like eight meshes, so what I did is I turned on
[34:15] the face wrong, and then this goes through the poses, and we can immediately see a lot of issues
[34:24] with the various expressions, and so even the eyes and everything, so keep that in mind. We're
[34:33] going back in here. The one thing about this converter that I like is it adheres exactly to
[34:45] how the mesh was wrapped, so I wrapped this ape with the mouth slightly open, and this is a common
[34:52] technique where you will, you know, you'll have your scan or your stult, and the mouth will be slightly
[34:57] open, and then the eyelids slightly closed, and then you can use that for baking like normals,
[35:02] color, and stuff, but what I use it for is vertex groups. So really when you have a rig that has,
[35:13] you know, I think it's around 800 bones, you probably don't want to have to weight paint
[35:18] all those bones, and so what you can do is you can do a 3D point transfer between your destination
[35:26] topology and your metahuman topology. Now I'm not going to demo this because this actually
[35:32] will break compatibility with metahuman creator, and we won't be able to go back once we do this,
[35:37] but it is something that I thought was worth calling now because that's why this mouth is open
[35:46] on this ape like this, and that is a technique you can use, especially if you're staying more
[35:50] on blender, or you can get it back into Unreal, but you can't pipe it through metahuman creator,
[35:56] you would have to use the option to import the skeletal mesh from the DNA file, which is also
[36:02] something that we'll show probably on our later tutorial here on our YouTube channel, but I'm
[36:09] just going to keep rolling with this, and this is going to be our first look at the raw editor,
[36:16] and it's called that because it's really for editing those primary raw controls that I was
[36:22] talking about on DNA, and those joint groups that are associated with the raw controls,
[36:30] so there's a default item, and then there is, that's the same way it is in the RBF, and that just
[36:36] is your bind pose, your rest pose, whatever you want to call it, and then you jump into an editing
[36:43] mode, and so you can see that you know that you're in an editing mode for one of these editors,
[36:48] and a lot of these editors all kind of have a similar concept of like editing, and then you
[36:52] revert or commit, so if I click this offset button, this is what's called my target mesh,
[37:02] and like I said, you know you're dealing with almost like 800 bones, so what you can do instead of
[37:09] manipulating all these bones, which you can, like you could come in here and just grab start, you
[37:14] know grab a bone, adjust it, and then commit that to DNA, but what I'm going to do is I'm going to
[37:20] use a feature that I'm about to demo here within the add-on, so I'm actually going to go to my
[37:25] few options, I'm going to solo the internal bones, so this just shows me what's the only internal
[37:31] bones to the head, so it makes it a little easier to navigate all those bones, and I grab the jaw
[37:36] bone, so let me go back to solid, I'm going to rotate the mouth closed, I'm going to grab it
[37:44] like this, now you may have noticed I just messed up the teeth, I moved the teeth, and I'm really
[37:49] just trying to close the lips over this, and I'll show you why I did that, so there is a tool for
[37:58] pasting over your selection, so this actually takes the deformed state of the geometry, and I
[38:03] just pasted it over onto my target mesh, and the teeth didn't move, it's just right there,
[38:09] so I can go back to some of these bone operations, I'm just going to revert the actual rig itself
[38:14] back to how it was, but this gives me a nice starting point for my sculpting, so I'm going to go in here
[38:21] and use maybe the inflate brush, and just close up the mouth here,
[38:28] and I'm not going to spend too much time on this, because it's really just to kind of
[38:36] illustrate the point I'm trying to make,
[38:43] yeah, you know, like something, maybe something like that,
[38:47] then what you can do is, like I said, this is all about moving the bones around,
[38:52] so I can run this bone matching operator, and it's going to look at this mesh, and then it's
[39:00] going to look at the bones, and it's going to do this computation, it's actually a hyper-ropped,
[39:05] so it's going to run through a thousand iterations of going, it's going to run through a thousand
[39:11] iterations of doing rotations, translations on all the bones across the face, and it's going to try
[39:18] to find the optimal position to where it can make this look like that, and so you can see it got
[39:23] very, very close, and so, you know, there's parts of the lips and stuff that don't exactly match,
[39:29] and one thing to note, I didn't do any changes to the weight painting or anything like that,
[39:35] but to take it the rest of the way, I'm going to go here, and I'm just going to click this option,
[39:40] which is paste vertices from the target mesh, now it is one-to-one, so I slightly altered the
[39:47] vertices on the rest pose of the character, so the rest pose is now fixed, I'm going to click
[39:54] commit, and then now it is updating the actual DNA file up until this point where we were just
[40:01] working with Blender scene data, and so now we will see the results of our changes as soon as it
[40:10] pops the spec out of the editor mode, so you can see this is the control that opens your jaw
[40:23] at zero, it is closed, so that is fixed, this is our starting point, there's still issues with it,
[40:32] you can see like that right there, but I will finally circle back to this right here, so this
[40:38] is what our first attempt was, now I'm going to remove this rig,
[40:50] and then this time I'm going to import from DNA, I'm going to choose replace option,
[40:55] and then I'm going to choose, let me see, maybe make sure I grab the right file,
[41:00] I will grab, this is that DNA that we just converted, so we've got the head, and let me put in the body,
[41:14] I'm going to apply this, so it's going to go and start putting in those bones,
[41:19] I mean it's going to pervade them, copy what is in the DNA, there's no
[41:23] automatic calibration stuff going on, it will just read that data directly,
[41:40] I think it's worth emphasizing here too that this is, it is right, this is a metahuman,
[41:48] so we're expecting very humanoid things like that, when you get to extreme bounds like this,
[41:53] there will obviously be things to fix that won't convert one to one perfectly, but these tools
[42:00] for fixing it seem extremely simple, so obviously the snout of an ape is like,
[42:07] that's not what a human's face looks like, so that's one of the first issues that we're seeing
[42:13] when you try to put human DNA onto an ape, so here is my current,
[42:20] this is where we're at with just that initial conversion, so it still has the issues,
[42:25] but I think this is maybe a little bit better of a starting point to go from than what we were
[42:30] working with before, and so this is what I'm going to roll with through the rest of the presentation,
[42:37] so I will jump to my next example file, I think this took me about like two and a half hours,
[42:48] kind of went through this the other night, I'm not a character artist, and I didn't look at any
[42:53] reference, what I was really doing was I was looking at the issues, like I saw where the teeth
[42:59] poking through different parts, and I was just fixing those things, so the expressiveness of it
[43:04] may not be exactly correct, but that was why I chose it, was because everyone can see there's
[43:12] issues that need to be fixed, and that's what we're going to do, we're going to go in and fix
[43:16] everything that we can see, so that's the first issue, the mouth side needs to be fixed,
[43:24] so I pre-sculpted these so you don't have to watch me do that,
[43:27] but what this will do is you get a raw control, so if we select that we say we want to edit that,
[43:40] so we're back in the raw control editor, but this is for a particular expression, and this is actually
[43:45] like, I'm going to show you here in a second what kind of what DNA looks like visually,
[43:51] but this is on that first layer of corrective expressions, but what I'm going to do is do the
[44:03] object select here, I'm going to do that offsetting again so we can see the target mesh,
[44:09] I'm going to use this paste from selection option, so do you see how I just fixed that,
[44:13] I'm going to trigger the hyperopt, it's going to run, and it just, you know, we don't have to fiddle
[44:19] with those bones, it doesn't get us there all the way, but that's what you can do on the shape key
[44:27] layer, so I'm going to go ahead and just commit this, like I said I didn't do any weight painting,
[44:35] so I'm going to try to correct as much of this as I can just with phone, moving some bones and
[44:42] editing the shape keys, so in the actual shape key editor,
[44:49] there is, there's some filtering options which I don't know if I explained that before,
[44:54] but I can disable viewing list items that do not have a value because there's, you know,
[45:02] hundreds of things in here, and so this is an easy way to navigate it, I know that this
[45:07] is activated, this shape key is activated when you have this control over here, so this is the one
[45:12] that needs to be edited, we're going here in the shape key editor, I will go also into object mode,
[45:22] you'll select this, and then we will just paste, so now it looks one to one, and the expression
[45:28] is fixed, so I will commit that, and then we will move the control the opposite way,
[45:40] so it's broken on the right side as well, same process, go in here, click this,
[45:48] offset that, select this one, paste that one, run the hyperopt,
[45:59] and we will edit this, and one last time we will paste
[46:19] shape key, so now that one is fixed, and I'll commit this, so that's about, I mean I'm not
[46:27] going to show you every single one, but you can see right away, this is actually looking a lot
[46:33] better just by fixing two of those poses, and it kind of has to do with, like I was saying,
[46:40] the snout of an ape, you know, being very different from humans, so it's going to be a little bit
[46:45] different, and the bones will need to be placed differently,
[46:49] from an artist's perspective, this is awesome, because in this instance, the thing that takes
[46:58] significantly the most work is the fun stuff, it's the creation of the model, and the character,
[47:03] and stuff like that, the actual fixing of the rig or adjusting the rig is a handful of button
[47:08] presses, and then I mean a fairly brief weight, I mean it was like what, maybe 10 seconds at most
[47:13] for most of those? Yeah, well yeah, and so actually that is a good point, is
[47:21] I keep running that hyperopt, and I wanted to explain that a little bit, so that is actually,
[47:28] it's a pie torch environment, but it is, it allows you to leverage your hardware, so you can use
[47:38] torch to leverage your hardware, so right now I have a 5090 in my machine, so I'm harnessing my GPU
[47:47] through the CUDA bindings, it also supports CPU, and CPU is actually really fast too,
[47:53] and then MPS on, if you're on macOS, you can also run this, but you do need to click the install,
[48:00] and this just installs a pie torch, and the dependencies into an environment, that's a
[48:06] one-time thing, and then that button will, that'll show, but yeah, I mean that saves a ton of time
[48:13] for artists where you can just have fun sculpting, and then most of this will take care of the kind
[48:20] of the technical side of things, and you just get to kind of play around, so with that actually
[48:30] I'm going to jump into the next example, and it's really not, isn't necessarily a feature of
[48:42] the add-on itself, but I did want to show a cool like blender feature, because I'm not a character
[48:49] artist, and I don't really know that much about sculpting, but there's this one feature I found
[48:54] that was pretty useful when doing a lot of this, because a lot of this has to do with stuff around
[48:59] the lips, and so if I go, if I go in here, do edit, what I did is I set up, set myself up some face
[49:08] sets, and I separated basically the upper, or I made a face set for the lower lip, and then there's
[49:15] this option here for auto masking by face sets, and so if I turn this off, and I pretty much have
[49:23] been using like one or two brushes the entire time, I don't, you know, these are just the ones
[49:30] that I found that kind of are working for me, but if I say want to fix this lip where the teeth
[49:36] are now touching the lip, I pull this, and you can see that I just pulled the upper lip, so that's
[49:43] not what you want, what this face sets option that auto masking does is, if you had that on, the first
[49:49] thing that you touch is what it's going to pull, so I can go here, and I can make these adjustments
[49:56] and pull the, you know, leverage some of Blender's awesome sculpting tools to get some of this done,
[50:05] so that's pretty much what I was going to show in that file, so you know, you commit that change
[50:12] for that particular pose, and then we're going to hop into a little more advanced
[50:27] example, and that's, we're going back to what I was saying before about the kind of the layers
[50:34] to DNA, so you want to start simple, you want to start at the raw controls, and then you start
[50:39] getting into a few more complex poses, and with every combination, there's a white paper that
[50:49] Epic released on RigLogic when they first came out with MetaHumans that I think is really
[50:55] interesting, but they're basically talking about how you, as you combine certain expressions,
[51:02] they're not going to linearly stack, can't literally stack them on top of each other,
[51:06] so for every combination, you have another corrective that brings maybe two together
[51:12] or several together, and we're going to see that here, and like I said, I'm not a character artist,
[51:22] but one thing that I've, a process that I've kind of like, try to follow is I saw something on the
[51:30] Epic documentation about with the scan reference poses, so they have what are called like MH12
[51:38] and then MH50 poses, and they say like when you're scanning that if you do the MH12, you capture,
[51:44] I think it was the essence of the character's expressions, and so you can see these poses here,
[51:50] so I'll go through and I'll just like, you know, toggle through these and see where I need to make
[51:56] the fixes, then the MH50, I think they said like this is where, if you calibrate all of these
[52:02] correctly to match your scans, then you actually have the, I think it's the likeness of the character,
[52:10] and so I kind of like just going through those, and then going through these and making sure they
[52:15] all look good, and when I was at this look down left pose, this is kind of our first example of
[52:23] where we have a little more complex, a little more complex evaluation of the corrective poses,
[52:34] so you have on your raw control, which these also have the bones and their associated shape keys,
[52:39] which we were showing before, you have a look down, and then you have a look left, but we do not have
[52:45] a down left, and this is where these other two shape keys come into play, and this is pretty easy
[52:55] to figure out when you're looking at something like this, but this gets a lot more complicated,
[53:01] the more complicated the expression is, so that's why we have this tool called the behavior graph,
[53:07] or behavior viewer, and what this does is it builds a graph, and if you remember at the very
[53:13] beginning of the slideshow I was talking about PSTs, those are post space deformations,
[53:19] and those are really these expressions that map together your correctives, so there's ones that
[53:27] are for the animated maps, but there's what we're really just going to focus on is the shape keys,
[53:32] so if we look at the actual equation here, this is just the product of these two values,
[53:38] so you multiply these two shape key values together, and then you get how this shape key value gets
[53:44] activated, so it's very obvious when you look at the graph that these are, this is the one I need
[53:51] to edit for this pose, because this is ultimately everything, all the dependencies evaluate down,
[53:56] and they get me to this pose on the left side, and this pose on the right side, so this is simple,
[54:01] I will show you a more complex one, but let's try that, so it was this I look left down pose,
[54:09] so I'm going to click that, and you can see that the add on actually backwards solves that graph
[54:17] that we were just looking at, and it says okay I need to activate the I look left blend shape,
[54:23] and the down, and then I also need to activate how those bones are transformed,
[54:26] and then that gets me to this pose, so all that to say this is the key we want to edit,
[54:32] so we click edit, go in here, and I will just fix the I, and I will commit, so that's kind of how
[54:44] you navigate, I tell you kind of how you navigate DNA, and the corrective expressions is kind of
[54:55] that's kind of at least my method for navigating those corrective expressions.
[55:02] I specifically enjoy the fact that the committing is a process, because that
[55:10] will make me feel more comfortable to just kind of get in there and start breaking stuff, if I
[55:13] know that like I'm not really breaking it until I press that button, which I think is really
[55:18] beneficial from an artist perspective. Yeah, no, so actually I'm really glad that you brought that
[55:24] because I forgot about this, so there is a there's another tool in here called the backup manager,
[55:32] and in your add-on preferences there's a policy, and I think the default value is five backups,
[55:37] but you can make a manual backup of your DNA, you know like I did well you know whatever,
[55:45] and you know it'll save a backup. The policy will not delete manual backups, but it does clean up
[55:51] automatic backups, and automatic backups happen before and after every commit, so the shape key
[56:00] commit that I just made, I can revert back to that state before I made the commit, I can then restore
[56:08] back to what I just committed, so that gives you a kind of a very non-destructive way, because you
[56:15] might get like you know you might get dozens of expressions deep in this, and you mess something
[56:21] up, because I'm going to show you here later how, I mean you could already seen that first graph how
[56:28] the expressions stack, but if you start modifying stuff at the beginning of that tree, and you've
[56:34] already done stuff at the end, you can have some unintended results, and so being able to roll back
[56:41] I think is a nice feature that you can utilize right there if that is a problem.
[56:48] Absolutely.
[56:53] Yeah, so the behavior viewer, let me just explain this a little bit more.
[57:04] I was kind of talking about like my I guess preference of like how I kind of go through
[57:09] and edit some of the poses or identify issues. I think what might be really tempting for people
[57:17] is to import, be like okay well you know I can see a metahuman creator that the face
[57:23] rom animation is messed up, I'm just going to import that animation and I'm going to start fixing my
[57:27] blend shapes, and that's I think kind of where you're going to you're going to run into issues,
[57:34] and so that's why I really recommend you go through, this comes from the actual rig definition,
[57:41] so these are target poses, and you'll notice if we have our shape key editor, see our shape keys,
[57:48] and our raw editor, you'll see that all of these activate at one for every single pose in here,
[57:56] so it goes through a bunch of these different poses, and what you would want to do is say
[58:03] fix your issues would be let's go through and find issues in these first, so you go through all
[58:12] the L1 poses that are free made for you here, and then what I did for this demo is I stopped there,
[58:19] I just did L1 and I didn't even do a very good job of making the expressions match what the
[58:29] expression is, like making the expression match what it's supposed to look like on a human,
[58:36] all I was doing was trying to fix stuff that's poking through the geometry, so I just looked for
[58:41] ones that had that, but that's layer one, you can filter your different layers, and I'm going to show
[58:49] you what layer six looks like, so it's got a pretty good amount of raw controls that are all
[58:58] activated in this single expression, and then we can take a look here, and these are all the shape
[59:06] keys that activate for this one pose, and so this can be pretty intimidating, especially when you're
[59:12] trying to figure out, okay, so what shape key am I supposed to edit, and that's where the behavior
[59:18] viewer is really going to be beneficial, so we go in here and we graph this, you can see that, okay,
[59:28] this is obvious, I just need to make the fix here on the left side and the right side,
[59:35] that is correct, but you kind of want to make sure that you're done with these, you know what I mean,
[59:44] because if you change anything down here, you can have an unintended result on your final shape
[59:51] key, so this will be the ultimate shape key where you make your fix, but all of these are
[59:56] deltas, they're not set poses, these are the shape keys are defined as deltas, and I guess one thing
[60:08] on the subject of deltas, you'll notice these little ghost icons that are appearing on these,
[60:15] so when I run that converter, it actually zeros out all of your shape keys, so what the ghost icon
[60:23] means is there are zero deltas on the shape key, so this shape key is equivalent to the basis shape
[60:29] key, there is no difference, so this can be helpful, sometimes you'll go through and you'll edit some
[60:37] shape keys and you're like, which one did I edit, which one actually has values, which one doesn't
[60:40] even matter, because if I freeze this, and what freezing is it, it's like a nice little tool
[60:48] where it keeps the items from moving, so I'm moving this, it does nothing, because there's
[60:55] nothing on the blend shape, this one, I might need to zoom in, this one actually does,
[61:06] and then this is what I meant by freezing, this sorts by what has a value, so like my
[61:12] shape key just disappeared there, so if you don't want that to happen, you can use the freezing option,
[61:19] all right, so we are basically getting to the end of it, make sure I open the right file,
[61:27] here is, like this is after me spending about two hours the other night trying to calibrate this,
[61:35] I got past all the L1s and then I loaded in the face ROM just to see how it's looking,
[61:41] and I wasn't seeing any geometry poking through, you know, obviously there's some,
[61:47] there's still some things that are not to be desired, but you could, with more time,
[61:54] you could go through and you could fix those, and like I said, I was only at the first
[61:59] layer of corrections, but we go back into the human creator here, so we have our
[62:07] chimp with our problems, I am going to remove the rig one more time,
[62:15] ROMDNA replace, I already exported this to something called, to a folder called final,
[62:26] and then do that exact same thing, we're going to import
[62:31] ROMDNA, we're replacing it, we don't want any kind of automatic
[62:37] calibration or anything going on in the human creator, we want to pull our data in exactly as
[62:41] we said it in our, in Blunder. Yeah, a lot, a lot of love for this, these tools in chat,
[62:54] and I'm one of them, this is awesome. That's great to hear, yeah, I mean,
[63:02] that was the goal, right, you know, was take a process that's honestly kind of nebulous,
[63:07] you know, because it's a different file format, unless you do a lot of scripting in Python,
[63:15] or you're using Maya, which Epic's got some really awesome tools to do something very similar
[63:22] in Maya, but if you're in Blunder, you don't really have any options, so
[63:29] this now gives people the option to do some of this advanced, you know, calibration,
[63:35] and you can see here, we scrub through, I'm not seeing any issues anymore on the
[63:42] on the ape, and then kind of as the final part of this, I made a little level,
[63:52] I'm going to open up, I'm going to not save that, open up this level sequence, and I loaded the
[63:58] face ROM again onto both of these characters, and we can watch here, let's go to a part where he
[64:11] moves like his mouth, so here, right, that's where we started from, this is where we're at now,
[64:20] so, you know, we fixed those issues with the mouth, there's also like, I think there's a part
[64:24] here where, yeah, like see the teeth are poking through on the front there, and this kind of
[64:28] lip bite, so he's doing the lip bite pose, let's try to find a part where he closes his eyes,
[64:41] so, people can see that, so see how the eyeballs are poking through, and the eyelids are actually
[64:49] not even closing fully, we go back here, the eyes are closing fully, the eyeballs are not poking
[64:56] through the machine, so, I mean, I think, I mean, your results will vary based on how
[65:06] much time and effort you put into calibrating, but this kind of unlocks that for you, that you can,
[65:14] you can actually edit that stuff now with these tools, so that is pretty much the demo, so,
[65:22] we can, I guess, go into questions, if you have any, Dan?
[65:28] Yeah, yeah, no, we've gotten quite a few, and I'll actually use this as another opportunity for
[65:34] folks, if you have any questions for James here, please leave them in the chat, put question in
[65:40] brackets, followed by your question, and we will throw as many of those to him as we can,
[65:47] first question, coming from a couple different folks here, and that is, what version of Blender
[65:53] does this plugin require? So, we have support from the last two LTSs, and actually, the most recent
[66:03] LTS came out last week, so that is updated, and you can use Blender 5.2 all the way back to
[66:11] 4.5. Awesome, awesome. Another question we have, at least half answered, but I wanted to throw this
[66:20] at you anyways, which is, will this transfer the body rig as well, which it appears, yes, it does,
[66:26] but also, what about RBF support on the free version? So, the RBFs do evaluate on the free
[66:37] version, so that you will get the one-to-one body rig in the free version. The thing that is not in
[66:44] the free version is the RBF editor, so you can't change the RBFs in the DNA, but your rig will
[66:53] function exactly like it does in Unreal with the RBFs on the body in the free version, so if
[66:59] you're using this for more of like an animation workflow, you pretty much have everything you
[67:03] need. There is another add-on that we have just started working on called Character Control Rig
[67:10] add-on. This is a paid one, but it's got a bunch of animator tools, and it's got a full control rig,
[67:17] so you've got your IK controls. We have a pre-made Rigify template, but we're also going to add
[67:24] support for AutoRig Pro, so some popular rigging frameworks that a lot of Blender users like to use.
[67:30] Awesome. Awesome. Are there any considerations or use cases for this pipeline for hair or grooms
[67:42] for characters? Yeah, so DNA itself does not contain hair. You can get hair, or you can get
[67:53] grooms out of Unreal by exporting as an Olympic, and I don't think you can actually do that out of
[67:59] the box. There are some third-party plugins that allow you to export Olympics from Unreal.
[68:07] Blender can import Olympics out of the box, so that's how you would get the actual grooms out
[68:14] and into Blender. If that's something that people are struggling with or are interested in,
[68:21] I would recommend leaving us a comment on our GitHub discussions, because we want to help support
[68:29] these character workflows in any ways we can. But if there's interest in that, then that's
[68:32] definitely something we could maybe streamline. But yeah, you just have to export as Olympic.
[68:38] You can't export grooms into DNA. Okay. Another question we had, which might not be in the scope
[68:48] of this, but I'll throw it at you anyways, is how can I use this to rig extra things to a character,
[68:55] like attach clothes to them in Blender? Is there a section for that in the plugin, or should that
[68:58] be done manually or with another tool? Yeah, so for the clothes, those are actually also not in DNA,
[69:07] but they are. When you assemble a metahuman character, and actually, if you give me a second,
[69:16] well, let me make sure I haven't assembled. Sure. Well, I do not. If I ran the assembly,
[69:22] it probably takes a minute or so. But my main answer would be that if you run assembly
[69:30] for your Unreal Engine project from Metahuman Creator, it takes your clothes and puts those
[69:35] into skeletal mesh assets in a content folder in your project. You can right click on those,
[69:42] and you can export those as FBX for sure. And I think probably there's support for other
[69:49] file formats, but you can pull those out as an FBX. Once you have the FBX, the FBX still should
[69:54] have those vertex groups on it. So you should be able to just put that in Blender, and then
[70:00] you would just assign the armature modifier from the rig that you have from the DNA add-on
[70:07] to your clothes, and it should scan immediately from that. You just need to make sure you fix
[70:12] the scale and everything and put it on the character. Right. Another question we had here is,
[70:20] why is it necessary to do the hyper op and then the second copy? Can't you just do the second copy?
[70:30] Yeah, so you actually could do everything with Metahumans with just Blundshakes.
[70:38] The thing about Metahumans is they are designed to go down in levels of detail. So only on
[70:48] LOD 0 are shape keys visible, and then once you get to LOD 1, you're dealing with the rig.
[70:55] So, you know, in Blender, you might be able to do that, but in a game, after you get a
[71:03] certain distance from your character, you're going to lose all those Blund shapes, and especially with
[71:07] something like an ape, your snout might be poking through and stuff, because all it's working with
[71:14] at that point are bones. And then if you wanted to do just shape keys, you would also need to make
[71:22] sure that your bones honestly aren't affecting the face at all. So you're going to have unintended
[71:30] consequences of the bones move here. I adjust the shape key. The bones can still move around,
[71:36] so you would basically want to take the bones kind of out of the picture if you wanted to do
[71:41] just shape keys. So that's why I recommend, you know, you do it, you match the bones, you get
[71:46] those as close as you can, then you do the little correction with the shape key.
[71:54] Another question we had here was, what is the process of wrapping the custom mesh to the
[72:02] metahuman rigs? How to approach that? So what I used for the ape was a program called Faceform
[72:11] Wrap, which I showed earlier, and it's a very powerful piece of software, and you can kind of
[72:18] arbitrarily wrap any kind of mesh. Metahuman Creator in 5.8, they actually do have a mesh
[72:27] wrapping feature, which I was going to demo as part of this presentation. And it has a really
[72:36] cool feature for auto solving. So if you have a humanoid character, you can throw in anything.
[72:43] Maybe you used one of these AI models to generate some humanoid looking character,
[72:48] you can throw it in. The topology is not at all metahuman topology, and it will magically
[72:54] match to it, and it does a really good job. You could do that for humans. I messed with it,
[73:01] because they also have these control points. And at least in the time constraint that I had,
[73:08] I was not able to get the results that I wanted. And also, I'm just more familiar with Wrap,
[73:14] so that's what I used, was Wrap. But both of those are options, and depending on how extreme it is,
[73:22] you might be able to do the whole thing with Metahuman Creator.
[73:27] Alongside that, another question we had here is, given that we've kind of shown that with these
[73:33] tools, we can kind of move a bit beyond your typical humanoid character here, in your opinion,
[73:40] would these tools be capable or good for doing something like moving the ears towards the top
[73:47] of the head? Or is it still try to keep it relatively in the position that you would expect?
[73:54] How versatile is that in your experience? Yes, you can do...
[74:01] Like I was kind of alluding to before, when I was talking about the mouth open, and then like
[74:07] closing it, as opposed to just having the mouth closed when I did that first convert, is the
[74:16] topology can be arbitrary if you do not want to go back through Metahuman Creator. The assembly
[74:22] gets a little more complicated on the Unreal side once you break compatibility with the Mesh
[74:28] topology. But there is a thing in the latest update of Unreal, where you'll now see that DNA
[74:36] actually displays as a U-Asset. And you can right click on that, and you can say, create Skeletal
[74:42] Mesh from DNA. And then it just populates the Skeletal Mesh with all the length of your morph
[74:48] targets on it. So you can kind of even use DNA just as like a file format, like you do with other
[74:56] file formats now in 5.8. But that's probably the route you would have to go, is like say we wanted
[75:04] to get rid of the ears, and there is a horn on the head. I mean, I guess for me, let's say there
[75:10] was an ear on the head, because that actually would maybe move. You could modify the rest position
[75:16] of the bones. I haven't done anything where I remove bones from the rig, but I have done stuff
[75:27] where I have custom meshes, and I use bones for various different things. But you could move the
[75:32] ear bones to the top of the head. You could have your custom mesh. As long as you transfer those
[75:37] vertex groups, it's skinned, the bones move, and you can repurpose it for that. Now, like you saw
[75:47] in that graph, all those shape keys, all the wiring, so to speak, is what makes metahumans work so well.
[75:57] So if you're going to kind of go down your own path of assembling those, that's not going to be
[76:05] a good easy thing. And you might be better off just trying to use those as kind of a convention
[76:14] and work that into your rig, especially. I think the real advantage to a metahuman rig is if you're
[76:20] doing speech and motion capture. I think that's really what you're trying to leverage. If your
[76:25] character is like that, then a metahuman rig might be something that you can repurpose for that.
[76:31] If you have some monster character that doesn't talk or something, you might just want to make
[76:35] your own rig. If that makes sense. Yeah. It feels like one of those things where it's almost like
[76:41] get in there and try it. See if you can make it work for your use case. It might be within
[76:47] the parameters that it is relatively simple and straightforward to do, but otherwise it might
[76:51] need something a little more custom. Yeah. And I've just been playing with this for a little bit.
[76:59] I'm just telling you what I've come into, but yeah, I've seen all kinds of crazy things that
[77:04] people have been able to do online. So yeah, like you're saying, play with it. Let me know.
[77:11] Maybe you can. Yeah. Out of the box sort of things might not have as much utility when you get to
[77:18] those more extremes, but it seems like a very versatile tool if you're willing to put the time
[77:24] into it. You could probably make some pretty custom things. Yeah, for sure. One of the other
[77:31] questions we had here, we're actually getting towards the end of the question. So if anybody
[77:34] else has any more, please put them in chat real quick. But someone said, I may have missed the
[77:40] start, but can you save out all the expressions or shapes to a grid in Blender scene to see them
[77:47] all and then batch import them, import the fixed shapes back? So basically like an asset zoo for
[77:54] the shapes, essentially. Yeah. Yeah, I mean, that could be a good feature that we add. And that's
[78:02] kind of why I was mentioning our GitHub discussions. So sometimes we'll have people that will just
[78:07] pop into those discussions and they'll say, you know, it'd be cool as if it did this. And so you
[78:14] can go in to the character DNA GitHub discussion and you could create an issue or a feature request.
[78:22] And that might be something that we should add, because I could see how, you know, that would be
[78:27] very beneficial and a big time saver for people, especially if you are trying to kind of do what
[78:35] I showed at the beginning part where I had that kind of like you were saying asset zoo of expressions
[78:40] pre-made, then yeah, that could be very useful. So I would say fill out a feature request and
[78:51] that's probably something we'll be adding here.
[78:56] Yeah. No, sorry. I laughed. The question we got here is where does Dan keep kidnapping these
[79:00] incredible guests? Because we keep getting great lectures because of it. That just made me laugh.
[79:04] They're out. So they're out there. They're great people. And these resources are also available
[79:09] to you. Please follow Polyhammer not only on their YouTube, but GitHub and everything else because
[79:16] they're out there and they have these really cool tools for you. So well, with that, James,
[79:22] thank you so much for taking the time to not only put this tool together, but then also come and
[79:28] join us to show it off and talk about it. Really positive feedback. I'm one of them. I think this
[79:35] is awesome. I think this is great. There's been many instances where I've wanted something just
[79:39] like this over the past year. And now I get it. So I know exactly what I'm going to do this weekend,
[79:45] which is going to be getting this on my own PC and starting to play around with it. So
[79:50] really appreciate you taking the time to come and join us. Yeah, no. I will say on that note too
[79:57] for people. Like James was saying, follow us. But also grab the free add-on and try it out.
[80:06] Joining on the discussions on our GitHub, like we got some great feedback today on what might be
[80:11] a great feature that we can add to the tools. And then help us hard in the beta because this is
[80:18] actually we're in the very late stages of beta for this and we're about to switch to version one
[80:25] and kind of lock in all of our features. So if there's any bugs, anything like that, you can
[80:32] report those. And then last thing I would say is support our future development. So
[80:37] we there's this free add-on, but the way that we fund ourselves is through our paid add-ons. So we
[80:44] actually have two different paid add-ons. And if you like what you're seeing here, then I would
[80:49] encourage you to just support us. And all that money goes towards funding development that goes
[80:55] towards more features and more cool stuff for you guys. All of our stuff is a one-time purchase.
[81:01] So you get full source code. They're very affordable. And you could modify them to
[81:07] whatever you want, lifetime updates. So check it out. Awesome. Awesome. Well, that is going to wrap
[81:17] up today's session of Inside Unreal. Again, a huge thank you to our guest and a huge thank you to
[81:24] everyone out there for watching as well. If you haven't checked it out yet and maybe you joined
[81:29] the show in the middle, our epic, sorry, the Fab Summer Mega Sale is currently live. So please
[81:36] go and check that out. We have tons of items up to 70% off that range the whole gamut from
[81:43] materials, templates, assets, all that sort of stuff. So please check that out. You have until
[81:48] 11.59 p.m. Eastern on July 29th to dive in. So go and get yourself a deal for anybody that came
[81:58] through the show partway through. Do not worry. We have all of our videos on VOD format that you
[82:04] can view at our channels on Twitch and YouTube at Unreal Engine. And we also have also cool social
[82:12] things that you can view on all of our different socials at Unreal Engine as well. And you can
[82:21] also keep up with other awesome updates on the EDC. We have our forums, documentation, tutorials
[82:29] from both community, Epic Staff alike, and so much more over there. So please check that out as well.
[82:34] But again, huge shout out to you, James, for taking the time to do this. And we will see you folks more
[82:42] next week. Bye, everybody.



---

## Captured Frames

- [18:40] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_000.jpg
- [19:30] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_001.jpg
- [20:05] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_002.jpg
- [21:40] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_003.jpg
- [22:55] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_004.jpg
- [24:40] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_005.jpg
- [29:30] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_006.jpg
- [32:20] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_007.jpg
- [37:50] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_008.jpg
- [39:10] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_009.jpg
- [45:10] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_010.jpg
- [49:45] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_011.jpg
- [53:40] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_012.jpg
- [58:00] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_013.jpg
- [64:45] tutorials/frames/metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea/frame_014.jpg

---

## Structured Notes

### Core Technique
Running the full MetaHuman rig natively in Blender via Polyhammer's free Character DNA add-on (built on Epic's OpenRigLogic C++/Python runtime released at Unreal Fest), then customizing the DNA's behavior — bones, shape keys, correctives (PSDs), wrinkle maps — entirely in Blender with the add-on's pro editors (Raw Editor, Shape Key Editor, Behavior Viewer, hyperopt bone matching), replacing the traditional Maya Expression Editor pipeline. Demonstrated by converting human MetaHuman DNA onto a wrapped ape mesh and calibrating its facial rig.

### Summary
Inside Unreal stream with James Baeber (3D tools engineer, Polyhammer). DNA is Epic's proprietary format holding meshes, joints (bones), blend shapes (shape keys), plus a behavior layer: GUI controls → raw controls feeding the RigLogic runtime, PSDs (pose-space deformations / corrective expressions), RBFs (radial-basis interpolation driving corrective bones, mainly body/neck), and animated maps (mask values that blend 3 wrinkle color/normal variants over the base textures at the material level). RigLogic is application-agnostic — it runs in UE, Maya, Houdini, and now Blender. Part 1: import MetaHuman Creator's DCC export (head DNA + body DNA + maps folder) by drag-dropping the .dna into the viewport; you get a 1:1 working rig with face board, poses/visemes/emotions, wrinkle-map debugging views, per-instance/component/output toggles (bones, shape keys, wrinkle maps, RBFs), RigLogic-managed LODs (edit LOD 0, an algorithm fixes all lower LODs), the Texture Logic shader node (inspection, not final rendering — build your Eevee/Cycles graph from it), MetaHuman Animator / audio-based / markerless (UE 5.8) mocap imported straight onto the face board, and DNA round-trip export mimicking MetaHuman Creator's folder/naming conventions. Part 2: an ape (wrapped in Faceform Wrap with mouth ajar) exposes what MetaHuman Creator's own mesh-template import gets wrong; the add-on's converter instead templates DNA to the wrapped mesh verbatim. Calibration workflow: Raw Editor (edit raw controls + joint groups against an offset "target mesh"; paste deformed geometry over selection; sculpt; then a PyTorch "hyperopt" bone-matching operator — ~1000 iterations, CUDA/CPU/MPS, updated 192 bones in 3.7s — followed by paste-vertices for the residual and commit-to-DNA), Shape Key Editor (filter to non-zero keys; ghost icon = zero deltas; freeze sorting), Behavior Viewer (graphs PSD dependency trees — e.g. eye_lookDown_L × eye_lookLeft_L multiply into the lookDownLeft corrective — so you know which terminal shape key to edit and to fix upstream L1 poses first), rig-definition target poses (work through L1 before higher layers; MH12/MH50 scan-pose sets capture "essence"/"likeness"), and a Backup Manager (auto backup before/after every commit; manual backups exempt from the retention policy). Result: the fixed ape DNA re-imports into MetaHuman Creator (replace, no auto-calibration) with eyes closing and teeth no longer poking through. Q&A: free version evaluates RBFs but the RBF *editor* is pro; grooms aren't in DNA (export Alembic); clothes come from MetaHuman assembly as FBX and bind via the armature modifier + existing vertex groups; bones-first-then-shape-keys matters because shape keys exist only at LOD 0; UE 5.8 can create a Skeletal Mesh directly from a DNA asset once topology compatibility is broken.

### Key Steps
1. **Export from MetaHuman Creator**: Export tab → DCC export → file path. Output: `head.dna`, `body.dna`, and a maps folder (neutral + 3 wrinkle-map variants for color and normals, plus region masks).
2. **Import into Blender**: File → Import → MetaHuman (.dna), or drag-drop the head DNA onto the viewport → dialog with *Include Body* (default on), LOD checkboxes, mesh/bones/vertex-group/material/face-board data toggles → Import. Face board controls (jaw, mouth, eyes) behave exactly as in UE.
3. **Explore the Character DNA tab**: Face Board panel — eye-aim toggle, pose library (visemes, emotions — useful to learn control→face mapping or overlay emotion on mocap), wrinkle-map poses (3 poses driving each map to max; mask view for debugging/scan extraction).
4. **Rig Instances panel** (scene data block persisting in the .blend): head + body components, each with its own RigLogic instance reading its DNA file; enable/disable per instance, per component, or per output (bones / shape keys / wrinkle maps / RBFs).
5. **RBF demo**: yellow driver bones (e.g. arm) feed rotations into radial basis functions that pose corrective bones; with RBFs off the shoulder pinches and loses volume, on it holds — correctives are statically authored at key poses (e.g. clavicle) with a falloff/interpolation function.
6. **Texture Logic node**: add in the shader graph, link the material in the rig instance; animation then drives the three variant mixes over base color/normal. For final Eevee/Cycles renders, use it as the starting point of your own graph — it's for inspection, not final pixels.
7. **Animation**: import MetaHuman Animator performances onto the face board (iPhone, audio-driven, HMC depth, or UE 5.8 markerless full-body from single video); body animation plays back in real time.
8. **LODs**: RigLogic natively handles LODs (and computes less at lower LODs — how MetaHuman crowds scale); edit LOD 0 only, the add-on algorithmically propagates to all lower LOD meshes.
9. **DNA export round-trip**: mesh edits (e.g. proportional-edit the head) export back to head/body DNA + maps in MetaHuman Creator's exact folder structure/naming; re-import to verify.
10. **Custom character (ape)**: wrap your sculpt/scan to MetaHuman topology in Faceform Wrap (or MetaHuman Creator 5.8's mesh import with auto-solve — great for humanoids, poor for an ape; it also auto-calibrates proportions you may not want). Wrap with mouth slightly open/eyelids nearly closed — usable for baking and for 3D point transfer of vertex groups (skips weight-painting ~800 bones, but breaks MetaHuman Creator compatibility; then use UE's create-Skeletal-Mesh-from-DNA instead).
11. **Converter**: feed a base DNA; it templates the DNA into your wrapped mesh's shape verbatim (no auto-calibration), ~1 min. Better starting point than MetaHuman Creator's import for non-humans.
12. **Raw Editor loop** (per broken pose): select raw control → Edit → Offset shows the target mesh copy → close the jaw via the (soloed) internal bones or paste-over-selection from deformed state → sculpt fixes (inflate brush etc.) → **Match Bones to Mesh** hyperopt (PyTorch env, one-time Install; CUDA/CPU/MPS; ~1000 iterations of bone rotations/translations; "updated 192 bones in 3.70s") → **Paste vertices from target mesh** for the 1:1 residual → Commit (writes the DNA; until commit you're only touching Blender scene data).
13. **Shape Key Editor**: filter out zero-value items; the pose's active key is the one to edit; Edit → paste → Commit; repeat mirrored controls. Ghost icon = zero deltas (converter zeroes all shape keys); Freeze keeps list order stable while values change.
14. **Sculpt helper**: Face Sets for upper/lower lip + *Auto-Masking by Face Sets* — first surface touched is the only one pulled, so lips can be adjusted without grabbing the opposing lip.
15. **Correctives / PSDs**: combined expressions don't stack linearly; every combination has a corrective (see Epic's RigLogic white paper). **Behavior Viewer** graphs the dependency tree (e.g. `eye_lookDown_L × eye_lookLeft_L → lookDownLeft_L`, product of input values = activation); fix upstream (L1) poses before terminal correctives since terminal keys are deltas on everything below.
16. **Calibration order**: use the rig definition's target poses (every listed raw control at 1.0), layer by layer — L1 first, then higher layers (L6 shown activating many controls at once); MH12 poses ≈ expression essence, MH50 ≈ likeness. Don't calibrate by scrubbing an imported face-ROM animation.
17. **Backup Manager**: automatic backups before/after every commit (default policy keeps 5; manual backups never auto-deleted); revert/restore any commit — work non-destructively dozens of expressions deep.
18. **Re-import to MetaHuman Creator**: remove rig → import from DNA (Replace, no auto-calibration) → verify with the face ROM; final UE level sequence shows before/after apes side by side (lip bite fixed, eyes close fully).

### Nodes / Settings
- **Polyhammer Character DNA add-on** (free, late beta): drag-drop .dna import (Include Body, LOD selection), Face Board + pose library, View Options (mask/combined view, solo internal bones, bone visibility), Rig Instances (head/body components, per-output toggles), Converter (DNA → wrapped mesh), Mesh Editor, **Raw Editor** (edit/revert/commit, offset target mesh, paste over selection, paste vertices from target, Match Bones to Mesh hyperopt with PyTorch install — CUDA/CPU/MPS), **Shape Key Editor** (filter by mesh/value, ghost = zero deltas, freeze, isolate dependency chain), **RBF Editor** (pro), **Behavior Viewer** (PSD graph; target poses per layer L1–L6+; show animated maps/RBFs), **Backup Manager** (auto pre/post-commit, manual, retention policy), Output/exporter (MetaHuman Creator folder conventions), **Texture Logic** shader node.
- **Pro vs free**: free = full 1:1 rig incl. RBF evaluation, import/export, animation; pro = DNA behavior editors (raw/shape key/RBF editing). Separate paid "Character Control Rig" add-on (IK controls, Rigify template, AutoRig Pro support planned). One-time purchase, full source, lifetime updates.
- **DNA format**: meshes, joints, blend shapes, GUI→raw controls, PSDs, RBFs, animated maps; head DNA + body DNA from MetaHuman Creator DCC export.
- **Blender techniques**: proportional editing, sculpt inflate brush, Face Sets + auto-masking by face sets, armature modifier for FBX clothes (vertex groups preserved), Alembic import for grooms.
- **UE 5.8 tie-ins**: markerless mocap, MetaHuman Creator mesh import auto-solve, DNA as U-Asset → right-click Create Skeletal Mesh from DNA.

### Difficulty
Advanced

### Blender Version
Blender 5.2 LTS shown; add-on supports Blender 4.5–5.2 (last two LTS releases). Unreal Engine 5.8 features referenced.

### Tags
metahuman, riglogic, dna, facial-rig, rigging, shape-keys, animation, mocap, add-on, unreal-engine, blender-5x, advanced

---

## Related Tutorials
- [Easy Rigging Using RIGIFY in Blender](easy-rigging-using-rigify-in-blender.md) — Blender's native auto-rigging alternative; the paid Character Control Rig add-on mentioned here ships a Rigify template for MetaHumans
- [Blender 5.1's NEW Rigging Tool is INSANE!](blender-51s-new-rigging-tool-is-insane.md) — armature/bone tooling in recent Blender releases
