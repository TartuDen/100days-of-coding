import time
"""Coffie Machine Program"""
#Requirements:
#1. Print report
#2. Check resources sufficient.
#3. Process coins.
#4. Check transaction successful
#5. Make coffee.



class CoffeeMaker():
    def __init__(self,start_instance):
        self.start_instance=start_instance

    def coffee_prep(self,n,t):
        """
        Prepare coffee by subtracting the resources required from the current supplies
        
        n: str - the name of the coffee (espresso, latte, cappuccino)
        t: int - the cost of the coffee in cents
        """

        print(f"preparing {n}")
        self.start_instance.water=self.start_instance.water-self.start_instance.coffee_type[n]["water"]
        self.start_instance.milk=self.start_instance.milk-self.start_instance.coffee_type[n]["milk"]
        self.start_instance.sugar=self.start_instance.sugar-self.start_instance.coffee_type[n]["sugar"]
        self.start_instance.coffie_grains=self.start_instance.coffie_grains-self.start_instance.coffee_type[n]["coffie_grains"]
        if self.start_instance.water<=0:
            print(f"please load more water")
        elif self.start_instance.milk<=0:
            print(f"please load more milk")
        elif self.start_instance.sugar<=0:
            print("please load more sugar")
        elif self.start_instance.coffie_grains<=0:
            print("please load more coffee")
        else:
            print("preparing.")
            for i in "........":
                print(i,end=' ',flush=True)
                time.sleep(1)
                
            print(f"\nplease enjoy your {n}")

class MoneyMachine():
    def __init__(self, start_instance, coffee_maker_instance):
        self.start=start_instance
        self.coffee_maker_instance=coffee_maker_instance
    def count_coins(self,c_name,c_type):
        """
        Accepts coins from user and prepares coffee if enough coins are inserted
        
        :param c_name: name of coffee (espresso, latte, cappuccino)
        :type c_name: str
        :param c_type: cost of coffee
        :type c_type: int
        :return: None
        """
        match=False
        total_added=0
        while not match:
            added=int(input("Insert coins, 1c/5c/10c/25c: "))
            total_added+=added
            if total_added < c_type:
                print(f"total added: {total_added}, please insert {c_type-total_added} cents more")
            else:
                match=True
                self.start.money+=c_type
                self.coffee_maker_instance.coffee_prep(c_name,c_type)






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
        self.coffee_maker=CoffeeMaker(self)
        self.money_maching=MoneyMachine(self,self.coffee_maker)
        

        



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
