"""
Author: Stephen Hutt
Course: 1351
Content: In Class Demo
"""

import dudraw
#Canvas Setup
dudraw.set_canvas_size(600,600)
dudraw.set_x_scale(0,600)
dudraw.set_y_scale(0,600)
dudraw.clear_rgb(0,0,0)
dudraw.set_pen_color_rgb(255,255,0)


#Drawing
r = 250
for i in range(20):
    dudraw.circle(300,300,r)
    r-=10

#show drawing on screen
dudraw.show(100000)