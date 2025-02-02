print(r'''
*******************************************************************************

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

*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
decision = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
if decision == "left":
    decision = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if decision == "wait":
        decision = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if decision == "yellow":
            print("You found the treasure! You Win!")
        elif decision == "red":
            print("It's a room full of fire. Game Over.")
        elif decision == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else :
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")    
