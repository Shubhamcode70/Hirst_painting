import random
from rgb import Rgb
import colorgram as cg
from turtle import Turtle, Screen

colors = cg.extract("image.jpg", 7)
color_tuple_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    color_tuple = (r, g, b)
    color_tuple_list.append(color_tuple)

rgb = Rgb()
ron = Turtle()
ron.penup()
ron.hideturtle()
ron.color("yellow")
ron.pencolor("yellow")
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")


ron.speed("fastest")
#270 + 180 / 2 = 225



ron.setheading(225)
ron.forward(225)
ron.setheading(360)
dot_count = 100


for dot in range(1, dot_count+1):
    #random.choice(color_tuple_list)
    ron.dot(40, rgb.random_rgb2())
    ron.forward(50)
    if dot % 10 == 0:
        ron.setheading(90)
        ron.forward(50)
        ron.setheading(180)
        ron.forward(500)
        ron.setheading(0)

screen.exitonclick()