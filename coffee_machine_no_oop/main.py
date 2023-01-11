import project_functions as p
import pyfiglet as q
coffee_machine = q.figlet_format("C o f f e e M a c h i n e", font="slant")
lette = q.figlet_format("L e t t e", font="slant")
exppresso = q.figlet_format("E x p p r e s s o", font="slant")
cappucino = q.figlet_format("C a p p u c i n o", font="slant")
q.figlet_format("L e t t e", font="slant")

water = 1000
milk = 1000
coffee = 300
money = 0
will_continue = True
while will_continue:
    print(coffee_machine)
    print(exppresso, "\t", lette, "\t", cappucino)
    coffee_type1 = p.coffee_type()
    print(f"Order one")
    if coffee_type1 in ["expresso", "lette", "cappucino"]:
        if coffee_type1 == "lette":
            print(lette) 
        elif coffee_type1 == "expresso":
            print(exppresso)
        elif coffee_type1 == "cappucino":
            print(cappucino)

        resources1 = p.resources(water, milk, coffee, money)

        sufficent_resources_list = p.sufficent_resources(
            resources1, coffee_type1)

        water_required_1 = sufficent_resources_list[0][0]
        milk_required_1 = sufficent_resources_list[0][1]
        coffee_required_1 = sufficent_resources_list[0][2]
        money_needed = sufficent_resources_list[0][3]
        resources_available_1 = sufficent_resources_list[1][0]
        water_available_1 = sufficent_resources_list[1][1]
        milk_available_1 = sufficent_resources_list[1][2]
        coffee_available_1 = sufficent_resources_list[1][3]
        if resources_available_1:
            print("All things are available.")
            money_entered_list = (p.process_coins(money))
            money_entered = money_entered_list[1]
            money = money_entered_list[0]
            print(money_entered)
            transction_suceess_list = (p.transaction_sucess(
                money_entered, money_needed))
            transction_suceess_2 = transction_suceess_list[1]
            extra = transction_suceess_list[0]
            if transction_suceess_2:
                if money >= extra:
                    print(f"Please collect ${extra}")
                    money -= extra
                else:
                    print(f"Please collect ${extra} from the counter")

                p.make_coffee(resources1, coffee_type1, water_required_1,
                              milk_required_1, coffee_required_1, money, lette, exppresso, cappucino)
                water = resources1[0]
                milk = resources1[1]
                coffee = resources1[2]
                money = resources1[3]

                will_continue = True
            else:
                money -= extra
                print(
                    f"Oops you have entered wrong price.Here is your ${extra}")
                will_continue = True

        elif not water_available_1:
            print("Oops! We re lacking water.Pls refill it")
        elif not milk_available_1:
            print("Oops! We re lacking milk.Pls refill it")
        elif not coffee_available_1:
            print("Oops! We re lacking Coffee.Pls refill it")

    elif coffee_type1 == "report":
        print("b")
        resources1 = p.resources(water, milk, coffee, money)
        print("Water:", resources1[0])
        print("Milk:", resources1[1])
        print("Coffee:", resources1[2])
        print("Money:", resources1[3])
        will_continue = True

    elif coffee_type1 == "off":
        p.clear()
        will_continue = False
