---
title: NLA Editor Introduction
source: Article
url: https://docs.blender.org/manual/en/5.2/editors/nla/introduction.html
author: docs.blender.org (Blender 5.2 LTS official docs)
ingested: 2026-09-04
blender_version: "Blender 5.2"
tags: [nla, animation, blender-5x, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/nla-editor-introduction/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# NLA Editor Introduction

**Source:** [Article](https://docs.blender.org/manual/en/5.2/editors/nla/introduction.html)
**Author:** docs.blender.org (Blender 5.2 LTS official docs)
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Introduction ¶ The NonLinear Animation editor, or NLA editor for short, lets you animate on a higher level. Instead of working with individual keyframes, it works with actions , which are named, reusable animation segments. The NLA editor. ¶ Main Region ¶ The editor displays a stack of tracks which work like layers in an image editing program. Higher tracks take precedence over lower ones, although you can also choose to blend them. Each track can contain any number of strips – typically Action Strips, which are instances of actions. The top track highlighted in orange is special: this is the Action Track. Unlike the other tracks, it doesn’t contain strips – instead, it contains the object’s active action , which is where new keyframes are added to by default. Editors like the Dope Sheet Editor normally only show the keyframes of this active action. If you want to edit another action, you can select it in the NLA editor and press Tab to enter Tweak Mode. Tweaking an action. Notice that it’s shown in both its original track and the Action Track. The active action is temporarily hidden. ¶ Header ¶ View Menu ¶ Sidebar N Shows or hides the Sidebar Region . Adjust Last Operation Displays a pop-up panel to alter properties of the last completed operation. See Adjust Last Operation . Channels Shows or hides the Track Region. Playback Controls Show or hide the Playback Controls . Frame Selected NumpadPeriod Pans and zooms the view to focus on the selected strips. Frame All Home Pans and zooms the view to show all strips. Frame Scene/Preview Range Reset the horizontal view to the current scene frame range, taking the preview range into account if it is active. Go to Current Frame Numpad0 Centers the view on the Playhead. Realtime Updates Whether to update other views (such as the 3D Viewport) while you’re moving strips around. If disabled, the other views only get updated once you finish the move. Show Control F-Curves Shows a graph on top of each strip that uses Animated Influence . Show Markers Shows the marker region (provided any markers have been defined). When disabled, the Marker Menu is also hidden and marker operators are not available in this editor. Show Local Markers Shows action-local markers (which you can create in the Action Editor ). This can be useful to align strips to each other. Local markers shown in the NLA Editor (top) and the Action Editor (bottom). ¶ Use Timecode Ctrl - T Shows timing in seconds instead of frames. Sync Visible Range Synchronizes the horizontal panning and scale of the editor with other time-based editors that also have this option enabled. That way, they always show the same section of time. Set Preview Range P Lets you drag a box to define a time range for previewing. As long as this range is active, playback will be limited to it, letting you repeatedly view a segment of the animation without having to manually rewind each time. You can change the start or end frame using the corresponding button in the Timeline editor’s Playback popover. Alternatively, you can simply run Set Preview Range again. Clear Preview Range Alt - P Clears the preview range. Set Preview Range to Selected Ctrl - Alt - P Applies a preview range that encompasses the selected strips. Area Area controls. See the user interface documentation for more information. Select Menu ¶ All A Selects all strips. None Alt - A Deselects all strips. Invert Ctrl - I Inverts the current selection. Box Select B Lets you drag a box and selects the strips that are partially or completely inside it. Box Select (Axis Range) Alt - B Lets you drag a box and selects the strips that overlap the corresponding time range, even if they’re above or below the box. Before Current Frame [ Selects all the strips that start before (or on) the current frame. After Current Frame ] Selects all the strips that end after (or on) the current frame. Marker Menu ¶ Markers are used to denote frames with key points or significant events within an animation. Like with most animation editors, they’re shown at the bottom. Markers in animation editor. ¶ For descriptions of the different marker tools, see Editing Markers . Add Menu ¶ Action Shift - A Adds a strip referencing an action to the active track. Transition Shift - T Adds a transition strip between the two selected action strips. Sound Shift - K Adds a strip that controls when the Speaker Objects object plays its sound clip. Selected Objects Makes the selected objects appear in the NLA Editor without adding an action or track to them. See Strips for details on the various strip types. Track Menu ¶ Contains tools for working with NLA tracks. See Editing Tracks for details. Strip Menu ¶ Contains tools for working with NLA strips. See Editing Strips for details. Filters ¶ Only Show Selected Only shows tracks belonging to objects that are selected. Show Hidden Shows tracks from objects that are hidden. Include Missing NLA Shows the Action Track even if there is no action in it. Search Filters the track list by a search term. Filtering Collection Select a collection to only show tracks from objects in that collection. Filter by Type Filter tracks by target type. Sort Data-Blocks Sorts data-blocks alphabetically to make them easier to find. If your playback speed suffers because of this (should only really be an issue when working with lots of objects), you can turn it off. Snap ¶ The toggle button enables/disables automatic strip snapping. The dropdown button shows a popover with the following options: Snap To Type of element to snap to. Frame : Snap to full frames. Second : Snap to seconds. Nearest Marker : Snap to the nearest Marker . Absolute Time Snap When disabled, strips will move in increments of Snap To . For example, if you selected Second and have a strip that currently starts on 0:06+5, dragging it to the right will snap it to 0:07+5. Its time increases by a second, and its subsecond offset of 5 frames remains the same. When enabled, strips will snap to multiples of Snap To . Taking the above example, the strip would snap to 0:07+0, removing the subsecond offset. Playback Controls ¶ The Playback Controls region contains controls and options related to playback, keying, auto keyframing, and transport. These settings allow you to: Control how animations are previewed and synchronized with audio. Insert and manage keyframes through keying sets and auto keying. Navigate the timeline using playback and transport controls. Adjust frame ranges and preview specific segments of the animation. See also For a detailed description of all properties and controls commonly found in the footer, see the Playback Controls documentation. On this page Introduction Main Region Header View Menu Select Menu Marker Menu Add Menu Track Menu Strip Menu Filters Snap Playback Controls



---

## Structured Notes

### Core Technique
The NLA editor animates with **actions** — named, reusable animation segments — instead of individual keyframes, stacking them as **strips on tracks** that layer like image-editor layers, higher over lower, with optional blending.

### Summary
This is the re-timing and re-use layer the gap named, and the concept that makes it legible is the **Action Track**: the top track, highlighted orange, holds the object's *active* action rather than strips, and that is where new keyframes land by default. Other editors — the Dope Sheet in particular — normally show only that active action's keyframes, which is why editing an action already pushed into a strip requires selecting it and pressing **`Tab`** to enter **Tweak Mode**, at which point it appears in both its original track and the Action Track while the active action is temporarily hidden. Around that sit the ordinary editor mechanics worth knowing: **Show Control F-Curves** draws a graph over each strip using Animated Influence, **Realtime Updates** decides whether the 3D Viewport follows a strip as you drag it or only once you let go, **Sync Visible Range** locks horizontal pan and zoom to other time editors, **Local Markers** shows action-local markers (created in the Action Editor) which are useful for aligning strips, and the preview range operators (**`P`**, **`Alt`-`P`**, **`Ctrl`-`Alt`-`P`**) limit playback to a segment.

### Key Steps
1. Think in **actions**, not keyframes — named reusable segments instanced as **Action Strips**.
2. Read the stack like layers: **higher tracks take precedence over lower ones**, or blend them.
3. Identify the **Action Track** (top, orange) — it holds the active action, not strips, and receives new keyframes by default.
4. Select a strip and press **`Tab`** for **Tweak Mode** to edit an action that is not the active one; it shows in both its own track and the Action Track.
5. Navigate with **Frame Selected** (`NumpadPeriod`), **Frame All** (`Home`), **Frame Scene/Preview Range**, and **Go to Current Frame** (`Numpad0`).
6. Toggle **Sidebar** (`N`) and the **Track Region** (Channels); use **Adjust Last Operation** for the pop-up of the last operator's properties.
7. Turn on **Show Control F-Curves** to see the influence graph on strips using Animated Influence, and **Show Markers** / **Show Local Markers** to align strips against Action Editor markers.
8. Set **Realtime Updates** according to whether you want the viewport to follow a drag or update only on release.
9. Use **Use Timecode** (`Ctrl`-`T`) for seconds instead of frames, and **Sync Visible Range** to keep other time editors on the same section.
10. Limit playback with **Set Preview Range** (`P`), clear it (`Alt`-`P`), or fit it to the selection (`Ctrl`-`Alt`-`P`).
11. Select with **`A`** / **`Alt`-`A`** / **`Ctrl`-`I`**, **Box Select** (`B`), **Box Select (Axis Range)** (`Alt`-`B`), and **Before/After Current Frame** (`[` / `]`).

### Nodes / Settings
- **Action** (reusable segment), **Action Strip**, **track**, **Action Track** (top, orange, holds the active action).
- **Tweak Mode** — `Tab` on a selected strip.
- View: Sidebar (`N`), Channels, Playback Controls, Frame Selected (`NumpadPeriod`), Frame All (`Home`), Frame Scene/Preview Range, Go to Current Frame (`Numpad0`), **Realtime Updates**, **Show Control F-Curves**, **Show Markers**, **Show Local Markers**, **Use Timecode** (`Ctrl`-`T`), **Sync Visible Range**.
- Preview range: Set (`P`), Clear (`Alt`-`P`), Set to Selected (`Ctrl`-`Alt`-`P`).
- Select: All (`A`), None (`Alt`-`A`), Invert (`Ctrl`-`I`), Box (`B`), Box Axis Range (`Alt`-`B`), Before (`[`) / After (`]`) Current Frame.

### Difficulty
Intermediate

### Blender Version
Blender 5.2.

### Tags
`nla`, `animation`, `blender-5x`, `intermediate`

---

## Related Tutorials
- [NLA Tracks](nla-tracks.md) — mute, lock, solo, and the Push Down / Pin behaviour of the Action Track.

---

> **Provenance.** Official Blender 5.2 LTS documentation, pinned to the versioned
> path (`docs.blender.org/manual/en/5.2/` and `docs.blender.org/api/5.2/`) rather
> than `latest`, so the entry keeps saying what 5.2 says after `latest` moves on.
> ⚠️ **These pages append site chrome to `<title>`** (" - Blender 5.2 LTS Manual",
> " - Blender Python API"), so `--title` is required when ingesting them.
> **Blender 5.2.1 LTS is installed on this machine** (`D:\Steam\steamapps\common\Blender`,
> build 2026-08-25), so the documented behaviour can be checked against the real
> build rather than taken on trust.
