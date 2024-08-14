# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()

# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature_number = int(row[1])
#             temperature.append(temperature_number)
#     print(temperature)

import pandas as pd

data = pd.read_csv("weather_data.csv")
# all_data = data.to_dict()
# temp_data = data["temp"].to_list()
#
# print(type(data))
# print(type(data["temp"]))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in columns
# print(data["Condition"])
# print(data.Condition)
# print(data.day)

# # Get data in row
# print(data[data.day == "Monday"])
#
# # CHALLENGE: Print the row of data which had the biggest temperature.
# highest_temp = data["temp"].max()
# print(data[data.temp == highest_temp])

monday = data[data.day == "Monday"]
print(monday.Condition)

# CHALLENGE: Convert Monday's temperature to Fahrenheit.
# Hint: use [] to get a single value from the pandas Series by index.
