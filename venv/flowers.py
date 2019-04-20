
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Техническое задание:
На основе цветочка из квадратов, сделанного в первой итерации,
нарисовать картину из этого цветочка и солнышка.
Солнышко такое как тут, подойдет https://docs.python.org/3.7/library/turtle.html
В будущем ожидаю увидеть поле из разных цветов. Может, сделать цветок красивее.
"""
import turtle as t

t.penup()
t.goto(-300,300)
a= abs(t.pos())
t.pendown()
t.begin_fill()
t.speed(200)

from turtle import *
t.color('red', 'yellow')
t.begin_fill()
while True:
    t.forward(100)
    t.left(130)
    b = abs(t.pos())
    if (a - 1 < b < a + 1):
        break
t.end_fill()
t.penup()


def draw_square(color,x=0,y=0, size=70):
    t.goto(x,y)
    t.begin_fill()
    t.pendown()
    t.color(color)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.fillcolor(color)
    t.penup()
    t.end_fill()


def draw_flower(strong, x, y, size=60):
    draw_square((int(255*strong),int (140*strong), int(250*strong)), x - size, y - size, size)
    draw_square((int(200*strong), int(110*strong), int(200*strong)), x + size, y + size, size)
    draw_square((int(147*strong), int(240*strong), int(251*strong)), x - size, y + size, size)
    draw_square((int(253*strong), int(230*strong), int(200*strong)), x + size, y - size, size)
    draw_square((int(172*strong), int(145*strong), int(253*strong)), x, y, size)

t.colormode(255)

t.bgcolor(0, 0, 100)

for number in range(5):
    draw_flower(0.5, (number)*110 + 55, number*10, 20)
    draw_flower(0.5, (number)*-110 - 55, number*10, 20)


for number in range(6):
    draw_flower(0.8, (number)*130 + 65, number*10 - 120, 30)
    draw_flower(0.8, (number)*-130 - 65 , number*10 - 120, 30)

for number in range(6):
    draw_flower(1, (number)*180 + 85, number*10 - 300, 50)
    draw_flower(1, (number)*-180 - 85 , number*10 - 300, 50)


t.color('blue')
t.shape("turtle")
t.hideturtle()




t.pendown()

t.exitonclick()