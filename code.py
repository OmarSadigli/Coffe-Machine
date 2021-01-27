MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

should_machine_work = True
should_serve = True

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0

while should_machine_work:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'report':
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

    if user_choice == 'espresso':
        required_water = MENU[user_choice]['ingredients']['water']
        required_coffee = MENU[user_choice]['ingredients']['coffee']
        if water > required_water and coffee > required_coffee:
            water -= required_water
            coffee -= required_coffee
            money += MENU[user_choice]['cost']
            should_serve = True
            should_machine_work = True
        else:
            print("Sorry there is not enough water")
            should_serve = False
            user_choice = input("What would you like? (espresso/latte/cappuccino): ")
            should_machine_work = True

    elif user_choice == 'latte' or user_choice == 'cappuccino':
        required_water = MENU[user_choice]['ingredients']['water']
        required_milk = MENU[user_choice]['ingredients']['milk']
        required_coffee = MENU[user_choice]['ingredients']['coffee']
        if water > required_water and milk > required_milk and coffee > required_coffee:
            water -= required_water
            milk -= required_milk
            coffee -= required_coffee
            money += MENU[user_choice]['cost']
            should_serve = True
            should_machine_work = True
        else:
            print("Sorry there is not enough water.")
            should_serve = False
            user_choice = input("What would you like? (espresso/latte/cappuccino): ")
            should_machine_work = True

    if user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        print("Please insert coins.")
        quarter_count = int(input("how many quarters?: "))
        dime_count = int(input("how many dimes?: "))
        nickel_count = int(input("how many nickles?: "))
        penny_count = int(input("how many pennies?: "))

        sum_of_inserted_coins = quarter_count * 0.25 + dime_count * 0.10 + nickel_count * 0.05 + penny_count * 0.01
        drink_cost = MENU[user_choice]["cost"]

        if drink_cost > sum_of_inserted_coins:
            print("Sorry that's not enough money. Money refunded.")
        else:
            change = round(sum_of_inserted_coins - drink_cost, 2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {user_choice} ☕ Enjoy!")
    if user_choice == 'off':
        should_machine_work = False
