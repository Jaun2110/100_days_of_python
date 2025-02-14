print('Welcome to Python Pizza!')
size = input('What size pizza do you want? S, M or L: ').upper()
pepperoni = input('Do you want pepperoni on your pizza? Y or N').upper()
extra_cheese = input('Do you want extra cheese? Y or N: ').upper()

bill = 0
if size == 'L':
    bill = 20
    if pepperoni == 'Y':
        bill += 5
    if extra_cheese == 'Y':
        bill += 2
elif size == 'M':
    bill = 15
    if pepperoni == 'Y':
        bill += 5
    if extra_cheese == 'Y':
        bill += 2
else:
    bill = 10
    if pepperoni == 'Y':
        bill += 5
    if extra_cheese == 'Y':
        bill += 2

print(f'Your total bill is R {bill}')
