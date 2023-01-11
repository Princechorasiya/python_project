# Higher or lower project
import random
import os
import pyfiglet
import main2 as m


print(m.logo())
print("Welcome to the higher or lower game!")
like_to_play = input("Would you like to play the game,Type 'y' or 'n':")
score = 0
if like_to_play == "y":
    like_to_continue = True
    while like_to_continue:
        a = random.randint(1, 14)
        b = random.randint(1, 14)
        while a == b:
            b = random.randint(1, 14)

        for key in m.dict_data[a]:
            c = key
            value1 = m.dict_data[a][key][1]
            id1 = m.dict_data[a][key][0]
            art1 = pyfiglet.figlet_format(key, font="bubble")
        for key in m.dict_data[b]:
            d = key
            value2 = m.dict_data[b][key][1]
            id2 = m.dict_data[b][key][0]
            art2 = pyfiglet.figlet_format(key, font="bubble")

        if value1 > value2:
            result = "higher"
        elif value1 < value2:
            result = "lower"

        print("Write 'higher' or 'lower' for:")
        print(
            f"(1) The followers of {c}.\nInstagram id{id1}\n{art1}\n\n\n\t\t\t vs \n\n\n(2)The followers of {d}.\nInstagram id {id2}\n{art2}")

        choice = input("Write your choice:")

        score = score

        def result1():
            global choice, result, score
            if choice == result:
                print("The choice was correct")
                score += 1

            else:
                print("The choice was wrong")
                score += 0
            return score

        result1()
        if choice == result:
            like_to_continue1 = input(
                f"You score is {score}.Would you like to continue,Type 'y' or 'n': ")
            if like_to_continue1 == "y":
                like_to_continue = True
                m.clear()
                print(m.logo())
            else:
                like_to_continue = False
                m.clear()
                print(m.logo())
                print(f"Your score is {score}")

        elif choice != result:
            print("Game over")
            like_to_continue1 = input(
                f"You score was {score}.Would you like play again,Type 'y' or 'n': ")
            if like_to_continue1 == "y":
                like_to_continue = True
                m.clear()
                print(m.logo())
            else:
                print(f"Your score is {score}")
                m.clear()

                like_to_continue = False
                print("Thank you for visiting us.")
else:
    m.clear()
    print("Thank you for visiting us.")
