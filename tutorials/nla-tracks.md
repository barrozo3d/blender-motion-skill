---
title: NLA Tracks
source: Article
url: https://docs.blender.org/manual/en/5.2/editors/nla/tracks.html
author: docs.blender.org (Blender 5.2 LTS official docs)
ingested: 2026-09-04
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/nla-tracks/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# NLA Tracks

**Source:** [Article](https://docs.blender.org/manual/en/5.2/editors/nla/tracks.html)
**Author:** docs.blender.org (Blender 5.2 LTS official docs)
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Tracks ¶ A track plays one or more actions in sequence. You can create multiple tracks to play several actions at the same time. NLA Tracks and Strips. ¶ The track region has the following properties: Disable NLA stack (checkbox in blue object header) When unchecked, mutes all the tracks except the Action Track. Track name Double-click to change. (Not possible for the Action Track, as this one simply displays the name of the action.) Mute (checkbox in gray track header) When unchecked, the track stops contributing to the animation. Its strips receive a dotted outline to indicate this. Note that you can also mute individual strips. Lock (padlock icon) Prevents changes from being made to this track. This is useful, for example, if you want to move the strips in all the tracks except for a few. Solo (star icon) Mutes all other tracks, including the Action Track, so that only this track contributes to the animation. This is useful for inspecting the track without any distractions from others. Action Track ¶ The topmost track with the orange header holds the action that’s being edited. Normally this is the object’s active action, but if you select a strip and press Tab to enter Tweak Mode, you can temporarily make that one editable instead – in the Action Editor or the Graph Editor , for example. The Action Track has one of the following buttons: Push Down Action Not available in Tweak Mode. Creates a new track below the Action Track and moves the active action into it as a strip, leaving the Action Track empty. (If you create a keyframe after this, Blender will automatically create a new active action to hold it.) Push Down Action button. ¶ Pin Only available in Tweak Mode. When unchecked, the action’s keyframes are shown at their original time points, rather than their new time points resulting from the strip being moved and scaled. Strip at its original time point. ¶ Strip moved. Notice that the keyframes are now shown to start at frame 20, which is also how the animation will behave. Within the action, however, they still start at frame 1. ¶ After unchecking the Pin icon, the keyframes are shown at their original time points. ¶ On this page Tracks Action Track



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
