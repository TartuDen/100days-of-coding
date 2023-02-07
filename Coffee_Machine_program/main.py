
"""Coffie Machine Program"""


import Coffee_maker
import money_machine

#1. Print report

class Start():
    def __init__(self):
        self.water=1000
        self.milk=500
        self.sugar=200
        self.coffie_grains=500
        self.espresso=75
        self.latte=83
        self.cappuccino=105
        self.money=15
        self.coffee_maker=Coffee_maker.CoffeeMaker(self)
        self.money_maching=money_machine.MoneyMachine(self,self.coffee_maker)
        

        



        self.coffee_type={"espresso":{"milk":25,"coffie_grains":10,"water": 550, "sugar":3},
        "latte":{"milk":15,"coffie_grains":7,"water": 350, "sugar":2},
        "cappuccino":{"milk":10,"coffie_grains":5,"water": 250, "sugar":3}}



        stop=False
        while not stop:
            def get_requrst(r):
                """
                Get request from user and call the appropriate function
                
                :param r: request from user (espresso, latte, cappuccino, report)
                :type r: str
                :return: None
                """

                if r.lower()=="report":
                    print(f"water-{self.water}mL, milk-{self.milk}mL, sugar-{self.sugar}g, coffee-{self.coffie_grains}g\nThe coffee machin has {self.money} dollars")
                elif r.lower()=="espresso":
                    self.money_maching.count_coins("espresso",self.espresso)
                elif r.lower()=="latte":
                    self.money_maching.count_coins("latte",self.latte)
                elif r.lower()=="cappuccino":
                    self.money_maching.count_coins("cappuccino",self.cappuccino)
                else:
                    print("please repeat")
            print("espresso - 75c\nlatte - 83c\ncappuccino - 1.05c\ntype 'report' to check supplies")
            req=input("What would you like? ")
            get_requrst(req)
            req_stop=input("Anything else? Y/N - ")
            if req_stop.lower()=='n':
                stop=True

def main():
    new_requrst=Start()
main()
