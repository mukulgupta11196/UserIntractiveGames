from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(pos)

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(x=self.xcor(), y=new_y)
