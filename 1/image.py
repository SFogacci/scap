import turtle


def line(lenght):
  turtle.forward(lenght/3)
  turtle.left(90)
  turtle.forward(0.1*lenght)
  turtle.right(90)
  turtle.forward(lenght/3)
  turtle.right(90)
  turtle.forward(0.1*lenght)
  turtle.left(90)
  turtle.forward(lenght/3)

def square(lenght):
  for i in range(4):
    line(lenght)
    turtle.left(90)

