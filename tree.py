# -*- coding:utf-8 -*-

import turtle
from turtle import Turtle

def tree(plist, l, a, f):
    if l > 5:
        lst = []
        for p in plist:
            p.forward(1)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst, l*f, a, f)

def main():
    p = Turtle()
    turtle.setup(800, 800, 0, 0)
    p.color("green")
    p.pensize(5)
    p.hideturtle()
    p.getscreen().tracer(30, 0)
    p.left(90)

    p.penup()
    p.goto(x, y)
    p.pendown()

    t = tree([p], 200, 65, 0.6735)

main()