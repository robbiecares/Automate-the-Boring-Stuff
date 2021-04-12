import random
set_of_flips = []
desired_set_count = 10000
current_set_count = 0
desired_set_length = 100
current_set_length = len(set_of_flips)
desired_streak_length = 6
numberOfStreaks = 0
sets_checked = 0
first_flip_in_check_set = 0

for flip in range(desired_set_count):

    # Code that creates a list of 100 'heads' or 'tails' values.
    while current_set_length < desired_set_length:
        flip = random.randint(0,1)
        if flip == 0:
            set_of_flips.append("H")
        else:
            set_of_flips.append("T")
        current_set_length += 1


    # Code that checks if there is a streak of 6 heads or tails in a row.
    while first_flip_in_check_set <= len(set_of_flips) - desired_streak_length:
        check_set = set_of_flips[first_flip_in_check_set:first_flip_in_check_set+desired_streak_length]
        if check_set == (["H"] * desired_streak_length):
            numberOfStreaks += 1
            sets_checked += 1
            first_flip_in_check_set += desired_streak_length
        elif check_set == (["T"] * desired_streak_length):
            numberOfStreaks += 1
            first_flip_in_check_set += desired_streak_length
            sets_checked +=1
        else:
            first_flip_in_check_set += 1
            sets_checked +=1
    check_set = []
    current_set_length = 0
    first_flip_in_check_set = 0
    set_of_flips = []


print("Number of trials: " + str(current_set_count))
print("Number of flips per trial: " + str(current_set_length))
print("Total number of flips: " + str(current_set_count*current_set_length))
print("Number of streaks: " + str(numberOfStreaks))
print("Number of sets checked: " + str(sets_checked))
print('Chance of streak: %s%%' % (numberOfStreaks / sets_checked * 100))

#This experiment increments the first item in the check set by the streak length after every check.
#There is an arguement to increment the check set by one item (rather than the streak length) after every check.
#e.g. If checking for a steak length of three, should check set [H1,H2,H3,H4,H5,H6] return two streaks(H1:H3 & H4:H6)
#or four streaks (H1:H3,H2:H4,H3:H5,H4:H6)?
#i.e. If a streak is found should I increment by one or by the streak length? What if no streak is found?