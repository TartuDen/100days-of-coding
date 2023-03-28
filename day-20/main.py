from turtle import Screen, Turtle

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake")



def create_snake(length):
    snake=[]
    for i in range(length):
        s=Turtle()
        s.shape("square")
        s.color("white")
        s.goto(0+len(snake)*20,0)
        snake.append(s)
    return(snake)

print(create_snake(3))




screen.exitonclick()