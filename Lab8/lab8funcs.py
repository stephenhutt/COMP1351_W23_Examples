"""TODO: Add Header Block"""

import dudraw

def myDrawCircles(centre_x, centre_y, radius):
    """Draw 2 circles next to each other
    param: float centre_x: circle centre fo two circles
    param: float centre_y: circle centre
    param: float radius: circle radius 
    return: None"""
    #Set a Pen Color
    center_x_left = centre_x - radius
    center_x_right = centre_x + radius
    #Draw the Circle
    dudraw.filled_circle(center_x_left,centre_y, radius)
    dudraw.filled_circle(center_x_right,centre_y, radius)


dudraw.set_canvas_size()

dudraw.set_pen_color_rgb(0,100,100)

myDrawCircles(0.5,0.5,0.25)
dudraw.show(float('inf'))