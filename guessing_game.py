import random
from guessing_game_logo import logo

EASY_GUESSES = 10
HARD_GUESSES = 5


def check_guess(guess, answer, turns):
    """Will check if the guess is equal to the answer. Will subtract a turn if guess is incorrect"""
    if guess < answer:
        print("Too low.")
        return turns - 1
    elif guess > answer:
        print("Too high.")
        return turns - 1
    elif guess == answer:
        print(f"You got it! the answer was {answer}")


def difficulty():
    """Sets the number of turns based on players response."""
    level = input("What difficulty would you like to play? 'Hard' or Easy'?\n").lower()
    if level == 'easy':
        return EASY_GUESSES
    else:
        return HARD_GUESSES


def play_game():
    answer = random.randint(1, 100)
    print(logo)
    print("""Welcome to the number guessing game.
I am thinking of a number between 1 and 100?""")
    # answer for testing purposes.
    print(f"The number selected is {answer}")

    turns = difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Guess a number: "))

        turns = check_guess(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose.")
            return
        elif guess != 0:
            print("Guess again.")


play_game()
