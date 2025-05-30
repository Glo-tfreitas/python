import random as r
import sys

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choices = [rock, paper, scissors]
computer_choice = r.randint(0, 2)
user_choice = int(input("What do you choose? (0 = Rock | 1 = Paper | 2 = Scissors) "))
print("\n\nComputer chose:\n" + choices[computer_choice] + "\nUser chose: ")
if user_choice == computer_choice:
    print(choices[user_choice] + "\nIt's a draw!")
    sys.exit()

user_wins = False

match user_choice:
    case 0:
        if computer_choice == 2:
            user_wins = True
    case 1:
        if computer_choice == 0:
            user_wins = True
    case 2:
        if computer_choice == 1:
            user_wins = True
    case _:
        user_choice = "incorrect_value"
        
if(user_choice == "incorrect_value"):
    print("Incorrect value, game is over.")
else : 
    print(choices[user_choice])
    if user_wins:
        print("You win!")
    else:
        print("You lose")