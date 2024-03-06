import random
from turtle import Turtle, Screen
t = Turtle()
Screen().bgcolor("black")
Screen().colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


t.width(2)
t.speed("fastest")
def draw_spirograph(size_of_gap):       
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)

draw_spirograph(2)
Screen().exitonclick()