---
title: Math x Blender 5.0 = UNLIMITED POWER!
source: YouTube
url: https://www.youtube.com/watch?v=EvWAcSA86fw
author: MTR Animation
ingested: 2026-05-18
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/math-x-blender-50-unlimited-power/
frame_count: 0
---

# Math x Blender 5.0 = UNLIMITED POWER!

**Source:** [YouTube](https://www.youtube.com/watch?v=EvWAcSA86fw)
**Author:** MTR Animation
**Duration:** 34m18s | 12 section(s)

---

## Raw Data (for Claude Code extraction)


### The Apollonian Gasket [0:00]
**Transcript:** This is the Apollonian Gasket. It's a mathematical phenomenon that starts with just three circles  and repeatedly adds new circles in the gaps between them. And at first this might seem  like a simple process until you look at the complex mathematics behind this. And that complexity  is exactly what inspired me to recreate this structure using Blender's geometry notes.


### Create first 3 circles [0:40]
**Transcript:** So let me show you how that is done. And in this tutorial we are going to use a lot of complex  formulas. And if we would add those formulas in one by one, note by note, then this tutorial  is going to take like hours and to be honest I don't think that's really needed. So I did some  pre-work. So if you go into the link in description, they will find a blend of file which contains  note groups that already implement the formulas that we're going to use. So download that and open  it up and then we can get started. And as always what we're going to start off with is clicking  on the cube and create a new geometry notes for this. And we're going to remove the group input  because we do not need the default cube. And also let's actually remove this light and let's move  the camera a bit to the side. We don't really need it for now. And the thing that we want to create  first is we want to create the structure of one circle that goes like this one big circle.  And then we want to create two smaller circles just like this in between it. And this we are going  to create with three points. So if we do a points note and this is going to be the bigger point  and the smaller points we want ...


### Radius of 4th point [5:08]
**Transcript:** adding in a fourth circle in between the gaps of the other three circles. And that we are going to do  in three steps. Step one is of course add that fourth circle in geometry notes and the second step  is to determine what should be the radius of this new point and then the third step is to determine  the position of that point. But let's start with the radius and the radius we are going to determine  that with these formulas. So you see the radius of this new circle is one divided by K. K is the  curvature that this new circle should have. And to calculate the curvature of this new circle we  need this bigger formula over here. You see K4 is the curvature of the new circle but then you see we  also need K1, K2 and K3 and those are the curvatures of this circle and this circle and this circle.  And to calculate the curvature of those three circles we need this formula. So let's calculate the  curvature of those circles first and we're going to do that by doing a store named attribute note  which we set on K. And you see this K value should be one divided by the radius of that circle.  So let's do a radius note with also a math note set on divide and let's do one divided by that ra...


### The Product Everyone Needs!!! [10:13]
**Transcript:** However before we do that I want to talk to you about something else because I can completely  understand if you're looking at these notes that you're thinking oh my god what is all of this?  How am I ever going to learn all these notes? I wish there was just some place in which I can  just learn every single note in geometry notes in a very easy and chill way. But then I have good  news for you because I released the big notebook. It's a book that explains every single note in  geometry notes in a very easy and chill way. The book starts from the very basics of geometry notes  and over the course of almost 300 pages it goes to more advanced techniques. The book is  available on my gumroad and it has been fully upgraded to blend the five point out so every new  note has been added in. And if you use the code math you'll get 25% off of your purchase. So if you


### Position of 4th point [10:59]
**Transcript:** want to expand your knowledge in geometry notes I recommend getting this book today and with that  being said let's continue the tutorial. Next up is we're going to calculate the position of this  new point and that we're going to do with this formula and it's formula it looks like a lot but if  you look closely you see that it looks similar to the formula for the curvature. So we have this part  and also a square root part and the k1, k2 and k3 are also going back. However you also see z1,  2 and 3 and z values over here represent the position of the three circles in complex form.  And a complex number is basically a simple way to store a 2d vector as a single value. And in this we  have the real part which represents the x position of each point and we have an imaginary part which  represents the y position of each point. And operations like multiplying two complex numbers or  taking the square root of a complex number work a little bit different than doing those things with  normal numbers. But rest assured I will make that all clear in a moment. Let's first focus on  this formula and this formula I also already implemented as a node group in this blend of file.  So if you do ne...


### More... and more... and more point... [15:12]
**Transcript:** we have the fourth circle the next step is to add more and more and more and more circles in the  gaps between. So let's start by adding in a circle over here, over here and over there.  So let's focus first on this middle circle over here. So let's make a bit more space. And this  new circle what we want to do is we want to apply this set of formulas to this point and this point  and this point to calculate the radius and the position of this point. So we need to get rid of  the bigger circle for now. And to do that we are going to do the lead geometry nodes and we want to  delete the point if it has an index equal to zero. So if we do a compare node set to integer we  can say if it's equal to zero then delete it. And you see we only have those circles. For those  three circles let's do this entire thing again. So let's do shift the it over here and let's  make some space and let's connect this one over there and let's connect this one over there.  Then you will see we have perfectly created that circle which you will also see that if I set this  on one then it will take this circle this circle on the bigger circle and it doesn't really work  but don't worry about it yet we're goi...


### Remove wrong points [20:45]
**Transcript:** that's really cool however we still have to get rid of those wrong points so in order to remove  the wrong points we want to check something and do that let's actually put the iterations lower to  this so what we want is we want to remove these three points and the thing we want to check is let  me go to this circle this circle is dependent on this circle and this circle and also the bigger  circle and what we want to check is if this circle is touching the other circles in a perfect way  in other words we want to check whether this circle is tangent to each circle that it is dependent on  and for that we are going to use a formula and that formula looks like this and for this process I  also made a node group so if we do an is tangent node group and this tangent node group it asks for  the index of one of the three points and it also wants to have the index of the new point and the  index of the new point is always three since we added in below the other points in the join geometry  nodes if we have a look inside of this so what we're doing here first is we first determine the  distance between one point and the new point like so and then we also take the radius of this point  lik...


### Remove duplicated points [23:34]
**Transcript:** iterations on six you will see that it starts lagging a little bit and the reason for that is a  little bit hidden because let me do this let me make a little bit more space and let me add  and set position node and a random value node which we set on vector I want to have a random  z location is put it like this you see we have a lot of duplicated points and that takes a lot  of computer power so basically we want to merge points if they are really close to each other so  let's do a merge by distance node and of course that doesn't really work yet because what comes out  of this are instances so let's realize those instances and then you see we have a lot less points  and it's a lot more responsive however the outer circle is gone and I'm not really sure why the  outer circle gets removed completely by the merge by distance but I have found a way to fix this  and the way to fix this is to do two merge by distances and this first one is only going to do it  for the outer circle and then this one is going to do it for the other circles so if we do  a named attribute node which we set on outer we can connect this one over here and then this one  we want to do the reversed so let's do...


### Instance objects on points [25:05]
**Transcript:** more beautiful because at the moment we are only instanting circles on this thing but to be honest  we can instant anything we like on these points so for example if we do an icosphere and we connect  that like so and we set these subdivisions a little bit higher and then you see the icosphere is  also instant on the biggest circle but that's not what we want we want to have it only on the  smaller parts as you can see so let's remove the bigger one by doing an radius node and then we can  say with a compare node we can say if the radius is less than 1.9 for example then instant it  let's do a set shade smooth node like so okay cool that already looks quite satisfying I think  let's also flatten the icosphere by doing a vector math node over here set this on multiply  multiply everything by one and let's set the z axis on point three and then you see that looks  really cool however if I now put the iterations higher you will see that the smaller icosphere  get the same resolution as the bigger icosphere and that's not really needed and it's going to take  a lot of computer power from us so let's make it that the smaller icosfheres are getting a lower  resolution of subdivisions to ...


### Render settings [30:49]
**Transcript:** this in a cool way of course let's go into cycles so let's go into render view and let's go into render  properties and let's also press control S to save the file so that it's not going to crash and let's  then set it from ev2 cycles and let's set device on GPU compute and some quick render settings that I  most of the time use is to make the denoiser also use your GPU and under lights let's turn off  light tree and under color management let's turn our look to very high contrast because I think  that looks a lot cooler okay let's see let me position this in a cool way let's add in a plane and  let me also make the world properties black and let's also add in an area light like so let's see  that's pretty cool I think let's first give each iqosphere a material so let's click on it and


### Materials [31:36]
**Transcript:** go over here and let's do a set material node and let me also go into the shader editor over here  let's name this material blobs and let's also assign it in geometry notes like this okay I'm  thinking let's give each blob a random color and that we are going to do by assigning a random  value in geometry notes so let's do a store named attribute node which we set on rent and we want  to give each instance an random value so let's do an random value node connected like so and then  if we go into the shader editor and we do an attribute node which we set on rent let's connect it  like this then you see that doesn't really work and the reason for that is because we have to  realize these instances so let's do an realize instances node and now we're getting a random value  for each point and a cool thing that I found is if you do a new saturation value node and we set the  color on red for example and now if we set the iteration lower you see we're changing it like  this I found that if you give each blob a random saturation then you're getting quite a cool result  to be honest and another thing that's going to give this object a little bit more depth so  to say is adding an ambient o...


### Thank you for watching :) [33:34]
**Transcript:** to you like this video again and if you did please give this video a thumbs up comment down below  if you have any questions and if you don't want to miss out on any future videos I recommend  subscribing to the channel and also be sure to check out the big notebook by going into the link  in description to get 25% off of your purchase and lastly I want to give a big thank you to the coding  train because the things that we did in this tutorial are inspired by the things that he does in  this tutorial and with that being said thank you for watching and I see you in the next one  oh



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
