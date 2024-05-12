from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

is_game_on = True


def quit_game():
    global is_game_on
    is_game_on = False


my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("Black")
my_screen.title("Classic Snake 🐍")
my_screen.tracer(0)

new_snake = Snake()
new_food = Food()
score = ScoreBoard()

my_screen.listen()
my_screen.onkey(new_snake.up, "Up")
my_screen.onkey(new_snake.down, "Down")
my_screen.onkey(new_snake.left, "Left")
my_screen.onkey(new_snake.right, "Right")
my_screen.onkey(quit_game, "q")


while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    new_snake.move()

    # Detecting collision with food
    if new_snake.head.distance(new_food) < 15:
        score.increase_score()
        score.refresh_score()
        new_food.refresh()
        new_snake.extend()

    # Detecting collision with wall
    if new_snake.head.xcor() > 280 or new_snake.head.xcor() < -280 or \
            new_snake.head.ycor() > 280 or new_snake.head.ycor() < -280:
        score.score_reset()
        new_snake.snake_reset()

    # Detect collision with tail
    for snake in new_snake.snakes[1:]:
        if new_snake.head.distance(snake) < 10:
            score.score_reset()
            new_snake.snake_reset()
my_screen.exitonclick()
