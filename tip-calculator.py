print("Welcome to the tip calculator.")
bill = float(input("what was the total bill?"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15?")) / 100
split_number = int(input("How many people to split the bill?"))

# calculate the total into the tip
total = (bill * tip_percentage) + bill

# calculate the value that each person owes after splitting
total = round(total / split_number, 3)

#print what each person should owe

print(f"Each person should pay: ${total}")
