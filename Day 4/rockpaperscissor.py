import random
rock = '''
    Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice > 2 or user_choice < 0 :
    print ("You typed an invalid number, you lose!")
else:
    print (f"You choose : {game_images[user_choice]}")
    print (f"Computer choose : {game_images[computer_choice]}")
    
    if user_choice == computer_choice:
        print ("Its a draw !")
    elif user_choice==0 and computer_choice==2:
        print ("You win !")
    elif computer_choice==0 and user_choice==2:
        print ("You lose !")
    elif computer_choice > user_choice:
        print ("You lose !")
    else :
        print ("You win !")

