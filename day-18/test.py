from turtle import Turtle, Screen, setup
import random
setup(600,400)
t=Turtle()
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink"]

def exercise1():
    dot_size=5

    t.penup()
    t.goto(-300, -200)
    t.pendown()
    t.pencolor(random.choice(colors))
    t.dot(dot_size)
    t.penup()
    for r in range(50):
        for c in range(50):
            t.goto(10*r,10*c)
            t.pencolor(random.choice(colors))
            t.pendown()
            t.dot(dot_size)
            t.penup()

def exercise2():
    side_length=50
    for i in range(3,20):
        t.pencolor(random.choice(colors))
        for j in range(i):
            t.forward(side_length)
            t.right(360/i)

def exercise3():
    amount_of_circles=10
    turns=360/amount_of_circles
    for i in range(1,amount_of_circles):
        c=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        t.pencolor("red")
        t.pensize(5)
        t.circle(50)
        turns=turns+i
        t.right(turns)


    

# exercise1()
# exercise2()
# exercise3()
screen=Screen()
screen.exitonclick()