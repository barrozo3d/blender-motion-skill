---
title: Create Text in Geometry Nodes! (Blender Tutorial)
source: YouTube
url: https://youtu.be/qrYmDg0HpYI
author: Ryan King Art
ingested: 2026-05-13
blender_version: "Blender 4.x"
tags: [geometry-nodes, typography, animation, procedural, particles-reveal, beginner, intermediate]
---

# Create Text in Geometry Nodes! (Blender Tutorial)

**Source:** [YouTube](https://youtu.be/qrYmDg0HpYI)
**Author:** Ryan King Art
**Ingested:** 2026-05-13

---

## Description

*In this Blender tutorial I will show you how to create text with Geometry Nodes.*

🗃️ *Purchase the project files and support the channel:*
• Gumroad: https://ryankingart.gumroad.com/l/text
• Patreon: https://www.patreon.com/posts/156394906

▶️ *Geometry Nodes Playlist:* https://www.youtube.com/playlist?list=PLsGl9GczcgBsv58A4sTYSmLDhipykRS4O
▶️ *1001 Fonts:* https://www.1001fonts.com/

✅ *Help Support the Channel:*
• Patreon: https://www.patreon.com/ryankingart
• Gumroad: https://ryankingart.g

---

## Raw Content (for analysis)

Kind: captions Language: en In this Blender tutorial, I'll show you how to create text with geometry nodes by using the string to curves node. So, in this tutorial, I'll first show you the basics of how to add text in geometry nodes and the different settings to customize the text. I'll show you how to add thickness to the text. [music] I'll show you how to add a cool wireframe effect. I'm also going to show you how to extrude the text so it has some thickness. And then I'll show you some cool examples that you can do with the geometry nodes to customize text to make, for example, random rotation, random location, and random scale for the letters. Then going to show you how to use geometry nodes to create a cool animated particle effect with the text. And then finally, at the end of the video, I'll show you how to make another really cool animation where we randomly animate the location, rotation, scale of the text to get this really cool bubbly animated text with geometry nodes. And if you'd like to purchase the tutorial project files and support the channel, then you can purchase them with the links in the description on my Gumroad store and Patreon page. So, with a completely new scene in Blender, I'm just going to select everything, so hit A to select everything. Now, I'll hit X and just delete everything cuz, you know, you can't use the default cube. Let's now hit Shift A for the add menu, and I'm just going to add a new cube. So, now what I'm going to do is click here to go to the geometry nodes workspace, and I'm going to click on new to add new geometry nodes. Now, because text is horizontal, I'm going to change the window layout so we have more space. So, what I'm going to do is click right here in the corner when the crosshair appears, and I'm going to click and drag down to split the window. And then what I'm going to do is click, drag over, and let go just to close that. And then right here, I'll click, drag over, and then let go just to close that. So, now we have a nice horizontal view here for our text, and then we have a nice large area for our geometry nodes. Now, to add text to geometry nodes, we want to hit Shift A for the add menu, and we want to search for string, and we want to search for string to curves. So, here it is, utilities, text, string to curves. Now, if I try to drop this right here in between the input and output, I can't actually drop it here in this wire, and that's because we don't actually want to use the group input because that's the geometry of the cube. what I'm going to do is just take the curve instances, and we're going to put that into the geometry. So, now the cube has disappeared because we're not using the original geometry, we're using the string to curves, which is going to be text. Now, here on the string, this is where you can type in whatever text. So, I can just type in Blender, and then you can see here if I hit seven on the numpad to go to top view, there is the text called Blender. Now, I want to add spaces and make this a bit longer so that I can show you more examples. So, I'm just going to call this geometry nodes text and hit enter. Then there's also a size value, so this is very straightforward. You can just change the size of the text. And then there's also a font, so you can actually choose a font to add to the text. So, I'll click on this file icon. So, if you're looking for some really great free fonts, I really like using a website called 1001fonts.com. I'll have a link to it in the video description. So, if you don't have any fonts, you can definitely check that out. What I'm going to do is just add this font here from 1001fonts.com. I'll just click on that, double click on it to add it in. And now we have a different font there for our text instead of the default Blender font. I actually think the default Blender font is pretty ugly, so I definitely like using a different font. Now, what I can also do is open up these arrows so we have text box, spacing, and alignment to change these settings for the text. So, you can see there's alignment, so there's like left or center or like right. What I'm going to do is just change it to center cuz that makes the most sense, so it's kind of in the center there of the object. You can also choose where the line of text is going to be. So, if I click right here, I'm just going to change it to middle, but you could also make it like bottom baseline, or you could make it like the bottom, or whatever you want to do. For me, middle makes the most sense, so it's just in the very center middle of the object. Then there's also the pivot point, and the pivot point is definitely going to be useful later when we animate the text because, for example, when we rotate the text, depending on the pivot point, depending on the pivot point location, it's going to determine where the text is going to rotate. So, I'm just going to leave it at midpoint, but you could change it to these other values, and we will go over this later, but for most things, I just leave it to midpoint, so it's going to be the very center of the text. Then there's also spacing, and so this is very straightforward. There's the character spacing, which is for each letter. Then there's also the word spacing, so when there's a space there in between the words, that's going to make that bigger or smaller. Then there's also line spacing, which we'll be covering in a moment. But the line spacing, you can't really see it changing right now cuz we haven't actually added multiple lines. Then there's also the text box. So, with the text box, there's a few different settings. First, there's overflow, which allows you to change the width. So, if I just drag this width value up, now you can see that each word here is on a separate line. So, now I can go back here to the line spacing, and I can drag the line spacing up and down, and each word is on a separate line. So, overflow is probably the easiest to use because, like if I just click he

---

## Structured Notes

*Fill in manually or ask Claude to analyze:*
> "Analyze the content of tutorials/create-text-in-geometry-nodes-blender-tutorial.md and extract:
> - Core Blender technique taught
> - Step-by-step workflow
> - Key nodes or settings
> - Blender version
> - Difficulty level
> - Tags"

### Core Technique
Creating and animating text entirely within Geometry Nodes using the String to Curves node, covering typography controls, extrusion, wireframe effects, and per-letter random transforms and particle animations.

### Key Steps
1. Add a cube as the host object; open Geometry Nodes workspace and click New; disconnect the Group Input from the output (don't use the original cube geometry).
2. Shift+A > Utilities > Text > String to Curves; plug Curve Instances into the Group Output geometry socket.
3. Type text in the String field; set Size and load a custom font file (e.g., from 1001fonts.com) via the font file picker.
4. Open text settings: set Alignment to Center, Vertical Alignment to Middle, Pivot Point to Midpoint for animation pivoting.
5. Adjust Spacing (character spacing, word spacing, line spacing); use Text Box Overflow and Width to control line wrapping.
6. Add thickness: use a Fill Curve node then an Extrude Mesh node on the filled text.
7. Create a wireframe effect: use a Wireframe node on the filled text geometry.
8. For per-letter random transforms: use an Instance on Points approach with Random Value nodes driving Scale, Rotation, and Location on each letter instance.
9. For animated particle reveal: use a combination of Distribute Points on Faces and Instance on Points with a time-based mask.
10. For bubbly animated text: keyframe random Location, Rotation, and Scale values changing per letter using Index-based random seeds driven by the current frame.

### Blender Nodes / Settings
- String to Curves node (String input, Size, Font file, Alignment, Pivot Point)
- Fill Curve node
- Extrude Mesh node (thickness)
- Wireframe node
- Instance on Points node
- Random Value node (per-letter variation)
- Text Box settings: Overflow, Width, Character/Word/Line Spacing
- Distribute Points on Faces node

### Difficulty
Beginner

### Blender Version
Not specified

### Tags
#geometry-nodes #typography #animation #procedural #particles-reveal #beginner #intermediate
