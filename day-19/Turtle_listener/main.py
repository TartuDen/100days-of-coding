from turtle import Turtle, Screen
import random

color_list=["red","green","blue"]
width_from_user=500
height_from_user=400
screen=Screen()
screen.setup(width=width_from_user,height=height_from_user)
user_bet=screen.textinput(title="Make a bet", prompt="Enter a color, red/green/blue: ")
print(user_bet)

tim=Turtle()
tom=Turtle()
mike=Turtle()
list_turtles=[tim,tom, mike]

def start_position(turtle_,h, c):
    turtle_.penup()
    turtle_.goto(-width_from_user/2+10,h)
    turtle_.pendown()
    turtle_.color(c)

def start_race():
    pass

for idx,t_name in enumerate(list_turtles):
    start_position(t_name, idx*20, color_list[idx])

end_game=False

while not end_game:
    for racer in list_turtles:
        racer.forward(random.randint(1,5))
        x,y=racer.position()
        if x>=(width_from_user/2-10):
            end_game=True

screen.exitonclick()