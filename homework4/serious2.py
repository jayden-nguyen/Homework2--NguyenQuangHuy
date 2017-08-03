prices = {"banana" : 4,
          "apple" : 2,
          "orange" : 1.5,
          "pear" : 3}
purchased = {
        "banana": 5,
        "orange":3
    }
purchased_items = list(purchased.items())
total = 0
for i in range(len(purchased_items)):
    print(purchased_items[i][0],"quantity: ",purchased_items[i][1]," price: ",prices[purchased_items[i][0]])
    total += purchased_items[i][1] * prices[purchased_items[i][0]]
print(total)
