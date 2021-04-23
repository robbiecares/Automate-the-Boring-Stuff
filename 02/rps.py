"""Rock, Paper, Scissors game"""

import random

# Choose an object
objs = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

active = True
player_obj = None
history = {}
games_played = 0


def determine_winner(player_obj, pc_obj):
    player_obj = objs[player_obj]
    pc_obj = objs[pc_obj]

    if player_obj == pc_obj:
        print(f"You chose {player_obj}, PC choose {pc_obj}, it's a draw!")
        outcome = 'tie'

    else:
        if (player_obj == 'rock' and pc_obj == 'scissors') or (player_obj == 'paper' and pc_obj == 'rock') or \
                (player_obj == 'scissors' and pc_obj == 'paper'):
            outcome = 'win'
        else:
            outcome = 'lose'

        print(f'You chose {player_obj}, PC choose {pc_obj}, you {outcome}!')

    return outcome


while active is True:

    # player picks object
    player_obj = input('Choose your weapon: (r)ock, (p)aper, (s)cissors or <(q)uit game>')
    if player_obj == 'q':
        active = False
        continue
    if player_obj not in list(objs.keys()):
        print("please choose a valid option: (r), (p), (s) or (q)")
        continue

    # pc picks random object
    pc_obj = random.choice(list(objs.keys()))

    # determine winner
    outcome = determine_winner(player_obj, pc_obj)

    # update stats
    games_played += 1
    history[games_played] = (player_obj, outcome)

    outcomes = []
    for deets in history.values():
        obj, outcome = deets
        outcomes.append(outcome)
    w = outcomes.count('win')
    l = outcomes.count('lose')
    t = outcomes.count('tie')
    win_pro = w / games_played * 100

    # display score
    print(f"w/l/t: {w}/{l}/{t}\n"
          f"games played: {games_played}\n"
          f"win%: {win_pro}%\n")

