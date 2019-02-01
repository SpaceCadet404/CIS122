# Program:      Lesson 4
# Programmer:   Douglas Rosenfield
# Date:         02/01/19
# Purpose:      This program is designed to total costs of grocery items for checkout, now using do while loops to do so.

# banner
print("Welcome to my grocery app")

# create variables
item_total = 0
order_total = 0
cont = input("Would you like to place an order? (y/n)> ")   #sentinel
item_cnt = 0
order_total = 0
receipt = ("\nItem    Price   Qty     Total\n")

while cont.lower() == "y":
    item_name = input("item: ")
    item_qty = int(input(item_name + " quantity: "))
    item_price = int(input(item_name + " price: "))
    item_total = item_qty * item_price
    order_total = (order_total + item_total)
    item_cnt += 1
    receipt = receipt + ("{}. {}  ${}     {}      ${}".format(item_cnt, item_name, item_price, item_qty, item_total)) + "\n"
    print(receipt)
    cont = (input("Would you like to add another item? (y/n)> "))

print("\nOrder for Douglas")
print(receipt)
print("You ordered {} items for a total price of ${}".format(item_cnt, order_total))
print("Thank you for your order!")
