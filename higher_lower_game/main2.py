# Higher or lower project
import random
import os
import pyfiglet


def logo():
    logo1 = pyfiglet.figlet_format("Higher or Lower", font="slant")
    return logo1


def clear():
   if os.name =="nt":
    _ = os.system("cls")


m = 10**6
names_list = ["a", "Cristiano Ronaldo", "Lionel Messi",
              "Kylie Jenner", "Selena Gomez", "Dwayne Johnson", "Ariana Grande", "Kim Kardashian", "Beyonce", "Khloé Kardashian", "Ujjwal dixit", "Prince Chorasiya", "Justin Bieber", "Kendall Jenner", "Sachin "]
followers_list = ["a", 502*m, 378*m, 372*m, 357*m,
                  349*m, 340*m, 333*m, 282*m, 280*m, 536, 535, 264*m, 263*m, 112]
instagram_ids = ["a", "@cristiano", "@leomessi", "@kyliejenner", "@selenagomez", "@therock", "@arianagrande",
                 "@kimkardashian", "@beyonce", "@khloekardesian", "ujjwal.golu224", "prince.chaurasia123",	"@ justinbieber", "@kendalljenner", "@sachin"]

dict_data = {}
for i in range(1, 15):
    dict_data[i] = {names_list[i]:
                    [instagram_ids[i], followers_list[i], ]}
