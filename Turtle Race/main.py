from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "purple", "pink"]
all_turtles = []

y = -100

for t_index in range(0, 6):
    turtle = Turtle("turtle")
    turtle.color(colors[t_index])
    turtle.penup()
    turtle.goto(-230, y)
    y += 40
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The winning turtle was {winning_color}.")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
