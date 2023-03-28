from turtle import Turtle, Screen, clear


t=Turtle()
screen=Screen()

def move_forward():
    t.forward(10)

def move_back():
    t.backward(10)

def turn_left():
    t.left(5)


def turn_right():
    t.right(5)

def clear_screen():
    t.clear()
    t.penup()
    t.goto(0,0)
    t.pendown()



screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_back)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkey(clear_screen,"c")



screen.exitonclick()
