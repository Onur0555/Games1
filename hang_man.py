import random


def hang_man():
    words = ["Strawberry", "Apple", "Pear", "Cherry", "Orange", "Kumquat", "Kiwi", "Apricot"]

    computer = random.choice(words).lower()

    print(" WELCOME ".center(40, "*"))
    print(" HANG MAN ".center(40, "*"))
    print("You can attempt 6 times".center(20, "*"))
    print("If you wanna quit , you can write 'exit', 'e', 'E', 'EXIT', 'Exit'")

    guessed_letters = []
    k = 6

    while True:
        display_word = ""

        for i in computer:

            if i in guessed_letters:
                display_word += i

            else:
                display_word += "_"

        print(f"Display Word={display_word}")
        print(f"You have {k} times attempts")

        player = input("Enter the letter: ").lower()

        if player in computer:
            guessed_letters.append(player)

        elif player in guessed_letters:
            print("You said !!!")

        else:
            k -= 1

        if k == 0:
            print("Sorry there is no attempts")
            print(f"Word={computer}")
            player = input("Do you wanna continue ? ")
            return hang_man()

        if player in ["exit", "e", "E", "EXIT", "Exit"]:
            break

        if all(i in player for i in computer):
            print("Congratulations!!")
            player = input("Do you wanna continue ? ")
            return hang_man()


hang_man()
