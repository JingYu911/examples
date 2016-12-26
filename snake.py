#-*- coding:utf-8 -*-

import turtle

def drawSnake(rad, angle, len, neckrad):   #半径，扇形圆心角，长度，
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)   #沿直线运动一段距离
    turtle.circle(neckrad+2, 180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 800, 0, 0)  #建立一个启动窗口，长，宽，在屏幕的坐标位置
    pythonsize = 30   #蛇的像素宽度
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40)   #蛇起始运动的方向
    drawSnake(40,80,3,pythonsize/2)

main()

