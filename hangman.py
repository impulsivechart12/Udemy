import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
print(logo)
print(f"Psst, the solution is {chosen_word}")

guessed_letter = []
display = []
word_length = len(chosen_word)
for number in range(word_length):
    display += "_"

end_game = False
lives = 6

while not end_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        if guess in guessed_letter:
            print(f"You have alreadly guessed the letter {guess}")
        else:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life\n"
              f"-----------------------------")
            if lives == 0:
                end_game = True
                print("You Lose!")

    guessed_letter += guess
    print(display)

    if "_" not in display:
        end_game = True
        print("You win!")

    print(stages[lives])