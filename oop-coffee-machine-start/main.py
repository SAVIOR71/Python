from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()
is_on = True

while is_on == True:
    print("Menu : ", menu.get_items())  ## 메뉴 보여주기
    order = input("What do you want? : ") ## 뭐먹을지 묻기
    if order == "report":
        coffee_maker.report()
        money_machine.report()

    elif order == "off":
        is_on = False

    else:
        drink = menu.find_drink(order)
        possible = coffee_maker.is_resource_sufficient(drink)
        if possible == True:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
