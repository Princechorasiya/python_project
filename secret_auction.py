# secret auction
import os
print("Welcome to secret auction program.")
logo = '''                    ___________
                    \         /
                    )_______(
                    |"""""""|_.-._,.---------.,_.-._
                    |       | | |               | | ''-.
                    |       |_| |_             _| |_..-'
                    |_______| '-' `'---------'` '-'
                    )"""""""(
                    /_________\\
                    `'-------'`
                .-------------.
            /_______________\\'''
print(logo)
name_list = []
value_list = []

mydict = {

}
name1 = input("What is your name?:")
bid1 = int(input("What is you bid?:"))
direction = input("Are there any other bidders?Type \'yes' or 'no'.")

os.system("cls")


def add_to_dict(name, bid):
    mydict[name] = bid
    name_list.append(name)
    value_list.append(bid)
    # return mydict


add_to_dict(name1, bid1)
while direction == "yes":
    name = input("What is your name?:")
    bid = int(input("What is you bid?:"))
    add_to_dict(name, bid)

    direction = input("Are there any other bidders?Type \'yes' or 'no'.")
    os.system("cls")

else:
    for i in name_list:
        value = mydict[i]
        if value == max(value_list):
            print(f"The winner is {i} with a bid of {value}.")
        else:
            pass


# second method


def clear():
    os.system("cls")


print("Welcome to secret auction program.")
logo = '''                    ___________
                    \         /
                    )_______(
                    |"""""""|_.-._,.---------.,_.-._
                    |       | | |               | | ''-.
                    |       |_| |_             _| |_..-'
                    |_______| '-' `'---------'` '-'
                    )"""""""(
                    /_________\\
                    `'-------'`
                .-------------.
            /_______________\\'''
print(logo)
mydict = {

}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for each_bidder in bidding_record:
        # for loop in a dictioanry
        bid_amount = bidding_record[each_bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = each_bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bidding_finished = False
while not bidding_finished:
    name1 = input("What is your name?:")
    bid1 = int(input("What is you bid?:$"))
    mydict[name1] = bid1
    direction = input("Are there any other bidders?Type \'yes' or 'no'.\n")
    if direction == "no":
        bidding_finished = True
        find_highest_bidder(mydict)
    elif direction == "yes":
        clear()
