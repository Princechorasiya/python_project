# Password Generator Project
import random
import pyfiglet as p
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

print(p.figlet_format("PyPassword", font="slant"))


def totalinput():
    nr_tot = int(input("Enter the length of the password: "))
    if nr_tot >= 12:
        return nr_tot
    else:
        print("Make sure minimum password length is 12")
        totalinput()
        return nr_tot


nr_total = totalinput()


def enterdata(nr_total):

    nr_letters = int(
        input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    if nr_total == (nr_letters + nr_symbols+nr_numbers):
        return nr_letters, nr_symbols, nr_numbers
    else:
        print("Please enter correct data")
        enterdata(nr_total)
        return nr_letters, nr_symbols, nr_numbers


datalist = enterdata(nr_total)
nr_letters = datalist[0]
nr_symbols = datalist[1]
nr_numbers = datalist[2]


# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter = ""
for n in range(1, nr_letters+1):

    letter_1 = letters[random.randint(0, 51)]
    letter += letter_1
# print(letter)
number = str()
for n in range(1, nr_numbers+1):
    number_1 = numbers[random.randint(0, 9)]
    number += str(number_1)
# print(number)
symbol = str()
for n in range(1, nr_symbols+1):
    symbol_1 = symbols[random.randint(0, 8)]
    symbol += symbol_1
# print(symbol)

print(f"Your password is {letter}{number}{symbol}")

list3 = list(letter + number + symbol)
print(list3)
# making it stronger
password = str()
for n in range(1, len(list3)+1):
    random_index = random.randrange(len(list3))
    password_1 = list3.pop(random_index)
    password += password_1

print(f"Your stronger password is {password}")
