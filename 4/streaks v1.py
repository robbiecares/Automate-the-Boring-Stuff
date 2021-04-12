import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = []
    count = 0
    while count < 100:
        flip = random.randint(0,1)
        if flip == 0:
            flips.append("H")
        else:
            flips.append("T")
        count += 1

    # Code that checks if there is a streak of 6 heads or tails in a row.
    x=0
    while x < 95:
        flip1 = flips[x]
        flip2 = flips[x+1]
        flip3 = flips[x+2]
        flip4 = flips[x+3]
        flip5 = flips[x+4]
        flip6 = flips[x+5]
        if flip1 == flip2:
            if flip2 == flip3:
                if flip3 == flip4:
                    if flip4 == flip5:
                        if flip5 == flip6:
                            numberOfStreaks += 1
                            x += 1
                        else:
                            x += 1
                    else:
                        x += 1
                else:
                    x += 1
            else:
                x += 1
        else:
            x += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))