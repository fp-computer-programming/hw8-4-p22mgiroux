# Author: MOG 12/10/21

from random import randint

def rock_paper_scissors():
    wins = 0
    x = 1
    while x != 0:
        """Play rock paper scissors"""
        player = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
        computer = randint(0, 2)

        # Check if the user or the computer won.
        if player == computer:
            print("It's a tie!")
        elif player == 0:
            if computer == 1:
                print("You lose, paper covers rock.\n")
            else:
                print("You win, rock crushes scissors!\n")
                wins += 1
        elif player == 1:
            if computer == 2:
                print("You lose, scissors cuts paper.\n")
            else:
                print("You win, paper covers rock!\n")
                wins += 1
        elif player == 2:
            if computer == 0:
                print("You lose, rock crushes scissors.\n")
            else:
                print("You win, scissors cuts paper!\n")
                wins += 1

        again = input("Do you want to play again ('Y' or 'N')? ")
        
        if again.lower() == "n":
            print("You won {} times!".format(wins))
            x = 0
    
rock_paper_scissors()