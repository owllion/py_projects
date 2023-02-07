# with open("./weather_data.csv") as data:
#     dataList = data.readlines()
#     print(dataList)
# import csv
import pandas
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#
#     temperature = []
#     for single_data in data:
#         print(single_data)
#         temperature.append(single_data[1])
#     new_temp = map(int, temperature[1:])
#     print(list(new_temp))

# 上面太麻煩了 用pandas
# import pandas as p
#
# data = p.read_csv("weather_data.csv")
#
# # Dataframe -> whole table / 2 dimension
# dic_cer = data.to_dict()
# print(dic_cer)
#
# temp_list = data["temp"].to_list()
# # Series -> single column(i.g temp) / list / 1 dimension
#
# avg_temp = sum(temp_list) // len(temp_list)
# print(avg_temp)
#
# # Get the highest temperature
# highest = data["temp"].max()
# avg = data["temp"].mean()
# print(f"highest: {highest}, avg temp: {avg}")
#
# # Get data in Row
# print(data[data.temp == highest])
#
# my_data = {
#     "grade": [3, 6, 2],
#     "name": ["James", "Angela", "Justin"]
# }
# data_frame = pandas.DataFrame(my_data)
# data_frame.to_csv("new_data.csc")

# -----------------------------
# find the number of each color of squirrel
# Primary Fur Color
import pandas as p

data = p.read_csv("squirrel.csv")
# print(data["Primary Fur Color"])
# 記得這邊要用的是雙層data去做filter喔! 單層無效!
num_of_gray = len(data[data["Primary Fur Color"] == "Gray"])
num_of_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
num_of_black = len(data[data["Primary Fur Color"] == "Black"])
print(num_of_gray)
print(num_of_cinnamon)
print(num_of_black)

# Create a dataframe
squirrel_color = {
    "fur_color": ["Gray", "Cinnamon", "Black"],
    "Number": [num_of_gray, num_of_cinnamon, num_of_black]
}
squirrel_data = pandas.DataFrame(squirrel_color)
squirrel_data.to_csv("squirrel_fur_color.csv")
