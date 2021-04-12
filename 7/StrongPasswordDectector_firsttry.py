# ! python3
# StrongPasswordDectector_firsttry.py - to check the string of a given string as a password

import re

def TryAgain(WhatsWrong):
    print("The password is " + WhatsWrong + ".\n")

password = input('''Please choose a password that meets the below criteria:
*Contains at least one upper case character (A-Z)
*Contains at least one lower case character (a-z)
*Contains at least one digit (0-9)

Password: ''')

UpperCaseRegex = re.compile(r'[A-Z]')
LowerCaseRegex = re.compile(r'[a-z]')
DigitRegex = re.compile(r'\d')

UCase = UpperCaseRegex.search(password)
LCase = LowerCaseRegex.search(password)
Digit = DigitRegex.search(password)


keys = ["hasupper", "haslower", "hasdigit", "AtLeast8"]
rules = {}

for i in keys:
    rules[i] = ""

while all(rules.values()) != True:
    for k in rules.keys():
        rules[k] = False
    if len(password) >= 8:
        rules["AtLeast8"] = True
    for char in password:
        if rules["hasupper"] == False:
            if UpperCaseRegex.search(char) != None:
                rules["hasupper"] = True
                continue
        elif rules["haslower"] == False:
            if LowerCaseRegex.search(char) != None:
                rules["haslower"] = True
                continue
        else: #"hasdigit" == False:
            if DigitRegex.search(char) != None:
                rules["hasdigit"] = True
                continue
    if all(rules.values()) == True:
        break
    else:
        print("The password does not meet the defined criteria. Please choose a different password: ")
        password = input()
        continue

print("You have a strong password")



