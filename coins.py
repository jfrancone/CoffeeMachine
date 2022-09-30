def receive_coins(resources):
    quarter_isnum = False
    dime_isnum = False
    nickel_isnum = False
    penny_isnum = False
    while quarter_isnum == False:
        quarters = input("How many quarters?\n")
        if quarters.isnumeric():
            quarters = int(quarters)
            quarter_isnum = True
        else:
            print("Please enter an integer(1, 2, 3, 4, etc.)")
    while dime_isnum == False:
        dimes = input("How many dimes?\n")
        if dimes.isnumeric():
            dimes = int(dimes)
            dime_isnum = True
        else:
            print("Please enter an integer(1, 2, 3, 4, etc.)\n")
    while nickel_isnum == False:
        nickels = input("How many nickels?\n")
        if nickels.isnumeric():
            nickels = int(nickels)
            nickel_isnum = True
        else:
            print("Please enter an integer(1, 2, 3, 4, etc.)\n")
    while penny_isnum == False:
        pennies = input("How many pennies?\n")
        if pennies.isnumeric():
            pennies = int(pennies)
            penny_isnum = True
        elif quarters == "off":
            break
        else:
            print("Please enter an integer(1, 2, 3, 4, etc.)\n")
    quarter_amnt = quarter_calc(quarters)
    dime_amnt = dime_calc(dimes)
    nickel_amnt = nickel_calc(nickels)
    penny_amnt = penny_calc(pennies)
    total_coin_amnt = quarter_amnt + dime_amnt + nickel_amnt + penny_amnt
    return total_coin_amnt


def sufficient_money(coin_amnt, price_of_drink):
    sufficient_money = False
    if coin_amnt >= price_of_drink:
        sufficient_money = True
        return sufficient_money
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return sufficient_money


def give_change(coin_amnt, drink_price):
    change = coin_amnt - drink_price
    print(f"Your change is ${change}")
    return change


def quarter_calc(quarters):
    quarter_amnt = quarters * 0.25
    return quarter_amnt


def dime_calc(dimes):
    dime_amnt = dimes * 0.10
    return dime_amnt


def nickel_calc(nickels):
    nickel_amnt = nickels * 0.05
    return nickel_amnt


def penny_calc(pennies):
    penny_amnt = pennies * 0.01
    return penny_amnt
