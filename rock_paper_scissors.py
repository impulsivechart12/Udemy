import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choices_list = [rock, paper, scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n'))
if user_choice >= 3 or user_choice < 0:
    print("You type and invalid option, you lose")
else:
    print(choices_list[user_choice])

    computer_choice = random.randint(0,2)
    print(f'Computer chose:{choices_list[computer_choice]}')

    if user_choice == computer_choice:
        print("It's a draw")
    elif user_choice >= 3 or user_choice < 0:
        print("You type and invalid option, you lose")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose")
    elif user_choice == 1 and computer_choice == 0:
        print("You win")
    elif user_choice ==2 and computer_choice == 0:
        print("You Lose")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")





