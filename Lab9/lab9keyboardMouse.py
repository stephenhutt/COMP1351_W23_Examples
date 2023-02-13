""" Circle left and right that changes based on user input
    File Name: lab9keyboardMouse.py
    Author: Stephen Hutt
    Date: Jan 25 2023
    Course: COMP 1351
    Assignment: Lab 9
    Collaborators: Based on starting code given in lab
    Internet Source:
"""
import dudraw
import random
# open 500x500 pixel window
dudraw.set_canvas_size(500,500)
radius = 0.1
x_center = 2*radius
y_center = radius
x_velocity = 0.01
while True:
    # clear the previous frame
    dudraw.clear(dudraw.LIGHT_GRAY)
    # draw the next frame of the animation
    dudraw.filled_circle(x_center, y_center, radius)
    # display the image for 50 milliseceonds, which is 20 frames per second
    dudraw.show(20)
    # prepare for next frame by advancing the position of the circle
    x_center = x_center + x_velocity
    if x_center + radius > 1:
        x_velocity = -x_velocity
    if x_center - radius < 0:
        x_velocity = -x_velocity
    #Check if the mouse has been clicked, since last time we checked
    if dudraw.mouse_clicked():
        #Randomly choose a new colour 
        r = int(random.random() * 255)
        g = int(random.random() * 255)
        b = int(random.random() * 255)
        #Set the new color
        dudraw.set_pen_color_rgb(r,g,b)
        #Move the circle to the location of the mouse click
        x_center = dudraw.mouse_x()
        y_center = dudraw.mouse_y()

    # Check if the user has pressed a key    
    if dudraw.has_next_key_typed():
        #check if the key press was "r"
        if dudraw.next_key_typed() == "r":
            dudraw.set_pen_color_rgb(255,0,0)


        
