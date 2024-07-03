import random

print("Welcome to the PyPassword Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


amt_of_letters = int(input("How many letters would you like in your password?\n"))
amt_of_symbols = int(input("Howmany symbols would you like?\n"))
amt_of_numbers = int(input("How many numbers would you like?\n"))



letter_string = ""
# get a random letter from letters_list
for n in range(1, amt_of_letters + 1):
    random_letter = letters[random.randint(0, len(letters))]
    letter_string += random_letter

# get a random number from numbers list
number_string = ""
for n in range(1, amt_of_numbers + 1):
    random_number = numbers[random.randint(0, len(numbers))]
    number_string += random_number

symbol_string = ""
for n in range(1, amt_of_symbols + 1):
    random_symbol = symbols[random.randint(0, len(symbols))]
    symbol_string += random_symbol

password_unscrambled = letter_string + symbol_string + number_string

print(f"your password is: {password_unscrambled}")







