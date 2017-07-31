from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for n in range (3,8):
    color(colors[n-3])
    for i in range(n):
        forward(100)
        left(360/n)
