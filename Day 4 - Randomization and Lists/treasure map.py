line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

# list containing all 3 lines
treasure_map = [line1, line2, line3]


letters = ["A", "B", "C"]
numbers = ["1", "2", "3"]

user_choice = input("Where do you want to put the treasure?\n").upper()
letter_chosen = user_choice[0:1]
position_chosen = user_choice[1:2]

letter_index = letters.index(letter_chosen)
# print(letter_index)

position_index = numbers.index(position_chosen)
# print(position_index)

treasure_map[position_index][letter_index] = 'X'
print(f"{line1}\n{line2}\n{line3}")
