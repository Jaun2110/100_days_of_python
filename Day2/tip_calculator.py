print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? R'))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12 or 15?'))
total_bill = bill + (bill * tip_percentage / 100)
number_of_people = int(input('How many people should split the bill?'))
bill_per_person = (round(total_bill / number_of_people, 2))

print(f'Each person should pay: R {bill_per_person}')
