import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word bank of animals
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
             'coyote crow deer dog donkey duck eagle ferret fox frog goat '
             'goose hawk lion lizard llama mole monkey moose mouse mule newt '
             'otter owl panda parrot pigeon python rabbit ram rat raven '
             'rhino salmon seal shark sheep skunk sloth snake spider '
             'stork swan tiger toad trout turkey turtle weasel whale wolf '
             'wombat zebra ').split()

chosen_word = random.choice(word_list)


display = []
for letter in chosen_word:
    display += ["_"]
print(display)


lives = 6
end_of_game = False
while not end_of_game:
    print(HANGMANPICS[6-lives])
    print(display)

    guess = input("Guess a letter: ")
    guess_lower = guess.lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess_lower:
                display[i] = guess_lower
    else:
        lives -= 1

    if "_" not in display and lives != 0:
        print("You win")
    elif "_" in display and lives == 0:
        print("You lost all lives.You lose.")
        print(HANGMANPICS[6])

    if "_" not in display:
        end_of_game = True
    elif lives == 0:
        end_of_game = True


print("the word was:", chosen_word)
