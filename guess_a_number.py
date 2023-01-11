import os
import random
print("Welcome to the number Guessing Game")
print("I'm thinking of a number between 1 and 100.")


def difficulty1():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty in ["easy", "hard"]:
        return difficulty
    else:
        print("enter valid input")
        difficulty = difficulty1()
        return difficulty


def clear():
    os.system("cls")


diff = difficulty1()


if diff == "hard":
    lives = 5
else:
    lives = 10
a = random.randint(1, 101)
b = int(input("Guess a number:"))


def guess_a_number():
    global lives, a, b

    while lives > 0:

        if a == b:

            print("You win")
            direction = input("Would you like to play again,Type 'y' or 'n':")
            if direction == "y":
                clear()
                a = random.randint(0, 101)

                diff = difficulty1()

                print(diff)

                if diff == "hard":
                    lives = 5
                else:
                    lives = 10
                b = int(input("Guess a number:"))
                guess_a_number()

        elif a > b:

            print("Too low")
            lives -= 1

            if lives != 0:

                print(f"You have {lives} attempts left,Guess a number again")
                b = int(input("Guess a number again:"))
            if lives == 0:
                print(f"You have {lives} attempts left,You lost")
                print(f"The number was {a}")

        else:

            print("Too high")
            lives -= 1
            if lives != 0:

                b = int(input("Guess a number again:"))
                print(f"You have {lives} attempts left,Guess a number again")
            if lives == 0:
                print(f"You have {lives} attempts left,You lost")
                print(f"The number was {a}")

    else:
        direction = input("Would you like to play again,Type 'y' or 'n':")
        if direction == "y":
            clear()
            a = random.randint(0, 101)

            diff = difficulty1()

            if diff == "hard":
                lives = 5
            else:
                lives = 10
            b = int(input("Guess a number:"))
            guess_a_number()
        else:
            clear()
            print("Thank you for playing the game.")


guess_a_number()
