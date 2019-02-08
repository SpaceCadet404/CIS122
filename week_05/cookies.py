# Program:      Lesson 5 Girl Scout Cookies Order Form
# Programmer:   Douglas Rosenfield
# Date:         02/04/2019
# Purpose:      To create an order form demonstrating use of "IF" statements

#variables
import locale
locale.setlocale( locale.LC_ALL, '')

item_cnt = 0                # count of items ordered
order_total = 0.0           # accumulated total dolars
price = 3.5                 # all cookies are #3.50 per box

# Banner
print("Thank you for placing your order")
user = input("Please enter your name> ")

# Validate data entry
cont = "" # set cont to neither "y" nor "n"
while cont.lower() != "y" and cont.lower() != "n":
    cont = input("Would you like to place an order? (y/n) > ")

while cont.lower() == "y":
    print()
    valid_data = False #bool flag

    #input and data validation

    while not valid_data:
        # display cookie list
        print("Please choose one of our flavors. Enter the item number to choose.")
        print("num\tflavor")
        print("1. \tSavannahs")
        print("2. \tThin Mints")
        print("3. \tTag-A-Longs")
        print()
        item = input("enter item number> ")

        if item == "1" or item == "2" or item == "3":
            valid_data = true
        else:
            print ("\nThat was not a valid choice, please try again.")

    
