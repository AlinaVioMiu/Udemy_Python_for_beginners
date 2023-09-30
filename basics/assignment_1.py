# DRIVERS LICENCE APPLICATION
first_name = input('first name = ')
last_name = input('last name = ')
age = int(input('age = '))
ssn = int(input('ssn = '))
height = float(input('height = '))
weight = float(input('weight = '))
print(first_name, last_name, age, ssn, height, weight)

first_name = input("Enter your first name: ").title()
second_name = input("Enter your second name: ").title()
age = int(input("Enter your age:"))
if age >= 18:
    social_security_number = int(input("Enter your social security number: "))
    height = float(input("Enter your height in cm: "))
    weight = int(input("Enter your weight in kg: "))

else:
    print("Sorry, you are not eligible to apply for driving license")
