
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


def draw_square(color,x=0,y=0):
    t.goto(x,y)
    t.begin_fill()
    t.pendown()
    t.color(color, 'red')
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


def drow_flower(x,y,size=60)
    draw_square('purple', x-size,y-size)
    draw_square('orange', x+size,y+size)
    draw_square('pink', x-y+60)
    draw_square('blue', x+60,y-60)
    draw_square('yellow', x-0,y-0)


drow_flower(100,-100)
drow_flower(-100,-10,size=30)
drow_flower(170,-300)
drow_flower(-250,-300)
drow_flower(-100,200)
drow_flower(166,200)
t.color('blue')
t.shape("turtle")
t.hideturtle()




t.pendown()

t.exitonclick()