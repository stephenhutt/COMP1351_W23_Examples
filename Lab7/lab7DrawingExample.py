import dudraw

def drawCircle(r,g,b,centre_x, centre_y, radius):
    """Draw a circle of a spcified size and color 
    param: int r: red value
    param: int g: green value
    param: int b: blue value
    param: float centre_x: circle centre
    param: float centre_y: circle centre
    param: float radius: circle radius 
    return: None"""
    #Set a Pen Color
    dudraw.set_pen_color_rgb(r,g,b)
    #Draw the Circle
    dudraw.filled_circle(centre_x,centre_y, radius)



drawCircle(255,0,0,0.5,0.5,0.49)
drawCircle(255,255,0,0.5,0.5,0.4)
drawCircle(255,0,255,0.5,0.5,0.3)
drawCircle(0,255,0,0.5,0.5,0.1)

dudraw.show(float('inf'))




