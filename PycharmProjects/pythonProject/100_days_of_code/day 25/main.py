# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)



# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())

# Data in columns
# print(data["temp"].max())
# print(data.condition.max())

# Data in row
# print(data[data["day"] == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(int(monday.temp) * 1.8 + 32)


# create a dataframe from stretch
# data_dict = {
#     "students": ["A", "B", "C"],
#     "scores": [76, 65, 23]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)


import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(df[df["Primary Fur Color"] == "Gray"])
red_squirrels = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(df[df["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

data = pd.DataFrame(data_dict)
data.to_csv("squirel_counts.csv")

