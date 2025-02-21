

from art import logo, vs
from game_data import data
import random
print(logo)
# function to compare followers
list1 = [1, 2]
# print(list1[1])


def compare_followers(data1, data2):
    if data1["follower_count"] > data2["follower_count"]:
        return [data1, 'a']
    else:
        return [data2, 'b']


# function to show choices
def show_choices(choice_1, choice_2):
    print(f"Compare A: {choice_1["name"]}, a {choice_1['description']} from {choice_1['country']}.")
    print(vs)
    print(f"Against B: {choice_2["name"]}, a {choice_2['description']} from {choice_2['country']}.")


# pick random entries from the list and assign them to variables

entry_a = random.choice(data)
entry_b = random.choice(data)
# keep track of player score
player_score = 0
end_of_game = False

while not end_of_game:
    show_choices(entry_a, entry_b)
    user_choice = input("Who has more followers? Type 'A' or 'B':").lower()
    answer = compare_followers(entry_a, entry_b)
    if user_choice == answer[1]:
        player_score += 1
        print(f'You are right! Current score: {player_score}')
        # set entry_a to answer and generate a random pick for entry_b
        entry_a = answer[0]
        entry_b = random.choice(data)
    else:
        print("\n" * 50)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {player_score}")
        end_of_game = True









