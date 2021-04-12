#! python3
# SandwichMaker.py - a program for determining sandwich prices

'''
Sandwich Maker
Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
'''

import pyinputplus as pyip

bread = pyip.inputMenu(["wheat", "white", "sourdough"])

protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"])

prompt = "Would you like cheese on that?"
cheese = pyip.inputYesNo(prompt)

prompt = "Would you like mayo, mustard, lettuce, or tomato?"
VegAndSauce = pyip.inputYesNo(prompt)

prompt = "How many sandwiches would you like?"
NumOfSands = pyip.inputInt(prompt, min = 1)

breadprice = {"wheat": 1, "white": 1, "sourdough": 1.25}
proteinprice = {"chicken": 1, "turkey": 1.25, "ham": 2, "tofu": 1.5}
cheeseprice = 1
VegAndSaucePrice = .75

price = breadprice[bread] + proteinprice[protein]
print("bread: $" + str(breadprice[bread]))
print("protein: $" + str(proteinprice[protein]))

if cheese == "yes":
    price += cheeseprice
    print("cheese: $" + str(cheeseprice))

if VegAndSauce == "yes":
    price += VegAndSaucePrice
    print("Veggies & Sauces: $" + str(VegAndSaucePrice))

print("Total: $" + str(price) + " x " + str(NumOfSands) + " sandwiches = $" + str(price*NumOfSands))















