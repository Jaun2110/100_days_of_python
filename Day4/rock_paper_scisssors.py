import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('Welcome to Rock, Paper, Scissors')
user_choice = (input('Enter 0 for Rock, 1 for Paper and 2 for Scessors:'))
computer_choice = random.randint(0, 2)

#0 beats 2 , 2 beats 1 and 1 beats 0
if not user_choice.isdigit():

    print('You typed an invalid character!')
elif user_choice in ('0', '1', '2'):
    user_choice = int(user_choice)

    if user_choice == 0:
        print(f'You chose Rock {rock}')
    elif user_choice == 1:
        print(f'You chose Paper {paper}')
    elif user_choice == 2:
        print(f'You chose Scissors {scissors}')

    if computer_choice == 0:
        print(f'Computer chose Rock {rock}')
    elif computer_choice == 1:
        print(f'Computer chose Paper {paper}')
    elif computer_choice == 2:
        print(f'Computer chose Scissors {scissors}')

    if computer_choice == user_choice:
        print('It is a draw!')
    elif computer_choice == 0 and user_choice == 2:
        print('Rock beats Scissors, YOU LOSE')
    elif computer_choice == 1 and user_choice == 2:
        print('Scissors cut Paper! YOU WIN')
    elif computer_choice == 2 and user_choice == 1:
        print('Scissors cut Paper! YOU LOSE')
    elif computer_choice == 0 and user_choice == 1:
        print("Paper cover's Rock! YOU WIN")
    elif computer_choice == 1 and user_choice == 0:
        print("Paper cover's Rock! YOU Lose")
    elif computer_choice == 2 and user_choice == 0:
        print('Rock beats Scissors, YOU WIN')

else:
    print("You must type 0, 1 or 2. TRY AGAIN! ")
