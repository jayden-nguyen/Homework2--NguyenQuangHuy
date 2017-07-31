import time
sheep = [4,45,23,34,24,12,250]
## function find the maximum size in list
def findMax(li):
    maxx = li[0]
    for i in range(len(li)):
        if li[i] > maxx:
            maxx = li[i]
    return maxx
## function that shear the list
def shear(maxx,li):
    for i in range(len(li)):
        if maxx == li[i]:
            n = i
    li[n] = 8
    return li
##print the list, maximum and the list after shear
def info(li):
    print(li)
    print("Now my biggest sheep has size ",findMax(li)," let's shear it")
    print(shear(findMax(li),li))
## function find the total sized
def total(li):
    sum = 0
    for i in range(len(li)):
        sum = sum + li[i]
    return sum
##------------------------ MAIN OPERATION----------------------------------------
#input the months work before retirement
n_month = int(input("What's the number of month that you wanna work before retire?"))
#input the expected cost per size
cost = int(input("What's the cost expexted per size?"))
##operation
print("Hello, my name is Huy and here is my flock ")
info(sheep)
for i in range(n_month):
    time.sleep(0.75) 
    sheep = [(lo + 50 ) for lo in sheep]
    print()
    print("MONTH {0}:".format(i+1))
    print("One month has passed and here is my flock ")
    info(sheep)
print()
print("My flock has the size in total: ", total(sheep))
print("I would get: "+ str(total(sheep))+" * "+str(cost)+"$"+" = "+str(total(sheep)*cost)+"$")
