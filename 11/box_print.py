"""

***************
*             *
*             *
*             *
***************

"""


def boxPrint(symbol, width, height):
    print(symbol * width)
    for i in range(height - 2):
        print(f'{symbol}{" " * (width - 2)}{symbol}')
    print(symbol * width)


boxPrint('*', 15, 5)
