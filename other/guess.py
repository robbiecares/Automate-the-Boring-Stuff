"""have a user guess a random number within a certain amount of tries"""

import sys
import random

secret_num = random.randint(0, 30)
attempts = 1

guess = ''


def give_hint(attempts=1):
    if guess < secret_num:
        print('your guess is too low, guess again')
    elif guess > secret_num:
        print('your guess is too high, guess again')

while attempts < 6:
    guess = int(input('guess the number'))
    if guess == secret_num:
        print('you guessed the secret number!')
        sys.exit()
    else:
        give_hint()
        attempts += 1
        continue

print(f'nope, the secret number was {secret_num}')
sys.exit()

