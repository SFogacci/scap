import turtle
import math


def bump(lenght):
  turtle.forward(lenght*0.4)
  turtle.right(90)
  turtle.forward(0.1*lenght)
  turtle.left(90)
  turtle.forward(lenght*0.2)
  turtle.left(90)
  turtle.forward(0.1*lenght)
  turtle.right(90)
  turtle.forward(lenght*0.4)

def straight(lenght):
  turtle.forward(lenght)


#draw a square with the position of a vertex, the angle of rotation, and length
def draw_polygon_vertex(x=0, y=0, angle=0, lenght=150, sides=4, side_shape = straight):

  turtle.teleport(x,y)
  turtle.setheading(angle)
  
  for i in range(sides):
    side_shape(lenght)
    turtle.left(360/sides)


def center_to_vertex(x_cen, y_cen, angle, length, sides=4):

  beta = (sides - 2) * 180 / (2 * sides)
  distance = length / (2 * math.cos(math.radians(beta)))

  start_angle = math.radians(angle + beta)

  x_ver = x_cen - distance * math.cos(start_angle)
  y_ver = y_cen - distance * math.sin(start_angle)

  turtle.teleport(x_ver, y_ver)
  turtle.setheading(angle)

  return x_ver, y_ver

def draw_polygon_center(x_cen=0, y_cen=0, angle=0, length=150, sides=4, side_shape = straight):

  x_ver, y_ver = center_to_vertex(x_cen, y_cen, angle, length, sides)
  draw_polygon_vertex(x_ver, y_ver, angle, length, sides, side_shape)

