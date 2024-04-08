# Tip Calculator

total_bill = float(input("Welcome to the tip calculator!\n What was the total bill? $"))

tip = float(input("How much tip would you like to give? 10, 12 or 15? "))

tip_percentage = 1 + tip/100

num_people = int(input("How many people to slip the bill? "))

result = (total_bill/num_people) * tip_percentage

round_result = round(result, 2)

format_result = format(round_result, ".2f")

print(f"Each person should pay: ${format_result}")
