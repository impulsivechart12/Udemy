import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
password_list = []

for number in range(1, nr_letters + 1):
    character_count = len(letters)
    random_number = random.randint(0, character_count - 1 )
    password_list.append(letters[random_number])

for number in range(1, nr_symbols + 1):
    character_count = len(symbols)
    random_number = random.randint(0, character_count - 1)
    password_list.append(symbols[random_number])

for number in range(1, nr_numbers + 1):
    character_count = len(numbers)
    random_number = random.randint(0, character_count - 1)
    password_list.append(numbers[random_number])

random.shuffle(password_list)

for character in password_list:
    password += character

number_of_char = len(password_list)

print(f"Your new password is {password}")
print(number_of_char)
