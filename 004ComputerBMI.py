#prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds:"))

#prompt the user to enter height in inches
height = eval(input("Enter height in inches:"))

KilogramsPerPound = 0.45359237
MetersPerInch = 0.0254

weightInKilograms = weight * KilogramsPerPound
heightInMeters = height * MetersPerInch
bmi = weightInKilograms / (heightInMeters * heightInMeters)

#display result
print("BMI is", format(bmi, ".2f"))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

    
