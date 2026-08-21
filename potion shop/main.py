import random

names = ['Mira', 'Evelynn', 'Clark', 'Haedin', 'Yuna']
day1_customers = []
day2_customers = []
day3_customers = []
def customer_name():
    rand_customer_name = random.choice(names) 
    return rand_customer_name
rand_customer_name = customer_name()



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
potions = []
Health_Potion = Potion('HP Potion', 20)
Antidote = Potion('Antidote', 30)
Mana_Potion = Potion('Mana Potion', 50)
potions.append(Health_Potion) 
potions.append(Antidote) 
potions.append(Mana_Potion)
#for potion in potions:
    #print(potion)


class Customer:
    def __init__(self):
        self.name = customer_name()
        self.gp = customer_gp_held()
        self.order = customer_order_details()
    def __str__(self):
        return(
            f"Name: {self.name} \n"
            f"Funds: {self.gp} \n"
            f"Order: {self.order} \n"
        )
    def __repr__(self):
        return(
            f"Name: {self.name} \n"
            f"Funds: {self.gp} \n"
        )
def create_customer():
    all_customers = []
    for _ in range(9):
        rand_customer = Customer()
        all_customers.append(rand_customer)
    return all_customers

customer_gp = [100, 150, 200, 250]
def customer_gp_held():
    rand_customer_gp = random.choice(customer_gp)
    return rand_customer_gp

def customer_order_details():
    customer_desired_potion = random.choice(potions)
    desired_quantity = random.randint(1,3)
    price = desired_quantity * customer_desired_potion.price
    customer_order = [customer_desired_potion, desired_quantity, price]
    return customer_order
    
    
    

all_customers = create_customer()
for customer in all_customers[0:3]:
	day1_customers.append(customer)
for customer in all_customers[3:6]:
	day2_customers.append(customer)
for customer in all_customers[6:9]:
	day3_customers.append(customer)
	
all_days_customers = []
all_days_customers.append(day1_customers)
all_days_customers.append(day2_customers)
all_days_customers.append(day3_customers)

for customer in day1_customers:
	print(
	f"Day 1: {customer.name} wants "

        f"{customer.order[1]} {customer.order[0].name} "

        f"for {customer.order[2]} gp"

    )
    
for customer in day2_customers:
	print(
	f"Day 2: {customer.name} wants "

        f"{customer.order[1]} {customer.order[0].name} "

        f"for {customer.order[2]} gp"

    )
    
for customer in day3_customers:
	print(
	f"Day 3: {customer.name} wants "

        f"{customer.order[1]} {customer.order[0].name} "

        f"for {customer.order[2]} gp"

    )

#day_1_orders()
#day_2_orders()
#day_3_orders()
