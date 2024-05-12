import random
from turtle import Turtle, Screen


def move_turtle(t_list):
    for move_tim in t_list:
        move_tim.forward(random.randint(0, 10))


def check_winner(m_list, bet):
    flag = True
    for item in m_list:
        if item.xcor() >= 200:
            flag = False
            if bet == item.pencolor():
                print("You Win !!")
            else:
                print(f"You Lose! The winner is {item.pencolor()}")
            break
        else:
            flag = True
    return flag


color = ["black", "green", "orange", "purple", "blue", "red"]

y_cod = 125
race_turtle = []
for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(color[i])
    tim.penup()
    tim.goto(x=-220.00, y=y_cod)
    y_cod -= 50
    race_turtle.append(tim)

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet!",
                               prompt="Which turtle is going to win. Enter the color. ").lower()

while check_winner(race_turtle, user_bet):
    move_turtle(race_turtle)


my_screen.exitonclick()
