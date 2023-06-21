import random

def guess_number():
    number = random.randint(1, 100)
    print("Let's Begin \nYou can try guess 10 times")
    i = 1
    while i < 11:

        guess = input(f"Round {i}\nEnter a number: ")
        while not guess.isnumeric():
            guess = input("Wrong!! Please enter numeric datatype!: ")

        while int(guess) not in range(0,100):
            guess = int(input("Wrong!! Please enter the number between 0 and 100: "))

        guess = int(guess)

        if number < guess - 10:
            print("Your guess the number too big")

        elif guess + 10 < number:
            print("Your guess the number too less")

        elif guess < number:
            print("Your guess the number little less")

        elif guess > number:
            print("Your guess the number little big")

        else:
            print(f"Bingo!! You win\nYou got {11-i} points \U0001F600")
            break
        i += 1
    if i == 11:
        print("Gameover!!!")
    while input("Do you wanna continue?") not in ["No", "NO", "no", "N", "n"]:
        guess_number()

guess_number()



