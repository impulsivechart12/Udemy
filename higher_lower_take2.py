import random
from os import system
from higher_lower_data import data

# Format and print out the accounts being compared
def format_account_info(account_data):
    name = account_data['name']
    account_description = account_data['description']
    account_location = account_data['country']
    return f"{name}, a {account_description}, from {account_location}."

# select a random number to get a random item out of the data
def get_random_account():
    account = random.choice(data)
    return account

# compare both answers and decide who has more followers
def compare_accounts(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == 'a'
    else:
        return guess == 'b'

score = 0
still_playing = True
account_b = get_random_account()
while still_playing:

    account_a = account_b
    account_b = get_random_account()

    if account_a == account_b:
        account_b = get_random_account()

    print(f"compare A: {format_account_info(account_a)}\n"
          f"VS")
    print(f"Against B: {format_account_info(account_b)}")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    account_a_followers = account_a['follower_count']
    account_b_followers = account_b['follower_count']
    is_correct = compare_accounts(user_guess, account_a_followers, account_b_followers)

    if is_correct:
        score += 1
        still_playing = True
        print("\n"
              "\n")
    else:
        still_playing = False
        print(f"Sorry, that's wrong. Final score: {score}")