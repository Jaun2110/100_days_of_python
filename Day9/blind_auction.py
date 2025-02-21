


bids = {}
no_other_players = False

logo = '''
▀█▀ █░█ █▀▀   █▀█ █▀█ █ █░█ ▄▀█ ▀█▀ █▀▀   █▄▄ █ █▀▄ █▀▄ █ █▄░█ █▀▀   ▄▀█ █░█ █▀▀ ▀█▀ █ █▀█ █▄░█
░█░ █▀█ ██▄   █▀▀ █▀▄ █ ▀▄▀ █▀█ ░█░ ██▄   █▄█ █ █▄▀ █▄▀ █ █░▀█ █▄█   █▀█ █▄█ █▄▄ ░█░ █ █▄█ █░▀█
'''
highest_bid = 0

#function to add bidder to dictionary


def add_bidder(name_, bid_):
    bids[name_] = bid_


while not no_other_players:
    print(logo)

    name = input("enter your name:")
    bid = int(input(f'Enter your bid: R'))
# add to dictionary:
    add_bidder(name, bid)
    if bid > highest_bid:
        highest_bid = bid
    other_players = input('Are there more bidders? Type Yes or No:').lower()
    if other_players == 'no':
        no_other_players = True
        for key in bids:
            if bids[key] == highest_bid:
                print(f"The highest bidder was {key} with R{highest_bid}")

    else:
        print("\n" * 25)
