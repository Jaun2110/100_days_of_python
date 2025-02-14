print('Ticket asystem starting....')
ticket_price = 0
ticket_price_child = 5
ticket_price_teen = 10
ticket_price_adult = 15

rider_height = int(input('Enter your height in cm:'))

if rider_height >= 120:
    print('Great, you are tall enough...')
    age = int(input('How old are you?'))
    if age > 18:
        ticket_price = ticket_price_adult
    elif 18 >= age >= 12:
        ticket_price = ticket_price_teen
    else:
        ticket_price = ticket_price_child

    wants_photo = input('Do you want a photo? Type y for Yes an n for No:')
    if wants_photo == 'y':
        ticket_price += 3
        print(f'You have to pay {ticket_price}')
    else:
        print(f"You have to pay {ticket_price}")
else:
    print('You have to grow taller sorry!')
