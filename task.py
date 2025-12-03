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

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][0])

travel_log = {
    "France": {
        "total_visits": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "total_visits": 5,
        "cities_visited": ["Stuttgart", "Berlin"]
    },
}

print(travel_log["Germany"]["cities_visited"][0])
