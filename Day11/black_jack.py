
import random

done_playing = False
def deal(cards_in_deck):
    card = random.choice(cards_in_deck)
    return card


def check_scores(player_score, cpu_score):
    """Tels the user if they win or not"""
    if player_score > 21:
        return "You Bust\nGame Over"
    elif cpu_score > 21:
        return "You Win"
    elif cpu_score == player_score:
        return " DRAW!"
    elif cpu_score > player_score:
        return "You Lose"
    else:
        return "You Win"


def no_more_cards(player_delt, cpu_delt):
    """Deals dealer final cards"""
    cpu_delt.append(deal(cards))

    cpu_sum = sum(cpu_delt)
    while cpu_sum < 17:
        cpu_sum += deal(cards)

    player_sum = sum(player_delt)
    result = check_scores(player_score=player_sum, cpu_score=cpu_sum)

    print(f"Your cards: {player_delt}, you have {player_sum}")
    print(f"The computer cards: {cpu_delt}, it has {cpu_sum}")
    print(result)


def keep_playing(player_current_cards):
    """Deals another card and adds it ti the list"""
    player_next_card = deal(cards)
    player_current_cards.append(player_next_card)
    return player_current_cards


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
cpu_cards = []

player_first_card = deal(cards)
player_cards.append(player_first_card)

player_second_card = deal(cards)
player_cards.append(player_second_card)
cpu_first_card = deal(cards)
cpu_cards.append(cpu_first_card)


print(f"The dealer's current card is: {cpu_cards} ")
print(f"Your cards: {player_cards}")
while not done_playing:
    want_card = input("Do you want another card? Type 'y' or 'n':").lower()


    if want_card == 'n':
        #call function to deal cpu card and compares scores
        no_more_cards(player_cards, cpu_cards)
        done_playing = True
    else:
        # deal player another card and check scores
        player_cards = keep_playing(player_cards)

        if sum(player_cards) > 21:
            print("You Bust\nGame Over")
            done_playing = True
        else:
            print(f"your cards: {player_cards} ")












