# DRIVERS LICENCE APPLICATION
first_name = 'Alina'
last_name = 'Miu'
age = 34
cnp = 123456789
height = 1.59
weight = 60.0
print(first_name, last_name, age, cnp, height, weight)

first_name = input("Enter your first name: ").title()
second_name = input("Enter your second name: ").title()
age = int(input("Enter your age:"))
if age >= 18:
   social_security_number = int(input("Enter your social security number: "))
   height = float(input("Enter your height in cm: "))
   weight = int(input("Enter your weight in kg: "))

else:
    print("Sorry, you are not eligible to apply for driving license")