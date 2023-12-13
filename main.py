import colorgram
from turtle import Turtle, Screen
import random

turtle_=Turtle()
screen=Screen()
screen.colormode(255)
turtle_.speed("fastest")

colors = colorgram.extract('pic.jpg', 100)
x=first_color = colors[0]
rgb = first_color.rgb
colors_rgb=[]
for color in colors:
    #print(color.proportion)
    if color.proportion>0.005 and color.proportion<0.03:
        print(color.proportion)
        colors_rgb.append((color.rgb[0],color.rgb[1],color.rgb[2]))
print(colors_rgb)
colors_rgb.pop(3)
#print(len(colors_rgb))
for i in range(11):
    turtle_.penup()
    turtle_.setpos(-400,450-90*i)
    for j in range(10):
        if random.randint(0,1)==1:
            #print(turtle_.position())
            turtle_.pendown()
            color_rnd=random.choice(colors_rgb)
            turtle_.pencolor(color_rnd)
            turtle_.fillcolor(color_rnd)
            turtle_.begin_fill()
            turtle_.circle(10)
            turtle_.end_fill()
        turtle_.penup()
        turtle_.forward(90)
screen.exitonclick()