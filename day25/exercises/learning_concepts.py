# Using just file methods
with open("weather_data.csv") as weather_data:
    data = weather_data.readlines()
    print(data)

# Using csv library
import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature_number = int(row[1])
            temperature.append(temperature_number)
    print(temperature)

# Using the pandas library
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

# Converting to df and series
# all_data = data.to_dict()
# print(all_data)
# temp_data = data["temp"].to_list()
# print(temp_data)

print(data["temp"].mean())
print(data["temp"].max())

# Get data in columns
print(data["Condition"])
print(data.Condition)
print(data.day)

# Get data in row
print(data[data.day == "Monday"])

# CHALLENGE: Print the row of data which had the biggest temperature.
highest_temp = data["temp"].max()
print(data[data.temp == highest_temp])

monday = data[data.day == "Monday"]
print(monday.Condition)

# CHALLENGE: Convert Monday's temperature to Fahrenheit.
# Hint: use [] to get a single value from the pandas Series by index.

# Get Row data value

monday_temp_celsius = monday.temp[0]
monday_temp_fahrenheit = (monday_temp_celsius * 1.8) + 32
print(monday_temp_fahrenheit)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [78, 56, 90]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
