from turtle import Turtle, Screen

tim = Turtle()
s = Screen()
s.listen()


def move():
    tim.forward(10)


def left():
    tim.left(10)


def right():
    tim.right(10)


def backward():
    tim.backward(10)


def clear():
    tim.reset()


s.onkeypress(move, "w".lower())
s.onkeypress(left, "a".lower())
s.onkeypress(backward, "s".lower())
s.onkeypress(right, "d".lower())
s.onkey(clear, "c".lower())

s.exitonclick()