from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 13, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        with open("High_score.txt") as f:
            self.high_score = int(f.read())
        self.write(arg=f"Score : {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def score_reset(self):
        if self.high_score < self.score:
            self.high_score = self.score

        self.score = 0
        self.refresh_score()
        with open("High_score.txt", mode="w") as f:
            f.write(str(self.high_score))

    def increase_score(self):
        self.score += 1



