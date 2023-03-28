
import time
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