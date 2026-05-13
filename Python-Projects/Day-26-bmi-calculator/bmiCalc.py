# Day 26: Simple BMI Calculator

print("BMI CALCULATOR")
print("=" * 20)

# Gets weight
weight = float(input("Enter weight in kg: "))

# Gets height
height = float(input("Enter height in meters: "))

# Calculates BMI
bmi = weight / (height * height)

# Shows result
print("\nYour BMI is: " + str(bmi))

# Tells the user what it means
if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal weight")
elif bmi < 30:
    print("You are overweight")
else:
    print("You are obese")