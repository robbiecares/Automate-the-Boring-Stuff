def collatz(number):
    if number%2 == 0:
        print(number//2)
        return(number//2)
    else:
        number%2 == 1
        print(3*number+1)
        return(3*number+1)

def guess_number():
    number = ""
    print("Guess any number and with a simple math formula I can make it equal to one!")
    while type(number) != int:
        try:
            number = int(input())
        except ValueError:
            print("please enter a number")
    return number

number = guess_number()
while number != 1:
    number = collatz(number)
else:
    print("Now your number equals one")
    exit