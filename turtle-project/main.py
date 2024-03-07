import random
import colorgram
from turtle import Turtle, Screen, color
count = 0
t = Turtle()
t.hideturtle()
t.width(15)
t.speed("fast")
colors = colorgram.extract('pic.png', 27)
t.pu()
t.goto(-75,200)
t.pd()
Screen().colormode(255)
for i in colors:
    if count == 3:
        t.pu()
        t.right(180)
        t.fd(150)
        t.left(90)
        t.fd(50)
        t.left(90)
        t.pd()
        count =0 
    r =i.rgb[0]
    g =i.rgb[1]
    b =i.rgb[2]
    t.color(r,g,b)
    t.dot(25)
    t.pu()
    t.fd(50)
    t.pd()
    count+=1


Screen().exitonclick()