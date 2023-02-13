"""
Author: Stephen Hutt
Course: 1351
Content: In Class Demo
"""

import dudraw
#Set up the Canvas
dudraw.set_canvas_size(300,200)
dudraw.set_x_scale(0,300)
dudraw.set_y_scale(0,200)
dudraw.clear_rgb(255,255,0)

#Set Pen Color
dudraw.set_pen_color_rgb(0,255,0)
#Draw One Shape
dudraw.filled_triangle(0,0,0,200,200,200)

dudraw.set_pen_color_rgb(255,0,0)
#Draw the other
dudraw.filled_triangle(300,0,300,200,100,0)
#Show the drawing
dudraw.show(10000)
