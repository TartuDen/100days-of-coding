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
