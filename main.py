import turtle as t
import random

is_race_on = False
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = t.Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter color: ")

position_y = -235
position_x = -90
all_turtles = []

for color in color_list:
    turtle = t.Turtle()
    turtle.color(color)
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(position_y, position_x)
    position_x += 40
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() < 230:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
        else:
            is_race_on = False
            print(turtle.pencolor())
            if user_bet == turtle.pencolor():
                print(f"You win! The winning colort is: {turtle.pencolor()}")
            else:
                print("You lose.")

screen.exitonclick()