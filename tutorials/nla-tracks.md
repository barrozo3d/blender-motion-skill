---
title: NLA Tracks
source: Article
url: https://docs.blender.org/manual/en/5.2/editors/nla/tracks.html
author: docs.blender.org (Blender 5.2 LTS official docs)
ingested: 2026-09-04
blender_version: "Blender 5.2"
tags: [nla, animation, blender-5x, intermediate]
extraction_status: complete
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
A track plays one or more actions in sequence; multiple tracks play actions **at the same time** — and **Push Down Action** is the move that turns the active action into a strip so a new one can be built on top.

### Summary
The operational half of the NLA. Each track carries **Mute** (stops contributing, strips get a dotted outline), **Lock** (prevents changes — the practical way to move strips in every track *except* a few), and **Solo** (mutes all others *including* the Action Track, for inspecting one track cleanly), with a **Disable NLA stack** checkbox on the object header that mutes everything except the Action Track. The Action Track shows one of two buttons depending on mode. **Push Down Action** — unavailable in Tweak Mode — creates a new track below, moves the active action into it as a strip, and leaves the Action Track empty; keyframe after that and Blender automatically makes a new active action to hold it. That single operation is the loop by which layered NLA animation gets built. **Pin**, available only in Tweak Mode, controls whether keyframes are displayed at their **original** time points or at the new ones produced by the strip being moved and scaled — the strip may play from frame 20 while the action itself still starts at frame 1, and unchecking Pin shows the original timing.

### Key Steps
1. Put actions that should play **in sequence** on one track; use **multiple tracks** for actions that should play **simultaneously**.
2. Rename a track by double-clicking it — not possible for the Action Track, which simply displays the action's name.
3. **Mute** a track to stop it contributing (its strips gain a dotted outline); individual strips can be muted too.
4. **Lock** the tracks you want untouched, then move strips freely in the rest.
5. **Solo** a track to mute every other track *including the Action Track* while inspecting it.
6. Use **Disable NLA stack** on the object header to mute all tracks except the Action Track at once.
7. **Push Down Action** to move the active action into a new track below as a strip, emptying the Action Track — the next keyframe creates a fresh active action automatically.
8. In **Tweak Mode**, uncheck **Pin** to view keyframes at their original time points rather than the strip's moved/scaled timing.

### Nodes / Settings
- **Track** — plays actions in sequence; several tracks play in parallel.
- Per-track: **name** (double-click), **Mute** (dotted-outline strips), **Lock** (padlock), **Solo** (star).
- Object header: **Disable NLA stack** — mutes all but the Action Track.
- **Action Track**: **Push Down Action** (not in Tweak Mode) and **Pin** (Tweak Mode only).

### Difficulty
Intermediate

### Blender Version
Blender 5.2.

### Tags
`nla`, `animation`, `blender-5x`, `intermediate`

---

## Related Tutorials
- [NLA Editor Introduction](nla-editor-introduction.md) — the editor these tracks live in, and Tweak Mode.

---

> **Provenance.** Official Blender 5.2 LTS documentation, pinned to the versioned
> path (`docs.blender.org/manual/en/5.2/` and `docs.blender.org/api/5.2/`) rather
> than `latest`, so the entry keeps saying what 5.2 says after `latest` moves on.
> ⚠️ **These pages append site chrome to `<title>`** (" - Blender 5.2 LTS Manual",
> " - Blender Python API"), so `--title` is required when ingesting them.
> **Blender 5.2.1 LTS is installed on this machine** (`D:\Steam\steamapps\common\Blender`,
> build 2026-08-25), so the documented behaviour can be checked against the real
> build rather than taken on trust.
