"""
Dice Rolling Simulator: A program that simulates rolling dice
"""
# use a while loop to make the code continuosly run
# use the random.randint functions to select a number between 1 and 6
# print te selected number
# ask if playing again: if yes, continue, if no quit
import random

try:
    minimum_value = int(input("Enter a mininum number: "))
    maximum_value = int(input("Enter a maximum number: "))
except:
    print('Wrong input, default values would be used')
    minimum_value = 1
    maximum_value = 6


def dice_rolling():
    random_num = random.randint(minimum_value, maximum_value)

    print(random_num)


play_again = True
while play_again:
    dice_rolling()
    input_ans = input('Do you want to play again? ')
    if input_ans == 'yes' or input_ans == 'y':
        play_again = True
    else:
        play_again = False
