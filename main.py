from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
race_on = False
user_ans = screen.textinput("Make your bet:", "Bet the colors that will win: ")
colors = ['green', 'red', 'blue', 'gray', 'orange', 'yellow']
y_pos = -70
all_turtles = []

for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.pu()
    tim.goto(x=-230, y=y_pos)
    y_pos += 30
    all_turtles.append(tim)

if user_ans:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            win_color = turtle.pencolor()
            if win_color == user_ans:
                print("The turtle you bet won!")
            else:
                print("You lost!")
            race_on = False
        speed = random.randint(0, 10)
        turtle.fd(speed)

screen.exitonclick()
