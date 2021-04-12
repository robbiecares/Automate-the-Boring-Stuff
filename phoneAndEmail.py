#! python3
# phoneAndEmail.py - A program to search text for phone numbers & email addresses.

import re
import pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

#([a-zA-Z0-9_\-\.]+@+[a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5})

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                # All characters. Special characters cannot appear as the first or last character or appear consecutively two or more times.
    @                                # @
    [a-zA-Z0-9.-]+                   # numbers, letters, hyphens or periods
    \.[a-zA-Z]{2,4}                  #something
    )''', re.VERBOSE)


text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum)
for groups in emailRegex.findall(text):
       matches.append(groups)


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

