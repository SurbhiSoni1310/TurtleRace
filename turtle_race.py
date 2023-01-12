from turtle import Turtle, Screen
import random

s = Screen()
choice = s.textinput("Bid in Turtle Race", "Which colour would you like to bid ?\nColours are : blue,cyan,green,"
                                           "purple,pink,red")
turtle_list = []
color = ["purple", "blue", "red", "pink", "green", "cyan"]

for i in range(0, 6):
    toto = Turtle()
    toto.color(color[i])
    toto.shape("turtle")
    toto.speed("slow")
    turtle_list.append(toto)


def condition():
    for k in turtle_list:
        if k.xcor() >= 350:
            return False
    return True


y_pos = 150
for i in turtle_list:
    i.penup()
    i.setposition(-350, y_pos)
    y_pos -= 50

if choice:
    while condition():
        for i in turtle_list:
            i.forward(random.randint(5, 50))
    for i in turtle_list:
        if i.xcor() >= 350:
            if i.color()[0] == choice:
                print("Congrats your turtle has won the race")
            else:
                print(i.color()[0] + " has won the race")
                print("Your turtle lost")
else:
    print("No choice made")

s.exitonclick()
