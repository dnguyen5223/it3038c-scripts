# Project 2

For Project 2 I recreated an animation of the DVD logo bouncing on a canvas with a space background
![image](https://user-images.githubusercontent.com/122412432/226483386-28f1466d-806f-487c-9b76-be72c25a0340.png)


Using Visual Studios I created a file with Python called Project2.py. I started off by implementing three pluggins to Tkinter, Astrict, and time

Tkinter is a pluggin that allows display of positioning and to control widgets, creates frame, labels SpinBox,etc. For the purpose of this project I mainly used frame and canvas. I used Time to help calculate and time the movement of the dvd logo.

First we will import the Pluggins
```
from tkinter import *
import time
```
Secondly we created Constraints of for size of our canvas or window (Set the canvas size to the length of the background)
```
WIDTH = 932
HEIGHT = 932
```
We then created our canvas and set these contraints onto our canvas
```
canvas = Canvas(window, width=WIDTH,height=HEIGHT)
canvas.pack()

```

Then we download PNG into our Scripting Language folders to allow us to pull images
```
background_image = PhotoImage(file='space.png')
space_image = canvas.create_image(0,0,image=background_image,anchor=NW)

dvd_image = PhotoImage(file='dvd.png')
my_image = canvas.create_image(0,0,image=dvd_image,anchor=NW)
```
Then with the DVD logo we set the images width and height to help ensure the DVD logo full logo doesn't pull off the screen
```
image_width = dvd_image.width()
image_height = dvd_image.height()
```
To set the Velocity of Speed of the DVD logo movement we created a xSpeed and ySpeed variable with speed constraints
```
xSpeed = 4 
ySpeed = 2
```

We then created a while loop to allow our image to stay fully on screen and move vertically and horizontally along the window.
```
while True:
    location = canvas.coords(my_image)
    print(location)
    if(location[0]>=(WIDTH-image_width) or location[0]<0):
        xSpeed = -xSpeed
    if(location[1]>=(HEIGHT-image_height) or location[1]<0):
        ySpeed = -ySpeed
```
Finally we are setting our DVD image to move at the contrained speed along our canvas at 0.01 seconds and the window to frequently update.

```
  canvas.move(my_image, xSpeed,ySpeed)
    window.update()
    time.sleep(0.01)


window.mainloop()

```
