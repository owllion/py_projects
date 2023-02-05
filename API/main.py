# import requests
# import datetime
# url = "https://api.sunrise-sunset.org/json"
# MY_LONG = "120.960518"
# MY_LAT = "23.697809"
#
# params = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0
# }
# response = requests.get(url=url, params=params)
# #Here we can also use the inline parameters ->
# #https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
#
# response.raise_for_status()
# data = response.json()
# sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
# sunset = data['results']['sunset'].split("T")[1].split(":")[0]
# print(sunrise)
# print(sunset)
#

#absolute
# with open("C:/Users/defra/OneDrive/桌面/test.txt", mode="w") as file:
#     file.write("Yes,fiesta")
#
# with open("C:/Users/defra/OneDrive/桌面/test.txt", mode="a") as file:
#     contents = file.write("\nnew line 123!")
#     print(contents)

