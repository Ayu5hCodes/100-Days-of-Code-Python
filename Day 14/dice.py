import random

def roll_dice():
    return random.randint(1, 6)

def main():
    roll_again = 'y'
    total_rolls = 0

    while roll_again.lower() == 'y':
        die1 = roll_dice()
        die2 = roll_dice()
        total_rolls += 1
        print(f"Roll {total_rolls}: Die 1: {die1}, Die 2: {die2}, Total: {die1 + die2}")
        roll_again = input("Do you want to roll the dice again? (y/n): ")

    print(f"Total rolls: {total_rolls}. Thanks for playing!")

if __name__ == "__main__":
    main()
