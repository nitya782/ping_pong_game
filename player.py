from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto_start()
        self.left(90)
        self.shape("turtle")
        self.color("white")
    def up(self):
        self.forward(15)

    def is_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)
