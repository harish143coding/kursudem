import random

import colorgram
import turtle
import random
from color_extract import color_extract


color_list = color_extract()


tim = turtle.Turtle()
turtle.colormode(255)
tim.setheading(360)
tim.forward(300)

for x in range(10):
    tim.dot(50, random.choice(color_list))
    tim.forward(50)


screen = turtle.Screen()
screen.exitonclick()