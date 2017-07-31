from turtle import *
for n in range(3,7):
    if n % 2 == 0:
        color('red')
    else:
        color('blue')
    for i in range(n):
        forward(100)
        left(360/n)
