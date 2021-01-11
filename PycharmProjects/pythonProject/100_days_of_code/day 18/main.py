# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g , b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import random


color_list = [(228, 225, 221), (231, 205, 85), (228, 148, 89), (230, 221, 226), (217, 226, 219), (120, 167, 186), (216, 222, 227), (162, 11, 19), (31, 111, 160), (234, 81, 45), (175, 19, 14), (124, 177, 145), (5, 99, 36), (189, 186, 23), (207, 65, 23), (26, 131, 43), (10, 40, 76), (243, 202, 5), (14, 63, 40), (86, 14, 22), (135, 84, 99), (48, 167, 74), (4, 65, 140), (173, 134, 149), (39, 22, 19), (49, 150, 195), (228, 171, 161), (219, 63, 69), (73, 134, 188), (173, 204, 175), (215, 176, 182), (167, 202, 210), (180, 190, 207), (64, 66, 56), (42, 72, 78), (245, 13, 13)]


graphic = turtle.Turtle()
graphic.speed("fastest")
graphic.hideturtle()
screen = turtle.Screen()
turtle.colormode(255)
hor = -225
ver = -225
number_of_dots = 100

graphic.penup()
graphic.goto(hor, ver)
for dot_count in range(1, number_of_dots + 1):
    graphic.dot(20, random.choice(color_list))
    graphic.forward(50)
    if dot_count % 10 == 0:
        ver += 50
        graphic.goto(hor, ver)
