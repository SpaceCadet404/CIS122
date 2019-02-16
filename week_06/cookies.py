# Program:      Lesson 6 Girl Scout Cookies Order Form
# Programmer:   Douglas Rosenfield
# Date:         02/15/2019
# Purpose:      To create an order form using try to validate data in user inputs

#variables
import locale
locale.setlocale( locale.LC_ALL, '')

item_cnt = 0                # count of items ordered
order_total = 0.0           # accumulated total dolars
price = 3.5                 # all cookies are #3.50 per box

# Banner
print("BUY COOKIES. IT IS MANDATORY.")
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
            valid_data = True
        else:
            print ("\nThat was not a valid choice, please try again.")

    valid_data = False      #reset bool flag
    while not valid_data:
        try:
            while not valid_data:
                qty = int(input("enter quantity> "))
                if 1 <= qty <= 10:
                    valid_data = True
                else:
                    print("Please enter a number between 1 and 10")
        except Exception as detail:
            print("quantity error: ", detail)
            print("Are you sure you entered a number?")

    # determine totals
    item_total = qty * price
    fmt_total = locale.currency(item_total, grouping=True)

    # determine cookie name for output display
    if item == "1":
        name = "Savannah"
    elif item == "2":
        name = "Thin Mints"
    else:
        name = "Tag-a-longs"

    print("\n{}  {}  {}  {}".format(name, qty, price, fmt_total))
    print()

    # verify inclusion of this item
    valid_data = False

    while not valid_data:
        incl = input("Would you like to add this to your order? (y/n)> ")
        print()
        if incl.lower() == "y":
            order_total = order_total + item_total #can += item_total work here?
            item_cnt += 1
            valid_data = True
            print("{} was added to your order".format(name))
        elif incl.lower() == "n":
            print ("{} was not added to your order".format(name))
            valid_data = True
        else:
            print("That was not a valid response. Please input either y or n." )

    # add another item?
    cont = input("\nWould you like to add another item? (y/n)> ")

fmt_total = locale.currency(order_total, grouping = True)
print("\nYou ordered {} item(s) for a total price of {}".format(item_cnt,fmt_total))
print("Thank you for your order, {}!".format(user))
