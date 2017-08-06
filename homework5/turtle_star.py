from turtle import *
##coi vi tri ban dau la 0,0. x chieu duong sang phai, y chieu duong len tren
def draw_star(x,y,length):
    penup()
    forward(x)
    left(90)
    forward(y)
    right(90)
    pendown()
    for i in range(5):
        forward(length)
        right(144)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

