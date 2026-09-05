---
title: Editing Motion Tracks
source: Article
url: https://docs.blender.org/manual/en/5.2/movie_clip/tracking/clip/editing/track.html
author: docs.blender.org (Blender 5.2 LTS official docs)
ingested: 2026-09-04
blender_version: "Blender 5.2"
tags: [tracking, camera-tracking, blender-5x, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/editing-motion-tracks/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Editing Motion Tracks

**Source:** [Article](https://docs.blender.org/manual/en/5.2/movie_clip/tracking/clip/editing/track.html)
**Author:** docs.blender.org (Blender 5.2 LTS official docs)
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)


Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Track ¶ Transform ¶ Track Motion ¶ The Track Motion menu is used to perform tracking of selected tracks (i.e. following the selected feature from frame to frame). This operator depends on settings from the Tracking Settings panel. If during sequence tracking the algorithm fails to track some markers, they will be disabled and tracking will continue for the rest of the markers. If the algorithm fails when tracking frame-by-frame, the marker is not disabled, and the most likely position of the feature on the next frame is used. Backwards ¶ Reference Mode : Tracking Menu : Track ‣ Track Motion ‣ Backwards Shortcut : Shift - Ctrl - T Tracks the motion backward along the sequence. Frame Backwards ¶ Reference Mode : Tracking Menu : Track ‣ Track Motion ‣ Frame Backwards Shortcut : Alt - Left Tracks the motion backward by one frame. Forwards ¶ Reference Mode : Tracking Menu : Track ‣ Track Motion ‣ Forwards Shortcut : Ctrl - T Tracks the motion forward along the whole sequence. Frame Forwards ¶ Reference Mode : Tracking Menu : Track ‣ Track Motion ‣ Frame Forwards Shortcut : Alt - Right Tracks the motion forward one frame. Clear ¶ Before ¶ Reference Mode : Tracking Menu : Track ‣ Clear ‣ Before Shortcut : Shift - T Deletes all tracked and keyframed markers after the current frame for all selected tracks. Clear Active Limits clear action to only active track (as opposite to all selected ones). After ¶ Reference Mode : Tracking Menu : Track ‣ Clear ‣ After Shortcut : Alt - T Deletes all tracked and keyframed markers before the current frame for all selected tracks. Clear Active Limits clear action to only active track (as opposite to all selected ones). Track Path ¶ Reference Mode : Tracking Menu : Track ‣ Clear ‣ Track Path Shortcut : Shift - Alt - T Clears all markers except the current one from all selected tracks. Clear Active Limits clear action to only active track (as opposite to all selected ones). Clear Solution ¶ Refine ¶ This operator will run a tracker from previous keyframe to current frame for all selected markers. Current markers positions are considering initial position guess which could be updated by a tracker for better match. Useful in cases when feature disappears from the frame and then appears again. Usage in this case is the following: When feature point re-appeared on frame, manually place marker on it. Use Refine Markers operation to allow tracker to find a better match. Depending on direction of tracking use either Forwards or Backwards refining. Accordingly if tracking happens forwards, use Refine Forwards , otherwise use Refine Backwards . Backwards ¶ Reference Mode : Tracking Menu : Track ‣ Refine ‣ Backwards Refine the track backwards. Forwards ¶ Reference Mode : Tracking Menu : Track ‣ Refine ‣ Forwards Refine the track forwards. Add Marker ¶ Reference Mode : Tracking Menu : Track ‣ Add Marker Places a new marker at the position of the mouse (which is under the button in this case, not ideal but it is just how things work) and then it can be moved to the needed location. When it is moved to the desired position, LMB can be used to finish placing the new marker. Also, Return and Spacebar can be used to finish placing the marker. But it is faster to use Ctrl - LMB to place markers directly on the footage. This shortcut will place the marker in the place you have clicked. In addition to this until you have released the mouse button, you can adjust the marker position by moving the mouse and using the track preview widget to control how accurately the marker is placed. Detect Features ¶ Reference Mode : Tracking Menu : Track ‣ Detect Features Detects all possible features on the current frame and places markers at these features. This operator does not take other frames into account, so it might place markers on features which belong to moving objects. If the camera is turning away from this shot, no markers could be present within the frames after the camera moved away. There are several properties for this operator: Placement Controls where to place markers. Whole Frame Places markers throughout the whole frame. Inside Annotated Area Places markers inside the area outlined with the Annotation Tools . This can be used to outline some areas with interesting features and place markers only inside the outlined area. Outside Annotated Area Places markers outside the area outlined with the Annotation Tools . This can be used to outline areas of no interest (like trees, humans, etc.) and place markers outside of these areas. Margin Controls the distance from the image boundary for created markers. If markers are placed too close to the image boundary, they will fail to track really quickly and they should be deleted manually. To reduce the amount of manual clean-up, this parameter can be used. Threshold Limits minimal threshold for placing markers. This value comes from the feature detection algorithm and it means: low values means most probably this feature would fail to track very soon, high value means it is not much such track. Amount of markers to be added can be controlled with this value. Distance Defines the minimal distance between placed markers. It is needed to prevent markers from being placed too close to each other (such placement can confuse the camera solver). Create Plane Track ¶ Reference Mode : Tracking Menu : Track ‣ Create Plane Track The Create Plane Track operator creates a new plane track. Planar tracking takes advantage of the fact that there are often planar surfaces in footage, by attaching markers to points on these flat planes. It can be used to replace things like billboards and screens on the footage with another image or video. It also might be used for masking. This button will create a plane object which is deforming in the same way as plane defined by all selected point tracks. At least four feature points tracked across the footage which belongs to the plane you want to replace are needed. More tracks will give better estimation of plane motion. Feature points used to estimate plane motion could be used from any place on the plane, meaning it’s not necessarily need to be corners. Corners are not always easy to be tracked, they might be occluded. In this case you can position tracked features that lay on the same plane far away from the actual plane which should be replaced. This provides more information about the possible deformation of the marker in following frames, and such markers can be tracked even if partially occluded (appear and disappear during the time). It is only required that two neighbor frames have at least four common tracks. An image can be projected onto the plane with the Plane Track Deform Node compositing node. Solve Camera/Object Motion ¶ Reference Mode : Tracking Menu : Track ‣ Solve Camera/Object Motion The Solve Camera/Object Motion operator solves the motion of the camera or the selected tracked object , using all tracks placed on the footage and two keyframes specified on this panel. There are some requirements: There should be at least eight common tracks on the both of the selected keyframes. There should be noticeable parallax effects between these two keyframes. If everything goes smoothly during the solve, the average reprojection error is reported to the information space and to the Clip editor header. Reprojection error means the average distance between reconstructed 3D position of tracks projected back to footage and original position of tracks. Basically, reprojection error below 0.3 means accurate reprojection, (0.3 - 3.0) means quite nice solving which still can be used. Values above 3 means some tracks should be tracked more accurately, or that values for focal length or distortion coefficients were set incorrectly. Join Tracks ¶ Reference Mode : Tracking Menu : Track ‣ Join Tracks Shortcut : Ctrl - J This operator joins all selected tracks into one. Selected tracks should not have common tracked or keyframed markers at the same frame. Average Tracks ¶ Reference Mode : Tracking Menu : Track ‣ Average Tracks The Average Tracks operator creates a new tracking marker by averaging the data from the selected tracks. This can be used to improve stability of tracking on blurry or non-very-sharp feature shapes. The operator takes into account all Marker properties however, disabled markers do not affect the averaging. Gaps in the original tracks will be linearly interpolated, to reduce result track jump. Note that this only applies to gaps “in between”. This means that if a track does not have markers in the beginning or end of it, there is nothing to interpolate with and the resulting track will jump. Keep Original When enabled, the selected tracks are not deleted. Copy Tracks ¶ Paste Tracks ¶ Animation ¶ Show/Hide ¶ Clean Up ¶ Clean Tracks ¶ Reference Mode : Tracking Menu : Track ‣ Clean Up ‣ Clean Tracks Identifies all tracks which match settings from above and performs desired action on them. Tracked Frames Tracks or tracked segments shorter than this number of frames will be removed. Reprojection Error Tracks which have reprojection error higher than this value will be removed. Action Several actions can be performed for bad tracks. Select They can simply be selected. Delete Track The whole track can be deleted. Delete Segments Bad segments of tracked sequence can be removed. Filter Tracks ¶ Reference Mode : Tracking Menu : Track ‣ Clean Up ‣ Filter Tracks This operator deletes obviously bad tracks (for example, the ones which are too short). Additionally, it identifies tracks which have suspicious spikes in their motion and selects them. Delete Track ¶ Reference Mode : Tracking Menu : Track ‣ Delete Track Shortcut : X Delete all selected tracks. Delete Marker ¶ Reference Mode : Tracking Menu : Track ‣ Delete Marker Shortcut : Shift - X On this page Track Transform Track Motion Backwards Frame Backwards Forwards Frame Forwards Clear Before After Track Path Clear Solution Refine Backwards Forwards Add Marker Detect Features Create Plane Track Solve Camera/Object Motion Join Tracks Average Tracks Copy Tracks Paste Tracks Animation Show/Hide Clean Up Clean Tracks Filter Tracks Delete Track Delete Marker



---

## Structured Notes

### Core Technique
Drive the 2D tracking pass from the **Track** menu — track forwards, backwards or one frame at a time, clear bad segments in either direction, and **Refine** a marker you have repositioned by hand.

### Summary
This is the day-to-day tracking work, and the useful detail is how failure behaves differently depending on how you track. During **sequence** tracking, markers the algorithm loses are **disabled** and tracking continues for the rest; during **frame-by-frame** tracking the marker is **not** disabled and the most likely position on the next frame is used instead. That difference decides which mode to use on difficult footage. The **Clear** operators are directional and easy to invert in memory — **Clear › Before** deletes tracked and keyframed markers *after* the current frame, **Clear › After** deletes them *before* it — with **Clear Active** limiting the action to the active track rather than all selected ones, and **Track Path** clearing every marker except the current one. **Refine** is the recovery tool for an occlusion: when a feature reappears, place the marker on it manually, then run Refine (Forwards or Backwards to match your tracking direction) so the tracker treats your placement as an initial guess and finds the better match.

### Key Steps
1. Track a whole sequence with **Track › Track Motion › Forwards** (`Ctrl`-`T`) or **Backwards** (`Shift`-`Ctrl`-`T`); tracking obeys the **Tracking Settings** panel.
2. Step one frame at a time with **Frame Forwards** (`Alt`-`Right`) or **Frame Backwards** (`Alt`-`Left`) where the footage is difficult.
3. Know the failure difference: sequence tracking **disables** lost markers and carries on; frame-by-frame tracking keeps the marker and guesses the most likely next position.
4. Trim a bad tail with **Clear › Before** (`Shift`-`T`) — which deletes markers **after** the current frame — or a bad head with **Clear › After** (`Alt`-`T`), which deletes markers **before** it.
5. Add **Clear Active** to restrict a clear to the active track instead of every selected one.
6. Use **Clear › Track Path** (`Shift`-`Alt`-`T`) to strip a track back to the current marker alone.
7. Recover from an occlusion with **Refine**: place the marker by hand on the frame where the feature reappears, then run **Refine Forwards** or **Refine Backwards** to match your tracking direction — the tracker runs from the previous keyframe to the current frame using your placement as the initial guess.

### Nodes / Settings
- **Track › Track Motion**: Forwards (`Ctrl`-`T`), Backwards (`Shift`-`Ctrl`-`T`), Frame Forwards (`Alt`-`Right`), Frame Backwards (`Alt`-`Left`).
- **Track › Clear**: Before (`Shift`-`T`, deletes *after* the frame), After (`Alt`-`T`, deletes *before* it), Track Path (`Shift`-`Alt`-`T`), Clear Solution; **Clear Active** modifier.
- **Refine** — Forwards / Backwards; runs from the previous keyframe to the current frame treating the current position as a guess.
- Depends on the **Tracking Settings** panel.

### Difficulty
Intermediate

### Blender Version
Blender 5.2.

### Tags
`tracking`, `camera-tracking`, `blender-5x`, `intermediate`

---

## Related Tutorials
- [Solving Camera Motion](solving-camera-motion.md) — Cleanup by reprojection error, which consumes these tracks.
- [Motion Tracking Introduction](motion-tracking-introduction.md) — where this sits in the whole workflow.

---

> **Provenance.** Official Blender 5.2 LTS documentation, pinned to the versioned
> path (`docs.blender.org/manual/en/5.2/` and `docs.blender.org/api/5.2/`) rather
> than `latest`, so the entry keeps saying what 5.2 says after `latest` moves on.
> ⚠️ **These pages append site chrome to `<title>`** (" - Blender 5.2 LTS Manual",
> " - Blender Python API"), so `--title` is required when ingesting them.
> **Blender 5.2.1 LTS is installed on this machine** (`D:\Steam\steamapps\common\Blender`,
> build 2026-08-25), so the documented behaviour can be checked against the real
> build rather than taken on trust.
