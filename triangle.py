#-*- coding:utf-8 -*-

import turtle
import time

def drawTriangle(side):
    turtle.fd(side)
    turtle.seth(120)
    turtle.fd(side)
    turtle.seth(-120)
    turtle.fd(side)

def main():
    turtle.setup(800, 800, 0, 0)
    line = 5
    turtle.pensize(line)
    turtle.pencolor("black")
    turtle.seth(-0)
    drawTriangle(100)

main()
time.sleep(5)
exit()
