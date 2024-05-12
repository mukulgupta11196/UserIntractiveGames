import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from part import Part

game_is_on = True
t_sleep = 0.09


def is_end():
    global game_is_on
    game_is_on = False


POS_RIGHT = (350, 0)
POS_LEFT = (-350, 0)
SCORE_R = (100, 200)
SCORE_L = (-100, 200)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

partition = Part()
paddle_r = Paddle(POS_RIGHT)
paddle_l = Paddle(POS_LEFT)
ball = Ball()
score_r = ScoreBoard(SCORE_R)
score_l = ScoreBoard(SCORE_L)

screen.update()
time.sleep(0.1)

screen.listen()
screen.onkey(fun=paddle_r.go_up, key="Up")
screen.onkey(fun=paddle_r.go_down, key="Down")
screen.onkey(fun=paddle_l.go_up, key="w")
screen.onkey(fun=paddle_l.go_down, key="x")
screen.onkey(fun=is_end, key="q")

while game_is_on:
    screen.update()
    time.sleep(t_sleep)
    ball.move()

    # Detecting collision of ball with upper/ lower wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detecting collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if t_sleep > 0.01:
            t_sleep -= 0.01

    # Detecting right paddle miss
    if ball.xcor() > 380:
        ball.reset_pos()
        score_l.score_increase()
        t_sleep = 0.09

    # Detecting left paddle miss
    if ball.xcor() < -380:
        ball.reset_pos()
        score_r.score_increase()
        t_sleep = 0.09

screen.exitonclick()