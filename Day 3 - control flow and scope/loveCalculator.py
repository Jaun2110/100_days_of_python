name1 = input(" enter the first name")
name2 = input("What is their name?")

namesCombined = (name1 + name2).lower()
t = namesCombined.count("t")
r = namesCombined.count("r")
u = namesCombined.count("u")
e = namesCombined.count("e")
# first digit
firstDigit = t + r + u + e

l = namesCombined.count("l")
o = namesCombined.count("o")
v = namesCombined.count("v")
e = namesCombined.count("e")

secondDigit = l + o + v + e


firstDigitString = str(firstDigit)
secondDigitString = str(secondDigit)
completeScore = int(firstDigitString + secondDigitString)

if completeScore < 10 or completeScore > 90:
    print(f"Your score is {firstDigitString}{secondDigitString}, you go together like coke and mentos.")
elif 40 <= completeScore <= 50:
    print(f"Your score is {firstDigitString}{secondDigitString}, you are alright together.")
else:

    print(f"your score  is {firstDigitString}{secondDigitString}")

