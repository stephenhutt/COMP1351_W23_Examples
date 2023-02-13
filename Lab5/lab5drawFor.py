"""
Author: Stephen Hutt
Course: 1351
Content: In Class Demo
"""
import dudraw

# Canvas Setup 
dudraw.set_canvas_size(300,600)
dudraw.set_x_scale(0,300)
dudraw.set_y_scale(0,600)
dudraw.clear_rgb(0,0,0)
dudraw.set_pen_color_rgb(0,255,0)

#Starting Point for my first circle
start = 100
#Draw Three Circles
for i in range(7):
    
    dudraw.filled_circle(150, start, 35)
    print(start)
    start += 100


dudraw.show(100000)