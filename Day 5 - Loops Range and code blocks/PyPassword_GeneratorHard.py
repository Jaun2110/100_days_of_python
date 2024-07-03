import random

print("Welcome to the PyPassword Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


amt_of_letters = int(input("How many letters would you like in your password?\n"))
amt_of_symbols = int(input("How many symbols would you like?\n"))
amt_of_numbers = int(input("How many numbers would you like?\n"))



password_list= []

# get a random letter number an symbol and add them in a list

for n in range(1, amt_of_letters + 1):
    random_letter = random.choice(letters)
    password_list.append(random_letter)

for n in range(1, amt_of_numbers + 1):
    random_number = random.choice(numbers)
    password_list.append(random_number)

for n in range(1, amt_of_symbols + 1):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)

print(password_list)
#shuffle the list
random.shuffle(password_list)

print(password_list)

# turn the list into a string
password_string = ""

for item in password_list:
    password_string += item

print(f"your password is:{password_string}  ")









