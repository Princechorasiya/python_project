alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet2 = alphabet.upper()
alpha = alphabet.split()
alphabets = []
for i in range(0, 26):
    alphabets += alpha[0][i]
print(alphabets)


alpha2 = alphabet2.split()
alphabets2 = []
for i in range(0, 26):
    alphabets2 += alpha2[0][i]

# encrypt the function second part.
number = "0123456789"
numbers = []
for i in range(0, 10):
    numbers += number[i]
print(numbers)


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba,  ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    ""  ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,   ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I  88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"'  `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)


direction = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")


def encrypt():
    text = input("type your message:\n")
    shift = int(input("Type the shift number:\n"))
    encoded = ""
    for letter in text:
        for i in range(0, 26):
            if letter == alphabets[i]:
                value = i+shift
                if value < 26:
                    encoded += alphabets[value]
                else:
                    encoded += alphabets[value % 26]
        if letter == " ":
            encoded += " "
        for i in range(0, 26):
            if letter == alphabets2[i]:
                value = i+shift
                if value < 26:
                    encoded += alphabets2[value]
                else:
                    encoded += alphabets2[value % 26]

        for i in range(0, 10):
            if letter == numbers[i]:
                value = i + shift
                if value < 10:
                    encoded += numbers[value]
                else:
                    encoded += numbers[value % 10]
    print(encoded)


def decrypt():
    text = input("type your message:\n")
    shift = int(input("Type the shift number:\n"))
    decoded = ""
    for letter in text:
        for i in range(0, 26):
            if letter == alphabets[i]:
                value = i-shift
                if value >= 0:
                    decoded += alphabets[value]
                else:
                    decoded += alphabets[-((shift - i) % 26)]

        if letter in alphabets2:

            for i in range(0, 26):
                if letter == alphabets2[i]:
                    value = i-shift
                    if value >= 0:
                        decoded += alphabets2[value]
                    else:
                        decoded += alphabets2[-((shift - i) % 26)]

        if letter == " ":
            decoded += " "
        if letter in numbers:
            for i in range(0, 10):
                if letter == numbers[i]:
                    value = i - shift
                    if value >= 0:
                        decoded += numbers[value]
                    else:
                        decoded += numbers[-((shift - i) % 10)]

    print(decoded)


while direction != "end":
    if direction == "encode":
        encrypt()
    elif direction == "decode":
        decrypt()
    elif direction == 'end':
        pass
    else:
        print("enter a valid input")

    direction = input(
        "Type 'encode' to encrypt,type 'decode' to decrypt,type 'end' to exit: \n")


# def number_to_roman(n):
#     c = n % 10
#     list1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
#     d = list1[c]
#     e = (n % 100)//10
#     if 0 < e < 5:
#         list2 = ["X", "XX", "XXX","XL"]
#         f = list2[e-1]
#     elif e == 0:
#         f = ""
#     elif e < 10:
#         list2 = ["L", "LX", "LXX", "LXXX", "XC"]
#         f = list2[e-5]
#     g = (n % 1000)//100
#     if 0 < g < 5:
#         list3 = ["C", "CC", "CCC", "CD"]
#         h = list3[g-1]
#     elif g == 0:
#         h = ""
#     elif g < 10:
#         list3 = ["D", "DC", "DCC", "DCCC", "CM"]
#         h = list3[g-5]
#     i = (n % 10000)//1000
#     if 0 < i < 4:
#         list4 = ["M", "MM", "MMM"]
#         j = list4[i-1]

#     if n < 10:
#         return d
#     elif n < 100:
#         return f+d
#     elif n < 1000:
#         return h+f+d
#     elif n < 4000:
#         return j+h+f+d
#     else:
#         return "invalid"


# n = int(input("enter the value: "))
# while n != 0:
#     print(number_to_roman(n))
#     n = int(input("enter the value or 0 to end: "))
