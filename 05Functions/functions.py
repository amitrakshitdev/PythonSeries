import turtle
import math
window = turtle.Screen()
window.bgcolor("#333")
window.title = "My window"

jimmy = turtle.Turtle()
jimmy.pencolor("#fff")


def draw_regular_polygon(tl:turtle, no_of_sides: int, center_xy: tuple, radius=50):
    tl.penup()
    tl.fd(center_xy[0])
    tl.right(90)
    tl.fd(center_xy[1])
    tl.left(90)
    tl.fd(radius)
    tl.pendown()
    turn_angle = 360 / no_of_sides
    first_turn_angle = 90 + turn_angle / 2
    turn_angle_in_rad = turn_angle * math.pi / 180
    side_length = radius * 2 * math.sin(turn_angle_in_rad / 2)
    tl.left(first_turn_angle)
    for _ in range(no_of_sides):
        tl.fd(side_length)
        tl.left(turn_angle)

draw_regular_polygon(jimmy, 5, (0, 0), radius=112)

window.mainloop()
