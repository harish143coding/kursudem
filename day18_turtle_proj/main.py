import turtle
from turtle import Turtle, Screen
import random as rand

# project spirograph
tim = Turtle()

tim.shape("turtle")
tim.speed('fastest')

def draw_spiro_graph(gap_size):
    for x in range(int(360 / gap_size)):
        tim.circle(radius=100)
        tim.color('blue')
        tim.setheading(tim.heading() + gap_size)
    return tim

draw_spiro_graph(4)




my_screen = Screen()
my_screen.exitonclick()