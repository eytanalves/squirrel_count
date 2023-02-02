# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temp_data = []
#     for row in data:
#          if row[1] != "temp":
#             temp_data.append(int(row[1]))
#
# print(temp_data)

import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(data[data["temp"] == data["temp"].max()])
#
# print(data[data["day"] == "Monday"])
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = (monday_temp * 9/5) + 32
# print(monday_temp_f)
#
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data-2.csv")
gray_data = len(data[data["Primary Fur Color"] == "Gray"])
rad_data = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_data = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "color_fur" : ["gray", "cinnamon", "black"],
    "count" : [gray_data, rad_data, black_data]
}

df = pandas.DataFrame(data_dict)

df.to_csv("squirrel_count.csv")