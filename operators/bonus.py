height = 6.2
weight = 85

# bmi = weight in kg / (height * height in meters)

height_in_meters = height * 0.4536
bmi = weight / (height_in_meters * height_in_meters)
print('BMI=', bmi)
