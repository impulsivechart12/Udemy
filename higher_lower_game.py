from higher_lower_art import logo, vs
from higher_lower_data import data
import random


def get_random_account():
    """Select a random account from the Data dictionary."""
    return random.choice(data)


def format_data(account):
    """Takes the account data and turns it into printable format."""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """take the user gues and follower counts and returns if they get it right."""
    if choice_a_followers > choice_a_followers:
        return guess == 'a'
    else:
        return guess == 'b'


score = 0
playing_game = True
choice_b = get_random_account()

# make the game repeatable.
while playing_game:
    # select two random accounts

    # make account at position B become the next account at position A
    choice_a = choice_b
    choice_b = get_random_account()

    while choice_a == choice_b:
        choice_b = get_random_account()

    # print formatted data
    print(f"Compare A: {format_data(choice_a)}")
    print(vs)
    print(f"Compare B: {format_data(choice_b)}")

    # ask guess for user
    guess = input("Who has more followers? Type 'A' or 'B': \n").lower()

    # check if user is correct
    ## get follower count of each account
    choice_a_followers = choice_a['follower_count']
    choice_b_followers = choice_b['follower_count']
    is_correct = check_answer(guess, choice_a_followers, choice_b_followers)

    # give user feedback on their guess
    # score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        playing_game = False
        print(f"Sorry you did not get the write answer, your final score: {score}")

# clear the screen between rounds
