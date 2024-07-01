print("Welcome to the BMI Calculator:")
height = float(input("enter your height:\n"))
weight = float(input("enter your weight:\n"))

heightSquared = height * height

bmi = round((weight / heightSquared), 2)

if bmi >= 35:
    print(f"Yor bmi is {bmi}, you are clinically obese.")
elif 35 > bmi >= 30:
    print(f"Yor bmi is {bmi}, you are obese.")
elif 30 > bmi >= 25:
    print(f"Yor bmi is {bmi}, you are slightly overweight.")
elif 25 > bmi >= 18.5:
    print(f"Yor bmi is {bmi}, you have a normal weight.")
elif weight < 18.5:
    print(f"Yor bmi is {bmi}, you are underweight.")