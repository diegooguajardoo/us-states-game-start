from turtle import Turtle


class Tag(Turtle):
    def __init__(self, name, xcor, ycor):
        super().__init__()
        self.text = ""
        self.penup()
        self.hideturtle()
        self.goto(xcor, ycor)
        self.write(arg=name, align="center", font=("Arial", 14))
