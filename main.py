import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("Guess", 'Who do you think will win the race? Enter a colour:')

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
y_positions = [-70,-40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_turtle = turtles.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle won the race.")
            else:
                print(f"You've lost! The {winning_turtle} turtle won the race.")

        random_distance = random.randint(0,10)
        turtles.forward(random_distance)


screen.exitonclick()
