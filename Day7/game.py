import words
import hangman_art
import random

#display hangman logo
print(hangman_art.logo)

stage_index = 6
print(hangman_art.stages[stage_index])

#choose a random word from the list
current_word = random.choice(words.word_list)
has_won = False
# print(current_word)

player_lives = len(hangman_art.stages) - 1
open_spaces_in_word = len(current_word)
# print(len(hangman_art.stages))

#generate spaces to represent the word
spaces = ''
for letter in current_word:
    spaces += '_'
while not has_won and player_lives > 0:

    # print(spaces)
    guess = input("Guess a letter:").lower()

    # replace the space with the representing letter

    if guess in current_word:
        for i, letter in enumerate(current_word):
            if letter == guess:
                letter_index = current_word.index(letter)
                spaces_list = list(spaces)
                spaces_list[i] = guess
                spaces = "".join(spaces_list)
                open_spaces_in_word -= 1

                if open_spaces_in_word == 0:
                    has_won = True
                    print('You win!')


    else:
        player_lives -= 1
        stage_index -= 1
        print(hangman_art.stages[stage_index])
        if player_lives == 0:

            print("You Lose")
            break



