# ! python3
# RegexStrip_firsttry.py - a regex version of the .strip method
import re

string = "***$123$***"
#string = input("Please enter a string: ")

StripChar = "*"
#StripChar = input('''Please input the character that you'd like to trim from the ends of the string. If you'd like to trim whitespace only just press enter.
#Character: ''')

def trimmer(string,StripChar = " "):

    modstring = string

    TrimFrontRegex = re.compile(r'^[StripChar]')
    FrontSearch = TrimFrontRegex.search(modstring)

    #StripBackRegex = re.search(r'(.*)([StripChar]*$)', modstring)

    while FrontSearch != None:
        modstring = modstring[1:]
        print(modstring)


"""
    FrontResult = StripFrontRegex.search(string)

    beg, afterbeg = FrontResult.groups()

    BackResult = StripBackRegex.search(afterbeg)

    mid, end = BackResult.groups()

    cutresult = mid

    print(cutresult)

    #TODO: backresult is leaving blankspaces at end of string
    #TODO:  incorporate second arguement (i.e. an alternative cut char) into code

"""

trimmer(string, StripChar)