import colorgram
from turtle import Turtle, Screen
import turtle
import random


t=Turtle()
turtle.colormode(255)

def color_extractor():
    colors=colorgram.extract("img.png", 6)
    c_list=[]

    for idx,color in enumerate(colors):
        if idx>0:
            color_tuple=color.rgb
            c_list.append(color_tuple)
    return(c_list)

def painter():
    dot_size=5

    t.pendown()
    t.pencolor((color_extractor()))
    t.dot(dot_size)
    t.penup()
    for r in range(10):
        for c in range(10):
            t.goto(10*r,10*c)
            t.pencolor(color_extractor())
            t.pendown()
            t.dot(dot_size)
            t.penup()
painter()


screen=Screen()
screen.exitonclick()