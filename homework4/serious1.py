inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['pocket'] = ['seashell','strange berry', 'lint']
print('after add "pocket"')
print(inventory)

inventory['backpack'].sort()
print("after sort 'backpack'")
print(inventory)

inventory['backpack'].remove('dagger')
print('after remove "dagger" in backpack')
print(inventory)

inventory['gold'] += 50
print("after add 50 to gold")
print(inventory)
