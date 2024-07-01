print(r'''

               .=.,
              ;c =\
            __|  _/
          .'-'-._/-'-._
         /..   ____    \
        /' _  [<_->] )  \
       (  / \--\_>/-/'._ )
        \-;_/\__;__/ _/ _/
         '._}|==o==\{_\/
          /  /-._.--\  \_
         // /   /|   \ \ \
        / | |   | \;  |  \ \
       / /  | :/   \: \   \_\
      /  |  /.'|   /: |    \ \
      |  |  |--| . |--|     \_\
      / _/   \ | : | /___--._) \
     |_(---'-| >-'-| |       '-'
  snd       /_/     \_\
  ''')
print("Welcome to treasure island\n"
      "Your mission is to find the treasure")

choice1 = input("You come to a fork in the road, do you go left or right? Type 'left' or 'right\n").lower()
if choice1 == 'right':
    print("you are crushed by an elefant. Game Over")
else:
    choice2 = input("you come to a lake, Do you want to wait for a boat or swim across? Type 'boat' or 'swim'\n").lower()
    if choice2 == "swim":
        print("Piranha's devour you! Game over!")
    else:
        choice3 = input("Now, there are 3 doors, RED, BLUE and YELLOW. Type 'red', 'yellow' or 'blue'\n").lower()
        if choice3 == "red":
            print("you get blasted by dragon breath! Game Over!")
        elif choice3 == "blue":
            print("You are dropped in the ocean and swallowed by a whale! Game Over!")
        else:
            print("You win!!")

