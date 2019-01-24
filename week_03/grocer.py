# Program:      Lesson 3
# Programmer:   Douglas Rosenfield
# Date:         01/20/19
# Purpose:      This program is designed to total costs of grocery items for checkout.

# banner
print("Welcome to my grocery app")

# create variables
item_total = 0
order_total = 0

item1_name = input("First item: ")
item1_qty = int(input(item1_name + " quantity: "))
item1_price = int(input(item1_name + " price: "))
item1_total = item1_qty * item1_price
order_total = (order_total + item1_total)

item2_name = input("Next item: ")
item2_qty = int(input(item2_name + " quantity: "))
item2_price = int(input(item2_name + " price: "))
item2_total = item2_qty * item2_price
order_total = (order_total + item2_total)

item3_name = input("Next item: ")
item3_qty = int(input(item3_name + " quantity: "))
item3_price = int(input(item3_name + " price: "))
item3_total = item3_qty * item3_price
order_total = (order_total + item3_total)

#output

print("Order for Douglas")
print("Item Name     Price     Qty     Total")
print("1. " + item1_name + "  " + str(item1_price) + "  " + str(item1_qty) + "  " + str(item1_total)) 
print("2. " + item2_name + "  " + str(item2_price) + "  " + str(item2_qty) + "  " + str(item2_total)) 
print("3. " + item3_name + "  " + str(item3_price) + "  " + str(item3_qty) + "  " + str(item3_total))

print("Order total: " + str(order_total))
