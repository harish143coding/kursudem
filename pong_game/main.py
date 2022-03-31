from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("pong_game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 300 or ball.distance(l_paddle) and ball.xcor() < -300:
        ball.bounce_x()


screen.exitonclick()


