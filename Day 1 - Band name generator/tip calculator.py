print("Welcome to the tip calculator!")
billTotal = float(input("what was the total bill?"))
tipPercentage = int(input("How much tip would you like to give? 10,12, or 15?"))
tipAmount = billTotal * (tipPercentage/100)
billTotal += tipAmount
numPeople = int(input("How many people to split the bill?"))
billTotal /= numPeople

print(f"Each person should pay: ${round(billTotal, 2)}")
