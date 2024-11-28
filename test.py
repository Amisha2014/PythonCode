# num1 = int(input("enter_a_number"))
# num2 = int(input("enter_a_number"))
# if (num1 > num2):
#     print ("Num1", num1)
# elif (num1 < num2):
#     print ("Num2", num2)
# else:
#     print("Same")
#
# string1 = input("enter_a_string")
# string2 = input("enter_a_string")
# if (string1 in string2):
#     print (string1, "is in", string2)

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
menu =[["Dosa", "Idly", "Chappathi", "Parrota", "Idiyappam"] , [10, 5, 10, 5, 5 ]]
print (menu)

menu[1][1] = 15
print (menu)

menu[0].append("Coffee")
menu[1].append(3)
print (menu)
print(menu[1].count(10))