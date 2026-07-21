---
title: Forgotten Metal Knowledge | Vray, Cycles, Arnold..
source: YouTube
url: https://www.youtube.com/watch?v=uz8PIi3ELJg
author: Lucas
ingested: 2026-07-20
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/forgotten-metal-knowledge-vray-cycles-arnold/
frame_count: 0
frame_status: pending-selection
---

# Forgotten Metal Knowledge | Vray, Cycles, Arnold..

**Source:** [YouTube](https://www.youtube.com/watch?v=uz8PIi3ELJg)
**Author:** Lucas
**Duration:** 30m21s | 13 section(s)

---

## Raw Data (for Claude Code extraction)


Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py forgotten-metal-knowledge-vray-cycles-arnold <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Today we're gonna take lessons from 2008 Iron Man and see how seemingly common in master materials still have a lot of secrets to share.
[0:07] Let me introduce to you Reflection Tape Off.
[0:15] So a while ago I was rewatching Iron Man and something in the mark 2 suit up scene code my eye.
[0:21] I posed and I looked closer to make sure I wasn't hallucinating and there it was, a dual reflection.
[0:26] I thought that was bizarre, why would there be two reflections?
[0:30] Usually you have a single roughness value or a roughness map and that's it.
[0:33] Now the mark 2 and mark 3 suits do have some fingerprints that create extra specular layers, but that wasn't the case here.
[0:40] Both visually and narratively this was pretty clean and brand new metal.
[0:44] Knowing I&M's reputation I figured they had to be right and that I was missing something about how real metal behaves.
[0:50] So I did some digging and I found a photo of the practical suit used in that same sequence and I was stunned.
[0:56] The dual reflection was there too.
[0:58] It was hard to spot because the physical suits finish is quite brushed.
[1:02] But when you zoom into the cleaner area you can clearly see a sharp distinct core reflection paired with a soft faded fall off.
[1:08] I wanna be absolutely clear about what I'm talking about here.
[1:11] I'm specifically interested in those seemingly secondary reflection added on top of the main one.
[1:16] You can clearly see that what is being reflected remains pretty sharp and yet you can also see that there's a huge tail off that goes way beyond the initial reflection.
[1:24] Where the colors of the subject are dark, the surrounding reflection is bleeding on top of the first one and darkening the surroundings.
[1:31] And when what's being reflected is bright, it's almost like it's glowing.
[1:35] And this is reflection tail off.
[1:37] Now if the sound of multiple reflections onto a metal shader don't sound completely bogus to you, let's look at the standard metal shader.
[1:44] You set the metalness to 1, you choose a roughness value or plug in a roughness map and let's get a little crazy and add some anisotropy as well.
[1:51] Despite all that, you still can't quite replicate the effect I'll limit sheet on Iron Man.
[1:56] No matter how you tweak your roughness value, you're only ever changing the blurriness of a single reflection.
[2:01] So at that point, I decided to look into it and I needed to do three things.
[2:05] First, I need to find reference.
[2:07] I needed to know if this was a 1 in a million anomaly because after all the practical suit I'll am recreated was made from a complex alloy and created specially for the movie.
[2:16] Secondly, I need to find information.
[2:18] I wanted to uncover what exactly happened during the production of Iron Man that I hadn't seen or heard of since.
[2:24] And thirdly, I need to find an explanation.
[2:26] Even if I could figure out how they replicated it in CG, I'd still need to understand the why, the actual physics behind why real metal behaves this way.
[2:35] So, I got to work.


### Finding References [2:37]
**Transcript (timestamped):**
[2:37] That one was pretty easy.
[2:39] Once you know what you're looking for, you see it everywhere.
[2:42] Have you ever looked at an elevator and thought, this reflection is really weird? What's going on?
[2:46] No? Oh, well, I have.
[2:48] And I don't know how I missed it until now.
[2:50] I think I might even have encountered it before without realizing.
[2:53] Back in my first year of school, I modeled a delirium and I couldn't figure out the roughness for the life of me.
[2:59] In one reference photo, it looked like 0.2 and in the next, 0.4.
[3:03] I couldn't point my finger on it.
[3:05] And it turns out that was exactly this phenomenon.
[3:07] And really, this double reflection effect is everywhere except on YouTube, in schools, discord, forums, or station.
[3:14] Even professionally, I've never really heard anyone mention this thing.
[3:17] There's actually only three types of reference I found that didn't display this at all.
[3:21] Extremely polished metal, extremely rough metal, and extremely rare uniform metal, but we'll get back to this one later.
[3:28] So, I went online and watched videos of metal working and other manufacturing stuff.
[3:32] And I noticed that lots of these do have these multi-reflections.
[3:36] And that right before these surfaces would show the multiple reflections,
[3:39] they'd first go through an intermediary scratch state where you could visibly see micro-scratches spreading the reflection.
[3:45] So, my first thought was that maybe there are millions of consistent micro-scratches below our visual acuity scattering the highlights,
[3:52] which, among them, gave the impression of a faint fall-off.
[3:55] So, I ran some tests, opened Macs, I met a metallic sphere, and I put a scratch map sized 1 cm and rendered.
[4:02] Hmm, it just looks like regular roughness.
[4:05] But wait, there is a setting in charge of controlling how much detail are preserved within one pixel of the render.
[4:12] That would be mip-mapping or filtering, depending on how you call it.
[4:15] So, I went into the settings, I turned it off, and I found that was exactly like the reference.
[4:20] Now, I had my main reflection, and I would have a huge fall-off that was exactly what I was looking for.
[4:27] And this is actually so common that I searched for it in real life,
[4:30] and I found a bunch of examples with zero struggle.
[4:33] In my elevator to-door where you see me both sharp and blurry,
[4:36] a fridge where the room's light glows way past the reflection,
[4:40] and even more interestingly, I came across this cooking pot lid while doing the dishes, and I thought,
[4:45] what the fuck is that?
[4:46] This is way more complex than every other example I could find.
[4:49] You've got everything on there, you've got scratches, anti-saltrapee, two reflections.
[4:53] There's clearly more to it than just a scratch layer.


### Finding Information [4:57]
**Transcript (timestamped):**
[4:57] Uncovering information about ILAM's specific approach was not an easy task at all.
[5:02] There really isn't much on the subject.
[5:04] One permissing resource was a SIGGRAPH 2010 paper,
[5:07] written by legendary VFX supervisor Ben Snow,
[5:10] who oversaw the creation and, crucially for us,
[5:13] the look development and surfacing of the CG Ironman suits.
[5:16] In this paper, he goes into great detail about their entire shading process,
[5:20] how they approached it, their challenges and solutions,
[5:23] how they developed new tech for the suits,
[5:25] and yet as detailed as the paper was,
[5:27] the process of creating such a complex hero asset
[5:30] was so massive that 25 pages can only cover so much,
[5:33] and my specific question wasn't directly addressed.
[5:36] But, within the paper, on the last paragraph of page 10,
[5:42] in between details about vector exponent values and UV management,
[5:46] I found it a brief mention of a second, specular highlight.
[5:52] And ladies and gentlemen, that is a clue.
[5:55] However, it's still very little information,
[5:57] because what does that even mean?
[5:58] Is it really what I think it is?
[6:00] Maybe it's something else and I'm connecting invisible dots.
[6:02] Maybe that was just a specific case in the pipeline
[6:05] that wasn't related to Ironman's surfacing in general.
[6:07] Or maybe even it was just a piece of 2007 VFX jargon
[6:11] that meant something entirely different back then.
[6:14] So I had to find more.
[6:16] I scoured interviews, articles, tech reviews and presentations
[6:19] from C-Graph and FMX, and nothing.
[6:22] There was practically zero information about this.
[6:25] Part of it because it was 2007, 2008, almost 20 years ago,
[6:29] and part of it because it's so specific.
[6:32] The only people who would know more would be the artists
[6:34] who worked on it themselves, but Ironman was released 19 years ago,
[6:38] and that is a massive gap in time in the industry.
[6:40] Most of those artists are scattered across the globe,
[6:43] working in near anonymity or even retired.
[6:45] Reaching out to them just wasn't feasible,
[6:47] so I had to find another way.
[6:50] Anyway, so I contacted Ileam's supervisor and principal engineer,
[6:53] Pixar Global Researcher and Facebook Research Director,
[6:57] Christoph Harry, who not only is one of the most influential figures
[7:00] in computer graphics, with more contributions than I could possibly list,
[7:04] but luckily for us was also one of the two people credited by Ben Snow
[7:08] for developing Ironman's shader in Anisotropic Tools.
[7:11] Oh, and he was also a key figure in Luke Deving and rendering David Jones.
[7:16] Christoph very kindly accepted to answer my questions,
[7:19] although I must preface this with a reminder that it occurred over 19 years ago,
[7:23] so everything might not be recollected to perfection.
[7:26] So I showed him my Ironman screenshot, and I asked him what is it,
[7:29] what could cause this and what's happening here.
[7:32] Christoph told me,
[7:33] All shaders at Ileam, since the ones I started distributing as generic circa 1996,
[7:39] had two specular lobes, so you could always mix and blend various properties through them,
[7:44] but these are normal gain controls and thus Fresnel,
[7:47] where dance through full cauldrons at 0 and 90 degrees incidences,
[7:50] and the curve itself was a schlick that we could change the exponent on it from a default of 5.
[7:55] For Ironman, we ensured some sort of energy conservation,
[7:58] where diffuse substrates would automatically rebalance themselves with a very strong approximation,
[8:02] so as to not explode in energy, this was becoming critical,
[8:05] because through important sampling and PBR,
[8:08] we were starting to do much more recursive raytracing, reflections, etc.
[8:12] I showed him my technical tests and my approach suggestions that we're gonna talk about in this video,
[8:17] compared to the ground truth and the default roughness workflow,
[8:20] I asked him if that made sense, and for his opinion on it, and he said,
[8:24] Yes, this solution might be the way to attempt to emulate it,
[8:27] as the two lobes were simply additive to one another.
[8:30] And that was more information and confirmation that I could have hoped for.
[8:34] There we are, we've got our explanation, and we know exactly how Ileam did it.
[8:38] At that point, I even had an hypothesis as to what's causing this in real life,
[8:42] which Christophe found adequate. I guess we're all done.
[8:45] We're all done, right? Not at all.
[8:47] My main issue with all of this was that, while I had real-world reference images and theoretical explanations
[8:53] as to why multi-reflection happened in the first place,
[8:56] my tests and explanation are all digital and honestly baseless beyond my own conjectures.
[9:02] My idea was that visual acuity can't resolve microscopic details,
[9:05] so our eyes interpret them as a faint secondary reflection,
[9:08] but unfortunately finding concrete evidence can be really tricky.
[9:12] You can see that close, a magnifying glass could see some scratches,
[9:16] but it won't be able to zoom enough for us to get a definitive answer.
[9:19] So, it's just not feasible, and I had to find another way.


### Finding Explanations [9:22]
**Transcript (timestamped):**
[9:23] Anyway, so I went to look at Metal under the microscope to see what's actually going on beyond our visual acuity,
[9:29] and huge thanks to EverSmaller for spending hours on Volko with me,
[9:32] looking at Metal on her microscope and proceeding to every visual test we could think of,
[9:37] rotating the sample, checking different angles, different lights, different light colors, orientations and whatnot.
[9:43] And what we found was so interesting, I was really happy because my theory was correct.
[9:48] But on top of finding microscopic scratches creating what looks like a faint secondary reflection from a distance,
[9:53] we could see live that scratches vary wildly in size, density, straightness and most importantly depth.
[10:00] That was the critical part, and seeing that under the microscope was really amazing,
[10:04] and not only was it correct when we first entered the microscope at the minimum zoom,
[10:09] and we kept zooming and zooming and every single iteration would reveal new scales of scratches,
[10:13] and each again slowly contributing to another roughness stacked onto the others,
[10:18] although at these scales they are so shallow that you really don't feel them from a distance.
[10:23] And why is that important, you ask me?
[10:25] Well, if you had a scatter of scratches that were all perfectly consistent in size and depth,
[10:29] they would reflect light at a consistent rate of disruption,
[10:32] and that would just look like a single secondary reflection of consistent roughness.
[10:36] If all scratches were deeper, reflect two would get blurrier,
[10:40] and if all scratches were denser, reflect two would get more visible.
[10:44] The reason for that being that more scratches would cover the initially clean surface,
[10:49] but still not completely, so the two would visually overlap due to our limited visual acuity.
[10:55] The point is, it would never look like a multitude of roughness's values coexisting all at once,
[11:00] but here is where it gets interesting.
[11:02] When you start varying the depth of those scratches, things change.


### Research Conclusions [11:05]
**Transcript (timestamped):**
[11:07] Some of them scatter light wildly, some scatter it just a little,
[11:10] and others reflect light at an almost identical angle than your reflect one.
[11:15] Of course, depth isn't the only factor driving this phenomenon,
[11:18] if you got density and size playing a massive role too,
[11:21] and this is how, when you factor in every possible variation of real-world micro-scratches,
[11:27] that you obtain rich metal revealing previously ignored variations.
[11:31] Some of them are smoky with a sharp reflect one, and a seemingly single rough reflect two.
[11:36] These ones, for example, have dense and consistent scratches.
[11:39] Some of them feature a beautiful long falloff,
[11:42] these have scratches of varied size, depth and density,
[11:45] and yes, thanks to all these variety, some of them have no falloff at all.
[11:49] Either metals with no falloff at all,
[11:51] not necessarily mean that they have no scratches,
[11:54] instead it actually means that they have consistent enough scratches and disruptions of any kind
[11:59] that there would be no variation that our eyes could interpret as coexisting roughness's.
[12:04] And last but not least, some surfaces are more exotic,
[12:07] and present both isotropic and anisotropic reflections at the same time.
[12:11] And remember, anisotropy is an illusion due to surface disruptions being biased towards a direction.
[12:17] However, the problem with regular anisotropies is how simple and surface level it is.
[12:22] A regular anisotropic shader applies those directional disruptions to the entire surface,
[12:27] as if it was fully covered without a single intact area,
[12:30] so naturally the entire reflection gets affected.
[12:33] But reality is more complex, and not all surfaces are entirely scratched.
[12:38] If in fact a surface isn't actually entirely covered in scratches,
[12:41] but instead is a mix of intact areas and disrupted areas,
[12:45] then a single pixel of your render will contain reflections from both situations,
[12:50] and therefore it'll look like a mix of both.
[12:52] And the final shader, instead of being entirely anisotropic,
[12:55] will be a mix of both types of reflections
[12:58] and preserve a certain amount of the original intact reflection,
[13:01] proportional to the area of intact surface within one pixel,
[13:05] but also a certain amount of the anisotropic reflection.
[13:08] And due to this, you can even have multiple anisotropy directions within a single surface,
[13:12] if the directional scratches are both non-constant and oriented differently.
[13:16] Okay, let's use a practical example to really understand this aspect.
[13:20] So on this reference, we have a green glove being reflected by a stainless steel surface.
[13:24] And we can see that the reflection is both clear and undisturbed,
[13:28] but also that there is a second reflection mixed to it that is hugely rough and hugely anisotropic.
[13:33] And that is a direct consequence of sub-pixel content and density variation.
[13:37] Looking at this, we can safely assume that the surface isn't entirely covered in scratches
[13:42] because we can see both results at once.
[13:44] And all of that has to do with visual acuity.
[13:47] And visual acuity is the sharpness of your vision, or your render,
[13:50] and your ability to discern distinct elements from one another.
[13:53] But because this acuity is finite and imperfect,
[13:56] there is a scale at which your vision and render cannot resolve details separately anymore.
[14:00] And because of that, the perception of that specific area will be a blend between both elements.
[14:06] A red square and a blue square up close? Easy, they're completely separate.
[14:10] Now a billion red and blue squares from a distance? And it looks purple.
[14:14] That's exactly where screens work, and it's exactly where reflection tail-off happens.
[14:18] So you've probably guessed it, while this video originates from forgotten metal techniques about reflection tail-off,
[14:23] the physical phenomenon this effect originates from
[14:26] allows us to talk about much deeper concepts, like perl-layer and anisotropic variation,
[14:31] and scratch-type dependent roughness variation.
[14:33] And now we have to replicate it. For those who've seen previous videos,
[14:37] you'll know what kind of approach fits the situations where two different surfaces coexist with one being entirely present
[14:43] and scattered beneath our visual acuity, and that's right, that would be material layering.


### Doing it in 3D [14:48]
**Transcript (timestamped):**
[14:48] Unlike my previous video where I was specifically talking about layering in the context of real materials
[14:54] sitting atop of a surface, like oil or dust, material lasuring in this case is a lot more niche
[15:00] and can seem inadequate at first glance, but it turns out it makes complete sense.
[15:05] Material layering, whether it's in V-Ray cycles or most other engines,
[15:09] doesn't actually take any virtual thickness parameter into account.
[15:13] All it's emulating is that there is, in some way or another, a different response to light around the surface,
[15:19] and that the area of this response is so small that it becomes invisible to our eyes and can be approximated to a solid.
[15:26] And because this different light response isn't completely covering the surface,
[15:30] it gets interpreted as a transparent value from a distance.
[15:33] So, because there is no thickness taken into account, material layering is actually adequate for multiple situations IRL.
[15:40] It could be particles sitting atop of a surface, like oil or dust,
[15:44] could be an area of that same surface that is altered in some way, like a glint, speckles, or millions of microscopic dots of rusts.
[15:52] There could also be holes revealing a deeper layer beneath the main surface,
[15:56] as if you had, for example, metal under a scratch-cover paint.
[15:59] So that being said, what does it mean in practice?
[16:02] Well, if you take a look at our microscopic footage, or any reference really,
[16:06] we just have to look at scratches to see what our setup should be.
[16:10] So, since our scratches are only visible when reflecting light,
[16:13] we can tell that they have the same diffuse IOR and other properties as the rest of the surface,
[16:18] or they would be visible at all time, no matter reflections.
[16:21] If we isolate a first scale of scratches,
[16:24] we can see that the only notable difference between the original surface and the scratches is the bump map.
[16:30] If we take another range of scale of scratches,
[16:32] the only difference with the previous one would be the density, the thickness of the scratches,
[16:36] and the bump map once again will take another range of scratches and there again,
[16:40] and it's just another variation of width and depth,
[16:43] and again, and again, and again,
[16:45] until we're reaching scales where we cannot even tell the bump anymore.
[16:48] And because we're dealing in general with variations beneath our visual acuity,
[16:52] we don't even have to use bump at all.
[16:54] We can use the approximation instead,
[16:56] and the approximation of bump is roughness.
[16:59] So what it means is that as the scratches get smaller, denser, and cover more and more of the surface,
[17:04] the apparent general roughness of that layer will increase.
[17:08] So instead of having multiple layers with multiple bump map and bump strength,
[17:11] we'll just blend identical shaders together where each is getting increasingly rougher.
[17:16] And on top of that, because smaller scratches also tend to be decreasingly deep,
[17:21] the apparent presence of each layer is going to decrease accordingly.
[17:25] So we're going to have our material layering set up with each of our duplicates and a master material at the base.
[17:31] Each other layer is going to be a duplicate of the first one, except the roughness is going to increase.
[17:36] And when you're building it, the game is going to increase or decrease the presence of each layer until it matches the reference.
[17:43] So you duplicate your material, plug it into your material layering set up, and you dial it up and down.
[17:49] And you're going to repeat this process however many times you like.
[17:52] Doing it in blender is going to be the same process, except the nodes are going to be principled BSDF.
[17:57] Material layering is going to be a series of mixed shaders,
[18:00] and the presence of each layer is going to be controlled via the factor.
[18:03] If you wanted to use roughness textures inside your material,
[18:06] you can plug the same texture inside a series of different curves
[18:09] and increase the lift value of every iteration of curve
[18:12] so that each layer is getting increasingly rougher while maintaining the work you've done into your roughness.


### Cycles : GlossyBSDF [18:18]
**Transcript (timestamped):**
[18:18] If your render allows it, like blender's cycle, you can use glossy BSDFs instead.
[18:23] The process is identical to full material layering, except you're going to use glossy BSDFs and mix as many as you need together.
[18:30] The way to set it up is very easy.
[18:32] You just create a principled BSDF, and you're going to mix it to as many glossy BSDFs as you want,
[18:38] just like the full material layering.
[18:40] Each glossy BSDF is going to get increasingly rougher,
[18:43] and will generally be decreasingly present through the factor slider.
[18:47] It is a little bit different than Irem's approach, because they initially added reflections together,
[18:52] so that broke energy conservation,
[18:54] but modern technology and render speed allow us to do mixed shaders instead.
[18:58] And now it's time to see alternative approaches to achieve a similar effect, each with their pros and cons.


### Alternative : Clearcoat [19:05]
**Transcript (timestamped):**
[19:06] So the first method for achieving a fake multi-reflection would be to use clear coat.
[19:11] This was a popular suggestion in the comments of my last material layering video,
[19:15] and while it has some limitations, it's a great one-click starting point.
[19:19] It can achieve a relatively similar looking tail-off by adding an extra reflection.
[19:23] It's cheaper than some of their options, and it's built in virtually every single render engine.
[19:28] However, it does have some limitations for all cases.
[19:31] This kind of effect is only going to be really present into hero assets,
[19:36] so clear coat deforming the look of the underlying material, such as diffuse color and apparent IOR,
[19:42] which in turns require AB compensations to restore original values, is a huge drawback.
[19:47] And clear coat isn't metallic, it's a blend to a dielectric material,
[19:51] so the reflections will not be colored by the metal.
[19:54] So while it will look normal if your metal is white,
[19:56] it'll start being obvious clear coat chitting once you've got any color in your metal.
[20:00] And you could think coloring the coat itself would fix it,
[20:02] and it would help the reflections to some degree,
[20:04] but then it only shifts the problem as now the entire underlying material
[20:08] and original reflect one are affected and incorrect.
[20:11] So clear coat is really case dependent, and I would not personally recommend it,
[20:15] but if it's from far away and that your metal is black and white,
[20:18] then it could be a nice cheap alternative.
[20:20] For example, on this lead study that I did,
[20:22] the clear coat approach really deforms the underlying material in shaders.
[20:26] Not only it doesn't look correct compared to the reference,
[20:29] it's also deforming materials in a way that isn't really desirable.


### Alternative : GGX Tailoff [20:34]
**Transcript (timestamped):**
[20:34] The GGS reflection model was created specifically to emulate the long reflection tail
[20:39] of visible on materials with micro textures.
[20:41] If your renderer allows it, you can control how far the tail and reflection fade point goes.
[20:46] This gives the impression of a roughness increase at first,
[20:49] because obviously the highlight takes more space now,
[20:51] so in turn you can lower the roughness and match your material.
[20:54] This reflection model is an excellent option for multiple reasons,
[20:58] firstly the control was created precisely to do that, so it's very handy.
[21:02] It can be a bit confusing at first to really understand its potential,
[21:06] but once you know what it's actually doing, it's very handy and very useful.
[21:09] It's fast and easy to use, and it comes at basically no cost,
[21:13] because it is only modifying the single reflection that is already being calculated either way.
[21:18] However, there are a few drawbacks that to me prevent the tail of control
[21:22] from being the number one option if you're trying to do the best looking render possible,
[21:25] although it is the handiest and easiest option to go for.
[21:29] It's not exposed on every render engine, so for example on cycles,
[21:33] you would need someone else to probably go into the Blender API
[21:36] to expose the control and hope that you have it at work.
[21:39] The various values you can choose from are basically just an exponent control
[21:43] for the unique tail of profile it has.
[21:45] So while you can control the inbuilt profile,
[21:47] you can't have a sharp highlight and a straight jump to point eight roughness for example.
[21:51] If I choose to customize my curve here and have a ground truth that would be quite unique,
[21:56] there will be no way to recreate that with the Ggx tail of control.
[21:59] And it can break if you lower the values too much.
[22:01] You start having undesirable reflections onto your image,
[22:04] and that obviously doesn't help your material at all.


### Turntables [22:05]
**Transcript (timestamped):**
[22:08] I rendered four different methods to achieve reflection tail of.
[22:11] There is ground truth, multilayered reflections, the regular roughness, and the Ggx tail of approach.
[22:17] I didn't include clear code because it's an insufficient solution that should only be considered in unimportant cases.
[22:23] It is inadequate if you want to be serious and precise in our recreations of the references.
[22:28] So on these table we can see multiple things.
[22:31] First off that the regular roughness workflow is completely inadequate to recreate the complexity
[22:36] and the richness of the ground truth approach.
[22:38] You're supposed to be able to see the text clearly, the neons are completely sharp,
[22:42] and all the anisotropic reflections are added and mixed to the original reflection and not replacing it.
[22:48] On the regular roughness workflow there's a massive loss of information.
[22:52] Everything gets blended into each other, it's just really poor and really insufficient if we want to make quality metal.
[22:58] If you use a renderer that allows you to edit it and happen to know about Ggx tail of,
[23:03] you could try to replicate it and that would get you pretty far ready.
[23:07] You could have an in-between that looks closer to the ground truth but is still pretty different.
[23:12] The text isn't as clear, there's a loss of information, and the biggest problem for last,
[23:17] you have that massive undesirable reflection spreading across the entire surface.
[23:21] And we can see that it is plaguing the render in all angles.
[23:25] Now on the other hand, the multi-layer reflection is a much more robust solution.
[23:30] It is more expensive than the Ggx tail of and that is pretty much its biggest drawback,
[23:35] but it allows you complete creative control and perfectly achieves the intended look of the Ggx.
[23:40] In fact, every look difference, for example, there is a very very subtle difference in the immediate fall-off around this neon,
[23:47] or a completely artist dependent and not method dependent.
[23:51] My roughness choice for the first layer is probably a tad bit too big
[23:55] and I could either reduce it or reduce the presence of the first layer to match this Ggx.


### Statistics [24:00]
**Transcript (timestamped):**
[24:01] I asked a few supervisors at work and other people who've generally been in the industry for 20 years
[24:07] and this phenomenon in shedding approach was basically no surprise to them.
[24:11] So don't worry if you saw the title of this video and thought
[24:14] I still remember clickbait.
[24:18] You're not alone, but I've never really seen anyone of my generation do it or mention it, so thought I would make a video about it.
[24:24] It's not taught at any of the best schools in the world, in courses, in private servers or anywhere.
[24:30] So to understand the different workflow landscape more transparently,
[24:33] I decided to write a Google form and test respondents with describing their workflow
[24:38] to four different metals that each showcase this reflection fall-off effect to various degrees.
[24:44] I asked them to estimate different properties of the shader if they could
[24:48] and I also told them to be as thorough or concise as they wished
[24:52] because I absolutely did not want to bias the question and suggest that there was actually something not worthy on these metals
[24:59] so thanks to them I was able to see recurring workflow patterns.
[25:02] Of these 52 people, 41% were generalists, 25% were surfaces and 10% were character artists.
[25:10] The majority of respondents are professionals with also 28 and 25% being hobbyists and students respectively.
[25:17] And lastly, most participants had 2 to 4 years of experience and 23% with over 5 years and even 11% at over 10 years.
[25:25] So I read through every single reply, I noted the workflow, the suggested values, the value variations,
[25:32] whether or not they noted the presence of the reflection fall-off and this is what came out of it.
[25:37] Across all examples, about 25% of people noticed something going on to the surface.
[25:43] Most of them suggested that it was dirt or fingerprints which what may not be entirely true, it is on some references but it's not the main effect.
[25:51] It still shows that they did notice an extra behavior to account for.
[25:55] Also a fair amount of people within those 25% suggested that it could be achieved with a coat layer.
[26:01] In those 52 respondents, 2 of them mentioned varying the GDX tail-off and more importantly,
[26:06] 2 other people mentioned explicitly that there was different reflections co-existing and not via coating.
[26:13] One interesting thing to look at would be the roughness value suggestions on each example.
[26:17] On example 1 you can see that the people suggested a wide variety of values, you've got 0, 0.15, even 0.7.
[26:25] You couldn't wonder why would suggestions be so different but it actually makes sense when you think about that.
[26:30] Reflection fall-off gives the impression of multiple roughnesses co-existing.
[26:35] So if the viewer looked more around those sharp edges, they might tend to say the roughness would be 0
[26:41] and instead if they noticed how the colors bleed largely onto the entire sphere, they'd probably suggest something higher like 0.4 or 0.7.
[26:50] So these heterogeneous estimations occur throughout all examples and while they generally gravitate toward the most visible reflections look,
[26:58] the last example was particularly tricky in that there doesn't seem to be a superior roughness choice and that one really messed up with people's estimates.
[27:07] The value suggestions were scattered evenly across almost all ranges of roughness.
[27:11] There was the most amount of confusion in written comments and it was generally the example that received the most extraordinary suggestions like GDX variations, coat overlay, etc.
[27:22] Really anything to make it work.
[27:24] Nothing this form was really informative, even with just 52 respondents.
[27:28] To me it highlights how this effect isn't accounted for, not because people don't see it, but rather because there is no clear consensus on what it is and how to achieve it.


### Comparisons [27:39]
**Transcript (timestamped):**
[27:39] Let's see how multi-layer reflections compare to regular roughness.
[27:43] So that's the first example from the Google Form.
[27:47] This is the fourth example from the Google Form.
[27:54] This one is one of the earliest tests that I did when I started researching this subject and on this specific example I'd like you to pay attention to the skin color the halo around the hand.
[28:04] These are completely missing before multi-layer reflections are applied.
[28:07] This effect is also present in balloons for example.
[28:13] In a traditional metal workflow, I would have to choose between the anisotropic reflection and the clear reflection, but with multi-layer reflections I can just have both exactly like the reference.
[28:23] Another example with the fridge I came across, and here you can clearly see that the door is perfectly clear, maybe something like .05 roughness, and there's a huge anisotropic falloff on top of it.
[28:34] This is a cooking pot of mine, where you can see that there is both a clear reflection and an anisotropic reflection at the same time.
[28:41] Before you'd have to choose between one reflection or the other, but now you can just have both at once.
[28:48] Here's a personal test on Ironman's helmet compared to the practical Mark II suit, and you've got Ironman's own render from Ben Snow's paper on the side as well, so you can judge this approach for yourself.
[29:00] And this is the reference of the green gloves with the semi-anisotropic multi-reflections.
[29:08] And here is the last example with an elevator.
[29:10] Before, the reflections were very simple, anisotropic, nice, but very simple nonetheless, and afterwards they cannot get these trippy elevator reflections.


### Conclusion [29:19]
**Transcript (timestamped):**
[29:19] And this is it.
[29:20] We've rediscovered forgotten metal workflows, looked at reflection tail-off, discovered pearl-layer anisotropy and visual-acuity, and understood sub-pixel-squared variations.
[29:31] Man, that was so much work.
[29:33] There's about 26,000 frames of explanatory motion graphics.
[29:39] I've been editing this for two weeks, every night after work.
[29:42] This is off-screen by the way, it's almost 2am on a weekday as I'm recording this, so I really hope you enjoyed this massively long and convoluted video.
[29:52] I hope I repeated myself enough to make things clear.
[29:55] I decided to put my social link under this video.
[29:58] Initially, I opened this channel anonymously, and I figured it might be curious to check out my work.
[30:04] There's a bunch of core resources as well on my all station.
[30:07] Do let me know if you have any comments or suggestions.
[30:11] And on that note, I'll see you next time.



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
