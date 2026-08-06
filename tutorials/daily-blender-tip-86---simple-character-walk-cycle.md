---
title: Daily Blender Tip 86 - Simple Character Walk Cycle
source: YouTube
url: https://www.youtube.com/watch?v=-QCqVZVwwvM
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Paste Pose Flipped (Ctrl+Shift+V) and standard Pose Mode keyframing are version-agnostic core Blender animation tools"
tags: [rigging, character, animation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-86---simple-character-walk-cycle/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 86 - Simple Character Walk Cycle

**Source:** [YouTube](https://www.youtube.com/watch?v=-QCqVZVwwvM)
**Author:** Blender Secrets
**Duration:** 2m1s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Total transcript only 6 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (6 chars) in 'Full Content'

---


Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[2:00] Sample



---

## Captured Frames

- [0:08] tutorials/frames/daily-blender-tip-86---simple-character-walk-cycle/frame_000.jpg
- [0:30] tutorials/frames/daily-blender-tip-86---simple-character-walk-cycle/frame_001.jpg
- [0:55] tutorials/frames/daily-blender-tip-86---simple-character-walk-cycle/frame_002.jpg
- [1:20] tutorials/frames/daily-blender-tip-86---simple-character-walk-cycle/frame_003.jpg
- [1:40] tutorials/frames/daily-blender-tip-86---simple-character-walk-cycle/frame_004.jpg
- [1:55] tutorials/frames/daily-blender-tip-86---simple-character-walk-cycle/frame_005.jpg

---

## Structured Notes

### Core Technique
Part 3 of the rigging series: building a basic walk cycle on the Rigify-rigged character from [Part 1](daily-blender-tip-84---rigging-a-simple-character-part-1.md)/[Part 2](daily-blender-tip-85---rigging-a-simple-character-part-2.md) using just four key poses (Contact, Passing/Down, Passing/Up, and the mirrored Contact) — leaning heavily on **Ctrl+C / Ctrl+Shift+V (Paste Pose Flipped)** to mirror each pose onto the opposite leg instead of hand-posing both sides.

### Summary
Frame 000 shows the character in side (Numpad 3 / Ctrl+3) view posed with one leg forward and one back (a classic **Contact pose**), the Dope Sheet showing a first keyframe column, captioned "Go to the side view (3 or ctrl+3 on your numpad) and start posing the first 'contact pose'. Set a key with 'i'." Frame 001 shows the pose selected and copied, the Dope Sheet now showing keys added further along the timeline (frame 17), captioned "Copy the pose (select all, ctrl+c) and go to frame 17, paste it mirrored: Ctrl+Shift+V. Set a key with 'i'." — creating the second Contact pose (opposite leg forward) via mirrored paste instead of re-posing. Frame 002 shows the character crouched low, mid-stride with legs crossing under the body, captioned "Set the 'down' pose on frame 5. It's the pose where the character is the lowest in a walk cycle. Set key." Frame 003 shows the character at its tallest, weight balanced on one leg mid-step, captioned "Set the 'up' pose on frame 13. It's the pose where the character is the highest in a walk cycle. Set key." Frames 004–005 show the character walking with a natural alternating stride, a dense Dope Sheet full of keyframes, both captioned "On each key, ctrl+c and ctrl+shift+v to mirror the pose and then set a key with 'i'. Check the animation." — confirming every pose in the cycle (Down, Up, and their mirrored counterparts) was built the same copy-and-mirror-paste way.

### Key Steps
1. Switch to **Side view** (Numpad 3 or Ctrl+Numpad3) for clear silhouette posing of a walk cycle.
2. Pose the first **Contact pose** (one leg forward, one back, both touching or near the ground) at frame 1, then press **I** to insert a keyframe.
3. With the pose selected, **Ctrl+C** to copy it, jump ahead on the timeline (e.g. frame 17), and **Ctrl+Shift+V** (**Paste Pose Flipped**) to paste a left-right mirrored version — this becomes the second Contact pose (opposite leg now forward) without manual re-posing. Key with **I**.
4. Pose the **Down** position (the character's lowest point in the cycle, legs crossing mid-stride) around frame 5, and key it.
5. Pose the **Up** position (the character's highest point, balanced on one leg) around frame 13, and key it.
6. For every subsequent key in the cycle, repeat the **Ctrl+C / Ctrl+Shift+V** mirrored-paste trick from the corresponding earlier pose rather than re-posing from scratch, then key with **I** — this keeps the left/right stride symmetric with minimal manual work.
7. Scrub/play back to check the walk reads correctly (natural weight shift between Down/Up/Contact poses) before refining timing further.

### Nodes / Settings
- **View:** Numpad 3 / Ctrl+Numpad3 — Side Orthographic, ideal for silhouette-based walk-cycle posing.
- **Shortcut:** I — Insert Keyframe (Pose Mode, on selected bones/whole rig).
- **Shortcut:** Ctrl+C then Ctrl+Shift+V — Copy Pose, then Paste Pose Flipped (mirrors the pose left-right).
- **Key poses used:** Contact (start), Down (lowest point), Up (highest point), mirrored Contact (repeat).

### Difficulty
Intermediate

### Blender Version
Not specified — Paste Pose Flipped (Ctrl+Shift+V) and standard Pose Mode keyframing are version-agnostic core Blender animation tools.

### Tags
rigging, character, animation, intermediate

---

## Related Tutorials
- [Daily Blender Tip 85 - Rigging A Simple Character Part 2](daily-blender-tip-85---rigging-a-simple-character-part-2.md) — shares rigging, character, animation; this is the direct Part 3 continuation, animating the exact rig cleaned up in Part 2 with a basic walk cycle.
- [Daily Blender Tip 84 - Rigging A Simple Character Part 1](daily-blender-tip-84---rigging-a-simple-character-part-1.md) — shares rigging, character, animation; Part 1 of the same series, providing the original Rigify meta-rig setup this walk cycle is built on.
- [Daily Blender Tip 87 - Adding Props To Your Character (like a stylish hat)](daily-blender-tip-87---adding-props-to-your-character-like-a-stylish-hat.md) — shares rigging, character, animation; continues the same character rig, adding a bone-parented prop after this tutorial's walk cycle.
