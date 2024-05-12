from turtle import Turtle


class Part(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(0, -300)
        self.left(90)
        self.pensize(width=4)
        while self.ycor() < 300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

        self.goto(0, -290)
        self.write(arg="Press Q for Quit", align="center", font=("Arial", 20, "normal"))
