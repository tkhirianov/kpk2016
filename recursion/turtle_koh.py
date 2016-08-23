from turtle import *


def koh_forward(L, n):
    if n == 0:
        t.forward(L)
    else:
        koh_forward(L/3, n-1)
        t.left(60)
        koh_forward(L/3, n-1)
        t.right(120)
        koh_forward(L/3, n-1)
        t.left(60)
        koh_forward(L/3, n-1)

def demo():
    for n in range(0, 4):
        t.color(colors[n])
        t.penup()
        t.goto(-200, 0)
        t.pendown()
        koh_forward(300, n)

def snowflake():
    t.penup()
    t.goto(-150, 100)
    t.color('black', 'cyan')
    t.pendown()
    t.begin_fill()
    for edge in range(3):
        koh_forward(300, 4)
        t.right(120)
    t.end_fill()
    
t = Turtle(shape='turtle')
colors = ['gray', 'green', 'blue', 'orange', 'black', 'magenta', 'cyan']
t.speed(10)
snowflake()
