import turtle
from turtle import *


def draw_line(point1: list, point2):
    penup()
    goto(point1[0], point1[1])
    pendown()
    goto(point2[0], point2[1])
    penup()


Screen(), setup(800, 700)

shape("turtle")
penup()
draw_line([-400, -250], [-100, -250])
draw_line([-120, -250], [-120, 300])
draw_line([-120, 300], [-300, 300])
draw_line([-300, 300], [-300, 250])
# goto([-300, 150])
pendown()
turtle.circle(-50)
draw_line([-300, 150], [-300, 100])
draw_line([-300, 100], [-225, 125])
# goto([-300, 100])
draw_line([-300, 100], [-375, 125])
# goto([-300, 100])
draw_line([-300, 100], [-300, 30])
draw_line([-300, 30], [-375, -60])
# goto([-300, 30])
draw_line([-300, 30], [-225, -60])

mainloop()
