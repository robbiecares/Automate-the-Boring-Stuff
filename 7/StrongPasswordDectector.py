# ! python3
# StrongPasswordDectector_firsttry.py - to check the string of a given string as a password

import re

# accept user input for password
pw = input('''Please choose a password that meets the below criteria:
*Contains at least one upper case character (A-Z)
*Contains at least one lower case character (a-z)
*Contains at least one digit (0-9)

Password: ''')

isstrong = False

while not isstrong:

    # capture reasons for weak pw
    weak_reasons = []

    # ensure pw is at least 9 characters (use len)
    islong = False
    if len(pw) >= 8:
        islong = True
    else:
        weak_reasons.append('too short')

    # ensure pw has at least one uppercase char (rx)
    hasupper = False
    uppercaseregex = re.compile(r'[A-Z]')
    ucase = uppercaseregex.search(pw)
    if ucase != None:
        hasupper = True
    else:
        weak_reasons.append('missing an uppercase character')

    # ensure pw has at least one lowercase char (rx)
    haslower = False
    lowercaseregex = re.compile(r'[a-z]')
    lcase = lowercaseregex.search(pw)
    if lcase != None:
        haslower = True
    else:
        weak_reasons.append('missing a lowercase character')

    # ensure pw has at least one digit (rx)
    hasdigit = False
    digitregex = re.compile(r'[0-9]')
    digit = digitregex.search(pw)
    if digit != None:
        hasdigit = True
    else:
        weak_reasons.append('missing a digit')

    # if all checks are true, return true
    if len(weak_reasons) > 0:
        print('Your password is:')
        for i in weak_reasons:
            print(i)
        pw = input('Please enter a different password:')
    else:
        isstrong = True
        print('Your password is strong!')

