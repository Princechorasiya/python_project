print('''
************************************************************************
          |                   |                  |                     |
 ___|_____.="";=._____|_______|__
|                   |  ,-"_,=""     `"=.|                  |
|______|"=._o`"-.        `"=._____|______
          |                `"=.o`"=.      `"=.                     |
 ___|_______:=.o "=..".-="'"=.______|__
|                   |    _.--" , ; `"=._o." ,-"""-. ".   |
|______|."  ,. .` ` `` ,  `"-."-._   ". '_|______
          |           |o`"=.` , "` `; .". ,  "-."-._; ;              |
 ___|____| ;`-.o`"=.; ." ` '`."\` . "-._ /_____|___
|                   | |o;    `"-.o`"=.``  '` " ,_.--o;   |
|______|| ;     (#) `-.o `"=.`.--"_o.-; ;_|______
_/__/__/_|o;.    "      `".o|o_.--"    ;o;_/__/__/_
/__/__/__/"=._o--.        ; | ;        ; ;/__/__/__/_
_/__/__/__/"=._o--.   ;o|o;     .;o;_/__/__/_
/__/__/__/__/_"=._o.; | ;.--"o.--"/__/__/__/_
_/__/__/__/__/_"=.o|o.--""_/__/__/__/__
/__/__/__/__/__/__/__/__/__/__/___ /
**************************************************************************
''')
print("Welcome to the Treasure island")
print("Your mission is to find the treasure")
choice1=input("You are at a cross road.\nWhere do you want to go?Type \"left\" or \"right\"\n")
if choice1=="left":
    choice2=input("You came at a lake.\nThere is an island in the middle of the lake.\nType \"wait\" to wait for the boat.Type\"swim\" to swim across\n ")
    if choice2=="wait":
        choice3=input("You arrive at the island safely.\nThere is a house on the island with 3 doors.\none red,one yellow and one blue.Which one do you choose?\n")
        if choice3=="blue":
            print("Congratulation, you have found the treasure")
        elif choice3=="yellow":
            print("You have arrived at the room filled with snake.You died.\"Game over\"")
        else:
            print("You arrived at a room filled with fire. You have been burned to death. \"Game over\"")
    else:
        print("You choose to swin in the lake.\nThe lake was filled with crocodiles.You have been eatan alive.\"Game over\"")

else:
    print("You walked about a mile,but didn't find anything.\n You choose to return but suddenly someone attacked you.\n You died of an heart attack due to fear \"Game over\"")
