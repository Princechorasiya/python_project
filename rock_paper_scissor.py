import random
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list1 = list+list+list+list+list
# list2 = list1+list1+list1+list1+list1

while True:
    print("Welcome to rock,paper,scissors game")
    move_player = input(
        "What do you choose?Type 0 for Rock,1 for paper or 2 for scissors.")
    move_1 = int(move_player)
    rock = '''
        ___
    ---'   __)
          (___)
          (___)
          (__)
    ---._(__)
    '''

    scissors = '''
        ___
    ---'   _________)
              ________)
              ___)
             ___)
    ---.____)
    '''

    paper = '''
        _____)
    ---'   _________)
              _______)
           _________)
          (______)
    ---.______)
    '''
    player_move = [rock, paper, scissors]
    if move_1 <= 2 and move_1 >= 0:
        player_move_1 = player_move[move_1]
        print(f"You have chosen {player_move_1}")
        if move_1 == 0 or 1 or 2:
            computer_move = [rock, paper, scissors]
            random_number = random.randint(0, 2)
            move = computer_move[random_number]
            print(f"Computer chose {move}")

            if move_1 == random_number:
                print("The game is a Draw")
            if move_1 == 0:
                if move == paper:
                    print("You lose")
                elif move == scissors:
                    print("You win")

            if move_1 == 1:
                if move == rock:
                    print("You win")
                elif move == scissors:
                    print("You lose")
            if move_1 == 2:
                if move == rock:
                    print("You lose")
                elif move == paper:
                    print("you win")

    else:
        print("you have chosen invalid number you lose.")

    # method2
    # game_images = [rock, paper, scissors]
    # user_choice = input(
    #     "What do you  want to choose?Type 0 for rock,1 for paper and 2 for scissors.\n")
    # user_choice_1 = int(user_choice)
    # if user_choice_1 <= 2 and user_choice_1 >= 0:
    #     print(f"You chose\n {game_images[user_choice_1]}")

    #     computer_choice = random.randint(0, 2)
    #     print(f"Computer choose\n {game_images[computer_choice]}")
    #     if user_choice_1 == 0 and computer_choice == 2:
    #         print("You win")
    #     elif computer_choice == 0 and user_choice_1 == 2:
    #         print("You lose")
    #     elif user_choice_1 >= 3 or computer_choice < 0:
    #         print("you typed an invalid number,you lose")
    #     elif computer_choice > user_choice_1:
    #         print("You lose")
    #     elif user_choice_1 > computer_choice:
    #         print("You win")
    #     elif computer_choice == user_choice_1:
    #         print("This is a draw")
    # else:
    #     print("you chose an invalid number.You lose")
