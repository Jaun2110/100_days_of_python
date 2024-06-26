weight = input("enter your weight\n")
height = input("enter your height\n")

weightI = int(weight)
heightI = float(height)
heightSquared = heightI * heightI
# print(type(weightI))
bmi = int(weightI/heightSquared)

print("your bmi is : " + str(bmi))
