# print('''
#  _                                     _     _                 _
# | |                                   (_)   | |               | |
# | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
# | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
# | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
#  \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
# ''')

print("Welcome to Treasure Island \n"
      "Your mission is to find the treasure")

direction = input('You\'re are at a cross road. Where do you want to go? Type "Left" or "Right" \n').lower()

if direction == "left":
    direction = input('You come across a lake. Do you want to Wait for a boat or Swim across? Type "Wait" or "Swim"\n').lower()
    if direction == "wait":
        direction = input("You arrive at the island unharmed. there is a house with 3  doors. One red, one yellow, and one blue. Which color do you choose?")
        if direction == "red":
            print("There is fire everywhere ahhhhhhhhh!!!")
        elif direction == "blue":
            print("The door is booby trapped, and you are done son!")
        elif direction == "yellow":
            print("You found the Treasure congratulations!!")
        else:
            print("Input a choice that is not an option, game over dude.")
    else:
        print('you were eaten by a monstrous catfish \n'
              'game over')
else:
    print("You fell into a hole \n"
          "game over")