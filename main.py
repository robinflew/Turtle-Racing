import turtle
from turtle import Turtle, Screen
import random

# Set up the screen
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# Create six turtles and position them at the starting line
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=-100 + i * 40)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        # Check if a turtle has reached the finish line
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_turtle = turtle.color()[0]
            if winning_turtle == user_bet:
                print(f"You won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You lost. The {winning_turtle} turtle is the winner.")

screen.exitonclick()
