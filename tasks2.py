# friends = ["Ashley", "Cole", "Erin", "Joe", "Matt", "Sara", "Zach"]
# random_friend = random.choice(friends)
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]

# Functions with more than 1 inputs

# def greet_with(name, location):
#     print(f"Hello, {name}!")
#     print(f"What is it like in {location}?")
#
# greet_with(location="Cole", name="Minnesota")

# programing_dictionary = {"Bug": "An error in a program that prevents the program from running as expected",
#                          "Loop": "The action of doing something over and over again",
#                          "Function": "A piece of code that you can easily call over and over again."}
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }
#
# print(travel_log["France"][1])
#
# nested_list = ["A", "B", ["Poop", "D"]]
# print(nested_list[2][0])
#
# travel_log = {
#     "France": {
#         "total_visits": 8,
#         "cities_visited": ["Paris", "Lille", "Dijon"]
#     },
#     "Germany": {
#         "total_visits": 5,
#         "cities_visited": ["Stuttgart", "Berlin"]
#     },
# }
#
# print(travel_log["Germany"]["cities_visited"][0])


# def format_name(first_name, last_name):
#     if first_name=='' or last_name=='':
#         return
#     formated_f_name = first_name.title()
#     formated_l_name =  last_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
# print(format_name(input("Enter your first name: "), input("Enter your last name: ")))


# def function_1(text):
#     return text + text
#
# def  function_2(text):
#     return text.title()
#
# output = function_2(function_1("COLE"))
# print(output)


# enemies = 1
#
# def increase_enemies():
#     global enemies = 2
# #     print(f"enemies inside function: {enemies}")
# #
# # increase_enemies()
# # print(f"enemies outside function: {enemies}")
# #
# # def game():
# #     def drink_potion():
# #         print(player_health)
# #     drink_potion()
# #
# # game()
#
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
#
# def create_enemy():
#     if game_level < 5:
#         new_enemy = enemies[0]
#
#     print(new_enemy)



# def my_fucntion():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it!")
#
#
# my_fucntion()

# dice_numbers = ["1", "2", "3", "4", "5", "6"]
# dice_numb = random.randint(1, 6)
# print(dice_numbers[dice_numb])

# year = int(input("What year were you born?\n"))
#
# if year > 1980 and year < 1994:
#     print("You are a Millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")
#
# try:
#     age = int(input("What is your age?\n"))
# except ValueError:
#     print("You have typed in valid number. Please type using a numerical value.")
#     age = int(input("What is your age?\n"))
#
# if age > 18:
#     print(f"You can drive a car at {age}.")
