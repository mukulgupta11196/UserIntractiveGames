from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_turtle()
        self.head = self.snakes[0]

    def create_turtle(self):
        for item in STARTING_POSITION:
            self.add(item)

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[i - 1].xcor()
            new_y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.speed("fastest")
        new_turtle.goto(position)
        self.snakes.append(new_turtle)

    def extend(self):
        new_x = self.snakes[-1].xcor()
        new_y = self.snakes[-1].ycor()
        pos = (new_x, new_y)
        self.add(pos)

    def snake_reset(self):
        for item in self.snakes:
            item.goto(1000, 1000)
        self.snakes.clear()
        self.create_turtle()
        self.head = self.snakes[0]