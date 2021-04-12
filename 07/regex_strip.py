# ! python3
# regex_strip.py - a regex version of Python's builtin .strip() method

import re


def rxstrip(string, stripchars=' '):
    # accept a user input which needs to be stripped
    # ex. '#*#meow!#***'

    # accept a user input of chars to remove from string_to_strip
    # ex. '#*'

    #convert stripchars to rx
    frontstripcharsrx = re.compile(f'(^[{stripchars}]+)(.*)')
    backstripcharsrx = re.compile(f'(.*?)([{stripchars}]+$)')

    # search string
    mo = frontstripcharsrx.search(string)
    if mo != None:
        front_trash, string = mo.groups()

    mo = backstripcharsrx.search(string)
    if mo != None:
        string, back_trash = mo.groups()

    print(string)
    print(len(string))


rxstrip('#*#meow!#***', '#*')
rxstrip('#*#meow!#***#', '#')
rxstrip('#*#meow!', '#')
rxstrip('    meow!   ',)
rxstrip('    meow   ', '#')
rxstrip('    meow   ')
rxstrip('******!Hello!*****','*')
rxstrip('******!Hello!**$***','*!')

