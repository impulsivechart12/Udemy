import random
from typing import List

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["apple","pineapple","impulsive","supercar","astroid"]
chosen_word = random.choice(word_list)

print(f"Psst, the solution is {chosen_word}")


display = []
counter = "_"
word_length = len(chosen_word)
for number in range(word_length):
    display += "_"

end_game = False
lives = 7

while not end_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if letter != guess:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You Lose!")

    print(display)


    if "_" not in display:
        end_game = True
        print("You win!")

    print(stages[lives])
