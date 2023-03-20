from tkinter import *
import time

WIDTH = 932
HEIGHT = 932
xSpeed = 4 
ySpeed = 2

window = Tk()

canvas = Canvas(window, width=WIDTH,height=HEIGHT)
canvas.pack()

background_image = PhotoImage(file='space.png')
space_image = canvas.create_image(0,0,image=background_image,anchor=NW)

dvd_image = PhotoImage(file='dvd.png')
my_image = canvas.create_image(0,0,image=dvd_image,anchor=NW)

image_width = dvd_image.width()
image_height = dvd_image.height()

while True:
    location = canvas.coords(my_image)
    print(location)
    if(location[0]>=(WIDTH-image_width) or location[0]<0):
        xSpeed = -xSpeed
    if(location[1]>=(HEIGHT-image_height) or location[1]<0):
        ySpeed = -ySpeed


    canvas.move(my_image, xSpeed,ySpeed)
    window.update()
    time.sleep(0.01)


window.mainloop()
