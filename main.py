from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()


class Snake:
    SEGMENT_SIZE = 20

    def __init__(self, length):
        self.segments = []
        for i in range(length):
            self.segments.append(self._create_segment((i * (-20), 0)))

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)

    def _create_segment(self, position):
        s = Turtle("square")
        s.color("white")
        s.penup()
        s.goto(position)
        return s

    def move_forward(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(20)


snake = Snake(20)
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

screen.exitonclick()
