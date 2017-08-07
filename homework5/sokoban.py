from random import randint

Px = randint(0,3)
Py = randint(0,3)
Bx = randint(0,3)
By = randint(0,3)
Gx = randint(0,3)
Gy = randint(0,3)
def check():
    if Bx == Gx and By == Gy:
        print("GREAAT JOBS YOU ARE THE WINNER")
        return 9
    if (Bx == 0 and By ==0) or (Bx == 3 and By == 3) or (Bx == 0 and By == 3) or (Bx == 3 and By == 0):
        print("GAME OVER :((((")
        return 10
    if Bx == 0 and Px==1 and By==Py:
        return 5
    if Bx == 3 and Px==2 and By==Py :
        return 6
    if By == 0 and Py==1 and Bx==Px:
        return 7
    if By == 3 and Py==2 and Bx==Px:
        return 8
    if Px - Bx ==1 and Py==By:
        return 1
    if Px - Bx == -1 and Py==By:
        return 2
    if Py - By ==1 and Px==Bx:
        return 3
    if Py - By == -1 and Px == Bx:
        return 4
    else:
        return 0


def push():
    global Px, Py, Bx, By
    va_check = check()
    mov = input("Move?")
    if va_check == 0:
        if mov.lower() == "w":
            Py -= 1
        elif mov.lower() == "a":
            Px -= 1
        elif mov.lower() =="s":
            Py += 1
        elif mov.lower() == "d":
            Px += 1
    elif va_check == 1:
        if mov.lower() == "a":
            Bx -= 1
            Px -= 1
        if mov.lower() == "w":
            Py -= 1
        if mov.lower() =="s":
            Py += 1
        if mov.lower() == "d":
            Px += 1
    elif va_check == 2:
        if mov.lower() == "d":
            Bx += 1
            Px += 1
        if mov.lower() == "w":
            Py -= 1
        if mov.lower() == "a":
            Px -= 1
        if mov.lower() =="s":
            Py += 1
    elif va_check == 3:
        if mov.lower() == "w":
            By -= 1
            Py -= 1
        if mov.lower() == "a":
            Px -= 1
        if mov.lower() =="s":
            Py += 1
        if mov.lower() == "d":
            Px += 1
    elif va_check == 4:
        if mov.lower() == "s":
            By += 1
            Py += 1
        if mov.lower() == "w":
            Py -= 1
        if mov.lower() == "a":
            Px -= 1
        if mov.lower() == "d":
            Px += 1
    elif va_check == 5:
        if mov.lower() == "a":
            Bx = Bx
        if mov.lower() == "w":
            Py -= 1
        if mov.lower() =="s":
            Py += 1
        if mov.lower() == "d":
            Px += 1
    elif va_check == 6:
        if mov.lower() == "d":
            Bx = Bx
        if mov.lower() == "w":
            Py -= 1
        if mov.lower() == "a":
            Px -= 1
        if mov.lower() =="s":
            Py += 1
    elif va_check == 7:
        if mov.lower() == "w":
            Bx = Bx
        if mov.lower() == "a":
            Px -= 1
        if mov.lower() =="s":
            Py += 1
        if mov.lower() == "d":
            Px += 1
    elif va_check == 8:
        if mov.lower() == "s":
            Bx = Bx
        if mov.lower() == "w":
            Py -= 1
        if mov.lower() == "a":
            Px -= 1
        if mov.lower() == "d":
            Px += 1
        
        
        
            
    
while True:
    for y in range(4):
        for x in range(4):
            if x == Px and y == Py:
                print("P", end = " ")
            elif x == Bx and y == By:
                print("B", end = " ")
            elif x == Gx and y == Gy:
                print("G", end = " ")
            else:
                print("-", end=" ")
        print()
    test= check()
    if test == 9:
        break
    if test == 10:
        print("Play again")
        Px = 2
        Py = 2
        Bx = 2
        By = 1
        Gx = 3
        Gy = 2
    push()
     
