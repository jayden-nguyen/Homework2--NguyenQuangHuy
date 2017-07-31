##funtion print all the list with comma between elements
def Ouritem():
        print("Our items: ",end="")
        for i in range(len(shop)):
            if i != len(shop)-1:
                print(shop[i]+",", end="")
            else:
                print(shop[i])

shop = ["T-Shirt","Sweater"]

choice = ""
#--------------------------------------MAIN OPERATION -----------------------------------
while choice.lower() != "e":
    choice = input("Welcome to our shop, what do you want (C, R, U, D)?(press E to exit)")
   
                
    if choice.lower() == "c":
        item = input("Enter new ===item:")
        shop.append(item)
        Ouritem()
    elif choice.lower() == "r":
        Ouritem()
    elif choice.lower() == "u":
        up_pos = int(input("Update position?"))
        if up_pos > len(shop) - 1 :
            print("INVALID NUMBER")
        else:
            new_i = input("New item? ")
            shop[up_pos] = new_i
            Ouritem()
    elif choice.lower() == "d":
        de_pos = int(input("Delete position?"))
        if de_pos > len(shop) - 1:
            print("INVALID NUMBER")
        else:
            shop.pop(de_pos)
            Ouritem()
    else:
        if choice.lower() != "e":
                print("INVALID")
