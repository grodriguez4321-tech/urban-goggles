
import random
potion_names = ['Healing', 'Antidote', 'Mana', 'Invisibility', 'Strength', 'Speed', 'Luck', 'Fire Resistance', 'Water Breathing', 'Night Vision', 'Feather Fall', 'Regeneration', 'Poison', 'Weakness', 'Slowness', 'Harming', 'Leaping', 'Swiftness', 'Turtle Master']
def random_potion_name():
    random_potion_name = random.choice(potion_names)
    return random_potion_name
def random_potion_price():
 random_potion_price = random.choice[25, 50, 75, 150, 100, 200]
 return random_potion_price
def random_potion_quant():
    random_potion_quant = random.randint(1,5)
    return random_potion_quant
shop_potions = []
class Potion:
    def __init__(self):
        self.name = random_potion_name()
        self.price = random_potion_price()
        self.quant = random_potion_quant()
        def __str__(self):
            return(
            	f"{self.name} \n"
                f"Price: {self.price} \n"
                f"In stock: {self.quant} \n"
            )
        def __repr__(self):
            return(
                f"Name: {self.name} \n"
                f"Price: {self.price} \n"
                f"In Stock: {self.quant} \n"
            )
def make_potions():
    for _ in range: (5)
    shop_potions = []
    rand_potion = Potion()
    shop_potions.append(rand_potion)
    return shop_potions
print(shop_potions)


class Shop:
    def __init__(self, name):
        self.name = name
        self.potions = shop_potions
        self.profit = 0
    def __str__(self):
        return(
            f"Name: {self.name} \n"
            f"Potions: {self.potions} \n"
            f"Profit: {self.profit} \n"
        )

def stock_quantity():
    stock_quantity = random.randint(1,5)
    return stock_quantity

     
'''print(f"HP Potion stock: {HP_pot_stock.quantity}")
print(f"Antidote stock: {Antidote_stock.quantity}")
print(f"Mana Potion stock: {Mana_pot_stock.quantity}")  '''


     
     
Potion_Shop = Shop('Potion Shop')



day1_profit = 0
day2_profit = 0
day3_profit = 0
total_profit = 0    
