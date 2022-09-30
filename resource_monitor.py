def print_report(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: ${money}")


def deduct_resources(order, resources):
    deduct_water(order, resources)
    deduct_coffee(order, resources)
    deduct_milk(order, resources)


def deduct_water(order, resources):
    ingredients = order["ingredients"]
    order_water = ingredients["water"]
    water_in_tank = resources["water"]
    water_in_tank -= order_water
    # print(f"The updated water in the tank is {water_in_tank}")
    return water_in_tank


def deduct_coffee(order, resources):
    ingredients = order["ingredients"]
    order_coffee = ingredients["coffee"]
    coffee_in_tank = resources["coffee"]
    coffee_in_tank -= order_coffee
    # print(f"The updated coffee in the tank is {coffee_in_tank}")
    return coffee_in_tank


def deduct_milk(order, resources):
    ingredients = order["ingredients"]
    if "milk" in ingredients:
        order_milk = ingredients["milk"]
        milk_in_tank = resources["milk"]
        milk_in_tank -= order_milk
        # print(f"The updated milk in the tank is: {milk_in_tank}")
    else:
        milk_in_tank = resources["milk"]
    return milk_in_tank
