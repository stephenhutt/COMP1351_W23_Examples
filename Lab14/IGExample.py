"""
Author: Stephen Hutt
Course: 1351
Content: In Class Demo
"""

import dudraw

dudraw.set_canvas_size(400,400)
dudraw.clear(dudraw.WHITE)

for i in range(1,5):
    for j in range(1,5):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
            dudraw.set_pen_color(dudraw.RED)
        else:
            dudraw.set_pen_color(dudraw.BLUE)
        dudraw.filled_circle(i/5, j/5, 0.1)

dudraw.show(float("infinity"))

