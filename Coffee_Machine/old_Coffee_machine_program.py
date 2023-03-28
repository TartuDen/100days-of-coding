import time
"""Coffie Machine Program"""
#Requirements:
#1. Print report
#2. Check resources sufficient.
#3. Process coins.
#4. Check transaction successful
#5. Make coffee.

water=1000
milk=500
sugar=200
coffie_grains=500

espresso=75
latte=83
cappuccino=105

money=15

coffee_type={"espresso":{"milk":25,"coffie_grains":10,"water": 550, "sugar":3},
"latte":{"milk":15,"coffie_grains":7,"water": 350, "sugar":2},
"cappuccino":{"milk":10,"coffie_grains":5,"water": 250, "sugar":3}}



stop=False

def coffee_prep(n,t):
    """
    Prepare coffee by subtracting the resources required from the current supplies
    
    n: str - the name of the coffee (espresso, latte, cappuccino)
    t: int - the cost of the coffee in cents
    """
    global water
    global milk
    global sugar
    global coffie_grains

    print(f"preparing {n}")
    water=water-coffee_type[n]["water"]
    milk=milk-coffee_type[n]["milk"]
    sugar=sugar-coffee_type[n]["sugar"]
    coffie_grains=coffie_grains-coffee_type[n]["coffie_grains"]
    if water<=0:
        print(f"please load more water")
    elif milk<=0:
        print(f"please load more milk")
    elif sugar<=0:
        print("please load more sugar")
    elif coffie_grains<=0:
        print("please load more coffee")
    else:
        print("preparing.")
        for i in "........":
            print(i,end=' ',flush=True)
            time.sleep(1)
            
        print(f"\nplease enjoy your {n}")


def count_coins(c_name,c_type):
    """
    Accepts coins from user and prepares coffee if enough coins are inserted
    
    :param c_name: name of coffee (espresso, latte, cappuccino)
    :type c_name: str
    :param c_type: cost of coffee
    :type c_type: int
    :return: None
    """
    global money
    match=False
    total_added=0
    while not match:
        added=int(input("Insert coins, 1c/5c/10c/25c: "))
        total_added+=added
        if total_added < c_type:
            print(f"total added: {total_added}, please insert {c_type-total_added} cents more")
        else:
            match=True
            money+=c_type
            coffee_prep(c_name,c_type)






#1. Print report


while not stop:
    def get_requrst(r):
        """
        Get request from user and call the appropriate function
        
        :param r: request from user (espresso, latte, cappuccino, report)
        :type r: str
        :return: None
        """
        global water
        global milk
        global sugar
        global coffie_grains

        if r.lower()=="report":
            print(f"water-{water}mL, milk-{milk}mL, sugar-{sugar}g, coffee-{coffie_grains}g\nThe coffee machin has {money} dollars")
        elif r.lower()=="espresso":
            count_coins("espresso",espresso)
        elif r.lower()=="latte":
            count_coins("latte",latte)
        elif r.lower()=="cappuccino":
            count_coins("cappuccino",cappuccino)
        else:
            print("please repeat")
    print("espresso - 75c\nlatte - 83c\ncappuccino - 1.05c\ntype 'report' to check supplies")
    req=input("What would you like? ")
    get_requrst(req)
    req_stop=input("Anything else? Y/N - ")
    if req_stop.lower()=='n':
        stop=True
