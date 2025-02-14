import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int((input("How many letters would you like in your password?\n")))
# nr_symbols = int((input(f"How many symbols would you like?\n")))
# nr_numbers = int((input(f"How many numbers would you like?\n")))

# #entry level:
# pw_letters = ''
# pw_numbers = ''
# pw_symbols = ''
#
# for letter in range(1, nr_letters):
#     random_letter = random.choice(letters)
#     pw_letters += random_letter
#
# for number in range(1, nr_numbers):
#     random_number = random.choice(numbers)
#     pw_numbers += random_number
# for letter in range(1, nr_symbols):
#     random_symbol = random.choice(symbols)
#     pw_symbols += random_symbol
#
# password = pw_letters + pw_numbers + pw_symbols
# print(password)
#
#

#advanced
print("Welcome to the PyPassword Generator!")
nr_letters = int((input("How many letters would you like in your password?\n")))
nr_symbols = int((input(f"How many symbols would you like?\n")))
nr_numbers = int((input(f"How many numbers would you like?\n")))

password = []
#generate a random index in teh range of letters and use it to add random letter to the password

for i in range(0, int(nr_letters)):
    random_letter_index = random.randint(0, len(letters)-1)
    password.append(letters[random_letter_index])

for i in range(0, int(nr_symbols)):
    random_symbol_index = random.randint(0, len(symbols)-1)
    password.append(symbols[random_symbol_index])

for i in range(0, int(nr_numbers)):
    random_number_index = random.randint(0, len(numbers)-1)
    password.append(symbols[random_number_index])

print(password)

#shuffle the password
random.shuffle(password)

#convert the shuffled pw to str
pw_string = ''.join(password)

print(f"Your unhackable password: {pw_string}")

