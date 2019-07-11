"""
program takes in an input from a player (either rock, paper, or scissors) and determins if the 
players wins against the computer
"""

from random import randint

def win():
    if computer_selection == player_selection:
        print("it was a tie")
    elif player_selection == "rock" and computer_selection == "scissors":
        print("Player wins!")
    elif player_selection == "paper" and computer_selection == "rock":
        print("Player wins!")
    elif player_selection == "scissors" and computer_selection == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")


while True:

    player_selection = input("Please select rock(r), paper(p), or scisssors(s): ")

    while player_selection != "r" and player_selection != "p" and player_selection != "s":
        player_selection = input("Please enter a valid input: ")
    
    if player_selection[0].lower() == "r":
        player_selection = "rock"
    elif player_selection[0].lower() == "p":
        player_selection = "paper"
    elif player_selection[0].lower() == "s":
        player_selection = "scissors"

    print("Player's choice is " + player_selection)
        
    computer_number = randint(1,3)
    if computer_number == 1:
        computer_selection = "rock"
    elif computer_number == 2:
        computer_selection = "paper"
    elif computer_number == 3:
        computer_selection = "scissors"

    print("Computer's choice is " + computer_selection)

    win()
    
    print("Would you like to play again? ")
    ans = input()

    if ans[0].lower() == "n":
        break

print("Thanks for playing!")


    






 

        
