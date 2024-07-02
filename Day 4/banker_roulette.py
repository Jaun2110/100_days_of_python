import random

names_string = "jaun, Jano, Patricia, Johan"
# create a list from the string
names = names_string.split(", ")
# print(names)
# pick a random name:
# return number of items in a list
# print(len(names))

random_number = random.randint(0, len(names)-1)
random_name = names[random_number]

print(f"{random_name} is going to buy the meal today!")

