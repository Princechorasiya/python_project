# Blackjack Capstone project:
import os
import random
logo = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/   
'''
card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
cards = card*4

a = random.choice(cards)
b = random.choice(cards)
user_cards = [a, b]

c = random.choice(cards)
e = random.choice(cards)
computer_cards = [c, e]


def like_to_play1():
    like_to_play = input("Would you like to blackjack, 'y' or 'n':\n")
    if like_to_play in ["y", "n"]:
        return like_to_play
    else:
        print("Enter valid input")
        like_to_play1()


def like_to_play2():
    like_to_play = input("Would you like to blackjack again, 'y' or 'n':\n")
    if like_to_play in ["y", "n"]:
        return like_to_play
    else:
        print("Enter valid input")
        like_to_play2()


like_to_play = like_to_play1()
if like_to_play == "y":
    play_game = True
else:
    play_game = False


def clear():
    os.system("cls")


def direction1():
    direction = input("Type 'y' to get another card,type 'n' to pass: ")
    if direction in ["y", "n"]:
        return direction
    else:
        print("enter a valid input")
        direction1()


def winner_calculator(a, b):
    if a > 21 and b > 21:
        return "The game is draw"
    elif a > 21 and b < 21:
        return "Computer wins"
    elif a < 21 and b > 21:
        return "You win"
    else:
        if a > b:
            return "You win"
        elif a == b:
            return "This game is draw"
        else:
            return "Computer wins"


def blackjack():
    global play_game

    while play_game:
        clear()
        print(logo)
        card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

        cards = card*4

        a = random.choice(cards)
        b = random.choice(cards)
        user_cards = [a, b]

        c = random.choice(cards)
        e = random.choice(cards)
        computer_cards = [c, e]

        print("Your cards:", [a, b])
        print("Computer first card:", c)
        direction = direction1()
        if direction == "y":
            d = random.choice(cards)
            user_cards.append(d)
            g = sum(user_cards)
            h = sum(computer_cards)
            print("Your final cards:", user_cards, "final hand", g)
            print("Computer final cards:", computer_cards, "final hand", h)

            print(winner_calculator(g, h))

            break
        elif direction == "n":
            g = sum(user_cards)
            h = sum(computer_cards)
            print("Your final cards:", user_cards, "final hand", g)
            print("Computer final cards:", computer_cards, "final hand", h)

            print(winner_calculator(g, h))
            break
    direction2 = like_to_play2()
    if direction2 == "y":
        clear()

        play_game = True

        blackjack()
    else:
        clear()
        print("Thank you for using blackjack")


blackjack()
