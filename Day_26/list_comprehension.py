# # # # number=[1,2,3]
# # # # new_number = [n+1 for n in number]
# # # # print(new_number)
# # # # name="Tabashi"
# # # # list = [n for n in name]
# # # # print(list)
# # # numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # # # 🚨 Do Not Change the code above 👆
# # #
# # # #Write your 1 line code 👇 below:
# # #
# # # squared_numbers=[i**2 for i in numbers]
# # #
# # # #Write your code 👆 above:
# # #
# # # print(squared_numbers)
# # with open("file1.txt") as file1:
# #     a = file1.readlines()
# # with open("file2.txt") as file2:
# #     b = file2.readlines()
# #
# # list=[int(i) for i in a if i in b]
# # print(list)
# #
# #
# #
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# split=sentence.split(" ")
# result={i:len(i)for i in split}
#
#
# print(result)
#
#
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f={i:weather_c[i]*9/5+32for i in weather_c}


print(weather_f)