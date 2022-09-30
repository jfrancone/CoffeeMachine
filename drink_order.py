from menu import MENU


def order_drink(MENU, resources):
    valid_request = False
    while not valid_request:
        order_string = input(
            "What would you like? (espresso/latte/cappuccino): \n"
        ).lower()
        # print(order_string)
        if (
            order_string == "report"
            or order_string == "off"
            or order_string == "latte"
            or order_string == "espresso"
            or order_string == "cappuccino"
        ):
            valid_request = True
            if order_string == "report":
                return "report"
            elif order_string == "off":
                return "off"
            else:
                order = MENU[order_string]
                print(f"Price: ${order['cost']}")
                return order
        else:
            print("That order is not valid. Please try again.")


def check_resources(order, resources):
    # print("Check resources is running")
    ingredients = order["ingredients"]
    order_water = ingredients["water"]
    order_coffee = ingredients["coffee"]
    if "milk" in ingredients:
        order_milk = ingredients["milk"]
    sufficient_resources = False
    if order_water > resources["water"]:
        print("Sorry, there is not enough water. Order Refunded.")
    elif order_coffee > resources["coffee"]:
        print("Sorry, there is not enough coffee. Order Refunded.")
    elif "milk" in ingredients and order_milk > resources["milk"]:
        print("Sorry, there is not enough milk. Order Refunded.")
    else:
        # print("There are sufficient resources for this drink")
        sufficient_resources = True
        return sufficient_resources
