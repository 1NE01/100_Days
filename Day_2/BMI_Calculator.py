import os
height = float(input("Enter your height in meters : "))
weight = float(input("Enter your wieght in kilograms : "))

bmi = weight / height**2
os.system('clear')

print("Your BMI is " + str(bmi))
