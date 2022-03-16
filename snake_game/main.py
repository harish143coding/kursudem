from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor('black')

segment1 = Turtle('square')
segment1.color('white')
segment1.goto((0,0))

segment2 = Turtle('square')
segment2.color('white')
segment2.goto((-20,0))

segment3 = Turtle('square')
segment3.color('white')
segment3.goto((-40,0))


screen.exitonclick()





