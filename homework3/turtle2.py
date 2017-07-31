from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(5):
    color(colors[i])
    begin_fill()
    for n in range(2):
        right(90)
        forward(100)
        right(90)
        forward((5-i)*60)
    end_fill()
