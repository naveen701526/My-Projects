from turtle import *
from random import randint
bgcolor('#121212')
x = 1
speed(0)
while x < 400:
 r = randint(0,255)
 g = randint(0,255)
 b = randint(0,255)
 colormode(255)
 pencolor(r,r,r)
 # for colorfull mess try this pencolor .
 # pencolor(r,g,b)
 forward(50 + x)
 right(120.91)
 x = x+1

exitonclick()
