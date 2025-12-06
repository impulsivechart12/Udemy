import random

EASY = 10
HARD = 5

def compare_guess(guess, chosen_number, user_lives):
    if guess == chosen_number:
        print("Correct!")
    elif guess > chosen_number:
        print("Too high!")
        return user_lives - 1
    elif guess < chosen_number:
        print("Too low!")
        return user_lives - 1

def select_difficulty():
    chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if chosen_difficulty == "easy":
        return EASY
    elif chosen_difficulty == "hard":
        return HARD
    else:
        print("You did not choose a difficulty! You get Hard")
        return HARD

def play_game():
    print("Welcome to the Guessing Game!\n"
          "I'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    lives = select_difficulty()
    still_playing = True
    while still_playing:
        print(lives)
        user_guess = int(input("Guess which number I am thinking: \n"))
        lives = compare_guess(user_guess, answer, lives)
        if lives == 0:
            print("You ran out of lives!")
            still_playing = input("Do you want to play again? Type 'yes' or 'no':\n")
            if still_playing == "yes":
                play_game()
            elif still_playing == "no":
                still_playing = False
        elif user_guess == answer:
            print("You won the guessing game!")
            still_playing = input("Do you want to play again? Type 'yes' or 'no':\n")
            if still_playing == "yes":
                play_game()
            elif still_playing == "no":
                still_playing = False

play_game()