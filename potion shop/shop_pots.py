
import random

potions = []

class Potion:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
            return(
            	  f"{self.name} \n"
                f"Price: {self.price} \n"
            )
    def __repr__(self):
            return(
                f"Name: {self.name} \n"
                f"Price: {self.price} \n"
            )

Health_Potion = Potion('HP Potion', 20)
Antidote = Potion('Antidote', 30)
Mana_Potion = Potion('Mana Potion', 50)
potions.append(Health_Potion) 
potions.append(Antidote) 
potions.append(Mana_Potion)


class Shop:
    def __init__(self, name, stock):
        self.name = name
        self.potions = potions
        self.profit = 0
        self.stock = stock
    def __str__(self):
        return(
            f"Name: {self.name} \n"
            f"Potions: {self.potions} \n"
            f"Profit: {self.profit} \n"
            f"Stock: {self.stock} \n"
        )
class Potion_Stock:
    def __init__(self, potion,):
        self.potion = potion
        self.quantity = stock_quantity()
    def __str__(self):
        return(
            f"Potion: {self.potion} \n"
            f"Quantity: {self.quantity} \n"
        )
def stock_quantity():
    stock_quantity = random.randint(1,5)
    return stock_quantity
HP_pot_stock = Potion_Stock(Health_Potion)
Antidote_stock = Potion_Stock(Antidote)
Mana_pot_stock = Potion_Stock(Mana_Potion)
print(f"HP Potion stock: {HP_pot_stock.quantity}")
print(f"Antidote stock: {Antidote_stock.quantity}")
print(f"Mana Potion stock: {Mana_pot_stock.quantity}")  
    

                         
Potion_Shop = Shop('Potion Shop', [HP_pot_stock, Antidote_stock, Mana_pot_stock])



day1_profit = 0
day2_profit = 0
day3_profit = 0
total_profit = 0    
