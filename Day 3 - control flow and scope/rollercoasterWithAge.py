# check height
# check age:
# <12 = $5, 12>18 = 7, >18 = $12


print(" Welcome to the RollerCoaster!")


notFinished = "True"
bill= 0
while notFinished == "True":
    tallness = int(input("enter your height in cm:\n"))
    age = int(input("how old are you?\n"))
    if tallness >= 150:
        if age > 18:
         bill += 12
         print(f"Total payable ${bill}")
         morePeople = input("are there more people in your group?")
         if morePeople == "no":
              notFinished = "False"

        elif age > 12 < 18:
         bill += 7
         print(f"Total payable ${bill}")
         morePeople = input("are there more people in your group?")
         if morePeople == "no":
              notFinished = "Fals1e"
        else:
         bill += 5
         print(f"Total payable ${bill}")
         morePeople = input("are there more people in your group?")
         if morePeople == "no":
             notFinished = "False"
    else:
        print("See you when you are taller!")



