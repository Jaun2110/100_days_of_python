import random
from guessing_game_art import logo
print(logo)
print("Welcome to the Number Guessing Game")

number = random.randint(1, 100)
# print(f'Number: {number}')
end_of_game = False
no_more_lives = False
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if difficulty == 'easy':
    lives = 10
else:
    lives = 5

while not end_of_game and not no_more_lives:
    print(f"You have {lives} attempts remaining to guess the number. ")
    guess = int(input("Make a guess:"))
    if guess == number:
        end_of_game = True
        print("You Win!")
    elif guess > number:
        print("Too high.")
        lives -= 1
        if lives == 0:
            no_more_lives = True
            print(f"You have {0} lives left!\nGame over.")
        else:
            print("Guess again.")
    else:
        print("Too low.")
        lives -= 1
        if lives == 0:
            no_more_lives = True
            print(f"You have {0} lives left!\nGame over.")
        else:
            print('Guess again')



