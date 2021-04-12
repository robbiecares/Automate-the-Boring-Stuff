#! python3
# DateDetection.py - to detect valid dates in the format DD/MM/YYYY (years = 1000 - 2999)

import re

text = "29/02/2004"
#text = input("Please enter a date in the format 'DD/MM/YYYY':")

DateRegex = re.compile(r'([0-9][0-9])/([0-9][0-9])/([0-9][0-9][0-9][0-9])')

date = DateRegex.search(text)

#store result of match into variable (use mult. assgn. groups trick)
day, month, year = date.groups()

day = int(day)
#month = month
year = int(year)

#code to confirm if date is valid (based on number of days in each month & leap years)

def BadDate():
    print("invalid date")

if day > 31:
    BadDate()

ThirtyDayMonths = ["09","04","06","11"]
if month in ThirtyDayMonths:
    if day > 30:
        BadDate()

LeapYear = []
for i in range(1000,2999,4):
    LeapYear.append(i)
for i in LeapYear:
    if i % 100 == 0 and i % 400 != 0:
        LeapYear.remove(i)

if month == "02":
    if day > 29:
        BadDate()
    elif day > 28 and year not in LeapYear:
        BadDate()
    else:
        print("Else Stmt")

print(day)
print(str(month))
print(year)

print(LeapYear)

# TODO: month is printing as the integer 2 rather than the 02. Need to correct
