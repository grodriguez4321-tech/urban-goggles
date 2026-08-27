import random
import customers
import shop_pots
customers.all_days_customers
'''print(customers.all_days_customers)'''
print(f"Welcome to the Potion Shop! We currently have the following potions in stock: \n {shop_pots.Potion_Shop.stock} \n")



'''if int(input("Press 1 to see Day 1 customers: ")) == 1:
    customers.show_day1_customers()
else:
    print("You have chosen not to see Day 1 customers")
if int(input("Press 2 to see Day 2 customers: ")) == 2:
    customers.show_day2_customers()
else:
    print("You have chosen not to see Day 2 customers")
if int(input("Press 3 to see Day 3 customers: ")) == 3:
    customers.show_day3_customers()
else:
    print("You have chosen not to see Day 3 customers")'''
'''day = 1
while True:
    print("End of Day:", day)
    day += 1
    if day > 4:
        break
print("Thanks for shopping at the Potion Shop!")'''