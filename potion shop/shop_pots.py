import random

potion_names = [
 'Healing', 'Antidote', 'Mana', 'Invisibility', 'Strength', 'Speed', 'Luck',
 'Fire Resistance', 'Water Breathing', 'Night Vision', 'Feather Fall',
 'Regeneration', 'Poison', 'Weakness', 'Slowness', 'Harming', 'Leaping',
 'Swiftness', 'Turtle Master'
]


def random_potion_name():
	return random.sample(potion_names, 5)


sampled_potion_names = random_potion_name()


def random_potion_price():
	return random.choice([25, 50, 75, 150, 100, 200])


def random_potion_quant():
	return random.randint(1, 5)


class Potion:

	def __init__(self, name):
		self.name = name
		self.price = random_potion_price()
		self.quant = random_potion_quant()

	def __str__(self):
		return (f"{self.name}\n"
		        f"Price: {self.price}\n"
		        f"In stock: {self.quant}\n")

	def __repr__(self):
		return (f"Potion(name={self.name!r},"
		        f"price={self.price}, quant={self.quant})")


def make_potions():
	potions = []

	for name in sampled_potion_names:
		potions.append(Potion(name))

	return potions



class Shop:

	def __init__(self, name):
		self.name = name
		self.potions = make_potions()
		self.profit = 0

	def __str__(self):
		return (f"Name: {self.name} \n"
		        f"Potions: {sampled_potion_names}: \n"
		        f"Profit: {self.profit} \n")


potion_shop = Shop("Potion Shop")
def show_potions():
	for potion in potion_shop.potions:
		print(potion)
	
	

		
show_potions()

day1_profit = 0
day2_profit = 0
day3_profit = 0
total_profit = 0
