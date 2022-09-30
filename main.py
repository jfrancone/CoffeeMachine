from resource_monitor import print_report, deduct_water, deduct_coffee, deduct_milk
from menu import resources, MENU
from drink_order import order_drink, check_resources
from coins import receive_coins, sufficient_money, give_change


def key_for_value(d, value):
    """Return a key in `d` having a value of `value`."""
    for k, v in d.items():
        if v == value:
            return k

machine_on = True
while machine_on:
    order = order_drink(MENU, resources)
    if order == 'report':
        print_report(resources)
    elif order == 'off':
        break
    else:
        sufficient_resources = check_resources(order, resources)
        if sufficient_resources:
            order_string = key_for_value(MENU, order)
            #print(f"Your order is a {order_string}")
            coin_amnt = receive_coins(resources)
            drink_price = order['cost']
            enough_money = sufficient_money(coin_amnt, drink_price)
            if enough_money:
                #print(f"The total money given was {coin_amnt}")
                print(f"Here is your {order_string}! Enjoy! :) ☕ ")
                give_change(coin_amnt, drink_price)
                resources['money'] += drink_price
                #print(f"Money in machine: ${resources['money']}")
                resources['water'] = deduct_water(order, resources)
                resources['coffee'] = deduct_coffee(order, resources)
                resources['milk'] = deduct_milk(order, resources)
    

        else:
            print("Would you like to choose a different beverage?")



