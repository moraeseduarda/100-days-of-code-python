# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# BMI Wikipedia Page

# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.usz.ch%2Fen%2Fbmi-calculator%2F&psig=AOvVaw2Q8s6qHj2Yi6cl_6OlQfea&ust=1710454314788000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCJjTgICh8oQDFQAAAAAdAAAAABAE

# NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests. See examples below.

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
kg = float(weight)
m = float(height)
bmi = kg/(m**2)
print(int(bmi))
