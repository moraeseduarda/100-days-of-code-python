# The Great Squirrel Census Data Analysis
# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_color_count)
print(black_color_count)
print(cinnamon_color_count)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_color_count, black_color_count, cinnamon_color_count]
}

print(data_dict)
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
