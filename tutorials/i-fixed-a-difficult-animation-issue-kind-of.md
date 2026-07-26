---
title: I Fixed a Difficult Animation Issue! (Kind Of)
source: YouTube
url: https://www.youtube.com/watch?v=ZqON1ms8VOM
author: Curtis Holt
ingested: 2026-07-26
blender_version: "Not specified"
tags: [animation, rigging, advanced]
extraction_status: complete
frames_dir: tutorials/frames/i-fixed-a-difficult-animation-issue-kind-of/
frame_count: 4
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# I Fixed a Difficult Animation Issue! (Kind Of)

**Source:** [YouTube](https://www.youtube.com/watch?v=ZqON1ms8VOM)
**Author:** Curtis Holt
**Duration:** 8m23s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Alright, another standing video means another report slash vlog.
[0:03] Alright, so first of all, human animation pipeline.
[0:06] I now have foot sliding fixed.
[0:09] And I say fixed like that because it works, but it's a little bit crap.
[0:15] No, no, it's fine.
[0:16] It's correctable with some like animator input.
[0:19] What it does is it assesses each foot as being like a support foot and it checks the rotation.
[0:25] So we call like a kind of a spin and a heel like control bone as well.
[0:28] So it checks the rotation within a certain threshold and the location.
[0:31] And if it's kind of flat enough within that boundary, then it will kind of consider it as being on the ground and it considers a little bit before and afterwards in terms of keyframes, right?
[0:40] So you kind of categorically assessing, well, heels being down for this long, or it's been tilted this way and then kind of became more flat.
[0:47] So you're trying to capture different like entry methods to like it being flat.
[0:52] And then once it thinks it's a support foot, basically it thinks it's like flat and supporting the body,
[0:56] then it will try and gravitate the remaining difference to that flat position.
[1:01] So in a way, it's a bit like magnetism.
[1:03] So what will happen is when you watch it back, the character will walk and then you'll just see the foot kind of go and then like snap to ground.
[1:11] Like it's like grav boots or something.
[1:12] So it works, but it's not completely natural, but it does stop the sliding because when they're like magnetized to the ground, then that kind of mocap body sliding thing doesn't happen.
[1:23] So it's not grave like natural ultra realistic, but it's fantastic as a starting point to then make a few more like realistic movement adjustments afterwards.
[1:31] So I mean, I'm quite impressed to manage to get to that point, but I think there's actually better ways to do it.
[1:36] For example, one thing I've noticed quite a bit when doing the cleanup script for animation is that a lot of the time it's having to consider a little bit before and a little bit after like the area you're trying to modify.
[1:45] And that's just contextual information.
[1:47] So maybe an important thing to do would be to instead have like before doing any automatic cleanup.
[1:54] I mean, I already do this slightly with the foot placement where we kind of be mark points with empties and like curves based on how far the sliding goes.
[2:00] And you can use like those pre created objects as like an informational source to tell you like where correction needs to be done.
[2:08] But I'm thinking about something smarter where, for example, not just with the feet, you know, trying to categorically say this time it's coming out of walking.
[2:15] Or this time it's just rotating the foot.
[2:17] But to do that all over the body, so just have like a kind of smart sense of what's happening, you know, neck turning, fingers extending, fingers closing.
[2:26] Because when you get that, like kind of general description of the category, the context really, like just what's happening, then you can use that as like markers.
[2:35] You can API it in some way, like so you could call that, you know, search for all cases where fingers open, blah, blah, blah, grab pre frames, this number, post frames.
[2:44] So it's kind of like a smarter lookup system.
[2:46] So you're not having to algorithmically detect those things for every single script.
[2:51] So does that make sense?
[2:52] So I'm thinking about that.
[2:53] So you do this smart analysis that again is not just for the fee, but for everything in the body.
[2:58] Maybe it's needed.
[2:59] Maybe it's not.
[2:59] Maybe we'll just kind of carry on hard coding and then, you know, throw enough computing power and techniques are a problem until it looks relatively usable.
[3:06] But basically there's there's some progress there.
[3:08] Another thing I've done just a little while ago is I emailed Rococo, you know, the people that do the motion capture suits.
[3:14] Now, I'm not great when it comes to company relationships because I hate sponsorships.
[3:18] I've only done them when I really needed to do them because I will not say what people want me to say.
[3:24] Pathological demand avoidance.
[3:26] We don't do that.
[3:26] But in the past, I've got two emails from Rococo inquiring about sponsorships.
[3:31] Now, this was like a few years ago.
[3:32] One of them did try to come through the casual sponsor system, you know, the system I did a while back, which was kind of like a pay-as-you-go sponsor system.
[3:38] But I could pick and choose.
[3:39] And the main point was I get ultimate freedom to do how I want to do it.
[3:42] What I've done is I've gone back to one of the emails that I got and I sent Rococo a message saying, Hey, just so you know, I'm working on a little animation thing at the moment.
[3:51] I'm building some tools of my own.
[3:52] I'm testing the Unreal to Blender workflow, Polyhammer, Cascade, or whatever.
[3:56] I said, it's getting some eyes on it.
[3:57] The interesting thing, though, like I said in the previous video is that while I don't get many views nowadays, for some reason, everyone fucking knows what I'm doing.
[4:04] Like whenever I mention a piece of software, the developers of the software say it like that.
[4:09] I'm getting private messages from like professionals in the industry, as I'm getting new people follow me that are like, game company animator for 20 years.
[4:15] And I'm like, why are you?
[4:16] You're already a professor.
[4:17] You don't need like my little crappy attempts at, you know, little animation tools.
[4:21] I just find it funny that I might not have the poor power for the general audience anymore, but I do have poor power for industry.
[4:28] And I wonder how much that comes down to my dad who watches some of these videos now.
[4:33] Hi, dad.
[4:34] I'll tell you a little funny story.
[4:35] I hope it doesn't come off as a flex, but it's just a bit funny.
[4:37] There's someone who watches my videos every now and again.
[4:39] Could Mike Lambert.
[4:40] Mike, if you're watching, how are you doing?
[4:42] How are you doing?
[4:42] Well, he's a stunt guy interested in animation as well, from what I see.
[4:46] Anyway, he's worked with my dad.
[4:47] I don't know how many times, but it's quite funny.
[4:49] Apparently he pieced two and two together and he went up to my dad and he was like, your son, I watch his videos on YouTube.
[4:55] It's kind of funny.
[4:55] Usually my dad's like the one that's well known.
[4:57] So it was a funny like, I could be known to when my dad comes over and tell him about the updates to the animation project.
[5:03] And other things because he finds that quite interesting.
[5:05] He said, yeah, I watched your video.
[5:06] I was just watching a video, the one where you say, holy fucking shit.
[5:10] I was like, yep.
[5:11] Yep, that happens.
[5:12] Anyway, if for a cocoa, don't get back to me, I'll just message one of their competitors.
[5:16] And then the reason I want to do this is because I am looking into Markless motion capture, of course, in a building a system here.
[5:21] But because I'm scientific, experimentalist, and this is an R&D project, I do want to try different solutions.
[5:28] I don't need to try another Markless motion capture solution because the fixing principles will basically be identical.
[5:34] So I'm already covering ground there.
[5:36] I mean, I can be useful, but one of the things I'm seeing is that most Markless systems don't take into consideration the hands.
[5:42] I don't need arms and legs moving.
[5:43] I need, you know, hands.
[5:45] Bro Coco has smart gloves and I've been thinking about a system of building my own.
[5:49] I've got ESP 32s of my own.
[5:51] I'm thinking about like a pressure volume system.
[5:53] That's what I'm calling it anyway.
[5:54] So I could do that with the microcontrollers.
[5:57] So I've been thinking about ways that maybe I can build my own equipment, but I'd like to try the Roco system.
[6:02] But I know they're not the only ones that have solutions.
[6:04] So I've messaged them first just because they had already expressed interest in the past.
[6:09] But I did say at the end of my email, if you do want to collaborate on anything, I have to maintain full messaging decision.
[6:17] Basically, you can't tell me what to say.
[6:19] That's it.
[6:19] Obviously, it's not very friendly for companies.
[6:21] I may just buy their system.
[6:22] But is kind of ludicrously expensive?
[6:25] Okay, I can't remember where I put my microcontrollers.
[6:26] I've got like GPUs laying around, but the ESP is somewhere and it's been a long time since I did any hardware stuff.
[6:33] But I guess for now, just keep working on like the Marcula system or any other updates.
[6:38] I've sent some more agreements on the talent system for people that have applied to my little side project of a talent agency.
[6:45] If you want to sign up, you can still apply.
[6:46] I had a client come through asking for some talent recommendations.
[6:51] So I sent a collection of the talents on a response to them.
[6:54] And then I let the talents know that I'd recommended them.
[6:56] So I'm going back.
[6:57] I'm trying to do like a few every day now, like sending out agreements to people.
[7:01] So if you did submit a while ago, just hang in there.
[7:04] It's going to take a while to get through the backlog.
[7:05] Alrighty, all of this development work is powered by your support on Patreon.
[7:09] Patreon.com.
[7:09] Slash Kurtis Holt.
[7:10] Check out the exclusive content on KurtisHolt.
[7:12] Online slash members.
[7:14] There you'll be able to find links to production files and exclusive tools and resources and all sorts of other stuff.
[7:18] And by the way, all of my products are available on the Gold tier.
[7:21] It's cheaper getting the Gold tier and then being able to use them for as long as the membership's active rather than buying them all individually.
[7:27] It's up to you.
[7:28] You can just tap in and out.
[7:29] And the R&D work for the human animation pipeline is also available on the workflow and pipeline section.
[7:35] I think it is.
[7:35] All right, I'll keep you updated with developments and I'll let you know both how my work goes and then if I hear back from any companies.
[7:41] Oh, but also in case for a Coco, don't get back to me.
[7:44] Who else should I contact?
[7:46] Again, this is just to learn more about the space, just to try out different tools.
[7:50] Again, we might not need them.
[7:51] And I can build my own equipment if I need to.
[7:53] And I probably learned a lot from doing that.
[7:55] But then again, you know, I don't want to spend all my time on the animation side.
[7:58] There's all the other fun stuff I want to do for the connected space.
[8:01] So it's just about, you know, divvying up time.
[8:04] Like how much of a month do I want to be on like R&D?
[8:07] How much I want to be on like, you know, entertainment content and trying to hit the milestones to get something out for the TCS channel.
[8:14] But there's always something happening.
[8:15] All right, if you made it this far, put a unicorn emoji in the comments.
[8:18] Windows key, period key that bring up an emoji keyboard.
[8:21] Have a great day and I'll see you next time.



---

## Captured Frames

- [1:05] tutorials/frames/i-fixed-a-difficult-animation-issue-kind-of/frame_000.jpg
- [1:55] tutorials/frames/i-fixed-a-difficult-animation-issue-kind-of/frame_001.jpg
- [2:20] tutorials/frames/i-fixed-a-difficult-animation-issue-kind-of/frame_002.jpg
- [5:45] tutorials/frames/i-fixed-a-difficult-animation-issue-kind-of/frame_003.jpg

---

## Structured Notes

> **Format note:** This is a talking-head progress vlog (Curtis Holt's human-animation-pipeline R&D), not a step-by-step tutorial. Frames confirm no on-screen Blender work beyond one picture-in-picture mocap-character clip at ~1:05. The value is the *conceptual design* of his automated foot-sliding cleanup, captured below.

### Core Technique
Algorithmic mocap foot-sliding cleanup: classify each foot per frame-range as a "support foot" (rotation + location within a flatness threshold, with look-back/look-ahead keyframe context), then magnetize the remaining positional difference to the flat grounded pose.

### Summary
Curtis Holt reports progress on his custom human animation pipeline (markerless mocap → Blender, with an Unreal-to-Blender workflow via Polyhammer tools). His foot-sliding fix works by assessing heel/spin control bones against rotation and location thresholds to categorize support feet, considering keyframes before and after the contact, then snapping ("grav boots"-style magnetism) the foot to ground — effective against sliding but needing animator polish for naturalness. He proposes a next step: a body-wide "smart context" pre-analysis pass that labels events (foot planting, fingers opening/closing, neck turning) as queryable markers/API so each cleanup script no longer re-detects context algorithmically. Also discusses hand-capture gaps in markerless systems, Rokoko Smart Gloves vs. a DIY ESP32 "pressure volume" glove idea.

### Key Steps
(Conceptual pipeline design, not reproducible click-path:)
1. Detect support feet: check heel + spin control bone rotation and location against a flatness threshold per frame window.
2. Include pre/post keyframe context to catch different "entry methods" into flat contact (heel-down duration, tilt-to-flat transitions).
3. When classified as supporting, gravitate/snap the residual offset to the flat grounded position — eliminates sliding at the cost of a visible snap.
4. Pre-mark correction regions with empties and curves sized by sliding distance, as an informational layer for cleanup scripts.
5. Proposed evolution: full-body semantic event labeling (a queryable marker API: "all cases where fingers open, N pre-frames, M post-frames") shared by all cleanup scripts.

### Nodes / Settings
None shown — no node setups or parameter values appear in the video.

### Difficulty
Advanced (conceptual pipeline/tool-development discussion)

### Blender Version
Not specified

### Tags
animation, rigging, advanced

---

## Related Tutorials
- [My New Favorite Lighting Trick in Blender!](my-new-favorite-lighting-trick-in-blender.md) — same author (Curtis Holt), Project Fold ecosystem
- [MetaHumans in Blender: Using OpenRigLogic to Customize DNA's Behavior](metahumans-in-blender-using-openriglogic-to-customize-dnas-behavior-inside-unrea.md) — the Polyhammer Unreal↔Blender character pipeline Curtis mentions testing, plus mocap import
