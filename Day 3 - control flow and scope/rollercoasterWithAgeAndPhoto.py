# check height
# check age:
# <12 = $5, 12>18 = 7, >18 = $12
#ask if they want photo and add 3$ to bill if yes


print(" Welcome to the RollerCoaster!")

bill = 0

tallness = int(input("enter your height in cm:\n"))
if tallness >= 150:
    age = int(input("how old are you?\n"))

    if age > 18:
        bill += 12
        photo = input("do you want a photo?")
        if photo == "yes":
            bill += 3
            print(f"Total payable ${bill}")
        else:
            print(f"Total payable ${bill}")
    elif age > 12 < 18:
        bill += 7
        photo = input("do you want a photo?")
        if photo == "yes":
            bill += 3
            print(f"Total payable ${bill}")
        else:
            print(f"Total payable ${bill}")

    else:
        bill += 5
        photo = input("do you want a photo?")
        if photo == "yes":
            bill += 3
            print(f"Total payable ${bill}")
        else:
            print(f"Total payable ${bill}")

else:
    print("See you when you are taller!")
