# import csv
#
# o = []
# with open("./weather_data.csv") as data:
#     danny = csv.reader(data)
#     temperature = []
#
#     for i in danny:
#         o.append(i)
#
#     for i in range(1, len(o)):
#         temperature.append(int(o[i][1]))
# #     print(temperature)
# import pandas
# data = pandas.read_csv("weather_data.csv")
# # temp_list = data["temp"].to_list()
# # temp_list.m
# #
# # print(data[data.temp==data.temp.max()])
# mon=data[data.day=="Monday"]
# print(mon.temp*1.8+32)
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel=data[data.Primary_Fur_Color=="Gray"]
black_squirrel=data[data.Primary_Fur_Color=="Black"]
cinamon_squirrel=data[data.Primary_Fur_Color=="Cinnamon"]


print(f"The gray squirel count={len(gray_squirrel.Primary_Fur_Color)}")
print(f"The black suirel count={len(black_squirrel.Primary_Fur_Color)}")
print(f"The cinamon suireel count={len(cinamon_squirrel.Primary_Fur_Color)}")

data_dict={
    "Fur Color":["Gray","Cinamon","Black"],
    "Count":[len(gray_squirrel.Primary_Fur_Color),len(black_squirrel.Primary_Fur_Color),len(cinamon_squirrel.Primary_Fur_Color)]
}
df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
