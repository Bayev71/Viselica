from turtle import *

text = 10
def draw_line(point1: list, point2, size=10, p_color='black'):
    oldPenSize = pen()['pensize']
    oldColour = pen()['pencolor']
    penup()
    goto(point1[0], point1[1])
    pendown()
    goto(point2[0], point2[1])
    penup()
    pensize(size)
    pencolor(p_color)

Screen(), setup(800, 700)

shape("turtle")
penup()
draw_line([-400, -250], [-100, -250])
draw_line([-120, -250], [-120, 300])
draw_line([-120, 300], [-300, 300])
draw_line([-300, 300], [-300, 250])
# goto([-300, 150])
pendown()
circle(-50)
draw_line([-300, 150], [-300, 100])
draw_line([-300, 100], [-225, 125])
# goto([-300, 100])
draw_line([-300, 100], [-375, 125])
# goto([-300, 100])
draw_line([-300, 100], [-300, 30])
draw_line([-300, 30], [-375, -60])
# goto([-300, 30])
draw_line([-300, 30], [-225, -60])
def draw_square(top_left,len_edge,size = 10,p_color = 'black'):
    x = top_left[0]
    y = top_left[1]
    points = [[x,y]], [x + len_edge, y], [x + len_edge , y - len_edge]]
    draw_line(point[0] , point[1] , size, p_color)
    draw_line(point[1 , point[2] , size, p_color)
    draw_line(point[1, point[2], size, p_color)
    mainloop()
