import random

guess = ''
outcomes = ['heads', 'tails']
while guess not in outcomes:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.choice(outcomes)

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
