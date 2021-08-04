import random


def print_output(computer_choice, player_choice):
    print("computer:", computer_choice)
    print("player:", player_choice)


while True:
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?:").lower()
    if player == computer:
        print_output(computer, player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print_output(computer, player)
            print("You lose!")
        if computer == "scissors":
            print_output(computer, player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print_output(computer, player)
            print("You lose!")
        if computer == "rock":
            print_output(computer, player)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print_output(computer, player)
            print("You lose!")
        if computer == "paper":
            print_output(computer, player)
            print("You win!")
    play_again = input("Play again? (yes/no):").lower()
    if play_again[0] != "y":
        break

print("Bye!")
