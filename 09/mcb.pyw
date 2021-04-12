#! python3

# mcb.pyw - Saves and load pieces of text to the clipboard

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - deletes saved keyword.
#        py.exe mcb.pyw delete - deletes all saved keywords.

import shelve
import sys
import pyperclip

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3:
    keyphrase = sys.argv[2]
    if sys.argv[1].lower() == 'save':
        mcbShelf[keyphrase] = pyperclip.paste()
    if sys.argv[1].lower() == 'delete':
        del mcbShelf[keyphrase]

elif len(sys.argv) == 2:
    keyphrase = sys.argv[1]
    if sys.argv[1].lower() == 'list':
        # List keywords
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        # delete all keywords
        for key in mcbShelf.keys():
            del key

    else:
        # copy saved value from shelf
        if keyphrase in mcbShelf:
            pyperclip.copy(mcbShelf[keyphrase])
            print(f'Text for {keyphrase} copied to clipboard.')
        else:
            print(f'There is no text for {keyphrase}')

mcbShelf.close()
