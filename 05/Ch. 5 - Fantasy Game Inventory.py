inventory = {'gold coin': 42, 'rope': 1}

def displayInventory(inventory):
    print("Inventory:")
    for item, amount in inventory.items():
        print(str(amount) + " " + item)

    print("Total number of items: " + str(sum(inventory.values())))
    return(inventory)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory.keys():
            inventory.setdefault(item, 1)
        else:
            inventory[item] = inventory[item] + 1
    return inventory


displayInventory(addToInventory(displayInventory(inventory), dragon_loot))