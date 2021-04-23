# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
guessed = []
for guesses in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    while guess in guessed:
        print("You already guessed that number, guess a different number!")
        guess = int(input())
    guessed.append(guess)

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guesses) + ' guesses! Your guesses were ' + str(guessed[:-2]) + "&" + str(guessed[-1]) + ".")
    #print('Good job! You guessed my number in ' + str(guesses) + ' guesses! Your guesses were ' + str(guessed) + ".")

else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))