import random
from Day_14.art import logo, vs
from Day_14.game_data import data
import os
def pick_celebrity():
    """Function that picks a random celebrity from out list of data from game_data.py"""
    return random.choice(data)

def return_celebrity_info(celebrity_dict):
    """ Function to print the celebrity information, such as name, descriptionn and country """
    return f"{celebrity_dict['name']}, a {celebrity_dict['description']} from {celebrity_dict['country']}"

def decide_winner(celebrity_A, celebrity_B):
    
    """ Function that returns the whether choice A or B have higher follower count """
    if celebrity_A['follower_count'] > celebrity_B['follower_count']:
        return 'a'
    return 'b'
def print_battle(celebrity_A, celebrity_B):
    print('Compare A: ' + return_celebrity_info(celebrity_A))

    print(vs)

    print('Against B: ' + return_celebrity_info(celebrity_B))



isGameOver = False
game_score = 0


choiceA = pick_celebrity()
choiceB = pick_celebrity()


while choiceA == choiceB:
    choiceB = pick_celebrity()


print(logo)


while not isGameOver:
  
    print_battle(choiceA, choiceB)

    user_pick = input("Who has more followers? Type 'A' or 'B' ").lower()

    if user_pick == decide_winner(choiceA, choiceB):
        os.system('cls')
        print(logo)
        game_score += 1
        print(f'You are right! The current score is {game_score}')
        choiceA = choiceB
        choiceB = pick_celebrity()
    
    else:
        print(f'Sorry! That\'s wrong :( \n\nFinal Score: {game_score}')
        isGameOver = True

