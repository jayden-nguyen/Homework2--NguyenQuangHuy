import sys
def test(did_pass):

    linenum = sys._getframe(1).f_lineno
    # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
n = 0
def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = 0
    inventory[fruit] += quantity
    global n
    n += inventory.get(fruit)
    inventory[fruit] = n
new_inventory = {}
add_fruit(new_inventory, "strawberry",10)
test("strawberry" in new_inventory)
test(new_inventory["strawberry"]==10)
add_fruit(new_inventory, "strawberry",25)
test(new_inventory["strawberry"]==35)

