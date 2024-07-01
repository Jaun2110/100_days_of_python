print("Thankyou for choosing Python Pizza Deliveries!")
pizzaSize = input("What size pizza do you want? S, M, L\n").upper()
addPepperoni = input("Do you want pepperoni? Y or N\n").upper()
extraCheese = input("Do you want extra cheese? Y or N\n").upper()
# pizza prices
priceSmall = 15
priceMedium = 20
priceLarge = 25
# pepperoni prices:
pepperoniSmall = 2
pepperoniMedLarge = 3
# extra cheese
extraCheesePrice = 1


bill = 0

if pizzaSize == "S":
    bill = 15
    if addPepperoni == "Y":
        bill += pepperoniSmall
    if extraCheese == "Y":
        bill += 1
elif pizzaSize == "M":
    bill = 20
    if addPepperoni == "Y":
        bill += pepperoniMedLarge
    if extraCheese == "Y":
        bill += 1

else:
    bill = 25
    if addPepperoni == "Y":
        bill += pepperoniMedLarge
    if extraCheese == "Y":
        bill += 1

print(f"Your final bill is: ${bill}.")



