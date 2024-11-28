## Create a menu with product and price list  Hint: Use list within a list
# Dosa        10
# Idly         5
# Chapathi    10
# Parotta      5
# Idiyappam    5
# 1. Print the list
# 2. Change the price of idly to 15
# 3. Add a new item to the list Coffee  3
# 4. Count how many products are of a same price
menu = [["Dosa", "Idly", "Chapathi", "Parotta", "Idiyappam"], [10, 5, 10, 5, 5]]
print (menu)
menu [1][1]=15
print (menu)
menu[0].append("Coffee")
print (menu)
menu[1].append (3)
print (menu)
print(menu[1].count(10))
print(menu[1].count(5))
print(menu[1].count(3))