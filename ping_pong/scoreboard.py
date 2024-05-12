from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.pencolor("white")
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)