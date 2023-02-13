import dudraw

dudraw.set_canvas_size(300,200)
dudraw.set_x_scale(0,300)
dudraw.set_y_scale(0,200)
dudraw.clear_rgb(255,255,0)
dudraw.set_pen_color_rgb(0,255,0)
dudraw.filled_triangle(0,0,0,200,200,200)

dudraw.set_pen_color_rgb(255,0,0)
dudraw.filled_triangle(300,0,300,200,100,0)



dudraw.show(10000)
