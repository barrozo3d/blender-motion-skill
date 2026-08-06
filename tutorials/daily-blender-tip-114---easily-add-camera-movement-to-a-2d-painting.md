---
title: Daily Blender Tip 114 - Easily Add Camera Movement To A 2D Painting
source: YouTube
url: https://www.youtube.com/watch?v=KMcdkXGBTo8
author: Blender Secrets
ingested: 2026-08-04
blender_version: "Not specified — Images as Planes add-on + Shape Keys, version-agnostic core workflow"
tags: [animation, camera, materials, motion-design, beginner]
extraction_status: complete
frames_dir: tutorials/frames/daily-blender-tip-114---easily-add-camera-movement-to-a-2d-painting/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Daily Blender Tip 114 - Easily Add Camera Movement To A 2D Painting

**Source:** [YouTube](https://www.youtube.com/watch?v=KMcdkXGBTo8)
**Author:** Blender Secrets
**Duration:** 1m34s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'ADD MOVEMENT TO A PAINTING'
- **CRITICAL:** Empty transcript in chapter 'It's easy to add movement to a picture with depth.'
- **CRITICAL:** Empty transcript in chapter 'These are just two planes that are being skewed.'
- **CRITICAL:** Empty transcript in chapter 'To keyframe it, I am using Shape Keys.'
- **CRITICAL:** Empty transcript in chapter 'From the side you can see they are just flat planes.'
- **CRITICAL:** Empty transcript in chapter 'I used the Import images as planes add-on.'
- **CRITICAL:** Empty transcript in chapter 'It can be activated in the user preferences'
- **CRITICAL:** Total transcript only 3 chars (min 500). Captions unavailable or audio silent — extraction will be poor.
- WARNING: Very short transcript (3 chars) in 'The car in the foreground is a PNG with alpha channel.'

---


Frames captured — see "Captured Frames" section below.


### ADD MOVEMENT TO A PAINTING [0:00]

### It's easy to add movement to a picture with depth. [0:11]

### These are just two planes that are being skewed. [0:21]

### To keyframe it, I am using Shape Keys. [0:31]

### From the side you can see they are just flat planes. [0:43]

### I used the Import images as planes add-on. [0:54]

### It can be activated in the user preferences [1:04]

### The car in the foreground is a PNG with alpha channel. [1:21]
**Transcript (timestamped):**
[1:30] Dr.



---

## Captured Frames

- [0:11] tutorials/frames/daily-blender-tip-114---easily-add-camera-movement-to-a-2d-painting/frame_000.jpg
- [0:21] tutorials/frames/daily-blender-tip-114---easily-add-camera-movement-to-a-2d-painting/frame_001.jpg
- [0:31] tutorials/frames/daily-blender-tip-114---easily-add-camera-movement-to-a-2d-painting/frame_002.jpg
- [0:43] tutorials/frames/daily-blender-tip-114---easily-add-camera-movement-to-a-2d-painting/frame_003.jpg
- [0:54] tutorials/frames/daily-blender-tip-114---easily-add-camera-movement-to-a-2d-painting/frame_004.jpg
- [1:22] tutorials/frames/daily-blender-tip-114---easily-add-camera-movement-to-a-2d-painting/frame_005.jpg

---

## Structured Notes

### Core Technique
A cheap "2.5D parallax" effect for a still 2D painting: the artwork is split into a couple of flat image planes (background scene + a foreground PNG cutout with alpha), each skewed via a Shape Key so that animating the shape key's value creates a fake sense of depth and camera movement without any real 3D geometry. Note: this video's audio track is silent/near-empty; this summary is built entirely from the captured on-screen text captions and frames.

### Summary
Frame 000 shows the target artwork viewed through the Camera: a stylized painted scene (a couple sitting on a pink car under a pastel sky), captioned "It's easy to add movement to a picture with depth." Frame 001 shows the same shot with the camera's safe-area guides visible and the underlying plane's rotated/skewed silhouette outline just visible at the frame edges, captioned "These are just two planes that are being skewed." Frame 002 shows the Shape Keys panel open in the sidebar on the "background" plane object (Basis + "Key 1" shape key, Value 0.114, Range Min 0/Max 1) — captioned "To keyframe it, I am using Shape Keys," confirming the skew amount is what gets keyframed. Frame 003 shows a side/orthographic view revealing the trick clearly: the background artwork is just a single flat plane in 3D space, tilted away from camera, captioned "From the side you can see they are just flat planes." Frame 004 shows the same side view with the Shape Keys panel still open, captioned "I used the Import Images as Planes add-on" — the add-on used to bring each image into the scene as a plane with the image mapped as its material. Frame 005 shows the foreground car/couple element as its own separate plane object ("background.001," also with a Shape Keys panel), positioned in front of the background plane, captioned "The car in the foreground is a PNG with alpha channel" — confirming the foreground cutout uses image transparency to only show the car/subjects, letting the background plane show through around it.

### Key Steps
1. Prepare the source artwork as at least two separate image layers: a full background painting, and a foreground element exported as a PNG with an alpha channel (transparent background) so only the desired subject/cutout is opaque.
2. Enable the **Import Images as Planes** add-on (Preferences > Add-ons) and use it to bring each image into the scene — each becomes its own flat plane object with the image applied as a material, and the PNG's alpha channel is respected for transparency on the foreground piece.
3. Position the foreground plane in front of the background plane along the camera's view axis, so from the camera's perspective they combine into one flat-looking composited image.
4. On each plane, add a **Shape Key** and use it to skew the plane's geometry (e.g. shearing one edge relative to the other) — this is purely a per-plane shape distortion, not a real 3D rotation.
5. Animate the Shape Key's Value (0 to 1) over time to keyframe the skew amount — since the two planes are offset in depth (Z distance from camera) and skew independently, animating this creates a convincing faked parallax/depth-movement effect as if the camera were subtly moving through the scene, even though everything is flat 2D artwork on planes.
6. Viewing the setup from the side (orthographic) reveals the trick plainly: both elements are just flat planes in 3D space — the illusion only works from the camera's specific viewing angle.

### Nodes / Settings
- **Add-on:** Import Images as Planes (Preferences > Add-ons) — imports an image directly as a textured plane object, respecting PNG alpha for transparency.
- **Shape Keys:** Basis + one additional key per plane (e.g. "Key 1"), Value animated 0-1 to drive a skew/shear distortion of the plane's geometry over time.
- **Scene setup:** multiple depth-offset planes (background + foreground alpha cutout) viewed through a single Camera to combine into one flat-looking composited shot.

### Difficulty
Beginner

### Blender Version
Not specified — Images as Planes add-on and Shape Keys are a version-agnostic core Blender workflow.

### Tags
animation, camera, materials, motion-design, beginner

---

## Related Tutorials
- [Creating a Realistic Forest in Blender using Billboards (low poly Planes with tree images)](creating-a-realistic-forest-in-blender-using-billboards-low-poly-planes-with-tre.md) — shares camera, beginner; both use the Images as Planes add-on to turn 2D artwork into camera-facing scene elements, here for depth animation rather than particle-scattered billboards.
