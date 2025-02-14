print(r'''
               _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'

       
''')
print('Welcome to Treasure Island.\nYour mission is to find the treasure.')
left_or_right = input("You are at a crossroad. Type 'left' or 'right':" ).upper()

if left_or_right == 'LEFT':
    swim_or_wait = input("You get to a lake, do you swim accross or wait for a boat? Type 'swim' or 'wait':").upper()
    if swim_or_wait == 'WAIT':
        print()
        door_color_chosen= input("You arrive at 3 doors: red, blue and yellow. To go through a door, type 'blue' , 'red' or 'yellow':").upper()
        if door_color_chosen == 'RED':
            print('A ball of fire kills you! GAME OVER')
        elif door_color_chosen == 'BLUE':
            print('Beasts eat you! GAME OVER')
        elif door_color_chosen == 'YELLOW':
            print('YOU WIN')
        else:
            print('GAME OVER!')
    else:
        print('You get attacked by a trout! GAME OVER')


else:
    print("You fall into a hole! GAME OVER")
