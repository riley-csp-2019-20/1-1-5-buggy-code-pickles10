#   a115_buggy_image.py
import turtle as trtl

turtle = trtl.Turtle()
#Create spiders body
turtle.pensize(40)
turtle.circle(20)
# Configure spiders legs
Legs = 8
length = 80
circle = 360/ Legs
#73373553724225 is for more relistic spider 
turtle.pensize(5)
x = 0
#Draw legs
while (x < Legs):
  turtle.goto(0,15)
  turtle.setheading(circle*x)
  turtle.forward(length)
  x= x+ 1
turtle.hideturtle()
wn = trtl.Screen()
wn.mainloop()
