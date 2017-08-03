prices = {"banana" : 4,
          "apple" : 2,
          "orange" : 1.5,
          "pear" : 3}
li = prices.keys()
purchased = {
        "banana": 5,
        "orange":3
    }
print("YOU BOUGHT 5 BANANAS AND 3 ORANGES")
choice = "yes"
while  choice.lower() != "no":
    choice = input("Do you want more(yes or no, press no to exit)? ")
    if choice.lower() == "yes":
        fruit = input("what's type of fruit? ")
        fruit = fruit.lower()
        if fruit in li:
            if fruit.lower() == "banana" or fruit == "orange":
                quant = int(input("how many?"))
                quant += purchased[fruit]
                purchased[fruit]=quant
            else:
                quant = int(input("how many?"))
                purchased[fruit] = quant
        else:
            print("We don't have it")
        print("you bought "+str(quant)+" "+fruit+"s")
    elif choice.lower()=='no':
        break
    else:
        print("IVALID,Please input again")
print("**********************************************")   
purchased_items = list(purchased.items())
total = 0
print("THIS IS YOUR BILL")
for i in range(len(purchased_items)):
    print(purchased_items[i][0],"quantity: ",purchased_items[i][1]," price: ",prices[purchased_items[i][0]])
    total += purchased_items[i][1] * prices[purchased_items[i][0]]
print("total is:")
print(str(total)+"$")
