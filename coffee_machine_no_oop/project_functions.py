# coffee maker
import os


def coffee_type():
    coffee_type = input(
        "Enter what do you want, '(expresso/lette/cappucino)' or other function '(report)':")
    return coffee_type


def clear():
    os.system("cls")


def resources(water=1000, milk=1000, coffee=300, money=0):
    water1 = water
    milk1 = milk
    coffee1 = coffee
    money1 = money
    return [water1, milk1, coffee1, money1]


def sufficent_resources(resources2, coffee_type):
    water_required, milk_required, coffee_required, money_needed = 0, 0, 0, 0
    resources_available, water_available, milk_available, coffee_available = True, True, True, True
    if coffee_type == "expresso":
        water_required = 200
        milk_required = 150
        coffee_required = 30
        money_needed = 1

    elif coffee_type == "lette":
        water_required = 200
        milk_required = 200
        coffee_required = 25
        money_needed = 2.5

    elif coffee_type == "cappucino":
        water_required = 250
        milk_required = 100
        coffee_required = 45
        money_needed = 3

    resource_required = [water_required,
                         milk_required, coffee_required, money_needed]
    if resources2[0] >= water_required and resources2[1] >= milk_required and resources2[2] >= coffee_required:
        resources_available = True
    else:
        resources_available = False
        if resources2[0] < water_required:
            water_available = False
        elif resources2[1] < milk_required:
            milk_available = False
        elif resources2[2] < coffee_required:
            coffee_available = False

    resources_available_list = [resources_available,
                                water_available, milk_available, coffee_available]
    output = [resource_required, resources_available_list]
    return output


def process_coins(money):
    dollar = int(input("Enter the dollars '($1)':"))
    quarter = int(input("Enter the dollars '($0.25)':"))*0.25
    nickel = int(input("Enter the nickel'($0.05)':"))*0.05
    dims = int(input("Enter the dims '($0.1)':"))*0.1
    penny = int(input("Enter the penny '($0.01)':"))*0.01
    total_money = dollar + quarter+nickel+dims+penny
    money += total_money
    return [money, total_money]


def transaction_sucess(money_entered, money_needed):
    transaction_sucess1 = True
    extra = 0
    if money_entered >= money_needed:
        transaction_sucess1 = True
        extra = money_entered - money_needed
    else:
        transaction_sucess1 = False
        extra = money_entered

    return [extra, transaction_sucess1]


def make_coffee(resources1, coffee_type1, water_needed, milk_needed, coffee_needed, money, lette, exppresso, cappucino):
    print("Water:", resources1[0])
    print("Milk:", resources1[1])
    print("Coffee:", resources1[2])
    print("Money:", resources1[3])
    print(f"Here is your {coffee_type1}.Pls Enjoy it.")
    if coffee_type1 in ["exppresso", "lette", "cappucino"]:
        if coffee_type1 == "lette":
            print(lette)
        elif coffee_type1 == "exppresso":
            print(exppresso)
        elif coffee_type1 == "cappucino":
            print(cappucino)
    resources1[0] -= water_needed
    resources1[1] -= milk_needed
    resources1[2] -= coffee_needed
    resources1[3] = money

    print("Water:", resources1[0])
    print("Milk:", resources1[1])
    print("Coffee:", resources1[2])
    print("Money:", resources1[3])
