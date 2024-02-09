import turtle
import math
window = turtle.Screen()
window.title("New window")
window.bgcolor("#333")

jimmy = turtle.Turtle()
jimmy.pencolor("#fff")
jimmy.pensize(10)
# jimmy.fd(100)
# jimmy.right(90)
# jimmy.fd(100)

# jimmy.fd(100)
# jimmy.right(120)
# jimmy.fd(100)
# jimmy.right(120)
# jimmy.fd(100)

# for _ in range(4):
#     jimmy.fd(100)
#     jimmy.right(90)

def draw_regular_polygon(tl:turtle, no_of_sides:int, radius, origin ):
    turn_angle = 360 / no_of_sides
    turn_angle_in_rad = math.pi / 180 * turn_angle
    side_length = radius * 2 * math.sin(turn_angle_in_rad / 2)
    origin_x = origin[0]
    origin_y = origin[1]
    tl.penup()
    tl.fd(origin_x)
    tl.right(90)
    tl.fd(origin_y)
    tl.left(90)
    tl.fd(radius)
    tl.pendown()
    first_turn_angle = 90 + turn_angle / 2
    tl.left(first_turn_angle)
    for _ in range(no_of_sides):
        tl.fd(side_length)
        tl.left(turn_angle)
    tl.penup()
    tl.right(first_turn_angle)
    tl.back(radius)

# draw_regular_polygon(jimmy, 3, 250, (0, 0))
# draw_regular_polygon(jimmy, 4, 50, (0, 0))
# draw_regular_polygon(jimmy, 5, 80, (0, 0))
# draw_regular_polygon(jimmy, 6, 120, (0, 0))
# draw_regular_polygon(jimmy, 7, 200, (0, 0))

def draw_regular_polygon_new(*argv, **kwargs):
    tl = argv[0]
    no_of_sides = argv[1]
    radius = argv[2]
    origin = argv[3]
    turn_angle = 360 / no_of_sides
    turn_angle_in_rad = math.pi / 180 * turn_angle
    side_length = radius * 2 * math.sin(turn_angle_in_rad / 2)
    origin_x = origin[0]
    origin_y = origin[1]
    tl.penup()
    tl.fd(origin_x)
    tl.right(90)
    tl.fd(origin_y)
    tl.left(90)
    tl.fd(radius)
    tl.pendown()
    first_turn_angle = 90 + turn_angle / 2
    tl.left(first_turn_angle)
    for _ in range(no_of_sides):
        tl.fd(side_length)
        tl.left(turn_angle)
    tl.penup()
    tl.right(first_turn_angle)
    tl.back(radius)

    
# draw_regular_polygon_new(jimmy, 3, 250, (0, 0))
# draw_regular_polygon_new(jimmy, 4, 50, (0, 0))
# draw_regular_polygon_new(jimmy, 5, 80, (0, 0))
# draw_regular_polygon_new(jimmy, 6, 120, (0, 0))
# draw_regular_polygon_new(jimmy, 7, 200, (0, 0))
    
def draw_regular_polygon_using_kw(*argv, **kwargs):
    tl = kwargs.get('tl')
    no_of_sides = kwargs.get('no_of_sides')
    radius = kwargs.get("radius")
    origin = kwargs.get("origin")
    turn_angle = 360 / no_of_sides
    turn_angle_in_rad = math.pi / 180 * turn_angle
    side_length = radius * 2 * math.sin(turn_angle_in_rad / 2)
    origin_x = origin[0]
    origin_y = origin[1]
    tl.penup()
    tl.fd(origin_x)
    tl.right(90)
    tl.fd(origin_y)
    tl.left(90)
    tl.fd(radius)
    tl.pendown()
    first_turn_angle = 90 + turn_angle / 2
    tl.left(first_turn_angle)
    for _ in range(no_of_sides):
        tl.fd(side_length)
        tl.left(turn_angle)
    tl.penup()
    tl.right(first_turn_angle)
    tl.back(radius)

draw_regular_polygon_using_kw(no_of_sides=7, radius=200, tl=jimmy, origin=(0, 0))


window.mainloop()