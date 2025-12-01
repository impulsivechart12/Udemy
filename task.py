# import random
#
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

programing_dictionary = {"Bug": "An error in a program that prevents the program from running as expected",
                         "Loop": "The action of doing something over and over again",
                         "Function": "A piece of code that you can easily call over and over again."}

for thing in programing_dictionary:
    print(thing)
    print(programing_dictionary[thing])