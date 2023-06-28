import random


def rock_paper_scissors():
    counter_player = 0
    counter_computer = 0
    while True:
        print("*" * 50)
        print(" WELCOME ".center(50, "*"))
        print("*" * 50)
        print("You should choose:'rock','paper','scissors'")

        choose = ["rock", "paper", "scissors", "exit", "e", "E", "EXIT", "Exit"]

        player = input("Enter the choice: ").lower()

        computer = random.choice(choose)

        while player not in choose or player == computer:

            if player not in choose:
                player = input("Please enter the correct choice: ").lower()

            elif player in ["exit", "e", "E", "EXIT", "Exit"]:
                print("Good Bye")

            else:
                player = input("it is tie!,again").lower()

        if (player == "rock" and computer == "scissors") or \
                (player == "scissors" and computer == "paper") or \
                (player == "paper" and computer == "rock"):
            counter_player += 1
            print(f"Player win!! {counter_player} times earn")

        elif player in ["exit", "e", "E", "EXIT", "Exit"]:
            break

        else:
            counter_computer += 1
            print(f"Computer win!! {counter_computer} times earn")

        print(f"Player:{counter_player} vs Computer:{counter_computer}")


rock_paper_scissors()

# Ödev: 2 player olacak
